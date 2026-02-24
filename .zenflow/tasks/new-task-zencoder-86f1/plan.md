# Full SDD workflow

## Configuration
- **Artifacts Path**: {@artifacts_path} → `.zenflow/tasks/{task_id}`

---

## Agent Instructions

If you are blocked and need user clarification, mark the current step with `[!]` in plan.md before stopping.

---

## Workflow Steps

### [ ] Step: Requirements
<!-- chat-id: bf5d1834-6b9a-4999-8e0f-b0b5ea9f13e6 -->

Create a Product Requirements Document (PRD) based on the feature description.

1. Review existing codebase to understand current architecture and patterns
2. Analyze the feature definition and identify unclear aspects
3. Ask the user for clarifications on aspects that significantly impact scope or user experience
4. Make reasonable decisions for minor details based on context and conventions
5. If user can't clarify, make a decision, state the assumption, and continue

Save the PRD to `{@artifacts_path}/requirements.md`.

### [x] Step: Technical Specification
<!-- chat-id: 4bccf74f-63ab-4691-8c82-4abffda797d5 -->

Create a technical specification based on the PRD in `{@artifacts_path}/requirements.md`.

1. Review existing codebase architecture and identify reusable components
2. Define the implementation approach

Save to `{@artifacts_path}/spec.md` with:
- Technical context (language, dependencies)
- Implementation approach referencing existing code patterns
- Source code structure changes
- Data model / API / interface changes
- Delivery phases (incremental, testable milestones)
- Verification approach using project lint/test commands

### [x] Step: Planning
<!-- chat-id: c09d374b-a622-4a05-8550-18217dfdd9a6 -->

Create a detailed implementation plan based on `{@artifacts_path}/spec.md`.

1. Break down the work into concrete tasks
2. Each task should reference relevant contracts and include verification steps
3. Replace the Implementation step below with the planned tasks

Rule of thumb for step size: each step should represent a coherent unit of work (e.g., implement a component, add an API endpoint). Avoid steps that are too granular (single function) or too broad (entire feature).

Important: unit tests must be part of each implementation task, not separate tasks. Each task should implement the code and its tests together, if relevant.

If the feature is trivial and doesn't warrant full specification, update this workflow to remove unnecessary steps and explain the reasoning to the user.

Save to `{@artifacts_path}/plan.md`.

### [x] Step: Phase 1 - Core Infrastructure Setup
<!-- chat-id: 62b63797-5fc7-4959-8933-181764070387 -->

Set up the basic project structure, data models, and configuration system.

1. Create project directory structure with distillation/ package
2. Set up pyproject.toml with all dependencies (pydantic, typer, beautifulsoup4, markdown, pytest, etc.)
3. Implement core data models (KnowledgeAtom, ProductSpec, etc.) in models/ directory
4. Create configuration management system with YAML support
5. Set up basic CLI interface with typer
6. Write unit tests for all data models and configuration

**Verification**: Run `pytest` for unit tests, `mypy` for type checking, `ruff` for linting. All models should validate correctly and CLI should accept basic commands.

### [x] Step: Phase 2 - Research Ingestion Engine
<!-- chat-id: f92346aa-7d39-458d-b9e2-3b26c4fee0f8 -->

Implement multi-format file parsing and content extraction.

1. Create ResearchIngestor class in processors/ingestion.py
2. Implement parsers for Markdown, HTML, JSON, and CSV formats
3. Add content chunking for large documents
4. Build metadata extraction (source, date, author, citations)
5. Create ResearchFile data model for processed content
6. Write integration tests for file processing pipeline

**Verification**: Process sample files of each format, verify metadata extraction accuracy, ensure large files are handled without memory issues.

### [x] Step: Phase 3 - Knowledge Atom Extraction
<!-- chat-id: 28c6f355-3de4-4b41-9d2f-f440a04790c5 -->

Build the core extraction logic with pattern-based rules.

1. Create AtomExtractor class in processors/extraction.py
2. Implement KEEP/DISCARD extraction rules as configurable patterns
3. Add evidence strength assessment (STRONG/MODERATE/WEAK)
4. Build deduplication algorithms across sources
5. Implement atom type classification (TECHNIQUE, METRIC, CONSTRAINT, etc.)
6. Create extraction rule configuration system
7. Write unit tests for extraction accuracy and deduplication

**Verification**: Extract atoms from sample research files, verify >95% precision in atom identification, test deduplication across multiple sources.

### [ ] Step: Phase 4 - Domain & Phase Mapping
<!-- chat-id: cdfc8a8f-32ee-4ca9-81d6-a4452cd26124 -->

Implement grouping logic for domains and SDLC phases.

1. Create DomainMapper class in processors/domain_mapper.py with all 12 domains
2. Implement SDLC Phase Assigner in processors/phase_assigner.py with all 8 phases
3. Add cross-domain relationship tracking
4. Build gap analysis reporting functionality
5. Create ranking algorithms for atoms within domains
6. Write tests for domain assignment accuracy and phase mapping

**Verification**: All atoms from test corpus assigned to appropriate domains, phase assignments match expected SDLC workflow, cross-domain links identified correctly.

### [ ] Step: Phase 5 - Product Assembly System
<!-- chat-id: 02a84dd1-94eb-48f2-862e-f78d725c4cb1 -->

Create template-based specification generation.

1. Create ProductAssembler class in processors/product_assembler.py
2. Implement YAML template system in templates/ directory for all 10 product types
3. Add confidence scoring algorithms for generated specs
4. Build spec validation against defined schemas
5. Create output formatting for product specifications
6. Write tests for template rendering and spec validation

**Verification**: Generate valid YAML specifications for all product types, specifications follow defined templates, confidence scores reflect research backing.

### [ ] Step: Phase 6 - Pipeline Integration & Optimization
<!-- chat-id: c711413a-2090-433d-b2c5-699701714afb -->

Integrate all components into a complete distillation pipeline.

1. Create ResearchDistiller orchestrator class with full pipeline integration
2. Implement async processing for concurrent file handling
3. Add comprehensive error handling and recovery
4. Optimize performance (target <5min for full corpus, <100MB memory)
5. Build end-to-end integration tests
6. Add performance monitoring and benchmarking

**Verification**: Full pipeline processes research corpus end-to-end, meets performance targets, handles edge cases gracefully, comprehensive test suite passes.

### [ ] Step: Final Integration & Validation
<!-- chat-id: b91beacc-a4a3-483a-80c0-08a46341bf99 -->

Complete system integration, testing, and validation.

1. Run full pipeline on complete research corpus
2. Perform manual review of 10% sample outputs
3. Validate generated specs can be used to create agent components
4. Ensure gap reports identify real missing knowledge areas
5. Final performance benchmarking and optimization
6. Create comprehensive documentation and usage examples

**Verification**: All success criteria met (95%+ extraction precision, <5min processing, 90%+ test coverage, manual review passes).
