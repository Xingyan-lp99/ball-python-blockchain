# Navigation bar

Source: https://m3.material.io/components/navigation-bar
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/9e4cdffa-f7fd-425f-9915-867aafbcc7d6.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Use navigation bars in <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact window size class" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact</app-froala-tooltip-element> or <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium window size class" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> window sizes</p></li><li><p>Can contain 3-5 destinations of equal importance</p></li><li><p>Destinations don't change. They should be consistent across app screens.</p></li></ul>

Two navigation bars of different widths with 4 destinations.

<p>Navigation bar for compact and medium window sizes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fodjau-01.png?alt=media

<h2><span style="white-space:pre-wrap" id="isPasted">Availability &amp; resources</span></h2>

resourceName: designSystems/030656e0a1083ef1/components/41c723c0c0347dee

libraryModuleType: STATUS_TABLE

<h2><span style="white-space:pre-wrap" id="isPasted">M3 Expressive update</span></h2>

<p><strong>May 2025</strong></p><p>A new flexible navigation bar was introduced to replace the baseline navigation bar. It’s shorter and supports horizontal navigation items in medium windows. <a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank">More on M3 Expressive</a></p>

<p>Variants and naming:</p><ul><li><p>Baseline navigation bar is no longer recommended </p></li><li><p>Added <strong>flexible </strong>navigation bar</p><ul><li><p>Shorter height</p></li><li><p>Can be used in medium window sizes with horizontal navigation items</p></li></ul></li></ul><p>Color:</p><ul><li><p>Active label changed from <strong>on-surface-variant</strong> to <strong>secondary</strong></p></li></ul>

Navigation bar in M3 Expressive. It’s shorter than the baseline nav bar.

<p><span style="white-space:pre-wrap">The flexible navigation bar is shorter and can be used in medium windows with horizontal nav items</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmae7qe43-02.png?alt=media

<h2>Differences from M2</h2>

<ul><li>Color: New color mappings and compatibility with dynamic color</li><li>Elevation: No shadow</li><li>Layout: Container height is taller </li><li>States: The active destination can be indicated with a pill shape in a contrasting color</li><li>Name: Bottom navigation has been renamed <strong>navigation bar</strong></li></ul>

M2 nav bar with a drop shadow and no active indicator.

<p><span style="white-space:pre-wrap">M2: A drop shadow indicates placement on top of content. Filled and regular weight icons indicate active states.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0ddmjvm-03.png?alt=media

M3 nav bar with a surface color and active indicator.

<p><span style="white-space:pre-wrap">M3: Taller and no drop shadow. Filled icons and an active indicator indicate active state.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmae7pvz8-04.png?alt=media

## Specs

<h2>Variants</h2>

The recommended flexible navigation bar.

<ol><li><span style="white-space:pre-wrap">Flexible navigation bar</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3onczd-01.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/UvjUYsyF9gAgVOmfiC9h3zFaS-jU0wYws-HjqFyeiABhm3ubP8ZtHn__4wPEPmw3eR3D4C4O6sUeHVmdJ_IX9zTrzi1GmuiTUcQlauA2Fs-B=s2048

<h3>Baseline variants</h3>

<p>The baseline nav bar is no longer recommended, and should be replaced by the flexible nav bar, which is shorter and supports horizontal navigation items in medium windows. <a href="/m3/pages/navigation-bar/specs#46dc2521-acf0-44e3-bbc0-78dc225b9749" target="_blank">View baseline nav bar specs</a></p>

1 baseline navigation bar.

<ol class="decimal"><li><p>Navigation bar (not recommended)</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkq5ef63-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/PmEPtOw84s8SQu9KJJ0EX-gTgEL5PDGneaQfz9OVdFSXWjLd7P41B6qpIiWnAOuSfGl7JnCQOqa3Lfx8hZfXRG7HzJJNam-HCDFV1lfKvLlw=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Variant</p></th><th style="text-align:center"><p>M3</p></th><th style="text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td><p>Flexible navigation bar</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td><p>Navigation bar</p></td><td><p>Available</p></td><td><p>Not recommended.</p><p>Use <strong>flexible navigation bar</strong>.</p></td></tr></tbody></table></div>

<h2><span style="white-space:pre-wrap" id="isPasted">Configurations</span></h2>

<p>In compact windows, navigation bars use vertical items. In medium windows, navigation bars should use horizontal items.</p>

Two size configurations for navigation bar and items.

<ol class="decimal"><li><span style="white-space:pre-wrap">Vertical navigation items<br /></span></li><li><span style="white-space:pre-wrap">Horizontal navigation items</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3oovxg-7.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/p7YCl5pH99g_eM4-BCFHmEgxIdJxmb5UuE-CUwR8M9OjjPkNJpYAwQPZTAxamQBoiRr25F23T4mxDVNRUG3kESL--vZihbUkQWN04W9DAFiH=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Category<br /></p></th><th><p>Configuration<br /></p></th><th style="text-align:center"><p>M3<br /></p></th><th style="text-align:center"><p>M3 Expressive<br /></p></th></tr></thead><tbody><tr><td rowspan="2" style="width:25%"><p>Navigation item layout<br /></p></td><td><p>Vertical (default)<br /></p></td><td><p>Available<br /></p></td><td><p>Available<br /></p></td></tr><tr><td><p>Horizontal<br /></p></td><td><p>--<br /></p></td><td><p>Available<br /></p></td></tr></tbody></table></div>

