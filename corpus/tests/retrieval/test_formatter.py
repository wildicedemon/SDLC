from corpus.db.models import DecisionCard
from corpus.retrieval.formatter import format_response


def _make_card() -> DecisionCard:
    return DecisionCard(
        decision_id="d1",
        question="How to secure?",
        capability="security",
        recommendation="Use TLS",
        alternatives="Use SSH",
        constraints="Must be fast",
        confidence_score=0.8,
        confidence_level="high",
        confidence_explanation="Strong evidence",
        has_unresolved_contradiction=True,
        provenance_refs="ref1,ref2",
        last_validated_at="2026-01-01",
        revisit_triggers="new CVE",
        status="active",
    )


class TestFormatter:
    def test_l0_has_recommendation_no_alternatives(self) -> None:
        output = format_response([_make_card()], "L0")
        assert "Use TLS" in output
        assert "Alternatives" not in output

    def test_l1_has_alternatives_and_contradiction(self) -> None:
        output = format_response([_make_card()], "L1")
        assert "Alternatives" in output
        assert "Contradiction" in output

    def test_l3_has_provenance_and_scoring(self) -> None:
        output = format_response([_make_card()], "L3")
        assert "Provenance" in output
        assert "Decision ID" in output
