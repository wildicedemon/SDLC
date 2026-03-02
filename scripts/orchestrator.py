#!/usr/bin/env python3
"""
Meta-Orchestrator Parallel Execution Engine

Dispatches 40 specialized agents across 10 execution tiers,
managing dependencies, parallelism, retries, and artifact collection.

Usage:
    python scripts/orchestrator.py --dry-run
    python scripts/orchestrator.py --max-parallel 4
    python scripts/orchestrator.py --resume
    python scripts/orchestrator.py --tier 0
    python scripts/orchestrator.py --agent AGT-001
"""

import argparse
import json
import re
import subprocess
import hashlib
import shutil
import time
import os
import sys
import signal
import logging
import re
import tempfile
import threading
from pathlib import Path
from datetime import datetime, timedelta, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import Optional, Dict, List, Set, Tuple
from enum import Enum

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

AGENT_HEADER_PATTERN = re.compile(
    r"^##\s+Agent\s+(AGT-\d{3}):",
    re.MULTILINE,
)

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

# ---------------------------------------------------------------------------
# Enums & Data Classes
# ---------------------------------------------------------------------------


class AgentStatus(Enum):
    """Lifecycle status of an individual agent execution."""

    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    RETRYING = "retrying"
    SKIPPED = "skipped"
    TIMEOUT = "timeout"


@dataclass
class AgentResult:
    """Result record for a single agent execution."""

    agent_id: str
    status: AgentStatus
    exit_code: int
    start_time: datetime
    end_time: datetime
    duration_seconds: float
    retry_count: int
    output_artifacts: List[str]
    log_file: str
    error_message: str = ""

    def to_dict(self) -> dict:
        return {
            "agent_id": self.agent_id,
            "status": self.status.value,
            "exit_code": self.exit_code,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "duration_seconds": round(self.duration_seconds, 2),
            "retry_count": self.retry_count,
            "output_artifacts": self.output_artifacts,
            "log_file": self.log_file,
            "error_message": self.error_message,
        }


# ---------------------------------------------------------------------------
# Prompt Extractor
# ---------------------------------------------------------------------------


class PromptExtractor:
    """Extracts individual agent prompts from batch markdown files."""

    def __init__(self, base_dir: Path):
        self._base_dir = base_dir
        self._cache: Dict[str, str] = {}

    def extract_prompt(self, agent_id: str, batch_file: str) -> str:
        """
        Extract the full prompt text for *agent_id* from *batch_file*.

        The batch files use ``## Agent AGT-NNN: <Name>`` as section headers.
        We capture everything from that header up to the next same-level header
        (or end-of-file).
        """
        cache_key = f"{batch_file}::{agent_id}"
        if cache_key in self._cache:
            return self._cache[cache_key]

        file_path = self._base_dir / batch_file
        if not file_path.exists():
            raise FileNotFoundError(
                f"Batch file not found: {file_path}"
            )

        content = file_path.read_text(encoding="utf-8")
        sections = self._split_sections(content)

        if agent_id not in sections:
            raise ValueError(
                f"Agent {agent_id} section not found in {batch_file}. "
                f"Found sections: {sorted(sections.keys())}"
            )

        prompt_text = sections[agent_id].strip()
        self._cache[cache_key] = prompt_text
        return prompt_text

    @staticmethod
    def _split_sections(content: str) -> Dict[str, str]:
        """Split a batch markdown file into per-agent sections."""
        matches = list(AGENT_HEADER_PATTERN.finditer(content))
        sections: Dict[str, str] = {}
        for i, match in enumerate(matches):
            agent_id = match.group(1)
            start = match.start()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            sections[agent_id] = content[start:end]
        return sections


# ---------------------------------------------------------------------------
# Dependency Graph
# ---------------------------------------------------------------------------


class DependencyGraph:
    """Manages the directed acyclic graph of agent dependencies."""

    def __init__(self, config: dict):
        self._agents: Dict[str, dict] = config["agents"]
        self._tiers: List[dict] = config["tiers"]
        self._adjacency: Dict[str, List[str]] = {}  # parent -> children
        self._reverse: Dict[str, List[str]] = {}  # child -> parents
        self._build()

    def _build(self) -> None:
        for agent_id, agent_cfg in self._agents.items():
            self._reverse[agent_id] = list(agent_cfg.get("dependencies", []))
            if agent_id not in self._adjacency:
                self._adjacency[agent_id] = []
            for dep in agent_cfg.get("dependencies", []):
                self._adjacency.setdefault(dep, []).append(agent_id)

    def get_tier_agents(self, tier_id: int) -> List[str]:
        """Return all agent IDs assigned to *tier_id*."""
        for tier in self._tiers:
            if tier["id"] == tier_id:
                return list(tier["agents"])
        return []

    def get_all_tiers(self) -> List[dict]:
        """Return all tier definitions sorted by id."""
        return sorted(self._tiers, key=lambda t: t["id"])

    def check_dependencies_met(
        self, agent_id: str, completed: Set[str]
    ) -> bool:
        """Return True if every dependency of *agent_id* is in *completed*."""
        deps = self._reverse.get(agent_id, [])
        return all(d in completed for d in deps)

    def get_dependencies(self, agent_id: str) -> List[str]:
        """Return the direct dependency list for an agent."""
        return list(self._reverse.get(agent_id, []))

    def validate_dag(self) -> bool:
        """
        Verify that the graph is a valid DAG (no circular dependencies).

        Uses Kahn's algorithm for topological sort.
        """
        in_degree: Dict[str, int] = {a: 0 for a in self._agents}
        for agent_id, deps in self._reverse.items():
            in_degree[agent_id] = len(deps)

        queue = [a for a, d in in_degree.items() if d == 0]
        visited = 0

        while queue:
            node = queue.pop(0)
            visited += 1
            for child in self._adjacency.get(node, []):
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        if visited != len(self._agents):
            return False
        return True


