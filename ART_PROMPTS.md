<!-- 出图 prompt 集。每生成 / 采用一张图，更新 ART_ref/ASSETS.md。准则来自《妖精丘陵》AGENT_PROCESS_GUIDELINES §5.3–5.4。 -->

# 《The Lantern Keeper》出图 Prompt 集（v1）

## 0. 准则

- 英文书写；一条只描述一个对象；同类图用同一个风格后缀。
- 不写具体游戏、作品、艺术家名称，用风格描述代替。
- 角色图：Midjourney 用 Niji 6 + Character Reference（选定第一张后作为后续参考，--cw 70–100）；OpenAI 图像则上传选定图作参考。
- 场景、道具：Midjourney V7。
- 出来的图是**概念图**，游戏内素材按 `TechnicalArt/HANDPAINTED_SPEC.md` 在 Photoshop 清理、拆层。
- 文字（标题）不要让 AI 生成：先用字体排好，再让 AI 只做质感（Retexture）。

### 风格后缀

- **STYLE_CHAR**（2026-11-02 改，去掉 Q 版）：`, natural child proportions about 5 heads tall, normal-sized eyes, restrained expression, clean silhouette, limited palette, soft painterly shading, plain light background, character concept sheet` 可加 `--no chibi, big eyes, blush, pastel`
- **STYLE_GAME**（2026-11-02 定，取代 STYLE_PIXEL）：`, 2D side-scrolling game art, hand-painted folklore fantasy, quiet melancholic but hopeful mood, clean ink outlines, flat cel shading with 2-3 tones, single strong warm light source in a cold night, readable silhouette` 加 `--no horror, gore, creepy` 角色另加 `--no chibi, big eyes, blush, pastel`
- **STYLE_SCENE**：`, side-scrolling 2D game background, painterly storybook style, layered parallax depth, Breton fishing village, moody atmosphere, limited palette`
- **COLD**：`, cold foggy blue-grey palette (#4A5A6E, #1E2633), dim, quiet`
- **WARM**：`, warm golden memory light (#E8B45A, #7A4A2A), nostalgic, glowing`

## 1. 角色

| # | 对象 | Prompt | 参数 |
|---|---|---|---|
| C01 | Maela 正面 | an 11-year-old girl, shoulder-length black hair, bright yellow raincoat with hood down, red short boots, dark stockings, holding an old brass hand lantern with a warm glowing flame in her left hand, quiet determined expression, front view and three-quarter view facing right STYLE_CHAR | Niji 6, --ar 3:2, --s 150 |
| C01-R2 | Maela 修正版（实际用过） | an 11-year-old girl, shoulder-length wavy black hair fully visible, bright lemon-yellow raincoat with the hood down resting on her back, red short rain boots, dark stockings, holding an old brass hurricane lantern with a warm glowing flame in her left hand, quiet determined expression, front view and three-quarter view facing right, cute storybook proportions, 3 heads tall, clean silhouette, limited palette, soft painterly shading, plain pale grey background, character concept sheet | Niji 6, --ar 3:2, --s 150, --no backpack, bag, hood on head。结果：灯笼常被画成单独道具、出现假文字“11”，**定稿反而来自 C01 + Vary (Subtle)** |
| C01-T | Maela 转身图（待做） | the same girl, character turnaround, full body side view facing right and back view, standing calmly, holding an old brass hurricane lantern with a warm glowing flame, shoulder-length wavy black hair, bright yellow raincoat with the hood down, red short boots, dark stockings, cute storybook proportions, clean silhouette, soft painterly shading, plain white background, character concept sheet | Niji 6, --ar 2:1, --s 150, Character Ref = MAELA_REF_v1, --cw 90, --no text, backpack |
| C01-G | Maela 游戏版侧面 | same girl as reference, full body side view facing right, standing, holding brass lantern, arms and legs clearly separated for rigging STYLE_GAME, plain white background | Niji 6，Character Ref = MAELA_REF_v1，--cw 90（取代原 C01-P 像素参考） |
| C02 | Soazig 现在 | an old Breton grandmother, grey hair in a bun, dark green wool shawl, long dark skirt, sitting in a wooden rocking chair mending a fishing net, gentle but distant expression STYLE_CHAR COLD | Niji 6, --ar 3:2 |
| C02-Y | Soazig 年轻 | a young Breton woman with black hair and a white lace coiffe headdress, dark green shawl, standing by a window looking at a distant lighthouse, smiling STYLE_CHAR WARM | Niji 6 |
| C03 | Old Per | an old hunched Breton fisherman, faded sailor cap, blue fisherman's smock, grey beard, holding a knotted rope, tired eyes STYLE_CHAR COLD | Niji 6 |
| C04 | Flick | a small white moth with faint golden wing edges, softly glowing, simple shape, game sprite concept, dark background | V7, --ar 1:1 |

## 2. 道具

