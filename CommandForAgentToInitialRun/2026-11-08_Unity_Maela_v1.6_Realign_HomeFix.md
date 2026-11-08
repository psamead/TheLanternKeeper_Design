# Task: Maela v1.6 (bigger layers) + sprite realign + Home scene repair + single AudioListener (2026-11-08)

Replaces `2026-11-07_Unity_Home_Fix_v1.5_SUPERSEDED.md` (do not run that one). Unity project **`TheLanternKeeper2D`**. Re-read `AGENTS.md`.

## What changed (Claude, not committed)
- `Assets/_Project/Art/Characters/Maela/Maela.psb` → **v1.6**: the user repainted hidden parts (front of the far boot, thighs, knees, skirt hem). **8 layers now have bigger pixel bounds** — by design. Layer names/order/canvas unchanged.
- `Assets/_Project/Art/Characters/Maela/maela_realign.json`: per-layer centre shift in PSB px (right / down), computed from old vs new bounds:
  Leg_Upper_L (+2, −1.5) · Leg_Lower_L (+1, −0.5) · Boot_L (+10, −1.5) · Leg_Upper_R (−2, +0.5) · Leg_Lower_R (−1, −12.5) · Boot_R (−2, +0.5) · Dress (0, +11) · Hand_L (0, 0).
- `Assets/_Project/Editor/MaelaSpriteRealign.cs` — menu **Tools ▸ Lantern Keeper ▸ Realign Maela Sprites**: moves each `<Layer>_Sprite` child in `Maela.prefab` by (dx/200, −dy/200). **Run exactly once.**
- Known accidental, uncommitted edit in `01_Home.unity`: Background moved to (−1.9156, −0.8494) with non-uniform scale; two camera positions changed. Committed version (Background (0,0,0), scale 0.8) is correct.
- Console spam: "There are 2 audio listeners in the scene" — a DontDestroyOnLoad object from the menu carries a second AudioListener.

## UPDATE 01:20 — cause of the 2 missing sprites found and fixed
The previous run stopped because `Hand_L_Sprite` and `Boot_R_Sprite` were missing. Cause: in the user's Photoshop edit those two layers got **new PSD layer IDs** (Boot_R 81→123, Hand_L 87→125); the PSD Importer maps sprites by layer ID, so it treated them as new sprites. Claude patched the IDs back in `Maela.psb` (now identical IDs to v1.4/v1.5, pixels unchanged) and re-copied `maela_realign.json`. `Maela.psb.meta` only differs from HEAD by CRLF line endings — restore it from git before reimport (`git checkout -- Assets/_Project/Art/Characters/Maela/Maela.psb.meta`).
If after reimport any sprite is still missing: right-click `Maela.psb` → Reimport; if still missing, close Unity, delete `Library/` entries for that asset is NOT allowed — instead report and stop.
Also: the user asked to keep his `01_Home` edits out — the background move was accidental; revert it as in step 1.

## Steps
1. Ask the user to save nothing in `01_Home` (discard). `git checkout -- Assets/_Project/Scenes/01_Home.unity`. Commit checkpoint "Before Maela v1.6" containing nothing else.
2. **Before** reimport, record a placement snapshot: for every SpriteRenderer under the Maela prefab, its sprite name + world-space `bounds.center` (prefab at origin, rest pose). Save as text in `TechnicalArt/` for the record.
3. Let `Maela.psb` re-import (no importer setting changes). Check every SpriteRenderer still has its sprite (no missing references). If any is missing → revert psb + json, report, stop.
4. Run **Realign Maela Sprites** once. Take the snapshot again. Expected: for every changed layer, new world centre − old world centre ≈ (dx/200, −dy/200) from the json — i.e. the *artwork* stays where it was and only the extra painted pixels appear. Visually: in the prefab at rest, compare against the PSB composite (`SharedWorkFolder/TechArtAsset/Characters/Maela/_work/fix_v1.5m/` previews) — nothing should jump. Report the max deviation in px.
5. Home scene: verify Background (0,0,0) scale 0.8; Confiner2D polygon = background `SpriteRenderer.bounds`; walls at its left/right edges; camera (ortho 3.8) never shows outside the background. If ortho 3.8 is taller than the background allows, lower it and report.
6. AudioListener: exactly one in every scene during Play (keep the Main Camera's; remove/disable the one on any persistent object). Menu → Prologue → Home: Console 0 warnings.
7. Commit "Maela v1.6 (repainted hidden parts) + sprite realign; Home background revert; single AudioListener" and **push**. Note hash, snapshot result, ortho value in `TechnicalArt/MENU_UNITY_PROGRESS.md`.
8. No video needed (synthetic input can't reach the Game view) — tell the user to record by hand (Win+Alt+R).

## Do not
- Don't run the realign tool twice. Don't change importer settings, animation clips, or bone transforms. Don't commit TMP fallback / Recorder / AGENTS changes.
