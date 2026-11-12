> 2026-11-13 Home 更新：以 `TechnicalArt/HOME_ART_KNOWLEDGE_BASE.md` 及同目录 `守灯人_Home美术交接与经验_2026-11-13_v1.docx` 为最新补充。风格优先，接受场景透视；旧正视限制按历史记录阅读。

<!-- 出图 prompt 集。每生成 / 采用一张图，更新 ART_ref/ASSETS.md。准则来自《妖精丘陵》AGENT_PROCESS_GUIDELINES §5.3–5.4。 -->

# 《The Lantern Keeper》出图 Prompt 集（v1）

## 0. 准则

- 英文书写；一条只描述一个对象；同类图用同一个风格后缀。
- 不写具体游戏、作品、艺术家名称，用风格描述代替。
- 角色图：Midjourney 用 Niji 6 + Character Reference（选定第一张后作为后续参考，--cw 70–100）；OpenAI 图像则上传选定图作参考。
- Home 本轮采用 Midjourney Niji 6，以已选图实际参数为准；V7 为早期建议。
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
| C01-T | Maela 转身图 v2（2026-11-05，右手提灯、无包、5 头身） | the same girl, character turnaround sheet, two full-body views side by side: strict side profile facing right, and back view, standing calmly, holding an old brass hurricane lantern with a warm glowing flame in her right hand, the lantern hangs on the near side of her body and is fully visible, shoulder-length wavy black hair with bangs, bright yellow raincoat with the hood down resting on her back, red short boots, dark stockings, natural child proportions about 5 heads tall, normal-sized eyes, restrained expression, clean ink outlines, flat cel shading with 2-3 tones, readable silhouette, limited palette, plain white background, character concept sheet | `--niji 6 --ar 2:1 --s 150 --cref <MAELA_REF_v1> --cw 90 --no text, letters, numbers, bag, backpack, strap, front view, chibi, big eyes, blush, pastel`。STYLE_GAME 只取线条 / 上色部分（白底设定图不要“cold night”）。老 v1 写的 cute storybook proportions 已删（会出 Q 版）。总给正面 → `--cw` 降到 60–70 |
| C01-G | Maela 游戏版侧面 v3（2026-11-06） | same girl as reference, full body strict side profile facing right, standing still in a relaxed idle pose, holding a lit brass hurricane lantern with a warm glowing flame in her right hand, arm slightly away from the body, the lantern on the near side of her body, shoulder-length wavy black hair with bangs, bright yellow raincoat with the hood down resting on her back, the raincoat hangs straight and ends above the knees, dark brown dress underneath, dark stockings, red short rain boots, small gap between the legs, natural child proportions about 5 heads tall, normal-sized eyes, 2D side-scrolling game art, hand-painted folklore fantasy, clean ink outlines, flat cel shading with 2-3 tones, even neutral lighting, readable silhouette, plain white background | `--niji 6 --ar 2:3 --s 100 --cref MAELA_SIDE_REF_v1 --cw 90 --no text, bag, backpack, strap, brown boots, red dress, unlit lantern, flowing coat, chibi, big eyes, blush, pastel, horror, cast shadow`。v2 没写服装颜色 → 靴子变棕、内裙变红、灯不亮；**即使挂了 cref 也要把服装颜色写全**。朝左的图可在 PS 水平翻转 |
| S01-H | Home 楼下 现在（2026-11-07，替换代码占位图；地板顶线须在底部 15%） | Side-scrolling 2D game background, straight-on side view of the ground floor interior of an old Breton fisherman's stone cottage at night, present day, abandoned and quiet. Left to right: a wooden front door, an empty wooden rocking chair beside a cold stone fireplace, a small window showing a distant dark unlit lighthouse on a cliff over the foggy sea, furniture covered with white dust sheets, an old wooden sea chest, on the far right a broken wooden ladder leaning toward a square opening in the ceiling to the attic with several rungs missing. Wide flat wooden plank floor running straight across the bottom of the image, perfectly horizontal, nothing standing on its front edge. Low beamed ceiling. No people, no text STYLE_SCENE STYLE_GAME COLD | `--niji 6 --ar 21:9 --s 150 --no people, characters, text, horror, perspective floor, tilted floor`。出图后按代码占位图 `TechArtAsset/Scenes/Home/Home_Present_placeholder_v0.png` 对齐：2400×1080、地板顶线 y=920 |
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

