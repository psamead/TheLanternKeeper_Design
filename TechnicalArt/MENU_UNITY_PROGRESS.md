# Unity 开始菜单进度记录

更新时间：2026-11-03

## 已完成

- 已将项目根目录 `AGENTS.md` 与共享 `UNITY_AGENTS.md` 的共享路径占位符替换为实际 UNC 路径。
- 确认仓库已有 Unity `.gitignore` 规则。
- 本地提交 `7d8ffdf Before start menu v1` 已推送；通过 `git ls-remote` 确认远端 `main` 指向该提交。
- 在目标 Unity 6000.3.24f1 Editor 中创建了 `01_StartMenu`、`02_Home`、`03_Harbor`、`04_EndCard`，并按该顺序加入 Build Settings；原 `SampleScene` 保持原样且不在 Build Settings 中。
- 创建了菜单 Canvas、背景/压暗/标题、Play / Settings / Quit 按钮、灯笼选择图标和下划线、设置占位面板，以及三个场景占位文字和 Esc 返回菜单组件。
- 菜单贴图与图标导入设置已核对为 Sprite、Bilinear、Mip Maps 关闭、Uncompressed。
- 菜单脚本已由目标 Editor 导入并编译，相关 Console 错误查询为空。

## 当前阻塞与验证状态

- 2026-11-03：用户已通过 Unity Editor 导入 TMP Essentials；确认 Liberation Sans SDF、EmojiOne、Default Style Sheet 及默认 TMP 字体均可加载。
- 已生成可用的动态 Cinzel SDF（`Assets/_Project/Fonts/Cinzel SDF Generated.asset`），图集和材质有效；75 个常用英文字符可用，六个 TMP 标签均已绑定此字体。
- 首次 Play Mode 截图显示背景为黑色。检查发现 `BG` 与 `LeftDark` 的全屏 RectTransform 纵向锚点反转，导致高度为 -1080；已改为标准全屏拉伸锚点并保存。修正后 1920×1080 Game View 与 `MENU_v1_mock.png` 的布局和视觉构图相符。
- Play Mode 的编辑器输入/事件检查通过：Down 选中 Settings、Enter 打开设置面板、Pointer Enter 高亮 Settings、Play 加载 `02_Home`、模拟 Escape 经 `BackToMenu` 返回 `01_StartMenu`；Quit 在 Editor 中安全输出预期日志。未做真实硬件鼠标操作或独立 Player 构建。
- 旧的不完整 `Assets/_Project/Fonts/Cinzel SDF.asset` 仍在本地但无场景引用。MCP 删除操作被交互保护拒绝；需要从 Project 窗口手动删除后再检查差异和暂存。
- Unity Camera Preview MCP 调用因失效实例 ID 失败；通过 Play Mode `ScreenCapture.CaptureScreenshot` 成功完成 Game View 视觉核对。
- 最终提交 `6aa6dc2 Implement start menu v1` 已创建并推送；`git ls-remote origin refs/heads/main` 确认远端 main 为 `6aa6dc2e4aff159eb2f203771bff9f177edc6584`。首次 HTTP/2/TLS 推送断开，改用 HTTP/1.1 后成功。
- 提交未包含本地旧不完整字体 `Assets/_Project/Fonts/Cinzel SDF.asset`，也未包含 TMP 的 `Examples & Extras`；它们仍显示为未跟踪内容，清理/保留前先由项目所有者确认。

## 后续步骤

1. 如要清理本机，先在 Unity Project 窗口删除旧的不完整 `Assets/_Project/Fonts/Cinzel SDF.asset`（确认无场景引用）；保留 `Cinzel SDF Generated.asset` 与已提交 TMP Essentials。
2. 在 Git 状态中确认 `Assets/TextMesh Pro/Examples & Extras` 是否为有意保留的本地资源；这部分未包含在提交内。
3. 开始下一项工作前重新读取 `AGENTS.md`、当前 handoff 和对应实施范围；完整 UI 清单中的对话框仍未完成。

## 2026-11-03 — 下划线与菜单音效后续

- 按用户反馈修正选中下划线：从 TMP 实际渲染字形边界定位，放在字形下方 8 UI 单位；Play Mode 中测得字形下缘到线顶间距为 8。
- 新增 `ProceduralMenuAudio`：运行时合成短悬停提示音和确认音，通过 `MainMenuController` 上单个 2D AudioSource 播放。没有外部声音素材。
- Play Mode 中触发 Settings 的 pointer-enter 与确认回调；两次检查时 AudioSource 均处于播放状态，Settings 面板正常打开。没有真实鼠标与扬声器人工听测，也没有独立 Player 构建。
- 此次只更新 `01_StartMenu`；不改 Demo 范围或清单勾选状态。旧 Cinzel SDF 与 TMP Examples & Extras 仍是本地未跟踪资源。

## 2026-11-03 — Home 占位标签编号修正

- 按用户要求，只将 `02_Home` 场景中 `PlaceholderLabel` 的可见标题从 `02_Home` 改为 `01_Home`；保留第二行 `Esc → menu`，场景文件名仍是 `02_Home`。
- 已保存目标场景并核对 TMP 文本值。此项仅修改占位文字，不涉及场景切换或 Demo 清单状态。
- 编辑时 `01_StartMenu` 在 Unity Editor 中显示未保存状态；为保护其内存改动，未保存或覆盖该场景。详见本地 `Docs/PROJECT_HANDOFF.md`。

