"""
Validation script for knowledge atom extraction system.
Validates extracted atoms against the JSON schema and checks for data quality.
"""

import json
import jsonschema
from jsonschema import validate
from pathlib import Path
from knowledge_atom_extractor.schemas import knowledge_atom_schema
from knowledge_atom_extractor.main import KnowledgeAtom
from datetime import datetime
from typing import Tuple, Dict, Any, List


def validate_atom(atom: KnowledgeAtom) -> Tuple[bool, List[str]]:
    """Validate a single knowledge atom against the schema."""
    errors = []
    
    # Convert dataclass to dict for validation
    atom_dict = atom.__dict__.copy()
    
    try:
        # Validate against JSON schema
        validate(instance=atom_dict, schema=knowledge_atom_schema)
        
        # Additional custom validations
        if not atom.content.strip():
            errors.append("Content cannot be empty or whitespace")
        
        if len(atom.content) < 10:
            errors.append("Content is too short (minimum 10 characters)")
        
        if not atom.sources:
            errors.append("Atom must have at least one source")
        
        for source in atom.sources:
            if not source.get("file"):
                errors.append("Source must have a file reference")
            if not source.get("lines"):
                errors.append("Source must have line numbers")
            if not source.get("relevance"):
                errors.append("Source must have relevance score")
        
        # Check evidence strength and specificity ranges
        if not (0.0 <= atom.evidence_strength <= 1.0):
            errors.append(f"Evidence strength {atom.evidence_strength} out of range [0.0, 1.0]")
        
        if not (0.0 <= atom.specificity <= 1.0):
            errors.append(f"Specificity {atom.specificity} out of range [0.0, 1.0]")
        
        # Check confidence value
        if atom.confidence not in ["HIGH", "MEDIUM", "LOW"]:
            errors.append(f"Invalid confidence value: {atom.confidence}")
        
        # Check timestamp format
        try:
            datetime.fromisoformat(atom.timestamp.replace("Z", "+00:00"))
        except ValueError:
            errors.append(f"Invalid timestamp format: {atom.timestamp}")
        
        return len(errors) == 0, errors
        
    except jsonschema.exceptions.ValidationError as e:
        errors.append(f"Schema validation error: {e.message}")
        return False, errors
    except Exception as e:
        errors.append(f"Unexpected validation error: {str(e)}")
        return False, errors


def validate_atoms(atoms: List[KnowledgeAtom]) -> Dict[str, Any]:
    """Validate a list of knowledge atoms and return summary."""
    results = {
        "total": len(atoms),
        "valid": 0,
        "invalid": 0,
        "errors": dict(),
        "categories": dict(),
        "types": dict(),
        "confidence_distribution": dict()
    }
    
    for i, atom in enumerate(atoms):
        is_valid, errors = validate_atom(atom)
        
        if is_valid:
            results["valid"] += 1
        else:
            results["invalid"] += 1
            results["errors"][f"atom_{i+1}"] = errors
        
        # Collect statistics
        results["categories"][atom.category] = results["categories"].get(atom.category, 0) + 1
        results["types"][atom.type] = results["types"].get(atom.type, 0) + 1
        results["confidence_distribution"][atom.confidence] = results["confidence_distribution"].get(atom.confidence, 0) + 1
    
    return results


def print_validation_summary(results: Dict[str, Any]):
    """Print a summary of validation results."""
    print("=" * 50)
    print("VALIDATION SUMMARY")
    print("=" * 50)
    print(f"Total atoms: {results['total']}")
    print(f"Valid atoms: {results['valid']}")
    print(f"Invalid atoms: {results['invalid']}")
    print()
    
    if results["invalid"] > 0:
        print("Errors:")
        for atom_id, errors in results["errors"].items():
            print(f"  {atom_id}: {', '.join(errors)}")
        print()
    
    print("Category Distribution:")
    for category, count in sorted(results["categories"].items()):
        print(f"  {category}: {count}")
    print()
    
    print("Type Distribution:")
    for atom_type, count in sorted(results["types"].items()):
        print(f"  {atom_type}: {count}")
    print()
    
    print("Confidence Distribution:")
    for confidence, count in sorted(results["confidence_distribution"].items()):
        print(f"  {confidence}: {count}")
    print("=" * 50)


def main():
    """Main validation function."""
    from knowledge_atom_extractor.main import RegistryManager
    
    print("Starting Knowledge Atom Validation...")
    
    # Load atoms from registry
    registry = RegistryManager()
    atoms = registry.load_atoms()
    
    print(f"Loaded {len(atoms)} atoms from registry")
    
    # Validate atoms
    results = validate_atoms(atoms)
    
    # Print summary
    print_validation_summary(results)
    
    # Check if all atoms are valid
    if results["invalid"] == 0:
        print("✓ All atoms are valid!")
    else:
        print(f"✗ {results['invalid']} invalid atoms found")
    
    print("Validation complete!")


