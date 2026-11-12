# Unity Home 修正与正式美术接入 2026-11-13

这是用户本轮 8 项问题与音频补充的合并执行单。先读 Unity 项目 AGENTS.md、共享目录 HOME_ART_KNOWLEDGE_BASE 和本文件。与 11-12 的 W 拾取、实体断梯、可操作攀爬要求冲突时，以本单为准。设计源从局域网共享目录取，不能静默改用 GitHub 旧版。

本单已查看用户截图、82 秒录屏抽帧概览及旧构图参考；没有运行 Unity 或确认根因。11-12 的 b61eb3f 是旧验证记录，执行前记录实际 HEAD 和工作区状态。先复现，再修改；不得将以下假设当作已确认原因。

## 最新资产

| 用途 | 共享目录中的文件 | 规格与状态 |
|---|---|---|
| 楼下两种状态共用的无梯底图 | TechArtAsset/Scenes/Home/Present/Home_Present_v3.png | 2520×1080；替换含烘焙梯子的旧背景，冷暖由现有滤镜/灯光表现 |
| 阁楼 | TechArtAsset/Scenes/Home/Attic/_candidates/Attic_PerspectiveRef_v3.png | 2912×1632；用户已去除画中梯子并处理塔灯；需镜头适配 |
| 完整梯 | TechArtAsset/Scenes/Home/Props/Ladder_Whole_v4.png | 1440×4200；独立 Sprite，仅记忆状态显示；有少量低 alpha 背景残留，实际缩放检查并回报，不能擅改画风 |
| 灯笼 | TechArtAsset/Scenes/Home/Props/Lantern_v4.png | 1032×1875，透明；替换旧占位灯，校对持握与落地点 |

PSD 在对应 _work，Unity 只导入所列 PNG。保留用户手绘风格和原比例。楼下共用同一无梯纹理；若已有两个状态 renderer，确保都更新且不同时重叠。不要等待另画记忆背景。阁楼可保留现有同场景分区，按区域启停渲染和设置镜头；不强制拆新场景。

## 问题与验收

### 1 和 6 镜头与背景边界

现象：起始构图偏移，边缘露出大块纯色，记忆层右端/底部亦明显。对照下面旧截图恢复用户认可的站位、人物与房间关系，而非盲目套用旧数值：
`ForDesignScreenshot/2026-11-07_Home_Scale_Review/user_note_1857_good_framing_ref.png`。
另看同目录 `user_note_1952_bg_shift_camera.png`、`user_note_1953_bg_shift_right_edge.png` 及 11-12 LanternSwitch 的 present_room/memory_room。

检查 Camera viewport rect、Game View 固定分辨率与缩放、Cinemachine 镜头/跟随偏移/Confiner 缓存、背景 transform/PPU/边界、阁楼区域是否错误扩大楼下跟随范围。编辑器 0.56x 预览留白不能直接等同游戏露底，必须输出原生 1920×1080 对照。历史 3.5–3.8 正交尺寸只作调查线索，不与现有实际配置混用。

验收：出生点、左右尽头、跳跃最高点、冷暖两状态、进入阁楼均不露出画外纯色/灰盒；地板与脚底接触合理，阁楼镜头只展示阁楼；普通窗口与 1920×1080 录屏构图一致，无拉伸或强制挤压背景。

### 2 缩小提示并替换 W

默认采用 T 作为拾取/交互键，移除旧 W/Up 的拾取绑定，避免与跳跃/方向键误触；保留 E 举灯/切换世界，Space 跳跃等不相关操作。若 T 已被占用，报告冲突后用用户允许的 Z，并同步所有提示与输入文档。

提示框及字一起缩小，参照截图 2 的红框：原高度约减半，宽度随内容调整。建议 1080p 初值：字体 22–26 px、框高约 42–48 px、水平 padding 8–12 px、细线框；最终按用户标注验收而非固定数字。避免遮脸。文案 `Press T`，同风格用于 `Press E` 与状态提示。

