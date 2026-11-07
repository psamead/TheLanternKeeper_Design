# 技术美术规格：手绘 2D 资产与 Unity 管线（v1.1）

> 给美术与 Unity 制作共用。与 `TechnicalArt/守灯人_技术美术方案_手绘规格_v1.1.docx` 同源。取代已移入 `deprecated/` 的 `PIXEL_ART_SPEC.md`（2026-11-02，见 `DESIGN_CHANGES.md`）。
> 标「建议」的数值是起点，做出第一批素材、在 Unity 里试过后可调，调整后登记。

## 0. 风格目标

- **基础**：沿用已定稿概念图的绘本风（`ART_ref/Maela_v1.png`、`POSTER_BG_v2.png`，Midjourney Niji 6）。
- **游戏化**（相对概念图）：外轮廓线更干净统一；明暗压到 2–3 层（亮 / 中 / 暗）加少量柔和渐变；减少笔触噪点；剪影在游戏尺寸下一眼可读。
- **基调**（2026-11-02 修订）：**奇幻为主，带一点民俗的暗与静**；不是儿童绘本，也**不走恐怖**。故事落脚点是人物的抉择与成长：夜和雾是冷的，但画面里永远有一盏暖光、一条能走的路。
- **与《妖精丘陵》**（参考图 `ART_ref/FAIRYHILLS_REF_01–05.png`，2026-11-02 拆解）：

| | 借鉴 | 回避 |
|---|---|---|
| 背景 | 清晰的墨线轮廓 + 平涂 / 赛璐璐上色；强烈的单一光源（日落、林间光柱）；横向长条分层，适合视差 | 大面积暖橙日落主导：我们以冷蓝夜雾为主，暖色只来自灯笼 / 塔灯 |
| 角色 | 民俗服饰细节（纹样、手工感）；干净的外轮廓 | **Q 版比例（2.5 头身）、超大眼睛、粉嫩腮红、柔和粉彩**——太小孩。梅拉保持约 5 头身、正常大小的眼睛、表情克制（以 `Maela_v1.png` 为准） |
| 氛围 | 夜空、发光的门（神秘感） | 甜美、可爱、明亮的整体感 |
| 质感 | 少量排线 / 颗粒肌理增加手工感 | 凯尔特结纹、三螺旋纹（都是它的标志）。**我们的民俗符号是白鼬尾纹（Hermine）+ 布列塔尼镂空蕾丝**（参考 `ART_ref/BRETON_*_REF_01.png`） |

- **一句话**：和《妖精丘陵》同为“手绘民俗奇幻”，但它是暖、甜、Q；我们是冷夜里的一盏暖灯——安静、略带忧郁、最终有希望，角色比例更接近真实。
- **调色板**：仍用 `ART_HANDOFF.md` §4.1；梅拉雨衣 #F6D743 全画面最亮；暖光只来自灯笼与塔灯。

## 1. 基础规格

| 项目 | 规格 |
|---|---|
| 参考分辨率 | 1920×1080（16:9） |
| PPU | 100（1 Unity 单位 = 100 px） |
| 相机 | 正交，Size 5.4（一屏 19.2×10.8 单位）；不使用 Pixel Perfect Camera。跟随用 **Cinemachine 3.1**（2026-11-05 装入）：`CinemachineCamera` + `CinemachinePositionComposer`（跟随 Maela，带少量阻尼）+ `CinemachineConfiner2D`（房间边界 PolygonCollider2D），不写自定义跟随脚本 |
| 关卡网格 | 1 格 = 1 单位 = 100 px（只用于碰撞 / 关卡布局，不再是美术图块） |
| Maela 屏幕高度 | **约 2.2 单位**（2026-11-07 改：.psb 仍是 1.6 单位，Unity 里视觉子物体 ×1.4；相机正交 3.5–3.8 → 约占屏高 1/4–1/3）。原定 1.6 单位 = 160 px 是远景小人比例，配手绘室内背景会显得“缩小了” |
| 绘制倍率 | 源文件按 **2×** 绘制（Maela 源约 320 px 高）。角色 .psb 保持 2× 尺寸，Unity 里用 **PPU 200** 显示为 1.6 单位（2026-11-06） |
| NPC | 与 Maela 同比例（老佩尔驼背略矮） |
| Flick | 约 0.3 单位（30 px） |
| 回忆插图 | 1920×1080（全屏） |
| 头像 | 256×256 |

