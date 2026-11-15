# Home 美术知识库与交接补充

更新：2026-11-15。读者：Psamead、设计 Agent、Unity Agent。本文记录当前 Home 视觉、流程决策和可复用经验；Unity 实施状态以 `MENU_UNITY_PROGRESS.md` 最新日期记录为准。较早的 11-13 快照只作历史参考。

## 当前设计决定与待执行修订 2026-11-15

- **背景**：用户已确认目前铃铛关卡使用的 Home 背景正确；较早 11-13 录像展示的是错误版本，仅供历史参考。本轮不要根据那批录像改背景或换回旧资产。
- **拾灯与探索**：未持灯时只显示 Press T。拾灯并完成/跳过故事 A 后，女孩回到门边；玩家重新靠近原灯位才记录第一步并显示固定的 Broken ladder，再新进入梯位触发区才显示固定 Press E。首次 E 必须重新按下才有效。
- **铃声与碰撞交接**：首次有效 E 后，Broken ladder 和 Press E 在铃声完整播放期间保留；铃声结束且完整梯出现后，提示渐隐并停用两个探索区，独立梯子碰撞区再接手传送。
- **阁楼**：淡入时角色已经站稳在阁楼梯口旁地板；通过真实地面与边界碰撞防止从阁楼坠回楼下，不用相机边界代替实体碰撞。
- **故事声音**：A1 音乐低到正常，A2 保持正常，A3 降低并有海浪，A4 与 A3 同音量且无海浪；B 与 EndCard 保持正常音乐并加入独立海风。
- **执行状态**：以上一轮拾灯与 A 门槛、顺序探索、铃声后提示交接、A4 收尾、逐页音频和阁楼安全在 Unity `a803050` 有实现记录。用户随后指出仍需复核/修正，follow-up 任务已准备、尚未执行。扬声器听测、物理键鼠和独立构建均不得标为通过；本轮状态见 `TechnicalArt/MENU_UNITY_PROGRESS.md` 最新条目。

完整玩家流程和音频 cue 表见 `DEMO_IMPLEMENTATION_PLAN.md` §4.1–4.3；用户图和验收录像索引见 `ForDesignScreenshot/2026-11-15_Home_Pickup_Story_Attic/README.md`。上一轮 Unity 任务已完成；新 follow-up 任务单待 Unity 工作站 Codex 执行。先读 `CommandForAgentToInitialRun/README.md`，再读最新单，不能把两轮任务混为一轮。

## 当前 Home 资产版本

- 楼下：`TechArtAsset/Scenes/Home/Present/Home_Present_v3.png`，当前背景经用户确认正确；不因本次交互修订更换。
- 灯笼：`TechArtAsset/Scenes/Home/Props/Lantern_v4.png`。
- 完整梯：`TechArtAsset/Scenes/Home/Props/Ladder_Whole_v5.png`，透明边清理版，当前作为 Unity 中的选用梯图；最终画面验收仍以用户观看为准。
- 阁楼：`TechArtAsset/Scenes/Home/Attic/_candidates/Attic_PerspectiveRef_v3.png`。

这些资产的制作/接入/最终接受是不同状态。Unity 已运行版本与尺寸、碰撞、镜头和淡变验收见 `MENU_UNITY_PROGRESS.md`，不要由共享目录中存在 PNG 推断它已经进 Unity。

## 当前阶段

Unity 已完成 Home 灰盒、LanternSwitch、完整梯与断梯切换、爬梯、阁楼和窗口到 EndCard 的旧路线。2026-11-13 读取网络盘仓库 HEAD 为 b61eb3f，与 MENU_UNITY_PROGRESS 的 11-12 验证记录一致。本轮没有重新运行游戏。用户最新反馈已要求取消断梯占位与操作攀爬；旧验证只作历史基线，不代表新设计已实施。

现在进入 Home 美术接入与实机问题修正阶段。手绘绘本风格优先，房间透视可接受。用户已给出 Unity 运行反馈并授权按新交接单修改；本机尚未连接远端 Unity Codex，本轮只整理命令和资产，不能把任务写成已实施。

## 已选资产与状态

- 灯笼：TechArtAsset/Scenes/Home/Props/Lantern_v4.png，1032×1875，含透明通道。来源是 MJ 铜灯，经 Photoshop 去底和投影后生成 v3，用户又清理残留区域，临时文件 Lantern_v3_m.png 已按版本规则改为 v4。v3 保留；对应 PSD 是 v3 的源文件，不能声称已包含用户的 v4 修补。v4 是当前选用图，Unity 比例和挂点待核对。
- 阁楼：TechArtAsset/Scenes/Home/Attic/_candidates/Attic_PerspectiveRef_v3.png，2912×1632。用户选中四宫格左上图，Upscale Subtle 后在 Photoshop 手工去除背景中画死的梯子，并处理窗外灯塔灯部；修改前 v2 保留在同目录。v3 是当前选用的手绘背景候选，尚未做游戏接入验收；梯口、窗口、地面与互动位置仍需核对。
- 阁楼可编辑源：TechArtAsset/Scenes/Home/Attic/_work/Attic_PerspectiveRef_v3.psd，由用户原临时文件 `Attic_PerspectiveRef_v2_m.psd` 归档；未将 PSD 接入 Unity。
- 阁楼来源：原 job 83223836-af12-427b-ae2d-cdd704152b9a，index 0；放大 job bf19f584-cd7e-43d5-b936-2b345e8a5097。原始提示词记录于 ART_PROMPTS 的 S02-H v4。
- **完整梯（当前导入版本 v5）**：`TechArtAsset/Scenes/Home/Props/Ladder_Whole_v5.png`（1440×4200，透明 PNG）作为钟声后显示的独立梯子，不要求攀爬动画。Unity `a803050` 已接入并通过连续路线验证；v4 与 PSD 留作历史源。用户最终美术接受仍待确认。
- Home_Attic_Both_v1.png 和 Lantern_v1/v2 是旧路线候选：用户反馈手绘风格不一致。保留历史，不作为本轮默认采用图。

