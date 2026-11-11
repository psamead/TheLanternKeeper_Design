# 2026-11-11 Unity — Prologue P2–P4 final art (replace placeholders)

Read from the LAN share `SharedWorkFolder` (path in AGENTS.md); GitHub only as a logged fallback (see AGENTS.md). Final art (all 2208×1242 RGB, same as SB_P1):
- `TechArtAsset/Storyboard/Prologue/SB_P2.png` — fog over the harbour village, one distant lit window (near houses dark on purpose)
- `TechArtAsset/Storyboard/Prologue/SB_P3.png` — Maela from behind at the cottage door, lighthouse dark
- `TechArtAsset/Storyboard/Prologue/SB_P4.png` — Grandma in the rocking chair, Maela from behind; cool teal room, warm floor light

## Steps
1. Copy the three PNGs into `Assets/_Project/Art/Storyboard/Prologue/` (names `SB_P2.png`, `SB_P3.png`, `SB_P4.png`, next to the `_placeholder` files; do not delete the placeholders yet).
2. Import settings = same as `SB_P1.png`: Sprite, PPU 100, no mips, Compression High Quality, Max Size 4096, Read/Write off.
3. In `Assets/_Project/Data/Storyboard/SB_Prologue.asset` point frames P2/P3/P4 to the new sprites. Captions unchanged.
4. Ken Burns (check nothing important gets cropped at the end of the move):
   | Frame | Zoom | Pan | Note |
   |---|---|---|---|
   | P2 | 1.08 → 1.00 | (0.15, 0) → (0, 0) | pull back; keep the distant lit window and fog mound in frame |
   | P3 | 1.00 → 1.08 | (0, 0) → (0.1, 0.05) | drift toward Maela / lighthouse (right); never crop her boots |
   | P4 | 1.00 → 1.10 | (0, 0) → (-0.1, 0) | slow push toward Grandma's face (left) |
5. Caption check: two caption lines sit in the sky / upper wall area with colour `#F0EED1` + soft underlay (same as P1). If a caption is hard to read on P2 (bright cyan sky), raise underlay alpha to ~0.6 for that frame only.
6. Play Mode: menu → prologue P1–P4 → Home. Screenshot each frame at the end of its Ken Burns into `SharedWorkFolder/ForDesignScreenshot/2026-11-11_Prologue_FinalArt/` (`P2_end.png` …).
6b. **Record the prologue with Unity Recorder** (package `com.unity.recorder` 5.1.7 is already installed — do not add another version). The prologue plays by itself, so no input is needed:
   - Window ▸ General ▸ Recorder ▸ Recorder Window → add **Movie** recorder: Source = Game View, 1920×1080, 30 fps, MP4 (H.264), Quality High, **Capture Audio ON**.
   - Recording mode: Manual (or Time Interval covering the whole prologue + 2 s of Home). Start Play directly from the prologue scene (or the Core_Persistent bootstrap that loads it — whatever the normal flow uses), stop after Home has loaded.
   - Output: `SharedWorkFolder/ForDesignScreenshot/2026-11-11_Prologue_FinalArt/Prologue_P1-P4_recorder.mp4`.
   - Do not commit Recorder settings assets that contain absolute paths; if Recorder creates a settings asset under `Assets/`, either leave it untracked or set a project-relative output path.
   - The menu (PLAY press) and walking in Home still need real input — the user records those parts manually.
7. Commit "Prologue P2–P4 final art", push, note hash in `TechnicalArt/MENU_UNITY_PROGRESS.md`. Also commit the pending items from earlier notes (`UniversalAdditionalCameraData`, synced `AGENTS.md`) if still uncommitted.
