# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Scoring Inputs
- Evidence strength
- Source diversity
- Recency
- Downstream success
- Contradiction penalty

## Default Formula
```text
confidence = 0.30*evidence_strength
           + 0.20*source_diversity
           + 0.20*recency
           + 0.20*downstream_success
           - 0.10*contradiction_penalty
```

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or contradiction density is high.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.
