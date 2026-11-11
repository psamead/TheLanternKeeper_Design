# 2026-11-11 Unity — Storyboard A/B: interim art + caption-free placeholders

Follow-up to `2026-11-11_Unity_Lantern_Pickup_StoryA_EndCard_B.md` (Unity `75aec35`). Read all design files from the LAN share `SharedWorkFolder` (path in AGENTS.md) — GitHub only if the share is unreachable, and then log a "GitHub fallback" note (reason, files, GitHub commit hash) per AGENTS.md.

## First: re-read `AGENTS.md`
It changed since your last run. New rules you must follow in this task:
1. **Design files come from the LAN share** `\\haoxi-surfacep\Administrator\Documents\MyFlie\AsArtPortfolioTeaching\Game_York\SharedWorkFolder`, not from GitHub. If the share is unreachable you may use GitHub, but log a "GitHub fallback" note (error text, files taken, GitHub commit hash) in your report and in `TechnicalArt/MENU_UNITY_PROGRESS.md`.
2. **Captures** (screenshots / recordings) go to `SharedWorkFolder/ForDesignScreenshot/YYYY-MM-DD_topic/`; if the share can't be written, use `TheLanternKeeper2D/_CodexCaptures/…` and copy over. Report full paths.
3. **Close extra scenes when done**: leave the Editor with only `00_StartMenu` open, no leftover DontDestroyOnLoad test objects, and say so in the report.

## Inputs (LAN share `SharedWorkFolder`, all 2208×1242)
- Interim real art: `TechArtAsset/Storyboard/LanternOrigin_A/SB_A1.png` … `SB_A4.png` (all four now exist); `TechArtAsset/Storyboard/Ending_B/SB_B1.png` … `SB_B5.png`.
- Placeholders **regenerated without caption text** (the old ones had the caption baked in → it showed twice): `TechArtAsset/Storyboard/LanternOrigin_A/placeholder/SB_A1..A3_placeholder.png`.

## Steps
1. Copy the nine real images into `Assets/_Project/Art/Storyboard/LanternOrigin_A/` and `…/Ending_B/` (same names; keep the placeholder files). Re-copy the three A1–A3 placeholders over the old ones (same names/GUIDs). Import like the prologue art.
2. Point all `SB_LanternOrigin_A.asset` frames A1–A4 and `SB_Ending_B.asset` frames B1–B5 to the real sprites (placeholders stay in the project, unused).
3. Captions: keep the P1-default rect for now **except** B5 — put B5's caption in the open sky upper half (approx. box 0.30–0.70 / 0.70–0.88, centred), since the image leaves that space for the title line. Same inside-the-box check as the prologue (no debug log left on).
4. Play Mode once through A (after pickup) and B (EndCard). Screenshots → `ForDesignScreenshot/2026-11-11_Lantern_StoryA_EndCard/A4_interim.png`, `B1_interim.png` … `B5_interim.png`. If possible, record A and B with Unity Recorder into the same folder (they play without input).
4b. **Speed check (user report, 11-12)**: after the previous run (Unity `75aec35`) the user saw *everything* play at roughly 2× speed (walking, animations, storyboard pacing) until they unloaded the extra scenes Codex had left open. Find and fix the cause, don't just unload:
   - In Play Mode, starting from `00_StartMenu` with **only that scene open in the Editor**, and again with `01_Home` opened directly: log `Time.timeScale`, `Time.captureFramerate`, and the count of each of `GameState`, `AudioManager`, `LevelLoader`, `StoryboardPlayer`, `PlayerController`, `Animator` on Maela, `AudioListener`, `EventSystem` (`FindObjectsByType`). Each manager / listener / player must be exactly 1.
   - Measure one storyboard frame with a stopwatch log (P1 should take its configured 6 s) and Maela's run speed (world units/s vs the configured 3.2).
   - Check for anything that can run twice when a scene is loaded additively on top of an already-open copy: duplicated `Core_Persistent`, `LevelBootstrap` creating a second persistent set, `DontDestroyOnLoad` duplicates, Recorder settings left with a fixed capture framerate, or code that multiplies by `Time.deltaTime` twice.
   - Fix it so the speed is correct **even if** a scene is already open in the Editor (guard singletons / bootstrap against duplicates). Report what the cause was, before/after numbers.
5. **Before finishing: unload every extra scene; leave only `00_StartMenu` open** (AGENTS.md rule). Say so in the report.
6. Commit "Storyboard A/B interim art", push, note hash in `TechnicalArt/MENU_UNITY_PROGRESS.md`. Also commit the updated `AGENTS.md`.
