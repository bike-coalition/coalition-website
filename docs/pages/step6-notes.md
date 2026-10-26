# Step 6: Board Candidates and CicloSDias blocks to jsDelivr

Prepared October 26, 2026. **Not live.** Nothing in Squarespace has changed, and the `v0.7.0` tag the loader lines point to does not exist yet. Step 6 of [the jsDelivr plan](../jsdelivr-plan.md).

## What changed in the repo

| Page | Before | After |
| --- | --- | --- |
| Board Candidates | One 19.1 KB Code block with two style sections and a script | [candidates.html](../../src/blocks/board-candidates/candidates.html) (markup, inline guard, two loader lines), [candidates.css](../../src/blocks/board-candidates/candidates.css), [candidates.js](../../src/blocks/board-candidates/candidates.js), page header code [board-candidates-header-injection.html](../../src/pages/board-candidates-header-injection.html) loading [board-candidates.css](../../src/pages/board-candidates.css) |
| CicloSDias | One 21.9 KB Code block with a style section and inline styles | [ciclosdias.html](../../src/blocks/ciclosdias/ciclosdias.html) (markup with its inline styles, inline guard, one loader line), [ciclosdias.css](../../src/blocks/ciclosdias/ciclosdias.css), page header code [ciclosdias-header-injection.html](../../src/pages/ciclosdias-header-injection.html) loading [ciclosdias.css](../../src/pages/ciclosdias.css) |

- **Checked against live first.** On October 26 both live blocks, fetched with curl, matched the repo copies byte for byte, so the split starts from what is on the site.
- **Class names:** `bc26` and its `bc-` children became `bc-board` and `bc-board__…`, with `is-ready`, `is-active`, `is-dark`, `is-green` and `is-outline` for states. `cs-page`, `btn` and `tile` became `bc-ciclo`, `bc-ciclo__btn` and `bc-ciclo__tile`. Every Board Candidates selector stays scoped under `.bc-board`, so each rule keeps the specificity it had (a flat `.bc-board__eyebrow` would have lost to `.bc-board p` and dropped its spacing).
- **Brand colors** in the Board Candidates stylesheet now read from `src/tokens.css`, with the same hex as fallback. CicloSDias uses its own event palette, which has no brand tokens, so its colors stay as they were (see the content problems below).
- **Page-wide rules** (sideways clip on both pages, smooth scrolling on CicloSDias) moved to `src/pages/`, loaded from each page's own header code. Neither page has any header code today.
- **Inline guards** are generated with `tools/make-guard.py`.
- **Board Candidates photos** moved from a list inside the script to a `data-photo` link on each candidate in the markup, so a photo can change without a new release.
- **Board Candidates script has no `defer`,** unlike step 4. The pasted script ran the moment the block was read. A deferred script could let the page draw all five candidates stacked and then jump to one. Loading it the same way as before avoids that.
- **Board Candidates stylesheet tidy-up:** dropped one unused selector (`.bc-hd`) and the exact repeats of the dark-card color rules inside the phone-width section. A rule-by-rule comparison after renaming shows every other declaration is unchanged (282 match).
- **CicloSDias buttons:** the five buttons used the class `btn`, which Squarespace's own stylesheet also styles: position relative, a 0.1 second opacity transition, and a fade to 80% on hover on screens with a mouse. That transition also overrode the block's own lift animation, so on the live page the lift jumps instead of gliding. The new stylesheet writes that exact behavior out, so nothing changes. The other 55 declarations match one for one.

## Test results

Local copies of each live page (fetched October 26), with every script removed except the block's own, served with `python3 -I -m http.server` and loaded side by side in cache-busted iframes in the built-in browser. "After" loads the new files with their real `sha384` hashes, so the hashes were checked too. Animations (the footer cities ticker) were paused at the same frame before each comparison.

**Computed styles, every element and its `::before`, `::after` and `::marker`, plus each element's position and size:**

