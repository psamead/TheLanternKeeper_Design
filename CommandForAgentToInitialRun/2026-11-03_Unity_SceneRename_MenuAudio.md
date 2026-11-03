# Task: Renumber scenes + Start Menu audio (2026-11-03)

Unity project: **`TheLanternKeeper2D`** (same as before). Re-read `AGENTS.md` first. Do Part A, commit, then Part B.

## Part A — Renumber scenes (start menu is 00; game chapters start at 01)

| Old | New |
|---|---|
| `01_StartMenu` | `00_StartMenu` |
| `02_Home` | `01_Home` |
| `03_Harbor` | `02_Harbor` |
| `04_EndCard` | `03_EndCard` |

1. Ask the user to save any open scene (Ctrl+S). Commit "Before scene renumber" and push.
2. Rename the four `.unity` files **inside Unity** (Project window or `AssetDatabase.RenameAsset`) so the `.meta` GUIDs are kept. Do not rename on disk outside Unity.
3. Build Settings: same four scenes, order 00 → 01 → 02 → 03; check the paths updated.
4. Code: `MainMenuController` Play → `01_Home`; `BackToMenu` → `00_StartMenu`; search `Assets/_Project/Scripts` for any other old name.
5. Placeholder labels (TMP text in each placeholder scene): Home already shows `01_Home` — leave it; Harbor shows `03_Harbor` → change to `02_Harbor`; EndCard shows `04_EndCard` → change to `03_EndCard`. Keep the `Esc → menu` line.
6. Docs inside the project: in `Docs/PROJECT_HANDOFF.md` and `Docs/MENU_UNITY_HANDOFF.md` update the scene list (old dated log lines may stay as history). `AGENTS.md` is already updated by Claude.
7. Play Mode check: menu → Play loads `01_Home`; Esc returns to `00_StartMenu`. Commit "Renumber scenes: 00_StartMenu, 01_Home, 02_Harbor, 03_EndCard" and push.

## Part B — Start Menu audio (scene `00_StartMenu`)

## Already done by Claude (not yet committed — include in your first commit)
- Audio files are **already in the project**: `Assets/_Project/Audio/Menu/` (OGG, 44.1 kHz stereo, made by Claude, no third-party licence). Do not copy them again; only set import settings. Source copies (`_v1`) live in `SharedWorkFolder/TechArtAsset/Audio/Menu/` — do not touch.

| File | Use | Import settings |
|---|---|---|
| `BGM_Menu_Gwerz_loop.ogg` (80 s) | Menu music, loops | Load Type **Streaming**, Vorbis Q 70, Load In Background on |
| `AMB_Menu_SeaWind_loop.ogg` (60 s) | Sea + wind bed under the music, loops | Streaming, Vorbis Q 70 |
| `SFX_Menu_Hover_Wave_01/02/03.ogg` (~1 s) | Selection changes (keyboard or mouse) — rotate, never the same one twice in a row | **Decompress On Load**, Vorbis Q 70 |
| `SFX_Menu_Confirm_Lantern.ogg` (~3 s) | Confirm (Play / Settings / Quit) | Decompress On Load |
| `SFX_Menu_Back_Wood.ogg` (~1 s) | Closing the Settings panel with Esc | Decompress On Load |

All files: Force To Mono **off**, Preload Audio Data on for SFX.

## Steps
1. (Part A already committed — no extra "before" commit needed.)
2. Replace the synthesized beeps: create `MenuAudio.cs` (small, commented) with serialized `AudioClip[] hoverClips`, `confirmClip`, `backClip`, and public `PlayHover()`, `PlayConfirm()`, `PlayBack()`. Use one 2D `AudioSource` for SFX (`PlayOneShot`; hover volume 0.6, confirm 0.8, back 0.7; random pitch 0.97–1.03 on hover only). `MainMenuController` uses `MenuAudio` instead of `ProceduralMenuAudio`; call `PlayBack()` when Esc closes Settings. Then delete `ProceduralMenuAudio.cs` and its component from the scene.
3. Music + ambience: add a `MenuMusic` GameObject in `00_StartMenu` with two 2D `AudioSource`s — BGM (loop, volume 0.6) and ambience (loop, volume 0.45), both Play On Awake. Fade both in over 2 s at scene start. When Play is confirmed, fade both out over ~1 s, **then** load `01_Home` (let the lantern confirm sound be heard; do not cut it).
4. Keep only one `AudioListener` (Main Camera).
5. Play Mode check: music and sea start and loop with no click at the loop point (listen once past 80 s if possible); hover sounds rotate; confirm + fade-out before Play loads `01_Home`; Esc in Settings plays the wood sound. Ask the user to save the scene (Ctrl+S) in Unity before you commit. Commit "Menu audio: natural SFX + BGM" and push.
6. Report: append a dated section to `SharedWorkFolder/TechnicalArt/MENU_UNITY_PROGRESS.md` (what was done, what you checked, what was not verified — e.g. no real speaker listening) and one dated line to `SharedWorkFolder/ART_HANDOFF.md` §10 (edit the current file; do not overwrite other changes).

## Do not
- Do not add an Audio Mixer yet (volume settings come later with the Settings panel).
- Do not change the menu layout, other scenes, or the Demo checklist.