## 2026-11-03 — 用户试玩反馈与下一步（Claude 记录）

- 用户已在 Unity 里保存 `01_StartMenu`，删除旧 `Cinzel SDF.asset` 与 TMP `Examples & Extras`。
- **提示音太电子**，与民俗海边主题不符：`ProceduralMenuAudio` 需替换为自然声（海浪 / 海风作为悬停，轻的木头或黄铜碰响、灯笼“叮”作为确认）。
- **菜单背景音乐**还没有：用户之后制作（参考《妖精丘陵》`AUDIO_PIPELINE.md` 做法：loop OGG，Streaming / Vorbis，AudioSource Loop，音量约 0.6）。
- 顺序：**先完善开始菜单**（音效、背景音乐、可选的雾 / 灯笼呼吸光动效），再开始搭 Home / Harbor 场景。

## 2026-11-03 — 菜单音频 v1 素材就绪（Claude 记录）

- Claude 用代码合成（无采样、无第三方版权）：`BGM_Menu_Gwerz_loop`（80 s，D 多利亚 3/4、72 BPM，竖琴琶音 + 低音持续音，第二遍加木笛旋律）、`AMB_Menu_SeaWind_loop`（60 s）、`SFX_Menu_Hover_Wave_01~03`、`SFX_Menu_Confirm_Lantern`、`SFX_Menu_Back_Wood`。用户试听确认。
- 源文件（带 `_v1`）：`TechArtAsset/Audio/Menu/`；生成脚本 `TechArtAsset/Audio/Menu/_src/synth_menu_audio.py`。
- 已拷入 Unity：`Assets/_Project/Audio/Menu/`（去掉 `_v1` 后缀，未提交）。
- 待 Codex 按 `CommandForAgentToInitialRun/2026-11-03_Unity_SceneRename_MenuAudio.md` 接入：替换 `ProceduralMenuAudio`、BGM + 环境声循环与淡入淡出、Esc 返回音。

## 2026-11-03 — 场景重新编号（决定，待 Codex 执行）

- 用户决定：开始菜单单独用 00，游戏章节从 01 起，文件名与画面编号一致：`00_StartMenu`、`01_Home`、`02_Harbor`、`03_EndCard`。
- 共享文档与 Unity 根目录 `AGENTS.md` 已由 Claude 更新；Unity 内的场景重命名、Build Settings、脚本里的场景名、占位标题由 Codex 按 `CommandForAgentToInitialRun/2026-11-03_Unity_SceneRename_MenuAudio.md` Part A 完成。

## 2026-11-03 — Scene renumbering and natural menu audio (Codex)

- Renamed the four Unity scene assets while preserving their `.meta` GUIDs: `00_StartMenu`, `01_Home`, `02_Harbor`, `03_EndCard`. Build Settings lists the four enabled paths in that order. Main Menu Play targets `01_Home`; Home Escape targets `00_StartMenu`. Harbor and EndCard placeholder titles now match their scene numbers; Home remains `01_Home`.
- Replaced runtime synthesized beeps with imported OGG cues. Hover changes rotate among three clips without repeating consecutively; confirm and Settings-close back cues use their assigned clips. The menu SFX uses one 2D AudioSource.
- Added `MenuMusic` with looping BGM and sea/wind ambience on two 2D sources. Both fade in over two seconds. Play waits for the lantern confirm clip, fades music/ambience out over about one second, then loads `01_Home`.
- Import settings checked in Unity: BGM/ambience Streaming, Vorbis quality 70%, stereo, BGM background loading enabled; SFX Decompress On Load, Vorbis 70%, stereo and preloaded. Start Menu has exactly one AudioListener on Main Camera.
- Play Mode: invoked Play and observed active scene become `01_Home` after confirm/fade; queued an Input System Escape event and observed return to `00_StartMenu`. Observed both menu audio sources playing and fade volumes. Clip triggering was exercised programmatically.
- Not verified: listening through speakers/headphones, music loop point after 80 seconds, perceived balance/click-free loop, or standalone Player build. A second event-system warning appeared when both Start Menu and Home were open additively in the Editor; each scene individually has its own expected EventSystem and AudioListener.
- The Start Menu scene has been saved in Unity. The requested user save confirmation was received; audio commit `be85569` and scene renumber commit `1de8084` are pushed to GitHub `main`.


## 2026-11-03 — Remove Home placeholder overlay

- Cleared the `PlaceholderLabel` TMP text in `01_Home` at the user's request, including the `Esc → menu` helper that appeared over the Start Menu when scenes were loaded additively in the Editor. Saved the scene and verified the label text is empty and the scene is not dirty.
- The screenshot's duplicate AudioListener/EventSystem warnings were caused by both scenes being loaded additively; Start Menu and Home each have one listener/EventSystem in their own scene. Commit `7415565` was pushed to GitHub `main`.

## 2026-11-03 — Fade startup follow-up

- Set the serialized MenuMusic source volumes to zero; `MenuMusic` then fades to the specified 0.6 / 0.45 targets. The scene was saved cleanly.
- A fresh Editor probe confirmed both volumes reached their targets, but then reported `isPlaying == false` and zero output samples. The Settings Escape path closed the panel and started the SFX source. BGM/ambience audibility and sustained playback remain unverified; a focused Game view or speaker listening check is still needed. This probe does not establish whether the condition is Editor focus or runtime behavior.
## 2026-11-03 下午 — 悬停跟手、Play 过渡、Home 占位（Claude 直接改，用户已在 Editor 验证前两版）

