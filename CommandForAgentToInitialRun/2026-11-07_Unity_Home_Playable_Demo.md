# Task: Playable Home demo — Maela walks/jumps in a placeholder room (2026-11-07, needed for class TODAY)

Unity project **`TheLanternKeeper2D`**. Re-read `AGENTS.md`. Keep it simple and working; polish later.

## Already done by Claude (not committed)
- `Assets/_Project/Scripts/PlayerController.cs` — Input System (A/D or ←/→ move, Space/W/↑ jump with coyote time + buffer + short hop, **E** fires `RaiseLantern`). Drives the Maela Animator params `Speed`, `Grounded`, `VelY`, `RaiseLantern`. Flips the visual child via `scale.x`.
- `Assets/_Project/Art/Scenes/Home/Home_Present_placeholder_v0.png` (2400×1080, **floor top 160 px from the bottom**) and `Crate_placeholder_v0.png` (130×110). Code-drawn placeholders; painted art will replace them with the same floor line.

## UPDATE 09:40 — use the painted background
- Use **`Assets/_Project/Art/Scenes/Home/Home_Present_v1.png`** (2520×1080, Midjourney, painted) instead of the placeholder → **25.2 × 10.8 units**. The room has perspective; the walk line is the front of the floor, **ground top at y = −4.0** (140 px above the bottom). Walls at x = ±12.6, camera confiner (−12.6, −5.4)…(12.6, 5.4). Keep the placeholder PNG in the project as a fallback.
- Adjust the ground y by eye if Maela's boots look like they float or sink (aim: soles about 1/3 of the way down the visible floor). Report the final value.

## Steps
1. Ask the user to save; commit "Before Home playable demo" and push.
2. Import both PNGs: Sprite, **PPU 100**, Bilinear, no mips, Compression None, pivot Center. → background = 24 × 10.8 units.
3. In `01_Home` (remove the "01_Home / Esc → menu" centre text from view or move it to a small corner label; keep Esc → menu working):
   - `Background` sprite at (0, 0), sorting layer/order behind everything. Floor top is therefore at **y = −3.8**.
   - `Ground`: empty GameObject + BoxCollider2D, top edge at y = −3.8, width 24 (x −12…12), layer **Ground** (create it).
   - `WallL` / `WallR`: BoxCollider2D at x = −12 and x = +12, tall, layer Ground.
   - `Crate`: sprite at about (−1.5, −3.8 + 0.55) with BoxCollider2D, layer Ground — something to jump on.
4. Player: new GameObject `Player` at (−8, −3.8) with **Rigidbody2D** (Dynamic, Gravity Scale 2.5, Continuous, Freeze Rotation Z), **CapsuleCollider2D** (size ≈ 0.45 × 1.5, offset y 0.75 so the bottom is at the feet), `PlayerController` (Ground Mask = Ground, Ground Box Size 0.3 × 0.06). Put the existing `Maela` prefab instance as a **child at (0,0)**; assign Animator + visual (the Maela child). Use a frictionless PhysicsMaterial2D on the capsule so she doesn't stick to walls.
5. Camera: Cinemachine Camera follows `Player` (Position Composer, small dead zone, damping ≈ 0.3), orthographic size so the room height fits (≈ 5.4), plus **CinemachineConfiner2D** with a PolygonCollider2D matching the background bounds (−12,−5.4)…(12,5.4).
6. Lighting: keep the dark-blue look. Global Light 2D colour **#8FA3BF**, intensity 0.8 (HANDPAINTED_SPEC §4); Maela's lantern light stays.
7. Play test at 1920×1080: walk both ways, jump onto the crate and off, press E. Fix only scene/physics values; **do not touch `Maela.psb`, the prefab's sprite positions, or animation clips.** If something in `PlayerController` must change, keep the change minimal and list it.
8. Record ~15 s video → `SharedWorkFolder/ForDesignScreenshot/2026-11-07_Home_Playable.mp4`. Commit "Home: playable placeholder room + PlayerController" and push; note hash in `TechnicalArt/MENU_UNITY_PROGRESS.md`.
