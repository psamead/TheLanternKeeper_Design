# Task: Home scene repair + Maela v1.5 seams + audio listener warning (2026-11-07)

Unity project **`TheLanternKeeper2D`**. Re-read `AGENTS.md`.

## Findings (Claude, from the user's screenshots + git)
1. `01_Home.unity` has an **uncommitted accidental edit**: `Background` moved to (−1.9156, −0.8494) and scaled non-uniformly (0.648, 0.643, 0.81); two camera positions also changed. Result: the camera shows empty space above the background and Maela can walk past its right edge. The committed version (`8dd187b`: Background at (0,0,0), scale 0.8) is correct.
2. Console: 999+ × "There are 2 audio listeners in the scene" — something in **DontDestroyOnLoad** (probably the menu music/audio object or a camera carried over from the menu) brings a second AudioListener into Home/Prologue.
3. `Maela.psb` → **v1.5** (already copied in, not committed): all interior seams sealed (the thin blue line through the head and between coat and skirt), far leg = near leg colour, far thigh fuller. Only interior pixels changed; script-verified layer names/order/bounds identical to v1.4. Backup: `SharedWorkFolder/TechArtAsset/Characters/Maela/_work/fix_v1.5/Maela_v1.4_before.psb`.

## Steps
1. Ask the user to close any open edit on `01_Home` **without saving**, then discard the uncommitted scene change: `git checkout -- Assets/_Project/Scenes/01_Home.unity` (reload the scene). Do not commit the accidental transform.
2. Verify in Edit + Play Mode: Background (0,0,0) scale (0.8,0.8,1); the Confiner2D polygon equals the background's rendered bounds (read `SpriteRenderer.bounds`, don't assume); walls at the background's left/right edges; camera never shows outside the background (top, bottom, left, right) at ortho 3.8. If the confiner can't contain a 3.8 ortho view vertically, lower ortho until it can and report the value.
3. Fix the duplicate AudioListener: make sure exactly one AudioListener exists in every scene in Play Mode (keep the one on the active Main Camera; remove/disable the one on any DontDestroyOnLoad object, or destroy the persistent object's listener on scene load). Re-run Menu → Prologue → Home: Console 0 warnings.
4. Let `Maela.psb` (v1.5) re-import (no importer changes). Same safety check as before: placement snapshot hash must equal the previous one; if any sprite moved, revert the psb and report.
5. Commit "Home: revert accidental background move; single AudioListener; Maela v1.5 seams" and **push**. Note hash + findings in `TechnicalArt/MENU_UNITY_PROGRESS.md` (in a dated section).
6. Video: synthetic input doesn't reach the Game view, so **don't spend time recording**. Tell the user it's ready; the user will record by hand (Win+Alt+R) while playing.

## Do not
- No importer setting changes, no sprite child position edits, no repainting. Don't commit the TMP fallback / Recorder package / AGENTS changes unless asked.