- 编辑器里 `01_Home` 曾被叠加打开 → Play 时两场景同跑（Home 字压在菜单上、2 AudioListener / 2 EventSystem）。用户已移除；只开当前场景。
- `MenuAudio.cs`：悬停改为两个专用声道轮换；划到新选项时旧浪声约 15 ms 内切掉、新的从头播（跟随玩家速度）；不划时浪声自然放完。确认音改在 DontDestroyOnLoad 的临时物体上播放，切场景不被截断。
- 悬停浪声 v2：起音即最响（13–35 ms 达峰，v1 要 0.1–0.3 s），长约 0.75 s；v1 移到 `deprecated/audio_2026-11-03/`。Unity 内同名替换（GUID 不变）。
- `MenuMusic.cs` + `00_StartMenu`：PLAY 后不再等确认音放完（原约 3 s + 1 s 淡出），改为 0.5 s 淡出后加载 `01_Home`。
- `01_Home.unity`：恢复两行居中占位字 `01_Home` / `Esc → menu`（游戏内点 PLAY 后才出现），相机背景 #1E2633。
- 以上 Unity 改动**未提交**：提交时还原 `LiberationSans SDF - Fallback.asset`（TMP 自动写入），其余 7 个文件提交。

## 2026-11-03 傍晚 — 悬停 v3 与“停留”状态（Claude 直接改，待用户验证）

- 悬停浪声 v3：开头加 ~10 ms 的“拍石”冲击，5–6 ms 达峰（v2 为 13–35 ms），总长约 0.7 s。v2 移入 `deprecated/audio_2026-11-03/`。
- 停留状态：鼠标停在同一选项上 **1.0 s** 后，浪声以 1.4–2.2 s 随机间隔轻拍（音量 0.42，划过时 0.6）；移出选项、键盘切换、确认 / 返回时结束。参数在 `MenuAudio` Inspector（Dwell 组）可调。
- 改动文件：`MenuAudio.cs`、`MenuItemHover.cs`（加 PointerExit）、`MainMenuController.cs`（`PointerLeft`、键盘不进停留）。仍未提交（同上，Fallback 字体资源不提交）。

- 2026-11-04：用户试听通过——划过的“哒”声（v3 起音冲击）可以，海浪停留机制保留。待 Codex 按 `CommandForAgentToInitialRun/2026-11-04_Unity_Commit_MenuFeel.md` 提交。
- 2026-11-04：编辑模式下选中图标 / 下划线错位（位置只在运行时计算）→ `MainMenuController` 加 `OnValidate` 编辑器预览，按运行时规则摆放第一项；只移动现有物体，不加组件、不发声。
- 2026-11-04：菜单手感改动已提交并推送：da9a7f37de04af3eb51efd7907b89ac9053fd290。Edit Mode 截图确认 PLAY 金色选中、灯图标与下划线位置；Play Mode Console 为 0 errors，直接验证 SceneLoader 在 00_StartMenu 与 01_Home 间切换。MCP 合成 Button.onClick 未完成淡出协程；实际鼠标点击的 Play→Home 仍以用户此前的 Play Mode 验证为准。

## 2026-11-05 — 菜单动效素材就绪（Claude）

- 贴图 `Assets/_Project/Art/Menu/FX/`（Fog_A / Fog_B / LanternGlow）与脚本 `UVScroll.cs`、`LanternGlowPulse.cs` 已放入项目，未提交、未接入场景。
- 预览 `SharedWorkFolder/TechArtAsset/Menu/FX/MENU_FX_preview_v2.mp4` 经用户确认。接入见 `CommandForAgentToInitialRun/2026-11-05_Unity_MenuFX.md`。
- 2026-11-05：菜单雾气与提灯呼吸光已接入并推送：f71483008d8baace8bb608a676d77f1c55093d0f。1920×1080 Play Mode 检查确认双层 UV 运动、3.2 秒呼吸、UI hover/click 命中，Play 加载 01_Home 并返回 00_StartMenu；TMP 字体资源已还原。MCP 使用过期 Camera ID 的捕获失败在 Console 留下一条工具错误，未发现其他项目错误。
- 2026-11-05：Codex 已接入菜单动效（`f714830`）。用户发现雾层下边有硬边 → Claude 重做 Fog_A / Fog_B（上下边缘 alpha 0），`.meta` Wrap V 改 Clamp；未提交，待用户确认后提交。
- 2026-11-05：Fog A/B 贴图边缘透明度修复并推送：dd02e9be74bc149227bcf100dfe5027107f49ba7。用户确认 00_StartMenu 已保存，Play Mode 中硬边已消失；仅提交两张雾贴图及其导入设置（Wrap U Repeat、Wrap V Clamp）。
- 2026-11-05：提交并推送 Cinemachine 3.1.7 包、相机规范与 URP Main Camera 附加数据：204379b3b1a69577101727045c39e3d8f134c4cf。Unity 中仅 00_StartMenu 打开且场景干净；未创建或配置 Cinemachine 相机。
- 2026-11-06：Maela 导入、刚性 cut-out rig 与 Idle 已提交并推送：1517f472a4c56e07e1b6d0f001a52c52a65b6465（导入前检查点 1e1fd7d）。使用任务允许的 Transform 层级 fallback：Character Rig 关闭，15 个指定关节、17 张 Sprite、每张只跟随所属关节，无网格形变；两个空白左臂层按要求跳过。PPU 200，Bilinear，无 mipmap/压缩，Mosaic；原 PSB 未修改。Maela.prefab 足底为根节点 y=0，01_Home 仅保留 (0,-2) 的正常实例；3 秒 Idle、提灯旋转及随灯 Point Light 2D 已接入。为渲染预览将静态 Main Camera z 从 0 改为 -10，添加规格色 #8FA3BF / 0.8 的全局填充光和 Sprite-Lit 材质；无移动/输入/碰撞/相机跟随代码。1920×1080 Play Mode 观察到循环、身体角度与灯光强度变化，角色约 1.59–1.60 单位，正常/镜像及手臂提灯特写未见明显肩肘膝接缝；放大图中部分轮廓有浅色边缘，留给美术复核，未重绘。截图 4 张：ForDesignScreenshot/2026-11-06_Maela_Idle_{NormalAndMirrored,Normal,Mirrored,ArmLantern_Closeup}.png；截图时临时隐藏旧 PlaceholderLabel，退出后原 UI 保留。Recorder 未安装，按任务跳过可选视频。TMP 自动变化已还原；最终 Console 无 Error，之前有一条 Unity AI Account API 超时 Warning。最终仅 01_Home 打开且 clean，镜像测试对象已移除，Git clean。
- 2026-11-06：追补 Unity Recorder 录像：安装 `com.unity.recorder` 5.1.7（Unity 6000.3 兼容发行版），Play Mode 捕获 Maela Idle 5.3 秒 H.264 MP4，1920×1080、30 fps、159 帧，存于 `ForDesignScreenshot/2026-11-06_Maela_Idle_Recorder.mp4`；ffprobe 已核验格式、分辨率、帧率和时长。此安装请求未包含 commit/push，因此 Packages/manifest.json 与 packages-lock.json 保持本地修改。捕获后已回到干净的 01_Home，临时 Editor helper 已移除。

