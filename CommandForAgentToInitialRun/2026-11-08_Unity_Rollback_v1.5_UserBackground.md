# Task: Roll Maela back to v1.5 + restore the user's background framing (2026-11-08, quick & safe)

Unity project **`TheLanternKeeper2D`**. Re-read `AGENTS.md`.

## Why
1. After `f4ea2c1` (v1.6 + realign), Maela's legs/skirt are broken in Play. Cause found by Claude in `Maela.psb.meta` → `layeredSpriteImportData`: for the enlarged layers the importer updated `spritePosition` to the NEW bounds but kept the OLD `rect` width/height (e.g. Boot_L 36×45 instead of 56×48; Leg_Lower_R 23×37 instead of 25×62; Dress 65×35 instead of 65×57). So new pixels were cropped, and the realign shift then misplaced them. Your snapshot only compared transform deltas, not `sprite.rect` sizes — please add that check in future.
2. The background transform you reverted was **not accidental**: the user had set it deliberately and wants that framing back.

## Steps
1. Commit checkpoint "Before rollback to v1.5" (nothing else).
2. Maela rollback:
   - `git checkout d5f4cce -- Assets/_Project/Prefabs/Maela.prefab` (pre-realign sprite positions).
   - Replace `Assets/_Project/Art/Characters/Maela/Maela.psb` with `SharedWorkFolder/TechArtAsset/Characters/Maela/_work/fix_v1.5/Maela_v1.5_before_v1.6.psb` (**v1.5**: same bounds and layer IDs as v1.4; seams sealed, legs same colour).
   - `git checkout d5f4cce -- Assets/_Project/Art/Characters/Maela/Maela.psb.meta`, then reimport.
   - Delete `maela_realign.json` (+meta) from Assets (keep `MaelaSpriteRealign.cs`).
   - Verify: all 17 SpriteRenderers valid AND each `sprite.rect` size equals the PSB layer size (list them); no gaps in rest pose, Run, JumpUp, Fall.
3. Background (user's framing from his screenshot): `Background` position **(−1.9156, −0.8494, 0)**, scale **(0.645, 0.645, 1)** (uniform; he had 0.648/0.643/0.81). Then re-derive from `Background` SpriteRenderer.bounds: Ground top on the front of the painted floor where Maela's boots sit (check by eye), WallL/WallR at the bounds' left/right, CameraBounds / Confiner2D polygon = bounds. Pick an ortho size ≤ bounds height/2 so the camera never shows outside the painting; report it. Crate stays on the ground.
4. Keep the single-AudioListener fix from `f4ea2c1`.
5. Play Menu → Prologue → Home; walk end to end, jump on crate. Console: 0 errors/warnings from our code.
6. Commit "Rollback Maela to v1.5 (v1.6 importer rect issue); restore user background framing" and **push**. Notes + rect-size table in `TechnicalArt/MENU_UNITY_PROGRESS.md`.

## Do not
- Don't run the realign tool. Don't touch animations or importer settings.
