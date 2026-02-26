import json

import pytest
from sqlalchemy.exc import IntegrityError

from corpus.db.engine import create_db_engine, make_session_factory
from corpus.db.models import Base
from corpus.db.repository import CorpusRepository


@pytest.fixture()
def repo(tmp_db_url: str):  # type: ignore[no-untyped-def]
    engine = create_db_engine(tmp_db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    yield CorpusRepository(session)
    session.close()


def test_create_and_get_run(repo: CorpusRepository) -> None:
    run = repo.create_run(
        run_id="cr_test_001",
        source_branch="test-branch",
        started_at="2026-01-01T00:00:00",
        status="pending",
    )
    assert run.run_id == "cr_test_001"

    fetched = repo.get_run("cr_test_001")
    assert fetched is not None
    assert fetched.source_branch == "test-branch"
    assert fetched.status == "pending"


def test_create_artifact_with_valid_fk(repo: CorpusRepository) -> None:
    repo.create_run(
        run_id="cr_art_test",
        source_branch="test-branch",
        started_at="2026-01-01T00:00:00",
        status="pending",
    )
    artifact = repo.create_artifact(
        artifact_id="ra_test_001",
        title="Test Artifact",
        content="some content",
        domain_tags=json.dumps(["security"]),
        capability_tags=json.dumps(["auth"]),
        source_branch="test-branch",
        source_path="docs/research/01/patterns.md",
        captured_at="2026-01-01T00:00:00",
        run_id="cr_art_test",
        status="active",
    )
    assert artifact.artifact_id == "ra_test_001"

    fetched = repo.get_artifact("ra_test_001")
    assert fetched is not None
    assert fetched.title == "Test Artifact"


def test_create_artifact_with_invalid_fk_raises(repo: CorpusRepository) -> None:
    with pytest.raises(IntegrityError):
        repo.create_artifact(
            artifact_id="ra_bad_fk",
            title="Bad FK",
            content="content",
            domain_tags=json.dumps(["test"]),
            capability_tags=json.dumps(["cap"]),
            source_branch="test-branch",
            source_path="test/path.md",
            captured_at="2026-01-01T00:00:00",
            run_id="nonexistent",
            status="active",
        )


def test_list_runs_by_status(repo: CorpusRepository) -> None:
    repo.create_run(run_id="cr_a", source_branch="a", started_at="2026-01-01T00:00:00", status="pending")
    repo.create_run(run_id="cr_b", source_branch="b", started_at="2026-01-01T00:00:00", status="running")
    repo.create_run(run_id="cr_c", source_branch="c", started_at="2026-01-01T00:00:00", status="pending")

    pending = repo.list_runs(status="pending")
    assert len(pending) == 2
    assert all(r.status == "pending" for r in pending)


def test_update_run_status(repo: CorpusRepository) -> None:
    repo.create_run(run_id="cr_upd", source_branch="x", started_at="2026-01-01T00:00:00", status="pending")
    updated = repo.update_run_status("cr_upd", "completed")
    assert updated is not None
    assert updated.status == "completed"
    assert updated.completed_at is not None


def test_create_and_get_decision_card(repo: CorpusRepository) -> None:
    card = repo.create_decision_card(
        decision_id="dc_test_001",
        question="Which framework?",
        capability="testing",
        recommendation=json.dumps({"summary": "Use pytest"}),
        confidence_score=0.85,
        confidence_level="high",
        provenance_refs=json.dumps(["ra_test_001"]),
        last_validated_at="2026-01-01T00:00:00",
        status="active",
    )
    assert card.decision_id == "dc_test_001"

    fetched = repo.get_decision_card("dc_test_001")
    assert fetched is not None
    assert fetched.question == "Which framework?"
    assert fetched.confidence_score == 0.85
