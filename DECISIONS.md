# DECISIONS

一条一个决策，最新的在最上面。改主意就追加新条目，不改历史。

## D-001 项目名与包名：PaceRule / 步尺

- 日期：2026-11-05
- 决定：GitHub 仓库 `pacerule`；Flutter applicationId `app.pacerule.mobile`；Python 包 `pacerule`；镜像 `ghcr.io/<owner>/pacerule-api`；APK `pacerule-x.y.z.apk`。
- 依据：实时查重结果 —— GitHub 无同名项目；npm、PyPI、pub.dev 均未占用。候选名 `campusrun`（撞 SHU-CampusRun 等 3 个）、`runtrail`（PyPI 已占、GitHub 3 个同名）、`campusmile`（1 个 2015 年停更仓库）均淘汰。
- 未完成：中国商标第 9 类 / 第 41 类尚未人工核查。若撞标，按本文件追加新条目并全局替换。

## D-002 许可证：MIT

- 日期：2026-11-05
- 决定：MIT。理由：校园社团、个人开发者最容易被 MIT 说服采用；AGPL-3.0 会挡掉一部分学校内部二次开发。
- 代价：允许他人做成收费服务。若后续介意（例如出现商用分叉），可在 v1.0 前换 AGPL-3.0 —— 已发布的旧版本无法追回授权。

## D-003 本地开发默认 SQLite，生产用 Postgres + PostGIS

- 日期：2026-11-05
- 决定：`DATABASE_URL` 决定后端连接串，默认 `sqlite:///./dev.db`。
- 理由：贡献者不该为了改一行文案就装 Docker + WSL2。O0 阶段只需要 `/health` 能通。
- 代价：PostGIS 专有函数（`ST_DistanceSphere`）在 SQLite 上不可用，距离计算统一用 Python 侧 haversine，保证两端口径一致。这个决定在 O3 落地时必须写测试锁住。
- 待办：O1 起加 Alembic 迁移，SQLite 只作为开发快捷路径，CI 的权威验证跑 Postgres。

## D-004 坐标系全库 WGS84

- 日期：2026-11-05
- 决定：`track_points` 存 WGS84 经纬度；OSM 底图直接渲染。若切高德，必须在展示层做 WGS84→GCJ02 转换，不能改存储。
- 理由：一旦库里混了 GCJ02，历史轨迹全错位，且不可逆。

## D-005 防作弊只出证据，不自动判罚

- 日期：2026-11-05
- 决定：规则引擎命中后只写 `audit_flags`，由教师端人工复核。
- 理由：GPS 漂移、雨天精度下降都会误伤，自动判零分会直接引发申诉和信任崩塌。规则与阈值放在 `rules` 表，接口可改、即时生效。
