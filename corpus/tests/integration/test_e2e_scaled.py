from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pytest
from git import Repo

from corpus.config import CorpusSettings
from corpus.consolidation.run_controller import complete_run
from corpus.db.engine import create_db_engine, get_session
from corpus.db.migrations.runner import migrate_forward
from corpus.db.repository import CorpusRepository
from corpus.decisions.card_updater import update_impacted_cards
from corpus.decisions.drift_detector import detect_drift
from corpus.decisions.index_updater import update_indices
from corpus.dedup.arbitrator import ArbitrationResult
from corpus.dedup.embeddings import Disagreement
from corpus.dedup.pipeline import run_dedup
from corpus.ingestion.pipeline import run_ingest
from corpus.references.integrity_validator import validate_integrity
from corpus.references.rewrite_mapper import generate_rewrite_map
from corpus.references.rewriter import rewrite_references
from corpus.retrieval.orchestrator import query as corpus_query
from corpus.sync.graph_sync import sync_graph
from corpus.sync.health_checker import check_sync_health
from corpus.sync.vector_sync import sync_vectors
from corpus.telemetry.metrics import compute_metrics


def _mock_embed(texts: list[str]) -> list[list[float]]:
    return [(np.ones(384, dtype=np.float32) * 0.5).tolist() for _ in texts]


def _mock_arbitrate(disagreements: list[Disagreement]) -> list[ArbitrationResult]:
    return [
        ArbitrationResult(
            chunk_a_id=d.chunk_a_id,
            chunk_b_id=d.chunk_b_id,
            confidence=0.50,
            recommendation="keep_both",
        )
        for d in disagreements
    ]


DOMAINS = {
    "01_meta_architecture": [
        ("security_architecture", "dc-sec", "How to secure?", "Use TLS"),
        ("system_design_philosophy", "dc-design", "Design approach?", "Microservices"),
        ("governance_compliance", "dc-gov", "Governance approach?", "Policy engine"),
        ("economic_optimization_modeling", "dc-econ", "Cost optimization?", "Spot instances"),
    ],
    "02_agent_orchestration": [
        ("agent_system_design", "dc-agent", "Agent pattern?", "ReAct loop"),
        ("task_architecture", "dc-task", "Task design?", "DAG execution"),
    ],
    "05_sdlc_automation": [
        ("testing_architecture", "dc-test", "Testing?", "Property-based tests"),
        ("cicd_devops", "dc-cicd", "CI/CD?", "Trunk-based dev"),
    ],
    "09_research_discipline": [
        ("research_benchmarking_framework", "dc-bench", "Benchmarking?", "A/B testing"),
    ],
    "03_context_memory_intelligence": [
        ("context_management", "dc-ctx", "Context approach?", "Sliding window"),
    ],
}


def _create_branch_artifacts(
    repo_dir: Path,
    git_repo: Repo,
    branch_name: str,
    top_dir: str,
    subdomains: list[str],
    contradict_subdomain: str | None = None,
) -> None:
    git_repo.create_head(branch_name)
    git_repo.heads[branch_name].checkout()

    for sd in subdomains:
        sd_dir = repo_dir / "docs" / "research" / top_dir / sd
        sd_dir.mkdir(parents=True, exist_ok=True)
        (sd_dir / "overview.md").write_text(
            f"# {sd.replace('_', ' ').title()}\n\nContent for {sd} from branch {branch_name}.\n"
        )

    if contradict_subdomain:
        c_dir = repo_dir / "docs" / "research" / top_dir / contradict_subdomain
        c_dir.mkdir(parents=True, exist_ok=True)
        (c_dir / "patterns.md").write_text(
            f"# {contradict_subdomain}\n\nThis contradicts existing {contradict_subdomain} recommendations.\n"
        )

    git_repo.index.add([str(p) for p in (repo_dir / "docs").rglob("*.md")])
    git_repo.index.commit(f"artifacts for {branch_name}")


