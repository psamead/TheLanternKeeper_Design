<!-- 美术交接文件：给美术对话（宣传美术 + 技术美术）、Codex 和日后追踪用。结构参考 Animation_yichun《妖精丘陵》的 ART_HANDOFF.md。 -->

# ART_HANDOFF：《The Lantern Keeper》美术宣传 + 技术美术交接

## 0. 怎么用这份文件

- 这是**美术工作**的起点。故事与玩法以 `STORY_BIBLE.md`（v2.0）和 `DEMO_IMPLEMENTATION_PLAN.md` 为准；美术以本文件为准。
- 新对话开始时先读：本文件 → `STORY_BIBLE.md` → `ART_ref/ASSETS.md` → `ART_PROMPTS.md` → `TechnicalArt/HANDPAINTED_SPEC.md`。**实际动手出图按 `TechnicalArt/ART_PRODUCTION_GUIDE.md` 的步骤**（角色 → 道具 → 场景 → NPC → 标题 → 海报 → 菜单 → 像素素材）。
- **设定可以改，但要走流程**：先登记到 `DESIGN_CHANGES.md`。只改美术细节（配色、服装小件）可以直接改并登记；涉及故事含义的只登记为「提议」，确认后再改 `STORY_BIBLE.md`。
- 每完成一项，把第 6 节的 ☐ 改为 ☑，并在第 10 节写一行变更记录；第 9 节是最新交接进度。
- 改动 md 时同步对应的 Word（`purposal_story/`、`TechnicalArt/`）；改前把旧版复制进 `deprecated/`。

## 1. 项目速览

- 游戏：《The Lantern Keeper》（中文工作名《守灯人》），2D 手绘横版解谜，布列塔尼海岸民俗题材。项目：York；协作：Psamead。
- 引擎 Unity 6.3 LTS（URP 2D）；平台 PC（Windows）。
- 游戏内文字、标题、菜单**只用英文**。
- 策略：**小体量 Demo**（11-07 再缩小）：00_StartMenu → 01_Home（奶奶家 + 阁楼，含故事版 A）→ 03_EndCard（故事版 B），4–6 分钟；码头移到完整版。完整版设计只作为方向，见 `purposal_story/守灯人_完整版概念设计说明_v1.0.docx`。

## 2. 关键决定

| 项目 | 决定 |
|---|---|
| 画面风格 | **手绘 2D（2026-11-02 定）**：沿用 Maela / 海报概念图的绘本风，稍微游戏化（线条更干净、明暗 2–3 层）；方向接近《妖精丘陵》但不照搬。原“像素风”方案已作废 |
| 规格 | 参考分辨率 1920×1080；PPU 100；Maela 屏幕高约 1.6 单位（160 px），源文件 2× 绘制；详见 `TechnicalArt/HANDPAINTED_SPEC.md` |
| 双色世界 | 现在层冷（雾蓝灰）、记忆层暖（暖金）；**同一套分层底图**，记忆层靠 Global Light 2D 变色 + 少量单独 Sprite 标志物替换，不重画整套 |
| 生产流程 | AI 出概念图（Midjourney 或 OpenAI 图像）→ 定稿概念 → **Photoshop 清理（统一线条、调色板，去 AI 瑕疵）并拆层** → 场景导出分层 PNG、角色导出 `.psb` 做骨骼动画 → Unity。AI 图不未经清理直接进游戏 |
| 宣传美术 | 海报、菜单主视觉可以比游戏画面更精细，配色用第 4 节调色板。**2026-10-31 起：海报概念图沿用 Maela 定稿的绘本风（Midjourney Niji 6）**；游戏内画风已确定沿用同一绘本风并稍作游戏化（2026-11-02） |
| 字体（2026-11-02 定） | 标题 Cinzel Decorative（油墨毛边，做成图片）；副标题 / 章节卡 IM Fell English SC；菜单 Cinzel；对话 EB Garamond；回忆字幕 Cormorant Garamond Italic。全部 OFL，文件在 `TechnicalArt/fonts/`；决定表 `TechnicalArt/守灯人_字体与UI决定.xlsx` |
| 平台 | 先 PC；不做 Web 压缩 |

## 3. 文件夹约定

