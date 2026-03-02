# Meta-Orchestrator Parallel Execution Engine

> Dispatches **40 specialized AI agents** across **7 execution tiers** with DAG-based dependency management, parallel execution, retry logic, checkpointing, and dry-run planning.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Prerequisites](#2-prerequisites)
3. [Quick Start](#3-quick-start)
4. [Usage & Configuration](#4-usage--configuration)
5. [Execution Model](#5-execution-model)
6. [Output Structure](#6-output-structure)
7. [Resume Mode](#7-resume-mode)
8. [Error Handling](#8-error-handling)
9. [Manifest & Reports](#9-manifest--reports)
10. [Agent Configuration](#10-agent-configuration)
11. [Examples](#11-examples)
12. [Troubleshooting](#12-troubleshooting)

---

## 1. Overview

The Meta-Orchestrator is a Python-based parallel execution engine that coordinates 40 specialized AI agents organized into 7 dependency-ordered tiers. Each agent is dispatched via the **Kilo Code CLI** (`kilo-code`) in a specific mode (architect, code, research, or review) with an extracted prompt from batch markdown files.

### Key Features

- **DAG-based dependency management** — Validates the directed acyclic graph using Kahn's algorithm before execution
- **Tiered parallel execution** — Tiers execute sequentially; agents within each tier run concurrently
- **Configurable parallelism** — Control simultaneous agent count (`--max-parallel`, default: 8)
- **Retry with exponential backoff** — Failed agents retry with `delay = 30s × 2^attempt`
- **Checkpoint & resume** — Progress saved after each tier; resume from any interruption point
- **Dry-run mode** — Generate a full execution plan without invoking any agents
- **Artifact collection** — SHA-256 manifest of all output files
- **Execution reports** — Per-agent timing, status, and artifact path summaries
- **Graceful shutdown** — Handles SIGINT/SIGTERM for clean interruption
- **Single-agent mode** — Run one agent in isolation for debugging

### Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                     Meta-Orchestrator Engine                        │
│                     (orchestrator.py)                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐   ┌───────────────┐   ┌────────────────────────┐ │
│  │ Config Loader │──▶│ DAG Validator  │──▶│ Checkpoint Manager     │ │
│  │ (JSON)        │   │ (Kahn's Algo) │   │ (Resume Support)       │ │
│  └──────────────┘   └───────────────┘   └────────────────────────┘ │
│                              │                                      │
│                              ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                    Tier Executor                              │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐       (parallel)     │   │
│  │  │ Agent 1 │  │ Agent 2 │  │ Agent N │  ← ThreadPoolExecutor │   │
│  │  └────┬────┘  └────┬────┘  └────┬────┘                       │   │
│  │       │            │            │                             │   │
│  │       ▼            ▼            ▼                             │   │
│  │  ┌──────────────────────────────────────┐                    │   │
│  │  │     Retry Engine (exp. backoff)      │                    │   │
│  │  └──────────────────────────────────────┘                    │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌───────────────────┐  ┌─────────────────┐  ┌──────────────────┐  │
│  │ Artifact Collector │  │ Manifest Writer │  │ Execution Report │  │
│  │ (SHA-256 hashes)  │  │ (manifest.json) │  │ (Markdown)       │  │
│  └───────────────────┘  └─────────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

### File Inventory

| File | Description |
|------|-------------|
| `scripts/orchestrator.py` | Main Python execution engine |
| `scripts/agent_config.json` | 40-agent configuration registry (7 tiers) |
| `scripts/run_orchestrator.sh` | Bash wrapper with pre-flight checks |
| `scripts/run_orchestrator.ps1` | PowerShell wrapper with pre-flight checks |

---

## 2. Prerequisites

| Requirement | Minimum Version | Notes |
|-------------|----------------|-------|
| **Python** | 3.10+ | Standard library only — no pip dependencies |
| **Kilo Code CLI** | — | `kilo-code` command available in `PATH` |
| **OS** | Linux / macOS / Windows | Bash wrapper for Unix; PowerShell 7+ for Windows |

### System Resources

Parallel execution launches multiple agent subprocesses simultaneously. At `--max-parallel 8` (default), expect up to 8 concurrent `kilo-code` processes. Adjust based on available CPU and memory.

---

## 3. Quick Start

### Bash (Linux / macOS)

```bash
# Dry run — see the full execution plan
python scripts/orchestrator.py --dry-run

# Full execution with defaults
python scripts/orchestrator.py

# Via shell wrapper (includes pre-flight checks)
./scripts/run_orchestrator.sh --dry-run
./scripts/run_orchestrator.sh
```

### PowerShell (Windows)

```powershell
# Dry run — see the full execution plan
.\scripts\run_orchestrator.ps1 -DryRun

# Full execution with defaults
.\scripts\run_orchestrator.ps1

# Resume after interruption
.\scripts\run_orchestrator.ps1 -Resume
```

---

## 4. Usage & Configuration

### CLI Options

```
python scripts/orchestrator.py [OPTIONS]
```

| Option | Default | Env Override | Description |
|--------|---------|-------------|-------------|
| `--config PATH` | `scripts/agent_config.json` | — | Path to agent configuration file |
| `--max-parallel N` | `8` | `ORCH_MAX_PARALLEL` | Maximum concurrent agents per tier |
| `--max-retries N` | `2` | — | Maximum retries per failed agent |
| `--timeout N` | `30` | `ORCH_TIMEOUT` | Per-agent timeout in minutes |
| `--dry-run` | `false` | — | Print execution plan without running agents |
| `--resume` | `false` | — | Resume from last checkpoint |
| `--output-dir DIR` | `output/` | — | Directory for agent output artifacts |
| `--log-dir DIR` | `logs/` | — | Directory for logs and checkpoints |
| `--tier N` | *(all)* | — | Run only a specific tier (0–6) |
| `--agent ID` | *(all)* | — | Run only a specific agent (e.g., `AGT-020`) |
| `-v`, `--verbose` | `false` | — | Enable verbose/debug-level logging |

### Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `ORCH_MAX_PARALLEL` | Override maximum concurrent agents | `8` |
| `ORCH_TIMEOUT` | Override per-agent timeout (minutes) | `30` |
| `PYTHON` | Python interpreter for bash wrapper | `python3` |

### PowerShell Parameters

The PowerShell wrapper (`run_orchestrator.ps1`) accepts equivalent named parameters:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `-DryRun` | Switch | — | Print plan without executing |
| `-Resume` | Switch | — | Resume from last checkpoint |
| `-MaxParallel` | Int | `0` (use env/default) | Concurrent agent limit |
| `-MaxRetries` | Int | `2` | Retries per failed agent |
| `-Timeout` | Int | `0` (use env/default) | Per-agent timeout in minutes |
| `-Tier` | Int | `-1` (all tiers) | Run specific tier only |
| `-Agent` | String | `""` (all agents) | Run specific agent ID |
| `-VerboseLog` | Switch | — | Enable debug logging |
| `-OutputDir` | String | `output` | Output directory |
| `-LogDir` | String | `logs` | Log directory |

### Bash Wrapper

The bash wrapper (`run_orchestrator.sh`) performs pre-flight checks before delegating to `orchestrator.py`:

1. Verifies Python 3.10+ is available
2. Confirms `orchestrator.py` and `agent_config.json` exist
3. Passes all remaining arguments through to the Python script

```bash
# Override Python interpreter
PYTHON=/usr/local/bin/python3.12 ./scripts/run_orchestrator.sh --dry-run
```

---

## 5. Execution Model

### Tier Architecture

The 40 agents are organized into 7 tiers of increasing specialization. Tiers execute **sequentially** (Tier 0 before Tier 1, etc.), while agents **within** each tier execute in **parallel**.

```
Tier 0 (Bootstrap):     AGT-001                                                [1 agent]
      │
      ▼
Tier 1 (Foundation):    AGT-002, AGT-003, AGT-019                             [3 agents]
      │
      ▼
Tier 2 (Core):          AGT-004, AGT-005, AGT-007, AGT-008, AGT-009, AGT-011  [6 agents]
      │
      ▼
Tier 3 (Intelligence):  AGT-012..AGT-018                                       [7 agents]
      │
      ▼
Tier 4 (Operational):   AGT-006, AGT-010, AGT-020..AGT-027                    [10 agents]
      │
      ▼
Tier 5 (Cross-Cutting): AGT-028..AGT-037                                      [10 agents]
      │
      ▼
Tier 6 (Emerging):      AGT-038, AGT-039, AGT-040                             [3 agents]
```

### Detailed Tier Breakdown

#### Tier 0 — Bootstrap (Sequential)

| Agent | Name | Mode | Dependencies |
|-------|------|------|-------------|
| AGT-001 | Governance Policy Agent | architect | *(none)* |

Root governance agent — must complete before all subsequent tiers.

#### Tier 1 — Foundation (Parallel: 3)

| Agent | Name | Mode | Dependencies |
|-------|------|------|-------------|
| AGT-002 | System Architect Agent | architect | AGT-001 |
| AGT-003 | Research & Benchmarking Agent | research | AGT-001 |
| AGT-019 | Economic Optimization Agent | research | AGT-002 |

System architecture, research foundations, and economic modeling.

#### Tier 2 — Core (Parallel: 6)

| Agent | Name | Mode | Dependencies |
|-------|------|------|-------------|
| AGT-004 | Agent Architecture Agent | architect | AGT-002 |
| AGT-005 | Task Architecture Agent | architect | AGT-002 |
| AGT-007 | Model Routing Agent | architect | AGT-002, AGT-019 |
| AGT-008 | Data Engineering Agent | code | AGT-002 |
| AGT-009 | Infrastructure Agent | code | AGT-002 |
| AGT-011 | Context & Prompt Agent | architect | AGT-002 |

Core infrastructure: agent lifecycles, task management, data, infra, context.

#### Tier 3 — Intelligence (Parallel: 7)

| Agent | Name | Mode | Dependencies |
|-------|------|------|-------------|
| AGT-012 | Memory Systems Agent | architect | AGT-008, AGT-011 |
| AGT-013 | Reasoning Agent | architect | AGT-011, AGT-012 |
| AGT-014 | Knowledge Graph Agent | architect | AGT-012, AGT-008 |
| AGT-015 | Code Explorer Agent | code | AGT-011 |
| AGT-016 | Specification Agent | architect | AGT-013, AGT-005 |
| AGT-017 | Code Generation Agent | code | AGT-016, AGT-015, AGT-013, AGT-007 |
| AGT-018 | Refactoring Agent | code | AGT-015 |

Intelligence layer: memory, reasoning, knowledge graphs, code analysis.

#### Tier 4 — Operational (Parallel: 10)

| Agent | Name | Mode | Dependencies |
|-------|------|------|-------------|
| AGT-006 | Distributed Orchestration Agent | architect | AGT-004, AGT-005 |
| AGT-010 | Workspace Management Agent | code | AGT-005 |
| AGT-020 | Testing Architecture Agent | code | AGT-017, AGT-016 |
| AGT-021 | CI/CD Pipeline Agent | code | AGT-020, AGT-009, AGT-010 |
| AGT-022 | Observability Agent | code | AGT-002, AGT-009 |
| AGT-023 | Human-in-the-Loop Agent | architect | AGT-001, AGT-031 |
| AGT-024 | Autonomous Runtime Agent | architect | AGT-004, AGT-001, AGT-031 |
| AGT-025 | Scaling Strategies Agent | architect | AGT-015, AGT-011, AGT-010 |
| AGT-026 | Debugging Agent | code | AGT-020, AGT-015 |
| AGT-027 | Deployment Agent | code | AGT-021, AGT-010, AGT-009 |

Operational systems: testing, CI/CD, deployment, debugging, scaling.

#### Tier 5 — Cross-Cutting (Parallel: 10)

| Agent | Name | Mode | Dependencies |
|-------|------|------|-------------|
| AGT-028 | Security Coordinator Agent | review | AGT-001, AGT-002 |
| AGT-029 | Cost Optimization Coordinator Agent | review | AGT-019, AGT-007 |
| AGT-030 | Quality Assurance Coordinator Agent | review | AGT-001, AGT-020 |
| AGT-031 | Human Escalation Coordinator Agent | architect | AGT-001 |
| AGT-032 | Telemetry Coordinator Agent | review | AGT-002, AGT-022 |
| AGT-033 | Context Poisoning Defense Agent | review | AGT-028, AGT-011 |
| AGT-034 | MCP Integration Coordinator Agent | architect | AGT-002 |
| AGT-035 | Compliance & Audit Coordinator Agent | review | AGT-001, AGT-032 |
| AGT-036 | Error Recovery Coordinator Agent | review | AGT-002, AGT-004 |
| AGT-037 | Performance Regression Agent | review | AGT-003, AGT-007 |

Cross-cutting concerns: security, cost, quality, compliance, observability.

#### Tier 6 — Emerging (Parallel: 3)

| Agent | Name | Mode | Dependencies |
|-------|------|------|-------------|
| AGT-038 | Self-Improvement Agent | research | AGT-003, AGT-037, AGT-032 |
| AGT-039 | Agent Trust Agent | research | AGT-004, AGT-037, AGT-030 |
| AGT-040 | Ecosystem Intelligence Agent | research | AGT-015, AGT-028, AGT-025 |

Emerging tech: self-improvement, trust scoring, ecosystem analysis.

### Dependency Flow

```
Tier 0:  [AGT-001] ─────────────────────────────────────────────────┐
              │                                                      │
Tier 1:  [AGT-002] ──────────────┬──────────┐    [AGT-003]  [AGT-019]
              │                   │          │         │          │
Tier 2:  [AGT-004] [AGT-005] [AGT-007] [AGT-008] [AGT-009] [AGT-011]
              │         │         │        │          │         │
Tier 3:  [AGT-012] [AGT-013] [AGT-014] [AGT-015] [AGT-016] [AGT-017] [AGT-018]
              │         │         │        │          │         │          │
Tier 4:  [AGT-006] [AGT-010] [AGT-020] [AGT-021] [AGT-022] [AGT-023]──[AGT-027]
              │         │         │        │          │         │
Tier 5:  [AGT-028] [AGT-029] [AGT-030] [AGT-031] [AGT-032]──[AGT-037]
              │                   │                   │
Tier 6:  [AGT-038]            [AGT-039]           [AGT-040]
```

Within each tier, agents whose **dependencies have already completed** are dispatched in parallel via `ThreadPoolExecutor(max_workers=max_parallel)`. Agents with unmet dependencies within the same tier are skipped with a warning.

### Retry & Exponential Backoff

When an agent fails (non-zero exit code or timeout), the tier executor retries according to:

```
delay = 30s × 2^(attempt - 1)
```

| Retry Attempt | Backoff Delay |
|---------------|---------------|
| 1 | 30 seconds |
| 2 | 60 seconds |

With `--max-retries 2` (default), each failed agent gets **2 retry attempts** before being marked as permanently failed. All retries within a tier execute in parallel.

---

## 6. Output Structure

```
output/
├── meta/
│   ├── AGT-001/          # Governance Policy Agent
│   │   ├── governance_framework.yaml
│   │   ├── policy_rules.yaml
│   │   └── bootstrap_process.md
│   ├── AGT-002/          # System Architect Agent
│   │   ├── architecture_contract.md
│   │   ├── design_patterns.yaml
│   │   └── modes.yaml
│   └── AGT-003/          # Research & Benchmarking Agent
│       ├── benchmarking_framework.yaml
│       └── ...
├── core_infrastructure/
│   ├── AGT-004/          # Agent Architecture Agent
│   ├── AGT-005/          # Task Architecture Agent
│   ├── AGT-006/          # Distributed Orchestration Agent
│   ├── AGT-007/          # Model Routing Agent
│   ├── AGT-008/          # Data Engineering Agent
│   ├── AGT-009/          # Infrastructure Agent
│   └── AGT-010/          # Workspace Management Agent
├── intelligence/
│   ├── AGT-011/          # Context & Prompt Agent
│   ├── AGT-012/          # Memory Systems Agent
│   ├── AGT-013/          # Reasoning Agent
│   ├── AGT-014/          # Knowledge Graph Agent
│   ├── AGT-015/          # Code Explorer Agent
│   ├── AGT-016/          # Specification Agent
│   ├── AGT-017/          # Code Generation Agent
│   ├── AGT-018/          # Refactoring Agent
│   └── AGT-019/          # Economic Optimization Agent
├── operational/
│   ├── AGT-020/          # Testing Architecture Agent
│   ├── AGT-021/          # CI/CD Pipeline Agent
│   ├── AGT-022/          # Observability Agent
│   ├── AGT-023/          # Human-in-the-Loop Agent
│   ├── AGT-024/          # Autonomous Runtime Agent
│   ├── AGT-025/          # Scaling Strategies Agent
│   ├── AGT-026/          # Debugging Agent
│   └── AGT-027/          # Deployment Agent
├── cross_cutting/
│   ├── AGT-028/          # Security Coordinator Agent
│   ├── AGT-029/          # Cost Optimization Coordinator Agent
│   ├── AGT-030/          # Quality Assurance Coordinator Agent
│   ├── AGT-031/          # Human Escalation Coordinator Agent
│   ├── AGT-032/          # Telemetry Coordinator Agent
│   ├── AGT-033/          # Context Poisoning Defense Agent
│   ├── AGT-034/          # MCP Integration Coordinator Agent
│   ├── AGT-035/          # Compliance & Audit Coordinator Agent
│   ├── AGT-036/          # Error Recovery Coordinator Agent
│   └── AGT-037/          # Performance Regression Agent
├── emerging/
│   ├── AGT-038/          # Self-Improvement Agent
│   ├── AGT-039/          # Agent Trust Agent
│   └── AGT-040/          # Ecosystem Intelligence Agent
└── manifest.json         # File inventory with SHA-256 checksums
```

```
logs/
├── orchestrator.log      # Main orchestrator log (all tiers)
├── checkpoint.json       # Resume checkpoint (updated after each tier)
├── execution_report.md   # Final markdown report (on completion)
├── dry_run_plan.md       # Dry-run plan output (with --dry-run)
├── AGT-001.log           # Per-agent execution log
├── AGT-001_prompt.md     # Extracted prompt sent to agent
├── AGT-002.log
├── AGT-002_prompt.md
└── ...                   # One log + prompt file per agent
```

---

## 7. Resume Mode

### How Checkpoints Work

After each tier completes, the orchestrator writes a checkpoint to `logs/checkpoint.json` containing:

```json
{
  "last_completed_tier": 2,
  "timestamp": "2026-03-01T03:00:00+00:00",
  "completed_agents": ["AGT-001", "AGT-002", "AGT-003", "AGT-019", "AGT-004", "..."],
  "results": {
    "AGT-001": { "status": "success", "duration_seconds": 45.2, "..." : "..." }
  }
}
```

The checkpoint is written atomically (write to `.tmp`, then rename) to prevent corruption during crashes.

### How to Resume After Interruption

```bash
python scripts/orchestrator.py --resume
```

On resume:

1. The checkpoint file at `logs/checkpoint.json` is read
2. The `last_completed_tier` value determines the starting tier: execution resumes at `last_completed_tier + 1`
3. The `completed_agents` set is restored so dependency checks pass correctly
4. All previously completed tiers are skipped with a log message

### Partially Completed Tiers

If the orchestrator is interrupted **during** a tier (e.g., Tier 3 with 4 of 7 agents done), the checkpoint reflects the **previous** fully completed tier. On resume, the entire interrupted tier re-executes from scratch. Agents that had already succeeded will run again — the system does not currently resume mid-tier.

---

## 8. Error Handling

### Per-Agent Failure

1. Agent exits with non-zero code → status becomes `FAILED`
2. Agent exceeds timeout → process is killed → status becomes `TIMEOUT`
3. Retry engine attempts up to `--max-retries` retries with exponential backoff
4. After all retries exhausted, agent is permanently marked `FAILED`

### Tier Failure

- **Tier 0 (Bootstrap):** Any failure is **fatal** — orchestration halts immediately. The bootstrap governance agent is a hard prerequisite for everything.
- **Tiers 1–6:** Failures are logged and reported. Agents in later tiers with unmet dependencies (due to upstream failures) are **skipped** with status `SKIPPED` and an `"Unmet dependencies"` error message.

### Graceful Shutdown

The orchestrator registers signal handlers for `SIGINT` (Ctrl+C) and `SIGTERM`:

1. Signal received → `_shutdown_requested` flag set
2. Current tier's retry loop exits early
3. No new tiers are started
4. Checkpoint is saved with current progress
5. Artifacts are still collected and the execution report is still generated

### Diagnosing Failures

1. **Check the orchestrator log** — `logs/orchestrator.log` contains all tier-level events, including which agents failed and why
2. **Check the per-agent log** — `logs/AGT-NNN.log` contains the full stdout/stderr from the `kilo-code` CLI invocation, including the command that was run and the timeout setting
3. **Check the execution report** — `logs/execution_report.md` has a per-tier summary table with status icons and error messages
4. **Check the extracted prompt** — `logs/AGT-NNN_prompt.md` shows exactly what prompt was sent to the agent

### Agent Status Lifecycle

```
PENDING ──▶ RUNNING ──▶ SUCCESS
                  │
                  ├──▶ FAILED ──▶ RETRYING ──▶ SUCCESS
                  │                       │
                  │                       └──▶ FAILED (permanent)
                  │
                  └──▶ TIMEOUT ──▶ RETRYING ──▶ SUCCESS
                                          │
                                          └──▶ TIMEOUT (permanent)

SKIPPED (unmet dependencies)
```

---

## 9. Manifest & Reports

### Artifact Manifest (`output/manifest.json`)

Generated after all tiers complete. Contains a file inventory with SHA-256 checksums for every artifact:

```json
{
  "generated_at": "2026-03-01T04:30:00+00:00",
  "total_files": 142,
  "files": [
    {
      "path": "meta/AGT-001/governance_framework.yaml",
      "size_bytes": 4521,
      "sha256": "a3f2b8c9d1e4f5..."
    }
  ]
}
```

### Execution Report (`logs/execution_report.md`)

A Markdown report generated at the end of orchestration containing:

- **Summary header:** total duration, agent counts by status, success rate percentage
- **Per-tier tables:** agent name, mode, status (with emoji icons), duration, retry count, log file path
- **Errors section:** detailed breakdown of every failed/timed-out agent with exit code, error message, and log path
- **Manifest reference:** link to `output/manifest.json`

Status icons used in the report:

| Icon | Status |
|------|--------|
| ✅ | Success |
| ❌ | Failed |
| ⏰ | Timeout |
| ⏭️ | Skipped |
| 🔄 | Running |
| ⏳ | Pending |
| 🔁 | Retrying |

---

## 10. Agent Configuration

### Configuration Schema (`agent_config.json`)

The configuration file has two top-level sections:

#### `meta` — Global metadata

```json
{
  "meta": {
    "version": "1.0.0",
    "total_agents": 40,
    "total_tiers": 7,
    "generated_from": "docs/research/orchestrator_execution_spec.md"
  }
}
```

#### `tiers` — Tier definitions

```json
{
  "tiers": [
    {
      "id": 0,
      "name": "Bootstrap",
      "agents": ["AGT-001"],
      "description": "Root governance agent - must complete before all others"
    }
  ]
}
```

#### `agents` — Per-agent configuration

```json
{
  "agents": {
    "AGT-001": {
      "name": "Governance Policy Agent",
      "domain_id": "DOM-001",
      "domain_name": "System Governance & Policy",
      "category": "Meta",
      "type": "Meta",
      "mode": "architect",
      "tier": 0,
      "dependencies": [],
      "prompt_source": "docs/agent_prompts_batch1.md",
      "prompt_section": "AGT-001",
      "output_dir": "output/meta/AGT-001",
      "expected_outputs": [
        "governance_framework.yaml",
        "policy_rules.yaml",
        "bootstrap_process.md"
      ],
      "max_recursion_depth": 3,
      "timeout_minutes": 30,
      "is_gap_filler": false
    }
  }
}
```

### Agent Config Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✓ | Human-readable agent name |
| `domain_id` | string | ✓ | Domain identifier (e.g., `DOM-001`) |
| `domain_name` | string | ✓ | Domain description |
| `category` | string | ✓ | Category grouping: Meta, Core Infrastructure, Intelligence, Operational, Cross-Cutting, Emerging |
| `type` | string | ✓ | Agent type: Meta, Primary, Gap-Filler, Cross-Cutting, Emerging |
| `mode` | string | ✓ | Kilo Code mode: `architect`, `code`, `research`, or `review` |
| `tier` | int | ✓ | Execution tier (0–6) |
| `dependencies` | list[str] | ✓ | Agent IDs that must complete before this agent runs |
| `prompt_source` | string | ✓ | Relative path to the batch prompt markdown file |
| `prompt_section` | string | ✓ | Section identifier within the batch file |
| `output_dir` | string | ✓ | Relative path for agent output artifacts |
| `expected_outputs` | list[str] | ✓ | Filenames expected to be produced |
| `max_recursion_depth` | int | ✓ | Maximum recursion depth for the agent |
| `timeout_minutes` | int | ✓ | Per-agent timeout (overrides `--timeout` global default) |
| `is_gap_filler` | bool | ✓ | Whether this agent addresses coverage gaps |

### Mode Distribution

| Mode | Count | Agents |
|------|-------|--------|
| `architect` | 15 | AGT-001, AGT-002, AGT-004, AGT-005, AGT-006, AGT-007, AGT-011, AGT-012, AGT-013, AGT-014, AGT-016, AGT-023, AGT-024, AGT-025, AGT-031, AGT-034 |
| `code` | 12 | AGT-008, AGT-009, AGT-010, AGT-015, AGT-017, AGT-018, AGT-020, AGT-021, AGT-022, AGT-026, AGT-027 |
| `research` | 5 | AGT-003, AGT-019, AGT-038, AGT-039, AGT-040 |
| `review` | 8 | AGT-028, AGT-029, AGT-030, AGT-032, AGT-033, AGT-035, AGT-036, AGT-037 |

### How to Add a New Agent

1. Add the agent entry to the `agents` object in `agent_config.json`
2. Include the agent ID in the appropriate tier's `agents` array
3. Update the `meta.total_agents` counter
4. Add the agent's prompt section to the appropriate batch file (`docs/agent_prompts_batch*.md`) with the header format: `## Agent AGT-NNN: Agent Name`
5. Ensure all declared `dependencies` exist and don't create cycles
6. Run `--dry-run` to validate the DAG and review the execution plan

### How to Modify an Agent

- **Change mode:** Update the `mode` field (must be one of: `architect`, `code`, `research`, `review`)
- **Change tier:** Update both the `tier` field in the agent entry and move the ID in the `tiers` array
- **Change timeout:** Update `timeout_minutes` in the agent entry (per-agent override) or use `--timeout` globally
- **Change dependencies:** Update the `dependencies` array — run `--dry-run` to validate no cycles exist

---

## 11. Examples

```bash
# Dry run — review the full plan before committing
python scripts/orchestrator.py --dry-run

# Verbose dry run — debug-level logging with full plan
python scripts/orchestrator.py --dry-run --verbose

# Full execution with default settings (8 parallel, 30 min timeout)
python scripts/orchestrator.py

# Conservative execution with 4 parallel agents
python scripts/orchestrator.py --max-parallel 4

# Extended timeout for complex agents
python scripts/orchestrator.py --timeout 60

# Run only the Bootstrap tier (Tier 0)
python scripts/orchestrator.py --tier 0

# Run only the Core tier (Tier 2)
python scripts/orchestrator.py --tier 2

# Run a single agent for debugging
python scripts/orchestrator.py --agent AGT-020

# Resume after interruption
python scripts/orchestrator.py --resume

# Resume with increased parallelism
python scripts/orchestrator.py --resume --max-parallel 12

# Custom output and log directories
python scripts/orchestrator.py --output-dir results/ --log-dir run_logs/

# Override via environment variables
ORCH_MAX_PARALLEL=4 ORCH_TIMEOUT=45 python scripts/orchestrator.py

# PowerShell equivalents
.\scripts\run_orchestrator.ps1 -DryRun
.\scripts\run_orchestrator.ps1 -MaxParallel 4 -Timeout 45
.\scripts\run_orchestrator.ps1 -Tier 0
.\scripts\run_orchestrator.ps1 -Agent AGT-020
.\scripts\run_orchestrator.ps1 -Resume -VerboseLog
```

---

## 12. Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| `kilo-code CLI not found` | `kilo-code` not on PATH | Install Kilo Code CLI and verify with `kilo-code --version` |
| `Config file not found` | Wrong working directory | Run from the project root, or provide `--config` with an absolute path |
| `Dependency graph contains cycles` | Circular dependency in `agent_config.json` | Check `dependencies` arrays for cycles; the orchestrator exits with code 2 |
| `Python 3.10+ required` | Older Python version | Upgrade Python; the wrapper scripts check version automatically |
| `Prompt extraction failed` | Missing or malformed batch file | Verify `prompt_source` path exists and contains `## Agent AGT-NNN:` headers |
| `Agent timed out after N minutes` | Agent took too long | Increase `--timeout` or the per-agent `timeout_minutes` in config |
| `Unmet dependencies` | Upstream agent failed | Fix the upstream agent first; check logs for root cause |
| `Bootstrap tier failed` | AGT-001 returned non-zero | Check `logs/AGT-001.log` — this is a fatal error that halts everything |

### Reading Log Files

**`logs/orchestrator.log`** — Structured log with timestamps and component names:

```
2026-03-01T03:00:00 [INFO] MetaOrchestrator: DAG validated: 40 agents, 7 tiers
2026-03-01T03:00:01 [INFO] MetaOrchestrator: === Tier 0: Bootstrap (1 agents) ===
2026-03-01T03:00:01 [INFO] TierExecutor: Tier 0: Executing 1 agents (max_parallel=8): ['AGT-001']
2026-03-01T03:00:45 [INFO] TierExecutor:   AGT-001 -> success (44.2s)
```

**`logs/AGT-NNN.log`** — Per-agent log with command and full output:

```
# Agent Execution Log: AGT-020
# Started: 2026-03-01T03:05:00+00:00
# Command: kilo-code --mode code --message-file logs/AGT-020_prompt.md
# Timeout: 60 minutes

[agent stdout/stderr follows...]
```

### Validating the Dependency Graph

The orchestrator validates the DAG automatically on every run using Kahn's algorithm for topological sort. To validate without executing:

```bash
python scripts/orchestrator.py --dry-run
```

If circular dependencies exist, the orchestrator logs:

```
CRITICAL: Dependency graph contains cycles! Aborting.
```

and exits with code `2`.

### Exit Codes

| Code | Meaning |
|------|---------|
| `0` | All agents succeeded |
| `1` | Some agents failed or timed out |
| `2` | Fatal error: config missing, DAG has cycles, or unknown agent |

---

## License

Part of the SDLC Meta-Orchestrator project. See repository root for license details.
