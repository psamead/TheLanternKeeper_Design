# ART_ref 图片资产清单（ASSETS）

> 给 Agent 读取，并追踪美术资产版本。位置：`SharedWorkFolder/ART_ref/`。最后更新：2026-11-13。

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
| `TechArtAsset/Scenes/Home/Props/_work/LadderPair_MJ_src_v1.png` | Home 道具源图 | 完整梯 + 断梯组合（2688×1792） | v1 | Midjourney Niji 6，job `591563a6-dd42-49c8-b459-5326e4fc8a07` | P02 梯子；`--sref eghoPUBkfKo --sw 15` | 形状、木纹与色彩参考 | 参考 |
| `TechArtAsset/Scenes/Home/Props/_work/Ladder_Whole_MJ_crop_src_v1.png` | Home 道具素材 | 白底短梯，1440×1792 | v1 | 用户提供，原名 `LadderPair_s_m.png` | 从 MJ 梯子素材整理 | 长梯拼接素材，非透明游戏导出 | 源素材 |
| `TechArtAsset/Scenes/Home/Props/_work/Ladder_Whole_v3.psd` | Home 道具可编辑源 | 分层长梯，1440×4200 | v3 | 用户 Photoshop 手工拼接与抠图；原名 `LadderPair_m.psd` | 保留用户画面与图层 | `Ladder_Whole_v3.png` 的分层源 | 源文件（旧版，当前见 v4） |
| `TechArtAsset/Scenes/Home/Props/_work/Ladder_Whole_v4.psd` | Home 道具可编辑源 | 分层长梯，1440×4200 | v4 | 用户 Photoshop 修订 v3 | 增强主体不透明度、调整拼接处 | `Ladder_Whole_v4.png` 的分层源 | 当前源文件 |
| `TechArtAsset/Scenes/Home/Props/_work/Lantern_MJ_src_v1.png` | Home 道具源图 | 铜制手提灯笼（2048×2048） | v1 | Midjourney Niji 6，job `2a9fe918-de40-4649-993d-9780b09c1ac0` | P01 灯笼；`--sref eghoPUBkfKo --sw 15` | 造型与材质参考 | 参考 |
| `TechArtAsset/Scenes/Home/Attic/_candidates/Attic_PerspectiveRef_v1.png` | Home 场景候选 | 阁楼透视构图，16:9 | v1 | Midjourney Niji 6，job `de6dc6e8-64ba-48a2-9835-8cdf91dc0d12` | 原 S02 阁楼图，`--sref eghoPUBkfKo --sw 60` | 仅作画风、灯光与物件参考；透视构图不作游戏背景 | 参考 |
| `TechArtAsset/Scenes/Home/Attic/_candidates/Attic_PerspectiveRef_v2.png` | Home 场景候选 | 阁楼轻透视背景，2912×1632（16:9） | v2 | Midjourney Niji 6，job `83223836-af12-427b-ae2d-cdd704152b9a` index 0 → Upscale (Subtle)，job `bf19f584-cd7e-43d5-b936-2b345e8a5097` | S02-H v4，`--sref eghoPUBkfKo --sw 60` | 用户选定的放大原图；保留修改前版本 | 已被 v3 取代 |
| `TechArtAsset/Scenes/Home/Attic/_candidates/Attic_PerspectiveRef_v3.png` | Home 场景候选 | 阁楼轻透视背景，2912×1632（16:9） | v3 | 用户在 v2 上用 Photoshop 修订；原临时名 `Attic_PerspectiveRef_v2_m.png` | 手工去除画中梯子、处理窗外灯塔灯部；分层源见 `Attic/_work/Attic_PerspectiveRef_v3.psd` | 当前选用背景候选；待 Unity 校对梯口、地面、镜头和互动位置 | 当前候选，未接入 Unity |
| `TechArtAsset/Scenes/Home/Props/_work/Ladder_Whole_cutout_src_v1.png` | 道具抠图源 | 完整木梯，透明底（1024×1536） | v1 | OpenAI 图像生成，用户选定 | 依照 LadderPair_MJ_src_v1 的木梯画风出单体 | 完整梯游戏图的透明底来源 | 参考 |
| `TechArtAsset/Scenes/Home/Props/_work/Ladder_Broken_cutout_src_v1.png` | 道具抠图源 | 断梯下半段，透明底（1024×1536） | v1 | OpenAI 图像生成 | 依照完整梯造型制作断梯，保留三档踏棍与断裂栏杆 | 现在层梯子残段 | 参考 |
| `TechArtAsset/Scenes/Home/Props/_work/Lantern_cutout_src_v1.png` | 道具抠图源 | 铜灯笼，透明底（1254×1254） | v1 | OpenAI 图像生成 | 依照 Lantern_MJ_src_v1 生成单体透明图 | Home 灯笼游戏图来源 | 参考 |
| `TechArtAsset/Scenes/Home/Props/_work/Ladder_Whole_cutout_src_v2.png` | 道具抠图源 | 完整木梯，透明底（1024×1536） | v2 | OpenAI ImageGen | 依据 MJ 梯子源图左侧完整梯单独生成；严格正视、无光晕 | v2 游戏梯子来源 | 参考 |
| `TechArtAsset/Scenes/Home/Props/_work/Ladder_Broken_cutout_src_v2.png` | 道具抠图源 | 断梯下半段，透明底（1199×1312） | v2 | OpenAI ImageGen | 依据 v1 断梯单体重制；保留三档踏棍与断裂栏杆 | v2 游戏梯子来源 | 参考 |
| `TechArtAsset/Scenes/Home/Props/_work/Lantern_cutout_src_v2.png` | 道具抠图源 | 铜灯笼，透明底（1254×1254） | v2 | OpenAI ImageGen | 依据 Lantern_MJ_src_v1 单独生成；灯光仅在玻璃内 | v2 游戏灯笼来源 | 参考 |
| `TechArtAsset/Scenes/Home/Attic/_work/Home_Attic_Both_src_v1.png` | Home 场景图源 | 阁楼正视横版背景（1672×941） | v1 | OpenAI ImageGen | 由正视阁楼候选编辑；移除烘焙梯子与壁挂灯，留下空梯口 | 阁楼游戏背景来源 | 参考 |
| `TechArtAsset/Scenes/Home/Attic/Home_Attic_Both_v1.png` | Home 场景候选 | 阁楼正视横版背景（1672×941） | v1 | OpenAI ImageGen | 依据 S02-H 正视构图；冷蓝石墙、屋梁、箱子、四格方窗与熄灯灯塔 | 旧正视候选；用户反馈风格不符，保留历史 | 旧候选 |

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
| `Scenes/Home/Props/Ladder_Whole_v1.png` | Home 道具 | 透明底，1024×1536 | LadderPair_MJ_src_v1 + 用户选定的单体风格图 | 已被 v2 取代；保留旧版存档 |
| `Scenes/Home/Props/Ladder_Broken_v1.png` | Home 道具 | 透明底，1024×1536 | Ladder_Whole_v1 的木梯造型；下半段保留三档踏棍、断裂栏杆 | 已被 v2 取代；保留旧版存档 |
| `Scenes/Home/Props/Lantern_v1.png` | Home 道具 | 透明底，1254×1254 | Lantern_MJ_src_v1 + 用户选定的单体风格图 | 已被 v2 取代；保留旧版存档 |
| `Scenes/Home/Props/Ladder_Whole_v2.png` | Home 道具 | 透明底，1024×1536 | LadderPair_MJ_src_v1；完整梯单体化 | 旧候选；当前完整梯见 v4 |
| `Scenes/Home/Props/Ladder_Whole_v3.png` | Home 道具 | 透明底，1440×4200 | 用户 PSD `Props/_work/Ladder_Whole_v3.psd`，Photoshop 原尺寸导出 | 已被 v4 取代，保留历史 |
| `Scenes/Home/Props/Ladder_Whole_v4.png` | Home 道具 | 透明背景，1440×4200 | 用户修订的 `Props/_work/Ladder_Whole_v4.psd`；增强主体不透明度并调整接缝，Photoshop 原尺寸导出 | 当前完整梯候选，用于钟声后的独立梯与剧情传送；待 Unity 校对；不制作配对断梯 |
| `Scenes/Home/Props/Ladder_Broken_v2.png` | Home 道具 | 透明底，1199×1312 | LadderPair_MJ_src_v1 + Ladder_Broken_v1；三档踏棍、上端断裂 | 旧候选；本轮未定稿，须与完整梯配对 |
| `Scenes/Home/Props/Lantern_v2.png` | Home 道具 | 透明底，1254×1254 | Lantern_MJ_src_v1；火焰限制在玻璃内部 | 旧候选；保留存档 |
| `Scenes/Home/Attic/Home_Attic_Both_v1.png` | Home 场景背景 | 16:9，1672×941；可叠加角色与道具 | 蓝灰石墙、平直地板、左侧空梯口、右侧四格方窗与熄灯灯塔 | 旧正视候选；用户反馈风格不符，当前选用见 Attic_PerspectiveRef_v3 |

