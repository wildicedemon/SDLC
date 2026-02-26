from __future__ import annotations

from sqlalchemy import Boolean, Float, Integer, Text, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ConsolidationRun(Base):
    __tablename__ = "consolidation_runs"

    run_id: Mapped[str] = mapped_column(Text, primary_key=True)
    source_branch: Mapped[str] = mapped_column(Text, nullable=False)
    source_worktree: Mapped[str | None] = mapped_column(Text)
    started_at: Mapped[str] = mapped_column(Text, nullable=False)
    completed_at: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Text, nullable=False)
    artifacts_ingested: Mapped[int] = mapped_column(Integer, default=0)
    artifacts_deduped: Mapped[int] = mapped_column(Integer, default=0)
    decisions_impacted: Mapped[int] = mapped_column(Integer, default=0)
    drift_events_count: Mapped[int] = mapped_column(Integer, default=0)
    retirement_action: Mapped[str | None] = mapped_column(Text)
    remediation_report: Mapped[str | None] = mapped_column(Text)


class ResearchArtifact(Base):
    __tablename__ = "research_artifacts"

    artifact_id: Mapped[str] = mapped_column(Text, primary_key=True)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    domain_tags: Mapped[str] = mapped_column(Text, nullable=False)
    capability_tags: Mapped[str] = mapped_column(Text, nullable=False)
    source_branch: Mapped[str] = mapped_column(Text, nullable=False)
    source_worktree: Mapped[str | None] = mapped_column(Text)
    source_path: Mapped[str] = mapped_column(Text, nullable=False)
    source_commit: Mapped[str | None] = mapped_column(Text)
    captured_at: Mapped[str] = mapped_column(Text, nullable=False)
    run_id: Mapped[str] = mapped_column(Text, nullable=False)
    evidence_type: Mapped[str | None] = mapped_column(Text)
    source_reliability: Mapped[float] = mapped_column(Float, default=0.0)
    freshness_days: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[str] = mapped_column(Text, nullable=False, default="active")


class ArtifactChunk(Base):
    __tablename__ = "artifact_chunks"
    __table_args__ = (UniqueConstraint("artifact_id", "chunk_index"),)

    chunk_id: Mapped[str] = mapped_column(Text, primary_key=True)
    artifact_id: Mapped[str] = mapped_column(Text, nullable=False)
    chunk_index: Mapped[int] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    embedding_synced: Mapped[bool] = mapped_column(Boolean, default=False)


class DecisionCard(Base):
    __tablename__ = "decision_cards"

    decision_id: Mapped[str] = mapped_column(Text, primary_key=True)
    question: Mapped[str] = mapped_column(Text, nullable=False)
    capability: Mapped[str] = mapped_column(Text, nullable=False)
    constraints: Mapped[str | None] = mapped_column(Text)
    recommendation: Mapped[str] = mapped_column(Text, nullable=False)
    alternatives: Mapped[str | None] = mapped_column(Text)
    confidence_score: Mapped[float] = mapped_column(Float, nullable=False)
    confidence_level: Mapped[str] = mapped_column(Text, nullable=False)
    confidence_explanation: Mapped[str | None] = mapped_column(Text)
    has_unresolved_contradiction: Mapped[bool] = mapped_column(Boolean, default=False)
    provenance_refs: Mapped[str] = mapped_column(Text, nullable=False)
    last_validated_at: Mapped[str] = mapped_column(Text, nullable=False)
    revisit_triggers: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Text, nullable=False, default="active")


class DriftEvent(Base):
    __tablename__ = "drift_events"

    event_id: Mapped[str] = mapped_column(Text, primary_key=True)
    decision_id: Mapped[str] = mapped_column(Text, nullable=False)
    trigger: Mapped[str] = mapped_column(Text, nullable=False)
    confidence_delta: Mapped[float | None] = mapped_column(Float)
    affected_sections: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Text, nullable=False)
    run_id: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[str] = mapped_column(Text, nullable=False)


class ReferenceRewriteMap(Base):
    __tablename__ = "reference_rewrite_maps"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    run_id: Mapped[str] = mapped_column(Text, nullable=False)
    old_path: Mapped[str] = mapped_column(Text, nullable=False)
    new_path: Mapped[str] = mapped_column(Text, nullable=False)
    rewritten: Mapped[bool] = mapped_column(Boolean, default=False)


class ReferenceIntegrityReport(Base):
    __tablename__ = "reference_integrity_reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    run_id: Mapped[str] = mapped_column(Text, nullable=False)
    check_type: Mapped[str] = mapped_column(Text, nullable=False)
    target_path: Mapped[str] = mapped_column(Text, nullable=False)
    resolved: Mapped[bool] = mapped_column(Boolean, nullable=False)
    error_detail: Mapped[str | None] = mapped_column(Text)


class HumanReviewQueue(Base):
    __tablename__ = "human_review_queue"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    run_id: Mapped[str] = mapped_column(Text, nullable=False)
    item_type: Mapped[str] = mapped_column(Text, nullable=False)
    artifact_a_id: Mapped[str] = mapped_column(Text, nullable=False)
    artifact_b_id: Mapped[str] = mapped_column(Text, nullable=False)
    ai_confidence: Mapped[float | None] = mapped_column(Float)
    ai_recommendation: Mapped[str | None] = mapped_column(Text)
    disposition: Mapped[str | None] = mapped_column(Text)
    resolved_at: Mapped[str | None] = mapped_column(Text)
    resolved_by: Mapped[str | None] = mapped_column(Text)


class CapabilityMapping(Base):
    __tablename__ = "capability_mappings"
    __table_args__ = (UniqueConstraint("capability", "decision_id"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    capability: Mapped[str] = mapped_column(Text, nullable=False)
    decision_id: Mapped[str] = mapped_column(Text, nullable=False)
    domain: Mapped[str] = mapped_column(Text, nullable=False)


class TelemetryOutcome(Base):
    __tablename__ = "telemetry_outcomes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    decision_id: Mapped[str] = mapped_column(Text, nullable=False)
    timestamp: Mapped[str] = mapped_column(Text, nullable=False)
    outcome: Mapped[str] = mapped_column(Text, nullable=False)
