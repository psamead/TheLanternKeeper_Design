# Task: Maela v1.3 art (gaps filled, bounds unchanged) + animation round 2 (2026-11-07)

Unity project **`TheLanternKeeper2D`**. Re-read `AGENTS.md`. Follows `2026-11-07_Unity_Maela_Run_Jump_Fall_Lantern.md`.

## Already done by Claude (not committed)
- `Assets/_Project/Art/Characters/Maela/Maela.psb` replaced with **v1.3**. Only 8 layers changed (Boot_L/R, Leg_Lower_L/R, Leg_Upper_L/R, Coat_Hem, Coat_Body), **only inside their old pixel bounds**: stray slivers made invisible, rounded knees, coat-hem notch filled, white patch on coat recoloured. Verified with a script: layer names, order and every layer bound are identical to v1. Previous file kept at `SharedWorkFolder/TechArtAsset/Characters/Maela/_work/fix_v1.3/Maela_v1_before.psb`.
- `Assets/_Project/Editor/MaelaAnimBuilder.cs` regenerated: Lantern is now **option A** (no arm raise; lantern pushed forward slightly, light flares to 2.6). Run/Jump/Fall keep the reduced amplitudes.

## Steps
1. Ask the user to save; commit "Before Maela v1.3" and push.
2. Let Unity re-import `Maela.psb` (do not change any importer setting). Then check **before anything else**: open the `Maela` prefab — every sprite must sit exactly where it did (compare with a screenshot from the last commit). If ANY part is offset, stop, revert `Maela.psb` with git, and report — do not try to fix positions.
3. Run **Tools ▸ Lantern Keeper ▸ Build Maela Animations**.
4. In `01_Home`, Game view 1920×1080: **record a video** (Unity Recorder, or Windows Game Bar Win+Alt+R if Recorder is not installed) of ~10 s: idle → run both directions → jump → fall/land → lantern. Save to `SharedWorkFolder/ForDesignScreenshot/2026-11-07_Maela_Anim_r2.mp4`. Plus one Scene-view close-up screenshot of Run with the Scene zoomed in.
5. Commit "Maela v1.3 art + anim round 2" and push; note hash + any problems in `TechnicalArt/MENU_UNITY_PROGRESS.md`.

## Do not
- No importer setting changes, no sprite/child position edits, no repainting.
