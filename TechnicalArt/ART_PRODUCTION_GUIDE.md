# 《The Lantern Keeper》美术资产制作指南：角色 · 场景 · 海报（v1）

> 给人看的操作手册。与 `TechnicalArt/守灯人_美术资产制作指南_v1.4.docx` 同源。流程参考 Animation_yichun《妖精丘陵》的实际做法（概念图 → 定稿参考 → 用定稿统一后续出图 → 合成海报）。
> 配套文件：`ART_PROMPTS.md`（全部 prompt）、`ART_HANDOFF.md`（角色外观约束、调色板）、`TechnicalArt/HANDPAINTED_SPEC.md`（手绘规格）、`ART_ref/ASSETS.md`（登记表）。

## 0. 总览：做什么、按什么顺序

海报需要“主角 + 场景 + 标题”三样东西，所以顺序是：

| 步骤 | 产出 | 用在哪里 | 预计时间 |
|---|---|---|---|
| 1 | 主角 Maela 定稿概念图 | 所有后续出图的参考；海报主体 | 1–2 天 |
| 2 | 灯笼与贝壳道具 | 角色手里的灯笼要一致 | 半天 |
| 3 | 码头场景：现在层 + 记忆层 | 游戏背景；海报的“灯光照见过去” | 1–2 天 |
| 4 | 奶奶、老佩尔 | 游戏 NPC | 1 天 |
| 5 | 标题字 | 海报、菜单 | 半天 |
| 6 | 海报合成 | 宣传、作品集封面 | 1–2 天 |
| 7 | 开始菜单背景 | 游戏菜单 | 1 天 |
| 8 | 游戏内素材（Photoshop 清理、拆层、骨骼） | Unity | 与程序并行 |

原则：**先把主角定下来**。主角定稿后，所有出图都用它作参考，风格和颜色才会统一。

## 1. 准备

1. 确认出图工具：Midjourney（网页版）或 OpenAI 图像。下文以 Midjourney 为例，OpenAI 用法见第 9 节。
2. Midjourney 设置里确认模型版本：角色用 **Niji 6**，场景和道具用 **V7**。版本不对时 `--cw` 等参数会报错。
3. 打开 `ART_HANDOFF.md` 第 4 节，对照角色“必须保留 / 不要画”。
4. 每次选定一张图，马上存进 `ART_ref/` 并在 `ASSETS.md` 登记一行（文件名、prompt 编号、状态）。

## 2. 第一步：主角 Maela

### 2.1 出第一轮

- 使用 `ART_PROMPTS.md` 的 **C01**（Niji 6，`--ar 3:2 --s 150`）。
- 第一轮没有参考图，Character Reference 留空。
- 跑 2–3 次（每次 4 张），挑出最接近的一张。

### 2.2 挑选标准（逐项打勾）

- ☐ 明黄雨衣，是画面里最亮的颜色
- ☐ 齐肩黑发、红色短靴
- ☐ 左手提铜灯笼，火焰暖白
- ☐ 看起来像 11 岁，不成年化
- ☐ 剪影清楚：缩小到很小时也能认出（游戏里 Maela 只有约 160 px 高）

### 2.3 修改

- 局部不对（例如灯笼形状）：用编辑器 **Smart Select → Erase selection → 只写这一处的短 prompt → Submit edit**，一次只改一处。
- 想换造型方向：Vary (Strong)；只想微调：Vary (Subtle)。

### 2.4 定稿与转身图

1. 定稿图存为 `ART_ref/Maela_v1.png`，在 ASSETS.md 标“当前定稿”。
2. 裁出正面，补白底成方形，放大到 1024 → `ART_ref/MAELA_REF_v1.png`。之后所有图都用它作 Character Reference。
3. 转身图（2026-11-06 实际做法）：**一张只出一个人**。侧面用 C01-T 侧面版（`--ar 2:3 --cw 40`，`--no front view, three-quarter view, looking at viewer`）→ Vary (Subtle) 挑脸最侧的一张；背面从 C01-T v2（`--ar 2:1 --cw 90`）出的“正 + 背”图里裁右半。两张抠图等高拼成 `Maela_v1_turnaround.png`，侧面另存 `MAELA_SIDE_REF_v1.png`（1024² 白底）作下一步参考。**朝右侧面**是游戏版角色的基准；海报要用**背面**。
4. 一次出“侧面 + 背面”会被 Character Reference 拉回正面（第一轮四张全是正 + 背）。

## 3. 第二步：灯笼与贝壳

- 灯笼：**P01**（V7）。挑一个与 Maela 定稿手里灯笼最像的版本 → `ART_ref/LANTERN_REF.png`。如果差别大，回到 Maela 定稿用编辑器把灯笼换成这一版，保证海报和游戏一致。
- 贝壳：**P02** → `ART_ref/SHELL_REF.png`。

## 4. 第三步：码头场景（现在层 + 记忆层）

