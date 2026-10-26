# Donate page: native build

How to build the San Diego County Bike Coalition's redesigned Donate page with native Squarespace blocks plus one small stylesheet from this repo, in time for Giving Tuesday, **December 1, 2026**. No custom scripts. The Givebutter form stays exactly as it is.

The design is the "Future: Donate" artboard on the redesign canvas. Why it changed: [the redesign review](../redesign-review-2026-10.md), item 3, "Make Donate convert".

## Native or custom?

`manifest.json` lists `/donate` as **undecided**. This guide recommends **native**:

- Both giving embeds (Givebutter and Infinite Giving) are already native Embed blocks on the live page. Keeping the page native means neither one is ever re-pasted.
- Staff can change the Giving Tuesday band, the impact amounts and the copy in Squarespace without a release.
- Everything the artboard needs is a native block. The stylesheet only adds four touches (arch photo, Peachy band, impact tiles, cards), and the page reads fine without it.

Once staff agree, change `/donate` to `"build": "native"` in `manifest.json` (open decision 1).

## Before you start

Have these answers first, or build with the `[FILL IN: ...]` text and swap it before go-live. The full list is at the end.

- The impact ladder's four amounts and what each one funds. **The amounts must match the Givebutter form's preset amounts**, which are set in Givebutter, not Squarespace.
- Whether there is a Giving Tuesday goal or match.
- Whether the form offers monthly giving, and which frequency it starts on.

**Don't change the Givebutter campaign as part of this build.** The preview page and the live page show the same form (widget `g8YMJp`), so any change in Givebutter shows on the live page right away.

## 1. Make the hidden preview page by duplicating the live one

Duplicating keeps the two embed blocks, the photos and the page's SEO settings, so nothing has to be re-pasted. Per [the runbook](../runbook.md), nothing changes on the live Donate page until go-live.

1. **Pages ›** Donate **› ⋯ › Duplicate.** Title the copy "Donate preview", slug `/donate-preview`.
2. Move it to **Not Linked**. Turn on **Page Settings › SEO › Hide page from search results**.
3. Leave it without a password if Claude should check it from the repo side (see step 2). Otherwise a password is fine.

The live Donate page is not touched in steps 1 to 5.

## 2. Set the section anchors

Each section in the table below has an anchor. Set it with **Edit section › Anchor link**, if your editor shows it. The anchors do three jobs: the hero and band buttons jump to the form (`#give`), the footer's existing "Bike Donations" link (`/donate#bike-donation`) finally lands somewhere (today it just opens the top of the page), and the stylesheet finds its sections by them.

If the editor has no anchor field: leave the preview page unpassworded and ask Claude to read each section's ID from it and swap them into `src/pages/donate.css` before the release.

## 3. Load the styling on the preview page only

After [donate.css](../../src/pages/donate.css) gets a release tag (runbook step 3), paste into the preview page's **Page Settings › Advanced › Page Header Code Injection**:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/bike-coalition/coalition-website@vX.Y.Z/src/pages/donate.css" integrity="sha384-HASH" crossorigin="anonymous">
```

The tag and hash get filled in at release, the same way as the Calendar page. `tokens.css` already loads on every page from the site-wide header, so this is the only line. Don't add anything else here: the Givebutter script already loads site-wide.

## 4. Build the sections, top to bottom

Section color themes, as the live site names them: **Light Bold** = Spring Green, **Bright Inverse** = Teal, **White Bold** = light gray, **White** = white. "Reuse" means rework a section that the duplicate already has; "Add" means a new blank section.

| # | Section | Anchor | Theme | How |
| --- | --- | --- | --- | --- |
| 1 | Hero | `start` | Bright Inverse | Add, above everything |
| 2 | Giving Tuesday band | `giving-tuesday` | Light Bold (the stylesheet turns it Peachy) | Add |
| 3 | Give | `give` | White | Reuse the live first section (it holds the Givebutter form) |
| 4 | Make it monthly | `monthly` | Light Bold | Reuse the live Membership section |
| 5 | More ways to give | `bike-donation` | White | Reuse the live "More Ways to Give" section (it holds the Infinite Giving form) |
| 6 | Keep rolling | `next` | White Bold | Add |
| 7 | Remove | | | Delete the live Bike Donation and Farm Fresh sections, after their content is in section 5 |

The global footer and the 18 cities ticker stay as they are.

### 1. Hero (Bright Inverse, anchor `start`)

| Block | Content and settings |
| --- | --- |
| Text | Small paragraph, all caps if your text styles allow: "Donate" |
| Text | Heading 1: "Your gift builds safer streets." One heading, not separate lines; use Shift+Enter if you want line breaks. |
| Text | Large paragraph: "Every gift to the San Diego County Bike Coalition pushes for safer, better-connected streets for everyone who rides. Together, we can make riding a bike mainstream and safe." |
| Button | Primary, "Donate now", link `#give` |
| Button | Secondary, "Give monthly", link `/membership` (open decision 3) |
| Image | Add an Image block and pick the live hero photo (the group ride on a new bike lane) from the image library; the duplicate's old first section uses it. Alt text: "A group ride rolls down a newly opened bike lane while a crowd cheers from the sidewalk". Tall crop, about 4 by 5. Leave its corner radius at 0: the stylesheet makes the arch. |

