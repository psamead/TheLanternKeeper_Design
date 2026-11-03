<!-- 与 purposal_story/守灯人_Demo制作方案_v1.0.docx 同源；更新时两者同步。清单项用 ☐ / ☑ 标记进度。 -->

# 《The Lantern Keeper》Demo 制作方案（v1.0）

> 体量参考 Game_zixiang 的 2D Battle Car Arena（菜单 → 一个主要玩法场景 → 结果 → 返回），不是《妖精丘陵》的垂直切片。目标：5–8 分钟、能从头玩到尾。

## 1. 范围原则

- 优先级：完整流程 > 核心机制能看懂 > 画面统一 > 反馈表现 > 内容数量。
- 先色块后美术：蓝 = 现在层，黄 = 记忆层，灰 = 两层都有。
- 只做一个核心机制：灯笼切换（全屏切换两层）。

## 2. 范围清单

| 级别 | 内容 |
|---|---|
| 必须做 | 4 个 Scene 与切换；移动 / 跳跃；灯笼切换；对话框（奶奶、老佩尔）；1 枚记忆贝壳；回忆插图播放；掉落重生；Back to Menu / Quit |
| 有时间再做 | 飞蛾跟随提示；切换颜色过渡与音效；背景音乐 1 首；记忆层远景伊斯钟楼剪影 |
| 不做（完整版内容） | 记忆值 / 灯油、烛台检查点、海妖、潮汐、光圈显现、多结局、存档、手柄、中文切换 |

## 3. Demo 流程

| Scene | 玩家做什么 | 完成标准 | 时长 |
|---|---|---|---|
| 01_StartMenu | 标题 + 夜晚灯塔背景；Play / Quit | 能进入、能退出 | — |
| 02_Home | 和奶奶对话 → 梯子断了 → 拾起灯笼、飞蛾出现、提示 E → 切到记忆层，梯子完好 → 爬上阁楼 → 出口到码头 | 学会移动、跳跃、互动、切换 | 2–3 分钟 |
| 03_Harbor | 房间 A：断木板路只在记忆层完整；房间 B：记忆层人群剪影挡路、现在层塌了一段，需中途切换；房间 C：拾起贝壳交给老佩尔 | 独立完成两次切换谜题 | 3–4 分钟 |
| 04_EndCard | 3 张回忆插图 + 台词；“To be continued…”；Back to Menu | 闭环可重玩 | 1 分钟 |

失败：掉进海里 → 淡出 → 当前房间起点重生。

## 4. 机制规格

| 机制 | 规格 | Unity 实现提示 |
|---|---|---|
| 移动 / 跳跃 | 左右 + 单段跳，参数在 Inspector 可调 | Rigidbody2D + BoxCollider2D |
| 灯笼切换 | 拿到灯笼后按 E 切换；冷却 0.3 秒 | 碰撞 Tilemap（Present / Memory）开关 TilemapCollider2D；分层美术中标志物 Sprite 按 WorldLayerObject 显隐（另一层透明度 30%） |
| 冷暖 | 现在层冷蓝、记忆层暖金 | 改 Global Light 2D 颜色 |
| 互动 | 靠近出现提示，按 W | 触发器 |
| 对话 | 底部对话框逐句翻页 | ScriptableObject |
| 重生 | 掉出画面 → 房间起点 | 空物体标记起点 |

## 5. 技术结构

| 脚本 | 职责 |
|---|---|
| GameSession | Singleton + DontDestroyOnLoad；hasLantern、hasShell |
| SceneLoader | 切换 4 个 Scene |
| PlayerController | 移动、跳跃、重生 |
| LanternSwitch | 切换两层、改光照颜色 |
| Interactable + DialogueBox | 对话、拾取 |
| EndCard | 回忆插图与文字、Back to Menu |

Unity 6.3 LTS · 2D URP · 1920×1080，PPU 100，正交相机 Size 5.4 · 2D Animation + PSD Importer（角色骨骼）· VS Code + Codex · Git / GitHub。

## 6. 台词（游戏内英文）

| 场景 | 角色 | 台词 |
|---|---|---|
| Home | Soazig | Whose child are you, little one? You shouldn't be in a stranger's house. |
| Home | Maela | …Grandma. It's me. |
| Home | Soazig | The lighthouse is dark. Has it always been dark? |
| Home（拾灯笼） | — | The lantern flickers. For a moment, the room looks the way it used to. |
| Harbor | Old Per | Can't remember why I'm tying this knot. Can't remember much at all. |
| Harbor（交还贝壳） | Old Per | Anaon night… We weren't supposed to sail. I jumped. Loïc didn't. |
| EndCard | 画外音 | What you forget doesn't vanish. It sinks. |
| EndCard | — | Six days until Anaon night. To be continued… |

## 7. 实施清单

### 程序
- ☐ 建项目、Git；4 个空 Scene 互相切换
- ☐ PlayerController（色块）
- ☐ 色块搭 Home、Harbor
- ☐ LanternSwitch + 冷暖光照
- ☐ 对话、拾取、GameSession
- ☐ EndCard
- ☐ 试玩 2–3 人并修改
- ☐ 打包 Windows

### 美术（详见 ART_HANDOFF.md）
- ☐ 主角 Maela 定稿 + 骨骼动画
- ☐ NPC：Soazig、Old Per
- ☐ 室内、码头分层底图 + 记忆层 / 现在层标志物
- ☐ 远景层
- ☐ 道具：灯笼、贝壳、飞蛾
- ☑ UI：开始菜单标题与按钮（v1，11-03；Play Mode 与视觉构图已核对）
- ☐ UI：对话框
- ☐ 回忆插图 ×3
- ☑ 开始菜单背景（美术 v1，11-03）
- ☑ Demo 海报（v2，11-02）

## 8. 里程碑（约 6 周）

| 周 | 内容 |
|---|---|
| 1 | 项目、4 Scene 切换、菜单按钮 |
| 2 | 角色控制；色块关卡 |
| 3 | 切换、对话、拾取 → 色块版完整可玩 |
| 4 | 试玩修改；美术并行 |
| 5 | 美术替换 |
| 6 | 声音、修 Bug、打包、录屏 |

时间更紧时：Harbor 缩到 2 个房间，回忆插图缩到 1 张。