<h2>Tokens &amp; specs</h2>

<p>Use the table's menu to switch between token sets for the navigation bar and the nav items. <a href="/m3/pages/navigation-bar/specs#3425f33a-0b11-492a-ae5a-40d63f939384" target="_blank" rel="noopener noreferrer"></a><a href="/m3/pages/design-tokens/overview/" target="_blank" rel="noopener noreferrer">Learn about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/52865380210a9b69

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Nav bar - Common', 'Nav bar - Item - Vertical', 'Nav bar - Item - Horizontal'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2><span style="white-space:pre-wrap" id="isPasted">Anatomy</span></h2>

Seven elements of the navigation bar.

<ol class="decimal"><li><span style="white-space:pre-wrap">Container<br /></span></li><li><span style="white-space:pre-wrap">Icon<br /></span></li><li><span style="white-space:pre-wrap">Label text<br /></span></li><li><span style="white-space:pre-wrap">Active indicator<br /></span></li><li><span style="white-space:pre-wrap">Small badge (optional)<br /></span></li><li><span style="white-space:pre-wrap">Large badge (optional)<br /></span></li><li><span style="white-space:pre-wrap">Large badge label </span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3opmda-1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/NkOIeqvJB7WxPg28DI-4uEHBrBfN38qDD2CWuX-NM2tTrxYwRknjdhOMzMCD1D9d65WN-Lzfo1Zg_B3G8Zk7pjT7Os-D2EfYGXQPDxawqpA=s2048

<h2 id="isPasted">Color</h2><p><span style="white-space:pre-wrap" id="isPasted">Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens; in implementation, a color value will be a token that references a value. </span><span style="white-space:pre-wrap" id="isPasted"><a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></span></p>

Six color roles of the navigation bar.

<p><span style="white-space:pre-wrap">Navigation bar color roles used for light and dark schemes:<br /></span></p><ol class="decimal"><li id="isPasted"><span style="white-space:pre-wrap">Surface container<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">On-secondary container<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">Secondary<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">Secondary container<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">On-surface variant<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">On-surface variant</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3oqa88-05.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ec6ZkQGVtf5t0AOua9lhgucAZ31inD_mF4vm24sW2MeH8X2dK3xV1rpfoNuX6hlO5rU7wJVfCH0KMCt8Xqzl0qDIR668oCFEKb97YswmeuuC=s2048

<p>For badge color roles, go to <a href="/m3/pages/badges/specs" target="_blank" rel="noopener noreferrer">badge specs</a>.</p>

<h2 id="isPasted">States</h2><p>States are visual representations used to communicate the status of a component or an interactive element.</p>

Four states of the navigation bar items.

<ol class="decimal"><li><span style="white-space:pre-wrap">Enabled<br /></span></li><li><span style="white-space:pre-wrap">Hovered (8% state layer)<br /></span></li><li><span style="white-space:pre-wrap">Focused (10% state layer)<br /></span></li><li><span style="white-space:pre-wrap">Pressed (10% state layer)</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmah8b097-3.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/FTJk0MWbkT2YuqVJl3k8F57gmzTtSUKbQCovcet18WLLqbCMFFYds_DS65Sx8fzuFpEK6G_W5lmDc55s5ZUEpvBZIGM31aOI1psEFpn7GWnk=s2048

<h2>Measurements</h2>

<p>The navigation bar stretches the full window width.</p>

Navigation bar padding and size measurements.

<p><span style="white-space:pre-wrap">Navigation bar padding and size measurements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3ovtkk-5.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/zjuYI8XOBcjHmnNU2V9qHk9gbz3xJW9E2cEVE0Ov9Bh2fz8VI7RoISP5ykh9u5mqCXhF1nYKXT696Hfw-YIUMzX37jseGZdsA2bN_-YfErA=s2048

<p>Vertical navigation items dynamically change width to equally fit the container. Horizontal navigation items have a fixed width, so extra space is added to the ends of the navigation bar instead.</p>

Navigation bar and item widths.

<p><span style="white-space:pre-wrap">Navigation bar width and margins for compact and medium windows.<br /></span></p><ol class="decimal"><li><span style="white-space:pre-wrap">Vertical navigation item<br /></span></li><li><span style="white-space:pre-wrap">Margin from window edge</span></li><li><span style="white-space:pre-wrap">Horizontal navigation item</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3owffv-6.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/VMRrzRH_T07zMqRPwp1sLZPmkAVJVwQDqqrhuD-synkhADa-mjbbjtbh_tWZ4QZ9ael3lvNq52dhMRNCMOTZRh5aISTWk7bvSEt-vud2RGvW=s2048

<hr /><p><br /></p>

<h2>Baseline navigation bar</h2>

7 elements of baseline navigation bar.

<ol class="decimal"><li><span style="white-space:pre-wrap">Container<br /></span></li><li><span style="white-space:pre-wrap">Icon<br /></span></li><li><span style="white-space:pre-wrap">Label text<br /></span></li><li><span style="white-space:pre-wrap">Active indicator<br /></span></li><li><span style="white-space:pre-wrap">Small badge<br /></span></li><li><span style="white-space:pre-wrap">Large badge<br /></span></li><li><span style="white-space:pre-wrap">Large badge label</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3ox4jl-3p_nav-bar_anatomy.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/DBrM1eLC6HN2CNBg9Gr9UjPRuBgV0C7N3JLMzR2Y3nemUs8z0I71LTJM36azNtt45cWQiwISFwjAGc2G8coCUD9vfnIi-30wBlBw7OB1rSk=s2048

