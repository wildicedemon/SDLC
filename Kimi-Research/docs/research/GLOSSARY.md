# SDLC Research Glossary

## A

**Abstract Syntax Tree (AST)**: A tree representation of the abstract syntactic structure of source code.

**Adversarial Reasoning**: A multi-agent approach where agents critique each other's outputs to improve quality.

**Agent Mode**: A distinct operational configuration determining how an AI agent approaches tasks (Code, Ask, Architect, Debug, Orchestrator).

**AI-SBOM**: Software Bill of Materials extended for AI systems, including models, training data, prompts, and agents.

**Anti-Hallucination**: Techniques to detect and mitigate LLM hallucinations in generated content.

**Approval Gateway**: A control point requiring explicit authorization before proceeding with an action.

**AST-Driven Retrieval**: Code search using Abstract Syntax Tree parsing for structural understanding.

## B

**Bayesian Optimization**: Sequential model-based optimization using a probabilistic surrogate model.

**Black-Box Optimization**: Optimizing functions where internal structure is unknown or cannot be differentiated.

**Blue-Green Deployment**: A deployment strategy with two identical environments for zero-downtime releases.

## C

**Canary Deployment**: Gradual rollout to a subset of users before full deployment.

**Chain-of-Thought (CoT)**: Prompting technique that breaks problems into step-by-step reasoning.

**CMA-ES**: Covariance Matrix Adaptation Evolution Strategy, a state-of-the-art evolutionary algorithm.

**Code Property Graph (CPG)**: Unified representation combining AST, CFG, and DFG.

**Complexity Budget**: A constraint limiting total complexity allowed in a system.

**Context Compression**: Techniques to reduce context window usage while preserving information.

**Context Poisoning**: Attacks that manipulate context to influence AI behavior.

**Context Window**: The maximum amount of text an LLM can process in a single request.

**Control Flow Graph (CFG)**: Graph representing all paths through a program.

**Cost-per-Task**: Total cost to complete a task including development, operational, and infrastructure costs.

**Cross-Repo Context**: Managing context across multiple repositories.

## D

**Data Drift**: Changes in data distributions over time affecting model performance.

**Data Flow Graph (DFG)**: Graph showing how data moves through a program.

**DEEVO**: Prompt evolution framework using multi-agent debate with Elo ratings.

**Dependency Graph**: Graph showing dependencies between code entities.

**Distributed Orchestration**: Managing agent clusters across multiple machines.

**Dynamic Model Routing**: Automatically selecting cost-effective models per task.

## E

**Economic Modeling**: Analysis of costs associated with AI agent development and operation.

**Embedding**: Dense vector representation of text for semantic similarity.

**Entropy Tracking**: Monitoring complexity metrics over time to identify refactoring needs.

**Episodic Memory**: Memory of specific events and experiences.

**EvoPrompt**: Evolutionary algorithm framework for prompt optimization.

**Evolutionary Prompt Optimization**: Using evolutionary algorithms to refine prompts.

## F

**Feature Flag**: Mechanism to enable/disable features without deployment.

**Feedback Loop**: Process where output data feeds back as input for improvement.

**FrugalGPT**: Cost optimization approach using LLM cascading.

## G

**GAAPO**: Genetic Algorithmic Applied to Prompt Optimization.

**gVisor**: User-space kernel providing VM-like isolation with container-like performance.

**Graph-of-Thought (GoT)**: Reasoning framework allowing arbitrary connections between thoughts.

**Graph-Based Retrieval**: Code search using graph structures for relationship analysis.

**Gradient-Free Optimization**: Optimization without gradient information.

## H

**Hall-of-Fame**: Pattern keeping best solutions across generations in evolutionary algorithms.

**Hallucination**: LLM generating plausible but incorrect or nonsensical content.

**Hierarchical Tasking**: Decomposing tasks into subtasks with clear dependencies.

**Human-in-the-Loop (HITL)**: Human oversight at key decision points in automated workflows.

**Hybrid Memory**: Combining vector and graph memory approaches.

## I

**Infrastructure-as-Code (IaC)**: Managing infrastructure through machine-readable definition files.

**Intent-Driven Development**: Focus on desired outcomes rather than specifications.

## K

**KISS Principle**: "Keep It Simple, Stupid" - design principle emphasizing simplicity.

**Knowledge Graph**: Graph structure representing entities and their relationships.

## L

**Latency-Intelligence Tradeoff**: Balance between response speed and model capability.

**LLM Cascading**: Using cheaper models first, escalating to expensive ones only when needed.

**Lossless Semantic Tree (LST)**: Enriched tree preserving semantic information beyond syntax.

## M

**MCP (Model Context Protocol)**: Protocol for tool/resource access in AI systems.

**Memory Systems**: Architectures for storing and retrieving information for AI agents.

**Model Context Protocol (MCP)**: Standard for AI agent tool access.

**Model Routing**: Selecting appropriate models for different tasks.

**Modularity**: Degree to which system components can be separated and recombined.

**Multi-Agent Orchestration**: Coordinating multiple AI agents working together.

**Multi-Pass Enrichment**: Progressive refinement through multiple processing stages.

**Mutation Testing**: Testing technique evaluating test suite quality by introducing bugs.

## O

**Observability**: Ability to understand system internal state by examining outputs.

**Orchestrator Mode**: Agent mode for coordinating multiple agents and tasks.

## P

**PageRank**: Algorithm for ranking nodes in a graph based on importance.

**Persistent Memory**: Long-term storage for agent knowledge.

**Policy Enforcement**: Automated mechanisms ensuring compliance with policies.

**PPO (Proximal Policy Optimization)**: RL algorithm for stable training.

**Prompt Breeder**: Self-referential prompt evolution framework.

**Prompt Evolution**: Automated refinement of prompts through optimization.

**Prompt Injection**: Attack manipulating prompts to alter AI behavior.

**Progressive Disclosure**: Architecture revealing information in stages.

## R

**RAG (Retrieval-Augmented Generation)**: Combining retrieval with generation for grounded responses.

**RCOTE Framework**: Request-Confirm-Options-Trust-Escalate for HITL.

**Reasoning Architecture**: Frameworks for structured AI reasoning.

**Refactoring**: Restructuring code without changing external behavior.

**Reinforcement Learning from AI Feedback (RLAIF)**: Training with AI-generated feedback.

**Relationship Chain**: Sequence of connected code elements.

**Repo Grokking**: Deep understanding of codebase structure and relationships.

**Risk-Based Approval**: Different approval levels based on risk assessment.

## S

**Sandboxing**: Isolated execution environments for security.

**SBOM (Software Bill of Materials)**: Comprehensive inventory of software components.

**Scope Creep**: Uncontrolled growth of project scope.

**Self-Healing**: Automatic detection and recovery from failures.

**Semantic Commits**: Convention for commit messages with type, scope, description.

**Semantic Evaluation**: Assessing AI output quality based on meaning.

**Semantic Pruning**: Removing semantically identical thoughts before expansion.

**Short-Term Memory**: Temporary working memory for immediate tasks.

**Skill**: Portable capability bundle encapsulating procedural knowledge.

**Spec-Driven Development**: Development based on detailed specifications.

**SPDX**: Software Package Data Exchange standard for SBOMs.

**Symbolic Memory**: Memory using symbolic representations.

## T

**Task Decomposition**: Breaking complex tasks into manageable subtasks.

**Task Graph**: Graph representing task dependencies and execution order.

**Telemetry**: Automated collection and transmission of monitoring data.

**Temperature**: Parameter controlling randomness in LLM outputs.

**Token Efficiency**: Ratio of useful output to tokens consumed.

**Tree-of-Thought (ToT)**: Reasoning framework organizing thoughts into tree structure.

**Tree-Sitter**: Parser generator for building ASTs.

## V

**Vector Database**: Database optimized for storing and querying vector embeddings.

**Vector Memory**: Memory using dense vector representations.

**Verifiable Tool Feedback**: Objective feedback from compilers, linters, test runners.

## W

**Workflow**: Structured multi-step execution pattern for agents.

**Work Tree**: Isolated working directory for parallel development.

---

*This glossary covers key terms from the SDLC research repository. For detailed explanations, see individual topic documents.*

# SDLC Research Glossary

## A

**Abstract Syntax Tree (AST)**: A tree representation of the abstract syntactic structure of source code.

**Adversarial Reasoning**: A multi-agent approach where agents critique each other's outputs to improve quality.

**Agent Mode**: A distinct operational configuration determining how an AI agent approaches tasks (Code, Ask, Architect, Debug, Orchestrator).

**AI-SBOM**: Software Bill of Materials extended for AI systems, including models, training data, prompts, and agents.

**Anti-Hallucination**: Techniques to detect and mitigate LLM hallucinations in generated content.

**Approval Gateway**: A control point requiring explicit authorization before proceeding with an action.

**AST-Driven Retrieval**: Code search using Abstract Syntax Tree parsing for structural understanding.

## B

**Bayesian Optimization**: Sequential model-based optimization using a probabilistic surrogate model.

**Black-Box Optimization**: Optimizing functions where internal structure is unknown or cannot be differentiated.

**Blue-Green Deployment**: A deployment strategy with two identical environments for zero-downtime releases.

## C

**Canary Deployment**: Gradual rollout to a subset of users before full deployment.

**Chain-of-Thought (CoT)**: Prompting technique that breaks problems into step-by-step reasoning.

**CMA-ES**: Covariance Matrix Adaptation Evolution Strategy, a state-of-the-art evolutionary algorithm.

**Code Property Graph (CPG)**: Unified representation combining AST, CFG, and DFG.

**Complexity Budget**: A constraint limiting total complexity allowed in a system.

**Context Compression**: Techniques to reduce context window usage while preserving information.

**Context Poisoning**: Attacks that manipulate context to influence AI behavior.

**Context Window**: The maximum amount of text an LLM can process in a single request.

**Control Flow Graph (CFG)**: Graph representing all paths through a program.

**Cost-per-Task**: Total cost to complete a task including development, operational, and infrastructure costs.

**Cross-Repo Context**: Managing context across multiple repositories.

## D

**Data Drift**: Changes in data distributions over time affecting model performance.

**Data Flow Graph (DFG)**: Graph showing how data moves through a program.

**DEEVO**: Prompt evolution framework using multi-agent debate with Elo ratings.

**Dependency Graph**: Graph showing dependencies between code entities.

**Distributed Orchestration**: Managing agent clusters across multiple machines.

**Dynamic Model Routing**: Automatically selecting cost-effective models per task.

## E

**Economic Modeling**: Analysis of costs associated with AI agent development and operation.

**Embedding**: Dense vector representation of text for semantic similarity.

**Entropy Tracking**: Monitoring complexity metrics over time to identify refactoring needs.

**Episodic Memory**: Memory of specific events and experiences.

**EvoPrompt**: Evolutionary algorithm framework for prompt optimization.

**Evolutionary Prompt Optimization**: Using evolutionary algorithms to refine prompts.

## F

**Feature Flag**: Mechanism to enable/disable features without deployment.

**Feedback Loop**: Process where output data feeds back as input for improvement.

