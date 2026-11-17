# Navigation drawer

Source: https://m3.material.io/components/navigation-drawer
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/d2a1a290-0db4-4622-8a4b-bd11b6a4ec8d.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">The navigation drawer is no longer recommended in the Material 3 Expressive update. For those who have updated, use an <a href="/m3/pages/navigation-rail/overview/" target="_blank">expanded navigation rail</a>, which has mostly the same functionality of the navigation drawer and adapts better across breakpoints.</div></div></div>

<ul type="disc" style="list-style-type:disc"><li><p>Use standard navigation drawers in <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded</app-froala-tooltip-element>, <app-froala-tooltip-element description="Window widths 1200dp to 1599dp, such as desktop." link-label="More on large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">large</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Window widths 1600dp and larger, such as ultra-wide monitors." link-label="More on extra-large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">extra-large breakpoints</app-froala-tooltip-element></p></li><li><p>Use modal navigation drawers in <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/google-material-3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium breakpoints</app-froala-tooltip-element> </p></li><li><p>Can be open or closed by default</p></li><li><p>Two variants: standard and modal</p></li><li><p>Put the most frequent destinations at the top and group related destinations together</p></li></ul>

2 variants of navigation drawers: standard and modal.

<ol><li>Standard navigation drawer</li><li>Modal navigation drawer</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoorr6v-1.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/5f54b6f53da7ecda

libraryModuleType: STATUS_TABLE

<h2>M3 Expressive update</h2>

<p><strong>May 2025</strong></p><p>The navigation drawer is no longer recommended. Use the <app-froala-tooltip-element description="Expanded navigation rails show text labels and an extended FAB, and can be default or modal." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">expanded navigation rail</app-froala-tooltip-element> instead. <a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank">More on M3 Expressive</a></p>

<h2>Differences from M2</h2>

<ul><li><p>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></p></li><li><p>Variants: Distinguishes two separate variants of navigation drawer: Standard and modal</p></li><li><p>Shape: Rounded corners at the ending edge of the drawer</p></li><li><p><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element>: Updated color and shape for indicating selected state</p></li></ul>

M2 navigation drawer with 4 destinations in a mail app. The active destination “Inbox” is rectangular.

<p>M2: Navigation drawer had square corners and a rectangular shape indicating the active destination</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fldox2g48-navdrawer_OLD_M2.png?alt=media

M3 navigation drawer with 4 destinations in a mail app. The active destination “Inbox” has rounded corners.

<p>M3: Navigation drawer has rounded corners, new color mappings, and an updated style for indicating the active destination</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzdbjtd0-4.png?alt=media

## Specs

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">The navigation drawer is no longer recommended in the Material 3 Expressive update. For those who have updated, use an <a href="/m3/pages/navigation-rail/overview/" target="_blank">expanded navigation rail</a>, which has mostly the same functionality of the navigation drawer and adapts better across breakpoints.</div></div></div>

Navigation drawer diagram numbering 7 elements

<ol class="decimal"><li><p>Container</p></li><li><p>Headline</p></li><li><p>Label text</p></li><li><p>Active indicator</p></li><li><p>Badge label text</p></li><li><p>Scrim</p></li><li><p>Icon</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmobm461s-1-3P-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/wzWoGqZcYHmlxmZaJ6h1mIIrnKAN6-ORvn-bAgZGnzVfSFw35XvFKnVMZ6aKAqVtw5sMblQfd0dN7cb5sOnknAbXZ47WMZnh8unDUHPqQQ6DfQ=s2048

<h2>Tokens &amp; specs</h2>

<p>The navigation drawer has one token set. <a href="/m3/pages/design-tokens/overview/" target="_blank">Learn about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/376969f91547be8e

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2 id="isPasted">Color</h2>

<p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p>

Navigation drawer diagram numbering 9 color roles.

