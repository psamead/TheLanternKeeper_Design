# 守灯人学生作品集跨电脑制作交接

更新：2026-11-15。执行者是在另一台设计电脑上使用 Codex 的制作 Agent；该电脑可使用 InDesign、Vectorcraft 等已安装设计工具。请从网络共享读取本项目现有资料，完成学生作品集 4–5 页 PDF，并把最终 PDF 和可编辑制作包存回同一个共享项目。当前只完成本说明，作品集尚未制作。

## 1 开始工作与共享路径

共享根目录的已知 UNC 入口：

```text
\\haoxi-surfacep\Administrator\Documents\MyFlie\AsArtPortfolioTeaching\Game_York\SharedWorkFolder
```

本机对应目录是 `C:\Users\Administrator\Documents\MyFlie\AsArtPortfolioTeaching\Game_York\SharedWorkFolder`。另一台电脑不要把这个 C 盘路径当作自己的本地路径。先验证 UNC 可读、`ForDesignPortfolio` 可写；映射盘可用，但制作记录写清实际共享根目录。网络不可达时报告具体原因，不从 GitHub 较旧发布版替代共享源文件。

先读本说明即可开始素材盘点和页序设计；细节按下文索引查阅。无需重新制作游戏、重跑旧 Unity 任务或重新生成一批美术。请读取你所在电脑适用的本地 Agent/技能说明，按实际可用软件完成制作，不假设这里的运行时路径或插件也安装在那里。

默认先做 5 页，资料不足时压缩为 4 页。院校尺寸、文件大小或语言要求若已提供，以它们为准；尚无要求时建议 A3 横版单页 PDF，页面文案英文、制作回报中文。此为制作起点，不是已确认的院校规范。姓名、课程、年份和个人职责只填已确认信息，缺项不编造，也不把 TODO 占位符留在最终 PDF。

## 2 项目是什么

**标题**：The Lantern Keeper／守灯人。副标题：A Tale from the Breton Coast。

**类型**：手绘绘本风格的 2D 横向叙事解谜 Demo。目标演示长度约 4–6 分钟，当前用户录制的参考录像约 184 秒；两者分别是设计目标和该次实录时长，不混称“实测平均游玩时间”。

**一句话**：在记忆逐渐被海雾带走的小镇，女孩提起守灯人的旧灯笼，照见过去并找到继续前行的路。

**情绪**：冷夜里的一盏暖灯。布列塔尼民俗奇幻，安静、略带忧郁、保有希望。不要把版面做成可爱 Q 版、像素风、惊悚海报或艳丽手游广告。

可用的英文简介草稿：

> A hand-painted-style 2D narrative puzzle demo set on the Breton coast. As sea fog carries away the town's memories, Maela uses an old lantern to reveal traces of the past and find a way forward.

这段是本次供排版使用的简介建议，不是对学生个人创作经历的陈述。

## 3 故事与 Demo 范围

故事设定以 ForAgent/Design/STORY_BIBLE.md 为准：灯塔守护海与岸、人与记忆之间的边界。一年前守灯人 Yann 熄灯，海雾开始带走记忆；孙女 Maela 来到奶奶 Soazig 家，发现奶奶已认不出她。爷爷留下的灯笼保有旧日火焰，可以照见记忆。完整故事涉及 Ys、Dahut、亡灵之夜和爷爷的承诺；这些世界观为故事设想，不都是 Demo 已出现的可玩内容。

已做 Demo 主线：开始菜单 → 序章 P（4 张插图）→ Home 楼下拾灯 → 故事 A（4 张灯笼来历插图）→ 从门边重新探索原灯位和梯位 → E 摇铃切入记忆层、完整梯出现 → 梯下剧情淡变进入阁楼 → 窗边触发结尾 B（5 张）→ B5 和返回选项。

核心交互是现在/记忆两层全屏切换，以冷蓝和暖金区分，通过记忆层完整梯前进。当前梯子是剧情传送入口，没有操作式攀爬；灯笼不是新增的瞬移能力。T 为拾灯，E 为持灯后的切换动作；未持灯不解锁探索和铃声。首次铃声完整播放期间锁定操作。

Demo 不包含可玩码头关卡、老佩尔 NPC、贝壳收集、灯油资源、多结局或完整七天冒险。B5 虽画有码头，只是故事版插图，不代表码头地图已开发。Soazig 概念已完成，游戏版立绘/对白和对话框仍是旧待办，不可列为已实现系统。当前本轮不把这些未做项新增为打包前置。