**FrugalGPT**: Cost optimization approach using LLM cascading.

## G

**GAAPO**: Genetic Algorithmic Applied to Prompt Optimization.

**gVisor**: User-space kernel providing VM-like isolation with container-like performance.

**Graph-of-Thought (GoT)**: Reasoning framework allowing arbitrary connections between thoughts.

**Graph-Based Retrieval**: Code search using graph structures for relationship analysis.

**Gradient-Free Optimization**: Optimization without gradient information.

## H

**Hall-of-Fame**: Pattern keeping best solutions across generations in evolutionary algorithms.

**Hallucination**: LLM generating plausible but incorrect or nonsensical content.

**Hierarchical Tasking**: Decomposing tasks into subtasks with clear dependencies.

**Human-in-the-Loop (HITL)**: Human oversight at key decision points in automated workflows.

**Hybrid Memory**: Combining vector and graph memory approaches.

## I

**Infrastructure-as-Code (IaC)**: Managing infrastructure through machine-readable definition files.

**Intent-Driven Development**: Focus on desired outcomes rather than specifications.

## K

**KISS Principle**: "Keep It Simple, Stupid" - design principle emphasizing simplicity.

**Knowledge Graph**: Graph structure representing entities and their relationships.

## L

**Latency-Intelligence Tradeoff**: Balance between response speed and model capability.

**LLM Cascading**: Using cheaper models first, escalating to expensive ones only when needed.

**Lossless Semantic Tree (LST)**: Enriched tree preserving semantic information beyond syntax.

## M

**MCP (Model Context Protocol)**: Protocol for tool/resource access in AI systems.

**Memory Systems**: Architectures for storing and retrieving information for AI agents.

**Model Context Protocol (MCP)**: Standard for AI agent tool access.

**Model Routing**: Selecting appropriate models for different tasks.

**Modularity**: Degree to which system components can be separated and recombined.

**Multi-Agent Orchestration**: Coordinating multiple AI agents working together.

**Multi-Pass Enrichment**: Progressive refinement through multiple processing stages.

**Mutation Testing**: Testing technique evaluating test suite quality by introducing bugs.

## O

**Observability**: Ability to understand system internal state by examining outputs.

**Orchestrator Mode**: Agent mode for coordinating multiple agents and tasks.

## P

**PageRank**: Algorithm for ranking nodes in a graph based on importance.

**Persistent Memory**: Long-term storage for agent knowledge.

**Policy Enforcement**: Automated mechanisms ensuring compliance with policies.

**PPO (Proximal Policy Optimization)**: RL algorithm for stable training.

**Prompt Breeder**: Self-referential prompt evolution framework.

**Prompt Evolution**: Automated refinement of prompts through optimization.

**Prompt Injection**: Attack manipulating prompts to alter AI behavior.

**Progressive Disclosure**: Architecture revealing information in stages.

## R

**RAG (Retrieval-Augmented Generation)**: Combining retrieval with generation for grounded responses.

**RCOTE Framework**: Request-Confirm-Options-Trust-Escalate for HITL.

**Reasoning Architecture**: Frameworks for structured AI reasoning.

**Refactoring**: Restructuring code without changing external behavior.

**Reinforcement Learning from AI Feedback (RLAIF)**: Training with AI-generated feedback.

**Relationship Chain**: Sequence of connected code elements.

**Repo Grokking**: Deep understanding of codebase structure and relationships.

**Risk-Based Approval**: Different approval levels based on risk assessment.

## S

**Sandboxing**: Isolated execution environments for security.

**SBOM (Software Bill of Materials)**: Comprehensive inventory of software components.

**Scope Creep**: Uncontrolled growth of project scope.

**Self-Healing**: Automatic detection and recovery from failures.

**Semantic Commits**: Convention for commit messages with type, scope, description.

**Semantic Evaluation**: Assessing AI output quality based on meaning.

**Semantic Pruning**: Removing semantically identical thoughts before expansion.

**Short-Term Memory**: Temporary working memory for immediate tasks.

**Skill**: Portable capability bundle encapsulating procedural knowledge.

**Spec-Driven Development**: Development based on detailed specifications.

**SPDX**: Software Package Data Exchange standard for SBOMs.

**Symbolic Memory**: Memory using symbolic representations.

## T

**Task Decomposition**: Breaking complex tasks into manageable subtasks.

**Task Graph**: Graph representing task dependencies and execution order.

**Telemetry**: Automated collection and transmission of monitoring data.

**Temperature**: Parameter controlling randomness in LLM outputs.

**Token Efficiency**: Ratio of useful output to tokens consumed.

**Tree-of-Thought (ToT)**: Reasoning framework organizing thoughts into tree structure.

**Tree-Sitter**: Parser generator for building ASTs.

## V

**Vector Database**: Database optimized for storing and querying vector embeddings.

**Vector Memory**: Memory using dense vector representations.

**Verifiable Tool Feedback**: Objective feedback from compilers, linters, test runners.

## W

**Workflow**: Structured multi-step execution pattern for agents.

**Work Tree**: Isolated working directory for parallel development.

---

*This glossary covers key terms from the SDLC research repository. For detailed explanations, see individual topic documents.*

# SDLC Research Glossary

## A

**Abstract Syntax Tree (AST)**: A tree representation of the abstract syntactic structure of source code.

**Adversarial Reasoning**: A multi-agent approach where agents critique each other's outputs to improve quality.

**Agent Mode**: A distinct operational configuration determining how an AI agent approaches tasks (Code, Ask, Architect, Debug, Orchestrator).

**AI-SBOM**: Software Bill of Materials extended for AI systems, including models, training data, prompts, and agents.

**Anti-Hallucination**: Techniques to detect and mitigate LLM hallucinations in generated content.

**Approval Gateway**: A control point requiring explicit authorization before proceeding with an action.

**AST-Driven Retrieval**: Code search using Abstract Syntax Tree parsing for structural understanding.

## B

**Bayesian Optimization**: Sequential model-based optimization using a probabilistic surrogate model.

**Black-Box Optimization**: Optimizing functions where internal structure is unknown or cannot be differentiated.

**Blue-Green Deployment**: A deployment strategy with two identical environments for zero-downtime releases.

## C

**Canary Deployment**: Gradual rollout to a subset of users before full deployment.

**Chain-of-Thought (CoT)**: Prompting technique that breaks problems into step-by-step reasoning.

**CMA-ES**: Covariance Matrix Adaptation Evolution Strategy, a state-of-the-art evolutionary algorithm.

**Code Property Graph (CPG)**: Unified representation combining AST, CFG, and DFG.

**Complexity Budget**: A constraint limiting total complexity allowed in a system.

**Context Compression**: Techniques to reduce context window usage while preserving information.

**Context Poisoning**: Attacks that manipulate context to influence AI behavior.

**Context Window**: The maximum amount of text an LLM can process in a single request.

**Control Flow Graph (CFG)**: Graph representing all paths through a program.

**Cost-per-Task**: Total cost to complete a task including development, operational, and infrastructure costs.

**Cross-Repo Context**: Managing context across multiple repositories.

## D

**Data Drift**: Changes in data distributions over time affecting model performance.

**Data Flow Graph (DFG)**: Graph showing how data moves through a program.

**DEEVO**: Prompt evolution framework using multi-agent debate with Elo ratings.

**Dependency Graph**: Graph showing dependencies between code entities.

**Distributed Orchestration**: Managing agent clusters across multiple machines.

**Dynamic Model Routing**: Automatically selecting cost-effective models per task.

## E

**Economic Modeling**: Analysis of costs associated with AI agent development and operation.

**Embedding**: Dense vector representation of text for semantic similarity.

**Entropy Tracking**: Monitoring complexity metrics over time to identify refactoring needs.

**Episodic Memory**: Memory of specific events and experiences.

**EvoPrompt**: Evolutionary algorithm framework for prompt optimization.

**Evolutionary Prompt Optimization**: Using evolutionary algorithms to refine prompts.

## F

**Feature Flag**: Mechanism to enable/disable features without deployment.

**Feedback Loop**: Process where output data feeds back as input for improvement.

**FrugalGPT**: Cost optimization approach using LLM cascading.

## G

**GAAPO**: Genetic Algorithmic Applied to Prompt Optimization.

**gVisor**: User-space kernel providing VM-like isolation with container-like performance.

**Graph-of-Thought (GoT)**: Reasoning framework allowing arbitrary connections between thoughts.

**Graph-Based Retrieval**: Code search using graph structures for relationship analysis.

**Gradient-Free Optimization**: Optimization without gradient information.

## H

**Hall-of-Fame**: Pattern keeping best solutions across generations in evolutionary algorithms.

**Hallucination**: LLM generating plausible but incorrect or nonsensical content.

**Hierarchical Tasking**: Decomposing tasks into subtasks with clear dependencies.

**Human-in-the-Loop (HITL)**: Human oversight at key decision points in automated workflows.

**Hybrid Memory**: Combining vector and graph memory approaches.

## I

**Infrastructure-as-Code (IaC)**: Managing infrastructure through machine-readable definition files.

**Intent-Driven Development**: Focus on desired outcomes rather than specifications.

## K

**KISS Principle**: "Keep It Simple, Stupid" - design principle emphasizing simplicity.

**Knowledge Graph**: Graph structure representing entities and their relationships.

## L

**Latency-Intelligence Tradeoff**: Balance between response speed and model capability.

**LLM Cascading**: Using cheaper models first, escalating to expensive ones only when needed.

**Lossless Semantic Tree (LST)**: Enriched tree preserving semantic information beyond syntax.

## M

**MCP (Model Context Protocol)**: Protocol for tool/resource access in AI systems.

**Memory Systems**: Architectures for storing and retrieving information for AI agents.

**Model Context Protocol (MCP)**: Standard for AI agent tool access.

**Model Routing**: Selecting appropriate models for different tasks.

**Modularity**: Degree to which system components can be separated and recombined.

**Multi-Agent Orchestration**: Coordinating multiple AI agents working together.

**Multi-Pass Enrichment**: Progressive refinement through multiple processing stages.

**Mutation Testing**: Testing technique evaluating test suite quality by introducing bugs.

## O

**Observability**: Ability to understand system internal state by examining outputs.

**Orchestrator Mode**: Agent mode for coordinating multiple agents and tasks.

## P

**PageRank**: Algorithm for ranking nodes in a graph based on importance.

**Persistent Memory**: Long-term storage for agent knowledge.

**Policy Enforcement**: Automated mechanisms ensuring compliance with policies.

**PPO (Proximal Policy Optimization)**: RL algorithm for stable training.

**Prompt Breeder**: Self-referential prompt evolution framework.

**Prompt Evolution**: Automated refinement of prompts through optimization.

**Prompt Injection**: Attack manipulating prompts to alter AI behavior.

**Progressive Disclosure**: Architecture revealing information in stages.

## R

**RAG (Retrieval-Augmented Generation)**: Combining retrieval with generation for grounded responses.

**RCOTE Framework**: Request-Confirm-Options-Trust-Escalate for HITL.

