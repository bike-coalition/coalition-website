# Homepage baseline, October 2026

A record of the live homepage before any custom code goes in. Captured with Claude in Chrome, logged out and read-only: nothing was edited, submitted, or added to the cart. Only the homepage has been captured so far. The other 34 pages are not done.

Screenshots are kept outside this repo.

## Capture conditions

- Desktop viewport: 1186 px wide. The browser window would not resize to 1440 px.
- Phone viewport: 410 px wide, not 390. The layout is the phone layout (hamburger menu, stacked sections).
- No popups, cookie banners, errors or broken layouts seen.

## Styles as measured

Measured with `getComputedStyle` at 1186 px. Footer values were not reliable; re-measure before using them.

| Element | Font | Size / line height | Weight | Color |
| --- | --- | --- | --- | --- |
| Header links | Poppins | 16 px | 400 | Teal Green on hover |
| Hero H1, "Bike for a Better San Diego" | Obviously-style display | 41.6 / 50.2 px | 500 | #EBEBEB over the photo |
| Section H2 | Display face | 33.1 / 40.9 px | 500 | #226550 |
| Section H3 | Display face | 27.4 / 34.5 px | 500 | not measured |
| Body paragraph | Inter | 23.1 / 32.4 px | 400 | #161614 |

- **Page background:** #C7EC7A at the top. Sections alternate Teal Green (#226550 family), navy (membership band) and light gray (testimonials).
- **Header:** white background.
- **Header Donate button:** pill (300 px radius), #226550 with white text. Hover: #C7EC7A with Teal Green text. About 16 px by 20.8 px padding.
- **Primary buttons** (Class, Event and Volunteer Schedule): Spring Green pills with dark text on the green section.
- **Membership buttons:** white pills on navy.
- **Footer links:** #C7EC7A.
- **Content width:** no max width. Content spans the viewport with about 48 px side margins.

## What's on the homepage

- Hero with a looping photo or video, and a "Learn more" link.
- Five header menus: About Us, Classes + Events, Advocacy, Resources, Get Involved. Donate button and cart in the header.
- Social links: Instagram, Facebook, YouTube, Discord, Strava.
- Squarespace Shop product carousel, 10 products.
- Testimonials carousel, 8 slides.
- Footer badges: Candid Platinum Transparency 2026, Live Well San Diego Recognized Partner, 1% for the Planet.
- Footer search field.
- No Givebutter, Point or Action Network embeds on the homepage.
- Several sections animate in on scroll.

## Phone

- Hamburger menu on the right, cart "(0)" to its left.
- Mobile menu: the five top-level items, social icons, Donate at the bottom. Submenus slide in with a Back link.
- Hero headline wraps to three lines over the photo.

## Issues found

| Issue | Status |
| --- | --- |
| Footer copyright reads "Copyright The Bike Coalition 2026" instead of the full name | On the fix-first list |
| Footer Tax ID breaks mid-number ("33-" / "0418006"), desktop and phone | On the fix-first list |
| Hero "Learn more" link has low contrast over a busy photo | Later |
| "Honk If You'd Rather Be Biking - Bumper Sticker" uses a hyphen as a dash | Later |
| PRIDE tote product name uses emoji flags, which can render unevenly | Later |
| Empty cart shows "(0)" in the header | Later |

## Still to capture

- Homepage phone at exactly 390 px, if that 20 px difference matters.
- Full-size originals of the homepage photos (not downloaded).
- Every page other than the homepage, including /donate.
