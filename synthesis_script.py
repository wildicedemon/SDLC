import os
import re

reports = {}
for i in range(1, 15):
    path = f"/tmp/workspace/wildicedemon/SDLC/report_target_{i}.md"
    try:
        with open(path, "r") as f:
            content = f.read()
            # Extract TLDR/Winner
            match = re.search(r'(?i)\*\*Winner:.*?\*\*', content)
            winner = match.group(0) if match else "Could not extract winner."
            reports[i] = winner
    except Exception as e:
        reports[i] = str(e)

with open("/tmp/workspace/wildicedemon/SDLC/FINAL_SYNTHESIS.md", "w") as f:
    f.write("# Family-Base Meeting Assistant: Consolidated Research Synthesis\n\n")
    f.write("## Component Winners Summary\n\n")
    for i, winner in reports.items():
        f.write(f"### Target {i}\n{winner}\n\n")
