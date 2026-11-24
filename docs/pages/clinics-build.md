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