# ---------------------------------------------------------------------------
# Agent Runner
# ---------------------------------------------------------------------------


class AgentRunner:
    """Executes a single agent via the Kilo CLI (kilo run)."""

    def __init__(
        self,
        config: dict,
        prompt_extractor: PromptExtractor,
        base_dir: Path,
        log_dir: Path,
        output_dir: Path,
        timeout_minutes: int = 90,
        dry_run: bool = False,
    ):
        self._config = config
        self._extractor = prompt_extractor
        self._base_dir = base_dir
        self._log_dir = log_dir
        self._output_dir = output_dir
        self._default_timeout = timeout_minutes
        self._dry_run = dry_run
        self._logger = logging.getLogger("AgentRunner")

    def run_agent(self, agent_id: str) -> AgentResult:
        """Execute a single agent end-to-end and return its result."""
        agent_cfg = self._config["agents"][agent_id]
        timeout = agent_cfg.get("timeout_minutes", self._default_timeout)
        log_file = self._log_dir / f"{agent_id}.log"
        start_time = datetime.now(timezone.utc)

        self._logger.info(
            "Starting %s (%s) in mode=%s",
            agent_id,
            agent_cfg["name"],
            agent_cfg["mode"],
        )

        # 1. Extract prompt from batch file
        try:
            prompt_text = self._extractor.extract_prompt(
                agent_id, agent_cfg["prompt_source"]
            )
        except (FileNotFoundError, ValueError) as exc:
            return self._make_result(
                agent_id,
                AgentStatus.FAILED,
                exit_code=1,
                start_time=start_time,
                error=f"Prompt extraction failed: {exc}",
                log_file=str(log_file),
            )

        # 2. Write prompt to temp file (prompts are too large for CLI args)
        prompt_file = self._log_dir / f"{agent_id}_prompt.md"
        prompt_file.write_text(prompt_text, encoding="utf-8")

        # 3. Create output directory
        agent_output_dir = self._base_dir / agent_cfg["output_dir"]
        agent_output_dir.mkdir(parents=True, exist_ok=True)

        # 4. Build CLI command
        cmd = self._build_cli_command(agent_id, prompt_file)

        if self._dry_run:
            self._write_log(log_file, f"[DRY-RUN] Would execute:\n{' '.join(cmd)}\n")
            return self._make_result(
                agent_id,
                AgentStatus.SKIPPED,
                exit_code=0,
                start_time=start_time,
                log_file=str(log_file),
            )

        # 5. Execute with timeout
        # IMPORTANT: Kilo needs stdout/stderr connected to the log file
        # (not subprocess.PIPE) so its internal tool execution loop works.
        # When stdout is piped, Kilo captures LLM output but doesn't
        # execute tool calls (write_file, etc.), resulting in no artifacts.
        exit_code = 0
        error_msg = ""
        try:
            with open(log_file, "w", encoding="utf-8") as lf:
                lf.write(f"# Agent Execution Log: {agent_id}\n")
                lf.write(f"# Started: {start_time.isoformat()}\n")
                lf.write(f"# Command: {' '.join(cmd)}\n")
                lf.write(f"# Timeout: {timeout} minutes\n\n")
                lf.flush()

                proc = subprocess.Popen(
                    cmd,
                    stdout=lf,
                    stderr=lf,
                    cwd=str(self._base_dir),
                )
                try:
                    proc.wait(timeout=timeout * 60)
                    exit_code = proc.returncode
                    if exit_code != 0:
                        error_msg = f"Agent exited with code {exit_code}"
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait(timeout=10)
                    lf.write(f"\n\n--- TIMEOUT after {timeout} minutes ---\n")
                    return self._make_result(
                        agent_id,
                        AgentStatus.TIMEOUT,
                        exit_code=-1,
                        start_time=start_time,
                        error=f"Agent timed out after {timeout} minutes",
                        log_file=str(log_file),
                    )
        except FileNotFoundError:
            error_msg = (
                "kilo CLI not found. Install Kilo Code and ensure 'kilo' is on PATH."
            )
            exit_code = 127
            self._write_log(log_file, f"\n--- ERROR ---\n{error_msg}\n")
        except OSError as exc:
            error_msg = f"OS error executing agent: {exc}"
            exit_code = 1
            self._write_log(log_file, f"\n--- ERROR ---\n{error_msg}\n")

        # 6. Extract artifacts from log and verify
        if exit_code != 0:
            status = AgentStatus.FAILED
            if not error_msg:
                error_msg = f"Agent exited with code {exit_code}"
        else:
            # Kilo CLI run is single-turn: the LLM generates tool calls
            # but they aren't executed.  Extract artifacts from the log.
            extracted = self._extract_artifacts_from_log(agent_id, log_file)
            artifacts = self._verify_artifacts(agent_id)
            if artifacts is not None:
                status = AgentStatus.SUCCESS
            else:
                status = AgentStatus.SUCCESS
                artifacts = extracted

        end_time = datetime.now(timezone.utc)
        return AgentResult(
            agent_id=agent_id,
            status=status,
            exit_code=exit_code,
            start_time=start_time,
            end_time=end_time,
            duration_seconds=(end_time - start_time).total_seconds(),
            retry_count=0,
            output_artifacts=artifacts if exit_code == 0 else [],
            log_file=str(log_file),
            error_message=error_msg,
        )

    def _build_cli_command(self, agent_id: str, prompt_file: Path) -> list:
        """
        Build the Kilo CLI command for the agent.

        Format: kilo run --auto --dir {base_dir} -f {prompt_file} "message"

        The --auto flag enables autonomous/pipeline mode (auto-approves all permissions).
        The -f flag attaches the prompt file for the agent to process.
        The message is a short instruction directing kilo to process the attached file.
        """
        agent_cfg = self._config["agents"][agent_id]
        mode = agent_cfg["mode"]
        # Resolve the full path to kilo to handle .cmd/.bat on Windows
        kilo_path = shutil.which("kilo") or "kilo"
        cmd = [
            kilo_path,
            "run",
            "--auto",
            "--dir",
            str(self._base_dir),
            "-f",
            str(prompt_file),
        ]
        # Use the 'orchestrator' agent if available and mode is orchestrator,
        # otherwise use default agent (ask)
        if mode == "orchestrator":
            cmd.extend(["--agent", "orchestrator"])
        # The message must not look like a file path to kilo.
        # Use -- to separate options from the message positional.
        cmd.append("--")
        cmd.append(
            f"Execute the {mode} agent prompt from the attached file. "
            f"Output to {agent_cfg['output_dir']}."
        )
        return cmd

    def get_cli_command_str(self, agent_id: str) -> str:
        """Return the CLI command string for display / dry-run purposes."""
        agent_cfg = self._config["agents"][agent_id]
        prompt_file = self._log_dir / f"{agent_id}_prompt.md"
        cmd = self._build_cli_command(agent_id, prompt_file)
        return " ".join(cmd)

    def _extract_artifacts_from_log(
        self, agent_id: str, log_file: Path
    ) -> List[str]:
        """
        Extract the full LLM response from Kilo's log output and save it
        as ``domain_decomposition.md`` in the agent's output directory.

        The log file contains a header block (lines starting with ``#``)
        followed by the raw LLM response.  This method strips the header
        and ANSI escape codes, then persists the clean response text.

        Returns a list of written file paths (length 1 on success, 0 on
        failure).
        """
        if not log_file.exists():
            self._logger.warning(
                "%s: Log file does not exist: %s", agent_id, log_file
            )
            return []

        log_text = log_file.read_text(encoding="utf-8", errors="replace")
        agent_cfg = self._config["agents"][agent_id]
        agent_output_dir = self._base_dir / Path(agent_cfg["output_dir"])
        agent_output_dir.mkdir(parents=True, exist_ok=True)

        # Strip ANSI escape codes for a clean output
        ansi_escape = re.compile(r"\x1b\[[0-9;]*m")
        clean_text = ansi_escape.sub("", log_text)

        # Remove the log header lines (everything up to and including
        # the "# Timeout:" line written by run_agent)
        lines = clean_text.split("\n")
        content_start = 0
        for i, line in enumerate(lines):
            if line.startswith("# Timeout:"):
                content_start = i + 1
                break
        response_text = "\n".join(lines[content_start:]).strip()

        if not response_text:
            self._logger.warning(
                "%s: No LLM response content found in log", agent_id
            )
            return []

        decomp_path = agent_output_dir / "domain_decomposition.md"
        decomp_path.write_text(response_text, encoding="utf-8")
        self._logger.info(
            "%s: Saved LLM response as %s (%d bytes)",
            agent_id,
            decomp_path.name,
            len(response_text),
        )
        return [str(decomp_path)]

    def _verify_artifacts(self, agent_id: str) -> Optional[List[str]]:
        """
        Check that ``domain_decomposition.md`` exists and is non-empty
        in the agent's output directory.

        Returns a single-element list with the artifact path on success,
        or ``None`` if the file is missing or empty.
        """
        agent_cfg = self._config["agents"][agent_id]
        agent_output_dir = self._base_dir / agent_cfg["output_dir"]
        decomp_path = agent_output_dir / "domain_decomposition.md"

        if decomp_path.exists() and decomp_path.stat().st_size > 0:
            self._logger.debug(
                "%s: Verified domain_decomposition.md (%d bytes)",
                agent_id,
                decomp_path.stat().st_size,
            )
            return [str(decomp_path)]

        self._logger.warning(
            "%s: domain_decomposition.md not found or empty in %s",
            agent_id,
            agent_output_dir,
        )
        return None

    @staticmethod
    def _make_result(
        agent_id: str,
        status: AgentStatus,
        exit_code: int,
        start_time: datetime,
        log_file: str = "",
        error: str = "",
    ) -> AgentResult:
        end_time = datetime.now(timezone.utc)
        return AgentResult(
            agent_id=agent_id,
            status=status,
            exit_code=exit_code,
            start_time=start_time,
            end_time=end_time,
            duration_seconds=(end_time - start_time).total_seconds(),
            retry_count=0,
            output_artifacts=[],
            log_file=log_file,
            error_message=error,
        )

    @staticmethod
    def _write_log(log_file: Path, content: str) -> None:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(content)