<h3>Tokens &amp; specs</h3>

<p>These tokens are for the baseline navigation bar.</p>

resourceName: designSystems/20543ce18892f7d9/components/52865380210a9b69

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Navigation bar (baseline)', 'Nav bar - Common', 'Nav bar - Item - Vertical', 'Nav bar - Item - Horizontal'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['Navigation bar (baseline)', 'Nav bar - Common', 'Nav bar - Item - Vertical', 'Nav bar - Item - Horizontal']}

<h3><span style="white-space:pre-wrap" id="isPasted">Color</span></h3><p>Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens; in implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview">Learn more about design tokens</a></p>

6 color roles of baseline navigation bar.

<p><span style="white-space:pre-wrap">Navigation bar color roles used for light and dark schemes:<br /></span></p><ol class="decimal"><li><span style="white-space:pre-wrap">Surface<br /></span></li><li><span style="white-space:pre-wrap">On secondary container<br /></span></li><li><span style="white-space:pre-wrap">On surface<br /></span></li><li><span style="white-space:pre-wrap">Secondary container<br /></span></li><li><span style="white-space:pre-wrap">On surface variant<br /></span></li><li><span style="white-space:pre-wrap">On surface variant</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3oxof4-3p_nav-bar_color.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/iFtbyGfchUzulQmxsrcS-I7WwK9b3AywZsdXqs8Z1jIytViyh4uD1UC9qpNKi44ejAswfg-jDNjzVCkq8diuRU4130swhkqbtGDL508M2zU=s2048

<p>For badge color roles, go to <a href="/m3/pages/badges/specs" target="_blank" rel="noopener noreferrer">badge specs</a>.</p>

<h3><span style="white-space:pre-wrap" id="isPasted">States</span></h3><p><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">States are visual representations used to communicate the status of a component or an interactive element.</span></span></p>

4 states of baseline navigation bar.

<p><span style="white-space:pre-wrap">Navigation bar states: <br /></span></p><ol class="decimal"><li><span style="white-space:pre-wrap">Enabled <br /></span></li><li><span style="white-space:pre-wrap">Hovered <br /></span></li><li><span style="white-space:pre-wrap">Focused <br /></span></li><li><span style="white-space:pre-wrap">Pressed</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmamkex4k-11-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Tz8X4rigXztIPIhpYB584wZpWuKYAEz4C4mIBNVQksaN4sRvl_eXy8dk9cwcWhM3iOfOJVLvlckzcDdPOScuGYJVhjvzuSAMRwpvZk2mdNOpTw=s2048

<h2>Measurements</h2>

Baseline navigation bar padding and size measurements.

<p><span style="white-space:pre-wrap">Navigation bar padding and size measurements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmamkf93e-12-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/yZAR82Wh75nazTTTOrRenBXPtuOb1BG45198tsOGQMOTUk0QS_Ety_wa_9wsQRVXkBVii9TYrwCmSAiwxxlvHY95EetWd78rd4DPR-qTy3X-4Q=s2048

Baseline navigation bar target size and margins.

<p><span style="white-space:pre-wrap">Navigation bar target size and margins</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmamkhglx-13-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Cx_HLEfaqKx72AHNtDdP7raUEXmHCDKOWC40CCuYLkfYn6d93KRaJHBWdxVHOkoU22j4UAJJExrl3uQYnpFQ_wu895nHHKn8qNUXZVMtCwqT=s2048

<h2 id="isPasted">Configurations</h2>

3 configurations of the baseline navigation bar.

<ol class="decimal"><li><span style="white-space:pre-wrap">3 destinations<br /></span></li><li><span style="white-space:pre-wrap">4 destinations<br /></span></li><li><span style="white-space:pre-wrap">5 destinations</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3ozytu-3p_nav-bar_config.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ALYNjmr0KKRFb33P4hKrUxeXha7V6L7eyz_izrbW4nGMgFfZtYjbLa7cHF3mxpWOr4TiAswFklndquusmv_dRJsruNjzu4ZSh7WgBrOCWDQ=s2048

## Guidelines

A nav bar with vertical items in a compact window, and horizontal items in a medium window.

<p>Navigation bars adapt to different breakpoints</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqgvk7-01.png?alt=media

<h2>Usage</h2>

<p id="isPasted">Navigation bars provide access to three to five destinations. The nav bar is positioned at the bottom of windows for convenient access.</p><p>Each destination is represented by an icon and label text. One navigation destination is always active.</p><p>When a navigation bar icon is tapped or focused, people are taken to the navigation destination associated with that icon.</p>

A nav bar for a music app with 4 destinations: Home, Browse, Radio, Library, It’s in a compact window.

<p><span style="white-space:pre-wrap">Navigation bars can have three to five destinations</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalnqdza-02.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">Navigation bars should be used for:</span></p><ul><li><span style="white-space:pre-wrap" id="isPasted">Three to five main pages in the product</span></li><li><span style="white-space:pre-wrap" id="isPasted">Mobile or tablet only</span></li></ul><p><span style="white-space:pre-wrap" id="isPasted">Navigation bars shouldn’t be used for accessing single tasks, such as viewing one email.</span></p>

