from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import get_settings
from app.db import init_db, ping

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    init_db()
    yield


app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="校园跑步打卡：轨迹记录、规则校验、教师端复核。",
    lifespan=lifespan,
)

# 本地开发放开；生产用 ALLOWED_ORIGINS 收紧。
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["运维"], summary="健康检查")
def health() -> JSONResponse:
    """返回服务与数据库状态。数据库不通时返回 503，方便编排系统做探针。"""
    if not ping():
        return JSONResponse(status_code=503, content={"status": "degraded", "db": "down"})
    return JSONResponse(status_code=200, content={"status": "ok", "db": "ok"})


@app.get("/", tags=["运维"], summary="根路径")
def root() -> dict[str, str]:
    return {"name": settings.app_name, "version": settings.version, "docs": "/docs"}
