# ART_ref 图片资产清单（ASSETS）

> 给 Agent 读取，并追踪美术资产版本。位置：`SharedWorkFolder/ART_ref/`。最后更新：2026-10-31。

## 约定

- 命名：`对象_REF.png` = 用作出图参考的裁切图；`对象_vN.png` = 生成结果。新版本不覆盖旧版本。
- 状态：存档、参考、定稿候选、当前定稿、已被 vN 取代。
- 每次新增或替换图片，更新本表和变更记录；做好的游戏资产登记在下方第二张表。

## 参考图 / 生成图

| 文件 | 类别 | 对象 | 版本 | 来源 | Prompt 编号 / 方式 | 用途 | 状态 |
|---|---|---|---|---|---|---|---|
| `Maela_v1.png` | 角色 | Maela 正面 ×2 + 背面 | v1 | Midjourney Niji 6（原名 `psamead_..._14aa2d9e-…png`） | C01 第一轮 ④ → Vary (Subtle) 右上（A2） | 主角概念定稿；兜帽放下、短靴、左手提灯 | 当前定稿 |
| `Maela_v1_alt.png` | 角色 | Maela 正面 ×2 + 背面 | v1 | Midjourney Niji 6（原名 `psamead_..._5a0cef49-…png`） | 同上，左上（A1） | 备选：靴子较高 | 定稿候选 |
| `Maela_sheet_B1_REF.png` | 角色 | Maela 表情头像 + 灯笼 + 正背面 | — | Midjourney Niji 6（原名 `0_0.png`） | C01 修正版（hood down / pale grey bg / `--no backpack, bag, hood on head`）左上（B1） | 以后做对话头像时参考表情；有 AI 假文字，不作定稿 | 参考 |
| `MAELA_REF_v1.png` | 角色 | Maela 正面单人，白底 1024×1024 | v1 | 由 `Maela_v1.png` 左侧正面裁切、去背景补白 | — | 后续出图的 Character Reference（`--cref`） | 参考（当前） |
| `MAELA_SRC_side_v1.png` | 角色 | Maela 侧面朝右走路，右手提灯（1792×2688） | v1 | Midjourney Niji 6 | C01-T 侧面单出版（--cw 40, --ar 2:3）→ Vary (Subtle) ④ → Upscale (Subtle) | 转身图侧面原图 | 参考 |
| `MAELA_SRC_back_v1.png` | 角色 | Maela 正面 + 背面（3072×1536；只用右半背面） | v1 | Midjourney Niji 6 | C01-T v2（--cw 90, --ar 2:1）第一轮左上 → Upscale (Subtle) | 转身图背面原图；后脑顶被原图裁平 | 参考 |
| `Maela_v1_turnaround.png` | 角色 | 侧面 + 背面，白底 4000×2000，两者等高 | v1 | 程序抠图拼合（分层 PNG 在 `TechArtAsset/Characters/Maela/_work/`） | — | 游戏版、拆部件的依据 | 当前定稿 |
| `MAELA_SIDE_REF_v1.png` | 角色 | 侧面单人，白底 1024² | v1 | 由 MAELA_SRC_side_v1 抠出 | — | C01-G 的 Character Reference | 参考（当前） |
| `MAELA_SRC_game_side_v1.png` | 角色 | Maela 游戏版侧面原图（1792×2688） | v1 | Midjourney Niji 6 | C01-G v3（cref = MAELA_SIDE_REF_v1, --cw 90）② → Upscale (Subtle) | 游戏版来源 | 参考 |
| `MAELA_GAME_SIDE_v1.png` | 角色 | 游戏版侧面，透明底 1157×2490 | v1 | 由上图抠出；2× / 1× 缩图与拆部件计划 `Maela_parts_plan_v1.png` 在 `TechArtAsset/Characters/Maela/_work/` | — | PS 清理、拆层为 Maela.psb 的底稿 | 当前定稿 |
| `deprecated/art_2026-11-02/POSTER_BG_v1.png` | 宣传 | 海报背景（竖版 2:3，绘本风），Upscale Subtle | v1 | Midjourney Niji 6（原名 `psamead_a_dark_unlit_lighthouse_on_a_rocky_cliff_above_a_foggy__c1ef3925-711e-4b0a-8785-f95d50ebcaa1.png`） | 远景小人物 prompt + Style ref MAELA_REF_v1 `--sw 30` → 编辑器擦塔顶改为熄灭 → 2:3 缩放外扩补顶部夜空 | 海报 K1 背景；上方约 1/3 留给标题 | 已被 v2 取代 |
| `BRETON_LACE_REF_01.png` | 参考 | 布列塔尼（比古登）白色镂空蕾丝：叶瓣 + 圆孔 | — | 用户提供 | — | 标题框、UI 边框纹样 | 参考 |
| `BRETON_HERMINE_REF_01.png` | 参考 | 白鼬尾纹（Hermine）重复图案 | — | 用户提供 | — | 标题主徽、UI 图标 | 参考 |
| `FAIRYHILLS_REF_01.png` – `_05.png` | 参考 | 《妖精丘陵》海报、两个角色、两条背景 | — | 用户提供 | — | 风格拆解（借墨线、平涂、强光源、分层；回避 Q 版与甜美粉彩），见 HANDPAINTED_SPEC §0 | 参考 |
| `POSTER_BG_v2.png` | 宣传 | 海报背景 v2：女孩兜帽放下露黑发、红色短靴（1792×2688） | v2 | POSTER_BG_v1 局部（x640 y1300，1024²）→ Google AI Studio Nano Banana 2.1 编辑（附 MAELA_REF_v1）→ 柔边蒙版只贴回头部与靴子 | 见 TechArtAsset/Poster/_work/ | 海报 K1 背景 | 当前定稿（取代 v1） |
| `POSTER_TITLE_REF_v1.png` | 宣传 | 海报背景 + 标题 TITLE_v1（1792×2688） | v1 | 程序合成 | — | 作海报 / 菜单出图的 Style 或 Image 参考；合成前预览 | 参考 |
| `deprecated/art_2026-11-02/POSTER_BG_v1_small.png` | 宣传 | 同上，放大前 896×1344 | v1 | Midjourney Niji 6（原名 `0_3.png`） | — | 存档 | 已被 POSTER_BG_v1 取代 |

