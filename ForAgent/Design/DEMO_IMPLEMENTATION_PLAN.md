<!-- 2026-11-15 文档迁移：当前原件在 ForAgent/Design/DEMO_IMPLEMENTATION_PLAN.md；除可点击相对链接外，文内文件路径相对共享根目录。 -->

<!-- 与 purposal_story/守灯人_Demo制作方案_v2.0.docx 同步内容；Markdown 与 Word 版本号各自递增。清单项用 ☐ / ☑ 标记进度。v1.0 在 deprecated/。 -->

# 《The Lantern Keeper》Demo 制作方案（v1.6，2026-11-15：阁楼与结尾小修及构建待执行）

本轮用户已认可昨晚录像整体效果。当前任务为阁楼脚底基线抬到绿线、B5 直接出选项、EndCard 两个选项均回开始菜单；随后交付 Windows x64 完整包、push Unity 并尝试 Web/Pages。任务已准备，Unity 与构建发布尚未执行；详见 §4.4 和 CommandForAgentToInitialRun/README.md。以下保留历次范围与实现规格。

> **2026-11-07 范围再缩小**（DESIGN_CHANGES）：只做第一章的开头——奶奶家 + 阁楼（新手村），用两段故事版（插图慢推镜头 + 英文字幕）讲清灯笼的来历、引出后面的故事，然后 To be continued。**码头（02_Harbor）、老佩尔、记忆贝壳移到完整版。** 目标：4–6 分钟、能从头玩到尾。
>
> **v1.2（2026-11-07）加序章**：开始菜单 → **故事版 P：序章（4 张，约 25 秒）** 交代地点、海雾带走记忆、梅拉来到奶奶家、奶奶认不出她 → 进入 01_Home。做法：静态插图 + 慢推 / 慢移为主；P1（无人物空镜）**试用 Google Flow（Veo）**做 8 秒动画，效果不好就退回静态。Flow 的深入调试不在本项目做（留给《妖精丘陵》项目）。

> **v1.3（2026-11-08）**：Unity 改为常驻场景 `Core_Persistent` + 叠加关卡（照《妖精丘陵》）；Maela 分走 / 跑（默认跑，Shift 慢走）；灯笼切换规则定稿（第一次全锁 + 推动剧情，之后只挡 E）；序章、Home、角色音效 v1 已进 Unity。

## 1. 范围原则

- 优先级：完整流程 > 核心机制能看懂 > 画面统一 > 故事版氛围 > 反馈表现。
- 先色块后美术：蓝 = 现在层，黄 = 记忆层，灰 = 两层都有。
- 只做一个核心机制：灯笼切换（全屏切换两层）。分层切换的做法借自《妖精丘陵》，Demo 里**不扩展成连续解谜**，只用作叙事表现 + 一处必须切换才能前进的地方。
- 故事靠故事版讲，不靠关卡数量。

## 2. 范围清单

| 级别 | 内容 |
|---|---|
| 必须做 | 3 个 Scene 与切换（00_StartMenu、01_Home、03_EndCard）；移动 / 跳跃；拾起灯笼；灯笼切换；对话框（奶奶）；**故事版 P（序章，4 张）**、故事版 A（灯笼的来历，3–4 张）与故事版 B（后续引子，4–5 张）；Back to Menu / Quit（EndCard 两者均回菜单，§4.4） |
| 有时间再做 | 飞蛾跟随提示；切换颜色过渡与音效；Home 背景音乐（冷 / 暖两轨）；记忆层窗外灯塔亮灯 |
| 不做（移到完整版） | **02_Harbor 码头、老佩尔、记忆贝壳、人群剪影**；记忆值 / 灯油、烛台检查点、海妖、潮汐、多结局、存档、手柄、中文切换；掉落重生（Home 里没有坑） |

> Unity 里的 `02_Harbor` 场景文件保留给完整版，**从 Build Settings 移除**；编号不改（01_Home 之后直接到 03_EndCard）。

## 3. Demo 流程

