import uuid
from datetime import datetime, timezone
from pathlib import Path

from corpus.db.engine import create_db_engine, get_session
from corpus.db.migrations.runner import migrate_forward
from corpus.db.repository import CorpusRepository
from corpus.references.integrity_validator import validate_integrity


def _setup(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    migrate_forward(engine)


class TestIntegrityValidator:
    def test_all_links_valid_passes(self, tmp_path: Path, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"

        research = tmp_path / "docs" / "research"
        research.mkdir(parents=True)
        target = research / "target.md"
        target.write_text("# Target", encoding="utf-8")
        source = research / "source.md"
        source.write_text("[link](target.md)", encoding="utf-8")

        source_file = tmp_path / "test.md"
        source_file.write_text("content", encoding="utf-8")

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_run(
                run_id=run_id,
                source_branch="test",
                started_at=datetime.now(timezone.utc).isoformat(),
                status="running",
            )
            repo.create_artifact(
                artifact_id=f"art-{uuid.uuid4().hex[:8]}",
                title="Test",
                content="content",
                domain_tags="test",
                capability_tags="",
                source_branch="test",
                source_path="test.md",
                captured_at=datetime.now(timezone.utc).isoformat(),
                run_id=run_id,
            )

        with get_session(engine) as session:
            report = validate_integrity(session, run_id, str(tmp_path))

        assert report.passed is True
        assert len(report.broken_links) == 0

    def test_broken_link_fails(self, tmp_path: Path, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"

        research = tmp_path / "docs" / "research"
        research.mkdir(parents=True)
        source = research / "source.md"
        source.write_text("[link](nonexistent.md)", encoding="utf-8")

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_run(
                run_id=run_id,
                source_branch="test",
                started_at=datetime.now(timezone.utc).isoformat(),
                status="running",
            )

        with get_session(engine) as session:
            report = validate_integrity(session, run_id, str(tmp_path))

        assert report.passed is False
        assert len(report.broken_links) >= 1

    def test_stale_source_path_detected(self, tmp_path: Path, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_run(
                run_id=run_id,
                source_branch="test",
                started_at=datetime.now(timezone.utc).isoformat(),
                status="running",
            )
            repo.create_artifact(
                artifact_id=f"art-{uuid.uuid4().hex[:8]}",
                title="Test",
                content="content",
                domain_tags="test",
                capability_tags="",
                source_branch="test",
                source_path="deleted_file.md",
                captured_at=datetime.now(timezone.utc).isoformat(),
                run_id=run_id,
            )

        with get_session(engine) as session:
            report = validate_integrity(session, run_id, str(tmp_path))

        assert report.passed is False
        assert "deleted_file.md" in report.stale_paths
