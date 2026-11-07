# Task: Home scale fix + P1 final art + push (2026-11-07, needed for class demo — keep it quick)

Unity project **`TheLanternKeeper2D`**. Re-read `AGENTS.md`.

## Why
The previous camera task was done correctly; the problem is **scale**: the painted Home background shows full-size furniture, but Maela was built for a far wide view (1.6 units). With the closer camera the chair seat reaches her chest and the door is 3× her height, so she looks shrunk. Decision (design, 11-07): make the room read as a normal house — **bigger Maela, slightly smaller room**. No art files change.

## Steps
1. Ask the user to save; commit "Before Home scale fix".
2. **Maela ×1.4**: on the `Player` object scale the **Maela visual child** to (1.4, 1.4, 1) — keep the sign of x for facing (PlayerController flips `scale.x` by sign and keeps its magnitude, so set 1.4 / −1.4, not 1). Resize the CapsuleCollider2D to match (≈ 0.63 × 2.1, offset y ≈ 1.05). Ground-check box can stay. If jumping now looks too low, raise `jumpVelocity` a little (≈ 7.5–8) and report the value. Maela's Point Light 2D outer radius ×1.4 (≈ 4.2) so the lantern glow keeps its size relative to her.
3. **Background ×0.8**: scale `Background` to 0.8 → 20.16 × 8.64 units. Move/resize to keep the floor walk line under her boots (new ground top ≈ old ground y × 0.8 if the background is centred at 0; adjust by eye so boot soles sit on the front of the floor). Walls at x ≈ ±10.08; Confiner2D polygon to the new background bounds. Crate: scale ×1.4 so it is a box she can jump onto, collider matching.
4. Camera: keep orthographic size in **3.5–3.8**; pick the value where Maela is ≈ 1/4–1/3 of screen height and the room still scrolls. Report it.
5. Check by eye (Game view 1920×1080): rocking chair seat ≈ her thigh/hip height; door ≈ 2× her height. Walk the whole room, jump onto the crate, press E. No camera jitter at edges.
6. **Prologue P1**: in `Assets/_Project/Data/Storyboard/SB_Prologue.asset` set frame P1 image to **`Art/Storyboard/Prologue/SB_P1.png`** (final art, 2208×1242; import same settings as the placeholders). P1 Ken Burns: zoom 1.00 → 1.08, pan (0, 0) → (−0.15, 0.05) so the push drifts toward the lighthouse (left) and never crops the spire at the top. Keep P2–P4 placeholders.
7. Play Menu → Prologue → Home once end to end. Record ~30 s → `SharedWorkFolder/ForDesignScreenshot/2026-11-07_Home_Scale_P1/2026-11-07_Home_Scale_P1.mp4`.
8. Commit "Home: Maela ×1.4, room ×0.8; prologue P1 final art" and **push to GitHub** (the user will pull this project on another laptop for class). Confirm the push succeeded and report the hash in `TechnicalArt/MENU_UNITY_PROGRESS.md`. Make sure the repo is clean afterwards (no uncommitted scene changes, TMP auto-changes restored).

## Do not
- Do not edit `Maela.psb`, sprite child positions, animation clips, or the background PNG.