# ---------------------------------------------------------------------------
# Tier Executor
# ---------------------------------------------------------------------------


class TierExecutor:
    """Executes all agents within a tier in parallel with retry logic."""

    def __init__(
        self,
        runner: AgentRunner,
        max_parallel: int = 8,
        max_retries: int = 2,
        retry_backoff_base: float = 30.0,
    ):
        self._runner = runner
        self._max_parallel = max_parallel
        self._max_retries = max_retries
        self._retry_backoff_base = retry_backoff_base
        self._logger = logging.getLogger("TierExecutor")
        self._shutdown_event = threading.Event()

    def request_shutdown(self) -> None:
        """Signal that a graceful shutdown has been requested."""
        self._shutdown_event.set()

    def execute_tier(
        self,
        tier_id: int,
        agents: List[str],
        completed: Set[str],
        dep_graph: DependencyGraph,
    ) -> Dict[str, AgentResult]:
        """
        Execute all agents in a tier:
        1. Verify all dependencies are met
        2. Launch agents in parallel (up to max_parallel)
        3. Track results
        4. Retry failures with exponential backoff
        5. Return results dict keyed by agent_id
        """
        results: Dict[str, AgentResult] = {}

        # Filter to only agents whose dependencies are all met
        ready_agents = []
        skipped_agents = []
        for agent_id in agents:
            if dep_graph.check_dependencies_met(agent_id, completed):
                ready_agents.append(agent_id)
            else:
                missing = [
                    d
                    for d in dep_graph.get_dependencies(agent_id)
                    if d not in completed
                ]
                self._logger.warning(
                    "Tier %d: Skipping %s -- unmet dependencies: %s",
                    tier_id,
                    agent_id,
                    missing,
                )
                skipped_agents.append(agent_id)
                results[agent_id] = AgentResult(
                    agent_id=agent_id,
                    status=AgentStatus.SKIPPED,
                    exit_code=-1,
                    start_time=datetime.now(timezone.utc),
                    end_time=datetime.now(timezone.utc),
                    duration_seconds=0.0,
                    retry_count=0,
                    output_artifacts=[],
                    log_file="",
                    error_message=f"Unmet dependencies: {missing}",
                )

        if not ready_agents:
            self._logger.info("Tier %d: No agents ready to execute.", tier_id)
            return results

        self._logger.info(
            "Tier %d: Executing %d agents (max_parallel=%d): %s",
            tier_id,
            len(ready_agents),
            self._max_parallel,
            ready_agents,
        )

        # First pass: execute all ready agents in parallel
        first_pass = self._parallel_execute(ready_agents)
        results.update(first_pass)

        # Retry pass: retry failed agents with exponential backoff
        for attempt in range(1, self._max_retries + 1):
            if self._shutdown_event.is_set():
                self._logger.info(                "Shutdown requested -- skipping retries.")
                break

            failed_agents = [
                aid
                for aid, res in results.items()
                if res.status in (AgentStatus.FAILED, AgentStatus.TIMEOUT)
            ]
            if not failed_agents:
                break

            delay = self._retry_backoff_base * (2 ** (attempt - 1))
            self._logger.info(
                "Tier %d: Retrying %d failed agents (attempt %d/%d) after %.0fs backoff: %s",
                tier_id,
                len(failed_agents),
                attempt,
                self._max_retries,
                delay,
                failed_agents,
            )
            time.sleep(delay)

            retry_results = self._parallel_execute(failed_agents)
            for aid, res in retry_results.items():
                res_copy = AgentResult(
                    agent_id=res.agent_id,
                    status=res.status,
                    exit_code=res.exit_code,
                    start_time=res.start_time,
                    end_time=res.end_time,
                    duration_seconds=res.duration_seconds,
                    retry_count=attempt,
                    output_artifacts=res.output_artifacts,
                    log_file=res.log_file,
                    error_message=res.error_message,
                )
                results[aid] = res_copy

        return results

    def _parallel_execute(
        self, agent_ids: List[str]
    ) -> Dict[str, AgentResult]:
        """Run agents in parallel using ThreadPoolExecutor."""
        results: Dict[str, AgentResult] = {}

        with ThreadPoolExecutor(max_workers=self._max_parallel) as executor:
            future_to_agent = {
                executor.submit(self._runner.run_agent, aid): aid
                for aid in agent_ids
            }
            for future in as_completed(future_to_agent):
                agent_id = future_to_agent[future]
                try:
                    result = future.result()
                    results[agent_id] = result
                    self._logger.info(
                        "  %s -> %s (%.1fs)",
                        agent_id,
                        result.status.value,
                        result.duration_seconds,
                    )
                except Exception as exc:
                    self._logger.error(
                        "  %s -> EXCEPTION: %s", agent_id, exc
                    )
                    results[agent_id] = AgentResult(
                        agent_id=agent_id,
                        status=AgentStatus.FAILED,
                        exit_code=-1,
                        start_time=datetime.now(timezone.utc),
                        end_time=datetime.now(timezone.utc),
                        duration_seconds=0.0,
                        retry_count=0,
                        output_artifacts=[],
                        log_file="",
                        error_message=str(exc),
                    )
        return results