if __name__ == "__main__":
    main()
Validation script for knowledge atom extraction system.
Validates extracted atoms against the JSON schema and checks for data quality.
"""

import json
import jsonschema
from jsonschema import validate
from pathlib import Path
from knowledge_atom_extractor.schemas import knowledge_atom_schema
from knowledge_atom_extractor.main import KnowledgeAtom
from datetime import datetime
from typing import Tuple, Dict, Any, List


def validate_atom(atom: KnowledgeAtom) -> Tuple[bool, List[str]]:
    """Validate a single knowledge atom against the schema."""
    errors = []
    
    # Convert dataclass to dict for validation
    atom_dict = atom.__dict__.copy()
    
    try:
        # Validate against JSON schema
        validate(instance=atom_dict, schema=knowledge_atom_schema)
        
        # Additional custom validations
        if not atom.content.strip():
            errors.append("Content cannot be empty or whitespace")
        
        if len(atom.content) < 10:
            errors.append("Content is too short (minimum 10 characters)")
        
        if not atom.sources:
            errors.append("Atom must have at least one source")
        
        for source in atom.sources:
            if not source.get("file"):
                errors.append("Source must have a file reference")
            if not source.get("lines"):
                errors.append("Source must have line numbers")
            if not source.get("relevance"):
                errors.append("Source must have relevance score")
        
        # Check evidence strength and specificity ranges
        if not (0.0 <= atom.evidence_strength <= 1.0):
            errors.append(f"Evidence strength {atom.evidence_strength} out of range [0.0, 1.0]")
        
        if not (0.0 <= atom.specificity <= 1.0):
            errors.append(f"Specificity {atom.specificity} out of range [0.0, 1.0]")
        
        # Check confidence value
        if atom.confidence not in ["HIGH", "MEDIUM", "LOW"]:
            errors.append(f"Invalid confidence value: {atom.confidence}")
        
        # Check timestamp format
        try:
            datetime.fromisoformat(atom.timestamp.replace("Z", "+00:00"))
        except ValueError:
            errors.append(f"Invalid timestamp format: {atom.timestamp}")
        
        return len(errors) == 0, errors
        
    except jsonschema.exceptions.ValidationError as e:
        errors.append(f"Schema validation error: {e.message}")
        return False, errors
    except Exception as e:
        errors.append(f"Unexpected validation error: {str(e)}")
        return False, errors


def validate_atoms(atoms: List[KnowledgeAtom]) -> Dict[str, Any]:
    """Validate a list of knowledge atoms and return summary."""
    results = {
        "total": len(atoms),
        "valid": 0,
        "invalid": 0,
        "errors": dict(),
        "categories": dict(),
        "types": dict(),
        "confidence_distribution": dict()
    }
    
    for i, atom in enumerate(atoms):
        is_valid, errors = validate_atom(atom)
        
        if is_valid:
            results["valid"] += 1
        else:
            results["invalid"] += 1
            results["errors"][f"atom_{i+1}"] = errors
        
        # Collect statistics
        results["categories"][atom.category] = results["categories"].get(atom.category, 0) + 1
        results["types"][atom.type] = results["types"].get(atom.type, 0) + 1
        results["confidence_distribution"][atom.confidence] = results["confidence_distribution"].get(atom.confidence, 0) + 1
    
    return results


def print_validation_summary(results: Dict[str, Any]):
    """Print a summary of validation results."""
    print("=" * 50)
    print("VALIDATION SUMMARY")
    print("=" * 50)
    print(f"Total atoms: {results['total']}")
    print(f"Valid atoms: {results['valid']}")
    print(f"Invalid atoms: {results['invalid']}")
    print()
    
    if results["invalid"] > 0:
        print("Errors:")
        for atom_id, errors in results["errors"].items():
            print(f"  {atom_id}: {', '.join(errors)}")
        print()
    
    print("Category Distribution:")
    for category, count in sorted(results["categories"].items()):
        print(f"  {category}: {count}")
    print()
    
    print("Type Distribution:")
    for atom_type, count in sorted(results["types"].items()):
        print(f"  {atom_type}: {count}")
    print()
    
    print("Confidence Distribution:")
    for confidence, count in sorted(results["confidence_distribution"].items()):
        print(f"  {confidence}: {count}")
    print("=" * 50)


def main():
    """Main validation function."""
    from knowledge_atom_extractor.main import RegistryManager
    
    print("Starting Knowledge Atom Validation...")
    
    # Load atoms from registry
    registry = RegistryManager()
    atoms = registry.load_atoms()
    
    print(f"Loaded {len(atoms)} atoms from registry")
    
    # Validate atoms
    results = validate_atoms(atoms)
    
    # Print summary
    print_validation_summary(results)
    
    # Check if all atoms are valid
    if results["invalid"] == 0:
        print("✓ All atoms are valid!")
    else:
        print(f"✗ {results['invalid']} invalid atoms found")
    
    print("Validation complete!")


if __name__ == "__main__":
    main()
Validates extracted atoms against the JSON schema and checks for data quality.
"""

