# Task: Home camera closer + Prologue storyboard (Menu → Prologue → Home) (2026-11-07)

Unity project **`TheLanternKeeper2D`**. Re-read `AGENTS.md` (scope now: Menu → Prologue → Home → EndCard). Two parts; commit after each.

## Already done by Claude (not committed)
- `Assets/_Project/Scripts/Storyboard/StoryboardData.cs` (ScriptableObject: frames = image or optional VideoClip, caption, duration, Ken Burns zoom/pan; `crossFade`; `nextScene`).
- `Assets/_Project/Scripts/Storyboard/StoryboardPlayer.cs` (two RawImage layers cross-fade, Ken Burns via uvRect "cover" fit, caption fade, black fade in/out, any key/click = next, **Esc = skip all**, then `SceneLoader.Load(nextScene)`; VideoPlayer support for Flow shots).
- Placeholder images `Assets/_Project/Art/Storyboard/Prologue/SB_P1..P4_placeholder.png` (2208×1242, tagged "PLACEHOLDER"; real art will replace them with the same names minus `_placeholder`).
- Font `Assets/_Project/Fonts/CormorantGaramond-Italic-Variable.ttf` (+ OFL) for captions.

## Part 1 — Home camera
1. Commit "Before camera + prologue". In `01_Home`, CinemachineCamera Lens orthographic size **3.8** (try 3.5–4.0, pick what frames Maela best; report value). Keep Position Composer follow + Confiner2D (confiner must still cover the whole background so the room scrolls left/right and slightly up/down). Dead zone small, damping ≈ 0.3–0.5; Maela slightly below centre so the floor and ceiling hole read.
2. Play test: walk end to end, jump on crate, no camera jitter at confiner edges. Commit "Home: closer camera".

## Part 2 — Prologue
1. New scene **`Assets/_Project/Scenes/00b_Prologue.unity`**; Build Settings order: 00_StartMenu, **00b_Prologue**, 01_Home, 03_EndCard (02_Harbor stays out).
2. Import placeholders: Sprite, PPU 100, no mips, Compression High Quality, Max Size 4096, Read/Write off.
3. Create `Assets/_Project/Data/Storyboard/SB_Prologue.asset` (StoryboardData), nextScene = `01_Home`, crossFade 1.0, frames (captions exactly):
   | # | image | caption | duration | zoom | pan from → to |
   |---|---|---|---|---|---|
   | P1 | SB_P1_placeholder | On the coast of Brittany, the old lighthouse has gone dark. | 6 | 1.00 → 1.10 | (0,0) → (0.3,0.2) |
   | P2 | SB_P2_placeholder | Each night the sea fog rolls in, and takes a little of what people remember. | 6 | 1.08 → 1.00 | (-0.3,0) → (0.3,0) |
   | P3 | SB_P3_placeholder | Seven days before the Night of Anaon, Maela comes to stay with her grandmother. | 6 | 1.00 → 1.10 | (0,-0.2) → (0,0.1) |
   | P4 | SB_P4_placeholder | The next morning, Grandma looks at her as if she were a stranger. | 7 | 1.00 → 1.15 | (0,0) → (-0.2,0) |
4. Scene setup: Main Camera (solid black). Canvas Screen Space Overlay, Canvas Scaler 1920×1080 match 0.5:
   - `LayerA`, `LayerB`: RawImage full-stretch, colour white alpha 0.
   - `Caption` (CanvasGroup) bottom-centre, ~1400 px wide, ~110 px from the bottom, soft dark gradient behind text; TMP text with a Cormorant Garamond Italic SDF asset (create it), size ≈ 44, colour #EDE6D6, centred, line spacing comfortable.
   - `BlackFade`: full-screen black Image with CanvasGroup alpha 1, top-most, raycast off.
   - `StoryboardPlayer` component wired to all of the above + SB_Prologue. Add a VideoPlayer (Render Texture mode, 1920×1080 RenderTexture `RT_Storyboard`, no audio) for future Flow clips.
   - Small hint text bottom-right "Any key — next   ·   Esc — skip" (Cinzel, small, 50 % opacity).
5. Menu: change `MainMenuController` Play → load **`00b_Prologue`** instead of `01_Home` (keep the music fade-out). Prologue music not needed now.
6. Test: Menu → Play → 4 frames with slow movement and captions → fade → Home playable. Any key skips a frame; Esc jumps straight to Home. No Console errors.
7. Record ~40 s (menu → prologue → walking in Home) → `SharedWorkFolder/ForDesignScreenshot/2026-11-07_Prologue_Camera/2026-11-07_Prologue_Flow.mp4`. Commit "Prologue storyboard (placeholders) + menu → prologue → home", push, note hash + camera size in `TechnicalArt/MENU_UNITY_PROGRESS.md`.

## Do not
- Don't touch Maela art/prefab sprite positions/animations. Keep captions in the ScriptableObject, not in code.
