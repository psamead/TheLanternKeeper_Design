> **Done (Unity `75aec35`).** The interim-art note (step −1) and the scene-cleanup step were added after Codex ran it; they are carried out in `2026-11-11_Unity_StoryAB_InterimArt.md`.

# 2026-11-11 Unity — Lantern pickup → Storyboard A; end trigger → 03_EndCard → Storyboard B (placeholders)

Goal: the Demo loop plays start-to-end with placeholders: Menu → Prologue → Home → pick up lantern → **Storyboard A** → "E" hint → (temporary) end trigger → **03_EndCard: Storyboard B** → "To be continued…" → Back to Menu. Real A/B art and the attic/memory layer come later with the same names.

`git pull` the design repo first. Read DEMO_IMPLEMENTATION_PLAN §3 (flow), §4 (mechanics), §5 (scripts), §6 (captions).

## Inputs (design repo)
- `TechArtAsset/Storyboard/LanternOrigin_A/placeholder/SB_A1..A4_placeholder.png` (2208×1242)
- `TechArtAsset/Storyboard/Ending_B/placeholder/SB_B1..B5_placeholder.png` (2208×1242)
- Captions: DEMO_IMPLEMENTATION_PLAN §6 tables A and B (copy text exactly).

## Steps
-1. Interim real art is already in the design repo for some frames — use it instead of the placeholder where it exists: `TechArtAsset/Storyboard/LanternOrigin_A/SB_A4.png`, `TechArtAsset/Storyboard/Ending_B/SB_B1..B5.png` (all 2208×1242). Frames without real art (A1–A3) keep the placeholder. Later versions will replace these files with the same names.
0. Cleanup: the `CAPTION_BOUNDS PASS …` Debug.Log lines from the caption check must not print in normal Play Mode — remove them or put them behind a `[SerializeField] bool logCaptionBounds` (default off) / editor menu item.
1. Import placeholders → `Assets/_Project/Art/Storyboard/LanternOrigin_A/` and `Assets/_Project/Art/Storyboard/Ending_B/`, same import settings as the prologue art.
2. Create `SB_LanternOrigin_A.asset` and `SB_Ending_B.asset` (same ScriptableObject type as `SB_Prologue`). Per frame: duration 6 s (B5: 8 s), gentle Ken Burns (zoom 1.00 → 1.06, alternate pan direction), caption rect = the **P1 default** for now (we'll place boxes after the real art). Caption colour/underlay same as prologue.
3. **Lantern on the floor** (01_Home, near the rocking chair / "grandpa's old box" area, left of the crate): placeholder sprite = duplicate of Maela's lantern part (or a simple code-drawn lantern), small Point Light 2D, faint pulse. Name the GameObject `Lantern_Pickup`.
   - `Interactable` trigger: when Maela is close, show a small prompt "W" above it; press **W** → pick up.
   - On pickup: `GameState.HasLantern = true`; hide `Lantern_Pickup`; show Maela's hand Lantern part + its Point Light 2D (both hidden before pickup — DEMO §4); then play **Storyboard A** as an overlay (player input locked; Home stays loaded underneath, no scene reload). Esc skips; any key = next.
   - After A ends: unlock input, show hint "Press E" (fade out after ~4 s or on first E). LanternSwitch itself is a later task: for now E only plays the existing lantern raise + bell (current behaviour) — do not build the memory layer yet.
   - Before pickup, E does nothing (no raise, no bell).
4. **Temporary end trigger**: a trigger volume `EndTrigger_TEMP` at the far right end of the walkable floor, active only when `HasLantern` is true. Entering it → fade out → load `03_EndCard`. (Later this moves to the attic window, reachable only in the memory layer.) Mark it clearly TEMP in the name and in a code comment.
5. **03_EndCard**: on load, play **Storyboard B** (B1–B5). After B5, show the title-card line "Six days until Anaon night. To be continued…" already in B5's caption — then show two buttons in the menu style: **Back to Menu** (→ 00_StartMenu, reset `GameState`: HasLantern=false, MemoryLayer=false) and **Quit**. Esc during B skips to the buttons. Keep 03_EndCard in Build Settings; make sure Core_Persistent objects (Maela, camera follow) don't show / don't receive input in the EndCard.
6. Audio: reuse what exists — storyboard A over the Home ambience (lowered ~50 %); storyboard B can use the prologue BGM. No new audio files.
7. Play Mode test the full loop twice (second time from Back to Menu, to check GameState reset). Screenshots into `SharedWorkFolder/ForDesignScreenshot/2026-11-11_Lantern_StoryA_EndCard/` (`pickup_prompt.png`, `A1.png`, `E_hint.png`, `B1.png`, `B5_buttons.png`). Record Storyboard A and B with Unity Recorder if possible (they play without input) → same folder. File-location rule in AGENTS.md applies.
8. **Before finishing: unload every extra scene** you opened or loaded additively; leave the Editor with only `00_StartMenu` open and no leftover DontDestroyOnLoad test objects (AGENTS.md rule, 11-11 — the last run left many scenes loaded and the Editor ran at half speed). Say so in the report.
9. Commit "Lantern pickup + Storyboard A + EndCard B (placeholders)", push, note hash in `TechnicalArt/MENU_UNITY_PROGRESS.md`; tick DEMO_IMPLEMENTATION_PLAN §7 items only where verified (pickup ☑, StoryboardPlayer A/B + EndCard ☑ (placeholders)).
