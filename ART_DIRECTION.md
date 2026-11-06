<!-- 宣传美术方向。与 TechnicalArt/守灯人_美术方向_标题海报菜单_v1.3.docx 同源。 -->

# 《The Lantern Keeper》美术方向：标题 · 海报 · 开始菜单

## 1. 目的

为 Demo 准备三件宣传 / 门面资产：标题字、开始菜单背景、Demo 海报。它们是玩家和评审最先看到的画面，也是作品集首页图。

## 2. 标题

| 项目 | 内容 |
|---|---|
| 正式标题 | **The Lantern Keeper** |
| 副标题 | A Tale from the Breton Coast（IM Fell English SC，米白） |
| 字体（2026-11-02 定） | 标题 Cinzel Decorative + 油墨毛边（轻）；副标题 IM Fell English SC；菜单 Cinzel；对话 EB Garamond；回忆字幕 Cormorant Garamond Italic。详见 `TechnicalArt/守灯人_字体与UI决定.xlsx` |
| 排版 | 两行：THE LANTERN / KEEPER；“O” 可替换成灯笼图形 |
| 颜色 | 暖金 #E8B45A，外描深海蓝 #1E2633，内发光 #FFF1C9 |
| 流程 | 先用字体排出正确的字 → 导出 PNG → AI Retexture 加铜质感（可选）→ 逐字检查拼写 → 存 `TechArtAsset/Menu/TITLE.png` |

## 3. 关键画面

### K1 Demo 海报（竖版 2:3）

- 构图：梅拉背影站在悬崖小路上，举起灯笼；前方是熄灭的灯塔。灯笼光圈内是暖金色的“过去的小镇”，光圈外是冷蓝雾；海面下隐约有伊斯钟楼。
- 上方 1/4 留给标题；下方留一行小字：Demo · 2026 · PC。
- 核心卖点一眼可见：**灯光照见过去**。
- 尺寸：出图 2:3 → 输出 A3（297×420 mm，300 dpi）与社交媒体 1080×1620。
- 画风（2026-10-31 更新）：海报概念图沿用 Maela 定稿的绘本风（Niji 6），不再要求像素风；游戏内画风同为手绘（2026-11-02 定）。背景已定：`ART_ref/POSTER_BG_v2.png`。
- 存放：`TechArtAsset/Poster/POSTER_v1.png`，源文件 `POSTER_wip.psd`。

### K2 开始菜单背景（16:9）

- 夜晚海岸，右侧悬崖上的灯塔熄灭，只有顶端一点灯笼光；海雾。
- 左侧 1/3 留暗，放标题和按钮（Play / Quit）。
- 游戏内版本 1920×1080，按 `TechnicalArt/HANDPAINTED_SPEC.md` 分层；与宣传版同一画风。
- 可选动效：海雾横向缓慢移动（前景层）、灯塔顶灯笼光呼吸闪烁。
- 存放：`TechArtAsset/Menu/MENU_BG.png`、`MENU_wip.psd`（图层：L0_Sky / L1_Sea / L2_Cliff_Lighthouse / L3_Fog / Title / Buttons）。

### K3 关键截图（作品集用，Demo 完成后）

- 切换瞬间：奶奶家断梯处，同一构图截“现在层”和“记忆层”两张并排（2026-11-07：Demo 不做码头）。

## 4. 菜单 UI 规范

| 状态 | 颜色 | 效果 |
|---|---|---|
| 普通 | 米白 #F2EBDD | 深色描边 |
| 选中 / 悬停 | 暖金 #E8B45A | 左侧显示小灯笼图标 |

按钮在 Unity 用 TextMeshPro 重建，不导出成图片。

## 5. 检查清单

- ☑ 标题拼写逐字检查（TITLE_v1）
- ☑ 所有字体有授权文件，存 `TechnicalArt/fonts/`
- ☐ 海报、菜单配色使用 ART_HANDOFF §4.1 调色板
- ☐ 去掉 AI 出图的签名 / 水印
- ☐ 海报在手机上缩小看，灯光与人物仍清楚
