# Working in this repo

Custom code for sdbikecoalition.org, a Squarespace 7.1 site. Read `README.md` and `docs/runbook.md` first.

## Ground rules

- Never change the live site directly. Commit to `main` (no pull requests for now: only two people edit this repo), then a release tag and a hidden preview page before anyone updates the tag in Squarespace Code Injection.
- The current homepage and menus stay as they are for now. Don't build a new homepage or reorganize the nav unless asked.
- Scheduled or automated runs open pull requests only. They never merge, tag, or publish.
- Roll out one page at a time. Save a page's old content before replacing it.
- Pages listed as `native` in `manifest.json` stay native Squarespace. Don't rebuild them in code.
- This repo is public. Never commit passwords, API keys, donor or member data, or anything from a private document.

## Writing on the site

- "San Diego County Bike Coalition" on first reference, "the Coalition" after. Never "SDBC", "SDCBC", "SD Bike Coalition" or "Bicycle Coalition".
- No em dashes or double hyphens. Use a comma, colon, or new sentence.
- "Crash" or "collision", never "accident". "Traffic violence" for systemic patterns.
- Use only approved statistics. Never invent a number. Leave `[FILL IN: ...]` placeholders and flag them in the PR.
- Voice: warm, direct, advocacy-forward. We take positions.
- Contact details, exactly: 300 15th Street, San Diego, CA 92101 | 619.786.5880 | info@sdbikecoalition.org | sdbikecoalition.org

## Design

- Use the variables in `src/tokens.css`. Don't hard-code colors.
- Headlines: Obviously (licensed, not in this repo; Archivo is the fallback). Body: Inter, 16 to 18px.
- Spring Green and Teal Green are the hero pair. No gradients. Don't mix the primary and secondary color sets.
- Accessible as built: real buttons and links, 4.5:1 text contrast, 44px touch targets, respect `prefers-reduced-motion`.
- Every page works at phone width.

## Embeds that must keep working

Givebutter (donate), Action Network (campaigns), BikeReg (Bike the Bay), Point (volunteer), and the Squarespace newsletter and calendar blocks.