**Reasoning Architecture**: Frameworks for structured AI reasoning.

**Refactoring**: Restructuring code without changing external behavior.

**Reinforcement Learning from AI Feedback (RLAIF)**: Training with AI-generated feedback.

**Relationship Chain**: Sequence of connected code elements.

**Repo Grokking**: Deep understanding of codebase structure and relationships.

**Risk-Based Approval**: Different approval levels based on risk assessment.

## S

**Sandboxing**: Isolated execution environments for security.

**SBOM (Software Bill of Materials)**: Comprehensive inventory of software components.

**Scope Creep**: Uncontrolled growth of project scope.

**Self-Healing**: Automatic detection and recovery from failures.

**Semantic Commits**: Convention for commit messages with type, scope, description.

**Semantic Evaluation**: Assessing AI output quality based on meaning.

**Semantic Pruning**: Removing semantically identical thoughts before expansion.

**Short-Term Memory**: Temporary working memory for immediate tasks.

**Skill**: Portable capability bundle encapsulating procedural knowledge.

**Spec-Driven Development**: Development based on detailed specifications.

**SPDX**: Software Package Data Exchange standard for SBOMs.

**Symbolic Memory**: Memory using symbolic representations.

## T

**Task Decomposition**: Breaking complex tasks into manageable subtasks.

**Task Graph**: Graph representing task dependencies and execution order.

**Telemetry**: Automated collection and transmission of monitoring data.

**Temperature**: Parameter controlling randomness in LLM outputs.

**Token Efficiency**: Ratio of useful output to tokens consumed.

**Tree-of-Thought (ToT)**: Reasoning framework organizing thoughts into tree structure.

**Tree-Sitter**: Parser generator for building ASTs.

## V

**Vector Database**: Database optimized for storing and querying vector embeddings.

**Vector Memory**: Memory using dense vector representations.

**Verifiable Tool Feedback**: Objective feedback from compilers, linters, test runners.

## W

**Workflow**: Structured multi-step execution pattern for agents.

**Work Tree**: Isolated working directory for parallel development.

---

*This glossary covers key terms from the SDLC research repository. For detailed explanations, see individual topic documents.*

# SDLC Research Glossary

## A

**Abstract Syntax Tree (AST)**: A tree representation of the abstract syntactic structure of source code.

**Adversarial Reasoning**: A multi-agent approach where agents critique each other's outputs to improve quality.

**Agent Mode**: A distinct operational configuration determining how an AI agent approaches tasks (Code, Ask, Architect, Debug, Orchestrator).

**AI-SBOM**: Software Bill of Materials extended for AI systems, including models, training data, prompts, and agents.

**Anti-Hallucination**: Techniques to detect and mitigate LLM hallucinations in generated content.

**Approval Gateway**: A control point requiring explicit authorization before proceeding with an action.

**AST-Driven Retrieval**: Code search using Abstract Syntax Tree parsing for structural understanding.

## B

**Bayesian Optimization**: Sequential model-based optimization using a probabilistic surrogate model.

**Black-Box Optimization**: Optimizing functions where internal structure is unknown or cannot be differentiated.

**Blue-Green Deployment**: A deployment strategy with two identical environments for zero-downtime releases.

## C

**Canary Deployment**: Gradual rollout to a subset of users before full deployment.

**Chain-of-Thought (CoT)**: Prompting technique that breaks problems into step-by-step reasoning.

**CMA-ES**: Covariance Matrix Adaptation Evolution Strategy, a state-of-the-art evolutionary algorithm.

**Code Property Graph (CPG)**: Unified representation combining AST, CFG, and DFG.

**Complexity Budget**: A constraint limiting total complexity allowed in a system.

**Context Compression**: Techniques to reduce context window usage while preserving information.

**Context Poisoning**: Attacks that manipulate context to influence AI behavior.

**Context Window**: The maximum amount of text an LLM can process in a single request.

**Control Flow Graph (CFG)**: Graph representing all paths through a program.

**Cost-per-Task**: Total cost to complete a task including development, operational, and infrastructure costs.

**Cross-Repo Context**: Managing context across multiple repositories.

## D

**Data Drift**: Changes in data distributions over time affecting model performance.

**Data Flow Graph (DFG)**: Graph showing how data moves through a program.

**DEEVO**: Prompt evolution framework using multi-agent debate with Elo ratings.

**Dependency Graph**: Graph showing dependencies between code entities.

**Distributed Orchestration**: Managing agent clusters across multiple machines.

**Dynamic Model Routing**: Automatically selecting cost-effective models per task.

## E

**Economic Modeling**: Analysis of costs associated with AI agent development and operation.

**Embedding**: Dense vector representation of text for semantic similarity.

**Entropy Tracking**: Monitoring complexity metrics over time to identify refactoring needs.

**Episodic Memory**: Memory of specific events and experiences.

**EvoPrompt**: Evolutionary algorithm framework for prompt optimization.

**Evolutionary Prompt Optimization**: Using evolutionary algorithms to refine prompts.

## F

**Feature Flag**: Mechanism to enable/disable features without deployment.

**Feedback Loop**: Process where output data feeds back as input for improvement.

**FrugalGPT**: Cost optimization approach using LLM cascading.

## G

**GAAPO**: Genetic Algorithmic Applied to Prompt Optimization.

**gVisor**: User-space kernel providing VM-like isolation with container-like performance.

**Graph-of-Thought (GoT)**: Reasoning framework allowing arbitrary connections between thoughts.

**Graph-Based Retrieval**: Code search using graph structures for relationship analysis.

**Gradient-Free Optimization**: Optimization without gradient information.

## H

**Hall-of-Fame**: Pattern keeping best solutions across generations in evolutionary algorithms.

**Hallucination**: LLM generating plausible but incorrect or nonsensical content.

**Hierarchical Tasking**: Decomposing tasks into subtasks with clear dependencies.

**Human-in-the-Loop (HITL)**: Human oversight at key decision points in automated workflows.

**Hybrid Memory**: Combining vector and graph memory approaches.

## I

**Infrastructure-as-Code (IaC)**: Managing infrastructure through machine-readable definition files.

**Intent-Driven Development**: Focus on desired outcomes rather than specifications.

## K

**KISS Principle**: "Keep It Simple, Stupid" - design principle emphasizing simplicity.

**Knowledge Graph**: Graph structure representing entities and their relationships.

## L

**Latency-Intelligence Tradeoff**: Balance between response speed and model capability.

**LLM Cascading**: Using cheaper models first, escalating to expensive ones only when needed.

**Lossless Semantic Tree (LST)**: Enriched tree preserving semantic information beyond syntax.

## M

**MCP (Model Context Protocol)**: Protocol for tool/resource access in AI systems.

**Memory Systems**: Architectures for storing and retrieving information for AI agents.

**Model Context Protocol (MCP)**: Standard for AI agent tool access.

**Model Routing**: Selecting appropriate models for different tasks.

**Modularity**: Degree to which system components can be separated and recombined.

**Multi-Agent Orchestration**: Coordinating multiple AI agents working together.

**Multi-Pass Enrichment**: Progressive refinement through multiple processing stages.

**Mutation Testing**: Testing technique evaluating test suite quality by introducing bugs.

## O

**Observability**: Ability to understand system internal state by examining outputs.

**Orchestrator Mode**: Agent mode for coordinating multiple agents and tasks.

## P

**PageRank**: Algorithm for ranking nodes in a graph based on importance.

**Persistent Memory**: Long-term storage for agent knowledge.

**Policy Enforcement**: Automated mechanisms ensuring compliance with policies.

**PPO (Proximal Policy Optimization)**: RL algorithm for stable training.

**Prompt Breeder**: Self-referential prompt evolution framework.

**Prompt Evolution**: Automated refinement of prompts through optimization.

**Prompt Injection**: Attack manipulating prompts to alter AI behavior.

**Progressive Disclosure**: Architecture revealing information in stages.

## R

**RAG (Retrieval-Augmented Generation)**: Combining retrieval with generation for grounded responses.

**RCOTE Framework**: Request-Confirm-Options-Trust-Escalate for HITL.

**Reasoning Architecture**: Frameworks for structured AI reasoning.

**Refactoring**: Restructuring code without changing external behavior.

**Reinforcement Learning from AI Feedback (RLAIF)**: Training with AI-generated feedback.

**Relationship Chain**: Sequence of connected code elements.

**Repo Grokking**: Deep understanding of codebase structure and relationships.

**Risk-Based Approval**: Different approval levels based on risk assessment.

## S

**Sandboxing**: Isolated execution environments for security.

**SBOM (Software Bill of Materials)**: Comprehensive inventory of software components.

**Scope Creep**: Uncontrolled growth of project scope.

**Self-Healing**: Automatic detection and recovery from failures.

**Semantic Commits**: Convention for commit messages with type, scope, description.

**Semantic Evaluation**: Assessing AI output quality based on meaning.

**Semantic Pruning**: Removing semantically identical thoughts before expansion.

**Short-Term Memory**: Temporary working memory for immediate tasks.

**Skill**: Portable capability bundle encapsulating procedural knowledge.

**Spec-Driven Development**: Development based on detailed specifications.

**SPDX**: Software Package Data Exchange standard for SBOMs.

**Symbolic Memory**: Memory using symbolic representations.

## T

**Task Decomposition**: Breaking complex tasks into manageable subtasks.

**Task Graph**: Graph representing task dependencies and execution order.

**Telemetry**: Automated collection and transmission of monitoring data.

**Temperature**: Parameter controlling randomness in LLM outputs.

**Token Efficiency**: Ratio of useful output to tokens consumed.

**Tree-of-Thought (ToT)**: Reasoning framework organizing thoughts into tree structure.

**Tree-Sitter**: Parser generator for building ASTs.

## V

**Vector Database**: Database optimized for storing and querying vector embeddings.

**Vector Memory**: Memory using dense vector representations.

**Verifiable Tool Feedback**: Objective feedback from compilers, linters, test runners.

## W

**Workflow**: Structured multi-step execution pattern for agents.

**Work Tree**: Isolated working directory for parallel development.

---

*This glossary covers key terms from the SDLC research repository. For detailed explanations, see individual topic documents.*

# SDLC Research Glossary

## A

**Abstract Syntax Tree (AST)**: A tree representation of the abstract syntactic structure of source code.

**Adversarial Reasoning**: A multi-agent approach where agents critique each other's outputs to improve quality.

**Agent Mode**: A distinct operational configuration determining how an AI agent approaches tasks (Code, Ask, Architect, Debug, Orchestrator).

**AI-SBOM**: Software Bill of Materials extended for AI systems, including models, training data, prompts, and agents.

**Anti-Hallucination**: Techniques to detect and mitigate LLM hallucinations in generated content.

**Approval Gateway**: A control point requiring explicit authorization before proceeding with an action.

**AST-Driven Retrieval**: Code search using Abstract Syntax Tree parsing for structural understanding.

## B

**Bayesian Optimization**: Sequential model-based optimization using a probabilistic surrogate model.

**Black-Box Optimization**: Optimizing functions where internal structure is unknown or cannot be differentiated.