import json
import jsonschema
from jsonschema import validate
from pathlib import Path
from knowledge_atom_extractor.schemas import knowledge_atom_schema
from knowledge_atom_extractor.main import KnowledgeAtom
from datetime import datetime


def validate_atom(atom: KnowledgeAtom) -> Tuple[bool, List[str]]:
    """Validate a single knowledge atom against the schema."""
    errors = []
    
    # Convert dataclass to dict for validation
    atom_dict = atom.__dict__.copy()
    
    try:
        # Validate against JSON schema
        validate(instance=atom_dict, schema=knowledge_atom_schema)
        
        # Additional custom validations
        if not atom.content.strip():
            errors.append("Content cannot be empty or whitespace")
        
        if len(atom.content) < 10:
            errors.append("Content is too short (minimum 10 characters)")
        
        if not atom.sources:
            errors.append("Atom must have at least one source")
        
        for source in atom.sources:
            if not source.get("file"):
                errors.append("Source must have a file reference")
            if not source.get("lines"):
                errors.append("Source must have line numbers")
            if not source.get("relevance"):
                errors.append("Source must have relevance score")
        
        # Check evidence strength and specificity ranges
        if not (0.0 <= atom.evidence_strength <= 1.0):
            errors.append(f"Evidence strength {atom.evidence_strength} out of range [0.0, 1.0]")
        
        if not (0.0 <= atom.specificity <= 1.0):
            errors.append(f"Specificity {atom.specificity} out of range [0.0, 1.0]")
        
        # Check confidence value
        if atom.confidence not in ["HIGH", "MEDIUM", "LOW"]:
            errors.append(f"Invalid confidence value: {atom.confidence}")
        
        # Check timestamp format
        try:
            datetime.fromisoformat(atom.timestamp.replace("Z", "+00:00"))
        except ValueError:
            errors.append(f"Invalid timestamp format: {atom.timestamp}")
        
        return len(errors) == 0, errors
        
    except jsonschema.exceptions.ValidationError as e:
        errors.append(f"Schema validation error: {e.message}")
        return False, errors
    except Exception as e:
        errors.append(f"Unexpected validation error: {str(e)}")
        return False, errors


def validate_atoms(atoms: List[KnowledgeAtom]) -> Dict[str, Any]:
    """Validate a list of knowledge atoms and return summary."""
    results = {
        "total": len(atoms),
        "valid": 0,
        "invalid": 0,
        "errors": dict(),
        "categories": dict(),
        "types": dict(),
        "confidence_distribution": dict()
    }
    
    for i, atom in enumerate(atoms):
        is_valid, errors = validate_atom(atom)
        
        if is_valid:
            results["valid"] += 1
        else:
            results["invalid"] += 1
            results["errors"][f"atom_{i+1}"] = errors
        
        # Collect statistics
        results["categories"][atom.category] = results["categories"].get(atom.category, 0) + 1
        results["types"][atom.type] = results["types"].get(atom.type, 0) + 1
        results["confidence_distribution"][atom.confidence] = results["confidence_distribution"].get(atom.confidence, 0) + 1
    
    return results


def print_validation_summary(results: Dict[str, Any]):
    """Print a summary of validation results."""
    print("=" * 50)
    print("VALIDATION SUMMARY")
    print("=" * 50)
    print(f"Total atoms: {results['total']}")
    print(f"Valid atoms: {results['valid']}")
    print(f"Invalid atoms: {results['invalid']}")
    print()
    
    if results["invalid"] > 0:
        print("Errors:")
        for atom_id, errors in results["errors"].items():
            print(f"  {atom_id}: {', '.join(errors)}")
        print()
    
    print("Category Distribution:")
    for category, count in sorted(results["categories"].items()):
        print(f"  {category}: {count}")
    print()
    
    print("Type Distribution:")
    for atom_type, count in sorted(results["types"].items()):
        print(f"  {atom_type}: {count}")
    print()
    
    print("Confidence Distribution:")
    for confidence, count in sorted(results["confidence_distribution"].items()):
        print(f"  {confidence}: {count}")
    print("=" * 50)


def main():
    """Main validation function."""
    from knowledge_atom_extractor.main import RegistryManager
    
    print("Starting Knowledge Atom Validation...")
    
    # Load atoms from registry
    registry = RegistryManager()
    atoms = registry.load_atoms()
    
    print(f"Loaded {len(atoms)} atoms from registry")
    
    # Validate atoms
    results = validate_atoms(atoms)
    
    # Print summary
    print_validation_summary(results)
    
    # Check if all atoms are valid
    if results["invalid"] == 0:
        print("✓ All atoms are valid!")
    else:
        print(f"✗ {results['invalid']} invalid atoms found")
    
    print("Validation complete!")


