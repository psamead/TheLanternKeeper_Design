<!-- 设定变更记录：故事、玩法、美术共用。任何会影响已定设定的修改，先在这里登记，再改具体文件。 -->

# DESIGN_CHANGES：设定变更记录与流程

## 1. 每个领域以哪份文件为准

| 领域 | 以此为准 |
|---|---|
| 故事、世界观、角色、结局 | `STORY_BIBLE.md`（v2.0） |
| Demo 范围、玩法、系统 | `DEMO_IMPLEMENTATION_PLAN.md`、`handoff.md` |
| 美术规格与资产管线 | `ART_HANDOFF.md`、`TechnicalArt/HANDPAINTED_SPEC.md` |
| 宣传美术 | `ART_DIRECTION.md` |
| 参考图与资产状态 | `ART_ref/ASSETS.md` |

## 2. 变更流程

1. **登记**：在第 3 节加一行，状态写「提议」。
2. **判断影响**：对照第 4 节清单列出要改的文件。美术细节可直接改并登记；涉及故事含义的只登记，等确认。
3. **确认**：用户确认后改为「已确认」。
4. **执行**：逐个改文件；版本号递增；旧版移入 `deprecated/`。
5. **完成**：状态改为「已完成」并写日期。

## 3. 变更记录

| 日期 | 变更 | 原因 | 影响的文件 | 状态 |
|---|---|---|---|---|
| 2026-10-22 | 三个故事构思中选定《守灯人》 | 用户选择 | — | 已完成 |
| 2026-10-24 | 故事 v1.0：补全海难、承诺、熄灯与失忆的因果 | 原故事不完整 | story_draft | 已被 v2.0 取代 |
| 2026-10-24 | 故事 v2.0：改为布列塔尼民俗奇幻（伊斯、达于、灯火之约）；角色改西方名（Maela、Soazig、Yann、Loïc、Old Per） | v1.0 像国内电视剧；向《妖精丘陵》风格靠拢 | 全部文档 | 已完成 |
| 2026-10-24 | Demo 体量缩小为 4 个 Scene、5–8 分钟（参考 Battle Car Arena） | 项目时间紧 | Demo 制作方案 v1.0 | 已完成 |
| 2026-10-30 | 建立 md 交接结构（STORY_BIBLE、DEMO_IMPLEMENTATION_PLAN、handoff、ART_HANDOFF 等）与美术文件夹 | 进入美术与制作阶段 | 根目录 md、TechnicalArt、ART_ref、TechArtAsset | 已完成 |
| 2026-10-31 | Maela 概念 v1 定稿：兜帽放下、齐肩黑色波波头、红色短靴、左手提灯（`ART_ref/Maela_v1.png`） | 第一次出图 | ASSETS.md、ART_HANDOFF §6 | 已完成 |
| 2026-10-31 | Maela 斜挎小包：保留作“贝壳包”或擦掉 | 概念图自带，设定中没有 | ART_HANDOFF §4.2、概念图 | 已确认（11-05）→ 见下一行 |
| 2026-11-05 | 斜挎包 **Demo 不做**（转身图、游戏版 `--no bag`）；另留一个“背包版” Maela，完整版作**过了新手村之后的储物包** | 用户决定；Demo 少一个部件 | ART_HANDOFF §4.2 / §8、ART_PROMPTS C01-T / C01-G；完整版：STORY_BIBLE、完整版概念设计说明 | Demo 部分已完成；完整版储物包为提议 |
| 2026-10-31 | 海报概念图画风改为沿用 Maela 绘本风（原定“高清像素风插画”） | 用户决定；游戏内画风可不同 | ART_HANDOFF §2、ART_DIRECTION K1、ART_PROMPTS K1-BG | 已完成 |
| 2026-10-31 | 游戏内画风：像素（原定）或接近海报的绘本风 | 与学生讨论中 | ART_HANDOFF §2、PIXEL_ART_SPEC、生产流程 | 已确认 → 见下一行 |
| 2026-11-02 | **游戏画风改为手绘 2D**：沿用概念图绘本风、稍游戏化，方向接近《妖精丘陵》但不照搬；1920×1080 / PPU 100；场景分层大图，角色骨骼动画；碰撞仍用 Tilemap | 用户决定；美术主要靠 AI 出图再清理，像素需全手画 | ART_HANDOFF、HANDPAINTED_SPEC（新）、PIXEL_ART_SPEC（移入 deprecated）、ART_PROMPTS、ART_PRODUCTION_GUIDE、ART_DIRECTION、handoff.md、DEMO_IMPLEMENTATION_PLAN、AGENT_PROCESS_GUIDELINES、对应 Word | 已完成 |
| 2026-11-02 | 美术基调：奇幻为主、带一点民俗的暗与静，不走恐怖，落脚点是抉择与成长（11-02 修订）；不做 Q 版；角色约 5 头身、正常眼睛、表情克制；借《妖精丘陵》墨线 / 平涂 / 强光源，回避其甜美粉彩 | 用户：角色太小孩，主题偏 fantasy、略 dark | HANDPAINTED_SPEC §0、ART_PROMPTS（STYLE_CHAR、STYLE_GAME）、ART_HANDOFF §4.2 | 已完成 |
| 2026-11-02 | 字体系统：标题 Cinzel Decorative（油墨毛边）、副标题 IM Fell English SC、菜单 Cinzel、对话 EB Garamond、回忆 Cormorant Garamond Italic；取代像素字体候选 | 画风改手绘；与《妖精丘陵》区分 | ART_HANDOFF §2、ART_DIRECTION §2、字体与UI决定.xlsx | 已完成 |
| 2026-11-02 | 民俗视觉符号：主用**白鼬尾纹 + 布列塔尼蕾丝**；三螺旋纹不作主视觉（《妖精丘陵》标题与菜单图标已用），最多作灯笼底座小刻纹 | 用户：与《妖精丘陵》太像 | ART_DIRECTION、HANDPAINTED_SPEC §0、标题框、UI 边框 | 已完成 |
| 2026-11-03 | 菜单音效改为自然声（海浪 / 海风 / 木头或黄铜轻响），不用合成电子音；菜单需背景音乐 | 用户试玩：太电子、与主题不符 | Unity `ProceduralMenuAudio`、MENU_UNITY_PROGRESS | 提议（待做） |
| 2026-10-31 | Maela 改为右手提灯（朝右时灯笼在近镜头一侧，不被身体挡住；flipX 后同样在近侧） | 侧面可读性 | ART_HANDOFF §4.2 / §8、ART_PROMPTS C01-T / C01-G、HANDPAINTED_SPEC §3.1 | 已完成（11-05 用户确认；概念图 Maela_v1 保持左手不改） |

## 4. 影响清单（改设定时逐项检查）

- ☐ `STORY_BIBLE.md` 与 `story_draft/` 故事设定 Word
- ☐ `purposal_story/` 完整版概念设计说明、Demo 制作方案
- ☐ `DEMO_IMPLEMENTATION_PLAN.md`、`handoff.md`
- ☐ `ART_HANDOFF.md` §4、`ART_PROMPTS.md`、`ART_ref/ASSETS.md`、已做好的资产
- ☐ Demo 台词
