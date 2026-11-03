# Task: Commit the menu-feel changes made by Claude (2026-11-04)

Unity project **`TheLanternKeeper2D`**. The user has tested these in Play Mode and approved them. **Do not change any code or scene content** — only review, commit and push.

1. Ask the user to save open scenes (Ctrl+S). Make sure only `00_StartMenu` is open in the Hierarchy (no additive `01_Home`).
2. Restore (do not commit) `Assets/TextMesh Pro/Resources/Fonts & Materials/LiberationSans SDF - Fallback.asset` — TMP rewrites it at runtime.
3. Commit these files (plus their `.meta` only if Unity changed them):
   - `Assets/_Project/Scripts/MenuAudio.cs` — two alternating hover voices (old wave cut in ~15 ms, new restarts); dwell: after 1.0 s resting on an item, soft waves every 1.4–2.2 s until pointer exit / keyboard / confirm; confirm sound on a DontDestroyOnLoad object
   - `Assets/_Project/Scripts/MenuItemHover.cs` — adds pointer exit
   - `Assets/_Project/Scripts/MainMenuController.cs` — `PointerLeft`, keyboard does not enter dwell; Edit Mode preview (`OnValidate` → icon / underline / colours placed as at runtime, item 0 selected)
   - `Assets/_Project/Scripts/MenuMusic.cs` + `Assets/_Project/Scenes/00_StartMenu.unity` — Play: 0.5 s fade then load `01_Home` (no wait for the confirm clip)
   - `Assets/_Project/Scenes/01_Home.unity` — placeholder label `01_Home` / `Esc → menu` restored, camera background #1E2633
   - `Assets/_Project/Audio/Menu/SFX_Menu_Hover_Wave_01/02/03.ogg` — hover v3 (peak at 5–6 ms)
4. In Edit Mode (not playing) check the Scene/Game view: lantern icon left of PLAY, gold underline under PLAY, PLAY gold — same as in Play Mode. Save `00_StartMenu` so the corrected positions are stored.
5. Quick Play Mode check: no Console errors; menu → PLAY → Home → Esc works.
6. Commit "Menu feel: instant hover restart, dwell waves, 0.5 s Play transition, Home placeholder" and push. Append one dated line to `SharedWorkFolder/TechnicalArt/MENU_UNITY_PROGRESS.md` with the commit hash.
