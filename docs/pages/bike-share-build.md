# Bike Share page: custom build ("Bring bike share back")

The redesigned Bike Share page is one Squarespace Code block holding the whole page, like Board Candidates and CicloSDias. The design is the "Future: Bike Share" artboard on the redesign canvas, as of November 19, 2026.

| Piece | Repo file | Where it goes |
| --- | --- | --- |
| Page markup | [src/blocks/bike-share/bike-share.html](../../src/blocks/bike-share/bike-share.html) | Pasted into the one Code block |
| Page styles | [bike-share.css](../../src/blocks/bike-share/bike-share.css) | jsDelivr, linked from the block |
| Pickers (steps, route stops, funding pillars) | [bike-share.js](../../src/blocks/bike-share/bike-share.js) | jsDelivr, linked from the block |
| Petition card styles and text fixes | [petition.css](../../src/blocks/bike-share/petition.css), [petition.js](../../src/blocks/bike-share/petition.js) | jsDelivr, linked from the block |
| Step photos (Unsplash, free license) | [img/](../../src/blocks/bike-share/img) | jsDelivr |
| Page-wide rules | [src/pages/bike-share.css](../../src/pages/bike-share.css) via [bike-share-header-injection.html](../../src/pages/bike-share-header-injection.html) | Page Settings › Advanced › Page Header Code Injection |

The old page is saved in [docs/baseline/bike-share-2026-11/](../baseline/bike-share-2026-11/): its text, links and images, and its petition Code block exactly as it was.

## What stays live and connected

- **Petition:** the same Action Network embed (`bring-bikeshare-back-to-san-diego`, full layout). The signature count updates itself. The card keeps the styling and text fixes it had on the old page (moved, unchanged, into `petition.css` and `petition.js`), so it is a Teal Green card rather than the white card drawn on the artboard.
- **$1 pledge:** links to the Givebutter campaign at `givebutter.com/c/bikeshare`. No progress bar: the campaign has no Givebutter widget, and fixed numbers would go stale (decided November 19, 2026).
- **FOX 5 video:** the same YouTube video as the old page (`FEBnMJSr1b0`), embedded from `youtube-nocookie.com`.
- **Letter of support** (Google Form) and **join the Alliance** (email to Ian) links are unchanged.
- Images already on the site (hero, docked station, riders, Alliance and Waymo logos, Ian's photo) load from Squarespace's image CDN, the same files the old page and the Staff & Board page use.

## Facts confirmed for launch

Staff confirmed on November 19, 2026: the "Estimated 2028" launch, "0 cities in San Diego County have public bike share," and the Waymo partnership logo.

## 1. Make the hidden preview page

1. **Pages ›** Bike Share **› Page settings › Duplicate Page › Confirm.** The copy lands in **Not Linked**. Title it "Bike Share preview", slug `/bike-share-preview`.
2. Turn on **Page Settings › SEO › Hide Page from Search Results**.
3. On the copy, delete every section but one. In that section, delete every block and add one **Code** block. Paste the whole of `bike-share.html` into it and save.
4. **Page Settings › Advanced › Page Header Code Injection:** paste `src/pages/bike-share-header-injection.html` and save.

**Done November 19, 2026 (Claude, in the Squarespace editor):** "Bike Share preview" at `/bike-share-preview`, in Not Linked, Hide from Search on (it is left out of the sitemap, but Squarespace adds no `noindex` tag, so keep the page unlinked and short-lived). All 15 copied sections removed; one blank section holds one Code block with `bike-share.html` from v0.12.0 (its text matches the repo file exactly). Header code holds the v0.12.0 line. The live `/bike-share` page was not changed (it had no page header code).

Checked on the published preview, November 19, 2026: at 1440 px and 390 px nothing scrolls sideways; the block fills its section with no extra height (the 100 px above it is the site header's space); every image loads; the petition loads with its live count; the step, stop and pillar buttons switch panels; the FOX 5 video is embedded. The site's fade-in animation also applies to the block's headings and paragraphs, as on other pages: each fades in as it scrolls into view, including panels shown by a button.

## 2. Check the preview page

- Desktop and phone: it matches the artboard; nothing scrolls sideways at phone width.
- The petition loads with its live count. Don't sign it from a test account unless you mean to: signatures are real.
- The Unlock, Ride, Dock buttons, the five route stops and the five funding pillars each switch the panel below them. The FAQ opens and closes.
- "Sign the petition" buttons jump to the petition; "I represent a group" jumps to the bottom section.
- The Givebutter, Union-Tribune, FOX 5, letter of support and email links open the right places. The video plays.

## 3. Go live (keep the old page)

1. Rename the old page "Bike Share (old, Nov 2026)", change its slug from `/bike-share` to `/bike-share-old` and turn off **Enable Page**. It stays in Squarespace as the undo.
2. On the preview page: title "Bike Share", slug `/bike-share`, Hide from Search off. Put it where the old page sat in the menus (drag it in **Pages**), and move the old page to Not Linked.
3. Check **Settings › Advanced › URL Mappings**: no rule should send `/bike-share` anywhere.
4. Run the step 2 checks again on `/bike-share`, logged out. Check the block's section isn't taller than the page (docs/jsdelivr-plan.md, step 1 lessons).
5. In the repo: record the go-live below, in [code-map.md](../code-map.md) and in `manifest.json`.

## Go-live record (November 19, 2026)

- Done by Claude in the Squarespace editor, at Jason's go-ahead after the preview.
- Old page: renamed "Bike Share (old, Nov 2026)", slug `/bike-share-old`, **Enable Page off**, moved to Not Linked. It still holds every original section, including its own petition block.
- New page: title and navigation title "Bike Share", slug `/bike-share`, Hide from Search off, in the Advocacy menu after Campaigns (where the old page sat). Page header code: v0.12.0 line from `src/pages/bike-share-header-injection.html`.
- URL Mappings: no rule mentions `/bike-share`.
- Checked logged out: `/bike-share` serves the new block and header code with no `noindex`, and is in the sitemap; the menu links to `/bike-share`; `/bike-share-old` and `/bike-share-preview` return 404. In the browser: the petition loads with its live count, every image loads, nothing scrolls sideways, the pickers work.
- Not checked by Claude: a real petition signature, the Givebutter checkout, and every outside link by hand. Click through them once.
- Delete the old page after a month (late December 2026) if nothing needs it.

## Undo

Swap the slugs back (new page to `/bike-share-preview`, old page to `/bike-share`, turn the old page back on). The old page still has its own petition block. Keep the old page for a month after go-live, then delete it.

## To change later

- A local San Diego photo for the Unlock, Ride and Dock steps (today: Unsplash photos from France and a Honolulu station) and for the docked section.
- If staff make a Givebutter widget for the $1 campaign, it can replace the buttons-only card.