## 2. 尺度与跳跃（关卡用，与原方案相同）

| 项目 | 数值 |
|---|---|
| 角色高 | 约 2.2 单位（11-07 起；室内家具按“孩子站在正常房子里”对齐：椅子座面到大腿、门约 2 倍身高） |
| 最大跳跃高度 | 2.5 单位 |
| 最大跳跃距离 | 4 单位 |
| 断木板缺口 | 记忆层可走；现在层缺口 ≥ 5 单位 |
| 一个房间 | 约 20×11 到 40×11 单位（相机跟随） |

## 3. 角色：骨骼动画（Unity 2D Animation）

- 包：`com.unity.2d.animation` + `com.unity.2d.psdimporter`。源文件存 `.psb`（Photoshop 大文档格式），每个部件一个图层，图层名用英文。
- 绘制：朝右侧面为基准（依据转身图）；左右翻转用 `flipX`，不另画朝左。

### 3.1 Maela 部件清单

| 部件 | 图层名 |
|---|---|
| 头（含脸） | Head |
| 前发 / 后发 | Hair_Front / Hair_Back |
| 雨衣上身 | Coat_Body |
| 雨衣下摆 | Coat_Hem |
| 上臂、前臂、手 ×2 | Arm_Upper_L/R、Arm_Lower_L/R、Hand_L/R |
| 大腿、小腿 ×2 | Leg_Upper_L/R、Leg_Lower_L/R |
| 靴子 ×2 | Boot_L/R |
| 灯笼 | Lantern（单独 Sprite，挂 Point Light 2D） |

> 提灯用**右手**（2026-11-05 定）：朝右时 Arm_*_R / Hand_R / Lantern 在身体前面（近镜头一侧），图层顺序在 Coat_Body 之上；左臂在 Coat_Body 之下。

### 3.2 动画清单（Demo）

| 角色 | 动作 | 做法 |
|---|---|---|
| Maela | Idle / Run / JumpUp / Fall / Lantern（举灯切换） | 骨骼关键帧；Run 循环约 0.6 秒 |
| Soazig（现在 / 年轻） | Idle（呼吸、织网手部） | 3–5 个部件的简单骨骼 |
| Old Per | Idle（打结） | 同上 |
| Flick | Fly | 逐帧 4 帧或粒子 + 简单 Sprite |
| 贝壳 | Glow | 一张 Sprite + 光强动画 |

## 4. 场景：分层大图

| 层 | 内容 | 视差 |
|---|---|---|
| L0_Sky | 天空、远雾 | 0.9（几乎不动） |
| L1_Far | 海、远处海岸、伊斯钟楼剪影 | 0.7 |
| L2_Mid | 小镇剪影、远景房屋 | 0.4 |
| L3_Ground | 角色站立的码头 / 室内地面（与碰撞对齐） | 0（随世界） |
| L4_Front | 前景雾、草、木桩 | -0.2（比世界快） |

- 每个房间宽度按 §2 计算：40 单位宽的码头 = L3 约 4000 px（1×）。L0–L2 可以比房间窄，靠视差。
- **两层世界**：现在 / 记忆共用 L0–L3 底图，冷暖靠 Global Light 2D；只在记忆层出现的东西（彩旗、完好木板、完好梯子、人群剪影）画成**单独 Sprite**，挂 `WorldLayerObject`（Memory）；只在现在层出现的（断板、白布家具）同理（Present）。

| 层 | Global Light 颜色 | 强度 |
|---|---|---|
| 现在 | #8FA3BF | 0.8 |
| 记忆 | #FFD9A0 | 1.0 |

