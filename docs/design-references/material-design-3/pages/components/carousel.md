# Carousel

Source: https://m3.material.io/components/carousel
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/b0726223-2639-4157-84ae-cb84c07ee2e5.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Contain visual items like images or video, along with optional label text</p></li><li><p>Six layouts: <app-froala-tooltip-element description="The multi-browse carousel layout shows at least one large, medium, and small carousel item at a time." link-label link-url should-open-link-in-new-tab="false">Multi-browse</app-froala-tooltip-element>, <app-froala-tooltip-element description="The uncontained carousel layout show items that scroll to the edge of the container." link-label link-url should-open-link-in-new-tab="false">uncontained</app-froala-tooltip-element>, <app-froala-tooltip-element description="The uncontained multi-aspect ratio layout shows carousel items of various widths." link-label link-url should-open-link-in-new-tab="true">uncontained multi-aspect ratio</app-froala-tooltip-element>, <app-froala-tooltip-element description="The hero carousel layout shows at least one large and one small item at a time." link-label link-url should-open-link-in-new-tab="false">hero</app-froala-tooltip-element>, <app-froala-tooltip-element description="The center-aligned hero carousel layout shows at least one large and two small items at a time. The large item is centered." link-label link-url should-open-link-in-new-tab="false">center-aligned hero</app-froala-tooltip-element> and <app-froala-tooltip-element description="The full-screen carousel layout shows one edge-to-edge large item at a time and scrolls vertically." link-label link-url should-open-link-in-new-tab="false">full-screen</app-froala-tooltip-element></p></li><li><p>Layouts can be start-aligned or center-aligned</p></li><li><p>Item visuals have a parallax effect when scrolled</p></li><li><p>Items change size as they move through the carousel</p></li></ul>

A carousel being scrolled horizontally. Each carousel item changes shape as it scrolls.

<p>Carousels can show items of various sizes</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuthdnj-GM3-Components-Carousel-Overview-1-v01.mp4?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/3fb6515e512e5c09

libraryModuleType: STATUS_TABLE

<h2>Updates</h2>

<p><strong>November 2025</strong></p><p>New carousel layout:</p><ul><li><p><app-froala-tooltip-element description="The uncontained multi-aspect ratio layout shows carousel items of various widths." link-label link-url should-open-link-in-new-tab="true">Uncontained multi-aspect ratio</app-froala-tooltip-element></p></li></ul><p><strong>2023 </strong></p><p>Additional layouts and configurations:</p><ul><li><p><app-froala-tooltip-element description="The uncontained carousel layout show items that scroll to the edge of the container." link-label link-url should-open-link-in-new-tab="false">Uncontained</app-froala-tooltip-element></p></li><li><p><app-froala-tooltip-element description="The full-screen carousel layout shows one edge-to-edge large item at a time and scrolls vertically." link-label link-url should-open-link-in-new-tab="false">Full-screen</app-froala-tooltip-element></p></li><li><p><app-froala-tooltip-element description="The center-aligned hero carousel layout shows at least one large and two small items at a time. The large item is centered." link-label link-url should-open-link-in-new-tab="false">Centered carousels</app-froala-tooltip-element></p></li><li><p><app-froala-tooltip-element description="The hero carousel layout shows at least one large and one small item at a time." link-label link-url should-open-link-in-new-tab="false">Hero carousel layout</app-froala-tooltip-element></p></li><li><p><app-froala-tooltip-element description="The multi-browse carousel layout shows at least one large, medium, and small carousel item at a time." link-label link-url should-open-link-in-new-tab="false">Multi-browse layout</app-froala-tooltip-element></p></li></ul>

Items of different widths in an uncontained multi-aspect ratio layout.

<p>New carousel layout: uncontained multi-aspect ratio</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmljue787-02.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/fVj4DyPx6HxKN7gxkVrxReCeNppE22Favi2407XaDtWc5AiUxr-xvwqelWFXfRaQ2AayTCiBEwL06duEvTEptd1dEt1FWREyAV1d_2kMAf-MHQ=s1352

<h2 id="isPasted">Differences from M2</h2>

<p><span style="white-space:pre-wrap" id="isPasted">This component is new in Material 3.</span></p><ul><li id="isPasted"><span style="white-space:pre-wrap" id="isPasted"><strong>Shape</strong>: Dynamic carousel items change shape when scrolled</span></li><li id="isPasted"><span style="white-space:pre-wrap" id="isPasted"><strong>Motion</strong>: Carousel items move at a different speed than their content, creating a parallax effect</span></li><li id="isPasted"><span style="white-space:pre-wrap" id="isPasted"><strong>Interaction</strong>: When scrolled, carousel items snap into place to maintain the same layout. </span><app-froala-tooltip-element description="The hero carousel layout shows at least one large and one small item at a time." link-label link-url should-open-link-in-new-tab="false">Hero carousels</app-froala-tooltip-element><span style="white-space:pre-wrap" id="isPasted"> swipe through one item at a time. </span><app-froala-tooltip-element description="The multi-browse carousel layout shows at least one large, medium, and small carousel item at a time." link-label link-url should-open-link-in-new-tab="false">Multi-browse carousels</app-froala-tooltip-element><span style="white-space:pre-wrap" id="isPasted"> scroll through many items at once.</span></li></ul>

Carousel in a contained layout with a large item and a small item.

