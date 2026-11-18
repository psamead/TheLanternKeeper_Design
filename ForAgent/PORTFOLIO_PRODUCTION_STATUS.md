# 守灯人作品集制作状态

## 最新用户反馈 2026-11-18

2026-11-18 用户反馈：网络另一台机器上的 Codex 已跑过 Unity，暂未发现问题；作品集制作端 Codex 也已跑过，暂未发现问题。来源为用户本次转述，本地未重新运行。此反馈作为继续工作的可用基线；未指定 EXE/Web、具体提交、测试路线或作品集软件兼容性，不扩写为所有平台及所有细节最终验收。

后续接手与资料维护注意事项见 [资料与经验索引](PROJECT_ARCHIVE_AND_LEARNING.md)。下方保留先前制作和验证记录；其中待审阅说明应结合本次反馈阅读，不自动重开旧任务。

当前状态：2026-11-15 v1 已完成并导出，5 页 A3 横版英文作品集；可编辑制作包、逐页预览、原视频副本已回存共享。待用户审阅版式与文案。Unity 后续发布反馈已收到：网页版已通过浏览器路线，Windows EXE 只验证启动；这些发布验证晚于本 PDF 导出，v1 本身不据此声称实机发布验收。没有修改游戏、原始 PSD/PSB 或共享原图。

## 2026-11-15 首轮制作

用户在阅读交接后授权制作，补充要求：短故事简介；角色、环境/故事版、配件与道具的图文介绍；游戏结构图；机制、碰撞触发、角色控制与页面/章节跳转代码；沿用游戏品牌气质、字体与颜色。

### 页面

1. 故事与概览：正式标题图、无字宣传主视觉、短故事、核心机制、原录屏入口。
2. 角色与道具：Maela 游戏侧面底稿与侧背造型、Soazig 概念、铜灯、完整梯、箱子；左右持灯迭代与拆层适配说明。
3. 环境与故事版：Home/Attic 原画，P2/A1/B2/B4 叙事选图与取舍说明。
4. 游戏结构：Menu → P → Home/A → B/EndCard；六步触发路线、场景承接、点击/跳过逻辑及 RequestAdvance 源码、制作链路。
5. 机制与代码：同轮现在/记忆运行图；角色移动、状态门槛、梯下淡变/阁楼窗口与菜单返回；PlayerController、GameState、EndCardController 短源码。

### 工具与路径

- 排版：DesignCraft headless 引擎，通过命令 API 直接控制；文档尺寸 1190.55 × 841.89 pt，5 个单页。
- 辅助：本机 bundled Python（运行时 bundle 26.1112.11011），Pillow 盘点/预览，PDFium 渲染最终 PDF，pypdf 核对页面、字体和链接。没有调用 Photoshop/InDesign，不声称生成 INDD。
- 正式 PDF：`ForDesignPortfolio/TheLanternKeeper_Portfolio_2026-11-15_v1.pdf`，19,792,500 bytes（约 18.88 MiB）。
- 原生：`ForDesignPortfolio/Source/TheLanternKeeper_Portfolio_2026-11-15_v1/TheLanternKeeper_Portfolio.designcraft`。
- IDML：同目录 `TheLanternKeeper_Portfolio.idml`，可供 InDesign 后续编辑；已在 DesignCraft 重新打开检查，未在 Adobe InDesign 实测。
- 所用图像副本、游戏 OFL 字体/许可、8 份只读源码快照、原视频副本、图片来源/哈希清单、文本提取和验证 JSON 均在该 Source 版本目录。
- 预览：`ForDesignPortfolio/Previews/TheLanternKeeper_Portfolio_2026-11-15_v1/page-01.png` 至 `page-05.png`，另有 overview.jpg。
- 实际共享根目录：`\\haoxi-surfacep\Administrator\Documents\MyFlie\AsArtPortfolioTeaching\Game_York\SharedWorkFolder`。

### 图片与录像来源