<p id="isPasted">Navigation drawer color roles used for light and dark schemes:</p><ol><li>Surface container low</li><li>On surface variant</li><li>On secondary container</li><li>On secondary container</li><li>Secondary container</li><li>On secondary container</li><li>On surface variant</li><li>On surface variant</li><li>Scrim</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6b7pyr-2-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/EFOoVjwBffIgl-Gs07m2W5WiNu8brQ2paefKx_U_eQexLGySjgLV_C9FYD7wkTs0o7j3_RvrcTcqh6oUAKyyrkRsYKsU3A6n-KFtlCBp1sKv=s1352

<p>For divider color roles, go to <a href="/m3/pages/divider/specs" target="_blank">divider specs</a>.</p>

<h2>States</h2><p><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element> are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states/overview" target="_blank">Learn more about interaction states</a></p>

4 navigation drawers illustrating enabled, hovered, focused, and pressed states.

<p>Navigation drawer states: </p><ol><li>Enabled </li><li>Hovered </li><li>Focused </li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma77ejxi-3b-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/xCUslUMH4a9wLA0cXIbv622e8KMYHe0R5TPMmzjG0lFKP2hX6vjQcnKVFwxI9HIdk1z3y6BR65wFxvpsx4LcCDTCkHk0J52aaChbC8h3YEZy=s2048

<p><a href="/m3/pages/navigation-drawer/specs#6207b00f-a259-41d2-8146-b6efc6380976" target="_self">State specs are in the tokens module above</a></p>

<h2>Measurements</h2>

<h3>Standard navigation drawer</h3>

Standard navigation drawer with measurements shown for various elements.

<p>Element size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmobmv0i5-4-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/bHQAcDd4Vluh3tirhRwnej1hWyUij6O-bjAclp-H5fmSqLHDanyQZsk-RQCLJtCnVYQhYeN1DM4GQG4I2F_Lbk401GH877nVSeKUr3wvgiAv_w=s1004

Standard navigation drawer with measurements shown for padding and margins.

<p>Padding and margins</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6bb7nw-5-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/0b273CFdNyDt3yEDRLSSICnKHb8rktNAiXmruD2EO82_S9iBxGsq08CPpYTupKoj0SRnuaNR0fo8dICOcrrev88RLidMbVhYvVgiudX80RJ4=s1004

<div class="table-wrapper"><table style="margin-right:calc(0%);width:100%"><thead><tr><th style="width:47.3735%;text-align:center">Attribute</th><th style="width:52.5292%;text-align:center">Value</th></tr></thead><tbody><tr><th>Container height<br /></th><td>100%</td></tr><tr><th>Container width<br /></th><td>360dp</td></tr><tr><th>Container shape<br /></th><td>0,16,16,0dp corner radii</td></tr><tr><th>Icon size<br /></th><td>24dp</td></tr><tr><th>Active indicator height<br /></th><td>56dp</td></tr><tr><th>Active indicator shape<br /></th><td>28dp</td></tr><tr><th>Active indicator width<br /></th><td>336dp</td></tr><tr><th>Horizontal label alignment<br /></th><td>Start-aligned</td></tr><tr><th>Left padding<br /></th><td>28dp</td></tr><tr><th>Right padding<br /></th><td>28dp</td></tr><tr><th>Active indicator padding<br /></th><td>12dp</td></tr><tr><th>Padding between elements<br /></th><td>0dp</td></tr></tbody></table></div>

<h3>Modal navigation drawer</h3>

Modal navigation drawer with measurements shown for various elements.

<p>Element size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma775z3o-6-3p-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/invVA4iDTyiHnbFHAMhycwQRAZds3tEMmOOPGaiv1HnriGnDeAV4MSXpQ9gOcnALm0eQcxgml_hzP-tTo1gWH4DQMu-ZM0iPuy1OgHvjULc_=s1004

Modal navigation drawer with measurements shown for padding and margins.

