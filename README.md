# The Lantern Keeper · Design Repository

**English** | [简体中文](README.zh-CN.md)

Design and art documentation for a hand-painted 2D side-scrolling puzzle **demo** set on the Breton coast: story, gameplay plan, art specs, handoff notes, and finished art / audio assets.
The Unity project lives in a separate repository: <https://github.com/psamead/TheLanternKeeper2D>

> This repository is **read-only** for collaborators: it is maintained and pushed by Psamead. Please do not edit it after pulling; send feedback to Psamead / York instead.
>
> Most documents are written in Chinese. In-game text, titles and menus are English only.

## Latest handoff 2026-11-15

The current Home background is approved. Unity `a803050` is the previous implementation baseline. The user has since requested a follow-up to recheck the no-lantern gate, ordered exploration, A4 exit, page audio, attic landing, and EndCard options. The task is prepared for the Unity workstation Codex and has not run yet. The earlier Editor report does not count as validation of these follow-up requirements.

For the current design, read [Demo flow and audio cues](DEMO_IMPLEMENTATION_PLAN.md), [Home art knowledge base](TechnicalArt/HOME_ART_KNOWLEDGE_BASE.md), [Home progress report](TechnicalArt/MENU_UNITY_PROGRESS.md), and [local chat resume](HOME_ART_RESUME.md). The new Unity task is prepared and waiting for the user to ask the remote Codex to read it; see [CommandForAgentToInitialRun](CommandForAgentToInitialRun/README.md). The user's 12 screenshots and first source recording are indexed in `ForDesignScreenshot/2026-11-15_Home_Pickup_Story_Attic/README.md`; the full-demo reference recording is in `ForDesignScreenshot/2026-11-15_Home_FullDemo_Recordings/README.md`.

People-facing Word versions: [Home art handoff and lessons, v3](TechnicalArt/守灯人_Home美术交接与经验_2026-11-15_v3.docx) and [Demo implementation plan, v1.8](purposal_story/守灯人_Demo制作方案_v1.8.docx).

## Get and update

```bash
# Recommended: clone next to the Unity project (sibling folder)
git clone https://github.com/psamead/TheLanternKeeper_Design.git
# Later updates
git pull
```

## For agents: read first (in order, as needed)

1. `ART_HANDOFF.md` **§9 "Current progress and next steps"** — where the project is now and what comes next
2. `handoff.md` — project overview, demo scope, code conventions
3. `DEMO_IMPLEMENTATION_PLAN.md` — scenes, mechanics, dialogue, implementation checklist (§7)
4. `STORY_BIBLE.md` — story and setting (v2.0)
5. `TechnicalArt/HANDPAINTED_SPEC.md` — art style, resolution, import settings
6. `TechnicalArt/LESSONS_ART_PIPELINE.md` — lessons learned / pitfalls
7. `UNITY_AGENTS.md` — Unity-side rules (the Unity repo's root `AGENTS.md` is derived from it)

What happened recently: `ART_HANDOFF.md` §10 (change log), `TechnicalArt/MENU_UNITY_PROGRESS.md`, or `git log`.

## Scenes (demo)

`00_StartMenu` → `01_Home` (grandma's house + attic, with storyboard A) → `03_EndCard` (storyboard B) → back to menu. `02_Harbor` is kept for the full game and is not in the Demo build (scope reduced 2026-11-07).

## Folders

| Path | Contents |
|---|---|
| Root `*.md` | Specs and handoff notes for people and agents |
| `story_draft/`, `purposal_story/` | Story setting, demo plan (Word) |
| `TechnicalArt/` | Technical / promotional art docs, fonts (OFL), Unity progress log |
| `ART_ref/` | Concept art, references, `ASSETS.md` asset list |
| `TechArtAsset/` | Finished game assets (exported PNG, OGG) |
| `HOME_ART_RESUME.md` (root) | Local design/art Codex chat continuation; context and reading order, not an execution task |
| `CommandForAgentToInitialRun/` | Dated, actionable task instructions for the Unity-workstation / remote Codex; see its README |
| `ForDesignScreenshot/` | Screenshots from the Unity / Codex side for design review |
| `deprecated/` | Superseded versions and process images (kept for visual history) |

Not uploaded: `.psd/.psb` source files, third-party reference images (`BRETON_*`, `FAIRYHILLS_*` — listed in `ASSETS.md` but kept local only).

## Licences

- Fonts: SIL Open Font License, see `TechnicalArt/fonts/OFL_*.txt`.
- Menu audio is synthesized in code (`TechArtAsset/Audio/Menu/_src/synth_menu_audio.py`); no third-party samples.
- All other design documents and art are original work of this project, shared for course / project collaboration only.
