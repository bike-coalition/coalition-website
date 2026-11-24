# Repair Clinic and Rolling Forward: refresh (option B, "Facts beside booking")

Both clinic pages get the same layout: a Spring Green hero, then the clinic's facts beside its Google booking calendar, then one band after it. Design: option B on the canvas boards "Repair Clinic: refresh options" and "Rolling Forward: refresh options" (staff picked B for both on November 24, 2026). Each page keeps its own native Google appointment-calendar Embed block, untouched; only Code blocks around it are new.

| Piece | Repo file | Where it goes |
| --- | --- | --- |
| Shared styles | [src/blocks/clinics/clinics.css](../../src/blocks/clinics/clinics.css) | jsDelivr, linked from every block below |
| `/repair` hero | [repair-hero.html](../../src/blocks/clinics/repair-hero.html) | Code block, alone in the page's first section |
| `/repair` facts | [repair-booking.html](../../src/blocks/clinics/repair-booking.html) | Code block in the `reservations` section, beside the calendar |
| `/repair` photo band | [repair-photo.html](../../src/blocks/clinics/repair-photo.html) | Code block in the `reservations` section |
| `/rolling-forward` hero | [rolling-forward-hero.html](../../src/blocks/clinics/rolling-forward-hero.html) | Code block in the page's one section |
| `/rolling-forward` facts | [rolling-forward-booking.html](../../src/blocks/clinics/rolling-forward-booking.html) | Same section, beside the calendar |
| `/rolling-forward` Find us band | [rolling-forward-find-us.html](../../src/blocks/clinics/rolling-forward-find-us.html) | Same section |

How the layout works: `clinics.css` turns any section holding a clinic block into its own grid. It places blocks by kind, not by where they sit in the editor: hero first (full width), then the facts block (left) and the Embed block (right), then the band (full width). Under 860 px everything stacks: hero, facts, calendar, band. So in the editor, blocks only need to be in the right section; their positions there don't matter. Every rule is scoped to `section.page-section:has(.bc-clinic)`.

Images are the photos already on each page, loaded from Squarespace's image CDN. The old pages' text and layout are saved in [docs/baseline/repair-2026-11-24.md](../baseline/repair-2026-11-24.md) and [docs/baseline/rolling-forward-2026-11-24.md](../baseline/rolling-forward-2026-11-24.md).

## Wording decisions (November 24, 2026)