A nav bar for a music app with 4 destinations: Home, Browse, Radio, Library. It’s in a medium window.

<p><span style="white-space:pre-wrap">On mobile or tablet, navigation bars should be used for top-level destinations</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqhln7-03.png?alt=media

<p>The navigation items can be <strong>vertical</strong> or <strong>horizontal</strong>.</p><ul type="disc" style="list-style-type:disc"><li><p>Use vertical items in <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact windows</app-froala-tooltip-element>, like mobile</p></li><li><p>Use horizontal items in <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium windows</app-froala-tooltip-element>, like tablets</p></li></ul>

A nav bar with vertical items in a compact window, and horizontal items in a medium window.

<p><span style="white-space:pre-wrap">Vertical navigation items work best in compact windows. Horizontal items work best in medium windows.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqhs7x-04.png?alt=media

<p>For products with more than five navigation items, don’t use a navigation bar; the elements may collide and there likely won’t be enough space for translated text.<br /><br />Instead, consider using <app-froala-tooltip-element description="Tabs organize content across different screens and views." link-label="More on tabs" link-url="/google-material-3/pages/tabs/overview" should-open-link-in-new-tab="true">tabs</app-froala-tooltip-element> to organize similar content within a page, or hide the navigation behind a menu icon using a <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/google-material-3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">modal expanded navigation rail</app-froala-tooltip-element>.</p>

A nav bar with 7 items in a compact window.

<p><span style="white-space:pre-wrap">Avoid putting more than five navigation items in a navigation bar</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqi614-05-don't.png?alt=media

A nav bar with no labels for each page item.

<p><span style="white-space:pre-wrap">Don’t remove the labels from navigation items</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqimzs-06-dont.png?alt=media

A nav bar with 2 page items.

<p><span style="white-space:pre-wrap">Don’t use a navigation bar for fewer than three destinations. Instead, use tabs.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqir51-07-dont.png?alt=media

A nav bar is on the Library page of a music app. Tabs at the top of the page have secondary navigation for playlists, artists, albums, and songs.

<p><span style="white-space:pre-wrap">Use navigation for distinct pages and tabs for related content within a page</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fp4omq-08.png?alt=media

Nav bar using horizontal items in a compact window. The items are too wide and flow off screen.

<p><span style="white-space:pre-wrap">Navigation bar destinations have fixed positions. Don’t scroll them or modify their positions.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fp4ti0-09.png?alt=media

<h2 id="isPasted">Anatomy</h2>

6 elements of the nav bar.

<ol><li id="isPasted"><span style="white-space:pre-wrap">Container<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">Icon<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">Label text<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">Active indicator<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">Large badge (optional)<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">Small badge (optional)</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm3t918of-10.png?alt=media

<h3 dir="ltr" id="isPasted">Container</h3><p dir="ltr">The container should always be placed at the bottom of the product and span the full length of the window. Navigation items are centered within the container.<br /><br />The container has a color fill to provide separation from other content.</p>

The nav bar at the bottom of a medium window has a color fill to differentiate from the background.

<p><span style="white-space:pre-wrap">The navigation bar container holds all elements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm3t91cku-11.png?alt=media

<h3>Navigation items</h3><p>Navigation items hold all elements for each destination: the icon, label text, and active indicator. They can be <strong>vertical</strong>, with the text below the icon and indicator, or <strong>horizontal</strong>, with the icon and text beside each other inside the indicator. <br /><br />Vertical items are best in <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact windows</app-froala-tooltip-element>, and horizontal items are best in <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation" link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium windows</app-froala-tooltip-element>.<br /><br />Horizontal items are centered in the nav bar with outer margins.</p>

The nav bar in a medium window with padding on each side.

<p><span style="white-space:pre-wrap">The navigation bar is divided into equal-width segments with padding from the window edge</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm3t91mur-12.png?alt=media

<h3 dir="ltr" id="isPasted">Icons</h3><p dir="ltr">Navigation rail items must use icons that symbolize the content of their page. Browse <a href="https://fonts.google.com/icons" target="_blank" rel="noopener noreferrer">popular icon</a>.<br /><br />Use a filled icon for the active destination and outlined icons for inactive destinations. If an icon doesn’t have a filled version, apply <strong>semibold</strong> weight to the icon instead.</p>

An active nav item with a filled icon compared to inactive items with outlined icons.

<p id="isPasted"><span style="white-space:pre-wrap">Use filled icons when the navigation item is active</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fp9y48-13.png?alt=media

An active nav item with a semibold icon compared to inactive items with outlined icons.

<p id="isPasted"><span style="white-space:pre-wrap">If a filled version of an icon is unavailable, the icon’s weight must increase</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fpa2te-14.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">Active and inactive icons must have a minimum 3:1 contrast ratio with the container.</span></p>

4 nav items that are each different colors with low contrast with the background.

<p><span style="white-space:pre-wrap">Don’t use multiple or low-contrast colors in a navigation bar, as they make it harder for people to distinguish the active item and navigate to other destinations</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqnpkt-15-dont.png?alt=media

<h3 dir="ltr" id="isPasted">Active indicator</h3><p dir="ltr"><span style="white-space:pre-wrap" id="isPasted">The active indicator shows which page from the nav bar is currently being displayed.</span></p>

The current page in a nav bar has an active indicator.

<p><span style="white-space:pre-wrap">Use the active indicator only for the active destination</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqo0n5-16-do.png?alt=media

