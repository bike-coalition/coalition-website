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

## Go live

Add a section at the very top of the live homepage, with one Code block holding `gala-teaser.html`. Check it logged out at 1440 and 390 px.

## Remove after the gala

Delete the section after December 15, 2026. Nothing else on the page depends on it.
