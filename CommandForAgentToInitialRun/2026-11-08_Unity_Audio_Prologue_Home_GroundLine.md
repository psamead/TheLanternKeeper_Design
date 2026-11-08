# Task: Prologue + Home audio v1, Maela SFX, Home ground line (2026-11-08)

Unity project **`TheLanternKeeper2D`**. Re-read `AGENTS.md`. Run this **after** (or independently of) `2026-11-08_Unity_Maela_v1.6_ImportFix_Trial.md` — do this one on `main` only if that trial branch is merged or abandoned; otherwise do it on its own branch `feat/audio-ground` and merge after.
User has listened to the preview and approved the audio ("整体感觉可以，放进去 Unity 试试").

## Part A — Home ground line (user values, not yet in the scene)
In `01_Home.unity`, set these Transform Y (keep X/Z):
| Object | current Y | new Y |
|---|---|---|
| Ground | −3.7519 | **−3.5225** |
| Crate | −2.6594 | **−2.43** |
| Player | −3.4294 | **−3.20** |
Reference: `SharedWorkFolder/ForDesignScreenshot/2026-11-07_Home_Scale_Review/user_note_1857_good_framing_ref.png`. Do NOT touch Background (−1.9156, −0.8494; scale 0.645) or camera (ortho 3.45). Play: Maela stands on the drawn floor, lands on the crate, no falling through.

## Part B — Audio import
Copy from `SharedWorkFolder/TechArtAsset/Audio/` into `Assets/_Project/Audio/` (same subfolders):
- `Prologue/BGM_Prologue_ArMorDu_loop_v1.ogg` (96 s loop), `Prologue/AMB_Prologue_SeaWind_loop_v1.ogg` (48 s loop) — not the .wav
- `Home/AMB_Home_Interior_loop_v1.ogg` (40 s loop)
- `Maela/SFX_Maela_Step_Wood_01..04_v1.ogg`, `SFX_Maela_Jump_01..02_v1.ogg`, `SFX_Maela_Land_01..02_v1.ogg`, `SFX_Maela_LanternRaise_v1.ogg`
Import settings: loops/BGM/AMB → Load Type Streaming, Vorbis q≈70; SFX → Decompress On Load. Same as menu audio.

## Part C — Wiring
1. **00b_Prologue**: music + ambience AudioSources (loop), fade in ~1.5 s; the menu BGM/ambience tail must stop/fade (reuse `MenuMusic` pattern). Volumes start: BGM 0.6, AMB 0.5.
2. **01_Home**: prologue BGM fades out on entering Home (~2 s); Home ambience loop at 0.5. No BGM in Home for now.
3. **Maela SFX** — new `MaelaAudio.cs` on the Player (one AudioSource, PlayOneShot, pitch random 0.95–1.05, never same clip twice in a row):
   - Footstep: driven from the Run clip — add Animation Events in `Maela_Run.anim` at each foot contact (or, if editing the clip is awkward because `MaelaAnimBuilder.cs` regenerates it, add the events in `MaelaAnimBuilder.cs` so they survive a rebuild). Only when Grounded. Volume 0.7.
   - Jump: when `PlayerController` actually starts a jump (expose an event `OnJump`). Volume 0.8.
   - Land: on Grounded false→true after being airborne > 0.15 s. Volume 0.9.
   - Lantern: when the `RaiseLantern` trigger is set (E key). Volume 0.8.
   Keep `PlayerController` changes minimal (events only, no movement changes).
4. Exactly one AudioListener per scene (Main Camera). Console 0 warnings on Menu → Prologue → Home.

## Done
- Commit "Prologue/Home audio v1 + Maela SFX; Home ground line" and push. Note hash in `TechnicalArt/MENU_UNITY_PROGRESS.md`.
- Screenshot of Home at rest (Maela standing on the floor) → `SharedWorkFolder/ForDesignScreenshot/2026-11-08_Home_Ground_Line/`.
- Tell the user to record a run-through himself (Win+Alt+R); synthetic input can't reach the Game view. Listening checks (levels, 96 s loop seam) are the user's.

## Do not
- Don't change importer settings of Maela.psb, bone transforms, movement tuning, or Home framing. Don't commit TMP fallback / Recorder / AGENTS / manifest changes.
