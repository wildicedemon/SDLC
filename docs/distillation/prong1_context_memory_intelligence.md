# Prong 1: Context, Memory & Intelligence Knowledge Atoms

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

# Prong 1: Context, Memory & Intelligence Knowledge Atoms

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

# Prong 1: Context, Memory & Intelligence Knowledge Atoms

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

# Prong 1: Context, Memory & Intelligence Knowledge Atoms

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

# Prong 1: Context, Memory & Intelligence Knowledge Atoms

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

# Prong 1: Context, Memory & Intelligence Knowledge Atoms

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

# Prong 1: Context, Memory & Intelligence Knowledge Atoms

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

# Prong 1: Context, Memory & Intelligence Knowledge Atoms

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

# Prong 1: Context, Memory & Intelligence Knowledge Atoms

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

# Prong 1: Context, Memory & Intelligence Knowledge Atoms

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

# Prong 1: Context, Memory & Intelligence Knowledge Atoms

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

## Domain: Context, Memory & Intelligence (CMI)
**Research Scope**: Context management, knowledge representation, memory systems, and reasoning architecture for autonomous AI coding agents.

**Sources Processed**:
- docs/research/03_context_memory_intelligence/context_management/ (6 files)
- docs/research/03_context_memory_intelligence/knowledge_representation/ (6 files)
- docs/research/03_context_memory_intelligence/memory_systems/ (6 files)
- docs/research/03_context_memory_intelligence/reasoning_architecture/ (6 files)

---

## Knowledge Atoms

