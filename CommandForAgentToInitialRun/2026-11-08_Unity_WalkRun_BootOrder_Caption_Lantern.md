# Task: Walk/Run split, boot order back, P1 caption colour, lantern SFX v2 (2026-11-08 evening)

Unity `TheLanternKeeper2D`, `main` at `d40cce5`. Re-read `AGENTS.md`. One commit per part, push after each; stop at the first part that fails. Don't commit TMP fallback / Recorder / AGENTS / manifest.

## Part 1 — Boot draw order back to the old one (user: the near boot must be behind the other)
Maela prefab SpriteRenderer `sortingOrder`: **Boot_L 7, Leg_Upper_R 8, Leg_Lower_R 9, Boot_R 10** (Leg_Lower_L 6, Leg_Upper_L 5, Dress 11 unchanged) — i.e. the order before `1d80154`. Check rest + Run on magenta. Commit "Maela boot draw order: back to v1.6 order".

## Part 2 — Walk and Run as two states
Source data (single source of truth): `SharedWorkFolder/TechArtAsset/Characters/Maela/_work/anim_v2/poses.py` — new clip **Maela_Walk** (0.9 s loop: upright body −1…−2°, thighs ±10°, near-straight legs) and changed **Maela_Run v3** (0.5 s: lean −10…−12°, back leg bent to −52°, front leg straight under the body at contact like the old Run, thighs +15/−14). Preview gifs and `contact_walk_run_v2.png` in the same folder; user reviewed them.
1. Copy the Walk and Run key values into `Assets/_Project/Editor/MaelaAnimBuilder.cs` exactly (same paths/props as the existing Run; JumpUp/Fall/Lantern unchanged). Regenerate clips. Footstep Animation Events: Walk at **0 and 0.45 s**, Run at 0 and 0.25 s (keep them in the builder so they survive rebuilds).
2. Controller: Idle → Walk when Speed > 0.1; Walk → Run when Speed > 2.6; back with the same thresholds (Run → Walk < 2.6, Walk → Idle < 0.1). Transition durations as now (0.08–0.1).
3. `PlayerController`: **default = run** `runSpeed = 3.2`; **hold Left/Right Shift = slow walk** `walkSpeed = 1.8` (user decision 11-08). No other movement changes (jump, coyote, buffer unchanged).
4. Footstep volume: Walk 0.55, Run 0.7 (MaelaAudio can read the current state or a simple flag from PlayerController).
5. Check: walk, run, switch walk↔run while moving, jump from run; no seams on magenta in Walk frames. Commit "Maela Walk/Run split (run default, Shift to walk)". Screenshots → `ForDesignScreenshot/2026-11-08_Maela_WalkRun/`.

## Part 3 — P1 caption colour (white was too close to the cold-blue sky)
P1 frame only (per-frame field; add `Color captionColor` + underlay settings to the frame data, default = current white/no underlay):
- Text colour **cold moonlight `#BFE6E2`** (pale, desaturated version of the lighthouse light in SB_P3; also hints at the old times).
- TMP **Underlay** on a per-frame material instance: colour `#0B1A2E`, alpha ~0.6, offset (0, −0.5), dilate 0.2, softness 0.6 — a soft dark halo so the text separates from the bright sky. Do NOT change the shared font material used by other frames/menu.
- Screenshot 1920×1080 → `ForDesignScreenshot/2026-11-08_Prologue_Caption/P1_moon.png`. Commit "Prologue P1 caption: moonlight colour + soft underlay".

## Part 4 — Lantern SFX v3 (v1 tail sounded like a temple bell)
Import `SharedWorkFolder/TechArtAsset/Audio/Maela/SFX_Maela_LanternRaise_v3.ogg` (v1 brass strike with the tail cut + v2 tink/glow) (DecompressOnLoad, like v1), set it in MaelaAudio instead of v1 (keep v1/v2 files). Commit "Lantern raise SFX v3 (short brass strike + glow)".

## Report
Hashes, pass/fail per part, notes in `TechnicalArt/MENU_UNITY_PROGRESS.md`. User records the run-through himself.