Text left, photo right on desktop. On phones, text first, photo below.

### 2. Giving Tuesday band (Light Bold, anchor `giving-tuesday`)

| Block | Content and settings |
| --- | --- |
| Text | Small paragraph, all caps: "Giving Tuesday" |
| Text | Heading 2: "Giving Tuesday is December 1." |
| Text | Large paragraph: "Put safer streets on your giving list this year and help make every corner of San Diego County better to ride." |
| Text | Bold paragraph: "[FILL IN: Giving Tuesday goal or match, if any]". Delete this block if there's neither. |
| Button | Primary, "Give for Giving Tuesday", link `#give` |

Text left, button right on desktop; stacked on phones. This band is seasonal: see step 7.

### 3. Give (White, anchor `give`)

Rework the duplicate's first section. **Don't touch its Givebutter Embed block** (see "The Givebutter form" below). Delete its old heading, intro text and image blocks, then build:

Left column:

| Block | Content and settings |
| --- | --- |
| Text | Small paragraph, all caps: "Give today" |
| Text | Heading 2: "What your gift does." |
| Text | Large paragraph: "Pick an amount and see where it goes. Choose your gift, add your details, and you're done." |
| Text | The impact ladder: one **bulleted list**, four items. Each item starts with the amount in **bold**, then what it funds: "**[FILL IN: $amount]** [FILL IN: what it funds]". Put the largest gift last; the stylesheet makes the last tile teal. Use a bulleted list here and nowhere else in this section, or that list turns into tiles too. |
| Text | Paragraph: "Rather give every month? Become a member." Link "Become a member" to `/membership`. |

Right column:

| Block | Content and settings |
| --- | --- |
| Embed | The existing Givebutter form, unchanged |
| Text | Small paragraphs, no list: "501(c)(3) nonprofit · EIN 33-0418006". "Candid Platinum Transparency" linked to our Candid profile (the same link as the footer seal). "Gifts are tax-deductible to the extent allowed by law." (open decision 9) |

**Phones:** in the mobile layout, put the form and the trust lines right after "What your gift does." and its intro, with the ladder below. A phone visitor who tapped "Donate now" should land on the form, not four tiles above it. The desktop layout keeps the ladder beside the form.

### 4. Make it monthly (Light Bold, anchor `monthly`)

Rework the duplicate's Membership section. Keep its photo (riders in front of Chula Vista City Hall).

| Block | Content and settings |
| --- | --- |
| Image | Existing photo. Alt text: "A group of riders with their bikes in front of Chula Vista City Hall". |
| Text | Small paragraph, all caps: "Monthly giving" |
| Text | Heading 2: "Make it monthly." (replaces "Membership") |
| Text | Large paragraph: "Become a sustaining member: keep the momentum going all year and enjoy the perks of membership." |
| Button | Primary, "Become a member", `/membership` (was "Individual Membership") |
| Button | Secondary, "Corporate membership", `/corporate` |

### 5. More ways to give (White, anchor `bike-donation`)

Rework the duplicate's "More Ways to Give" section (live theme is teal; change it to White). **Don't touch its Infinite Giving Embed block.** Its code has a line break inside the script address; it works as is, so leave it.

| Block | Content and settings |
| --- | --- |
| Text | Small paragraph, all caps: "More ways to give" |
| Text | Heading 2: "More ways to give." |
| Text | Small paragraph: "Consult your tax professional to understand how gifts like these may benefit your situation." |
| Text card | Heading 3: "Stocks and crypto". Paragraph: "Give appreciated assets directly and you typically avoid capital gains tax, so more of your gift goes to the mission." Links, one per line: "Stock guide (PDF)" to `/s/Stock-Donation-Guide.pdf`, "Crypto guide (PDF)" to `/s/Crypto-Donation-Guide.pdf`. |
| Text card | Heading 3: "Endowments". Paragraph: "Make your impact last for generations and keep San Diego's streets safer and more bikeable long into the future." Link: "Endowment guide (PDF)" to `/s/Endowment-Donation-Guide.pdf`. |
| Text card | Heading 3: "Donate a bike". Paragraph: "Email Doug, our bike manager, a photo and any details. ReBikeSD refurbishes it so a neighbor gets an affordable, reliable ride." Links: "Email Doug" to the same mailto link as today's Email Doug button (open decision 6), and "Need a receipt? Use the receipt form" to `/donation-receipt-form`. |
| Text card | Heading 3: "Farm Fresh to You". Paragraph: "Produce delivered to your door. Use code SDBIKECOALITION on new or current accounts: you get 5% off every box and we get 10% back." Small paragraph: "Existing accounts: go to My Account, then Apply Promo Code." Link: "Sign up with the code" to `https://www.farmfreshtoyou.com/compare`. (open decision 7) |
| Text | Heading 3: "Give stocks or crypto". Paragraph: "The full fair market value counts as a charitable deduction." Link: "Watch a video from Infinite Giving" to the existing Loom link. Place it beside the Infinite Giving form. |
| Embed | The existing Infinite Giving form, unchanged |

