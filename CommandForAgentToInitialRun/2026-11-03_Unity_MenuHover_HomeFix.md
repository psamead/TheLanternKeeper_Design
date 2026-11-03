# Task: Menu hover sound restart + Home placeholder fix (2026-11-03)

Unity project **`TheLanternKeeper2D`**. Re-read `AGENTS.md` first. Small task; one commit.

## Background (from user testing)
- Moving the mouse quickly over Play / Settings / Quit stacks wave sounds: `MenuAudio.PlayHover()` uses `PlayOneShot`, so old waves keep playing. Wanted: **a new hover sound restarts; the previous one stops.**
- The Editor had `01_Home` open **additively** next to `00_StartMenu` (left from the earlier label edit). In Play Mode both scenes ran: the Home label drew over the menu, and the Console filled with "2 audio listeners / 2 event systems". This is an Editor scene-setup issue, not a code bug.
- After the label was removed, `01_Home` is completely black (camera + empty canvas). Expected for now, but the user wants a visible placeholder.

## Steps
1. Ask the user to save open scenes (Ctrl+S). In the Hierarchy, **remove `01_Home` from the Editor scene setup** (right-click → Remove Scene) so only `00_StartMenu` is open. Do not open other scenes additively again; open them one at a time (`Single`).
2. `MenuAudio`: hover gets its **own AudioSource** (`hoverSource`, 2D, not Play On Awake). In `PlayHover()`:
   - pick the clip as now (no immediate repeat, pitch 0.97–1.03 on `hoverSource.pitch`);
   - if `hoverSource.isPlaying`, fade it out over ~0.04 s (coroutine, unscaled time) and stop it, then set `clip`, `volume = 0.6`, `Play()` from the start. Keep it simple: one running fade coroutine at a time; stop it before starting a new one.
   - Confirm and back sounds stay on the existing source with `PlayOneShot` (they must not be cut by hover). Starting confirm should also stop the hover source (quick fade) so the lantern "ting" is clean.
3. `01_Home` placeholder: put back a small, clearly temporary label so the scene is not black — bottom-left, Cinzel 28 px, colour `#F2EBDD` at 60 % alpha: `01_Home — placeholder · Esc → menu`. Background colour of the Home camera: `#1E2633` (palette dark blue) instead of black.
4. Play Mode check (start from `00_StartMenu` only): no "2 audio listeners / 2 event systems" messages; sweep the mouse fast across the three items — only one wave plays at a time, restarting each time; confirm Play → lantern sound, fade, `01_Home` shows dark blue + label; Esc returns to menu.
5. Also restore the TMP fallback font asset change (`LiberationSans SDF - Fallback.asset`) — do not commit it.
6. Commit "Menu hover restarts; Home placeholder" and push. Append a dated note to `SharedWorkFolder/TechnicalArt/MENU_UNITY_PROGRESS.md`.