| 段落 | 玩家做什么 | 完成标准 | 时长 |
|---|---|---|---|
| 00_StartMenu | 标题 + 夜晚灯塔背景；Play / Settings / Quit | 已完成（11-05） | — |
| 序章（故事版 P） | 点 Play 后播放 4 张插图 + 字幕；任意键下一张，Esc 跳过 → 淡入 01_Home | 知道在哪、发生了什么、奶奶为什么认不出梅拉 | 约 25 秒 |
| 01_Home ① 楼下 | 移动、跳上箱子；和摇椅上的奶奶对话——她认不出梅拉 | 学会移动、跳跃、互动 | 约 1 分钟 |
| 01_Home ② 断梯 | 通往阁楼的梯子断了，上不去 | 看懂“此路不通” | — |
| 01_Home ③ 灯笼 | 按 T 拾灯 → **故事版 A：灯笼的来历** → 回门边 → 原灯位探索 → 梯位检查 → 首次 E 摇铃 | 先探索并看懂断梯，再用灯推进故事 | 约 40 秒 + 探索 |
| 01_Home ④ 切换 | 首次 E 完整摇铃后，记忆层完整梯出现；之后 E 按既定规则切换两层 | 看见记忆中的通路 | — |
| 01_Home ⑤ 阁楼 | **只有在记忆层**靠近完整梯下方才自动淡变到阁楼；阁楼里看到爷爷留下的东西、窗外的灯塔 → 走到窗边触发结尾 | 一处必须切换才能前进 | 约 1 分钟 |
| 03_EndCard | **故事版 B：后续引子** → “Six days until Anaon night. To be continued…” → Back to Menu | 闭环可重玩 | 约 1 分钟 |

## 4. 机制规格

最新用户小修与交付以 §4.4 为准；§4.1–4.3 的门槛和声音意图继续作为回归检查。

| 机制 | 规格 | Unity 实现提示 |
|---|---|---|
| 移动 / 跳跃 | 左右 + 单段跳；**默认跑**（3.2），按住 **Shift 慢走**（速度按步幅匹配，约 0.8）；参数在 Inspector 可调 | Rigidbody2D + BoxCollider2D；Maela 骨骼 Prefab（Idle / Walk / Run / JumpUp / Fall / Lantern），动作数据唯一来源 `TechArtAsset/Characters/Maela/_work/anim_v2/poses.py` |
| 拾起灯笼 | 拾起前 Maela 手里的 Lantern 部件和 Point Light 2D 隐藏 | GameState.HasLantern |
| 灯笼切换 | 拿到灯笼后按 E 切换（11-08 定）：**第一次**＝完整长铃声，响铃期间锁定一切操作，铃声结束后场景变换、推动剧情；**之后**＝按 E 立即切换场景并响铃，响铃期间可以移动 / 跳，但 E 无效（直接忽略：不切换、不排队、不发声，保证“铃声 = 切换那一刻”；可选：灯光轻闪一下表示还在响），铃声响完才能再切换 | 碰撞 Tilemap（Present / Memory）开关 TilemapCollider2D；标志物 Sprite 按 WorldLayerObject 显隐 |
| 冷暖 | 现在层冷蓝、记忆层暖金 | Global Light 2D 颜色（HANDPAINTED_SPEC §4） |
| 互动 | 靠近出现提示，按 W | 触发器 |
| 对话 | 底部对话框逐句翻页 | ScriptableObject |
| 故事版 | 全屏插图，每张 5–7 秒慢推 / 慢移（Ken Burns），交叉淡入；底部英文字幕（Cormorant Garamond Italic）；任意键跳到下一张，Esc 跳过整段 | `StoryboardPlayer` + ScriptableObject（图片、字幕、时长、推镜起止）；A、B 共用 |

### 4.1 Home 首次探索与阁楼路线（2026-11-15 用户确认）

本节记录用户最新确认的目标流程。Unity `a803050` 是上一轮实现基线；用户随后指出需要再次核对/修正，本节不能视为已通过。该要求现并入 §4.4 最新任务的回归核对，当前执行入口见 `CommandForAgentToInitialRun/README.md`。

| 阶段 | 玩家行为 | 反馈与门槛 |
|---|---|---|
| 拾灯前 | 在原灯位置探索或按 E | 只显示固定的 Press T；不记录探索，不显示 Broken ladder / Press E，不触发铃声或切层 |
| 拾灯与故事 A | 按 T 拾灯，观看或跳过 A1–A4 | A 完成前探索仍未开始；结束后女孩回到门边并恢复操作 |
| 发现断梯 | 从门边重新走到原灯位探索区 | 记录第一步，并在远处固定位置显示 Broken ladder |
| 检查断梯 | 之后新进入梯位探索区 | 记录第二步，并在固定位置显示 Press E |
| 首次摇铃 | 新按 E | 铃声完整播放；梯子出现后两条提示才渐隐，两处探索区停用，独立梯子触发区接管阁楼传送 |
| 阁楼与结尾 | 自动淡变到阁楼，走到窗口触发 B | 淡入第一帧角色已站在地板上；不可从阁楼掉回楼下；结尾保持正常音乐并加海风 |

