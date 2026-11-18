# 守灯人 Agent 统一入口

## 最新反馈与接手提醒 2026-11-18

2026-11-18 用户反馈：网络另一台机器上的 Codex 已跑过 Unity，暂未发现问题；作品集制作端 Codex 也已跑过，暂未发现问题。来源为用户本次转述，本地未重新运行。此反馈作为继续工作的可用基线；未指定 EXE/Web、具体提交、测试路线或作品集软件兼容性，不扩写为所有平台及所有细节最终验收。

后续接手与资料维护注意事项见 [资料与经验索引](PROJECT_ARCHIVE_AND_LEARNING.md)。下方保留先前制作和验证记录；其中待审阅说明应结合本次反馈阅读，不自动重开旧任务。

更新：2026-11-18。这里按用途集中当前设计原件、Agent 规则与跨电脑交接。根目录只保留项目 README、本地接续与工作准则；从本入口按任务进入，避免扫描历史任务。

| 当前工作 | 先读 | 写回位置 |
|---|---|---|
| 阅读已完成的作品集 | [`ForDesignPortfolio/README.md`](../ForDesignPortfolio/README.md) | PDF、预览、原生源及制作包在 `ForDesignPortfolio/` |
| 更新作品集 | [Agent 制作规则](PORTFOLIO_PRODUCTION_AGENT.md) → [后续版本交接](PORTFOLIO_NEXT_HANDOFF.md) → [首轮原始交接](PORTFOLIO_PRODUCTION_HANDOFF.md) | 新版本另存于 `ForDesignPortfolio/`，回写 [制作状态](PORTFOLIO_PRODUCTION_STATUS.md) |
| Unity 三项小修、Windows 导出与网页试玩 | [Unity 当前任务入口](../CommandForAgentToInitialRun/README.md) | Unity 工程与共享进度记录；运行包放 DemoBuilds |
| 本地设计、美术与反馈审阅 | [本地接续摘要](../HOME_ART_RESUME.md) → [工作准则](../AGENT_PROCESS_GUIDELINES.md) | 相关设计说明、TechnicalArt 与人读文档 |

## 项目定位与现状

The Lantern Keeper／守灯人是布列塔尼民俗奇幻题材的手绘风格 2D 叙事解谜 Demo。核心体验是用灯笼照见过去，通过现在/记忆两层的差异找到阁楼通路。用户认可自己录制的整段视频整体效果，当前只交接阁楼基线、B5 直接出选项、EndCard Quit 回菜单三项小修，以及随后构建发布。

Unity 三项小修已实施；游戏提交 `6adac6ca9d5532c9f646defca38c94255e55070c` 和 Pages 工作流已推送，Unity `main` 当前为 `a469e412e5867ac488aac5558f17682c4c582ffd`。网页 Demo 已在 Chrome 实际走通主要路线；Windows 完整包和 EXE 启动已确认，但 Windows 游戏内路线仍待用户验收。作品集 5 页 v1 已生成并归档。详见 [Unity 发布进度](../TechnicalArt/MENU_UNITY_PROGRESS.md)、[发布实测](../ForDesignScreenshot/2026-11-15_AtticBaseline_EndCard_Release/after/Release_Report.md) 与 [作品集状态](PORTFOLIO_PRODUCTION_STATUS.md)。当前 Home 背景仍按用户确认版本保留。

## 按需查资料