| 位置 | 放什么 | 读者 |
|---|---|---|
| 根目录 `*.md` | 给 Agent / Codex 读的说明 | Agent |
| `story_draft/` | 故事设定 Word | 人 |
| `purposal_story/` | 完整版概念设计说明、Demo 制作方案 Word | 人 |
| `TechnicalArt/` | 技术美术与宣传美术给人看的文档、手绘规格、字体 | 人 |
| `ART_ref/` | 参考图、AI 生成图、裁切图、`ASSETS.md` 总表 | 人 + Agent |
| `TechArtAsset/` | **做好的**游戏资产（PSD / PSB 源文件 + 导出 PNG） | 人 + Unity |
| `deprecated/` | 旧版本 | — |

**Git**：本文件夹即公开仓库 `psamead/TheLanternKeeper_Design`（2026-11-03 起）。改完在本地提交，由 Psamead 推送；`deprecated/` 也上传（保留视觉演变）；Unity 那边的截图放 `ForDesignScreenshot/`。`.psd/.psb`、第三方参考图（`ART_ref/BRETON_*`、`FAIRYHILLS_*`）不上传。新增第三方图片时同样写进 `.gitignore`。

规则：新版本另存新文件名（`_v2`），不覆盖用户编辑过的文件。`TechArtAsset/` 子目录与命名：

```text
TechArtAsset/Characters/<Char>/<Char>.psb                                  例：Maela/Maela.psb（骨骼动画）
TechArtAsset/Backgrounds/<Scene>/<Scene>_L0_Sky.png … _L4_Front.png        例：Harbor/Harbor_L3_Ground.png
TechArtAsset/Props/   TechArtAsset/UI/   TechArtAsset/Menu/   TechArtAsset/Audio/<Scene>/   TechArtAsset/Illustrations/   TechArtAsset/Poster/
```

## 4. 与美术有关的故事约束

### 4.1 调色板（约 24 色，全作统一）

| 用途 | Hex |
|---|---|
| 现在层 主色 / 阴影 | #4A5A6E / #1E2633 |
| 记忆层 主色 / 阴影 | #E8B45A / #7A4A2A |
| 梅拉雨衣（全画面最亮） | #F6D743 |
| 灯笼火焰 | #FFF1C9 |
| 海雾 | #9AA3AD |
| UI 文字 | #F2EBDD |

建议从 Lospec 的 Resurrect 32 / Endesga 32 中补足其余颜色，定稿后导出 `TechnicalArt/LK_palette.aco`（Photoshop 色板）。

### 4.2 角色（Demo 需要的）

| 角色 | 外观关键词 | 必须保留 | 不要画 |
|---|---|---|---|
| **Maela** 梅拉（11 岁，玩家） | 明黄雨衣（兜帽放下）、红色短靴、齐肩黑发、深色长袜；**右手**提铜灯笼（11-05 改；概念图为左手） | 雨衣是全画面最亮色；灯笼始终发暖光 | 不要成年感；不要武器；**不要 Q 版**（约 5 头身、正常眼睛，2026-11-02）；Demo 不画斜挎包（11-05） |
| **Soazig** 索齐格（奶奶） | 灰白发髻、深绿羊毛披肩、深色长裙、坐在摇椅上织网；记忆层为年轻版（黑发、白色蕾丝头饰 Coiffe） | Coiffe 只在年轻版出现 | — |
| **Old Per** 老佩尔 | 驼背老渔夫、旧水手帽、蓝色渔夫罩衫、灰胡子，手里一段打结的绳子 | 蓝色罩衫（布列塔尼渔民特征） | — |
| **Flick** 飞蛾 | 8×8，白色、翅膀淡金边、发微光 | — | 不要蝴蝶化 |
| **记忆层人群剪影** | 纯暖色剪影，无细节 | — | — |

### 4.3 道具

| 道具 | 外观 | 状态 |
|---|---|---|
| 灯笼 | 铜制手提风灯、玻璃罩、顶部提环，刻一个小三螺旋纹 | 熄灭 / 点亮 |
| 记忆贝壳 | 扇贝形，内侧发暖金光 | 静止 + 闪烁 2 帧 |
| 梯子 | 木梯 | 断（现在层）/ 完好（记忆层） |

### 4.4 场景（Demo）