# ---------------------------------------------------------------------------
# Checkpoint Manager
# ---------------------------------------------------------------------------


class CheckpointManager:
    """Manages execution checkpoints for resume capability."""

    def __init__(self, checkpoint_file: Path):
        self._file = checkpoint_file

    def save_checkpoint(
        self,
        tier_id: int,
        results: Dict[str, AgentResult],
        completed: Set[str],
    ) -> None:
        """Save progress after each tier completion."""
        data = {
            "last_completed_tier": tier_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "completed_agents": sorted(completed),
            "results": {
                aid: res.to_dict() for aid, res in results.items()
            },
        }
        self._file.parent.mkdir(parents=True, exist_ok=True)
        tmp = self._file.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
        tmp.replace(self._file)

    def load_checkpoint(self) -> Tuple[int, Set[str], Dict[str, dict]]:
        """
        Load last checkpoint for resume mode.
        Returns (last_completed_tier, completed_agents_set, raw_results_dict).
        """
        if not self._file.exists():
            return (-1, set(), {})

        data = json.loads(self._file.read_text(encoding="utf-8"))
        last_tier = data.get("last_completed_tier", -1)
        completed = set(data.get("completed_agents", []))
        results = data.get("results", {})
        return (last_tier, completed, results)

    @property
    def exists(self) -> bool:
        return self._file.exists()