## 2026-11-07 — Maela art v1.1: defringe and lantern flame (Codex)

- Reimported the updated `Maela.psb`. Unity regenerated the sprite subasset IDs, so the prefab's 17 `SpriteRenderer` references were null; reconnected all 17 by their unchanged layer names without changing bones or pivots. The two intentionally empty left-arm layers remain omitted.
- Play Mode check: only `01_Home` loaded; all 17 sprites rendered, the 3-second Idle advanced, lantern Point Light 2D followed the lantern, and the camera rendered at 1920×1080. Console error count was zero. No obvious joint gaps in the rendered screenshot.
- Screenshot: `ForDesignScreenshot/2026-11-07_Maela_Idle_v1.1.png` (1920×1080).
- Unity commit `a6d55819e1edef04db59eb1e72d228e8fab9a559` pushed to `main`; includes PSB, Unity reimport metadata, and prefab sprite-reference updates. Recorder package edits remain uncommitted and were excluded.

## 2026-11-07 — Maela art v1.2: face and shoulder cleanup (Codex)

- Reimported the updated PSB and reconnected four missing sprite references (`Head`, `Hair_Front`, `Hair_Back`, `Coat_Body`) by unchanged layer names. Kept the existing bones and pivots.
- Play Mode: 17 sprites present; 3-second Idle advanced; only `01_Home` loaded; 1920×1080 camera; Console had zero errors. No changes to scene layout.
- Screenshots: `ForDesignScreenshot/2026-11-07_Maela_v1.2_Overview.png` and `ForDesignScreenshot/2026-11-07_Maela_v1.2_HeadCloseup_4x.png` (both 1920×1080; close-up camera zoom 4×).
- Commit `68dc87d4489a356ae770ea3c73b2a4db7eea1ae8` pushed to Unity `main`; includes PSB, Unity reimport metadata, and the four prefab sprite-reference updates. Recorder package modifications remain uncommitted.

## 2026-11-07 — Maela v1 safe colour-only art update (Codex)

- Imported the replacement v1 PSB. Unity regenerated sprite subasset IDs; reconnected all 17 existing prefab renderers by exact layer name. Preserved the v1 rig, bone transforms, and centered sprite pivots; the two intentionally empty left-arm layers remain omitted.
- Play Mode: only `01_Home` loaded; `Maela_Idle` was active; 17 renderers had valid sprite references. Main Camera output was 1920×1080. Visual check showed no doubled eye or visible shoulder gap; white edge fringe was not visible and the lantern glow was clean.
- Screenshots: `ForDesignScreenshot/2026-11-07_Maela_v1safe_Overview.png` (1920×1080) and `ForDesignScreenshot/2026-11-07_Maela_v1safe_HeadCloseup_4x.png` (4× crop from the overview).
- Unity commit `6ec559bc4dea22263eacdebe72cdf30eb5abb83c` pushed to `main`; includes PSB, Unity reimport metadata, and prefab reference updates. No scene diff was needed. Recorder package changes and `_to_delete/` were excluded.

## 2026-11-07 — Maela Run / JumpUp / Fall / Lantern animations (Codex)

