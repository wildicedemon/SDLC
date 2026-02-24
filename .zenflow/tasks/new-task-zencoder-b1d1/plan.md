# Full SDD workflow

## Configuration
- **Artifacts Path**: {@artifacts_path} → `.zenflow/tasks/{task_id}`

---

## Agent Instructions

If you are blocked and need user clarification, mark the current step with `[!]` in plan.md before stopping.

---

## Workflow Steps

### [x] Step: Requirements
<!-- chat-id: 639e68af-b010-437b-8557-741902dad0ff -->

Create a Product Requirements Document (PRD) based on the feature description.

1. Review existing codebase to understand current architecture and patterns
2. Analyze the feature definition and identify unclear aspects
3. Ask the user for clarifications on aspects that significantly impact scope or user experience
4. Make reasonable decisions for minor details based on context and conventions
5. If user can't clarify, make a decision, state the assumption, and continue

Save the PRD to `{@artifacts_path}/requirements.md`.

### [x] Step: Technical Specification
<!-- chat-id: bc6cb2b2-5207-48df-9200-d61e4fd40d52 -->

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
<!-- chat-id: a0e1c75a-c684-4396-8eb5-797f4d3c7cef -->

Create a detailed implementation plan based on `{@artifacts_path}/spec.md`.

1. Break down the work into concrete tasks
2. Each task should reference relevant contracts and include verification steps
3. Replace the Implementation step below with the planned tasks

Rule of thumb for step size: each step should represent a coherent unit of work (e.g., implement a component, add an API endpoint). Avoid steps that are too granular (single function) or too broad (entire feature).

Important: unit tests must be part of each implementation task, not separate tasks. Each task should implement the code and its tests together, if relevant.

If the feature is trivial and doesn't warrant full specification, update this workflow to remove unnecessary steps and explain the reasoning to the user.

Save to `{@artifacts_path}/plan.md`.

### [x] Step: Project Setup
<!-- chat-id: 64148ab5-a650-4de2-a5b6-1df08d24ac82 -->
- Initialize Python project with a `requirements.txt` or `pyproject.toml` including dependencies: `pydantic`, `pyyaml`, `anthropic` or `openai`, `pytest`, `flake8`, `black`, `mypy`.
- Create directory structure: `scripts/distillation/`, `scripts/prompts/`, and `output/distilled/`.
- Verify environment setup by successfully installing dependencies.

### [x] Step: Phase 1 Foundation & Data Models
<!-- chat-id: 137bb056-3c1e-4dda-8ab7-81b1fbd21296 -->
- Create the Pydantic schemas corresponding to the YAML templates and the Knowledge Atom format in `scripts/distillation/schemas.py`.
- Write simple unit tests for schema validation in `tests/test_schemas.py`.
- Verify with `pytest` and `mypy`.

### [x] Step: Phase 2 LLM Integration & Parsing
<!-- chat-id: 6339c619-1b41-4a3b-9430-5553a561988c -->
- Implement `llm_client.py` and `parser.py` in `scripts/distillation/`.
- Add `scripts/prompts/distillation_prompt.txt` based on the PRD prompt.
- Create a test in `tests/test_parser.py` using a small sample markdown file to verify successful generation and extraction of Knowledge Atoms.
- Verify with `pytest`.

### [ ] Step: Phase 3 Pipeline Orchestration
- Build `main.py` in `scripts/distillation/` to chain the prompt executions (Prong 1 -> Prongs 2/3 -> Prong 4).
- Ensure parsed outputs are written correctly to the `output/distilled/` directory structure using `pyyaml`.
- Verify end-to-end execution against a curated dummy research file (`dummy_research.md`).

### [ ] Step: Phase 4 Validation Engine
- Implement `validator.py` in `scripts/distillation/` to check for orphaned atoms, missing cross-references, and unhandled failure modes.
- Implement generation of the final Gap Report.
- Write unit tests in `tests/test_validator.py` to ensure orphaned atoms or missing references are caught.
- Run `flake8`, `black`, and `mypy` against the entire `scripts/distillation` module to ensure code quality.
