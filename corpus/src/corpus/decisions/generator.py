"""Generate DecisionCards from ingested artifacts using LLM deep research.

Groups artifacts by domain, retrieves relevant chunks from ChromaDB, and
uses an LLM (default: perplexity/sonar-deep-research) to synthesize
concise, evidence-backed decision cards.
"""

from __future__ import annotations

import json
import logging
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone

import chromadb
from openai import OpenAI
from sqlalchemy.orm import Session

from corpus.config import CorpusSettings, get_settings
from corpus.db.repository import CorpusRepository

logger = logging.getLogger(__name__)

# Domains that are metadata/structural — not worth a decision card
_SKIP_DOMAINS = frozenset(
    {
        "meta",
        "indices",
        "progress",
        "extractions",
        "research_root",
        "distillation",
        "distilled",
        # Numbered duplicates of existing domains
        "01_meta_architecture",
        "02_agent_orchestration",
        "03_context_memory_intelligence",
        "04_code_intelligence",
        "05_sdlc_automation",
        "06_data_infrastructure",
        "07_human_interaction",
        "08_model_management",
        "09_research_discipline",
        "11_advanced_runtime",
        "12_self_improvement",
    }
)

_SYSTEM_PROMPT = """\
You are a senior engineering advisor synthesising a **Decision Card** — a \
concise reference that helps an engineering team make a specific technical \
decision.

You will receive:
1. A **domain** name (the technical area).
2. **Corpus excerpts** — internal research notes the team already gathered.

Your job:
- Use the corpus excerpts as starting context, then **research further** to \
find real-world metrics, benchmarks, case studies, comparisons, failure modes, \
and best practices.
- Produce ONE Decision Card as a JSON object (schema below).
- Be **concise and dense** — every sentence should carry information. No filler.
- Prefer quantified evidence (percentages, latency numbers, adoption stats) \
over vague claims.
- State where the approach **excels**, where it **fails**, and what the \
**trade-offs** are.

### JSON Schema (respond with ONLY this JSON, no markdown fences):

{
  "question": "The specific decision question this card answers (e.g. 'Which context management strategy should we use for AI coding agents?')",
  "recommendation": "The recommended approach in 2-4 sentences. Include the core 'what' and 'why'.",
  "alternatives": "2-3 viable alternatives with 1-sentence trade-off for each, separated by semicolons.",
  "constraints": "Conditions or prerequisites where this recommendation applies (e.g. team size, scale, language).",
  "confidence_score": 0.85,
  "confidence_level": "high | medium | low",
  "confidence_explanation": "Why this confidence level — cite source diversity, evidence strength, recency.",
  "has_unresolved_contradiction": false,
  "revisit_triggers": "Concrete events that should trigger re-evaluation (e.g. 'New framework release', 'Team grows past 20')."
}

Rules:
- confidence_score: 0.0–1.0 float.  high ≥ 0.75, medium 0.50–0.74, low < 0.50.
- If sources conflict, set has_unresolved_contradiction to true and explain in confidence_explanation.
- Keep the total JSON under 600 words.
- Do NOT wrap in markdown code fences. Return raw JSON only.
"""


def _user_prompt(domain: str, chunks: list[str]) -> str:
    joined = "\n---\n".join(chunks)
    return (
        f"**Domain:** {domain.replace('_', ' ').title()}\n\n"
        f"**Internal corpus excerpts (use as starting context, then research further):**\n\n"
        f"{joined}\n\n"
        f"Synthesise the Decision Card JSON for this domain."
    )


@dataclass
class GenerationReport:
    generated: int = 0
    skipped_existing: int = 0
    skipped_structural: int = 0
    failed: int = 0
    details: list[str] = field(default_factory=list)


