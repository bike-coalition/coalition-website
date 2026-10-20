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
| `src/tokens.css` | Brand colors, type, spacing and buttons as CSS variables |
| `manifest.json` | Every page, and whether it stays native Squarespace or gets custom code |
| `docs/sitemap.md` | A proposed menu structure, on hold |
| `docs/runbook.md` | How a change goes from this repo to the live site |
| `docs/baseline/` | Records of the live site before custom code goes in |
| `CLAUDE.md` | Rules for Claude when it works in this repo |

## Status

Phase 3 of the website roadmap: repo and security. The current homepage and menus stay as they are for now. A new homepage and a nav reorganization are on hold.

## Contact

San Diego County Bike Coalition · 300 15th Street, San Diego, CA 92101 · 619.786.5880 · info@sdbikecoalition.org
