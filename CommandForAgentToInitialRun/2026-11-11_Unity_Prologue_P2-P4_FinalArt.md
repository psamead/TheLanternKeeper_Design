# 2026-11-11 Unity — Prologue P2–P4 final art (replace placeholders)

Design repo: pull `psamead/TheLanternKeeper_Design` (main) first. Final art (all 2208×1242 RGB, same as SB_P1):
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
6. Play Mode: menu → prologue P1–P4 → Home. Screenshot each frame at the end of its Ken Burns into `SharedWorkFolder/ForDesignScreenshot/2026-11-11_Prologue_FinalArt/` (`P2_end.png` …). User records the video manually.
7. Commit "Prologue P2–P4 final art", push, note hash in `TechnicalArt/MENU_UNITY_PROGRESS.md`. Also commit the pending items from earlier notes (`UniversalAdditionalCameraData`, synced `AGENTS.md`) if still uncommitted.
