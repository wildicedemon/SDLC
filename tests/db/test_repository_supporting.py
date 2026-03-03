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
    r = CorpusRepository(session)
    r.create_run(run_id="cr_sup", source_branch="main", started_at="2026-01-01T00:00:00", status="pending")
    r.create_artifact(
        artifact_id="ra_sup_a",
        title="A",
        content="a",
        domain_tags=json.dumps(["d"]),
        capability_tags=json.dumps(["c"]),
        source_branch="main",
        source_path="a.md",
        captured_at="2026-01-01T00:00:00",
        run_id="cr_sup",
        status="active",
    )
    r.create_artifact(
        artifact_id="ra_sup_b",
        title="B",
        content="b",
        domain_tags=json.dumps(["d"]),
        capability_tags=json.dumps(["c"]),
        source_branch="main",
        source_path="b.md",
        captured_at="2026-01-01T00:00:00",
        run_id="cr_sup",
        status="active",
    )
    r.create_decision_card(
        decision_id="dc_sup_001",
        question="Q?",
        capability="cap",
        recommendation=json.dumps({"summary": "R"}),
        confidence_score=0.8,
        confidence_level="high",
        provenance_refs=json.dumps(["ra_sup_a"]),
        last_validated_at="2026-01-01T00:00:00",
        status="active",
    )
    yield r
    session.close()


def test_chunk_unique_constraint(repo: CorpusRepository) -> None:
    repo.create_chunk(chunk_id="c1", artifact_id="ra_sup_a", chunk_index=0, content="x")
    with pytest.raises(IntegrityError):
        repo.create_chunk(chunk_id="c2", artifact_id="ra_sup_a", chunk_index=0, content="y")


def test_create_drift_event(repo: CorpusRepository) -> None:
    event = repo.create_drift_event(
        event_id="de_001",
        decision_id="dc_sup_001",
        trigger="confidence_drop",
        confidence_delta=-0.15,
        status="pending_revalidation",
        run_id="cr_sup",
        created_at="2026-01-01T00:00:00",
    )
    assert event.event_id == "de_001"
    fetched = repo.get_drift_event("de_001")
    assert fetched is not None
    assert fetched.trigger == "confidence_drop"


def test_review_queue_lifecycle(repo: CorpusRepository) -> None:
    item = repo.create_review_item(
        run_id="cr_sup",
        item_type="dedup_arbitration",
        artifact_a_id="ra_sup_a",
        artifact_b_id="ra_sup_b",
        ai_confidence=0.55,
        ai_recommendation="merge",
    )
    unresolved = repo.list_unresolved_reviews("cr_sup")
    assert len(unresolved) == 1

    repo.resolve_review(item.id, "approved_merge")
    unresolved = repo.list_unresolved_reviews("cr_sup")
    assert len(unresolved) == 0


def test_capability_mapping_unique(repo: CorpusRepository) -> None:
    repo.create_capability_mapping(capability="auth", decision_id="dc_sup_001", domain="security")
    with pytest.raises(IntegrityError):
        repo.create_capability_mapping(capability="auth", decision_id="dc_sup_001", domain="security")


def test_telemetry_outcome_lifecycle(repo: CorpusRepository) -> None:
    repo.create_telemetry_outcome(decision_id="dc_sup_001", timestamp="2026-01-01T00:00:00", outcome="success")
    repo.create_telemetry_outcome(decision_id="dc_sup_001", timestamp="2026-01-02T00:00:00", outcome="failure")
    outcomes = repo.list_outcomes("dc_sup_001")
    assert len(outcomes) == 2


def test_rewrite_and_integrity_entries(repo: CorpusRepository) -> None:
    rw = repo.create_rewrite_map_entry(run_id="cr_sup", old_path="old.md", new_path="new.md")
    assert rw.old_path == "old.md"

    ir = repo.create_integrity_report_entry(
        run_id="cr_sup",
        check_type="internal_link",
        target_path="docs/ref.md",
        resolved=True,
    )
    assert ir.resolved is True
