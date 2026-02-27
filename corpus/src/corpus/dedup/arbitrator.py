from __future__ import annotations

import json
import logging
from dataclasses import dataclass

from openai import OpenAI

from corpus.dedup.embeddings import Disagreement

logger = logging.getLogger(__name__)


@dataclass
class ArbitrationResult:
    chunk_a_id: str
    chunk_b_id: str
    confidence: float
    recommendation: str


def arbitrate(
    disagreements: list[Disagreement],
    base_url: str = "https://api.kilo.ai/api/gateway",
    api_key: str = "",
    model: str = "z-ai/glm-5:free",
) -> list[ArbitrationResult]:
    if not disagreements:
        return []

    client = OpenAI(base_url=base_url, api_key=api_key or "anonymous")
    results: list[ArbitrationResult] = []

    for d in disagreements:
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
                max_tokens=100,
            )
            raw = (resp.choices[0].message.content or "").strip()
            start = raw.find("{")
            end = raw.rfind("}") + 1
            if start >= 0 and end > start:
                parsed = json.loads(raw[start:end])
            else:
                parsed = {"confidence": 0.5, "recommendation": "keep_both"}

            results.append(
                ArbitrationResult(
                    chunk_a_id=d.chunk_a_id,
                    chunk_b_id=d.chunk_b_id,
                    confidence=float(parsed.get("confidence", 0.5)),
                    recommendation=str(parsed.get("recommendation", "keep_both")),
                )
            )
        except Exception:
            logger.warning(
                "Kilo API call failed for pair (%s, %s); routing to human queue",
                d.chunk_a_id,
                d.chunk_b_id,
                exc_info=True,
            )
            results.append(
                ArbitrationResult(
                    chunk_a_id=d.chunk_a_id,
                    chunk_b_id=d.chunk_b_id,
                    confidence=0.0,
                    recommendation="human_review",
                )
            )

    return results
