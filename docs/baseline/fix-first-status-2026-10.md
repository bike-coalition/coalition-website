# Fix first status, October 26, 2026

A re-check of every item in [site-issues-2026-10.md](site-issues-2026-10.md) against the live public site. Checked on October 26, 2026, logged out and read only: pages fetched with `curl` (including Squarespace's public `?format=json` view) and a few looked at in the built-in browser. Nothing was edited, no form was submitted, and nobody logged in.

What a logged-out check can't see: form storage settings, URL mappings, page settings and anything in the Squarespace editor. Those items are marked **cannot tell**.

Block IDs below come from the live HTML. In the editor you won't see the ID; use the quoted text to find the block.

## Summary

| Status | Count |
| --- | --- |
| Still open | 35 |
| Fixed | 3 |
| Cannot tell from the public site | 6 |

## The three items left open from the fix-first list

### 1. Clubs: "Join" section still has no club signup (still open)

**What it does now.** On [/clubs](https://sdbikecoalition.org/clubs), the "Join" text block (`block-yui_3_17_2_1_1738640740527_76386`) says "If your bike club is not yet a member, we invite you to join the Coalition today." The only two buttons beside it are:

| Block | Button text | Goes to |
| --- | --- | --- |
| `block-yui_3_17_2_1_1738803822656_25223` | Sign up for our Newsletter | /newsletter |
| `block-b0cb0912b0cf9a2a385b` | Donate today! | /donate (opens a new tab) |

A club that wants to join still has nowhere to go. The change staff saved is not on the live page.

**Why the saved change may not show.** The public "last updated" time for /clubs is March 30, 2026. That time doesn't always change for block edits (the Newsletter page still shows August 2025 after its October storage fix), so it's only a hint. Common causes: leaving the editor with **Exit** instead of **Save**, editing a different page, or editing the button on a Not Linked copy. There is no public duplicate at /clubs-1, /clubs-2, /clubs-copy or /clubs-preview.

**Fix.**

1. Decide where club signups go: [FILL IN: club signup destination]. Options that already exist: an email to clubs-chair@sdbikecoalition.org (listed on /meetings), or a new Squarespace form block on /clubs. The membership page has no club tier today.
2. **Pages** › **Group Rides & Clubs** › **Edit**.
3. Click the **Sign up for our Newsletter** button (or add a new Button block beside the "Join" text). Click the pencil.
4. **Text:** "Join as a club". **Link:** the destination from step 1 (for email, `mailto:clubs-chair@sdbikecoalition.org` with nothing after it, no `?`).
5. Click **Save** at the top left, not **Exit**. Wait for "Saved".
6. Check it in a private window (logged out): open /clubs, click the button, confirm it goes to the right place.

While editing this page: the two "Bicycle Coalition" references and the "Bike Coalition's Origin Story" heading are on the name list below. The "City Cycling Classes" link goes to /calendar; the open questions ask whether it should go to /classes.

### 2. Ambassador form: present, test submission still needed (cannot tell if storage works)

**What can be seen publicly.** [/ambassador-program](https://sdbikecoalition.org/ambassador-program) has a native Squarespace form block, `block-a6691a31f77dcaacaf0a`, under "Become an Ambassador!".

| Setting | Live value |
| --- | --- |
| Form name | Ambassador Program Form 2 |
| Fields | Name (required), Email (required), Phone (optional), About you (required, placeholder "Why are you passionate about bikes?") |
| Submit button | Become a Bike Ambassador |
| Message after submit | "Thank you!" |
| Redirect after submit | none |
| CAPTCHA | on |
| SMS consent | on, with no privacy policy or terms link set |

The public page never shows where submissions go. Storage is only visible in the editor.

**How staff send one test submission.**

1. Before testing, open the block's settings: **Pages** › **Be an Ambassador** › **Edit** › click the form › pencil › **Storage**. Note which destination is connected (email address, Google Drive sheet or Mailchimp list). **Exit** without changing anything.
2. Tell whoever receives Ambassador applications that a test is coming, so it isn't treated as a real applicant.
3. Open /ambassador-program in a private window (logged out).
4. Fill in: Name "TEST Ambassador form", Email: your own staff address, leave Phone blank, About you "Test submission on [date], please delete". Leave any SMS consent box unchecked.
5. Complete the CAPTCHA and click **Become a Bike Ambassador**. Confirm "Thank you!" appears.
6. Within 10 minutes, look in the destination from step 1: the inbox (check spam too), the Google Sheet's newest row, or the Mailchimp list. If nothing arrives, go back to **Storage** and reconnect it, then test once more.
7. Delete the test entry from wherever it landed.
8. Record the result in this file: date, who tested, where it arrived.

**Worth fixing at the same time.**

- "Thank you!" tells an applicant nothing. Suggested message: "Thanks for applying to be an Ambassador. [FILL IN: who replies] will reach out within [FILL IN: time frame]." The open questions still list "who receives applications and replies".
- SMS consent is on but there's no privacy policy link. Either turn SMS consent off (the form doesn't need it) or add the /privacy-policy link in the form settings.
- The page says "San Diego County Bicycle Coalition" once and ends with a 🌟 emoji (see the lists below).

### 3. After a Crash: "[MADD Support Literature]" placeholder still live (still open)

**What it does now.** On [/traffic-violence](https://sdbikecoalition.org/traffic-violence), the "Additional Resources" text block (`block-e423c76631174d57174d`) still shows the bracketed text "[MADD Support Literature]", then an em dash and "guides for injury and bereavement, in English & Spanish", with no link. None of the other nine resources in that block are links either.

**Fix.**

1. Get the URL: [FILL IN: MADD support literature URL]. MADD's site blocks automated checks, so a person needs to open madd.org, find the victim services publications page, and copy its address.
2. **Pages** › **After a Crash** › **Edit**. Click the "Additional Resources" text block.
3. Replace "[MADD Support Literature]" and the em dash after it with "MADD support literature:" so the line reads "MADD support literature: guides for injury and bereavement, in English & Spanish".
4. Highlight "MADD support literature", click the link icon, paste the URL, **Apply**.
5. Do the same for the other nine resources once their URLs are known ([FILL IN: links for the 9 other resources]).
6. **Save**. Check logged out that the link opens the MADD page.

The other After a Crash items (no local resources, no Coalition contact, the Facebook group link) are in the list below.

## Still open

### Fix soon

| Issue | Page | Live now | Fix |
| --- | --- | --- | --- |
| CicloSDias promoted as upcoming | /ciclosdias | Code block `block-yui_3_17_2_1_1792047490262_458` still says "Sunday, October 18, 2026" three times and invites people to come. | This block is a repo file: edit [src/blocks/ciclosdias/ciclosdias.html](../../src/blocks/ciclosdias/ciclosdias.html) first (recap wording, or next date [FILL IN: next CicloSDias date]), commit, then paste into the Code block per [the runbook](../runbook.md). |
| Meeting dates have no year, past dates listed | /meetings | Text block `block-354de407230204f384c4`: "Mar. 18, May 13, Jul. 8, Sep. 9, Nov. 11" and so on, no year. Only the November dates are still ahead. | Edit each meeting's text: drop past dates, add the year and next dates ("Nov. 11, 2026" and [FILL IN: 2027 dates]). |
| Board Meetings has no location or Zoom link | /meetings | Same block: "Meets at 6:30 pm on ..." with no place or link. The other three meetings have Zoom links. | Add [FILL IN: Board meeting location or Zoom link]. The Board chair line also has no name. |
| 30 past events in the calendar list | /calendar | 42 events in the native event list: 12 upcoming, 30 past. The new Summary block sections above it show upcoming only. | Hide past events in the Calendar page's event list settings if the option shows, or unpublish past events (they stay in the collection). |
| "Calendar View" and "Bike Classes" buttons go through /full-calendar | /calendar | Buttons `block-e9a0687bf1244af1aea1` (to `https://sdbikecoalition.org/full-calendar#calendar-view`) and `block-39d61feebf827d475859` (to `/full-calendar#classes`). /full-calendar returns a 301 to `http://sdbikecoalition.org/calendar` (plain http), then a second 301 to https. | Change the button links to `/calendar#calendar-view` and `/calendar#classes`. Then **Settings** › **Advanced** › **URL Mappings**: change the /full-calendar line to `/full-calendar -> /calendar 301` (relative, not `http://`). |
| FY 2025-26 budget campaign still current | /start-here | Text block `block-yui_3_17_2_1_1753228274436_6669`: "our FY 2025-26 Budget Campaign is Getting Kids to School Safely!" with the FY26 letter. | Update to the current campaign and letter [FILL IN: current budget campaign and letter link]. |
| "Reach out to us directly" with no contact | /hazard | Text block `block-2a0901750d8087a80e72`. No email, phone or link. | Link "reach out to us directly" to /contact, or add info@sdbikecoalition.org. |
| Corporate sponsor email link is empty | /corporate | Text block `block-yui_3_17_2_1_1755726887404_8525`: chloe@sdbikecoalition.org is a link with an empty `href`, so it goes nowhere. | Select the address, link icon, set it to `mailto:chloe@sdbikecoalition.org`. |
| Checkbox description reads "Description" | /bike-valet-registration | Form "Bike Valet Reg Form", checkbox "Get the latest bike news": description is the default "Description". | Form block › pencil › click the checkbox field › clear the Description box (or write a real line [FILL IN: what the newsletter covers]). The waiver checkbox text also has an em dash between "on time" and "our team": change it to a period. |
| After a Crash: only out-of-region resources, no Coalition contact | /traffic-violence | Resources are CityLab, MassBike, Grist, RoadPeace (UK), AllLaw, Wheels of Justice, NY Bicycle Coalition, US DOJ, Transportation Alternatives. No Coalition contact. The Facebook group (`block-031091ad012c7e83aedc`) isn't linked. | Add San Diego County resources [FILL IN: which local resources] and a Coalition contact line: info@sdbikecoalition.org, 619.786.5880. Link the Facebook group [FILL IN: group URL]. |

### Name and wording

| Issue | Where it's still live | Fix |
| --- | --- | --- |
| "San Diego County Bicycle Coalition" or "San Diego Bicycle Coalition" | /privacy-policy (2), /clubs (2), /hazard, /ambassador-program, /bike-valet-registration (heading "Hosted by San Diego County Bicycle Coalition"), /contact map pin ("San Diego Bicycle Coalition" in the Map block's address title), a calendar event excerpt (e-bike seminar), /blog (3, two inside quoted news text) | Edit each text block. For the map: Map block › pencil › **Location** › change the title. For the calendar and blog: edit the event or post itself. Leave text inside quotes from news articles as published. |
| "SDCBC" | /privacy-policy | Replace with "the Coalition". |
| "The Bike Coalition" / "the Bike Coalition" | /mission, /contact (2), /donate (3), /donors (2), /corporate (2), /repair, /rolling-forward, /bike-share, /clubs, /board-candidates, /blog (10), homepage membership band. /volunteer and /ambassador-program no longer use the phrase as a short name. | See "Style rules disagree" below before changing these. |
| Em dashes, en dashes, double hyphens | Homepage (10), /traffic-violence (11), /shop (9), /bike-share (7), /blog (7), /contact (5), /calendar (3), /hazard (3), /policy-statements (1), /bike-valet-registration (waiver text) | Replace with a comma, colon or new sentence. |
| Phone not written 619.786.5880 | Homepage footer: "(619) 786-5880 (texting only)" | Footer text block: "619.786.5880". The open questions still ask whether to keep "texting only". |
| Address with "#100" or no ZIP | /privacy-policy (`block-c2f4590df7a827ce850d`: "300 15th Street, #100"), /contact ("Our Office: 300 15th Street, San Diego") | Use "300 15th Street, San Diego, CA 92101" on both. |
| "available in at" | /contact FAQ (`block-yui_3_17_2_1_1739573402404_12013`) | "available at". |
| "Union Tribute" | /blog (post excerpt about Reuven's comment) | Edit the post: "Union-Tribune". |
| "to to" | /board-candidates candidate quote | Needs the candidate's OK (open questions list it). |
| "mechanics experience" | /repair | "mechanics' experience". |

### Content to review

| Issue | Live now | What's needed |
| --- | --- | --- |
| Unchecked statistics | Homepage: "6% of regional roadways where 54% of collisions occur". /teach: "30 LCIs". /policy-statements: "20x more space-efficient". /ciclosdias: "Since 2013", "30+ local organizations", "over one mile". | Check each against the approved stats, or remove it. |
| Annual reports missing years | /annual-reports lists 2010, 2013 to 2016, 2020, 2023 to 2025. Still missing 2011, 2012, 2017 to 2019, 2021, 2022. | Confirm whether those reports exist. |
| Fund descriptions only inside images | /donors: the four fund names are text, but "See each fund description below" points to images and a Dropbox PDF. All 8 images have empty alt text. | Put each fund description in a text block. |
| Donors overlaps Donate | Both pages still live with overlapping content. | Decision in the open questions. |
| Bike Share New York photo | /bike-share still uses `bike_city_blue_new_york_bicycle_urban_lifestyle_street-689581.jpg`. | Swap for a San Diego photo. |
| Helmet "Fitting" Guide has no fitting steps | /helmet-guide H1 is still "Helmet Fitting Guide"; the page covers choosing a helmet, not fitting one. | Add fitting steps, or rename to "Helmet Guide". |
| Privacy policy has no effective date | /privacy-policy says it will update "the effective date" but shows none. | Add [FILL IN: effective date]. |
| Blog's newest post is July 6, 2026 | Newest post: "We're Partnering with Bike Streets to Map San Diego's Low-Stress Bike Routes", July 6, 2026. | Post something new. |

### Accessibility and structure

| Issue | Live now | Fix |
| --- | --- | --- |
| Empty or file-name alt text | Still on almost every page. Worst: /shop (144 of 155 images), /blog (8), /donors (8 of 8), /safety-tips (6 of 6), /traffic-violence (6 of 6), homepage (5 of 15), /bike-share (5 of 5), /corporate, /hazard and /helmet-guide (4 of 4 each). /ciclosdias is the only page where every image has alt text. | Image block › pencil › **Alt text** (product images: in each product's settings). |
| Several H1s per page | /calendar 43, /blog 10, /e-bikes 4, /clubs 2, /bike-share 2, /helmet-guide 2, /ciclosdias-signup-form 2. Empty headings on /meetings (3), /bike-share and /ciclosdias-signup-form (1 each). | Keep one Heading 1 per page; set the rest to Heading 2 or 3. Delete empty headings. On /calendar the extra H1s come from event titles in the list. |
| Emoji in headings and copy | /contact, /ambassador-program (🌟), /traffic-violence (⚠️), /rolling-forward (4), /shop (8, including the page title "Shop: 🚲👕"), calendar events (4) | Remove the emoji. |
| Mail links ending in "?" | /meetings: advocacy-chair, education-chair, clubs-chair and chair addresses. /staff-board: quincie@. | Re-link each as `mailto:name@sdbikecoalition.org` with nothing after it. |
| http:// links | /contact: sdmba.com, 911law.com, bikesdelpueblosd.blogspot.com, sandag.org/bikemap. /repair: rebikesd.org. /hazard: Oceanside (old `ci.oceanside.ca.us` URL, returns 403) and Del Mar. /safety-tips: nhtsa.gov/Bicycles (returns 403). /calendar: bikingis.fun. | Change each to https. Replace the Oceanside and NHTSA links with current pages (403 may only mean they block automated checks, so open them by hand first). Map and "add to calendar" links on /calendar come from Squarespace and can't be edited. |

## Fixed

| Item | Checked |
| --- | --- |
| Footer copyright (was "Copyright The Bike Coalition 2026") | Live: "© 2026 San Diego County Bike Coalition. Site by Chloé Lauer and Jason Vance with support from Bit Palette." |
| Footer Tax ID breaking mid-number | Live with the non-breaking hyphen: "Tax ID 33‑0418006". |
| Shop desktop store heading hidden | At 1280 px the "Merch Store" heading shows (Custom CSS overrides Squarespace's `hidden-up-md`). Fixed as far as this check can tell. |

The newsletter block storage was also fixed and tested in October, according to the parent session. Its block is on /newsletter, but storage can't be confirmed from the public site.

## Cannot tell from the public site

| Item | Why |
| --- | --- |
| Ambassador form storage | Storage is only visible in the editor. See the test steps above. |
| White text on light gray (/corporate), teal heading on teal photo (/mission) | Both sections use photo backgrounds, so a computed contrast check can't measure them. A person needs to look at desktop and phone widths. |
| E-bike legal details | Needs someone to check against current California law. |
| Bylaws in two places | Both still live: the Google Doc embed on /bylaws and `/s/Board-Bylaws.pdf` on /staff-board. Whether they match needs a person reading both. |
| /full-calendar URL mapping | The redirect through http is visible, but the mapping itself is in **Settings** › **Advanced** › **URL Mappings**. |
| Calendar "show past events" setting | The setting is in the editor. The 30 past events are visible in the page HTML. |

## Style rules disagree

The organization's writing rules say "the Bike Coalition" after the first reference and allow "San Diego County Bicycle Coalition". This repo's `CLAUDE.md` says "the Coalition" and never "Bicycle Coalition". The baseline counts every "the Bike Coalition" as an issue. Someone needs to pick one rule before staff change the 30 or so "the Bike Coalition" references above, and `CLAUDE.md` or the organization rules should be updated to match.