All items in a nav bar have active indicators.

<p><span style="white-space:pre-wrap">Don’t use the active indicator for more than one destination at a time</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqo7ag-17-dont.png?alt=media

<h3 dir="ltr" id="isPasted">Label text</h3><p dir="ltr">The label text should be a short, meaningful description of each navigation destination and another way for people to understand an icon’s meaning.<br /><br />All navigation items require a label text. It should be 1-2 words.</p>

A nav bar on a music app with clearly labelled destinations: home, browse, radio, library.

<p><span style="white-space:pre-wrap">Label text must be brief and clear</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fpamvs-18.png?alt=media

A nav bar with 1-word labels for each page.

<p><span style="white-space:pre-wrap">Use brief text labels to identify the purpose of a destination</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqoweq-19-do.png?alt=media

A nav bar with “Music catalog” for a label. The label is truncated.

<p><span style="white-space:pre-wrap">Don’t wrap or truncate text as it can make the label hard to understand</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqp27c-20-dont.png?alt=media

A nav bar with “Music catalog” for a label. The label is a smaller size to make the text fit.

<p><span style="white-space:pre-wrap">Don’t shrink longer text to fit on a single line</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqpu1t-21-dont.png?alt=media

<h3 dir="ltr" id="isPasted">Badges (optional)</h3><p dir="ltr">Navigation bars can display badges in the upper right corners of the destination icon.<br /><br />Badges can contain dynamic information, such as the number of new messages.</p>

A nav bar with a destination called “Go” with a small badge and one called “Saved” with a large badge saying “3.”

<p><span style="white-space:pre-wrap">Use a small badge to indicate an update, and a large badge to show the amount of updates</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqqg5m-22.png?alt=media

Horizontal nav items with the badges in the same place of the icon as vertical nav items.

<p><span style="white-space:pre-wrap">Badges overlap the icon in both vertical and horizontal navigation items</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqqlk1-23.png?alt=media

<h2>Placement</h2>

<p><span style="white-space:pre-wrap" id="isPasted">The floating action button (FAB) is placed above the navigation bar. Nav bars are always placed at the bottom of the window.</span></p>

The FAB should be right-aligned above the navigation bar

<p><span style="white-space:pre-wrap" id="isPasted">The FAB should be right-aligned above the navigation bar</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqqsyh-24-do.png?alt=media

A mobile page with a FAB overlapping a nav bar.

<p><span style="white-space:pre-wrap">Don’t cover the navigation bar with a FAB</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqqy0m-25-dont.png?alt=media

<p>Navigation bars can be temporarily covered by dialogs, bottom sheets, navigation drawers, the on-screen keyboard, or other elements needed to complete a flow. They should not be permanently obstructed on any screen.</p>

The navigation bar being covered by a bottom sheet when users take an action on screen.

<p><span style="white-space:pre-wrap">The search feature of the screen triggers the on-screen keyboard, temporarily covering the bottom navigation bar until the search flow is completed</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalo9ujs-GM3_Expressive_NavBar_Guidelines_26_IA_v01.mp4?alt=media

<h2>Adaptive design</h2>

<p>Adaptive design allows an interface to respond or change based on context, such as the user, device, and usage. More on <a href="/m3/pages/layout-overview/adaptive-design" target="_blank">adaptive design</a></p>

<h3>Resizing</h3><p>Only use navigation bars for <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> breakpoints. </p><p><strong>Compact</strong>: For narrow windows, use a navigation bar or modal navigation rail.</p><p><strong>Medium</strong>: Use a navigation bar or navigation rail. Decide based on whether horizontal or vertical space is more important.</p><p><strong>Expanded and extra-large</strong>: Use a navigation rail instead. Decide based on available window space and the number of navigation destinations.</p>

A music app with a nav bar adapting to larger screens, where it changes to horizontal items, and then into a nav rail.

<p>Navigation bars are best suited for compact and medium breakpoints</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalo6njn-GM3-Expressive_NavBar_Guidelines_Responsive%20Layout_27_IA_v04.mp4?alt=media

<p>The navigation bar container spans 100% of the window width.</p>

Navigation bar spanning the full width of a compact window.

<p><span style="white-space:pre-wrap">Navigation bars use 100% of the screen width</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalo8a44-28.png?alt=media

<p>The navigation bar is used on smaller devices. It’s not intended for desktop.</p>

Navigation bar spanning the full width of an expanded window size.

<p><span style="white-space:pre-wrap">Don’t use navigation bars for desktop layouts. Instead, use a navigation rail or tabs.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqsfoq-29.png?alt=media

<h3>Presentation</h3><p>In medium breakpoints, use horizontal nav items to better use available space.</p><p>Horizontal nav items should remain centered with the same padding at each breakpoint.</p>

Horizontal nav items have the same width in medium and expanded windows. Only the padding changes.

<p><span style="white-space:pre-wrap">A navigation bar in horizontal orientation keeps the same spacing between destinations</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fpt5k2-30.png?alt=media

<h2>Behavior</h2>

