# Runbook: getting a change onto the live site

Plain-English steps for anyone at the Coalition. You don't need to write code to follow them.

## The short version

Commit the change → make a release tag → test it on the hidden preview page → update the tag in Squarespace.

## 1. Make the change

Claude commits the change to `main` on GitHub and shares a screenshot. Nothing on the live site changes yet. (Only two people edit this repo right now, so there are no pull requests. Add them back when more people join.)

## 2. Look it over

Check the screenshot and the commit on GitHub. Ask for changes before anything gets tagged.

## 3. Make a release tag

A release tag is a frozen snapshot, like `v0.2.0`. Claude can make one when asked. Once it exists, jsDelivr serves that snapshot at:

```
https://cdn.jsdelivr.net/gh/bike-coalition/coalition-website@v0.2.0/
```

## 4. Test on the hidden preview page

The preview page in Squarespace loads the new tag. Check it on a phone and a laptop. Make sure donate, newsletter sign-up, the calendar and any other embeds still work.

## 5. Go live

In Squarespace: **Settings › Developer tools › Code Injection › Header**. Change the old tag to the new one in the loader line, then save. The whole site now uses the new version.

## Undo

Put the previous tag back in Code Injection and save. The site goes back to how it was within a few minutes.

## Not set up yet

- The hidden preview page
- The loader in Code Injection (pinned tag, integrity hash, preconnect)
- Automatic checks for links, speed and accessibility
