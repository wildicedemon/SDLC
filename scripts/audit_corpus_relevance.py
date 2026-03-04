"""Corpus relevance auditor — LLM-powered audit for off-topic content.

Iterates over all ResearchArtifact and DecisionCard rows in the corpus
database, sends each to an LLM for a relevance judgment, and produces
a structured report of items flagged as irrelevant.

Usage::

    python scripts/audit_corpus_relevance.py
    python scripts/audit_corpus_relevance.py --dry-run
    python scripts/audit_corpus_relevance.py --skip-decisions --max-calls 100
    python scripts/audit_corpus_relevance.py --checkpoint data/relevance_audit_checkpoint.json

See ``scripts/AUDIT_DESIGN.md`` for the full specification.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# sys.path hack — match existing scripts (bootstrap_corpus.py, etc.)
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

# Ensure stdout can handle Unicode on Windows (cp1252 default would crash)
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]

from openai import OpenAI, RateLimitError  # noqa: E402

from corpus.config import get_settings  # noqa: E402
from corpus.db.engine import create_db_engine, get_session  # noqa: E402
from corpus.db.repository import CorpusRepository  # noqa: E402

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
_FALLBACK_API_KEY = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJlbnYiOiJwcm9kdWN0aW9uIiwia2lsb1VzZXJJZCI6IjMwZjYwMDQ5LTIyMjktNGUxMy1i"
    "YmVhLTIyNjRjNTEzZGQ5ZiIsImFwaVRva2VuUGVwcGVyIjpudWxsLCJ2ZXJzaW9uIjozLCJp"
    "YXQiOjE3NzI1OTQ4OTYsImV4cCI6MTkzMDI3NDg5Nn0."
    "U52JU0QcdLPFJjYfIHNHxmbVynOrMkdd2a2UuQqrwhI"
)
_MAX_CONSECUTIVE_FAILURES = 10
_MAX_RETRIES_RATE_LIMIT = 3
_PROGRESS_LOG_INTERVAL = 25

# ---------------------------------------------------------------------------
# Prompt templates (AUDIT_DESIGN.md §3)
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """\
You are a corpus relevance auditor for an engineering knowledge base.
The knowledge base exists to support the design, planning, building,
testing, deployment, and operation of AUTONOMOUS AI AGENTS — software
systems that perceive their environment, make decisions, and take
actions with minimal human intervention.

Relevant topics include, but are not limited to:
- Agent architectures, orchestration, and multi-agent coordination
- LLM integration, prompt engineering, context management
- Code generation, analysis, and self-modification
- SDLC automation, CI/CD for AI systems
- Memory systems, RAG, knowledge graphs
- Tool use, function calling, MCP servers
- Model evaluation, benchmarking, fine-tuning
- Safety, alignment, guardrails, human-in-the-loop
- Deployment infrastructure, scaling, monitoring
- Self-improvement, meta-learning, recursive optimization

Your job: determine whether a given piece of content is RELEVANT to
this mission. Respond ONLY with a JSON object — no markdown fences,
no extra text."""

ARTIFACT_USER_TEMPLATE = """\
Evaluate this research artifact for relevance.

TITLE: {title}
DOMAIN TAGS: {domain_tags}
CAPABILITY TAGS: {capability_tags}
SOURCE PATH: {source_path}

CONTENT (first {max_chars} characters):
---
{content_truncated}
---

Respond with JSON:
{{
  "relevant": true | false,
  "confidence": 0.0 to 1.0,
  "reason": "1-2 sentence explanation"
}}"""

DECISION_CARD_USER_TEMPLATE = """\
Evaluate this decision card for relevance.

QUESTION: {question}
CAPABILITY: {capability}
RECOMMENDATION: {recommendation}
ALTERNATIVES: {alternatives}

