# 2026-11-11 Unity — Storyboard A/B: interim art + caption-free placeholders

Follow-up to `2026-11-11_Unity_Lantern_Pickup_StoryA_EndCard_B.md` (Unity `75aec35`). `git pull` the design repo first.

## Inputs (design repo, all 2208×1242)
- Interim real art: `TechArtAsset/Storyboard/LanternOrigin_A/SB_A4.png`; `TechArtAsset/Storyboard/Ending_B/SB_B1.png` … `SB_B5.png`.
- Placeholders **regenerated without caption text** (the old ones had the caption baked in → it showed twice): `TechArtAsset/Storyboard/LanternOrigin_A/placeholder/SB_A1..A3_placeholder.png`.

## Steps
1. Copy the six real images into `Assets/_Project/Art/Storyboard/LanternOrigin_A/` and `…/Ending_B/` (same names; keep the placeholder files). Re-copy the three A1–A3 placeholders over the old ones (same names/GUIDs). Import like the prologue art.
2. Point `SB_LanternOrigin_A.asset` frame A4 and `SB_Ending_B.asset` frames B1–B5 to the real sprites; A1–A3 stay on the placeholders.
3. Captions: keep the P1-default rect for now **except** B5 — put B5's caption in the open sky upper half (approx. box 0.30–0.70 / 0.70–0.88, centred), since the image leaves that space for the title line. Same inside-the-box check as the prologue (no debug log left on).
4. Play Mode once through A (after pickup) and B (EndCard). Screenshots → `ForDesignScreenshot/2026-11-11_Lantern_StoryA_EndCard/A4_interim.png`, `B1_interim.png` … `B5_interim.png`. If possible, record A and B with Unity Recorder into the same folder (they play without input).
5. **Before finishing: unload every extra scene; leave only `00_StartMenu` open** (AGENTS.md rule). Say so in the report.
6. Commit "Storyboard A/B interim art", push, note hash in `TechnicalArt/MENU_UNITY_PROGRESS.md`. Also commit the updated `AGENTS.md`.