<h3 dir="ltr" id="isPasted">Navigation</h3><p id="isPasted">When selecting a navigation bar item not currently selected, the product navigates to that destination’s screen using a <a href="/m3/pages/motion-transitions/transition-patterns#f852afd2-396f-49fd-a265-5f6d96680e16" target="_blank" rel="noopener noreferrer">top level</a> transition pattern. It can either remember where you left off, or reset to the default view.</p><ol class="decimal"><li><strong>Preserve state</strong>: If someone has interacted with this destination, it returns to their scroll position, current tab, and in-line search status.</li><li><strong>Reset state</strong>: Any prior user interactions are reset, including scroll position, tab selection, and in-line search.</li></ol><p>Choose the behavior that best suits the product and user needs. For example, an app that requires frequent switching between sections should preserve each section’s state.</p>

After selecting an item on the bottom navigation bar, the app navigates to that destination’s screen

<p><span style="white-space:pre-wrap">After selecting an item on the bottom navigation bar, the app navigates to that destination’s screen</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fpu2iy-C%20-%20Switch%20Destination%20-%20RENDER%202x_240821.mp4?alt=media

<p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Re-selecting the currently active destination should reset the scroll position to the top of the page.</span></p><p><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted"><strong>Don't swipe between destinations</strong><br />Swiping across the screen does not navigate between destinations, and is not supported by the navigation bar. Swipe behavior should be reserved for related items, such as cards in a carousel, or actions such as archiving a list item.</span></span></p>

Selecting the currently active nav item scrolls the page content back to the top.

<p><span style="white-space:pre-wrap">Selecting the already selected navigation item scrolls to the top of the screen</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalod84x-GM3_Expressive_Nav-Bar_Guidelines_Behavior_Scrolling_32_IA_V04.mp4?alt=media

<h3>Scrolling</h3><p>Upon scroll, the navigation bar can appear or disappear. </p><p>Don’t hide the navigation bar on scroll when a <a href="https://m3.material.io/foundations/overview/assistive-technology#ec6f3e84-a51c-4dc0-a353-6844f5bde698" target="_self">screen reader</a> is active.</p>

When scrolling on the page, the nav bar scrolls the opposite direction off screen.

<p><span style="white-space:pre-wrap">Scrolling downward can hide the navigation bar; scrolling upward reveals it</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmaloebec-GM3_Expressive_Nav-Bar_Guidelines_Behavior_Scrolling_33_IA_V04.mp4?alt=media

<h3 dir="ltr" id="isPasted">Selection</h3><p dir="ltr">The icon becomes filled and the active indicator expands from the center of the icon when switching between destinations.<br /><br />The active indicator animation should only apply on one axis to better represent a flat, shared plane.</p>

The active indicator expands from the target when a destination is selected

<p><span style="white-space:pre-wrap">An active indicator appears when the item is selected.</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalof0yh-GM3-Expressive_NavBar_Guidelines_34_IA_v01.mp4?alt=media

<p id="isPasted">When a destination is tapped, the destination screens use a <a href="/m3/pages/motion-transitions/transition-patterns#f852afd2-396f-49fd-a265-5f6d96680e16" target="_blank" rel="noopener noreferrer">top level</a> transition pattern. In addition, the icon becomes filled and the active indicator expands from the center of the icon.</p>

Selecting the home item changes the entire page contents.

<p><span style="white-space:pre-wrap">Tapping a destination uses a top level transition pattern</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fq2m3b-G%20-%20CU%20Destination%20Change%20-%20RENDER%202x_240821.mp4?alt=media

## XR

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">This is a rapidly changing space. Guidelines are primarily intended for designers at this time. Find what’s implemented in code in the <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank" rel="noopener noreferrer">design kit</a>.</div></div></div>

<p><span style="white-space:pre-wrap" id="isPasted">Extended reality (XR) interfaces have special design requirements, like showing apps in 3D space. Material has an XR-specific navigation bar with custom specs and guidance. See </span><span style="white-space:pre-wrap" id="isPasted"><a href="http://developer.android.com/design/ui/xr/guides/foundations" target="_blank" rel="noopener noreferrer">XR developer documentation</a></span><span style="white-space:pre-wrap" id="isPasted"> for more details.</span></p>

<h2>Anatomy</h2>

Diagram of navigation bar orbiter identifying 7 internal elements of the component.

<ol><li>Container</li><li>Icon</li><li>Active indicator </li><li>Small badge (optional)</li><li>Large badge (optional)</li><li>Large badge label (optional)</li><li>Label text</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3p1hrw-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/NW9kaqkcTarsiort-BDPnf0QKIkvHB7lo6Mbbh8SZUvS-c-EB3LLLFQrfeJMXk7uRlDFbNtkCWBCSRYRe00HwvDagwyWESwwQbf9Vpkiz-nKqw=s2048

<h2>Color &amp; elevation</h2>

<p>On XR, color is used to highlight elevated UI elements and <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels." link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiters</app-froala-tooltip-element>. With <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation" target="_blank" rel="noopener noreferrer">spatial elevation</a>, the navigation bar displays above the <app-froala-tooltip-element description="In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content." link-label="More on spatial panels" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels" should-open-link-in-new-tab="true">spatial panel</app-froala-tooltip-element>, on the Z-axis. Color communicates elevation on UI elements and orbiters. Elevated nav bars can use any of these color options:</p>

4 versions of elevation color strategy.

<ol><li>Surface container</li><li>Surface container high</li><li>Surface container highest</li><li>Tertiary container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3p20d1-03.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/EYtK3dWA1t7RZze6HZnobQWRtKQiC_cuLBnJ_ceCPtbTbbqbc0E1LXNz2qCjRKTlibK7HZk1ks2RuQC1UWfAoSsRwrvlbySXSPEUSz8or2QO=s2048

