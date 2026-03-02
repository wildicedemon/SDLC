from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class ConstraintSet:
    domains: list[str] = field(default_factory=list)
    capabilities: list[str] = field(default_factory=list)


_TAG_RE = re.compile(r"\[(\w+):(\w+)\]")


def extract_constraints(query: str) -> ConstraintSet:
    cs = ConstraintSet()
    for match in _TAG_RE.finditer(query):
        tag_type = match.group(1)
        tag_value = match.group(2)
        if tag_type == "domain":
            cs.domains.append(tag_value)
        elif tag_type == "capability":
            cs.capabilities.append(tag_value)
    return cs
