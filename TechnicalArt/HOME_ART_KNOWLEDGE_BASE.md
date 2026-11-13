# Home 美术知识库与交接补充

更新：2026-11-13。读者：Psamead、设计 Agent、Unity Agent。本文记录本轮已确认的选择与待办；同名 Word 是给人阅读的同步版本。与早期正视构图、工具或版本说明冲突时，以本补充为准。

## 当前阶段

Unity 已完成 Home 灰盒、LanternSwitch、完整梯与断梯切换、爬梯、阁楼和窗口到 EndCard 的旧路线。2026-11-13 读取网络盘仓库 HEAD 为 b61eb3f，与 MENU_UNITY_PROGRESS 的 11-12 验证记录一致。本轮没有重新运行游戏。用户最新反馈已要求取消断梯占位与操作攀爬；旧验证只作历史基线，不代表新设计已实施。

现在进入 Home 美术接入与实机问题修正阶段。手绘绘本风格优先，房间透视可接受。用户已给出 Unity 运行反馈并授权按新交接单修改；本机尚未连接远端 Unity Codex，本轮只整理命令和资产，不能把任务写成已实施。

## 已选资产与状态

- 灯笼：TechArtAsset/Scenes/Home/Props/Lantern_v4.png，1032×1875，含透明通道。来源是 MJ 铜灯，经 Photoshop 去底和投影后生成 v3，用户又清理残留区域，临时文件 Lantern_v3_m.png 已按版本规则改为 v4。v3 保留；对应 PSD 是 v3 的源文件，不能声称已包含用户的 v4 修补。v4 是当前选用图，Unity 比例和挂点待核对。
- 阁楼：TechArtAsset/Scenes/Home/Attic/_candidates/Attic_PerspectiveRef_v3.png，2912×1632。用户选中四宫格左上图，Upscale Subtle 后在 Photoshop 手工去除背景中画死的梯子，并处理窗外灯塔灯部；修改前 v2 保留在同目录。v3 是当前选用的手绘背景候选，尚未做游戏接入验收；梯口、窗口、地面与互动位置仍需核对。
- 阁楼可编辑源：TechArtAsset/Scenes/Home/Attic/_work/Attic_PerspectiveRef_v3.psd，由用户原临时文件 `Attic_PerspectiveRef_v2_m.psd` 归档；未将 PSD 接入 Unity。
- 阁楼来源：原 job 83223836-af12-427b-ae2d-cdd704152b9a，index 0；放大 job bf19f584-cd7e-43d5-b936-2b345e8a5097。原始提示词记录于 ART_PROMPTS 的 S02-H v4。
- 完整梯：用户手工拼接、抠图的完整长梯已导出为 `TechArtAsset/Scenes/Home/Props/Ladder_Whole_v4.png`（1440×4200，透明 PNG），作为钟声事件后显示的独立梯子；不要求爬行动画；分层源 `_work/Ladder_Whole_v4.psd`，白底短梯素材 `_work/Ladder_Whole_MJ_crop_src_v1.png`。保留原手绘风格。用户最新决定不制作或显示现在层断梯；v1/v2 单体只保留历史。v4 待 Unity 核对高度、踏板间距、底部挂点与碰撞。用户在 v4 中增强主体不透明度并调整拼接处；v3 源文件、导出及预览保留历史。导出保持 PSD 原画布与像素，待实际游戏尺寸校对。
- Home_Attic_Both_v1.png 和 Lantern_v1/v2 是旧路线候选：用户反馈手绘风格不一致。保留历史，不作为本轮默认采用图。

## 楼下无梯背景更新 2026-11-13

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

先读本文件、ART_HANDOFF 第 9 节、ART_ref/ASSETS、ART_PROMPTS 和 MENU_UNITY_PROGRESS 末尾；本轮按新 Unity 执行清单继续。文档及资产已整理，Unity 实施和验收仍待执行。

下一步执行 `CommandForAgentToInitialRun/2026-11-13_Unity_Home_Review_Art_Transition_Audio.md`。导入 Home_Present_v3、Attic_PerspectiveRef_v3、Ladder_Whole_v4、Lantern_v4；解决镜头边界、W 改 T、提示重叠、故事透底、EndCard 按钮内缩；取消爬梯并实现梯下锁输入淡变到阁楼；补齐 Home/A 段音乐。原因需先复现，Singleton 已是原架构设计，不能假定它能修透底。执行者需记录证据并完整测试，明确未验证事项。

## 文档与发布范围

ART_ref/ASSETS 管文件版本；ART_PROMPTS 管实际提示词与参数；LESSONS_ART_PIPELINE 管可复用经验；根目录 `HOME_ART_RESUME.md` 是本地美术 / 设计 Codex 的对话续接入口；`CommandForAgentToInitialRun/` 只放发给 Unity 工作站 / 网络端 Codex 的可执行任务单。旧 Word v1.5 制作指南和 Prompt 集配合本次 Word 补充阅读。

本轮推送应包含灯笼 v4、阁楼 v3、楼下 Home_Present_v3 与完整梯 v4 PNG；源 PSD/PSB 保留本地。所有新图尚未接入 Unity。

## 2026-11-13 用户实机反馈后的最新决定

执行入口：`CommandForAgentToInitialRun/2026-11-13_Unity_Home_Review_Art_Transition_Audio.md`。以此取代旧 Demo 的 W 拾取、可爬梯、断梯占位物及断梯配对前置要求：拾取建议 T；现在层梯位为空并提示 Broken ladder；钟声切换后显示完整梯，进入梯下范围锁输入并淡变到阁楼，不播放攀爬。修正镜头、故事版透底、提示重叠、EndCard 按钮内部缩放并接通 Home/A 中段音乐。已归档截图并查看录屏抽帧，尚未在 Unity 实施或验证。