## 游戏资产（TechArtAsset/）

| 文件 | 类别 | 规格 | 依据参考图 | 状态 |
|---|---|---|---|---|
| `Characters/Maela/Maela.psb`（工作文件 `Maela_src.psd` 不进 Git） | 角色 | 149×320（2×），19 个部件图层，组 `Maela` | MAELA_GAME_SIDE_v1 → Maela_CLEAN_v1（代码调色）→ 代码切层（`_work/parts/`） | 当前定稿（11-07：v1 + 只改颜色去边、灯笼补孔；Unity `6ec559b`）；左臂空、被挡部分未补、远眼未修 |
| `Poster/POSTER_v2.png` + `POSTER_v2_social.png` | 海报 | 竖版 2:3 | v1 + 标题框 TITLE_FRAME_v1（蕾丝花边 + 白鼬尾纹圆章 + 切角铭牌，整体 90%） | 当前定稿 |
| `Menu/MENU_BG_v1.png`（+ `MENU_L0_BG_1920.png`、`MENU_L1_left_dark.png`） | 菜单 | 16:9，原图 2752×1536 | MJ niji 6（Style ref = POSTER_v2）构图 → AI Studio Nano Banana 2.1 改夜景、熄灯塔 | 当前定稿 |
| `ART_ref/MENU_SRC_fantasy.png` / `MENU_SRC_realistic.png` | 菜单原图 | 16:9 | MJ 原图（MENU_BG_v1 / _alt 的来源） | 参考 |
| `UI/ICON_lantern_128.png` / `_64.png` | UI | 透明底 | 程序绘制，暖金灯笼 | 当前定稿 |
| `Menu/MENU_BG_alt.png` | 菜单 | 16:9 | MJ 写实构图 → AI Studio 统一画风（偏紧张，备选） | 备选 |
| `Menu/MENU_v1_mock.png` | 菜单 | 1920×1080 静态稿 | BG + 左侧压暗 + TITLE_FRAMED_v1 + Play/Settings/Quit（Cinzel 54，选中暖金 + 下划线 + 灯笼图标） | 当前定稿 |
| `Menu/TITLE_FRAMED_v1.png`（标题+框）/ `TITLE_FRAME_v1.png`（只有框） | 标题 | 透明底 | 程序绘制 SVG，参考 BRETON_LACE / HERMINE | 当前定稿 |
| `deprecated/art_2026-11-02/POSTER_v1.png`（3508 前的源尺寸 1792×2688）+ `POSTER_v1_social.png`（1080×1620） | 海报 | 竖版 2:3 | POSTER_BG_v2 + 记忆层 MEMORY_aligned（AI Studio 暖金版，SIFT 对齐）圆形柔边光圈 88% + 保留女孩 + 灯笼暖光 + TITLE_v1 + DEMO · 2026 · PC | 已被 v2 取代 |
| `Menu/TITLE_v1.png`（+ _nosub / _noglow / _glow） | 标题 | 透明底，约 2848×1324 | 字体 Cinzel Decorative + IM Fell English SC，程序加油墨毛边 | 当前定稿 |

## 变更记录

| 日期 | 变更 |
|---|---|
| 2026-10-30 | 建立本表 |
| 2026-10-31 | 登记 Maela 概念图 v1（定稿 A2、备选 A1、表情参考 B1）与 `MAELA_REF_v1.png`；斜挎小包是否保留待定 |
| 2026-10-31 | 登记海报背景 `POSTER_BG_v1.png`（绘本风；游戏内画风另定） |
| 2026-11-02 | 加入《妖精丘陵》风格参考图 5 张 |
| 2026-11-02 | 标题 TITLE_v1 登记 |
| 2026-11-02 | 海报背景 v2（MJ 编辑器上传失败，改用 AI Studio Nano Banana 2.1 局部编辑） |
| 2026-11-02 | 海报 v1 合成完成；分层素材在 TechArtAsset/Poster/_work/（MEMORY_aligned、L_memory_mask、GIRL_mask、L_lantern_light、POSTER_noTitle） |
| 2026-11-02 | 已被取代的 POSTER_BG_v1 / _small 与 _work 中的预览图移入 `deprecated/art_2026-11-02/`（预览在 previews/），作追踪 |
| 2026-11-02 | 加入布列塔尼蕾丝、白鼬尾纹参考；决定不用三螺旋纹作主视觉（与《妖精丘陵》撞） |
| 2026-11-02 | 海报 v2：加布列塔尼标题框；v1 移入 deprecated |
| 2026-11-03 | 开始菜单 v1 静态稿与分层 |
| 2026-11-06 | Maela 游戏版侧面 v1 + 拆部件计划 |
| 2026-11-06 | Maela 转身图 v1：侧面 / 背面原图、拼合图、侧面参考图 |
| 2026-11-03 | 菜单原图入 ART_ref；海报 AI Studio 过程图移入 deprecated/art_2026-11-03/poster_process |
