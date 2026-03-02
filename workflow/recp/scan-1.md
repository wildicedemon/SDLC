# RECP Cycle 1 - Entropy Map

**Timestamp:** 2026-03-02  
**Repository:** SDLC Knowledge Atom Extraction System  
**Files Scanned:** 802  
**Directories:** 194  

---

## Executive Summary

This repository contains significant structural entropy with **CRITICAL** issues requiring immediate attention. The codebase has evolved organically with multiple overlapping implementations, broken references, and duplicated content.

---

## CRITICAL Severity Issues (Immediate Action Required)

### CRITICAL-001: Massive Code Duplication - Extractor Files
- **Files:** `extract_knowledge.py` vs `extract_knowledge_atoms.py`
- **Duplication:** 90.1% identical
- **Impact:** ~400 lines of redundant code
- **Evidence:** 8 functions 100% identical (should_keep, determine_atom_type, calculate_evidence_strength, map_to_domains, map_to_sdlc_phases, map_to_products, create_atom, deduplicate_atoms)

### CRITICAL-002: Broken Import Statements
- **Files:** `scripts/distill.py`, `scripts/test_distill.py`
- **Count:** 132 broken import occurrences
- **Issue:** Imports reference `distillation.X` but modules are at `scripts/distillation/X.py`
- **Impact:** Code is non-functional

### CRITICAL-003: Malformed JSON Files
- **Files:** 
  - `knowledge_atom_extractor/schemas/knowledge_atom_schema.json` - entire schema duplicated (lines 1-136 and 137-270)
  - `registry_simple.json` - all content duplicated
- **Impact:** Files are unparseable, data integrity compromised

### CRITICAL-004: Security Vulnerability
- **File:** `.kilocode/mcp.json`
- **Issue:** Hardcoded API keys (Perplexity JWT + GitHub PAT) committed to repository
- **Impact:** Security breach, credentials exposed

### CRITICAL-005: Directory Duplication
- **Directories:** `Kimi-Research/` vs `docs/`
- **Size:** ~70MB of duplicate research content
- **Files:** 137 files nearly identical

---

## HIGH Severity Issues (Next Priority)

### HIGH-001: Multiple Extractor Implementations
- **Files:** 
  - `knowledge_atom_extractor.py` (main implementation)
  - `simple_extractor.py` (simplified version)
  - `minimal_extractor.py` (minimal version)
  - `extractor.js` (JavaScript version)
  - `knowledge_atom_extractor/main.py` (package version)
- **Issue:** 5+ implementations of same functionality
- **Duplication:** 55.3% between simple/minimal extractors

### HIGH-002: Scattered Registry Files
- **Files:** 6 registry-related files
  - `knowledge_atom_registry.json`
  - `knowledge_atom_registry.json` (64.9% duplicate)
  - `registry_simple.json` (malformed)
  - `generate_registry.py`
  - `generate_full_registry.py` (32.2% duplicate)
- **Issue:** Knowledge atoms scattered across multiple sources

### HIGH-003: Orphaned Test Files
- **Count:** 12 test files without corresponding source
- **Location:** `corpus/tests/` directory
- **Files:** conftest.py, test_kilo_gateway.py, integration tests, db tests

### HIGH-004: Configuration Dispersal
- **Count:** 35+ configuration files across 7+ locations
- **Issue:** Inconsistent formats (JSON, YAML, TOML)
- **Conflicts:** Python versions (3.9 vs 3.12), line lengths (88 vs 120)

### HIGH-005: Duplicate Mode Configuration
- **Files:** `.roomodes` (JSON) vs `.kilocodemodes` (YAML)
- **Issue:** Same IDE mode configs in different formats

---

## MEDIUM Severity Issues

### MEDIUM-001: Deep Directory Nesting
- **Depth:** 5-6 levels in research documentation
- **Impact:** Reduced navigability

### MEDIUM-002: Bloated logs/ Directory
- **Count:** 43 files
- **Issue:** Log files committed to repository

### MEDIUM-003: Missing Package Structure
- **Directory:** `knowledge_atom_extractor/`
- **Issue:** Missing `__init__.py` for proper Python package

### MEDIUM-004: Potentially Missing Dependencies
- **Count:** 15 packages imported but not in requirements.txt
- **Packages:** bs4, chromadb, click, datasketch, git, markdown, networkx, numpy, perplexity, psutil, pydantic_settings, rich, sentence_transformers, sqlalchemy, typer

---

## LOW Severity Issues

### LOW-001: Naming Convention Inconsistencies
- **Patterns Found:**
  - snake_case: `extract_knowledge.py`
  - verb-noun: `generate_registry.py`
  - noun-only: `knowledge_atom_extractor.py`
  - adjective-noun: `simple_extractor.py`

### LOW-002: Empty/Placeholder Files
- **Files:** `$null`, `Index`, `Structured` (0 bytes each)

---

## Metrics Summary

| Metric | Value |
|--------|-------|
| Total Files | 802 |
| Total Directories | 194 |
| Max Depth | 6 levels |
| Python Files | 156 |
| Test Files | 37 matched, 12 orphaned |
| Config Files | 35+ |
| Duplicate Content | ~5-7% of codebase |
| Reducible LOC | ~800-1000 lines |

---

## Cycle 1 Action Plan

1. **Fix CRITICAL-002** (Broken imports) - enables test execution
2. **Fix CRITICAL-003** (Malformed JSON) - restores data integrity
3. **Fix CRITICAL-004** (Security) - remove hardcoded keys
4. **Consolidate CRITICAL-001** (Duplicate extractors)
5. **Verify** all changes with test execution

---

## Evidence Files Generated

- `/mnt/okcomputer/sdlc_repo/SDLC-main/REPOSITORY_STRUCTURE_ANALYSIS.md`
- `/mnt/okcomputer/sdlc_repo/SDLC-main/duplication_analysis_report.txt`
- `/mnt/okcomputer/sdlc_repo/SDLC-main/detailed_orphaned_code_analysis.txt`
- `/mnt/okcomputer/sdlc_repo/SDLC-main/orphaned_code_analysis.json`
- `/mnt/okcomputer/sdlc_repo/SDLC-main/config_analysis_report.md`
