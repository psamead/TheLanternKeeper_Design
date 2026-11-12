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

**存放规则（11-11）**：Codex 的所有输出直接放 `YYYY-MM-DD_主题/`，中间文件放其中的 `_work/`；写不进来时先放 Unity 根目录 `_CodexCaptures/` 再拷过来。`_codex_capture/` 不再使用。用户标注图命名 `user_note_HHMM_说明.png`（本地时间）。

注：2026-11-07 之前的任务说明和 deprecated 进度记录里写的是旧的平铺路径，文件现在在对应日期文件夹里。
