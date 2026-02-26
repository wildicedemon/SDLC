CREATE TABLE consolidation_runs (
    run_id TEXT PRIMARY KEY,
    source_branch TEXT NOT NULL,
    source_worktree TEXT,
    started_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL CHECK (status IN ('pending', 'running', 'completed', 'failed')),
    artifacts_ingested INTEGER DEFAULT 0,
    artifacts_deduped INTEGER DEFAULT 0,
    decisions_impacted INTEGER DEFAULT 0,
    drift_events_count INTEGER DEFAULT 0,
    retirement_action TEXT CHECK (retirement_action IN ('archived', 'deleted', 'n/a') OR retirement_action IS NULL),
    remediation_report TEXT
);

CREATE TABLE research_artifacts (
    artifact_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    domain_tags TEXT NOT NULL,
    capability_tags TEXT NOT NULL,
    source_branch TEXT NOT NULL,
    source_worktree TEXT,
    source_path TEXT NOT NULL,
    source_commit TEXT,
    captured_at TEXT NOT NULL,
    run_id TEXT NOT NULL REFERENCES consolidation_runs(run_id),
    evidence_type TEXT CHECK (evidence_type IN ('theory', 'experiment', 'benchmark', 'postmortem') OR evidence_type IS NULL),
    source_reliability REAL DEFAULT 0.0,
    freshness_days INTEGER DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('candidate', 'active', 'superseded', 'archived'))
);

CREATE TABLE artifact_chunks (
    chunk_id TEXT PRIMARY KEY,
    artifact_id TEXT NOT NULL REFERENCES research_artifacts(artifact_id),
    chunk_index INTEGER NOT NULL,
    content TEXT NOT NULL,
    embedding_synced BOOLEAN DEFAULT 0,
    UNIQUE(artifact_id, chunk_index)
);

CREATE TABLE decision_cards (
    decision_id TEXT PRIMARY KEY,
    question TEXT NOT NULL,
    capability TEXT NOT NULL,
    constraints TEXT,
    recommendation TEXT NOT NULL,
    alternatives TEXT,
    confidence_score REAL NOT NULL,
    confidence_level TEXT NOT NULL CHECK (confidence_level IN ('high', 'medium', 'low')),
    confidence_explanation TEXT,
    has_unresolved_contradiction BOOLEAN DEFAULT 0,
    provenance_refs TEXT NOT NULL,
    last_validated_at TEXT NOT NULL,
    revisit_triggers TEXT,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'superseded', 'archived'))
);

CREATE TABLE drift_events (
    event_id TEXT PRIMARY KEY,
    decision_id TEXT NOT NULL REFERENCES decision_cards(decision_id),
    trigger TEXT NOT NULL,
    confidence_delta REAL,
    affected_sections TEXT,
    status TEXT NOT NULL CHECK (status IN ('pending_revalidation', 'resolved', 'dismissed')),
    run_id TEXT NOT NULL REFERENCES consolidation_runs(run_id),
    created_at TEXT NOT NULL
);

CREATE TABLE reference_rewrite_maps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL REFERENCES consolidation_runs(run_id),
    old_path TEXT NOT NULL,
    new_path TEXT NOT NULL,
    rewritten BOOLEAN DEFAULT 0
);

CREATE TABLE reference_integrity_reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL REFERENCES consolidation_runs(run_id),
    check_type TEXT NOT NULL CHECK (check_type IN ('internal_link', 'source_path', 'index_ref')),
    target_path TEXT NOT NULL,
    resolved BOOLEAN NOT NULL,
    error_detail TEXT
);

CREATE TABLE human_review_queue (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL REFERENCES consolidation_runs(run_id),
    item_type TEXT NOT NULL,
    artifact_a_id TEXT NOT NULL REFERENCES research_artifacts(artifact_id),
    artifact_b_id TEXT NOT NULL REFERENCES research_artifacts(artifact_id),
    ai_confidence REAL,
    ai_recommendation TEXT CHECK (ai_recommendation IN ('merge', 'keep_both', 'discard_one') OR ai_recommendation IS NULL),
    disposition TEXT CHECK (disposition IN ('approved_merge', 'rejected_merge', 'deferred') OR disposition IS NULL),
    resolved_at TEXT,
    resolved_by TEXT
);

CREATE TABLE capability_mappings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    capability TEXT NOT NULL,
    decision_id TEXT NOT NULL REFERENCES decision_cards(decision_id),
    domain TEXT NOT NULL,
    UNIQUE(capability, decision_id)
);

CREATE TABLE telemetry_outcomes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    decision_id TEXT NOT NULL REFERENCES decision_cards(decision_id),
    timestamp TEXT NOT NULL,
    outcome TEXT NOT NULL CHECK (outcome IN ('success', 'failure'))
);