### 3 去除断梯占位物

移除截图 2a 圈出的短梯灰盒及其碰撞/攀爬组件；使用无梯底图。现在层靠近梯位时显示小型信息 `Broken ladder`，不显示可爬/交互键。记忆层才出现正式完整梯。此决定取代旧“需要制作断梯配对”的当前 Demo 前置任务。

### 4 Slideshow 过渡透出 Home 和提示

截图 4 明确可见 Home/Press W 穿过故事版。排查两张故事图交叉淡化时总体不透明度下降、底层遮罩未覆盖、Canvas 排序、世界提示独立 Canvas、退出/进入协程时序及重复订阅。在故事模式全过程禁用世界交互与提示，使用始终完全覆盖画面的不透明底层，仅在有意进入/退出时统一淡变；切图不能漏出世界。输入从游戏转到故事模式，结束后再恢复，避免按住或同一按键穿透。

无需仅为遮挡而强制卸载 Home；如保留加载，必须不可见/不可交互。若确有重复加载则修生命周期。项目原设计已经是 Core_Persistent + GameState/AudioManager/LevelLoader 单例，先核查现状。Singleton 可防重复实例，但无法自动修复透明度、排序或残留 UI，不做无依据的全局重构。

验收：P/A/B 自然播放、快进、Esc 跳过以及进入退出的逐帧记录，均无 Home、灰盒、旧提示闪现；故事切图不跳位；正确数量的 Core/相机/AudioListener/EventSystem，重入后也一致。

### 5 提示重叠与残留

拾灯完成立刻注销/关闭拾取提示和触发源，故事 A 后只出现对应的 E 提示。建立明确的提示优先级/统一仲裁，同一时刻至多一个主交互提示；故事模式和传送模式强制隐藏。检查退出范围、拾取后、跳过故事、状态切换、回菜单重开时的订阅和协程清理。不要仅挪位置来掩盖旧提示仍在运行。

### 7 取消操作式攀爬 改为淡变到阁楼

用户确认本 Demo 不做爬梯动画/操作。停止 W/Up、S/Down 爬梯逻辑及爬梯姿态，删除不再需要的攀爬触发与顶端跳跃通关依赖。保留现有钟声机制：有灯笼才能 E；首次长钟声结束后切记忆并显示完整梯；期间锁操作；以后切换和钟声防连按按既有规则保留。

完整梯已出现且首次钟声锁结束后，玩家进入梯下范围自动触发一次淡变（建议淡出 0.35–0.5 秒，黑屏切换，再淡入 0.35–0.5 秒）。传送不增加额外按键要求。

流程：锁移动/跳跃/交互/E → 隐藏所有世界提示 → 停止速度及残留运动 → 淡出全黑 → 将玩家放到阁楼入口梯旁安全站位、更新 camera zone/confiner 并立即定位镜头 → 确认落地且目标区域已就绪 → 淡入 → 解锁。用户不需要看着角色滑上梯子或在楼板处跳跃。整个过渡无一帧可操作，淡入期间也不能提前解锁。

要防同帧重复触发、长按输入穿透、站在梯下时刚切记忆立刻与钟声锁冲突。状态失败/退出必须释放自己持有的锁，不能解除其他系统的锁。阁楼落点在回传触发之外且不挨结尾窗口；本 Demo 不新增返程玩法，若已有返程则保证不会立刻来回传送。玩家到达阁楼后走向窗口才能触发 EndCard；切回现在层仍可安全站立。

### 8 EndCard 按钮内部缩放

缩小的是整个 Back to Menu / Quit 组件：容器、按钮 RectTransform、LayoutGroup preferred/min 尺寸、字、padding、间距、导航高亮和点击区域都应一致。不能只缩外框。两按钮完整落在目标面板内，留边，不遮字幕与灯笼，点击区域与可见边界一致。以截图 8 为对照，建议先缩至原 70–75% 再按 1080p 检查。最后一帧按钮出现后移除过时的 `Any key — next / Esc — skip` 故事提示，避免逻辑冲突。

