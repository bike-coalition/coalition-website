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
- "What to wear": bold jewel tones (ruby red, emerald green, sapphire blue, amethyst purple) with rich textures (velvet, tweed, silk, satin).

The words come from the event description staff wrote (saved in [docs/baseline/gala-event-2026-11-23.md](../baseline/gala-event-2026-11-23.md)), lightly edited. "Get tickets" scrolls down to the Givebutter widget on the same page; without JavaScript it opens the Givebutter page (givebutter.com/c/121526-golden-gear-gala).

The section sits in the event description column, which is about 900 px wide on a laptop, 495 px on a tablet and 340 px on a phone. Its layout follows the column's width (CSS container queries): under 560 px the intro stacks, the snapshots go two by two and the tiles become rows; from 560 px the snapshots sit four in a row and the tiles go two by two; from 720 px the reel sits beside the words; from 820 px the five tiles sit in a row.

## v0.14.0 (November 23, 2026)

- Tested on a local copy of the page layout at 390, 768, 1024 and 1440 px: nothing scrolls sideways, the reel plays, "Get tickets" scrolls to the widget and moves keyboard focus there.
- Old description saved first in docs/baseline/gala-event-2026-11-23.md.

## Go-live record (November 23, 2026)

- At Jason's go-ahead ("option B please build and publish to the website"): in the event's editor, added a Code block at the top of the description (`block-yui_3_17_2_1_1795473296867_3027`) holding `gala-event.html` from v0.14.0. Its text matches the repo file exactly.
- Removed the old intro text block, the collage image block and the video block (the same 28.6 second reel the section now plays). Kept the "Tickets are $100" text block and the Givebutter widget Code block, unchanged.
- **Watch out:** removing the image first made Squarespace merge the two text blocks on either side of it into one. Undone; remove a text block before the block that separates it from another text block.
- Checked live: the description now runs section, "Tickets are $100" text, Givebutter widget. At 1440 px the reel sits beside the words and plays, the four snapshots and five tiles sit in rows, and "Get tickets" scrolls to the widget and moves focus there. At 390 px everything stacks inside the column and nothing from the section runs past it.
- Not checked by Claude: buying a ticket.

## "What to wear" details (November 23, 2026)

Staff's fuller wording: "Bold jewel tones such as ruby red, emerald green, sapphire blue, and amethyst purple, paired with rich textures like velvet, tweed, silk, and satin." Markup only, so the stylesheet and script stay at v0.14.0; the block was pasted from this commit's file.

## v0.15.0 (November 23, 2026): no one cropped, outfit ideas, tiles reordered

- **Group snapshot shows everyone.** The 4:5 crop cut people off at both edges, so "See you there" now shows the whole photo (`img/gala-crowd-full.jpg`, all eleven people) as a wide print: two columns' worth on laptops and tablets, a full row on phones. `img/gala-crowd.jpg` stays in the repo only so older tags keep working.
- **Outfit ideas in "What to wear":** five Unsplash photos (Unsplash License, free to use), each shown whole in a white frame with a color pill, staff picks 5, 1, 3, 6 and 7 from the board "Gala event page: what to wear image options". One row at equal height from 560 px, three then two on phones. A credit line names the photographers.

| File | Pill | Unsplash page | Photographer |
| --- | --- | --- | --- |
| img/wear-ruby-satin.jpg | Ruby | unsplash.com/photos/woman-in-a-red-dress-with-a-high-slit-_kx6ShhfCvs | FOTOGRAFÍA EDITORIAL |
| img/wear-emerald-gown.jpg | Emerald | unsplash.com/photos/woman-in-a-long-emerald-green-gown-with-lace-er3bBysHPI8 | FOTOGRAFÍA EDITORIAL |
| img/wear-sapphire-sparkle.jpg | Sapphire | unsplash.com/photos/woman-in-a-sparkling-blue-dress-on-red-background-Y1VzhoaULkM | Brooke Balentine |
| img/wear-ruby-blazer.jpg | Ruby | unsplash.com/photos/man-in-red-coat-standing-on-road-during-daytime-ssnSQS6-UbA | Brock Wegner |
| img/wear-plum-jacket.jpg | Plum | unsplash.com/photos/man-in-purple-and-black-suit-sitting-on-black-armchair-20XqbpJJn0U | Bulbul Ahmed |

- **"What to expect" order (staff request):** hors d'oeuvres, a drink on us, bike valet, photo booth, then "Holiday cheer" (was "Fun times").
- Tested on the local copy at 390 and 1440 px: nothing scrolls sideways, every photo shows whole.
- Live November 23, 2026: pasted into the event's Code block (it held the previous version exactly; it now matches this file). Checked live at 1440 and 390 px: the group photo and all five outfit photos render at their own shape (nothing cropped), the tiles read in the new order, and nothing from the section runs past the column.

## v0.16.0 (November 23, 2026): fabric swatches instead of outfits

Staff asked for fabric swatches only, not full outfits, so the five outfit photos came out (they stay in tag v0.15.0) and "What to wear" now shows five square swatches. Narrow columns: three, then two, with the name underneath. From 560 px: one row. From 720 px: the names sit in Spring Green pills.

| File | Name | Unsplash page | Photographer |
| --- | --- | --- | --- |
| img/swatch-ruby-satin.jpg | Ruby satin | unsplash.com/photos/red-textile-HyBXy5PHQR8 | MontyLov |
| img/swatch-emerald-velvet.jpg | Emerald velvet | unsplash.com/photos/green-textile-in-close-up-image-HEMIBJ8QQuA | engin akyurt |
| img/swatch-sapphire-velvet.jpg | Sapphire velvet | unsplash.com/photos/blue-textile-in-close-up-photography-A4rqd2g-eLo | Kseniya Lapteva |
| img/swatch-amethyst-silk.jpg | Amethyst silk | unsplash.com/photos/purple-fabric-with-soft-folds-LnrNWayL4rE | Alexander Grey |
| img/swatch-tweed.jpg | Tweed | unsplash.com/photos/a-close-up-of-a-blue-and-white-tweed-fabric-B8ZmImP2ww4 | Divazus Fabric Store |

Tested on the local copy at 390 and 1440 px: nothing scrolls sideways.

Live November 23, 2026: pasted into the event's Code block (it held v0.15.0 exactly; it now matches this file). Checked live at 1440 px (one row, names in pills) and 390 px (three then two, everything inside the column).

Remove (or swap back to plain text) after December 15, 2026.
