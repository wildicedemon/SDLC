"""CRUD repository for all corpus pipeline ORM models.

Provides a single :class:`CorpusRepository` that wraps a SQLAlchemy
:class:`~sqlalchemy.orm.Session` and exposes create / get / list /
update helpers for every model in the schema.  All mutating methods
call :meth:`Session.flush` (but **not** commit) so that callers can
compose multiple operations inside one transaction.
"""

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
    """Unified data-access layer for the corpus pipeline.

    All methods operate within the session passed at construction time.
    Callers are responsible for committing or rolling back the session.

    Attributes:
        session: The active SQLAlchemy session.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    # ------------------------------------------------------------------
    # ConsolidationRun helpers
    # ------------------------------------------------------------------

    def create_run(self, **kwargs: object) -> ConsolidationRun:
        """Insert a new :class:`ConsolidationRun`.

        Args:
            **kwargs: Column values forwarded to the model constructor.

        Returns:
            The newly created (and flushed) run instance.
        """
        run = ConsolidationRun(**kwargs)
        self.session.add(run)
        self.session.flush()
        return run

    def get_run(self, run_id: str) -> ConsolidationRun | None:
        """Fetch a single run by its primary key.

        Args:
            run_id: The run's unique identifier.

        Returns:
            The matching run, or ``None`` if not found.
        """
        return self.session.get(ConsolidationRun, run_id)

    def list_runs(self, status: str | None = None) -> list[ConsolidationRun]:
        """List consolidation runs, optionally filtered by status.

        Args:
            status: If provided, only return runs with this status.

        Returns:
            A list of matching :class:`ConsolidationRun` instances.
        """
        q = self.session.query(ConsolidationRun)
        if status is not None:
            q = q.filter(ConsolidationRun.status == status)
        return list(q.all())

    def update_run_status(self, run_id: str, status: str) -> ConsolidationRun | None:
        """Transition a run to a new status.

        When *status* is ``"completed"``, the ``completed_at`` timestamp
        is automatically set to the current UTC time.

        Args:
            run_id: The run to update.
            status: The new status value.

        Returns:
            The updated run, or ``None`` if *run_id* was not found.
        """
        run = self.get_run(run_id)
        if run is None:
            return None
        run.status = status  # type: ignore[assignment]
        if status == "completed":
            run.completed_at = datetime.now(timezone.utc).isoformat()  # type: ignore[assignment]
        self.session.flush()
        return run

    # ------------------------------------------------------------------
    # ResearchArtifact helpers
    # ------------------------------------------------------------------

    def create_artifact(self, **kwargs: object) -> ResearchArtifact:
        """Insert a new :class:`ResearchArtifact`.

        Args:
            **kwargs: Column values forwarded to the model constructor.

        Returns:
            The newly created artifact instance.
        """
        artifact = ResearchArtifact(**kwargs)
        self.session.add(artifact)
        self.session.flush()
        return artifact

    def get_artifact(self, artifact_id: str) -> ResearchArtifact | None:
        """Fetch a single artifact by its primary key.

        Args:
            artifact_id: The artifact's unique identifier.

        Returns:
            The matching artifact, or ``None`` if not found.
        """
        return self.session.get(ResearchArtifact, artifact_id)

    def list_artifacts(self, run_id: str | None = None) -> list[ResearchArtifact]:
        """List artifacts, optionally scoped to a single run.

        Args:
            run_id: If provided, only return artifacts from this run.

        Returns:
            A list of matching :class:`ResearchArtifact` instances.
        """
        q = self.session.query(ResearchArtifact)
        if run_id is not None:
            q = q.filter(ResearchArtifact.run_id == run_id)
        return list(q.all())

    # ------------------------------------------------------------------
    # DecisionCard helpers
    # ------------------------------------------------------------------

    def create_decision_card(self, **kwargs: object) -> DecisionCard:
        """Insert a new :class:`DecisionCard`.

        Args:
            **kwargs: Column values forwarded to the model constructor.

        Returns:
            The newly created decision card instance.
        """
        card = DecisionCard(**kwargs)
        self.session.add(card)
        self.session.flush()
        return card

    def get_decision_card(self, decision_id: str) -> DecisionCard | None:
        """Fetch a single decision card by its primary key.

        Args:
            decision_id: The card's unique identifier.

        Returns:
            The matching decision card, or ``None`` if not found.
        """
        return self.session.get(DecisionCard, decision_id)

    def list_decision_cards(self, status: str | None = None) -> list[DecisionCard]:
        """List decision cards, optionally filtered by status.

        Args:
            status: If provided, only return cards with this status.

        Returns:
            A list of matching :class:`DecisionCard` instances.
        """
        q = self.session.query(DecisionCard)
        if status is not None:
            q = q.filter(DecisionCard.status == status)
        return list(q.all())

    # ------------------------------------------------------------------
    # ArtifactChunk helpers
    # ------------------------------------------------------------------

    def create_chunk(self, **kwargs: object) -> ArtifactChunk:
        """Insert a new :class:`ArtifactChunk`.

        Args:
            **kwargs: Column values forwarded to the model constructor.

        Returns:
            The newly created chunk instance.
        """
        chunk = ArtifactChunk(**kwargs)
        self.session.add(chunk)
        self.session.flush()
        return chunk

    def get_chunk(self, chunk_id: str) -> ArtifactChunk | None:
        """Fetch a single chunk by its primary key.

        Args:
            chunk_id: The chunk's unique identifier.

        Returns:
            The matching chunk, or ``None`` if not found.
        """
        return self.session.get(ArtifactChunk, chunk_id)

    def list_chunks(self, artifact_id: str | None = None) -> list[ArtifactChunk]:
        """List chunks, optionally scoped to a single artifact.

        Args:
            artifact_id: If provided, only return chunks for this artifact.

        Returns:
            A list of matching :class:`ArtifactChunk` instances.
        """
        q = self.session.query(ArtifactChunk)
        if artifact_id is not None:
            q = q.filter(ArtifactChunk.artifact_id == artifact_id)
        return list(q.all())

    # ------------------------------------------------------------------
    # DriftEvent helpers
    # ------------------------------------------------------------------

    def create_drift_event(self, **kwargs: object) -> DriftEvent:
        """Insert a new :class:`DriftEvent`.

        Args:
            **kwargs: Column values forwarded to the model constructor.

        Returns:
            The newly created drift event instance.
        """
        event = DriftEvent(**kwargs)
        self.session.add(event)
        self.session.flush()
        return event

    def get_drift_event(self, event_id: str) -> DriftEvent | None:
        """Fetch a single drift event by its primary key.

        Args:
            event_id: The event's unique identifier.

        Returns:
            The matching drift event, or ``None`` if not found.
        """
        return self.session.get(DriftEvent, event_id)

    # ------------------------------------------------------------------
    # ReferenceRewriteMap / ReferenceIntegrityReport helpers
    # ------------------------------------------------------------------

    def create_rewrite_map_entry(self, **kwargs: object) -> ReferenceRewriteMap:
        """Insert a new :class:`ReferenceRewriteMap` entry.

        Args:
            **kwargs: Column values forwarded to the model constructor.

        Returns:
            The newly created rewrite-map entry.
        """
        entry = ReferenceRewriteMap(**kwargs)
        self.session.add(entry)
        self.session.flush()
        return entry

    def create_integrity_report_entry(self, **kwargs: object) -> ReferenceIntegrityReport:
        """Insert a new :class:`ReferenceIntegrityReport` entry.

        Args:
            **kwargs: Column values forwarded to the model constructor.

        Returns:
            The newly created integrity-report entry.
        """
        entry = ReferenceIntegrityReport(**kwargs)
        self.session.add(entry)
        self.session.flush()
        return entry

    # ------------------------------------------------------------------
    # HumanReviewQueue helpers
    # ------------------------------------------------------------------

    def create_review_item(self, **kwargs: object) -> HumanReviewQueue:
        """Insert a new :class:`HumanReviewQueue` item.

        Args:
            **kwargs: Column values forwarded to the model constructor.

        Returns:
            The newly created review-queue item.
        """
        item = HumanReviewQueue(**kwargs)
        self.session.add(item)
        self.session.flush()
        return item

    def list_unresolved_reviews(self, run_id: str) -> list[HumanReviewQueue]:
        """List review items that have not yet been resolved.

        Args:
            run_id: Scope the query to this consolidation run.

        Returns:
            A list of :class:`HumanReviewQueue` items with no disposition.
        """
        return list(
            self.session.query(HumanReviewQueue)
            .filter(HumanReviewQueue.run_id == run_id, HumanReviewQueue.disposition.is_(None))
            .all()
        )

    def resolve_review(self, item_id: int, disposition: str, resolved_by: str = "system") -> HumanReviewQueue | None:
        """Mark a review-queue item as resolved.

        Args:
            item_id: Primary key of the item to resolve.
            disposition: The resolution decision (e.g. ``merge``, ``keep_both``).
            resolved_by: Identity of the resolver; defaults to ``"system"``.

        Returns:
            The updated item, or ``None`` if *item_id* was not found.
        """
        item = self.session.get(HumanReviewQueue, item_id)
        if item is None:
            return None
        item.disposition = disposition  # type: ignore[assignment]
        item.resolved_at = datetime.now(timezone.utc).isoformat()  # type: ignore[assignment]
        item.resolved_by = resolved_by  # type: ignore[assignment]
        self.session.flush()
        return item

    # ------------------------------------------------------------------
    # CapabilityMapping helpers
    # ------------------------------------------------------------------

    def create_capability_mapping(self, **kwargs: object) -> CapabilityMapping:
        """Insert a new :class:`CapabilityMapping`.

        Args:
            **kwargs: Column values forwarded to the model constructor.

        Returns:
            The newly created capability-mapping entry.
        """
        mapping = CapabilityMapping(**kwargs)
        self.session.add(mapping)
        self.session.flush()
        return mapping

    def list_capability_mappings(self, capability: str | None = None) -> list[CapabilityMapping]:
        """List capability mappings, optionally filtered by keyword.

        Args:
            capability: If provided, only return mappings for this capability.

        Returns:
            A list of matching :class:`CapabilityMapping` instances.
        """
        q = self.session.query(CapabilityMapping)
        if capability is not None:
            q = q.filter(CapabilityMapping.capability == capability)
        return list(q.all())

    # ------------------------------------------------------------------
    # TelemetryOutcome helpers
    # ------------------------------------------------------------------

    def create_telemetry_outcome(self, **kwargs: object) -> TelemetryOutcome:
        """Insert a new :class:`TelemetryOutcome`.

        Args:
            **kwargs: Column values forwarded to the model constructor.

        Returns:
            The newly created telemetry-outcome entry.
        """
        outcome = TelemetryOutcome(**kwargs)
        self.session.add(outcome)
        self.session.flush()
        return outcome

    def list_outcomes(self, decision_id: str) -> list[TelemetryOutcome]:
        """List telemetry outcomes for a specific decision card.

        Args:
            decision_id: The decision card to query outcomes for.

        Returns:
            A list of :class:`TelemetryOutcome` instances for the card.
        """
        return list(self.session.query(TelemetryOutcome).filter(TelemetryOutcome.decision_id == decision_id).all())
