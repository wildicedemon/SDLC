import pytest
from unittest.mock import patch, MagicMock
from scripts.distillation.parser import Parser
from scripts.distillation.llm_client import LLMClient
from scripts.distillation.schemas import AtomType, EvidenceStrength

# A small sample markdown file representing typical LLM output
SAMPLE_MARKDOWN = """
Here are the extracted Knowledge Atoms based on your criteria:

ID: KA-001
TYPE: TOOL
CONTENT: Tree-sitter is a parser generator tool and an incremental parsing library. It can build a concrete syntax tree for a source file and efficiently update the syntax tree as the source file is edited.
EVIDENCE_STRENGTH: STRONG
SOURCE: research/tools/tree_sitter.md
DOMAINS: D5
SDLC_PHASES: P1, P3, P5
PRODUCTS: PC2

Here is another one:

ID: KA-002
TYPE: TECHNIQUE
CONTENT: Use Chain-of-Verification by generating an answer, extracting independent claims, verifying each claim individually, and producing a final answer based on the verified claims.
EVIDENCE_STRENGTH: MODERATE
SOURCE: research/techniques/chain_of_verification.md
DOMAINS: D1, D3
SDLC_PHASES: P2, P4
PRODUCTS: PC1, PC3
"""


def test_parser_extracts_knowledge_atoms():
    # Test just the parsing
    atoms = Parser.parse_knowledge_atoms(SAMPLE_MARKDOWN)

    assert len(atoms) == 2

    atom1 = atoms[0]
    assert atom1.id == "KA-001"
    assert atom1.type == AtomType.TOOL
    assert atom1.content.startswith("Tree-sitter is a parser generator tool")
    assert atom1.evidence_strength == EvidenceStrength.STRONG
    assert atom1.source == ["research/tools/tree_sitter.md"]
    assert atom1.domains == ["D5"]
    assert atom1.sdlc_phases == ["P1", "P3", "P5"]
    assert atom1.products == ["PC2"]

    atom2 = atoms[1]
    assert atom2.id == "KA-002"
    assert atom2.type == AtomType.TECHNIQUE
    assert atom2.content.startswith("Use Chain-of-Verification")
    assert atom2.evidence_strength == EvidenceStrength.MODERATE
    assert atom2.source == ["research/techniques/chain_of_verification.md"]
    assert atom2.domains == ["D1", "D3"]
    assert atom2.sdlc_phases == ["P2", "P4"]
    assert atom2.products == ["PC1", "PC3"]


@patch("scripts.distillation.llm_client.OpenAI")
def test_llm_integration_and_parsing(mock_openai):
    # Mock the LLM client
    mock_client_instance = MagicMock()
    mock_openai.return_value = mock_client_instance

    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = SAMPLE_MARKDOWN
    mock_client_instance.chat.completions.create.return_value = mock_response

    # Need to set env var so LLMClient doesn't throw ValueError
    with patch.dict("os.environ", {"OPENAI_API_KEY": "fake_key"}):
        llm = LLMClient()
        response = llm.generate("system prompt", "user content")

        atoms = Parser.parse_knowledge_atoms(response)
        assert len(atoms) == 2
        assert atoms[0].id == "KA-001"
