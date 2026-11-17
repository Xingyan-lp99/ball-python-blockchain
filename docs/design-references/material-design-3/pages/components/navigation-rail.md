# Navigation rail

Source: https://m3.material.io/components/navigation-rail
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/98fe42bd-9bb1-4307-9e92-e61e57c3e9da.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Use navigation rails in medium, expanded, large, or extra-large window sizes</span></li><li id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Can contain 3-7 destinations plus an optional FAB</span></li><li id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Always put the rail in the same place, even on different screens of an app</span></li></ul>

Navigation rail with 4 destinations, 1 active, and FAB.

<p><span style="white-space:pre-wrap">Collapsed and expanded navigation rails can transition between each other on any device, including: </span></p><p><span style="white-space:pre-wrap">1. Large or medium window size classes like tablets<br />2. Compact window size classes like phones in portrait orientation</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmbs2h57x-GM3_Expressive_Nav-Rail_Overview_01_IA_v02.mp4?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/6073fa0062bb7074

libraryModuleType: STATUS_TABLE

<h2>M3 Expressive update</h2>

<p><strong>May 2025</strong></p><p>A <strong>collapsed</strong> and <strong>expanded</strong> navigation rail have been introduced to replace the baseline nav rail. The expanded nav rail is meant to replace the <app-froala-tooltip-element description="Navigation drawers let people switch between UI views on larger devices. In the expressive update, use an expanded navigation rail." link-label="More on navigation drawers" link-url="/m3/pages/navigation-drawer/overview" should-open-link-in-new-tab="true">navigation drawer</app-froala-tooltip-element>. <a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank">More on M3 Expressive</a></p>

<p>Variants and naming:</p><ul><li><p>The baseline <strong>navigation rail</strong> is no longer recommended</p></li><li><p>Added two wider navigation rails:</p><ul><li><p><strong>Collapsed:</strong> replaces baseline nav rail</p></li><li><p><strong>Expanded</strong>: replaces <app-froala-tooltip-element description="Navigation drawers let people switch between UI views on larger devices. In the expressive update, use an expanded navigation rail." link-label="More on navigation drawers" link-url="/m3/pages/navigation-drawer/overview" should-open-link-in-new-tab="true">navigation drawer</app-froala-tooltip-element></p></li></ul></li></ul><p>Configurations:</p><ul><li><p>Expanded rail modality:</p><ul><li><p>Non-modal</p></li><li><p>Modal</p></li></ul></li><li><p>Expanded behavior:</p><ul><li><p>Transition to collapsed navigation rail</p></li><li><p>Hide when collapsed</p></li></ul></li><li><p>Color:</p><ul><li><p>Active label on vertical items changed from <strong>on surface variant</strong> to <strong>secondary </strong></p></li></ul></li></ul>

A collapsed and expanded navigation rail.

<p><span style="white-space:pre-wrap">The collapsed and expanded navigation rails match visually and can transition into each other</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fsz2c4-2.png?alt=media

<h2>Differences from M2</h2>

<ul id="isPasted"><li id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Behavior: Predictive back interaction</span></li><li id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Color: New color mappings and compatibility with dynamic color</span></li><li id="isPasted"><span style="white-space:pre-wrap" id="isPasted">States: The active destination can be indicated with a pill shape in a contrasting color</span></li></ul>

M2 navigation rail with 1 colored and filled icon showing the active state and 3 inactive icons.

<p><span style="white-space:pre-wrap">M2: The navigation rail uses icon color, weight, and fill to communicate which destination is active</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0dtdapc-3.png?alt=media

M3 navigation rail with 1 icon surrounded by a pill shape in contrasting color to show the active state.

<p><span style="white-space:pre-wrap">M3: The navigation rail uses a pill-shaped active indicator to communicate which destination is active</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fszcgl-4.png?alt=media

## Specs

<h2>Variants</h2>

2 variants of navigation rails.

<ol class="decimal"><li><p>Collapsed navigation rail</p></li><li><p>Expanded navigation rail</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmal9f2lt-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/iQ9mPuq7sZfsnSF_EfYMxQdypYp9K_fDEGHm0-4zuKdHXU48Kf7zItSC0hxmu3QW_ugdX67kQeQlrkgs7GzF6Kpo1FFERw1SFlVd6DCQC5gm=s2048

<h3>Baseline variants</h3>

<p>The baseline navigation rail is no longer recommended, and should be replaced by the collapsed navigation rail. <a href="/m3/pages/navigation-rail/specs#d4d97764-20ec-496f-a6f3-0d423940ec5a" target="_self">View baseline tokens</a></p>

Baseline navigation rail.

<ol class="decimal"><li><p>The baseline navigation rail is no longer recommended</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkvenn9g-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/_GDghBF084KxFoboNpBiBukL7eC9btnn0Mb6Jk_768f3C75CzUZ_lS1sJyKteHLGeR2sa__sSE-baRgcdfAxgBR3jxoUV13DucOJj2FXrDM=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:33.2734%"><p>Variant</p></th><th style="width:33.3333%;text-align:center"><p>M3</p></th><th style="width:33.3333%;text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td><p>Collapsed navigation rail<br /></p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td><p>Expanded navigation rail <br /></p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td><p>Navigation rail (baseline)<br /></p></td><td><p>Available</p></td><td><p>Not recommended.</p><p>Use <strong>collapsed navigation rail</strong>.<br /></p></td></tr></tbody></table></div>

<h2>Configurations</h2>

Standard and modal layouts of navigation rail.

<ol class="decimal"><li><span style="white-space:pre-wrap">Expanded layout: standard</span></li><li><span style="white-space:pre-wrap">Expanded layout: modal</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmal9fbzs-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Q6opw4o2Z-4QOi0ydyk2R1MLywKayfVfAMWjKN6nvzz6OZzoJOGsl_BvoY_XaQp0dSV2iH4gwgEJ0tYqAXEKQKJy1Gko4-M5s1umRBx2MaHD=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Category</p></th><th style="text-align:center"><p>Configuration</p></th><th style="text-align:center"><p>M3</p></th><th style="text-align:center"><p>      M3 Expressive</p></th></tr></thead><tbody><tr><td rowspan="2" style="width:21.223%"><p>Expanded layout</p></td><td><p>Standard (default)</p></td><td><p>Available as <app-froala-tooltip-element description="Navigation drawers let people switch between UI views on larger devices. In the expressive update, use an expanded navigation rail." link-label="More on navigation drawers" link-url="/m3/pages/navigation-drawer/overview" should-open-link-in-new-tab="true">navigation drawer</app-froala-tooltip-element><br /></p></td><td><p>Available</p></td></tr><tr><td><p>Modal</p></td><td><p>Available as <app-froala-tooltip-element description="Navigation drawers let people switch between UI views on larger devices. In the expressive update, use an expanded navigation rail." link-label="More on navigation drawers" link-url="/m3/pages/navigation-drawer/overview" should-open-link-in-new-tab="true">navigation drawer</app-froala-tooltip-element><br /></p></td><td><p>Available</p></td></tr><tr><td><p>Expanded behavior</p></td><td><p>Hide when collapsed</p></td><td><p>--</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Tokens &amp; specs</h2>

