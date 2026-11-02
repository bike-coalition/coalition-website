# Newsletter page: native build ("Join the ride")

How to build the redesigned Newsletter page with native Squarespace blocks plus one small stylesheet from this repo. No custom scripts. The signup form stays Squarespace's own Newsletter block, so signups keep going to the same list and staff keep editing it in Squarespace.

The design is the "Future: Newsletter" artboard on the redesign canvas. The stylesheet is [src/pages/newsletter.css](../../src/pages/newsletter.css).

## What the stylesheet does, and what it can't

It restyles the form to match the artboard: a light green card, bold Teal Green labels above white fields, a Teal Green "Sign up" button with Spring Green text, all in Inter. It also sets the "Newsletter" label and the big "JOIN THE RIDE." headline, and gives the photo the sprocket arch.

Squarespace still owns how the form works: what it asks for, where signups go, the thank-you message, error checking and the spam check. None of that changes.

Differences from the artboard, on purpose:

- **Field borders.** The artboard draws white fields with a white border on the light green card, which is 1.1:1 and hard to see. The fields get a 2 px green border at 3.08:1 instead.
- **Placeholders.** Squarespace hides the labels and shows placeholder text in the fields. The stylesheet shows the labels and hides the placeholders, so the label stays visible while someone types.
- **Headline font.** The artboard asks for regular-width Obviously, extra bold. The site's Adobe Fonts kit only serves Obviously Wide (medium and bold) on this page, so the headline uses Obviously Wide Bold, a little smaller. If the kit gets regular-width Obviously later, change the `h1` rule.
- **Keep rolling band.** The artboard ends with the shared "Keep rolling" band. It's left out: it belongs on every page, so it should be built once for the whole site.

One problem the stylesheet can't fix: Squarespace doesn't connect the First Name and Last Name labels to their fields, so a screen reader announces those two fields by their (hidden) placeholder text, "First Name" and "Last Name". That still works, but only Squarespace can fix it properly.

## 1. Make the hidden preview page by duplicating the live one

Duplicating keeps the Newsletter block and its storage, the photo and the SEO settings. Nothing changes on the live page until step 6.

1. **Pages ›** Newsletter **› ⋯ › Duplicate.** Title the copy "Newsletter preview", slug `/newsletter-preview`.
2. Move it to **Not Linked** right away, so it never shows in the menus. Turn on **Page Settings › SEO › Hide page from search results**.
3. Open the copy's Newsletter block, **Storage** tab, and check it sends signups to the same place as the live block. Don't change it.

## 2. Hero section (keep its Bright Inverse theme)

The section today holds three blocks: the Newsletter block, a text block ("Donations are welcome! ...") and the photo of two riders.

1. **Text block:** reuse the "Donations are welcome!" block. Replace its text with three paragraphs, in this order:
   - Paragraph: `Newsletter` (the stylesheet turns it into the small caps label)
   - Heading 1: `Join the ride.`
   - Paragraph: `Get the latest biking news, events and local updates from the San Diego County Bike Coalition, straight to your inbox.`

   Move it to the top left, above the form. The donation line moves to the new band in step 3.
2. **Newsletter block › Content:** clear the **Title** ("Join the Ride") and the **Description**, so the page doesn't say it twice. Keep the name and email fields as they are. Change the button label from "Sign Up" to `Sign up`.
3. **Newsletter block:** put it under the text block, in the same columns (on desktop, the left half).
4. **Photo:** keep it in the right half, about 4 wide to 5 tall, running to the bottom of the section. The stylesheet rounds its top into the arch.
5. **Section divider:** the live section has a divider at the bottom. The artboard has none. Turn it off if the band in step 3 looks better without it (open decision 3).
6. **Phone layout:** text block, then the form, then the photo.

## 3. Donate band (new section, Light Bold)

Add a section right under the hero. Theme **Light Bold** (Spring Green).

- **Text block:** Heading 2 `Want to do more than read about it?`, then a paragraph: `Donations are welcome. Every gift goes toward making San Diego an amazing place to ride a bike.`
- **Button block:** `Donate`, linking to `/donate`. On desktop, to the right of the text; on phones, under it.

No stylesheet rule is needed here. If the theme's button isn't Teal Green with Spring Green text, tell Claude.

## 4. Load the stylesheet on the preview page

Claude tags a release and gives you the line, which also goes in the repo as `src/pages/newsletter-header-injection.html`. Paste it in the preview page's **Page Settings › Advanced › Page Header Code Injection** and save.

## 5. Check the preview page

- Desktop and phone: it looks like the artboard; nothing scrolls sideways at phone width.
- Tab through the form: each field and the button show a green focus ring.
- **Sign up once with a staff email address**, then check it arrives in the same list as signups from the live page, and that the thank-you message shows in green on the card. (Claude doesn't submit the form itself.)
- Try "Sign up" with the email field empty: the error shows in a white box on the card.
- The Donate button goes to `/donate`.

## 6. Go live

1. **Save the old page.** It stays as it is and becomes the undo. Today's SEO title is "Newsletter | Stay Informed & Ride" (Squarespace adds the site name) and the description is "Subscribe to San Diego County Bike Coalition's newsletter for updates on biking events, advocacy, and community news to enhance your cycling experience."
2. Change the old page's slug from `/newsletter` to `/newsletter-old`, move it to Not Linked, hide it from search and give it a password.
3. Change the preview page's title to "Newsletter" and its slug from `/newsletter-preview` to `/newsletter`. Every menu, footer and email link to `/newsletter` now reaches the new page.
4. Check **Settings › Advanced › URL Mappings**: no rule should send `/newsletter` anywhere.
5. Run the step 5 checks again on `/newsletter`.
6. In the repo: record the page in [code-map.md](../code-map.md) and set `/newsletter`'s status in `manifest.json`.

## Undo

- **Whole page:** swap the slugs back (new page to `/newsletter-preview`, old page to `/newsletter`, remove the old page's password). The old page still has its own Newsletter block.
- **Styling only:** delete the `<link>` line from the page's Page Header Code Injection. The form goes back to Squarespace's look; nothing stops working.
- Keep the old page for a month after go-live, then delete it.

## Open decisions for staff

1. **New wording.** The intro line, the band's two lines and the "Sign up" label are new copy from the artboard. Approve or change them.
2. **Thank-you message.** It says "Thank you!" today (Newsletter block settings). Keep it, or write a warmer one.
3. **Section divider** under the hero: keep or drop.
4. **Short name after first reference.** The repo's `CLAUDE.md` says "the Coalition"; the organization's style rules say "the Bike Coalition". This page's copy uses neither.

## The live page today (November 2, 2026)

Read from the published page.

| # | Section | Theme | Blocks |
| --- | --- | --- | --- |
| 1 | Join the Ride | Bright Inverse, with a section divider | Newsletter (title "Join the Ride", description "Subscribe to our newsletter for the latest biking news, events, and other local updates", First and Last Name, Email Address, "Sign Up"), Text ("Donations are welcome! All proceeds go directly towards making San Diego an amazing place to ride bikes!" linked to `/donate`), Image (two riders in red jerseys) |

No page-level header code. No Heading 1 on the page.