| Page | Width | Elements | Pseudo-elements | Differences |
| --- | --- | --- | --- | --- |
| Board Candidates, at rest | 1440 | 1,008 | 1,120 | none |
| Board Candidates, after picking candidate 3, Next, then Previous twice | 1440 | 1,008 | 1,120 | none at each step |
| Board Candidates, at rest | 390 | 1,008 | 1,100 | none |
| Board Candidates, same clicks | 390 | 1,008 | 1,100 | none at each step |
| CicloSDias | 1440 | 947 | 1,044 | none |
| CicloSDias | 390 | 947 | 1,024 | none |

A deliberate 1 px change was caught by the same check, so it does detect differences. The candidate picker gives the same button labels, `aria-pressed` states and active candidate before and after. Hovering a CicloSDias button with the mouse gives the same result before and after: 2 px lift, 80% opacity, same transition.

**The editor case:** no block stylesheet, no page stylesheet, no scripts, only the inline guard, against the old block with its own styles and no script. Heights in px:

| Page | Width | Block before | Block after | Section before / after | Page before / after |
| --- | --- | --- | --- | --- | --- |
| Board Candidates | 1440 | 4,503.3 | 4,503.3 | 4,632.1 / 4,632.1 | 5,667 / 5,667 |
| Board Candidates | 1024 | 4,421.1 | 4,421.1 | 4,541.6 / 4,541.6 | 5,338 / 5,338 |
| Board Candidates | 390 | 7,933.4 | 7,933.4 | 8,021.4 / 8,021.4 | 9,395 / 9,395 |
| CicloSDias | 1440 | 7,876.8 | 7,876.8 | 7,876.8 / 7,876.8 | 8,912 / 8,912 |
| CicloSDias | 1024 | 8,199.7 | 8,199.7 | 8,199.7 / 8,199.7 | 8,996 / 8,996 |
| CicloSDias | 390 | 10,367.6 | 10,367.6 | 10,367.6 / 10,367.6 | 11,741 / 11,741 |

Visible content (all text, links, image sources and alt text, aria labels) is identical in both blocks.

**Not covered locally:** Squarespace's own scripts were removed from both copies, so these numbers are not the live page heights. Keyboard focus rings were not compared (the focus rules were renamed one for one). Whether the Squarespace editor loads page header code was not checked; the guard does not depend on it.