## 楼下无梯背景更新 2026-11-13（历史资产记录）

用户移除了楼下底图右侧的梯子，当前导出为 `TechArtAsset/Scenes/Home/Present/Home_Present_v3.png`（2520×1080）。源文件原名 `Home_Present_v2.psd`，因已有 v2 断梯背景，递增并归档到 `Present/_work/Home_Present_v3.psd`。原 v1 和 `Home_Present_v2_brokenLadder.png` 保留历史。

用户说明当前游戏通过同一底图加滤镜表现状态变化，触发后叠加独立完整梯，因此底图梯位应留空。本轮按此整理资产；不再把另画记忆层背景作为接入此图的前置条件。用户将触发描述为“女孩敲响钟声”，具体触发脚本和当前 Unity 的滤镜实现尚未复核；未修改游戏逻辑。新底图尚未接入 Unity。

## 经验与制作规则

1. 以用户认可的 MJ 场景和铜灯为视觉依据。蓝色阴影、黄色高光只是配色，不能代替松散笔触、柔和轮廓和手绘材质；不要因技术构图要求把画面做成平滑或矢量感。
2. 本轮继续使用 MJ 出候选。已选 Home 图来自 Niji 6；旧的场景一律用 V7 不是本轮硬规则。灯笼原图采用 sw 15，阁楼采用 sw 60。参数要与实际 job 绑定，不保证同参数必然得到统一风格。
3. 用户接受房间透视。地面可玩性、碰撞与镜头适配交给 Unity 校对；不因透视本身否决图片。梯子当前是剧情传送道具，不做攀爬和断梯状态。
4. 单体道具先核对风格和透明边缘；若剧情变更使断梯配对失去用途，及时停掉配对制作。本轮用户已明确现在层留空。
5. Photoshop 抠图需检查外轮廓、提环内孔、支架空隙及落地投影；在明暗底色上查看边缘。本次只核对了 v4 尺寸和透明通道，最终边缘由用户清理，尚未做 Unity 验收。
6. 选图后先 Upscale Subtle，再从对应结果页下载。记录原 job、index、放大 job、尺寸、文件路径和用户选择理由。下载文件名的 0_N 不能替代画面确认。按钮超时后先查页面任务，避免重复放大。
7. 直接 CDN 下载可能遇到 TLS 或访问失败；本轮通过已登录网页的下载按钮成功保存原图。截图和缩略图不能充当放大原图。
8. 用户的 _m 是临时修订标记；按对象_vN.png 递增版本且保留原版。源文件放 _work，背景未验收候选放 _candidates，可用的道具导出放 Props。资产生成、用户采用、Unity 接入与验证分别记录。

## 下一次对话如何继续

先读本文件顶部当前决定、`ART_HANDOFF.md` 第 9 节、`ART_ref/ASSETS.md`、`ART_PROMPTS.md` 和 `TechnicalArt/MENU_UNITY_PROGRESS.md` 最新条目。上一轮 `a803050` 已有 Editor 验证，但用户复核后建立了新的 follow-up。下一轮先读 Command README 与新任务单；不重跑旧单。背景经用户确认正确，不根据历史错版视频调整。旧版本资产/Unity 状态仍保留在下文作为追溯记录。

## 文档与发布范围

ART_ref/ASSETS 管文件版本；ART_PROMPTS 管实际提示词与参数；LESSONS_ART_PIPELINE 管可复用经验；根目录 `HOME_ART_RESUME.md` 是本地美术 / 设计 Codex 的对话续接入口；`CommandForAgentToInitialRun/` 只放发给 Unity 工作站 / 网络端 Codex 的可执行任务单。旧 Word v1.5 制作指南和 Prompt 集配合本次 Word 补充阅读。

当时计划推送灯笼 v4、阁楼 v3、楼下 Home_Present_v3 与完整梯 v4 PNG；源 PSD/PSB 保留本地。以上是 11-13 历史记录。当前接入与验证以本文件开头和 MENU_UNITY_PROGRESS 最新条目为准。

## 2026-11-13 用户实机反馈后的最新决定

执行入口：`CommandForAgentToInitialRun/2026-11-13_Unity_Home_Review_Art_Transition_Audio.md`。以此取代旧 Demo 的 W 拾取、可爬梯、断梯占位物及断梯配对前置要求：拾取建议 T；现在层梯位为空并提示 Broken ladder；钟声切换后显示完整梯，进入梯下范围锁输入并淡变到阁楼，不播放攀爬。修正镜头、故事版透底、提示重叠、EndCard 按钮内部缩放并接通 Home/A 中段音乐。已归档截图并查看录屏抽帧，尚未在 Unity 实施或验证。
