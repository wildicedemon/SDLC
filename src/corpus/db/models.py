"""SQLAlchemy ORM models for the corpus pipeline database.

Defines the nine core tables that back the pipeline:

* :class:`ConsolidationRun` — top-level run lifecycle tracking.
* :class:`ResearchArtifact` — ingested research documents.
* :class:`ArtifactChunk` — split content segments for embedding.
* :class:`DecisionCard` — LLM-generated architectural decisions.
* :class:`DriftEvent` — confidence-score drift records.
* :class:`ReferenceRewriteMap` — old→new path rewrites per run.
* :class:`ReferenceIntegrityReport` — link-integrity check results.
* :class:`HumanReviewQueue` — items queued for manual triage.
* :class:`CapabilityMapping` — decision↔capability associations.
* :class:`TelemetryOutcome` — success/failure telemetry records.

All text-date columns store ISO-8601 strings; SQLite has no native
datetime type, so this keeps the schema portable.
"""

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    Float,
    ForeignKey,
    Integer,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    """Declarative base class shared by all corpus ORM models."""

    pass


class ConsolidationRun(Base):
    """A single pipeline consolidation run.

    Tracks the full lifecycle from *pending* → *running* →
    *completed* / *failed*, along with aggregate counters for
    artifacts ingested, deduped, decisions impacted, and drift events.

    Attributes:
        run_id: Unique identifier for the run (UUID string).
        source_branch: Git branch the run consolidates from.
        source_worktree: Optional worktree path for the branch.
        started_at: ISO-8601 timestamp when the run began.
        completed_at: ISO-8601 timestamp when the run finished.
        status: Current state — ``pending``, ``running``, ``completed``, or ``failed``.
        artifacts_ingested: Count of artifacts ingested during this run.
        artifacts_deduped: Count of artifacts removed by dedup.
        decisions_impacted: Count of decision cards affected.
        drift_events_count: Number of drift events generated.
        retirement_action: Branch retirement disposition (e.g. ``delete``).
        remediation_report: Free-text remediation summary.
    """

    __tablename__ = "consolidation_runs"

    run_id = Column(Text, primary_key=True)
    source_branch = Column(Text, nullable=False)
    source_worktree = Column(Text)
    started_at = Column(Text, nullable=False)
    completed_at = Column(Text)
    status = Column(Text, nullable=False)
    artifacts_ingested = Column(Integer, default=0)
    artifacts_deduped = Column(Integer, default=0)
    decisions_impacted = Column(Integer, default=0)
    drift_events_count = Column(Integer, default=0)
    retirement_action = Column(Text)
    remediation_report = Column(Text)

    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'running', 'completed', 'failed')",
            name="ck_consolidation_runs_status",
        ),
    )

    # Relationships
    artifacts = relationship("ResearchArtifact", back_populates="run")
    drift_events = relationship("DriftEvent", back_populates="run")


class ResearchArtifact(Base):
    """An ingested research document or knowledge fragment.

    Represents a single piece of research captured from a branch,
    classified by domain and capability tags, and tracked through
    its lifecycle (``candidate`` → ``active`` → ``superseded`` / ``archived``).

    Attributes:
        artifact_id: Unique identifier (UUID string).
        title: Human-readable title extracted from the source.
        content: Full normalized text content.
        domain_tags: Comma-separated domain classification tags.
        capability_tags: Comma-separated capability tags.
        source_branch: Git branch the artifact was found in.
        source_worktree: Optional worktree path.
        source_path: File path relative to the repository root.
        source_commit: Git commit SHA at capture time.
        captured_at: ISO-8601 capture timestamp.
        run_id: Foreign key to the owning :class:`ConsolidationRun`.
        evidence_type: Type of evidence (e.g. ``benchmark``, ``analysis``).
        source_reliability: Reliability score (0.0–1.0).
        freshness_days: Age in days since the source was last modified.
        status: Lifecycle state — ``candidate``, ``active``, ``superseded``, or ``archived``.
    """

    __tablename__ = "research_artifacts"

    artifact_id = Column(Text, primary_key=True)
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    domain_tags = Column(Text, nullable=False)
    capability_tags = Column(Text, nullable=False)
    source_branch = Column(Text, nullable=False)
    source_worktree = Column(Text)
    source_path = Column(Text, nullable=False)
    source_commit = Column(Text)
    captured_at = Column(Text, nullable=False)
    run_id = Column(Text, ForeignKey("consolidation_runs.run_id"), nullable=False)
    evidence_type = Column(Text)
    source_reliability = Column(Float, default=0.0)
    freshness_days = Column(Integer, default=0)
    status = Column(Text, nullable=False, default="active")

    __table_args__ = (
        CheckConstraint(
            "status IN ('candidate', 'active', 'superseded', 'archived')",
            name="ck_research_artifacts_status",
        ),
    )

    # Relationships
    run = relationship("ConsolidationRun", back_populates="artifacts")
    chunks = relationship("ArtifactChunk", back_populates="artifact")