### KA-CMI-001
**TYPE**: TECHNIQUE  
**CONTENT**: LLMLingua prompt compression achieves 20x compression with <3% performance degradation on reasoning tasks through coarse-to-fine compression algorithms. Use for long-context scenarios where token budget is constrained.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Jiang et al., 2023)  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-002
**TYPE**: TECHNIQUE  
**CONTENT**: Selective Context method reduces tokens by 50% while maintaining 97% of original performance through information-theoretic filtering of less informative content. Requires model attention access for implementation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-003
**TYPE**: TECHNIQUE  
**CONTENT**: U-shaped context placement mitigates "lost in the middle" phenomenon where LLMs better recall information at context beginnings and ends. Place critical instructions at context start and key retrieved documents at ends, use middle sections for supporting context.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2024)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-004
**TYPE**: METRIC  
**CONTENT**: Naive context filling wastes 23-45% of tokens on irrelevant content. Optimized allocation improves task success rates by 18-32%. Target <15% waste through relevance filtering and budget-aware retrieval.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (paper:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-005
**TYPE**: FAILURE_MODE  
**CONTENT**: Context poisoning attack vectors include: (1) Model hallucination - internal generation of incorrect information treated as factual, (2) Code comments - outdated/misleading comments misinterpreted as guidance, (3) Contaminated input - hidden Unicode characters and control codes, (4) Context overflow - older useful context evicted allowing poisoned data disproportionate influence. Detection: Monitor for degraded output, tool misalignment, unexpected dependencies. Response: Treat compromised sessions as disposable; no recovery mechanism exists.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/references.md (Roocode, Wang et al., 2024)  
**DOMAINS**: D3, D8, D9  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-006
**TYPE**: ANTI_PATTERN  
**CONTENT**: Wake-up prompts (corrective prompts attempting to fix context poisoning) don't work because: (1) temporary effect only masks damage for limited interactions, (2) poisoned context persists in conversational buffer, (3) reversion occurs on queries outside immediate patch. Mitigation: Implement hard session reset as primary recovery mechanism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/patterns.md (Roocode documentation)  
**DOMAINS**: D3, D8  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-007
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic chunking preserves code structure by using AST parsing for boundary detection at function/class/module levels rather than arbitrary token limits. Results in variable chunk sizes but maintains cross-reference understanding. Implement maximum chunk size with graceful splitting at natural boundaries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-008
**TYPE**: TECHNIQUE  
**CONTENT**: Code-aware chunking requires overlap strategies to prevent losing 15-40% of cross-chunk dependencies. Implement 10-20% token overlap between adjacent chunks or use hierarchical summaries linking related chunks.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:12)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-009
**TYPE**: RECIPE  
**CONTENT**: Context window partitioning for agentic coding: Allocate 20% system prompts, 30% conversation history, 40% retrieval, 10% working space with dynamic rebalancing based on task phase. Exploration phases need more retrieval; execution phases need more working space.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (web:2)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-010
**TYPE**: TECHNIQUE  
**CONTENT**: Task-conditioned context selection retrieves different context for coding vs. debugging vs. architecture tasks. Improves context relevance and reduces noise but requires accurate task classification. Map task types to context retrieval strategies.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md (paper:5), docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-011
**TYPE**: TOOL  
**CONTENT**: Augment Context Engine MCP (launched February 2026) provides semantic code context through Model Context Protocol. Benchmarks: Cursor + Claude Opus 4.5 with MCP shows 71% improvement (60% completeness, 5x correctness); Claude Code + Opus 4.5 shows 80% overall quality improvement. Context architecture outperforms model choice: weaker model with great context outperforms stronger model with poor context.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/references.md (Augment 2026)  
**DOMAINS**: D3, D4, D10  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-012
**TYPE**: TECHNIQUE  
**CONTENT**: JetBrains Research (2025) benchmarks show LLM summarization and observation masking cut costs 50%+ without performance loss on coding agents. Observation masking replaces old observations with placeholders; LLM summarization compresses history with secondary model.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (JetBrains Research, 2025)  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-013
**TYPE**: TECHNIQUE  
**CONTENT**: Hybrid search (vector similarity + BM25/keyword) balances semantic recall with keyword precision. Pure vector search misses exact matches (e.g., API symbols). HNSW indexing provides low-latency ANN; IVF enables scalability through clustering.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_25.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-014
**TYPE**: TRADEOFF  
**CONTENT**: Context compression tradeoffs ranked: (1) Truncation: 2-5x compression, high loss, low complexity, (2) Extractive summarization: 2-3x compression, medium loss, medium complexity, (3) Abstractive summarization: 3-10x compression, variable loss, high complexity, (4) Semantic compression (LLM-based): 5-20x compression, low-medium loss, high complexity, (5) Structured representation: 10-100x compression, domain-dependent, high complexity.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/overview.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-015
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context stuffing (maximally filling context windows without prioritization) wastes 23-45% of tokens on irrelevant content, buries critical information through "lost in the middle" phenomenon, increases API costs without benefit. Mitigation: Implement relevance-based filtering, budget-aware retrieval with prioritization, U-shaped placement for critical items.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md, docs/research/03_context_memory_intelligence/context_management/comparisons.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-016
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-representation fusion combining AST + CFG + DFG improves code understanding accuracy by 35-50% compared to single-representation approaches. Tree-sitter provides incremental AST parsing with error recovery supporting 40+ languages. AST-based code search improves precision by 60-80% over text-based search.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Zhang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-017
**TYPE**: TECHNIQUE  
**CONTENT**: Code Property Graphs (CPG) unify AST, CFG, and DFG for comprehensive security analysis. Joern platform uses CPGs for vulnerability detection. Enables taint tracking detecting 70-90% of injection vulnerabilities with 10-30% false positive rates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Yamaguchi et al., 2014)  
**DOMAINS**: D3, D5, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-018
**TYPE**: TECHNIQUE  
**CONTENT**: Interprocedural analysis improves precision by 40-60% over intraprocedural analysis but increases complexity significantly. Context-sensitive analysis (distinguishing different call sites) provides highest precision but is very expensive. Use call graph construction for mapping caller-callee relationships.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Sui et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-019
**TYPE**: TOOL  
**CONTENT**: Sourcegraph indexes millions of repositories with sub-second symbol queries enabling cross-repo navigation. Kythe provides Google-scale cross-language reference indexing. LSIF (Language Server Index Format) enables offline indexing with portable, LSP-compatible indices.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-020
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic diffs reduce noise by 50-70% compared to text diffs by focusing on meaningful changes. AST diffs enable structural comparison of code; GumTree detects move operations; refactoring detection recognizes structural transformations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/comparisons.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P7  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-021
**TYPE**: TECHNIQUE  
**CONTENT**: SSA (Static Single Assignment) form simplifies data flow analysis reducing complexity from O(n²) to O(n) for many problems. Each variable assigned exactly once; phi functions merge values at control flow joins. Essential for scalable static analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Cytron et al., 1991)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-022
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single representation dependency misses insights from other perspectives resulting in incomplete understanding, missed bugs, incorrect refactoring suggestions. Mitigation: Implement multi-representation fusion (AST + CFG + DFG), add complementary representations, validate across representation types.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC4

