# 守灯人：资料、归档与经验索引

更新：2026-11-18。本页整理资料关系，不产生新的游戏需求或测试结果。

## 先找当前事实

| 要解决的问题 | 当前入口 | 使用边界 |
|---|---|---|
| 新 Agent 如何接手 | [统一入口](README.md)、[工作准则](../AGENT_PROCESS_GUIDELINES.md) | 按任务继续阅读，不遍历执行全部历史任务 |
| Demo 做到哪里、还做什么 | [Demo 方案](Design/DEMO_IMPLEMENTATION_PLAN.md)、[设计变更](Design/DESIGN_CHANGES.md) | 完整版故事方向不等于 Demo 待办 |
| 当前资产用哪版 | [美术交接](Design/ART_HANDOFF.md)、[Home 知识库](../TechnicalArt/HOME_ART_KNOWLEDGE_BASE.md)、[故事版选图](../TechArtAsset/Storyboard/STORYBOARD_SELECTION.md) | 最新明确决定优先于旧提示词和旧录像 |
| Unity 实施、构建和验证 | [任务索引](../CommandForAgentToInitialRun/README.md)、[实施进度](../TechnicalArt/MENU_UNITY_PROGRESS.md)、[发布报告](../ForDesignScreenshot/2026-11-15_AtticBaseline_EndCard_Release/after/Release_Report.md) | 准备、实施、测试和用户验收分开记录 |
| 作品集成品与下轮制作 | [交付入口](../ForDesignPortfolio/README.md)、[制作状态](PORTFOLIO_PRODUCTION_STATUS.md)、[后续交接](PORTFOLIO_NEXT_HANDOFF.md) | 首版 PDF 的证据早于后来的网页发布验证 |
| 为什么这样做、下次如何复用 | [导入历史](CLAUDE_CONTEXT_2026-11-18.md)、[美术制作经验](../TechnicalArt/LESSONS_ART_PIPELINE.md)、[MJ 经验](MIDJOURNEY_PROJECT_LESSONS.md) | 历史理由和试验参数不能自动成为当前要求 |

## Claude 原始记忆的核对结果

原始资料位于设计电脑 `C:/Users/Administrator/Documents/MyFlie/ClaudeMemory/`。先读该目录的 `README.md` 和 `IMPORTED_CONTEXT.md`；原始摘要位于 `claude-memory-2026-11-18/`。这些本机路径不保证在另一台电脑成立。

本次直接阅读的原始摘要：

- `projects/GameDev_TheLanternKeeper_York_Design/areas/york-game-project.md`
- `projects/GameDev_SP_YiChun_Design/areas/fairy-hills-game.md`
- `topics/working-style.md`

| 原始摘要内容 | 本项目处理方式 |
|---|---|
| 小 Demo、手绘 2D、布列塔尼民俗、英文游戏文本 | 当前设计已有记录，保留理由，不另建一套设定 |
| 第一章教学村庄、阁楼取得能力、菜单到 Home 的旧序章构想 | 只作历史；当前路线按 Demo 方案，不用旧摘要重排拾灯和故事 A |
| 11-15 中午展示、跳过试玩 | 已过期的任务条件，不恢复；后续实际测试报告继续有效 |
| 设计放共享目录，网络不可达才读 GitHub | 交接优先给共享路径；回退时记录原因及所用提交，避免读到旧文档 |
| 妖精丘陵的文件分类、MD 与 Word 同步 | 可复用组织方法；守灯人采用自己的当前目录，不照搬另一项目目录和角色决定 |
| 妖精丘陵旧的禁止 Agent 自测、机器账号、订阅和软件环境 | 不提升为守灯人通用规则；需要时重新核实实际环境 |
| 先跑通再迭代、根据本机输出诊断 | 用于组织工作；不能把“先跑通”记成最终质量或用户验收 |

完整原始导出继续留在 ClaudeMemory，公开设计仓库只保留与本项目有关的归纳和来源。已有导入上下文及 MJ 方法笔记不重复复制为新副本。

## 文件归档去向

| 文件类别 | 保存位置 | 最少记录 |
|---|---|---|
| 当前设计和 Agent 规则 | `ForAgent/Design/`、`ForAgent/Unity/` | 当前版本、替代关系、相关任务链接 |
| 人读 Word | `story_draft/`、`purposal_story/`、`TechnicalArt/` | 对应 MD、版本；内容改变时同步，交付前渲染检查 |
| Unity 可执行任务 | `CommandForAgentToInitialRun/` | 目标、资产、验收、回报位置；README 指向当前单 |
| 本地续接 | 根目录 `*_RESUME.md` | 最新状态放顶部，旧状态明确为历史 |
| 用户截图、视频和运行证据 | `ForDesignScreenshot/YYYY-MM-DD_主题/` | 来源、版本/提交、用途；用户原件与 `after/` 新证据区分 |
| 正式资产与参考资料 | `TechArtAsset/`、`ART_ref/` | 批准/候选/拒绝状态；参考索引更新 `ART_ref/ASSETS.md` |
| 被替代的设计文档与旧资产 | `deprecated/` 对应日期/类别 | 原路径、新路径、为何替代、替代版本 |
| 运行包和作品集 | `DemoBuilds/日期_主题/`、`ForDesignPortfolio/` | 源提交/素材版本、依赖、验证限制 |
| 临时处理和 Word 排版检查 | 对应 `_work/`、`.story_document_qa/` | 不作为成品和新验收，不批量加入 Git |

历史执行单及其证据保留原目录，通过状态与索引归档。不要仅因为日期旧就移动或删除；如确需移动，先确认无并行编辑，记录映射并修复引用。正式原画、交付包按 `.gitattributes` 的 LFS 规则提交；第三方参考和临时缓存按 `.gitignore` 保留本地。日期旧不等于可以公开。

## 把一次经历写成可复用经验

经验写入既有知识库或制作经验，避免每次新增一份重复总结。建议每条使用以下结构：

1. **问题与条件**：场景、资产版本、模型/软件版本、实际观察到的症状。
2. **证据与原因**：报告、原始截图/录像及时间码；区分已确认原因与推测。
3. **处理与结果**：具体改了什么，在哪种环境验证，哪些仍未验证。
4. **复用边界**：适合什么情况，不能直接照搬的参数和条件。
5. **来源**：当前设计、实施提交或历史摘要路径；用户认可只写明确认可的范围。

可直接延续的学习方向：先锁定最小完整路线；为参考图分别指定身份、构图和风格用途；以同轮镜头对比画面；将物理地板、落点与角色脚底一起验证；作品集图注明原画/故事版/真实运行截图。具体案例已在相关知识库，不再复制一遍。

## 本次整理记录

- 确认此前已导入项目上下文与 MJ 经验，未重复导入或执行旧任务。
- 修正工作准则中“运行包被忽略”“源文件不上传”与现行 LFS 约定冲突的描述。
- 修正截图总索引中过期的待执行单，补入最终发布与用户全流程录像入口。
- 将接续摘要中已被后续回报覆盖的“最新状态”改为“历史快照”。
- 未移动或删除原始素材，未修改游戏设计、人读 Word 或 Unity 工程，未新增运行验证和用户验收。
