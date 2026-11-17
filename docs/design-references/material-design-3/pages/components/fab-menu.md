# FAB menu

Source: https://m3.material.io/components/fab-menu
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/f00af5db-3477-49da-bae5-44b90b3dd7ba.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li id="isPasted">Opens from a <app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/m3/pages/fab/overview" should-open-link-in-new-tab="true">FAB</app-froala-tooltip-element> to show 2–6 related actions floating on screen</li><li>One FAB menu size for all sizes of FABs</li><li>Not used with <app-froala-tooltip-element description="Extended floating action buttons (extended FABs) help people take primary actions." link-label="More on extended FABs" link-url="/m3/pages/extended-fab/overview" should-open-link-in-new-tab="true">extended FABs</app-froala-tooltip-element></li><li>Available in primary, secondary, and tertiary color sets</li></ul>

3 FAB menus in different color schemes.

<p>The FAB menu comes in three color sets: primary, secondary, tertiary</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0aj37mw-01.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/7851d4a3eb38c46d

libraryModuleType: STATUS_TABLE

<h2>M3 Expressive update</h2>

<p><strong id="isPasted">May 2025</strong></p><p>The FAB menu adds more options to the FAB. It should replace the speed dial and any usage of stacked small FABs. <a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank" rel="noopener noreferrer">More on M3 Expressive</a></p>

<p><span style="white-space:pre-wrap" id="isPasted">New component added to catalog</span>:</p><ul><li>One menu size that pairs with any FAB</li><li>Replaces any usage of stacked small FABs</li></ul><p>Color:</p><ul><li>Contrasting close button and item colors</li><li>Supports dynamic color</li><li>Compatible with any FAB color style</li></ul>

4 screens. The FAB menu is on the first, and 3 FABs of different sizes are on the others.

<p>The FAB menu uses contrasting color and large items to focus attention. It can open from any size FAB.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0aj3ip6-02.png?alt=media

<h2>Differences from M2</h2>

M2 speed dial.

<p>M2: The speed dial used small round FABs</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0aj3w24-Diff%20GM2.png?alt=media

GM3 FAB menu.

<p><span style="white-space:pre-wrap">M3: The FAB menu uses dynamic color and a larger item size</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0aj42vs-Diff%20GM3%20Expressive.png?alt=media

## Specs

<h2>Variants</h2>

The FAB menu in its single variant.

<p>There’s one variant of FAB menu</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3q0apv-01-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/aEJrDU0HXKoBxMGFWOq1I7O6QB2fl6EPJGEDSP0L7CVDgvAjMdaM_LX10txGb1GDquvp0R-IiszOHSY23xw1qRcCit1YcAxSgB4P3HKa4wGs=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:23.1076%"><p>Variant</p></th><th style="width:43.5291%;text-align:center"><p> M3</p></th><th style="text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td><p>FAB menu</p></td><td><p>--</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Configurations</h2>

3 color configurations of FAB menus.

<p>Three color sets:</p><ol class="decimal"><li><p>Primary</p></li><li><p>Secondary</p></li><li><p>Tertiary</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3q1bvc-02-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ysJ9Ea896_EYwed_YofScZMv_HuE8BH4IJVkWyw4v2Xw-KInaEtXmOyWaaQNTTAZw0oLB9neXbgOnHTv2rPWRCii81v_hwh0ZkDiyQp2seY=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:16.3642%"><p>Category</p></th><th style="width:21.8155%"><p>Configuration</p></th><th style="width:31.7729%;text-align:center"><p> M3</p></th><th style="width:30.0976%;text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td><p>Color</p></td><td><p>Primary set, secondary set, tertiary set</p></td><td><p>--</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Tokens &amp; specs</h2>