<p>Browse the component elements, attributes, tokens, and their values. <a href="/m3/pages/design-tokens/overview/" target="_blank">Learn about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/5b55bd7cc1ea6e29

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Nav rail - Common', 'Nav rail - Collapsed', 'Nav rail - Expanded', 'Nav rail item - Common', 'Nav rail item - Vertical', 'Nav rail item - Horizontal'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['Navigation rail (baseline)', 'Nav rail - Common', 'Nav rail - Collapsed', 'Nav rail - Expanded', 'Nav rail item - Common', 'Nav rail item - Vertical', 'Nav rail item - Horizontal'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Anatomy</h2>

9 elements of collapsed and expanded navigation rails.

<p><span style="white-space:pre-wrap">Collapsed and expanded navigation rail elements:</span></p><ol class="decimal"><li><span style="white-space:pre-wrap">Container</span></li><li><span style="white-space:pre-wrap">Menu (optional)</span></li><li><span style="white-space:pre-wrap">FAB or Extended FAB (optional)</span></li><li><span style="white-space:pre-wrap">Icon</span></li><li><span style="white-space:pre-wrap">Active indicator</span></li><li><span style="white-space:pre-wrap">Label text</span></li><li><span style="white-space:pre-wrap">Large badge (optional)</span></li><li><span style="white-space:pre-wrap">Large badge label (optional)</span></li><li><span style="white-space:pre-wrap">Small badge (optional)</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg0uznol-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/zju3SaKNZtIg8oswdNqjqbU2pgzAazbfcyzRL_wo1UneMQSp9D6yIVFbPDeEtmh09MwYuYYHofz5j6DGbwBVO9cBdpqUxwJehXqI242Tz80bUg=s2048

<h2 id="isPasted">Color</h2><p><span style="white-space:pre-wrap" id="isPasted">Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens; in implementation, a color value will be a token that references a value. </span><span style="white-space:pre-wrap" id="isPasted"><a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></span></p>

Color roles of 9 elements of collapsed and expanded navigation rails in light and dark color schemes.

<p>Navigation rail color roles used for light and dark schemes:</p><ol class="decimal"><li><p>Surface container (optional)</p></li><li><p>On secondary container</p></li><li><p>Secondary container</p></li><li><p>Secondary (vertical), On secondary container (horizontal)</p></li><li><p>On surface variant</p></li><li><p>On surface variant</p></li><li><p>Error</p></li><li><p>On error</p></li><li><p>Error</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmyzgq71-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/d3PlE8MkpZrvAvwFNjnOiUQXi8R7ep0qmhurwSRvAq_yf3Eb44NIbzr78sGxD1gNgCLxhWdlVv_Mti8eRMPEi3Nn0WQRUnjZNO_XRFQt6Yan=s2048

<h2 id="isPasted">States</h2><p><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element> are visual representations used to communicate the status of a component or an interactive element.<span style="white-space:pre-wrap" id="isPasted"><br /><br />The navigation item’s target area always spans the full width of the nav rail, even if the item container hugs its contents.</span></p>

4 states of collapsed navigation rails.

<p></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmal9s5f0-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/1IxCo2XIMga54ROSNhrWET0gIRcndin6fwUN_DdJMu2VZ4PFpdW1-c-vio2nIOXxmj3p_tGkbBc1N0KGdzg6iuqMCS1_ZsgFG1FfzS6Fppk=s2048

4 states of expanded navigation rails.

<ol class="decimal"><li id="isPasted">Enabled</li><li>Hovered</li><li>Focused</li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmal9sbiq-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/uvOYTNSaWtfWdqdoR0tVR9eCjmd4f-AEfdMVEacZJc0VwURGK8_8FeAvzOY4Kr3sV9YzZfIF-gguMC8haBwaeJB7tgykjwBvSFhlQtuC4AzahA=s2048

<h2>Measurements</h2>

Padding and measurements for expanded and collapsed navigation rails.

<p>Navigation rail padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmal9t1mb-08-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/RTqY8bTqiMpwcsU_pJkWy9rMeFIjRoSs3m15t8w64kdPnvtTTTE6_Dklo68o5dm4vNj_CA14xM6FrVZkyBtYlf4hcPjBAMOTQ3rvBDY60BrmGw=s2048

<h2>Common layouts</h2>

4 common layouts of collapsed navigation rail.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmal9twwq-09-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Q7TK1on1e6Srj9rXvfTaKHDKgYKSh07xaPRGq0zatThZiQkiwf-UMR1-H60g1esYikZSHRedr3h-lkPoU4ICPljobiH8pOBRjSINWIs7ANcD=s2048

4 common layouts of expanded navigation rail.

<ol class="decimal"><li><span style="white-space:pre-wrap">Three navigation items </span></li><li><span style="white-space:pre-wrap">Three navigation items with a menu</span></li><li><span style="white-space:pre-wrap">Three navigation items with a FAB</span></li><li><span style="white-space:pre-wrap">Three navigation items with a menu and FAB</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmal9u2w3-10-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/z_uzDW3EjZiO_WRnWUJem6qKFygJFreR0EX_C_F4b4gyUdaq1KV9KFpJqgJpBWstqQ1O-CdNp0N6b7mAK8Xp6CkIKHupoRyeHFQkqfLEpnI=s2048

<hr /><p><br /></p>

<h2>Baseline navigation rail</h2>

8 elements of baseline navigation rail.

<ol class="decimal"><li><span style="white-space:pre-wrap">Container</span></li><li><span style="white-space:pre-wrap">Menu icon (optional)</span></li><li><span style="white-space:pre-wrap">Icon</span></li><li><span style="white-space:pre-wrap">Active indicator</span></li><li><span style="white-space:pre-wrap">Label text</span></li><li><span style="white-space:pre-wrap">Large badge label (optional)</span></li><li><span style="white-space:pre-wrap">Large badge (optional)</span></li><li><span style="white-space:pre-wrap">Badge (optional)</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmal9uv1q-11-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ADBFvMHXuRRv0_6Z-N3tRHlMrh88FQQszAdMrNhAM-p2IdU_v8QQRA0cezT6n2vPpVmhQ7R8saOYcTsI1okUonFMqT8GzmCfjymxB9hHPv8=s2048

<h3>Tokens &amp; specs</h3>

