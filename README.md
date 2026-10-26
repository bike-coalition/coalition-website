# San Diego County Bike Coalition website code

Custom code for [sdbikecoalition.org](https://sdbikecoalition.org). The site itself runs on Squarespace 7.1. This repo holds the parts Squarespace can't do on its own: shared styles, custom page sections, and the small loader that pulls them into the site.

## How it fits together

1. The code lives here, in `src/`.
2. When a version is ready, it gets a release tag, like `v0.1.0`.
3. jsDelivr, a free public CDN, serves the files for that exact tag.
4. Squarespace Code Injection loads one pinned tag. Nothing changes on the live site until someone updates that tag in Squarespace.

The step-by-step version is in [docs/runbook.md](docs/runbook.md).

## What's here

| Path | What it is |
| --- | --- |
| `src/site/` | Site-wide CSS (served from jsDelivr since v0.3.0) and the Code Injection header that loads it |
| `src/blocks/` | Every Squarespace Code block, one file each, plus `registry.json` mapping each to its page and block ID |
| `docs/code-map.md` | Where every piece of custom code lives on the live site |
| `docs/jsdelivr-plan.md` | How the pasted code moves to jsDelivr, step by step |
| `src/tokens.css` | Brand colors, type, spacing and buttons as CSS variables |
| `src/pages/` | Page stylesheets, each loaded only on its own page |
| `docs/pages/` | Step-by-step Squarespace build guides, one per page |
| `manifest.json` | Every page, and whether it stays native Squarespace or gets custom code |
| `docs/sitemap.md` | A proposed menu structure, on hold |
| `docs/runbook.md` | How a change goes from this repo to the live site |
| `docs/baseline/` | Records of the live site before custom code goes in |
| `tools/site-check.py` | Read-only check of the live site for broken links, missing alt text and page weight. Runs weekly on GitHub Actions (`.github/workflows/site-check.yml`); see the runbook |
| `docs/reports/` | Site check reports, starting with the first run |
| `CLAUDE.md` | Rules for Claude when it works in this repo |

## Status

Phase 3 of the website roadmap: repo and security. The current homepage and menus stay as they are for now. A new homepage and a nav reorganization are on hold.

## Contact

San Diego County Bike Coalition · 300 15th Street, San Diego, CA 92101 · 619.786.5880 · info@sdbikecoalition.org
