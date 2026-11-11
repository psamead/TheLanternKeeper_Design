# 2026-11-12 Unity — LanternSwitch (present / memory) + broken ladder + attic (greybox)

**Deadline context**: the Demo is shown to students at noon on **2026-11-15** and should be basically complete by then. This is the core mechanic — keep it simple, robust, and data-driven so the real art can be dropped in later by swapping sprites only.

Run this **after** `2026-11-11_Unity_StoryAB_InterimArt.md` (separate commits).

## First: re-read `AGENTS.md`
Rules for this task: design files from the LAN share `SharedWorkFolder` (GitHub only as a logged "GitHub fallback"); captures to `SharedWorkFolder/ForDesignScreenshot/2026-11-12_LanternSwitch/`; **when done, unload extra scenes, leave only `00_StartMenu` open** and say so.

Read: DEMO_IMPLEMENTATION_PLAN §3 rows ②–⑤, §4 (lantern switch rules — already decided, follow exactly), §5 (`LanternSwitch`, `WorldLayerObject`, `GameState`); HANDPAINTED_SPEC §4 "两层世界".

## 0. Small art refresh (do first, own commit)
- Re-copy `TechArtAsset/Storyboard/LanternOrigin_A/SB_A4.png` and `TechArtAsset/Storyboard/Ending_B/SB_B1.png` from the share over the Unity copies (same names/GUIDs) — both were replaced with final versions on 11-12.
- Your last report said the storyboard source images were **2048×1152**. The files on the share are **2208×1242** (15 % margin for Ken Burns). Check every storyboard texture (P, A, B): source file must be 2208×1242 and the importer must not downscale it (Max Size 4096, no NPOT scaling). If anything was resized on copy, re-copy the originals. Report the actual sizes.

## What to build

### 1. GameState + LanternSwitch
- `GameState.MemoryLayer` (bool). `LanternSwitch` (in Core_Persistent): toggles it on **E**, only when `HasLantern`.
- Rules (DEMO §4, decided 11-08): **first switch** = full long bell, all input locked until the bell ends, *then* the world changes. **Later switches** = world changes immediately + bell; player can move/jump during the bell, but **E is ignored** (no switch, no queue, no sound) until the bell has ended.
- Event `OnWorldSwitched(bool isMemory)`. Global Light 2D colour/intensity: present = current cold blue; memory = warm gold (HANDPAINTED_SPEC; start from `#F2C48A`, intensity +15 %). Blend over **0.6 s** (not a hard cut).
- Reset on Back to Menu (already resets `MemoryLayer=false`; keep).

### 2. WorldLayerObject
- Component with enum `Present / Memory / Both`. On `OnWorldSwitched`: Present objects visible+collidable only in present, Memory only in memory. Fade SpriteRenderers over the same 0.6 s; colliders switch at the moment of the switch.
- **Background**: add a second background sprite slot `Home_Memory_bg` (same size/position as the present background) tagged Memory; present background tagged Present. For now the memory background = a **warm-tinted duplicate** of the present background (tint `#F2C48A` multiply) — real art `TechArtAsset/Scenes/Home/Memory/Home_Memory_v1.png` will replace it with the same transform.

### 3. Broken ladder → attic (greybox, coloured blocks, clearly placeholder)
- Put the ladder at the right part of the room (use the ladder area visible in the present background if it fits; otherwise right of the crate). Make it clearly readable in greybox colours:
  - `Ladder_Broken` (Present): short stump, bottom half only, grey-brown. Not climbable. If the player presses **W/Up** at it in present: show a one-line hint above Maela for 2.5 s: *"The ladder is broken."*
  - `Ladder_Whole` (Memory): full ladder to the attic hatch, warm brown. Climbable with **W/Up** (hold), **S/Down** to go down; gravity off while on the ladder; Space jumps off. Simple climb pose: reuse Idle/JumpUp, no new animation needed.
- **Attic**: a small room directly above the Home room (greybox floor, walls, sloped roof blocks), reached through a hatch at the ladder top. One small **square window** on the attic's far wall (placeholder rectangle with a dark lighthouse silhouette behind it is enough). Extend the Cinemachine confiner so the camera follows Maela up into the attic and frames the attic (attic only — don't show the room below).
- If the player switches back to present **while on the ladder or in the attic**: keep it fair — present attic stays walkable (it exists in both layers); only the ladder changes. If Maela is on the ladder when it disappears, drop her safely to the floor (no falling through, no softlock).

### 4. End trigger → attic window
- Move `EndTrigger_TEMP` to the attic window and rename it `EndTrigger_AtticWindow`. It fires when Maela stands at the window (any layer) → same fade → `03_EndCard` as now. Remove the far-right temporary trigger.

### 5. Hints (minimal, in-world text, same caption font, small)
- After Storyboard A: existing "Press E" hint stays.
- First time in memory layer: *"The ladder is whole here."* near the ladder, 3 s, once.

## Test (Play Mode, from `00_StartMenu` only)
1. Full route: menu → prologue → Home → W pickup → A → E (first switch: long bell, locked, then warm world) → climb ladder → attic → window → EndCard B → Back to Menu. Then a second full route to check reset.
2. Switch spam: press E repeatedly during the bell → ignored; after the bell → works.
3. Broken ladder message in present; switch to present while on the ladder → safe drop.
4. Speed sanity (from the previous task): Maela run speed and one storyboard frame duration still correct.
Screenshots → `ForDesignScreenshot/2026-11-12_LanternSwitch/`: `present_room.png`, `memory_room.png`, `broken_ladder_hint.png`, `climbing.png`, `attic.png`, `window_trigger.png`. Record the switch moment with Unity Recorder if possible (Recorder can't take keyboard input — a scripted test that triggers the switch is fine).

## Commit
"LanternSwitch + ladder + attic greybox", push, note hash + any decisions in `TechnicalArt/MENU_UNITY_PROGRESS.md`; tick DEMO §7 "色块搭 Home（楼下、断梯、阁楼）" and "LanternSwitch + 冷暖光照 + WorldLayerObject" only if verified. Leave only `00_StartMenu` open.