resourceName: designSystems/20543ce18892f7d9/components/5b55bd7cc1ea6e29

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Navigation rail (baseline)', 'Nav rail item - Horizontal', 'Nav rail item - Common', 'Nav rail - Common', 'Nav rail - Collapsed', 'Nav rail - Expanded', 'Nav rail item - Vertical'], 'tokenSetOrder': ['Navigation rail (baseline)', 'Nav rail item - Horizontal', 'Nav rail item - Common', 'Nav rail - Common', 'Nav rail - Collapsed', 'Nav rail - Expanded', 'Nav rail item - Vertical']}

<h3>Color</h3>

<p><span style="white-space:pre-wrap" id="isPasted">Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. </span><span style="white-space:pre-wrap" id="isPasted"><a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></span></p>

8 color roles of baseline navigation rail.

<p id="isPasted">Navigation rail color roles used for light and dark themes:</p><ol class="decimal"><li>On secondary container</li><li>Secondary container</li><li>On surface</li><li>On surface variant</li><li>On surface variant</li><li>Error</li><li>On error</li><li>Error</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmal9vzs8-12-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/bYdm_ngSm_bDBlh7cCiignDkbte5hHytBrpjYGp_9BfBLH1hF2zPxV-Oqdm6nn8fSHRROojsHBUwN5etdowcM8IHoq2XH1Qy7rRFtshsl5ca=s2048

<h3>States</h3>

<p><span style="white-space:pre-wrap" id="isPasted">States are visual representations used to communicate the status of a component or interactive element.</span></p>

8 states of baseline navigation rail.

<p><span style="white-space:pre-wrap">Navigation rail states:</span></p><ol class="decimal"><li><span style="white-space:pre-wrap">Enabled (on active destination)</span></li><li><span style="white-space:pre-wrap">Hovered (on active destination)</span></li><li><span style="white-space:pre-wrap">Focused (on active destination)</span></li><li><span style="white-space:pre-wrap">Pressed (on active destination)</span></li><li><span style="white-space:pre-wrap">Enabled (on inactive destination)</span></li><li><span style="white-space:pre-wrap">Hovered (on inactive destination)</span></li><li><span style="white-space:pre-wrap">Focused (on inactive destination)</span></li><li><span style="white-space:pre-wrap">Pressed (on inactive destination)</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmal9x9ol-13-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/q4Ce0kmHkUU63AUNns9xbrnQx2UlJBT9dfmW-RzlP1iM5biz8sOwR4G7BU8pEmGTbMSy2nnmyYzPFBNwQdyM6b8tJ20dhgkmDEF86WcUpVE=s2048

<h3>Measurements</h3>

Baseline nav rail size measurements.

<p><span style="white-space:pre-wrap">Navigation rail size measurements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmal9xiu7-14-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/PsBusqTr-OE5bCxYRV_i7_t-UpABd6wh-bbKu-mzMDv5-O3eoKvh-B144jLbqI5sf4B63G0hAv5k0m_hf7qTNA6ktxvfRVdk0cILpP3kghqk=s1004

Baseline nav rail padding and margin measurements.

<p><span style="white-space:pre-wrap">Navigation rail padding and margin measurements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmal9xyxt-15-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/HCDSa0-MhFtUTT-jj2x4OG8rghWPku3boxc3_KKZzParDgXb2n-nNyXxh-eq8DyOgLXlqmxFHoc2sShKRMWf8m2DKVLHdtpCfsY9_7GGTFA=s1004

<h3 id="isPasted">Configurations</h3><p><span style="white-space:pre-wrap" id="isPasted">Common arrangements of elements within a navigation rail.</span></p>

5 configurations of the baseline navigation rail.

<ol><li><span style="white-space:pre-wrap">With a menu</span></li><li><span style="white-space:pre-wrap">With a FAB</span></li><li><span style="white-space:pre-wrap">With menu and FAB, without labels</span></li><li><span style="white-space:pre-wrap">All destinations with text labels</span></li><li><span style="white-space:pre-wrap">With menu, FAB, and label text for all destinations</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmal9yote-16-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/0ArxFOIUj1oF4bmcdt98kcylfvstmfHlWXRI2sVpFC5UG246qn6yr4185ERKim5I5IYDjTqDnWX_fMqGE_nrXr_7dJj5H7sCznQWP5SfkX4h=s2274

## Guidelines

Colorful, purple navigation rail shown collapsed and expanded.

<p><span style="white-space:pre-wrap">Use the menu icon to transition between collapsed and expanded navigation rails</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fueyh1-01.png?alt=media

<h2 id="isPasted">Usage</h2>

<p>The navigation rail can display navigation items, a menu, and a <app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/m3/pages/fab/overview" should-open-link-in-new-tab="true">floating action button</app-froala-tooltip-element> (FAB) in a vertical orientation.</p><p>There are two variants of navigation rails, <strong>collapsed</strong> and <strong>expanded</strong>, which can easily transform into each other when the menu button is selected.</p><h3>Collapsed</h3><p>The <strong>collapsed</strong> nav rail runs along the leading edge of the window, and should contain 3–7 navigation items. It should not be hidden.</p><p>It can be used in <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> to <app-froala-tooltip-element description="Window widths 1600dp and larger, such as ultra-wide monitors." link-label="More on extra-large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">extra large breakpoints</app-froala-tooltip-element>, such as tablets and desktop. In  medium windows with few destinations, consider using a <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/google-material-3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element> instead. <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">Compact windows</app-froala-tooltip-element> should always use a navigation bar.</p>

Collapsed navigation rail with “timer” icon on FAB.

<p><span style="white-space:pre-wrap">A navigation rail should be the only visible navigation element</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmalbc2cg-02.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/2h46aO3pI3H6sk6nAElUSXgQFeS-w8ASJc8WcVkSbZ4bM8FJoTDWdNodAqWyROvWADumQNodvIQiUGDoBjq162uNRm52qDDoSVxUvoCDeNDx=s1352

<h3>Expanded</h3><p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">The <strong>expanded</strong> navigation rail can be standard or modal, and should always open from a menu icon. An expanded rail can reveal secondary destinations not visible when collapsed.<br /><br />The <strong>standard</strong> configuration is placed beside body content. It’s best for larger windows with lots of available space.<br /><br />The <strong>modal</strong> configuration overlaps the body content, and should be opened from a menu icon. Use the modal configuration for:</span></p><ul><li><span style="white-space:pre-wrap">Information dense layouts where space is limited</span></li><li><span style="white-space:pre-wrap">Products with many navigation items</span></li></ul>

Expanded navigation rail shown expanded by default and expanded over screen content.

<p><span style="white-space:pre-wrap">A navigation rail can be expanded by default on larger screen sizes, or can be expanded over content on smaller screen sizes</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fuf9qz-03.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">In immersive experiences, the expanded navigation rail can be hidden entirely, appearing only when the menu icon is selected.<br /><br />The collapsed navigation rail should not be hidden.</span></p>

