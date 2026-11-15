# CommandForAgentToInitialRun

This folder contains dated, actionable task sheets for Codex on the Unity workstation (the remote/network-side Unity machine).

Put a task sheet here only when it is intended to be executed against the Unity project. It should state the target outcome, scope, required source assets, ordered steps or investigation questions, acceptance checks, and what evidence/status to report back. Keep Unity-side task history here by date.

Local design/art chat continuation summaries belong in the repository root as `*_RESUME.md`. They provide context and reading order for the local Codex chat; they are not execution commands. Reusable art decisions and production lessons belong in `TechnicalArt/`, while people-facing supplements belong with the relevant Word documents.

The latest task is [2026-11-15 Home story gate, attic and audio follow-up](2026-11-15_Unity_Home_StoryGate_Attic_Audio_Followup.md). It is **prepared and awaiting the Unity workstation Codex**; the user will ask that Codex to read it. The previous [pickup gate, story audio and safe attic arrival](2026-11-15_Unity_PickupGate_StoryAudio_Attic.md) was implemented in Unity `a803050`, but its earlier PASS does not prove this follow-up is done. Keep the user-approved Home background unchanged. Record new implementation and tests in `TechnicalArt/MENU_UNITY_PROGRESS.md` and the new task’s evidence folder.

The follow-up rechecks the pickup gate, ordered triggers, A4 ending, attic placement, audio mix and EndCard position against the latest user feedback.

The [earlier 2026-11-15 first bell task](2026-11-15_Unity_FirstBell_Exploration_EndCard.md) was implemented in Unity `c7ba7f2` and should not be rerun. Its allowance for recording exploration before pickup and its immediate hint dismissal are superseded by the current task. EndCard option placement remains as implemented.

The [2026-11-14 visual task](2026-11-14_Unity_Home_Visual_Refinement.md) was implemented in Unity commit `a84fa68`; its checks and limits are in `TechnicalArt/MENU_UNITY_PROGRESS.md`. Earlier decisions are in [2026-11-13 Home review](2026-11-13_Unity_Home_Review_Art_Transition_Audio.md). The local art-chat continuation is [HOME_ART_RESUME.md](../HOME_ART_RESUME.md).