- 灯笼：Point Light 2D，颜色 #FFF1C9，半径约 3 单位，两层都亮。

## 5. Unity 场景层级（单个关卡）

```
Grid（Cell Size 1）
├─ Collision_Both      （Tilemap，灰盒色块；美术到位后关闭 TilemapRenderer，只留碰撞）
├─ Collision_Present
└─ Collision_Memory
Art
├─ L0_Sky / L1_Far / L2_Mid（Parallax）
├─ L3_Ground
├─ Present（WorldLayerObject = Present 的 Sprite）
├─ Memory （WorldLayerObject = Memory 的 Sprite）
└─ L4_Front
Global Light 2D
Player（Maela 骨骼 Prefab + Lantern Point Light 2D）
Rooms（Respawn 点）
Interactables（NPC、灯笼、贝壳）
```

> 碰撞仍用 Tilemap 搭（灰盒快、好改），画面改由分层大图承担。这样程序端的 `LanternSwitch` / `WorldLayerObject` 结构不变。

## 6. 导入设置

- Texture Type = Sprite (2D and UI)；Pixels Per Unit = 100；Filter Mode = Bilinear；Generate Mip Maps = 关；Compression = High Quality（主角、UI 用 None）；Max Size 按图片实际尺寸（大背景 8192）。
- 角色 `.psb`（2× 源）：PSD Importer，**PPU 200**，Compression None，Mosaic、Use Layer Group 开。骨骼用**剪纸式**：每个部件 100 % 跟一个关节、不做网格变形。Maela 由 Codex 用 Transform 层级实现（Character Rig 关；关节坐标见 `CommandForAgentToInitialRun/2026-11-06_Unity_Maela_Import_Idle.md`）。
- **角色进 Unity 后，改图不得改变任何图层的像素外框**（只改颜色和内部）；改完在 Photoshop 里逐层核对外框与上一版一致。否则 Sprite 裁切范围变化，骨骼里的部件全部错位（2026-11-07 教训）。
- 小物件打 Sprite Atlas。

## 7. 占位色块（灰盒阶段）

| 类型 | 颜色 |
|---|---|
| Present | 蓝 #3B6FD6 |
| Memory | 黄 #E8C341 |
| Both | 灰 #808080 |
| 危险（海） | 深蓝 #102040 |
| 角色 | 白色胶囊 0.8×1.6 单位 |

## 8. 生产流程

AI 概念图（Midjourney Niji 6，风格后缀 STYLE_GAME，见 `ART_PROMPTS.md`）→ 定稿（ASSETS.md 标“当前定稿”）→ **Photoshop 清理**：统一线条与调色板、去 AI 瑕疵、**去边**（浅色背景抠图留下的亮边，深色场景里很显眼）、发光物体内部填实、补缺的部分 → **拆层**（场景按 §4，角色按 §3.1）→ 导出 PNG / `.psb` → `TechArtAsset/` → Unity 替换色块。

### 8.1 清理以游戏尺寸为准（2026-11-07）

角色在游戏里约 160 px 高，很多细节只剩 1–2 px。清理时只检查四件事：**剪影可读、主色对（雨衣全画面最亮）、无浅色毛边、关节转动不露缝**。被挡部分、头发前后层、褶皱细节不精修，进 Unity 动起来后再决定。NPC 和道具同样按此标准。

## 9. 命名与存放

```text
TechArtAsset/Characters/<Char>/<Char>.psb                         例：Maela/Maela.psb
TechArtAsset/Backgrounds/<Scene>/<Scene>_L0_Sky.png … _L4_Front.png    例：Harbor/Harbor_L3_Ground.png
TechArtAsset/Backgrounds/<Scene>/<Scene>_<Layer>_src.psd          （源文件）
TechArtAsset/Props/<Name>.png   TechArtAsset/UI/   TechArtAsset/Illustrations/   TechArtAsset/Menu/   TechArtAsset/Poster/
```