<p>Hero carousels scroll through one large item at a time</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwur4ddz-3.png?alt=media

<h2>Research</h2>

<p>The Material Research Team conducted two studies (quantitative and qualitative) with over 200 participants to understand their perspectives of five different carousel designs. The studies measured their understanding of how to interact with each carousel, their expectations of the number of items in each design, and how they expected carousels to be used.</p><p><strong>Summary of findings:</strong></p><ul><li><p>Participants thought carousels were a good way to explore many different kinds of content</p></li><li><p>A previewed or squished item strongly indicated that there was more content to swipe through</p></li><li><p>Participants expected around 10 items in a carousel that scrolled multiple items at once</p></li><li><p>While some contexts were considered better for some carousel designs, all designs were considered similarly usable</p></li></ul>

## Specs

4 elements of a carousel.

<ol><li id="isPasted">Container</li><li>Large carousel item</li><li>Medium carousel item</li><li>Small carousel item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyr7cydt-1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Bfe7F5i-YHBu3MctH6XdfsSYD1VNZVWrAC2hTpG-vOuHgn1-npiiivwifJe1ddHkbRZxlXtKJuq0GV9ScQUHvelSAEkjsMkWnAUznOdSjSPG=s2048

<h2>Tokens &amp; specs</h2>

<p>Browse the component elements, attributes, tokens, and their values.</p>

resourceName: designSystems/20543ce18892f7d9/components/43a124d2adc8a2ef

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2 id="isPasted">Color</h2><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview/" id="isPasted" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

2 color roles of a carousel.

<p>Carousel color roles used for light and dark schemes:</p><ol><li>Container</li><li>Surface</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyr7dtgs-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Mzrpy7os0Evw3KGIkxaFfkon8IgFJgpyqGgYD2DIMMbywuPHponDXt8yaG9F6u0lJAhluoYHtJE1Sv2KYym2NJiXYSBSqOT6pMFsQMCdXZF77w=s2048

<h2>States</h2><p><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element> are visual representations used to communicate the status of a component or interactive element. <a id="isPasted" href="/m3/pages/interaction-states/overview" target="_blank" rel="noopener noreferrer">Learn more about interaction states</a></p>

5 states of a carousel in light and dark schemes.

<ol><li>Enabled</li><li>Hovered</li><li>Focused</li><li>Pressed</li><li>Disabled</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8tafq6c-3.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/D7QutV1hQsVv50Nbn-UkT_BAJ4JRYAHLcohN50l4y2t5BDjn0pSq5jHk29phmxHU4H-UZszf7UaQoCPDkjWvVki1t4vlhxzzHfBL9vabMqo=s2048

<h2>Carousel item dynamic widths</h2>

<p>All kinds of carousel items dynamically adapt to the width of the container.</p><p>Large items have a customizable maximum width that's used to optimally fit carousel items into the available space.</p><p>Small carousel items have a minimum width of 40dp and a maximum width of 56dp.</p><p>Items change size as they move through the carousel layout.</p>

Measurements for a small carousel item.

<p>Small carousel items have a minimum and maximum width</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi9mff4k-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/l_O_4sY-OWT2K7Ot5jY_yhXxSErGV6Cu33URxwXPnt8D6oTDXh3oWlg5utAL2Iw0afdYNvkjpYZzLlsXjeONHtFJIqbO4dCEZO2xTzUvChjV=s1352

<h2><span style="white-space:pre-wrap" id="isPasted">Multi-browse</span></h2><p>The <app-froala-tooltip-element description="The multi-browse carousel layout shows at least one large, medium, and small carousel item at a time." link-label link-url should-open-link-in-new-tab="false">multi-browse layout</app-froala-tooltip-element> shows at least one large, medium, and small carousel item.</p>

4 elements of a multi-browse carousel layout.

<ol><li id="isPasted">Container</li><li>Large carousel item</li><li>Medium carousel item</li><li>Small carousel item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyr7hu8z-5.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/evx3sPQvpKArdG4MTkQQCOFPM387eGsABK9x_Ecv_LeJy23RGxJyVZU50_GThcTacMUgP5tuLoPOXRwk3s0QZgpKmJpiEj8pG_kZaAgertAC=s2048

<h3>Measurements</h3>

Measurements of a multi-browse carousel layout.

<p>Multi-browse carousels have padding on both sides of the container</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi9meptr-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Py7GKPNbLAGSs7Zx0w19v21_MWZgZSX5ztGYvSQ8bDM4DeZ-ilsU5Ra3bR2_24qAgkiEn8j7dTfdKO7YGmz8Jfd-cFR80M3rtWzzDt3nwUHtaQ=s2048

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="text-align:center">Attribute</th><th style="text-align:center">Value</th></tr></thead><tbody><tr><th style="width:50%;text-align:center">Alignment</th><td>Vertically centered</td></tr><tr><th style="width:50%;text-align:center">Leading/trailing padding</th><td>16dp</td></tr><tr><th style="width:50%;text-align:center">Top/bottom padding<br /></th><td>8dp</td></tr><tr><th style="width:50%;text-align:center">Padding between elements<br /></th><td>8dp</td></tr><tr><th style="width:50%;text-align:center">Large item width</th><td><span style="white-space:pre-wrap" id="isPasted">Dynamic, or user-set</span></td></tr><tr><th style="width:50%;text-align:center">Medium item width</th><td><span style="white-space:pre-wrap" id="isPasted">Dynamic</span></td></tr><tr><th style="width:50%;text-align:center">Small item width</th><td>40–56dp, dynamic</td></tr><tr><th style="width:50%;text-align:center">Item corner radius</th><td>28dp</td></tr></tbody></table></div>