Navigation rail and hidden navigation rail with menu icon button for expansion.

<p><span style="white-space:pre-wrap">The expanded navigation rail can also be hidden, appearing only when the menu icon is selected</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fufhuq-04.png?alt=media

<h2 id="isPasted">Anatomy</h2>

10 elements of expanded and collapsed navigation rails.

<ol><li><span style="white-space:pre-wrap">Container</span></li><li><span style="white-space:pre-wrap">Menu (optional)<br /></span></li><li><span style="white-space:pre-wrap">Floating action button (FAB) (optional)<br /></span></li><li><span style="white-space:pre-wrap">Icon - active<br /></span></li><li><span style="white-space:pre-wrap">Label text - active<br /></span></li><li><span style="white-space:pre-wrap">Active indicator<br /></span></li><li><span style="white-space:pre-wrap">Icon - inactive<br /></span></li><li><span style="white-space:pre-wrap">Large badge (optional)<br /></span></li><li><span style="white-space:pre-wrap">Large badge label<br /></span></li><li><span style="white-space:pre-wrap">Small badge<br /></span></li><li><span style="white-space:pre-wrap">Label text - inactive</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fug0sy-05.png?alt=media

<h3 dir="ltr" id="isPasted">Container</h3><p dir="ltr"><span style="white-space:pre-wrap" id="isPasted">The navigation rail should be placed on the leading edge of the window. This is the left side for left-to-right languages, and the right side for right-to-left languages.<br /><br />The container fill can be turned off so the nav rail appears directly on the surface. When doing this, make sure all items have a minimum of 3:1 color contrast.</span></p>

Right-to-left navigation rail in Hebrew, and left-to-right navigation rail in English.

<p><span style="white-space:pre-wrap">The navigation rail should be placed on the leading edge of the window</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fugb5b-06.png?alt=media

<p id="isPasted">The navigation rail should always run vertically along the side of a layout. Don’t make it horizontal.<br /><br />Use a <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element> for horizontal navigation.</p>

Horizontal navigation rail on timer screen.

<p><span style="white-space:pre-wrap">Don’t use the navigation rail horizontally. Use a navigation bar instead.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmacys6lz-07.png?alt=media

<p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Navigation rail items can be aligned as a group to the top or center of a layout. On tablets, use center alignment to make it easier to reach items.<br /><br />The menu icon and FAB should always be top-aligned.</span></p>

Navigation rails with different alignments.

<p><span style="white-space:pre-wrap">Top and center aligned rail destination placement</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fuh0i5-08.png?alt=media

<h3 dir="ltr" id="isPasted">Menu (optional)</h3><p dir="ltr"><span style="white-space:pre-wrap" id="isPasted">The menu button can transition between the <strong>collapsed </strong>and <strong>expanded</strong> navigation rails.<br /><br />Once expanded, the rail can reveal secondary destinations.<br /><br />When the navigation rail is expanded, the menu icon should change to represent that it can be collapsed.</span></p>

Expanded and collapsed navigation rails controlled by a menu icon button.

<p><span style="white-space:pre-wrap">A navigation rail can expand to reveal more destinations</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fuh7km-09.png?alt=media

<h3 dir="ltr" id="isPasted">Floating action button (FAB) (optional)</h3><p dir="ltr"><span style="white-space:pre-wrap" id="isPasted">The container of the navigation rail is ideal for anchoring the FAB to the top of a screen, placing the app’s key action above navigation destinations.<br /><br />When nested within another component, such as the navigation rail, the FAB's resting elevation should be </span><span style="white-space:pre-wrap" id="isPasted"><a href="/m3/pages/elevation/applying-elevation" target="_blank" rel="noopener noreferrer">level 0</a></span><span style="white-space:pre-wrap" id="isPasted">.</span></p>

Navigation rail with a FAB button at the top of the screen.

<p><span style="white-space:pre-wrap">A top-aligned FAB in the navigation rail</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmalbkctg-10.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/oYiKoFrv-NTEJMP1NoGGpnlw0RTHmfpGWDm7KmDgeKzvpXq6tMZvMjBzUcZkXpnEK2Lb_cbeWRkwS4i4RGn1zfW0N4RcwSGVgltbcvmD6vY=s656

Navigation rail with a FAB button at the bottom of the screen.

<p><span style="white-space:pre-wrap">Avoid placing the FAB below navigation items</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fuhrl8-11.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">The top of the rail can also be used for a logo, however avoid using logos that could be mistaken as buttons.<br /><br />Don’t use a logo as a menu button to expand the navigation rail.</span></p>

Navigation rail with Material design logo at the top of the screen.

<p><span style="white-space:pre-wrap">Use caution when placing logos in the rail where they might be confused with an action or destination</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fuhyto-12.png?alt=media

<h3 dir="ltr" id="isPasted">Active indicator</h3><p dir="ltr"><span style="white-space:pre-wrap" id="isPasted">The active indicator shows which page is being displayed.</span></p>

Navigation rail with active indicators present for the current screen.

<p><span style="white-space:pre-wrap">Use the active indicator only for the current open page</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fuicr9-13.png?alt=media

Navigation rail with active indicators present for all navigation items.

<p><span style="white-space:pre-wrap">Don’t use the active indicator for more than one navigation item at a time</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fujiob-14.png?alt=media

<p>The active indicator hugs the label text in the expanded nav rail. To achieve a similar style to the baseline <app-froala-tooltip-element description="Navigation drawers let people switch between UI views on larger devices. In the expressive update, use an expanded navigation rail." link-label="More on navigation drawers" link-url="/m3/pages/navigation-drawer/overview" should-open-link-in-new-tab="true">navigation drawer</app-froala-tooltip-element>, consider modifying the active indicator to fill the container.<br /><br />The target area should always span the full width.</p>

Navigation rail with active indicator that hugs the text and icon.

<p><span style="white-space:pre-wrap">The active indicator hugs contents in the expanded nav rail</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fujt7v-15.png?alt=media

Navigation rail with active indicator that is larger than the content within it.

<p>Override the indicator to fill the container to more closely resemble the baseline navigation drawer</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fujxyu-16.png?alt=media

<h3 dir="ltr" id="isPasted">Icons</h3><p dir="ltr"><span style="white-space:pre-wrap" id="isPasted">Navigation rail items must use icons that symbolize the content of their page. Browse popular icons on </span><span style="white-space:pre-wrap" id="isPasted"><a href="http://fonts.google.com/icons" target="_blank" rel="noopener noreferrer">Google Fonts</a></span><span style="white-space:pre-wrap" id="isPasted">.</span></p>

Navigation rail with icons that fit the destinations, like a timer icon and label leading to a timer feature.