def generate_decisions(
    session: Session,
    run_id: str,
    settings: CorpusSettings | None = None,
    domains: list[str] | None = None,
    dry_run: bool = False,
) -> GenerationReport:
    """Generate DecisionCards for each domain in the corpus.

    Args:
        session: DB session.
        run_id: The consolidation run to pull artifacts from.
        settings: Corpus settings (auto-loaded if None).
        domains: Optional list of specific domains to generate for.
                 If None, generates for all non-structural domains.
        dry_run: If True, log what would be generated but don't call LLM or write DB.
    """
    if settings is None:
        settings = get_settings()

    repo = CorpusRepository(session)
    report = GenerationReport()

    # --- Collect domains from artifacts ---
    artifacts = repo.list_artifacts(run_id=run_id)
    if not artifacts:
        logger.warning("No artifacts found for run %s", run_id)
        return report

    domain_artifacts: dict[str, list[str]] = {}
    for art in artifacts:
        tags = json.loads(str(art.domain_tags)) if art.domain_tags else []
        for tag in tags:
            domain_artifacts.setdefault(tag, []).append(str(art.artifact_id))

    # Filter to requested domains or all non-structural
    target_domains = sorted(domain_artifacts.keys())
    if domains:
        target_domains = [d for d in target_domains if d in domains]
    target_domains = [d for d in target_domains if d not in _SKIP_DOMAINS]

    # Skip domains that already have a card
    existing_cards = repo.list_decision_cards()
    existing_capabilities = {str(c.capability) for c in existing_cards}

    logger.info(
        "Targeting %d domains for decision card generation (run=%s)",
        len(target_domains),
        run_id,
    )

    # --- Set up ChromaDB + LLM ---
    try:
        chroma = chromadb.PersistentClient(path=settings.chroma_dir)
        collection = chroma.get_collection("corpus_chunks")
    except Exception:
        logger.error("ChromaDB collection not found — run the pipeline first")
        return report

    client = OpenAI(
        base_url=settings.llm_base_url,
        api_key=settings.kilo_api_key,
        max_retries=1,
        timeout=120.0,  # deep research can be slow
    )

    for i, domain in enumerate(target_domains):
        if domain in existing_capabilities:
            report.skipped_existing += 1
            report.details.append(f"SKIP (exists): {domain}")
            continue

        if domain in _SKIP_DOMAINS:
            report.skipped_structural += 1
            continue

        logger.info(
            "[%d/%d] Generating decision card for: %s",
            i + 1,
            len(target_domains),
            domain,
        )

        # Retrieve top chunks for this domain from vector store
        query_text = domain.replace("_", " ")
        try:
            results = collection.query(query_texts=[query_text], n_results=8)
            chunks = results["documents"][0] if results["documents"] else []
        except Exception:
            chunks = []

        # Truncate each chunk to keep prompt manageable
        chunks = [c[:600] for c in chunks]

        if dry_run:
            report.generated += 1
            report.details.append(f"DRY RUN: {domain} ({len(chunks)} chunks)")
            continue

        # --- Call LLM ---
        try:
            resp = client.chat.completions.create(
                model=settings.decision_model,
                messages=[
                    {"role": "system", "content": _SYSTEM_PROMPT},
                    {"role": "user", "content": _user_prompt(domain, chunks)},
                ],
                max_tokens=4000,
            )
            raw = (resp.choices[0].message.content or "").strip()

            # Strip markdown fences if present
            if raw.startswith("```"):
                lines = raw.split("\n")
                raw = "\n".join(
                    l for l in lines if not l.strip().startswith("```")
                ).strip()

            start = raw.find("{")
            end = raw.rfind("}") + 1
            if start < 0 or end <= start:
                # Try to repair truncated JSON by closing braces
                if start >= 0:
                    raw_attempt = raw[start:] + '"}'  
                    try:
                        card_data = json.loads(raw_attempt)
                    except json.JSONDecodeError:
                        raise ValueError(f"Truncated/malformed JSON: {raw[start:start+200]}")
                else:
                    raise ValueError(f"No JSON object found in response: {raw[:200]}")
            else:
                card_data = json.loads(raw[start:end])

        except Exception as exc:
            report.failed += 1
            report.details.append(f"FAIL: {domain} — {type(exc).__name__}: {str(exc)[:120]}")
            logger.warning("Failed to generate card for %s: %s", domain, exc)
            time.sleep(1)
            continue

        # --- Validate and insert ---
        conf_score = float(card_data.get("confidence_score", 0.5))
        conf_level = str(card_data.get("confidence_level", "medium"))
        if conf_level not in ("high", "medium", "low"):
            conf_level = "high" if conf_score >= 0.75 else "medium" if conf_score >= 0.5 else "low"

        decision_id = f"dc_{uuid.uuid4().hex[:16]}"
        now = datetime.now(timezone.utc).isoformat()

        provenance = ",".join(domain_artifacts.get(domain, [])[:10])

        repo.create_decision_card(
            decision_id=decision_id,
            question=str(card_data.get("question", f"What approach for {domain}?")),
            capability=domain,
            constraints=str(card_data.get("constraints", "")),
            recommendation=str(card_data.get("recommendation", "")),
            alternatives=str(card_data.get("alternatives", "")),
            confidence_score=conf_score,
            confidence_level=conf_level,
            confidence_explanation=str(card_data.get("confidence_explanation", "")),
            has_unresolved_contradiction=bool(card_data.get("has_unresolved_contradiction", False)),
            provenance_refs=provenance,
            last_validated_at=now,
            revisit_triggers=str(card_data.get("revisit_triggers", "")),
            status="active",
        )

        # Also create capability mapping
        repo.create_capability_mapping(
            capability=domain,
            decision_id=decision_id,
            domain=domain,
        )

        session.commit()

        report.generated += 1
        report.details.append(
            f"OK: {domain} -> {decision_id} (confidence={conf_score:.2f}/{conf_level})"
        )
        logger.info(
            "  Created %s — %s (confidence=%.2f)",
            decision_id,
            card_data.get("question", domain)[:60],
            conf_score,
        )

        # Rate-limit delay — deep research is slow anyway but be polite
        if i < len(target_domains) - 1:
            time.sleep(2)

    return report