## 4b. 故事版 P：序章（2026-11-07）

通用：Niji 6，`--ar 16:9 --s 150`；Style Reference 用 11-03 的灯塔小路图或 `Home_Present_MJ_v1_src.png`，`--sw 60`（只带画风不带颜色）。推镜头要留 15 % 余量：Upscale 后裁 / 缩到约 2208×1242。人物镜头写全服装颜色（LESSONS §8）。

| 编号 | 用途 | 提示词 | 参数 / 备注 |
|---|---|---|---|
| SB-P1 | 序章 1：熄灭的灯塔（空镜） | a wide view of a dark Breton coastline at night, an old stone lighthouse on a rocky cliff with its lamp dark and unlit, cold sea fog drifting over black water, a small fishing village with a few dim windows along the shore, large quiet night sky, soft painterly storybook illustration, cold foggy blue-grey palette (#4A5A6E, #1E2633), quiet melancholic mood | `--no people, text, lit lighthouse, light beam`。**熄灭灯塔一律用海报两步法（K1-E1）**：① 照常写 lighthouse 出图，挑塔形最好的（细高 + 灯室 + 尖顶，亮着也没关系）→ ② Editor 只擦灯室，用 K1-E1 提示词重画（不写 lighthouse）。一步出“灭灯塔”不可行：写 lighthouse 必亮，不写就变碉堡（11-07 实测）。**11-07 定稿 C 版**：MJ 编辑出塔身 + 天空上延 + 海报灯室缩小后立在圆塔顶（Python 拼 + 用户 PS 调整），`TechArtAsset/Storyboard/Prologue/SB_P1_C_layered.psd` → `SB_P1.png`。之后可做 Flow 动画（见下） |
| SB-P2 | 序章 2：海雾进镇 | a narrow street of an old Breton fishing village at night, thick pale sea fog rolling in from the harbour and curling around stone houses and against the windows, one window with a faint warm candle inside slowly swallowed by fog, soft painterly storybook illustration, cold foggy blue-grey palette, dreamlike and sad | `--no people, text, horror` |
| SB-P3 | 序章 3：梅拉到奶奶家（背影） | a small girl seen from behind standing at the wooden door of an old stone fisherman's cottage at dusk, holding a small worn suitcase, shoulder-length wavy black hair, bright yellow raincoat with the hood down, dark brown dress, dark stockings, red short rain boots, sea fog in the lane, one warm light in the cottage window, soft painterly storybook illustration, cold blue dusk with a single warm light | `--cref MAELA_REF_v1 --cw 40`；`--no front view, face, text, lantern`（这时还没拿到灯笼） |
| SB-P4 | 序章 4：奶奶认不出她 | interior of an old Breton cottage in cold grey morning light, an old grandmother with grey hair in a bun and a dark green wool shawl sitting in a wooden rocking chair, looking with a polite empty expression at a small girl in a bright yellow raincoat standing in front of her (girl seen from behind, red boots), quiet and sad, soft painterly storybook illustration, muted cold palette | `--cref MAELA_REF_v1 --cw 40`；`--no text, horror, smiling grandmother`。奶奶尚无定稿，这张同时当 Soazig 的风格探索 |

**11-08 定稿用提示词 v2（P2–P4 + Soazig，可直接粘贴）**
共通：Niji 6，`--ar 16:9 --s 150 --sref SB_P1.png --sw 60`（只带 P1 画风）。每张**留一块干净的大面积（天空 / 墙面 / 雾）给两行字幕**，字幕颜色 #F0EED1 + 深色柔光，所以留白处不要太亮。顺序：先出 Soazig（C02-v2）→ 定稿裁 `SOAZIG_REF_v1.png`（白底正面）→ 再出 P4。

| 编号 | 提示词 | 参数 |
|---|---|---|
| C02-v2 Soazig 现在 | an old Breton grandmother in her seventies, full body, standing calmly, grey hair in a neat low bun, kind but tired face with a distant polite expression, dark green wool shawl over her shoulders, long dark charcoal skirt, plain white apron, black wooden-soled shoes, holding a half-mended fishing net, natural adult proportions, restrained expression, clean silhouette, limited palette, soft painterly storybook shading, plain light background, character concept sheet, front view and side view | `--ar 3:2 --s 150 --sref MAELA_REF_v1.png --sw 80 --no chibi, big eyes, blush, pastel, witch, horror` |
| SB-P2 v2 海雾进镇 | a narrow cobbled street of an old Breton fishing village at night, thick pale sea fog rolling in from the harbour and curling around low granite cottages, one small window with a faint warm candle being slowly swallowed by the fog, wet slate roofs, quiet and empty, large soft area of fog in the upper half, soft painterly storybook illustration, cold foggy blue-grey palette #4A5A6E #1E2633 #9AA3AD, a single tiny warm light, dreamlike and sad | `--no people, text, horror, lit lighthouse` |
| SB-P3 v2 梅拉到奶奶家 | a small 11-year-old girl seen from behind at the wooden door of an old granite fisherman's cottage at dusk, holding a small worn brown suitcase, shoulder-length wavy black hair, bright yellow raincoat with the hood down, dark brown dress, dark stockings, red short rain boots, sea fog in the lane, one warm light in the cottage window, far in the background a dark unlit lighthouse on a cliff, girl small in the lower left third, open foggy sky in the upper right, soft painterly storybook illustration, cold blue dusk with a single warm light | `--cref MAELA_REF_v1.png --cw 40 --no front view, face, text, lantern, lit lighthouse` |
| SB-P4 v2 奶奶认不出她 | interior of an old Breton cottage in cold grey morning light from a small window, an old grandmother with a grey bun and a dark green wool shawl sitting in a wooden rocking chair, a half-mended fishing net on her lap, looking with a polite empty expression at a small girl in a bright yellow raincoat and red boots standing in front of her (girl seen from behind), quiet and sad, plain bare stone wall above them, soft painterly storybook illustration, muted cold palette with the yellow raincoat as the only bright colour | `--cref SOAZIG_REF_v1.png MAELA_REF_v1.png --cw 30 --no text, horror, smiling grandmother, lantern` |

检查：P2–P4 灯塔一律不亮；人物服装颜色照写；留白处放得下两行字。下载 Upscale (Subtle) 后：`python TechArtAsset/Storyboard/Prologue/_work/finish_sb.py <图> P2`（`--x/--y/--zoom` 调裁切）。


**11-09 实际用的改版**（参考图一律用 GitHub raw 链接，见 LESSONS §8）：
- SB-P2：v2 原样，`--sw 60` 偏青蓝，后期调色。
- SB-P3 v3：开头改成 `back view, a tiny lone figure seen from far behind, a small girl with her back to the camera facing the wooden door ...`，加 `wide shot, far in the background a dark extinguished lighthouse silhouette on a cliff with no light, muted ... desaturated`；**去掉 --cref**；`--sw 30 --no face, looking back, looking at viewer, front view, text, lantern, lit lighthouse, lighthouse beam, glowing lighthouse, close-up`。四张全背影、灯塔全暗。
- SB-P4 v3：只挂 `--cref SOAZIG_REF_v1 --cw 50`，梅拉靠文字；奶奶对了但会笑。v4：开头 `over-the-shoulder view from behind a girl ... back fully to the camera`，奶奶写 `polite blank expression, not smiling`，`--no smile, smiling, girl face, girl profile, side view of girl`（结果待看）。

**Flow（Google Veo）— P1 空镜动画（试用，不行就用静态）**：Flow 里选 Frames to Video，起始帧放 SB-P1 定稿图，8 秒，提示词：
`Slow gentle push-in toward the dark lighthouse. Sea fog drifts slowly from left to right over the water, small waves move softly, a few village windows flicker faintly. The lighthouse stays dark. Painterly storybook style kept exactly as the input image. No camera shake, no people, no text, no new objects.`
检查：画风不变、灯塔不亮、无新物体。导出 1080p MP4 → `TechArtAsset/Storyboard/Prologue/`。不理想就不改了，直接用静态图（深入调 Flow 留给《妖精丘陵》）。

## 4c. 故事版 A / B（11-11 第一轮，MJ 网页实际用的）

共通：`--ar 16:9 --s 150 --niji 6 --sref <GitHub raw>/TechArtAsset/Storyboard/Prologue/SB_P1.png --sw 30`（B2、B3 回忆画面 `--sw 20` 让暖棕色出来）。梅拉镜头不挂 cref，写服装 + `back view` + `--no face, looking back`。灯塔熄灭的镜头 `--no lit lighthouse, light beam, glowing lamp`（仍常常亮，挑暗的或编辑器擦）。

| 编号 | 提示词要点 | 结果（第一轮） |
|---|---|---|
| A1 | lamp room at top of lighthouse, old keeper from behind (grey beard, navy sweater, cap) lighting a small brass hand lantern from the great lamp, warm fire on hands, cold blue sea through windows | 构图好，爷爷是侧脸；大塔灯没画出来 |
| A2 | wide village + harbour, lit lighthouse casting a big soft circle of warm gold light, fog outside the circle held back | 暖光圈明显，可用 |
| A3 | lighthouse gone dark, fog rolling ashore toward the dim village | 4 张里 3 张灯塔仍亮 |
| A4 | cold blue cottage room, Maela from behind raising the lantern, warm circle shows old memories (fishing net, photos) | 背影对；暖光圈偏弱 |
| B1 | through a small attic window: dark lighthouse, black sea under fog | 圆窗像船舷窗 |
| B2 | warm faded memory: two boats rowing out on Anaon night, candles in village windows | 暖棕回忆色好 |
| B3 | one fisherman jumped back on the rocks, the other rows into fog toward a faint cold light | 有两张“空中跳跃”像喜剧 |
| B4 | keeper from behind before the just-darkened great lamp, fog at the glass with a faint figure | 部分灯仍亮；一张雾里有人影 |
| B5 | Maela from behind at the end of a long pier, lantern up, distant bell tower, open sky for title | 很好 |

**用户挑选（11-11）**：A1 右下（灯型接近）；B2 左上（回忆高光 → 后面跌落）；B3 左上；B4 左下，但塔身橘色光要去掉（橘色 = "还有希望"，与熄灯后的怨恨 / 内疚相反）；B5 右上，举灯杆子 PS 重摆。下一轮提示词注意：熄灯镜头 `--no orange light, warm glow on the tower`；梅拉举灯写 `holding a small brass lantern by its ring handle, arm bent`（避免长杆）。

**第二轮（11-12）**
- B1 v2：`view from inside a dark dusty attic ... a small square wooden attic window with four panes under the sloping roof beams, through the glass a dark extinguished stone lighthouse ...` + `--no round window, porthole, lit lighthouse, light beam, glowing lamp, orange light` → 四张都是方窗、灯塔暗，可用。
- A4 v2：写 "casts a large warm golden circle of light" → MJ 画成**发光的光环 / 传送门**，不能用（别写 circle of light）。
- A4 v3：`warm lantern light spills softly across the room so the side of the room near her looks warm, old and lived-in like years ago ... while the far side of the room stays cold, dark blue and empty, natural soft light falloff` + `--no ring, circle, portal, halo, magic circle, sparks, long pole` → 冷暖分边自然，左上最好。

**道具：Home 箱子（11-11 定稿 `Crate_v1.png`）**
`game prop sprite, one old weathered wooden crate, orthographic front view, flat 2D side-on elevation, dark oak planks with one diagonal brace, worn iron corner straps, small coil of rope on top, centered, isolated on pure white background, clean silhouette, soft painterly hand-painted storybook texture, muted desaturated brown and blue-grey --ar 13:11 --s 100 --niji 6 --sref <GitHub raw>/TechArtAsset/Scenes/Home/Present/Home_Present_v1.png --sw 15 --no scenery, background, floor, ground, grass, night sky, lantern, candle, light, glow, shadow, perspective, three-quarter view, text`
（第一版 `--sw 60` 把整个夜景带进来，抠不出；道具一律低 sw + 白底 + 正面。后处理 `TechArtAsset/Scenes/Home/Props/_work/make_crate.py`。）

## 4d Home 道具与阁楼（2026-11-12）

Home 道具共通：单体透明图用于游戏；原 MJ 合成图留 `_work/`。道具比例和锚点需在 Unity 中结合场景确认。

| 编号 | 对象 | 提示词 | 参数 / 备注 |
|---|---|---|---|
| P01-H | 铜灯笼（MJ 源） | game prop sprite, one old brass ship's hand lantern with a round ring handle on top, glass chimney with a small warm flame, dented weathered brass, standing upright on the ground, orthographic front view, flat 2D side-on, centered, isolated on pure white background, clean silhouette, soft painterly hand-painted storybook texture | `--niji 6 --sref https://s.mj.run/eghoPUBkfKo --sw 15 --no scenery, background, floor, shadow, perspective, three-quarter view, text, hand, person`。源 job `2a9fe918-de40-4649-993d-9780b09c1ac0`；之后依照用户选定的单体画风制作成 `Lantern_v1.png` |
| P02-H | 完整梯 + 断梯（MJ 源） | game prop sprites, two versions of the same old wooden ladder side by side: on the left a complete sturdy wooden ladder, on the right the same ladder broken, only the lower half remaining with snapped splintered rails and missing rungs, orthographic front view, flat 2D, isolated on pure white background, clean silhouettes, soft painterly hand-painted storybook texture, muted brown | `--niji 6 --ar 3:2 --sref https://s.mj.run/eghoPUBkfKo --sw 15 --no scenery, background, floor, shadow, perspective, three-quarter view, text, person`。源 job `591563a6-dd42-49c8-b459-5326e4fc8a07`；原合成图只作形状参考，分成 `Ladder_Whole_v1.png` 与 `Ladder_Broken_v1.png` |
| S02-H v2 | 阁楼现在层（正视版重跑） | side view 2D game background of a small cramped attic room inside an old Breton stone cottage at night, composed as a flat straight-on side elevation for a 2D side-scroller. See the room directly from the side with no visible floor depth: a horizontal worn timber floor spans the bottom, low sloping roof beams meet above, and rough stone walls frame the room. On the left, a square open hatch breaks the floor and a ladder rises into the attic; a few old trunks covered with dusty white sheets sit against the wall. On the right wall, a small square window divided into four panes; beyond it the dark unlit lighthouse stands on a distant cliff above a foggy sea. Empty room, uncluttered playable floor through the middle. Cold blue-grey night with restrained amber accents. Closely match the attached style reference's hand-painted storybook brushwork, inked shapes, color treatment and lighting, with painterly textured surfaces and crisp readable forms | `--ar 16:9 --niji 6 --sw 60 --stylize 150 --sref https://s.mj.run/eghoPUBkfKo --no people, characters, text, round window, lit lighthouse, light beam, three-quarter view, isometric view, perspective floor, receding floorboards, visible downstairs, moon, cast shadow`。旧图 job `de6dc6e8-64ba-48a2-9835-8cdf91dc0d12` 透视太强，只作画风、灯光参考；此版 job `59ae29d2-4e1e-49cb-b31b-dbed6f94c1d0`，提交于 2026-11-12 |
| S02-H v3 | 阁楼现在层（扁平切面） | 2D side-scrolling attic background, orthographic side elevation of one small cramped attic inside an old Breton stone cottage at night. The room is a flat theatrical cutaway viewed head-on: camera parallel to the broad back wall, front wall removed, back wall flat across the frame. Show no side walls and no floor surface; the floor is only a thin perfectly horizontal strip along the bottom, with no receding floorboards or vanishing point. Roof beams sit flat against the back wall and slope up to the ridge. At far left, a square hatch interrupts the floor with a vertical ladder rising through it. A few old trunks under dusty white sheets rest against the wall. At far right, a small square four-pane window; through it, a tiny dark unlit lighthouse on a distant cliff above a foggy sea. Keep the middle floor open for gameplay. Closely match the attached style reference: same hand-painted storybook brushwork, inked shapes, textured paint, saturated cobalt blue shadows and restrained amber highlights | `--ar 16:9 --niji 6 --sw 60 --stylize 150 --sref https://s.mj.run/eghoPUBkfKo --no people, characters, text, round window, lit lighthouse, light beam, three-quarter view, isometric, perspective, vanishing point, visible side walls, floor plane, receding lines, visible downstairs, moon, cast shadow`。job `aa2c55e4-7411-4076-8118-3e244ea8c1a0`；已出四张，画风一致但仍有透视，暂不作游戏背景 |
| S02-H v4 | 阁楼（用户选定的轻透视候选） | Hand-painted 2D game background illustration for a Breton storybook adventure: one small cramped attic room inside an old stone fishing cottage at night. Gentle three-quarter side perspective from the left, shallow visible side walls and timber floorboards receding naturally toward the back. The attic must read clearly as an attic: steep sloping roof with heavy exposed crossbeams, rough blue-grey granite walls, one square open hatch in the floor at far left with a short old wooden ladder emerging through it, a few trunks draped in faded off-white sheets against the back wall, and one small four-pane square window high on the right wall. Through that small window, show dark sea and a tiny completely unlit lighthouse. Keep a broad uncluttered patch of floor through the center for platform game play. Warm amber light from off-screen, cobalt blue-grey shadows, visible loose brushstrokes, hand-painted shapes and softened edges matching the existing Home scene reference. Keep the back wall continuous except for the small window; no large opening or doorway. | `--ar 16:9 --niji 6 --sw 60 --stylize 150 --sref https://s.mj.run/eghoPUBkfKo --no people, text, doorway, large opening, missing wall, large window, visible ship, glowing lighthouse, light beam, photorealism, 3d render`。原 job `83223836-af12-427b-ae2d-cdd704152b9a` index 0；Upscale (Subtle) job `bf19f584-cd7e-43d5-b936-2b345e8a5097`，图片已下载为 `Attic_PerspectiveRef_v2.png`（2912×1632）；用户认可，待 Unity 校对 |

## 4e Home 梯子 / 灯笼清理版与阁楼背景（2026-11-12）

本轮把选定的梯子与灯笼做成透明单体 v2；旧 v1 保留，不覆盖。阁楼采用正视切面构图，制作后再把烘焙进背景的梯子和壁挂灯移除，便于 Unity 以独立图层切换 / 替换道具。

| 文件 | 工具 / 参考 | Prompt 要点 | 结果 |
|---|---|---|---|
| `Ladder_Whole_v2.png` | OpenAI ImageGen；参考 `LadderPair_MJ_src_v1.png` 左侧完整梯 | 单独重绘完整木梯，严格正视，双侧木轨 + 五档踏棍；手绘木纹、深色墨线；真实透明底，不要光晕、阴影或背景 | 透明单体，1024×1536 |
| `Ladder_Broken_v2.png` | OpenAI ImageGen；参考 `Ladder_Broken_v1.png` | 保留断梯下半段，双侧断裂栏杆 + 三档踏棍；正视；真实透明底，光线限制在木头表面 | 透明单体，1199×1312 |
| `Lantern_v2.png` | OpenAI ImageGen；参考 `Lantern_MJ_src_v1.png` | 铜制圆环提手灯笼，正视；火焰仅在玻璃内发光；真实透明底，无外部光晕、地面阴影与背景 | 透明单体，1254×1254 |
| `Home_Attic_Both_v1.png` | OpenAI ImageGen；参考原阁楼透视候选的画风，按 S02-H 正视切面构图 | 16:9 横版石墙阁楼；平直地板与屋梁；左侧空方形梯口，右侧四格方窗，窗外熄灯灯塔；保留中间可走区域。二次编辑仅移除烘焙梯子和壁挂灯，保持其余布局不变 | 阁楼现在 / 记忆共用背景，1672×941；待 Unity 检查镜头和梯口对位 |

## 4f Home 铜灯笼去影（2026-11-12）

| 文件 | 工具 / 参考 | 处理 | 结果 |
|---|---|---|---|
| `Scenes/Home/Props/Lantern_v3.png` | Photoshop 2023；用户选定 `Props/_work/Lantern_MJ_src_v1.png`，MJ Niji 6 job `2a9fe918-de40-4649-993d-9780b09c1ac0` | 保留 MJ 绘制像素；选择主体后修正底座边缘蒙版，移除白底和地面投影；透明画布留 16 px 边距 | 透明单体，1032×1875；分层 PSD `Props/_work/Lantern_MJ_v2_PS.psd` 保存原图层和去影图层 |

## 4g Home 当前资产与提示词边界（2026-11-13）

以下是当前实现交接；旧提示词与 job 仅作为制作历史，不能覆盖本节的剧情/资产决定。

- 楼下无梯背景 `Home_Present_v3.png` 是用户在旧背景上编辑的结果，不是本轮新 MJ 出图。楼下现在 / 记忆共用这张底图，由 Unity 现有滤镜/灯光表现状态变化。
- 阁楼采用 `Attic_PerspectiveRef_v3.png`：来自 S02-H v4 选定并 Subtle 放大的原图，用户手工去掉画中梯子、处理窗外塔灯。这里的“v4”是 Prompt 编号，不是当前导出图版本；导出图为 v3。没有为该修订另抽 MJ 卡。
- `Ladder_Whole_v4.png` 是用户 Photoshop 手工拼接、修订并导出的透明完整梯，保留手绘风格；不是新 MJ 生成。旧 P02-H 成对梯子 prompt 及其 job 只归档来源。剧情确定现在层梯位为空，钟声后出现完整梯并触发锁输入、淡变到阁楼，不制作断梯配对、不做攀爬玩法。
- 当前 Unity 交接不需要新生成图。若 Unity 校对发现美术缺口，再按用户要求先检查画风参考，另提 prompt；不要自行改成矢量/平涂风格。

执行与验收要求见 `CommandForAgentToInitialRun/2026-11-13_Unity_Home_Review_Art_Transition_Audio.md`。

## 5. 变更记录

| 日期 | 变更 |
|---|---|
| 2026-10-31 | 新增 C01-R2、C01-T、K1-BG、K1-E1、K1-E2（实际用过 / 待用的 prompt 与参数） |
| 2026-11-02 | 游戏画风改手绘：STYLE_PIXEL → STYLE_GAME；C01-P → C01-G；STYLE_SCENE 加 painterly；K2、KT 去掉像素描述 |
| 2026-11-02 | 按《妖精丘陵》拆解结果定 STYLE_GAME；STYLE_CHAR 去掉 Q 版（3 heads tall → 约 5 头身） |
| 2026-11-06 | C01-T 实际改为单出侧面（--cw 40）+ 背面取自 v2 第一轮；C01-G v3 补服装颜色 |
| 2026-11-05 | C01-T、C01-G 改 v2：右手提灯、`--no bag`、5 头身；C01-G 用中性光照 |
| 2026-11-11 | 新增 §4c 箱子提示词 |
| 2026-11-11 | 新增 §4c 故事版 A / B 第一轮提示词与结果 |
| 2026-11-09 | §4b 记录 P3 v3、P4 v3/v4 实际写法（背影不挂 cref；双人只挂一张 cref） |
| 2026-11-08 | 新增 §4b v2：SB-P2..P4 v2（留字幕位、--sref SB_P1）与 C02-v2 Soazig（--sref MAELA_REF_v1） |
| 2026-11-12 | 新增 §4d Home 梯子、灯笼来源提示词与阁楼重跑提示词；阁楼沿用原 Niji 6 与 style reference；v2 `59ae29d2…` 仍有透视，v3 `aa2c55e4…` 画风接近参考但仍有透视 |
| 2026-11-12 | 新增 §4e：梯子、灯笼透明单体 v2 和阁楼正视共用背景；说明 ImageGen 参考来源、去掉烘焙道具的处理及 Unity 对位检查 |
| 2026-11-12 | 新增 §4f：选用 MJ 灯笼并在 Photoshop 去白底与地面投影；保留 MJ 原图和透明单体 v1 / v2 |

## 2026-11-13 采用与拒绝记录

- P01-H 原 MJ 铜灯继续采用；Photoshop 清理 v3 后由用户去除残留，临时名 Lantern_v3_m.png 已改为 Lantern_v4.png。此步没有新生成提示词。
- S02-H v4 左上 index 0 已被用户选中并 Subtle 放大下载；实际图为轻透视，画风获认可。提示词中的四格窗、梯口和熄灯灯塔属于目标要求，不能当作输出已满足的验收结论。
- 拒绝的梯子 job：15a42fcf-e51e-4992-8858-29f08ec21907；提示词要求左右完整梯／破损下半梯，参数 --ar 3:2 --niji 6 --sw 60 --stylize 150，style ref eghoPUBkfKo。输出形状、配对和场景污染不适用，勿自动复用。
- 拒绝的灯笼 job：e4a50227-c748-4813-bd78-33773a913f4c；蓝色灯笼批次未采用，继续用 P01-H 铜灯。该批次完整 prompt 未在本地归档，不凭截图补造。
- 历史建议（已被剧情决定取代）：曾建议生成断梯配对；用户现已明确现在层梯位保持空置，不制作断梯、不做攀爬。当前 Unity 阶段无需新增出图。