| # | 对象 | Prompt |
|---|---|---|
| P01 | 灯笼 | an old brass hand lantern with glass panes and a top ring handle, a small triple-spiral engraving on the base, warm white flame inside, game prop concept, plain background, side view |
| P02 | 记忆贝壳 | a scallop shell glowing warm gold from inside, small sparkles, washed up on dark wet sand, game collectible concept |

## 3. 场景

| # | 对象 | Prompt | 参数 |
|---|---|---|---|
| S01 | 码头 · 现在 | a small Breton fishing harbor at dusk, broken wooden boardwalk with missing planks, a blue fishing boat stranded on the mud, thick sea fog, stone cottages in the background, a dark unlit lighthouse on a distant cliff STYLE_SCENE COLD | V7, --ar 16:9 |
| S01-M | 码头 · 记忆 | the same Breton fishing harbor twenty years ago, intact wooden boardwalk, festival bunting flags, neatly moored blue fishing boats, silhouettes of busy villagers, the lighthouse shining STYLE_SCENE WARM | V7, --ar 16:9，用 S01 定稿作 Image Prompt |
| S02 | 奶奶家 · 现在 | interior of an old Breton stone cottage at night, furniture covered with white sheets, a broken wooden ladder leading to an attic hatch, a rocking chair by the window, dark lighthouse visible through the window STYLE_SCENE COLD | V7, --ar 16:9 |
| S02-M | 奶奶家 · 记忆 | the same cottage interior in warm afternoon sunlight, intact ladder, fishing nets and family photos on the walls STYLE_SCENE WARM | V7 |
| S03 | 远景 | a calm sea horizon at night, faint silhouette of a drowned medieval bell tower under the water surface, distant cliffs, layered parallax background STYLE_SCENE COLD | V7, --ar 32:9 |

## 4. 宣传（详见 ART_DIRECTION.md）

| # | 对象 | Prompt | 参数 |
|---|---|---|---|
| K1 | Demo 海报 | a small girl in a bright yellow raincoat seen from behind, holding up a glowing brass lantern on a foggy cliff path, a dark lighthouse ahead, the lantern light reveals a warm golden ghostly image of the past village around her while the rest stays cold blue, under the sea surface the faint silhouette of a drowned bell tower, empty space at the top for a title, detailed pixel art illustration, cinematic | V7, --ar 2:3（原方案；2026-10-31 起海报改用 K1-BG 绘本风） |
| K2 | 菜单背景 | a dark Breton coastline at night, an unlit lighthouse on a cliff to the right, sea fog rolling over the water, one tiny warm light glowing at the top of the lighthouse, calm composition with empty dark space on the left for menu buttons, detailed pixel art illustration | V7, --ar 16:9（原方案；做时把 detailed pixel art illustration 换成 soft painterly storybook illustration，用 Niji 6） |
| K1-BG | 海报背景（实际采用） | wide cinematic night landscape, vertical poster composition, a tiny distant figure of a little girl in a yellow raincoat seen from behind, small in the lower third of the frame, walking up a narrow foggy cliff path and raising a glowing lantern, a tall dark unlit lighthouse on the cliff ahead, the lantern casts a small circle of warm golden light revealing a ghostly image of an old fishing village, everything outside the light is cold foggy blue-grey, dark sea below with the faint silhouette of a drowned bell tower under the water, large calm night sky with empty space in the top quarter, soft painterly storybook illustration | Niji 6, --ar 2:3, --s 150, Style Ref = MAELA_REF_v1 --sw 30（**不放** Character Ref），--no white background, character sheet, front view → 定稿 POSTER_BG_v1 |
| K1-E1 | 编辑：熄灭灯塔 | （编辑器擦掉塔顶及上半段塔身）the dark top of an old stone tower with empty black glass windows, abandoned, cold foggy blue-grey night sky, soft painterly storybook illustration | --no light, glow, lamp, yellow。**不要写 lighthouse**，否则一定画亮灯 |
| K1-E2 | 编辑：外扩顶部夜空 | a dark unlit lighthouse on a rocky cliff above a foggy sea at night, steep dark cliffs on both sides, wide calm dark foggy night sky above with plenty of empty space, cold blue-grey, soft painterly storybook illustration | 编辑器选 2:3，Scale 缩到约 75%，原图拖到底部居中；--no light, moon, stars, text |
| KT | 标题质感 | （上传用字体排好的标题图）weathered brass lettering with a faint warm glow | Retexture（原写 pixel art，已去掉） |

## 5. 变更记录

| 日期 | 变更 |
|---|---|
| 2026-10-31 | 新增 C01-R2、C01-T、K1-BG、K1-E1、K1-E2（实际用过 / 待用的 prompt 与参数） |
| 2026-11-02 | 游戏画风改手绘：STYLE_PIXEL → STYLE_GAME；C01-P → C01-G；STYLE_SCENE 加 painterly；K2、KT 去掉像素描述 |
| 2026-11-02 | 按《妖精丘陵》拆解结果定 STYLE_GAME；STYLE_CHAR 去掉 Q 版（3 heads tall → 约 5 头身） |