def _run_pipeline(
    engine: object,
    repo_dir: Path,
    branch: str,
    settings: CorpusSettings,
) -> str:
    with get_session(engine) as session:
        repo = CorpusRepository(session)
        result = run_ingest(repo, str(repo_dir), branch, "main", corpus_root=str(repo_dir))
    assert not result.failed, f"Ingest failed: {result.unclassified_files}"
    run_id = result.run_id

    with get_session(engine) as session:
        run_dedup(session, run_id, settings=settings, embed_fn=_mock_embed, arbitrate_fn=_mock_arbitrate)

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        all_cards = repo.list_decision_cards()
        prev_scores = {str(c.decision_id): float(c.confidence_score) for c in all_cards}
        updated_ids = update_impacted_cards(session, run_id)
        update_indices(session, updated_ids)
        detect_drift(session, run_id, prev_scores)

    with get_session(engine) as session:
        rmap = generate_rewrite_map(session, run_id)
        rewrite_references(rmap, str(repo_dir))
        validate_integrity(session, run_id, str(repo_dir))

    with get_session(engine) as session:
        sync_vectors(session, run_id, settings=settings)

    with get_session(engine) as session:
        sync_graph(session, run_id, settings=settings)

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        reviews = repo.list_unresolved_reviews(run_id)
        for r in reviews:
            r.disposition = "accepted"
            r.resolved_by = "test-automation"
        session.flush()

    with get_session(engine) as session:
        passed = complete_run(session, run_id, corpus_root=str(repo_dir), settings=settings)
    assert passed, f"Run {run_id} failed gates"

    return run_id


@pytest.fixture()
def scaled_env(tmp_path: Path) -> tuple[Path, str, CorpusSettings]:
    repo_dir = tmp_path / "repo"
    repo_dir.mkdir()
    git_repo = Repo.init(str(repo_dir))
    git_repo.config_writer().set_value("user", "name", "Test").release()
    git_repo.config_writer().set_value("user", "email", "test@test.com").release()

    readme = repo_dir / "README.md"
    readme.write_text("# Root")
    git_repo.index.add([str(readme)])
    git_repo.index.commit("init")
    git_repo.create_head("main")

    db_path = tmp_path / "data" / "corpus.db"
    db_path.parent.mkdir(parents=True)
    chroma_dir = tmp_path / "data" / "chroma"
    chroma_dir.mkdir(parents=True)
    graph_path = tmp_path / "data" / "graph.json"
    db_url = f"sqlite:///{db_path}"

    settings = CorpusSettings(
        db_url=db_url,
        chroma_dir=str(chroma_dir),
        graph_path=str(graph_path),
        kilo_api_key="test",
    )

    engine = create_db_engine(db_url)
    migrate_forward(engine)

    now = datetime.now(timezone.utc).isoformat()
    with get_session(engine) as session:
        repo = CorpusRepository(session)
        for _top_dir, subdomain_list in DOMAINS.items():
            for sd_name, dc_id, question, rec in subdomain_list:
                repo.create_decision_card(
                    decision_id=dc_id,
                    question=question,
                    capability=sd_name,
                    recommendation=rec,
                    confidence_score=0.75,
                    confidence_level="high",
                    provenance_refs=f"ref-{dc_id}",
                    last_validated_at=now,
                )

    return repo_dir, db_url, settings


def test_e2e_scaled(scaled_env: tuple[Path, str, CorpusSettings]) -> None:
    repo_dir, db_url, settings = scaled_env
    engine = create_db_engine(db_url)
    git_repo = Repo(str(repo_dir))

    _create_branch_artifacts(
        repo_dir,
        git_repo,
        "feature/branch-1",
        "01_meta_architecture",
        ["security_architecture", "system_design_philosophy"],
        contradict_subdomain="governance_compliance",
    )
    git_repo.git.add(A=True)
    git_repo.index.commit("stash changes")
    git_repo.heads["main"].checkout()

    _create_branch_artifacts(
        repo_dir,
        git_repo,
        "feature/branch-2",
        "02_agent_orchestration",
        ["agent_system_design", "task_architecture"],
    )
    git_repo.git.add(A=True)
    git_repo.index.commit("stash changes")
    git_repo.heads["main"].checkout()

    _create_branch_artifacts(
        repo_dir,
        git_repo,
        "feature/branch-3",
        "09_research_discipline",
        ["research_benchmarking_framework"],
    )
    git_repo.git.add(A=True)
    git_repo.index.commit("stash changes")
    git_repo.heads["main"].checkout()

    run_ids = []
    for branch in ["feature/branch-1", "feature/branch-2", "feature/branch-3"]:
        run_id = _run_pipeline(engine, repo_dir, branch, settings)
        run_ids.append(run_id)

    assert len(run_ids) == 3

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        for rid in run_ids:
            run = repo.get_run(rid)
            assert str(run.status) == "completed", f"Run {rid} status={run.status}"

    with get_session(engine) as session:
        health = check_sync_health(session, settings=settings)
    assert health.healthy

    with get_session(engine) as session:
        response = corpus_query(session, "research_benchmarking_framework", settings=settings)
    assert response.content
    assert response.provenance

    with get_session(engine) as session:
        m = compute_metrics(session)
    assert m.total_runs >= 3
    assert m.completed_runs >= 3
    assert m.total_artifacts >= 3
    assert m.total_decisions >= 10
