# 2026-11-11 Unity — Home crate: replace placeholder with painted Crate_v1

Design repo (pull first): `TechArtAsset/Scenes/Home/Props/Crate_v1.png` — 520×440 RGBA, transparent background, crate bottom edge = image bottom row. Visible crate is ~436×440 px, centred horizontally (≈42 px transparent margin left and right). Already cooled to the Home night palette; edges defringed (checked on magenta).

## Steps
1. Copy to `Assets/_Project/Art/Scenes/Home/Crate_v1.png` (keep `Crate_placeholder_v0.png` for now). Import: Sprite (Single), **pivot Bottom Center**, no mips, Bilinear, Compression High Quality, Read/Write off.
2. PPU: choose so the crate keeps its current on-screen size — i.e. the visible crate height in world units equals the current placeholder height (placeholder was 110 px tall; compute PPU from the placeholder's current PPU × scale; report the value). Do not change the Crate transform scale if you can avoid it; prefer PPU.
3. Swap the `Crate` SpriteRenderer to `Crate_v1`. Keep sorting layer/order. Make sure the bottom of the crate sits on the floor line (Ground Y) — no floating, no sinking.
4. Resize the `BoxCollider2D` to the **visible** crate (exclude the transparent side margins; top = top plank, not the rope). Player must still be able to jump on and off it.
5. Optional, only if it looks floating: add a soft dark contact shadow (simple ellipse sprite, alpha ~0.35) under the crate, behind it.
6. Play Mode at 1920×1080: walk past, jump on/off. Screenshots → `SharedWorkFolder/ForDesignScreenshot/2026-11-11_Home_Crate/crate_v1_idle.png`, `crate_v1_player_on_top.png`. (File-location rule in AGENTS.md: if the share cannot be written, use `TheLanternKeeper2D/_CodexCaptures/2026-11-11_Home_Crate/` and copy over.)
7. Commit "Home crate v1 art", push, note hash + PPU in `TechnicalArt/MENU_UNITY_PROGRESS.md`.
