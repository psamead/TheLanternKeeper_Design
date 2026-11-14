# Home 美术：本地对话接续

## 最新状态 2026-11-15 第二轮

Unity 第一轮探索任务已在 `c7ba7f2` 实施并回报连续路线，实际听音仍未验收。用户观看后明确修正：未拾灯只显示 Press T，不能记录探索；必须 T 拾灯并结束 A，回门边，再进入原灯位区显示 Broken ladder、去梯位查看后才解锁 E。此前允许拾灯前记录探索的说明不再适用。

新执行单为 `CommandForAgentToInitialRun/2026-11-15_Unity_PickupGate_StoryAudio_Attic.md`，还包含 A4 收尾重现修复、铃声完整响完后才渐隐文字并停用两个旧区/启用梯子传送区、阁楼淡入即站稳且不能掉回楼下。音频为 A1 渐强至正常、A2 正常、A3 较低+海浪、A4 保持低音量且无海浪、结尾 B 正常音乐+海风。当前背景正确，不调整背景。

本地已检查代码和用户 85 秒录像：RecordExploration 缺少持灯/A 完成门槛、首铃 Used/锁定立即关闭提示；A4 收尾先变暗又露出与 fadeBackAtEnd=1 在结束回调之前揭开黑幕相符。阁楼具体下落/坠穿原因仍需 Unity 端按新要求复现，不能把旧报告最终 Grounded 读数当作可见过程通过。新要求与灯笼照见记忆、Demo 单向进阁楼的剧情一致，不新增瞬移能力设定。

用户 12 张附图和原始录像归档在 `ForDesignScreenshot/2026-11-15_Home_Pickup_Story_Attic/`。本轮是新单准备和证据整理，未直接修改网络 Unity 工程；任务待那边 Codex 读取执行。旧任务已加已执行/后续入口标识。

## 2026-11-15 第一轮快照（历史，已实施）

用户补充确认：当前 Unity 铃铛关卡背景图正确。新标注借用了之前错误版本的录像画面，仅用于碰撞区与文字位置；本轮不据此调整或回退当前背景。此限制已同步到 11-15 Unity 执行单。

Unity `a84fa68` 已完成 11-14 视觉单：T 提示固定到地上灯笼，Present 带暗梯 v1 / Memory 无梯 v3 + 完整梯 v5，故事版 A 小字去框，EndCard 灯笼图标与下划线。详见 `TechnicalArt/MENU_UNITY_PROGRESS.md` 11-14 回报。v5 仍待用户最终认可；最新视觉版本尚缺一条连续穿过阁楼出口到 B5 的新录像，实际听音和独立构建未验证。

用户 11-15 授权本轮只做两项：首次 E 要按序经历铃铛区探索（显示远处固定 Broken ladder）、梯位查看（解锁固定 Press E），然后才允许首次摇铃出梯；EndCard 选项移入女孩左侧红框。当前执行单：`CommandForAgentToInitialRun/2026-11-15_Unity_FirstBell_Exploration_EndCard.md`。两个提示为世界位置固定、触发后持续；首次解锁前 E 无任何副作用，菜单重开重置。任务已放共享入口，目前可见会话中未连接网络工作站 Codex，不能声称已发送聊天消息或已开跑；用户需让那边 Codex 读取任务单。

新用户标注归档到 `ForDesignScreenshot/2026-11-15_Home_FirstBell_Exploration/`；两段 11-13 旧视频归到 `2026-11-13_Home_User_Recordings/`，原字节保留，不是本轮实现的验收。下面 11-14 / 11-13 各节为当时快照。

## 2026-11-14 续接快照（历史）

Unity 端 `3417fc4` 已接入楼下 v3、阁楼 v3、灯笼 v4 和完整梯 v4，并完成两轮路线检查；此文件下方的 11-13「尚未实施」描述是旧快照。用户新一轮视觉反馈及执行要求以 `CommandForAgentToInitialRun/2026-11-14_Unity_Home_Visual_Refinement.md` 为准：现在层改用带梯子的 `Home_Present_v1.png`，记忆层用无梯的 v3、滤镜及独立完整梯；拾灯提示固定在灯上方；故事版 A 右下小字去框；EndCard 选择项采用开始菜单灯笼图标和下划线。机制与其他 Bug 留到后续。

完整梯 v5 已用 PhotoCraft CLI 对 v4 PNG 清理透明残留，保留 1440×4200 及完全不透明的原画像素；`TechArtAsset/Scenes/Home/Props/Ladder_Whole_v5.png` 是待 Unity 游戏画面验收的候选，v4 PNG 和 PSD 保留。用户标注图归档至 `ForDesignScreenshot/2026-11-13_Home_Visual_Notes/`。新视觉任务已准备交由 Unity 端 Codex 执行，尚未实施或验收。`TechnicalArt/HOME_ART_KNOWLEDGE_BASE.md` 的 11-13 状态是历史记录，与上述新决定冲突时以本节和 11-14 执行单为准。

## 2026-11-13 续接快照（历史）

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