<p>Padding and margins</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma7769l7-7-3p-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/2T9NqmBF4mES5SgaRMeuXBm0CXnjDhysHSNKT1lr_iIEUZKCbKtRtIXvzyFbVR8RnSZ17O4sK483ySXplBOwNiw0N_DoqjM0npsQ6uA6c9nnYA=s1004

<div class="table-wrapper"><table style="margin-right:calc(1%);width:99%"><thead><tr><th style="width:50.5055%;text-align:center">Attribute</th><th style="width:49.3962%;text-align:center">Value</th></tr></thead><tbody><tr><th>Container height<br /></th><td>100%</td></tr><tr><th>Container width<br /></th><td>360dp</td></tr><tr><th>Icon size<br /></th><td>24dp</td></tr><tr><th>Active indicator height<br /></th><td>56dp</td></tr><tr><th>Active indicator shape<br /></th><td>28dp</td></tr><tr><th>Active indicator width<br /></th><td>336dp</td></tr><tr><th>Horizontal label alignment<br /></th><td>Start-aligned</td></tr><tr><th>Left padding<br /></th><td>28dp</td></tr><tr><th>Right padding<br /></th><td>28dp</td></tr><tr><th>Active indicator padding<br /></th><td>12dp</td></tr><tr><th>Padding between elements<br /></th><td>0dp</td></tr></tbody></table></div>

## Guidelines

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">The navigation drawer is no longer recommended in the Material 3 Expressive update. For those who have updated, use an <a href="/m3/pages/navigation-rail/overview/" target="_blank">expanded navigation rail</a>, which has mostly the same functionality of the navigation drawer and adapts better across breakpoints.</div></div></div>

Navigation drawer with 4 primary destinations 

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwopun3e-1.png?alt=media

<h2>Usage</h2>

<p dir="ltr" id="isPasted">Navigation drawers provide access to destinations and app functionality, such as switching accounts. They can either be permanently on-screen or opened and closed by a navigation <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element> icon. One navigation destination is always active.</p><p dir="ltr">Navigation drawers are recommended for:</p><ul><li dir="ltr">Apps with 5 or more top-level destinations</li><li dir="ltr">Apps with 2 or more levels of navigation hierarchy</li><li dir="ltr">Quick navigation between unrelated destinations</li><li dir="ltr">Replacing the <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element> or <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element> on large screens</li></ul>

Navigation drawer with multiple destinations in a mail app.

Use a navigation drawer for 5 or more primary destinations, or more than 1 level of navigation hierarchy

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwopv1qw-2.png?alt=media

<p>Avoid using a navigation drawer with other primary navigation components, such as a navigation bar.</p><p>Instead, choose a single navigation component based on product requirements and breakpoints:</p><ul type="disc" style="list-style-type:disc"><li><p><app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">Navigation bars</app-froala-tooltip-element> for <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoints</app-froala-tooltip-element></p></li><li><p><app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">Navigation rails</app-froala-tooltip-element> for <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints</app-froala-tooltip-element> </p></li><li><p>Standard navigation drawers for expanded, <app-froala-tooltip-element description="Window widths 1200dp to 1599dp, such as desktop." link-label="More on large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">large</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths 1600dp and larger, such as ultra-wide monitors." link-label="More on extra-large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">extra-large</app-froala-tooltip-element> breakpoints</p></li></ul>

Standard navigation drawer and navigation bar used together.

<p>Avoid using two navigation components on the same screen</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwopvjco-3.png?alt=media

<p>There are two variants of navigation drawers:</p><ol class="decimal"><li><p>Standard navigation drawer</p></li><li><p>Modal navigation drawer</p></li></ol>

Standard navigation drawer with destinations in mail app.

<p>Standard navigation drawer</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwopw575-4.png?alt=media

Modal navigation drawer with destinations and scrim.

<p>Modal navigation drawer</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwopwhen-5.png?alt=media

<h3>Standard navigation drawer</h3>