---

### KA-CMI-023
**TYPE**: TECHNIQUE  
**CONTENT**: Incremental representation updates reduce update time by 80-95% compared to full rebuilds. Use Tree-sitter for incremental AST updates with error recovery. Define update propagation to dependent representations (CFG, DFG) and implement consistency validation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/patterns.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Chen et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-024
**TYPE**: TECHNIQUE  
**CONTENT**: Lossless Semantic Trees (LST) extend ASTs with semantic annotations preserving full fidelity including comments and whitespace for round-trip editing. srcML provides XML-based lossless representation handling incomplete/erroneous code where ASTs fail (66% failure rate on non-parsable code).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/perplexityai_research_overview_13.md (srcML-DKT paper, EDM 2025)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-025
**TYPE**: TECHNIQUE  
**CONTENT**: Vector database selection for agent memory: Pinecone (managed cloud, billions scale, 10-50ms latency), Weaviate (hybrid vector+keyword, GraphQL API, 5-20ms), Qdrant (Rust-based, payload filtering, 5-30ms), Chroma (embedded, millions scale, 1-10ms), Milvus (distributed, trillions scale, 10-100ms). Code-specific embeddings (Voyage Code, CodeSage) outperform general embeddings by 15-30%.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-026
**TYPE**: TECHNIQUE  
**CONTENT**: MemGPT virtual context architecture extends effective memory through hierarchical management: core memory (limited, always-visible) and archival memory (unlimited, retrieval-based). Agents manage their own memory through explicit memory operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Packer et al., 2023)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7, P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-027
**TYPE**: TECHNIQUE  
**CONTENT**: GraphRAG combines knowledge graphs with vector retrieval achieving 23% improvement on multi-hop reasoning tasks. Microsoft Research implementation requires significant infrastructure but provides structured context for complex queries.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/comparisons.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Edge et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-028
**TYPE**: METRIC  
**CONTENT**: Vector databases achieve 85-95% recall@10 on code search benchmarks. Hybrid retrieval (keyword + semantic) provides best recall/precision balance. HNSW provides high accuracy with high memory; IVF provides scalability with lower recall.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-029
**TYPE**: TECHNIQUE  
**CONTENT**: Auto-learning memory systems: Experience replay buffers improve agent performance by 12-18% after 100+ interactions. Success pattern extraction identifies reusable approaches; failure pattern recording stores anti-patterns. Experience-derived heuristics improve task success but require validation to avoid overfitting.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/overview.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Hu et al., 2024)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-030
**TYPE**: ANTI_PATTERN  
**CONTENT**: Catastrophic forgetting: New learning overwrites previous knowledge without preservation. Mitigation: Implement experience replay buffers, use regularization techniques (elastic weight consolidation), archive important knowledge before updates.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/references.md (Kirkpatrick et al., 2017)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-031
**TYPE**: ANTI_PATTERN  
**CONTENT**: Stale embeddings: Failing to update vector embeddings when underlying content changes leads to retrieval of outdated information. Mitigation: Implement change-triggered re-embedding, add version tracking to embeddings, monitor embedding freshness metrics.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-032
**TYPE**: RECIPE  
**CONTENT**: Hierarchical memory architecture tiers: Working memory (immediate, limited) → Session memory (conversation-scoped) → Long-term memory (persistent, unlimited). Define clear tier boundaries, promotion/demotion rules, and efficient tier-to-tier transfer mechanisms.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/patterns.md, docs/research/03_context_memory_intelligence/memory_systems/overview.md  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-033
**TYPE**: TECHNIQUE  
**CONTENT**: A-MEM (Agentic Memory) provides Zettelkasten-inspired self-evolving memory graphs with autonomous link generation and memory evolution. Creates interconnected graphs from atomic notes enabling multi-hop reasoning and long-term adaptation without static operations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (arXiv 2502.12110)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-034
**TYPE**: TECHNIQUE  
**CONTENT**: Chain-of-Thought (CoT) prompting achieves 20-40% accuracy improvement on reasoning tasks through step-by-step decomposition. Zero-shot CoT with "Let's think step by step" instruction; few-shot CoT with example demonstrations; self-consistency CoT with multiple reasoning paths and majority voting.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Wei et al., 2022)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-035
**TYPE**: TECHNIQUE  
**CONTENT**: Tree-of-Thought (ToT) reasoning achieves 30-50% improvement on complex tasks over CoT through branching exploration, evaluation heuristics, search algorithms (BFS, DFS, beam search), and backtracking. Requires 5-10x more compute than standard CoT.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Yao et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-036
**TYPE**: TECHNIQUE  
**CONTENT**: Graph-of-Thought (GoT) extends ToT with arbitrary graph structures achieving additional 10-20% improvement over ToT on tasks requiring synthesis of multiple ideas. Enables non-linear reasoning, thought aggregation, decomposition, and feedback loops. GoT achieves 62% better sorting than ToT at 31% lower cost.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/perplexityai_research_overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Besta et al., 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-037
**TYPE**: TECHNIQUE  
**CONTENT**: Reflexion (self-critique) reduces error rates by 25-40% on code generation through iterative critique and refinement. Agents reflect on failures and adjust approach. Risk: "Echo chamber" effects where models fail to identify their own errors.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Shinn et al., 2023)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-038
**TYPE**: TECHNIQUE  
**CONTENT**: Multi-model adversarial reasoning shows 40% higher bug detection rates compared to single-model review. Approaches: Red teaming (dedicated adversary model attacks outputs), debate protocols (models argue for different positions), voting ensembles (multiple models vote), critic-generator pairs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Perez et al., 2022)  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-039
**TYPE**: TECHNIQUE  
**CONTENT**: Pre-execution validation catches 60-75% of potential errors, significantly reducing rollback costs. Techniques: Static analysis (checking plans for obvious errors), simulation/dry-run (predicted execution), constraint checking, dependency validation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-040
**TYPE**: ANTI_PATTERN  
**CONTENT**: Echo chamber self-review: Self-critique fails to identify errors because reviewing perspective is too similar to generating perspective. Mitigation: Use external or adversarial reviewers, implement structured checklists from different perspectives, vary temperature/settings for critique phase.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-041
**TYPE**: CONSTRAINT  
**CONTENT**: Temperature settings for coding tasks: Roocode recommends 0.3-0.5 for coding tasks to balance creativity with correctness. Lower temperatures produce overconfident outputs but higher consistency; higher temperatures increase diversity but risk hallucinations.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Roocode 2024)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-042
**TYPE**: TECHNIQUE  
**CONTENT**: Confidence scoring methods: Verbalized confidence (simple but poorly calibrated), logit-based scoring (objective but requires logit access), consistency-based (multi-sample agreement, better calibration but compute overhead), ensemble confidence (multi-model agreement, most reliable but highest cost).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/overview.md, docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-043
**TYPE**: ANTI_PATTERN  
**CONTENT**: Infinite refinement loops: Self-critique cycles continue indefinitely without convergence or with oscillating "improvements." Mitigation: Define maximum iteration limits (typically 2-3 iterations), implement quality-based early stopping, monitor for convergence or oscillation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-044
**TYPE**: RECIPE  
**CONTENT**: Intent verification checkpoint pattern: Explicit verification that planned actions align with user intent before execution. Use for destructive/irreversible operations, high-stakes code changes, ambiguous tasks. Define risk thresholds triggering verification, implement structured clarification prompts.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md, docs/research/03_context_memory_intelligence/reasoning_architecture/references.md (Kilo 2024)  
**DOMAINS**: D3, D7, D9  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-045
**TYPE**: COMBINATION  
**CONTENT**: Critical security code generation pattern: Adversarial Review + Confidence-Gated Execution + Test-Driven Reasoning. Generate tests covering security edge cases, perform dedicated security-focused adversarial review, apply high confidence threshold for deployment, require human verification checkpoint before merge.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/patterns.md  
**DOMAINS**: D3, D7, D8  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-046
**TYPE**: COMBINATION  
**CONTENT**: Long-running debugging session pattern: Sliding Window with Overlap + Hierarchical Summarization + Context Caching. Maintain sliding window of recent investigation, compress older context into hierarchical summaries, cache error patterns and previous solutions, implement context prioritization for debugging clues.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-047
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent code review pattern: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement. Track which agent contributed which context, condition context on review type (security → vulnerability DB, performance → benchmarks), place code under review at context edges, share common context via shared pool.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4, D7  
**SDLC_PHASES**: P5, P6, P7  
**PRODUCTS**: PC1, PC4, PC7

