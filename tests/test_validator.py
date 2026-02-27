import pytest
from scripts.distillation.validator import Validator

def test_orphaned_atoms():
    atoms = [{"id": "KA-001"}, {"id": "KA-002"}]
    domains = [{"knowledge_atoms": ["KA-001", "KA-002"]}]
    phases = [{"knowledge_atoms": ["KA-001", "KA-002"]}]
    products = [{"knowledge_atoms_consumed": ["KA-001"]}]

    validator = Validator(atoms, domains, phases, products)
    orphaned = validator.check_orphaned_atoms()
    assert len(orphaned) == 1
    assert orphaned[0]["id"] == "KA-002"

def test_missing_references():
    atoms = [{"id": "KA-001"}]
    domains = [{"knowledge_atoms": ["KA-001", "KA-003"]}]
    phases = []
    products = []

    validator = Validator(atoms, domains, phases, products)
    missing = validator.check_missing_references()
    assert len(missing) == 1
    assert "KA-003" in missing

def test_unhandled_failure_modes():
    atoms = [{"id": "KA-001", "type": "FAILURE_MODE"}, {"id": "KA-002", "type": "FAILURE_MODE"}]
    domains = []
    phases = []
    products = [{"knowledge_atoms_consumed": ["KA-001"]}]

    validator = Validator(atoms, domains, phases, products)
    unhandled = validator.check_unhandled_failure_modes()
    assert len(unhandled) == 1
    assert "KA-002" in unhandled

def test_generate_gap_report():
    atoms = [
        {"id": "KA-001", "type": "FAILURE_MODE", "evidence_strength": "STRONG", "content": "Error"},
        {"id": "KA-002", "type": "TECHNIQUE", "evidence_strength": "MODERATE", "content": "Tech"},
    ]
    domains = [{"knowledge_atoms": ["KA-001", "KA-003"]}]
    phases = []
    products = [{"knowledge_atoms_consumed": []}]

    validator = Validator(atoms, domains, phases, products)
    report = validator.generate_gap_report()

    assert "KA-001: Error" in report
    assert "KA-003" in report
    assert "KA-001" in report
    assert "Total Strong Atoms: 1" in report
