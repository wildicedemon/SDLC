# Technical Specification: Multi-Prong Research Distillation System

## 1. Technical Context
- **Language**: Python 3.10+
- **Key Dependencies**:
  - `anthropic` or `openai`: SDKs to invoke the LLM with a large context window (e.g., Claude 3.5 Sonnet / GPT-4o) since the context could be large (hundreds of KB of research).
  - `pydantic` (v2.x): For strict schema definition of Knowledge Atoms, Domains, SDLC Phases, and various Product Specs.
  - `pyyaml`: For serializing models into valid YAML outputs according to the template requirements.
  - `asyncio`: For parallelized execution where independent processing is possible.

## 2. Implementation Approach
The distillation system will be built as a Python CLI application that automates the execution of the provided "Multi-Prong Research Distillation Prompt". Given the length of the research corpus, feeding everything in one go and expecting perfect, non-truncated output is challenging. The approach uses an LLM with an extended context window in a multi-stage (map-refine) pipeline to match the four prongs.

### Workflow:
1. **Corpus Ingestion**: The script loads `.md` research files from the configured directory (e.g., local markdown files like `Perplexity_Thread.md` and `Research.md`).
2. **LLM Invocation (Prong 1 - Refine)**: Sends the corpus alongside the instructions to extract the Knowledge Atoms.
3. **Structured Parsing (Intermediate)**: The script intercepts the LLM output, parsing out the extracted Atoms using regex or structured LLM tool calling to cast them into `KnowledgeAtom` Pydantic models.
4. **LLM Invocation (Prongs 2-4)**: Using the extracted structured atoms, it queries the LLM again for Domains (Prong 2), SDLC Phases (Prong 3), and Product Mappings (Prong 4).
5. **Serialization**: Pydantic models are serialized into separate YAML files for each domain, phase, and product type.
6. **Validation Engine**: A programmatic Python validator asserts that all cross-references exist, checking that no atom is orphaned and constraints have matching enforcements.
7. **Report Generation**: Outputs a gap analysis markdown file based on the PRD criteria.

## 3. Source Code Structure Changes
- `scripts/distillation/`: Main module directory.
  - `__init__.py`
  - `main.py`: Entry point for the CLI pipeline.
  - `schemas.py`: Pydantic models (`KnowledgeAtom`, `Domain`, `Phase`, `SkillSpec`, `ModeSpec`, etc.).
  - `llm_client.py`: Async interface for the LLM API with chunking support.
  - `parser.py`: Logic to parse and clean markdown/YAML code blocks from LLM responses.
  - `validator.py`: Cross-reference and gap analysis checking logic.
- `scripts/prompts/distillation_prompt.txt`: The system instructions separated into stages to aid the LLM.
- `output/distilled/`: Generated artifacts target folder (e.g., `atoms/`, `domains/`, `phases/`, `products/`).

## 4. Data Model / API / Interface Changes
**Pydantic Models (in `schemas.py`)**:
- `KnowledgeAtom`: `id` (str), `type` (Enum), `content` (str), `evidence_strength` (Enum), `source` (list[str]), `domains` (list[str]), `sdlc_phases` (list[str]), `products` (list[str]).
- `DomainSpec`: `domain` (str), `knowledge_atoms` (list[str]), `key_techniques` (list[dict]), `key_constraints` (list[dict]), etc.
- `PhaseSpec`: `phase` (str), `what_the_agent_is_doing` (str), `techniques_to_use` (list[dict]), etc.
- `ProductSpec`: Base model with `product_category` (str), `instance` (str), `knowledge_atoms_consumed` (list[str]), `draft_spec` (dict), `confidence` (Enum), `gaps` (str).
- `SkillSpec`, `ModeSpec`, `WorkflowSpec`, `RuleSpec`, etc.: Strict typed schemas mirroring the YAML templates in the PRD.

## 5. Delivery Phases
- **Phase 1: Foundation & Data Models**: Create the Pydantic schemas corresponding to the YAML templates and the Knowledge Atom format. Write simple unit tests for schema validation.
- **Phase 2: LLM Integration & Parsing**: Implement `llm_client.py` and `parser.py`. Create a test using a small sample markdown file to verify successful generation and extraction of Knowledge Atoms.
- **Phase 3: Pipeline Orchestration**: Build `main.py` to chain the prompt executions (Prong 1 -> Prongs 2/3 -> Prong 4) and write the parsed outputs to the `output/distilled/` directory structure.
- **Phase 4: Validation Engine**: Implement `validator.py` to check for orphaned atoms, missing cross-references, and unhandled failure modes. Generate the final Gap Report.

## 6. Verification Approach
- **Unit Testing**: Run `pytest` on `schemas.py` and `validator.py` using mocked LLM outputs (sample YAML blocks) to ensure the pipeline correctly catches schema violations or orphaned atoms.
- **Integration Testing**: Execute the script against a curated dummy research file (`dummy_research.md`) to verify end-to-end execution without encountering token limits.
- **Linting & Typing**: Standard `flake8`, `black`, and `mypy` running against the `scripts/distillation` module to ensure type safety, particularly for complex nested Pydantic models.