from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings


class CorpusSettings(BaseSettings):
    model_config = {"env_prefix": "CORPUS_"}

    db_url: str = Field(default="sqlite:///data/corpus.db")
    chroma_dir: str = Field(default="data/chroma")
    graph_path: str = Field(default="data/graph.json")
    embedding_model: str = Field(default="all-MiniLM-L6-v2")
    kilo_api_key: str = Field(default="")
    llm_base_url: str = Field(default="https://api.kilo.ai/api/gateway")
    llm_model: str = Field(default="google/gemini-2.5-flash")
    decision_model: str = Field(default="perplexity/sonar-deep-research")
    max_arbitration_calls: int = Field(default=500)
    dedup_l1_threshold: float = Field(default=0.5)
    dedup_l2_threshold: float = Field(default=0.85)
    arbitration_confidence_min: float = Field(default=0.70)
    l3_rate_alert_threshold: float = Field(default=0.20)
    sync_lag_tolerance_seconds: int = Field(default=300)

    def data_dir(self) -> Path:
        return Path("data")

    def ensure_data_dirs(self) -> None:
        self.data_dir().mkdir(parents=True, exist_ok=True)
        Path(self.chroma_dir).mkdir(parents=True, exist_ok=True)


def get_settings() -> CorpusSettings:
    return CorpusSettings()
