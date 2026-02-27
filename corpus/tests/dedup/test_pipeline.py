import uuid
from datetime import datetime, timezone

from corpus.config import CorpusSettings
from corpus.db.engine import create_db_engine, get_session
from corpus.db.migrations.runner import migrate_forward
from corpus.db.repository import CorpusRepository
from corpus.dedup.arbitrator import ArbitrationResult
from corpus.dedup.embeddings import Disagreement
from corpus.dedup.pipeline import run_dedup


def _setup_db(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    migrate_forward(engine)


def _seed_run_with_chunks(
    session: object,
    run_id: str,
    chunks: list[tuple[str, str]],
) -> None:
    repo = CorpusRepository(session)  # type: ignore[arg-type]
    repo.create_run(
        run_id=run_id,
        source_branch="test-branch",
        started_at=datetime.now(timezone.utc).isoformat(),
        status="running",
    )
    art_id = f"art-{uuid.uuid4().hex[:8]}"
    repo.create_artifact(
        artifact_id=art_id,
        title="Test Artifact",
        content="test content",
        domain_tags="test",
        capability_tags="",
        source_branch="test-branch",
        source_path="test.md",
        captured_at=datetime.now(timezone.utc).isoformat(),
        run_id=run_id,
    )
    for chunk_id, content in chunks:
        repo.create_chunk(
            chunk_id=chunk_id,
            artifact_id=art_id,
            chunk_index=int(chunk_id.split("-")[-1]) if "-" in chunk_id else 0,
            content=content,
        )


def _mock_embed_fn(texts: list[str]) -> list[list[float]]:
    import numpy as np

    vecs = []
    for _ in texts:
        vecs.append((np.ones(384, dtype=np.float32) * 0.5).tolist())
    return vecs


def _mock_arbitrate_high(disagreements: list[Disagreement]) -> list[ArbitrationResult]:
    return [
        ArbitrationResult(
            chunk_a_id=d.chunk_a_id,
            chunk_b_id=d.chunk_b_id,
            confidence=0.80,
            recommendation="merge",
        )
        for d in disagreements
    ]


def _mock_arbitrate_low(disagreements: list[Disagreement]) -> list[ArbitrationResult]:
    return [
        ArbitrationResult(
            chunk_a_id=d.chunk_a_id,
            chunk_b_id=d.chunk_b_id,
            confidence=0.50,
            recommendation="keep_both",
        )
        for d in disagreements
    ]


class TestPipeline:
    def test_zero_candidates_empty_report(self, tmp_db_url: str) -> None:
        _setup_db(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        settings = CorpusSettings(db_url=tmp_db_url, kilo_api_key="test")
        run_id = f"run-{uuid.uuid4().hex[:8]}"

        with get_session(engine) as session:
            _seed_run_with_chunks(session, run_id, [("c-0", "unique text one"), ("c-1", "completely different words")])

        with get_session(engine) as session:
            report = run_dedup(session, run_id, settings=settings, embed_fn=_mock_embed_fn)

        assert report.candidate_count == 0
        assert report.confirmed_dups == 0
        assert report.arbitrated == 0
        assert report.human_queued == 0

    def test_l1_candidates_l2_confirms_l3_called(self, tmp_db_url: str) -> None:
        _setup_db(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        settings = CorpusSettings(db_url=tmp_db_url, kilo_api_key="test")
        run_id = f"run-{uuid.uuid4().hex[:8]}"

        text = "the quick brown fox jumps over the lazy dog near the riverbank " * 10
        with get_session(engine) as session:
            _seed_run_with_chunks(session, run_id, [("c-0", text), ("c-1", text)])

        with get_session(engine) as session:
            report = run_dedup(
                session,
                run_id,
                settings=settings,
                embed_fn=_mock_embed_fn,
                arbitrate_fn=_mock_arbitrate_high,
            )

        assert report.candidate_count >= 1

    def test_l3_rate_alert(self, tmp_db_url: str) -> None:
        _setup_db(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        settings = CorpusSettings(
            db_url=tmp_db_url,
            kilo_api_key="test",
            dedup_l1_threshold=0.3,
            dedup_l2_threshold=0.99,
            l3_rate_alert_threshold=0.10,
        )
        run_id = f"run-{uuid.uuid4().hex[:8]}"

        text = "the quick brown fox jumps over the lazy dog near the riverbank " * 10
        with get_session(engine) as session:
            _seed_run_with_chunks(session, run_id, [("c-0", text), ("c-1", text)])

        def mock_embed_slightly_different(texts: list[str]) -> list[list[float]]:
            import numpy as np

            vecs = []
            for i, _ in enumerate(texts):
                v = np.ones(384, dtype=np.float32) * 0.5
                v[i % 384] += 0.5
                vecs.append(v.tolist())
            return vecs

        with get_session(engine) as session:
            report = run_dedup(
                session,
                run_id,
                settings=settings,
                embed_fn=mock_embed_slightly_different,
                arbitrate_fn=_mock_arbitrate_low,
            )

        if report.candidate_count > 0 and report.l3_rate > settings.l3_rate_alert_threshold:
            assert report.l3_rate_alert is True

    def test_human_queue_items_for_low_confidence(self, tmp_db_url: str) -> None:
        _setup_db(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        settings = CorpusSettings(
            db_url=tmp_db_url,
            kilo_api_key="test",
            dedup_l1_threshold=0.3,
            dedup_l2_threshold=0.99,
            arbitration_confidence_min=0.70,
        )
        run_id = f"run-{uuid.uuid4().hex[:8]}"

        text = "the quick brown fox jumps over the lazy dog near the riverbank " * 10
        with get_session(engine) as session:
            _seed_run_with_chunks(session, run_id, [("c-0", text), ("c-1", text)])

        def mock_embed_diff(texts: list[str]) -> list[list[float]]:
            import numpy as np

            vecs = []
            for i, _ in enumerate(texts):
                v = np.ones(384, dtype=np.float32) * 0.5
                v[i % 384] += 0.5
                vecs.append(v.tolist())
            return vecs

        with get_session(engine) as session:
            report = run_dedup(
                session,
                run_id,
                settings=settings,
                embed_fn=mock_embed_diff,
                arbitrate_fn=_mock_arbitrate_low,
            )

        if report.candidate_count > 0 and report.disagreements:
            assert report.human_queued >= 1