## 4 当前版本和用户反馈

- 已知上一轮 Unity 游戏实现提交：a803050，已有 Editor 路线/边界记录；122e013 只有文档链接更新。
- 用户明确说自己昨晚录制的视频版本整体正常、基本满意。它就是下文列出的完整录屏，可直接用于理解流程、选择现有画面、辅助作品集取材，不要求 Unity Agent 再录一条重复的完整流程。
- 当前 Home 背景已确认正确，禁止根据历史错版截图/录像改回旧背景。
- 最新三项小修：阁楼脚底行走线提高至用户绿线；B5 保持画面直接出选项，不二次淡黑；EndCard 的 Quit 同样返回开始菜单。
- 随后 Windows x64 EXE、Unity push、Web 构建与 GitHub Pages 试玩是交给 Unity 工作站的任务，目前本地没有新的实施/构建/上线回报。制作端先看 MENU_UNITY_PROGRESS.md 末尾，有新回报再用新的确认画面。
- 作品集可以先用已确认原图与现有录像开始制作。修后新图尚未出现时，不把绿线标注画进成品或假造“已修正”截图；选用不受改动影响的画面，或在制作回报中说明待换素材。

录像路径（相对共享根目录）：

```text
ForDesignScreenshot/2026-11-15_Home_FullDemo_Recordings/user_recording_0546_14_full_demo.mp4
```

录像是用户对既有流程的参考和认可，不证明之后的新小修、独立 EXE 或网页构建已经通过。无需把所有开发验收细节写进学生作品集。

## 5 作品集要展示的设计判断

请用少量、明确的证据说明“为什么这样设计”和“从概念到可玩 Demo 怎么落地”，避免仅排列成图片画册。

1. 灯光与记忆：冷蓝现在层和暖金记忆层形成空间与情绪差异；灯笼让过去变为通路，而不只承担装饰光源。
2. 角色可读性：黄色雨衣、黑短发、红色短靴与铜灯形成稳定剪影；游戏版约五头身、不做 Q 版。概念版和游戏版左右持灯差异有迭代原因，按图注明。
3. 民俗转为视觉语言：采用白鼬尾纹 Hermine、布列塔尼蕾丝；后期手绘规格优先于旧 Story Bible 中的三螺旋纹泛例。标题与 UI 统一使用现有纹样，不另外换成凯尔特结纹系统。
4. 叙事构图：P2 的远处单窗亮光代表希望与落差；B2 暖色往事与 B4 失去形成情绪跌落；B1 的斜构图与关闭的方窗表现距离感。具体选图理由查 STORYBOARD_SELECTION.md，不自行补造调研结论。
5. 控制规模：从较大的民俗故事收束为一个房间加阁楼，结合 P/A/B 故事版完成短 Demo。体现范围判断与清楚的玩家引导，不宣称做完全部章节。

## 6 建议 5 页结构

| 页 | 阅读问题 | 建议内容与证据 | 排版重点 |
|---|---|---|---|
| 1 项目概览 | 这是什么作品，有什么吸引力 | 海报或无字主视觉、正式标题、一两句简介、Demo 类型与核心机制、确认过的个人职责 | 一张有分量的大图；文字短，不复刻整份 GDD |
| 2 主题与视觉开发 | 如何把记忆与海岸民俗变成视觉 | 简短概念关系图、冷暖调色、Hermine/蕾丝、2–3 张已记录的方案/选图对比 | 每个对比都配明确取舍理由；只用可追溯的过程 |
| 3 角色与道具 | 人物如何适应游戏画面 | Maela 侧背面/游戏版、铜灯、少量部件拆分或动作图；说明剪影、持灯方向、图层/动画适配 | 给人物足够空间，不堆满各版本；不能把源概念误当最终运行图 |
| 4 场景与核心机制 | 玩家怎样理解并使用灯笼 | 尽可能同镜头的现在层/记忆层运行截图，加简短路线图，阁楼入口作为结果 | 明确区分原画、运行截图和制作示意；不手工给原画叠人物冒充实机 |
| 5 叙事呈现与结果 | Demo 的最终体验及下一步是什么 | 少量 P/A/B 插图或菜单/EndCard 画面、简短迭代反思、确认后的可玩链接或视频入口 | 收束为作品成果；真实链接未就绪则先用已提供视频方式，不生成假的上线二维码 |

