import os
import re

reports = {}
for i in range(1, 15):
    path = f"/tmp/workspace/wildicedemon/SDLC/report_target_{i}.md"
    try:
        with open(path, "r") as f:
            content = f.read()
            # Extract TLDR section
            match = re.search(r'(?i)(?<=TL;DR).*?(?=##)', content, re.DOTALL)
            if not match:
                match = re.search(r'(?i)(?<=TL;DR).*?(?=#)', content, re.DOTALL)
            if not match:
                match = re.search(r'(?i)(?<=Winner).*?\n', content, re.DOTALL)
            
            tldr = match.group(0).strip() if match else "Could not extract."
            reports[i] = tldr
    except Exception as e:
        reports[i] = str(e)

with open("/tmp/workspace/wildicedemon/SDLC/FINAL_SYNTHESIS.md", "w") as f:
    f.write("# Family-Base Meeting Assistant: Consolidated Research Synthesis\n\n")
    f.write("## Component Winners Summary\n\n")
    for i, tldr in reports.items():
        f.write(f"### Target {i}\n{tldr[:500]}...\n\n")
