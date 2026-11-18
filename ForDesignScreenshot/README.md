# ForDesignScreenshot

Unity / Codex 截图和录屏，以及用户标注截图。**每次任务一个子文件夹**：`YYYY-MM-DD_主题`（例 `2026-11-07_Home_Playable/`）。用户随手截的标注图命名 `user_note_HHMM.png`。

| 文件夹 | 内容 |
|---|---|
| 2026-11-03_Menu / 2026-11-04_Menu | 开始菜单阶段截图 |
| 2026-11-06_Maela_Idle | 首次导入 + Idle（正常 / 镜像 / 手臂特写 / 录屏） |
| 2026-11-07_Maela_Fixes_v1.1-v1.2 | 去边 v1.1、v1.2（已回滚）与 v1safe 对比 |
| 2026-11-07_Maela_Anim_r1 | Run / JumpUp / Fall / Lantern 第一轮 |
| 2026-11-07_Maela_Anim_r2 | v1.3 美术 + 第二轮动画录屏 |
| 2026-11-07_Home_Playable | Home 可玩场景录屏 |
| 2026-11-07_Home_Scale_P1 | 比例调整 + 序章 P1 录屏 |
| 2026-11-07_Prologue_Camera | 镜头拉近 + 序章占位录屏 |
| 2026-11-07_Home_Scale_Review | 用户标注：比例、腿部、背景偏移（`user_note_1857_good_framing_ref` = 用户认可的站位参考） |
| 2026-11-08_Maela_v1.6_Realign_Issue | v1.6 扩外框后 Unity 部件断开（导入器未重切图） |
| 2026-11-08_Home_Ground_Line | 地面线偏低 → 目标线（Ground −3.5225 / Crate −2.43 / Player −3.20） |
| 2026-11-08_Maela_WalkRun | 走 / 跑分开、靴子前后顺序（含 Maela_*_BootOrder） |
| 2026-11-08_Prologue_Caption | P1 字幕对比度；`_work/` = 旧 `_codex_capture` 的中间帧和视频 |
| 2026-11-08_user_notes | 用户 11-08 的随手截图（原 `New folder/1–9`，按本地时间改名；主题未标） |
| 2026-11-11_Prologue_FinalArt | 序章 P2–P4 正式图、Codex Recorder 录屏、字幕框标注（`user_note_1225_*`、`_1411/_1414_*_v2`）、用户录的菜单→Home（`user_note_1154_menu_to_home.mp4`）；`_work/` = Codex 中间文件 |
| 2026-11-11_Home_Crate | 箱子 v1 换上后的截图（Codex） |
| 2026-11-11_Lantern_StoryA_EndCard | 拾灯笼 → 故事版 A → EndCard B（占位版，Codex） |
| 2026-11-11_user_notes / 2026-11-12_user_notes | 用户随手截图（根目录的 1/2/3.PNG 按本地时间改名移入） |
| 2026-11-12_StoryAB_InterimArt | 故事版 A/B 暂用图 + 2 倍速修复（Codex）；`user_markup/` = 用户 03:11 画的字幕框 |
| 2026-11-12_StoryAB_Final | 定稿 A4/B1 + 尺寸核对 + A/B 字幕框（Codex）；`user_markup/` = 用户 10:30 画的字幕框 |
| 2026-11-12_Story_Polish | （Codex 下一个任务）跳页 bug、字幕加粗、Press W、序章配乐 |
| 2026-11-12_LanternSwitch | （Codex 之后的任务）灯笼切换、梯子、阁楼 |

| `2026-11-13_Prologue_UI` | 用户标注的序章底部 Next / Skip 提示，红叉标记待复核 |

**存放规则（11-11）**：Codex 的所有输出直接放 `YYYY-MM-DD_主题/`，中间文件放其中的 `_work/`；写不进来时先放 Unity 根目录 `_CodexCaptures/` 再拷过来。`_codex_capture/` 不再使用。用户标注图命名 `user_note_HHMM_说明.png`（本地时间）。

注：2026-11-07 之前的任务说明和 deprecated 进度记录里写的是旧的平铺路径，文件现在在对应日期文件夹里。

- `2026-11-13_Home_Review/`：用户 8 项反馈图、Unity 录屏及抽帧概览；修复回报放 `after/`。
- `2026-11-13_Home_Visual_Notes/`：用户 11-13 晚新增 8 张视觉反馈图；11-14 视觉修整执行单与回报见该目录 README。
- `2026-11-13_Home_User_Recordings/`：根目录两段 22:11 / 22:13 用户旧版录像，11-15 核对内容与哈希后归档，保留原始文件字节；不是新探索机制的验收。
- `2026-11-15_Home_FirstBell_Exploration/`：3 张新标注图，首次摇铃的两阶段探索、固定文字和 EndCard 移位；Unity 新验收放 `after/`。
- `2026-11-15_Home_Pickup_Story_Attic/`：本轮 12 张用户附图、85 秒原始录像，拾灯/A 前置、故事版音频/收尾、铃声后碰撞移交、阁楼安全落点；图序见目录 README，新验收放 `after/`。

当前任务入口：[Unity 任务索引](../CommandForAgentToInitialRun/README.md)。11-15 最终小修已有实施与发布报告：[发布证据](2026-11-15_AtticBaseline_EndCard_Release/after/Release_Report.md)。按既有报告，浏览器路线已通过，Windows 包已交付并验证启动；Windows 游戏内路线与用户视觉/声音验收仍待完成。本次整理未重跑测试。此前任务和证据保留历史，不作为独立待执行清单。

- `2026-11-15_Home_FullDemo_Recordings/`：用户认可整体效果的旧版全流程参考，不能替代后续修改验收。
- `2026-11-15_AtticBaseline_EndCard_Release/`：阁楼基线、B5 直接显示选项、Quit 回菜单的用户反馈与发布证据；新结果见 `after/`。

归档与查找总规则见 [资料与经验索引](../ForAgent/PROJECT_ARCHIVE_AND_LEARNING.md)。
