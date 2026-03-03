"""Corpus pipeline — research ingestion, dedup, decision synthesis, and retrieval.

This package implements the full SDLC corpus consolidation pipeline:

* **ingestion** — enumerate, classify, normalise, and chunk research artifacts.
* **dedup** — 3-layer deduplication (MinHash → embeddings → LLM arbitration).
* **decisions** — LLM-generated decision cards with confidence scoring.
* **references** — path rewriting and link-integrity validation.
* **consolidation** — run lifecycle, quality gates, and branch retirement.
* **sync** — ChromaDB vector sync and NetworkX graph sync.
* **retrieval** — hybrid semantic + graph + symbolic query answering.
* **telemetry** — outcome collection, calibration, compaction, and metrics.
* **db** — SQLAlchemy ORM models, repository, and SQL migrations.
"""

__version__ = "0.1.0"