if __name__ == "__main__":
    main()
"""

import json
import jsonschema
from jsonschema import validate
from pathlib import Path
from knowledge_atom_extractor.schemas import knowledge_atom_schema
from knowledge_atom_extractor.main import KnowledgeAtom


def validate_atom(atom: KnowledgeAtom) -> Tuple[bool, List[str]]:
    """Validate a single knowledge atom against the schema."""
    errors = []
    
    # Convert dataclass to dict for validation
    atom_dict = atom.__dict__.copy()
    
    try:
        # Validate against JSON schema
        validate(instance=atom_dict, schema=knowledge_atom_schema)
        
        # Additional custom validations
        if not atom.content.strip():
            errors.append("Content cannot be empty or whitespace")
        
        if len(atom.content) < 10:
            errors.append("Content is too short (minimum 10 characters)")
        
        if not atom.sources:
            errors.append("Atom must have at least one source")
        
        for source in atom.sources:
            if not source.get("file"):
                errors.append("Source must have a file reference")
            if not source.get("lines"):
                errors.append("Source must have line numbers")
            if not source.get("relevance"):
                errors.append("Source must have relevance score")
        
        # Check evidence strength and specificity ranges
        if not (0.0 <= atom.evidence_strength <= 1.0):
            errors.append(f"Evidence strength {atom.evidence_strength} out of range [0.0, 1.0]")
        
        if not (0.0 <= atom.specificity <= 1.0):
            errors.append(f"Specificity {atom.specificity} out of range [0.0, 1.0]")
        
        # Check confidence value
        if atom.confidence not in ["HIGH", "MEDIUM", "LOW"]:
            errors.append(f"Invalid confidence value: {atom.confidence}")
        
        # Check timestamp format
        try:
            datetime.fromisoformat(atom.timestamp.replace("Z", "+00:00"))
        except ValueError:
            errors.append(f"Invalid timestamp format: {atom.timestamp}")
        
        return len(errors) == 0, errors
        
    except jsonschema.exceptions.ValidationError as e:
        errors.append(f"Schema validation error: {e.message}")
        return False, errors
    except Exception as e:
        errors.append(f"Unexpected validation error: {str(e)}")
        return False, errors


def validate_atoms(atoms: List[KnowledgeAtom]) -> Dict[str, Any]:
    """Validate a list of knowledge atoms and return summary."""
    results = {
        "total": len(atoms),
        "valid": 0,
        "invalid": 0,
        "errors": defaultdict(list),
        "categories": defaultdict(int),
        "types": defaultdict(int),
        "confidence_distribution": defaultdict(int)
    }
    
    for i, atom in enumerate(atoms):
        is_valid, errors = validate_atom(atom)
        
        if is_valid:
            results["valid"] += 1
        else:
            results["invalid"] += 1
            results["errors"][f"atom_{i+1}"] = errors
        
        # Collect statistics
        results["categories"][atom.category] += 1
        results["types"][atom.type] += 1
        results["confidence_distribution"][atom.confidence] += 1
    
    return results


def print_validation_summary(results: Dict[str, Any]):
    """Print a summary of validation results."""
    print("=" * 50)
    print("VALIDATION SUMMARY")
    print("=" * 50)
    print(f"Total atoms: {results[\"total\"]}")
    print(f"Valid atoms: {results[\"valid\"]}")
    print(f"Invalid atoms: {results[\"invalid\"]}")
    print()
    
    if results["invalid"] > 0:
        print("Errors:")
        for atom_id, errors in results["errors"].items():
            print(f"  {atom_id}: {', '.join(errors)}")
        print()
    
    print("Category Distribution:")
    for category, count in sorted(results["categories"].items()):
        print(f"  {category}: {count}")
    print()
    
    print("Type Distribution:")
    for atom_type, count in sorted(results["types"].items()):
        print(f"  {atom_type}: {count}")
    print()
    
    print("Confidence Distribution:")
    for confidence, count in sorted(results["confidence_distribution"].items()):
        print(f"  {confidence}: {count}")
    print("=" * 50)


def main():
    """Main validation function."""
    from knowledge_atom_extractor.main import RegistryManager
    
    print("Starting Knowledge Atom Validation...")
    
    # Load atoms from registry
    registry = RegistryManager()
    atoms = registry.load_atoms()
    
    print(f"Loaded {len(atoms)} atoms from registry")
    
    # Validate atoms
    results = validate_atoms(atoms)
    
    # Print summary
    print_validation_summary(results)
    
    # Check if all atoms are valid
    if results["invalid"] == 0:
        print("✓ All atoms are valid!")
    else:
        print(f"✗ {results[\"invalid\"]} invalid atoms found")
    
    print("Validation complete!")


if __name__ == "__main__":
    main()
Validation script for knowledge atom extraction system.
Validates extracted atoms against the JSON schema and checks for data quality.
"""

