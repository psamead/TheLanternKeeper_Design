# 2026-11-12 Unity — Storyboard A/B: final A4 + B1, size check, per-frame caption boxes

Short task. Run it **before** `2026-11-12_Unity_LanternSwitch_Ladder_Attic_Greybox.md`. The user has already marked where each caption should go (red boxes drawn on your previous captures, copies in `ForDesignScreenshot/2026-11-12_StoryAB_InterimArt/user_markup/user_note_0311_caption_*.png`).

## First: re-read `AGENTS.md`
Design files from the LAN share `SharedWorkFolder` (GitHub only as a logged "GitHub fallback"). Captures to `SharedWorkFolder/ForDesignScreenshot/2026-11-12_StoryAB_Final/`. When done, only `00_StartMenu` open — say so.

## Steps
1. Re-copy from the share over the Unity copies (same names/GUIDs): `TechArtAsset/Storyboard/LanternOrigin_A/SB_A4.png`, `TechArtAsset/Storyboard/Ending_B/SB_B1.png` (both replaced with final versions on 11-12).
2. **Size check**: your last report said the storyboard sources were 2048×1152, but every file on the share is **2208×1242** (15 % margin for Ken Burns). For every storyboard texture in Unity (P1–P4, A1–A4, B1–B5): report the source file's pixel size and the imported texture size. If any copy is not 2208×1242, re-copy the original from the share; importer Max Size 4096, NPOT = None, no downscale.
3. **Caption boxes** (normalized screen coords, (0,0) = bottom-left, measured at the **end** of each frame's Ken Burns move). Same rule as the prologue: **every glyph inside the box**, as many lines as needed, if it still overflows vertically reduce that frame's font size by at most 15 %. Underlay sized to the text. Measured from the user's red boxes:

| Frame | x min–max | y min–max | Note |
|---|---|---|---|
| A1 | 0.10–0.34 | 0.44–0.68 | open sea area left of the lantern |
| A2 | 0.54–0.78 | 0.65–0.76 | sky right of the lighthouse (short box — 2 lines, may need smaller font) |
| A3 | 0.45–0.64 | 0.55–0.69 | fog band in front of the houses |
| A4 | 0.20–0.39 | 0.37–0.58 | **measured on the old A4** — the image is replaced in step 1; check it lands on a calm area of the new A4 (left side, away from Maela and the lantern); if it covers her or the lantern, shift it left and report |
| B1 | 0.06–0.30 | 0.62–0.85 | **no user box yet** (B1 image changed) — proposal: dark beams upper-left, away from the window. Report how it looks; the user may adjust |
| B2 | 0.06–0.26 | 0.39–0.61 | dark left side, away from the boats |
| B3 | 0.40–0.65 | 0.46–0.60 | sea between the shore figure and the boat |
| B4 | 0.73–0.93 | 0.15–0.35 | lower right, under the lighthouse gallery |
| B5 | 0.36–0.63 | 0.75–0.88 | sky above the bell tower (replaces 0.30–0.70 / 0.70–0.88) |

   Log PASS/FAIL per frame with measured text bounds and font size (same `textBounds` check; no debug log left on afterwards).
4. Capture, with the **new** captions visible, **at the end of each frame's Ken Burns move** (that's where caption boxes are measured): `A1_end.png` … `A4_end.png`, `B1_end.png` … `B5_end.png` (1920×1080). Also one capture of each frame **without** the caption (hide the caption canvas): `A1_clean.png` … `B5_clean.png` — for any further adjustment.
5. Record Story A and Story B with Unity Recorder: `StoryA_final.mp4`, `StoryB_final.mp4`.
6. Commit "Storyboard A4/B1 final art + size check + A/B caption boxes", push, note hash and the size table in `TechnicalArt/MENU_UNITY_PROGRESS.md`. Leave only `00_StartMenu` open.
