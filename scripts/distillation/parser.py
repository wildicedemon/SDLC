import re
from typing import List
from .schemas import KnowledgeAtom, AtomType, EvidenceStrength


class Parser:
    @staticmethod
    def parse_knowledge_atoms(text: str) -> List[KnowledgeAtom]:
        """
        Parse text containing Knowledge Atoms and return a list of KnowledgeAtom objects.
        """
        atoms = []

        # Regex to match Knowledge Atom blocks
        pattern = re.compile(
            r"ID:\s*(?P<id>[^\n]+)\n+"
            r"TYPE:\s*(?P<type>[^\n]+)\n+"
            r"CONTENT:\s*(?P<content>.*?)\n+"
            r"EVIDENCE_STRENGTH:\s*(?P<evidence>[^\n]+)\n+"
            r"SOURCE:\s*(?P<source>[^\n]+)\n+"
            r"DOMAINS:\s*(?P<domains>[^\n]+)\n+"
            r"SDLC_PHASES:\s*(?P<phases>[^\n]+)\n+"
            r"PRODUCTS:\s*(?P<products>[^\n]+)",
            re.MULTILINE | re.DOTALL | re.IGNORECASE,
        )

        for match in pattern.finditer(text):
            try:
                # Clean up and split lists
                atom_id = match.group("id").strip()
                atom_type_str = match.group("type").strip().upper()
                content = match.group("content").strip()
                evidence_str = match.group("evidence").strip().upper()

                # Split comma-separated lists and clean them
                sources = [
                    s.strip() for s in match.group("source").split(",") if s.strip()
                ]
                domains = [
                    d.strip() for d in match.group("domains").split(",") if d.strip()
                ]
                phases = [
                    p.strip() for p in match.group("phases").split(",") if p.strip()
                ]
                products = [
                    p.strip() for p in match.group("products").split(",") if p.strip()
                ]

                atom = KnowledgeAtom(
                    id=atom_id,
                    type=AtomType(atom_type_str),
                    content=content,
                    evidence_strength=EvidenceStrength(evidence_str),
                    source=sources,
                    domains=domains,
                    sdlc_phases=phases,
                    products=products,
                )
                atoms.append(atom)
            except Exception as e:
                print(
                    f"Failed to parse atom block starting with {match.group('id')}: {e}"
                )

        return atoms