- 全部图像读共享原件、复制到制作包 Links；详细源路径、尺寸与 SHA256 见 `asset_manifest.json`。
- 机制对照采用 `ForDesignScreenshot/2026-11-15_Home_FirstBell_Exploration/after/05_route_both_fixed_hints.png` 与 `06_route_memory_ladder.png`；同轮、近似相同镜头，未使用 11-13 错版背景。
- 结构页 Home/EndCard 来自 `2026-11-15_Home_Pickup_Story_Attic/after/03_fixed_hints.png` 与 `05_endcard_dwell.png`；菜单明确标记为设计 mockup。
- 录像：用户原片 `user_recording_0546_14_full_demo.mp4`，141,897,246 bytes，约 184 秒。仅复制到 Media，未取帧，因此没有新截图时间码或裁切记录；不要求重录。
- 宣传图、源角色/环境、故事版插图与运行图分别标明；没有手工合成人物冒充实机，没有把 B5 码头称为可玩地图。

### 字体、链接与导出验证

- Cinzel Regular、EB Garamond Regular 从本制作包 Document Fonts 读取，OFL 许可随包。代码用本机 Courier New，PDF 已嵌入；不复制 Windows 字体文件，跨非 Windows 编辑需本机具备该字体或另行替换。
- 色彩延续 #1E2633 / #4A5A6E / #E8B45A / #F2EBDD，现有标题图保留白鼬尾纹与装饰系统。
- 所用 20 个图像链接状态正常；截图约 255 PPI，封面约 230 PPI。采用屏幕阅读用途，不宣称所有素材 300 PPI 印刷级。
- 修复 3 处技术说明溢出，最终原生与 IDML 重开均为 0 overset、0 缺字体；IDML 128 个可编辑文本 story，5 页。
- PDF 实际核验 5 个 A3 横版独立页、三种字体全部嵌入、25 个内部章节链接、5 个书签及 1 个相对视频链接。视频目标确实存在；浏览器 PDF 阅读器可能限制本地视频链接，Source README 提供直接打开说明。
- 最终 PDF 已用 PDFium 逐页渲染，5 页均逐页目视核对：未见缺字、比例失真、文字裁断、空白页或覆盖。导出无 warnings。详细结果见 `export_validation.json`。

### 事实边界与后续

- 不填未确认的学生姓名、课程、个人职责；未把项目协作链路写成学生独立完成声明。结构页注明 AI 辅助概念、选图/Photoshop 清理、拆层与 Unity 接入。
- 截至 PDF 导出时，没有编造用户研究、玩家测试、学校评分、上线 URL 或二维码；之后发布的网页地址另记于本节下方。
- 截至 PDF 导出时，Unity 进度尚未附新构建验收；源代码存在不等同 EXE/Web 实跑完成。v1 不宣称新发布完成，后续验收单独记录于下方。
- 下一步是用户审阅首版；有真实院校规范、署名/职责信息、后续验证截图或公开试玩地址后，另存 v2 更新，不覆盖 v1。

## 2026-11-15 Unity 发布反馈（作品集导出之后）

- Unity `main` 已推送至 `a469e412e5867ac488aac5558f17682c4c582ffd`；本次游戏构建源为 `6adac6ca9d5532c9f646defca38c94255e55070c`。
- 已发布并实际浏览器验证的网页 Demo：<https://psamead.github.io/TheLanternKeeper2D/>。报告称自然菜单至 B5、阁楼操作、EndCard 两种返回、重开和刷新路线通过。
- Windows x64 完整包已交付，EXE 启动成功；Windows 游戏内路线、EndCard 和视觉仍因窗口捕获失败而未验证。
- 详细证据：`ForDesignScreenshot/2026-11-15_AtticBaseline_EndCard_Release/after/Release_Report.md`。用户的最终视觉/音频验收仍待完成。
- 首版 PDF 不回改历史文本或页面；后续 v2 可在用户审阅且确认署名、学校规范后，纳入网页地址和这轮新实机截图。
