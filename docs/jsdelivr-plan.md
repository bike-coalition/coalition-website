# Moving custom code to jsDelivr

Today every piece of custom code is pasted straight into Squarespace (see [code-map.md](code-map.md)). The goal: Squarespace holds only small "loader" lines and page markup, and the CSS and JavaScript come from this repo through jsDelivr at a pinned release tag. One edit here, one tag, every page updates; one tag back, every page rolls back.

jsDelivr needs no account or setup. It already serves this public repo at any tag, for example `https://cdn.jsdelivr.net/gh/bike-coalition/coalition-website@v0.1.0/src/tokens.css`.

## Target shape

```
src/
  tokens.css              brand variables (already served)
  site/custom.css         site-wide CSS, replaces Design › Custom CSS
  site/site.js            site-wide behavior, if any is needed later
  blocks/<page>/<name>.css   one stylesheet per block
  blocks/<page>/<name>.js    one script per block, when it has one
  blocks/<page>/<name>.html  the markup left in the Squarespace Code block
```

Each Code block shrinks to its markup plus one line:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/bike-coalition/coalition-website@vX.Y.Z/src/blocks/home/testimonials.css" integrity="sha384-..." crossorigin="anonymous">
```

A block with behavior also gets one `<script src="..." integrity="..." crossorigin="anonymous" defer>` line, so the script loads only on pages that have the block and releasing it never touches Code Injection. Each script only acts on its own blocks.

## The site-wide loader

Goes in Pages › Code Injection (search "code injection" in the dashboard) › Header, replacing nothing yet:

```html
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/bike-coalition/coalition-website@vX.Y.Z/src/tokens.css" integrity="sha384-..." crossorigin="anonymous">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/bike-coalition/coalition-website@vX.Y.Z/src/site/custom.css" integrity="sha384-..." crossorigin="anonymous">
```

The existing Givebutter line stays.

## Order of work, lowest risk first

Each step: split the block's CSS and JS out of its HTML, tag a release, test it on a hidden copy of the page, then swap the live block. Keep the old pasted code in the repo history so any step can be undone by pasting it back.

1. **Footer: cities ticker.** On every page, small, CSS only. **Done, live October 21, 2026, v0.2.0.** CSS split out, classes renamed, verified identical at 1440 and 390 px before release and on the live site after. Swap steps: [pages/footer-cities-ticker-swap.md](pages/footer-cities-ticker-swap.md).
2. **Footer: Candid seal.** Fix the screen-reader label ("San Diego County Bike Coalition") and add the image's alt text. **Done, live October 22, 2026.** No CSS to move, so no tag needed. Checked live at 1440 and 390 px: seal 108 px, block grid area and footer rows unchanged.
3. **Site Custom CSS.** Move Design › Custom CSS into `src/site/custom.css`, loaded by the loader. Then empty Custom CSS in Squarespace. Test every page template: home, a content page, the blog, an event, a product. **Done, live October 23, 2026, v0.3.0.** Computed styles matched on 9 page types at 1440 and 390 px before release, on the Code Preview page, and on the live site after Squarespace's copy was emptied. The accordion title size is pinned to the 1.4rem Squarespace actually served (its LESS compiler had broken the clamp). Rollback: paste [baseline/squarespace-custom-css-v53.less](baseline/squarespace-custom-css-v53.less) back into Custom CSS.
4. **Homepage testimonials.** First block with JavaScript. **Done, live October 23, 2026, v0.4.0.** CSS and JS split out, classes renamed to `bc-quotes__`, brand colors from tokens.css. Verified identical locally (at rest, after Next, after a dot, keyboard, wrap-around) and on the live homepage at 1440, 1024 and 390 px: same grid area, block height and page height as before.
5. **Classes, both blocks.** Move the two base64 photos out of the HTML (about 300 KB of the page) to Squarespace image uploads or the repo. **Done, live October 25, 2026, v0.5.0.** Photos moved to `src/blocks/classes/img/` (byte-identical, now lazy-loaded); the page HTML dropped from 705 KB to 300 KB. CSS and JS split out; page-wide rules (sideways clip, hidden cities band) moved to `src/pages/classes.css`, loaded from the Classes page header code. Inline guards generated with `tools/make-guard.py`. Verified identical locally and live at 1440, 1024 and 390 px: every block, section and page height matches the pre-change baseline.
6. **Board Candidates, CicloSDias.** Seasonal pages; do these when they're next updated. **Prepared October 26, 2026, not live.** Both blocks split into markup, CSS (and JS for Board Candidates) with loader lines for `v0.7.0`; classes renamed to `bc-board__` and `bc-ciclo`; page-wide rules moved to `src/pages/board-candidates.css` and `src/pages/ciclosdias.css`, each loaded from that page's header code. Verified identical locally at 1440 and 390 px, and the same block height before the CSS loads at 1440, 1024 and 390. Test results, content problems and the go-live steps: [pages/step6-notes.md](pages/step6-notes.md).
7. **Event ticket widgets.** Drop the duplicate Givebutter script from each block; the site-wide one already loads it. Test one event first. **Done, live October 26, 2026.** A scan of all 153 event pages found 75 with a Givebutter form; 70 already relied on the site-wide script alone. The five La Mesa City Cycling pages (January 23, March 13, May 22, June 12, August 7, 2027) also loaded `js.givebutter.com/elements/latest.js`; their blocks now hold only `<givebutter-widget id="...">`. Each form was checked live afterwards: same size, right class and date, no errors. No page loads the duplicate any more. Note: the squarespace-manager skill's from-scratch event steps still say to type the script line; update it so new pages match.

## Cleanups to make along the way

- **Class names:** the live code uses `sdbc-` prefixes (`sdbc-cities`, `sdbcQuotes`, `sdbc-slide`). Rename to `bc-` as each block moves, in the CSS, the JS and the markup together.
- **Fonts:** three blocks load their own Google Fonts (Archivo, Archivo Black, Inter, Montserrat, Open Sans). The site already loads Obviously from Adobe Fonts. Settle on Obviously plus Inter and load them once.
- **Page-wide side effects:** ~~the Classes block hides the footer cities band and sets `overflow-x: clip` on the whole page~~ Done in step 5: both rules are now in `src/pages/classes.css`. The footer ticker still carries the old `sdbc-cities` class; nothing uses it any more, so it can be dropped next time the footer is edited.
- **CicloSDias:** off-palette colors and a past event date. Listed with the other content problems in [pages/step6-notes.md](pages/step6-notes.md); the step 6 split kept them as they are.

## Release checklist (every tag)

1. Commit the change to `main`.
2. `git tag -a vX.Y.Z -m "what changed"` and push the tag.
3. Compute each changed file's hash: `openssl dgst -sha384 -binary FILE | openssl base64 -A`.
4. Confirm jsDelivr serves the tag and the hash matches.
5. Update the version and `integrity` values on the hidden preview page; check it.
6. Then update them on the live page or in Code Injection.

To roll back, put the previous version and hashes back. jsDelivr keeps every tag.

## Lessons from step 1: the footer that grew to 3,300 px

On October 21, swapping the ticker block made the whole footer about 3,300 px tall on every page. Fixed October 22; the footer is back to 1,062 px on desktop.

- **Why:** when code is pasted into a Code block, the Squarespace editor measures it right away, before an external stylesheet has loaded. The unstyled content (a 36-item list) was tall, so the editor grew the block from 8 grid rows to 88, and the section to 89, and saved that.
- **Prevention, every block that moves:** keep a one-line inline `<style>` in the block with just enough layout (flex, no wrapping, a max height) that the unstyled content is already about the right size. See the first lines of `src/blocks/footer/cities-ticker.html`.
- **Squarespace trap:** the editor redraws a section to fit its content while editing, so a section that saved too tall can look correct in the editor, and Save stays gray with nothing to save. The fix was to nudge the section so Save turned black, then save. Afterwards, check the published row count, not the editor.
- **After every swap, check on the live site, logged out:** the block's grid size and its section's height at desktop and phone width, not just how the block itself looks.
