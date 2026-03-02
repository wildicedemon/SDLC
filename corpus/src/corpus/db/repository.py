from datetime import datetime, timezone

from sqlalchemy.orm import Session

from corpus.db.models import (
    ArtifactChunk,
    CapabilityMapping,
    ConsolidationRun,
    DecisionCard,
    DriftEvent,
    HumanReviewQueue,
    ReferenceIntegrityReport,
    ReferenceRewriteMap,
    ResearchArtifact,
    TelemetryOutcome,
)


class CorpusRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_run(self, **kwargs: object) -> ConsolidationRun:
        run = ConsolidationRun(**kwargs)
        self.session.add(run)
        self.session.flush()
        return run

    def get_run(self, run_id: str) -> ConsolidationRun | None:
        return self.session.get(ConsolidationRun, run_id)

    def list_runs(self, status: str | None = None) -> list[ConsolidationRun]:
        q = self.session.query(ConsolidationRun)
        if status is not None:
            q = q.filter(ConsolidationRun.status == status)
        return list(q.all())

    def update_run_status(self, run_id: str, status: str) -> ConsolidationRun | None:
        run = self.get_run(run_id)
        if run is None:
            return None
        run.status = status  # type: ignore[assignment]
        if status == "completed":
            run.completed_at = datetime.now(timezone.utc).isoformat()  # type: ignore[assignment]
        self.session.flush()
        return run

    def create_artifact(self, **kwargs: object) -> ResearchArtifact:
        artifact = ResearchArtifact(**kwargs)
        self.session.add(artifact)
        self.session.flush()
        return artifact

    def get_artifact(self, artifact_id: str) -> ResearchArtifact | None:
        return self.session.get(ResearchArtifact, artifact_id)

    def list_artifacts(self, run_id: str | None = None) -> list[ResearchArtifact]:
        q = self.session.query(ResearchArtifact)
        if run_id is not None:
            q = q.filter(ResearchArtifact.run_id == run_id)
        return list(q.all())

    def create_decision_card(self, **kwargs: object) -> DecisionCard:
        card = DecisionCard(**kwargs)
        self.session.add(card)
        self.session.flush()
        return card

    def get_decision_card(self, decision_id: str) -> DecisionCard | None:
        return self.session.get(DecisionCard, decision_id)

    def list_decision_cards(self, status: str | None = None) -> list[DecisionCard]:
        q = self.session.query(DecisionCard)
        if status is not None:
            q = q.filter(DecisionCard.status == status)
        return list(q.all())

    def create_chunk(self, **kwargs: object) -> ArtifactChunk:
        chunk = ArtifactChunk(**kwargs)
        self.session.add(chunk)
        self.session.flush()
        return chunk

    def get_chunk(self, chunk_id: str) -> ArtifactChunk | None:
        return self.session.get(ArtifactChunk, chunk_id)

    def list_chunks(self, artifact_id: str | None = None) -> list[ArtifactChunk]:
        q = self.session.query(ArtifactChunk)
        if artifact_id is not None:
            q = q.filter(ArtifactChunk.artifact_id == artifact_id)
        return list(q.all())

    def create_drift_event(self, **kwargs: object) -> DriftEvent:
        event = DriftEvent(**kwargs)
        self.session.add(event)
        self.session.flush()
        return event

    def get_drift_event(self, event_id: str) -> DriftEvent | None:
        return self.session.get(DriftEvent, event_id)

    def create_rewrite_map_entry(self, **kwargs: object) -> ReferenceRewriteMap:
        entry = ReferenceRewriteMap(**kwargs)
        self.session.add(entry)
        self.session.flush()
        return entry

    def create_integrity_report_entry(self, **kwargs: object) -> ReferenceIntegrityReport:
        entry = ReferenceIntegrityReport(**kwargs)
        self.session.add(entry)
        self.session.flush()
        return entry

    def create_review_item(self, **kwargs: object) -> HumanReviewQueue:
        item = HumanReviewQueue(**kwargs)
        self.session.add(item)
        self.session.flush()
        return item

    def list_unresolved_reviews(self, run_id: str) -> list[HumanReviewQueue]:
        return list(
            self.session.query(HumanReviewQueue)
            .filter(HumanReviewQueue.run_id == run_id, HumanReviewQueue.disposition.is_(None))
            .all()
        )

    def resolve_review(self, item_id: int, disposition: str, resolved_by: str = "system") -> HumanReviewQueue | None:
        item = self.session.get(HumanReviewQueue, item_id)
        if item is None:
            return None
        item.disposition = disposition  # type: ignore[assignment]
        item.resolved_at = datetime.now(timezone.utc).isoformat()  # type: ignore[assignment]
        item.resolved_by = resolved_by  # type: ignore[assignment]
        self.session.flush()
        return item

    def create_capability_mapping(self, **kwargs: object) -> CapabilityMapping:
        mapping = CapabilityMapping(**kwargs)
        self.session.add(mapping)
        self.session.flush()
        return mapping

    def list_capability_mappings(self, capability: str | None = None) -> list[CapabilityMapping]:
        q = self.session.query(CapabilityMapping)
        if capability is not None:
            q = q.filter(CapabilityMapping.capability == capability)
        return list(q.all())

    def create_telemetry_outcome(self, **kwargs: object) -> TelemetryOutcome:
        outcome = TelemetryOutcome(**kwargs)
        self.session.add(outcome)
        self.session.flush()
        return outcome

    def list_outcomes(self, decision_id: str) -> list[TelemetryOutcome]:
        return list(self.session.query(TelemetryOutcome).filter(TelemetryOutcome.decision_id == decision_id).all())
