# Task: Maela Run / JumpUp / Fall / Lantern animations (2026-11-07)

Unity project **`TheLanternKeeper2D`**. Re-read `AGENTS.md`. **Animation only — the art (`Maela.psb`, its import settings, sprite rects, prefab sprite positions) must not change.** (Lesson LESSONS_ART_PIPELINE §8: any change to a layer's bounds breaks the rig.)

## Already done by Claude (not committed)
- `Assets/_Project/Editor/MaelaAnimBuilder.cs` — menu **Tools ▸ Lantern Keeper ▸ Build Maela Animations**. Generated from `SharedWorkFolder/TechArtAsset/Characters/Maela/_work/anim_v1/poses.py` (do not hand-edit; ask Claude to change poses). Previews: `_work/anim_v1/*.gif`, `contact_sheet.png`.
- It creates/overwrites `Maela_Run.anim` (0.5 s loop), `Maela_JumpUp.anim` (0.3 s, holds), `Maela_Fall.anim` (0.6 s loop), `Maela_Lantern.anim` (1.1 s, raise lantern + LanternLight intensity peak 2.4), and adds to `Maela.controller`:
  - Parameters: `Speed` (float, abs horizontal speed), `Grounded` (bool), `VelY` (float), `RaiseLantern` (trigger).
  - Idle ⇄ Run on Speed 0.1; Idle/Run → JumpUp (airborne, VelY>0) / Fall (airborne, VelY<0); JumpUp → Fall when VelY<0; Fall → Idle/Run on landing; Idle/Run → Lantern on trigger, back to Idle at exit time 0.95.
  - Curves animate only Transform `localEulerAnglesRaw.z`, `Hip` `m_LocalPosition.y`, and Light2D `m_Intensity`. Idle is untouched.

## Steps
1. Ask the user to save; commit "Before Maela run/jump anims" and push.
2. Let Unity compile; run the menu item once. Fix compile errors only if trivial (e.g. Light2D namespace) and report them.
3. Check each clip in the Animation window on the `Maela` prefab: no sprite separation at shoulder / elbow / knee beyond ~1 px at game size; lantern hangs from the hand. If the builder logs missing paths, report them (paths must match the prefab: `Hip/Body/Shoulder_R/Elbow_R/Wrist_R/Lantern` etc.).
4. If `PlayerController` already exists, feed the 4 parameters from Rigidbody2D (Speed = |vx|, VelY = vy, Grounded from ground check) and fire `RaiseLantern` from the lantern-switch input. If it does not exist yet, skip — the programmer task wires it.
4b. **Priority this round = Run.** In `01_Home`, preview Maela_Run at real game size (Game view 1920×1080, Maela ≈ 160 px). Record a 3–5 s clip or 4 screenshots and look specifically for gaps between skirt and thighs and behind the right shoulder. Report which gaps are still visible at game size — Claude will then add **new** patch layers (existing layers stay untouched) only where needed.
5. Play Mode screenshots (run, jump peak, fall, lantern raised) → `SharedWorkFolder/ForDesignScreenshot/2026-11-07_Maela_Anim_*.png`.
6. Commit "Maela: Run / JumpUp / Fall / Lantern animations" and push; append hash + problems to `TechnicalArt/MENU_UNITY_PROGRESS.md`.

## Do not
- Do not touch `Maela.psb`, its .meta, or sprite child positions in the prefab. Report art problems instead.
