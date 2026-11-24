# Homepage: Golden Gear Gala teaser (December 2026)

One section at the very top of the homepage that teases the 2026 Golden Gear Gala (Tuesday, December 15, 6 to 9 PM, Négociant Winery, Hillcrest). Design: option B on the canvas board "Homepage: Golden Gear Gala teaser options". The rest of the homepage is unchanged.

| Piece | Repo file |
| --- | --- |
| Markup (pasted into one Code block) | [src/blocks/home/gala-teaser.html](../../src/blocks/home/gala-teaser.html) |
| Styles | [gala-teaser.css](../../src/blocks/home/gala-teaser.css) |
| Video and pause button | [gala-teaser.js](../../src/blocks/home/gala-teaser.js) |
| Reel (540 x 960, H.264, no audio, 5 MB) and poster | [img/gala-reel.mp4](../../src/blocks/home/img/gala-reel.mp4), [img/gala-reel-poster.jpg](../../src/blocks/home/img/gala-reel-poster.jpg) |

Facts come from the gala's Givebutter page (givebutter.com/c/121526-golden-gear-gala) and its event page (/calendar/golden-gear-gala), checked November 23, 2026. Both buttons go to the Givebutter page, which sells tickets and has the "I'll be there in-spirit!" option.

The reel is "Golden Gear Gala final edit.mp4" from the shared Drive, re-encoded on November 23, 2026 (the original is 1080 x 1920 HEVC, 33 MB, which Chrome and Firefox can't reliably play). It plays muted on a loop only when the visitor's device allows motion, pauses when scrolled out of view, and has a pause button (needed for anything that moves on its own for more than 5 seconds).

## Test page

A hidden copy of the homepage with this section added at the top: see "Test page record" below. The live homepage is not changed until staff approve it.

## Test page record (November 23, 2026)

- Duplicated the homepage in Squarespace as "Homepage preview (gala teaser)", slug `/home-gala-preview`, in Not Linked, Hide from Search on (left out of the sitemap; Squarespace adds no `noindex` tag, so keep it unlinked). The homepage's own header code (home.css v0.11.0) came with the copy.
- Added a blank section at the very top with one Code block holding `gala-teaser.html` from v0.13.0 (its text matches the repo file exactly).
- Checked on the published test page: at 1440 px the teaser is 632 px tall under the header and the hero follows it; at 390 px it stacks (text, then the reel), nothing scrolls sideways, and the reel plays muted on a loop.
- The live homepage was not changed.

**v0.13.1 (November 23, 2026):** works at every screen size. The text and reel stay side by side down to 641 px wide (the reel and headline shrink with the window), the section is shorter than 600 px below 1024 px wide, and phones (640 px and under) stack the text above a smaller reel. Checked at 390, 480, 600, 660, 745, 820, 1024, 1280, 1440 and 1920 px: nothing scrolls sideways.

## Go live

Add a section at the very top of the live homepage, with one Code block holding `gala-teaser.html`. Check it logged out at 1440 and 390 px.

## Go-live record (November 23, 2026)

- At Jason's go-ahead after reviewing the test page: added a blank section at the very top of the live homepage (`/home`, section `6b048ef0ef26100db08d1468`, above the "Bike for a Better San Diego" hero) with one Code block holding `gala-teaser.html` from v0.13.1 (its text matches the repo file exactly). Nothing else on the homepage changed; its header code still loads home.css v0.11.0.
- Checked live, logged out: sdbikecoalition.org serves the teaser first, then the hero. In the browser at 1440, 745 and 390 px nothing scrolls sideways, the reel loads and plays, and phones stack the text above the reel.
- Not checked by Claude: buying a ticket. The hidden test page `/home-gala-preview` is still in Not Linked; disable or delete it whenever it's no longer needed.

## Incident and fix: v0.13.2 (November 23, 2026)

Right after go-live, the rest of the homepage collapsed (hero 228 px tall instead of about 540, every section's grid switched off). Cause: the block's "fill the section" rules used `section:has(.bc-gala)`, and the homepage wraps all its sections in an outer `<section class="region">`, which also "has" the teaser, so the rules reached every section. Single-section pages (Bike Share, Board Candidates, CicloSDias) use the same pattern without visible harm, which is why it wasn't caught there. The test page had the same problem; only the teaser itself was checked there, not the sections below it.

Fix: v0.13.2 scopes every one of those rules to `section.page-section:has(.bc-gala)`. Pasted into the live homepage the same day. Checked live at 1440 px: the teaser's section is the only one matched, every other homepage section's grid is back, and the hero, Vision, goals, "Where do I start?", membership, testimonials and shop sections render as before.

**Lesson for every custom block:** scope section rules to `section.page-section:has(...)`, never plain `section:has(...)`, and on any page with more than one section, check the sections around the block, not just the block.

## v0.13.3 (November 23, 2026): wide screens

On screens 1500 px and wider, a Teal Green ticket stub sits between the text and the reel: Tuesday, DEC 15, 6 to 9 PM, Négociant Winery, 1263 University Ave, Hillcrest, Tickets $100, and a countdown ("22 days to go", counted in Pacific calendar days, "Tomorrow night" and "Tonight" near the end, hidden after 9 PM on December 15). The reel grows to 340 px wide there. Below 1500 px nothing changes.

## v0.13.4 (November 23, 2026): wide screens, take two

The ticket stub looked off (its bottom notch hung below the card), so it was scrapped. On screens 1500 px and wider the text column now does the work instead: a bigger title, a When / Where / Tickets row (Tuesday, December 15, 6 to 9 PM; Négociant Winery, 1263 University Ave, Hillcrest; $100) and a countdown pill next to the eyebrow, counted the same way as before. The one-line "when" is hidden there because the row repeats it. The reel is 360 px wide. Below 1500 px nothing changes.

## v0.13.5 (November 23, 2026): closer to the reel

On laptop screens (about 1100 to 1499 px) the text column stretched while its words didn't, leaving up to 275 px between the text and the reel. The text column is now capped (680 px, or 1040 px at 1500 px and wider) and the text and reel sit centered as a pair, so the space between them stays about 75 to 95 px at every width.

## v0.13.6 (November 23, 2026): "Get tickets" goes to /gala

"Get tickets" now links to `/gala`, a URL mapping (Settings > Developer Tools > URL Mappings) that sends visitors to the invite page at `/calendar/golden-gear-gala`. The line was `/gala -> /full-calendar/golden-gear-awards 301` (last year's page, now a 404) and is now `/gala -> /calendar/golden-gear-gala 302`. It's a 302 so the link can be pointed at next year's gala without browsers holding on to this year's page. The full list as it was before the change is saved in `docs/baseline/url-mappings-2026-11-23.txt`. "Can't make it? Join in spirit" still goes straight to Givebutter.

A second line, `/full-calendar/golden-gear-awards -> /calendar/golden-gear-gala 302`, catches visitors whose browsers remembered the old permanent `/gala` redirect to last year's page (which is gone).

## Remove after the gala

Delete the section after December 15, 2026. Nothing else on the page depends on it.

## v0.17.0 (November 23, 2026): food line, spirit button to /gala

- Under the lead, a Teal Green "On the menu" tag and the line "A generous spread of appetizers and beverages." (staff wording), at every width.
- "Can't make it? Join in spirit" now goes to /gala (the event page, whose Givebutter widget has the "I'll be there in spirit!" option) instead of straight to Givebutter. Both buttons now go to /gala.
- Tested on a local copy at 390, 1440 and 1600 px: nothing scrolls sideways.
- Live November 23, 2026: pasted into the homepage Code block (`block-yui_3_17_2_1_1795460826642_5906`, which held v0.13.6 exactly; it now matches this file). Checked live: at 1440 px the food line shows under the lead and the other homepage sections keep their grids; at 390 px nothing scrolls sideways.
