# PaceRule · 步尺

一个可自部署的校园跑步打卡开源项目：记录轨迹、按可配置规则给出**作弊证据**、教师端复核，而不是又做一个打卡 App。

> 状态：**O0 骨架**（后端可启动、/health 可查、CI 四 job 就绪）。功能按里程碑推进，见 [CHANGELOG.md](CHANGELOG.md)。

## 它能做什么 / 不能做什么

| 能做 | 不做 |
|---|---|
| 记录一次跑步的轨迹、里程、配速 | 社交、好友、聊天 |
| 必达点位按序打卡校验 | 商城、皮肤、勋章 |
| 8 类可配置的异常标记（只出证据，不自动判罚） | 人脸识别、通讯录、广告 SDK |
| 教师端看班级完成率、导出 CSV | 虚拟定位、代跑、破解任何商业 App |
| 一条命令自部署（Docker） | 多租户 SaaS（留给 fork 的人自己加） |

## 5 分钟上手

### 方式一：本机直接跑后端（无需 Docker，SQLite）

```bash
# 1. 建虚拟环境并装依赖（Windows 下 python 路径按你自己的来）
cd backend
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt   # macOS/Linux: .venv/bin/python

# 2. 启动
.venv/Scripts/python.exe -m uvicorn app.main:app --reload --port 8000
```

另开一个终端：

```bash
curl http://localhost:8000/health
# {"status":"ok","db":"ok"}
```

接口文档：http://localhost:8000/docs

### 方式二：Docker 全家桶（Postgres 16 + PostGIS 3.4 + API）

```bash
cd infra
docker compose up -d --build
curl http://localhost:8000/health
```

> 前端后台（admin/）与移动端（mobile/）在 O2/O4 接入，现在目录是占位。

## 本机验证过的命令（2026-11-05，Windows 11）

| 命令 | 结果 |
|---|---|
| `uvicorn app.main:app --port 8000` + `curl /health` | `{"status":"ok","db":"ok"}` |
| `pytest -q` | 通过 |
| `ruff check .` | 无告警 |
| `docker compose up` | **未在本机验证**（本机未装 Docker/WSL2） |

## Non-goals

见上表右列。任何 PR 提议加入"虚拟定位""代跑""接入某商业校园跑平台接口"的，一律关闭。

## 与现有项目的关系

- 本项目不是任何项目的 fork。
- 不读、不抄 `SHU-CampusRun/CampusRun`（该项目未声明许可证，默认版权保留）。
- 不对接"华体运动汇"等商业校园跑平台的接口，也不提供其辅助工具。
- 没有引入任何商业 App 的代码、图标、字体或抓包数据；外部素材出处见 [NOTICE](NOTICE)。

## 数据处理说明

学生 GPS 轨迹属于敏感个人信息，本项目按《个人信息保护法》的最小必要原则处理：单独告知与同意、加密传输、90 天后只保留聚合统计、可导出可删除、服务端日志不落原始经纬度。细则在 O1 落地时补全到 `docs/privacy.md`。

## 开发

```bash
# 后端
cd backend && .venv/Scripts/python.exe -m pytest -q
cd backend && .venv/Scripts/python.exe -m ruff check .
```

Windows 上没有 `make`，`Makefile` 里的目标请对照 `scripts/dev.ps1` 执行。

## 许可证

MIT，见 [LICENSE](LICENSE)。
