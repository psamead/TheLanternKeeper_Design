# Task: Maela — roll back to the v1 rig and apply the "safe" white-edge fix (2026-11-07)

The v1.1 / v1.2 art updates broke the rig (they changed layer pixel bounds, so the importer's sprite rects moved; v1.2 also made every layer full-canvas). **Both are abandoned.**

Already done by Claude in the working tree (not committed):
- `Maela.psb.meta`, `Maela.prefab` and `01_Home.unity` restored to commit **1517f47** (the v1 that worked).
- `Maela.psb` = v1 with only colours changed: light fringe recoloured, lantern-glass holes filled. **Every layer's bounds are identical to v1** (checked layer by layer in Photoshop), so sprite rects, pivots and the rig must stay exactly as in 1517f47.
- The editor script `MaelaSpriteAligner.cs` was moved out to `_to_delete/` at the project root (not used). Do not commit `_to_delete/`; the user deletes it.

## Steps
1. Ask the user to save; only `01_Home` open. Let Unity reimport. **Do not** re-slice, change pivots, run any aligner, or move any sprite/bone.
2. Play Mode: Maela looks exactly like the v1 screenshot (`ForDesignScreenshot/2026-11-06_Maela_Idle_Normal.png`) except no white fringe and a clean lantern glow. Screenshot 1920×1080 + 4× head close-up → `SharedWorkFolder/ForDesignScreenshot/2026-11-07_Maela_v1safe_*.png`.
3. If anything is misaligned, stop and report — do not fix by hand.
4. Commit "Maela: revert v1.1/v1.2, v1 + colour-only edge fix" (psb, psb.meta, prefab, scene) and push. Add a dated note with the hash to `SharedWorkFolder/TechnicalArt/MENU_UNITY_PROGRESS.md`.
