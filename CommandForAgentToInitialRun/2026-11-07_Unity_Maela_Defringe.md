# Task: Maela art update v1.1 — defringe + lantern flame (2026-11-07)

Unity project **`TheLanternKeeper2D`**. Claude already replaced `Assets/_Project/Art/Characters/Maela/Maela.psb` (same file name, same 19 layers, same canvas 149×320; `.meta` untouched, so the GUID and importer settings stay).

What changed in the art: light outline fringe removed from every part (the cream background halo on the dark scene); holes inside the lantern glass filled and the flame repainted as one soft warm core. No layer was added, removed, renamed or moved.

## Steps
1. Ask the user to save; only `01_Home` open. Let Unity reimport the .psb.
2. Check the rig still works: open `Maela.prefab` and `01_Home` in Play Mode — all sprites in place, Idle plays, no missing-sprite warnings. If any sprite reference broke on reimport, reconnect it to the layer with the same name (do not change pivots or bones).
3. Screenshot at 1920×1080 → `SharedWorkFolder/ForDesignScreenshot/2026-11-07_Maela_Idle_v1.1.png`.
4. Commit "Maela art v1.1: defringe, lantern flame" (the .psb only, plus anything the reimport legitimately changed) and push. Also commit the Unity Recorder package change from 11-06 if the user agrees (it is still a local modification). Add a dated note with the hash to `SharedWorkFolder/TechnicalArt/MENU_UNITY_PROGRESS.md`.
