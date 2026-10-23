# Footer text blocks before the October 23, 2026 edit

Native Squarespace Text blocks in the global footer. Saved here before changing them.

| Block | Before | After |
| --- | --- | --- |
| `block-yui_3_17_2_1_1736024945066_9503` (copyright, small text) | Copyright The Bike Coalition 2026; designed by Chloé Lauer and Jason Vance with support from Bit Palette. | © 2026 San Diego County Bike Coalition. Site by Chloé Lauer and Jason Vance with support from Bit Palette. |
| `block-yui_3_17_2_1_1736024945066_4969` (Compliance column, first line) | Tax ID 33-0418006 | Tax ID 33‑0418006 (the hyphen is a non-breaking hyphen, U+2011) |

Why:

- The copyright line used "The Bike Coalition" instead of the full name. "Designed by" became "Site by" so the line keeps its current length: with the full name, "Designed by" adds a fourth line at about 1024 px and spills out of the block. Checked at 390, 800, 900, 1024, 1280 and 1440 px: no more lines than before at any width.
- The Tax ID broke after the hyphen ("33-" / "0418006") at about 1024 px, where the column is 148 px and the line needs 179 px. With a non-breaking hyphen, the line breaks at the space instead, so the number stays whole.
- Trade-off: someone copying the number from the footer gets the U+2011 character instead of a plain hyphen. Most EIN fields only read the digits. Only this footer line uses it.

Live October 23, 2026. Checked logged out at 1440, 1024, 900 and 390 px on Mission and the homepage: new copyright text in small type, never more lines than before; Tax ID on one line at 1440 and 390, and at 1024 and 900 it breaks as "Tax ID" / "33‑0418006"; footer still 1,062 px on desktop and 1,396 px on phones; no sideways scroll.