E 是“使用灯笼”的动作；T 是“拾取灯笼”的动作。提示必须由探索顺序解锁并固定在世界位置。未解锁输入无副作用、不排队。菜单重开后本局探索进度重置。

### 4.2 故事版 A/B 音频意图（2026-11-15）

| 段落 | 音乐 | 环境声 |
|---|---|---|
| A1 守灯人 | 由低渐升至正常叙事音量 | 不加本轮指定的海浪 |
| A2 灯塔与小镇 | 延续正常音量 | 保持页面现有环境声 |
| A3 灯塔熄灭 | 比 A2 降低 | 有可听见的海浪 |
| A4 女孩举灯 | 保持与 A3 相同 | 海浪停止；不应出现重复的无字幕 A4 |
| B 与 EndCard | 正常音乐连续播放，包括最终停留页 | 加海风；音乐和风声独立调节 |

具体音量、淡变时长与实听结果由 Unity 实施记录；旧的“整段故事统一 duck”描述不覆盖此逐页意图。

### 4.3 当前执行状态

上一轮 `a803050` 有 Editor 路线和边界报告；此前 follow-up 没有新执行回报。用户最新认可昨晚录像整体效果，并提出 §4.4 三项小修和构建发布要求；门槛、A4、声音与安全并入最新任务的回归核对。新单已准备，Unity/Windows/Web/Pages 尚未执行。当前 Home 背景正确；扬声器听感、实体键鼠与独立构建分别记录。

### 4.4 最新录屏小修与交付 2026-11-15

2026-11-15 录屏补充：用户已有完整录像看起来正常，直接作既有流程参考，不强制 Unity Codex 再录完整流程；只对新改动保存对应截图/必要短片，EXE/浏览器运行仍须实测。作品集跨电脑制作另读 `ForAgent/PORTFOLIO_PRODUCTION_HANDOFF.md`；作品集不是新增可玩关卡。

用户认可昨晚录屏版本整体效果，并提出三项小修：阁楼人物脚底行走基线提高至绿线；故事 B5 结束时直接在当前画面显示选项，不再淡黑再重新显示 B5；EndCard 的 Quit 同样返回开始菜单。之后由 Unity 工作站导出完整 Windows x64 可运行包，定向提交并 push Unity 仓库，再尝试 Web 构建及 GitHub Pages 网页试玩。

当前执行入口为 `CommandForAgentToInitialRun/2026-11-15_Unity_AtticBaseline_EndCard_Windows_Web.md`。本地已准备任务与三张用户图，未在 Unity 实施、未导出 EXE、未部署网页。`a803050` 是已知上一轮游戏实现基线；`122e013` 仅更新 Unity 文档链接。用户认可录像整体效果，不等同于此前全部边界、扬声器或独立构建已通过。此前 follow-up 未有新执行报告，其门槛、A4、音频与安全条目并入新单的回归核对，已符合的项目保留。当前 Home 背景继续沿用用户确认版本。

| 项目 | 目标 | 状态 |
|---|---|---|
| 阁楼行走线 | 靴底提高至绿线，实体地板、安全落点及必要窗触发同步；楼下不随改 | 已确认，待 Unity |
| B5 收尾 | 末页图、字幕、最终镜头保持，直接显示左侧选项，不二次淡黑或重播 B5；声音连续 | 已确认，待 Unity |
| EndCard Quit | 保留标签，和 Back to Menu 一样返回开始菜单并重置；开始菜单自身 Quit 保留 | 已确认，待 Unity |
| Windows x64 | 完整 EXE 依赖目录与 ZIP，实际启动并走通；交付 DemoBuilds | 待导出与实跑 |
| Unity Git | 定向提交/push 并核对远端 hash | 待工作站执行 |
| Web 与 Pages | Unity Web 构建、HTTP 本地运行、部署 Pages、真实 HTTPS 完整路线 | 待尝试，未上线 |

范围仍是 Menu/P → Home/A/阁楼 → EndCard/B；本轮不新增奶奶立绘/对白/UI 等旧待办作为导出前置。用户认可昨晚录像整体效果，本轮修改后的结果仍待用户验收。截图见 `ForDesignScreenshot/2026-11-15_AtticBaseline_EndCard_Release/README.md`。可运行包与 Word QA 分别归档到 DemoBuilds/ 和 .story_document_qa/。

## 5. 技术结构