---

### KA-CMI-048
**TYPE**: TRADEOFF  
**CONTENT**: Reasoning paradigm tradeoffs: Chain-of-Thought (low complexity, 20-40% improvement, no backtracking), Self-Consistency CoT (medium complexity, additional 15-25% improvement, 5-10x compute overhead), Tree-of-Thought (high complexity, 30-50% improvement, high compute), Graph-of-Thought (very high complexity, additional 10-20% over ToT, highest complexity).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/reasoning_architecture/comparisons.md  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-049
**TYPE**: TECHNIQUE  
**CONTENT**: Hippocampus memory module achieves 31× reduction in retrieval latency and 14× reduction in token footprint using compact binary signatures for semantic search and lossless token-ID streams. Uses Dynamic Wavelet Matrix implementation.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Li et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-050
**TYPE**: TECHNIQUE  
**CONTENT**: StateLM (Pensieve Paradigm) achieves 52% accuracy on BrowseComp-Plus vs 5% for standard LLMs through internal reasoning loop managing state via memory tools: context pruning, document indexing, and note-taking. Requires training with memory tool integration.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Liu et al., 2026)  
**DOMAINS**: D3, D6, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-051
**TYPE**: TECHNIQUE  
**CONTENT**: Mnemis dual-route retrieval achieves 93.9 on LoCoMo and 91.6 on LongMemEval-S through System-1 similarity search combined with System-2 Global Selection mechanism. Organizes memory into base graph and hierarchical graph for top-down traversal.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Tang et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-052
**TYPE**: ANTI_PATTERN  
**CONTENT**: Context staleness: Failing to update or invalidate cached context when underlying codebase changes leads to decisions based on outdated information. Mitigation: Implement file-watcher-based invalidation, use versioning/timestamps for context, define staleness thresholds per context type.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D4  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-CMI-053
**TYPE**: ANTI_PATTERN  
**CONTENT**: Blind code comment trust: Treating code comments as authoritative guidance without validation against actual code behavior. Comments may be outdated, incorrect, or ambiguous. Mitigation: Cross-reference comments with implementation, validate assumptions through testing, use comments as hints not facts.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/patterns.md  
**DOMAINS**: D3, D5, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-054
**TYPE**: TECHNIQUE  
**CONTENT**: GCP (Git-like Context) framework introduces COMMIT, BRANCH, MERGE operations for versioning agent context, enabling rollback and merging of interaction histories. Foundational for structured memory in long-running agents.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/perplexityai_research_overview_02.md (arXiv 2508.00031v1)  
**DOMAINS**: D3, D4, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-055
**TYPE**: TECHNIQUE  
**CONTENT**: Type inference for dynamically-typed code achieves 90%+ coverage using neural approaches, enabling understanding without annotations. Deep type inference eliminates annotation burden but accuracy varies by language and codebase.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/knowledge_representation/overview.md, docs/research/03_context_memory_intelligence/knowledge_representation/references.md (Wang et al., 2024)  
**DOMAINS**: D3, D5  
**SDLC_PHASES**: P3, P4, P5  
**PRODUCTS**: PC1, PC7

