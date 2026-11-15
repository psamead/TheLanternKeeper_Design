# Unity 阁楼行走线与 EndCard 小修及 Windows 网页版交付

日期：2026-11-15。执行者：另一台 Unity 工作站 Codex。用户会手动让你读取本单。本地设计端已整理需求和参考图，尚未执行 Unity 改动、构建或发布。

## 1 当前入口与基线

先读 Unity 根目录 AGENTS.md、共享 CommandForAgentToInitialRun/README.md、TechnicalArt/MENU_UNITY_PROGRESS.md 最新条目，再核对实时 Git/Editor 状态。已知游戏实现基线为 a803050；122e013 只有文档链接更新。不要覆盖工作站已有的新实现或无关未提交改动。

用户最新意见是昨晚录屏版本整体效果基本满意。此单成为唯一当前执行入口，接续并覆盖 `2026-11-15_Unity_Home_StoryGate_Attic_Audio_Followup.md` 的任务入口；该旧单尚无新实施报告。旧单的持灯门槛、按序探索、A4 无重复、逐页音频、阁楼安全作为本单回归检查，已符合的结果保持，不机械重做。旧单 EndCard Quit 调用 Application.Quit 的历史验收不再适用。Home 背景已确认正确，不依据旧录像换图。

## 2 参考图与归档

全部原图见 `ForDesignScreenshot/2026-11-15_AtticBaseline_EndCard_Release/README.md`，按内容认图，不按旧录屏画面推断当前资产版本。

1. user_note_attic_green_baseline.png：阁楼地板绿线是脚底走路基线目标。
2. user_note_B5_before_options.png：B5 插图和字幕自然播放至结尾。
3. user_note_B5_options.png：B5 同画面上直接出现左侧 Back to Menu / Quit。

## 3 阁楼行走基线抬高

- 只将阁楼玩家可见靴底的站立与行走高度提高到标注绿线附近。绿线是大致水平的行走线，不要求做沿整段手绘曲线的斜坡；不把 UI 截图像素直接当世界坐标。
- 从截图的 Game viewport 内部归一化坐标确定目标，结合当前相机与角色实际靴底换算并在游戏里复核。当前图中靴底约在 Game 画面高度从上往下 92% 附近，绿线在约 85% 附近，仅作视觉估计；精确世界 Y/抬升量由当前 Editor 测量后回报。
- 实体地板顶面、传送安全落点、玩家支撑求解同步调整；根据需要调整窗边结束触发器的高度/覆盖范围及阁楼实体挡边。不要只抬 Sprite 而让碰撞脚底与画面脱离；不改 Maela PSB 或骨骼源。
- 保留安全单向阁楼路线：淡入第一帧已站稳，不能从上空掉下来，也不能从梯口/两侧坠回楼下。Present/Memory 切换都要有连续实体支撑。楼下基线、背景与相机构图沿用当前结果；只有为本次抬升必需的阁楼相关设置才调整并说明。
- 交付修改前后同构图截图、靴底/地板顶面/落点实测值，测试走、跑、跳、切层、左右边界与窗边进入 B。

## 4 B5 直接显示选项

- 故事 B 正常播放到 B5，结束时保留当前 B5 插图、字幕及最终镜头状态，直接启用现有选项组。取消“淡出到全黑 → 再显示有选项的 B5”的二次揭幕，不重新从头播放 B5、不重置缩放或产生前后跳帧。
- 只针对 B5 收尾到选项的流程；保留此前正常翻页、进入 EndCard 的过渡及故事 A 黑幕交接。自然结束、按键快进到末页、Esc 跳过均进入同一最终 B5+选项状态，不出现黑场闪回。触发下一页/跳过的同一按键不能顺带激活选项。
- 隐藏 Next/Skip 小字，保留 B5 的 Six days until Anaon night. To be continued… 字幕、音乐与独立海风连续播放。沿用已经选定的左侧按钮位置、灯笼图标、字体、下划线和命中区域。

## 5 EndCard 两个选项均返回开始菜单

- 用户明确要求这里的 Quit 也返回游戏开始菜单。保留可见英文标签 Back to Menu / Quit，两者通过统一菜单返回流程到 00_StartMenu，清理 Core/关卡运行对象和本局状态，不能只在 Editor 打日志。
- 此要求仅限 EndCard；开始菜单自己的 Quit 保留平台原有行为。
- 分别验证鼠标点击和键盘 Enter，两条返回路径后重新 Play，灯笼、记忆层与探索进度全部重置，AudioListener/EventSystem 不重复。Windows EXE 中点 EndCard Quit 后游戏进程仍在且显示开始菜单；Web 中也返回菜单，不能依赖关闭浏览器标签页。

## 6 回归路线与 Windows x64 导出