**Blue-Green Deployment**: A deployment strategy with two identical environments for zero-downtime releases.

## C

**Canary Deployment**: Gradual rollout to a subset of users before full deployment.

**Chain-of-Thought (CoT)**: Prompting technique that breaks problems into step-by-step reasoning.

**CMA-ES**: Covariance Matrix Adaptation Evolution Strategy, a state-of-the-art evolutionary algorithm.

**Code Property Graph (CPG)**: Unified representation combining AST, CFG, and DFG.

**Complexity Budget**: A constraint limiting total complexity allowed in a system.

**Context Compression**: Techniques to reduce context window usage while preserving information.

**Context Poisoning**: Attacks that manipulate context to influence AI behavior.

**Context Window**: The maximum amount of text an LLM can process in a single request.

**Control Flow Graph (CFG)**: Graph representing all paths through a program.

**Cost-per-Task**: Total cost to complete a task including development, operational, and infrastructure costs.

**Cross-Repo Context**: Managing context across multiple repositories.

## D

**Data Drift**: Changes in data distributions over time affecting model performance.

**Data Flow Graph (DFG)**: Graph showing how data moves through a program.

**DEEVO**: Prompt evolution framework using multi-agent debate with Elo ratings.

**Dependency Graph**: Graph showing dependencies between code entities.

**Distributed Orchestration**: Managing agent clusters across multiple machines.

**Dynamic Model Routing**: Automatically selecting cost-effective models per task.

## E

**Economic Modeling**: Analysis of costs associated with AI agent development and operation.

**Embedding**: Dense vector representation of text for semantic similarity.

**Entropy Tracking**: Monitoring complexity metrics over time to identify refactoring needs.

**Episodic Memory**: Memory of specific events and experiences.

**EvoPrompt**: Evolutionary algorithm framework for prompt optimization.

**Evolutionary Prompt Optimization**: Using evolutionary algorithms to refine prompts.

## F

**Feature Flag**: Mechanism to enable/disable features without deployment.

**Feedback Loop**: Process where output data feeds back as input for improvement.

**FrugalGPT**: Cost optimization approach using LLM cascading.

## G

**GAAPO**: Genetic Algorithmic Applied to Prompt Optimization.

**gVisor**: User-space kernel providing VM-like isolation with container-like performance.

**Graph-of-Thought (GoT)**: Reasoning framework allowing arbitrary connections between thoughts.

**Graph-Based Retrieval**: Code search using graph structures for relationship analysis.

**Gradient-Free Optimization**: Optimization without gradient information.

## H

**Hall-of-Fame**: Pattern keeping best solutions across generations in evolutionary algorithms.

**Hallucination**: LLM generating plausible but incorrect or nonsensical content.

**Hierarchical Tasking**: Decomposing tasks into subtasks with clear dependencies.

**Human-in-the-Loop (HITL)**: Human oversight at key decision points in automated workflows.

**Hybrid Memory**: Combining vector and graph memory approaches.

## I

**Infrastructure-as-Code (IaC)**: Managing infrastructure through machine-readable definition files.

**Intent-Driven Development**: Focus on desired outcomes rather than specifications.

## K

**KISS Principle**: "Keep It Simple, Stupid" - design principle emphasizing simplicity.

**Knowledge Graph**: Graph structure representing entities and their relationships.

## L

**Latency-Intelligence Tradeoff**: Balance between response speed and model capability.

**LLM Cascading**: Using cheaper models first, escalating to expensive ones only when needed.

**Lossless Semantic Tree (LST)**: Enriched tree preserving semantic information beyond syntax.

## M

**MCP (Model Context Protocol)**: Protocol for tool/resource access in AI systems.

**Memory Systems**: Architectures for storing and retrieving information for AI agents.

**Model Context Protocol (MCP)**: Standard for AI agent tool access.

**Model Routing**: Selecting appropriate models for different tasks.

**Modularity**: Degree to which system components can be separated and recombined.

**Multi-Agent Orchestration**: Coordinating multiple AI agents working together.

**Multi-Pass Enrichment**: Progressive refinement through multiple processing stages.

**Mutation Testing**: Testing technique evaluating test suite quality by introducing bugs.

## O

**Observability**: Ability to understand system internal state by examining outputs.

**Orchestrator Mode**: Agent mode for coordinating multiple agents and tasks.

## P

**PageRank**: Algorithm for ranking nodes in a graph based on importance.

**Persistent Memory**: Long-term storage for agent knowledge.

**Policy Enforcement**: Automated mechanisms ensuring compliance with policies.

**PPO (Proximal Policy Optimization)**: RL algorithm for stable training.

**Prompt Breeder**: Self-referential prompt evolution framework.

**Prompt Evolution**: Automated refinement of prompts through optimization.

**Prompt Injection**: Attack manipulating prompts to alter AI behavior.

**Progressive Disclosure**: Architecture revealing information in stages.

## R

**RAG (Retrieval-Augmented Generation)**: Combining retrieval with generation for grounded responses.

**RCOTE Framework**: Request-Confirm-Options-Trust-Escalate for HITL.

**Reasoning Architecture**: Frameworks for structured AI reasoning.

**Refactoring**: Restructuring code without changing external behavior.

**Reinforcement Learning from AI Feedback (RLAIF)**: Training with AI-generated feedback.

**Relationship Chain**: Sequence of connected code elements.

**Repo Grokking**: Deep understanding of codebase structure and relationships.

**Risk-Based Approval**: Different approval levels based on risk assessment.

## S

**Sandboxing**: Isolated execution environments for security.

**SBOM (Software Bill of Materials)**: Comprehensive inventory of software components.

**Scope Creep**: Uncontrolled growth of project scope.

**Self-Healing**: Automatic detection and recovery from failures.

**Semantic Commits**: Convention for commit messages with type, scope, description.

**Semantic Evaluation**: Assessing AI output quality based on meaning.

**Semantic Pruning**: Removing semantically identical thoughts before expansion.

**Short-Term Memory**: Temporary working memory for immediate tasks.

**Skill**: Portable capability bundle encapsulating procedural knowledge.

**Spec-Driven Development**: Development based on detailed specifications.

**SPDX**: Software Package Data Exchange standard for SBOMs.

**Symbolic Memory**: Memory using symbolic representations.

## T

**Task Decomposition**: Breaking complex tasks into manageable subtasks.

**Task Graph**: Graph representing task dependencies and execution order.

**Telemetry**: Automated collection and transmission of monitoring data.

**Temperature**: Parameter controlling randomness in LLM outputs.

**Token Efficiency**: Ratio of useful output to tokens consumed.

**Tree-of-Thought (ToT)**: Reasoning framework organizing thoughts into tree structure.

**Tree-Sitter**: Parser generator for building ASTs.

## V

**Vector Database**: Database optimized for storing and querying vector embeddings.

**Vector Memory**: Memory using dense vector representations.

**Verifiable Tool Feedback**: Objective feedback from compilers, linters, test runners.

## W

**Workflow**: Structured multi-step execution pattern for agents.

**Work Tree**: Isolated working directory for parallel development.

---

*This glossary covers key terms from the SDLC research repository. For detailed explanations, see individual topic documents.*

# SDLC Research Glossary

## A

**Abstract Syntax Tree (AST)**: A tree representation of the abstract syntactic structure of source code.

**Adversarial Reasoning**: A multi-agent approach where agents critique each other's outputs to improve quality.

**Agent Mode**: A distinct operational configuration determining how an AI agent approaches tasks (Code, Ask, Architect, Debug, Orchestrator).

**AI-SBOM**: Software Bill of Materials extended for AI systems, including models, training data, prompts, and agents.

**Anti-Hallucination**: Techniques to detect and mitigate LLM hallucinations in generated content.

**Approval Gateway**: A control point requiring explicit authorization before proceeding with an action.

**AST-Driven Retrieval**: Code search using Abstract Syntax Tree parsing for structural understanding.

## B

**Bayesian Optimization**: Sequential model-based optimization using a probabilistic surrogate model.

**Black-Box Optimization**: Optimizing functions where internal structure is unknown or cannot be differentiated.

**Blue-Green Deployment**: A deployment strategy with two identical environments for zero-downtime releases.

## C

**Canary Deployment**: Gradual rollout to a subset of users before full deployment.

**Chain-of-Thought (CoT)**: Prompting technique that breaks problems into step-by-step reasoning.

**CMA-ES**: Covariance Matrix Adaptation Evolution Strategy, a state-of-the-art evolutionary algorithm.

**Code Property Graph (CPG)**: Unified representation combining AST, CFG, and DFG.

**Complexity Budget**: A constraint limiting total complexity allowed in a system.

**Context Compression**: Techniques to reduce context window usage while preserving information.

**Context Poisoning**: Attacks that manipulate context to influence AI behavior.

**Context Window**: The maximum amount of text an LLM can process in a single request.

**Control Flow Graph (CFG)**: Graph representing all paths through a program.

**Cost-per-Task**: Total cost to complete a task including development, operational, and infrastructure costs.

**Cross-Repo Context**: Managing context across multiple repositories.

## D

**Data Drift**: Changes in data distributions over time affecting model performance.

**Data Flow Graph (DFG)**: Graph showing how data moves through a program.

**DEEVO**: Prompt evolution framework using multi-agent debate with Elo ratings.

**Dependency Graph**: Graph showing dependencies between code entities.

**Distributed Orchestration**: Managing agent clusters across multiple machines.

**Dynamic Model Routing**: Automatically selecting cost-effective models per task.

## E

**Economic Modeling**: Analysis of costs associated with AI agent development and operation.

**Embedding**: Dense vector representation of text for semantic similarity.

**Entropy Tracking**: Monitoring complexity metrics over time to identify refactoring needs.

**Episodic Memory**: Memory of specific events and experiences.

**EvoPrompt**: Evolutionary algorithm framework for prompt optimization.

**Evolutionary Prompt Optimization**: Using evolutionary algorithms to refine prompts.

## F

**Feature Flag**: Mechanism to enable/disable features without deployment.

**Feedback Loop**: Process where output data feeds back as input for improvement.

**FrugalGPT**: Cost optimization approach using LLM cascading.

## G

**GAAPO**: Genetic Algorithmic Applied to Prompt Optimization.

**gVisor**: User-space kernel providing VM-like isolation with container-like performance.

**Graph-of-Thought (GoT)**: Reasoning framework allowing arbitrary connections between thoughts.

**Graph-Based Retrieval**: Code search using graph structures for relationship analysis.

**Gradient-Free Optimization**: Optimization without gradient information.

## H

**Hall-of-Fame**: Pattern keeping best solutions across generations in evolutionary algorithms.

**Hallucination**: LLM generating plausible but incorrect or nonsensical content.

**Hierarchical Tasking**: Decomposing tasks into subtasks with clear dependencies.

**Human-in-the-Loop (HITL)**: Human oversight at key decision points in automated workflows.

**Hybrid Memory**: Combining vector and graph memory approaches.

## I

**Infrastructure-as-Code (IaC)**: Managing infrastructure through machine-readable definition files.

**Intent-Driven Development**: Focus on desired outcomes rather than specifications.