- Pre-animation checkpoint: `f73794fc26b3d1d8c04f402b08f68a333669a6a6` (empty marker; existing unrelated working-tree edits were excluded).
- Built and committed `Maela_Run`, `Maela_JumpUp`, `Maela_Fall`, and `Maela_Lantern`; added Animator states and `Speed`, `Grounded`, `VelY`, `RaiseLantern` parameters. The generated `MaelaAnimBuilder.cs` is included for reproducibility. All clip curve paths resolved against the current Maela prefab hierarchy. Unity completed compilation; Console inspection found one unrelated Unity Account API timeout warning and no animation error.
- Play Mode review in `01_Home`, 1920×1080; scene remained clean. No PlayerController exists under `Assets`, so parameter wiring was skipped as instructed. Run, jump peak, fall, and lantern raised were previewed; four Run phase screenshots were also captured:
  - `ForDesignScreenshot/2026-11-07_Maela_Anim_Run_01.png` through `_04.png`
  - `ForDesignScreenshot/2026-11-07_Maela_Anim_JumpUp_Peak.png`
  - `ForDesignScreenshot/2026-11-07_Maela_Anim_Fall.png`
  - `ForDesignScreenshot/2026-11-07_Maela_Anim_Lantern_Raised.png`
- Visual follow-up: Fall reads nearly upright at game size; the Lantern pose shows a small white gap behind the right shoulder. No clear skirt/thigh gap was seen. Please address those in the animation/art source pass; the generated pose source was not hand-edited. PSB, its metadata, prefab sprite positions, and scene layout were untouched.
- Commit `1a65a73` (`Maela: Run / JumpUp / Fall / Lantern animations`) pushed to Unity `main`.

## 2026-11-07 — Maela v1.3 art + animation round 2 (Codex)

- Pre-import checkpoint `b8d50e1` (`Before Maela v1.3`) pushed before forcing the PSB reimport; the scene was already saved and clean. The v1.3 PSB and generated builder updates were kept for the final commit.
- Reimported `Maela.psb` without changing importer settings. Opened `Assets/_Project/Prefabs/Maela.prefab`: all 17 SpriteRenderers retained valid sprites and their local positions/scales; compared the overall placement with the previous committed overview. No prefab, sprite/child position, or scene edits were made.
- Ran `Tools > Lantern Keeper > Build Maela Animations`. Updated Lantern option A: no arm raise, lantern slightly forward, Light2D peaks at 2.6. `MaelaAnimBuilder.cs` was committed with the controller and clip update.
- Recorded `ForDesignScreenshot/2026-11-07_Maela_Anim_r2.mp4` in `01_Home`: idle, run right, run left, jump, fall/land, lantern. `ffprobe`: H.264 + AAC, 1920×1080, 30 fps, 306 video frames, 10.2 s. Local-to-shared SHA256 verified: `7B0B991A068407E39C8F7627DD5985DBB08959E095F441E6B471D97340C0C95F`.
- Close-up Run Scene capture: `ForDesignScreenshot/2026-11-07_Maela_Anim_r2_Run_SceneView.png` (Run sampled at 0.125 s, 410×487 px). Temporary Editor capture helper was removed. Final Editor state: only `01_Home` loaded, not playing, not compiling, scene clean.
- Unity commit `6620fad` (`Maela v1.3 art + anim round 2`) pushed to `main`; includes the v1.3 PSB, regenerated Animator controller/Lantern clip, and updated builder. Recorder package, TMP fallback, AGENTS, and `_to_delete/` changes remain excluded.
- Tool hiccups resolved during capture: Recorder helper initially used obsolete API members; fixed for the installed package. One SceneView request exceeded the supported PPU and one helper compile attempt failed before the corrected capture. No unresolved animation/importer issue remains; Unity also logged an unrelated Account API timeout warning.

## 2026-11-07 — Home playable placeholder room (Codex)

- Added the painted Home background, floor and side-wall colliders, crate, frictionless player physics, PlayerController wiring, Cinemachine follow/confiner, and the specified cool Global Light 2D. Ground top is y=-4.0. No PlayerController source changes; jump velocity is a scene override of 7.6.
- Play Mode: verified walking both directions and jumping onto/off the crate with the configured physics; checked the existing RaiseLantern Animator trigger route. Scene saved clean and Editor returned to Edit Mode.
- Recorded `ForDesignScreenshot/2026-11-07_Home_Playable.mp4` (15 s, H.264 + AAC, 1920×1080, 30 fps). Local/shared SHA256: `8E589F0C4EB00721251E77AA95DDE0A4E7CCC8BDF304C2751D193590C2BE5BB2`.
- Commit `e5edf680` (`Home: playable placeholder room + PlayerController`) pushed to Unity `main`.

## 2026-11-07 — Home camera + Prologue storyboard (Codex)

- Set the `01_Home` Cinemachine orthographic size to **3.8**; kept the existing follow, composer, and Confiner2D setup. Play Mode movement across the room and jumping onto/off the crate were exercised. The specific confiner-edge jitter check was not independently instrumented.
- Added the four-frame placeholder Prologue (`00b_Prologue`) with the specified captions, timing, Ken Burns movement, fades, keyboard/click advance, Esc skip, and transition to `01_Home`. Start Menu Play now enters the Prologue; Build Settings order is `00_StartMenu`, `00b_Prologue`, `01_Home`, `03_EndCard` (Harbor excluded).
- Play Mode: menu → Prologue, caption display and frame advance, Esc → Home were verified. A 40 s H.264 capture was reviewed at 1920×1080, 30 fps and includes the menu, Prologue frames, and playable Home. Shared video: `ForDesignScreenshot/2026-11-07_Prologue_Camera/2026-11-07_Prologue_Flow.mp4`; local/shared SHA256: `CD643D3F31212B1A43A7B4AF553EBE2B8BD6ECF0A6698D96B7AB22122F9CAECC`.
- Commits: `9ece716` (`Home: closer camera`) and `aa2dc4f` (`Prologue storyboard (placeholders) + menu → prologue → home`).

