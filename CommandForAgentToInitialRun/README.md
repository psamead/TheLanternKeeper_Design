# CommandForAgentToInitialRun

## Latest owner report 2026-11-18

2026-11-18 用户反馈：网络另一台机器上的 Codex 已跑过 Unity，暂未发现问题；作品集制作端 Codex 也已跑过，暂未发现问题。来源为用户本次转述，本地未重新运行。此反馈作为继续工作的可用基线；未指定 EXE/Web、具体提交、测试路线或作品集软件兼容性，不扩写为所有平台及所有细节最终验收。

后续接手与资料维护注意事项见 [资料与经验索引](../ForAgent/PROJECT_ARCHIVE_AND_LEARNING.md)。下方保留先前制作和验证记录；其中待审阅说明应结合本次反馈阅读，不自动重开旧任务。

This folder contains dated actionable task sheets for Codex on the Unity workstation. Local chat resumes belong in the repository root as *_RESUME.md; art knowledge and lessons belong in TechnicalArt. A prepared task is not an implementation or acceptance report.

## Current task 2026-11-15

Read [Attic baseline EndCard Windows and Web](2026-11-15_Unity_AtticBaseline_EndCard_Windows_Web.md). Status: **implemented; Editor and HTTPS gameplay passed; Windows package delivered, startup verified, gameplay pending manual verification**. Read the execution report appended to the task and the latest progress entry.

The three changes are implemented in `6adac6ca9d5532c9f646defca38c94255e55070c`; Unity `main` is pushed through `a469e412e5867ac488aac5558f17682c4c582ffd`. Full Windows package is delivered and EXE startup passed; gameplay remains unverified because window capture timed out. The verified Web demo is https://psamead.github.io/TheLanternKeeper2D/ . Browser gameplay passed; subjective listening and owner acceptance remain pending.

The [previous follow-up](2026-11-15_Unity_Home_StoryGate_Attic_Audio_Followup.md) has no new execution report. Its pickup/story gate, ordered exploration, A4, page audio and safe attic requirements are carried into the current task as regression checks. Keep passing behavior; do not rerun old task sheets independently. The approved Home background stays as it is. The old EndCard Application.Quit behavior is superseded; Start Menu Quit is outside this change.

## Earlier implemented baselines

- [Pickup gate story audio attic](2026-11-15_Unity_PickupGate_StoryAudio_Attic.md): Unity a803050, Editor report exists; physical listening/hardware and standalone checks were not verified.
- [First bell and EndCard placement](2026-11-15_Unity_FirstBell_Exploration_EndCard.md): c7ba7f2; pre-pickup exploration and immediate hint dismissal were superseded.
- [Visual refinement](2026-11-14_Unity_Home_Visual_Refinement.md): a84fa68. [Home art review](2026-11-13_Unity_Home_Review_Art_Transition_Audio.md): 3417fc4.

New evidence: ForDesignScreenshot/2026-11-15_AtticBaseline_EndCard_Release/after/. Runnable packages: DemoBuilds/2026-11-15_FinalDemo/. Word QA: .story_document_qa/. Implementation reports: TechnicalArt/MENU_UNITY_PROGRESS.md. Local context: HOME_ART_RESUME.md.

Recording clarification 2026-11-15: use the user's existing full-demo recording as the accepted reference for existing flow. Do not require a duplicate full recording. Verify the new changes with relevant screenshots or necessary short clips; real EXE/browser checks still apply. Cross-computer agent navigation and the separate portfolio handoff are in [ForAgent](../ForAgent/README.md).