## K

**KISS Principle**: "Keep It Simple, Stupid" - design principle emphasizing simplicity.

**Knowledge Graph**: Graph structure representing entities and their relationships.

## L

**Latency-Intelligence Tradeoff**: Balance between response speed and model capability.

**LLM Cascading**: Using cheaper models first, escalating to expensive ones only when needed.

**Lossless Semantic Tree (LST)**: Enriched tree preserving semantic information beyond syntax.

## M

**MCP (Model Context Protocol)**: Protocol for tool/resource access in AI systems.

**Memory Systems**: Architectures for storing and retrieving information for AI agents.

**Model Context Protocol (MCP)**: Standard for AI agent tool access.

**Model Routing**: Selecting appropriate models for different tasks.

**Modularity**: Degree to which system components can be separated and recombined.

**Multi-Agent Orchestration**: Coordinating multiple AI agents working together.

**Multi-Pass Enrichment**: Progressive refinement through multiple processing stages.

**Mutation Testing**: Testing technique evaluating test suite quality by introducing bugs.

## O

**Observability**: Ability to understand system internal state by examining outputs.

**Orchestrator Mode**: Agent mode for coordinating multiple agents and tasks.

## P

**PageRank**: Algorithm for ranking nodes in a graph based on importance.

**Persistent Memory**: Long-term storage for agent knowledge.

**Policy Enforcement**: Automated mechanisms ensuring compliance with policies.

**PPO (Proximal Policy Optimization)**: RL algorithm for stable training.

**Prompt Breeder**: Self-referential prompt evolution framework.

**Prompt Evolution**: Automated refinement of prompts through optimization.

**Prompt Injection**: Attack manipulating prompts to alter AI behavior.

**Progressive Disclosure**: Architecture revealing information in stages.

## R

**RAG (Retrieval-Augmented Generation)**: Combining retrieval with generation for grounded responses.

**RCOTE Framework**: Request-Confirm-Options-Trust-Escalate for HITL.

**Reasoning Architecture**: Frameworks for structured AI reasoning.

**Refactoring**: Restructuring code without changing external behavior.

**Reinforcement Learning from AI Feedback (RLAIF)**: Training with AI-generated feedback.

**Relationship Chain**: Sequence of connected code elements.

**Repo Grokking**: Deep understanding of codebase structure and relationships.

**Risk-Based Approval**: Different approval levels based on risk assessment.

## S

**Sandboxing**: Isolated execution environments for security.

**SBOM (Software Bill of Materials)**: Comprehensive inventory of software components.

**Scope Creep**: Uncontrolled growth of project scope.

**Self-Healing**: Automatic detection and recovery from failures.

**Semantic Commits**: Convention for commit messages with type, scope, description.

**Semantic Evaluation**: Assessing AI output quality based on meaning.

**Semantic Pruning**: Removing semantically identical thoughts before expansion.

**Short-Term Memory**: Temporary working memory for immediate tasks.

**Skill**: Portable capability bundle encapsulating procedural knowledge.

**Spec-Driven Development**: Development based on detailed specifications.

**SPDX**: Software Package Data Exchange standard for SBOMs.

**Symbolic Memory**: Memory using symbolic representations.

## T

**Task Decomposition**: Breaking complex tasks into manageable subtasks.

**Task Graph**: Graph representing task dependencies and execution order.

**Telemetry**: Automated collection and transmission of monitoring data.

**Temperature**: Parameter controlling randomness in LLM outputs.

**Token Efficiency**: Ratio of useful output to tokens consumed.

**Tree-of-Thought (ToT)**: Reasoning framework organizing thoughts into tree structure.

**Tree-Sitter**: Parser generator for building ASTs.

## V

**Vector Database**: Database optimized for storing and querying vector embeddings.

**Vector Memory**: Memory using dense vector representations.

**Verifiable Tool Feedback**: Objective feedback from compilers, linters, test runners.

## W

**Workflow**: Structured multi-step execution pattern for agents.

**Work Tree**: Isolated working directory for parallel development.

---

*This glossary covers key terms from the SDLC research repository. For detailed explanations, see individual topic documents.*

# SDLC Research Glossary

## A

**Abstract Syntax Tree (AST)**: A tree representation of the abstract syntactic structure of source code.

**Adversarial Reasoning**: A multi-agent approach where agents critique each other's outputs to improve quality.

**Agent Mode**: A distinct operational configuration determining how an AI agent approaches tasks (Code, Ask, Architect, Debug, Orchestrator).

**AI-SBOM**: Software Bill of Materials extended for AI systems, including models, training data, prompts, and agents.

**Anti-Hallucination**: Techniques to detect and mitigate LLM hallucinations in generated content.

**Approval Gateway**: A control point requiring explicit authorization before proceeding with an action.

**AST-Driven Retrieval**: Code search using Abstract Syntax Tree parsing for structural understanding.

## B

**Bayesian Optimization**: Sequential model-based optimization using a probabilistic surrogate model.

**Black-Box Optimization**: Optimizing functions where internal structure is unknown or cannot be differentiated.

**Blue-Green Deployment**: A deployment strategy with two identical environments for zero-downtime releases.

## C

**Canary Deployment**: Gradual rollout to a subset of users before full deployment.

**Chain-of-Thought (CoT)**: Prompting technique that breaks problems into step-by-step reasoning.

**CMA-ES**: Covariance Matrix Adaptation Evolution Strategy, a state-of-the-art evolutionary algorithm.

**Code Property Graph (CPG)**: Unified representation combining AST, CFG, and DFG.

**Complexity Budget**: A constraint limiting total complexity allowed in a system.

**Context Compression**: Techniques to reduce context window usage while preserving information.

**Context Poisoning**: Attacks that manipulate context to influence AI behavior.

**Context Window**: The maximum amount of text an LLM can process in a single request.

**Control Flow Graph (CFG)**: Graph representing all paths through a program.

**Cost-per-Task**: Total cost to complete a task including development, operational, and infrastructure costs.

**Cross-Repo Context**: Managing context across multiple repositories.

## D

**Data Drift**: Changes in data distributions over time affecting model performance.

**Data Flow Graph (DFG)**: Graph showing how data moves through a program.

**DEEVO**: Prompt evolution framework using multi-agent debate with Elo ratings.

**Dependency Graph**: Graph showing dependencies between code entities.

**Distributed Orchestration**: Managing agent clusters across multiple machines.

**Dynamic Model Routing**: Automatically selecting cost-effective models per task.

## E

**Economic Modeling**: Analysis of costs associated with AI agent development and operation.

**Embedding**: Dense vector representation of text for semantic similarity.

**Entropy Tracking**: Monitoring complexity metrics over time to identify refactoring needs.

**Episodic Memory**: Memory of specific events and experiences.

**EvoPrompt**: Evolutionary algorithm framework for prompt optimization.

**Evolutionary Prompt Optimization**: Using evolutionary algorithms to refine prompts.

## F

**Feature Flag**: Mechanism to enable/disable features without deployment.

**Feedback Loop**: Process where output data feeds back as input for improvement.

**FrugalGPT**: Cost optimization approach using LLM cascading.

## G

**GAAPO**: Genetic Algorithmic Applied to Prompt Optimization.

**gVisor**: User-space kernel providing VM-like isolation with container-like performance.

**Graph-of-Thought (GoT)**: Reasoning framework allowing arbitrary connections between thoughts.

**Graph-Based Retrieval**: Code search using graph structures for relationship analysis.

**Gradient-Free Optimization**: Optimization without gradient information.

## H

**Hall-of-Fame**: Pattern keeping best solutions across generations in evolutionary algorithms.

**Hallucination**: LLM generating plausible but incorrect or nonsensical content.

**Hierarchical Tasking**: Decomposing tasks into subtasks with clear dependencies.

**Human-in-the-Loop (HITL)**: Human oversight at key decision points in automated workflows.

**Hybrid Memory**: Combining vector and graph memory approaches.

## I

**Infrastructure-as-Code (IaC)**: Managing infrastructure through machine-readable definition files.

**Intent-Driven Development**: Focus on desired outcomes rather than specifications.

## K

**KISS Principle**: "Keep It Simple, Stupid" - design principle emphasizing simplicity.

**Knowledge Graph**: Graph structure representing entities and their relationships.

## L

**Latency-Intelligence Tradeoff**: Balance between response speed and model capability.

**LLM Cascading**: Using cheaper models first, escalating to expensive ones only when needed.

**Lossless Semantic Tree (LST)**: Enriched tree preserving semantic information beyond syntax.

## M

**MCP (Model Context Protocol)**: Protocol for tool/resource access in AI systems.

**Memory Systems**: Architectures for storing and retrieving information for AI agents.

**Model Context Protocol (MCP)**: Standard for AI agent tool access.

**Model Routing**: Selecting appropriate models for different tasks.

**Modularity**: Degree to which system components can be separated and recombined.

**Multi-Agent Orchestration**: Coordinating multiple AI agents working together.

**Multi-Pass Enrichment**: Progressive refinement through multiple processing stages.

**Mutation Testing**: Testing technique evaluating test suite quality by introducing bugs.

## O

**Observability**: Ability to understand system internal state by examining outputs.

**Orchestrator Mode**: Agent mode for coordinating multiple agents and tasks.

## P

**PageRank**: Algorithm for ranking nodes in a graph based on importance.

**Persistent Memory**: Long-term storage for agent knowledge.

**Policy Enforcement**: Automated mechanisms ensuring compliance with policies.

**PPO (Proximal Policy Optimization)**: RL algorithm for stable training.

**Prompt Breeder**: Self-referential prompt evolution framework.

**Prompt Evolution**: Automated refinement of prompts through optimization.

**Prompt Injection**: Attack manipulating prompts to alter AI behavior.

**Progressive Disclosure**: Architecture revealing information in stages.

## R

**RAG (Retrieval-Augmented Generation)**: Combining retrieval with generation for grounded responses.

**RCOTE Framework**: Request-Confirm-Options-Trust-Escalate for HITL.

**Reasoning Architecture**: Frameworks for structured AI reasoning.

**Refactoring**: Restructuring code without changing external behavior.

**Reinforcement Learning from AI Feedback (RLAIF)**: Training with AI-generated feedback.

**Relationship Chain**: Sequence of connected code elements.

**Repo Grokking**: Deep understanding of codebase structure and relationships.

**Risk-Based Approval**: Different approval levels based on risk assessment.

## S

**Sandboxing**: Isolated execution environments for security.

**SBOM (Software Bill of Materials)**: Comprehensive inventory of software components.

**Scope Creep**: Uncontrolled growth of project scope.

**Self-Healing**: Automatic detection and recovery from failures.

**Semantic Commits**: Convention for commit messages with type, scope, description.

**Semantic Evaluation**: Assessing AI output quality based on meaning.

**Semantic Pruning**: Removing semantically identical thoughts before expansion.

**Short-Term Memory**: Temporary working memory for immediate tasks.

**Skill**: Portable capability bundle encapsulating procedural knowledge.

**Spec-Driven Development**: Development based on detailed specifications.

