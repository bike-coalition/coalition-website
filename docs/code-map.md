# Code map: every piece of custom code on the live site

Captured October 21, 2026 from the public HTML of all 293 URLs in the sitemap. This repo is now the source of truth: edit the file here first, then paste it into Squarespace (until each piece moves to jsDelivr, see [jsdelivr-plan.md](jsdelivr-plan.md)).

Machine-readable version, with Squarespace block IDs: [src/blocks/registry.json](../src/blocks/registry.json).

## Site-wide

| What | Where in Squarespace | Repo file | Notes |
| --- | --- | --- | --- |
| Custom CSS (all pages) | Design › Custom CSS | [src/site/custom.css](../src/site/custom.css) | 28.7 KB live (version 53). Formatted here for reading; rules are identical. |
| Header code (all pages) | Settings › Developer tools › Code Injection › Header | [src/site/header-injection.html](../src/site/header-injection.html) | Givebutter widget script only. Google Analytics and the cookie banner come from Squarespace settings, not code injection. |
| Footer code | Code Injection › Footer | none | Empty. |
| Page-level header code | Page Settings › Advanced | none | No page has its own header code. |

## Code blocks

| Page | What | Repo file | Size | Has | Notes |
| --- | --- | --- | --- | --- | --- |
| Every page (global footer) | Candid transparency seal | [footer/candid-seal.html](../src/blocks/footer/candid-seal.html) | 0.3 KB | HTML | Screen-reader label says "San Diego County Bicycle Coalition". Empty `alt` on the seal image. |
| Every page (global footer) | 18 cities band and ticker | [footer/cities-ticker.html](../src/blocks/footer/cities-ticker.html) + [.css](../src/blocks/footer/cities-ticker.css) | 3.1 KB block | HTML; CSS from jsDelivr v0.2.0 | Moved to jsDelivr in step 1 (block swap pending). Classes renamed to `bc-`; keeps `sdbc-cities` until the Classes block moves. Loads Archivo and Inter from Google Fonts. |
| Homepage | What people are saying (testimonials carousel) | [home/testimonials.html](../src/blocks/home/testimonials.html) | 9.9 KB | HTML, CSS, JS | Uses `sdbc-` class names and the `sdbcQuotes` id. |
| Classes | Class carousel, paths and FAQ | [classes/find-your-class.html](../src/blocks/classes/find-your-class.html) | 329 KB | HTML, CSS, JS | Two photos are embedded as base64 (most of the size), which slows the page. |
| Classes | Free classes at your school or workplace | [classes/let-us-come-to-you.html](../src/blocks/classes/let-us-come-to-you.html) | 13.7 KB | HTML, CSS | Also hides the footer cities band on the Classes page, and sets `overflow-x: clip` on the whole page. |
| Board Candidates | Full page | [board-candidates/candidates.html](../src/blocks/board-candidates/candidates.html) | 19.1 KB | HTML, CSS, JS | Loads Archivo Black and Inter. Seasonal (November 2026 election). |
| CicloSDias | Full page | [ciclosdias/ciclosdias.html](../src/blocks/ciclosdias/ciclosdias.html) | 21.9 KB | HTML, CSS | Loads Montserrat and Open Sans; its own palette outside the brand. Still promotes the October 18, 2026 event. |
| Bike the Bay Festival event | Givebutter widget | [events/bike-the-bay-festival-widget.html](../src/blocks/events/bike-the-bay-festival-widget.html) | 52 B | HTML | Relies on the site-wide Givebutter script. |
| 5 City Cycling: La Mesa events | Givebutter ticket widget | [events/givebutter-ticket-widget.html](../src/blocks/events/givebutter-ticket-widget.html) | template | HTML, JS | One block per event, identical except the widget ID (table below). Each loads the Givebutter script again, on top of the site-wide one. |

### Givebutter ticket widgets

| Event page | Widget ID |
| --- | --- |
| /calendar/012327-city-cycling-la-mesa | gJRroP |
| /calendar/031327-city-cycling-la-mesa | gBZXqd |
| /calendar/052227-city-cycling-la-mesa | prWZxz |
| /calendar/061227-city-cycling-la-mesa | g8MXRw |
| /calendar/080727-city-cycling-la-mesa | LZoaX2 |
| /calendar/bike-the-bay-festival | paXQlK (no script in the block) |

## Not custom code, listed so nothing is missed

Squarespace-native embeds stay in Squarespace: Givebutter forms on Donate, Donors, Membership, Corporate and Tacos; Point on Volunteer and Teach; Google appointment calendars on Repair and Rolling Forward; the Google Docs embed on Bylaws; YouTube on Clubs and Bike Share; the Google Map on Contact.

## How this was captured

Squarespace renders Code block contents into the page as written. The capture strips Squarespace's own wrapper (`sqs-code-container` and its transform styles) so each file is what was pasted into the block. Whitespace may differ slightly from the editor copy. To recapture, rerun the crawl and compare against these files.