| 脚本 | 职责 |
|---|---|
| Core_Persistent（场景） | 常驻：Maela、Main Camera（唯一 AudioListener）、Cinemachine + Confiner2D、Global Light 2D、EventSystem、下面三个单例 |
| GameState | 单例；`HasLantern`、`MemoryLayer` |
| AudioManager | 单例；BGM / 环境声各两路交叉淡入淡出 |
| LevelLoader | 单例；叠加加载关卡、移到 SpawnPoint、按 LevelInfo 设相机边界 / ortho / 环境声 / 光，卸载上一关 |
| LevelInfo + SpawnPoint + LevelBootstrap | 每个关卡场景里；Bootstrap 让 Editor 里单独打开关卡也能玩 |
| SceneLoader | 菜单 / 序章 / EndCard 等普通场景切换 |
| PlayerController + MaelaAudio | 移动、跳跃、走 / 跑、举灯锁定；MaelaAudio：脚步（动画事件）/ 跳 / 落地一个声源（随机音高），灯笼单独声源（音高固定） |
| LanternSwitch | 切换两层、改光照颜色；事件 `OnWorldSwitched(bool isMemory)` |
| WorldLayerObject | Present / Memory / Both |
| Interactable + DialogueBox | 对话、拾取 |
| StoryboardPlayer | 播放故事版 P（序章）/ A / B；支持静态图（Ken Burns）和短视频（VideoPlayer，给 Flow 空镜用） |
| EndCard | 播放故事版 B，Back to Menu |

Unity 6.3 LTS · 2D URP · 1920×1080，PPU 100（角色 .psb 为 2× 源，PPU 200）· 正交相机 Size 5.4，Cinemachine 3.1 · 2D Animation + PSD Importer · Codex · Git / GitHub。

## 6. 台词与故事版字幕（游戏内英文；故事版字幕为草稿，York 可改）

| 场景 | 角色 | 台词 |
|---|---|---|
| Home | Soazig | Whose child are you, little one? You shouldn't be in a stranger's house. |
| Home | Maela | …Grandma. It's me. |
| Home | Soazig | The lighthouse is dark. Has it always been dark? |
| Home（拾灯笼） | — | The lantern flickers. For a moment, the room looks the way it used to. |

**故事版 P：序章（4 张，Menu → Home 之间）**

| # | 画面 | 字幕（草稿） | 做法 |
|---|---|---|---|
| P1 | 布列塔尼海岸的夜，灯塔熄灭 | On the coast of Brittany, the old lighthouse has gone dark. | 插图；试 Flow 8 秒空镜，不好就用静态 |
| P2 | 海雾漫进小镇的窗户 | Each night the sea fog rolls in, and takes a little of what people remember. | 插图 + 慢推 |
| P3 | 梅拉提着行李站在奶奶家门口（背影） | Seven days before the Night of Anaon, Maela comes to stay with her grandmother. | 插图 + 慢移（有人物，不用 Veo） |
| P4 | 清晨，奶奶坐在摇椅上，看着梅拉像看陌生人 | The next morning, Grandma looks at her as if she were a stranger. | 插图 + 慢推 → 淡出进 Home |

> P1 与 A3 都提到灯塔熄灭：序章只交代现状，A 讲原因，不冲突。表格版：`TechnicalArt/LanternKeeper_Prologue_Storyboard.xlsx`。

**故事版 A：灯笼的来历（3–4 张）**

| # | 画面 | 字幕（草稿） |
|---|---|---|
| A1 | 灯塔顶，守灯人（爷爷扬，背影）从塔灯引火到手提灯笼 | Every night, the keeper carried fire from the great lamp down into this lantern. |
| A2 | 灯光照亮的海岸与小镇，光圈外是雾 | The Lantern Pact: where the light falls, memory belongs to people. |
| A3 | 一年前，灯塔熄灭，海雾漫上岸 | Then the lighthouse went dark, and the fog came ashore. |
| A4 | 梅拉手里的灯笼亮起，屋里一角变暖 | The lantern still remembers. In its light, the past comes back. |

**故事版 B：后续引子（4–5 张，结尾）**

| # | 画面 | 字幕（草稿） |
|---|---|---|
| B1 | 阁楼窗外，熄灭的灯塔与海 | What you forget doesn't vanish. It sinks. |
| B2 | 二十年前亡灵之夜，两条渔船出海（暖色记忆） | Twenty years ago, on Anaon night, two fishermen sailed when no one should. |
| B3 | 一人跳回岸上，另一人追着远处的光消失 | One jumped back to shore. The other followed a light that never brought him home. |
| B4 | 一年前，爷爷站在熄灭的塔灯前，雾中有人影 | Last year, the keeper put out the lamp — and the sea took him too. |
| B5 | 梅拉提灯站在码头尽头，远处钟楼剪影 | Six days until Anaon night. To be continued… |

## 7. 实施清单