| 场景 | 现在层 | 记忆层 |
|---|---|---|
| 01 开始菜单 | 夜晚，熄灭的灯塔立在海边悬崖，海雾 | —（可选：灯塔顶一点灯笼光） |
| 01 Home 奶奶家 + 阁楼（Demo 唯一关卡） | 昏暗石屋、家具盖白布、梯子断 | 阳光、梯子完好、墙上挂渔网与照片 |
| 02 Harbor 码头（**完整版**，Demo 不做） | 断木板、搁浅的蓝色渔船、浓雾 | 节日彩旗、整齐的渔船、人群剪影 |
| 远景（两层共用） | 天空 / 海 / 小镇剪影；可选海平线下伊斯钟楼剪影 | 同一张，用光照变暖 |

## 5. 现有资产状态（详见 `ART_ref/ASSETS.md`）

| 资产 | 状态 | 下一步 |
|---|---|---|
| Maela 概念 | v1 定稿（`ART_ref/Maela_v1.png`） | 转身图 → 游戏版角色（拆部件、骨骼） |
| 海报 | v1 完成（`TechArtAsset/Poster/POSTER_v1.png`；背景 `ART_ref/POSTER_BG_v2.png`） | A3 放大；旧版在 `deprecated/art_2026-11-02/` |
| 开始菜单 | Unity v1 完成（Codex，11-03） | 音效换自然声、加背景音乐 |
| 其余 | 尚未开始 | 按第 6 节顺序 |

## 6. 待办（按顺序）

### 6.1 角色
- ☑ Maela 概念图（AI）→ 选定 → 存为 `ART_ref/Maela_v1.png`；参考图 `MAELA_REF_v1.png` 已裁好
- ☑ Maela 转身图（侧面朝右 + 背面）→ `ART_ref/Maela_v1_turnaround.png`（11-06；侧面参考 `MAELA_SIDE_REF_v1.png`）
- ◐ Maela 游戏版：概念 ☑ `ART_ref/MAELA_GAME_SIDE_v1.png`（11-06）；拆部件计划 `TechArtAsset/Characters/Maela/_work/Maela_parts_plan_v1.png`；◐ `Maela.psb` v1 已导出（11-06，149×320，19 层，Claude 用代码调色 + 切层；大图工作文件 `Maela_src.psd`）。占位待补：左臂 Arm_*_L 为空、Boot_L 被挡部分、大腿、Coat_Body 袖下为自动填补。Unity 导入时 **PPU = 200**（2× 源 → 屏幕 1.6 单位）。细节进 Unity 动起来后再修
- ☐ Maela 骨骼动画：Idle / Run / JumpUp / Fall / Lantern
- ☐ Soazig 现在版 + 年轻版（待机 2–4 帧）
- ☐ Old Per（**完整版**，Demo 不做）
- ☐ Flick（飞行 4 帧，有时间再做）

### 6.2 场景
- ✕ 码头概念图、Harbor 分层底图（11-07 移到完整版）
- ☐ Home 室内分层底图 + 标志物（完好梯子、渔网照片；现在层白布家具、断梯）
- ☐ 远景层（天空、海、伊斯钟楼剪影）两个场景可共用

### 6.3 道具 / UI
- ☐ 灯笼（地上可拾起的版本）；记忆贝壳移到完整版
- ☐ 对话框（9-slice）、头像框 ×3
- ☐ 故事版 A ×4（灯笼的来历）、B ×5（后续引子），画面与字幕见 DEMO_IMPLEMENTATION_PLAN §6

### 6.4 宣传美术（详见 `ART_DIRECTION.md`）
- ☑ 标题字 → `TechArtAsset/Menu/TITLE_v1.png`（+ `_nosub` / `_noglow` / `_glow`）
- ☑ 开始菜单 v1（11-03）：背景 `Menu/MENU_BG_v1.png`，静态稿 `Menu/MENU_v1_mock.png`；分层 L0_BG_1920 / L1_left_dark / TITLE_FRAMED_v1；按钮在 Unity 用 TMP（Cinzel）重建，选中 = 暖金 + 金色下划线 + 左侧小灯笼图标（图标待单独导出）
- ☑ Demo 海报背景 → `ART_ref/POSTER_BG_v2.png`
- ☑ Demo 海报 v2 → `TechArtAsset/Poster/POSTER_v2.png`（1792×2688）+ `POSTER_v2_social.png`（1080×1620），带标题框 `Menu/TITLE_FRAMED_v1.png`；v1 在 deprecated；分层素材在 `Poster/_work/`。待做：A3 放大（PS 保留细节 2.0 → 3508×4961）、可选在 PS 里组成分层 PSD 微调