**SPDX**: Software Package Data Exchange standard for SBOMs.

**Symbolic Memory**: Memory using symbolic representations.

## T

**Task Decomposition**: Breaking complex tasks into manageable subtasks.

**Task Graph**: Graph representing task dependencies and execution order.

**Telemetry**: Automated collection and transmission of monitoring data.

**Temperature**: Parameter controlling randomness in LLM outputs.

**Token Efficiency**: Ratio of useful output to tokens consumed.

**Tree-of-Thought (ToT)**: Reasoning framework organizing thoughts into tree structure.

**Tree-Sitter**: Parser generator for building ASTs.

## V

**Vector Database**: Database optimized for storing and querying vector embeddings.

**Vector Memory**: Memory using dense vector representations.

**Verifiable Tool Feedback**: Objective feedback from compilers, linters, test runners.

## W

**Workflow**: Structured multi-step execution pattern for agents.

**Work Tree**: Isolated working directory for parallel development.

---

*This glossary covers key terms from the SDLC research repository. For detailed explanations, see individual topic documents.*

# SDLC Research Glossary

## A

**Abstract Syntax Tree (AST)**: A tree representation of the abstract syntactic structure of source code.

**Adversarial Reasoning**: A multi-agent approach where agents critique each other's outputs to improve quality.

**Agent Mode**: A distinct operational configuration determining how an AI agent approaches tasks (Code, Ask, Architect, Debug, Orchestrator).

**AI-SBOM**: Software Bill of Materials extended for AI systems, including models, training data, prompts, and agents.

**Anti-Hallucination**: Techniques to detect and mitigate LLM hallucinations in generated content.

**Approval Gateway**: A control point requiring explicit authorization before proceeding with an action.

**AST-Driven Retrieval**: Code search using Abstract Syntax Tree parsing for structural understanding.

## B

**Bayesian Optimization**: Sequential model-based optimization using a probabilistic surrogate model.

**Black-Box Optimization**: Optimizing functions where internal structure is unknown or cannot be differentiated.

**Blue-Green Deployment**: A deployment strategy with two identical environments for zero-downtime releases.

## C

**Canary Deployment**: Gradual rollout to a subset of users before full deployment.

**Chain-of-Thought (CoT)**: Prompting technique that breaks problems into step-by-step reasoning.

**CMA-ES**: Covariance Matrix Adaptation Evolution Strategy, a state-of-the-art evolutionary algorithm.

**Code Property Graph (CPG)**: Unified representation combining AST, CFG, and DFG.

**Complexity Budget**: A constraint limiting total complexity allowed in a system.

**Context Compression**: Techniques to reduce context window usage while preserving information.

**Context Poisoning**: Attacks that manipulate context to influence AI behavior.

**Context Window**: The maximum amount of text an LLM can process in a single request.

**Control Flow Graph (CFG)**: Graph representing all paths through a program.

**Cost-per-Task**: Total cost to complete a task including development, operational, and infrastructure costs.

**Cross-Repo Context**: Managing context across multiple repositories.

## D

**Data Drift**: Changes in data distributions over time affecting model performance.

**Data Flow Graph (DFG)**: Graph showing how data moves through a program.

**DEEVO**: Prompt evolution framework using multi-agent debate with Elo ratings.

**Dependency Graph**: Graph showing dependencies between code entities.

**Distributed Orchestration**: Managing agent clusters across multiple machines.

**Dynamic Model Routing**: Automatically selecting cost-effective models per task.

## E

**Economic Modeling**: Analysis of costs associated with AI agent development and operation.

**Embedding**: Dense vector representation of text for semantic similarity.

**Entropy Tracking**: Monitoring complexity metrics over time to identify refactoring needs.

**Episodic Memory**: Memory of specific events and experiences.

**EvoPrompt**: Evolutionary algorithm framework for prompt optimization.

**Evolutionary Prompt Optimization**: Using evolutionary algorithms to refine prompts.

## F

**Feature Flag**: Mechanism to enable/disable features without deployment.

**Feedback Loop**: Process where output data feeds back as input for improvement.

**FrugalGPT**: Cost optimization approach using LLM cascading.

## G

**GAAPO**: Genetic Algorithmic Applied to Prompt Optimization.

**gVisor**: User-space kernel providing VM-like isolation with container-like performance.

**Graph-of-Thought (GoT)**: Reasoning framework allowing arbitrary connections between thoughts.

**Graph-Based Retrieval**: Code search using graph structures for relationship analysis.

**Gradient-Free Optimization**: Optimization without gradient information.

## H

**Hall-of-Fame**: Pattern keeping best solutions across generations in evolutionary algorithms.

**Hallucination**: LLM generating plausible but incorrect or nonsensical content.

**Hierarchical Tasking**: Decomposing tasks into subtasks with clear dependencies.

**Human-in-the-Loop (HITL)**: Human oversight at key decision points in automated workflows.

**Hybrid Memory**: Combining vector and graph memory approaches.

## I

**Infrastructure-as-Code (IaC)**: Managing infrastructure through machine-readable definition files.

**Intent-Driven Development**: Focus on desired outcomes rather than specifications.

## K

**KISS Principle**: "Keep It Simple, Stupid" - design principle emphasizing simplicity.

**Knowledge Graph**: Graph structure representing entities and their relationships.

## L

**Latency-Intelligence Tradeoff**: Balance between response speed and model capability.

**LLM Cascading**: Using cheaper models first, escalating to expensive ones only when needed.

**Lossless Semantic Tree (LST)**: Enriched tree preserving semantic information beyond syntax.

## M

**MCP (Model Context Protocol)**: Protocol for tool/resource access in AI systems.

**Memory Systems**: Architectures for storing and retrieving information for AI agents.

**Model Context Protocol (MCP)**: Standard for AI agent tool access.

**Model Routing**: Selecting appropriate models for different tasks.

**Modularity**: Degree to which system components can be separated and recombined.

**Multi-Agent Orchestration**: Coordinating multiple AI agents working together.

**Multi-Pass Enrichment**: Progressive refinement through multiple processing stages.

**Mutation Testing**: Testing technique evaluating test suite quality by introducing bugs.

## O

**Observability**: Ability to understand system internal state by examining outputs.

**Orchestrator Mode**: Agent mode for coordinating multiple agents and tasks.

## P

**PageRank**: Algorithm for ranking nodes in a graph based on importance.

**Persistent Memory**: Long-term storage for agent knowledge.

**Policy Enforcement**: Automated mechanisms ensuring compliance with policies.

**PPO (Proximal Policy Optimization)**: RL algorithm for stable training.

**Prompt Breeder**: Self-referential prompt evolution framework.

**Prompt Evolution**: Automated refinement of prompts through optimization.

**Prompt Injection**: Attack manipulating prompts to alter AI behavior.

**Progressive Disclosure**: Architecture revealing information in stages.

## R

**RAG (Retrieval-Augmented Generation)**: Combining retrieval with generation for grounded responses.

**RCOTE Framework**: Request-Confirm-Options-Trust-Escalate for HITL.

**Reasoning Architecture**: Frameworks for structured AI reasoning.

**Refactoring**: Restructuring code without changing external behavior.

**Reinforcement Learning from AI Feedback (RLAIF)**: Training with AI-generated feedback.

**Relationship Chain**: Sequence of connected code elements.

**Repo Grokking**: Deep understanding of codebase structure and relationships.

**Risk-Based Approval**: Different approval levels based on risk assessment.

## S

**Sandboxing**: Isolated execution environments for security.

**SBOM (Software Bill of Materials)**: Comprehensive inventory of software components.

**Scope Creep**: Uncontrolled growth of project scope.

**Self-Healing**: Automatic detection and recovery from failures.

**Semantic Commits**: Convention for commit messages with type, scope, description.

**Semantic Evaluation**: Assessing AI output quality based on meaning.

**Semantic Pruning**: Removing semantically identical thoughts before expansion.

**Short-Term Memory**: Temporary working memory for immediate tasks.

**Skill**: Portable capability bundle encapsulating procedural knowledge.

**Spec-Driven Development**: Development based on detailed specifications.

**SPDX**: Software Package Data Exchange standard for SBOMs.

**Symbolic Memory**: Memory using symbolic representations.

## T

**Task Decomposition**: Breaking complex tasks into manageable subtasks.

**Task Graph**: Graph representing task dependencies and execution order.

**Telemetry**: Automated collection and transmission of monitoring data.

**Temperature**: Parameter controlling randomness in LLM outputs.

**Token Efficiency**: Ratio of useful output to tokens consumed.

**Tree-of-Thought (ToT)**: Reasoning framework organizing thoughts into tree structure.

**Tree-Sitter**: Parser generator for building ASTs.

## V

**Vector Database**: Database optimized for storing and querying vector embeddings.

**Vector Memory**: Memory using dense vector representations.

**Verifiable Tool Feedback**: Objective feedback from compilers, linters, test runners.

## W

**Workflow**: Structured multi-step execution pattern for agents.

**Work Tree**: Isolated working directory for parallel development.

---

*This glossary covers key terms from the SDLC research repository. For detailed explanations, see individual topic documents.*

# SDLC Research Glossary

## A

**Abstract Syntax Tree (AST)**: A tree representation of the abstract syntactic structure of source code.

**Adversarial Reasoning**: A multi-agent approach where agents critique each other's outputs to improve quality.

**Agent Mode**: A distinct operational configuration determining how an AI agent approaches tasks (Code, Ask, Architect, Debug, Orchestrator).

**AI-SBOM**: Software Bill of Materials extended for AI systems, including models, training data, prompts, and agents.

**Anti-Hallucination**: Techniques to detect and mitigate LLM hallucinations in generated content.

**Approval Gateway**: A control point requiring explicit authorization before proceeding with an action.

**AST-Driven Retrieval**: Code search using Abstract Syntax Tree parsing for structural understanding.

## B

**Bayesian Optimization**: Sequential model-based optimization using a probabilistic surrogate model.

**Black-Box Optimization**: Optimizing functions where internal structure is unknown or cannot be differentiated.

**Blue-Green Deployment**: A deployment strategy with two identical environments for zero-downtime releases.

## C

**Canary Deployment**: Gradual rollout to a subset of users before full deployment.

**Chain-of-Thought (CoT)**: Prompting technique that breaks problems into step-by-step reasoning.

**CMA-ES**: Covariance Matrix Adaptation Evolution Strategy, a state-of-the-art evolutionary algorithm.

**Code Property Graph (CPG)**: Unified representation combining AST, CFG, and DFG.

**Complexity Budget**: A constraint limiting total complexity allowed in a system.

**Context Compression**: Techniques to reduce context window usage while preserving information.

**Context Poisoning**: Attacks that manipulate context to influence AI behavior.

**Context Window**: The maximum amount of text an LLM can process in a single request.

**Control Flow Graph (CFG)**: Graph representing all paths through a program.

**Cost-per-Task**: Total cost to complete a task including development, operational, and infrastructure costs.

**Cross-Repo Context**: Managing context across multiple repositories.

## D

**Data Drift**: Changes in data distributions over time affecting model performance.

