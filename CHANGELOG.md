# CHANGELOG

格式参考 Keep a Changelog，版本号遵循语义化版本。

## [0.1.0] - 未发布（O0 骨架）

### 新增
- FastAPI 后端骨架，`/health` 真实探活（执行 `SELECT 1`，数据库不通返回 503）
- `DATABASE_URL` 配置层：本地默认 SQLite，生产可切 Postgres
- 单仓目录结构：`backend/` `infra/` `scripts/`，`mobile/` 与 `admin/` 待 O2/O4 接入
- `infra/docker-compose.yml`：PostGIS 16-3.4 + API，带健康检查与依赖等待
- `backend/Dockerfile`，含容器内 HEALTHCHECK
- GitHub Actions 四个 job：backend（ruff + pytest）、licenses（GPL/AGPL 依赖即失败）、mobile、admin（后两者在目录出现前自动跳过）
- `Makefile` + `scripts/dev.ps1`（Windows 无 make 的等价命令）
- `.devcontainer`，贡献者可不装本地环境
- 文档：README（含 Non-goals、与现有项目的关系、数据处理说明）、DECISIONS、NOTICE

### 已知限制
- `docker compose up` 未在本机验证（开发机未装 WSL2/Docker）
- 无认证、无数据模型、无规则引擎 —— O1 与 O3

## 里程碑路线

- O1 数据与登录：模型 + Alembic + seed + JWT + 学生/班级管理
- O2 跑步闭环：轨迹上传 → 计算 → 学生端历史
- O3 规则引擎：8 条规则 + 点位顺序 + audit_flags
- O4 教师后台：Next.js 记录列表、轨迹地图、异常复核、CSV 导出
- O5 开源化收尾：CONTRIBUTING/COC/SECURITY、issue 模板、真实截图、v0.1.0 release
