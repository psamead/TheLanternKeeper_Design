# 2026-11-12 Unity — Storyboard polish (skip-jump bug, caption weight/shadow, 4 caption boxes, B5 buttons) + "Press W" prompt + prologue music

Run **before** `2026-11-12_Unity_LanternSwitch_Ladder_Attic_Greybox.md` (separate commits). Demo is shown to students at noon on 2026-11-15.

## First: re-read `AGENTS.md`
Design files from the LAN share `SharedWorkFolder` (GitHub only as a logged "GitHub fallback"). Captures to `SharedWorkFolder/ForDesignScreenshot/2026-11-12_Story_Polish/`. When done, only `00_StartMenu` open — say so.

User markup for this task: `ForDesignScreenshot/2026-11-12_StoryAB_Final/user_markup/user_note_1030_caption_*.png` (orange boxes = where the caption should go). Goal of this round (user): **balanced composition and readable text**.

## 1. Bug: skipping a frame makes the picture jump
When the player presses a key / clicks to go to the next frame (prologue P, A or B), the image suddenly jumps a short distance forward or backward along the zoom direction before the crossfade. Find the cause and fix it. Likely: on advance the outgoing frame's Ken Burns is snapped to its end pose (or restarted), or the incoming frame starts from the wrong pose. Required behaviour: on advance, the **outgoing image freezes at its current transform** for the crossfade; the **incoming image starts at its own start pose** and animates normally. Same for Esc-skip (fade out from the current pose). Verify with a scripted advance at ~30 % and ~80 % of a frame: log the image scale/position on the frame before and after the key press — no discontinuity.

## 2. Caption look (all storyboards: P, A, B)
- Text **a bit bolder**: e.g. TMP material Face Dilate ≈ +0.15–0.2 (or a SemiBold weight of Cormorant Garamond Italic if available in the project — don't add new font files without asking). Keep the colour `#F0EED1`.
- Shadow / underlay **heavier**: darker and a little tighter (underlay colour `#0B1A2E`, alpha ≈ 0.75–0.8, softness lower, small offset ≈ (0.8, −0.8)). Keep the soft caption backplate as is unless it now looks muddy.
- Re-run the inside-the-box check for every frame after this (bolder text is wider).

## 3. Caption boxes — new positions (A2, A4, B1, B4)
Normalized screen coords, (0,0) = bottom-left, end of Ken Burns. Measured from the user's orange boxes. Same rule: every glyph inside, more lines first, then font −15 % max.

| Frame | x min–max | y min–max | Where |
|---|---|---|---|
| A2 | 0.75–0.92 | 0.44–0.62 | sea to the right of the village |
| A4 | 0.71–0.89 | 0.46–0.67 | wall on the right, above the table |
| B1 | 0.06–0.24 | 0.42–0.61 | dark wall left of the window, lower than before |
| B4 | 0.20–0.39 | 0.09–0.30 | over the keeper's dark coat (lower left) |

A1, A3, B2, B3, B5 and all P frames: unchanged.

## 4. EndCard B5 buttons
The Back to Menu / Quit panel currently covers B5's caption ("…To be continued" is cut off). Move the buttons **down**, below the caption: buttons centred, roughly in the band x 0.35–0.65, y 0.58–0.72 (screen-normalized), above Maela's lantern. The whole B5 caption must stay fully visible. Make the panel's dark backplate smaller/softer so it doesn't read as a big box.

## 5. "Press W" pickup prompt (01_Home)
Replace the current bare "W" above the lantern with: the text **"Press W"** inside a **rounded-rectangle outline in the same colour as the text** (thin line, ~2 px at 1080p, corner radius ~8 px, small padding, no fill or a very faint dark fill for readability). Same caption font, small size. Position: centred over the floor lantern at about Maela's head height (where the user drew the red box in `ForDesignScreenshot/…/user_markup` / the screenshot at 10:30 — just above and slightly right of the old "W"). Gentle fade in/out when Maela enters/leaves range. Use the same style for the "Press E" hint after Storyboard A (it currently is plain text).

## 6. Prologue music
The prologue slideshow has no music. Use the existing `TechArtAsset/Audio/Prologue/BGM_Prologue_ArMorDu_loop_v1.ogg` (96 s loop) plus `AMB_Prologue_SeaWind_loop_v1.ogg`, via AudioManager: fade in over 1.5 s when the prologue starts, crossfade (≈1.5 s) into the Home ambience when the prologue ends or is skipped. Check whether Story A / Story B already have music; if B has none, give it the same Ar Mor Du BGM (fade in/out); A keeps the Home ambience lowered (as now). Volumes: BGM ≈ 0.6, ambience ≈ 0.5 of the existing menu levels — report the values. Confirm audible playback (AudioSource.isPlaying + non-zero output, as you did before).

## Test & captures
- Full route once from `00_StartMenu`: skip some frames mid-move (bug check), let others play out.
- Screenshots → `ForDesignScreenshot/2026-11-12_Story_Polish/`: every P/A/B frame at end of move with captions (`P1_end.png` … `B5_end.png`), `B5_buttons.png`, `press_w.png`, `press_e.png`. Recorder clips of P, A, B: `StoryP_polish.mp4`, `StoryA_polish.mp4`, `StoryB_polish.mp4` (with audio).
- Report: skip-bug cause + before/after numbers; caption bounds table (all 13 frames); music volumes.

## Commit
"Storyboard polish + Press W prompt + prologue music", push, note in `TechnicalArt/MENU_UNITY_PROGRESS.md`. Only `00_StartMenu` open at the end.
