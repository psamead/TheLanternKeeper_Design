# 2026-11-11 Unity — Prologue caption layout v3 (small nudge, P2 + P3)

Follow-up to `2026-11-11_Unity_Prologue_CaptionLayout.md` (Unity `044cc81`, all PASS). User reviewed the v2 captures and wants two boxes nudged. Markup: `ForDesignScreenshot/2026-11-11_Prologue_FinalArt/user_note_1411_caption_P2_v2.png`, `user_note_1414_caption_P3_v2.png`.

Same rules as before: normalized screen coords (0,0 bottom-left), measured at the end of the Ken Burns move; **every glyph inside the box**; lines as many as needed; if still overflowing vertically, reduce that frame's font size (≤ 15 %).

| Frame | Old box | **New box** xMin–xMax / yMin–yMax | What changes |
|---|---|---|---|
| P2 | 0.54–0.72 / 0.32–0.69 | **0.54–0.71 / 0.48–0.67** | text moves **up** into the upper half of the fog gap (box is shorter → may need smaller font) |
| P3 | 0.56–0.80 / 0.63–0.85 | **0.50–0.72 / 0.64–0.80** | text moves **left** (away from the right edge), a bit lower |
| P1, P4 | unchanged | unchanged | — |

## Steps
0. Read everything from the LAN share `SharedWorkFolder` (path in AGENTS.md) — GitHub only if the share is unreachable, and then log a "GitHub fallback" note (reason, files, GitHub commit hash) per AGENTS.md.
1. Update P2/P3 caption rects in `SB_Prologue.asset`; keep underlay sized to the text.
2. Re-run the `textBounds` check; report box, text bounds, line count, and font size per frame (PASS/FAIL).
3. Screenshots `P2_caption_v3.png`, `P3_caption_v3.png` → `ForDesignScreenshot/2026-11-11_Prologue_FinalArt/`.
4. Commit "Prologue caption layout v3 (P2/P3 nudge)", push, note in `TechnicalArt/MENU_UNITY_PROGRESS.md`.
5. Then continue with `CommandForAgentToInitialRun/2026-11-11_Unity_Home_Crate_v1.md` (separate commit). Do not skip it; that file holds the crate steps.
