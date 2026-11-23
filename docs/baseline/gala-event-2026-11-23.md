# Golden Gear Gala event page: description before the custom section (November 23, 2026)

Saved before the custom section went in, so it can be put back. Page: /calendar/golden-gear-gala (Squarespace event "Golden Gear Gala", Tuesday, December 15, 2026, 6:00 to 9:00 PM, Négociant Winery). The event's title, date, time and location fields were not changed.

The description had five blocks, top to bottom:

1. **Text block** `block-a8b31f55eb14f7c9032b` (replaced by the custom section):

```html
<div class="sqs-html-content" data-sqsp-text-block-content><h1 style="white-space:pre-wrap;" data-rte-preserve-empty="true">You're Invited!</h1><p style="white-space:pre-wrap;" data-rte-preserve-empty="true">Join the San Diego County Bike Coalition for the second annual Golden Gear Gala, an evening celebrating the people and partners who make San Diego County a better place to ride.</p><p style="white-space:pre-wrap;" data-rte-preserve-empty="true">This year we're gathering at Négociant Winery in Hillcrest to honor the 2026 Golden Gear winners and toast a year of work for bike-friendly streets. Every ticket supports the Bike Coalition's advocacy, education, and community events across all 18 cities in the county.</p><p style="white-space:pre-wrap;" data-rte-preserve-empty="true">Tuesday, December 15, 6:00 to 9:00 PM, at Négociant Winery, 1263 University Ave, San Diego.</p><p style="white-space:pre-wrap;" data-rte-preserve-empty="true"><strong>What to expect: </strong>complimentary bike valet; professional photo booth; heavy hors d'oeuvres; drink ticket for a cocktail, beer, or wine (N/A options!); fun times!</p><p style="white-space:pre-wrap;" data-rte-preserve-empty="true"><strong>What to wear:</strong> bold jewel tones with rich textures (think velvet, tweed, or satin)</p></div>
```

2. **Image block** `block-yui_3_17_2_1_1795466695872_2776` (replaced): a four-photo collage, no alt text.
   https://images.squarespace-cdn.com/content/v1/673b90cbaf336204b2122a4a/8f5335e6-2ad2-4713-81de-03fac140d663/Untitled+Design.png
   The section's four photos (src/blocks/events/img/) are crops of this collage.

3. **Text block** `block-yui_3_17_2_1_1795466695872_2857` (kept, unchanged):

```html
<div class="sqs-html-content" data-sqsp-text-block-content><p style="white-space:pre-wrap;" data-rte-preserve-empty="true" id="yui_3_17_2_1_1795466695872_2848">Tickets are $100. Can't make it? Choose "I'll be there in spirit!" to support the night from wherever you are.</p></div>
```

4. **Video block** `block-yui_3_17_2_1_1795466695872_3903` (replaced): the gala reel uploaded to Squarespace (video id `6b04aac3047f2a112c931654`, 28.6 seconds, 9:16, controls on, no autoplay). The section plays the same reel from the repo (src/blocks/home/img/gala-reel.mp4), muted on a loop. The upload stays in the Squarespace asset library.

5. **Code block** `block-yui_3_17_2_1_1794686219276_1998` (kept, unchanged): the Givebutter ticket widget.

```html
<givebutter-widget id="LeZOKo"></givebutter-widget>
<script async src="https://js.givebutter.com/elements/latest.js?acct=Ehw36OIDvycv74YV&p=squarespace"></script>
```

To undo: delete the custom Code block at the top of the description, then add a Text block with block 1's text (an H1 and five paragraphs, the last two starting with a bold label), the image block with the collage, and a Video block with the reel, in that order above block 3.
