# Task: Commit Cinemachine install + small leftovers (2026-11-05)

Unity project **`TheLanternKeeper2D`**. Commit only — do not set up any camera yet.

The user installed **Cinemachine 3.1.7** via Package Manager. Claude updated the camera rule in the project-root `AGENTS.md` (camera follow = Cinemachine; no custom follow script).

1. Make sure scenes are saved (Ctrl+S). Restore TMP auto-changed font assets if modified.
2. Commit:
   - `Packages/manifest.json`, `Packages/packages-lock.json` — Cinemachine 3.1.7
   - `AGENTS.md` — camera rule
   - `Assets/_Project/Scenes/00_StartMenu.unity` — URP auto-added `UniversalAdditionalCameraData` on Main Camera (no other change; check the diff)
3. Commit message: "Add Cinemachine 3.1.7; camera rule; URP camera data" and push. Append one dated line with the hash to `SharedWorkFolder/TechnicalArt/MENU_UNITY_PROGRESS.md`.