| `TechArtAsset/Scenes/Home/Props/_work/Lantern_MJ_v2_PS.psd` | Home 道具可编辑源 | Photoshop 分层文件，保留 MJ 原图隐藏层 | v2 | Adobe Photoshop 2023；源 `Lantern_MJ_src_v1.png` | 主体选区加底座边缘蒙版，去白底和地面投影 | `Lantern_v3.png` 的可编辑源文件 |
| `Scenes/Home/Props/Lantern_v3.png` | Home 道具 | 透明底，1032×1875 | Midjourney 原图 `Lantern_MJ_src_v1.png`；Photoshop 去白底与地面投影 | 已被 v4 取代；保留旧版 |
| `Scenes/Home/Props/Lantern_v4.png` | Home 道具 | 透明底，1032×1875 | `Lantern_v3.png`；用户手工清除剩余未抠净区域，原临时名 `Lantern_v3_m.png` 按版本规则重命名 | 当前手绘风格候选；待 Unity 校对挂点与比例 |

| `Scenes/Home/Present/Home_Present_v3.png` | Home 楼下背景 | 2520×1080，无背景梯子 | 用户修订；源 `Present/_work/Home_Present_v3.psd`（原名 Home_Present_v2.psd），PhotoCraft CLI 导出 | 当前候选，用于同底图滤镜及独立梯子叠加；未接入 Unity |

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
| 2026-11-09 | Soazig 概念定稿：`ART_ref/SOAZIG_REF_v1.png`（白底正面 1024²，MJ C02-v2 → Vary Subtle → 用户 PS 去竿子 → 脚本去网堆）；源 `SOAZIG_SRC_v1.psd`、`_src_soazig/SOAZIG_SRC_v1_MJ_upscale.png`；作 P4 等的 `--cref` |
| 2026-11-11 | 序章定稿 `TechArtAsset/Storyboard/Prologue/SB_P2.png`（远处雾团、远窗一盏灯）/ `SB_P3.png`（背影门口）/ `SB_P4.png`（奶奶摇椅，PS 压冷；`SB_P4.psd`）；源 `Prologue/_work/SB_P*_src*.png`，候选 `Prologue/_candidates/` |
| 2026-11-11 | Home 箱子 `TechArtAsset/Scenes/Home/Props/Crate_v1.png`（520×440，底边贴地；MJ 源 `Props/_work/Crate_src_MJ.png`，脚本 `make_crate.py`） |
| 2026-11-11 | 故事版 A / B 占位 `TechArtAsset/Storyboard/LanternOrigin_A/placeholder/SB_A1..4_placeholder.png`、`Ending_B/placeholder/SB_B1..5_placeholder.png`（2208×1242，代码生成） |
| 2026-11-11 | 故事版暂用图（MJ 第一轮）：`Storyboard/LanternOrigin_A/SB_A4.png`；`Storyboard/Ending_B/SB_B1..B5.png`（B4 待去橘光、B5 待重摆举灯杆、B1/A4 可能重跑）；源 `_work/SB_*_src_*.png` |
| 2026-11-12 | 故事版 A1–A3 暂用图 `LanternOrigin_A/SB_A1..A3.png`（A1 右下，灯型接近）；B4 去橘光、B5 重摆举灯杆（用户 PS，源 `Ending_B/_work/*_PSfix.*`） |
| 2026-11-12 | 故事版 A4 定稿（第三轮，`LanternOrigin_A/_work/SB_A4_src_r3.png`）、B1 定稿（第二轮斜构图方窗，`Ending_B/_work/SB_B1_src_r2_slanted.png`；正面版备用）。P / A / B 全部定稿 |
| 2026-11-12 | Home 道具首轮：完整梯、断梯、灯笼透明图入 `TechArtAsset/Scenes/Home/Props/`；MJ 原图及 ImageGen 输出入 `_work/`。原阁楼透视图移入 `Attic/_candidates/`，只作画风和道具参考；阁楼重跑 job `59ae29d2…`（画风回归但仍有透视）与 `aa2c55e4…`（同风格，仍有透视；暂不采纳） |
| 2026-11-12 | Home 美术第二版：梯子与灯笼 v2 作为透明单体图入 `Scenes/Home/Props/`，v1 保留存档；阁楼正视背景 `Attic/Home_Attic_Both_v1.png` 入库，保留空梯口以便叠加可切换梯子，不把灯笼烘焙进背景。原透视候选仍仅作风格参考；所有新图待 Unity 中检查比例 / 锚点与地形对齐 |
| 2026-11-12 | 灯笼 v3：用户选用 MJ 铜灯原图；Photoshop 2023 去白底与落地投影，输出透明 PNG 1032×1875 与分层 PSD；v1 / v2 / MJ 源图均保留 |
| 2026-11-13 | Home 阁楼透视候选 v2：用户选定 Midjourney job `83223836-af12-427b-ae2d-cdd704152b9a` index 0，经 Upscale (Subtle) job `bf19f584-cd7e-43d5-b936-2b345e8a5097`，保存为 `Attic/_candidates/Attic_PerspectiveRef_v2.png`（2912×1632）；保留候选待 Unity 校对，未替换现有正视背景 |
| 2026-11-13 | Home 灯笼 v4：用户在 v3 上手工清除剩余未抠净区域；保留 `Lantern_v3.png`，将 `Lantern_v3_m.png` 按 `对象_vN.png` 命名规则改为 `Scenes/Home/Props/Lantern_v4.png`（透明底，1032×1875） |
| 2026-11-13 | Home 阁楼 v3：用户在透视候选 v2 上手工去除画中梯子并处理窗外灯塔灯部；`Attic_PerspectiveRef_v2_m.png` 改名为 `_candidates/Attic_PerspectiveRef_v3.png`，配套 PSD 改名移至 `Attic/_work/Attic_PerspectiveRef_v3.psd`。v2 保留，v3 待 Unity 验收。 |
| 2026-11-13 | 完整长梯 v3：用户新增 `LadderPair_m.psd` 与 `LadderPair_s_m.png`，分别整理为 `Props/_work/Ladder_Whole_v3.psd` 与 `Ladder_Whole_MJ_crop_src_v1.png`；Photoshop 从 PSD 原尺寸导出 `Props/Ladder_Whole_v3.png`（1440×4200，透明底），用于记忆层。旧版保留，配对断梯待制作，尚未接入 Unity。 |
| 2026-11-13 | 完整梯 v4：用户调整主体透明度和拼接处；PSD 已按命名规则放在 `Props/_work/Ladder_Whole_v4.psd`，原尺寸导出 `Props/Ladder_Whole_v4.png`。v3 保留，v4 尚未接入 Unity。 |
| 2026-11-13 | 楼下背景去除梯子，PSD 归档为 `Present/_work/Home_Present_v3.psd`，导出 `Present/Home_Present_v3.png`（2520×1080）。原 v1、v2 断梯背景保留；用户说明使用同底图滤镜与独立梯子切换，新图尚未接入 Unity。 |

> 2026-11-13：当前采用表以 Home 知识库为准。灯笼 v4、楼下无梯背景 v3、阁楼透视 v3、完整梯 v4 为当前候选；源 PSD/PSB 保留本地，尚未进行新图 Unity 接入。当前 Unity 修改方向详见 `CommandForAgentToInitialRun/2026-11-13_Unity_Home_Review_Art_Transition_Audio.md`。
