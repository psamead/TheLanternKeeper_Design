# Task: Commit fog texture edge fix (2026-11-05)

Unity project **`TheLanternKeeper2D`**, scene `00_StartMenu`. Small task — commit only, no other changes.

## Background
After "Menu FX" (`f714830`) the user saw a hard horizontal edge under the fog. Cause: the top/bottom rows of the fog textures were not fully transparent (alpha 4–9/255), and Wrap V was Repeat (bilinear sampling pulled in the opposite edge).

## Already done by Claude (not committed)
- `Assets/_Project/Art/Menu/FX/MENU_FX_Fog_A.png` (+ `.meta`)
- `Assets/_Project/Art/Menu/FX/MENU_FX_Fog_B.png` (+ `.meta`)
- New PNGs: alpha = 0 at the top/bottom edges (smooth fade over the outer 18 %); left-right still seamless.
- Import: Wrap U = **Repeat** (unchanged), Wrap V = **Clamp**.
- **No scene, script or numeric changes.**

## Steps
1. Make sure the user has saved the scene (Ctrl+S) and confirmed the edge is gone in Play Mode.
2. Do not change anything else. Restore TMP auto-changed font assets if modified (`LiberationSans SDF - Fallback.asset`, `Cinzel SDF Generated.asset`).
3. Commit only these 4 files as "Fog textures: transparent edges, Wrap V clamp" and push.
4. Append one dated line with the commit hash to `SharedWorkFolder/TechnicalArt/MENU_UNITY_PROGRESS.md`.