Respond with JSON:
{{
  "relevant": true | false,
  "confidence": 0.0 to 1.0,
  "reason": "1-2 sentence explanation"
}}"""


# ---------------------------------------------------------------------------
# Section 3: LLM client abstraction
# ---------------------------------------------------------------------------
class RelevanceAuditor:
    """Wraps the OpenAI-compatible API for relevance judgments.

    Follows the same client-construction pattern used in
    :func:`corpus.dedup.arbitrator.arbitrate`.
    """

    def __init__(
        self,
        base_url: str,
        api_key: str,
        model: str,
        max_content_chars: int,
        delay: float,
    ) -> None:
        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key,
            max_retries=1,
            timeout=30.0,
        )
        self.model = model
        self.max_content_chars = max_content_chars
        self.delay = delay

    # -- public API --------------------------------------------------------

    def audit_artifact(self, artifact: object) -> dict:
        """Build a user prompt for a *ResearchArtifact* and call the LLM."""
        content = (getattr(artifact, "content", "") or "")[: self.max_content_chars]
        user_prompt = ARTIFACT_USER_TEMPLATE.format(
            title=getattr(artifact, "title", "") or "",
            domain_tags=getattr(artifact, "domain_tags", "") or "",
            capability_tags=getattr(artifact, "capability_tags", "") or "",
            source_path=getattr(artifact, "source_path", "") or "",
            max_chars=self.max_content_chars,
            content_truncated=content,
        )
        result = self._call_llm(user_prompt)
        result["artifact_id"] = artifact.artifact_id  # type: ignore[attr-defined]
        result["title"] = getattr(artifact, "title", "") or ""
        result["domain_tags"] = getattr(artifact, "domain_tags", "") or ""
        result["source_path"] = getattr(artifact, "source_path", "") or ""
        result["status"] = getattr(artifact, "status", "") or ""
        return result

    def audit_decision_card(self, card: object) -> dict:
        """Build a user prompt for a *DecisionCard* and call the LLM."""
        user_prompt = DECISION_CARD_USER_TEMPLATE.format(
            question=getattr(card, "question", "") or "",
            capability=getattr(card, "capability", "") or "",
            recommendation=getattr(card, "recommendation", "") or "",
            alternatives=getattr(card, "alternatives", "") or "",
        )
        result = self._call_llm(user_prompt)
        result["decision_id"] = card.decision_id  # type: ignore[attr-defined]
        result["question"] = getattr(card, "question", "") or ""
        result["capability"] = getattr(card, "capability", "") or ""
        return result

    # -- internals ---------------------------------------------------------

    def _call_llm(self, user_prompt: str) -> dict:
        """Send a chat completion and parse the JSON response.

        Retries up to ``_MAX_RETRIES_RATE_LIMIT`` times on HTTP 429.
        Non-retryable errors return a safe default (``relevant=True``).
        """
        last_exc: Exception | None = None

        for attempt in range(_MAX_RETRIES_RATE_LIMIT):
            try:
                resp = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt},
                    ],
                    max_tokens=300,
                )
                raw = (resp.choices[0].message.content or "").strip()
                return self._parse_response(raw)

            except RateLimitError as exc:
                last_exc = exc
                wait = self.delay * (2**attempt)
                logger.warning(
                    "Rate limited (attempt %d/%d), waiting %.1fs: %s",
                    attempt + 1,
                    _MAX_RETRIES_RATE_LIMIT,
                    wait,
                    str(exc)[:120],
                )
                time.sleep(wait)

            except Exception as exc:  # noqa: BLE001
                logger.warning(
                    "LLM call failed: %s: %s",
                    type(exc).__name__,
                    str(exc)[:120],
                )
                return {
                    "relevant": True,
                    "confidence": 0.0,
                    "reason": "LLM call error",
                    "error": f"{type(exc).__name__}: {str(exc)[:200]}",
                }

        # Exhausted rate-limit retries
        return {
            "relevant": True,
            "confidence": 0.0,
            "reason": "Rate limit exceeded after retries",
            "error": f"RateLimitError: {str(last_exc)[:200]}",
        }

    @staticmethod
    def _parse_response(raw: str) -> dict:
        """Extract and validate a JSON object from the LLM response.

        Defensively handles markdown fences and extraneous text, matching
        the approach in :func:`corpus.dedup.arbitrator.arbitrate`.
        """
        try:
            cleaned = raw
            # Strip markdown code fences if present
            if cleaned.startswith("```"):
                lines = cleaned.split("\n")
                cleaned = "\n".join(
                    line for line in lines if not line.strip().startswith("```")
                ).strip()

            # Find the first { and last } to extract JSON
            start = cleaned.find("{")
            end = cleaned.rfind("}") + 1
            if start >= 0 and end > start:
                parsed = json.loads(cleaned[start:end])
            else:
                raise ValueError("No JSON object found in response")

            # Validate / coerce expected fields
            relevant = parsed.get("relevant")
            if not isinstance(relevant, bool):
                if isinstance(relevant, str):
                    relevant = relevant.lower() in ("true", "yes", "1")
                else:
                    relevant = True

            confidence = float(parsed.get("confidence", 0.0))
            confidence = max(0.0, min(1.0, confidence))
            reason = str(parsed.get("reason", ""))

            return {
                "relevant": relevant,
                "confidence": confidence,
                "reason": reason,
                "error": None,
            }

        except Exception as exc:  # noqa: BLE001
            logger.debug("Response parse failure: %s — raw: %s", exc, raw[:200])
            return {
                "relevant": True,
                "confidence": 0.0,
                "reason": "parse error",
                "error": f"Parse error: {str(exc)[:200]}",
            }


# ---------------------------------------------------------------------------
# Section 4: Checkpoint management
# ---------------------------------------------------------------------------
class CheckpointManager:
    """Atomic checkpoint writes for audit resume support.

    Checkpoint format (see AUDIT_DESIGN.md §7.1)::

        {
          "phase": "artifacts" | "decisions",
          "completed_ids": [...],
          "results": [...],
          "last_updated": "ISO-8601"
        }
    """

    def __init__(self, checkpoint_path: Path) -> None:
        self.path = checkpoint_path

    def load(self) -> tuple[set[str], list[dict]]:
        """Load checkpoint state.

        Returns:
            A tuple of *(completed_ids, partial_results)*.
        """
        if not self.path.exists():
            return set(), []
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            ids = set(data.get("completed_ids", []))
            results = data.get("results", [])
            logger.info(
                "Loaded checkpoint: %d completed items, phase=%s",
                len(ids),
                data.get("phase", "unknown"),
            )
            return ids, results
        except Exception as exc:  # noqa: BLE001
            logger.warning("Failed to load checkpoint (%s) — starting fresh", exc)
            return set(), []

    def save(
        self, completed_ids: set[str], results: list[dict], phase: str
    ) -> None:
        """Atomically write checkpoint via tmp-then-rename."""
        data = {
            "phase": phase,
            "completed_ids": sorted(completed_ids),
            "results": results,
            "last_updated": datetime.now(timezone.utc).isoformat(),
        }
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = self.path.with_suffix(".tmp")
        tmp_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        tmp_path.replace(self.path)

    def delete(self) -> None:
        """Remove checkpoint file on successful completion."""
        if self.path.exists():
            self.path.unlink()
            logger.info("Checkpoint file removed")


# ---------------------------------------------------------------------------
# Section 5: Report generation
# ---------------------------------------------------------------------------
def write_json_report(
    audit_metadata: dict,
    artifact_results: list[dict],
    decision_card_results: list[dict],
    output_path: Path,
    *,
    only_flagged: bool = False,
) -> None:
    """Write the full JSON audit report (AUDIT_DESIGN.md §4)."""
    a_out = artifact_results
    d_out = decision_card_results
    if only_flagged:
        a_out = [r for r in a_out if not r.get("relevant", True)]
        d_out = [r for r in d_out if not r.get("relevant", True)]

    report = {
        "audit_metadata": audit_metadata,
        "artifact_results": a_out,
        "decision_card_results": d_out,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    logger.info("JSON report written to %s", output_path)


def write_markdown_report(
    audit_metadata: dict,
    artifact_results: list[dict],
    decision_card_results: list[dict],
    output_path: Path,
) -> None:
    """Write the markdown report with only flagged items (AUDIT_DESIGN.md §5)."""
    flagged_artifacts = [r for r in artifact_results if not r.get("relevant", True)]
    flagged_decisions = [
        r for r in decision_card_results if not r.get("relevant", True)
    ]
    error_items = [
        r for r in artifact_results + decision_card_results if r.get("error")
    ]

    total_a = audit_metadata["total_artifacts"]
    total_d = audit_metadata["total_decision_cards"]
    flagged_a = len(flagged_artifacts)
    flagged_d = len(flagged_decisions)
    pct_a = (flagged_a / total_a * 100) if total_a else 0.0
    pct_d = (flagged_d / total_d * 100) if total_d else 0.0

    lines: list[str] = [
        "# Corpus Relevance Audit Report",
        "",
        f"**Date:** {audit_metadata.get('completed_at', 'N/A')}",
        f"**Model:** {audit_metadata.get('model_used', 'N/A')}",
        f"**Total artifacts:** {total_a} | **Flagged:** {flagged_a} ({pct_a:.1f}%)",
        f"**Total decision cards:** {total_d} | **Flagged:** {flagged_d} ({pct_d:.1f}%)",
        f"**Errors:** {audit_metadata.get('errors', 0)}",
        "",
        "---",
        "",
    ]

    # -- Flagged artifacts table -------------------------------------------
    lines.append("## Flagged Artifacts")
    lines.append("")
    if flagged_artifacts:
        lines.append(
            "| # | Artifact ID | Title | Domain Tags | Confidence | Reason |"
        )
        lines.append(
            "|---|-------------|-------|-------------|------------|--------|"
        )
        for i, r in enumerate(flagged_artifacts, 1):
            aid = r.get("artifact_id", "")
            title = (r.get("title", "") or "").replace("|", "\\|")
            tags = (r.get("domain_tags", "") or "").replace("|", "\\|")
            conf = r.get("confidence", 0.0)
            reason = (r.get("reason", "") or "").replace("|", "\\|")
            lines.append(f"| {i} | {aid} | {title} | {tags} | {conf:.2f} | {reason} |")
    else:
        lines.append("_No artifacts flagged._")
    lines.append("")

    # -- Flagged decision cards table --------------------------------------
    lines.append("## Flagged Decision Cards")
    lines.append("")
    if flagged_decisions:
        lines.append(
            "| # | Decision ID | Question | Capability | Confidence | Reason |"
        )
        lines.append(
            "|---|-------------|----------|------------|------------|--------|"
        )
        for i, r in enumerate(flagged_decisions, 1):
            did = r.get("decision_id", "")
            question = (r.get("question", "") or "").replace("|", "\\|")
            cap = (r.get("capability", "") or "").replace("|", "\\|")
            conf = r.get("confidence", 0.0)
            reason = (r.get("reason", "") or "").replace("|", "\\|")
            lines.append(
                f"| {i} | {did} | {question} | {cap} | {conf:.2f} | {reason} |"
            )
    else:
        lines.append("_No decision cards flagged._")
    lines.append("")

    # -- Errors table ------------------------------------------------------
    lines.append("## Errors")
    lines.append("")
    if error_items:
        lines.append("| # | Item ID | Type | Error |")
        lines.append("|---|---------|------|-------|")
        for i, r in enumerate(error_items, 1):
            if "artifact_id" in r:
                item_id = r["artifact_id"]
                item_type = "artifact"
            else:
                item_id = r.get("decision_id", "")
                item_type = "decision"
            error_text = (r.get("error", "") or "").replace("|", "\\|")
            lines.append(f"| {i} | {item_id} | {item_type} | {error_text} |")
    else:
        lines.append("_No errors._")
    lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    logger.info("Markdown report written to %s", output_path)


# ---------------------------------------------------------------------------
# Section 6: CLI and main orchestration
# ---------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser (AUDIT_DESIGN.md §6)."""
    settings = get_settings()

    parser = argparse.ArgumentParser(
        description=(
            "Audit corpus relevance — flag off-topic artifacts and decision cards "
            "using an LLM judge."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--db-url",
        default=settings.db_url,
        help=f"SQLAlchemy database URL (default: {settings.db_url})",
    )
    parser.add_argument(
        "--base-url",
        default=settings.llm_base_url,
        help=f"OpenAI-compatible API base URL (default: {settings.llm_base_url})",
    )
    parser.add_argument(
        "--api-key",
        default=(
            os.environ.get("OPENAI_API_KEY")
            or settings.kilo_api_key
            or _FALLBACK_API_KEY
        ),
        help="API key (default: OPENAI_API_KEY env var > CORPUS_KILO_API_KEY > built-in key)",
    )
    parser.add_argument(
        "--model",
        default=settings.llm_model,
        help=f"LLM model identifier (default: {settings.llm_model})",
    )
    parser.add_argument(
        "--max-content-chars",
        type=int,
        default=4000,
        help="Max characters of content sent per item (default: 4000)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Seconds between API calls (default: 0.5)",
    )
    parser.add_argument(
        "--max-calls",
        type=int,
        default=0,
        help="Max total LLM calls; 0 = unlimited (default: 0)",
    )
    parser.add_argument(
        "--output-dir",
        default="data",
        help="Directory for output files (default: data)",
    )
    parser.add_argument(
        "--checkpoint",
        default="data/relevance_audit_checkpoint.json",
        help="Checkpoint file path for resume (default: data/relevance_audit_checkpoint.json)",
    )
    parser.add_argument(
        "--skip-artifacts",
        action="store_true",
        help="Skip artifact auditing",
    )
    parser.add_argument(
        "--skip-decisions",
        action="store_true",
        help="Skip decision card auditing",
    )
    parser.add_argument(
        "--only-flagged",
        action="store_true",
        help="Only write flagged items to JSON output",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List items to audit without calling the LLM",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable DEBUG-level logging",
    )
    return parser


def main() -> None:  # noqa: C901 — orchestration function, intentionally linear
    """Entry point for the corpus relevance audit."""
    args = build_parser().parse_args()

    # -- Logging -----------------------------------------------------------
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    started_at = datetime.now(timezone.utc).isoformat()
    logger.info("Corpus relevance audit starting")
    logger.info("Model: %s | Base URL: %s", args.model, args.base_url)
    logger.info(
        "Max content chars: %d | Delay: %.1fs | Max calls: %s",
        args.max_content_chars,
        args.delay,
        args.max_calls or "unlimited",
    )

    # -- Database access ---------------------------------------------------
    engine = create_db_engine(args.db_url)

    with get_session(engine) as session:
        repo = CorpusRepository(session)

        artifacts = [] if args.skip_artifacts else repo.list_artifacts()
        decisions = [] if args.skip_decisions else repo.list_decision_cards()

        logger.info(
            "Found %d artifacts and %d decision cards",
            len(artifacts),
            len(decisions),
        )

        # -- Dry-run mode --------------------------------------------------
        if args.dry_run:
            _print_dry_run(artifacts, decisions, args.max_calls)
            return

        # -- Checkpoint load -----------------------------------------------
        checkpoint_path = Path(args.checkpoint)
        ckpt = CheckpointManager(checkpoint_path)
        completed_ids, partial_results = ckpt.load()

        # Split partial results into per-type buckets
        artifact_results: list[dict] = [
            r for r in partial_results if "artifact_id" in r
        ]
        decision_results: list[dict] = [
            r for r in partial_results if "decision_id" in r
        ]

        # -- Validate API key ----------------------------------------------
        if not args.api_key or args.api_key == "anonymous":
            logger.error(
                "No API key configured. "
                "Set CORPUS_KILO_API_KEY or OPENAI_API_KEY, or pass --api-key."
            )
            sys.exit(1)

        auditor = RelevanceAuditor(
            base_url=args.base_url,
            api_key=args.api_key,
            model=args.model,
            max_content_chars=args.max_content_chars,
            delay=args.delay,
        )

        call_count = 0
        consecutive_failures = 0
        aborted = False

        # -- Phase 1: Artifacts --------------------------------------------
        if not args.skip_artifacts:
            already_done = sum(
                1 for a in artifacts if a.artifact_id in completed_ids
            )
            logger.info(
                "Phase: artifacts (%d total, %d already done)",
                len(artifacts),
                already_done,
            )
            for i, artifact in enumerate(artifacts):
                if artifact.artifact_id in completed_ids:
                    continue
                if args.max_calls and call_count >= args.max_calls:
                    logger.info("Reached --max-calls limit (%d)", args.max_calls)
                    break
                if consecutive_failures >= _MAX_CONSECUTIVE_FAILURES:
                    logger.error(
                        "%d consecutive failures — aborting. "
                        "Resume with --checkpoint.",
                        _MAX_CONSECUTIVE_FAILURES,
                    )
                    aborted = True
                    break

                logger.debug(
                    "Auditing artifact %d/%d: %s",
                    i + 1,
                    len(artifacts),
                    artifact.title,
                )

                result = auditor.audit_artifact(artifact)
                call_count += 1

                if result.get("error"):
                    consecutive_failures += 1
                else:
                    consecutive_failures = 0

                artifact_results.append(result)
                completed_ids.add(artifact.artifact_id)
                ckpt.save(
                    completed_ids,
                    artifact_results + decision_results,
                    "artifacts",
                )

                if call_count % _PROGRESS_LOG_INTERVAL == 0:
                    logger.info("Progress: %d LLM calls completed", call_count)

                # Rate-limit delay (skip after last item)
                if args.delay > 0 and i < len(artifacts) - 1:
                    time.sleep(args.delay)

        # -- Phase 2: Decision Cards ---------------------------------------
        if not args.skip_decisions and not aborted:
            already_done = sum(
                1 for d in decisions if d.decision_id in completed_ids
            )
            logger.info(
                "Phase: decision cards (%d total, %d already done)",
                len(decisions),
                already_done,
            )
            for i, card in enumerate(decisions):
                if card.decision_id in completed_ids:
                    continue
                if args.max_calls and call_count >= args.max_calls:
                    logger.info("Reached --max-calls limit (%d)", args.max_calls)
                    break
                if consecutive_failures >= _MAX_CONSECUTIVE_FAILURES:
                    logger.error(
                        "%d consecutive failures — aborting. "
                        "Resume with --checkpoint.",
                        _MAX_CONSECUTIVE_FAILURES,
                    )
                    aborted = True
                    break

                logger.debug(
                    "Auditing decision card %d/%d: %s",
                    i + 1,
                    len(decisions),
                    card.question,
                )

                result = auditor.audit_decision_card(card)
                call_count += 1

                if result.get("error"):
                    consecutive_failures += 1
                else:
                    consecutive_failures = 0

                decision_results.append(result)
                completed_ids.add(card.decision_id)
                ckpt.save(
                    completed_ids,
                    artifact_results + decision_results,
                    "decisions",
                )

                if call_count % _PROGRESS_LOG_INTERVAL == 0:
                    logger.info("Progress: %d LLM calls completed", call_count)

                if args.delay > 0 and i < len(decisions) - 1:
                    time.sleep(args.delay)

        # -- Write final outputs -------------------------------------------
        completed_at = datetime.now(timezone.utc).isoformat()
        all_results = artifact_results + decision_results
        total_errors = sum(1 for r in all_results if r.get("error"))
        artifacts_flagged = sum(
            1 for r in artifact_results if not r.get("relevant", True)
        )
        decisions_flagged = sum(
            1 for r in decision_results if not r.get("relevant", True)
        )

        audit_metadata: dict = {
            "started_at": started_at,
            "completed_at": completed_at,
            "model_used": args.model,
            "base_url": args.base_url,
            "max_content_chars": args.max_content_chars,
            "total_artifacts": len(artifacts),
            "total_decision_cards": len(decisions),
            "artifacts_flagged": artifacts_flagged,
            "decision_cards_flagged": decisions_flagged,
            "errors": total_errors,
        }

        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        write_json_report(
            audit_metadata=audit_metadata,
            artifact_results=artifact_results,
            decision_card_results=decision_results,
            output_path=output_dir / "relevance_audit.json",
            only_flagged=args.only_flagged,
        )
        write_markdown_report(
            audit_metadata=audit_metadata,
            artifact_results=artifact_results,
            decision_card_results=decision_results,
            output_path=output_dir / "relevance_audit.md",
        )

        # Clean checkpoint on success (not aborted, not max-calls partial)
        all_artifact_ids = {a.artifact_id for a in artifacts}
        all_decision_ids = {d.decision_id for d in decisions}
        all_expected = all_artifact_ids | all_decision_ids
        if not aborted and completed_ids >= all_expected:
            ckpt.delete()
        elif not aborted:
            logger.info(
                "Partial run (max-calls or skips) — checkpoint preserved for resume"
            )

        # -- Summary -------------------------------------------------------
        logger.info("=" * 60)
        logger.info("Audit complete: %d LLM calls", call_count)
        logger.info(
            "Artifacts: %d total, %d flagged | "
            "Decisions: %d total, %d flagged | "
            "Errors: %d",
            len(artifacts),
            artifacts_flagged,
            len(decisions),
            decisions_flagged,
            total_errors,
        )
        if aborted:
            logger.warning(
                "Run was aborted due to consecutive failures. "
                "Use --checkpoint to resume."
            )
        logger.info("=" * 60)


def _print_dry_run(
    artifacts: list, decisions: list, max_calls: int
) -> None:
    """Print a summary of items that would be audited (no LLM calls)."""
    sep = "=" * 60
    print(f"\n{sep}")
    print(f"DRY RUN — {len(artifacts)} artifacts, {len(decisions)} decision cards")
    print(f"{sep}\n")

    if artifacts:
        print("ARTIFACTS:")
        for a in artifacts:
            print(f"  [{a.artifact_id}] {a.title}  ({a.domain_tags})")

    if decisions:
        print("\nDECISION CARDS:")
        for d in decisions:
            print(f"  [{d.decision_id}] {d.question}  ({d.capability})")

    total = len(artifacts) + len(decisions)
    print(f"\nTotal items: {total}")
    if max_calls:
        print(f"Max LLM calls: {max_calls}")
    print()


if __name__ == "__main__":
    main()