<p><span style="white-space:pre-wrap">Icons should symbolize the content of the page they open</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fuk4ze-17.png?alt=media

<p dir="ltr" id="isPasted"><span style="white-space:pre-wrap" id="isPasted">When a destination is selected, the icon fills and changes color. An active indicator appears behind the icon.</span></p>

Icons with and without an active indicator.

<p><span style="white-space:pre-wrap">Selected navigation items have an active indicator, a filled icon, and a more prominent color</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fukavr-18.png?alt=media

<h3 dir="ltr" id="isPasted">Label text</h3><p dir="ltr"><span style="white-space:pre-wrap" id="isPasted">The label text should be a short, meaningful description of each navigation destination and another way for users to understand an icon’s meaning.<br /><br />All navigation items require a one word label text.</span></p>

Navigation rail with clear text labels.

<p><span style="white-space:pre-wrap">Write clear and concise labels that describe the destination page</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fukhnw-19.png?alt=media

<p dir="ltr" id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Avoid wrapping long labels when possible. If necessary, create a line break between words, or hyphenate longer words.</span></p>

Navigation rail with lengthy text labels.

<p><span style="white-space:pre-wrap">Break up longer phrases into two text lines if necessary</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fune8p-20.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">Labels should be short enough to not be truncated. Don’t shrink the type scale to fit longer text labels.</span></p>

Navigation rail with truncated text label with ellipses. 

<p><span style="white-space:pre-wrap">Don’t truncate or display an ellipsis in place of label text</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0funlrw-21.png?alt=media

Navigation rail with small text label.

<p><span style="white-space:pre-wrap">Don’t reduce the type size to fit more characters into a destination label</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0funqlw-22.png?alt=media

<h3 dir="ltr" id="isPasted">Badges</h3><p dir="ltr"><span style="white-space:pre-wrap" id="isPasted">Navigation rail icons can include badges to communicate dynamic information about the  destination, such as counts or status.<br /><br />In compact nav rails, the badge is placed in the upper right corner of the icon. In expanded nav rails, the badge should be placed next to the label text.<br /><br /></span></p>

Navigation rail with badges on each icon.

<p><span style="white-space:pre-wrap">1. Small badge on a rail destination <br />2. Large badge with a number<br />3. Large badge with a maximum character count</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fuomdi-23.png?alt=media

<h3 dir="ltr" id="isPasted">Divider (optional)</h3><p dir="ltr"><span style="white-space:pre-wrap" id="isPasted">A vertical divider can help separate the rail from app content. The divider should be positioned on the edge of the rail container that’s adjacent to the app’s content area.</span></p>

Navigation rail with divider separating it from screen content.

<p><span style="white-space:pre-wrap">A divider can make the navigation rail container distinct from other on-screen content</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fuouq0-24.png?alt=media

<h2>Placement</h2>

<p dir="ltr">In adaptive layouts, the navigation rail should be placed outside any <app-froala-tooltip-element description="Panes are layout containers that house other components and elements within a single app. A pane can be: fixed, flexible, floating, or semi permanent." link-label="More on panes" link-url="/m3/pages/understanding-layout/parts-of-layout#73de653a-fc57-4a7c-bc3b-5b9e94207de8" should-open-link-in-new-tab="true">panes</app-froala-tooltip-element>, always along the leading edge of the window. Don’t place it within body content.<br /><br />When the navigation rail is hidden, the body content can fill in the remaining space as long as the menu icon is still accessible.<br /><br /><app-froala-tooltip-element description="Tabs organize content across different screens and views." link-label="More on tabs" link-url="/m3/pages/tabs/overview" should-open-link-in-new-tab="true">Tabs</app-froala-tooltip-element> can be used alongside a navigation rail to create an extra layer of visible navigation.</p>

Navigation rail collapsed next to screen content, and expanded overlaying screen content with secondary destinations.

<p>Expanded navigation rails can open from menu buttons on mobile</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmapifwv9-GM3_Expressive_Nav-Rail_Guidelines_32_IA_V10.mp4?alt=media

<h2 id="isPasted">Adaptive design</h2>

<p>For more, see <a href="/m3/pages/layout-overview/adaptive-design/" target="_self">adaptive design</a>.</p>

<h3>Resizing</h3><p>When moving from a large screen to a small screen, a navigation rail can transform into a navigation bar, providing the same quick access in a configuration that’s easier to use on smaller displays. Never use the navigation rail and navigation bar simultaneously. </p><p>Only use navigation rails for medium breakpoints and larger. Don’t use a navigation bar. If there are more than five destinations, consider using a modal expanded nav rail instead.</p><p><strong>Compact:</strong> Don’t use a standard navigation rail for compact layouts due to space constraints. Use a navigation bar instead.</p><p><strong>Medium:</strong> Use a navigation rail, especially if prioritizing persistent vertical navigation over maximizing vertical content space.</p><p><strong>Expanded to extra-large:</strong> Use a navigation rail, not a navigation bar. Consider available horizontal space and the number of destinations when choosing between standard and modal.</p><p></p>

Navigation bar on a phone screen and navigation rail on a tablet screen.

<p><span style="white-space:pre-wrap">On smaller devices, use a navigation bar. On larger displays, use a navigation rail.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fupcvd-26.png?alt=media

<h3>Presentation</h3><p><span style="white-space:pre-wrap" id="isPasted">When the navigation rail transitions from collapsed to expanded, the contents of the page should automatically adjust to fit.<br /><br />The contents of the navigation rail also expand to fill the space. For example, the FAB should transition into an extended FAB. <br /><br />Extra destinations can be shown in an expanded nav rail.</span></p>

Extra destinations in an expanded navigation rail.

<p>Use a standard expanded rail when there are secondary destinations or actions that have lower priority than the main navigation items</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalqalnw-GM3_Expressive_Nav-Rail_Guidelines_27_IA_V07.mp4?alt=media

<h2>Behavior</h2>

<h3 dir="ltr" id="isPasted">Scrolling</h3><p dir="ltr"><span style="white-space:pre-wrap" id="isPasted">Destinations in the navigation rail should remain visible and fixed when scrolling vertically.</span></p>

Screen content scrolls while rails stay fixed.

<p><span style="white-space:pre-wrap">Rail destinations remain fixed while on-screen content scrolls vertically</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm5v1vvd7-J%20-%20Scrolling%20RENDER%20-%202x.mp4?alt=media

<p dir="ltr" id="isPasted"><span style="white-space:pre-wrap" id="isPasted">If a layout scrolls horizontally, the rail can scroll off-screen or remain fixed. To distinguish that content is scrolling underneath the rail, use a divider or add elevation to the rail.</span></p>

A nav rail with a divider between it and the page’s content.