若做 4 页，合并第 2 页主题开发与第 3 页角色开发，保留第 4 页机制说明和最终成果页。每页只承担一个清楚的问题，建议每页英文正文约 60–120 词，图注另计；按学生材料实际可讲的内容调整，不凑字数。

## 7 已验证存在的优先素材清单

下面路径均相对共享根目录。本清单于 2026-11-15 本地核对过文件存在和像素尺寸；“文件存在”不等于学生已亲手绘制，也不等于最新版游戏已采用。源图可以直接读共享原件，制作包内使用副本并保留来源。

| 用途 | 文件 | 像素尺寸 | 使用说明 |
|---|---|---|---|
| 项目主视觉 | `TechArtAsset/Poster/POSTER_v2.png` | 1792 × 2688 | 已做好的海报；可作开篇主视觉，保留原画比例，不把整张海报挤在小格里。 |
| 主视觉无字图 | `ART_ref/POSTER_BG_v2.png` | 1792 × 2688 | 便于另排作品集标题；是宣传图，不是运行截图。 |
| 标题组合 | `TechArtAsset/Menu/TITLE_FRAMED_v1.png` | 1470 × 897 | 现有项目标题和装饰框，检查透明底效果。 |
| 菜单静态设计 | `TechArtAsset/Menu/MENU_v1_mock.png` | 1920 × 1080 | 菜单设计稿，不冒充最终游戏截图。 |
| 角色概念 | `ART_ref/Maela_v1.png` | 2688 × 1792 | 早期概念左手提灯；游戏版改右手，注明迭代差异。 |
| 角色侧背面 | `ART_ref/Maela_v1_turnaround.png` | 4000 × 2000 | 游戏角色造型与剪影展示。 |
| 游戏版透明角色 | `ART_ref/MAELA_GAME_SIDE_v1.png` | 1157 × 2490 | 清理后的游戏侧面底稿，不等同当前 Unity 每个部件的最终像素。 |
| 奶奶概念 | `ART_ref/SOAZIG_REF_v1.png` | 1024 × 1024 | 概念已定；游戏立绘/对白未完成，不列为已实现功能。 |
| 楼下背景 | `TechArtAsset/Scenes/Home/Present/Home_Present_v3.png` | 2520 × 1080 | 底图可展示绘本风；实际游戏使用情况以当前录屏和进度为准。 |
| 阁楼背景 | `TechArtAsset/Scenes/Home/Attic/_candidates/Attic_PerspectiveRef_v3.png` | 2912 × 1632 | 当前采用阁楼图；目录名 candidates 不代表现在没进 Unity，参照最新进度。 |
| 独立铜灯 | `TechArtAsset/Scenes/Home/Props/Lantern_v4.png` | 1032 × 1875 | 核心叙事道具。 |
| 完整梯 | `TechArtAsset/Scenes/Home/Props/Ladder_Whole_v5.png` | 1440 × 4200 | 记忆层通路；高度很长，版面适当裁细节，不强塞满页。 |
| 箱子 | `TechArtAsset/Scenes/Home/Props/Crate_v1.png` | 520 × 440 | 可选的小道具与游戏化细节。 |
| 叙事开篇 | `TechArtAsset/Storyboard/Prologue/SB_P1.png` | 2208 × 1242 | 已定序章插图；塔灯熄灭。 |
| 奶奶失忆 | `TechArtAsset/Storyboard/Prologue/SB_P4.png` | 2208 × 1242 | 叙事情绪，可和角色页小图结合。 |
| 灯火之约 | `TechArtAsset/Storyboard/LanternOrigin_A/SB_A2.png` | 2208 × 1242 | 暖光守住小镇的故事版，不能标作可玩地图。 |
| 灯笼记忆 | `TechArtAsset/Storyboard/LanternOrigin_A/SB_A4.png` | 2208 × 1242 | 冷暖空间变化的叙事插图，不能标作 Unity 层切换截图。 |
| 暖色往事 | `TechArtAsset/Storyboard/Ending_B/SB_B2.png` | 2208 × 1242 | 回忆的高光与后续失去形成落差。 |
| 最终 B5 | `TechArtAsset/Storyboard/Ending_B/SB_B5.png` | 2208 × 1242 | 结束页主图；静态干净源图不含运行 UI。 |
| 现在层运行图 | `ForDesignScreenshot/2026-11-13_Home_Visual_Notes/after/present_v1.png` | 1920 × 1080 | 历史运行截图；选用时标明版本，不能据此改当前背景。 |
| 记忆层运行图 | `ForDesignScreenshot/2026-11-13_Home_Visual_Notes/after/memory_ladder_v5.png` | 1920 × 1080 | 与上张同轮、可用于机制对照；核对裁切与镜头一致。 |
| 新路线 Home | `ForDesignScreenshot/2026-11-15_Home_Pickup_Story_Attic/after/03_fixed_hints.png` | 1920 × 1080 | a803050 路线证据中的游戏画面；按画面实际内容写说明。 |
| 阁楼运行图 | `ForDesignScreenshot/2026-11-15_Home_Pickup_Story_Attic/after/04_attic_first_landing.png` | 1920 × 1080 | 本轮绿线抬升前，不能标作已修正的新阁楼地板。 |
| EndCard 运行图 | `ForDesignScreenshot/2026-11-15_Home_Pickup_Story_Attic/after/05_endcard_dwell.png` | 1920 × 1080 | B5 和菜单运行画面；待新的小修结果后再按需替换。 |

