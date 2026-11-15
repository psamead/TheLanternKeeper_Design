# Portfolio production agent notes

Updated 2026-11-15 after the first portfolio export. Read this file together with `PORTFOLIO_PRODUCTION_HANDOFF.md` for the original brief and `PORTFOLIO_NEXT_HANDOFF.md` before making a later version.

## Current deliverable

- Reader entry: `ForDesignPortfolio/README.md`.
- PDF: `ForDesignPortfolio/TheLanternKeeper_Portfolio_2026-11-15_v1.pdf`.
- Editable native layout and IDML, links, fonts/licences, media, source snapshots and validation: `ForDesignPortfolio/Source/TheLanternKeeper_Portfolio_2026-11-15_v1/`.
- Page previews: `ForDesignPortfolio/Previews/TheLanternKeeper_Portfolio_2026-11-15_v1/`.
- Production record: `ForAgent/PORTFOLIO_PRODUCTION_STATUS.md`.

## Editing workflow

The v1 was made in DesignCraft using its headless layout API. It contains five A3 landscape pages, Cinzel and EB Garamond from the supplied OFL font files, and Courier New for code. The IDML roundtrip was checked in DesignCraft; Adobe InDesign itself was not used or tested. There is no INDD file.

For edits, first duplicate the version directory and export a new version. Keep image references inside its `Links/` folder. `asset_manifest.json` records original shared paths, dimensions, and hashes. Use the bundled `Document Fonts/` and keep the accompanying licence files. Courier New is a locally installed Windows font and is not redistributed as a font file.

After edits, export a fresh PDF and individual PNG previews. Check page count and dimensions, hyperlinks, missing assets/fonts, overset text, and every rendered page. Update `export_validation.json`, the reader README if page content changes, and `PORTFOLIO_PRODUCTION_STATUS.md`. Never claim an executable or web build passed based only on Unity source or an Editor recording.

## Fact and attribution rules

- Keep the implemented Demo distinct from the full seven-day story concept. The harbour shown in B5 is a storyboard image, not a playable map.
- Preserve labels that distinguish character source art, storyboard illustration, environment art, menu mockups, and gameplay captures.
- Do not infer individual student credit, course, or name. Add those only from confirmed information.
- Do not invent research, playtest results, ratings, release links, or build verification.
- Current Home art is the approved background. Use current evidence and avoid superseded 13 November screenshots for the present/memory comparison.
- Do not modify source PSD/PSB or game art while preparing page assets. Make page-specific crops as separate package files.
- The source excerpt snapshots are read-only references; check the current Unity scripts before revising code descriptions.

## Tool fit

DesignCraft gave the most reliable control for page layout, typography, image links, navigation, native save, IDML, and PDF. Use Photoshop only if a later version needs substantial raster cleanup or compositing. Use InDesign if a human editor needs its familiar native workflow; reopen the IDML and check font substitution, links, and page rendering before delivering an INDD/PDF pair.