<h2>Uncontained</h2><p>The <app-froala-tooltip-element description="The uncontained carousel layout show items that scroll to the edge of the container." link-label link-url should-open-link-in-new-tab="false">uncontained</app-froala-tooltip-element> layout shows items that scroll to the edge of the container.</p>

4 elements of an uncontained carousel layout.

<ol><li id="isPasted">Container</li><li>Large carousel item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyr7jh4c-7.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/p9Q_QbNpwi3QeDBOCZ64MWO3Vm83NIV7SFc6IqJ7BPGlsGidp5FJdTOq4yVq6zCZkqkSf03SLJ2pSEU4vrj7udhaxrBi10bGrtfAWev8AZWU=s2048

<h3>Measurements</h3>

Measurements of an uncontained carousel layout.

<p>Uncontained carousel items bleed over the padding on each side when scrolling</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi9mdco2-08-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/kHmHj0O9aT5Nlb2KyOQq6CWd8sRWmGjzg3TMKEzoHQLd9OG08KSdrH7g3vUxMkGebXOb17s3kAT6fh16dVWyzKDJrBkuFIedIZpi3H1rGBmtbg=s2048

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="text-align:center">Attribute</th><th style="text-align:center">Value</th></tr></thead><tbody><tr><th style="width:50%;text-align:center" class="fr-cell-fixed ">Alignment</th><td>Vertically centered</td></tr><tr><th style="width:50%;text-align:center">Leading padding</th><td>16dp</td></tr><tr><th style="width:50%;text-align:center">Top/bottom padding<br /></th><td>8dp</td></tr><tr><th style="width:50%;text-align:center">Padding between elements<br /></th><td>8dp</td></tr><tr><th style="width:50%;text-align:center" class="fr-cell-handler ">Item corner radius</th><td>28dp</td></tr></tbody></table></div>

<h2 id="isPasted">Uncontained mutli-aspect ratio</h2><p>The uncontained multi-aspect ratio layout shows carousel items of various widths.</p>

4 elements of an uncontained carousel layout

<ol class="decimal"><li id="isPasted">Container</li><li>Carousel item (16:9)</li><li>Carousel item (9:16)</li><li>Carousel item (1:1)</li><li>Carousel item (3:4)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi9lyvnk-09-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/FM3l_rU4tOFqCVj-gmDwOG9zyWk279AI0tz5aHQa5hRW5v3P4cS3ydvtXKwZMy_ClxODMX76POePAuI9k_ZsvZfZt3yxWISoKWkbSQhmw1M=s2048

<h3>Measurements</h3>

<p>Uncontained multi-aspect ratio carousels only have leading padding, with 8dp of padding between items.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi9m4p2v-10-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/1SazYXoMFnNnFpmqXCe7pchjco1F_R03ws6GfweuJDv4cgafUAQ0l0P_8ELNDh-l8UEyycEhodtkGYJgG_s6Zn0GLzQ6IP4UwcSpCUW9O0N-=s2048

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="text-align:center">Attribute</th><th style="text-align:center">Value</th></tr></thead><tbody><tr><th style="width:50%;text-align:center" class="fr-cell-fixed ">Alignment</th><td>Vertically centered</td></tr><tr><th style="width:50%;text-align:center">Leading padding</th><td>16dp</td></tr><tr><th style="width:50%;text-align:center">Top/bottom padding<br /></th><td>8dp</td></tr><tr><th style="width:50%;text-align:center">Padding between elements<br /></th><td>8dp</td></tr><tr><th style="width:50%;text-align:center" class="fr-cell-handler ">Item corner radius</th><td>28dp</td></tr></tbody></table></div>

<h2>Hero</h2><p>The <app-froala-tooltip-element description="The hero carousel layout shows at least one large and one small item at a time." link-label link-url should-open-link-in-new-tab="false">hero layout</app-froala-tooltip-element> shows at least one large item and one small item.</p>

3 elements of a hero carousel layout.

<ol><li id="isPasted">Container</li><li>Large carousel item</li><li>Small carousel item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyr7l425-9.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/I9ALEx4jwdluVMjRmR2zhTCFVHo3N05uccMHUOXxA1pAD-XMUdr9GNHJPfOT9mkNz862VyWH2ItNhseEOpdJsWv1RI-o6-sxxPuV4UG6coQdDg=s2048

<h3>Measurements</h3>

Measurements of a hero carousel layout.

<p>Hero<span style="white-space:pre-wrap"> carousels have padding on both sides of the container</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi9macpj-12-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LOm-yrGl6Hmuxn-eQ995_1ZlFqkd90so8hX-xPss8PWGCyXWDJECAupl-paVut_4taB6DVA7OENO39mxBfDAgXcPC_kZXCNlPTdnCQxBYZ4=s2048

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="text-align:center">Attribute</th><th style="text-align:center">Value</th></tr></thead><tbody><tr><th class="fr-cell-fixed " style="width:50%;text-align:center">Alignment</th><td>Vertically centered</td></tr><tr><th style="width:50%;text-align:center">Leading/Trailing padding</th><td>16dp</td></tr><tr><th style="width:50%;text-align:center">Top/bottom padding</th><td>8dp</td></tr><tr><th style="width:50%;text-align:center">Padding between elements</th><td>8dp</td></tr><tr><th style="width:50%;text-align:center">Large item width</th><td>Dynamic</td></tr><tr><th style="width:50%;text-align:center">Small item width</th><td>40-56dp, dynamic</td></tr><tr><th class="fr-cell-handler " style="width:50%;text-align:center">Item corner radius</th><td>28dp</td></tr></tbody></table></div>

