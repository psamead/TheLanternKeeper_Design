<!-- 与 purposal_story/守灯人_Demo制作方案_v1.4.docx 同源；更新时两者同步。清单项用 ☐ / ☑ 标记进度。v1.0 在 deprecated/。 -->

# 《The Lantern Keeper》Demo 制作方案（v1.1，2026-11-07）

> **2026-11-07 范围再缩小**（DESIGN_CHANGES）：只做第一章的开头——奶奶家 + 阁楼（新手村），用两段故事版（插图慢推镜头 + 英文字幕）讲清灯笼的来历、引出后面的故事，然后 To be continued。**码头（02_Harbor）、老佩尔、记忆贝壳移到完整版。** 目标：4–6 分钟、能从头玩到尾。

## 1. 范围原则

- 优先级：完整流程 > 核心机制能看懂 > 画面统一 > 故事版氛围 > 反馈表现。
- 先色块后美术：蓝 = 现在层，黄 = 记忆层，灰 = 两层都有。
- 只做一个核心机制：灯笼切换（全屏切换两层）。分层切换的做法借自《妖精丘陵》，Demo 里**不扩展成连续解谜**，只用作叙事表现 + 一处必须切换才能前进的地方。
- 故事靠故事版讲，不靠关卡数量。

## 2. 范围清单

| 级别 | 内容 |
|---|---|
| 必须做 | 3 个 Scene 与切换（00_StartMenu、01_Home、03_EndCard）；移动 / 跳跃；拾起灯笼；灯笼切换；对话框（奶奶）；故事版 A（灯笼的来历，3–4 张）与故事版 B（后续引子，4–5 张）；Back to Menu / Quit |
| 有时间再做 | 飞蛾跟随提示；切换颜色过渡与音效；Home 背景音乐（冷 / 暖两轨）；记忆层窗外灯塔亮灯 |
| 不做（移到完整版） | **02_Harbor 码头、老佩尔、记忆贝壳、人群剪影**；记忆值 / 灯油、烛台检查点、海妖、潮汐、多结局、存档、手柄、中文切换；掉落重生（Home 里没有坑） |

> Unity 里的 `02_Harbor` 场景文件保留给完整版，**从 Build Settings 移除**；编号不改（01_Home 之后直接到 03_EndCard）。

## 3. Demo 流程

| 段落 | 玩家做什么 | 完成标准 | 时长 |
|---|---|---|---|
| 00_StartMenu | 标题 + 夜晚灯塔背景；Play / Settings / Quit | 已完成（11-05） | — |
| 01_Home ① 楼下 | 移动、跳上箱子；和摇椅上的奶奶对话——她认不出梅拉 | 学会移动、跳跃、互动 | 约 1 分钟 |
| 01_Home ② 断梯 | 通往阁楼的梯子断了，上不去 | 看懂“此路不通” | — |
| 01_Home ③ 灯笼 | 在楼下（爷爷的旧箱子旁）拾起灯笼 → **故事版 A：灯笼的来历** → 提示「E」 | 拿到能力，知道为什么 | 约 40 秒 |
| 01_Home ④ 切换 | 按 E 切到记忆层：暖光，梯子完好，墙上渔网和照片出现；可以随时切回现在层看对比 | 学会切换 | — |
| 01_Home ⑤ 阁楼 | **只有在记忆层才能爬梯子**上阁楼；阁楼里看到爷爷留下的东西、窗外的灯塔 → 走到窗边触发结尾 | 一处必须切换才能前进 | 约 1 分钟 |
| 03_EndCard | **故事版 B：后续引子** → “Six days until Anaon night. To be continued…” → Back to Menu | 闭环可重玩 | 约 1 分钟 |

## 4. 机制规格

