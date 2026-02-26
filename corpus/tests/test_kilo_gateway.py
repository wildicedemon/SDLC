import pytest
from openai import OpenAI

from corpus.config import CorpusSettings

KILO_BASE_URL = "https://api.kilo.ai/api/gateway"
PRIMARY_MODEL = "moonshotai/kimi-k2.5:free"
FALLBACK_MODEL = "minimax/minimax-m2.5:free"


def _make_client(api_key: str = "") -> OpenAI:
    return OpenAI(
        base_url=KILO_BASE_URL,
        api_key=api_key or "anonymous",
    )


def _chat(client: OpenAI, model: str) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Reply with the word OK"}],
        max_tokens=256,
    )
    content = response.choices[0].message.content
    assert content is not None
    return content


@pytest.mark.integration
def test_kilo_gateway_primary_model() -> None:
    client = _make_client()
    content = _chat(client, PRIMARY_MODEL)
    assert len(content.strip()) > 0


@pytest.mark.integration
def test_kilo_gateway_fallback_model() -> None:
    client = _make_client()
    content = _chat(client, FALLBACK_MODEL)
    assert len(content.strip()) > 0


@pytest.mark.integration
def test_kilo_gateway_config_defaults() -> None:
    settings = CorpusSettings()
    assert settings.llm_base_url == KILO_BASE_URL
    assert settings.llm_model == PRIMARY_MODEL

    client = OpenAI(
        base_url=settings.llm_base_url,
        api_key=settings.kilo_api_key or "anonymous",
    )
    content = _chat(client, settings.llm_model)
    assert len(content.strip()) > 0