class ArtifactChunk(Base):
    """A content chunk belonging to a :class:`ResearchArtifact`.

    Large artifacts are split into ordered chunks for embedding
    and vector-search purposes. Each chunk tracks whether its
    embedding has been synced to the vector store.

    Attributes:
        chunk_id: Unique chunk identifier (UUID string).
        artifact_id: Foreign key to the parent artifact.
        chunk_index: Zero-based position within the artifact.
        content: The chunk's text content.
        embedding_synced: Whether the embedding has been written to ChromaDB.
    """

    __tablename__ = "artifact_chunks"

    chunk_id = Column(Text, primary_key=True)
    artifact_id = Column(Text, ForeignKey("research_artifacts.artifact_id"), nullable=False)
    chunk_index = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    embedding_synced = Column(Boolean, default=False)

    __table_args__ = (UniqueConstraint("artifact_id", "chunk_index", name="uq_artifact_chunk_index"),)

    artifact = relationship("ResearchArtifact", back_populates="chunks")


class DecisionCard(Base):
    """An architectural decision card generated by the LLM.

    Captures a question, the recommended answer, alternatives,
    confidence scoring, and provenance links back to the evidence.

    Attributes:
        decision_id: Unique identifier (UUID string).
        question: The architectural question being answered.
        capability: The capability area this decision relates to.
        constraints: Known constraints influencing the decision.
        recommendation: The recommended course of action.
        alternatives: JSON-encoded alternative options considered.
        confidence_score: Numeric confidence (0.0–1.0).
        confidence_level: Bucketed level — ``high``, ``medium``, or ``low``.
        confidence_explanation: Free-text justification for the score.
        has_unresolved_contradiction: Flag for conflicting evidence.
        provenance_refs: Comma-separated artifact IDs as evidence.
        last_validated_at: ISO-8601 timestamp of the last validation.
        revisit_triggers: Conditions that should trigger re-evaluation.
        status: Lifecycle state — ``active``, ``superseded``, or ``archived``.
    """

    __tablename__ = "decision_cards"

    decision_id = Column(Text, primary_key=True)
    question = Column(Text, nullable=False)
    capability = Column(Text, nullable=False)
    constraints = Column(Text)
    recommendation = Column(Text, nullable=False)
    alternatives = Column(Text)
    confidence_score = Column(Float, nullable=False)
    confidence_level = Column(Text, nullable=False)
    confidence_explanation = Column(Text)
    has_unresolved_contradiction = Column(Boolean, default=False)
    provenance_refs = Column(Text, nullable=False)
    last_validated_at = Column(Text, nullable=False)
    revisit_triggers = Column(Text)
    status = Column(Text, nullable=False, default="active")

    __table_args__ = (
        CheckConstraint(
            "confidence_level IN ('high', 'medium', 'low')",
            name="ck_decision_cards_confidence_level",
        ),
        CheckConstraint(
            "status IN ('active', 'superseded', 'archived')",
            name="ck_decision_cards_status",
        ),
    )

    # Relationships
    drift_events = relationship("DriftEvent", back_populates="decision")
    capability_mappings = relationship("CapabilityMapping", back_populates="decision")
    telemetry_outcomes = relationship("TelemetryOutcome", back_populates="decision")


class DriftEvent(Base):
    """Records a confidence-score drift event on a decision card.

    Created when new evidence causes a decision card's confidence
    to shift beyond a configured threshold.

    Attributes:
        event_id: Unique event identifier (UUID string).
        decision_id: Foreign key to the affected :class:`DecisionCard`.
        trigger: Description of what caused the drift.
        confidence_delta: Magnitude of the confidence change.
        affected_sections: Sections of the decision card impacted.
        status: Resolution state — ``pending_revalidation``, ``resolved``, or ``dismissed``.
        run_id: Foreign key to the :class:`ConsolidationRun` that detected it.
        created_at: ISO-8601 creation timestamp.
    """

    __tablename__ = "drift_events"

    event_id = Column(Text, primary_key=True)
    decision_id = Column(Text, ForeignKey("decision_cards.decision_id"), nullable=False)
    trigger = Column(Text, nullable=False)
    confidence_delta = Column(Float)
    affected_sections = Column(Text)
    status = Column(Text, nullable=False)
    run_id = Column(Text, ForeignKey("consolidation_runs.run_id"), nullable=False)
    created_at = Column(Text, nullable=False)

    __table_args__ = (
        CheckConstraint(
            "status IN ('pending_revalidation', 'resolved', 'dismissed')",
            name="ck_drift_events_status",
        ),
    )

    decision = relationship("DecisionCard", back_populates="drift_events")
    run = relationship("ConsolidationRun", back_populates="drift_events")


