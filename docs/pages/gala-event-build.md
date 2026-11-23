# Event page: Golden Gear Gala custom section (December 2026)

A custom section at the top of the gala's event page, `/calendar/golden-gear-gala` (also reached at `/gala`). Design: option B on the canvas board "Gala event page: custom section options". The event's own title, date, time and location fields, the "Tickets are $100" text and the Givebutter ticket widget below it stay native and unchanged.

| Piece | Repo file |
| --- | --- |
| Markup (pasted into one Code block) | [src/blocks/events/gala-event.html](../../src/blocks/events/gala-event.html) |
| Styles | [gala-event.css](../../src/blocks/events/gala-event.css) |
| Video, pause button, "Get tickets" scroll | [gala-event.js](../../src/blocks/events/gala-event.js) |
| Four photos (4:5 JPEG crops of the collage staff added to the page) | [img/](../../src/blocks/events/img) |
| Reel and poster (shared with the homepage teaser) | [../home/img/](../../src/blocks/home/img) |

What it shows, top to bottom:

- "You're invited", the headline "An evening for safer streets", two short paragraphs and a Spring Green "Get tickets, $100" button. The gala reel plays muted on a loop in the sprocket arch beside the words (below them on narrow columns), with a pause button. It only plays when the visitor's device allows motion and pauses when scrolled out of view.
- Four snapshots (the guests at the backdrop, charcuterie, bruschetta, kale salad), tilted like prints on a table. They straighten up when you point at them, unless the visitor's device asks for less motion.
- "What to expect": five numbered tiles (bike valet, photo booth, hors d'oeuvres, a drink on us, fun times).
- "What to wear": bold jewel tones with rich textures.

The words come from the event description staff wrote (saved in [docs/baseline/gala-event-2026-11-23.md](../baseline/gala-event-2026-11-23.md)), lightly edited. "Get tickets" scrolls down to the Givebutter widget on the same page; without JavaScript it opens the Givebutter page (givebutter.com/c/121526-golden-gear-gala).

The section sits in the event description column, which is about 900 px wide on a laptop, 495 px on a tablet and 340 px on a phone. Its layout follows the column's width (CSS container queries): under 560 px the intro stacks, the snapshots go two by two and the tiles become rows; from 560 px the snapshots sit four in a row and the tiles go two by two; from 720 px the reel sits beside the words; from 820 px the five tiles sit in a row.

## v0.14.0 (November 23, 2026)

- Tested on a local copy of the page layout at 390, 768, 1024 and 1440 px: nothing scrolls sideways, the reel plays, "Get tickets" scrolls to the widget and moves keyboard focus there.
- Go live: the old description's intro text, collage image and video blocks are replaced by one Code block holding `gala-event.html`. Saved first in docs/baseline/gala-event-2026-11-23.md.

Remove (or swap back to plain text) after December 15, 2026.
