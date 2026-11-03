# 经验库：《守灯人》美术与菜单流程（2026-10-31 ~ 11-03）

> 每条都来自实际踩过的坑。以后做场景、NPC、其他项目时先查这里。格式参考《妖精丘陵》`TechnicalArt/LESSONS_SCENE_PIPELINE.md`。

## 1. 出图（Midjourney / Google AI Studio）

- **主角定稿**：第一轮挑最接近的一张做 **Vary (Subtle)**，比改 prompt 重跑稳。改 prompt（加“hood down / 冷灰背景”）反而会带来新问题（灯笼变成独立道具、出现假文字“11”）。
- **数字年龄别写进 prompt**：“11-year-old” 容易让 MJ 在图上写 “11”。
- **黄雨衣 + 戴兜帽 ≈ 知名游戏主角**：坚持兜帽放下。
- **Q 版来自 prompt**：“cute, 3 heads tall” 会出 Q 版；要正常比例写 “about 5 heads tall, normal-sized eyes”，加 `--no chibi, big eyes, blush, pastel`。
- **lighthouse 一定会画亮灯**：`--no lit lighthouse` 压不住。要熄灯：编辑时把塔顶描述成 “dark top of an old stone tower”，或交给 AI Studio 改，或后期涂暗。
- **场景里不要同时挂高权重 Style Ref + Character Ref**：会变回白底正面设定图。场景只用 Style Ref（`--sw 30` 左右），人物后期合成。
- **没挂风格参考的场景图会偏写实、偏青绿**；挂了海报作 Style Ref 后画风统一，但容易变亮、变白天，还是要后期压夜色。
- **MJ 编辑器 / 参考图上传失败（fail to upload image）**：换浏览器不一定好；直接改用 **Google AI Studio（Nano Banana 2.1）**。它的输出约 1–2K，整图编辑会变糊——**局部修改先裁 1024² 区块，改完按坐标贴回原图**（OpenCV 相位相关对齐 + 差异蒙版只贴改动处）。
- **统一画风**：AI Studio 里第一张放要改的图、第二张放风格参考（海报），写清“保持第一张构图”。记忆层暖金版也这样做，再用 SIFT 自动对齐到原图。
- **标题字不让 AI 写**：先用字体排字（程序加油墨毛边），再合成。

## 2. 风格与区分（和《妖精丘陵》）

- 基调：**奇幻为主，带一点民俗的暗与静，不走恐怖**；一句话 = 冷夜里的一盏暖灯。两个候选菜单背景里选了“石阶被照暖、像邀请往前走”的那张，而不是更陡、更压抑的那张。
- 三螺旋纹、凯尔特结纹、石刻标题牌都是《妖精丘陵》的标志，不要用作主视觉。本作民俗符号 = **白鼬尾纹（Hermine）+ 布列塔尼镂空蕾丝**（参考 `ART_ref/BRETON_*_REF_01.png`）。
- 字体五种都不与《妖精丘陵》重复（见 `守灯人_字体与UI决定.xlsx`）。

## 3. 平面设计（标题框）

- 用代码画 SVG 框（cairosvg 渲染）很适合“graphic design”式的框：改尺寸、位置、对称都快，可以逐轮按用户圈注改。
- **凹口弧要与图案同心**：圆章、蕾丝花处的边框凹口用图案的圆心和“半径 + 固定间距”计算，内外两条线各自算交点，才像四角的弧。
- 图案不能压到字：先测标题字形的最上 / 最下像素行，再定圆章和底部花饰位置。
- 整体缩放（如 90%）对“框 + 标题”合成后的整层做，绕内容中心缩。

## 4. 进 Unity（开始菜单，Codex 首跑）

- **把素材预先放进 Unity 项目**、把 `AGENTS.md` 放到项目根，Codex 不必再找共享文件夹，指令也更短。
- 项目 Active Input Handling = **新 Input System**：指令里要写明用 `UnityEngine.InputSystem` + `InputSystemUIInputModule`，否则旧 `Input` 类会报错。
- TMP 字体第一次生成可能不完整：要先导入 TMP Essentials；失败的旧 SDF 要手动删。`Examples & Extras` 不需要，删掉。
- 全屏 UI Image 背景全黑 → 检查 RectTransform 锚点是否纵向反转（高度 -1080）。
- 下划线要按 TMP 实际字形边界定位，不要按文本框。
- Codex 改别的场景时会留下“未保存”的场景，**做完让用户在 Unity 里 Ctrl+S 后再提交**。
- 程序合成的提示音太“电子”，与民俗主题不符：**菜单音效要用海风、海浪、木头 / 黄铜等自然声**。

## 5. 音频

- Higgsfield 免费账户没有积分，也没有可单独使用的音乐 / 音效模型（sonilo、mirelo 只限它自己的游戏管线）。**菜单级的自然声可以直接用代码合成**：海浪 = 低 / 中 / 高三段滤波噪声分别包络（涌起 → 拍碎 → 泡沫回退）；海风 = 粉噪声过慢慢游移的共振带通；黄铜灯笼 = 非谐泛音（成对微失谐出拍音）；木头 = 短衰减模态 + 敲击噪声。
- 悬停音要短（约 1 秒以内）、压掉 4 kHz 以上的嘶声，并做 2–3 个变体轮换，否则快速切换会糊、会腻。
- 循环素材：多渲染几秒，把超出循环点的尾巴（混响等）叠回开头，接缝无咔哒。
- BGM 和环境声分成两个文件，Unity 里各自调音量。

## 6. 协作与 GitHub

- 让学生的 Agent 知道进度：把设计文件夹做成**公开仓库**（`psamead/TheLanternKeeper_Design`），学生只 `git pull`。只由一个人推送——Word / Excel 是二进制，多人同改会冲突且无法合并。
- 公开前先查：第三方参考图（别人的作品、网上找的纹样图）、带电脑名的局域网路径、个人邮箱。提交作者用 `<用户名>@users.noreply.github.com`。
- 有 Git 历史后 `deprecated/` 不必上传；`.psd/.psb` 不进 Git。
- 设备上的 Linux 环境没有 GitHub 凭据：Claude 在本地 init / commit，用户在 Windows 上 `git push`（在网页建仓库时不要勾选自动 README，否则推送被拒）。
- GitHub README 没有切换按钮：英文 `README.md` 放前面，中文 `README.zh-CN.md`，顶部互链 `English | 简体中文`。

## 7. 文件管理

- 被取代的版本和过程图按日期放 `deprecated/art_日期/`（`previews/`、`poster_process/` 子文件夹）。
- 合成用的分层素材留在 `TechArtAsset/Poster/_work/`；MJ / AI Studio 原图改名放 `ART_ref/`（如 `MENU_SRC_*`）。
