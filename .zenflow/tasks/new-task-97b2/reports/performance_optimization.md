# Domain Report: Performance & Optimization

## A. Executive Summary

This report covers cost modeling, token efficiency, resource telemetry, waste detection, dynamic model routing, and profiling strategies for the SDLC Framework. Research identifies token waste as the primary cost driver in autonomous agent systems, with >15K tokens per task without progress as the warning threshold. The framework requires integrated observability via Langfuse, budget enforcement at phase and task levels, and cost-aware model selection. Critical gaps include undefined performance baselines, absence of latency benchmarks for CLI and scanner operations, and no implemented cache strategy for repeated code analysis.

*Sources: Research.md §I.2 (Economic & Optimization Modeling), §V.17 (Observability & Feedback Loops), §VIII.21 (Model Capability Management); start_prompt.md §4.4.5 (Waste Detection), §6.4 (Resource Management), §3.3 (Code Quality and Performance)*

## B. Core Concepts

- **Token efficiency tracking**: Per-operation and per-task token accounting with cost rollup to phase and initiative levels *(start_prompt.md §4.4.5)*
- **Waste detection rules**: >15K tokens without progress triggers warning; >30K triggers pause; repeated same errors trigger escalation; loop detection triggers break-and-report *(start_prompt.md §4.4.5)*
- **Cost-per-task modeling**: Calculate monetary cost per task based on model pricing and token consumption *(Research.md §I.2)*
- **Budget enforcement at checkpoints**: Warn at 50% of phase budget; pause at 80% without justification; escalate at 100% or overrun *(start_prompt.md §6.4)*
- **Dynamic model routing**: Select model per task based on cost, capability, and latency tradeoffs *(Research.md §VIII.21; see [Master Report §7 O-2](../sdlc_framework_master_report.md#open-decisions))*
- **Langfuse integration**: Observability dashboard for token usage, cost tracking, and telemetry pipelines *(start_prompt.md §4.4.5)*
- **Resource utilization telemetry**: Track CPU, RAM, disk, and API call consumption per component *(Research.md §I.2)*
- **Latency vs. intelligence tradeoff**: Faster/cheaper models for routine tasks; larger models for complex reasoning *(Research.md §I.2)*
- **Cache strategy design**: Reuse prior analysis results for unchanged files to avoid redundant computation *(Research.md §I.2)*
- **Cold start optimization**: Minimize bootstrap and first-scan latency *(Research.md §VI.19; see [Environment Report §E](./environment_infrastructure.md#e-known-gaps--risks))*
- **Loop detection**: Identify repeated error patterns or stalled progress to prevent infinite retry cycles *(start_prompt.md §4.4.5)*
- **ROI measurement per workflow**: Track value delivered vs. cost incurred per SDLC phase *(Research.md §I.2)*
- **Temperature optimization**: Per-task model temperature tuning for determinism vs. creativity tradeoff *(Research.md §VIII.21; seed source: Roocode model temperature docs)*
- **Performance regression detection**: Compare current metrics against baselines to catch degradation *(Research.md §XII.26)*

## C. Implementation Guidance

### What to Build

| Component | Location | Purpose |
|-----------|----------|---------|
| Waste detector | `src/observability/waste-detector.ts` | Evaluates waste rules per operation |
| Cost tracker | `src/observability/cost-tracker.ts` | Calculates cost per task, per phase |
| Langfuse client | `src/observability/langfuse-client.ts` | Sends telemetry to Langfuse dashboard |
| Token counter | `src/observability/token-counter.ts` | Counts tokens per LLM request/response |
| Budget enforcer | `src/observability/budget-enforcer.ts` | Checkpoint-based budget threshold checks |
| Performance benchmarks | `tests/performance/` | Baseline and regression benchmarks |

### How to Build It

- **Waste detector**: Subscribe to LLM request events; accumulate token count per task; evaluate rules (15K warn, 30K pause, repeated errors escalate, loop detection break); emit alerts via callback or notification *(start_prompt.md §4.4.5)*
- **Cost tracker**: Maintain a running ledger per task and phase; compute cost from model pricing table x token count; persist to `.framework/logs/cost/` for audit *(start_prompt.md §4.4.5)*
- **Langfuse client**: Initialize Langfuse SDK with project key; instrument each LLM call with trace context (task ID, phase, mode); send spans for token usage, latency, and outcome *(start_prompt.md §4.4.5)*
- **Token counter**: Wrap LLM client to intercept request/response; extract token counts from API response metadata; fall back to tokenizer estimation if metadata unavailable
- **Budget enforcer**: At each checkpoint (every 5 tasks, at 50% budget, before architectural decisions), compare accumulated cost against phase budget; return warn/pause/escalate action *(start_prompt.md §6.4)*
- **Performance benchmarks**: Establish baselines for CLI command latency, scanner pass duration, and LangGraph state transition time; compare on each CI run *(start_prompt.md §3.3)*

### Why This Approach

- Token-level granularity enables precise cost attribution and waste identification
- Threshold-based rules (15K/30K) provide automated circuit breakers without human monitoring
- Langfuse is already in the technology stack; avoids adding another observability tool *(see [Master Report §3](../sdlc_framework_master_report.md#3-technology-stack))*
- Budget enforcement at checkpoints aligns with the orchestration checkpoint protocol *(see [Orchestration Report §B](./orchestration_workflow.md#b-core-concepts))*
- Baselines established on first run; regressions detected automatically on subsequent runs

### Dependencies

- Langfuse must be installed and API key configured (via bootstrap) *(see [Environment Report §C](./environment_infrastructure.md#c-implementation-guidance))*
- LLM client must support token count extraction or provide response metadata
- Checkpoint enforcement depends on orchestration progress tracker *(see [Orchestration Report §C](./orchestration_workflow.md#c-implementation-guidance))*
- Cost pricing table must be maintained per model in `.framework/config.yaml`

## D. Validation Criteria

| Criterion | Metric | Method |
|-----------|--------|--------|
| Token counting accuracy | Counts match LLM API response metadata | Unit test: compare counter output vs. known API response |
| Waste detection: warn threshold | Alert emitted at 15K tokens without progress | Unit test: simulate 15K tokens, no task state change |
| Waste detection: pause threshold | Execution paused at 30K tokens without progress | Unit test: simulate 30K tokens, verify pause action |
| Loop detection | Repeated identical errors trigger break | Unit test: feed 3+ identical error strings |
| Cost calculation | Cost = model price x tokens (input + output) | Unit test: known pricing table, known token counts |
| Budget enforcement | Warn at 50%, pause at 80%, escalate at 100% | Unit test: mock accumulated cost at each threshold |
| Langfuse telemetry | Spans sent with correct task/phase metadata | Integration test: verify Langfuse receives expected traces |
| CLI latency | Commands complete within baseline + 10% tolerance | Performance test: time `framework status` over N runs |
| Scanner throughput | All 4 passes complete within configured time bound | Integration test: full scan cycle timing |
| No performance regression | Key operations within baseline thresholds | CI benchmark comparison on each run |

## E. Known Gaps & Risks

| Gap/Risk | Severity | Mitigation |
|----------|----------|------------|
| No performance baselines established | High | First CI run must establish baselines; regressions unmeasurable until then |
| Dynamic model routing not implemented | Medium | Static model config only; cost-based routing deferred *(see [Master Report §7 O-2](../sdlc_framework_master_report.md#open-decisions))* |
| Cache strategy for scanner results undefined | Medium | Scanner re-analyzes unchanged files; caching by file hash deferred *(Research.md §I.2)* |
| Langfuse API key required for observability | Low | Framework functional without Langfuse; observability degraded to local logs |
| Model pricing table not maintained | Medium | Cost calculations require up-to-date pricing; manual update needed per model change |
| Temperature optimization not automated | Low | Per-task temperature tuning specified but requires manual configuration *(Research.md §VIII.21)* |
| No GPU utilization tracking | Low | CPU/RAM tracked; GPU metrics deferred until model serving is local *(Research.md §VI.19)* |
| ROI measurement undefined | Low | Value-per-task metric not quantified; cost tracking alone is insufficient for ROI |
| Notification mechanism for alerts undecided | Medium | Waste alerts need delivery channel; Apprise considered but not selected *(see [Master Report §7 O-7](../sdlc_framework_master_report.md#open-decisions))* |

## F. Decision Log

### Resolved Decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| P-1 | Langfuse for observability/cost tracking | Already in technology stack; provides dashboard, tracing, and cost attribution *(start_prompt.md §4.4.5)* |
| P-2 | 15K/30K token thresholds for waste detection | Concrete, enforceable limits; warn first, then pause; prevents runaway costs *(start_prompt.md §4.4.5)* |
| P-3 | Budget enforcement at orchestration checkpoints | Aligns cost control with existing checkpoint protocol; no separate monitoring loop needed *(start_prompt.md §6.4)* |
| P-4 | Per-task and per-phase cost ledger | Enables granular attribution; supports both real-time alerts and post-hoc analysis *(start_prompt.md §4.4.5)* |
| P-5 | Loop detection via repeated error pattern matching | Simple heuristic; catches common stall patterns without complex analysis *(start_prompt.md §4.4.5)* |

### Open Decisions

| ID | Question | Options | Recommendation |
|----|----------|---------|----------------|
| P-O1 | Model routing strategy | Static config, dynamic cost-based, capability-based | Start static; add dynamic routing as optimization *(see [Master Report §7 O-2](../sdlc_framework_master_report.md#open-decisions))* |
| P-O2 | Cache strategy for scanner results | File-hash based, timestamp-based, none initially | File-hash based; cache invalidation on file content change |
| P-O3 | Performance benchmark tooling | pytest-benchmark, custom timing scripts, k6 | pytest-benchmark for unit-level; custom for CLI *(see [Testing Report §F T-O4](./testing_validation.md#f-decision-log))* |
| P-O4 | Notification delivery for cost alerts | Apprise, Slack webhook, email, log-only | Apprise for multi-channel; log-only as fallback *(see [Master Report §7 O-7](../sdlc_framework_master_report.md#open-decisions))* |
| P-O5 | Model pricing table maintenance | Manual config, API-fetched, vendor webhook | Manual config initially; automate if model changes are frequent |
| P-O6 | Cold start optimization targets | Bootstrap < 60s, first scan < 120s, CLI < 2s | Define after baselines measured; optimize worst offenders first |

*Cross-references: See [Master Report §6](../sdlc_framework_master_report.md#6-performance--compliance) for performance targets overview; [Master Report §2.5](../sdlc_framework_master_report.md#25-waste-detection--cost-oversight) for waste detection component summary; [Orchestration Report §B](./orchestration_workflow.md#b-core-concepts) for checkpoint protocol; [Testing Report §F T-O4](./testing_validation.md#f-decision-log) for benchmark tooling decision.*