- Short name after the first full name: "the Bike Coalition" (staff's choice for these pages, following the organization's writing rules; the repo's `CLAUDE.md` still says "the Coalition").
- SDSU facts come from the SDSU booking page: the Repair Station at the Sundial outside Hepner Hall, Thursdays 11:30 am to 2:30 pm during the school year, for SDSU students and employees. The old page's "where the Aztec Walk meets the Campanile Bikeway" is gone; the campus map stays.
- Each page links to the other: `/repair` tells SDSU students and employees about Thursday tune-ups, and `/rolling-forward` tells everyone else about the Sunday clinic.

## Rollout, one page at a time

For each page, `/repair` first:

1. Save the old page's content in `docs/baseline/` (done for both, November 24, 2026).
2. **Pages ›** the page **› Duplicate Page.** Title the copy "<page> preview", slug `/<slug>-preview`, Hide from Search on. Duplicating keeps the Embed block exactly as it is.
3. On the copy, delete the old text and image blocks (text blocks first, so Squarespace doesn't merge two text blocks), and any section that ends up empty. Add the Code blocks above to the sections named in the table, pasting each file from the release tag.
4. Check the preview at 1440 px and 390 px: the order is right, nothing scrolls sideways, the calendar shows open times, the buttons jump to the right places.
5. Go live: old page renamed "(old, Nov 2026)", slug `/<slug>-old`, disabled. Preview page gets the old title, navigation title and slug, Hide from Search off. For `/repair`, the menu item is the page itself: drag the new page into its place under Classes + Events and the old one to Not Linked.
6. Check live, logged out, at laptop and phone widths. Record it below, in [code-map.md](../code-map.md) and in `manifest.json`.

## Undo

Swap the slugs back (new page to `/<slug>-preview`, old page to `/<slug>`, turn the old page back on) and swap the menu item back. Keep the old pages for a month, then delete them.

## Release history

- **v0.19.0** (November 24, 2026): first build. Tested on a local copy of each live page at 1440 and 390 px before tagging.
- **v0.19.1**: the section layout rules skip the Squarespace editor (`body:not(.sqs-edit-mode)`). The editor puts its own row and column guides inside the section, and the grid squeezed them.
- **v0.19.2**: in the editor each block shows as a short preview that scrolls (`max-height: 360px`). Without it the editor measured a block's full content in its narrow default cell and grew it to 6,400 px. Live on `/repair` and on the first two `/rolling-forward` blocks.
- **v0.19.3** (November 24, 2026): `/rolling-forward` Find us band only. Staff said the helmet photo was tiny (120 px square, cropped from a 3:4 photo). It now takes half the text column on laptops (286 by 381 px at 1440) and the full width on phones (358 by 477 at 390), shown whole from a 1000w source. New class `bc-clinic__gear` (was `__helmet`), because the other blocks' inline guards still carry the old 120 px rule. Alt text no longer says kids' helmets (the yellow one is an adult M). Only the Find us block was re-pasted (SHA-256 matched the file; the text replaced was exactly v0.19.2); the other five blocks stay on v0.19.2, which is fine because only the Find us band uses the changed rules. Checked live at 1440 and 390 px: no sideways scroll, block order unchanged, calendar loads.
- **jsDelivr lesson:** a request for a file at a tag that isn't pushed yet gets a cached "not found". A GitHub push failed once, a check ran meanwhile, and `clinics.css` and `rolling-forward-booking.html` at v0.19.2 had to be purged (`purge.jsdelivr.net/gh/...`). Don't fetch a tag's files until the push has gone through.

## In the editor

The published page lays the blocks out with `clinics.css`. The editor keeps Squarespace's own grid, so there the Code blocks sit in narrow cells near the top of their section and scroll inside. That is expected; their editor positions don't change the published page. To edit a Code block, select it from the section's **Layers** list (the calendar Embed sits under them, and a click can land on it).

## Go-live record (November 24, 2026)

At staff's go-ahead ("Yes, swap both"), one page at a time:

**/repair**
- Old page: renamed "Repair Clinic (old, Nov 2026)", slug `/repair-old`, Enable Page off, in Not Linked. It still holds every original section and its own copy of the booking embed.
- New page (was `/repair-preview`): title and navigation title "Repair Clinic", slug `/repair`, Hide from Search off. SEO title and description are the old page's, unchanged. Moved into Classes + Events, after Rides and before Bike the Bay, where the old page sat.
- Blocks: section `6b05eb9838a3e67c2969c0d4` holds the hero (`block-yui_3_17_2_1_1795550429548_1447`). Section `6b05eb9838a3e67c2969c0dc` (anchor `reservations`) holds the facts (`..._1970`), the photo band (`..._2224`) and the Embed block `block-7e2de60ec9be7cb68d2f` (Sunday Bike Clinic, schedule `AcZssZ1G2Unp...`, the same as calendar.app.google/Z5iFWf58bZePCJER9). Each Code block's text matches the v0.19.2 file exactly (SHA-256 checked after pasting). The old middle section (text and two photos) was removed on the copy.
- While moving the old page to Not Linked it was dropped into the "LCI Resources" member site by mistake. It was disabled the whole time; it was moved straight back out with "Move out of Member Site", which put it in Not Linked.

**/rolling-forward**
- Old page: renamed "SDSU Rolling Forward (old, Nov 2026)", slug `/rolling-forward-old`, Enable Page off, in Not Linked (it was never in a menu).
- New page (was `/rolling-forward-preview`): title and navigation title "SDSU Rolling Forward", slug `/rolling-forward`, Hide from Search off. New SEO title "SDSU Rolling Forward | Free Tune-Ups on Campus" and description (the old ones had em dashes).
- Blocks: one section `6b05ee5e04e0be2393b9f445`: hero (`block-yui_3_17_2_1_1795550888947_2748`), facts (`..._2995`, anchor `#reserve`), Find us band (`..._3250`, anchor `#find-us`) and the Embed block `block-48b0716732d715f3038e` (SDSU Rolling Forward Tune-Up, schedule `AcZssZ35-WST...`, the same as calendar.app.google/FHQf88Shsitc7CaD7). Each Code block's text matches the v0.19.2 file exactly. The nine old text and image blocks were removed on the copy (the Embed was removed once by a stray click and restored with Undo before saving; same block, same calendar).

**Checked live, logged out:** `/repair` and `/rolling-forward` return 200 with the new blocks and no `noindex`; the `-old` and `-preview` slugs return 404. The Classes + Events menu links Repair Clinic to `/repair`. At 1440 px the facts sit beside the calendar; at 390 px everything stacks (hero, facts, calendar, band); nothing scrolls sideways at either width. Buttons are 52 px tall; "Book a slot" buttons jump to the facts; all photos load. Both calendars load and show open slots (Sunday December 6 from 11:00 am; Thursday December 3 from 11:30 am). The URL mappings saved November 23 have no rule for either slug.

**Not checked by Claude:** making a real booking. Book and cancel one test slot on each page to be sure.

Delete the two old pages after a month (late December 2026) if nothing needs them.

## Open items

- At 1024 px (small laptops) the hero stacks (words above the photo) and runs about 1,300 px tall. Lowering the hero's column minimum in `clinics.css` would keep it side by side; that needs a new tag and a re-paste of all six blocks.
- The site-wide title format adds " — San Diego County Bike Coalition" (an em dash) to every page title. That is a site setting, not part of these pages.
- `CLAUDE.md` says "the Coalition" after the first full name; staff chose "the Bike Coalition" for these two pages. Settle one rule for the whole repo.
