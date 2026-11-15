# The Lantern Keeper（守灯人）· 设计仓库

[English](README.md) | **简体中文**

2D 手绘横版解谜 Demo 的**设计与美术文档**：故事、玩法方案、美术规格、交接记录、已完成的美术 / 音频资产。
Unity 工程在另一个仓库：<https://github.com/psamead/TheLanternKeeper2D>

> 本仓库**只读**：由 Psamead 维护和推送。拉取后请不要直接修改；有意见请告诉 Psamead / York。

## 最新交接 2026-11-15

当前 Home 背景已由用户确认正确。Unity `a803050` 是上一轮实现基线。用户随后提出 follow-up，要求复核未持灯门槛、按序探索、A4 收尾、逐页声音、阁楼落点和 EndCard 选项。新任务已准备给 Unity 工作站 Codex，尚未执行；上一轮 Editor 报告不能代替新要求的验收。

当前设计先读 [Demo 流程与音频 cue](DEMO_IMPLEMENTATION_PLAN.md)、[Home 美术知识库](TechnicalArt/HOME_ART_KNOWLEDGE_BASE.md)、[Unity 进度报告](TechnicalArt/MENU_UNITY_PROGRESS.md) 和[本地接续说明](HOME_ART_RESUME.md)。新 Unity 任务单已准备，等用户在另一台机器让 Codex 读取；入口见 [CommandForAgentToInitialRun](CommandForAgentToInitialRun/README.md)。12 张用户截图和原始录像索引见 `ForDesignScreenshot/2026-11-15_Home_Pickup_Story_Attic/README.md`；全流程参考录像见 `ForDesignScreenshot/2026-11-15_Home_FullDemo_Recordings/README.md`。

给人阅读的 Word 版：[Home 美术交接与经验 v3](TechnicalArt/守灯人_Home美术交接与经验_2026-11-15_v3.docx)，[Demo 制作方案 v1.8](purposal_story/守灯人_Demo制作方案_v1.8.docx)。

## 获取与更新

```bash
# 建议克隆到 Unity 工程旁边（同级文件夹）
git clone https://github.com/psamead/TheLanternKeeper_Design.git
# 以后更新
git pull
```

## Agent 先读（按顺序，按需）

1. `ART_HANDOFF.md` **§9「当前进度与下一步」** —— 现在做到哪了、下一步做什么
2. `handoff.md` —— 项目速览、Demo 范围、代码约定
3. `DEMO_IMPLEMENTATION_PLAN.md` —— 场景、机制、台词、实施清单（§7）
4. `STORY_BIBLE.md` —— 故事与设定（v2.0）
5. `TechnicalArt/HANDPAINTED_SPEC.md` —— 画风、分辨率、导入设置
6. `TechnicalArt/LESSONS_ART_PIPELINE.md` —— 踩过的坑
7. `UNITY_AGENTS.md` —— Unity 端规则（Unity 仓库根目录的 `AGENTS.md` 由它而来）

最近发生了什么：看 `ART_HANDOFF.md` §10 变更记录、`TechnicalArt/MENU_UNITY_PROGRESS.md`，或 `git log`。

## 场景（Demo）

`00_StartMenu` → `01_Home`（奶奶家 + 阁楼，含故事版 A）→ `03_EndCard`（故事版 B）→ 回菜单。`02_Harbor` 留给完整版，不进 Demo（2026-11-07 缩小范围）。

## 文件夹

| 位置 | 内容 |
|---|---|
| 根目录 `*.md` | 给人和 Agent 读的说明与交接 |
| `story_draft/`、`purposal_story/` | 故事设定、Demo 方案（Word） |
| `TechnicalArt/` | 技术美术与宣传美术文档、字体（OFL）、Unity 进度记录 |
| `ART_ref/` | 概念图、参考图、`ASSETS.md` 资产总表 |
| `TechArtAsset/` | 做好的游戏资产（导出 PNG、OGG） |
| 根目录 `HOME_ART_RESUME.md` | 本地美术 / 设计 Codex 的对话接续摘要，不是执行任务单 |
| `CommandForAgentToInitialRun/` | 发给 Unity 工作站 / 网络端 Codex 的按日期可执行任务单；见其中 README |
| `ForDesignScreenshot/` | Unity / Codex 那边的截图，供设计核对 |
| `deprecated/` | 被取代的旧版本和过程图（保留视觉演变） |

未上传：`.psd/.psb` 源文件、第三方参考图（`BRETON_*`、`FAIRYHILLS_*`，`ASSETS.md` 中有登记但只在本地）。

## 版权

- 字体：SIL Open Font License，见 `TechnicalArt/fonts/OFL_*.txt`。
- 菜单音频由代码合成（`TechArtAsset/Audio/Menu/_src/synth_menu_audio.py`），无第三方素材。
- 其余设计文档与美术为本项目作品，仅供本课程 / 项目协作使用。
