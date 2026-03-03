from corpus.retrieval.symbolic_filter import extract_constraints


class TestSymbolicFilter:
    def test_domain_tag_extracted(self) -> None:
        cs = extract_constraints("[domain:security] best practices")
        assert cs.domains == ["security"]

    def test_no_tags_empty(self) -> None:
        cs = extract_constraints("how to test")
        assert cs.domains == []
        assert cs.capabilities == []
