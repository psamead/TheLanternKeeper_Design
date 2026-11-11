"""Writes STORYBOARD_SELECTION.xlsx (for people) and STORYBOARD_SELECTION.md (for agents) from one table."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
P=[
 ["P1","熄灭的灯塔（空镜）","C 版：MJ 塔身 + 海报灯室拼合","已定稿","灯塔必须熄灭；一步出图会亮，走两步法（K1-E1）","SB_P1.png；源 SB_P1_C_layered.psd"],
 ["P2","海雾进镇","远处雾团那张（第 4 格）","已定稿","近景屋子全黑、只有远处一扇窗亮——给玩家“那边有希望”，真走进去却不是想要的，形成反差和荒谬感（后面“远处的灯”沿用）","SB_P2.png；另一张 _candidates/SB_P2_alt_street.png"],
 ["P3","梅拉到奶奶家（背影）","v3 左上","已定稿","v2 挂 cref 全变正脸、灯塔亮；v3 去掉 cref、开头写 back view 后四张全背影、灯塔暗","SB_P3.png"],
 ["P4","奶奶认不出她","v4 第 1 张","已定稿","奶奶皱眉、像在努力认人又认不出；梅拉站在门口光里背对镜头。用户 PS 压冷（Photo Filter 偏青 50 %，脸手蒙版保暖）","SB_P4.png；SB_P4.psd；候选 _candidates/"],
 ["Soazig","奶奶概念","Vary(Subtle) 后左下那张（下载名带 upscale），用户 PS 去竿子","已定稿","表情“客气但空”、白围裙、颜色守规矩、正面完整；网和竿子当道具另画","ART_ref/SOAZIG_REF_v1.png；源 SOAZIG_SRC_v1.psd"],
]
AB=[
 ["A1","爷爷给灯笼引火","右下（下载名 0_1）","已定稿","灯型和游戏里的灯笼接近；爷爷侧脸可接受（第一次见到他）。缺塔顶大灯","SB_A1.png；左上备用 _work/SB_A1_src_alt.png"],
 ["A2","灯光守住小镇","右上","已定稿","一圈暖光把雾挡在外面，“光照到的地方，记忆属于人”一眼能懂","SB_A2.png"],
 ["A3","灯塔熄灭，雾上岸","最暗那张","要处理","四张里三张灯塔仍亮；这张灯室还有一点亮光，要 PS 涂暗或重跑","SB_A3.png 暂用"],
 ["A4","梅拉手里的灯笼亮起","右上","暂用","背影对；暖光圈太小，“屋里一角变暖”不够明显，可能重跑","SB_A4.png 暂用"],
 ["B1","阁楼窗外","右上（圆窗）","暂用","灯塔是暗的，但圆窗像船舷窗，阁楼该是方窗，可能重跑","SB_B1.png 暂用"],
 ["B2","二十年前出海","左上","已定稿","回忆感最强：暖色的“高光时刻”和后面的熄灯、失踪形成跌落感，现实与回忆反差拉大","SB_B2.png；另一张 _work/SB_B2_src_alt.png"],
 ["B3","一人跳回岸上","左上","已定稿","另两张人在半空中跳像喜剧；左上一人站在礁石上、船驶向远处，最安静","SB_B3.png"],
 ["B4","爷爷熄灯，雾中人影","左下 + 用户 PS 去塔身橘光","已定稿","只有这张塔灯暗、雾里有人影；橘色会读成“还有希望”，去掉后才是熄灯与雾中人的怨恨、遗憾、内疚（脚本自动去色失败，PS 完成）","SB_B4.png；源 _work/SB_B4_src_BL_PSfix.psd"],
 ["B5","码头尽头","右上 + 用户 PS 重摆举灯","已定稿","梅拉很小站在码头尽头、远处钟楼、上方天空放 “To be continued”；原图举灯长杆很怪，PS 改成手举提灯","SB_B5.png；源 _work/SB_B5_src_TR_PSfix.psd"],
]
H=["张","画面","选了哪张","状态","选图理由 / 问题","文件"]
wb=openpyxl.Workbook(); 
for title,rows in [("序章P与Soazig",P),("故事版A_B",AB)]:
    ws=wb.active if title=="序章P与Soazig" else wb.create_sheet(); ws.title=title
    ws.append(H); [ws.append(r) for r in rows]
    for c in ws[1]: c.font=Font(bold=True); c.fill=PatternFill("solid",fgColor="F3F3F3")
    for col,w in zip("ABCDEF",[8,18,26,9,60,40]): ws.column_dimensions[col].width=w
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment=Alignment(wrap_text=True,vertical="top")
    ws.freeze_panes="A2"
wb.save("STORYBOARD_SELECTION.xlsx")
def md(rows): return "\n".join(["| "+" | ".join(H)+" |","|"+"---|"*len(H)]+["| "+" | ".join(r)+" |" for r in rows])
open("STORYBOARD_SELECTION.md","w",encoding="utf-8").write(f"""# 故事版选图记录（P / Soazig / A / B）

> 每张图选了哪一张、为什么。给人看的版本是同目录 `STORYBOARD_SELECTION.xlsx`（同一份内容，由 `_storyboard_selection.py` 生成，改这里的表就重跑脚本）。提示词见 `ART_PROMPTS.md` §4b / §4c，过程见 `ART_HANDOFF.md` §9。在线挑选表（Claude Sheets）：「守灯人 故事版 A/B 第一轮」「守灯人 故事版补图 11-11」——以本文件为准。

## 选图原则（用户，11-08 ~ 11-12）
- **情绪落差**：回忆镜头选最暖、最“高光”的，让后面的失去有跌落感；悲剧镜头去掉多余暖色（会读成“还有希望”）。
- **远处的灯**：近处黑、远处一盏灯 = 希望在那边，但走过去不是想要的（P2 起沿用）。
- **道具一致**：灯笼选和游戏灯型接近的（A1）。
- **构图服务字幕**：留一块不太亮的大面积给两行字幕。
- 灯塔在序章和熄灭后的镜头一律不亮。

## 序章 P 与 Soazig
{md(P)}

## 故事版 A（灯笼的来历）/ B（后续引子）
{md(AB)}

更新：2026-11-12
""")
print("ok")
