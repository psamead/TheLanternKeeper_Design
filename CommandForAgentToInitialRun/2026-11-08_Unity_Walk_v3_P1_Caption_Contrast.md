# Task: Walk v3 (slower, no floating) + P1 caption contrast (2026-11-08 late)

Unity `TheLanternKeeper2D`, `main` at `8f5869e`. Re-read `AGENTS.md`. One commit per part, push after each.

## Part 1 — Walk v3
User: walking looks like floating. Cause: walk speed 1.8 u/s is far faster than the stride the Walk clip actually covers (thighs ±10° → the planted foot slides along the floor).
1. Copy **Maela_Walk** keys from `SharedWorkFolder/TechArtAsset/Characters/Maela/_work/anim_v2/poses.py` (v3: length **1.1 s**, thighs +12/−11, hip bob only 0.003, body −1°) into `MaelaAnimBuilder.cs`; regenerate. Footstep events: **0 and 0.55 s**. Run/Jump/Fall/Lantern unchanged.
2. **Match speed to stride**: start `walkSpeed = 0.8`. Measure in Play Mode: world X of the planted boot (Boot_R/Boot_L sprite bottom) over the contact half-cycle; adjust `walkSpeed` until the planted boot moves < 0.02 units while in contact. Report the final value. (Same check for Run only as information — don't change run.)
3. Screenshot/short note in `ForDesignScreenshot/2026-11-08_Maela_WalkRun/walk_v3_note.md`. Commit "Maela Walk v3 (slower, stride-matched speed)".

## Part 2 — P1 caption: stronger separation from the sky
`#BFE6E2` + soft underlay still blends into the bright cyan sky.
- Text colour: the **P3 lighthouse light** itself, **`#93FEFC`** (sampled from `SB_P3_placeholder.png`).
- Underlay much stronger: colour `#0B1A2E`, alpha **0.85**, offset (0, −0.4), dilate **0.4**, softness **0.45** (dark halo reads as a soft shadow, not a box).
- If still low-contrast at 1920×1080, also raise font weight via TMP `Face Dilate 0.1` on the same per-frame material. Don't touch shared materials.
- Screenshot → `ForDesignScreenshot/2026-11-08_Prologue_Caption/P1_moon_v2.png`. Commit "P1 caption: lighthouse-light colour + stronger underlay".

## Part 3 — Console spam (check only)
Console shows ~80× `Unknown platform passed to AudioImporter.ContainsSampleSettingsOverride (Unknown)`. Usually an Editor bug while an AudioClip import inspector or an editor script queries a platform name like "Unknown". Find whether any of our Editor scripts / the audio import step calls `ContainsSampleSettingsOverride`/`GetOverrideSampleSettings` with a bad platform string and fix it; if it's only the Inspector, report and leave it.

## Report
Hashes, final walkSpeed, note in `TechnicalArt/MENU_UNITY_PROGRESS.md`.
