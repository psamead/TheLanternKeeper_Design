

## 2026-11-15 第二轮 — PickupGate / StoryAudio / Attic 已实施及实测

任务：`CommandForAgentToInitialRun/2026-11-15_Unity_PickupGate_StoryAudio_Attic.md`，基线 Unity `c7ba7f2`。本轮取代旧规则中的拾灯前探索与 E 接受立即隐藏提示。当前 Home 背景、EndCard 位置和手绘源图保持。

- 状态层及真实入口同时要求 HasLantern + StoryACompleted；拾灯前实际多次走过两区、按 E 均保持未探索。A 内不预存；自然、Esc、单页快进统一在门边站稳返回，阶段仍为零。多 Player 碰撞体、乱序、按住 E 跨解锁、同帧只进一阶段、回菜单新局重置均通过。
- A4 原因确认：旧 fadeBackAtEnd 先重新揭开 A Canvas，回调才关闭。现在黑幕下清除全部 A 图层/提示并摆放玩家，再揭开 Home；没有删 A4 正常页。检查录像连续 92 帧（末尾 A4 约 2 秒 + Home 前 1 秒），未见无字幕 A4 再出现、旧提示或多余层。调试去字幕捕获已关闭。
- `ReturnAfterStoryA=(-4.7,-3.2,0)`，在原灯位探索 x[-3.6,-2.4] 外。碰撞体脚底按实际 Ground 支撑求解，清零速度/跳跃缓冲，黑幕内同步物理及 Cinemachine。首个 Home 可见样本根节点 (-4.7000,-3.1958)，Grounded=True，控制仍锁定；持灯与朝向保留。
- 首铃完整播放期间两条固定字持续；铃声结束切 Memory，再 .5 秒渐隐。两个旧探索 Collider/组件退出并清占用/订阅。梯子 renderer 全显且 tutorialExited 后才启独立梯区；占区等待、多碰撞体不需退出重入，最多传送一次。后续 E 不复活教学。
- 原阁楼地板 x[2.2,3.4] 存在空洞，已改为连续支撑 x[1.8,10.2]、表面 y=2.725；左右墙/屋顶均为 Ground，两层共用。落点锚点 (4.7,2.725)，首个阁楼可见样本根节点 (4.7000,2.7288)，Grounded=True，控制锁定。逐帧揭幕无可见下坠；真实持续跑、跳、贴左梯口和右边界、切层均未掉回楼下。独立边界测试临时禁用窗口根物件；正常录像窗口始终有效并进入 B。阁楼构图单向锁定。
- 故意把运行时落点移至无支撑处：实际 transition 保持 alpha=1 + ControlsLocked=True，玩家留楼下，并明确报错；未按超时揭幕。该测试运行态已丢弃。
- A/B 逐页配置已写入 StoryboardData.audioCue；取消整段 A duck 和 B5 Stop。ArMorDu 同声源/采样位置连续承接，无新 BGM。共享 `TechArtAsset/Audio/Storyboard/` 已归档独立 wave-only / wind-only 源程序、WAV、OGG、参数 README；风分轨没有 wave/foam helper。原 Home ambience 含远处混合元素，不把它称作纯风。

| 段落 | 音乐 | 环境 | 淡变/停止 | 实测 |
|---|---:|---|---|---|
| A1 | .25→.60 | Home interior .18 | 1 s | 页状态/增益通过 |
| A2 | .60 | Home interior .18 | 1 s | 通过 |
| A3 | .38 | 独立 Waves v1 .55 | 1 s | 通过 |
| A4/跳过目标 | .38 | 无故事浪 | 1 s 后 wave source Stop | 观测 isPlaying=False |
| Home | .26 | Interior .50 | 1 s 恢复 | 通过；首次铃声沿用既有 duck |
| B1–B4 | .60 | 独立 Wind v1 .40 | 1 s | 各页观测通过 |
| B5 自然/跳过 | .60 | Wind .40 | 保持至退出场景 | 两路径均通过，单 music voice |

证据：`ForDesignScreenshot/2026-11-15_Home_Pickup_Story_Attic/after/`。
- `PickupStory_ContinuousRoute.mp4`：自然 Menu/P → 拾灯前 Home → T/A → 门边 → 两步探索 → 完整铃声/渐字 → 阁楼运动/切层 → 窗口 → 自然 B5 停留。Time.timeScale=1，无加速、剪切或改速；133.666633 秒 / 4010 帧，1920×1080 H.264 30 fps，AAC 双声道 48 kHz，121478915 bytes。完整解码成功，音频 mean -21.9 dB、peak -5.2 dB。
- SHA256 本地/共享一致：`064DCF205B7D4BEBBA9A16B47463FA4EA77000D0FF2E73ED4D8C509E50BADA7F`。本地 fallback 视频已删除；本任务 `_CodexCaptures` 无剩余捕获文件。
- `FRAME_REVIEW.md`、`edge_cases_checks.txt`、`continuous_route_checks.txt`、`_work/frame_audit.csv`（1801 连续帧）、`_work/audio_cue_observations.txt`、逐帧 PNG/索引及临时测试源码已归档。独立最终 PNG 均 1920×1080。Assets 测试驱动已移除。
- 成功跑测无新产品编译错误/非预期运行错误。Console 留有一次已修正测试夹具异常（切层重新启用了测试禁用的窗 Collider）与一次故意触发的无支撑落点错误；不宣称 Console 历史记录为空。
- 限制：注入 Unity Input System 事件，不是物理键鼠或独立构建验证。未实际监听扬声器，非静音/音量正确不能称混音音质通过；用户仍需听音和最终位置/美术确认。
- Unity 本地详细记录：`Docs/2026-11-15_Pickup_Story_Attic.md`，同步 PROJECT_HANDOFF / MENU_UNITY_HANDOFF。只定向提交本任务，保留无关 TMP/字体、EndCard 场景、Packages 改动。

Final Editor verification: Edit Mode, not compiling, exactly one clean `00_StartMenu`, zero runtime Player/GameState objects, temporary test scripts absent. Editor 已回到只开 00_StartMenu。

Publication verified: Unity commit `a8030500baab20c7870cfe0dd79d87d28847df65` pushed to `origin/main`; local HEAD equals remote refs/heads/main. Only the 31 task files were committed; the seven pre-existing TMP/font/EndCard/Packages files remain local. Editor 已回到只开 00_StartMenu。