Four cards in a row on desktop, two by two on tablets, stacked on phones. Give the four cards the same height in the grid so their backgrounds line up. Every text block in this section that has a Heading 3 becomes a card, including "Give stocks or crypto"; the section heading is a Heading 2 so it stays plain.

Optional: the bike and produce photos from the old sections as small square images beside those cards' headings. Bike photo alt: "Two people stand behind a donated black and red Schwinn bike inside our office". Produce alt: "A Farm Fresh to You produce box filled with fruits and vegetables".

### 6. Keep rolling (White Bold, anchor `next`)

The shared "next step" band from the canvas, built natively. Three cards, each an Image, a Text block and a Button.

| | Card 1 | Card 2 | Card 3 |
| --- | --- | --- | --- |
| Small caps label | Join | Show up | Give more |
| Heading 3 | Become a member. | Lend a hand. | Plan a bigger gift. |
| Paragraph | Back safer streets every month, not just once. | Pick a shift at a ride, a class or an event and help more people ride. | Choose a fund, give stock or crypto, or talk with our Executive Director. |
| Button | "See the levels", `/membership` | "Pick a shift", `/volunteer` | "Explore major gifts", `/donors` |

Above the cards: small caps "Where to next", Heading 2 "Keep rolling.", paragraph "Money moves streets. Time and voices do too." Photos: pick from the image library (a crowd of members, volunteers at an event, a class).

### 7. Remove the old sections

Once their content is in section 5, delete the duplicate's Bike Donation (navy) and Farm Fresh sections. The old live page still has them.

## The Givebutter form

What must not change:

- **The block.** It's an Embed block holding exactly `<givebutter-widget id="g8YMJp"></givebutter-widget>`. Move the section around it, never the code. If the block is ever lost, add an Embed block and paste that one line, nothing more.
- **The widget ID**, `g8YMJp`. It's the donate campaign. Other Givebutter IDs on the site are event ticket widgets.
- **The script.** The form only works because the site-wide header (Pages › Code Injection › Header, file [header-injection.html](../../src/site/header-injection.html)) loads the Givebutter script on every page. Don't add a second copy to this page or this block; the event widgets just had their duplicates removed for this reason.
- **No CSS on it.** `donate.css` never targets the embed. Colors, amounts, monthly options and any goal bar are Givebutter campaign settings.

Squarespace turns embedded scripts off while you're logged in, so the form looks blank in the editor. Check it logged out or in a private window.

## 5. Check the preview before going live

Open `/donate-preview` logged out, in a private window, on a laptop and on a phone.

- The Givebutter form loads, preset amounts can be picked, "Other amount" works and you can reach the payment step. **Don't submit**: this is the live campaign and a gift would be real.
- The Infinite Giving form loads.
- "Donate now" and "Give for Giving Tuesday" jump to the form. `/donate-preview#bike-donation` opens at More ways to give.
- The hero photo has the arch, the band is Peachy, the impact items are tiles with the last one teal, the four cards are light green-gray.
- No `[FILL IN: ...]` text left anywhere on the page.
- Tab through the page: every button and link shows a focus ring, and the Givebutter fields can be reached by keyboard.
- Phone width: nothing scrolls sideways, the form comes before the ladder, buttons are at least 44 px tall.
- Contrast: teal text on the Peachy band is 4.79:1, the closest pass on the page. If Squarespace's Light Bold theme puts a lighter color on that band's text, tell Claude before go-live.
- Links: membership, corporate, volunteer, donors, the three PDF guides, the receipt form, Farm Fresh, the Loom video, the Candid profile.

## 6. Go live

Aim for at least a week before December 1, so there's time to fix anything before the Giving Tuesday emails go out.

