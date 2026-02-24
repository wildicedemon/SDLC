# Domain Report: Testing & Validation

## A. Executive Summary

This report covers testing architecture, quality gates, and validation strategies for the SDLC Framework. The framework mandates evidence-first completion: no task is marked done without passing test output, artifact files, or successful CLI execution logs. Testing spans four levels (unit, integration, E2E, performance) with an 80% coverage floor on critical paths. Quality gates enforce compile, test, integration, and full-suite checks at defined boundaries. Key gaps include absence of mutation testing, formal verification tooling, and automated test generation capabilities.

*Sources: Research.md §V (SDLC Automation), §2.3 (quality gates, evidence-first); start_prompt.md §4.6, §6.2, §7.8*

## B. Core Concepts

- **Evidence-first completion**: Tests must produce passing output logs; scanner passes must produce artifacts; CLI commands must exit without error codes *(Research.md §2.3)*
- **Four-level test pyramid**: Unit > Integration > E2E > Performance; each level has distinct scope and triggers *(start_prompt.md §4.6)*
- **80% coverage floor**: Minimum coverage on critical paths; test gate blocks phase promotion below threshold *(start_prompt.md §4.6)*
- **Quality gate enforcement**: Compile gate at phase 2>3; test gate every 5 tasks; integration gate at phase boundaries; full suite before completion *(start_prompt.md §6.2)*
- **Gate failure triggers Debug mode**: Failed gates create remediation subtasks automatically *(see [Orchestration Report §C](./orchestration_workflow.md#c-implementation-guidance))*
- **Mock external dependencies**: All tests must mock MCP servers, APIs, and external services *(start_prompt.md §4.6)*
- **Happy and sad path coverage**: Both success and failure scenarios tested for all critical flows *(Research.md §V.15)*
- **Multi-stage validated testing**: Validation pipelines with sequential pass/fail gates *(Research.md §V.15)*
- **Automated repair looping**: Test failures feed back into code repair cycles *(Research.md §IV.14)*
- **Test data lifecycle management**: Synthetic data generation and cleanup per test run *(Research.md §VI.18)*
- **Runtime validation**: Production-like checks during integration and E2E tests *(Research.md §V.15)*

## C. Implementation Guidance

### What to Build

| Component | Location | Purpose |
|-----------|----------|---------|
| Unit test suite | `tests/unit/` | Per-module tests with pytest |
| Integration test suite | `tests/integration/` | CLI command execution tests |
| E2E test suite | `tests/e2e/` | Full SDLC pipeline flow tests via Playwright |
| Performance benchmarks | `tests/performance/` | Regression detection for key operations |
| Quality gate runner | `src/framework/quality-gates.ts` | Enforces compile/test/integration/full-suite gates |
| Test coverage reporter | CI pipeline config | Coverage collection and threshold enforcement |
| Verification checklist validator | `src/framework/verify.ts` | Automated checklist evaluation per task |

### How to Build It

- **pytest for Python components**: Unit and integration tests for CLI scripts, LangGraph integration, scanner passes *(start_prompt.md §0; Research.md §V.15)*
- **Playwright for E2E**: Full SDLC flow tests exercising CLI > LangGraph > mode transitions > output verification *(start_prompt.md §4.4.7)*
- **Quality gate runner**: TypeScript module that evaluates gate conditions at defined checkpoints; returns pass/fail with remediation context *(start_prompt.md §6.2)*
- **Coverage enforcement**: Configure coverage tools to fail CI below 80% on critical path modules *(start_prompt.md §4.6)*
- **Mock strategy**: Mock MCP servers via fixture factories; mock GitHub webhooks via test HTTP server; mock Langfuse via stub client *(start_prompt.md §4.6)*
- **Verification checklist**: Programmatic evaluation of the 8-item checklist from start_prompt.md §4.6; each item maps to a test assertion

### Why This Approach

- pytest + Playwright are already specified in the technology stack; no additional framework dependencies needed *(Master Report §3)*
- Quality gates at defined checkpoints prevent accumulated technical debt from blocking late-stage work
- Evidence-first completion eliminates false progress reporting that plagues self-reported status systems *(Master Report D-9)*
- Mocking external dependencies ensures tests run in isolation without network or service availability concerns

### Dependencies

- pytest and Playwright must be installed (via bootstrap) *(see [Master Report §2.7](./sdlc_framework_master_report.md#27-bootstrap--self-provisioning))*
- CI pipeline must be configured to run test suites and collect coverage *(see [Master Report §5.4](./sdlc_framework_master_report.md#54-cicd-pipelines))*
- Quality gate runner depends on mode transition controller *(see [Orchestration Report §C](./orchestration_workflow.md#c-implementation-guidance))*
- Scanner pass tests depend on Deep Scanner implementation *(see [Master Report §2.4](./sdlc_framework_master_report.md#24-deep-scanner))*

## D. Validation Criteria

| Criterion | Metric | Method |
|-----------|--------|--------|
| Unit test coverage | >= 80% on critical paths | Coverage tool report in CI |
| Integration tests | All CLI commands execute successfully | `framework start\|status\|scan\|bootstrap` test suite |
| E2E tests | Full SDLC flow completes without errors | Playwright test: Research > Plan > Implement > Verify |
| Performance | No regressions vs. baseline benchmarks | Benchmark comparison in CI |
| Scanner tests | All 4 passes execute and persist findings | Integration test per scanner pass |
| Quality gates | Gates trigger at correct boundaries | Unit test: gate condition evaluation |
| Evidence production | Every completed task has associated artifact | Verification script checks artifact existence |
| Error paths | All error conditions produce actionable messages | Sad-path test coverage |
| Workspace hygiene | Clean branches, committed state after tests | Git status assertion in CI |

## E. Known Gaps & Risks

| Gap/Risk | Severity | Mitigation |
|----------|----------|------------|
| No mutation testing framework selected | Medium | Research.md lists mutation testing as a research target; no tool selected yet *(Research.md §V.15)* |
| No formal verification or theorem prover integration | Low | Listed in Research.md §V.15 as research target; not required for initial delivery |
| No automatic test generation capability | Medium | Research.md identifies this as Tier 1 research; manual test writing required initially *(Research.md §V.15)* |
| Contract testing absent | Medium | Service-level and component-level contract testing not yet specified *(Research.md §V.15)* |
| Test data lifecycle not automated | Low | Synthetic data generation listed in Research.md §VI.18 but not yet implemented |
| Performance baseline undefined | Medium | No baseline benchmarks established; first run will establish baselines |
| E2E test environment requirements unclear | Medium | Full pipeline test requires LangGraph, MCP servers, Kilo Code; environment setup complexity is high |
| Flaky test detection absent | Low | No mechanism for identifying and quarantining intermittent failures |

## F. Decision Log

### Resolved Decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| T-1 | pytest for Python testing | Already in technology stack; well-supported for unit and integration testing *(start_prompt.md §0)* |
| T-2 | Playwright for E2E testing | Already in dependency list; supports browser and CLI testing *(start_prompt.md §4.4.7)* |
| T-3 | 80% coverage floor on critical paths | Balances coverage with development velocity; blocks promotion below threshold *(start_prompt.md §4.6)* |
| T-4 | Quality gates at defined checkpoints | Prevents accumulated debt; enforced at every 5 tasks, phase boundaries, and completion *(start_prompt.md §6.2)* |
| D-9 | Evidence-first completion | Tests/artifacts must exist before done; prevents false progress *(Research.md §2.3)* |

### Open Decisions

| ID | Question | Options | Recommendation |
|----|----------|---------|----------------|
| T-O1 | Mutation testing tool | mutmut (Python), Stryker (TypeScript), none initially | Defer; add after core test suites are stable |
| T-O2 | Contract testing approach | Pact, custom schema validation, none initially | Evaluate when inter-service boundaries are defined |
| T-O3 | Automatic test generation strategy | LLM-based, property-based (Hypothesis), manual only | Start manual; add property-based testing for data-heavy modules |
| T-O4 | Performance benchmark tooling | pytest-benchmark, custom scripts, k6 for HTTP | pytest-benchmark for unit-level; custom for CLI timing |

*Cross-references: See [Master Report §4](./sdlc_framework_master_report.md#4-workflow-lifecycle) for phase verification details; [Orchestration Report §D](./orchestration_workflow.md#d-validation-criteria) for gate trigger validation.*