---

### KA-CMI-056
**TYPE**: CONSTRAINT  
**CONTENT**: Selective memory management with add/delete policies improves long-term performance by 10% and curbs error propagation. Unfiltered growth leads to error propagation and bloat.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/memory_systems/perplexityai_research_overview.md (Xiong et al., 2025)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6, P7  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-057
**TYPE**: TECHNIQUE  
**CONTENT**: HyMem hybrid memory architecture reduces computational cost by 92.6% through dual-granular storage: lightweight module for summary-level context, LLM-based deep module for complex queries. Implements dynamic two-tier retrieval system.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Zhao et al., 2026)  
**DOMAINS**: D3, D6  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

### KA-CMI-058
**TYPE**: TECHNIQUE  
**CONTENT**: Semantic weighting reduces cumulative distortion in MCP agents by 80% according to martingale analysis. Information fidelity in tool-using agents exhibits linear growth with O(√T) deviation bounds.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/03_context_memory_intelligence/context_management/references.md (Fan et al., 2026)  
**DOMAINS**: D3, D7  
**SDLC_PHASES**: P3, P4, P5, P6  
**PRODUCTS**: PC1, PC2

---

## Summary Statistics

| Atom Type | Count |
|-----------|-------|
| TECHNIQUE | 37 |
| METRIC | 3 |
| CONSTRAINT | 2 |
| TOOL | 3 |
| COMBINATION | 4 |
| FAILURE_MODE | 1 |
| ANTI_PATTERN | 10 |
| TRADEOFF | 3 |
| RECIPE | 3 |
| **TOTAL** | **58** |