**Data Flow Graph (DFG)**: Graph showing how data moves through a program.

**DEEVO**: Prompt evolution framework using multi-agent debate with Elo ratings.

**Dependency Graph**: Graph showing dependencies between code entities.

**Distributed Orchestration**: Managing agent clusters across multiple machines.

**Dynamic Model Routing**: Automatically selecting cost-effective models per task.

## E

**Economic Modeling**: Analysis of costs associated with AI agent development and operation.

**Embedding**: Dense vector representation of text for semantic similarity.

**Entropy Tracking**: Monitoring complexity metrics over time to identify refactoring needs.

**Episodic Memory**: Memory of specific events and experiences.

**EvoPrompt**: Evolutionary algorithm framework for prompt optimization.

**Evolutionary Prompt Optimization**: Using evolutionary algorithms to refine prompts.

## F

**Feature Flag**: Mechanism to enable/disable features without deployment.

**Feedback Loop**: Process where output data feeds back as input for improvement.

**FrugalGPT**: Cost optimization approach using LLM cascading.

## G

**GAAPO**: Genetic Algorithmic Applied to Prompt Optimization.

**gVisor**: User-space kernel providing VM-like isolation with container-like performance.

**Graph-of-Thought (GoT)**: Reasoning framework allowing arbitrary connections between thoughts.

**Graph-Based Retrieval**: Code search using graph structures for relationship analysis.

**Gradient-Free Optimization**: Optimization without gradient information.

## H

**Hall-of-Fame**: Pattern keeping best solutions across generations in evolutionary algorithms.

**Hallucination**: LLM generating plausible but incorrect or nonsensical content.

**Hierarchical Tasking**: Decomposing tasks into subtasks with clear dependencies.

**Human-in-the-Loop (HITL)**: Human oversight at key decision points in automated workflows.

**Hybrid Memory**: Combining vector and graph memory approaches.

## I

**Infrastructure-as-Code (IaC)**: Managing infrastructure through machine-readable definition files.

**Intent-Driven Development**: Focus on desired outcomes rather than specifications.

## K

**KISS Principle**: "Keep It Simple, Stupid" - design principle emphasizing simplicity.

**Knowledge Graph**: Graph structure representing entities and their relationships.

## L

**Latency-Intelligence Tradeoff**: Balance between response speed and model capability.

**LLM Cascading**: Using cheaper models first, escalating to expensive ones only when needed.

**Lossless Semantic Tree (LST)**: Enriched tree preserving semantic information beyond syntax.

## M

**MCP (Model Context Protocol)**: Protocol for tool/resource access in AI systems.

**Memory Systems**: Architectures for storing and retrieving information for AI agents.

**Model Context Protocol (MCP)**: Standard for AI agent tool access.

**Model Routing**: Selecting appropriate models for different tasks.

**Modularity**: Degree to which system components can be separated and recombined.

**Multi-Agent Orchestration**: Coordinating multiple AI agents working together.

**Multi-Pass Enrichment**: Progressive refinement through multiple processing stages.

**Mutation Testing**: Testing technique evaluating test suite quality by introducing bugs.

## O

**Observability**: Ability to understand system internal state by examining outputs.

**Orchestrator Mode**: Agent mode for coordinating multiple agents and tasks.

## P

**PageRank**: Algorithm for ranking nodes in a graph based on importance.

**Persistent Memory**: Long-term storage for agent knowledge.

**Policy Enforcement**: Automated mechanisms ensuring compliance with policies.

**PPO (Proximal Policy Optimization)**: RL algorithm for stable training.

**Prompt Breeder**: Self-referential prompt evolution framework.

**Prompt Evolution**: Automated refinement of prompts through optimization.

**Prompt Injection**: Attack manipulating prompts to alter AI behavior.

**Progressive Disclosure**: Architecture revealing information in stages.

## R

**RAG (Retrieval-Augmented Generation)**: Combining retrieval with generation for grounded responses.

**RCOTE Framework**: Request-Confirm-Options-Trust-Escalate for HITL.

**Reasoning Architecture**: Frameworks for structured AI reasoning.

**Refactoring**: Restructuring code without changing external behavior.

**Reinforcement Learning from AI Feedback (RLAIF)**: Training with AI-generated feedback.

**Relationship Chain**: Sequence of connected code elements.

**Repo Grokking**: Deep understanding of codebase structure and relationships.

**Risk-Based Approval**: Different approval levels based on risk assessment.

## S

**Sandboxing**: Isolated execution environments for security.

**SBOM (Software Bill of Materials)**: Comprehensive inventory of software components.

**Scope Creep**: Uncontrolled growth of project scope.

**Self-Healing**: Automatic detection and recovery from failures.

**Semantic Commits**: Convention for commit messages with type, scope, description.

**Semantic Evaluation**: Assessing AI output quality based on meaning.

**Semantic Pruning**: Removing semantically identical thoughts before expansion.

**Short-Term Memory**: Temporary working memory for immediate tasks.

**Skill**: Portable capability bundle encapsulating procedural knowledge.

**Spec-Driven Development**: Development based on detailed specifications.

**SPDX**: Software Package Data Exchange standard for SBOMs.

**Symbolic Memory**: Memory using symbolic representations.

## T

**Task Decomposition**: Breaking complex tasks into manageable subtasks.

**Task Graph**: Graph representing task dependencies and execution order.

**Telemetry**: Automated collection and transmission of monitoring data.

**Temperature**: Parameter controlling randomness in LLM outputs.

**Token Efficiency**: Ratio of useful output to tokens consumed.

**Tree-of-Thought (ToT)**: Reasoning framework organizing thoughts into tree structure.

**Tree-Sitter**: Parser generator for building ASTs.

## V

**Vector Database**: Database optimized for storing and querying vector embeddings.

**Vector Memory**: Memory using dense vector representations.

**Verifiable Tool Feedback**: Objective feedback from compilers, linters, test runners.

## W

**Workflow**: Structured multi-step execution pattern for agents.

**Work Tree**: Isolated working directory for parallel development.

---

*This glossary covers key terms from the SDLC research repository. For detailed explanations, see individual topic documents.*

# SDLC Research Glossary

## A

**Abstract Syntax Tree (AST)**: A tree representation of the abstract syntactic structure of source code.

**Adversarial Reasoning**: A multi-agent approach where agents critique each other's outputs to improve quality.

**Agent Mode**: A distinct operational configuration determining how an AI agent approaches tasks (Code, Ask, Architect, Debug, Orchestrator).

**AI-SBOM**: Software Bill of Materials extended for AI systems, including models, training data, prompts, and agents.

**Anti-Hallucination**: Techniques to detect and mitigate LLM hallucinations in generated content.

**Approval Gateway**: A control point requiring explicit authorization before proceeding with an action.

**AST-Driven Retrieval**: Code search using Abstract Syntax Tree parsing for structural understanding.

## B

**Bayesian Optimization**: Sequential model-based optimization using a probabilistic surrogate model.

**Black-Box Optimization**: Optimizing functions where internal structure is unknown or cannot be differentiated.

**Blue-Green Deployment**: A deployment strategy with two identical environments for zero-downtime releases.

## C

**Canary Deployment**: Gradual rollout to a subset of users before full deployment.

**Chain-of-Thought (CoT)**: Prompting technique that breaks problems into step-by-step reasoning.

**CMA-ES**: Covariance Matrix Adaptation Evolution Strategy, a state-of-the-art evolutionary algorithm.

**Code Property Graph (CPG)**: Unified representation combining AST, CFG, and DFG.

**Complexity Budget**: A constraint limiting total complexity allowed in a system.

**Context Compression**: Techniques to reduce context window usage while preserving information.

**Context Poisoning**: Attacks that manipulate context to influence AI behavior.

**Context Window**: The maximum amount of text an LLM can process in a single request.

**Control Flow Graph (CFG)**: Graph representing all paths through a program.

**Cost-per-Task**: Total cost to complete a task including development, operational, and infrastructure costs.

**Cross-Repo Context**: Managing context across multiple repositories.

## D

**Data Drift**: Changes in data distributions over time affecting model performance.

**Data Flow Graph (DFG)**: Graph showing how data moves through a program.

**DEEVO**: Prompt evolution framework using multi-agent debate with Elo ratings.

**Dependency Graph**: Graph showing dependencies between code entities.

**Distributed Orchestration**: Managing agent clusters across multiple machines.

**Dynamic Model Routing**: Automatically selecting cost-effective models per task.

## E

**Economic Modeling**: Analysis of costs associated with AI agent development and operation.

**Embedding**: Dense vector representation of text for semantic similarity.

**Entropy Tracking**: Monitoring complexity metrics over time to identify refactoring needs.

**Episodic Memory**: Memory of specific events and experiences.

**EvoPrompt**: Evolutionary algorithm framework for prompt optimization.

**Evolutionary Prompt Optimization**: Using evolutionary algorithms to refine prompts.

## F

**Feature Flag**: Mechanism to enable/disable features without deployment.

**Feedback Loop**: Process where output data feeds back as input for improvement.

**FrugalGPT**: Cost optimization approach using LLM cascading.

## G

**GAAPO**: Genetic Algorithmic Applied to Prompt Optimization.

**gVisor**: User-space kernel providing VM-like isolation with container-like performance.

**Graph-of-Thought (GoT)**: Reasoning framework allowing arbitrary connections between thoughts.

**Graph-Based Retrieval**: Code search using graph structures for relationship analysis.

**Gradient-Free Optimization**: Optimization without gradient information.

## H

**Hall-of-Fame**: Pattern keeping best solutions across generations in evolutionary algorithms.

**Hallucination**: LLM generating plausible but incorrect or nonsensical content.

**Hierarchical Tasking**: Decomposing tasks into subtasks with clear dependencies.

**Human-in-the-Loop (HITL)**: Human oversight at key decision points in automated workflows.

**Hybrid Memory**: Combining vector and graph memory approaches.

## I

**Infrastructure-as-Code (IaC)**: Managing infrastructure through machine-readable definition files.

**Intent-Driven Development**: Focus on desired outcomes rather than specifications.

## K

**KISS Principle**: "Keep It Simple, Stupid" - design principle emphasizing simplicity.

**Knowledge Graph**: Graph structure representing entities and their relationships.

## L

**Latency-Intelligence Tradeoff**: Balance between response speed and model capability.

**LLM Cascading**: Using cheaper models first, escalating to expensive ones only when needed.

**Lossless Semantic Tree (LST)**: Enriched tree preserving semantic information beyond syntax.

## M

**MCP (Model Context Protocol)**: Protocol for tool/resource access in AI systems.

**Memory Systems**: Architectures for storing and retrieving information for AI agents.

**Model Context Protocol (MCP)**: Standard for AI agent tool access.

**Model Routing**: Selecting appropriate models for different tasks.

**Modularity**: Degree to which system components can be separated and recombined.

**Multi-Agent Orchestration**: Coordinating multiple AI agents working together.

**Multi-Pass Enrichment**: Progressive refinement through multiple processing stages.

**Mutation Testing**: Testing technique evaluating test suite quality by introducing bugs.