<h2>Center-aligned hero</h2><p><span style="white-space:pre-wrap" id="isPasted">The center-aligned hero layout shows at least one large item and two small items.</span></p>

3 elements of a center-aligned hero carousel layout.

<ol><li id="isPasted">Container</li><li>Large carousel item</li><li>Small carousel item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyr7mksj-11.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/4LmjbjezXxY7ctWR2bmLAa35m3No8ErHZO31L0jTLxRBc3ivUMC_DA5rDEEZRILu8VlJLE__deFfvXQxuvJ0hjhAuD4-MLc1D3RVqUF-7g=s2048

<h3>Measurements</h3>

Measurements of a center-aligned hero carousel layout.

<p>Center-aligned hero carousels have padding on both sides of the container</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi9mb8nd-14-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/SuFPyTcmkMVHYU4NubWqAMrraBaL0OAFzvUcuXPWlkmIsASj8fOjlwGNfNpl4LP9revB2iU8dc-oFBOXNlX3tfcFfD7ny6W2MrubF9hcGqH1=s2048

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="text-align:center">Attribute</th><th style="text-align:center">Value<br /></th></tr></thead><tbody><tr><th style="width:50%;text-align:center">Alignment</th><td>Vertically centered</td></tr><tr><th style="width:50%;text-align:center">Leading/Trailing padding</th><td>16dp</td></tr><tr><th style="width:50%;text-align:center">Top/bottom padding</th><td>8dp</td></tr><tr><th class="fr-cell-fixed " style="width:50%;text-align:center">Padding between elements</th><td>8dp</td></tr><tr><th style="width:50%;text-align:center">Large item width</th><td>Dynamic</td></tr><tr><th style="width:50%;text-align:center">Small item width</th><td>40-56dp, dynamic</td></tr><tr><th class="fr-cell-handler " style="width:50%;text-align:center">Item corner radius</th><td>28dp</td></tr></tbody></table></div>

<h2>Full-screen</h2><p>The <app-froala-tooltip-element description="The full-screen carousel layout shows one edge-to-edge large item at a time and scrolls vertically." link-label link-url should-open-link-in-new-tab="false">full-screen layout</app-froala-tooltip-element> shows one edge-to-edge large item.</p>

2 elements of a full-screen carousel layout.

<ol><li id="isPasted">Container</li><li>Large carousel item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyr7o850-13.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/bn-epGZhbTWJijBRurEco_OYDKB-s-DEYMJgCwj7OSBbLJMEm34yEZY1AaKy2gEKjnMCT--UTHHqR0IOGlwj2p8aaPNPW3zdAENXMy5BwpT0SA=s2048

<h3>Measurements</h3>

Measurements of a full-screen carousel layout.

<p>Full-screen carousels fill the window edge-to-edge</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi9mbqt5-16-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/qo38AJlGFDaPzNKJX24tQG5PrvIQ_PRl0ZEmeh-7YE8FvikHGuh96N5ggGpDoOStYSzbhUAg0-36VmHVC9QmpqGifut7G4QG3G1RCtu13UKO=s2048

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="text-align:center">Attribute</th><th style="text-align:center">Value</th></tr></thead><tbody><tr><th style="width:50%;text-align:center">Alignment</th><td>Centered</td></tr><tr><th style="width:50%;text-align:center">Leading/Trailing padding</th><td>0dp</td></tr><tr><th style="width:50%;text-align:center">Top/bottom padding<br /></th><td>0dp</td></tr><tr><th style="width:50%;text-align:center">Padding between elements<br /></th><td>16dp</td></tr></tbody></table></div>

## Guidelines

Carousel items adapting dynamically to device size by shrinking and reducing in number.

<p>Carousel items adapt dynamically based on breakpoint</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwusb1kq-1.png?alt=media

<h2>Usage</h2>

<p id="isPasted">Carousels display a scrollable list of items. Carousel items emphasize visuals, but can also contain brief text that adapts to the item size.</p><p>There are four carousel layouts:</p><ul><li><app-froala-tooltip-element description="The multi-browse carousel layout shows at least one large, medium, and small carousel item at a time." link-label link-url should-open-link-in-new-tab="false">Multi-browse</app-froala-tooltip-element></li><li><app-froala-tooltip-element description="The uncontained carousel layout show items that scroll to the edge of the container." link-label link-url should-open-link-in-new-tab="false">Uncontained</app-froala-tooltip-element></li><li><app-froala-tooltip-element description="The hero carousel layout shows at least one large and one small item at a time." link-label link-url should-open-link-in-new-tab="false">Hero</app-froala-tooltip-element></li><li><app-froala-tooltip-element description="The full-screen carousel layout shows one edge-to-edge large item at a time and scrolls vertically." link-label link-url should-open-link-in-new-tab="false">Full-screen</app-froala-tooltip-element></li></ul><p>All of these layouts can be centered, though <app-froala-tooltip-element description="The center-aligned hero carousel layout shows at least one large and two small items at a time. The large item is centered." link-label link-url should-open-link-in-new-tab="false">center-aligned hero</app-froala-tooltip-element> is the most common centered carousel.</p><p>Carousels can scroll in two ways:</p><ul><li><strong>Default</strong>: Standard scrolling. Recommended for uncontained layouts.</li><li><strong>Snap-scrolling</strong>: Scrolled items snap to the carousel's layout. Recommended for multi-browse, hero, and full-screen layouts</li></ul>

