# Home 美术：本地对话接续

用途：供本地美术 / 设计 Codex 新对话恢复上下文；本文件不是 Unity 执行命令。发给另一台 Unity 工作站 / 网络端 Codex 的可执行任务单放在 `CommandForAgentToInitialRun/`，当前 Home 执行单见 [Unity Home 审查与接入](CommandForAgentToInitialRun/2026-11-13_Unity_Home_Review_Art_Transition_Audio.md)。目录分类规则见 [CommandForAgentToInitialRun/README.md](CommandForAgentToInitialRun/README.md)。

先读 TechnicalArt/HOME_ART_KNOWLEDGE_BASE.md、ART_HANDOFF.md 第 9 节、ART_ref/ASSETS.md、ART_PROMPTS.md、TechnicalArt/MENU_UNITY_PROGRESS.md 末尾。

当前暂停点：Home 灰盒功能已有 Unity b61eb3f 的验证记录；用户已给出新一轮实机问题并授权按执行单处理。文档与资产已整理推送；Unity 实施和验收仍待执行。

- 风格优先：保留 MJ 手绘笔触与绘本感，房间透视可接受。
- 灯笼用 TechArtAsset/Scenes/Home/Props/Lantern_v4.png；由用户清理 v3_m 后改名，1032×1875 透明 PNG。
- 阁楼当前候选用 TechArtAsset/Scenes/Home/Attic/_candidates/Attic_PerspectiveRef_v3.png；用户在 Subtle 放大的 v2 上用 Photoshop 去除画中梯子并处理窗外灯塔灯部，2912×1632，仍需场景适配。v2 保留，v3 分层源在 `Attic/_work/Attic_PerspectiveRef_v3.psd`。
- 完整梯当前候选为 `TechArtAsset/Scenes/Home/Props/Ladder_Whole_v4.png`（1440×4200，透明 PNG；用户手工拼接，PSD 在 Props/_work/Ladder_Whole_v4.psd），剧情传送用独立完整梯；现在层梯位留空，钟声后出现并用于触发锁输入淡变到阁楼；不制作断梯配对、不做操作式攀爬。尚未接入 Unity。旧平面阁楼与灯笼 v1/v2 不作为默认采用图。
- 先按 `CommandForAgentToInitialRun/2026-11-13_Unity_Home_Review_Art_Transition_Audio.md` 处理用户列出的 Unity 设计问题。不要把图片已下载等同于游戏已验收。
- 局域网共享文件优先；GitHub fallback 必须记录原因、路径和提交号。源 PSD/PSB 和部分历史候选仅在本地。

- 楼下无梯底图用 `TechArtAsset/Scenes/Home/Present/Home_Present_v3.png`（2520×1080），源在 `Present/_work/Home_Present_v3.psd`。用户说明同一底图加滤镜、触发后叠加独立梯子；此图尚未接入 Unity，具体触发与滤镜实现待核对。

## 2026-11-13 用户实机反馈后的最新决定

以另一台 Unity 工作站 Codex 的执行任务单为准：`CommandForAgentToInitialRun/2026-11-13_Unity_Home_Review_Art_Transition_Audio.md`。它取代旧 Demo 的 W 拾取、可爬梯、断梯占位物及断梯配对前置要求：拾取建议 T；现在层梯位为空并提示 Broken ladder；钟声切换后显示完整梯，进入梯下范围锁输入并淡变到阁楼，不播放攀爬。修正镜头、故事透底、提示重叠、EndCard 按钮内部缩放并接通 Home/A 中段音乐。已归档截图并查看录屏抽帧，尚未在 Unity 实施或验证。