<p>Standard navigation drawers provide access to drawer destinations and app content for <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/layout-overview/overview" should-open-link-in-new-tab="true">layouts</app-froala-tooltip-element> in <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded</app-froala-tooltip-element>, <app-froala-tooltip-element description="Window widths 1200dp to 1599dp, such as desktop." link-label="More on large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">large</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Window widths 1600dp and larger, such as ultra-wide monitors." link-label="More on extra-large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">extra-large</app-froala-tooltip-element> breakpoints. </p><p>Standard drawers can be permanently visible (best for frequently switching destinations) or opened and closed by tapping a <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element> icon (best for focusing more on screen content).</p><p>In <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoints</app-froala-tooltip-element>, use modal drawers instead.</p>

Standard navigation drawer in a mail app with active destination “Inbox” next to app content.

<p>Standard navigation drawer providing access to drawer destinations next to app content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwopx4a0-6.png?alt=media

<h3>Modal navigation drawer</h3>

<p>Modal navigation drawers use a scrim to block interaction with the rest of an app’s content, and don’t affect the screen’s <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/layout-overview/overview" should-open-link-in-new-tab="true">layout</app-froala-tooltip-element> grid.</p><p>Modal navigation drawers can be used in any breakpoint, but are primarily used in compact and medium sizes where space is limited or prioritized for app content.</p><p>They can be swapped with standard drawers on expanded, <app-froala-tooltip-element description="Window widths 1200dp to 1599dp, such as desktop." link-label="More on large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">large</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Window widths 1600dp and larger, such as ultra-wide monitors." link-label="More on extra-large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">extra-large</app-froala-tooltip-element> breakpoints. </p>

Modal navigation drawer with 1 active destination and scrim.

<p>Modal navigation drawer using a scrim to block interaction with the rest of an app’s content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwopxvvj-7.png?alt=media

<p dir="ltr" id="isPasted">Modal navigation drawers are always opened by an action outside of the drawer, such as clicking a navigation <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element> icon in a <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element>.</p><p dir="ltr">Modal drawers can be dismissed by:</p><ul><li dir="ltr">Selecting a drawer item</li><li dir="ltr">Tapping the scrim</li><li dir="ltr">Swiping toward the drawer’s anchoring edge (for example, swiping right-to-left for a left-aligned navigation drawer)</li></ul>

Diagram noting a navigation menu icon in a navigation rail.

<p>A modal drawer opened by an action such as clicking a navigation menu icon <span style="white-space:pre-wrap">(1)</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwopy7b1-8.png?alt=media

<p>Modal drawers can be dismissed by tapping the scrim or swiping the drawer toward its anchoring screen edge.</p>

2 modal navigations illustrating tapping the scrim or swiping to dismiss a modal drawer

<p><span style="white-space:pre-wrap" id="isPasted">1. Dismiss by tapping the scrim<br />2. Dismiss by swiping the drawer</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwopyjta-9.png?alt=media

<h2 id="isPasted">Anatomy</h2><p>Navigation drawers are essentially a <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> contained within a <app-froala-tooltip-element description="Side sheets show secondary content anchored to the side of the screen." link-label="More on side sheets" link-url="/m3/pages/side-sheets/overview" should-open-link-in-new-tab="true">side sheet</app-froala-tooltip-element>. They can also include headers, subheads, and <app-froala-tooltip-element description="Dividers are thin lines that group content in lists or other containers." link-label="More on dividers" link-url="/m3/pages/divider/overview" should-open-link-in-new-tab="true">dividers</app-froala-tooltip-element> to organize longer lists.</p>

Navigation drawer diagram numbering 8 elements.

<p>Navigation drawers can include headers, subheads, and dividers to organize longer lists</p><ol><li>Active Indicator</li><li>Icon</li><li>Label</li><li>Badge label</li><li>Sheet</li><li>Divider</li><li>Section label (optional)</li><li>Scrim</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwopzqbr-10.png?alt=media

