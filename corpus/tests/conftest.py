from pathlib import Path

import pytest

from corpus.config import CorpusSettings


@pytest.fixture()
def tmp_data_dir(tmp_path: Path) -> Path:
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    return data_dir


@pytest.fixture()
def test_settings(tmp_data_dir: Path) -> CorpusSettings:
    db_path = tmp_data_dir / "corpus.db"
    return CorpusSettings(
        db_url=f"sqlite:///{db_path}",
        chroma_dir=str(tmp_data_dir / "chroma"),
        graph_path=str(tmp_data_dir / "graph.json"),
        openai_api_key="test-key",
    )


@pytest.fixture()
def tmp_db_url(tmp_data_dir: Path) -> str:
    db_path = tmp_data_dir / "corpus.db"
    return f"sqlite:///{db_path}"
