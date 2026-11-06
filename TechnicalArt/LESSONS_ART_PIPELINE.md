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
- 运行时才计算位置的 UI（选中图标、下划线）在编辑模式会错位：加 `OnValidate` + `EditorApplication.delayCall` 做编辑器预览，按运行时同一套规则摆放。
- Codex 改别的场景时会留下“未保存”的场景，**做完让用户在 Unity 里 Ctrl+S 后再提交**。
- **编辑器里不要叠加打开场景**：Codex 为改别的场景用 additive 打开后没关，Play 时两个场景一起跑——另一个场景的字压在菜单上，Console 刷“2 audio listeners / 2 event systems”。Hierarchy 里只留当前场景。
- 悬停音不要用 `PlayOneShot` 叠播：单独一个 AudioSource，新的一响先快速淡掉旧的再从头播。
- 空占位场景会全黑，看起来像出错：留一行小占位字 + 调色板深蓝背景。
- 程序合成的提示音太“电子”，与民俗主题不符：**菜单音效要用海风、海浪、木头 / 黄铜等自然声**。

## 5. 音频

- Higgsfield 免费账户没有积分，也没有可单独使用的音乐 / 音效模型（sonilo、mirelo 只限它自己的游戏管线）。**菜单级的自然声可以直接用代码合成**：海浪 = 低 / 中 / 高三段滤波噪声分别包络（涌起 → 拍碎 → 泡沫回退）；海风 = 粉噪声过慢慢游移的共振带通；黄铜灯笼 = 非谐泛音（成对微失谐出拍音）；木头 = 短衰减模态 + 敲击噪声。
- 悬停音要短（约 1 秒以内）、压掉 4 kHz 以上的嘶声，并做 2–3 个变体轮换，否则快速切换会糊、会腻。
- **UI 悬停音要“起音即最响”**：带涌起过程的浪声（0.1–0.3 s 才到峰值）在快速划动时听起来慢一拍；改成 5–10 ms 达峰——噪声做的浪随机起伏，要在开头加一个确定的短冲击（~10 ms 衰减）并让它始终最响。切换时旧声几乎立刻切（约 15 ms 防爆音），玩家停下才让它放完；停留超过约 1 s 才进入“轻拍循环”，移出即停（只对鼠标，键盘不循环）。
- 确认后切场景别等确认音放完：音乐 0.5 s 淡出就切，确认音放在 DontDestroyOnLoad 的临时物体上，余音带进下一场景。
- 循环素材：多渲染几秒，把超出循环点的尾巴（混响等）叠回开头，接缝无咔哒。
- 菜单动效可以全用代码生成：雾 = FFT 噪声（天然左右可平铺）+ 阈值 + 上下渐隐；灯笼光 = 径向渐变，**边缘用 smoothstep 淡到 0**，否则会看到圆边。先渲染 MP4 预览给用户确认，再进 Unity。
- **雾贴图上下边缘必须 alpha = 0**：高斯渐隐只到 4–9/255，暗背景上仍是一条硬边。再乘一个 smoothstep 窗口（外 18 % 收到 0），Unity 里 Wrap U = Repeat、**V = Clamp**（V 也 Repeat 时会采样到另一头）。
- 呼吸光要“看得出来”：亮度 30–100 %、大小 86–110 %、约 3 s 一次；55–85 % 太含蓄。
- BGM 和环境声分成两个文件，Unity 里各自调音量。

## 6. 协作与 GitHub