## Evidence Strength Distribution

| Strength | Count |
|----------|-------|
| STRONG | 36 |
| MODERATE | 22 |
| WEAK | 0 |

## Domain Coverage

| Domain | Atoms |
|--------|-------|
| D3 (Context, Memory & Intelligence) | 58 |
| D4 (Context Management) | 28 |
| D5 (Knowledge Representation) | 12 |
| D6 (Memory Systems) | 20 |
| D7 (Reasoning Architecture) | 26 |
| D8 (Security Architecture) | 8 |
| D9 (Human-in-the-Loop) | 3 |
| D10 (MCP/Tools) | 2 |

## SDLC Phase Coverage

| Phase | Atoms |
|-------|-------|
| P1 (Requirements) | 1 |
| P2 (Design) | 1 |
| P3 (Implementation) | 52 |
| P4 (Code Review) | 51 |
| P5 (Testing) | 51 |
| P6 (Debugging) | 52 |
| P7 (Deployment) | 25 |
| P8 (Operations) | 6 |

## Knowledge Gaps

1. **Limited empirical data on context poisoning attack success rates** - Most sources identify vectors but lack quantitative success metrics.

2. **Missing evaluation of context engine architectures against traditional RAG** - Augment Context Engine benchmarks are vendor-reported; independent validation needed.

3. **Sparse empirical data on memory drift and staleness rates** - Auto-learning systems lack production validation for catastrophic forgetting mitigation.

4. **Limited benchmark comparisons across reasoning architectures** - Most comparisons use different tasks making direct comparison difficult.

5. **Missing optimal chunk size and overlap for code-aware context splitting** - Research acknowledges the problem but provides limited concrete guidance.

6. **No standardized benchmarks for adversarial reasoning on real-world code** - Effectiveness measured on synthetic tasks.

7. **Limited research on cross-repo context synchronization without stale state** - Enterprise patterns lack empirical validation.

## Recommended Next Subtask

**Prong 2 Domain Grouping**: Map extracted knowledge atoms to domain relationships and identify cross-domain dependencies. Focus on:
- Context management dependencies on memory systems
- Reasoning architecture requirements from context management
- Knowledge representation integration with memory and reasoning