<h3 dir="ltr" id="isPasted">Sheet</h3><p dir="ltr">A sheet holds all navigation drawer elements. <app-froala-tooltip-element description="Side sheets show secondary content anchored to the side of the screen." link-label="More on side sheets" link-url="/m3/pages/side-sheets/overview" should-open-link-in-new-tab="true">Side sheets</app-froala-tooltip-element> are used as the container for standard and modal navigation drawers.</p><p dir="ltr">Navigation drawers that open from the side are always placed on the start edge of the screen, on the left for left-to-right (LTR) languages, and on the right for right-to-left (RTL) languages.</p>

Modal navigation drawer opening from left side of screen.

<p>A navigation drawer opens from the left side of the screen for left-to-right languages</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq08ti-11.png?alt=media

<h3 dir="ltr" id="isPasted">Divider (optional)</h3><p dir="ltr"><app-froala-tooltip-element description="Dividers are thin lines that group content in lists or other containers." link-label="More on dividers" link-url="/m3/pages/divider/overview" should-open-link-in-new-tab="true">Dividers</app-froala-tooltip-element> can be used to separate groups of destinations within the navigation drawer.</p>

Navigation drawer using horizontal dividers to separate a group of destinations

<p>Use full-width dividers (1) to separate groups of destinations</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq1xf0-12.png?alt=media

Navigation drawer using horizontal dividers to separate individual destinations

<p>Don’t use dividers to separate individual destinations</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq29df-13.png?alt=media

<h3 dir="ltr" id="isPasted">Active indicator</h3><p dir="ltr">The active indicator is a background shape communicating which destination of the navigation drawer is currently being displayed.</p>

Navigation drawer diagram numbering 1 element.

<p>The active indicator (1) is a background shape communicating which destination of the navigation drawer is currently being displayed</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq2qbs-14.png?alt=media

<h3 dir="ltr" id="isPasted">Label text and icons</h3><p dir="ltr">Destinations in a navigation drawer take the form of actionable <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> items. Each item describes its destination using label text and an optional icon.</p>

Navigation drawer diagram numbering 2 elements.

<p>Actionable list items in a navigation drawer describe each destination using (1) an optional icon and (2) required label text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq358i-15.png?alt=media

<p dir="ltr" id="isPasted">Label text should be clear and short enough that it isn’t cut off by the sheet.</p>

Navigation drawer using only label text for 4 destinations. Label text “Inbox” in active destination.

<p>Navigation drawers can use text labels without icons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq3i6v-16.png?alt=media

Navigation drawer with 1 truncated text label.

<p>Keep text labels concise, but truncate them if they extend beyond the container width</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq4gjj-17.png?alt=media

Navigation drawer with 1 text label with wrapped label text.

<p>Don’t wrap label text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq4tkk-18.png?alt=media

Navigation drawer with 1 text label featuring smaller text.

<p>Don’t shrink text size in order to fit a text label on a single line</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq56gb-19.png?alt=media

<p>Icons can supplement labels as indicators of a destination. When used, they should always be placed before text. Other app components and content should reference these icons.</p>

Navigation drawer with active destination “Inbox” featuring recognizable icon.

<p>Use recognizable icons when conventions exist</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq67nf-20.png?alt=media

Navigation drawer with 4 destinations, 2 with text label and icon, 2 with only text label.

<p>Don’t apply icons to some destinations and not others. Icons should be used for all destinations, or none.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq6mto-21.png?alt=media

<h3 dir="ltr" id="isPasted">Section label (optional)</h3><p dir="ltr">Short subhead section labels can help group related destinations in the navigation drawer.</p>

Navigation drawer showing subhead section labels.

Related destinations can be grouped using short subhead section labels in the navigation drawer

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq710s-22.png?alt=media

