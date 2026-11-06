# Task: Import Maela (.psb), rig her, Idle animation test (2026-11-06)

Unity project **`TheLanternKeeper2D`**. Re-read `AGENTS.md`. Goal: see Maela move in the game so the user can judge which cut-out details still need art fixes. **No movement code yet** — only import, rig, Idle, and a static placement in `01_Home`.

## Already done by Claude (not committed)
- `Assets/_Project/Art/Characters/Maela/Maela.psb` — 149×320 px, painted at **2×**. One group `Maela`, 19 layers (top → bottom):
  Lantern, Hand_R, Arm_Lower_R, Arm_Upper_R, Hair_Front, Head, Coat_Body, Coat_Hem, Dress, Boot_R, Leg_Lower_R, Leg_Upper_R, Boot_L, Leg_Lower_L, Leg_Upper_L, Hand_L, Arm_Lower_L, Arm_Upper_L, Hair_Back.
  `Arm_Upper_L` / `Arm_Lower_L` are **empty on purpose** (placeholders; art comes later) — skip them if the importer drops them, do not treat it as an error.
- Commit this .psb in the Unity repo (it is the game asset; the large `Maela_src.psd` stays in the design folder).

## Steps
1. Ask the user to save (Ctrl+S); only `01_Home` open. Commit "Before Maela import" and push.
2. PSD Importer settings on `Maela.psb`: Texture Type Sprite, **Pixels Per Unit = 200** (2× source → 1.6 units tall, matches HANDPAINTED_SPEC §1), Filter Bilinear, Mip Maps off, Compression **None**, Mosaic on, **Use Layer Group on**, **Character Rig on**, Main Skeleton none. Apply.
3. Rig as a **cut-out (rigid) skeleton** — every sprite 100 % weighted to one bone, no mesh deformation. In the Skinning Editor create bones at the pivots below, then Auto Geometry + Auto Weights is fine, but afterwards make sure each sprite is bound to **only its own bone** (rigid). If the Skinning Editor cannot be driven reliably, use the fallback: import with Character Rig **off**, instantiate the layers as child GameObjects and build a Transform hierarchy with the same pivots (move each sprite so its joint sits on the parent Transform's origin). Either way, report which method you used.

   Pivot positions in **.psb pixels, origin = top-left of the 149×320 canvas** (convert: x_unit = (x − 59)/200, y_unit = (206 − y)/200 relative to Hip):

   | Bone | x | y | Parent | Sprites bound |
   |---|---|---|---|---|
   | Hip (root) | 59 | 206 | — | Dress, Coat_Hem |
   | Body | 59 | 206 | Hip | Coat_Body |
   | Head | 69 | 70 | Body | Head, Hair_Front, Hair_Back |
   | Shoulder_R | 89 | 93 | Body | Arm_Upper_R |
   | Elbow_R | 102 | 123 | Shoulder_R | Arm_Lower_R |
   | Wrist_R | 124 | 123 | Elbow_R | Hand_R |
   | Lantern | 130 | 127 | Wrist_R | Lantern |
   | Shoulder_L | 64 | 86 | Body | Arm_Upper_L |
   | Elbow_L | 53 | 144 | Shoulder_L | Arm_Lower_L, Hand_L (wrist at 50,184) |
   | Thigh_R | 66 | 206 | Hip | Leg_Upper_R (knee at 66,247) |
   | Shin_R | 66 | 247 | Thigh_R | Leg_Lower_R (ankle at 64,278) |
   | Foot_R | 64 | 278 | Shin_R | Boot_R |
   | Thigh_L | 52 | 206 | Hip | Leg_Upper_L (knee at 48,245) |
   | Shin_L | 48 | 245 | Thigh_L | Leg_Lower_L (ankle at 42,276) |
   | Foot_L | 42 | 276 | Shin_L | Boot_L |

   Sorting: one `SortingGroup` on the root; keep the layer order above (Lantern on top, Hair_Back at the bottom).
4. Prefab `Assets/_Project/Prefabs/Maela.prefab`: root at the feet (move the rig so the boot soles sit on y = 0 of the root). Add a child `LanternLight` = **Point Light 2D** on the Lantern bone at the glass centre (≈ x 130, y 210 px), colour **#FFF1C9**, outer radius **3**, intensity 1.
5. Animator Controller `Maela.controller` with one state **Idle** (`Maela_Idle.anim`, loop, 3.0 s):
   - Body: rotate 0 → −1.5° → 0 (breathing lean) and position y +0.006 at the middle.
   - Head: rotate 0 → +2° → 0, offset ¼ cycle from Body.
   - Lantern: rotate −3° → +3° → −3° (gentle swing, ease in/out).
   - LanternLight: intensity 0.9 → 1.1 → 0.9.
   - Everything else still. Keep curves smooth (auto tangents).
6. Place one instance in `01_Home` at (0, −2), facing right; temporarily add a second instance with **flipX via scale.x = −1** at (3, −2) to check the mirrored look. Keep the scene's dark-blue background so the warm light is visible.
7. Play Mode check at 1920×1080: Maela ≈ 1.6 units tall (≈ 160 px on screen); no gaps at elbow/shoulder/knee joints while idling; lantern swings from the handle top; light follows the lantern. Take two screenshots (normal + mirrored, plus one close-up of the arm/lantern) and save them to `SharedWorkFolder/ForDesignScreenshot/2026-11-06_Maela_Idle_*.png`. Also record a 5-second clip if possible (Unity Recorder is fine if installed; skip otherwise).
8. Remove the mirrored test instance, keep the normal one. Restore TMP auto-changed font assets (do not commit them). Commit "Maela: import psb, cut-out rig, Idle" and push. Append a dated note with the hash, the rig method used, and any problems to `SharedWorkFolder/TechnicalArt/MENU_UNITY_PROGRESS.md`.

## Do not
- Do not edit the .psb or repaint anything — report art problems (gaps, wrong cuts, missing pieces) in the progress note instead; Claude fixes art in the design folder.
- No player controller, input, Cinemachine follow or collision in this task.