Contained carousel with a large, medium, and small item. Text is hidden on the small item.

<p>A carousel can contain different sized items</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwusbuoo-2.png?alt=media

<p>Choose the best carousel layout for your product. Some layouts are more visual-focused, while others are more customizable.</p>

<div class="table-wrapper"><table style="width:100%" class="fr-table-selection-hover"><thead><tr><th style="text-align:center"><div style="text-align:center">Layout</div></th><th style="text-align:center"><div style="text-align:center">Best used for</div></th></tr></thead><tbody><tr><td><a href="/m3/pages/carousel/guidelines#d95cefa4-53df-45e2-bbb2-3aeeecbe9639"><u>Multi-browse</u></a></td><td>Browsing many visual items at once (like photos), dynamic designs</td></tr><tr><td><a href="/m3/pages/carousel/guidelines#96c5c157-fe5b-4ee3-a9b4-72bf8efab7e9"><u>Uncontained</u></a></td><td>Highly-customized or text-heavy carousels, stacked imaged and text, traditional carousel behavior</td></tr><tr><td><a href="/m3/pages/carousel/guidelines#5991f961-79aa-4955-b86e-3e15432108e6"><u>Hero</u></a></td><td>Spotlighting very large visual items (like a movie or featured app)</td></tr><tr><td><a href="/m3/pages/carousel/guidelines#a9f8dcde-e5c5-464f-b488-d9ded9ae4a4a"><u>Center-aligned hero</u><br /></a></td><td>Centered, large visual items</td></tr><tr><td><a href="/m3/pages/carousel/guidelines#ae0f1566-a956-4c4b-b153-d50ee20c32e7"><u>Full-screen</u><br /></a></td><td>Vertically-scrolling video or image feeds, immersive experiences</td></tr></tbody></table></div>

<p>Carousel items must be fully visible on-screen (except for the <app-froala-tooltip-element description="The uncontained carousel layout show items that scroll to the edge of the container." link-label link-url should-open-link-in-new-tab="false">uncontained layout</app-froala-tooltip-element>). When scrolled, items automatically change size and snap into place to maintain the same layout.</p>

Multi-browse carousel with all images and text easily legible.

<p>Set the large carousel item size to ensure the images and text are easy to read and recognize</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuscosc-3-do.png?alt=media

Multi-browse carousel with a very thin small item, making the image unrecognizable.

<p>Avoid setting carousel items so small that the image isn't recognizable</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwusd3wu-3-don't.png?alt=media