- [Demo 范围和当前设计](Design/DEMO_IMPLEMENTATION_PLAN.md)，最新小修见 §4.4。
- [故事设定](Design/STORY_BIBLE.md)：完整版设想要与已做 Demo 区分；游戏内英文。
- [Home 当前知识库](../TechnicalArt/HOME_ART_KNOWLEDGE_BASE.md) 与 [制作经验](../TechnicalArt/LESSONS_ART_PIPELINE.md)。
- [Unity 实际进度](../TechnicalArt/MENU_UNITY_PROGRESS.md)：最新条目优先，不把历史待办重新执行。
- [故事版选图理由](../TechArtAsset/Storyboard/STORYBOARD_SELECTION.md)。
- [作品集阅读入口](../ForDesignPortfolio/README.md)、[制作 Agent 规则](PORTFOLIO_PRODUCTION_AGENT.md)、[后续版本交接](PORTFOLIO_NEXT_HANDOFF.md) 与 [已完成制作状态](PORTFOLIO_PRODUCTION_STATUS.md)。
- [用户完整录像索引](../ForDesignScreenshot/2026-11-15_Home_FullDemo_Recordings/README.md)：是现有已认可流程参考，不强制另录一段完整流程。

## 文件分工

ForAgent 放新 Agent 总入口与跨电脑交接；CommandForAgentToInitialRun 保留 Unity 可执行任务；根目录 *_RESUME.md 放本地接续。ForDesignPortfolio 放作品集 PDF 与可编辑制作包；ForDesignScreenshot 放游戏/用户截图与录像；DemoBuilds 放运行包；.story_document_qa 放 Word 排版检查。

2026-11-15 已将原根目录的 7 份设计说明迁入 Design/，Unity Agent 规则原件迁入 Unity/；相关 Markdown 链接与当前任务引用同步更新，不在根目录保留多份原件。旧阅读顺序如仍写根目录文件名，请按本入口找当前原件。

| 位置 | 内容 |
|---|---|
| Design/ | Demo 方案、故事、美术、项目速览与变更记录的当前原件 |
| Unity/UNITY_AGENTS.md | 同步到 Unity 工程 AGENTS.md 的规则原件 |
| PORTFOLIO_PRODUCTION_HANDOFF.md | 首轮作品集制作要求和事实边界（首版已完成） |
| PORTFOLIO_PRODUCTION_AGENT.md | 作品集 Agent 编辑流程、证据与品牌规则 |
| PORTFOLIO_NEXT_HANDOFF.md | 后续版本所需信息和交付步骤 |
| PORTFOLIO_PRODUCTION_STATUS.md | 已完成 v1 的素材、工具与验证记录 |
| ../TechnicalArt/ | 知识库、可复用经验、Unity 实施报告、人读 Word |
| ../CommandForAgentToInitialRun/ | Unity 当前执行任务与历史任务单 |

## Design 目录查找

| 要找的内容 | 当前原件 |
|---|---|
| 项目速览和代码分工 | [handoff](Design/handoff.md) |
| Demo 范围、流程、台词和最新小修 | [Demo 制作方案](Design/DEMO_IMPLEMENTATION_PLAN.md) |
| 世界观、人物与完整版构想 | [Story Bible](Design/STORY_BIBLE.md) |
| 设计决定与状态变化 | [设计变更](Design/DESIGN_CHANGES.md) |
| 美术约束和当前进度 | [美术交接](Design/ART_HANDOFF.md) |
| 标题、海报、菜单视觉系统 | [美术方向](Design/ART_DIRECTION.md) |
| 出图提示词与历史生成参数 | [美术提示词](Design/ART_PROMPTS.md) |
| Unity 工作站规则原件 | [Unity Agent 规则](Unity/UNITY_AGENTS.md) |


## Claude 历史上下文与经验（2026-11-18）

[导入上下文与可复用经验](CLAUDE_CONTEXT_2026-11-18.md)：已对照当前发布、作品集和设计入口；只补充历史理由与经验，不恢复旧截止日期或旧测试限制，不改变当前设计。共享 Obsidian 知识库的 TheLanternKeeper2D 分区有对应副本。


Midjourney 实用方法：[提示词、参考图与迭代经验](MIDJOURNEY_PROJECT_LESSONS.md)。含两项目的实测案例、失败边界、未测试模板和来源记录格式；不改变现有美术定稿。


资料查找、历史归档、Claude 记忆核对与经验写法：[资料与经验索引](PROJECT_ARCHIVE_AND_LEARNING.md)。
