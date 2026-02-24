#!/usr/bin/env python3
"""
split_prompts.py — Prompt Splitter & Config Generator

Reads Prompt_thread.md, splits it into 38 individual prompts by parsing
## N. headers, saves each as scripts/prompts/prompt_NN.md, and generates
scripts/prompts/config.json mapping each prompt to its output path.

Usage:
    python scripts/split_prompts.py
"""

import io
import json
import re
import sys
from pathlib import Path

# Force UTF-8 output on Windows (cp1252 can't handle emoji)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# ──────────────────────────────────────────────────────────────────────
# Output-path mapping: prompt # → (title, output directory)
# ──────────────────────────────────────────────────────────────────────

OUTPUT_MAP: dict[int, tuple[str, str]] = {
    1:  ("Agent Orchestration & Multi-Agent Patterns",
         "docs/research/02_agent_orchestration/agent_system_design/"),
    2:  ("Context Management for LLM/Agent Systems",
         "docs/research/03_context_memory_intelligence/context_management/"),
    3:  ("Memory Systems",
         "docs/research/03_context_memory_intelligence/memory_systems/"),
    4:  ("MCP Servers & MCP Security",
         "docs/research/02_agent_orchestration/agent_system_design/"),
    5:  ("Task Decomposition & Agent Coordination",
         "docs/research/02_agent_orchestration/task_architecture/"),
    6:  ("Testing Architecture & Automatic Validation",
         "docs/research/05_sdlc_automation/testing_architecture/"),
    7:  ("Model Routing, Switching & Fallback",
         "docs/research/08_model_management/model_capability_management/"),
    8:  ("Security Architecture",
         "docs/research/01_meta_architecture/security_architecture/"),
    9:  ("Anti-Hallucination Strategies & Guardrails",
         "docs/research/01_meta_architecture/security_architecture/"),
    10: ("Self-Healing CI/CD for Agentic Systems",
         "docs/research/05_sdlc_automation/cicd_devops/"),
    11: ("Human-in-the-Loop Interaction",
         "docs/research/07_human_interaction/human_in_the_loop_systems/"),
    12: ("Reasoning Architecture",
         "docs/research/03_context_memory_intelligence/reasoning_architecture/"),
    13: ("Knowledge Representation",
         "docs/research/03_context_memory_intelligence/knowledge_representation/"),
    14: ("Governance & Compliance",
         "docs/research/01_meta_architecture/governance_compliance/"),
    15: ("Large Codebase Handling",
         "docs/research/10_scaling_enterprise/large_codebase_handling/"),
    16: ("Ecosystem Intelligence",
         "docs/research/10_scaling_enterprise/ecosystem_intelligence/"),
    17: ("Observability & Feedback Loops",
         "docs/research/05_sdlc_automation/observability_feedback_loops/"),
    18: ("Human Interaction & UX",
         "docs/research/07_human_interaction/human_in_the_loop_systems/"),
    19: ("Org-Wide Knowledge Base Patterns",
         "docs/research/03_context_memory_intelligence/knowledge_representation/"),
    20: ("System Design & Philosophy",
         "docs/research/01_meta_architecture/system_design_philosophy/"),
    21: ("Economic & Optimization Modeling",
         "docs/research/01_meta_architecture/economic_optimization_modeling/"),
    22: ("Database & Data Engineering",
         "docs/research/06_data_infrastructure/database_data_engineering/"),
    23: ("Infrastructure Engineering",
         "docs/research/06_data_infrastructure/infrastructure_engineering/"),
    24: ("Model Serving & GPU Management",
         "docs/research/08_model_management/model_capability_management/"),
    25: ("Vector Search, RAG & Semantic Indexing",
         "docs/research/03_context_memory_intelligence/context_management/"),
    26: ("Agent Modes, Skills & Role-Based Design",
         "docs/research/02_agent_orchestration/agent_system_design/"),
    27: ("Orchestration Graphs, Workflows & Task Graphs",
         "docs/research/02_agent_orchestration/distributed_orchestration/"),
    28: ("Agent Lifecycle, State Machines & Failure Handling",
         "docs/research/02_agent_orchestration/agent_system_design/"),
    29: ("Agent Trust, Scoring & Multi-Agent Consensus",
         "docs/research/02_agent_orchestration/distributed_orchestration/"),
    30: ("SDLC Automation Overview",
         "docs/research/05_sdlc_automation/cicd_devops/"),
    31: ("Code Repair, Refactoring & Optimization",
         "docs/research/04_code_intelligence/refactoring_optimization/"),
    32: ("CI/CD & DevOps Automation",
         "docs/research/05_sdlc_automation/cicd_devops/"),
    33: ("Research & Benchmarking Framework",
         "docs/research/09_research_discipline/research_benchmarking_framework/"),
    34: ("System Self-Improvement",
         "docs/research/12_self_improvement/system_self_improvement/"),
    35: ("Feedback, Telemetry & AI Feedback Loops",
         "docs/research/05_sdlc_automation/observability_feedback_loops/"),
    36: ("Meta-Prompting & Prompt Evolution",
         "docs/research/12_self_improvement/system_self_improvement/"),
    37: ("Gradient-Free Workflow Optimization",
         "docs/research/11_advanced_runtime/autonomous_runtime_systems/"),
    38: ("Gödel-like Self-Referential Agents",
         "docs/research/11_advanced_runtime/autonomous_runtime_systems/"),
}