## 2026-11-07 — Home scale correction + Prologue P1 final art (Codex)

- Saved `01_Home`: Maela visual child scale 1.4; Player CapsuleCollider2D 0.63×2.1, offset (0,1.05); jumpVelocity 8 and Rigidbody2D gravityScale 1.7 for the resized crate; lantern outer radius 4.2. Background/ground/wall/confiner scale 0.8 with floor top y=-3.2 and walls at x=±10.08; crate scale 1.4; Cinemachine orthographic size 3.8. Ground check unchanged. Visual height measured about 29% of a 1920×1080 frame.
- Set Prologue P1 to `Assets/_Project/Art/Storyboard/Prologue/SB_P1.png`, matching placeholder importer settings; zoom 1→1.08, pan (0,0)→(-0.15,0.05). P2–P4 remain placeholders.
- Captured/reviewed `ForDesignScreenshot/2026-11-07_Home_Scale_P1/2026-11-07_Home_Scale_P1.mp4`: 42 s, H.264, 1920×1080; shows Start Menu → Prologue storyboard → Home. Shared SHA256: `4B386A0DD3A64B45B20DD313068918F89B6F58753261F04539D2A52220CC917B`.
- Validation limit: Unity loaded the Home scene in Play Mode and framing/ground alignment were inspected. Synthetic keyboard input did not reach the Game View in this desktop session, so controller-driven room traversal, crate jump, E trigger, and confiner-edge jitter were not confirmed; the recording does not demonstrate those interactions.
- Checkpoint `1f45a38` (`Before Home scale fix`) and final commit `cef0bf1f9fff6aa45c87d64058b4e1d3a44a2182` (`Home: Maela ×1.4, room ×0.8; prologue P1 final art`) are on `main`. TMP generated font changes and temporary ProjectSettings change were restored; pre-existing unrelated working-tree edits remain excluded.

## 2026-11-07 — Maela v1.4 legs + Console pass (Codex)

- User confirmed Unity changes were saved; checkpoint `3e026eb` (`Before Maela v1.4`) created before the PSB reimport. Reimported `Assets/_Project/Art/Characters/Maela/Maela.psb` without changing importer settings. Compared prefab and `01_Home` character snapshots before/after: all 17 SpriteRenderers remained valid and the placement snapshot hash stayed `D75FD96481A50798601B7A27A8EC74E5`; no offsets detected.
- Removed the untracked duplicate `Cormorant Garamond Italic SDF.asset` and its `.meta`; Prologue uses the separate Persistent font asset. Forced TMP mesh generation produced 49 visible caption characters.
- Cleared the stale 999+ Console entries. A fresh ~10 s `01_Home` Play Mode run reported 0 logs, 0 warnings, and 0 errors. No `SCALEP1_CRATE_CHECK` or `CRATE_JUMP_RESULT` project-source hits were found.
- Synthetic keyboard input still did not reach Game View, so walking/jump/E could not be exercised. The attempted Animator-preview screen capture stayed static; a Unity render-command retry was rejected by the bridge with `User interactions are not supported for MCP tool calls`. No valid motion video was delivered in this pass; capture remains outstanding.
- No importer setting, sprite child position, repaint, or scene edits were included in this task commit. The pre-existing `01_Home` transform diff and unrelated package/AGENTS/TMP changes remain outside it.

## 2026-11-08 — Maela v1.6 preflight stopped on missing sprite refs (Codex)

- Confirmed Unity target `Application.dataPath=C:/Users/Administrator/Documents/UnityProject/TheLanternKeeper2D/Assets`; active `01_Home` reported clean in the Editor. Checkpoint `d5f4cce` (`Before Maela v1.6`) is local. User asked to preserve the existing `01_Home` edits, so the task's scene-discard step was skipped and that scene remains untouched.
- Saved pre-force snapshot to `TechnicalArt/Maela_v1.6_prefab_snapshot_before.txt` (17 SpriteRenderers with sprite names and world-space bounds centers). It already showed 2 missing sprites: `Hand_L_Sprite` and `Boot_R_Sprite`. Forced PSD reimport with no importer setting edits; result remained 15 valid / 2 missing. Per task stop condition, did not run `Realign Maela Sprites` or edit the prefab. Restored the tracked PSB and removed the incoming realignment JSON; preserved incoming PSB/JSON copies locally at `PrologueCapture/Maela_v1.6_reverted_backup/`. A subsequent tracked-PSB import still reports those same 2 missing references; unresolved and needs review before retrying v1.6.
- Read-only Home geometry while preserving the user's current scene edit: Background center (-1.9156,-0.8494), bounds extents (8.16,3.47), CameraBounds extents (10.08,4.32), walls at x=±10.08, camera orthographic size 3.8. Background no longer matches the bounds polygon and is shorter than the 7.6-unit camera view. No Home repair or runtime navigation was performed. Edit Mode currently shows one enabled Main Camera AudioListener; menu→Prologue→Home Play Mode count/warnings were not tested because the missing-sprite stop condition ended the task.

## 2026-11-08 — Maela v1.6 repaired layer IDs and completed realignment (Codex)