### 程序
- ◐ 上一轮 `a803050` 已实施并有 Editor 报告；用户认可录像整体效果，§4.4 三项小修及 Windows/Web 交付任务待工作站执行，旧问题并入回归核对。
- ☑ 11-15 首次摇铃第一版 `c7ba7f2` 与后续门槛修正 `a803050` 均已实施并 Editor 验证；EndCard 选项移位保留。第二轮未覆盖项（真实扬声器、物理键鼠、独立构建）见 `TechnicalArt/MENU_UNITY_PROGRESS.md`。
- ☑ 建项目、Git；场景互相切换；开始菜单（11-05）
- ☑ PlayerController + Cinemachine 跟随（Home 可玩房间，11-07）
- ◐ Home 路线上一轮通过 Editor 检查；最新的拾灯门槛、A4 结尾、提示交接、阁楼安全与音频需求并入 §4.4 新单回归核对。Present 断梯灰盒已移除；保留固定 `Broken ladder` 信息提示。
- ☑ LanternSwitch + 冷暖光照 + WorldLayerObject（首次锁定铃声、后续即时切换、层物体显隐/碰撞，11-12）
- ☑ Core_Persistent + 叠加关卡（GameState / AudioManager / LevelLoader，11-08）
- ◐ 对话、☑ 拾灯笼（11-13 实际 T 输入拾取、A 后单一 E 提示；对话待做）
- ◐ StoryboardPlayer：P/A/B 与 EndCard 路线已接入；上一轮报告称 A4/逐页音频已修正，但最新反馈要求复核 A4 是否重复显现、声场时序和落点衔接。回归核对见 §4.4；扬声器实听未做。
- ☑ Build Settings 去掉 02_Harbor（11-07）
- ☑ 11-13 Home 修正：P/A/B 故事版遮罩、统一世界提示、镜头边界、B5 按钮缩放；梯子 v5 去除白边后由 `a803050` 接入并在路线录像中使用。素材最终美术接受仍待用户确认。
- ~~试玩 2–3 人并修改~~（11-12 用户决定：不做）
- ☐ 按 §4.4 小修后导出并实际运行 Windows x64 完整包；push Unity 后尝试 Web 构建与 Pages 真实 URL 验证

### 美术（详见 ForAgent/Design/ART_HANDOFF.md）
- ☑ 主角 Maela 定稿 + `.psb` + Idle（11-07）
- ☑ Maela Run / JumpUp / Fall / Lantern（举灯切换，11-07）；☑ v1.6_m 补画被挡部分 + Walk / Run 分开（11-08）
- ☑ 声音 v1：序章 BGM + 海风浪、Home 屋内环境、脚步 / 跳落 / 举灯；Unity `a803050` 加入 A/B 逐页增益、独立海浪与海风。真实扬声器混音与听感仍待验收。
- ◐ NPC：Soazig 概念定稿 `ART_ref/SOAZIG_REF_v1.png`（11-09）；☐ 游戏版立绘（摇椅，Idle）
- ◐ Home 楼下共用无梯 `Home_Present_v3.png` 已由用户确认，阁楼 `Attic_PerspectiveRef_v3.png` 与完整梯 `Ladder_Whole_v5.png` 已接入；当前背景不变。其余分层物件待做，素材美术验收以用户最终反馈为准。
- ☑ 道具：箱子 v1（11-11，`TechArtAsset/Scenes/Home/Props/Crate_v1.png`）；灯笼拾取/手持改用 `Lantern_v4.png`（11-13）；飞蛾（有时间再做）
- ☐ UI：对话框
- ◐ 故事版 ☑ **P ×4（序章，11-11 完成）**；◐ A ×4、B ×5（MJ 第一轮 11-11，见 ART_PROMPTS §4c）（Midjourney，海报绘本风；1920×1080，推镜头留 15 % 余量 → 源图约 2208×1242）
- ☑ UI：开始菜单（11-05）
- ☑ Demo 海报（v2，11-02）

## 8. 里程碑（约 4–5 周）

| 周 | 内容 |
|---|---|
| 1 | 角色控制 + 色块 Home + 切换；Maela 动作 |
| 2 | 对话、拾灯笼、故事版播放器（占位图）→ 色块版完整可玩 |
| 3 | 试玩修改；Soazig、Home 分层美术 |
| 4 | 故事版插图、美术替换、声音 |
| 5 | 修 Bug、打包、录屏（缓冲） |

时间更紧时：序章缩到 2 张（P1 + P4）、故事版 A 缩到 2 张、B 缩到 3 张；阁楼只做一个小房间；Flow 动画直接放弃，全用静态图。
