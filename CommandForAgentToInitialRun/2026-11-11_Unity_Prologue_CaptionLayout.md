# 2026-11-11 Unity — Prologue caption layout per frame (P2–P4)

User reviewed `Prologue_P1-P4_recorder.mp4`: art is fine, captions need to move into empty areas and wrap narrower.
User's markup screenshots are in `SharedWorkFolder/ForDesignScreenshot/2026-11-11_Prologue_FinalArt/` (`user_note_1225_caption_P2/P3/P4.png`).

## Target caption box per frame
Normalized **screen** coordinates (0,0 = bottom-left, 1,1 = top-right of the 16:9 Game view), measured at the **end** of the Ken Burns move. **Hard rule: the whole caption (every glyph, every line) must stay inside the box.** The "Lines" column is only an estimate — use as many lines as needed. Order of fixes if it does not fit: (1) more lines, (2) only if still overflowing vertically, reduce font size for that frame, no more than 15 %. Never let text spill outside the box.

| Frame | Box xMin–xMax | Box yMin–yMax | Lines (expected) | Align | Why |
|---|---|---|---|---|---|
| P1 | unchanged | unchanged | 2 | center | OK |
| P2 | 0.54 – 0.72 | 0.32 – 0.69 | ~4 | center | empty fog/sky between the fog mound and right house |
| P3 | 0.56 – 0.80 | 0.63 – 0.85 | ~3 | center | upper right sky (may overlap the lighthouse — user accepts) |
| P4 | 0.40 – 0.65 | 0.64 – 0.86 | ~3 | center | dark wall between Grandma and Maela; must not touch Maela's head |

## Steps
1. If the storyboard frame data has no per-frame caption rect yet, add one (e.g. `Rect captionRect` in normalized screen space) to the frame struct in `SB_Prologue.asset`'s ScriptableObject type, defaulting to the current P1 layout so P1 is unchanged. Caption RectTransform is set from it when the frame starts (anchors = rect; no per-frame code branches).
2. Fill P2–P4 values from the table. Keep the underlay (`#0B1A2E`, alpha 0.60 P2 / 0.55 P3–P4) sized to the new text block.
3. Play Mode: screenshot each frame at the end of its move → `ForDesignScreenshot/2026-11-11_Prologue_FinalArt/P2_caption_v2.png`, `P3_…`, `P4_…`. Check no caption overlaps Maela or Grandma's face. **Verify numerically**: after TMP layout, read the text's rendered bounds (`TMP_Text.textBounds` → screen space) and log PASS/FAIL per frame that all four corners are inside the box (with the Ken Burns at its end position). All PASS before commit; list the measured bounds in the progress note.
4. Commit "Prologue per-frame caption layout", push, note hash in `TechnicalArt/MENU_UNITY_PROGRESS.md`. Also commit the updated `AGENTS.md` (file-location rule, 11-11).
