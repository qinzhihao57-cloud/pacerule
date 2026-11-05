from __future__ import annotations

from collections.abc import Generator

from sqlalchemy import text
from sqlmodel import Session, SQLModel, create_engine

from app.config import get_settings

_settings = get_settings()

_connect_args = {"check_same_thread": False} if _settings.is_sqlite else {}

engine = create_engine(_settings.database_url, echo=False, connect_args=_connect_args)


def init_db() -> None:
    """O0 只是建空表；O1 换成 Alembic 迁移。"""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def ping() -> bool:
    """探活：真的向数据库发一条 SELECT 1，不是假装连上了。"""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except Exception:
        return False
