#!/usr/bin/env python3
"""Analyze and fix tier assignments in agent_config.json.

Computes correct tier assignments using topological sort (Kahn's algorithm)
to ensure no agent is in the same tier as or earlier than its dependencies.
"""

import json
import sys
from collections import defaultdict, deque
from pathlib import Path


def main():
    config_path = Path("scripts/agent_config.json")
    with open(config_path) as f:
        cfg = json.load(f)

    # Build current tier lookup
    agent_tier = {}
    for tier in cfg["tiers"]:
        for a in tier["agents"]:
            agent_tier[a] = tier["id"]

    # Build dependency graph
    graph = defaultdict(list)  # dep -> [dependents]
    in_degree = defaultdict(int)
    all_agents = set(cfg["agents"].keys())

    for aid, acfg in cfg["agents"].items():
        for dep in acfg.get("dependencies", []):
            graph[dep].append(aid)
            in_degree[aid] += 1

    # Kahn's algorithm to compute correct tier levels
    tier_assignment = {}
    queue = deque()
    for a in all_agents:
        if in_degree[a] == 0:
            tier_assignment[a] = 0
            queue.append(a)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            tier_assignment[neighbor] = max(
                tier_assignment.get(neighbor, 0),
                tier_assignment[node] + 1,
            )
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Report changes
    print("=== REQUIRED TIER REASSIGNMENTS ===")
    changes = []
    for aid in sorted(cfg["agents"].keys()):
        current = cfg["agents"][aid]["tier"]
        correct = tier_assignment.get(aid, current)
        if current != correct:
            changes.append((aid, current, correct))
            print(f"  {aid} ({cfg['agents'][aid]['name']}): tier {current} -> tier {correct}")
    print(f"\nTotal changes needed: {len(changes)}")

    # Show new tier composition
    print("\n=== NEW TIER COMPOSITION ===")
    new_tiers = defaultdict(list)
    for a, t in tier_assignment.items():
        new_tiers[t].append(a)
    max_tier = max(new_tiers.keys())
    for t in range(max_tier + 1):
        agents = sorted(new_tiers.get(t, []))
        print(f"  Tier {t} ({len(agents)} agents): {agents}")
    print(f"\nTotal tiers: {max_tier + 1}")

    # Apply fix if --apply flag
    if "--apply" in sys.argv:
        print("\n=== APPLYING FIXES ===")

        # Tier name mapping
        tier_names = {
            0: "Bootstrap",
            1: "Foundation",
            2: "Core",
            3: "Intelligence",
            4: "Operational",
            5: "Cross-Cutting",
            6: "Emerging",
        }
        # Extend names for any new tiers
        for t in range(max_tier + 1):
            if t not in tier_names:
                tier_names[t] = f"Extended-{t}"

        # Update agent tier fields
        for aid, current, correct in changes:
            cfg["agents"][aid]["tier"] = correct

        # Rebuild tiers array
        new_tiers_list = []
        for t in range(max_tier + 1):
            agents = sorted(new_tiers.get(t, []))
            if agents:
                new_tiers_list.append({
                    "id": t,
                    "name": tier_names.get(t, f"Tier-{t}"),
                    "agents": agents,
                    "description": f"Tier {t} agents",
                })

        cfg["tiers"] = new_tiers_list
        cfg["meta"]["total_tiers"] = len(new_tiers_list)

        with open(config_path, "w") as f:
            json.dump(cfg, f, indent=2)
        print(f"Updated {config_path} with {len(changes)} tier reassignments")
        print(f"New tier count: {len(new_tiers_list)}")

        # Verify no violations remain
        print("\n=== VERIFICATION ===")
        violations = 0
        for aid in sorted(cfg["agents"].keys()):
            my_tier = cfg["agents"][aid]["tier"]
            for dep in cfg["agents"][aid].get("dependencies", []):
                dep_tier = cfg["agents"][dep]["tier"]
                if dep_tier >= my_tier:
                    print(f"  VIOLATION: {aid}(t{my_tier}) -> {dep}(t{dep_tier})")
                    violations += 1
        if violations == 0:
            print("  No violations found! All tiers are correctly assigned.")
        else:
            print(f"  {violations} violations remain!")


if __name__ == "__main__":
    main()
