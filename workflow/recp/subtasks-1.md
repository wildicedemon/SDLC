# RECP Cycle 1 - Spawned Sub-Tasks

**Timestamp:** 2026-03-02  
**Cycle:** 1  

---

## Sub-Task 1: Fix Broken Imports (CRITICAL-002)

**Scope:** Fix 132 broken import statements in scripts/distill.py and scripts/test_distill.py

**Invariants:**
- Conservation of Knowledge: All import functionality preserved
- Zero Net Creation: Only fix paths, no new logic
- Empirical Integrity: Verify Python syntax after changes

**Action:**
- Change `from distillation.X` to `from scripts.distillation.X`
- Verify with Python syntax check

---

## Sub-Task 2: Repair Malformed JSON (CRITICAL-003)

**Scope:** Fix duplicated content in:
- knowledge_atom_extractor/schemas/knowledge_atom_schema.json
- registry_simple.json

**Invariants:**
- Conservation of Knowledge: Preserve unique data, remove duplicates
- Empirical Integrity: Validate JSON after repair

**Action:**
- Remove duplicate content sections
- Validate with Python json module

---

## Sub-Task 3: Sanitize Security Issues (CRITICAL-004)

**Scope:** Remove hardcoded API keys from .kilocode/mcp.json

**Invariants:**
- Conservation of Knowledge: Replace with env var references
- Empirical Integrity: Verify no secrets remain

**Action:**
- Replace hardcoded JWT and PAT with ${ENV_VAR} references
- Add .env to .gitignore

---

## Sub-Task 4: Consolidate Duplicate Extractors (CRITICAL-001)

**Scope:** Merge extract_knowledge.py and extract_knowledge_atoms.py

**Invariants:**
- Conservation of Knowledge: Merge all unique functionality
- Empirical Integrity: Verify merged code is valid Python

**Action:**
- Create unified extractor module
- Update all imports
- Remove duplicate file

---

## Execution Order

1. Sub-Task 1 (Import fixes) - enables test execution
2. Sub-Task 2 (JSON repair) - restores data integrity
3. Sub-Task 3 (Security) - removes vulnerabilities
4. Sub-Task 4 (Consolidation) - reduces duplication

All sub-tasks can execute in parallel as they target different files.
