# 2026-11-12 Unity — Storyboard A/B: drop in final A4 + B1, check sizes, capture every frame for caption layout

Short task. Run it **before** `2026-11-12_Unity_LanternSwitch_Ladder_Attic_Greybox.md`. The user will look at the captures and then mark caption boxes for every A/B frame.

## First: re-read `AGENTS.md`
Design files from the LAN share `SharedWorkFolder` (GitHub only as a logged "GitHub fallback"). Captures to `SharedWorkFolder/ForDesignScreenshot/2026-11-12_StoryAB_Final/`. When done, only `00_StartMenu` open — say so.

## Steps
1. Re-copy from the share over the Unity copies (same names/GUIDs): `TechArtAsset/Storyboard/LanternOrigin_A/SB_A4.png`, `TechArtAsset/Storyboard/Ending_B/SB_B1.png` (both replaced with final versions on 11-12).
2. **Size check**: your last report said the storyboard sources were 2048×1152, but every file on the share is **2208×1242** (15 % margin for Ken Burns). For every storyboard texture in Unity (P1–P4, A1–A4, B1–B5): report the source file's pixel size and the imported texture size. If any copy is not 2208×1242, re-copy the original from the share; importer Max Size 4096, NPOT = None, no downscale.
3. Captions: leave as they are (P1-default rect for A1–B4, B5 in the sky). Do not move them in this task.
4. Capture, with captions visible, **at the end of each frame's Ken Burns move** (that's where caption boxes are measured): `A1_end.png` … `A4_end.png`, `B1_end.png` … `B5_end.png` (1920×1080). Also one capture of each frame **without** the caption (hide the caption canvas): `A1_clean.png` … `B5_clean.png` — the user draws the boxes on these.
5. Record Story A and Story B with Unity Recorder: `StoryA_final.mp4`, `StoryB_final.mp4`.
6. Commit "Storyboard A4/B1 final art + size check", push, note hash and the size table in `TechnicalArt/MENU_UNITY_PROGRESS.md`. Leave only `00_StartMenu` open.