1. Editor 走完整路线：新局 → P → 未持灯只见 Press T，E 无副作用 → T/A → 门边 → 原灯区 Broken ladder → 梯位 Press E → 新按 E → 完整首铃后提示渐隐/旧区退出 → 梯区 → 已抬高且站稳的阁楼 → 窗边 → B → 无二次黑场的 B5 选项 → 任一选项回开始菜单 → 重开状态重置。
2. 沿用上一轮逐页声音：A1 渐强、A2 正常、A3 降低+海浪、A4 同 A3 音量且无浪，B/EndCard 正常音乐+海风。无听音设备则如实标未实听。
3. 从当前已修正工程构建 Windows x86_64 非 Development 可运行版。场景入口 00_StartMenu；包含 P/Core/Home/EndCard 的必需场景，Harbor 不进入 Demo。记录 Editor 版本、构建配置、BuildReport、源提交及包 SHA256。
4. 必须交付完整播放器目录和 ZIP：exe、同名 _Data、UnityPlayer.dll 以及构建实际生成的其余运行依赖，不能只交一个 exe。先在 Unity 工程 Assets 外的 Builds/ 本地构建，最终拷到 `SharedWorkFolder/DemoBuilds/2026-11-15_FinalDemo/Windows/`，ZIP 放同级；二进制目录加入适当 gitignore，不提交到设计仓库或 Unity 源码主分支。
5. 实际启动 exe（不能用 Editor 测试冒充），走路线并验证两条 EndCard 返回。记录启动、运行与日志结果；若无法完成测试，明确哪些只构建成功、哪些真实运行未验证。
6. 完成 Unity 定向提交/push，核对 origin/main 的完整 hash 与本地目标提交一致。无关 TMP/Packages/用户场景改动先识别归属，未经判断不可一并提交。若构建源与最终提交不同，补做对应版本构建或清楚记录纯文档差异。

## 7 尝试 GitHub Pages 网页试玩

用户要求在 Windows 导出与 Unity git push 后检查并尽量实现 `psamead/TheLanternKeeper2D` 的网页试玩。此步骤已授权在该仓库尝试构建和部署；本地设计端不代替工作站执行。GitHub 仓库文件页不会直接运行 exe，需另做 Unity Web 构建并发布 GitHub Pages。

- 先检查当前 Unity 6000.3.24f1 的 Web Build Support、构建工具、仓库 Pages/Actions 权限与现有站点，不升级 Editor 或重建项目。缺少模块优先用匹配版本模块；若环境/账号权限确实阻塞，完成可做部分并报告确切阻塞与需要用户的最小操作。
- 优先本地用已安装 Unity 导出 Web 成品，再通过仓库现有部署方式或 GitHub Actions 发布静态成品，避免为了云构建额外引入 Unity 许可证密钥。Windows 可运行包不上传到 Pages。
- 检查 Pages 的项目子路径、Build/TemplateData 文件相对路径、WASM/数据文件加载、大小写与缓存。压缩与服务器响应头需兼容；无法设置正确 Content-Encoding 时采用 Unity Decompression Fallback 或适当的不压缩方案，并记录实际设置。避免无需求地启用依赖跨源隔离响应头的线程配置。
- 可选 Pages artifact 工作流或单独 gh-pages 发布分支，按仓库现有方式选最小可维护方案；源码 main 保持清楚，不将大包塞入 Assets 或源码历史。遵守 Pages 发布站点大小限制，并实测 Web 文件大小；若单文件/总量受限，先用合理压缩和只保留 Demo 必需资产，无法满足时明确原因。
- 先 HTTP 本地预览，再打开真实 HTTPS Pages URL 做浏览器验收。不能用 file:// 打开来代替。检查加载完成、初次点击后的声音、键盘焦点、移动跳跃/T/E/故事翻页/Skip、阁楼新基线与 B5 无黑场、两个选项回菜单、刷新重开。至少一条从菜单到 B5 的浏览器实走路线。
- 访问链接通常形如 https://psamead.github.io/TheLanternKeeper2D/，这只是候选，必须用部署回报和实际打开结果确认；未验证前不得写“网页版已上线”。更新 Unity README 的可玩链接与 Windows 包获取说明，记录部署源 commit、Actions run/deployment URL、实际试玩 URL 和浏览器验证结果。
- Windows 交付、Unity push、Web 构建、Pages 部署、实际浏览器可玩是独立状态。网页失败不影响先交付 Windows；禁止把 Pages 返回 200 或 Actions 绿灯等同于游戏已玩通。

技术依据（2026-11-15 查询；执行时核对当前文档）：
- Unity 压缩 fallback：https://docs.unity.com/en-us/engine/6000.0/script-reference/unityeditor/playersettings/webgl/decompressionfallback
- Pages 工作流：https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- Pages 限制：https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits

## 8 证据与回报

- 新截图及至少一段带声音连续验收录像放 `ForDesignScreenshot/2026-11-15_AtticBaseline_EndCard_Release/after/`；抽帧和验证记录放同目录 `_work/`。Word/PDF 排版检查不放这里。
- Windows/Web 本地包交付到 `DemoBuilds/2026-11-15_FinalDemo/` 各自子目录；报告共享最终完整路径、ZIP/hash/大小和使用说明。共享写入失败时本地保留在工程 Assets 外并报告最终位置与复制结果。
- 更新共享 TechnicalArt/MENU_UNITY_PROGRESS.md，Unity Docs/PROJECT_HANDOFF.md 和任务相关记录；将本单逐项状态回写，区分任务已准备、Unity 已实施、Editor 验证、Windows 实跑、Web 本地实跑、Pages 已部署、真实 URL 可玩、用户已验收。
- 定向提交并推送实现和必要部署配置，核对远端提交；最后退出 Play Mode，只留一个干净 00_StartMenu，清除临时测试对象。回报“Editor 已回到只开 00_StartMenu”。

## 9 本单初始状态

设计与任务已准备；Unity 未实施；Windows 未导出；Web/Pages 未构建或部署；本轮新结果未由用户验收。
