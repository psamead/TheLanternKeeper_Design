# The Lantern Keeper（守灯人）· 设计仓库

[English](README.md) | **简体中文**

2D 手绘横版解谜 Demo 的**设计与美术文档**：故事、玩法方案、美术规格、交接记录、已完成的美术 / 音频资产。
Unity 工程在另一个仓库：<https://github.com/psamead/TheLanternKeeper2D>

> 本仓库**只读**：由 Psamead 维护和推送。拉取后请不要直接修改；有意见请告诉 Psamead / York。

## 最新交接 2026-11-15

Unity 发布已实施并推送至 a469e41；[网页试玩](https://psamead.github.io/TheLanternKeeper2D/) 的浏览器路线已通过。Windows 包和 EXE 启动通过，Windows 游戏内路线及用户视觉/声音验收仍待完成。详见 [发布报告](ForDesignScreenshot/2026-11-15_AtticBaseline_EndCard_Release/after/Release_Report.md)。

5 页作品集 v1 已完成：[PDF 与制作包入口](ForDesignPortfolio/README.md)。新 Agent 从 [ForAgent 总入口](ForAgent/README.md) 开始；本地接续读 [HOME_ART_RESUME](HOME_ART_RESUME.md)。

项目大文件现在使用 Git LFS：PSD/PSB 源文件、录像、作品集可编辑源/PDF，以及 DemoBuilds 中的完整 Windows/Web 交付包。克隆前安装 Git LFS；临时排版缓存和第三方参考图继续保留本地。

## 获取与更新

```bash
# 建议克隆到 Unity 工程旁边（同级文件夹）
git lfs install
git clone https://github.com/psamead/TheLanternKeeper_Design.git
cd TheLanternKeeper_Design
git lfs pull
# 以后更新
git pull
git lfs pull
```

## Agent 先读（按顺序，按需）

1. `ForAgent/Design/ART_HANDOFF.md` **§9「当前进度与下一步」** —— 现在做到哪了、下一步做什么
2. `ForAgent/Design/handoff.md` —— 项目速览、Demo 范围、代码约定
3. `ForAgent/Design/DEMO_IMPLEMENTATION_PLAN.md` —— 场景、机制、台词、实施清单（§7）
4. `ForAgent/Design/STORY_BIBLE.md` —— 故事与设定（v2.0）
5. `TechnicalArt/HANDPAINTED_SPEC.md` —— 画风、分辨率、导入设置
6. `TechnicalArt/LESSONS_ART_PIPELINE.md` —— 踩过的坑
7. `ForAgent/Unity/UNITY_AGENTS.md` —— Unity 端规则（Unity 仓库根目录的 `AGENTS.md` 由它而来）

最近发生了什么：看 `ForAgent/Design/ART_HANDOFF.md` §10 变更记录、`TechnicalArt/MENU_UNITY_PROGRESS.md`，或 `git log`。

## 场景（Demo）

`00_StartMenu` → `01_Home`（奶奶家 + 阁楼，含故事版 A）→ `03_EndCard`（故事版 B）→ 回菜单。`02_Harbor` 留给完整版，不进 Demo（2026-11-07 缩小范围）。

## 文件夹

| 位置 | 内容 |
|---|---|
| `ForAgent/` | 当前设计原件、Agent 总入口、Unity 规则与跨电脑作品集交接 |
| 根目录 README / *_RESUME / 工作准则 | 项目入口、本地接续和协作约定 |
| `story_draft/`、`purposal_story/` | 故事设定、Demo 方案（Word） |
| `TechnicalArt/` | 技术美术与宣传美术文档、字体（OFL）、Unity 进度记录 |
| `ART_ref/` | 概念图、参考图、`ASSETS.md` 资产总表 |
| `TechArtAsset/` | 做好的游戏资产（导出 PNG、OGG） |
| 根目录 `HOME_ART_RESUME.md` | 本地美术 / 设计 Codex 的对话接续摘要，不是执行任务单 |
| `CommandForAgentToInitialRun/` | 发给 Unity 工作站 / 网络端 Codex 的按日期可执行任务单；见其中 README |
| `ForDesignPortfolio/` | 另一台设计电脑制作的学生 4–5 页 PDF、可编辑源包与页面预览 |
| `ForDesignScreenshot/` | Unity / Codex 那边的截图，供设计核对 |
| `deprecated/` | 被取代的旧版本和过程图（保留视觉演变） |

未上传：临时 QA 缓存、第三方参考图（`BRETON_*`、`FAIRYHILLS_*`，`ASSETS.md` 中有登记但只在本地）。

## 版权

- 字体：SIL Open Font License，见 `TechnicalArt/fonts/OFL_*.txt`。
- 菜单音频由代码合成（`TechArtAsset/Audio/Menu/_src/synth_menu_audio.py`），无第三方素材。
- 其余设计文档与美术为本项目作品，仅供本课程 / 项目协作使用。
