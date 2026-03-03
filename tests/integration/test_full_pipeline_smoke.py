import json
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
from corpus.sync.graph_sync import sync_graph
from corpus.sync.vector_sync import sync_vectors


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


@pytest.fixture()
def full_env(tmp_path: Path) -> tuple[Path, str, str, CorpusSettings]:
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

    branch = "feature/full-pipeline"
    git_repo.create_head(branch)
    git_repo.heads[branch].checkout()

    sec_dir = repo_dir / "docs" / "research" / "01_meta_architecture" / "security_architecture"
    sec_dir.mkdir(parents=True)
    (sec_dir / "patterns.md").write_text("# Security Patterns\n\n## Pattern A\nDetailed unique security content.\n")
    (sec_dir / "comparisons.md").write_text("# Security Patterns\n\n## Pattern A\nDetailed unique security content.\n")

    design_dir = repo_dir / "docs" / "research" / "01_meta_architecture" / "system_design_philosophy"
    design_dir.mkdir(parents=True)
    (design_dir / "overview.md").write_text("# System Design\n\n## Approach\nNovel design philosophy content.\n")
    (design_dir / "references.md").write_text("# Novel Design Ideas\n\n## Idea A\nBrand new content for design.\n")

    contradict_dir = repo_dir / "docs" / "research" / "05_sdlc_automation" / "testing_architecture"
    contradict_dir.mkdir(parents=True)
    (contradict_dir / "overview.md").write_text(
        "# Testing Contradiction\n\nThis document explicitly contradicts the existing testing recommendation.\n"
    )

    git_repo.index.add(
        [
            str(sec_dir / "patterns.md"),
            str(sec_dir / "comparisons.md"),
            str(design_dir / "overview.md"),
            str(design_dir / "references.md"),
            str(contradict_dir / "overview.md"),
        ]
    )
    git_repo.index.commit("add artifacts")

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

    return repo_dir, branch, db_url, settings


def test_full_pipeline_smoke(full_env: tuple[Path, str, str, CorpusSettings]) -> None:
    repo_dir, branch, db_url, settings = full_env
    engine = create_db_engine(db_url)
    migrate_forward(engine)

    now = datetime.now(timezone.utc).isoformat()
    with get_session(engine) as session:
        repo = CorpusRepository(session)
        repo.create_decision_card(
            decision_id="dc-sec",
            question="How to secure?",
            capability="security_architecture",
            recommendation="Use TLS everywhere",
            confidence_score=0.7,
            confidence_level="medium",
            provenance_refs="ref1",
            last_validated_at=now,
        )
        repo.create_decision_card(
            decision_id="dc-design",
            question="Design approach?",
            capability="system_design_philosophy",
            recommendation="Use microservices",
            confidence_score=0.8,
            confidence_level="high",
            provenance_refs="ref2",
            last_validated_at=now,
        )
        repo.create_decision_card(
            decision_id="dc-testing",
            question="Testing approach?",
            capability="testing_architecture",
            recommendation="Use integration tests",
            confidence_score=0.75,
            confidence_level="high",
            provenance_refs="ref3",
            last_validated_at=now,
        )

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        ingest_result = run_ingest(repo, str(repo_dir), branch, "main", corpus_root=str(repo_dir))

    assert not ingest_result.failed
    assert ingest_result.artifacts_ingested >= 5
    run_id = ingest_result.run_id

    with get_session(engine) as session:
        dedup_report = run_dedup(
            session,
            run_id,
            settings=settings,
            embed_fn=_mock_embed,
            arbitrate_fn=_mock_arbitrate,
        )
    assert dedup_report.candidate_count >= 0

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        all_cards = repo.list_decision_cards()
        prev_scores = {str(c.decision_id): float(c.confidence_score) for c in all_cards}
        updated_ids = update_impacted_cards(session, run_id)
        update_indices(session, updated_ids)
        drift_ids = detect_drift(session, run_id, prev_scores)

    assert len(updated_ids) >= 1

    drift_events = drift_ids
    assert len(drift_events) >= 1, "Expected at least 1 drift event from contradiction"

    with get_session(engine) as session:
        rmap = generate_rewrite_map(session, run_id)
        rewrite_references(rmap, str(repo_dir))
        integrity = validate_integrity(session, run_id, str(repo_dir))
    assert integrity.passed

    with get_session(engine) as session:
        vsync = sync_vectors(session, run_id, settings=settings)
    assert vsync.synced >= 1

    with get_session(engine) as session:
        gsync = sync_graph(session, run_id, settings=settings)
    assert gsync.nodes_added >= 1

    graph_path = Path(settings.graph_path)
    assert graph_path.exists()
    graph_data = json.loads(graph_path.read_text(encoding="utf-8"))
    import networkx as nx

    G = nx.node_link_graph(graph_data)
    assert G.number_of_nodes() >= 4
    assert G.number_of_edges() >= 1

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        reviews = repo.list_unresolved_reviews(run_id)
        for r in reviews:
            r.disposition = "accepted"
            r.resolved_by = "test-automation"
        session.flush()

    with get_session(engine) as session:
        passed = complete_run(session, run_id, corpus_root=str(repo_dir), settings=settings)
    assert passed, "Expected all gates to pass after resolving reviews"

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        run = repo.get_run(run_id)
        assert str(run.status) == "completed"
        assert run.completed_at is not None

    with get_session(engine) as session:
        from corpus.retrieval.orchestrator import query

        response = query(session, "security_architecture", settings=settings)
    assert response.content
    assert response.provenance

    from corpus.consolidation.branch_retirement import retire_branch

    git_repo = Repo(str(repo_dir))
    git_repo.git.add(A=True)
    git_repo.index.commit("pre-retirement commit")
    git_repo.heads["main"].checkout()

    with get_session(engine) as session:
        retire_branch(session, run_id, action="archived", repo_path=str(repo_dir))

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        run = repo.get_run(run_id)
        assert str(run.retirement_action) == "archived"

    assert f"archive/{branch}" in [t.name for t in git_repo.tags]
