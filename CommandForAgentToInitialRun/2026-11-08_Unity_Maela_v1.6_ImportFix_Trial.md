# Task: Maela v1.6 import — fix cropped sprites (TRIAL on a branch) (2026-11-08)

Unity project **`TheLanternKeeper2D`**, current HEAD `cd0243f` (Maela v1.5, user framing). Re-read `AGENTS.md`. This replaces the import part of `2026-11-08_Unity_Maela_v1.6_Realign_HomeFix.md` (do NOT re-run that one).

## Why
Last time v1.6 was imported, PSD Importer updated `spritePosition` but kept the old `rect` width/height for the 8 enlarged layers → new pixels cropped, realign then made it worse (LESSONS §8 "扩外框后 Unity 不重切图"). Rule now: **acceptance = `sprite.rect` size equals PSB layer size**, not "transforms look right".

## Files Claude prepared
- PSB v1.6 (layer IDs already correct): `SharedWorkFolder/TechArtAsset/Characters/Maela/Maela.psb` (md5 f6b65581…).
- `SharedWorkFolder/TechArtAsset/Characters/Maela/_work/fix_v1.6_import/`
  - `patch_psb_meta.py` — writes new width/height + spritePosition for changed layers into `Maela.psb.meta` (keeps spriteIDs, CRLF; makes `.bak`).
  - `Maela.psb.meta.v1.6_patched` — the result of that script on the current v1.5 meta (20 lines: Hand_L, Leg_Upper_L/R, Leg_Lower_L/R, Boot_L/R, Dress).
  - `maela_expected_rects.json` — expected size of all 17 sprites.
- Unity: `Assets/_Project/Editor/MaelaSpriteRectCheck.cs` — menu **Tools ▸ Lantern Keeper ▸ Check Maela Sprite Rects** (logs ok/FAIL per sprite, missing prefab sprites, then PASS/FAIL).
- Existing: `MaelaSpriteRealign.cs` + `maela_realign.json` (centre shift per layer, v1.5 → v1.6).

## Steps (all on branch `try/maela-v1.6`; main untouched until PASS)
0. `git switch -c try/maela-v1.6`. Leave the user's uncommitted TMP/manifest/AGENTS changes alone (don't commit them).
1. Close Unity (or make sure it isn't importing). Copy into `Assets/_Project/Art/Characters/Maela/`:
   `Maela.psb` (v1.6), `Maela.psb.meta.v1.6_patched` → **as** `Maela.psb.meta`, `maela_expected_rects.json`, and `_work/fix_v1.5/maela_realign.json` → `maela_realign.json`.
2. Open Unity, let it import. Run **Check Maela Sprite Rects**.
   - **PASS** → go to 4 (path A worked).
   - FAIL on size → path B (step 3).
3. Path B (new sprites + rebind) — only if A failed:
   a. `git checkout -- Assets/_Project/Art/Characters/Maela/Maela.psb.meta`, then in the meta delete the 8 changed layers' entries from `layeredSpriteImportData` (and set their `spriteID` empty in the PSD layer list) so the importer creates fresh sprites with the correct size. Reimport.
   b. Rebind: for every SpriteRenderer in `Maela.prefab` whose sprite is missing, assign the sprite from `Maela.psb` with the same name (`<Layer>_Sprite` → `<Layer>`). Also check `.anim` files don't reference sprites (they shouldn't — animation is transforms only).
   c. Run the check → must PASS. If not, stop and report the log.
4. Run **Realign Maela Sprites** exactly once. Check: Maela prefab at rest on a **magenta** background — no holes, no jumped parts; compare with the PSB composite. Then play Run / Jump / Fall / Lantern in `01_Home`: no cropped edges on boots/thighs/dress hem.
5. Screenshots to `SharedWorkFolder/ForDesignScreenshot/2026-11-08_Maela_v1.6_Import/` (rest pose magenta, Console with RectCheck PASS, one Run frame).
6. If good: commit on the branch "Maela v1.6 import (rect fix, path A|B) + realign", merge to main, push. Record hash + which path worked in `TechnicalArt/MENU_UNITY_PROGRESS.md`. If bad: `git switch main`, delete branch, report.

## Do not
- Don't change importer settings, animation clips, bone transforms, Home scene framing (user's values: Background pos −1.9156, −0.8494, scale 0.645; ortho 3.45).
- Don't run realign twice. Don't touch Library/ by hand.
- User records gameplay video himself (Win+Alt+R).