import json
import jsonschema
from jsonschema import validate
from pathlib import Path
from knowledge_atom_extractor.schemas import knowledge_atom_schema
from knowledge_atom_extractor.main import KnowledgeAtom
from datetime import datetime
from typing import Tuple, Dict, Any, List


def validate_atom(atom: KnowledgeAtom) -> Tuple[bool, List[str]]:
    """Validate a single knowledge atom against the schema."""
    errors = []
    
    # Convert dataclass to dict for validation
    atom_dict = atom.__dict__.copy()
    
    try:
        # Validate against JSON schema
        validate(instance=atom_dict, schema=knowledge_atom_schema)
        
        # Additional custom validations
        if not atom.content.strip():
            errors.append("Content cannot be empty or whitespace")
        
        if len(atom.content) < 10:
            errors.append("Content is too short (minimum 10 characters)")
        
        if not atom.sources:
            errors.append("Atom must have at least one source")
        
        for source in atom.sources:
            if not source.get("file"):
                errors.append("Source must have a file reference")
            if not source.get("lines"):
                errors.append("Source must have line numbers")
            if not source.get("relevance"):
                errors.append("Source must have relevance score")
        
        # Check evidence strength and specificity ranges
        if not (0.0 <= atom.evidence_strength <= 1.0):
            errors.append(f"Evidence strength {atom.evidence_strength} out of range [0.0, 1.0]")
        
        if not (0.0 <= atom.specificity <= 1.0):
            errors.append(f"Specificity {atom.specificity} out of range [0.0, 1.0]")
        
        # Check confidence value
        if atom.confidence not in ["HIGH", "MEDIUM", "LOW"]:
            errors.append(f"Invalid confidence value: {atom.confidence}")
        
        # Check timestamp format
        try:
            datetime.fromisoformat(atom.timestamp.replace("Z", "+00:00"))
        except ValueError:
            errors.append(f"Invalid timestamp format: {atom.timestamp}")
        
        return len(errors) == 0, errors
        
    except jsonschema.exceptions.ValidationError as e:
        errors.append(f"Schema validation error: {e.message}")
        return False, errors
    except Exception as e:
        errors.append(f"Unexpected validation error: {str(e)}")
        return False, errors


def validate_atoms(atoms: List[KnowledgeAtom]) -> Dict[str, Any]:
    """Validate a list of knowledge atoms and return summary."""
    results = {
        "total": len(atoms),
        "valid": 0,
        "invalid": 0,
        "errors": dict(),
        "categories": dict(),
        "types": dict(),
        "confidence_distribution": dict()
    }
    
    for i, atom in enumerate(atoms):
        is_valid, errors = validate_atom(atom)
        
        if is_valid:
            results["valid"] += 1
        else:
            results["invalid"] += 1
            results["errors"][f"atom_{i+1}"] = errors
        
        # Collect statistics
        results["categories"][atom.category] = results["categories"].get(atom.category, 0) + 1
        results["types"][atom.type] = results["types"].get(atom.type, 0) + 1
        results["confidence_distribution"][atom.confidence] = results["confidence_distribution"].get(atom.confidence, 0) + 1
    
    return results


def print_validation_summary(results: Dict[str, Any]):
    """Print a summary of validation results."""
    print("=" * 50)
    print("VALIDATION SUMMARY")
    print("=" * 50)
    print(f"Total atoms: {results['total']}")
    print(f"Valid atoms: {results['valid']}")
    print(f"Invalid atoms: {results['invalid']}")
    print()
    
    if results["invalid"] > 0:
        print("Errors:")
        for atom_id, errors in results["errors"].items():
            print(f"  {atom_id}: {', '.join(errors)}")
        print()
    
    print("Category Distribution:")
    for category, count in sorted(results["categories"].items()):
        print(f"  {category}: {count}")
    print()
    
    print("Type Distribution:")
    for atom_type, count in sorted(results["types"].items()):
        print(f"  {atom_type}: {count}")
    print()
    
    print("Confidence Distribution:")
    for confidence, count in sorted(results["confidence_distribution"].items()):
        print(f"  {confidence}: {count}")
    print("=" * 50)


def main():
    """Main validation function."""
    from knowledge_atom_extractor.main import RegistryManager
    
    print("Starting Knowledge Atom Validation...")
    
    # Load atoms from registry
    registry = RegistryManager()
    atoms = registry.load_atoms()
    
    print(f"Loaded {len(atoms)} atoms from registry")
    
    # Validate atoms
    results = validate_atoms(atoms)
    
    # Print summary
    print_validation_summary(results)
    
    # Check if all atoms are valid
    if results["invalid"] == 0:
        print("✓ All atoms are valid!")
    else:
        print(f"✗ {results['invalid']} invalid atoms found")
    
    print("Validation complete!")


if __name__ == "__main__":
    main()
