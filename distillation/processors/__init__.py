"""Processing modules for research distillation."""

from .domain_mapper import DomainMapper
from .phase_assigner import PhaseAssigner
from .extraction import AtomExtractor
from .ingestion import ResearchIngestor

__all__ = [
    "DomainMapper",
    "PhaseAssigner",
    "AtomExtractor",
    "ResearchIngestor",
]