<p><span style="white-space:pre-wrap">A divider and color fill change create visual distinction between the rail and horizontally scrolling content</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0gtjndl-K%20-%20Side%20Scroll%20RENDER%20-2x_240821.mp4?alt=media

A nav rail with slight elevation.

<p><span style="white-space:pre-wrap">Elevating the rail to level 1 creates visual distinction between the rail and horizontally scrolling content</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmbs2jj48-GM3_Expressive_Nav-Rail_Guidelines_30_IA_v01%20(1).mp4?alt=media

<h3 dir="ltr" id="isPasted">Selection</h3><p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">When a destination is tapped, the destination screen uses a </span><span style="white-space:pre-wrap" id="isPasted"><a href="/m3/pages/motion-transitions/transition-patterns#f852afd2-396f-49fd-a265-5f6d96680e16" target="_blank" rel="noopener noreferrer">top level</a></span><span style="white-space:pre-wrap" id="isPasted"> transition pattern. In addition, the icon becomes filled and the active indicator expands from the center of the icon.</span></p>

Selection transition between one navigation item and another.

<p><span style="white-space:pre-wrap">Tapping a destination uses a top level transition pattern</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fvmjbe-L%20-%20NAV%20Selection%20-%20RENDER%202x_240821.mp4?alt=media

<h3>Back</h3><p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">On Android, a gesture called </span><span style="white-space:pre-wrap" id="isPasted">predictive back</span><span style="white-space:pre-wrap" id="isPasted"> allows people to swipe left or right on the screen to go back or dismiss modal components.<br /></span></p><ul><li><span style="white-space:pre-wrap">Previous screen is revealed in a preview to signal the destination<br /></span></li><li><span style="white-space:pre-wrap">Predictive back only applies to the <strong>modal expanded</strong> navigation rail.</span></li></ul><p><span style="white-space:pre-wrap">A list of compatible components is available on the </span><span style="white-space:pre-wrap"><a href="/m3/pages/gestures/" target="_blank" rel="noopener noreferrer">gestures page</a></span><span style="white-space:pre-wrap">.</span></p>

Modal expanded navigation rail with Android predictive back feature.

<p>The nav rail pops off the edge of the window during the predictive back gesture</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmapifi58-GM3_Expressive_Nav-Rail_Guidelines_PredictiveBack_IA_V02.mp4?alt=media

<h3 dir="ltr" id="isPasted">Selection</h3><p dir="ltr">When a destination is tapped, several transitions occur:</p><ul><li>A touch ripple appears</li><li>The outgoing icon color changes from a brand color to grey</li><li>The outgoing icon moves down to align with the deactivated tabs, and then the label fades out</li><li>The incoming icon color changes from grey to a brand color</li><li dir="ltr">The incoming icon moves up, and the incoming label fades in</li></ul>

A tapped destination transitions from inactive to active

<p>Tapping a destination changes the outgoing icon color to grey, aligns the icon with deactivated tabs, allowing for the incoming icon to move up and change to a brand color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fktug7t17-3_Mid.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/B7aiYo5IM932EzqTfX7bkS08Ebciat0LGJWQg8PM6ZD1tl7iIqXm2lmUyfQ56VoXLoaTaNmMuVgsSg5QLBA6q67v88RUwONUL0LfX01m5LU9=s676

## XR

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">This is a rapidly changing space. Guidelines are primarily intended for designers at this time. Find what’s implemented in code in the <a href="https://www.figma.com/design/cVjQvQ0moD8wkPWH2rn2c6/XR?node-id=294149-10229&amp;t=AFAz42CCMXa5470T-4" target="_blank" rel="noopener noreferrer">design kit</a>.</div></div></div>

<p><span style="white-space:pre-wrap" id="isPasted">Extended reality (XR) interfaces have special design requirements, like showing apps in 3D space. Material has XR-specific navigation rails with custom specs and guidance. See </span><span style="white-space:pre-wrap" id="isPasted"><a href="http://developer.android.com/design/ui/xr/guides/foundations" target="_blank" rel="noopener noreferrer">XR developer documentation</a></span><span style="white-space:pre-wrap" id="isPasted"> for more details.</span></p>

<h2>Variants</h2>

<p>There are two variants of navigation rail <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels." link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters " should-open-link-in-new-tab="true">orbiters</app-froala-tooltip-element>: the contained FAB and spatialized FAB navigation rails.</p>

Navigation bar orbiters with a contained FAB and a spatialized FAB.

<ol class="decimal"><li>Contained FAB rail</li><li>Spatialized FAB rail</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaffw03x-n.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/dPJqjYJCk9bPHeSRMvYPWuDtexUzZDMRBk6vNciqpu5z0dQG30QbaVle64vcI2dusE8aqPEUqFra47gf6R870mBGAhYghroP90OYqWugm180=s2048

<h2>Anatomy</h2>

Diagram of navigation rail orbiter identifying 9 internal elements of the component.

<ol><li>Container</li><li>Active indicator</li><li>Large badge (optional)</li><li>Badge (optional)</li><li>Large badge label (optional)</li><li>Label text</li><li>Icon</li><li>Embedded or spatialized FAB (optional)</li><li>Menu icon (optional)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaffwe2f-n.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/rU4TAGNiKzJj6z-L-jcKcfsZTlzzuIycA30T85HGQ_JyBo49apcjkI9TKY5yvPo4-heaO-X5nfrETlyizfZ9_FlQaV-z9BZQFNZ1S7N-MP-y=s2048

<h2>Color &amp; elevation</h2>

<p>On XR, color is used to highlight elevated UI elements and orbiters. With <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation" target="_blank" rel="noopener noreferrer">spatial elevation</a>, the navigation bar displays above the <app-froala-tooltip-element description="In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content." link-label="More on spatial panels" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels" should-open-link-in-new-tab="true">spatial panel</app-froala-tooltip-element>, on the Z-axis. Color communicates elevation on UI elements and orbiters. Elevated nav rails can use any of these color options:</p>

4 versions of elevation color strategy.

<ol><li>Surface container with tertiary FAB</li><li>Surface container high with tertiary fixed dim FAB</li><li>Surface container highest with tertiary fixed dim FAB</li><li>Tertiary container with primary FAB</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaffwte4-n.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/M6OH6zh7_zTrkS1zUDj-eceTyjgUMahrpEPl6WDJMMAuoODDcaGHDbMtZDzxApkri7IjSHwtCZnBxQnucLJCwA_zJawPO2gSn5i8Qo7-DxNp=s2048

<h2>Measurements</h2>

Measurements and padding for navigation rail orbiter with contained FAB.

<p>Navigation rail orbiter padding and measurements with contained FAB</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaffxdwj-n.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/rLe0xRyUvCeR1tXOPjPJ-hELWYJVzjkIMhHriNOGkHBiJEzAGt7hAMOrn9O5uGpAapq6A1uzhFSbP9u7GChXoBzMVpGj-MJ_q72tJBrP0X0avA=s1004