## O

**Observability**: Ability to understand system internal state by examining outputs.

**Orchestrator Mode**: Agent mode for coordinating multiple agents and tasks.

## P

**PageRank**: Algorithm for ranking nodes in a graph based on importance.

**Persistent Memory**: Long-term storage for agent knowledge.

**Policy Enforcement**: Automated mechanisms ensuring compliance with policies.

**PPO (Proximal Policy Optimization)**: RL algorithm for stable training.

**Prompt Breeder**: Self-referential prompt evolution framework.

**Prompt Evolution**: Automated refinement of prompts through optimization.

**Prompt Injection**: Attack manipulating prompts to alter AI behavior.

**Progressive Disclosure**: Architecture revealing information in stages.

## R

**RAG (Retrieval-Augmented Generation)**: Combining retrieval with generation for grounded responses.

**RCOTE Framework**: Request-Confirm-Options-Trust-Escalate for HITL.

**Reasoning Architecture**: Frameworks for structured AI reasoning.

**Refactoring**: Restructuring code without changing external behavior.

**Reinforcement Learning from AI Feedback (RLAIF)**: Training with AI-generated feedback.

**Relationship Chain**: Sequence of connected code elements.

**Repo Grokking**: Deep understanding of codebase structure and relationships.

**Risk-Based Approval**: Different approval levels based on risk assessment.

## S

**Sandboxing**: Isolated execution environments for security.

**SBOM (Software Bill of Materials)**: Comprehensive inventory of software components.

**Scope Creep**: Uncontrolled growth of project scope.

**Self-Healing**: Automatic detection and recovery from failures.

**Semantic Commits**: Convention for commit messages with type, scope, description.

**Semantic Evaluation**: Assessing AI output quality based on meaning.

**Semantic Pruning**: Removing semantically identical thoughts before expansion.

**Short-Term Memory**: Temporary working memory for immediate tasks.

**Skill**: Portable capability bundle encapsulating procedural knowledge.

**Spec-Driven Development**: Development based on detailed specifications.

**SPDX**: Software Package Data Exchange standard for SBOMs.

**Symbolic Memory**: Memory using symbolic representations.

## T

**Task Decomposition**: Breaking complex tasks into manageable subtasks.

**Task Graph**: Graph representing task dependencies and execution order.

**Telemetry**: Automated collection and transmission of monitoring data.

**Temperature**: Parameter controlling randomness in LLM outputs.

**Token Efficiency**: Ratio of useful output to tokens consumed.

**Tree-of-Thought (ToT)**: Reasoning framework organizing thoughts into tree structure.

**Tree-Sitter**: Parser generator for building ASTs.

## V

**Vector Database**: Database optimized for storing and querying vector embeddings.

**Vector Memory**: Memory using dense vector representations.

**Verifiable Tool Feedback**: Objective feedback from compilers, linters, test runners.

## W

**Workflow**: Structured multi-step execution pattern for agents.

**Work Tree**: Isolated working directory for parallel development.

---

*This glossary covers key terms from the SDLC research repository. For detailed explanations, see individual topic documents.*

# SDLC Research Glossary

## A

**Abstract Syntax Tree (AST)**: A tree representation of the abstract syntactic structure of source code.

**Adversarial Reasoning**: A multi-agent approach where agents critique each other's outputs to improve quality.

**Agent Mode**: A distinct operational configuration determining how an AI agent approaches tasks (Code, Ask, Architect, Debug, Orchestrator).

**AI-SBOM**: Software Bill of Materials extended for AI systems, including models, training data, prompts, and agents.

**Anti-Hallucination**: Techniques to detect and mitigate LLM hallucinations in generated content.

**Approval Gateway**: A control point requiring explicit authorization before proceeding with an action.

**AST-Driven Retrieval**: Code search using Abstract Syntax Tree parsing for structural understanding.

## B

**Bayesian Optimization**: Sequential model-based optimization using a probabilistic surrogate model.

**Black-Box Optimization**: Optimizing functions where internal structure is unknown or cannot be differentiated.

**Blue-Green Deployment**: A deployment strategy with two identical environments for zero-downtime releases.

## C

**Canary Deployment**: Gradual rollout to a subset of users before full deployment.

**Chain-of-Thought (CoT)**: Prompting technique that breaks problems into step-by-step reasoning.

**CMA-ES**: Covariance Matrix Adaptation Evolution Strategy, a state-of-the-art evolutionary algorithm.

**Code Property Graph (CPG)**: Unified representation combining AST, CFG, and DFG.

**Complexity Budget**: A constraint limiting total complexity allowed in a system.

**Context Compression**: Techniques to reduce context window usage while preserving information.

**Context Poisoning**: Attacks that manipulate context to influence AI behavior.

**Context Window**: The maximum amount of text an LLM can process in a single request.

**Control Flow Graph (CFG)**: Graph representing all paths through a program.

**Cost-per-Task**: Total cost to complete a task including development, operational, and infrastructure costs.

**Cross-Repo Context**: Managing context across multiple repositories.

## D

**Data Drift**: Changes in data distributions over time affecting model performance.

**Data Flow Graph (DFG)**: Graph showing how data moves through a program.

**DEEVO**: Prompt evolution framework using multi-agent debate with Elo ratings.

**Dependency Graph**: Graph showing dependencies between code entities.

**Distributed Orchestration**: Managing agent clusters across multiple machines.

**Dynamic Model Routing**: Automatically selecting cost-effective models per task.

## E

**Economic Modeling**: Analysis of costs associated with AI agent development and operation.

**Embedding**: Dense vector representation of text for semantic similarity.

**Entropy Tracking**: Monitoring complexity metrics over time to identify refactoring needs.

**Episodic Memory**: Memory of specific events and experiences.

**EvoPrompt**: Evolutionary algorithm framework for prompt optimization.

**Evolutionary Prompt Optimization**: Using evolutionary algorithms to refine prompts.

## F

**Feature Flag**: Mechanism to enable/disable features without deployment.

**Feedback Loop**: Process where output data feeds back as input for improvement.

**FrugalGPT**: Cost optimization approach using LLM cascading.

## G

**GAAPO**: Genetic Algorithmic Applied to Prompt Optimization.

**gVisor**: User-space kernel providing VM-like isolation with container-like performance.

**Graph-of-Thought (GoT)**: Reasoning framework allowing arbitrary connections between thoughts.

**Graph-Based Retrieval**: Code search using graph structures for relationship analysis.

**Gradient-Free Optimization**: Optimization without gradient information.

## H

**Hall-of-Fame**: Pattern keeping best solutions across generations in evolutionary algorithms.

**Hallucination**: LLM generating plausible but incorrect or nonsensical content.

**Hierarchical Tasking**: Decomposing tasks into subtasks with clear dependencies.

**Human-in-the-Loop (HITL)**: Human oversight at key decision points in automated workflows.

**Hybrid Memory**: Combining vector and graph memory approaches.

## I

**Infrastructure-as-Code (IaC)**: Managing infrastructure through machine-readable definition files.

**Intent-Driven Development**: Focus on desired outcomes rather than specifications.

## K

**KISS Principle**: "Keep It Simple, Stupid" - design principle emphasizing simplicity.

**Knowledge Graph**: Graph structure representing entities and their relationships.

## L

**Latency-Intelligence Tradeoff**: Balance between response speed and model capability.

**LLM Cascading**: Using cheaper models first, escalating to expensive ones only when needed.

**Lossless Semantic Tree (LST)**: Enriched tree preserving semantic information beyond syntax.

## M

**MCP (Model Context Protocol)**: Protocol for tool/resource access in AI systems.

**Memory Systems**: Architectures for storing and retrieving information for AI agents.

**Model Context Protocol (MCP)**: Standard for AI agent tool access.

**Model Routing**: Selecting appropriate models for different tasks.

**Modularity**: Degree to which system components can be separated and recombined.

**Multi-Agent Orchestration**: Coordinating multiple AI agents working together.

**Multi-Pass Enrichment**: Progressive refinement through multiple processing stages.

**Mutation Testing**: Testing technique evaluating test suite quality by introducing bugs.

## O

**Observability**: Ability to understand system internal state by examining outputs.

**Orchestrator Mode**: Agent mode for coordinating multiple agents and tasks.

## P

**PageRank**: Algorithm for ranking nodes in a graph based on importance.

**Persistent Memory**: Long-term storage for agent knowledge.

**Policy Enforcement**: Automated mechanisms ensuring compliance with policies.

**PPO (Proximal Policy Optimization)**: RL algorithm for stable training.

**Prompt Breeder**: Self-referential prompt evolution framework.

**Prompt Evolution**: Automated refinement of prompts through optimization.

**Prompt Injection**: Attack manipulating prompts to alter AI behavior.

**Progressive Disclosure**: Architecture revealing information in stages.

## R

**RAG (Retrieval-Augmented Generation)**: Combining retrieval with generation for grounded responses.

**RCOTE Framework**: Request-Confirm-Options-Trust-Escalate for HITL.

**Reasoning Architecture**: Frameworks for structured AI reasoning.

**Refactoring**: Restructuring code without changing external behavior.

**Reinforcement Learning from AI Feedback (RLAIF)**: Training with AI-generated feedback.

**Relationship Chain**: Sequence of connected code elements.

**Repo Grokking**: Deep understanding of codebase structure and relationships.

**Risk-Based Approval**: Different approval levels based on risk assessment.

## S

**Sandboxing**: Isolated execution environments for security.

**SBOM (Software Bill of Materials)**: Comprehensive inventory of software components.

**Scope Creep**: Uncontrolled growth of project scope.

**Self-Healing**: Automatic detection and recovery from failures.

**Semantic Commits**: Convention for commit messages with type, scope, description.

**Semantic Evaluation**: Assessing AI output quality based on meaning.

**Semantic Pruning**: Removing semantically identical thoughts before expansion.

**Short-Term Memory**: Temporary working memory for immediate tasks.

**Skill**: Portable capability bundle encapsulating procedural knowledge.

**Spec-Driven Development**: Development based on detailed specifications.

**SPDX**: Software Package Data Exchange standard for SBOMs.

**Symbolic Memory**: Memory using symbolic representations.

## T

**Task Decomposition**: Breaking complex tasks into manageable subtasks.

**Task Graph**: Graph representing task dependencies and execution order.

**Telemetry**: Automated collection and transmission of monitoring data.

**Temperature**: Parameter controlling randomness in LLM outputs.

**Token Efficiency**: Ratio of useful output to tokens consumed.

**Tree-of-Thought (ToT)**: Reasoning framework organizing thoughts into tree structure.

**Tree-Sitter**: Parser generator for building ASTs.

## V

**Vector Database**: Database optimized for storing and querying vector embeddings.

**Vector Memory**: Memory using dense vector representations.

**Verifiable Tool Feedback**: Objective feedback from compilers, linters, test runners.

## W

**Workflow**: Structured multi-step execution pattern for agents.

**Work Tree**: Isolated working directory for parallel development.

---

*This glossary covers key terms from the SDLC research repository. For detailed explanations, see individual topic documents.*