<h2>Measurements</h2>

Measurements and padding for navigation bar orbiter.

<p><span style="white-space:pre-wrap">Navigation bar orbiter padding and measurements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3p2yvo-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/sHMs2ZBzr0w6PdPaUdjH4C-qlDH0Otnv-tBwkRLU3cO6-8MyE9Kkrjupxd5Y9oLtniqIjoeTHjjkN4aojalS0--hvHAYjrufQQMw7tiIPfGOjg=s2048

<h2>Usage</h2>

<p>In <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components." link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element>, a navigation bar can appear in an <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels." link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiter</app-froala-tooltip-element> for a more immersive experience. Currently, spatial capabilities, such as orbiters, are only available in full space. In <app-froala-tooltip-element description="Home space is compatible with mobile and large screen apps, but doesn’t support spatial components." link-label="More on home space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">home space</app-froala-tooltip-element>, use a regular navigation bar on the same plane as the body content to mimic a 2D experience.</p>

Interface showcasing navigation bar behavior and placement when transitioning from a 2D to 3D experience.

<p><span style="white-space:pre-wrap">Navigation bar behavior and placement changing when going from a 2D to a 3D experience</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4cjn15p-navbar_01.mp4?alt=media

<h2>Behavior</h2>

<h3>Global context</h3><p>When placed in global context, the navigation bar orbiter is centered at the bottom of the app it controls. It stays anchored to the app during layout or content changes. This ensures navigation elements are easy to find and use.</p>

A navigation bar orbiter placed in global context.

<p><span style="white-space:pre-wrap">A navigation bar orbiter centered and anchored to the bottom of the app</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma4aab35-XR_Nav-Bar_Behavior_01_V02.mp4?alt=media

<h3>Local context</h3><p><span style="white-space:pre-wrap" id="isPasted">When placed in local context, the navigation bar orbiter is centered at the bottom of the spatial panel it controls. It repositions in response to layout or content changes.</span></p>

A navigation bar orbiter placed in local context.

<p><span style="white-space:pre-wrap">Use caution before placing a navigation bar in local context. If it contains navigation elements that affect the overall app, a navigation bar orbiter should be placed in global context.</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma4aas8k-XR_Nav-Bar_Behavior_02_V02.mp4?alt=media

<h2>Placement</h2>

<h3>Navigation context</h3><p><span style="white-space:pre-wrap" id="isPasted">The position of the navigation bar orbiter should communicate its navigational context:</span></p><ul><li><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Use <strong>offset positioning</strong> for global actions that affect the overall app experience</span></span></li><li><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Use <strong>inset positioning</strong> for local actions that are specific to a spatial panel<br /></span></span></li></ul><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap" id="isPasted">A navigation bar orbiter can either overlap or be positioned adjacent to spatial panels with a 20dp margin for visual separation.</span><br /></span></p>

Navigation bar orbiter offset and inset positioning.

<p><span style="white-space:pre-wrap">Position the navigation bar orbiter to reflect context: offset for global actions, inset for spatial panel-specific actions</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cjc36g-navbar_02.mp4?alt=media

<h3>Inset positioning</h3><p><span style="white-space:pre-wrap" id="isPasted">Don’t obstruct content. To ensure a balanced and uncluttered layout, a navigation bar orbiter should overlap spatial panels by 12dp and no more than half their height.</span></p>

Navigation bar orbiter inset positioning beyond the 12dp recommendation.

<p><span style="white-space:pre-wrap">Avoid overlapping an inset a navigation bar orbiter by more than half its height</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cjdjqh-navbar_04.mp4?alt=media

<h3>Horizontal alignment</h3><p><span style="white-space:pre-wrap" id="isPasted">The navigation bar orbiter placement shouldn't exceed the width of adjacent spatial panels.</span></p>

Nav bar orbiter placement that exceeds the width of its spatial panel.

<p><span style="white-space:pre-wrap">The navigation bar orbiter shouldn’t exceed the width of the spatial panel</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cjfzpt-navbar_05.mp4?alt=media

<h3>Spatial panel alignment</h3><p><span style="white-space:pre-wrap" id="isPasted">A navigation bar orbiter should always be placed at the bottom of a spatial panel and within the immediate field of view (FOV). Follow common usability practices to make the experience easy to use and consistent across platforms.<br /><br />Avoid placing the navigation bar orbiter at the top of a spatial panel, as this area is typically reserved for app bar orbiters or other critical UI elements.</span></p>

Nav bar orbiter incorrectly placed above a spatial panel.

<p><span style="white-space:pre-wrap">Don't position a navigation bar orbiter at the top of a spatial panel. Position it at the bottom in the field of view to maintain usability and minimize interaction effort.</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cjhfb6-navbar_06.mp4?alt=media

<h2 id="isPasted">Accessibility considerations</h2>

<p><span style="white-space:pre-wrap" id="isPasted"><a href="https://developer.android.com/design/ui/xr/guides/get-started#make-app" target="_blank" rel="noopener noreferrer">XR accessibility</a></span><span style="white-space:pre-wrap" id="isPasted"> guidelines are still evolving. XR navigation bars should follow applicable Material </span><span style="white-space:pre-wrap" id="isPasted"><a href="/m3/pages/navigation-bar/accessibility">nav bar accessibility standards</a></span><span style="white-space:pre-wrap" id="isPasted">.</span></p>

## Accessibility

