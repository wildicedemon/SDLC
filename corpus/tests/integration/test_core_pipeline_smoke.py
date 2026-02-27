from datetime import datetime, timezone
from pathlib import Path

import pytest
from git import Repo

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


@pytest.fixture()
def pipeline_env(tmp_path: Path) -> tuple[Path, str, str]:
    repo_dir = tmp_path / "repo"
    repo_dir.mkdir()
    repo = Repo.init(str(repo_dir))
    repo.config_writer().set_value("user", "name", "Test").release()
    repo.config_writer().set_value("user", "email", "test@test.com").release()

    readme = repo_dir / "README.md"
    readme.write_text("# Root")
    repo.index.add([str(readme)])
    repo.index.commit("init")
    repo.create_head("main")

    branch = "feature/pipeline-smoke"
    repo.create_head(branch)
    repo.heads[branch].checkout()

    sec_dir = repo_dir / "docs" / "research" / "01_meta_architecture" / "security_architecture"
    sec_dir.mkdir(parents=True)
    (sec_dir / "patterns.md").write_text(
        "# Security Patterns\n\n## Pattern A\nDetailed pattern A content for security.\n"
    )
    (sec_dir / "near_dup.md").write_text(
        "# Security Patterns\n\n## Pattern A\nDetailed pattern A content for security.\n"
    )

    design_dir = repo_dir / "docs" / "research" / "01_meta_architecture" / "system_design_philosophy"
    design_dir.mkdir(parents=True)
    (design_dir / "overview.md").write_text("# System Design\n\n## Approach\nSystem design content.\n")

    repo.index.add(
        [
            str(sec_dir / "patterns.md"),
            str(sec_dir / "near_dup.md"),
            str(design_dir / "overview.md"),
        ]
    )
    repo.index.commit("add artifacts")

    db_path = tmp_path / "data" / "corpus.db"
    db_path.parent.mkdir(parents=True)
    db_url = f"sqlite:///{db_path}"

    return repo_dir, branch, db_url


def _mock_embed(texts: list[str]) -> list[list[float]]:
    import numpy as np

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


def test_core_pipeline_smoke(pipeline_env: tuple[Path, str, str]) -> None:
    repo_dir, branch, db_url = pipeline_env
    engine = create_db_engine(db_url)
    migrate_forward(engine)

    from corpus.config import CorpusSettings

    settings = CorpusSettings(db_url=db_url, kilo_api_key="test")

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        repo.create_decision_card(
            decision_id="dc-sec",
            question="How to secure?",
            capability="security_architecture",
            recommendation="Use TLS",
            confidence_score=0.7,
            confidence_level="medium",
            provenance_refs="ref1",
            last_validated_at=datetime.now(timezone.utc).isoformat(),
        )
        repo.create_decision_card(
            decision_id="dc-design",
            question="Design approach?",
            capability="system_design_philosophy",
            recommendation="Use microservices",
            confidence_score=0.8,
            confidence_level="high",
            provenance_refs="ref2",
            last_validated_at=datetime.now(timezone.utc).isoformat(),
        )

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        ingest_result = run_ingest(repo, str(repo_dir), branch, "main", corpus_root=str(repo_dir))

    assert not ingest_result.failed
    assert ingest_result.artifacts_ingested >= 3
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
        detect_drift(session, run_id, prev_scores)

    assert len(updated_ids) >= 1

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        reviews = repo.list_unresolved_reviews(run_id)
        if dedup_report.human_queued > 0:
            assert len(reviews) >= 1
