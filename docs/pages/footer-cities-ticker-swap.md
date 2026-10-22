# Swap: footer cities ticker to jsDelivr (v0.2.0)

Step 1 of [the jsDelivr plan](../jsdelivr-plan.md). The new block looks the same as the old one; the difference is that its styles come from this repo instead of being pasted in.

Verified before release: the old and new versions render identically (83 elements, same computed styles and sizes) at 1440 px and 390 px wide.

## What you paste

The whole contents of [src/blocks/footer/cities-ticker.html](../../src/blocks/footer/cities-ticker.html). It is the old block minus its `<style>` section, plus one line that loads `cities-ticker.css` from jsDelivr at tag `v0.2.0`, locked with an integrity hash.

## 1. Test on a hidden page

The footer is on every page, so try the new code somewhere private first.

1. Open the hidden **Calendar preview** page (or make any page under **Not Linked**).
2. Add a **Code** block anywhere on it and paste the new block contents.
3. Save, log out (or open a private window), and view the page.
4. Check: the green "18 cities. One county." band appears in the block, the city names scroll, hovering pauses them, and it looks the same as the footer below it.
5. Delete the test Code block.

## 2. Swap the live footer block

1. On any page, **Edit**, scroll to the footer, and click **Edit Footer**.
2. Click the cities band's Code block, then the pencil.
3. Select all the code in the block and delete it. (The old code is saved in the repo at the commit before v0.2.0, so nothing is lost.)
4. Paste the new block contents. Click **Apply**, then **Save**.
5. Log out or use a private window and check three pages: the homepage, a content page, and Classes. On Classes the band should still be hidden, as it is today.

## Undo

Paste the old block back. Get it with:

```bash
git show 5196c98:src/blocks/footer/cities-ticker.html
```

## Notes

- Editing tip: Squarespace disables scripts and some external styles while you're logged in. Always check logged out.
- Nothing else on the site changes in this step. Custom CSS, header code and every other block stay as they are.