<h2 id="isPasted">Use cases</h2>

<p>People should be able to do the following using the assistive technology:</p><ul><li>Move between navigation destinations</li><li>Select a particular navigation destination from a set</li><li>Get appropriate feedback based on input type</li></ul>

<h2><span style="white-space:pre-wrap">Interaction &amp; style</span></h2>

<p><span style="white-space:pre-wrap"><strong>Touch</strong></span></p><ul><li><span style="white-space:pre-wrap" id="isPasted">When a navigation item is tapped, the active indicator appears in place, providing feedback that it’s selected<br /></span></li><li><span style="white-space:pre-wrap" id="isPasted">A touch ripple passes through the indicator<br /></span></li><li><span style="white-space:pre-wrap" id="isPasted">The icon switches from outlined to filled<br /></span></li><li><span style="white-space:pre-wrap" id="isPasted">The icon changes color</span></li></ul>

On a navigation bar, when the Home and Explore icons are tapped, an active indicator is displayed as interaction feedback.

<p><span style="white-space:pre-wrap">Touch: Tap</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7paivnz-GM3-Accessibility_Expressive_NavBar_a11y_01_V03.mp4?alt=media

<p><span style="white-space:pre-wrap"><strong>Cursor</strong></span></p><ul><li><span style="white-space:pre-wrap" id="isPasted">When hovered, the active indicator appears in a reduced state providing a visual cue that the destination is interactive<br /></span></li><li><span style="white-space:pre-wrap" id="isPasted">When clicked (in both active and inactive states), a ripple passes through the indicator<br /></span></li><li><span style="white-space:pre-wrap" id="isPasted">The icon switches from outlined to filled<br /></span></li><li><span style="white-space:pre-wrap" id="isPasted">The icon changes color, becoming darker</span></li></ul>

On a navigation bar, the hover and click interactions on the Home and Explore icons have different interaction feedback.

<p><span style="white-space:pre-wrap">Cursor: Hover, Click</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7paj7kh-GM3_Expressive_Accessibility_NavBar_a11y_02_V04.mp4?alt=media

<h3>Text scaling and truncation</h3><p id="isPasted">When someone sets their device to show a larger text size, the navigation bar should grow vertically to accommodate larger labels while retaining the default padding. It’s okay for scaled text to wrap in navigation items.</p><p>To remain accessible, ensure the full label is always visible on-screen at up to 2x text sizing. Beyond this size, text can truncate. </p>

Nav bar with text scaled to 1.5x size. Some labels are on two lines, others are on one line.

<p>Text scaled to 1.5 size</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2kua3ge-03.png?alt=media

Nav bar with text scaled to 2x size. Some labels wrap to two lines.

<p>Text scaled to 2x size</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2kuaeol-04.png?alt=media

<h2>Initial focus</h2>

<p>Initial focus lands directly on the first navigation item, since that is the first interactive element of the component.</p>

Focus order and keyboard navigation of a nav bar.

<p><span style="white-space:pre-wrap">Focus lands on first navigation item</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fr7kb3-03.png?alt=media

Activating a nav item with space on a keyboard.

<p><span style="white-space:pre-wrap">The navigation item is selected with Space/Enter</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fr7nd7-04.png?alt=media

<h2 id="isPasted">Visual indicators</h2>

<p>Use a filled icon with a bold label for selected destinations. For unselected destinations use an outlined icon with a medium label.<br /><br />If an icon doesn’t have a filled style, use a thicker or heavier version of the icon instead.</p>

A nav bar with a filled icon for the selected nav item.

<p><span style="white-space:pre-wrap">Use a filled icon for the selected navigation destination to differentiate from the other destinations</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fr7qqu-05.png?alt=media

A nav bar with an outlined icon for the selected nav item.

<p><span style="white-space:pre-wrap">Don’t use outlined icons on selected nav items</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fr7ugl-06.png?alt=media

2 nav items, one selected, one unselected.

<p><span style="white-space:pre-wrap">When selected, the icon fills, darkens, and is backed by an active indicator shape</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fr7yfn-07.png?alt=media

<h2>Keyboard navigation</h2><div class="table-wrapper"><table style="width:100%"><tbody><tr><th>Keys</th><td>Actions</td></tr><tr><th>Tab</th><td><span style="white-space:pre-wrap" id="isPasted">Move between navigation items</span></td></tr><tr><th>Space / Enter</th><td><span style="white-space:pre-wrap" id="isPasted">Selects the focused navigation item</span></td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<p><span style="white-space:pre-wrap" id="isPasted">The accessibility label for a navigation item is typically the same as the destination name.<br /></span></p>

Accessibility label and role defined for a Home icon on a navigation bar.

<p><span style="white-space:pre-wrap">A navigation bar’s accessibility label can incorporate its adjacent UI text</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fr861i-08.png?alt=media

<p>When the visible UI text is ambiguous, accessibility labels need to be more descriptive. For example, a navigation destination visibly labeled <strong>Library </strong>would benefit from additional information in its accessibility label to clarify the destination’s intent.<br /><br />Note: On Android Views (MDC-Android), a more descriptive accessibility label is not available and the role is not announced.</p>

Accessibility labels of a navigation bar.

<p><span style="white-space:pre-wrap">While the visible label text reads <strong>Library</strong>, the accessibility label for this destination clarifies its function: <strong>Music library</strong></span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fr8a8y-09.png?alt=media