<h3 dir="ltr" id="isPasted">Scrim (modal only)</h3><p dir="ltr">Modal navigation drawers use a scrim to block interaction with the rest of the app. The scrim is placed directly behind the drawer’s sheet and can be tapped or clicked to dismiss the drawer.</p>

Modal navigation drawer with scrim placed behind.

<p>Scrim applied behind a modal navigation drawer</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq7esu-23.png?alt=media

<h2>Responsive layout</h2>

<p>A product’s navigation component should change to suit the <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoint</app-froala-tooltip-element> and form factor of the screen.</p><p>Modal navigation drawers can be used at any breakpoint but are most common in <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium breakpoints</app-froala-tooltip-element>.</p><p>Standard navigation drawers are best for <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded</app-froala-tooltip-element>, <app-froala-tooltip-element description="Window widths 1200dp to 1599dp, such as desktop." link-label="More on large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">large</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Window widths 1600dp and larger, such as ultra-wide monitors." link-label="More on extra-large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">extra-large</app-froala-tooltip-element> breakpoints. </p><p>Use a transition when swapping components. For example, when switching from a portrait to landscape <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/layout-overview/overview" should-open-link-in-new-tab="true">layout</app-froala-tooltip-element>, the <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element> should transform into a navigation drawer.</p>

Navigation rail changing to navigation. drawer on a larger screen

<p>Standard navigation drawers change size to suit the device’s screen</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq7wck-24.png?alt=media

<h3>Compact breakpoint</h3><p>Use modal navigation drawers in <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoints</app-froala-tooltip-element>. Or swap the drawer for a navigation bar.</p><p>On web, when the screen size is smaller than 320 <app-froala-tooltip-element description="CSS pixels are the most common unit of measurement when developing for the web." link-label="More on CSS pixels" link-url="https://www.w3.org/Style/Examples/007/units.en.html" should-open-link-in-new-tab="true">CSS pixels</app-froala-tooltip-element>, swap the navigation drawer for a navigation bar to ensure <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview/principles" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element>.</p>

Modal navigation drawer with 1 active destination.

<p>Use a modal navigation drawer on mobile screens</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoq8evf-25.png?alt=media

<h3>Medium &amp; expanded breakpoints</h3><p>Use a modal navigation drawer alone or with a navigation rail on <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded</app-froala-tooltip-element> breakpoints.</p><p>When a <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element> and modal navigation drawer are used together, the drawer can repeat destinations in the navigation rail as long as the drawer offers enough visual separation between levels of the navigation hierarchy.</p><p>A standard navigation drawer can be used in <a href="/m3/pages/understanding-layout/parts-of-layout" target="_blank">single pane layouts</a> in expanded breakpoints. </p><p></p>

Navigation drawer on tablet with 1 active destination.

<p>Use a navigation rail on tablet screens, or also allow a drawer to open and close via a menu icon</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoqh0d1-GM3-Components-NavDrawer-Guidelines-1-v01.mp4?alt=media

<h3>Large and extra-large breakpoints</h3><p>For web experiences on laptop and desktop devices, use either a standard navigation drawer, or a <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element> that transitions into a modal navigation drawer.<br /><br /></p><p></p>

Navigation drawer showing 1 active destination.

<p>Use a standard navigation drawer on large and desktop screens</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx54v3bi-27.png?alt=media

<h2>Behavior</h2>

<h3 class="normal" dir="ltr" id="isPasted">Scrolling</h3><p class="normal" dir="ltr">Navigation drawers can be vertically scrolled, independent of the rest of the screen’s content and UI. If the <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> of navigation destinations is longer than the height of the drawer, the drawer’s contents can be scrolled within the drawer.</p>

A navigation drawer on the left region of an email app is scrolled vertically without disturbing the rest of the content.

<p><span style="white-space:pre-wrap">When a navigation drawer is scrolled, the body content should remain stationary</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoqihhy-GM3-Components-NavDrawer-Guidelines-2-v01.mp4?alt=media