<h3 id="isPasted">Accessibility requirements on scrolling pages</h3><p id="isPasted">On vertically-scrolling pages, carousels require an accessible way to view all the items without horizontally scrolling. (This requirement doesn't apply to <app-froala-tooltip-element description="The full-screen carousel layout shows one edge-to-edge large item at a time and scrolls vertically." link-label link-url should-open-link-in-new-tab="false">full-screen carousels</app-froala-tooltip-element>.)</p><p>Material recommends adding a <strong>Show all</strong> button below the carousel, which opens a dedicated vertically-scrolling page of all carousel items.</p><p>If the carousel has a header, you can use an arrow icon button instead. </p><p>View the <a href="/m3/pages/carousel/accessibility"><u>accessibility tab</u></a> for more details and alternate solutions.</p>

Carousel on mobile has a "show all" button that opens a page with all carousel items.

<p>Make sure users can scroll vertically through all carousel items</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwutlc75-GM3-Components-Carousel-Guidelines-1-v01.mp4?alt=media

<h3 id="isPasted">Multi-browse</h3><p>The <app-froala-tooltip-element description="The multi-browse carousel layout shows at least one large, medium, and small carousel item at a time." link-label link-url should-open-link-in-new-tab="false">multi-browse layout</app-froala-tooltip-element> is best for browsing many items at once, like photos or event feeds. Snap-scrolling is recommended to ensure items are recognizable and consistently sized.</p><p>On larger screens, more large and medium items are visible in this layout.</p><p>Avoid using this layout if the carousel items need lots of text or have complicated imagery.</p>

Swiping a multi-browse carousel with snap-scrolling. Items adjust size to fit the layout.

<p>A multi-browse layout has different sized items within the carousel</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwutm3x8-GM3-Components-Carousel-Guidelines-2-v01.mp4?alt=media

<p>At <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoints</app-froala-tooltip-element>, only show up to three carousel items if they have text.</p><p>If you need to show more than three items, make sure the images and content are easy to understand and recognize.</p>

Carousel on a phone. 2 large, 1 medium, and 1 small item are fully visible but thin. The items don't have text.

<p>At compact breakpoints, only show more than three items if the items are easy to understand and recognize</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwusga4v-6.png?alt=media

<h3 id="isPasted">Uncontained</h3><p>The <app-froala-tooltip-element description="The uncontained carousel layout show items that scroll to the edge of the container." link-label link-url should-open-link-in-new-tab="false">uncontained layout</app-froala-tooltip-element> is most similar to a traditional carousel, where items are a single size and flow past the edge of the screen.</p><p>Both default scrolling and snap-scrolling work well with this layout.</p><p>Since items don't change size, this layout can be customized to show more text or other UI above or below each item without the text being masked or cropped.</p>

Swiping an uncontained carousel with default scrolling. Items scroll to the edge and can stop anywhere.

<p>Carousel items are all the same size in an uncontained layout</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwutpwf6-GM3-Components-Carousel-Guidelines-3-v01.mp4?alt=media

<h3>Uncontained multi-aspect ratio</h3><p>The <app-froala-tooltip-element description="The uncontained multi-aspect ratio layout shows carousel items of various widths." link-label link-url should-open-link-in-new-tab="false">uncontained multi-aspect ratio</app-froala-tooltip-element> carousel has the same layout as the uncontained carousel but contains items of various sizes.</p><p>Item widths can range anywhere between 9:16 for min width size to 16:9 for max width.</p><p>Only use this carousel layout if the items have various widths.</p>

Swiping an uncontained carousel with default scrolling. Items scroll to the edge and can stop anywhere.

<p id="isPasted"><span style="white-space:pre-wrap">Carousel items are of various sizes in an uncontained multi-aspect ratio layout</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmgtvndn1-GM3_Expressive_Carousel_Guidelines%2008_IA_v02.mp4?alt=media

<h3 id="isPasted">Hero</h3><p>The <app-froala-tooltip-element description="The hero carousel layout shows at least one large and one small item at a time." link-label link-url should-open-link-in-new-tab="false">hero layout</app-froala-tooltip-element> is best for spotlighting content that needs more attention, like movie, shows, or other media thumbnails. It highlights one large image to focus on, while providing a sneak peek of what’s next. </p><p>On larger screens, more large items are visible.</p><p>Use snap-scrolling so users can easily cycle through items one at a time.</p>

Swiping a hero carousel with snap-scrolling. Items adjust size to fit the layout.

<p>A hero carousel at a compact breakpoint should show one large item and one small item</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwutqti0-GM3-Components-Carousel-Guidelines-4-v01.mp4?alt=media

<h3 id="isPasted">Center-aligned hero</h3><p>When the <app-froala-tooltip-element description="The hero carousel layout shows at least one large and one small item at a time." link-label link-url should-open-link-in-new-tab="false">hero layout</app-froala-tooltip-element> is center-aligned, it adds an additional previewed item on the leading edge, making the large carousel item centered.</p>

Swiping a center-aligned hero carousel with snap-scrolling. Items adjust size to fit the layout.

<p>A centered hero carousel has two small carousel items, with a large item centered</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuts7ja-GM3-Components-Carousel-Guidelines-5-v01.mp4?alt=media

<h3>Full-screen</h3><p>The <app-froala-tooltip-element description="The full-screen carousel layout shows one edge-to-edge large item at a time and scrolls vertically." link-label link-url should-open-link-in-new-tab="false">full-screen layout</app-froala-tooltip-element> is best used for immersive experiences like video articles, featured headlines, or items that are visually rich. It can contain text and other UI elements on top of the image.</p><p>This layout works best with content that is taller than it is wide, and scrolls vertically. It only works in portrait orientation in compact and <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium breakpoints</app-froala-tooltip-element>. Don't use this layout in landscape orientation.</p><p>Use snap-scrolling for full-screen layouts. Don't use default scrolling.</p>

Vertically swiping a full-screen carousel with snap-scrolling. Items fit edge-to-edge.

<p>Full-screen carousels fill the entire content area of the screen</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwutt19y-GM3-Components-Carousel-Guidelines-6-v01.mp4?alt=media

<h2>Anatomy</h2>

4 elements of a carousel.

<p>Multi-browse carousel (left) and hero carousel (right):</p><ol><li id="isPasted">Container</li><li>Large carousel item</li><li>Medium carousel item</li><li>Small carousel item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwushw0z-11.png?alt=media

<h3>Container</h3><p>The carousel container holds all carousel items. The number of carousel items visible in the container can change based on the carousel <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/google-material-3/pages/layout-overview" should-open-link-in-new-tab="true">layout</app-froala-tooltip-element> and <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoint</app-froala-tooltip-element>.</p>

An empty rectangle representing a carousel container.

<p>The carousel container is a rectangle. It can be used in many ways and stretched to any size.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwusikhn-12.png?alt=media

<h3>Carousel items</h3><p>Carousel items hold content. A carousel item has no fixed width; it changes width depending on the breakpoint or its position in the carousel's layout. There are three dynamic widths an item can be: <strong>large</strong>, <strong>medium</strong>, and <strong>small</strong>.</p>

3 sizes of carousel items.

<ol><li id="isPasted">Large carousel item</li><li>Medium carousel item</li><li>Small carousel item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwusj1ii-13.png?alt=media

<p id="isPasted">Large items have a max width that can be adjusted. This changes how all other large, medium, and small carousel items fit on screen. Large items must remain big enough to be easy to understand and recognize.</p><p>Medium items adjust width dynamically to the carousel size and available space. </p><p>Small items have a width range of 40–56dp.</p>

2 sizes of carousel items for hero layouts.

<ol><li id="isPasted">Large item</li><li>Small item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwusjjti-14.png?alt=media

<p>When the large item's max width is narrow enough, more items can be shown on screen at once. At compact breakpoints, this is only recommended for carousels with simple imagery.</p>

3 sizes of carousel items for multi-browse layouts. 2 large items are visible.

<ol><li>Large item</li><li>Medium item</li><li>Small item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuslefr-15.png?alt=media

<h3>Item text (optional)</h3><p id="isPasted">Carousel items are primarily visual. Item text is optional and should be brief. </p><p>If your carousel items require a lot of text, consider using the <strong><app-froala-tooltip-element description="The uncontained carousel layout show items that scroll to the edge of the container." link-label link-url should-open-link-in-new-tab="false">uncontained layout</app-froala-tooltip-element></strong>, which can show more information, or use a series of <app-froala-tooltip-element description="Cards display content and actions about a single subject." link-label="More on cards" link-url="/m3/pages/cards/overview" should-open-link-in-new-tab="true">cards</app-froala-tooltip-element> instead.</p>

Contained carousel items with 5 lines of content: a title, a description, and a label.

<p>Avoid exceeding two lines of text in carousel items at compact breakpoints unless the background is simple, like a single color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwusmns4-16.png?alt=media

<p>Content within a carousel item can adapt dynamically based on the container and breakpoint. </p><p>Text should always be understandable at each size. Consider adapting the text to use brief labels on smaller carousel items.</p>

A carousel item at 3 different sizes to show  how text changes at each size.

<ol><li id="isPasted">Large carousel item with the full title and label text</li><li>Medium carousel item hiding the title text</li><li>Small carousel item abbreviating the label text</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwusqbrm-17.png?alt=media

<h2>Adaptive design</h2>

<p>As the carousel container size increases, so do the number of carousel items visible at a time.</p><p>At <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoints</app-froala-tooltip-element>, carousels can comfortably show up to three carousel items at once.</p><p>At larger breakpoints, more carousel items are added and scale in size.</p><p><app-froala-tooltip-element description="The full-screen carousel layout shows one edge-to-edge large item at a time and scrolls vertically." link-label link-url should-open-link-in-new-tab="false">Full-screen carousels</app-froala-tooltip-element> only ever show one item at once.</p>

8 carousel items visible at once on a tablet in landscape orientation.

<p>Carousels can show more items at once on larger screens</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuso0q8-18.png?alt=media

<h2>Behavior</h2>

<h3 class="placeholder--hidden">Scrolling</h3><p id="isPasted">Carousel items have a parallax effect when they're scrolled.</p><p>The <strong>default</strong> scrolling behavior doesn't snap items to a layout grid. They can stop anywhere in the container. Only use this for the <app-froala-tooltip-element description="The uncontained carousel layout show items that scroll to the edge of the container." link-label link-url should-open-link-in-new-tab="false">uncontained layout</app-froala-tooltip-element>.</p><p>The <strong>snap-scrolling</strong> behavior aligns carousel items to the layout grid after they're scrolled. Items snap to the grid when released. Use this for <app-froala-tooltip-element description="The multi-browse carousel layout shows at least one large, medium, and small carousel item at a time." link-label link-url should-open-link-in-new-tab="false">multi-browse</app-froala-tooltip-element>, <app-froala-tooltip-element description="The hero carousel layout shows at least one large and one small item at a time." link-label link-url should-open-link-in-new-tab="false">hero</app-froala-tooltip-element>, and <app-froala-tooltip-element description="The full-screen carousel layout shows one edge-to-edge large item at a time and scrolls vertically." link-label link-url should-open-link-in-new-tab="false">full-screen layouts</app-froala-tooltip-element>.</p>

Multi-browse carousel with snap-scrolling. Items slot into the layout once scrolled.

<p>Carousel items with snap-scrolling maintain the same layout when released</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwutupr4-GM3-Components-Carousel-Guidelines-7-v01.mp4?alt=media

<p id="isPasted">In full-screen layouts, make sure the carousel items snap to the edges of the carousel container. Avoid letting them scroll freely or stop halfway.</p><p>Full-screen layouts must use snap-scrolling.</p>

Full-screen carousel with items stopping halfway off screen once scrolled.

<p>Avoid scrolling freely on full-screen carousels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuspl2g-20-don't.png?alt=media

## Accessibility

<h2>Use cases</h2>

<p id="isPasted">Users should be able to do the following with assistive technology:</p><ul><li>Navigate to the carousel container</li><li>Navigate between different carousel items</li><li>Activate a carousel item</li><li>Skip over the carousel items</li></ul>

<h2>Requirements on scrolling pages</h2>

<p id="isPasted">On vertically-scrolling pages, carousels require an accessible way to view all the items without horizontally scrolling. (This requirement doesn't apply to <app-froala-tooltip-element description="The full-screen carousel layout shows one edge-to-edge large item at a time and scrolls vertically." link-label link-url should-open-link-in-new-tab="false">full-screen carousels</app-froala-tooltip-element>.)</p><p>Material recommends adding a <strong>Show all</strong> button below the carousel, which opens a dedicated vertically-scrolling page of all carousel items.</p>

Carousel on mobile has a "show all" button that opens a page with all carousel items.

<p>Carousels without headers should use a <strong>Show all </strong>button to view all carousel items</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwutxg2r-GM3-Components-Carousel-Accesibility-1-v01.mp4?alt=media

Measurements of a "show all" button added below a carousel.

<p>The <strong>Show all</strong> button should have a padding of 4dp</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwut0q8v-2.png?alt=media

<p id="isPasted">If the carousel has a header, you can use an arrow icon button instead. Place the arrow icon directly next to the header or in the same row.</p><p>Make sure the header is also displayed on the page of all carousel items.</p>

Carousels in a list on mobile with headers have an arrow icon that opens a page with all carousel items.

<p>Carousels with headers should use an arrow to view all carousel items</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwutykt0-GM3-Components-Carousel-Accesibility-2-v01.mp4?alt=media

Measurements of an arrow icon button added next to a carousel header.

<p>Headers should align with the leading edge, and the arrow icon should have a size of 48dp </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwut172a-4.png?alt=media

<p id="isPasted">Avoid customizing the accessibility solution when possible. However, if your product needs an alternative solution, consider adding a <strong>Show all</strong> button in nearby navigation, or add alternative control buttons close to the carousel.</p><p>Avoid adding UI elements, like arrows or other icons, within or beside the carousel.</p>

Arrow icons on the left and right of the carousel, reducing container width.

<p>Avoid adding buttons into the carousel container or beside it. Place any buttons above or below the carousel.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwykx1vc-5a-don't.png?alt=media

Arrow icons floating on top of the carousel edge, concealing items.

<p>Don't cover the carousel with buttons or other UI</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwykxhsn-5b-don't.png?alt=media

<h2>Interaction &amp; style</h2>

<h3>Touch</h3><p class="placeholder--hidden">Tapping on a carousel item changes the shape slightly, and creates a touch ripple for interaction feedback.</p>

Carousel providing a ripple feedback when being tapped.

<p>Touch: Tap</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuu2jae-GM3-Components-Carousel-Accesibility-3-v01.mp4?alt=media

<h3>Cursor</h3><p id="isPasted">The <app-froala-tooltip-element description="A hover state communicates when a user has placed a cursor above an interactive element." link-label="More on hover state" link-url="/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844" should-open-link-in-new-tab="true">hover state</app-froala-tooltip-element> provides a visual cue that the carousel item is interactive.</p><p>When the carousel item is clicked (in both active and inactive states), a ripple appears for interaction feedback.</p>

Carousel changing state when hovered.

<p>Cursor: Hover, click</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuu32xk-GM3-Components-Carousel-Accesibility-4-v02.mp4?alt=media

<h3>Initial focus</h3><p id="isPasted">When navigating to a carousel using assistive technology, use <strong>Tab</strong> to place initial focus on the first carousel item. Then, use <strong>Tab</strong> or the arrow keys to navigate the carousel items.</p><p>Use the up and down arrow keys to leave the carousel and focus on the next element on the page, like the <strong>Show all</strong> button.</p>

Diagram of how to navigate a carousel using assistive technology.

<p>Set initial focus on the first carousel item, and use arrows to navigate items</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwut9phs-8.png?alt=media

Diagram of how not to navigate a carousel using assistive technology.

<p>Avoid focusing on the carousel container</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuta5uo-9.png?alt=media

<h2 id="isPasted">Keyboard navigation</h2>

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="width:19.6256%;font-weight:500">Keys</th><th style="width:80.2536%;font-weight:500">Actions</th></tr></thead><tbody><tr><th style="width:19.6256%"><strong>Tab </strong>or <strong>Arrows</strong></th><td class="placeholder--hidden " style="width:80.2536%">Moves to the previous or next carousel item<br /></td></tr><tr><th><strong>Space</strong> or <strong>Enter</strong></th><td class="placeholder--hidden ">Activates the <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element> carousel item</td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<p>The carousel container has the <strong>container</strong> role.</p>

Accessibility labels of a carousel.

<p>The carousel container is labelled appropriately and has the <strong>container</strong> role</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwutav24-10.png?alt=media

<p>Each carousel may have a different number of items, so the label reads out the total amount of items and the current item in focus.</p>

Accessibility labels of a carousel item.

<p>The carousel item label indicates the current item in focus and the total number of items</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwutbdy7-11.png?alt=media

<h2 id="isPasted">Reduced motion</h2>

<p id="isPasted">When reduced motion settings are turned on, the parallax effect should be removed and carousel items should no longer expand as they come into view. All items are the same size.</p><p>Make sure carousels with reduced motion reach the edges of the window to avoid clipping visuals.</p>

Comparison of a multi-browse carousel with the reduced motion setting off and on.

<ol><li>Default carousel for multi-scroll</li><li>Carousel with reduced motion settings turned on</li></ol>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuu4mjv-GM3-Components-Carousel-Accesibility-5-v01.mp4?alt=media

<p>For <app-froala-tooltip-element description="The hero carousel layout shows at least one large and one small item at a time." link-label link-url should-open-link-in-new-tab="false">hero carousels</app-froala-tooltip-element> with reduced motion, the small carousel item is only partially shown on screen.</p>

Comparison of a hero carousel with the reduced motion setting off and on.

<ol><li>Default carousel for single-scroll</li><li>Carousel with reduced motion settings turned on</li></ol>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuu5ddb-GM3-Components-Carousel-Accesibility-6-v01.mp4?alt=media
