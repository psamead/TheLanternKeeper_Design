# Task: Core_Persistent split + Maela v1.6_m + footstep v3 + prologue caption layout (2026-11-08)

Unity project **`TheLanternKeeper2D`**, current `main` (after `fb1958e` + the user's collider fix). Re-read `AGENTS.md`.
**Four separate commits, in this order**, push after each. If one part fails, stop there and report — earlier commits stay.
Don't commit the user's TMP fallback / Recorder / AGENTS / manifest changes.

---
## Part 1 — Core_Persistent + additive levels (like *The Fairy Hills*)
Reference implementation (read, don't copy namespaces blindly): `W:\...\TheFairyHill2D\Assets\_Project\Scripts\Gameplay\ChapterSceneLoader.cs`, `LevelBootstrap.cs`, `GameState.cs`, scene `Assets/Scenes/Core_Persistent.unity`.

1. Commit checkpoint "Before Core split".
2. New scene `Assets/_Project/Scenes/Core_Persistent.unity` containing everything that must persist through gameplay:
   - **Maela** (the prefab instance, with PlayerController + MaelaAudio + her Light2D)
   - **Main Camera** (only AudioListener in the game), **Cinemachine** camera + Confiner2D
   - **AudioManager** (new, singleton `AudioManager.Instance`): `PlayMusic(clip, vol, fade)`, `PlayAmbience(clip, vol, fade)`, crossfade, two sources each. Replaces the DontDestroyOnLoad audio carry-over from the menu (menu → prologue → home fades must sound the same as now).
   - **GameState** (singleton): `bool HasLantern`, `bool MemoryLayer` (present/memory toggle, used later), nothing else yet.
   - **LevelLoader** (singleton): `LoadLevel(sceneName, spawnId)` — additive load, SetActiveScene, apply LevelInfo, move Maela to SpawnPoint, rebind Confiner2D to the level's bounds collider, unload previous level.
   - Global Light 2D, EventSystem (only one in the game while Core is loaded).
3. In each level scene put only level content + two new components:
   - `LevelInfo`: camera bounds collider (PolygonCollider2D), ortho size, ambience clip + volume, music clip (null = keep/stop), global light colour/intensity.
   - `SpawnPoint` (id string). 01_Home: `Spawn_Start` at the current player position **(−8, −3.20)**.
   - `LevelBootstrap`: if the level is opened directly in the Editor and Core isn't loaded, load Core additively (for testing).
4. Move out of `01_Home`: Maela, camera, Cinemachine, AudioListener, EventSystem, global light. **Keep in `01_Home`, values unchanged:** Background (−1.9156, −0.8494, scale 0.645), Ground (−1.91, −3.5225) + collider, Crate (−1.5, −2.43, scale 1.4) + collider, walls. LevelInfo ortho **3.45**, bounds = current CameraBounds.
5. Flow: `00_StartMenu` → `00b_Prologue` (normal single scenes, unchanged) → at the end Prologue loads `Core_Persistent` then `LevelLoader.LoadLevel("01_Home","Spawn_Start")`. Esc/back-to-menu from a level unloads level + Core and loads the menu. Build Settings: add Core_Persistent.
6. Acceptance: Game view of Home at rest matches `ForDesignScreenshot/2026-11-08_Home_Ground_Line/Home_Rest.png` (same framing, Maela on the floor); walk to both walls, jump on crate; opening `01_Home` directly + Play also works (bootstrap); exactly one AudioListener and one EventSystem at all times; Console 0 project warnings on Menu → Prologue → Home → Esc → Menu.
7. Commit "Core_Persistent + additive level loading (AudioManager, GameState, LevelLoader)". Screenshot `ForDesignScreenshot/2026-11-08_CoreSplit/Home_Rest_after.png`.

---
## Part 2 — Maela v1.6_m (user's final fix of v1.6)
Source: `SharedWorkFolder/TechArtAsset/Characters/Maela/_work/fix_v1.5/Maela_v1.6_m.psb`. Claude compared it with the v1.6 now in Unity: layer IDs all identical; **one bounds change** (Leg_Upper_L 26→33 px wide, right edge +7, centre +3.5 px right); pixel-only changes in Leg_Upper_R, Dress, Coat_Hem, Lantern; **layer order changed** (Boot_R moved below Boot_L and the right legs).
Prepared in `SharedWorkFolder/TechArtAsset/Characters/Maela/_work/fix_v1.6m_import/`: `Maela.psb.meta.v1.6m_patched` (only Leg_Upper_L width 26→33), `maela_expected_rects.json`, `maela_realign.json` (Leg_Upper_L dx +3.5, dy 0).
1. Copy `Maela_v1.6_m.psb` → `Assets/_Project/Art/Characters/Maela/Maela.psb`; `Maela.psb.meta.v1.6m_patched` → `Maela.psb.meta`; both json → same folder (replace). Same path A as last time.
2. Reimport → **Check Maela Sprite Rects** must PASS. FAIL → revert, report the log + meta diff, stop (no path B).
3. **Realign Maela Sprites** once.
4. Draw order to match Photoshop — set SpriteRenderer `sortingOrder` on the prefab children (don't touch PSB/importer order): **Leg_Lower_L 6, Boot_R 7, Boot_L 8, Leg_Upper_R 9, Leg_Lower_R 10** (others unchanged: Leg_Upper_L 5, Dress 11 …). If `MaelaAnimBuilder.cs` or any script sets sortingOrder, update it there too. **If the new order looks wrong in any pose (boot/leg overlap, seams), revert to the old order** (Boot_L 7, Leg_Upper_R 8, Leg_Lower_R 9, Boot_R 10) and say so in the report — user decision 11-08.
5. Check rest pose on magenta + Run/Jump/Fall/Lantern; screenshots → `ForDesignScreenshot/2026-11-08_Maela_v1.6m/`. Commit "Maela v1.6_m (Leg_Upper_L wider, Boot_R draw order)".

---
## Part 3 — Footstep v4 (v3 superseded)
Replace footsteps with `SharedWorkFolder/TechArtAsset/Audio/Maela/SFX_Maela_Step_Wood_01..04_v4.ogg` (deep old-floorboard "dong") (same import settings as v1; remove v1 steps from the MaelaAudio list, keep the files). Commit "Footstep v4 (deep old floorboards)".

---
## Part 4 — Prologue caption layout (P1)
User's markup: put the text in the sky area **right of the lighthouse**, **two lines**, **bigger**.
1. Add per-frame caption layout to `StoryboardData` frames: `Vector2 anchorMin, anchorMax` (0–1 of the screen), `TextAlignmentOptions align`, `float fontScale` (default = current bottom-centre layout, so frames without values look as now). `StoryboardPlayer` applies them per frame.
2. SB_Prologue frame 1: anchorMin **(0.51, 0.36)**, anchorMax **(0.82, 0.71)**, align **Center**, fontScale **1.5**, caption with a line break:
   `On the coast of Brittany,` / `the old lighthouse has gone dark.`
   Keep the same font (Cormorant Garamond Italic), colour, fade. Add a soft shadow/outline only if it becomes hard to read on the bright sky.
3. Frames 2–4 unchanged for now (art not final). "ANY KEY NEXT · ESC SKIP" unchanged.
4. Screenshot 1920×1080 → `ForDesignScreenshot/2026-11-08_Prologue_Caption/P1.png`. Commit "Prologue caption: per-frame layout, P1 two lines in sky".

---
## Report
Hashes of all four commits + which parts passed. Note in `TechnicalArt/MENU_UNITY_PROGRESS.md`. User records the run-through himself (Win+Alt+R).