1. **Save the old page.** It stays as it is and becomes the undo. Note today's SEO title and description (Page Settings › SEO): "Donate | Support Safer Streets – Donate Today" and "Support safe, vibrant streets in San Diego by donating to the Bike Coalition. Help promote cycling and sustainable transportation for all communities." Both get replaced in item 5.
2. Change the old page's slug from `/donate` to `/donate-old`, move it to Not Linked, hide it from search and give it a password.
3. Change the preview page's title to "Donate" and its slug from `/donate-preview` to `/donate`. The header Donate button, the footer links and every email that links to `/donate` now reach the new page. Section IDs and anchors move with it, so the stylesheet keeps working.
4. Check **Settings › Advanced › URL Mappings**: no rule should send `/donate` anywhere.
5. Set the new page's SEO title and description (open decision 10). The duplicate copied the old ones.
6. Run the step 5 checks again on `/donate`.
7. In the repo: record the page in [code-map.md](../code-map.md), add a `donate-header-injection.html` beside the Calendar one, and set `/donate` to native in `manifest.json`.

## 7. After Giving Tuesday

On December 2, change the band to [FILL IN: year-end message for December 2 to 31, or delete the band] (open decision 4). If the band is deleted, its stylesheet rule simply matches nothing. Update the "Give for Giving Tuesday" button text to match.

## Undo

- **Whole page:** swap the slugs back (new page to `/donate-preview`, old page to `/donate`, remove the old page's password). The old page still has its own Givebutter block, so the form keeps working.
- **Styling only:** delete the one `<link>` line from the page's Page Header Code Injection. The page still works with Squarespace's own styling: the band shows Light Bold green, the ladder shows as a bulleted list, the cards lose their backgrounds.
- Keep the old page until January 2027, after year-end giving, then delete it.

## Open decisions for staff

1. **Native build.** This guide assumes the page stays native. Agree, and `manifest.json` changes from undecided to native.
2. **Preset amounts and the impact ladder.** Confirm the Givebutter form's preset amounts, then the four amounts and what each funds. They must match.
3. **Monthly giving.** Does the Givebutter form offer monthly giving, and does it start on one-time or monthly? Should the hero's "Give monthly" button go to `/membership` (as drawn) or to the form's monthly option?
4. **Giving Tuesday.** Is there a goal or a match? What does the band say from December 2 to 31, or does it come down?
5. **Donate vs Donors.** Still open on [the open questions list](../future-pages-open-questions.md). This build keeps them separate, with Donors as the major-gifts page linked from Keep rolling.
6. **Bike donation email.** The Email Doug link goes to a personal Gmail address. Switch to an sdbikecoalition.org address?
7. **Farm Fresh to You.** Are the code and the 5% off / 10% back terms still current, and should the partnership stay on the Donate page?
8. **Short name after first reference.** The repo's `CLAUDE.md` says "the Coalition"; the organization's style rules say "the Bike Coalition". The page copy above avoids both (it uses "we" and "our") until one is chosen.
9. **Trust line wording.** Approve "Gifts are tax-deductible to the extent allowed by law." Should the Candid line be text (as drawn) or the seal image already used in the footer?
10. **SEO.** Suggested title "Donate | San Diego County Bike Coalition". Suggested description: "Give to the San Diego County Bike Coalition and help build safer, better-connected streets for everyone who rides, across all 18 cities in the county."

## Placeholders to fill

| Where | Placeholder |
| --- | --- |
| Section 2, Giving Tuesday band | [FILL IN: Giving Tuesday goal or match, if any] |
| Section 3, impact ladder item 1 | [FILL IN: $amount] and [FILL IN: what it funds] |
| Section 3, impact ladder item 2 | [FILL IN: $amount] and [FILL IN: what it funds] |
| Section 3, impact ladder item 3 | [FILL IN: $amount] and [FILL IN: what it funds] |
| Section 3, impact ladder item 4 (the teal tile) | [FILL IN: $amount] and [FILL IN: what it funds] |
| Step 7, after Giving Tuesday | [FILL IN: year-end message for December 2 to 31, or delete the band] |

Filled at release, not copy: the stylesheet's tag (`vX.Y.Z`) and hash in step 3, and the section IDs in `donate.css` only if the editor has no anchor field.

## The live page today (October 26, 2026)

Read from the published page. The duplicate in step 1 starts from this.

| # | Section | Theme | Blocks |
| --- | --- | --- | --- |
| 1 | Hero and form | White Bold | Image (group ride), Text (H1 "Support our Pursuit of Safe, Vibrant Streets"), Text (intro, monthly and stocks lines), Embed (Givebutter `g8YMJp`) |
| 2 | More Ways to Give | Teal | Text (stocks, crypto, endowments, tax note), Embed (Infinite Giving) |
| 3 | Membership | Light Bold | Image (Chula Vista City Hall), Text, Buttons "Corporate Membership" and "Individual Membership" |
| 4 | Bike Donation | Dark (navy) | Text headings, Image (donated Schwinn), Text, Button "Email Doug", Text (receipt form link) |
| 5 | Farm Fresh to You | White | Text (code and terms), Image (produce box), Text |

No page-level header code. The footer's "Bike Donations" link points to `/donate#bike-donation`, but no section on the live page has that anchor.