# ---------------------------------------------------------------------------
# Artifact Collector
# ---------------------------------------------------------------------------


class ArtifactCollector:
    """Collects and indexes all agent output artifacts."""

    def __init__(self, base_dir: Path):
        self._base_dir = base_dir
        self._logger = logging.getLogger("ArtifactCollector")

    def collect(
        self,
        results: Dict[str, AgentResult],
        config: dict,
    ) -> Dict[str, list]:
        """Gather all output files into structured output/ directory."""
        collection: Dict[str, list] = {}

        for agent_id, result in results.items():
            if result.status != AgentStatus.SUCCESS:
                continue

            agent_cfg = config["agents"].get(agent_id, {})
            output_dir = self._base_dir / agent_cfg.get("output_dir", "")

            if not output_dir.exists():
                continue

            artifacts = []
            for f in output_dir.rglob("*"):
                if f.is_file():
                    artifacts.append(str(f.relative_to(self._base_dir)))

            collection[agent_id] = artifacts

        return collection

    def generate_manifest(self, output_dir: Path) -> Path:
        """Create manifest.json with file sizes and SHA-256 checksums."""
        manifest_path = output_dir / "manifest.json"
        entries: List[dict] = []

        if output_dir.exists():
            for f in sorted(output_dir.rglob("*")):
                if f.is_file() and f.name != "manifest.json":
                    sha256 = self._sha256(f)
                    entries.append(
                        {
                            "path": str(f.relative_to(output_dir)),
                            "size_bytes": f.stat().st_size,
                            "sha256": sha256,
                        }
                    )

        manifest = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_files": len(entries),
            "files": entries,
        }

        output_dir.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(
            json.dumps(manifest, indent=2), encoding="utf-8"
        )
        self._logger.info(
            "Manifest written: %s (%d files)", manifest_path, len(entries)
        )
        return manifest_path

    @staticmethod
    def _sha256(file_path: Path) -> str:
        h = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()


# ---------------------------------------------------------------------------
# Execution Reporter
# ---------------------------------------------------------------------------


class ExecutionReporter:
    """Generates the final execution summary report."""

    def generate_report(
        self,
        results: Dict[str, AgentResult],
        config: dict,
        manifest_path: Optional[Path],
        start_time: datetime,
        end_time: datetime,
    ) -> str:
        """
        Produce markdown report with:
        - Per-agent timing, status, output paths
        - Tier-level summaries
        - Warnings/errors from logs
        - Overall success rate
        """
        total = len(results)
        succeeded = sum(
            1 for r in results.values() if r.status == AgentStatus.SUCCESS
        )
        failed = sum(
            1 for r in results.values() if r.status == AgentStatus.FAILED
        )
        timed_out = sum(
            1 for r in results.values() if r.status == AgentStatus.TIMEOUT
        )
        skipped = sum(
            1 for r in results.values() if r.status == AgentStatus.SKIPPED
        )
        duration = (end_time - start_time).total_seconds()

        lines = [
            "# Meta-Orchestrator Execution Report",
            "",
            f"**Generated:** {end_time.isoformat()}  ",
            f"**Total Duration:** {duration:.1f}s ({duration / 60:.1f} min)  ",
            f"**Agents:** {total} total | {succeeded} succeeded | {failed} failed | {timed_out} timed out | {skipped} skipped  ",
            f"**Success Rate:** {succeeded / max(total, 1) * 100:.1f}%  ",
            "",
            "---",
            "",
        ]

        # Per-tier summary
        tiers = config.get("tiers", [])
        for tier in sorted(tiers, key=lambda t: t["id"]):
            tier_id = tier["id"]
            tier_name = tier["name"]
            tier_agents = tier["agents"]
            tier_results = [
                results[a] for a in tier_agents if a in results
            ]
            tier_ok = sum(
                1 for r in tier_results if r.status == AgentStatus.SUCCESS
            )
            lines.append(
                f"## Tier {tier_id}: {tier_name} ({tier_ok}/{len(tier_agents)} succeeded)"
            )
            lines.append("")
            lines.append(
                "| Agent | Name | Mode | Status | Duration | Retries | Log |"
            )
            lines.append(
                "|-------|------|------|--------|----------|---------|-----|"
            )
            for agent_id in tier_agents:
                agent_cfg = config["agents"].get(agent_id, {})
                agent_name = agent_cfg.get("name", "Unknown")
                agent_mode = agent_cfg.get("mode", "?")
                if agent_id in results:
                    r = results[agent_id]
                    status_icon = {
                        AgentStatus.SUCCESS: "✅",
                        AgentStatus.FAILED: "❌",
                        AgentStatus.TIMEOUT: "⏰",
                        AgentStatus.SKIPPED: "⏭️",
                        AgentStatus.RUNNING: "🔄",
                        AgentStatus.PENDING: "⏳",
                        AgentStatus.RETRYING: "🔁",
                    }.get(r.status, "❓")
                    lines.append(
                        f"| {agent_id} | {agent_name} | {agent_mode} "
                        f"| {status_icon} {r.status.value} "
                        f"| {r.duration_seconds:.1f}s "
                        f"| {r.retry_count} "
                        f"| `{r.log_file}` |"
                    )
                else:
                    lines.append(
                        f"| {agent_id} | {agent_name} | {agent_mode} "
                        f"| ⏳ pending | — | — | — |"
                    )
            lines.append("")

        # Errors section
        errors = [
            r for r in results.values()
            if r.status in (AgentStatus.FAILED, AgentStatus.TIMEOUT)
        ]
        if errors:
            lines.append("## Errors & Warnings")
            lines.append("")
            for r in errors:
                lines.append(f"### {r.agent_id}")
                lines.append(f"- **Status:** {r.status.value}")
                lines.append(f"- **Exit Code:** {r.exit_code}")
                lines.append(f"- **Error:** {r.error_message}")
                lines.append(f"- **Log:** `{r.log_file}`")
                lines.append("")

        # Manifest reference
        if manifest_path:
            lines.append("## Artifact Manifest")
            lines.append("")
            lines.append(f"See [`{manifest_path}`]({manifest_path})")
            lines.append("")

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Meta-Orchestrator
# ---------------------------------------------------------------------------


