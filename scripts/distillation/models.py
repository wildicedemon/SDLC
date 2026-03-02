from __future__ import annotations

from dataclasses import dataclass, field

from .constants import AtomType, Domain, EvidenceStrength, ProductCategory, SDLCPhase


@dataclass
class KnowledgeAtom:
    id: str
    type: AtomType
    content: str
    evidence_strength: EvidenceStrength
    sources: list[str] = field(default_factory=list)
    domains: list[str] = field(default_factory=list)
    sdlc_phases: list[str] = field(default_factory=list)
    products: list[str] = field(default_factory=list)
    content_hash: str = ""
    raw_section: str = ""


@dataclass
class DomainSpec:
    domain: Domain
    name: str
    atom_ids: list[str] = field(default_factory=list)
    key_techniques: list[str] = field(default_factory=list)
    key_constraints: list[str] = field(default_factory=list)
    key_tools: list[str] = field(default_factory=list)
    combination_recipes: list[str] = field(default_factory=list)
    failure_modes: list[str] = field(default_factory=list)
    cross_domain_links: dict[str, list[str]] = field(default_factory=dict)
    gaps: list[str] = field(default_factory=list)


@dataclass
class PhaseSpec:
    phase: SDLCPhase
    name: str
    description: str = ""
    atom_ids: list[str] = field(default_factory=list)
    techniques_by_step: dict[str, list[str]] = field(default_factory=dict)
    constraints: list[str] = field(default_factory=list)
    tools: list[str] = field(default_factory=list)
    failure_modes: list[str] = field(default_factory=list)
    transitions: dict[str, str] = field(default_factory=dict)


@dataclass
class ProductSpec:
    category: ProductCategory
    instance_name: str
    atom_ids: list[str] = field(default_factory=list)
    yaml_spec: dict = field(default_factory=dict)
    confidence: str = "LOW"
    gaps: list[str] = field(default_factory=list)