- Follow-up to the earlier preflight entry: the two PSB layer IDs for `Hand_L` and `Boot_R` were corrected in the supplied v1.6 art. Captured the required prefab placement snapshot before reimport; after restoring the PSB importer metadata from Git, forced reimport without changing importer settings. All 17 SpriteRenderers were valid (0 missing).
- Ran `Tools > Lantern Keeper > Realign Maela Sprites` exactly once. Compared all eight configured sprite offsets with before/after world-bound centers; every delta matched the JSON expectation, with maximum discrepancy about 0.000003 px. Saved the post-realignment snapshot at `TechnicalArt/Maela_v1.6_prefab_snapshot_after_realign_2026-11-08.txt`. Visual review against the supplied comparison image showed the expected alignment and no displaced parts.
- `01_Home` background bounds are 20.16×8.64 units, centered at (0,0); CameraBounds and side walls align to those bounds. The Cinemachine Confiner2D references CameraBounds. Orthographic size is 3.8 (7.6-unit view height), which fits within the background. Home remained clean in the Editor.
- Play Mode route check: Start Menu Play loaded `00b_Prologue`; the standard `SceneLoader` then loaded `01_Home`. Each tested scene had exactly one enabled AudioListener on its Main Camera; no duplicate-listener warning appeared. The Prologue was not allowed to finish naturally in this check. No video was requested.
- Unity Console contained stale Unity AI MCP bridge/account warnings plus one rejected SceneView capture request with an unsupported PPU value; no project AudioListener warning was observed. This is not a claim of a globally warning-free Console.
- Editor returned to Edit Mode, not compiling, on `00_StartMenu`; `01_Home` was clean. The v1.6 PSB SHA256 is `6DB0CFB499BFAFFFFA953E5F6B6170B8C49F113D559A655D384C42E238C10256`.

## 2026-11-08 — Maela v1.5 rollback + Home framing restore (Codex)

- Empty pre-change checkpoint `8c0ce2c` (`Before rollback to v1.5`) was created without staging any pre-existing working-tree edits.
- Restored `Maela.prefab` and `Maela.psb.meta` from `d5f4cce`; replaced `Maela.psb` with shared `Maela_v1.5_before_v1.6.psb`; Unity reimported it. Removed `maela_realign.json` and its meta; kept `MaelaSpriteRealign.cs`. All 17 prefab SpriteRenderers are valid. Each prefab sprite rect matches the corresponding imported PSB layer rect:

| Layer / Sprite | Rect (px) |
|---|---:|
| Arm_Lower_R | 33 × 46 |
| Arm_Upper_R | 23 × 70 |
| Boot_L | 36 × 45 |
| Boot_R | 46 × 45 |
| Coat_Body | 138 × 91 |
| Coat_Hem | 116 × 50 |
| Dress | 65 × 35 |
| Hair_Back | 51 × 73 |
| Hair_Front | 51 × 76 |
| Hand_L | 17 × 18 |
| Hand_R | 18 × 11 |
| Head | 101 × 73 |
| Lantern | 39 × 118 |
| Leg_Lower_L | 30 × 37 |
| Leg_Lower_R | 23 × 37 |
| Leg_Upper_L | 20 × 34 |
| Leg_Upper_R | 43 × 34 |

- Rest, Run (0.25 s), JumpUp (0.15 s), and Fall (0.30 s) poses were sampled and visually reviewed; no gaps were visible.
- Restored `Background` to position (-1.9156, -0.8494, 0), scale (0.645, 0.645, 1). Its bounds are 16.254 × 6.966 units, from (-10.0426, -4.3324) to (6.2114, 2.6336). Aligned Ground top, Player bottom, and Crate bottom at y=-3.4294; walls at x=-10.0426 and x=6.2114; CameraBounds and Cinemachine Confiner2D match the background bounds. Cinemachine orthographic size is 3.45 (below the 3.483 maximum).
- Play Mode physics/input check: PlayerController moved to the right boundary and stayed grounded. The crate jump landed with Player bottom y=-1.8844 vs crate top y=-1.8894 (0.005 units). The keyboard Space edge did not register in the MCP-paused frame, so the jump arc was exercised directly with the configured Rigidbody2D velocity; walking used the PlayerController with a virtual D key.
- Invoked the Start Menu Play button; its fade did not advance while Unity's unscaled clock was stationary. Loaded `00b_Prologue` and `01_Home` through the project's `SceneLoader` while in Play Mode. This confirms both scene loads but not the live menu fade/storyboard skip input sequence. Final Editor state: Edit Mode on `01_Home`, scene clean, one enabled AudioListener.
- Console contained prior Unity AI MCP bridge warnings and a rejected capture request; no new project-code error was observed in this pass. Pre-existing AGENTS/TMP font/Recorder package edits were left untouched.
- Final commit `cd0243f` (`Rollback Maela to v1.5 and restore Home framing`) and checkpoint `8c0ce2c` were pushed to Unity `main`; verified `origin/main` at `cd0243f111ae4378cad3f9ffc3a22ccc230f3c2c`.

## 2026-11-08 — Maela v1.6 import trial + Prologue/Home audio v1 (Codex)