def resolve_output_filename(prompt_id: int, output_dir: str) -> str:
    """
    For prompts mapping to the same directory, append the prompt number
    to make filenames unique: perplexityai_research_overview_NN.md.
    For prompts that are the sole occupant of a directory, use the plain name.
    """
    # Build a map of directory → list of prompt IDs that target it
    dir_occupants: dict[str, list[int]] = {}
    for pid, (_title, odir) in OUTPUT_MAP.items():
        dir_occupants.setdefault(odir, []).append(pid)

    if len(dir_occupants[output_dir]) > 1:
        return f"perplexityai_research_overview_{prompt_id:02d}.md"
    else:
        return "perplexityai_research_overview.md"


def parse_prompts(source_path: Path) -> dict[int, str]:
    """
    Parse Prompt_thread.md and extract the code-fenced prompt text for
    each ## N. section.  Returns {prompt_id: prompt_text}.

    Uses a line-by-line parser that tracks code-fence state so that
    ## N. headers inside code fences are ignored.
    """
    lines = source_path.read_text(encoding="utf-8").splitlines(keepends=True)

    header_re = re.compile(r"^## (\d+)\.\s+(.+)")
    fence_re = re.compile(r"^```")

    prompts: dict[int, str] = {}
    current_id: int | None = None
    in_fence = False
    fence_lines: list[str] = []

    for line in lines:
        stripped = line.rstrip("\n\r")

        # Toggle code-fence state
        if fence_re.match(stripped):
            if in_fence:
                # Closing fence — save collected content
                if current_id is not None:
                    content = "".join(fence_lines).strip()
                    if content:
                        prompts[current_id] = content
                    else:
                        print(f"  ⚠  Empty code fence for prompt #{current_id}")
                in_fence = False
                fence_lines = []
            else:
                # Opening fence
                in_fence = True
                fence_lines = []
            continue

        if in_fence:
            fence_lines.append(line)
            continue

        # Outside code fence — check for section header
        m = header_re.match(stripped)
        if m:
            current_id = int(m.group(1))

    return prompts


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    source_path = project_root / "Prompt_thread.md"
    prompts_dir = project_root / "scripts" / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)

    if not source_path.exists():
        print(f"❌ Source file not found: {source_path}")
        return

    print(f"📖 Reading {source_path.name}...")
    prompts = parse_prompts(source_path)
    print(f"   Found {len(prompts)} prompts\n")

    if len(prompts) != 38:
        print(f"⚠  Expected 38 prompts but found {len(prompts)}")

    config: list[dict] = []

    for prompt_id in sorted(prompts.keys()):
        if prompt_id not in OUTPUT_MAP:
            print(f"  ⚠  Prompt #{prompt_id} has no output mapping — skipping")
            continue

        title, output_dir = OUTPUT_MAP[prompt_id]
        filename = resolve_output_filename(prompt_id, output_dir)
        output_path = f"{output_dir}{filename}"
        prompt_file = f"scripts/prompts/prompt_{prompt_id:02d}.md"

        # Save individual prompt file
        dest = project_root / prompt_file
        dest.write_text(prompts[prompt_id], encoding="utf-8")
        print(f"  ✅ prompt_{prompt_id:02d}.md  ({len(prompts[prompt_id]):,} chars)")

        config.append({
            "id": prompt_id,
            "title": title,
            "prompt_file": prompt_file,
            "output_path": output_path,
        })

    # Write config.json
    config_path = prompts_dir / "config.json"
    config_path.write_text(
        json.dumps(config, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n📄 Config written to {config_path.relative_to(project_root)}")
    print(f"   {len(config)} entries")

    # Summary of directory collisions
    dir_counts: dict[str, list[int]] = {}
    for entry in config:
        d = str(Path(entry["output_path"]).parent)
        dir_counts.setdefault(d, []).append(entry["id"])
    shared = {d: ids for d, ids in dir_counts.items() if len(ids) > 1}
    if shared:
        print(f"\n📁 Shared output directories ({len(shared)}):")
        for d, ids in sorted(shared.items()):
            print(f"   {d}  ← prompts {ids}")


if __name__ == "__main__":
    main()
