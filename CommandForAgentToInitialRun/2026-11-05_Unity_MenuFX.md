# Task: Start menu motion — drifting fog + lantern breathing glow (2026-11-05)

Unity project **`TheLanternKeeper2D`**, scene `00_StartMenu` only. Re-read `AGENTS.md`. Visual target: `SharedWorkFolder/TechArtAsset/Menu/FX/MENU_FX_preview_v2.mp4` (user approved: fog as is, stronger breathing).

## Already done by Claude (not committed)
- Textures in `Assets/_Project/Art/Menu/FX/`: `MENU_FX_Fog_A.png` (2048×512, big soft banks), `MENU_FX_Fog_B.png` (2048×256, thin wisps), `MENU_FX_LanternGlow.png` (512², warm radial). Fog textures tile horizontally.
- Scripts in `Assets/_Project/Scripts/`: `UVScroll.cs` (scrolls a RawImage), `LanternGlowPulse.cs` (alpha + scale breathing with flicker). Defaults already match the approved preview — do not change the numbers.

## Steps
1. Ask the user to save (Ctrl+S); only `00_StartMenu` open. Commit "Before menu FX" and push.
2. Import settings: all three = Texture Type **Default** for the fogs (Wrap Mode **Repeat**, Filter Bilinear, no mip maps, Compression None, Alpha Is Transparency on); the glow = **Sprite (2D and UI)**, Clamp, no mips, Compression None.
3. In `Canvas`, add between `BG` and `LeftDark` (sibling order exactly: BG → FogA → FogB → LanternGlow → LeftDark → Title → MenuButtons …). All three: Raycast Target **off**.

| Object | Component | Rect (1920×1080 reference, origin top-left) | Script |
|---|---|---|---|
| `FogA` | RawImage, texture Fog_A, colour white, alpha 0.9 | stretch horizontally (left 0, right 0), top y = 260, height 600 | `UVScroll` speed 14, displayWidth 2400 |
| `FogB` | RawImage, texture Fog_B, alpha 0.9 | stretch horizontally, top y = 640, height 300 | `UVScroll` speed 26, displayWidth 2400 |
| `LanternGlow` | Image, sprite LanternGlow, colour white | centre at **x = 1591, y = 373**, size 440×440 | `LanternGlowPulse` (defaults) |

   For the RawImages set `uvRect` width = 1920 / 2400 = **0.8**, height 1 (so one texture repeat spans 2400 px).
4. Play Mode check at 1920×1080 against the preview: fog drifts right slowly, two speeds, seamless (no jump/seam); glow sits exactly on the lantern and clearly breathes (≈3.2 s); title, buttons, icon and underline unaffected; mouse hover/click still work (raycast off on FX). Edit Mode preview of the menu still correct.
5. Restore TMP auto-changed font assets (`LiberationSans SDF - Fallback.asset`, `Cinzel SDF Generated.asset`) — do not commit them. Commit "Menu FX: drifting fog + lantern breathing glow" and push. Append a dated note with the hash to `SharedWorkFolder/TechnicalArt/MENU_UNITY_PROGRESS.md`.