- 让学生的 Agent 知道进度：把设计文件夹做成**公开仓库**（`psamead/TheLanternKeeper_Design`），学生只 `git pull`。只由一个人推送——Word / Excel 是二进制，多人同改会冲突且无法合并。
- 公开前先查：第三方参考图（别人的作品、网上找的纹样图）、带电脑名的局域网路径、个人邮箱。提交作者用 `<用户名>@users.noreply.github.com`。
- `deprecated/` 也上传：人查起来能看到视觉演变（上传前把里面的局域网路径等去掉）；`.psd/.psb` 不进 Git。截图另放 `ForDesignScreenshot/`。
- 设备上的 Linux 环境没有 GitHub 凭据：Claude 在本地 init / commit，用户在 Windows 上 `git push`（在网页建仓库时不要勾选自动 README，否则推送被拒）。
- 在国内推 GitHub 报 `Connection was reset` / 超时：给 git 设代理（`git config --global http.proxy http://192.168.1.41:10808`，即 Windows 系统代理地址）；大文件推送中途断开时再加 `http.postBuffer 524288000` 并用 `git -c http.version=HTTP/1.1 push`。注意：断开后仍可能显示 "Everything up-to-date"，要用 `git ls-remote origin main` 核对远端。
- GitHub README 没有切换按钮：英文 `README.md` 放前面，中文 `README.zh-CN.md`，顶部互链 `English | 简体中文`。

## 7. 文件管理

- 被取代的版本和过程图按日期放 `deprecated/art_日期/`（`previews/`、`poster_process/` 子文件夹）。
- 合成用的分层素材留在 `TechArtAsset/Poster/_work/`；MJ / AI Studio 原图改名放 `ART_ref/`（如 `MENU_SRC_*`）。

## 8. 角色（Maela，2026-11-05 ~ 07）

- **Midjourney 侧面**：转身图一张出“侧面 + 背面”会被 cref 拉回正面；**一张只出一个人**，侧面用 `--cw 40` + `--no front view, three-quarter view, looking at viewer`，再 Vary (Subtle) 挑最侧的脸。背面可从“正 + 背”图里裁。
- **挂了 cref 也要写全服装颜色**：C01-G 没写颜色 → 靴子变棕、内裙变红、灯不亮。
- **游戏尺寸下细节只有 1–2 px**（Maela 160 px 高）：清理只管剪影、主色、去边、关节不露缝；头发前后层、被挡部分、褶皱细节不值得精修。
- **AI 图抠图要去边**：浅色背景抠出来的轮廓带一圈亮边，在深色夜景上很显眼（角色越小越显眼）。做法：轮廓 7 px 内的低饱和高亮像素去掉 → alpha 收 2 px → 边缘颜色用内部颜色 inpaint。
- **灯笼玻璃里的“白斑”其实是抠穿的透明孔**：白底上看不出，深底上变成灰洞。发光物体内部要整体填实 alpha。
- **拆部件**：手臂按袖子外轮廓整只切（沿袖子上缘），不要斜穿袖子；袖子描边要跟着袖子走，否则手臂动时身体上留下旧描边；拿走袖子后在身体层补底色。提环这类细线贴着别的部件时，按线条走向手工给多边形，不要用形态学“粗细”自动判断（会把贴着袖口的铜丝一起切走）。
- **Photoshop 可以由 Claude 直接操作**（adobe-desktop / COM）：代码出部件 PNG → JSX 导入成图层、导出 .psb。PhotoCraft 无法连接。
- **Unity 切图**：2× 源文件 PPU = 200；Codex 用 Transform 层级做剪纸式骨骼（每张 Sprite 只跟一个关节）最稳，Skinning Editor 不好用脚本驱动。
- **AI 的“侧面”常带一点 3/4**：远眼从鼻梁后露出一点，缩到 160 px 就像两只眼睛叠在一起。游戏版侧脸要把远眼、远眉涂成肤色（只用脸上的肤色填，别让自动填补取到头发）。
- **改图后 Unity 里部件错位（11-07 实际教训）**：PSD Importer 按每层像素外框裁 Sprite；v1.1 去边时“收 alpha”、v1.2 改远眼和补缝，都改了图层外框 → Unity 里全部错位。“每层整张画布 + 对位脚本”的补救更糟（Sprite 全丢），已放弃并回滚到 v1。**规则：角色进 Unity 后，改图只改颜色和图层内部；不收边、不扩边、不删边缘像素。改完先在 Photoshop 里逐层核对外框与上一版一致，再交给 Unity。** 必须改外框时，请 Codex 同步重摆该部件。
- 去边的安全做法：透明度一点不动，只把轮廓带（半透明像素 + 6 px 内发白的像素）的颜色换成内部颜色。