<h3>Visibility</h3><p><strong>Dismissible standard drawers</strong> can be used for <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/layout-overview/overview" should-open-link-in-new-tab="true">layouts</app-froala-tooltip-element> that prioritize content (such as a photo gallery) or for apps where users are unlikely to switch destinations often. They should use a visible navigation <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element> icon to open and close the drawer.</p>

Side-by-side standard navigation drawer opened and then closed after tapping menu bar.

<p>A standard dismissible navigation drawer is opened and closed by tapping the navigation menu icon in the app bar (1), and remains open until the menu icon is tapped again (2)</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoqb1nm-27.png?alt=media

<p><strong id="isPasted">Permanently visible standard drawers</strong> allow quick navigation between unrelated destinations. They can’t be closed or dismissed by the user.</p>

Standard navigation drawer moving between destinations.

<p>A permanently-visible standard navigation drawer on desktop</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoqf0gp-28.png?alt=media

<h3 id="isPasted">Appearing</h3><p>When a navigation drawer animates on screen, it uses an <a href="/m3/pages/motion-transitions" rel="noopener noreferrer" target="_blank">enter and exit</a> transition pattern.</p>

In an email app, navigation drawer opens on menu icon click, and closes on outside click.

<p>A navigation drawer animating on screen</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoqk3j4-GM3-Components-NavDrawer-Guidelines-3-v01.mp4?alt=media

## Accessibility

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">The navigation drawer is no longer recommended in the Material 3 Expressive update. For those who have updated, use an <a href="/m3/pages/navigation-rail/overview/" target="_blank">expanded navigation rail</a>, which has mostly the same functionality of the navigation drawer and adapts better across window size classes.</div></div></div>

<h2 id="isPasted"><span style="white-space:pre-wrap">Use cases</span></h2>

<p><span style="white-space:pre-wrap">Users should be able to: </span></p><ul><li><span style="white-space:pre-wrap">Move between navigation destinations with assistive technology</span></li><li><span style="white-space:pre-wrap">Select a particular navigation destination from a set</span></li><li>Get appropriate feedback based on <app-froala-tooltip-element description="Device inputs provide interactive control of an app. Common inputs include a mouse, keyboard, and touchpad." link-label="More on inputs" link-url="/m3/pages/inputs" should-open-link-in-new-tab="true">input</app-froala-tooltip-element> type</li></ul>

<h2><span style="white-space:pre-wrap">Interaction &amp; style</span></h2>

<p><span style="white-space:pre-wrap"><strong>Touch</strong></span></p><ul><li><span style="white-space:pre-wrap">When a navigation item is tapped, the active indicator appears in place, providing feedback to the user that it is selected</span></li><li><span style="white-space:pre-wrap">A touch ripple passes through the indicator</span></li><li><span style="white-space:pre-wrap">The icon switches from outlined to filled</span></li><li><span style="white-space:pre-wrap">The icon changes color, becoming darker</span></li></ul>

Active indicator and other visual cues appear when nav drawers are tapped.

<p>Touch: Tap</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoqqvsf-GM3-Components-NavDrawer-Accessibility-1-v01.mp4?alt=media

<p><span style="white-space:pre-wrap"><strong>Cursor</strong></span></p><ul><li>When hovered, the <app-froala-tooltip-element description="A hover state communicates when a user has placed a cursor above an interactive element." link-label="More on hover state" link-url="/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844" should-open-link-in-new-tab="true">hover</app-froala-tooltip-element> indicator appears providing a visual cue that the destination is interactive</li><li>When clicked, a ripple passes through the indicator</li><li>The icon switches from outlined to filled</li><li>The icon changes color, becoming darker in light theme and lighter in dark theme, to increase the contrast</li></ul>

When a cursor goes over a navigation drawer, a hover indicator appears. When tapped, the active indicator appears.

<p>Cursor: Hover, Click</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoqr8nd-GM3-Components-NavDrawer-Accessibility-2-v01.mp4?alt=media

