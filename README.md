# The Lantern Keeper · Design Repository

**English** | [简体中文](README.zh-CN.md)

Design and art documentation for a hand-painted 2D side-scrolling puzzle **demo** set on the Breton coast: story, gameplay plan, art specs, handoff notes, and finished art / audio assets.
The Unity project lives in a separate repository: <https://github.com/psamead/TheLanternKeeper2D>

> This repository is **read-only** for collaborators: it is maintained and pushed by Psamead. Please do not edit it after pulling; send feedback to Psamead / York instead.
>
> Most documents are written in Chinese. In-game text, titles and menus are English only.

## Latest handoff 2026-11-13

Home greybox, world switching, ladder climbing and attic exit have recorded Unity validation at `b61eb3f`. Current work is art consistency and integration preparation: preserve the painterly hand-painted style; room perspective is acceptable. Selected assets are `Lantern_v4.png`, `Home_Present_v3.png`, `Attic_PerspectiveRef_v3.png`, and `Ladder_Whole_v4.png`. They have not been integrated into Unity.

For a local design/art Codex chat, start with [Home art knowledge base](TechnicalArt/HOME_ART_KNOWLEDGE_BASE.md) and [local chat resume](HOME_ART_RESUME.md). The matching human-readable Word supplement is `TechnicalArt/守灯人_Home美术交接与经验_2026-11-13_v1.docx`. The Unity workstation Codex task is separate: [Home Unity review and integration command](CommandForAgentToInitialRun/2026-11-13_Unity_Home_Review_Art_Transition_Audio.md). Historical source files may be local-only; the shared folder remains the primary source for Unity work.

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