其他可用材料：

- P1–P4：`TechArtAsset/Storyboard/Prologue/SB_P1.png` 至 `SB_P4.png`。
- A1–A4：`TechArtAsset/Storyboard/LanternOrigin_A/SB_A1.png` 至 `SB_A4.png`。
- B1–B5：`TechArtAsset/Storyboard/Ending_B/SB_B1.png` 至 `SB_B5.png`。
- 角色动作预览：`TechArtAsset/Characters/Maela/_work/anim_v2/Maela_Run_v4.gif`、`Maela_Walk_v3.gif`；可抽代表帧并注明动作预览，不当作当前完整 Unity 骨骼工程截图。
- 可编辑角色源：`TechArtAsset/Characters/Maela/Maela.psb` 与 `Maela_src.psd`；PSB 的具体游戏版本按进度记录，不在作品集机器改层名/ID/外框。
- 背景、灯笼、梯子 PSD 多在相应 `_work/`，仅按需要读取；本地存在，GitHub 未必有。

若须从用户录像取图，定位真实帧、只裁 Game 画面，去掉 Unity Editor、任务栏和播放器控制条，不拉伸原画、不让旧截图上绿线或红框进入成品。记录视频文件名、时间码和裁切方式到制作记录；现成干净图能满足时优先用干净图。取帧是作品集取材，不要求重新录屏，也不替代 Unity 实际截图的来源说明。

## 8 版式与字体

整体延续冷海蓝、暖金与米白，留出阅读空间。游戏原图为主体，统一栅格、页边距、标题层级、图注和页码。不要每张图套相同粗框，不把游戏暗背景直接铺满所有正文；正文可用浅色底保证可读。重要画面保持足够尺寸，1920×1080 截图不要跨整页强行放大再假称高清印刷图。

已有调色参考：现在层 #4A5A6E／#1E2633，记忆层 #E8B45A／#7A4A2A，雨衣 #F6D743，火焰 #FFF1C9，正文米白 #F2EBDD。允许为阅读调整页面底色与正文对比，不改项目主视觉色彩。

`TechnicalArt/fonts/` 已有字体及 OFL：CinzelDecorative-Bold.ttf、Cinzel-Variable.ttf、IMFellEnglishSC.ttf、EBGaramond-Variable.ttf、CormorantGaramond-Italic-Variable.ttf。项目标题可用现成 TITLE_FRAMED_v1，正文优先清楚易读，装饰字体和斜体不承担长段文字。若 InDesign/导出流程不支持某个可变字体，选可用的嵌入方案并在制作记录中说明替换，不把缺字留到最终 PDF。

## 9 工具与网络制作方式

优先使用这台设计电脑实际可用的 InDesign 生成可编辑页稿；Vectorcraft 或其他矢量工具用于原创的流程图、配色/图标或版式辅助。软件只是手段，最终以 4–5 页 PDF 的阅读效果为准，不为使用更多工具而重画全部资产。

共享原资产只读引用。先检查网络链接与字体；可以在工作站本地临时目录工作以提高软件响应，保存与导出阶段将最新源文件、链接图、字体许可和 PDF 一并复制回共享 ForDesignPortfolio，核对复制成功。最终不能只留本地桌面文件，也不能留下仅指向另一台机器 C 盘的失效 Links。