## 7. 交给 Unity 时

- Import：PPU 100；Filter Mode = Bilinear；Mip Maps 关；Compression = High Quality（主角、UI 用 None）。
- 相机：正交 Size 5.4，不用 Pixel Perfect Camera。
- 碰撞仍用 Tilemap（`Collision_Both / _Present / _Memory`），画面用分层大图；详见 `TechnicalArt/HANDPAINTED_SPEC.md` §5。

## 8. 待确认

1. ~~字体~~：已定（2026-11-02）。待定：UI 边框主题（黄铜铆钉 / 绳结纹）。
2. 主角是否保留“黄色雨衣”作为标志色（建议保留）。
3. ~~出图工具~~：已用 Midjourney（2026-10-31）。
4. ~~Maela 斜挎小包~~：已定（11-05）——Demo 不画；另留“背包版”，完整版作过了新手村之后的储物包（提议，见 DESIGN_CHANGES）。
5. ~~游戏内画风~~：已定为手绘 2D、偏暗民俗奇幻（2026-11-02）；与《妖精丘陵》的借鉴 / 回避见 HANDPAINTED_SPEC §0。
6. ~~Maela 提灯的手~~：已定（11-05）——改**右手**（朝右时灯笼在近镜头一侧）。

## 9. 当前进度与下一步（2026-11-05 更新）

> 下次对话从这里接着做。

**已完成**
- Maela 概念 v1：`ART_ref/Maela_v1.png`（定稿）、`Maela_v1_alt.png`（备选）、`Maela_sheet_B1_REF.png`（表情参考）、`MAELA_REF_v1.png`（白底正面 1024²，作 `--cref` / `--sref`）。
- 海报背景 v2：`ART_ref/POSTER_BG_v2.png`（兜帽放下、红靴；v1 移入 deprecated/art_2026-11-02/；1792×2688，绘本风；灯塔已熄灭；上方约 1/3 留给标题）。评估表：`TechnicalArt/守灯人_海报背景_第3轮评估.xlsx`。
- **游戏画风定为手绘 2D**（2026-11-02）：新规格 `TechnicalArt/HANDPAINTED_SPEC.md`；像素规格移入 `deprecated/`。

**下一步（2026-11-03 更新，建议顺序）**
1. ☑ **开始菜单**（2026-11-03 ~ 05 完成）：
   - ☑ 菜单音频 v1 已做好并经用户确认（2026-11-03）：`TechArtAsset/Audio/Menu/`（BGM 80 s 循环、海浪海风环境声 60 s 循环、悬停浪声 ×3、灯笼确认音、木头返回音；代码合成，无第三方版权，脚本 `_src/synth_menu_audio.py`）。已拷入 Unity `Assets/_Project/Audio/Menu/`。
   - ☑ 按 `CommandForAgentToInitialRun/2026-11-03_Unity_SceneRename_MenuAudio.md` 完成场景重新编号和菜单音频接入；Play Mode 路由通过。扬声器听测与 80 秒循环点监听未验证。
   - ☑ 雾横移 + 灯笼呼吸光（2026-11-05）：素材 `TechArtAsset/Menu/FX/`（预览 `MENU_FX_preview_v2.mp4`）；Unity 提交 `f714830`，雾边缘修复 `dd02e9b`。**开始菜单完成。**（小尾巴：URP 保存场景时给 Main Camera 自动补的 `UniversalAdditionalCameraData` 未提交，下次 Codex 顺手提交。）
