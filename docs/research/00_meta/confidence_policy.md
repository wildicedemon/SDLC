# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.

# Confidence Policy

## Purpose
Define how confidence is scored, calibrated, and used for retrieval escalation.

## Confidence Formula
```text
confidence = (min(source_count, 5) / 5.0) × 0.6
           + (max(0, 1 - age_days/730)) × 0.3
           + (success_rate if usage_count ≥ 5 else 0.5) × 0.1
```

## Input Definitions
- `source_count`: Number of independent source artifacts supporting the DecisionCard.
- `age_days`: Days since the DecisionCard was last validated.
- `success_rate`: Observed success ratio from telemetry (`successes / total`) when sufficient usage exists.
- `usage_count`: Number of production or benchmarked uses recorded for the DecisionCard.

## Contradiction Visibility
- `has_unresolved_contradiction`: `true | false`
- This flag must be displayed alongside confidence scores; contradictions are surfaced, not buried in weighted penalties.

## Confidence Bands
- High: `>= 0.75`
- Medium: `0.50 - 0.74`
- Low: `< 0.50`

## Downstream Success Handling
- New DecisionCards with `usage_count < 5` default to neutral downstream term `0.5`.
- DecisionCards with `usage_count >= 5` use actual `success_rate` from telemetry.

## Telemetry Schema
Track downstream outcomes as:
- `(decision_id, timestamp, outcome: success|failure)`

## Escalation Thresholds (Initial)
- Return L1 by default.
- Escalate to L2 when confidence `< 0.70`.
- Escalate to L3 when confidence `< 0.50` or `has_unresolved_contradiction=true`.

## Calibration Cadence
- Weekly: compare predicted confidence vs downstream outcomes.
- Monthly: adjust weights/thresholds if calibration error increases.

## Guardrails
- No recommendation can be High confidence with fewer than 2 independent sources.
- Contradictions unresolved for >1 cycle force max confidence to Medium.