| 机制 | 规格 | Unity 实现提示 |
|---|---|---|
| 移动 / 跳跃 | 左右 + 单段跳，参数在 Inspector 可调 | Rigidbody2D + BoxCollider2D；Maela 骨骼 Prefab（Idle / Run / JumpUp / Fall） |
| 拾起灯笼 | 拾起前 Maela 手里的 Lantern 部件和 Point Light 2D 隐藏 | GameSession.hasLantern |
| 灯笼切换 | 拿到灯笼后按 E 切换；冷却 0.3 秒 | 碰撞 Tilemap（Present / Memory）开关 TilemapCollider2D；标志物 Sprite 按 WorldLayerObject 显隐 |
| 冷暖 | 现在层冷蓝、记忆层暖金 | Global Light 2D 颜色（HANDPAINTED_SPEC §4） |
| 互动 | 靠近出现提示，按 W | 触发器 |
| 对话 | 底部对话框逐句翻页 | ScriptableObject |
| 故事版 | 全屏插图，每张 5–7 秒慢推 / 慢移（Ken Burns），交叉淡入；底部英文字幕（Cormorant Garamond Italic）；任意键跳到下一张，Esc 跳过整段 | `StoryboardPlayer` + ScriptableObject（图片、字幕、时长、推镜起止）；A、B 共用 |

## 5. 技术结构

| 脚本 | 职责 |
|---|---|
| GameSession | Singleton + DontDestroyOnLoad；`hasLantern` |
| SceneLoader | 切换场景 |
| PlayerController | 移动、跳跃、驱动 Maela Animator |
| LanternSwitch | 切换两层、改光照颜色；事件 `OnWorldSwitched(bool isMemory)` |
| WorldLayerObject | Present / Memory / Both |
| Interactable + DialogueBox | 对话、拾取 |
| StoryboardPlayer | 播放故事版 A / B |
| EndCard | 播放故事版 B，Back to Menu |

Unity 6.3 LTS · 2D URP · 1920×1080，PPU 100（角色 .psb 为 2× 源，PPU 200）· 正交相机 Size 5.4，Cinemachine 3.1 · 2D Animation + PSD Importer · Codex · Git / GitHub。

## 6. 台词与故事版字幕（游戏内英文；故事版字幕为草稿，York 可改）

| 场景 | 角色 | 台词 |
|---|---|---|
| Home | Soazig | Whose child are you, little one? You shouldn't be in a stranger's house. |
| Home | Maela | …Grandma. It's me. |
| Home | Soazig | The lighthouse is dark. Has it always been dark? |
| Home（拾灯笼） | — | The lantern flickers. For a moment, the room looks the way it used to. |

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
- ☑ 建项目、Git；场景互相切换；开始菜单（11-05）
- ☑ PlayerController + Cinemachine 跟随（Home 可玩房间，11-07）
- ☐ 色块搭 Home（楼下、断梯、阁楼）
- ☐ LanternSwitch + 冷暖光照 + WorldLayerObject
- ☐ 对话、拾灯笼、GameSession
- ☐ StoryboardPlayer（A、B）+ EndCard
- ☐ Build Settings 去掉 02_Harbor
- ☐ 试玩 2–3 人并修改
- ☐ 打包 Windows

### 美术（详见 ART_HANDOFF.md）
- ☑ 主角 Maela 定稿 + `.psb` + Idle（11-07）
- ☐ Maela Run / JumpUp / Fall / Lantern（举灯切换）
- ☐ NPC：Soazig（摇椅，Idle）
- ☐ Home 室内分层底图（楼下 + 阁楼）+ 记忆层 / 现在层标志物（完好梯子 / 断梯、渔网、照片、白布家具）
- ☐ 道具：灯笼（地上可拾起的版本）；飞蛾（有时间再做）
- ☐ UI：对话框
- ☐ 故事版 A ×4、B ×5（Midjourney，海报绘本风；1920×1080，推镜头留 15 % 余量 → 源图约 2208×1242）
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

时间更紧时：故事版 A 缩到 2 张、B 缩到 3 张；阁楼只做一个小房间。