2. **▶ Maela**：☑ 转身图 ☑ 游戏版侧面 ☑ `Maela.psb` v1 + 只改颜色的去边 / 灯笼补孔（11-07 定版；Unity 提交 `6ec559b`；部件源在 `TechArtAsset/Characters/Maela/_work/parts_v1_safe/`，大图 `Maela_src.psd`）→ ▶ Run / JumpUp / Fall / Lantern 动画。已知小问题：远眼从鼻梁后露出一点（修要改头发层外框，需 Codex 同时重摆该部件，暂缓）。**改图规则：不改任何图层外框。**
2b. **Demo 范围已定（11-07）**：只做 01_Home + 两段故事版（见 DEMO_IMPLEMENTATION_PLAN v1.1）。美术顺序：▶ Maela Run / JumpUp / Fall / Lantern → Soazig → Home 室内分层底图（楼下 + 阁楼，现在 + 记忆标志物）→ 地上的灯笼 → 对话框 → 故事版 A / B 插图。
3. 海报 A3 放大（PS 保留细节 2.0 → 3508×4961）。

设计仓库（公开，学生只拉取）：<https://github.com/psamead/TheLanternKeeper_Design>，入口 `README.md`（英文）/ `README.zh-CN.md`（中文）。

Unity 现状：`TheLanternKeeper2D` 有四个场景 `00_StartMenu`、`01_Home`、`02_Harbor`、`03_EndCard`；开始菜单 OGG 音效、BGM 与海风环境声已接入，最新提交见 `TechnicalArt/MENU_UNITY_PROGRESS.md`。

**经验库**：`TechnicalArt/LESSONS_ART_PIPELINE.md`（全部踩坑）；Midjourney 细节另见 `ART_PRODUCTION_GUIDE.md` §12。

## 10. 变更记录

