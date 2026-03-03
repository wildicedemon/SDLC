"""Bootstrap the corpus DB with decision cards from 03_indices and per-domain cards."""

import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from corpus.config import CorpusSettings
from corpus.db.engine import create_db_engine, get_session
from corpus.db.migrations.runner import migrate_forward
from corpus.db.repository import CorpusRepository
from corpus.ingestion.classifier import DOMAIN_DIRECTORIES

SUBDOMAIN_TO_DOMAIN: dict[str, str] = {}
for top_dir, subs in DOMAIN_DIRECTORIES.items():
    for sub in subs:
        SUBDOMAIN_TO_DOMAIN[sub] = top_dir

DECISIONS_FROM_INDEX = [
    {
        "decision_id": "dc_rbf_001",
        "capability": "research_benchmarking_framework",
        "question": "How should experiments be pre-registered?",
        "recommendation": "Use pre-registered experiment protocols with hypothesis, methodology, analysis plan",
        "confidence_score": 0.74,
        "confidence_level": "medium",
        "provenance_refs": "patterns.md#L5-L27",
    },
    {
        "decision_id": "dc_rbf_002",
        "capability": "research_benchmarking_framework",
        "question": "How should statistical evaluation be performed?",
        "recommendation": "Use multi-run statistical evaluation with confidence intervals and effect sizes",
        "confidence_score": 0.78,
        "confidence_level": "high",
        "provenance_refs": "patterns.md#L30-L52",
    },
    {
        "decision_id": "dc_rbf_003",
        "capability": "research_benchmarking_framework",
        "question": "How should deployment evaluation be handled?",
        "recommendation": "Use shadow deployment evaluation with A/B testing",
        "confidence_score": 0.71,
        "confidence_level": "medium",
        "provenance_refs": "patterns.md#L55-L77",
    },
    {
        "decision_id": "dc_rbf_004",
        "capability": "research_benchmarking_framework",
        "question": "How should benchmarks be structured?",
        "recommendation": "Use hierarchical benchmark suites with unit, integration, and system levels",
        "confidence_score": 0.76,
        "confidence_level": "high",
        "provenance_refs": "patterns.md#L80-L103",
    },
    {
        "decision_id": "dc_rbf_005",
        "capability": "research_benchmarking_framework",
        "question": "How should contamination be controlled?",
        "recommendation": "Implement contamination control via data isolation and holdout sets",
        "confidence_score": 0.77,
        "confidence_level": "high",
        "provenance_refs": "patterns.md#L106-L129",
    },
    {
        "decision_id": "dc_rbf_006",
        "capability": "research_benchmarking_framework",
        "question": "How should experiments be logged?",
        "recommendation": "Use structured experiment logging with versioned artifacts and reproducibility metadata",
        "confidence_score": 0.80,
        "confidence_level": "high",
        "provenance_refs": "patterns.md#L132-L155",
    },
    {
        "decision_id": "dc_rbf_007",
        "capability": "research_benchmarking_framework",
        "question": "How should capabilities be evaluated?",
        "recommendation": "Use capability matrix evaluation across multiple dimensions",
        "confidence_score": 0.73,
        "confidence_level": "medium",
        "provenance_refs": "patterns.md#L158-L181",
    },
    {
        "decision_id": "dc_rbf_008",
        "capability": "research_benchmarking_framework",
        "question": "How should baseline drift be monitored?",
        "recommendation": "Implement continuous baseline drift monitoring with alerting",
        "confidence_score": 0.75,
        "confidence_level": "high",
        "provenance_refs": "patterns.md#L184-L207",
    },
    {
        "decision_id": "dc_rbf_009",
        "capability": "research_benchmarking_framework",
        "question": "How should cost-aware evaluation be done?",
        "recommendation": "Include cost metrics alongside quality metrics in evaluation frameworks",
        "confidence_score": 0.72,
        "confidence_level": "medium",
        "provenance_refs": "patterns.md#L210-L233",
    },
    {
        "decision_id": "dc_rbf_010",
        "capability": "research_benchmarking_framework",
        "question": "How should reproducibility be packaged?",
        "recommendation": "Package experiments with all dependencies for full reproducibility",
        "confidence_score": 0.79,
        "confidence_level": "high",
        "provenance_refs": "patterns.md#L236-L258",
    },
]

