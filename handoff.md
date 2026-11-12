<!-- 给后续开发 Agent（Codex / Claude）的交接文档。新对话先读这份。 -->

# handoff：《The Lantern Keeper》项目交接（v1.3，2026-11-08：Unity 改为 Core_Persistent + 叠加关卡，详见 UNITY_AGENTS.md）

## 1. 项目速览

- 游戏：《The Lantern Keeper》（中文工作名《守灯人》），2D 手绘横版解谜，布列塔尼海岸民俗题材。
- 项目：York（Game_York）；协作：Psamead。
- GitHub：设计仓库（本文件夹）：<https://github.com/psamead/TheLanternKeeper_Design>（公开）；Unity 仓库：<https://github.com/psamead/TheLanternKeeper2D>。学生 / 其他 Agent 只拉取（`git pull`），不改。
- 当前目标：**小体量 Demo**（2026-11-07 再缩小）：开始菜单 + 一个关卡（奶奶家与阁楼）+ 两段故事版，4–6 分钟。
- 引擎：Unity 6.3 LTS，URP 2D；平台 PC（Windows）。游戏内只用英文。
- 一句话（Demo）：梅拉在奶奶家拾起爷爷的灯笼，灯光照出“正在沉没的过去”——断掉的梯子在记忆里完好如初；她爬上阁楼，故事的后续以故事版揭开。

## 2. 阅读顺序

| 你要做什么 | 先读 |
|---|---|
| 了解故事 | `STORY_BIBLE.md` |
| 写代码 / 搭场景 | 本文件 → `DEMO_IMPLEMENTATION_PLAN.md` → `TechnicalArt/HANDPAINTED_SPEC.md` |
| 做美术 | `ART_HANDOFF.md` → `ART_PROMPTS.md` → `ART_ref/ASSETS.md` |
| 查经验 / 踩坑 | `TechnicalArt/LESSONS_ART_PIPELINE.md` |
| 做海报 / 菜单 | `ART_DIRECTION.md`；菜单进 Unity 看 `TechnicalArt/MENU_UNITY_HANDOFF.md` |
| 改设定 | `DESIGN_CHANGES.md` |
| 了解工作规则 | `AGENT_PROCESS_GUIDELINES.md` |
| 给 Unity 项目放 Codex 规则 | `UNITY_AGENTS.md`（复制到 Unity 根目录改名 `AGENTS.md`） |

## 3. 文件地图（SharedWorkFolder/）

| 位置 | 内容 |
|---|---|
| 根目录 `*.md` | Agent 用说明 |
| `story_draft/` | 故事设定 Word（v2.0） |
| `purposal_story/` | 完整版概念设计说明、Demo 制作方案 Word |
| `TechnicalArt/` | 技术美术与美术方向 Word、手绘规格、字体 |
| `ART_ref/` | 参考图、AI 出图、ASSETS.md |
| `TechArtAsset/` | 做好的游戏资产 |
| `deprecated/` | 旧版本 |

## 4. Demo 范围（摘要，以 DEMO_IMPLEMENTATION_PLAN.md 为准）

- Scene：`00_StartMenu` → `01_Home`（含故事版 A）→ `03_EndCard`（故事版 B）→ 回菜单。`02_Harbor` 保留给完整版，不进 Build Settings。
- 唯一核心机制：按 E 在现在层 / 记忆层之间全屏切换（碰撞 Tilemap 开关 + 分层美术里的标志物 Sprite 显隐 + Global Light 2D 变色）。
- 不做：灯油、检查点、敌人、潮汐、多结局、存档。

## 5. 代码结构

| 脚本 | 职责 |
|---|---|
| GameSession | Singleton + DontDestroyOnLoad；`hasLantern` |
| SceneLoader | 统一切场景（按钮、触发器调用） |
| PlayerController | 移动、跳跃、掉落重生 |
| LanternSwitch | 切换两层；事件 `OnWorldSwitched(bool isMemory)` |
| WorldLayerObject | 挂在单个物体上：Present / Memory / Both，响应切换 |
| Interactable / DialogueBox | 互动提示、对话、拾取 |
| StoryboardPlayer | 故事版 A / B：全屏插图慢推 + 字幕（数据放 ScriptableObject） |
| EndCard | 播放故事版 B、Back to Menu |

可参考 Game_zixiang 2DBattleCarArena 的 GameSession、场景切换与 UI 代码。

## 6. 约定

- 灰盒先行：用 `HANDPAINTED_SPEC.md` §7 的色块；美术到位后关闭碰撞 Tilemap 的渲染，挂上分层美术（§5 层级）。
- 文本（对话、插图文字）放 ScriptableObject，不写死在脚本里。
- Git：每完成一项提交一次；美术源文件（.psd / .psb）不进 Git，放 `TechArtAsset/`。
- 设计仓库：由 Psamead 维护。Claude 改完文档在本地提交（作者 `psamead <psamead@users.noreply.github.com>`），Psamead 在 Windows 上 `git push`。不上传：源文件、第三方参考图（见 `.gitignore`）。README 英文在前（`README.md`），中文 `README.zh-CN.md`，两份同步改。
- 完成事项后在 `DEMO_IMPLEMENTATION_PLAN.md` 第 7 节把 ☐ 改为 ☑；未在 Play Mode 验证的不要标为完成。

## 7. 当前状态（2026-11-13）

**2026-11-13 当前交接**：Home 灰盒、切层、爬梯和阁楼出口已有 Unity `b61eb3f` 的验证记录；本轮处于美术统一与接入准备。手绘风格优先，房间透视可接受。灯笼采用 `Props/Lantern_v4.png`；阁楼采用 `_candidates/Attic_PerspectiveRef_v2.png`（已 Subtle 放大下载）；梯子和记忆层房间仍待定稿。新图尚未接入 Unity。

新对话先读 [Home 美术知识库](TechnicalArt/HOME_ART_KNOWLEDGE_BASE.md) 和 [接续说明](CommandForAgentToInitialRun/2026-11-13_Home_Art_Resume.md)。给人看的同步补充为 `TechnicalArt/守灯人_Home美术交接与经验_2026-11-13_v1.docx`。本次暂停在交接完成处；下次先看用户提出的 Unity 设计问题。

### 早期状态快照（2026-11-07，供追溯）

| 部分 | 状态 |
|---|---|
| 故事 | v2.0 定稿 |
| Demo 方案 | v1.1（11-07 范围缩小） |
| 美术 | 手绘 2D；海报、开始菜单完成；Maela `.psb` + Idle 进 Unity（11-07）；下一步 Maela 动作 → Soazig → Home 底图 → 故事版 |
| Unity | `TheLanternKeeper2D`：开始菜单完成（音频、动效）；Maela 已导入（Idle）；下一步 PlayerController + 色块 Home |

## 8. 待确认

1. 字体（ART_HANDOFF §8）。
2. Home 本轮已确认继续使用 Midjourney 保持手绘风格；后处理用 Photoshop。
3. Demo 截止日期。
