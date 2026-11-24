# Calendar page: Repair Clinic section before the two-card change (November 24, 2026)

Saved from the live `/calendar` page before the section was rebuilt to show both repair clinics. The full rendered section is in [calendar-repair-section-2026-11-24.html](calendar-repair-section-2026-11-24.html).

Section `69d048ae2b29ce400aff4e9a`, theme **White**, fluid engine, content width wide. Four native blocks:

| Block | Type | Desktop grid area | Phone grid area | Content |
| --- | --- | --- | --- | --- |
| `block-631a82f74f73de7c7a84` | Text | 1/2/3/26 | 1/2/4/10 | Heading 2, accent color, bold: "East Village Repair Clinic" |
| `block-7f4ee817a576e54167f9` | Text | 3/2/4/26 | 4/2/6/10 | Heading 4, accent, bold: "Most Sundays 10a - 2p, at " + link "our office" to `/contact` |
| `block-yui_3_17_2_1_1775257433394_8327` | Text | 4/2/9/26 | 6/2/18/10 | Two large paragraphs (below) |
| `block-yui_3_17_2_1_1775257433394_9570` | Button, medium, primary | 9/11/11/17 | 18/2/20/10 | "Reserve your spot!" to `/repair` |

Paragraph text, exactly:

> Need help getting your bike rolling? Our partners at ReBikeSD are here to help! They have the tools, expertise, and passion for keeping San Diego rolling.
>
> Whether you need help troubleshooting a repair, want to learn hands-on bike maintenance skills, or are looking for an affordable refurbished ride to take home, there's something for everyone. Space is limited so make a reservation to guarantee your spot!

To put it back: restore these four blocks with this text and these positions, and remove the repair-card rules from `src/pages/calendar-live.css` (or load the previous tag, v0.9.3).