| 日期 | 变更 |
|---|---|
| 2026-10-30 | 建立本文件与美术文件夹结构（参考《妖精丘陵》） |
| 2026-10-31 | 新增 `TechnicalArt/ART_PRODUCTION_GUIDE.md` 与对应 Word；同步给人读的 Word（Demo 制作方案 v1.1） |
| 2026-10-31 | Maela 概念图 v1 定稿（Midjourney Niji 6，C01 → Vary Subtle）；裁出 `MAELA_REF_v1.png`；登记 ASSETS.md |
| 2026-10-31 | 海报背景 POSTER_BG_v1 定稿；Word 同步为 v1.1（制作指南、Prompt 集、美术方向，旧版移入 deprecated）；海报概念图画风改为沿用 Maela 绘本风；新增第 9 节交接进度（变更记录移到第 10 节）；第 8 节加画风、提灯手两项待确认 |
| 2026-11-02 | **游戏画风改为手绘 2D**（沿用概念图绘本风、稍游戏化）：更新 §1、§2、§3、§6、§7、§8、§9；新增 `TechnicalArt/HANDPAINTED_SPEC.md`；`PIXEL_ART_SPEC.md` 移入 deprecated |
| 2026-11-02 | 《妖精丘陵》参考入库并拆解；基调定为偏暗民俗奇幻、角色不做 Q 版 |
| 2026-11-02 | 字体系统定稿（五种，均不与《妖精丘陵》重复）；标题 TITLE_v1 导出；新增 `TechnicalArt/守灯人_字体与UI决定.xlsx` |
| 2026-11-02 | 海报 v1 完成：兜帽/靴子用 AI Studio Nano Banana 2.1 局部改（MJ 编辑器上传失败）；记忆层暖金版对齐后做光圈；标题 TITLE_v1 |
| 2026-11-02 | 海报 v2：标题框（蕾丝 + 白鼬尾纹，切角铭牌，同心半圆凹口）；导出 TITLE_FRAMED_v1 / TITLE_FRAME_v1 |
| 2026-11-03 | 开始菜单 v1：背景（MJ 构图 + AI Studio 夜景化）、静态稿与分层；标题框民俗符号改为蕾丝 + 白鼬尾纹 |
| 2026-11-03 | 小灯笼选中图标；_work 整理（AI Studio 过程图 → deprecated/art_2026-11-03/，菜单原图 → ART_ref/MENU_SRC_*）；新增 `TechnicalArt/MENU_UNITY_HANDOFF.md` 与 Codex 指令 |
| 2026-11-03 | Unity 开始菜单 v1：四场景、Build Settings、菜单与占位脚本完成；用户导入 TMP Essentials，Cinzel SDF 及六个文字引用已验证；修复全屏背景反向锚点，Play Mode 输入/场景路由与 1920×1080 Game View 对照 mock 通过。标题/按钮子项已在 DEMO_IMPLEMENTATION_PLAN §7 标记完成，对话框仍待做。提交 `6aa6dc2` 已推送并由远端 main 确认；旧的不完整 Cinzel SDF 和 TMP Examples & Extras 保留为本地未跟踪内容，不在提交中。无独立 Player 构建。详见 TechnicalArt/MENU_UNITY_PROGRESS.md |
| 2026-11-03 | Unity 开始菜单交互反馈：选中线按 TMP 字形边界下移至字形下方 8 UI 单位；新增运行时程序化悬停音与确认音。Play Mode 检查触发两种回调并打开 Settings；无硬件鼠标/扬声器听测或独立 Player 构建。详见 TechnicalArt/MENU_UNITY_PROGRESS.md |
| 2026-11-03 | Unity `02_Home` 占位标题按用户要求由 `02_Home` 改为 `01_Home`；保留 `Esc → menu` 提示与场景文件名。已核对 TMP 文本并记录到 TechnicalArt/MENU_UNITY_PROGRESS.md。 |
| 2026-11-03 | Codex 开始菜单 v1 完成；用户试玩：提示音太电子需换自然声、缺背景音乐；决定先完善菜单再搭场景；新增经验库 `TechnicalArt/LESSONS_ART_PIPELINE.md` |
| 2026-11-03 | 菜单音频 v1（Claude 代码合成，用户确认）：BGM「Gwerz」D 多利亚 3/4 竖琴 + 木笛、海浪海风环境声、悬停 / 确认 / 返回自然音效；源文件 `TechArtAsset/Audio/Menu/`，已放入 Unity `Assets/_Project/Audio/Menu/`；Codex 指令 `CommandForAgentToInitialRun/2026-11-03_Unity_SceneRename_MenuAudio.md` |
| 2026-11-03 | 场景编号改为开始菜单 `00_StartMenu`、章节 `01_Home` / `02_Harbor` / `03_EndCard`；Unity Editor 内重命名并保留 GUID，Build Settings、脚本路由、Harbor/EndCard 占位标签已同步。 |
| 2026-11-03 | Unity 菜单音频接入：OGG 悬停/确认/返回音、循环 BGM 与海风环境声及淡入淡出；Play Mode 验证 Play 到 Home、Escape 返回菜单。未做扬声器听测、80 秒循环监听或独立 Player 构建。提交 `be85569`，详见 `TechnicalArt/MENU_UNITY_PROGRESS.md`。 |
| 2026-11-03 | 按用户要求清空 `01_Home` 的占位标题与 `Esc → menu` 文本，避免其在 Editor 同时加载开始菜单与 Home 时叠显示；场景已保存，单场景各自 AudioListener / EventSystem 正常。提交 `7415565` 已推送至 GitHub `main`；详见 `TechnicalArt/MENU_UNITY_PROGRESS.md`。 |
| 2026-11-03 | 共享文件夹建为 Git 仓库，公开发布到 `psamead/TheLanternKeeper_Design`（学生只拉取）；新增 README（Agent 阅读顺序）、`.gitignore`（不传 deprecated/、源文件、第三方参考图 BRETON_* / FAIRYHILLS_*）；UNITY_AGENTS.md 去掉局域网路径，改指向设计仓库 |
| 2026-11-03 | 仓库已推送到 GitHub；README 改为英文在前（`README.md`），中文另存 `README.zh-CN.md`，顶部互相链接切换；handoff、AGENT_PROCESS_GUIDELINES、LESSONS 与《项目总览与文件说明》Word 加入仓库说明 |
| 2026-11-03 | `deprecated/` 改为上传（方便查看视觉演变）；新增 `ForDesignScreenshot/` 放 Unity / Codex 截图；README 两版同步 |
| 2026-11-03 | 菜单 BGM / 环境声 AudioSource 初始音量保存为 0，由 MenuMusic 淡入至目标音量；Editor 检查 Settings Escape 返回音有效，但音乐源后续报告停止且输出采样为零，持续播放与扬声器听感仍待核验。详见 TechnicalArt/MENU_UNITY_PROGRESS.md。 |
| 2026-11-03 | 菜单跟手调整：悬停浪声 v2（起音即达峰）+ 新选项立即切掉旧声；PLAY → 01_Home 过渡缩短为 0.5 s；Home 恢复占位字、深蓝背景。Unity 改动待提交，详见 MENU_UNITY_PROGRESS |
| 2026-11-04 | 菜单悬停 v3（“哒”声起音 + 停留 1 s 后海浪轻拍）用户确认通过；Codex 提交指令 `2026-11-04_Unity_Commit_MenuFeel.md` |
| 2026-11-05 | 菜单动效：两层雾横移（14 / 26 px/s）+ 灯笼呼吸光（用户要求加强）；素材 `TechArtAsset/Menu/FX/`，脚本已放入 Unity；Codex 指令 `2026-11-05_Unity_MenuFX.md`；Maela 改在新对话进行 |
| 2026-11-05 | 雾层硬边修复：Fog_A / Fog_B 上下边缘 alpha 0、Wrap V = Clamp；Codex 提交指令 `2026-11-05_Unity_FogEdgeFix.md` |
| 2026-11-05 | 开始菜单完成（音频、跟手悬停、动效、雾边修复）；§9 下一步改为 Maela（新对话） |
| 2026-11-05 | 用户在 Unity 装入 Cinemachine 3.1.7；HANDPAINTED_SPEC §相机、UNITY_AGENTS 写入用法（相机跟随一律用 Cinemachine） |
| 2026-11-07 | Maela v1.2：用户在 Unity 里发现“眼睛 / 肩膀重复”——AI 原图不是纯侧脸，远眼从鼻梁后露出；头发与脖子间有透明缝。已涂掉远眼、补缝、压暗棕色发梢；psb 已替换进 Unity；Codex 指令 `2026-11-07_Unity_Maela_v1.2.md` |
| 2026-11-07 | **Demo 范围再缩小（用户确认）**：01_Home（灯笼在楼下拾起 → 故事版 A → 记忆层梯子完好 → 阁楼）+ 03_EndCard 故事版 B；码头、老佩尔、贝壳移到完整版；DEMO_IMPLEMENTATION_PLAN v1.1、handoff、README、UNITY_AGENTS、Demo 制作方案 Word v1.4 同步 |
| 2026-11-07 | 用户确认 v1 + 只改颜色去边版：白边已除，无错位（Unity `6ec559b`）。中间部件图不进 Git（.gitignore） |
| 2026-11-07 | v1.1 / v1.2 改了图层外框 → Unity 部件错位；“整张画布 + 对位脚本”补救失败。**全部回滚到 Unity 1517f47（v1）**，只做“只换颜色”的去边 + 灯笼补孔（逐层核对外框与 v1 一致）；Codex 指令 `2026-11-07_Unity_Maela_v1.2.md` 已改写；规格 §6、经验库改为“进 Unity 后不改外框” |
| 2026-11-07 | 给人读的 Word 同步：`守灯人_出图Prompt集_v1.3`、`守灯人_技术美术方案_手绘规格_v1.1`、`守灯人_美术资产制作指南_v1.4`（新增 §13 Maela 实操经验；HANDPAINTED_SPEC 加 §8.1 以游戏尺寸为准、PPU 200、剪纸式骨骼）；旧版移入 deprecated/ |
| 2026-11-07 | Maela v1.1：全部件去边、灯笼玻璃补孔 + 火焰改暖白光芯；psb 已替换进 Unity（同名、同 meta）；Codex 指令 `2026-11-07_Unity_Maela_Defringe.md`；经验库 §8 |
| 2026-11-06 | Codex 指令 `2026-11-06_Unity_Maela_Import_Idle.md`：PPU 200、剪纸式骨骼（每个部件只绑一根骨）、Idle 3 s、灯笼 Point Light 2D |
| 2026-11-06 | Maela 转身图、游戏版侧面、`Maela.psb` v1（自动拆层，部分占位）完成；登记 ASSETS |
| 2026-11-05 | 开始 Maela：定右手提灯、Demo 不画斜挎包（§4.2、§8）；ART_PROMPTS C01-T / C01-G 改为 v2（去掉 cute / Q 版写法，加 STYLE_GAME 线条与上色部分） |
