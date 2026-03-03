"""Symbolic tag extraction from retrieval queries.

Parses inline tag annotations of the form ``[domain:x]`` and
``[capability:y]`` out of a query string so the orchestrator can
apply symbolic (non-vector) filters.

Key function: :func:`extract_constraints`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class ConstraintSet:
    """Symbolic constraints extracted from a query.

    Attributes:
        domains: Domain tags found (e.g. ``["caching"]``).
        capabilities: Capability tags found.
    """

    domains: list[str] = field(default_factory=list)
    capabilities: list[str] = field(default_factory=list)


# Matches [type:value] annotations embedded in the query
_TAG_RE = re.compile(r"\[(\w+):(\w+)\]")


def extract_constraints(query: str) -> ConstraintSet:
    """Parse ``[domain:x]`` and ``[capability:y]`` tags from *query*.

    Args:
        query: A natural-language query possibly containing inline tags.

    Returns:
        A :class:`ConstraintSet` with extracted domain and capability lists.
    """
    cs = ConstraintSet()
    for match in _TAG_RE.finditer(query):
        tag_type = match.group(1)
        tag_value = match.group(2)
        if tag_type == "domain":
            cs.domains.append(tag_value)
        elif tag_type == "capability":
            cs.capabilities.append(tag_value)
    return cs
