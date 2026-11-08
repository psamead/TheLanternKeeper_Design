# Task: Maela v1.4 legs (art only, bounds unchanged) + console cleanup + push (2026-11-07)

Unity project **`TheLanternKeeper2D`**. Re-read `AGENTS.md`.

## Already done by Claude (not committed)
- `Assets/_Project/Art/Characters/Maela/Maela.psb` → **v1.4**. Only the 6 leg layers changed (Leg_Upper/Lower_L/R, Boot_L/R), **inside their old pixel bounds**: far (left) leg recoloured to match the near leg (slightly darker), far thigh filled out at the top, semi-transparent edges between the legs made solid, a stray boot sliver hidden. Script-verified: layer names, order and every bound identical to v1.3. Previous file: `SharedWorkFolder/TechArtAsset/Characters/Maela/_work/fix_v1.4/Maela_v1.3_before.psb`.

## Steps
1. Ask the user to save; commit "Before Maela v1.4".
2. Let Unity re-import `Maela.psb` (no importer setting changes). **First check**: open `Maela.prefab` and `01_Home` — every sprite must sit exactly where it did. If any part is offset, stop, `git checkout` the psb back and report.
3. **Console**: the Console shows 999+ errors. Clear it, enter Play Mode in `01_Home` for ~10 s, and report what the errors are (first unique messages + source). Fix them if they come from our scripts or scene setup; if they come from the Unity AI Assistant / MCP capture tools, just report and ignore. Remove any temporary debug logging left in scenes/scripts from earlier tests (e.g. `SCALEP1_CRATE_CHECK`, `CRATE_JUMP_RESULT`).
4. Delete the unused untracked `Assets/_Project/Fonts/Cormorant Garamond Italic SDF.asset` (+ .meta) — the Prologue uses `… SDF Persistent`. Confirm Prologue captions still render.
5. Visual check in `01_Home` (Game view 1920×1080): Run both directions, jump, fall, land, press E. Look at the legs: no light/dark mismatch, no thin far thigh, no background line between legs/boots.
6. Record ~15 s of Maela running back and forth + jumping → `SharedWorkFolder/ForDesignScreenshot/2026-11-07_Maela_v1.4_Legs/2026-11-07_Maela_v1.4_Legs.mp4`. If synthetic input can't reach the Game view, say so and record the Animator previewing Run/JumpUp/Fall on the scene instance instead.
7. Commit "Maela v1.4 legs; console cleanup" and **push**; note hash + findings in `TechnicalArt/MENU_UNITY_PROGRESS.md`.

## Do not
- No importer changes, no sprite child position edits, no repainting.
