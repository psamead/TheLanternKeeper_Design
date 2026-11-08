# Task: Lantern action lock + audio pitch bug, P1 caption shadow lighter (2026-11-08 night)

Unity `TheLanternKeeper2D`, `main` at `bc5f3df`. Re-read `AGENTS.md`. One commit per part, push after each.

## Part 1 — Lantern (E) bugs + lock (user decisions 11-08)
Observed by user:
- E pressed again while the ring is still sounding → the ring **changes pitch**.
- Pressing arrows during it → the ring keeps sounding, the body stays in the lantern pose, but she slides/moves.
Cause (Claude read the code): `MaelaAudio` plays everything through **one AudioSource** and sets `source.pitch = Random.Range(0.95,1.05)` before every `PlayOneShot` — changing pitch also bends every one-shot still playing (the 3.3 s lantern ring). And `PlayerController` keeps applying movement while the Lantern state plays.
Fix:
1. `MaelaAudio`: a **second AudioSource only for the lantern**, pitch fixed **1.0**, `Play()` (not OneShot). Footsteps/jump/land keep their own source with random pitch.
2. **Lock while the ring sounds** — new rule: the ring must finish before the next E, and during the ring no other action or input:
   - `PlayerController`: `bool LanternLocked` true from E press until the lantern clip ends (`clip.length`, ≈3.3 s; read it, don't hard-code). While locked: ignore move / jump / E input, set horizontal velocity to 0 (gravity still applies), Animator Speed = 0.
   - E only accepted when grounded and not locked (no mid-air raise).
   - Animator: Lantern state plays fully; no Speed/Grounded transitions out of it while locked; return to Idle after. Reset the `RaiseLantern` trigger after use so it can't queue.
3. Test: E then spam E/arrows/space during the ring → one clean ring, no pitch change, no movement, then normal control. Walk/run footsteps still randomise pitch. Commit "Lantern action lock + separate lantern AudioSource".
(Later, per DEMO plan, E will also switch Present/Memory and only work after picking up the lantern — not in this task.)

## Part 2 — P1 caption shadow lighter
Colour `#F0EED1` stays. The underlay is now too heavy (text "jumps" out). Set: alpha **0.55**, dilate **0.2**, softness **0.65**, offset (0, −0.3); remove any Face Dilate added last time. Screenshot → `ForDesignScreenshot/2026-11-08_Prologue_Caption/P1_moon_v3.png`. Commit "P1 caption: lighter underlay".

## Report
Hashes; note in `TechnicalArt/MENU_UNITY_PROGRESS.md`.