1. 先出 **S01 码头 · 现在**（V7，`--ar 16:9`）。挑选标准：
   - ☐ 冷蓝灰色调、浓雾
   - ☐ 断掉的木板路清楚可见（这是谜题的位置）
   - ☐ 远处悬崖上有熄灭的灯塔
   - ☐ 左右有横向延伸感（横版游戏）
2. 定稿存 `ART_ref/HARBOR_PRESENT_v1.png`。
3. 再出 **S01-M 码头 · 记忆**：把 HARBOR_PRESENT_v1 放进 **Image Prompts**（不是 Character Reference），`--iw 1.5` 左右，保持构图一致，只变成暖金、完好、热闹。
4. 两张并排检查：构图（码头、船、灯塔的位置）基本对齐 → 存 `HARBOR_MEMORY_v1.png`。
5. 奶奶家（S02 / S02-M）同样方法，Demo 时间紧可以放到最后。

> 小技巧：两张图对齐得越好，游戏里切换时的“变化感”越强，作品集截图也越好看。

## 5. 第四步：NPC

- **C02 / C02-Y 奶奶**、**C03 老佩尔**（Niji 6）。为了让画风和 Maela 一致，把 MAELA_REF_v1 放进 **Style Reference**（不是 Character Reference），`--sw 100`。
- 存 `SOAZIG_v1.png`、`SOAZIG_YOUNG_v1.png`、`PER_v1.png`。

## 6. 第五步：标题字

1. 不要让 AI 直接写字（会拼错）。
2. 在 Photoshop / Figma 用候选字体（Pixelify Sans 或 Silkscreen）排出 THE LANTERN / KEEPER 两行，颜色 #E8B45A，描边 #1E2633，透明底，导出 PNG。
3. 可选：上传到 Midjourney 编辑器用 **Retexture**（**KT**）加铜质感。
4. 逐字检查拼写 → 存 `TechArtAsset/Menu/TITLE.png`，字体文件和授权放 `TechnicalArt/fonts/`。

## 7. 第六步：海报（K1，竖版 2:3）

### 7.1 方案

用 AI 出背景，再在 Photoshop 合成主角和标题（《妖精丘陵》海报的做法：背景 + 角色背影 + 标题分开做，可控性最好）。

### 7.2 步骤

1. **背景**：用 **K1** prompt（V7，`--ar 2:3`），把 HARBOR_PRESENT_v1 放进 Image Prompts（`--iw 0.5`）统一色调。要点：
   - ☐ 悬崖小路通向熄灭的灯塔
   - ☐ 画面中下部留出人物位置
   - ☐ 上方 1/4 是相对干净的夜空（放标题）
   - ☐ 海面下隐约有沉没的钟楼
   - 存 `ART_ref/POSTER_BG_v1.png`。
2. **主角**：用 Maela 转身图的**背面**，或用 C01 + MAELA_REF_v1 单独出一张“举起灯笼的背影”（`--cw 100`），去背景。
3. **合成**（Photoshop，新建 `TechArtAsset/Poster/POSTER_wip.psd`）：
   - 图层：`BG` → `Memory_glow`（灯笼光圈内贴一部分 HARBOR_MEMORY_v1，圆形柔边蒙版，叠加模式“滤色 / 叠加”）→ `Maela` → `Lantern_light`（暖白径向渐变）→ `Fog_front` → `Title` → `Info_text`（Demo · 2026 · PC）。
   - 关键效果：**光圈内暖、光圈外冷**，一眼看懂“灯光照见过去”。
4. **检查**：
   - ☐ 缩小到手机大小，人物、灯光、标题仍然清楚
   - ☐ 去掉 AI 签名 / 水印
   - ☐ 标题拼写正确
5. **导出**：`POSTER_v1.png`（A3 300 dpi：3508×4961）、`POSTER_v1_social.png`（1080×1620）。

## 8. 第七步：开始菜单背景（K2）

- **K2**（V7，`--ar 16:9`），Image Prompts 放 POSTER_BG_v1 统一色调。
- 左侧 1/3 留暗放按钮；右侧悬崖灯塔，顶端一点灯笼光。
- PSD 分层：L0_Sky / L1_Sea / L2_Cliff_Lighthouse / L3_Fog / Title / Buttons → `TechArtAsset/Menu/MENU_wip.psd`。
- 游戏内用的版本：1920×1080，按 HANDPAINTED_SPEC 清理并分层。

## 9. 用 OpenAI 图像代替 Midjourney

- 把 prompt 原文（去掉 `--` 参数）粘贴，比例写进文字（例如 “vertical 2:3 poster”）。
- 参考图：直接上传 MAELA_REF_v1，并写 “keep the same character design as the reference image”。
- 局部修改：用编辑功能圈选区域，再写一句修改说明。

## 10. 第八步：游戏内素材（手绘，2026-11-02 改）

