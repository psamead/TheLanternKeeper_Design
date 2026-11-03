# 技术美术规格：像素资产与 Unity 管线（v1）

> 给美术与 Unity 制作共用。与 `TechnicalArt/守灯人_技术美术方案_像素规格.docx` 同源。

## 1. 基础规格

| 项目 | 规格 |
|---|---|
| 参考分辨率 | 320×180（16:9），整数 6 倍到 1920×1080 |
| PPU | 16 |
| 图块 | 16×16 |
| 主角 / NPC | 16×24（站在地面上约 1.5 格高） |
| 飞蛾 | 8×8 |
| 回忆插图 | 160×90（显示时放大 2 倍） |
| 头像 | 32×32 |
| 调色板 | ART_HANDOFF §4.1，导出 `LK_palette.gpl` |

## 2. 尺度与跳跃（关卡用）

| 项目 | 数值 |
|---|---|
| 角色高 | 1.5 格 |
| 最大跳跃高度 | 2.5 格（40 px） |
| 最大跳跃距离 | 4 格（64 px） |
| 断木板缺口 | 记忆层可走；现在层缺口 ≥ 5 格（跳不过去，必须切换） |
| 一个房间 | 20×11 格（= 一屏）到 40×11 格 |

## 3. 动画清单（Demo）

| 角色 | 动作 | 帧数 | 每帧时长 |
|---|---|---|---|
| Maela | Idle / Run / JumpUp / Fall / Lantern | 4 / 6 / 2 / 2 / 3 | 150 / 80 / 100 / 100 / 80 ms |
| Soazig（现在 / 年轻） | Idle | 4 / 2 | 200 ms |
| Old Per | Idle（打结） | 4 | 200 ms |
| Flick | Fly | 4 | 80 ms |
| 贝壳 | Glow | 2 | 400 ms |

Sprite Sheet：每个动作一行，从左到右；导出 `<Char>_sheet.png` + Aseprite JSON（可选）。

## 4. 图块与双层世界

- 一套码头图块 ≈ 30 块：地面、木板（完好 / 断）、桥墩、栏杆、船、石墙、渔网、箱子。
- 现在层与记忆层**共用图块**；记忆层只替换标志物（彩旗、完好木板、人群剪影）。冷暖由 Global Light 2D 控制：

| 层 | Global Light 颜色 | 强度 |
|---|---|---|
| 现在 | #8FA3BF | 0.8 |
| 记忆 | #FFD9A0 | 1.0 |

- 灯笼：Point Light 2D，颜色 #FFF1C9，半径 3 格，两层都亮。

## 5. Unity 场景层级（单个关卡）

```
Grid
├─ Tilemap_Background
├─ Tilemap_Both        （两层都有，灰色块）
├─ Tilemap_Present     （只在现在层，蓝色块）
├─ Tilemap_Memory      （只在记忆层，黄色块）
└─ Tilemap_Foreground
Global Light 2D
Player（Maela + Point Light 2D）
Rooms（每个房间一个起点 Respawn）
Interactables（NPC、灯笼、贝壳）
Parallax（L0_Sky / L1_Sea / L2_Town）
```

## 6. 导入设置

Filter Mode = Point；Compression = None；Sprite Mode = Multiple；Pixels Per Unit = 16；Mesh Type = Full Rect（图块）。相机：Pixel Perfect Camera，Assets PPU 16，Ref 320×180，Upscale Render Texture 开启。

## 7. 占位色块（灰盒阶段）

| 类型 | 颜色 |
|---|---|
| Present | 蓝 #3B6FD6 |
| Memory | 黄 #E8C341 |
| Both | 灰 #808080 |
| 危险（海） | 深蓝 #102040 |
| 角色 | 白 16×24 |

## 8. 生产流程

AI 概念图 → 定稿（ASSETS.md 标“当前定稿”）→ Aseprite 用 `LK_palette.gpl` 重绘 → 导出 PNG → `TechArtAsset/` → Unity 替换色块（同名 Sprite 直接替换引用）。