<p>Use the table's menu to switch token sets. The FAB menu has a common token set and six color sets, three for each element (close button and menu item). <a href="/m3/pages/design-tokens/overview/" target="_blank" rel="noopener noreferrer">Learn about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/1a076cec8bc202c2

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['FAB menu - Common', 'FAB menu close button - Color - Primary', 'FAB menu close button - Color - Secondary', 'FAB menu close button - Color - Tertiary', 'FAB menu list items - Color - Primary', 'FAB menu list items - Color - Secondary', 'FAB menu list items - Color - Tertiary'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['FAB menu - Common', 'FAB menu close button - Color - Primary', 'FAB menu close button - Color - Secondary', 'FAB menu close button - Color - Tertiary', 'FAB menu list items - Color - Primary', 'FAB menu list items - Color - Secondary', 'FAB menu list items - Color - Tertiary'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Anatomy</h2>

2 elements of a FAB menu.

<ol class="decimal"><li id="isPasted">Close button</li><li>Menu item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3q41o4-03-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/CsC2u7L3QL6svcrFzmZM2foCzJxzUjF93lwZuZ-oJW7RK-lKsp4Ei0iNdLiNhbFST2y9U34PClKaRDJVJK8dT582gl98nYYhiCGKAwXNSKO6=s2048

5 FAB menus showing the range of 2–6 items.

<p>The FAB menu can have up to six items</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3q4pvy-04-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/KIWWfbv6JG0LIK8rzUSHcalH5BrNbW8_o8_U3uLqVkUDcdZNw4VS_nwoQ33DaomQXt95s6R_EY49aEQsWTQhxxDn2aYrDvU4ZSv4_arxasPc=s2048

<h2>Color</h2><p>Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview">Learn more about design tokens</a></p>

12 colors of the FAB menu.

<ol class="decimal"><li id="isPasted">On primary container</li><li>Primary container</li><li>On primary</li><li>Primary</li><li>On secondary container</li><li>Secondary container</li><li>On secondary</li><li>Secondary</li><li>On tertiary container</li><li>Tertiary container</li><li>On tertiary</li><li>Tertiary</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3q6ipd-05-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/tZxH6WCjbJBIqPlpd4_nt_npacUlh9WWyrIqJWs6Z1BCdGKbGFPt_BaW0CrG9HHNVQzBFYxxGU4hYm8LnEeWldCP9dezTNn3BwRy0uvJR2FoEw=s2048

<h2>States</h2><p>States are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states">Learn more about interaction states</a></p>

<h3>Close button</h3>

4 states of the FAB menu close button.

<p>Close button states in light and dark themes: </p><ol class="decimal"><li><p>Enabled</p></li><li><p>Hovered</p></li><li><p>Focused</p></li><li><p>Pressed</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3q7h0v-06-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/IBxWcDPavbWf55MsedxQZnCouJM3OZfbOudsfZQNrILcXhsyU_EI9iIEZ1UeKo-BwB7btsT0_0ZApQFHjZA4TOMjuOaY7TDtozX-qV09ssI=s2048

<h3>Menu item</h3>

4 states of the FAB menu items.

<p>Menu item states in light and dark themes:</p><ol class="decimal"><li><p>Enabled</p></li><li><p>Hovered</p></li><li><p>Focused</p></li><li><p>Pressed</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3q8bqk-07-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/GHST3WLAtYjpsKWjXfoTtSy1pybwjIFPYgrw1GBjynLRHHSxmZWT-t8VhnSMGbOvYWG0O65po5ceeOVrqt5KKtMzyxazm1PLFiTj4KMgg-CB=s2048

<h2>Measurements</h2>

<p>FAB menu items share the same measurements as the medium <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">button</app-froala-tooltip-element> specs. </p><p>The close button should always be 56dp.</p>

FAB menu size measurements.

<p>FAB menu size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3qcpur-08-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/6K5OibGh_d83LTRduhambKrHPD8JMVCHm19eHlen8e58fVWnoLyh8wWGZyLrdCPSO8Q3m01icndNcp7uuA0LLzeHzKWk60mGzGS3wrlB78o=s1352

<p>The FAB menu animates from the top trailing edge of the FAB to ensure a smooth animation.</p>

FAB on a mobile screen with 16dp margins annotated.

<p>The FAB should always have 16dp margins</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3qf9rm-08-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/WhBYTHZseZ9EfjdiU3CqPLeEC36wFENc3fV_9h5eR9T5ze6ooQya6w3-f1JWj7bBOkJnQHFL3LpbcmG_N1zDZC9RT3dkok2EOHrbxNP5-rQ=s656

FAB menu opened from a FAB has matching margins of 16dp.

<p>The close button and FAB share the top trailing corner as an anchor and appear in the same place</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3qfqs9-10-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/HWYLNxfsd_aBEZRMazrMRxUthRgVqeA8_evmV1IZrkKg878uq7DK0dg5EZaR8q7n-QP_kLrEaYALuBpmKtQjnBiVXhjfz_1-yYZw-CG0MTQ=s656

<p>Larger FABs will place the FAB menu slightly higher, with larger margins underneath.</p>

Medium FAB on a mobile screen with 16dp margins annotated.

<p>The medium FAB placement has 16dp margins</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3qhher-11-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/gce3Kgv0OcZSOCiWq672oYOzAE9YJhGCC0oGLAcdxJ59BPnVhlV3HdjJPyrHiJy1LgUNnQkTKyOc9d6e2N7EL7hyrzOoMq8kRrAZwtFYUDJz=s656

FAB menu opened from the medium FAB has a 40dp margin from bottom of screen.

<p>The close button is placed higher to align with the top of the medium FAB</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3qhtwe-12-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/kfovl3xRwL77xd7_XYJlFsLMybMdv16Nd0U9T5f87iZTyW3lo8gU72nkr81ZLumjSbxXIYnkvJX7ea84B8WmUtmukv4fhG1Wppp4IGnOgENn=s656

<p> </p>

Large FAB on a mobile screen with 16dp margins annotated.

<p>The large FAB placement has 16dp margins</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3qj0c0-13-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/_9hh4PDq9vnfiJ2AAOX8VKeIFe9De47Av_acmKjjFbTkWQOGjZTLOqGY5cWqLsxkDLWjG4bgquVe81njJP9pL12nQlj_F7iNMl7KTugTGLWP=s656

FAB menu opened from the large FAB has a 56dp margin from bottom of screen.

<p>The close button is placed higher to align with the top of the large FAB</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma3qjff7-14-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/zGkr1v4xtHihId5hAGO-4ESfqwzsweXE2xqXba2w8m0zl9Hswn3RWimV53apAvslPo7y0G2yrUchBqCB8sR1_96IAzSaJyALM8gE8GshfO85=s656

<p>On web, the FAB menu opens from the FAB, and inherits its states and specs from the baseline <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview/" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element> component. </p><p>The gap between the FAB and menu can vary, but 4dp is recommended.</p>

FAB menu on web states and specifications.

<p>Spacing and interaction on FAB menu for web:</p><ol class="decimal"><li><p>Enabled</p></li><li><p>Hovered</p></li><li><p>Selected</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn7ox1xs-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/EvVSXxIPCIQmi5H_Tf238AlVWE4QCT1NNKDXE9IYMtRbF3FF7S-t0Y_sxaQ1dCGsRSQGM6EkWT2LI5yHx3lpiF-agl1JQ8D670U0NjvwG8Jd=s2048

## Guidelines

On a page of music albums, a FAB menu shows options to make a new playlist, collection, or station.

<p>Use the FAB menu to show multiple related actions in a prominent, expressive style</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0al2scq-01.png?alt=media

<h2>Usage</h2>

<p id="isPasted">A FAB menu opens from a FAB to show multiple related actions. It should always appear in the same place as the FAB that opened it.</p><p>This makes actions immediately accessible, and keeps the UI clean by concealing actions when they’re not needed.</p><p>Don’t open a FAB menu from an <app-froala-tooltip-element description="Extended floating action buttons (extended FABs) help people take primary actions." link-label="More on extended FABs" link-url="/m3/pages/extended-fab/overview" should-open-link-in-new-tab="true">extended FAB</app-froala-tooltip-element> or any other component.</p>

1 mobile screen with a FAB, 1 with a FAB menu. Both are right aligned.

<p>The FAB menu should always open from a FAB</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0al39xa-02.png?alt=media

<p>The FAB menu should be aligned to the trailing edge of the window. </p><p>In right-to-left (RTL) languages, this means the FAB and FAB menu should be aligned to the left edge, and the layout of elements should be mirrored.</p>

1 mobile screen with a FAB, 1 with a FAB menu. Both are left aligned and mirrored for a right-to-left language.

<p>In RTL languages, the FAB menu should be left-aligned with the icon and text placement mirrored</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0al3tfx-03.png?alt=media

<p class="placeholder--hidden">FAB menus can contain 2–6 items. These should be closely related under a single action, like <strong>Share</strong>. </p><p class="placeholder--hidden">Avoid grouping unrelated actions in the same FAB menu.</p>

A FAB menu with 5 options on a photo gallery UI.

<p>FAB menus can have 2-6 items</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0al46l0-04.png?alt=media

A FAB menu with 1 option on a photo gallery UI.

<p>Don’t use a FAB menu with one item</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0al4jux-05.png?alt=media

<p>When a FAB is paired with other components, like the <app-froala-tooltip-element description="Floating toolbars float on top of page content and can provide contextual, dynamic actions." link-label="More on toolbars" link-url="/m3/pages/toolbars/overview" should-open-link-in-new-tab="true">floating toolbar</app-froala-tooltip-element> or <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element>, don’t use the FAB menu. This prevents cognitive overload and interface clutter. </p>

A toolbar with a FAB directly next to it.

<p>FABs can be placed next to toolbars and other components</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0al73q3-06.png?alt=media

A toolbar with a FAB menu next to it.

<p>Don't use a FAB menu with a toolbar or navigation rail</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0al7run-07.png?alt=media

<h3>Color sets</h3><p>FAB menus have three color sets: primary, secondary, and tertiary. Use the color set that best matches the FAB color style.   </p><p>Use the primary FAB menu color set with the <strong>primary</strong> or <strong>primary container</strong> FAB color styles. </p>

A FAB menu using the primary color set. 

<p>A primary FAB is paired with a primary FAB menu</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0al91ki-08.png?alt=media

<p>Use the secondary FAB menu color set with the <strong>secondary</strong> or <strong>secondary container</strong> FAB color styles. </p>

A FAB menu using the secondary color set.

<p>A secondary FAB is paired with a secondary FAB menu</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0alljh0-09.png?alt=media

<p>Use the tertiary FAB menu color set with the <strong>tertiary</strong> or <strong>tertiary container</strong> FAB color styles. </p>

A FAB menu using the tertiary color set.

<p>A tertiary FAB is paired with a tertiary FAB menu</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0almfyg-10.png?alt=media

<h2>Anatomy</h2>

2 elements of a FAB menu.

<ol class="decimal"><li id="isPasted">Close button</li><li>List item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0alqq5m-11.png?alt=media

<p>FAB menu items should always have label text. The icons shouldn’t be removed since they make each item easy to identify. </p>

A FAB menu with 3 options for selecting Food, People, or Nature. There are no icons next to the text.

<p>Only remove the icon if necessary. The icon provides a differentiation between items.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0alqzgn-12.png?alt=media

A FAB menu with 3 options for selecting Food, People, or Nature. The options are only icons, no text.

<p>Don’t remove the label</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0feodak-13.png?alt=media

<p>The list item should always hug its contents and look consistent. Avoid truncating text or setting fixed widths. All FAB menu elements should be rounded.</p>

A FAB menu used out of the box with no configurations.

<p>Keep the padding between the container and icon, icon and text, and text and container consistent</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0alssof-14.png?alt=media

FAB menu items are equal width despite having different lengths of text.

<p>Don’t expand container sizes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0alt3lp-15.png?alt=media

FAB menu items are square instead of round.

<p>Don’t change FAB menu shapes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0altd3s-16.png?alt=media

<h2 id="isPasted">Adaptive layout</h2>

<p>The FAB menu can open from any sized <app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/m3/pages/fab/overview" should-open-link-in-new-tab="true">FAB</app-froala-tooltip-element>. Use with a FAB size suitable for the window size class. For example, larger FABs are recommended for larger windows.</p>

The same FAB menu used in medium and compact window sizes.

<p>The FAB menu works in any window size. Pair it with the FAB suitable for that window size.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc0tzxol-GM3_Expressive_FAB_Guidelines_FAB-Menu%20D_v01.mp4?alt=media

<p id="isPasted">The FAB menu should remain anchored to the same corner or edge regardless of window size. </p><p>In large and extra large windows, the FAB and FAB menu margins should increase from 16dp to 24dp.</p>

A FAB menu with 24dp margins from the edge of the window.

<p id="isPasted">On desktop, use larger FABs and margins</p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0alwg82-18.png?alt=media

<p>On web, the FAB menu uses a <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element> component for an experience that's consistent with other desktop apps.</p>

A FAB menu using menu component on web and traditional FAB menu on compact screen.

<p>The same FAB menu options on both large window (left) and an Android compact window (right)</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn7ozpxv-18%20-%20Web%20vs.%20Mobile%20-%203P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/JR39TV-vwPs6mYgmYNupLSLvGTNxo5S0wG8x-r0qVa89Q8qAGCVWxuhQLATpYedNHvIvXtfJrhfK7HIHn99Hr2LR1_hqchcKnNdofvRXj2lL=s2048

<h2>Behavior</h2>

<h3 class="placeholder--hidden">Appearing</h3><p id="isPasted">The FAB should transform into the close button of the FAB menu. The menu items should appear using the <a href="/m3/pages/motion-transitions/transition-patterns#e1c2a650-d7a4-4a6d-9025-e6b7845291ed" target="_blank" rel="noopener noreferrer">enter and exit</a> transition.</p><p>Originate the transition from one of the FAB's trailing corners, preferably the top-aligned corner.</p>

A FAB transforms into a FAB menu while anchoring the animation to the top right corner of the FAB.

<p>Animate FAB menus from the top-aligned corner of FABs</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm23g9t73-FAB-Menu-A-1.mp4?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">To ensure accessibility for keyboard users on the web, avoid positioning the FAB menu to completely obscure the focus indicator of an actionable element. <br /><br />Partially covering the desired element is fine, as long as the focus indicator is visible.</span></p>

FAB menu doesn’t obscure actionable element and its focus indicator.

<p>Ensure the actionable element and its focus indicator are visible behind the FAB menu</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4hkgdmm-21.png?alt=media

FAB menu obscures both an actionable element and its focus indicator.

<p><span style="white-space:pre-wrap">Don’t block an actionable element and its focus indicator completely with the FAB menu</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4hkgqnr-22.png?alt=media

<h3>Scrolling</h3><p>When window height is limited, like when viewing phones in horizontal orientation, FAB menu items can scroll. </p><p>The items should scroll behind the close button.</p>

A FAB menu with 6 items scrolls off screen on a horizontal-oriented device. Scrolled items move behind the close button.

<p>FAB menus can scroll if the window height is too short to contain all the options</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fevuhp-FAB-Menu-B.mp4?alt=media

<h3>Expanding</h3><p>Any FAB menu item can expand and adapt to any shape using a <a href="/m3/pages/motion-transitions/transition-patterns#b67cba74-6240-4663-a423-d537b6d21187" target="_blank" rel="noopener noreferrer">container transform</a> transition pattern. This includes a surface that is part of the app structure, or a surface that spans the entire screen.</p>

A FAB menu item expands and transforms into a full screen dialog.

<p>FAB menu items can transition into any kind of shape when selected</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0few8ot-FAB-Menu-C.mp4?alt=media

## Accessibility

<h2 id="isPasted">Use cases</h2>

<p id="isPasted">People should be able to do the following using assistive technology:</p><ul><li>Navigate and interact with the FAB menu</li><li>Ensure focus is correct when navigating through the menu</li></ul>

<h2 id="isPasted">Interaction &amp; style</h2>

<p class="placeholder--hidden">FAB menu elements meet the minimum target size of 48dp.</p>

FAB menu measurement annotations. All elements are larger than the minimum target size.

<p>FAB menus have 48x48dp minimum width and sufficient spacing by default</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0am5xpn-01.png?alt=media

<p>When the FAB menu can scroll, make sure the items scroll behind the close button. </p><p>The close button should always be easy to access and unobstructed.</p>

FAB menu items are scrolling behind the close button.

<p>Allow the menu items to scroll behind the close button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0am8l9a-02.png?alt=media

FAB menu items are scrolling in front of the close button.

<p>Don’t obstruct the close button in short screens like horizontal orientation</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0am8ym2-03.png?alt=media

<h2>Initial focus</h2>

<p id="isPasted">When the FAB is selected, the FAB menu opens, and initial focus remains on the close button, which takes the place of the original FAB.</p><p>Then the focus moves from the top menu item to the bottom.</p>

4 FAB menus with the focus order labelled. Focus moves from the close button at the bottom to the topmost menu item next.

<p id="isPasted">Focus lands on the close button. People can then navigate through all the items.</p><ol class="decimal"><li>Close button</li><li>First menu item</li><li>Second menu item</li><li>Third menu item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmaejeaf9-04.png?alt=media

<h2>Keyboard navigation</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:19.6256%"><p><strong>Keys</strong></p></th><th style="width:80.2536%"><p><strong>Actions</strong></p></th></tr></thead><tbody><tr><td><p><strong>Tab</strong></p></td><td><p>Navigate to the next interactive element</p></td></tr><tr><td><p><strong>Space</strong> or <strong>Enter</strong></p></td><td><p>Activate the focused button or item</p></td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<h3>Android</h3><p>On Android, a FAB menu’s close button should include a state to tell screen readers what action will occur when it's toggled. The close button should be labeled: </p><ul><li><p>Label: Toggle menu</p></li><li><p>Role: Button</p></li><li><p>State: Expanded or collapsed</p></li></ul>

Accessibility labels for the close button on an Android device.

<p>On Android, the <strong>close button</strong> accessibility labels should include a toggle menu label, button role, and an expanded or collapsed state</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmmksaup-05.png?alt=media

<p>FAB menu items should be labeled:</p><ul><li><p>Label: Match the item’s UI text, such as <strong>Reply all </strong></p></li><li><p>Role: Button</p></li></ul>

Accessibility labels for a FAB menu item on an Android device.

<p>Label FAB menu items to match their UI text, like <strong>Reply all</strong>, and use the button role   </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmmksh30-06.png?alt=media

<h3>Web</h3><p>On web, a FAB menu is a combination of a <app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/m3/pages/fab/overview" should-open-link-in-new-tab="true">FAB</app-froala-tooltip-element> and a <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element> component. The FAB opens the menu. Follow the <a href="/m3/pages/fab/accessibility" target="_blank">accessibility guidelines for FABs</a> and <a href="/m3/pages/menus/accessibility" target="_blank">menus</a>.</p><p>The FAB's accessibility label should describe the menu that the FAB will open.</p>