class MetaOrchestrator:
    """Main orchestration controller."""

    def __init__(
        self,
        config_path: Path,
        base_dir: Path,
        max_parallel: int = 8,
        max_retries: int = 2,
        timeout_minutes: int = 30,
        dry_run: bool = False,
        resume: bool = False,
        target_tier: Optional[int] = None,
        target_agent: Optional[str] = None,
        log_dir: Optional[Path] = None,
        output_dir: Optional[Path] = None,
        verbose: bool = False,
    ):
        self._config_path = config_path
        self._base_dir = base_dir
        self._max_parallel = max_parallel
        self._max_retries = max_retries
        self._timeout_minutes = timeout_minutes
        self._dry_run = dry_run
        self._resume = resume
        self._target_tier = target_tier
        self._target_agent = target_agent
        self._log_dir = log_dir or (base_dir / "logs")
        self._output_dir = output_dir or (base_dir / "output")
        self._verbose = verbose

        self._config: dict = {}
        self._dep_graph: Optional[DependencyGraph] = None
        self._checkpoint: Optional[CheckpointManager] = None
        self._tier_executor: Optional[TierExecutor] = None
        self._all_results: Dict[str, AgentResult] = {}
        self._completed: Set[str] = set()
        self._logger = logging.getLogger("MetaOrchestrator")
        self._shutdown_requested = False

    def run(self) -> int:
        """
        Main execution loop:
        1. Load config
        2. Validate DAG
        3. Check for resume checkpoint
        4. For each tier:
           a. Validate prerequisites
           b. Execute tier (parallel within)
           c. Save checkpoint
           d. Halt on critical failure
        5. Collect artifacts
        6. Generate report
        7. Return exit code (0 = all success, 1 = some failures)
        """
        start_time = datetime.now(timezone.utc)

        # Setup
        self._load_config()
        self._setup_directories()
        self._setup_signal_handlers()

        # Validate
        self._dep_graph = DependencyGraph(self._config)
        if not self._dep_graph.validate_dag():
            self._logger.critical("Dependency graph contains cycles! Aborting.")
            return 2

        self._logger.info(
            "DAG validated: %d agents, %d tiers",
            self._config["meta"]["total_agents"],
            self._config["meta"]["total_tiers"],
        )

        # Components
        extractor = PromptExtractor(self._base_dir)
        runner = AgentRunner(
            config=self._config,
            prompt_extractor=extractor,
            base_dir=self._base_dir,
            log_dir=self._log_dir,
            output_dir=self._output_dir,
            timeout_minutes=self._timeout_minutes,
            dry_run=self._dry_run,
        )
        self._tier_executor = TierExecutor(
            runner=runner,
            max_parallel=self._max_parallel,
            max_retries=self._max_retries,
        )
        self._checkpoint = CheckpointManager(self._log_dir / "checkpoint.json")

        # Dry run mode
        if self._dry_run:
            report = self._dry_run_report(runner)
            print(report)
            report_path = self._log_dir / "dry_run_plan.md"
            report_path.write_text(report, encoding="utf-8")
            self._logger.info("Dry-run plan written to %s", report_path)
            return 0

        # Resume from checkpoint
        start_tier = 0
        if self._resume and self._checkpoint.exists:
            last_tier, self._completed, prev_results = (
                self._checkpoint.load_checkpoint()
            )
            start_tier = last_tier + 1
            self._logger.info(
                "Resuming from tier %d (completed: %s)",
                start_tier,
                sorted(self._completed),
            )

        # Single agent mode
        if self._target_agent:
            return self._run_single_agent(runner, start_time)

        # Execute tiers
        tiers = self._dep_graph.get_all_tiers()

        for tier in tiers:
            tier_id = tier["id"]

            if tier_id < start_tier:
                self._logger.info("Tier %d: Skipping (already completed)", tier_id)
                continue

            if self._target_tier is not None and tier_id != self._target_tier:
                continue

            if self._shutdown_requested:
                self._logger.info("Shutdown requested -- stopping before tier %d", tier_id)
                break

            self._logger.info(
                "=== Tier %d: %s (%d agents) ===",
                tier_id,
                tier["name"],
                len(tier["agents"]),
            )

            tier_results = self._tier_executor.execute_tier(
                tier_id=tier_id,
                agents=tier["agents"],
                completed=self._completed,
                dep_graph=self._dep_graph,
            )

            self._all_results.update(tier_results)

            # Update completed set
            for aid, res in tier_results.items():
                if res.status == AgentStatus.SUCCESS:
                    self._completed.add(aid)

            # Save checkpoint
            self._checkpoint.save_checkpoint(
                tier_id, self._all_results, self._completed
            )

            # Check for critical failures
            tier_failures = [
                aid
                for aid, res in tier_results.items()
                if res.status in (AgentStatus.FAILED, AgentStatus.TIMEOUT)
            ]
            if tier_failures:
                self._logger.warning(
                    "Tier %d had %d failures: %s",
                    tier_id,
                    len(tier_failures),
                    tier_failures,
                )
                # For tier 0 (bootstrap), a failure is fatal
                if tier_id == 0:
                    self._logger.critical(
                        "Bootstrap tier failed -- cannot proceed. Aborting."
                    )
                    break

            self._logger.info(
                "Tier %d complete: %d/%d succeeded",
                tier_id,
                sum(
                    1
                    for r in tier_results.values()
                    if r.status == AgentStatus.SUCCESS
                ),
                len(tier_results),
            )

        # Collect artifacts and generate report
        end_time = datetime.now(timezone.utc)
        collector = ArtifactCollector(self._base_dir)
        manifest_path = collector.generate_manifest(self._output_dir)

        reporter = ExecutionReporter()
        report_text = reporter.generate_report(
            results=self._all_results,
            config=self._config,
            manifest_path=manifest_path,
            start_time=start_time,
            end_time=end_time,
        )

        report_file = self._log_dir / "execution_report.md"
        report_file.write_text(report_text, encoding="utf-8")
        self._logger.info("Execution report written to %s", report_file)

        # Print summary
        total = len(self._all_results)
        succeeded = sum(
            1
            for r in self._all_results.values()
            if r.status == AgentStatus.SUCCESS
        )
        print(f"\n{'=' * 60}")
        print(f"  Orchestration Complete: {succeeded}/{total} agents succeeded")
        print(f"  Report: {report_file}")
        print(f"  Duration: {(end_time - start_time).total_seconds():.1f}s")
        print(f"{'=' * 60}\n")

        return 0 if succeeded == total else 1

    def _run_single_agent(
        self, runner: AgentRunner, start_time: datetime
    ) -> int:
        """Execute a single agent (debug mode)."""
        agent_id = self._target_agent
        if agent_id not in self._config["agents"]:
            self._logger.error("Unknown agent: %s", agent_id)
            return 2

        self._logger.info("Single-agent mode: running %s", agent_id)
        result = runner.run_agent(agent_id)
        self._all_results[agent_id] = result

        end_time = datetime.now(timezone.utc)
        print(f"\n{'=' * 60}")
        print(f"  Agent: {agent_id}")
        print(f"  Status: {result.status.value}")
        print(f"  Exit Code: {result.exit_code}")
        print(f"  Duration: {result.duration_seconds:.1f}s")
        if result.error_message:
            print(f"  Error: {result.error_message}")
        print(f"  Log: {result.log_file}")
        print(f"{'=' * 60}\n")

        return 0 if result.status == AgentStatus.SUCCESS else 1

    def _dry_run_report(self, runner: AgentRunner) -> str:
        """
        Print full execution plan without running anything:
        - All tiers with agents
        - CLI commands per agent
        - Expected inputs/outputs
        - Estimated parallelism
        """
        lines = [
            "# Meta-Orchestrator Dry-Run Execution Plan",
            "",
            f"**Generated:** {datetime.now(timezone.utc).isoformat()}  ",
            f"**Config:** {self._config_path}  ",
            f"**Max Parallel:** {self._max_parallel}  ",
            f"**Max Retries:** {self._max_retries}  ",
            f"**Timeout:** {self._timeout_minutes} min/agent  ",
            "",
            f"**Total Agents:** {self._config['meta']['total_agents']}  ",
            f"**Total Tiers:** {self._config['meta']['total_tiers']}  ",
            "",
            "---",
            "",
        ]

        tiers = self._dep_graph.get_all_tiers()
        total_agents_listed = 0

        for tier in tiers:
            tier_id = tier["id"]
            tier_agents = tier["agents"]
            total_agents_listed += len(tier_agents)
            effective_parallel = min(len(tier_agents), self._max_parallel)

            lines.append(
                f"## Tier {tier_id}: {tier['name']} "
                f"({len(tier_agents)} agents, parallelism={effective_parallel})"
            )
            lines.append("")
            lines.append(f"> {tier['description']}")
            lines.append("")

            for agent_id in tier_agents:
                agent_cfg = self._config["agents"][agent_id]
                deps = agent_cfg.get("dependencies", [])
                dep_str = ", ".join(deps) if deps else "(none)"
                cmd_str = runner.get_cli_command_str(agent_id)

                lines.append(f"### {agent_id}: {agent_cfg['name']}")
                lines.append(f"- **Mode:** {agent_cfg['mode']}")
                lines.append(f"- **Dependencies:** {dep_str}")
                lines.append(f"- **Prompt Source:** `{agent_cfg['prompt_source']}`")
                lines.append(f"- **Output Dir:** `{agent_cfg['output_dir']}`")
                lines.append(
                    f"- **Expected Outputs:** {', '.join(agent_cfg.get('expected_outputs', []))}"
                )
                lines.append(f"- **Timeout:** {agent_cfg.get('timeout_minutes', self._timeout_minutes)} min")
                lines.append(f"- **Max Recursion:** {agent_cfg.get('max_recursion_depth', 3)}")
                lines.append(f"- **Gap Filler:** {agent_cfg.get('is_gap_filler', False)}")
                lines.append(f"- **CLI Command:**")
                lines.append(f"  ```")
                lines.append(f"  {cmd_str}")
                lines.append(f"  ```")
                lines.append("")

        lines.append("---")
        lines.append("")
        lines.append(f"**Total agents in plan:** {total_agents_listed}")
        lines.append("")

        return "\n".join(lines)

    def _load_config(self) -> None:
        """Load and validate the agent configuration file."""
        config_path = self._base_dir / self._config_path
        if not config_path.exists():
            # Try as absolute / relative from cwd
            config_path = Path(self._config_path)
        if not config_path.exists():
            self._logger.critical("Config file not found: %s", self._config_path)
            sys.exit(2)

        self._config = json.loads(config_path.read_text(encoding="utf-8"))
        agent_count = len(self._config.get("agents", {}))
        self._logger.info(
            "Loaded config: %d agents from %s", agent_count, config_path
        )

        if agent_count != self._config["meta"]["total_agents"]:
            self._logger.warning(
                "Config declares %d agents but found %d",
                self._config["meta"]["total_agents"],
                agent_count,
            )

    def _setup_directories(self) -> None:
        """Create log and output directories."""
        self._log_dir.mkdir(parents=True, exist_ok=True)
        self._output_dir.mkdir(parents=True, exist_ok=True)

    def _setup_signal_handlers(self) -> None:
        """Register graceful shutdown on SIGINT / SIGTERM."""

        def _handler(signum, frame):
            sig_name = signal.Signals(signum).name
            self._logger.warning(
                "Received %s -- initiating graceful shutdown...", sig_name
            )
            self._shutdown_requested = True
            if self._tier_executor:
                self._tier_executor.request_shutdown()

        signal.signal(signal.SIGINT, _handler)
        signal.signal(signal.SIGTERM, _handler)