Measurements and padding for navigation rail orbiter with spatialized FAB.

<p><span style="white-space:pre-wrap">Navigation rail orbiter padding and measurements with spatialized FAB</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaffxpih-n.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/VGWnkF5eQPdJ2RNo4C0VAmVigdGhBqswyXKAYq0cQgHfCPwPFHm7JKlRPkOgAHxPTtww-Wmm2TnRan4iae_giCyC0KgU76nsh_2z6K2-lW-7=s1004

<h2>Usage</h2>

<p>In <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components." link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element>, a navigation rail can appear in an <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels." link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiter</app-froala-tooltip-element> for a more immersive experience. Currently, spatial capabilities, such as orbiters, are only available in full space. In <app-froala-tooltip-element description="Home space is compatible with mobile and large screen apps, but doesn’t support spatial components" link-label="More on home space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">home space</app-froala-tooltip-element>, use a regular navigation rail on the same plane as the body content to mimic a 2D experience.</p>

Interface showcasing navigation rail behavior and placement when transitioning from a 2D to 3D experience.

<p><span style="white-space:pre-wrap">Navigation rail orbiter behavior and placement changing when going from a 2D to a 3D experience</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cmf60w-navrail_01.mp4?alt=media

<h2>Behavior</h2>

<h3>Global context</h3><p><span style="white-space:pre-wrap" id="isPasted">Intended for global navigation, a nav rail orbiter should be centered along the left or right edge of the app it controls. It stays anchored to the app during layout or content changes to ensure controls are easy to find. </span></p>

A navigation rail orbiter placed in global context.

<p><span style="white-space:pre-wrap">A navigation rail orbiter should be placed in global context, centered and anchored to the left or right of the app</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma4acdxe-XR_Nav-Rail_Behavior_01_V02.mp4?alt=media

<h3>Local context</h3><p><span style="white-space:pre-wrap" id="isPasted">Don’t place a navigation rail orbiter in local context or </span><span style="white-space:pre-wrap" id="isPasted"><a href="/m3/pages/navigation-rail/xr#519a112b-51d6-4200-96a9-54af92fb787d">between spatial panels</a></span><span style="white-space:pre-wrap" id="isPasted">. Local placement can make controls hard to find. Nav rails are designed for app-level navigation, so should only use the global context.</span></p>

A navigation rail orbiter placed in local context.

<p><span style="white-space:pre-wrap">Avoid placing a navigation rail orbiter in local context. It can be hard to find if placed between two spatial panels.</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma4acsak-XR_Nav-Rail_Behavior_02_V02.mp4?alt=media

<h2>Placement</h2>

<h3>Navigation context</h3><p><span style="white-space:pre-wrap" id="isPasted">The position of the navigation rail orbiter should communicate its navigational context:</span></p><ul><li>Use <strong><app-froala-tooltip-element description="Offset positioning is when orbiters are placed adjacent to spatial panels without overlap." link-label="More on offset positioning" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">offset positioning</app-froala-tooltip-element></strong> for global actions that affect the overall app experience</li><li>Use <strong><app-froala-tooltip-element description="Inset positioning is when orbiters overlap with spatial panels." link-label="More on inset positioning" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">inset positioning</app-froala-tooltip-element></strong> for local actions that are specific to a spatial panel</li></ul><p><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">A navigation rail orbiter can either overlap or be positioned adjacent to spatial panels with a 20dp margin for visual separation.</span></span></p>

Navigation rail orbiter offset and inset positioning.

<p><span style="white-space:pre-wrap">Position the navigation rail orbiter to reflect context: offset for global actions, inset for spatial panel-specific actions</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cmibon-navrail_02.mp4?alt=media

<h3>Inset positioning</h3><p><span style="white-space:pre-wrap" id="isPasted">Don’t obstruct content. To ensure a balanced and uncluttered layout, a navigation rail orbiter should overlap spatial panels by 12dp and no more than half their width.</span></p>

Nav rail orbiter overlapping content by more than half its width.

<p><span style="white-space:pre-wrap">Avoid overlapping an inset navigation rail orbiter by more than half its width</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cmliqr-navrail_03.mp4?alt=media

<h3>Vertical alignment</h3><p><span style="white-space:pre-wrap" id="isPasted">A navigation rail orbiter can be aligned to the top, middle, or center of spatialized panels, providing different levels of visual prominence and accessibility.<br /><br />Align the navigation rail orbiter based on the specific design and user experience goals for the application.</span></p>

Nav rail orbiter positioning moving from the top, to middle, to center of spatialized panels.

<p><span style="white-space:pre-wrap">Align the navigation rail orbiter at the top, middle, or center of spatialized panels</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cmooik-navrail_04.mp4?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">The navigation rail orbiter placement shouldn't exceed the height of adjacent spatial panels.</span></p>

A nav rail orbiter positioning above its spatial panel.

<p><span style="white-space:pre-wrap">The navigation rail orbiter shouldn’t exceed the height of the spatial panel</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cmqshd-navrail_05.mp4?alt=media

<h3>Spatial panel alignment</h3><p><span style="white-space:pre-wrap" id="isPasted">Avoid placing a navigation rail orbiter between spatial panels. This negatively affects the interface structure.<br /><br />For layouts that span more than two spatial panels, consider using a navigation bar orbiter.</span></p>

A nav rail orbiter incorrectly positioned between spatial panels.

<p><span style="white-space:pre-wrap">Don't place a navigation rail orbiter between spatial panels</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cmtuvy-navrail_06.mp4?alt=media

<h2>Spatialized FAB</h2>

<p>There are two variants of navigation rail orbiters with different FAB treatments:</p><ul><li><p><strong>Contained FAB rail:</strong> A contained FAB within the rail. This offers a compact and familiar layout.</p></li><li><p><strong>Spatialized FAB rail:</strong> The FAB becomes an orbiter of it’s own and is placed outside the navigation rail orbiter. Use this for higher emphasis and a distinct spatial effect.</p></li></ul><p>Use the spatialized FAB rail to emphasize key actions and leverage XR hierarchy. Use the contained FAB rail to be more subtle, and align the experience with the baseline navigation bar.</p>

Interface showing the difference between a navigation rail orbiter with a contained FAB and spatialized FAB.

<p><span style="white-space:pre-wrap">Choose between a navigation rail orbiter with a contained FAB or a spatialized FAB</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cmvtu0-navrail_07.mp4?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">To maintain visual association, place the spatialized FAB in close proximity to the navigation rail orbiter. Material recommends a 20dp margin.<br /><br />The spatialized FAB can be placed above or below the navigation rail orbiter.</span></p>

