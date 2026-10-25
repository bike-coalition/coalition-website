# Calendar page: native build

How to build the future Calendar page with native Squarespace blocks plus one stylesheet from this repo. No custom scripts. Staff keep adding events in Squarespace exactly as they do now.

The design is the "Future: Calendar" artboard on the redesign canvas.

## Before you start

The live Calendar collection already has what the page sorts by (checked October 21, 2026):

| Use | Category or tag | Upcoming now |
| --- | --- | --- |
| Signature events row | Tag: **Signature Event** | yes |
| Beginner to intermediate classes | Category: **City Cycling** | yes |
| Intermediate to advanced classes | Category: **Smart Cycling** | yes |
| Group rides | Category: **Rides** | none at the moment |
| Everything else | Categories: **Class**, **Events** | yes |

**The rule for staff:** every new event needs its category (and the Signature Event tag when it applies), or it won't show in the right row.

## 1. Make a hidden preview page

Per [the runbook](../runbook.md), nothing changes on the live Calendar first.

1. **Pages › Not Linked › +** › Blank page. Title it "Calendar preview". It stays out of the menus.
2. Optional: **Page Settings › General › Password** so only staff can open it.

## 2. Load the styling on that page only

**Page Settings › Advanced › Page Header Code Injection**, paste:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/bike-coalition/coalition-website@v0.1.0/src/tokens.css" integrity="sha384-xqRXfXfgNZ1ujUeIVsvwhW7fhxwO75wM0SsXa5xZsdKteWeiGChhmtmgCmqwAvjk" crossorigin="anonymous">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/bike-coalition/coalition-website@v0.1.0/src/pages/calendar.css" integrity="sha384-OwQIsFZmRQlxvxFou8lXLv/uvGOjNh2rC5PxfKpXAF+cDDyMHh6dve2qVYhPuQcE" crossorigin="anonymous">
```

The `@v0.1.0` tag pins the exact version. The `integrity` hash makes the browser refuse the file if it was ever altered.

## 3. Build the sections, top to bottom

Section color themes, as the live site names them: **Light Bold** = Spring Green, **Bright Inverse** = Teal, **White Bold** = light gray, **White** = white.

| # | Section | Theme | Blocks |
| --- | --- | --- | --- |
| 1 | Hero | Light Bold | Text: eyebrow "Calendar · Events, rides and classes", heading "Find your next ride.", one line. Button "See what's next" to the section below. Image block with a group ride photo, rounded corners. |
| 2 | On this page | White Bold | Buttons to each section below (use each section's Anchor link setting, if your editor shows it). |
| 3 | Signature events | White | Text heading "Signature events." Summary block, settings below. |
| 4 | Bike classes | White Bold | Heading "Bike classes." Two Summary blocks side by side (City Cycling, Smart Cycling). Button "All classes" to /classes. |
| 5 | Group rides | White | Heading "Group rides." Summary block (Rides). Text "Check out bikingis.fun for more group rides" linking to https://bikingis.fun. |
| 6 | Repair clinic | Light Bold | Text: East Village Repair Clinic, most Sundays, 10 am to 2 pm. Button "Reserve your spot" to /repair. |
| 7 | Calendar view | Bright Inverse | Calendar block, Calendar collection. |
| 8 | All upcoming | Bright Inverse | Summary block, all categories, List layout. |

### Summary block settings

Add each one with **+ › Summary**, then:

| Setting | Signature events | Classes (two blocks) | Group rides | All upcoming |
| --- | --- | --- | --- | --- |
| Content › Collection | Calendar | Calendar | Calendar | Calendar |
| Content › Filter | Tag: Signature Event | Category: City Cycling, then a second block for Smart Cycling | Category: Rides | none |
| Content › Items | 3 | 4 each | 3 | 12 |
| Layout | Carousel | List | Carousel | List |
| Display › Header text | Off (use the text heading) | "Beginner to intermediate" / "Intermediate to advanced" | Off | Off |
| Display › Show | Thumbnail, Title, Excerpt, Date | Title, Date | Thumbnail, Title, Date | Title, Excerpt, Date |
| Display › Read more link | On | On | On | On |

Squarespace Summary blocks for events show upcoming events, so past events drop off on their own. Confirm this once the blocks are in.

## 4. Check before going live

- Every row shows the right events, and nothing past.
- Cards render as white rounded cards with the Spring Green date pill.
- Tab through the page: every card, button and carousel arrow gets a visible focus ring.
- Phone width: carousels swipe, nothing overflows sideways.
- Text contrast on the teal sections (headings flip to Spring Green).

## 5. Go live

1. Build the same sections on the real Calendar page (or swap pages: rename the old one, give the preview its URL). Save the old page's content first.
2. Move the two `<link>` lines from the preview page to the real Calendar page's Page Header Code Injection.
3. Unpublish or delete the preview page.

To undo, remove the two lines. The blocks keep working with Squarespace's default styling.

## Later, optional

An All / Classes / Events filter needs a small script reading `/calendar?format=json`. That's a separate release, only if the filter turns out to matter.

## The live page today (October 25, 2026)

Separate from the redesign above. The current Calendar page loads [calendar-live.css](../../src/pages/calendar-live.css) from its Page Header Code Injection ([calendar-header-injection.html](../../src/pages/calendar-header-injection.html)):

- **Class rows:** each class heading is a text block with the class name, then a paragraph that becomes the level pill (as on the Classes page), then a one-line description. To change a level, edit that paragraph's words; the pill style stays.
- **Group rides:** while the Rides Summary block has nothing to show, the Group Rides section and its jump button are hidden, and the other two buttons close up. Publishing a ride brings both back on their own. In the editor the section always shows.
- The rules use this page's block IDs. If one of those blocks is deleted and re-added, or the jump buttons are rearranged, update the IDs and positions at the top of the file.