Validation script for knowledge atom extraction system.
Validates extracted atoms against the JSON schema and checks for data quality.
"""

import json
import jsonschema
from jsonschema import validate
from pathlib import Path
from knowledge_atom_extractor.schemas import knowledge_atom_schema
from knowledge_atom_extractor.main import KnowledgeAtom
from datetime import datetime
from typing import Tuple, Dict, Any, List


def validate_atom(atom: KnowledgeAtom) -> Tuple[bool, List[str]]:
    """Validate a single knowledge atom against the schema."""
    errors = []
    
    # Convert dataclass to dict for validation
    atom_dict = atom.__dict__.copy()
    
    try:
        # Validate against JSON schema
        validate(instance=atom_dict, schema=knowledge_atom_schema)
        
        # Additional custom validations
        if not atom.content.strip():
            errors.append("Content cannot be empty or whitespace")
        
        if len(atom.content) < 10:
            errors.append("Content is too short (minimum 10 characters)")
        
        if not atom.sources:
            errors.append("Atom must have at least one source")
        
        for source in atom.sources:
            if not source.get("file"):
                errors.append("Source must have a file reference")
            if not source.get("lines"):
                errors.append("Source must have line numbers")
            if not source.get("relevance"):
                errors.append("Source must have relevance score")
        
        # Check evidence strength and specificity ranges
        if not (0.0 <= atom.evidence_strength <= 1.0):
            errors.append(f"Evidence strength {atom.evidence_strength} out of range [0.0, 1.0]")
        
        if not (0.0 <= atom.specificity <= 1.0):
            errors.append(f"Specificity {atom.specificity} out of range [0.0, 1.0]")
        
        # Check confidence value
        if atom.confidence not in ["HIGH", "MEDIUM", "LOW"]:
            errors.append(f"Invalid confidence value: {atom.confidence}")
        
        # Check timestamp format
        try:
            datetime.fromisoformat(atom.timestamp.replace("Z", "+00:00"))
        except ValueError:
            errors.append(f"Invalid timestamp format: {atom.timestamp}")
        
        return len(errors) == 0, errors
        
    except jsonschema.exceptions.ValidationError as e:
        errors.append(f"Schema validation error: {e.message}")
        return False, errors
    except Exception as e:
        errors.append(f"Unexpected validation error: {str(e)}")
        return False, errors


def validate_atoms(atoms: List[KnowledgeAtom]) -> Dict[str, Any]:
    """Validate a list of knowledge atoms and return summary."""
    results = {
        "total": len(atoms),
        "valid": 0,
        "invalid": 0,
        "errors": dict(),
        "categories": dict(),
        "types": dict(),
        "confidence_distribution": dict()
    }
    
    for i, atom in enumerate(atoms):
        is_valid, errors = validate_atom(atom)
        
        if is_valid:
            results["valid"] += 1
        else:
            results["invalid"] += 1
            results["errors"][f"atom_{i+1}"] = errors
        
        # Collect statistics
        results["categories"][atom.category] = results["categories"].get(atom.category, 0) + 1
        results["types"][atom.type] = results["types"].get(atom.type, 0) + 1
        results["confidence_distribution"][atom.confidence] = results["confidence_distribution"].get(atom.confidence, 0) + 1
    
    return results


def print_validation_summary(results: Dict[str, Any]):
    """Print a summary of validation results."""
    print("=" * 50)
    print("VALIDATION SUMMARY")
    print("=" * 50)
    print(f"Total atoms: {results['total']}")
    print(f"Valid atoms: {results['valid']}")
    print(f"Invalid atoms: {results['invalid']}")
    print()
    
    if results["invalid"] > 0:
        print("Errors:")
        for atom_id, errors in results["errors"].items():
            print(f"  {atom_id}: {', '.join(errors)}")
        print()
    
    print("Category Distribution:")
    for category, count in sorted(results["categories"].items()):
        print(f"  {category}: {count}")
    print()
    
    print("Type Distribution:")
    for atom_type, count in sorted(results["types"].items()):
        print(f"  {atom_type}: {count}")
    print()
    
    print("Confidence Distribution:")
    for confidence, count in sorted(results["confidence_distribution"].items()):
        print(f"  {confidence}: {count}")
    print("=" * 50)


def main():
    """Main validation function."""
    from knowledge_atom_extractor.main import RegistryManager
    
    print("Starting Knowledge Atom Validation...")
    
    # Load atoms from registry
    registry = RegistryManager()
    atoms = registry.load_atoms()
    
    print(f"Loaded {len(atoms)} atoms from registry")
    
    # Validate atoms
    results = validate_atoms(atoms)
    
    # Print summary
    print_validation_summary(results)
    
    # Check if all atoms are valid
    if results["invalid"] == 0:
        print("✓ All atoms are valid!")
    else:
        print(f"✗ {results['invalid']} invalid atoms found")
    
    print("Validation complete!")


if __name__ == "__main__":
    main()
Validates extracted atoms against the JSON schema and checks for data quality.
"""

