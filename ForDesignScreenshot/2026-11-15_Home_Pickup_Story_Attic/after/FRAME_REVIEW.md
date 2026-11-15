# Recorded frame review

Recorder: Time.timeScale=1, 30 fps; Unity time 80.31–213.95 (133.64 s), output 133.666633 s / 4010 frames. No speed-up, cuts or retiming. Full video includes Menu, natural P, pre-pickup Home, natural A, exploration, complete bell, attic movement/jump/layer switches, natural B and eight-second B5 dwell.

A4 images disabled under fully opaque black at Unity time 142.4481 (video approximately 62.14 s). First Home reveal sample 142.5148, root (-4.7000,-3.1958), Grounded=True, controls locked. First attic reveal sample 157.4815 (video approximately 77.17 s), root (4.7000,2.7288), Grounded=True, controls locked. Floor surface 2.725; observed root separation is normal physics contact tolerance.

Reviewed all 92 consecutive 1920x1080 PNGs in `_work/a4_exit_frames/` (video 60.1381–63.2 s) using all-frame sheets 1–4. Captioned A4 dims once; frames 58–61 are black; frame 62 starts revealing Home. No captionless A4 reappearance, old world prompt or extra image layer. The first visible attic sequence is indexed in `_work/attic_reveal_all_frames.jpg`: first revealed pose already stands on the floor, with no visible fall.

Runtime `frame_audit.csv` contains 1801 consecutive frames with no frame-number gaps. All 44 sampled frames across the two reveal windows report Grounded=True; the A image never re-enables after removal. Actual route movement and the separate boundary suite additionally exercise physical containment, rather than inferring safety from one grounded sample.

Audio: whole file decoded successfully with FFmpeg. AAC stereo 48 kHz; mean -21.9 dB, peak -5.2 dB. This proves a non-silent captured signal, not audible mix quality. Runtime cue observations separately show A1/A2 .60, A3 .38 + waves .55, A4 .38 + wave source stopped, B1–B5 .60 + wind .40. ArMorDu playback sample advances continuously, including normal loop wrap; exactly one music voice on natural/skip B5.

Video size: 121478915 bytes. SHA256 local/shared match: `064DCF205B7D4BEBBA9A16B47463FA4EA77000D0FF2E73ED4D8C509E50BADA7F`.

Visual placement and subjective listening still require owner acceptance. Input was injected through Unity Input System; no physical hardware or standalone build claim.