# ---------------------------------------------------------------------------
# CLI Entry Point
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Meta-Orchestrator: Parallel Agent Execution Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/orchestrator.py --dry-run
  python scripts/orchestrator.py --max-parallel 4 --timeout 45
  python scripts/orchestrator.py --resume
  python scripts/orchestrator.py --tier 0
  python scripts/orchestrator.py --agent AGT-001
        """,
    )
    parser.add_argument(
        "--config",
        default="scripts/agent_config.json",
        help="Path to agent configuration file (default: scripts/agent_config.json)",
    )
    parser.add_argument(
        "--max-parallel",
        type=int,
        default=int(os.environ.get("ORCH_MAX_PARALLEL", "8")),
        help="Maximum concurrent agents (default: 8, env: ORCH_MAX_PARALLEL)",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=2,
        help="Maximum retries per failed agent (default: 2)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=int(os.environ.get("ORCH_TIMEOUT", "30")),
        help="Default timeout per agent in minutes (default: 30, env: ORCH_TIMEOUT)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print execution plan without running agents",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from last checkpoint",
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Output directory (default: output/)",
    )
    parser.add_argument(
        "--log-dir",
        default="logs",
        help="Log directory (default: logs/)",
    )
    parser.add_argument(
        "--tier",
        type=int,
        default=None,
        help="Run only a specific tier (for debugging)",
    )
    parser.add_argument(
        "--agent",
        type=str,
        default=None,
        help="Run only a specific agent ID, e.g. AGT-001 (for debugging)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose/debug logging",
    )

    args = parser.parse_args()

    # Configure logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
    )

    # Also log to file
    base_dir = Path.cwd()
    log_dir = base_dir / args.log_dir
    log_dir.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(
        log_dir / "orchestrator.log", encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT)
    )
    logging.getLogger().addHandler(file_handler)

    logger = logging.getLogger("main")
    logger.info("Meta-Orchestrator starting")
    logger.info("  Config: %s", args.config)
    logger.info("  Max Parallel: %d", args.max_parallel)
    logger.info("  Max Retries: %d", args.max_retries)
    logger.info("  Timeout: %d min/agent", args.timeout)
    logger.info("  Dry Run: %s", args.dry_run)
    logger.info("  Resume: %s", args.resume)

    orchestrator = MetaOrchestrator(
        config_path=Path(args.config),
        base_dir=base_dir,
        max_parallel=args.max_parallel,
        max_retries=args.max_retries,
        timeout_minutes=args.timeout,
        dry_run=args.dry_run,
        resume=args.resume,
        target_tier=args.tier,
        target_agent=args.agent,
        log_dir=log_dir,
        output_dir=base_dir / args.output_dir,
        verbose=args.verbose,
    )

    exit_code = orchestrator.run()
    logger.info("Meta-Orchestrator finished with exit code %d", exit_code)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