**No differences were left unexplained.** The only two found (Squarespace's `btn` styling, and the cities ticker animation running at a different frame in each copy) are explained above, and both now compare clean.

## Content problems noticed (not changed)

Board Candidates (`/board-candidates`):

- Seasonal: built for the November 2026 board election (2027 to 2028 term). Once the vote closes it needs results, or to come down.
- No voting dates anywhere. The steps say "Voting happens in November", and the markup has a note asking for the dates.
- Stephan Vance's quote reads "want everyone who wants to to be able to". The candidates still need to approve quote edits ([future-pages-open-questions.md](../future-pages-open-questions.md)).
- The "Next" button reads "Next:" followed by two spaces before the name.
- The hero is ultramarine with spring green, not the spring green and teal hero pair, and body text is `#12302a`, which is not a brand color.
- Loads Archivo Black and Inter from Google Fonts; headings ask for Obviously first.
- The button lift on hover has no reduced-motion opt-out.

CicloSDias (`/ciclosdias`):

- Still promotes Sunday, October 18, 2026 as upcoming: the hero pill, the street band, the "10 to 3" stat and "Drop in anywhere along the route between 10 am and 3 pm".
- Colors outside the brand palette: orange `#FFA02F`, blues `#005BBB`, `#00346E`, `#0B2447`, `#001F45`, cream `#FFF8EC`.
- Gradient overlays on the hero and street photos. The brand rules say no gradients.
- Montserrat and Open Sans instead of Obviously and Inter.
- Numbers not in the approved statistics: "over one mile", "30+ local organizations", "Since 2013", "approximately 6.7-mile bikeway".
- A quote attributed to Chloé Lauer, Executive Director: confirm the title and that it is approved for reuse.
- Smooth scrolling and hover motion have no reduced-motion opt-out.
- The block carries its own `<footer>` element above the site footer.
- Both pages use "the Coalition" as the short name; see the open questions.

## Go-live steps

Do CicloSDias first (no script), then Board Candidates. One page at a time.

### 1. Release

1. Merge branch `claude/step6-seasonal-blocks-f166f3` into `main` and push.
2. `git tag -a v0.7.0 -m "Step 6: Board Candidates and CicloSDias from jsDelivr"` and `git push origin v0.7.0`. If `v0.7.0` is already taken, use the next free number and change `@v0.7.0` in the two block files and two header files. The hashes stay the same as long as the files do.
3. Check jsDelivr serves each file with the hash in the repo:

```bash
for f in src/blocks/board-candidates/candidates.css src/blocks/board-candidates/candidates.js src/blocks/ciclosdias/ciclosdias.css src/pages/board-candidates.css src/pages/ciclosdias.css; do echo "$f sha384-$(curl -sS https://cdn.jsdelivr.net/gh/bike-coalition/coalition-website@v0.7.0/$f | openssl dgst -sha384 -binary | openssl base64 -A)"; done
```

Each line must match the `integrity` value in the matching `.html` file.

### 2. Test on a hidden copy

1. In Squarespace, duplicate the page (Pages, the page's gear menu, Duplicate). Move the copy under Not Linked.
2. On the copy: Page settings, Advanced, Page Header Code Injection. Paste the page's header file (`src/pages/ciclosdias-header-injection.html` or `src/pages/board-candidates-header-injection.html`). Save.
3. Edit the copy's Code block: select all, delete, paste the whole new block file. Apply. In the editor the block should keep its normal size. Save.
4. Log out or use a private window. Compare the copy with the live page at desktop and phone width: same look, same section height, same page length.
   - CicloSDias: "Get involved" jumps smoothly to "Be part of the day"; buttons lift and fade on hover.
   - Board Candidates: the five name buttons switch candidates, Previous and Next work, photos appear, "Register to vote" opens the Google Form.
5. Delete the copy.

### 3. Swap the live page

1. Page settings, Advanced, Page Header Code Injection: paste the header file. Save. (Header first: until the block is swapped, the clip rule is simply there twice.)
2. Edit the Code block, select all, delete, paste the new block file, Apply, Save.
3. Logged out, at desktop and phone width: check the block's grid rows and the section's height on the published page, not in the editor (step 1 lesson), then the same checks as on the copy.
4. Record it: mark step 6 live in [jsdelivr-plan.md](../jsdelivr-plan.md), [code-map.md](../code-map.md) and [registry.json](../../src/blocks/registry.json).

### Undo

Paste the old block back and clear the page header code. The old blocks:

```bash
git show 5cc3ab6:src/blocks/ciclosdias/ciclosdias.html
```

```bash
git show 5cc3ab6:src/blocks/board-candidates/candidates.html
```

## Open questions

1. **Release Board Candidates at all?** The election is next month and the page will need results or to come down soon after. Moving it now is low risk but may be work for a page with weeks left. The plan says to do seasonal pages "when they're next updated".
2. **CicloSDias timing:** release now, or with the content update for the next event (new date, recap, palette)?
3. **Tag number:** is `v0.7.0` free, or is another release planned under it?
4. **Board Candidates script without `defer`:** OK to differ from the step 4 pattern for this reason?
5. **CicloSDias button motion:** keep Squarespace's fade with the jumpy lift, or let the lift animate as the block intended? That would be a small visible change, so it is left for later.
6. **Short name:** `CLAUDE.md` says "the Coalition" after first reference and never "Bicycle Coalition". The organization's style instructions say "the Bike Coalition" after first reference, and allow "Bicycle" on first reference. Which one is right? Both pages use "the Coalition" today.
