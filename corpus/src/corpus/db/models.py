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
    pass


class ConsolidationRun(Base):
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

    artifacts = relationship("ResearchArtifact", back_populates="run")
    drift_events = relationship("DriftEvent", back_populates="run")


class ResearchArtifact(Base):
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

    run = relationship("ConsolidationRun", back_populates="artifacts")
    chunks = relationship("ArtifactChunk", back_populates="artifact")


class ArtifactChunk(Base):
    __tablename__ = "artifact_chunks"

    chunk_id = Column(Text, primary_key=True)
    artifact_id = Column(Text, ForeignKey("research_artifacts.artifact_id"), nullable=False)
    chunk_index = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    embedding_synced = Column(Boolean, default=False)

    __table_args__ = (UniqueConstraint("artifact_id", "chunk_index", name="uq_artifact_chunk_index"),)

    artifact = relationship("ResearchArtifact", back_populates="chunks")


class DecisionCard(Base):
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

    drift_events = relationship("DriftEvent", back_populates="decision")
    capability_mappings = relationship("CapabilityMapping", back_populates="decision")
    telemetry_outcomes = relationship("TelemetryOutcome", back_populates="decision")


class DriftEvent(Base):
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
    __tablename__ = "reference_rewrite_maps"

    id = Column(Integer, primary_key=True, autoincrement=True)
    run_id = Column(Text, ForeignKey("consolidation_runs.run_id"), nullable=False)
    old_path = Column(Text, nullable=False)
    new_path = Column(Text, nullable=False)
    rewritten = Column(Boolean, default=False)


class ReferenceIntegrityReport(Base):
    __tablename__ = "reference_integrity_reports"

    id = Column(Integer, primary_key=True, autoincrement=True)
    run_id = Column(Text, ForeignKey("consolidation_runs.run_id"), nullable=False)
    check_type = Column(Text, nullable=False)
    target_path = Column(Text, nullable=False)
    resolved = Column(Boolean, nullable=False)
    error_detail = Column(Text)


class HumanReviewQueue(Base):
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
    __tablename__ = "capability_mappings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    capability = Column(Text, nullable=False)
    decision_id = Column(Text, ForeignKey("decision_cards.decision_id"), nullable=False)
    domain = Column(Text, nullable=False)

    __table_args__ = (UniqueConstraint("capability", "decision_id", name="uq_capability_decision"),)

    decision = relationship("DecisionCard", back_populates="capability_mappings")


class TelemetryOutcome(Base):
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