import json
import jsonschema
from jsonschema import validate
from pathlib import Path
from knowledge_atom_extractor.schemas import knowledge_atom_schema
from knowledge_atom_extractor.main import KnowledgeAtom
from datetime import datetime


def validate_atom(atom: KnowledgeAtom) -> Tuple[bool, List[str]]:
    """Validate a single knowledge atom against the schema."""
    errors = []
    
    # Convert dataclass to dict for validation
    atom_dict = atom.__dict__.copy()
    
    try:
        # Validate against JSON schema
        validate(instance=atom_dict, schema=knowledge_atom_schema)
        
        # Additional custom validations
        if not atom.content.strip():
            errors.append("Content cannot be empty or whitespace")
        
        if len(atom.content) < 10:
            errors.append("Content is too short (minimum 10 characters)")
        
        if not atom.sources:
            errors.append("Atom must have at least one source")
        
        for source in atom.sources:
            if not source.get("file"):
                errors.append("Source must have a file reference")
            if not source.get("lines"):
                errors.append("Source must have line numbers")
            if not source.get("relevance"):
                errors.append("Source must have relevance score")
        
        # Check evidence strength and specificity ranges
        if not (0.0 <= atom.evidence_strength <= 1.0):
            errors.append(f"Evidence strength {atom.evidence_strength} out of range [0.0, 1.0]")
        
        if not (0.0 <= atom.specificity <= 1.0):
            errors.append(f"Specificity {atom.specificity} out of range [0.0, 1.0]")
        
        # Check confidence value
        if atom.confidence not in ["HIGH", "MEDIUM", "LOW"]:
            errors.append(f"Invalid confidence value: {atom.confidence}")
        
        # Check timestamp format
        try:
            datetime.fromisoformat(atom.timestamp.replace("Z", "+00:00"))
        except ValueError:
            errors.append(f"Invalid timestamp format: {atom.timestamp}")
        
        return len(errors) == 0, errors
        
    except jsonschema.exceptions.ValidationError as e:
        errors.append(f"Schema validation error: {e.message}")
        return False, errors
    except Exception as e:
        errors.append(f"Unexpected validation error: {str(e)}")
        return False, errors


def validate_atoms(atoms: List[KnowledgeAtom]) -> Dict[str, Any]:
    """Validate a list of knowledge atoms and return summary."""
    results = {
        "total": len(atoms),
        "valid": 0,
        "invalid": 0,
        "errors": dict(),
        "categories": dict(),
        "types": dict(),
        "confidence_distribution": dict()
    }
    
    for i, atom in enumerate(atoms):
        is_valid, errors = validate_atom(atom)
        
        if is_valid:
            results["valid"] += 1
        else:
            results["invalid"] += 1
            results["errors"][f"atom_{i+1}"] = errors
        
        # Collect statistics
        results["categories"][atom.category] = results["categories"].get(atom.category, 0) + 1
        results["types"][atom.type] = results["types"].get(atom.type, 0) + 1
        results["confidence_distribution"][atom.confidence] = results["confidence_distribution"].get(atom.confidence, 0) + 1
    
    return results


def print_validation_summary(results: Dict[str, Any]):
    """Print a summary of validation results."""
    print("=" * 50)
    print("VALIDATION SUMMARY")
    print("=" * 50)
    print(f"Total atoms: {results['total']}")
    print(f"Valid atoms: {results['valid']}")
    print(f"Invalid atoms: {results['invalid']}")
    print()
    
    if results["invalid"] > 0:
        print("Errors:")
        for atom_id, errors in results["errors"].items():
            print(f"  {atom_id}: {', '.join(errors)}")
        print()
    
    print("Category Distribution:")
    for category, count in sorted(results["categories"].items()):
        print(f"  {category}: {count}")
    print()
    
    print("Type Distribution:")
    for atom_type, count in sorted(results["types"].items()):
        print(f"  {atom_type}: {count}")
    print()
    
    print("Confidence Distribution:")
    for confidence, count in sorted(results["confidence_distribution"].items()):
        print(f"  {confidence}: {count}")
    print("=" * 50)


def main():
    """Main validation function."""
    from knowledge_atom_extractor.main import RegistryManager
    
    print("Starting Knowledge Atom Validation...")
    
    # Load atoms from registry
    registry = RegistryManager()
    atoms = registry.load_atoms()
    
    print(f"Loaded {len(atoms)} atoms from registry")
    
    # Validate atoms
    results = validate_atoms(atoms)
    
    # Print summary
    print_validation_summary(results)
    
    # Check if all atoms are valid
    if results["invalid"] == 0:
        print("✓ All atoms are valid!")
    else:
        print(f"✗ {results['invalid']} invalid atoms found")
    
    print("Validation complete!")


