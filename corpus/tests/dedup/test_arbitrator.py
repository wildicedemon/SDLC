from unittest.mock import MagicMock, patch

from corpus.dedup.arbitrator import arbitrate
from corpus.dedup.embeddings import Disagreement


def _make_disagreement(a_id: str = "c1", b_id: str = "c2") -> Disagreement:
    return Disagreement(
        chunk_a_id=a_id,
        chunk_b_id=b_id,
        chunk_a_content="chunk a content text",
        chunk_b_content="chunk b content text",
        jaccard=0.6,
        cosine_similarity=0.7,
    )


class TestArbitrator:
    def test_successful_api_returns_result(self) -> None:
        mock_client = MagicMock()
        mock_resp = MagicMock()
        mock_resp.choices = [MagicMock()]
        mock_resp.choices[0].message.content = '{"confidence": 0.80, "recommendation": "merge"}'
        mock_client.chat.completions.create.return_value = mock_resp

        with patch("corpus.dedup.arbitrator.OpenAI", return_value=mock_client):
            results = arbitrate([_make_disagreement()])

        assert len(results) == 1
        assert results[0].confidence == 0.80
        assert results[0].recommendation == "merge"

    def test_api_failure_routes_to_human(self) -> None:
        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = Exception("API down")

        with patch("corpus.dedup.arbitrator.OpenAI", return_value=mock_client):
            results = arbitrate([_make_disagreement()])

        assert len(results) == 1
        assert results[0].confidence == 0.0
        assert results[0].recommendation == "human_review"

    def test_low_confidence_result(self) -> None:
        mock_client = MagicMock()
        mock_resp = MagicMock()
        mock_resp.choices = [MagicMock()]
        mock_resp.choices[0].message.content = '{"confidence": 0.60, "recommendation": "keep_both"}'
        mock_client.chat.completions.create.return_value = mock_resp

        with patch("corpus.dedup.arbitrator.OpenAI", return_value=mock_client):
            results = arbitrate([_make_disagreement()])

        assert len(results) == 1
        assert results[0].confidence == 0.60
        assert results[0].recommendation == "keep_both"