## 音乐补充

用户报告中段缺 BGM。历史任务明确 Home 只有 `Audio/Home/AMB_Home_Interior_loop_v1.ogg`，A 只压低 Home 环境声；因此先区分“原设计没配乐”和播放失败。已有 `Audio/Prologue/BGM_Prologue_ArMorDu_loop_v1.ogg`（96 秒），此前为 P/B 使用；程序合成来源在 `Audio/Prologue/_src/synth_prologue_home_audio.py`，菜单另有 `_src/synth_menu_audio.py`。

优先让已有 Ar Mor Du 以较低音量覆盖 Home/A/阁楼，P→Home、Home↔A、阁楼→B 采用平滑音量变化/交叉淡化，避免反复从头播放与意外静音；环境声继续低声存在。钟声与叙事关键声需短暂压低音乐。先核对已有 AudioManager，不加第二个相互竞争的播放器。若现有音乐不适合循环衔接，再在共享 Audio/Home/_src 用类似本地程序合成新曲，保留脚本、WAV 母版、OGG 循环版和试听，遵循版本规则；用户已允许按需制作，但不要因没接上现有音乐就重复作曲。

验收：从菜单到 B5 的带声录屏；记录各阶段 clip/isPlaying/音量/非零输出，实听确认中段有音乐，钟声清楚、无明显循环接缝、无双重播放；不能只凭 isPlaying 宣称听感通过。

## 顺序与回报

1. 记录实际 HEAD、复现录屏、旧构图与 UI 初值；导入本单四项正式图，正确映射原对象，避免保留可见灰盒。
2. 修复故事遮挡和提示生命周期、T 键绑定；修镜头边界与 EndCard 布局。
3. 取消攀爬、实现梯下淡变到阁楼；接通音乐。
4. 从唯一 00_StartMenu 启动，完整两轮并包含一次故事跳过、一次传送期间乱按键、一次回菜单重开。验证不重复加载、触发/提示/灯笼状态重置正确。
5. 在本证据文件夹下新增 `after/` 与带声音全流程录屏；对照 8 项逐条报告 PASS/FAIL/未验证、根因、修改位置、镜头参数、UI 尺寸、音乐配置以及尚存美术残留。完成有意义的编译和运行验证后提交 Unity 改动，按项目发布规则推送，回写 MENU_UNITY_PROGRESS。结束退出 Play，只保留 00_StartMenu。

## 本轮证据索引

- 问题图 1.PNG：`ForDesignScreenshot/2026-11-13_Home_Review/user_note_0032_01_camera.png`
- 问题图 2.PNG：`ForDesignScreenshot/2026-11-13_Home_Review/user_note_0034_02_prompt_size_key.png`
- 问题图 2a.PNG：`ForDesignScreenshot/2026-11-13_Home_Review/user_note_0227_03_remove_broken_placeholder.png`
- 问题图 4.PNG：`ForDesignScreenshot/2026-11-13_Home_Review/user_note_0050_04_story_world_leak.png`
- 问题图 5.PNG：`ForDesignScreenshot/2026-11-13_Home_Review/user_note_0050_05_prompt_overlap.png`
- 问题图 6.PNG：`ForDesignScreenshot/2026-11-13_Home_Review/user_note_0053_06_camera_edge.png`
- 问题图 7.PNG：`ForDesignScreenshot/2026-11-13_Home_Review/user_note_0054_07_attic_transition.png`
- 问题图 8.PNG：`ForDesignScreenshot/2026-11-13_Home_Review/user_note_0038_08_endcard_buttons.png`
- 用户完整录屏：`ForDesignScreenshot/2026-11-13 00-39-31.mp4`（82 秒；本轮已抽帧核对，精确异常时间由 Unity 复现时补记）。
