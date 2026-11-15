# The Lantern Keeper · Design Repository

**English** | [简体中文](README.zh-CN.md)

Design and art documentation for a hand-painted 2D side-scrolling puzzle **demo** set on the Breton coast: story, gameplay plan, art specs, handoff notes, and finished art / audio assets.
The Unity project lives in a separate repository: <https://github.com/psamead/TheLanternKeeper2D>

> This repository is **read-only** for collaborators: it is maintained and pushed by Psamead. Please do not edit it after pulling; send feedback to Psamead / York instead.
>
> Most documents are written in Chinese. In-game text, titles and menus are English only.

## Latest handoff 2026-11-15

The Unity release is implemented and pushed through a469e41. Play the browser Demo at <https://psamead.github.io/TheLanternKeeper2D/>. Browser routes passed; the Windows package and EXE startup passed, while Windows gameplay and owner visual/audio acceptance remain pending. See [release report](ForDesignScreenshot/2026-11-15_AtticBaseline_EndCard_Release/after/Release_Report.md).

The five-page portfolio v1 is complete: [PDF and editing package](ForDesignPortfolio/README.md). New agents start at [ForAgent](ForAgent/README.md); current context is in [HOME_ART_RESUME](HOME_ART_RESUME.md).

Large project files now use Git LFS: PSD/PSB art sources, videos, portfolio editable sources/PDF and complete Windows/Web deliverables in DemoBuilds/. Install Git LFS before cloning. Temporary QA files and third-party references remain local.

## Get and update

```bash
# Recommended: clone next to the Unity project (sibling folder)
git lfs install
git clone https://github.com/psamead/TheLanternKeeper_Design.git
cd TheLanternKeeper_Design
git lfs pull
# Later updates
git pull
git lfs pull
```

## For agents: read first (in order, as needed)

1. `ForAgent/Design/ART_HANDOFF.md` **§9 "Current progress and next steps"** — where the project is now and what comes next
2. `ForAgent/Design/handoff.md` — project overview, demo scope, code conventions
3. `ForAgent/Design/DEMO_IMPLEMENTATION_PLAN.md` — scenes, mechanics, dialogue, implementation checklist (§7)
4. `ForAgent/Design/STORY_BIBLE.md` — story and setting (v2.0)
5. `TechnicalArt/HANDPAINTED_SPEC.md` — art style, resolution, import settings
6. `TechnicalArt/LESSONS_ART_PIPELINE.md` — lessons learned / pitfalls
7. `ForAgent/Unity/UNITY_AGENTS.md` — Unity-side rules (the Unity repo's root `AGENTS.md` is derived from it)

What happened recently: `ForAgent/Design/ART_HANDOFF.md` §10 (change log), `TechnicalArt/MENU_UNITY_PROGRESS.md`, or `git log`.

## Scenes (demo)

`00_StartMenu` → `01_Home` (grandma's house + attic, with storyboard A) → `03_EndCard` (storyboard B) → back to menu. `02_Harbor` is kept for the full game and is not in the Demo build (scope reduced 2026-11-07).

## Folders

| Path | Contents |
|---|---|
| `ForAgent/` | Specs and handoff notes for people and agents |
| `story_draft/`, `purposal_story/` | Story setting, demo plan (Word) |
| `TechnicalArt/` | Technical / promotional art docs, fonts (OFL), Unity progress log |
| `ART_ref/` | Concept art, references, `ASSETS.md` asset list |
| `TechArtAsset/` | Finished game assets (exported PNG, OGG) |
| `HOME_ART_RESUME.md` (root) | Local design/art Codex chat continuation; context and reading order, not an execution task |
| `CommandForAgentToInitialRun/` | Dated, actionable task instructions for the Unity-workstation / remote Codex; see its README |
| `ForDesignPortfolio/` | Student 4–5-page PDF, editable sources, and page previews produced on the design workstation |
| `ForDesignScreenshot/` | Screenshots from the Unity / Codex side for design review |
| `deprecated/` | Superseded versions and process images (kept for visual history) |

Not uploaded: temporary QA caches and third-party reference images (`BRETON_*`, `FAIRYHILLS_*` — listed in `ASSETS.md` but kept local only).

## Licences

- Fonts: SIL Open Font License, see `TechnicalArt/fonts/OFL_*.txt`.
- Menu audio is synthesized in code (`TechArtAsset/Audio/Menu/_src/synth_menu_audio.py`); no third-party samples.
- All other design documents and art are original work of this project, shared for course / project collaboration only.
