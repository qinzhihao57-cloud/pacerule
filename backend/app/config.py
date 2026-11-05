from __future__ import annotations

import os
from functools import lru_cache


def _normalize(url: str) -> str:
    """把 Postgres 的常见写法统一成 SQLAlchemy + psycopg3 的驱动串。"""
    if url.startswith("postgres://"):
        return url.replace("postgres://", "postgresql+psycopg://", 1)
    if url.startswith("postgresql://"):
        return url.replace("postgresql://", "postgresql+psycopg://", 1)
    return url


class Settings:
    """极简配置。所有值都从环境变量读，不读 .env 文件（避免本地文件漂进容器）。"""

    def __init__(self) -> None:
        self.database_url: str = _normalize(
            os.environ.get("DATABASE_URL", "sqlite:///./dev.db")
        )
        self.app_name: str = os.environ.get("APP_NAME", "PaceRule API")
        self.version: str = os.environ.get("APP_VERSION", "0.1.0")
        self.debug: bool = os.environ.get("DEBUG", "0") == "1"

    @property
    def is_sqlite(self) -> bool:
        return self.database_url.startswith("sqlite")


@lru_cache
def get_settings() -> Settings:
    return Settings()
