<!-- 与 purposal_story/守灯人_Demo制作方案_v1.6.docx 同源；更新时两者同步。清单项用 ☐ / ☑ 标记进度。v1.0 在 deprecated/。 -->

# 《The Lantern Keeper》Demo 制作方案（v1.3，2026-11-08）

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
| 必须做 | 3 个 Scene 与切换（00_StartMenu、01_Home、03_EndCard）；移动 / 跳跃；拾起灯笼；灯笼切换；对话框（奶奶）；**故事版 P（序章，4 张）**、故事版 A（灯笼的来历，3–4 张）与故事版 B（后续引子，4–5 张）；Back to Menu / Quit |
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
| 01_Home ③ 灯笼 | 在楼下（爷爷的旧箱子旁）拾起灯笼 → **故事版 A：灯笼的来历** → 提示「E」 | 拿到能力，知道为什么 | 约 40 秒 |
| 01_Home ④ 切换 | 按 E 切到记忆层：暖光，梯子完好，墙上渔网和照片出现；可以随时切回现在层看对比 | 学会切换 | — |
| 01_Home ⑤ 阁楼 | **只有在记忆层才能爬梯子**上阁楼；阁楼里看到爷爷留下的东西、窗外的灯塔 → 走到窗边触发结尾 | 一处必须切换才能前进 | 约 1 分钟 |
| 03_EndCard | **故事版 B：后续引子** → “Six days until Anaon night. To be continued…” → Back to Menu | 闭环可重玩 | 约 1 分钟 |

## 4. 机制规格

| 机制 | 规格 | Unity 实现提示 |
|---|---|---|
| 移动 / 跳跃 | 左右 + 单段跳；**默认跑**（3.2），按住 **Shift 慢走**（速度按步幅匹配，约 0.8）；参数在 Inspector 可调 | Rigidbody2D + BoxCollider2D；Maela 骨骼 Prefab（Idle / Walk / Run / JumpUp / Fall / Lantern），动作数据唯一来源 `TechArtAsset/Characters/Maela/_work/anim_v2/poses.py` |
| 拾起灯笼 | 拾起前 Maela 手里的 Lantern 部件和 Point Light 2D 隐藏 | GameState.HasLantern |
| 灯笼切换 | 拿到灯笼后按 E 切换（11-08 定）：**第一次**＝完整长铃声，响铃期间锁定一切操作，铃声结束后场景变换、推动剧情；**之后**＝按 E 立即切换场景并响铃，响铃期间可以移动 / 跳，但 E 无效（直接忽略：不切换、不排队、不发声，保证“铃声 = 切换那一刻”；可选：灯光轻闪一下表示还在响），铃声响完才能再切换 | 碰撞 Tilemap（Present / Memory）开关 TilemapCollider2D；标志物 Sprite 按 WorldLayerObject 显隐 |
| 冷暖 | 现在层冷蓝、记忆层暖金 | Global Light 2D 颜色（HANDPAINTED_SPEC §4） |
| 互动 | 靠近出现提示，按 W | 触发器 |
| 对话 | 底部对话框逐句翻页 | ScriptableObject |
| 故事版 | 全屏插图，每张 5–7 秒慢推 / 慢移（Ken Burns），交叉淡入；底部英文字幕（Cormorant Garamond Italic）；任意键跳到下一张，Esc 跳过整段 | `StoryboardPlayer` + ScriptableObject（图片、字幕、时长、推镜起止）；A、B 共用 |

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
- ☑ 建项目、Git；场景互相切换；开始菜单（11-05）
- ☑ PlayerController + Cinemachine 跟随（Home 可玩房间，11-07）
- ☑ 色块搭 Home（楼下、断梯、阁楼；阁楼梯子与窗口路线 Play Mode 验证，11-12）
- ☑ LanternSwitch + 冷暖光照 + WorldLayerObject（首次锁定铃声、后续即时切换、层物体显隐/碰撞，11-12）
- ☑ Core_Persistent + 叠加关卡（GameState / AudioManager / LevelLoader，11-08）
- ◐ 对话、☑ 拾灯笼（拾灯笼 + W 拾取 + E 提示验证于 11-11；对话待做）
- ☑ StoryboardPlayer：☑ P 序章 + Menu → 序章 → Home（每页可设字幕位置 / 颜色 / underlay，11-08；P2–P4 正式图 + 每页字幕框，11-11）；☑ A、B + EndCard（占位版，拾取 / Home 叠加 / EndCard 按钮与状态重置于 11-11 验证）
- ☑ Build Settings 去掉 02_Harbor（11-07）
- ~~试玩 2–3 人并修改~~（11-12 用户决定：不做）
- ☐ 打包 Windows

### 美术（详见 ART_HANDOFF.md）
- ☑ 主角 Maela 定稿 + `.psb` + Idle（11-07）
- ☑ Maela Run / JumpUp / Fall / Lantern（举灯切换，11-07）；☑ v1.6_m 补画被挡部分 + Walk / Run 分开（11-08）
- ☑ 声音 v1：序章 BGM + 海风浪、Home 屋内环境、脚步 v4、跳 / 落地、举灯 v5（11-08）
- ◐ NPC：Soazig 概念定稿 `ART_ref/SOAZIG_REF_v1.png`（11-09）；☐ 游戏版立绘（摇椅，Idle）
- ◐ Home 楼下现在层底图 v1（Midjourney，11-07 已进 Unity）；☐ 阁楼、记忆层、分层+ 记忆层 / 现在层标志物（完好梯子 / 断梯、渔网、照片、白布家具）
- ☑ 道具：箱子 v1（11-11，`TechArtAsset/Scenes/Home/Props/Crate_v1.png`）；☐ 灯笼（地上可拾起的版本）；飞蛾（有时间再做）
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