class ReferenceRewriteMap(Base):
    """Maps an old file path to a new one for a given consolidation run.

    Used by the reference-rewriting phase to update markdown links
    after files are moved or renamed during consolidation.

    Attributes:
        id: Auto-incremented primary key.
        run_id: Foreign key to the :class:`ConsolidationRun`.
        old_path: The original file path.
        new_path: The rewritten file path.
        rewritten: Whether the rewrite has been applied.
    """

    __tablename__ = "reference_rewrite_maps"

    id = Column(Integer, primary_key=True, autoincrement=True)
    run_id = Column(Text, ForeignKey("consolidation_runs.run_id"), nullable=False)
    old_path = Column(Text, nullable=False)
    new_path = Column(Text, nullable=False)
    rewritten = Column(Boolean, default=False)


class ReferenceIntegrityReport(Base):
    """Result of a single link-integrity check within a run.

    Each row records whether a particular reference (link, image,
    anchor) resolved successfully or produced an error.

    Attributes:
        id: Auto-incremented primary key.
        run_id: Foreign key to the :class:`ConsolidationRun`.
        check_type: Kind of check (e.g. ``link``, ``image``, ``anchor``).
        target_path: The path or URL being validated.
        resolved: Whether the target was reachable.
        error_detail: Explanation when *resolved* is ``False``.
    """

    __tablename__ = "reference_integrity_reports"

    id = Column(Integer, primary_key=True, autoincrement=True)
    run_id = Column(Text, ForeignKey("consolidation_runs.run_id"), nullable=False)
    check_type = Column(Text, nullable=False)
    target_path = Column(Text, nullable=False)
    resolved = Column(Boolean, nullable=False)
    error_detail = Column(Text)


class HumanReviewQueue(Base):
    """An item requiring human review during deduplication.

    When the LLM arbitrator cannot confidently resolve a near-duplicate
    pair, the conflict is queued here for manual disposition.

    Attributes:
        id: Auto-incremented primary key.
        run_id: Foreign key to the :class:`ConsolidationRun`.
        item_type: Category of the review item (e.g. ``dedup_conflict``).
        artifact_a_id: First artifact in the conflict pair.
        artifact_b_id: Second artifact in the conflict pair.
        ai_confidence: LLM's confidence that the pair is duplicated.
        ai_recommendation: LLM's suggested action (``merge``, ``keep_both``, etc.).
        disposition: Final human decision, or ``None`` if unresolved.
        resolved_at: ISO-8601 timestamp when resolved.
        resolved_by: Identity of the resolver (user or ``system``).
    """

    __tablename__ = "human_review_queue"

    id = Column(Integer, primary_key=True, autoincrement=True)
    run_id = Column(Text, ForeignKey("consolidation_runs.run_id"), nullable=False)
    item_type = Column(Text, nullable=False)
    artifact_a_id = Column(Text, ForeignKey("research_artifacts.artifact_id"), nullable=False)
    artifact_b_id = Column(Text, ForeignKey("research_artifacts.artifact_id"), nullable=False)
    ai_confidence = Column(Float)
    ai_recommendation = Column(Text)
    disposition = Column(Text)
    resolved_at = Column(Text)
    resolved_by = Column(Text)


class CapabilityMapping(Base):
    """Associates a capability keyword with a decision card and domain.

    Provides a lightweight index that the retrieval layer uses to
    filter decisions by capability and domain.

    Attributes:
        id: Auto-incremented primary key.
        capability: The capability keyword (e.g. ``caching``).
        decision_id: Foreign key to the :class:`DecisionCard`.
        domain: Domain the mapping belongs to (e.g. ``backend``).
    """

    __tablename__ = "capability_mappings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    capability = Column(Text, nullable=False)
    decision_id = Column(Text, ForeignKey("decision_cards.decision_id"), nullable=False)
    domain = Column(Text, nullable=False)

    __table_args__ = (UniqueConstraint("capability", "decision_id", name="uq_capability_decision"),)

    decision = relationship("DecisionCard", back_populates="capability_mappings")


class TelemetryOutcome(Base):
    """Records a success or failure outcome for a decision card.

    The telemetry calibrator aggregates these records to adjust
    confidence scores over time based on real-world results.

    Attributes:
        id: Auto-incremented primary key.
        decision_id: Foreign key to the :class:`DecisionCard`.
        timestamp: ISO-8601 timestamp of the outcome.
        outcome: Either ``success`` or ``failure``.
    """

    __tablename__ = "telemetry_outcomes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    decision_id = Column(Text, ForeignKey("decision_cards.decision_id"), nullable=False)
    timestamp = Column(Text, nullable=False)
    outcome = Column(Text, nullable=False)

    __table_args__ = (
        CheckConstraint(
            "outcome IN ('success', 'failure')",
            name="ck_telemetry_outcomes_outcome",
        ),
    )

    decision = relationship("DecisionCard", back_populates="telemetry_outcomes")