InDesign 建议同时保存 INDD 与 IDML；打包所用链接图到 Source/对应版本/Links，包含必要许可与可移交字体文件（按许可证），或记录字体取得方式。Vectorcraft/其他软件保留原生可编辑文件及通用 SVG/PDF（按实际用途）。不改原始 PSB/PSD 来配合版面，版式需要的裁切或处理另存到作品集制作包。

## 10 交付到共享目录

最终位置（本机看到的相对路径与网络下对应路径一致）：

```text
ForDesignPortfolio/
  TheLanternKeeper_Portfolio_2026-11-15_v1.pdf
  Source/
    TheLanternKeeper_Portfolio_2026-11-15_v1/
      项目原生文件与可交换文件
      Links/
      Fonts_or_Licenses/
  Previews/
    TheLanternKeeper_Portfolio_2026-11-15_v1/
      page-01.png ... page-05.png
  _work/
    临时裁图和试排
```

上述日期是本次交接日期；实际制作日不同时使用实际日期。新修改用 v2/v3 另存，先比较共享最新文件修改时间，不能覆盖用户修改版。正式 PDF 直接放 ForDesignPortfolio 根目录，方便用户找到；检查图、源包和临时文件放各自子目录。

制作端同时更新 `ForAgent/PORTFOLIO_PRODUCTION_STATUS.md`（首次实施时创建）：完成了哪些页面、工具与版本、源文件/最终 PDF 路径、图片来源/视频时间码、字体/链接检查、导出验证结果、未解决项和下一步。不要为每次尝试新建一份根目录交接文档；历史过程在同一状态文件追加，顶部写当前状态。

## 11 最终检查与事实边界

1. PDF 必须是 4 或 5 个独立页面，顺序明确；不把两页合并跨页后误算页数。检查页面尺寸、图片比例、字体嵌入、缺字、溢出文字、低分辨率、裁掉人物/字幕和空白页。
2. 导出后逐页渲染并查看 PNG，检查原尺寸和缩览效果。需要修正则修改原生页稿后重新导出；打印质量与文件大小优先遵从院校要求，没有要求则交付清晰可屏幕阅读的 PDF 并记录大小。
3. 学生个人工作、用户指导、AI 辅助和 Unity 实施职责目前未有一份已确认的归属表。可以陈述项目采用的流程，不替学生写“独立完成全部美术/程序”等第一人称结论。注明 AI 辅助概念探索、选图与 Photoshop 清理/拆层、Unity 接入等实际链路；个人署名和职责据用户后续信息填写。
4. 未做用户研究、访谈、量化测试、实际玩家评价和学校评分，不编造数据或引语。“用户认可录像整体效果”属于开发反馈，不包装为玩家测试成果。
5. 图像生成结果、第三方民俗参考和本项目成品区别标记。只展示有来源记录的迭代；第三方参考如要放进公开作品集，说明来源与许可/引用方式，不把它们称作自绘成果。不要将未经核对的历史三螺旋纹方案当当前设计系统。
6. EXE/Pages 若尚未交付，则只称为待发布；有真实回报再补测试过的链接或二维码。二维码的目的地址必须真的可访问。

## 12 资料索引与暂停点

当前流程与范围：ForAgent/Design/DEMO_IMPLEMENTATION_PLAN.md。全部文件路径相对共享根目录，当前原件已迁入 ForAgent；不要继续找旧根目录版本。故事完整版：ForAgent/Design/STORY_BIBLE.md。美术当前约束：TechnicalArt/HANDPAINTED_SPEC.md 与 HOME_ART_KNOWLEDGE_BASE.md。选图理由：TechArtAsset/Storyboard/STORYBOARD_SELECTION.md。实施事实：TechnicalArt/MENU_UNITY_PROGRESS.md 最新条目。作品集素材清单以本说明为首轮入口，详细来源再查 ART_ref/ASSETS.md 与 ForAgent/Design/ART_PROMPTS.md；旧资产表中的“未接入”可能是历史状态，应与最新进度交叉核对。

本地已准备资料与工作方式，未制作作品集 PDF、未调用另一台电脑的 InDesign/Vectorcraft，也未向那边 Codex 发送消息。用户将在另一台电脑手动让 Codex 读取本文件并开始制作。作品集设计电脑负责页面制作，Unity 工作站负责游戏小修与构建；两者通过共享目录读取彼此最新回报。
