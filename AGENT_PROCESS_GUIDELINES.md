# Agent 设计开发过程与准则

> 《The Lantern Keeper》· 项目 GameDev_SP_York_Design · 协作：Psamead · 参考 Animation_yichun《妖精丘陵》的同名文件

## 1. 过程记录

| # | 日期 | 阶段 | 做了什么 | 产出 |
|---|---|---|---|---|
| 1 | 10-22 | 构思 | 三个 2D 像素游戏故事构思（中英双语） | deprecated/ 中的构思文档 |
| 2 | 10-24 | 详细方案 | 读取 Game_zixiang（L2–L4、Prologue、Clearance）与课程讲义，把《守灯人》扩展为完整 GDD v0.1 | 已移入 deprecated/ |
| 3 | 10-24 | Demo 化 | 按《妖精丘陵》Demo 实施说明的写法改成 Demo 方案 v0.2 | 已移入 deprecated/ |
| 4 | 10-24 | 故事 v1.0 | 补全海难、承诺、熄灯与失忆的因果 | 已移入 deprecated/（风格像电视剧） |
| 5 | 10-24 | 故事 v2.0 | 改为布列塔尼民俗奇幻；民俗对照表 | story_draft/ 故事设定 v2.0 |
| 6 | 10-24 | 完整版 + 小 Demo | 完整版概念设计说明（7 章）；Demo 缩小到 4 Scene（参考 Battle Car Arena） | purposal_story/ 两份 Word |
| 7 | 10-30 | 交接结构 | 参考《妖精丘陵》建立 md 交接文件、美术规格、出图 prompt、资产表、文件夹 | 根目录 md、TechnicalArt/、ART_ref/、TechArtAsset/ |
| 8 | 10-31 | 主角与海报 | Midjourney 出 Maela 概念 v1、海报背景 v1；海报改绘本风 | ART_ref/、TechnicalArt/ 评估表与 v1.1 Word |
| 9 | 11-02 | 画风定稿 | 游戏画风改为手绘 2D，新规格 HANDPAINTED_SPEC | TechnicalArt/HANDPAINTED_SPEC.md 与 Word |
| 10 | 11-02~03 | 标题 · 海报 · 菜单 | 字体系统；标题框（蕾丝 + 白鼬尾纹）；海报 v2；开始菜单 v1；MJ 编辑器故障改用 AI Studio；交 Codex 进 Unity | TechArtAsset/Menu、Poster、UI；TechnicalArt/MENU_UNITY_HANDOFF.md |
| 11 | 11-03 | Unity 首跑 | Codex 建 4 场景 + 开始菜单 v1；用户试玩反馈（音效太电子、缺 BGM）；建立经验库 | TechnicalArt/MENU_UNITY_PROGRESS.md、LESSONS_ART_PIPELINE.md |

## 2. 关键决策

| 决策 | 理由 | 可否推翻 |
|---|---|---|
| 布列塔尼民俗（伊斯、达于） | 与海和灯塔契合；和《妖精丘陵》的爱尔兰题材区分 | 可（备选：苏格兰海豹人） |
| ~~像素风~~ → **手绘 2D**（2026-11-02） | 美术靠 AI 出图再清理，像素需全手画反而慢；与海报、概念图画风统一；用分层大图 + 骨骼动画控制工作量 | 可 |
| Demo 只做全屏切换 | 小体量；初学者能实现 | 光圈模式留给完整版 |
| 游戏内只用英文 | 与《妖精丘陵》一致；民俗名词保持原文 | 可，文本表预留中文 |

## 3. 工作准则

### 3.1 文件与版本
- md（给 Agent）放根目录；Word（给人看）放 `story_draft/`、`purposal_story/`、`TechnicalArt/`；旧版本放 `deprecated/`。
- 新版本另存新文件名，不覆盖用户编辑过的文件；写入前比对设备上的修改时间。
- md 与对应 Word 同源，改一处要同步另一处。
- 参考图放 `ART_ref/`，每次新增或替换都更新 `ART_ref/ASSETS.md`。

### 3.2 设定
- 设定以 `STORY_BIBLE.md` 为准；修改先登记 `DESIGN_CHANGES.md`。
- 为补齐逻辑而新增的细节标「建议」并列入待确认。

### 3.3 范围
- 本项目只做 Demo，体量参考 Battle Car Arena；完整版只作方向。新增内容前先对照 `DEMO_IMPLEMENTATION_PLAN.md` 的范围清单。
- 优先级：完整流程 > 核心机制能看懂 > 画面统一 > 反馈 > 数量。

### 3.4 出图（沿用《妖精丘陵》经验）
- prompt 用英文；一条一个对象；同类图同一风格后缀；不写作品或艺术家名称。
- 角色用 Niji 6 + Character Reference；场景、道具用 V7；选定新造型后用新图作参考并调高 --cw（70–100）。
- 想摆脱参考图配色时 Style reference 留空，并用 --no 排除颜色。
- 网页版不填 URL：把图拖进对应格子，删掉 prompt 里的占位符。
- 编辑器局部重画一次只改一处。
- 文字类资产先用字体排字，再 AI 加质感，最后逐字检查。
- AI 图是概念图，游戏内素材按 `HANDPAINTED_SPEC.md` 在 Photoshop 清理、拆层后进 Unity。
- 场景里放角色时只用低权重 Style Ref；同时用高权重 Style + Character Ref 会变回白底设定图。
- Midjourney 编辑器上传失败时，用 Google AI Studio（Nano Banana 2.1）：局部改先裁 1024² 区块再贴回；统一画风时第二张图放风格参考。
- prompt 里写 lighthouse 一定会画亮灯；要熄灭就用其他词描述塔顶，或后期涂暗。
- 用户图片超过约 2 MB 时远程读取容易失败，请用户直接拖进对话。

### 3.5 质量检查
- Word 交付前渲染为 PDF 检查版式。
- 每张生成图对照 `ART_HANDOFF.md` §4 的“必须保留 / 不要画”逐项检查。