概念图清理后进游戏。按 `HANDPAINTED_SPEC.md`：

1. **角色**：C01-G 出站姿侧面（Character Ref = `MAELA_SIDE_REF_v1`，服装颜色写全）→ 抠图 → 调色（头发、雨衣主色、火焰）→ **去边** → 按 HANDPAINTED_SPEC §3.1 拆部件（Maela 另有 Dress 层）→ 大图存 `Maela_src.psd`，缩到高 320 px 存 `TechArtAsset/Characters/Maela/Maela.psb`。Maela 这一步由 Claude 用代码 + 直接操作 Photoshop 完成（见 §13）。
2. Unity：PSD Importer 导入（**PPU 200**）→ 剪纸式骨骼（每个部件只跟一个关节；Codex 用 Transform 层级实现）→ 做 Idle / Run / JumpUp / Fall / Lantern。
3. **场景**：AI 出 16:9 概念 → 按房间长度外扩 → Photoshop 清理 → 拆成 L0–L4 → 记忆层标志物单独存 → 导出 PNG。
4. 现在 / 记忆层用同一套底图，对齐后在 Unity 里由 Global Light 2D 变冷暖。
5. 每做完一张，在 ASSETS.md 第二张表登记。

## 11. 每做完一样，记得

- ☐ 文件存到正确位置，命名照第 2–8 节
- ☐ `ART_ref/ASSETS.md` 加一行
- ☐ `ART_HANDOFF.md` 第 6 节把 ☐ 改为 ☑，第 10 节写一行，并更新第 9 节交接进度
- ☐ 如果改了角色外观或设定，登记 `DESIGN_CHANGES.md`

## 12. 实操经验（2026-10-31，Maela 与海报背景）

| 情况 | 结论 / 做法 |
|---|---|
| 选定 Maela | C01 第一轮挑最接近的一张 → **Vary (Subtle)** 比改 prompt 重跑更稳；改 prompt（C01-R2）反而引入新问题 |
| 黄雨衣 + 兜帽戴起 | 太像其他游戏的知名主角，坚持“兜帽放下” |
| 颜色、左右手 | Midjourney 不认 hex，也常画反左右手；定稿时不卡，Photoshop 清理阶段统一修 |
| 网页版 Vary (Region) | 已并入 **Editor**：点图 → Open Editor → Erase / Smart Select → 改 prompt → Submit edit |
| 场景里放角色 | **不要同时用 Style Ref + Character Ref 且权重高**：会变回白底正面设定图。场景只用 Style Ref（`--sw 30`），角色之后合成 |
| 让灯塔熄灭 | prompt 里出现 “lighthouse” 就会画亮灯，`--no light` 压不住。擦掉塔顶，用 “dark top of an old stone tower” 描述；不行就 PS 涂暗 |
| 给标题留空 | 编辑器里保持 2:3，Scale 缩到约 75%，原图拖到底部；prompt 写整个场景（不只写天空），否则两侧会补成天空 |
| 外扩时多出物体 | 外扩可能凭空多画一座亮灯塔，从 4 张里挑没有的 |
| 下载前 | 先 **Upscale (Subtle)**；未放大的只有 896×1344。A3 最终放大在 PS 做 |
| 海报画风 | 海报概念沿用 Maela 绘本风；游戏内画风另定（ART_HANDOFF §8） |

## 13. 实操经验（2026-11-05 ~ 07，Maela 游戏版）

| 情况 | 结论 / 做法 |
|---|---|
| 提灯的手 | 改为**右手**：朝右时灯笼在近镜头一侧，不被身体挡住；flipX 后仍在近侧 |
| 斜挎包 | Demo 不画（`--no bag, backpack, strap`）；完整版作过了新手村后的储物包（提议） |
| 出侧面 | 一张只出一个人；`--cw 40` 只借脸和衣服，不照搬参考图的正面姿势 |
| 游戏版颜色乱 | 挂了 Character Reference 也要把服装颜色写全，否则靴子变棕、内裙变红、灯不亮 |
| 游戏尺寸 | Maela 在游戏里只有约 160 px 高，很多细节只剩 1–2 px。**清理只管：剪影、主色、去边、关节不露缝**；头发前后层、被挡部分、褶皱不必精修 |
| 浅色毛边 | 浅色背景上抠出的角色，轮廓带一圈亮边，放到深色夜景上很显眼（角色越小越显眼）→ 必须去边 |
| 灯笼里的“白斑” | 其实是抠穿的透明孔，深色背景上变成灰洞 → 发光物体内部要整体填实 |
| 拆手臂 | 沿袖子上缘把整只袖子切下来，在肘部再分两段；袖子拿走后给身体层补底色 |
| 细线（提环） | 贴着别的部件的细线要按走向单独切，提环归灯笼，握在手里的一小段归手 |
| 工具 | Photoshop 可由 Claude 直接操作（导入图层、导出 .psb）；PhotoCraft 无法连接 |