<h2><span style="white-space:pre-wrap">Initial focus</span></h2>

<p><span style="white-space:pre-wrap">Initial focus lands directly on the first navigation item, since that is the first interactive element of the component.</span></p>

1. Tab lands on the first navigation item, Inbox. 2. Down arrow to get to the second navigation item, Outbox.

<p>Focus lands on first navigation item</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flworf9hl-3.png?alt=media

<h2>Closing</h2>

<p>The modal navigation drawer can be dismissed by selecting the scrim that covers the rest of the screen.</p>

A navigation drawer with a scrim covering the body content. A touch target is selecting the scrim.

<p>Select the scrim to close the navigation drawer</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm36co6ff-navdrawer-tablet-do-md.png?alt=media

<h2><span style="white-space:pre-wrap">Visual indicators</span></h2>

<p>Icons are the primary focus of the navigation and such give the dominant cue of its <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">state</app-froala-tooltip-element>. Use a filled icon for the selected destination to differentiate from the outlined icons of non-selected destinations.</p>

Space + enter is used to select the navigation item inbox.

<p>The navigation item is selected via <strong>Space</strong>/<strong>Enter</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flworgt4a-4.png?alt=media

A navigation drawer with the home destination using a filled icon.

<p>Use a filled icon for the selected navigation destination to differentiate from the other destinations</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flworfw7l-5.png?alt=media

A navigation drawer with the home destination using an outlined icon.

<p>Avoid keeping the icon style for the selected navigation destination the same as unselected destination's icons. This removes an important visual indicator of which destination is active.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flworg85u-6.png?alt=media

A selected home icon using a filled icon and active indicator and a unselected home icon using an outlined icon.

<p>When selected, the icon fills, darkens in light theme (or lightens in dark theme), and is backed by an active indicator shape</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flworh5ui-7.png?alt=media

<h2><span style="white-space:pre-wrap">Keyboard navigation</span></h2>

<div class="table-wrapper"><table style="width:100%" class="fr-table-selection-hover"><thead><tr><th style="width:26.45%"><strong>Keys</strong></th><th style="width:73.55%"><strong>Actions</strong></th></tr></thead><tbody><tr><th>Tab</th><td><span style="white-space:pre-wrap">Focus lands on the first navigation destination </span></td></tr><tr><th><span style="white-space:pre-wrap">Space or Enter</span></th><td>Selects the <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bfc1624f-6bcc-4306-b0c1-425e2d8a1bf9" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element> navigation destination, and focus moves to the newly opened section (if applicable)</td></tr><tr><th><span style="white-space:pre-wrap">Arrow</span></th><td><span style="white-space:pre-wrap">Navigate between destinations within the navigation drawer</span></td></tr></tbody></table></div>

<h2><span style="white-space:pre-wrap">Labeling elements</span></h2>

<p>The <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview/principles" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> label for a navigation item is typically the same as the destination name.<br /><br />If the UI text is correctly linked, assistive tech (such as a screenreader) will read the UI text followed by the component’s role.<br /><br />For Android Views (MDC-Android), a more descriptive accessibility label is not available to be set and the role is not announced.</p>

A navigation drawer item’s label text and accessibility label both read “photos.” The role is “tab.”

<p>A navigation drawer’s accessibility label can incorporate its adjacent UI text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flworho52-8.png?alt=media

<p>When the visible UI text is ambiguous, accessibility labels need to be more descriptive.<span style="white-space:pre-wrap"> For example, a navigation destination visibly labeled <strong>Recents</strong> would benefit from additional information in its accessibility label to clarify the destination’s intent.</span></p>

A navigation drawer item’s label text is “recents”, the accessibility label is “recent images.” The role is “tab.”

<p>While the visible label text reads <strong>Recents,</strong> the accessibility label for this destination clarifies its function: <strong>Recent images</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwori08q-9.png?alt=media
