# Code map: every piece of custom code on the live site

Captured October 21, 2026 from the public HTML of all 293 URLs in the sitemap. This repo is now the source of truth: edit the file here first, then paste it into Squarespace (until each piece moves to jsDelivr, see [jsdelivr-plan.md](jsdelivr-plan.md)).

Machine-readable version, with Squarespace block IDs: [src/blocks/registry.json](../src/blocks/registry.json).

## Site-wide

| What | Where in Squarespace | Repo file | Notes |
| --- | --- | --- | --- |
| Custom CSS (all pages) | jsDelivr, loaded by Code Injection › Header (v0.3.0). Squarespace Pages › Custom CSS is empty except a pointer comment. | [src/site/custom.css](../src/site/custom.css) | Live from jsDelivr since October 23, 2026 (step 3). The last Squarespace version (53) is saved exactly in [docs/baseline/squarespace-custom-css-v53.less](baseline/squarespace-custom-css-v53.less). |
| Header code (all pages) | Pages › Code Injection (search "code injection" in the dashboard) › Header | [src/site/header-injection.html](../src/site/header-injection.html) | Givebutter widget script only. Google Analytics and the cookie banner come from Squarespace settings, not code injection. |
| Footer code | Code Injection › Footer | none | Empty. |
| Page-level header code: Calendar | Calendar page settings › Advanced › Page Header Code Injection | [src/pages/calendar-header-injection.html](../src/pages/calendar-header-injection.html) loads [calendar-live.css](../src/pages/calendar-live.css) | Live since October 25, 2026 (v0.6.0; v0.6.1 arrows below the cards; v0.6.3 pill beside a bigger title, v0.6.4 pill centered on the title letters, arrows tight to the cards, classes section rows sized to content). Level pills under the class headings; hides the Group Rides section and its jump button while the Rides Summary block is empty. Targets block IDs: update them if those blocks are re-added. |
| Page-level header code: Classes | Classes page settings › Advanced › Page Header Code Injection | [src/pages/classes-header-injection.html](../src/pages/classes-header-injection.html) loads [classes.css](../src/pages/classes.css) | Live since October 25, 2026 (v0.5.0). Clips sideways overflow and hides the footer cities band on this page. |
| Page-level header code: Board Candidates | Board Candidates page settings › Advanced › Page Header Code Injection | [src/pages/board-candidates-header-injection.html](../src/pages/board-candidates-header-injection.html) loads [board-candidates.css](../src/pages/board-candidates.css) | Ready for v0.7.0, not live (the page has no header code today). Clips sideways overflow on this page. |
| Page-level header code: CicloSDias | CicloSDias page settings › Advanced › Page Header Code Injection | [src/pages/ciclosdias-header-injection.html](../src/pages/ciclosdias-header-injection.html) loads [ciclosdias.css](../src/pages/ciclosdias.css) | Ready for v0.7.0, not live (the page has no header code today). Clips sideways overflow and turns on smooth scrolling on this page. |
| Page-level header code: Code Preview | Code Preview page settings › Advanced | none in repo | Hidden test page; loads the release under test. |

## Code blocks

| Page | What | Repo file | Size | Has | Notes |
| --- | --- | --- | --- | --- | --- |
| Every page (global footer) | Candid transparency seal | [footer/candid-seal.html](../src/blocks/footer/candid-seal.html) | 0.5 KB | HTML | Repo copy fixes the screen-reader label (was "San Diego County Bicycle Coalition") and adds `alt` text. Live since October 22, 2026 (step 2); seal size and footer layout unchanged. |
| Every page (global footer) | 18 cities band and ticker | [footer/cities-ticker.html](../src/blocks/footer/cities-ticker.html) + [.css](../src/blocks/footer/cities-ticker.css) | 3.1 KB block | HTML; CSS from jsDelivr v0.2.0 | Live on jsDelivr since October 21, 2026 (step 1). Classes renamed to `bc-`; keeps `sdbc-cities` until the Classes block moves. Loads Archivo and Inter from Google Fonts. |
| Homepage | What people are saying (testimonials carousel) | [home/testimonials.html](../src/blocks/home/testimonials.html) + [.css](../src/blocks/home/testimonials.css) + [.js](../src/blocks/home/testimonials.js) | 5.9 KB block | HTML; CSS and JS from jsDelivr v0.4.0 | Live on jsDelivr since October 23, 2026 (step 4). Classes renamed to `bc-quotes__`. Quotes flagged for review: "Ocsar G." (likely Oscar), "SD Bike Coalition" and "clickiness" in James T.'s quote. |
| Classes | Find your class (carousel) | [classes/find-your-class.html](../src/blocks/classes/find-your-class.html) + [.css](../src/blocks/classes/find-your-class.css) + [.js](../src/blocks/classes/find-your-class.js) + [img/](../src/blocks/classes/img) | 10.5 KB block | HTML; CSS, JS and two photos from jsDelivr v0.5.0 | Live since October 25, 2026 (step 5). Was 329 KB with base64 photos. Classes renamed to `bc-classes__`. |
| Classes | Let us come to you (free classes at schools and workplaces) | [classes/let-us-come-to-you.html](../src/blocks/classes/let-us-come-to-you.html) + [.css](../src/blocks/classes/let-us-come-to-you.css) | 14 KB block | HTML (inline styles); CSS from jsDelivr v0.5.0 | Live since October 25, 2026 (step 5). Its page-wide rules moved to the Classes page header code. |
| Board Candidates | Full page | [board-candidates/candidates.html](../src/blocks/board-candidates/candidates.html) + [.css](../src/blocks/board-candidates/candidates.css) + [.js](../src/blocks/board-candidates/candidates.js) | 17 KB block | HTML; CSS and JS ready for jsDelivr v0.7.0 | Split in step 6, not live: the live block is still the 19.1 KB pasted version (saved in git at 5cc3ab6). Classes renamed to `bc-board__`; photo links moved from the script to `data-photo` in the markup. Page-wide rule in [src/pages/board-candidates.css](../src/pages/board-candidates.css). Loads Archivo Black and Inter. Seasonal (November 2026 election). Notes: [pages/step6-notes.md](pages/step6-notes.md). |
| CicloSDias | Full page | [ciclosdias/ciclosdias.html](../src/blocks/ciclosdias/ciclosdias.html) + [.css](../src/blocks/ciclosdias/ciclosdias.css) | 22 KB block | HTML (inline styles); CSS ready for jsDelivr v0.7.0 | Split in step 6, not live: the live block is still the pasted version (saved in git at 5cc3ab6). Classes renamed to `bc-ciclo`. Page-wide rules in [src/pages/ciclosdias.css](../src/pages/ciclosdias.css). Loads Montserrat and Open Sans; its own palette outside the brand. Still promotes the October 18, 2026 event. Notes: [pages/step6-notes.md](pages/step6-notes.md). |
| Bike the Bay Festival event | Givebutter widget | [events/bike-the-bay-festival-widget.html](../src/blocks/events/bike-the-bay-festival-widget.html) | 52 B | HTML | Relies on the site-wide Givebutter script. |
| 5 City Cycling: La Mesa events | Givebutter ticket widget | [events/givebutter-ticket-widget.html](../src/blocks/events/givebutter-ticket-widget.html) | template | HTML | One block per event, identical except the widget ID (table below). Since October 26, 2026 (step 7) each holds only the widget tag and relies on the site-wide Givebutter script, like every other event page. |

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