DOMAIN_CARDS = {
    "security_architecture": (
        "dc_dom_sec",
        "What security architecture should be used?",
        "Defense-in-depth with threat modeling, isolation, and secrets management",
    ),
    "system_design_philosophy": (
        "dc_dom_sdp",
        "What system design philosophy to follow?",
        "Modular microservices with clear boundaries and event-driven communication",
    ),
    "governance_compliance": (
        "dc_dom_gov",
        "How to handle governance and compliance?",
        "Policy-as-code with automated enforcement and audit trails",
    ),
    "economic_optimization_modeling": (
        "dc_dom_eom",
        "How to optimize costs?",
        "Spot instances with fallback, right-sizing, and cost-aware scheduling",
    ),
    "agent_system_design": (
        "dc_dom_asd",
        "What agent system pattern to use?",
        "ReAct loop with tool augmentation and structured output",
    ),
    "distributed_orchestration": (
        "dc_dom_dor",
        "How to handle distributed orchestration?",
        "DAG-based execution with retry, checkpoint, and distributed coordination",
    ),
    "task_architecture": (
        "dc_dom_tar",
        "What task architecture to use?",
        "Hierarchical task decomposition with dependency resolution",
    ),
    "context_management": (
        "dc_dom_ctx",
        "How to manage context?",
        "Sliding window with semantic compression and priority-based retention",
    ),
    "knowledge_representation": (
        "dc_dom_kre",
        "How to represent knowledge?",
        "Hybrid graph + vector store with typed relationships",
    ),
    "memory_systems": (
        "dc_dom_mem",
        "What memory system to use?",
        "Tiered memory with working, episodic, and semantic layers",
    ),
    "reasoning_architecture": (
        "dc_dom_rea",
        "What reasoning architecture to apply?",
        "Chain-of-thought with verification and self-correction loops",
    ),
    "code_exploration": (
        "dc_dom_cex",
        "How to explore codebases?",
        "AST-based analysis with semantic search and dependency graphs",
    ),
    "refactoring_optimization": (
        "dc_dom_ref",
        "How to handle refactoring?",
        "Incremental refactoring with automated test verification",
    ),
    "specification_design": (
        "dc_dom_spe",
        "How to design specifications?",
        "Formal specs with property-based testing and contract verification",
    ),
    "testing_architecture": (
        "dc_dom_tst",
        "What testing architecture to use?",
        "Property-based testing with mutation testing and coverage-guided fuzzing",
    ),
    "cicd_devops": (
        "dc_dom_cic",
        "What CI/CD approach to take?",
        "Trunk-based development with feature flags and automated rollback",
    ),
    "observability_feedback_loops": (
        "dc_dom_obs",
        "How to implement observability?",
        "OpenTelemetry with distributed tracing and SLO-based alerting",
    ),
    "database_data_engineering": (
        "dc_dom_dde",
        "What database approach to use?",
        "Event-sourced with CQRS and materialized views",
    ),
    "infrastructure_engineering": (
        "dc_dom_inf",
        "What infrastructure approach?",
        "Infrastructure-as-code with immutable deployments",
    ),
    "human_in_the_loop_systems": (
        "dc_dom_hil",
        "How to handle human-in-the-loop?",
        "Async review queues with confidence-based escalation",
    ),
    "model_capability_management": (
        "dc_dom_mcm",
        "How to manage model capabilities?",
        "Capability matrix with version tracking and fallback chains",
    ),
    "ecosystem_intelligence": (
        "dc_dom_eco",
        "How to handle ecosystem intelligence?",
        "Dependency scanning with automated vulnerability assessment",
    ),
    "large_codebase_handling": (
        "dc_dom_lcb",
        "How to handle large codebases?",
        "Incremental analysis with caching and parallel processing",
    ),
    "autonomous_runtime_systems": (
        "dc_dom_ars",
        "What autonomous runtime pattern?",
        "Self-healing with circuit breakers and adaptive scaling",
    ),
    "system_self_improvement": (
        "dc_dom_ssi",
        "How should the system self-improve?",
        "Feedback-driven optimization with A/B testing and regression guards",
    ),
}


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent.parent
    settings = CorpusSettings(
        db_url=f"sqlite:///{repo_root / 'data' / 'corpus.db'}",
        chroma_dir=str(repo_root / "data" / "chroma"),
        graph_path=str(repo_root / "data" / "graph.json"),
    )
    settings.ensure_data_dirs()

    engine = create_db_engine(settings.db_url)
    applied = migrate_forward(engine)
    if applied:
        print(f"Applied migrations: {', '.join(applied)}")

    now = datetime.now(timezone.utc).isoformat()

    with get_session(engine) as session:
        repo = CorpusRepository(session)

        existing = {str(c.decision_id) for c in repo.list_decision_cards()}

        created = 0
        for dc in DECISIONS_FROM_INDEX:
            if dc["decision_id"] in existing:
                continue
            repo.create_decision_card(
                decision_id=dc["decision_id"],
                question=dc["question"],
                capability=dc["capability"],
                recommendation=dc["recommendation"],
                confidence_score=dc["confidence_score"],
                confidence_level=dc["confidence_level"],
                provenance_refs=dc["provenance_refs"],
                last_validated_at=now,
            )
            repo.create_capability_mapping(
                decision_id=dc["decision_id"],
                capability=dc["capability"],
                domain=SUBDOMAIN_TO_DOMAIN.get(dc["capability"], "09_research_discipline"),
            )
            created += 1

        for subdomain, (dc_id, question, recommendation) in DOMAIN_CARDS.items():
            if dc_id in existing:
                continue
            repo.create_decision_card(
                decision_id=dc_id,
                question=question,
                capability=subdomain,
                recommendation=recommendation,
                confidence_score=0.70,
                confidence_level="medium",
                provenance_refs=f"docs/research/*/{subdomain}/patterns.md",
                last_validated_at=now,
            )
            repo.create_capability_mapping(
                decision_id=dc_id,
                capability=subdomain,
                domain=SUBDOMAIN_TO_DOMAIN.get(subdomain, "unknown"),
            )
            created += 1

    print(f"Bootstrap complete: {created} decision cards created, {len(existing)} already existed.")
    print(f"Total: {created + len(existing)} cards")


if __name__ == "__main__":
    main()