- Maela v1.6 path A passed: all 17 imported sprite rects matched expected sizes; prefab had no missing sprite references. Ran the Maela realign action once, visually checked Rest/Run/Jump/Fall/Lantern, and captured `ForDesignScreenshot/2026-11-08_Maela_v1.6_Import/RestPose_Magenta.png` and `Run.png`.
- Maela trial commit `cdc42a1` (`Maela v1.6 import rect fix and realign (path A)`) merged to `main` and pushed; remote ref verified.
- Added Prologue music/sea ambience and Home ambience, crossfaded Prologue audio into Home over 2 s, and added Maela footstep/jump/land/lantern one-shots. All 12 new audio import settings match the requested Streaming/DecompressOnLoad presets at Vorbis q=0.7.
- `01_Home`: Ground y=-3.5225, Crate y=-2.43, Player y=-3.20; saved screenshot `ForDesignScreenshot/2026-11-08_Home_Ground_Line/Home_Rest.png`. Main Camera and Cinemachine settings were preserved.
- Play Mode route Menu → Prologue → Home: one enabled AudioListener in each scene; Prologue music and ambience reached 0.6/0.5 and stopped on Home; Home ambience reached 0.5. Player started grounded; physics drop settled on crate at bottom y=-1.655 vs crate top y=-1.66. Run animation event played through the single Player AudioSource.
- Console review showed existing Unity AI Account/MCP warnings and one MCP camera-preview error; no project audio/listener warning was seen during the route. User should listen for balance and the 96 s loop seam, then record a full run-through with Win+Alt+R.
- Audio commit `fb1958e` (`Prologue/Home audio v1 + Maela SFX; Home ground line`) pushed to `main`; remote ref verified at `fb1958e6010cdfafa988c2a51ba7c2146c826797`.

## 2026-11-08 — Home Ground collision alignment

- In `01_Home`, `Ground` is positioned at `(-1.91, -3.5225, 0)`. `BoxCollider2D` offset remains `(0, 0)`, size `(25.2, 1)`, and Transform scale `(0.645, 0.645, 1)`.
- This gives world collision bounds X `[-10.037, 6.217]`, Y `[-3.845, -3.200]`; the top surface is Y `-3.2`. The shifted horizontal span follows the Home ground/background layout.
- `Crate` collider adjustment: position `(-1.5, -2.43, 0)`, scale `(1.4, 1.4, 1)`, `BoxCollider2D` offset `(0, -0.016816527)`, size `(1.3, 1.0663669)`. Its world bounds are X `[-2.41, -0.59]`, Y `[-3.2, -1.707086]`, so the crate collider bottom meets the Ground top at Y `-3.2`.
- Unity MCP readback confirmed the scene is clean in Edit Mode and both saved collider configurations are present. No Play Mode collision test was run for these adjustments.


## 2026-11-08 — Core_Persistent + additive Home (Codex)

- Added `Core_Persistent` as the owner of Player/Maela, Main Camera/AudioListener, Cinemachine camera and Confiner2D, Global Light 2D, EventSystem, AudioManager, GameState and LevelLoader. `01_Home` now contains only level geometry and its LevelInfo, Spawn_Start and direct-open bootstrap. Ground/Crate collision geometry was preserved.
- Flow is Menu → Prologue → Core → additive Home; Prologue audio playback state transfers to Core audio voices. Escape returns to Menu and unloads both Home and Core. Core is enabled in Build Settings; Harbor remains excluded.
- Editor Play Mode acceptance passed: 6,846 samples with exactly one enabled AudioListener and EventSystem; Home rest/floor, both wall contacts, crate jump/landing, Escape/menu teardown, and direct-open Home bootstrap. Fresh bounded project diagnostics recorded zero warnings/errors. No physical speaker listening or standalone build was performed.
- Commit `76b4163ec849b3867913f95c4391174799f47794` (`Core_Persistent + additive level loading (AudioManager, GameState, LevelLoader)`) pushed; verified remote `main` at the same hash.
- Screenshot: `ForDesignScreenshot/2026-11-08_CoreSplit/Home_Rest_after.png` (1920×1080). Temporary runtime capture settings were restored; Editor returned to Edit Mode.

## 2026-11-08 — Maela v1.6_m, Footstep v4 and Prologue caption (Codex)

- Part 2: Maela v1.6_m import check passed for all 17 expected sprite rectangles; prefab had no missing references. Applied the one supplied realignment (+3.5 px X to `Leg_Upper_L_Sprite`) and requested draw order. Magenta Rest/Run/JumpUp/Fall/Lantern captures and Play Mode state checks showed no visible boot/leg seams; five states and all sprites passed. Screenshots are in `ForDesignScreenshot/2026-11-08_Maela_v1.6m/`. Commit `1d801545a9e331c0680cdbb71e5c81e07d17ee3c` pushed.
- Part 3: Imported the four v4 footstep OGGs with v1 importer settings and changed the Core `MaelaAudio` array to v4. Unity readback matched all four references; v1 source assets remain. Commit `3ae585f30d1f58e20ff6a40369b90c5ee6a54ec6` pushed.
- Part 4: Added per-frame caption anchors/alignment/font scale and word-wrap control. P1 uses anchors `(0.51, 0.36)`–`(0.82, 0.71)`, scale 1.5 and the requested two-line text; P2–P4 retain their original caption content and default bottom-centre layout. Captured/reviewed `ForDesignScreenshot/2026-11-08_Prologue_Caption/P1.png` (1920×1080); exactly two lines appear in the sky and the navigation prompt is unchanged. Commit `d40cce5676e527286dee811960928853efb4b9d4` pushed.
- Final `origin/main` verified at `d40cce5676e527286dee811960928853efb4b9d4`. Complete ordered task commits: `28aae3e` checkpoint, `76b4163` Core/additive levels, `1d80154` Maela v1.6_m, `3ae585f` Footstep v4, `d40cce5` Prologue P1 caption.
