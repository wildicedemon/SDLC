# Skill and Workflow Design Guide (Companion)

## Purpose
Provide stable architecture/design principles so agents build consistent skills/workflows using corpus evidence.

## Invariants
- Skills are single-responsibility.
- Skill interfaces must define explicit inputs/outputs.
- Cross-skill sequencing belongs in orchestrators, not in leaf skills.
- DecisionCards are canonical; BacklogSeeds are generated and replaceable.

## Composition Rules
- Prefer reusable atomic skills over large multi-purpose skills.
- Decompose by capability boundaries, not by tool availability.
- Add retry/recovery at workflow layer.
- Escalate retrieval depth when confidence is low or conflicts are present.

## Prompt Evolution Guardrails
- Prompt changes require benchmark comparison against prior version.
- Apply bounded mutations; avoid unreviewed large prompt rewrites.
- Promote new prompt variants only after measurable improvement.

## Model/Tool Routing Defaults
- Route by capability requirements first (quality/risk), then optimize for latency/cost.
- Maintain explicit fallback chains.
- Log routing decisions for future calibration.

## Quality Gates
- Every workflow has measurable acceptance criteria.
- Confidence calibration is reviewed regularly.
- Contradictions must be represented, not hidden.

# Skill and Workflow Design Guide (Companion)

## Purpose
Provide stable architecture/design principles so agents build consistent skills/workflows using corpus evidence.

## Invariants
- Skills are single-responsibility.
- Skill interfaces must define explicit inputs/outputs.
- Cross-skill sequencing belongs in orchestrators, not in leaf skills.
- DecisionCards are canonical; BacklogSeeds are generated and replaceable.

## Composition Rules
- Prefer reusable atomic skills over large multi-purpose skills.
- Decompose by capability boundaries, not by tool availability.
- Add retry/recovery at workflow layer.
- Escalate retrieval depth when confidence is low or conflicts are present.

## Prompt Evolution Guardrails
- Prompt changes require benchmark comparison against prior version.
- Apply bounded mutations; avoid unreviewed large prompt rewrites.
- Promote new prompt variants only after measurable improvement.

## Model/Tool Routing Defaults
- Route by capability requirements first (quality/risk), then optimize for latency/cost.
- Maintain explicit fallback chains.
- Log routing decisions for future calibration.

## Quality Gates
- Every workflow has measurable acceptance criteria.
- Confidence calibration is reviewed regularly.
- Contradictions must be represented, not hidden.
