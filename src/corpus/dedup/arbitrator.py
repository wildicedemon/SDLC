"""LLM arbitration for dedup disagreements — Layer 3 of the dedup pipeline.

When Layer 1 (MinHash) and Layer 2 (embeddings) disagree on whether
two chunks are duplicates, this module asks an LLM to make the final
call.  The LLM returns a JSON verdict with a confidence score and a
recommendation (``merge``, ``keep_both``, or ``discard_one``).

If no API key is configured, or after too many consecutive failures,
all remaining disagreements are auto-resolved as ``keep_both``.

Key function: :func:`arbitrate`.
"""

from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass

from openai import OpenAI

from corpus.dedup.embeddings import Disagreement

logger = logging.getLogger(__name__)

# Maximum consecutive API failures before fast-failing the rest
_MAX_CONSECUTIVE_FAILURES = 10
# Delay in seconds between API calls to avoid rate limits
_CALL_DELAY = 0.3


@dataclass
class ArbitrationResult:
    """Outcome of LLM (or auto-) arbitration for a disagreement pair.

    Attributes:
        chunk_a_id: ID of the first chunk.
        chunk_b_id: ID of the second chunk.
        confidence: Confidence score (0.0–1.0) in the recommendation.
        recommendation: One of ``merge``, ``keep_both``, ``discard_one``,
            or ``human_review``.
    """

    chunk_a_id: str
    chunk_b_id: str
    confidence: float
    recommendation: str


def _auto_resolve(disagreements: list[Disagreement]) -> list[ArbitrationResult]:
    """Auto-resolve disagreements as keep_both with high confidence.

    When L1 and L2 disagree, defaulting to keep_both trusts the embedding
    model (L2) — a reasonable heuristic since embeddings capture semantic
    similarity better than minhash.
    """
    return [
        ArbitrationResult(
            chunk_a_id=d.chunk_a_id,
            chunk_b_id=d.chunk_b_id,
            confidence=0.75,
            recommendation="keep_both",
        )
        for d in disagreements
    ]


def arbitrate(
    disagreements: list[Disagreement],
    base_url: str = "https://api.kilo.ai/api/gateway",
    api_key: str = "",
    model: str = "google/gemini-2.5-flash",
    max_calls: int = 500,
) -> list[ArbitrationResult]:
    """Resolve Layer 1/Layer 2 disagreements via LLM or auto-resolution.

    Processing strategy:

    1. If *api_key* is empty or ``"anonymous"``, auto-resolve everything.
    2. Otherwise, send up to *max_calls* disagreements to the LLM.
    3. Any overflow beyond *max_calls* is auto-resolved.
    4. If ``_MAX_CONSECUTIVE_FAILURES`` API errors occur in a row,
       the remaining batch is also auto-resolved.

    Args:
        disagreements: Pairs where MinHash and embeddings disagree.
        base_url: OpenAI-compatible API base URL.
        api_key: API key for authentication.
        model: Model identifier for the chat completion.
        max_calls: Maximum LLM calls to make before falling back.

    Returns:
        A list of :class:`ArbitrationResult` — one per disagreement.
    """
    if not disagreements:
        return []

    # If no real API key, auto-resolve everything
    if not api_key or api_key == "anonymous":
        logger.info(
            "No API key configured — auto-resolving all %d disagreements as keep_both",
            len(disagreements),
        )
        return _auto_resolve(disagreements)

    # Cap the number of API calls; auto-resolve the rest
    to_arbitrate = disagreements[:max_calls]
    to_auto_resolve = disagreements[max_calls:]

    if to_auto_resolve:
        logger.info(
            "Capping LLM arbitration at %d calls; auto-resolving remaining %d as keep_both",
            len(to_arbitrate),
            len(to_auto_resolve),
        )

    client = OpenAI(base_url=base_url, api_key=api_key, max_retries=1, timeout=30.0)
    results: list[ArbitrationResult] = []
    consecutive_failures = 0
    successful_calls = 0

    for i, d in enumerate(to_arbitrate):
        # Fast-fail after too many consecutive failures
        if consecutive_failures >= _MAX_CONSECUTIVE_FAILURES:
            remaining = to_arbitrate[i:]
            logger.warning(
                "%d consecutive API failures — auto-resolving remaining %d disagreements",
                _MAX_CONSECUTIVE_FAILURES,
                len(remaining),
            )
            results.extend(_auto_resolve(remaining))
            break

        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a deduplication judge. Given two text chunks, "
                            "decide if they are duplicates. Respond ONLY with JSON: "
                            '{"confidence": 0.0-1.0, '
                            '"recommendation": "merge|keep_both|discard_one"}'
                        ),
                    },
                    {
                        "role": "user",
                        "content": f"Chunk A:\n{d.chunk_a_content[:500]}\n\nChunk B:\n{d.chunk_b_content[:500]}",
                    },
                ],
                max_tokens=200,
            )
            raw = (resp.choices[0].message.content or "").strip()
            # Strip markdown code fences if present
            if raw.startswith("```"):
                lines = raw.split("\n")
                raw = "\n".join(
                    l for l in lines if not l.strip().startswith("```")
                ).strip()
            # Extract the JSON object from the response
            start = raw.find("{")
            end = raw.rfind("}") + 1
            if start >= 0 and end > start:
                parsed = json.loads(raw[start:end])
            else:
                parsed = {"confidence": 0.5, "recommendation": "keep_both"}

            consecutive_failures = 0
            successful_calls += 1
            results.append(
                ArbitrationResult(
                    chunk_a_id=d.chunk_a_id,
                    chunk_b_id=d.chunk_b_id,
                    confidence=float(parsed.get("confidence", 0.5)),
                    recommendation=str(parsed.get("recommendation", "keep_both")),
                )
            )

            # Progress logging every 50 calls
            if successful_calls % 50 == 0:
                logger.info(
                    "Arbitration progress: %d/%d calls completed",
                    successful_calls,
                    len(to_arbitrate),
                )

        except (Exception, KeyboardInterrupt) as exc:
            consecutive_failures += 1
            logger.warning(
                "API call %d failed (%s): %s",
                i + 1,
                type(exc).__name__,
                str(exc)[:120],
            )
            # Fallback to keep_both on individual failures
            results.append(
                ArbitrationResult(
                    chunk_a_id=d.chunk_a_id,
                    chunk_b_id=d.chunk_b_id,
                    confidence=0.75,
                    recommendation="keep_both",
                )
            )

        # Rate-limit delay between calls
        if i < len(to_arbitrate) - 1:
            time.sleep(_CALL_DELAY)

    # Append auto-resolved results for the capped overflow
    results.extend(_auto_resolve(to_auto_resolve))

    logger.info(
        "Arbitration complete: %d LLM calls (%d successful), %d auto-resolved",
        min(len(to_arbitrate), len(results)),
        successful_calls,
        len(to_auto_resolve) + (len(to_arbitrate) - successful_calls),
    )

    return results

    return results  # NOTE: unreachable duplicate return (dead code from original port)