Spatialized FAB positioned close to the navigation rail orbiter.

<p><span style="white-space:pre-wrap">Position the spatialized FAB close to the navigation rail orbiter</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cmyijj-navrail_08.mp4?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">While the spatialized FAB and navigation rail orbiter are typically positioned together, their placement is adaptable.</span></p>

Spatialized FAB positioned with excessive spacing between itself and the navigation rail orbiter.

<p><span style="white-space:pre-wrap">Use caution when positioning spatialized FABs. Keep them within the height of adjacent spatial panels</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cn0kcj-navrail_09.mp4?alt=media

<h2>Accessibility considerations</h2>

<p><span style="white-space:pre-wrap" id="isPasted"><a href="https://developer.android.com/design/ui/xr/guides/get-started#make-app" target="_blank" rel="noopener noreferrer">XR accessibility</a></span><span style="white-space:pre-wrap" id="isPasted"> guidelines are still evolving. XR navigation rails should follow applicable Material </span><span style="white-space:pre-wrap" id="isPasted"><a href="/m3/pages/navigation-rail/accessibility" target="_blank" rel="noopener noreferrer">nav rail accessibility standards</a></span><span style="white-space:pre-wrap" id="isPasted">.</span></p>

## Accessibility

<h2 id="isPasted">Use cases</h2><p><span style="white-space:pre-wrap" id="isPasted">People should be able to do the following using the assistive technology:</span></p><ul><li><span style="white-space:pre-wrap">Navigate between navigation destinations</span></li><li><span style="white-space:pre-wrap">Select a particular navigation destination from a set</span></li><li><span style="white-space:pre-wrap">Get appropriate feedback based on input type</span></li></ul>

<h2 id="isPasted">Interaction &amp; style</h2>

<p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">When a navigation item is tapped, the active indicator appears, providing the following feedback to the user that it is selected:</span></p><ul><li><span style="white-space:pre-wrap">A ripple passes through the indicator</span></li><li><span style="white-space:pre-wrap">The icon switches from outlined to filled</span></li><li><span style="white-space:pre-wrap">The icon and text change color</span></li></ul><p><span style="white-space:pre-wrap">When hovered, the hover state appears, providing a visual cue that the destination is interactive.</span></p>

Colorful, purple navigation rail shown collapsed and expanded.

<p><span style="white-space:pre-wrap">Touch: Tap</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0guemtv-01-static.png?alt=media

Tap indicator on a collapsed nav rail.

<p><span style="white-space:pre-wrap">Cursor: Hover, Click</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0guep9g-02-static.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">The target area for expanded navigation rails spans the full width of the container, even though the active indicator visually hugs the content.</span></p>

Touch indicator on a nav rail.

<p>Touch: Tap</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0gud02c-03-static.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">Use a filled icon for the active destination and outlined icons for inactive destinations.<br /><br />Active and inactive icon colors need sufficient contrast against the container.<br /></span></p>

Navigation rail with filled element.

<p><span style="white-space:pre-wrap">Use the default color scheme to ensure proper contrast and emphasis on the active destination</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fut28q-04.png?alt=media

Nav rail with multiple navigation destinations and multi-colored contrast.

<p><span style="white-space:pre-wrap">Don’t use more than two colors for destinations or low-contrast colors in the navigation rail. This will make distinguishing active items difficult.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fut791-05.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">If an icon doesn’t have a filled style, use the semibold icon weight instead.</span></p>

Icon button with semibold weight, without filled options.

<p><span style="white-space:pre-wrap">An icon with no filled option should use the semibold weight when active</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2kvazns-09.png?alt=media

<h3>Text scaling and truncation</h3><p id="isPasted">When someone sets their device to show a larger text size, the navigation rail items should grow vertically to accommodate larger labels while retaining the default padding. It’s okay for scaled text to wrap in navigation items.</p><p>To remain accessible, ensure the full label is always visible on-screen at up to 2x text sizing. Beyond this size, text can truncate. </p>

Nav rail with text scaled to 1.5x size. All labels are on one line.

<p>Text scaled to 1.5 size</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm36brxfu-04.png?alt=media

Nav rail with text scaled to 2x size. Some labels wrap to two lines.

<p>Text scaled to 2x size</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm36bs1jw-05.png?alt=media

<h3>Initial focus</h3><p><span style="white-space:pre-wrap" id="isPasted">Initial focus lands directly on the first interactive item, whether it’s the menu, the FAB, or the first navigation item.<br /><br />From the FAB or menu, <strong>Tab</strong> brings the person to the navigation items. <strong>Tab</strong> or <strong>Arrows</strong> then navigate between items.</span></p>

Arrows help people move between pages.

<p><span style="white-space:pre-wrap">Use arrows to move between navigation items</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0futkj8-07.png?alt=media

Space/enter help people choose a navigation destination.

<p><span style="white-space:pre-wrap">Use space/enter to activate the focused navigation item</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0futowb-08.png?alt=media

<h3>Visual indicators</h3><p><span style="white-space:pre-wrap" id="isPasted">Icons give the dominant cue of the navigation state. Use a filled icon for the selected destination to contrast with outlined icons for the non-selected destinations.</span></p>

Nav bar with an active, filled icon button.

<p><span style="white-space:pre-wrap">Use a filled icon variant on the selected navigation item to differentiate from inactive navigation items</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0futxf6-09.png?alt=media

Selected navigation item without filled icon style.

<p><span style="white-space:pre-wrap">Avoid using the same unfilled icon style for both selected and unselected items because it lacks important visual feedback cue</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fv1bxc-10.png?alt=media

<h2>Keyboard navigation</h2><div class="table-wrapper"><table style="width:100%" class="fr-table-selection-hover"><thead><tr><th>Keys</th><th style="width:78.9317%">Actions</th></tr></thead><tbody><tr><th>Tab / Arrows</th><td><span style="white-space:pre-wrap" id="isPasted">Navigate between interactive elements</span></td></tr><tr><th>Space / Enter<br /></th><td><span style="white-space:pre-wrap" id="isPasted">Selects an interactive element</span></td></tr></tbody></table></div>

<h2>Labeling elements</h2><p>The accessibility label for a navigation item is typically the same as the adjacent text label.<br /><br />When the visible UI text is ambiguous, accessibility labels need to be more descriptive. For example, a navigation item visibly labeled <strong>Recent</strong> would benefit from additional information in its accessibility label to clarify the destination's intent.<br /><br />Note: On Android Views (MDC-Android), a more descriptive accessibility label is not available and the role is not announced.</p>

“Maps” is both the icon label text and the accessibility label.

<p><span style="white-space:pre-wrap">While the visible label text reads <strong>Recent</strong>, the accessibility label for this switch clarifies its function: <strong>Recent images</strong></span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fuvxlx-11.png?alt=media