if __name__ == "__main__":
    main()
"""

import json
import jsonschema
from jsonschema import validate
from pathlib import Path
from knowledge_atom_extractor.schemas import knowledge_atom_schema
from knowledge_atom_extractor.main import KnowledgeAtom


def validate_atom(atom: KnowledgeAtom) -> Tuple[bool, List[str]]:
    """Validate a single knowledge atom against the schema."""
    errors = []
    
    # Convert dataclass to dict for validation
    atom_dict = atom.__dict__.copy()
    
    try:
        # Validate against JSON schema
        validate(instance=atom_dict, schema=knowledge_atom_schema)
        
        # Additional custom validations
        if not atom.content.strip():
            errors.append("Content cannot be empty or whitespace")
        
        if len(atom.content) < 10:
            errors.append("Content is too short (minimum 10 characters)")
        
        if not atom.sources:
            errors.append("Atom must have at least one source")
        
        for source in atom.sources:
            if not source.get("file"):
                errors.append("Source must have a file reference")
            if not source.get("lines"):
                errors.append("Source must have line numbers")
            if not source.get("relevance"):
                errors.append("Source must have relevance score")
        
        # Check evidence strength and specificity ranges
        if not (0.0 <= atom.evidence_strength <= 1.0):
            errors.append(f"Evidence strength {atom.evidence_strength} out of range [0.0, 1.0]")
        
        if not (0.0 <= atom.specificity <= 1.0):
            errors.append(f"Specificity {atom.specificity} out of range [0.0, 1.0]")
        
        # Check confidence value
        if atom.confidence not in ["HIGH", "MEDIUM", "LOW"]:
            errors.append(f"Invalid confidence value: {atom.confidence}")
        
        # Check timestamp format
        try:
            datetime.fromisoformat(atom.timestamp.replace("Z", "+00:00"))
        except ValueError:
            errors.append(f"Invalid timestamp format: {atom.timestamp}")
        
        return len(errors) == 0, errors
        
    except jsonschema.exceptions.ValidationError as e:
        errors.append(f"Schema validation error: {e.message}")
        return False, errors
    except Exception as e:
        errors.append(f"Unexpected validation error: {str(e)}")
        return False, errors


def validate_atoms(atoms: List[KnowledgeAtom]) -> Dict[str, Any]:
    """Validate a list of knowledge atoms and return summary."""
    results = {
        "total": len(atoms),
        "valid": 0,
        "invalid": 0,
        "errors": defaultdict(list),
        "categories": defaultdict(int),
        "types": defaultdict(int),
        "confidence_distribution": defaultdict(int)
    }
    
    for i, atom in enumerate(atoms):
        is_valid, errors = validate_atom(atom)
        
        if is_valid:
            results["valid"] += 1
        else:
            results["invalid"] += 1
            results["errors"][f"atom_{i+1}"] = errors
        
        # Collect statistics
        results["categories"][atom.category] += 1
        results["types"][atom.type] += 1
        results["confidence_distribution"][atom.confidence] += 1
    
    return results


def print_validation_summary(results: Dict[str, Any]):
    """Print a summary of validation results."""
    print("=" * 50)
    print("VALIDATION SUMMARY")
    print("=" * 50)
    print(f"Total atoms: {results[\"total\"]}")
    print(f"Valid atoms: {results[\"valid\"]}")
    print(f"Invalid atoms: {results[\"invalid\"]}")
    print()
    
    if results["invalid"] > 0:
        print("Errors:")
        for atom_id, errors in results["errors"].items():
            print(f"  {atom_id}: {', '.join(errors)}")
        print()
    
    print("Category Distribution:")
    for category, count in sorted(results["categories"].items()):
        print(f"  {category}: {count}")
    print()
    
    print("Type Distribution:")
    for atom_type, count in sorted(results["types"].items()):
        print(f"  {atom_type}: {count}")
    print()
    
    print("Confidence Distribution:")
    for confidence, count in sorted(results["confidence_distribution"].items()):
        print(f"  {confidence}: {count}")
    print("=" * 50)


def main():
    """Main validation function."""
    from knowledge_atom_extractor.main import RegistryManager
    
    print("Starting Knowledge Atom Validation...")
    
    # Load atoms from registry
    registry = RegistryManager()
    atoms = registry.load_atoms()
    
    print(f"Loaded {len(atoms)} atoms from registry")
    
    # Validate atoms
    results = validate_atoms(atoms)
    
    # Print summary
    print_validation_summary(results)
    
    # Check if all atoms are valid
    if results["invalid"] == 0:
        print("✓ All atoms are valid!")
    else:
        print(f"✗ {results[\"invalid\"]} invalid atoms found")
    
    print("Validation complete!")


if __name__ == "__main__":
    main()

        print(f"✗ {results[\"invalid\"]} invalid atoms found")
    
    print("Validation complete!")


if __name__ == "__main__":
    main()
