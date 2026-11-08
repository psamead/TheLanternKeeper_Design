# Walk v3 stride check (2026-11-08)

- Walk clip: 1.1 s loop; footstep events at 0 and 0.55 s. Pose keys were copied from shared `poses.py` v3 and regenerated in Unity.
- Final `walkSpeed`: **0.8 units/s** (Left/Right Shift). Run remains **3.2 units/s**.
- Play Mode measurement used the live `01_Home` Ground top at Y = -3.200. In Play Mode, I sampled the live Animator at 80 phase samples per clip and moved the player root by the configured speed times each sample time; the boot-bottom midpoint was measured in world space. Contact samples were the planted-sole intervals within ±0.006 units of the Ground top.
- Walk v3 planted-foot world-X results: Boot_R t=0.150–0.313: +0.0025 units (range 0.0056); Boot_R t=0.388–0.513: +0.0004 (range 0.0072); Boot_L t=0.688–0.888: −0.0009 (range 0.0054). Each measured interval stayed under the 0.02-unit limit, so the starting 0.8 speed was retained.
- Run was measured for information only, without changing its speed: Boot_R contact segments had +0.0534 and −0.0250 units drift; Boot_L had +0.0277.
- Walk-in-Home capture: [`walk_v3_contact.png`](walk_v3_contact.png), 1920×1080.

