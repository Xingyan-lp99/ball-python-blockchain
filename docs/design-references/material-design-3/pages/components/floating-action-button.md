# FABs

Source: https://m3.material.io/components/floating-action-button
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/1e52f150-575c-45fa-8f5f-75868c5ab068.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Use a FAB for the most common or important action on a screen</p></li><li><p>Make sure the icon in a FAB is clear and understandable</p></li><li><p>FABs persist on the screen when content is scrolling</p></li><li><p>Three variants: FAB, medium FAB, large FAB</p></li></ul>

The 3 sizes of floating action buttons.

<ol class="decimal"><li><p>FAB</p></li><li><p>Medium FAB</p></li><li><p>Large FAB</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkap9gay-01.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/455af1b95b07ca01

libraryModuleType: STATUS_TABLE

moduleConfigurationOverrides: {'headings': ['Type', 'Resource', 'Status']}

<h2>M3 Expressive update</h2>

<p><strong>May 2025</strong></p><p>The FAB has new sizes to match the extended FAB and more color options. The small FAB is no longer recommended. <a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank">More on M3 Expressive</a></p>

<p>Variants and naming:</p><ul><li><p>Added <strong>medium</strong> FAB size</p></li><li><p><strong>Small</strong> FAB size is no longer recommended</p></li><li><p>FAB and large FAB sizes are unchanged</p></li><li><p>FAB variants are based on size, not color</p></li></ul><p>Color:</p><ul><li><p>Added tone color styles: </p><ul><li><p>Primary</p></li><li><p>Secondary</p></li><li><p>Tertiary</p></li></ul></li><li><p>Renamed existing tonal color styles to match their token names: </p><ul><li><p><strong>Primary</strong> to <strong>Primary container</strong></p></li><li><p><strong>Secondary</strong> to <strong>Secondary container</strong></p></li><li><p><strong>Tertiary</strong> to <strong>Tertiary container</strong></p></li><li><p>The values haven't changed</p></li></ul></li><li><p>Surface color FABs  are no longer recommended</p></li></ul>

4 FABs showing the colors available after the expressive update.

<p><span style="white-space:pre-wrap">FABs have updated colors and sizes</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc68z96-02.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Kyq0kFrZiQkyIGco9EHQ5yzaPCDzbUydpq5bcHqcin1vLOhBpnqAeAW6D86dFvHrexhyJvo5jK0Brc4PwckWVOtXFqRcMhUA-h05047nERg=s1352

<h2>Differences from M2</h2>

M2 circular FAB with a plus icon.

<p><span style="white-space:pre-wrap">M2: FABs are circles and always have a drop shadow</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc69mae-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/biMTAbEZ8apVSF9QNSr9S8V1F1DCCRCRckdBmlU0g9XLCrNJMwkw_cbBk_gvb6b0JbaulKKD9lAeDTQp4h3sZK5yKXP0CrSWlefMrFoTxK3T=s1004

M3 rounded corner square FAB with an artist’s palette icon.

<p><span style="white-space:pre-wrap">M3: FABs have a boxier shape, can use dynamic color, and include a new large FAB variation</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6a5yd-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/eSZyi5bl8kk_aCpEVo6DV_KiYuZ3i_rEVB9y7rWbFd5SSILeUBlvQ3n2ztYzvPSTe1fyMK0LKDD_axvANAOOt6VLnf4GoSbWWSKy3j9bcRI=s1004

## Specs

<h2>Variants</h2>

An icon on the container of a FAB, medium FAB, and large FAB.

<ol><li>FAB</li><li>Medium FAB</li><li>Large FAB</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6atia-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/CdTXXgPJ5XavoUEXtTKTczb0ENYt1VwreirVIJMyIYnwI6gFCYn1S4LCQyptGlF6EzKq9xL2hzPOQKv2RdKrhf6kTIj5vkcNY2u-VuQRqghs=s2048

<h3>Baseline variants</h3><p>The small FAB is still available, but no longer recommended. <a href="/m3/pages/fab/specs#cd336045-e97d-4a6d-ac23-f778fa695e3c" target="_self">Jump to baseline specs</a></p>

An icon on the container of a small FAB.

<p>1. Small FAB</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6bkq8-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LVMfvx2rKsoVM1_1Pq9CQ8o0dDyfSQtfCxYgle_57GhDKX0oDkNepZr0yvyqmoI6mL-0QfWWfFkmVJV5RwLbJVGJ4YGXZBTcT9JW2-IPRQNpVg=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:17.479%"><p>Variant</p></th><th style="width:38.8359%;text-align:center"><p>M3</p></th><th style="width:43.6281%;text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td><p>FAB</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Medium FAB</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td><p>Large FAB</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Small FAB</p></td><td><p>Available</p></td><td><p>Not recommended.</p><p>Use a larger size.</p></td></tr></tbody></table></div>

<h2>Configurations</h2>

<p>In the expressive update, the <strong>primary</strong>, <strong>secondary</strong>, and <strong>tertiary</strong> set colors were renamed to <strong>primary container</strong>, <strong>secondary container</strong>, and <strong>tertiary container </strong>to match the actual color roles used. New primary, secondary, and tertiary color styles were created to match the corresponding color roles. <a href="/m3/pages/fab/specs#67e71ec7-b520-405a-aa06-2decfa0b92a3" target="_self">View details in the color styles section</a></p>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:16.9683%"><p>Category</p></th><th style="width:40.4764%"><p>Configuration</p></th><th style="width:20.4061%;text-align:center"><p>M3</p></th><th style="width:22.0786%;text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td rowspan="2" style="width:16.9683%"><p>Color</p></td><td><p>Primary container, secondary container, tertiary container</p></td><td><p>Available as primary, secondary, tertiary</p></td><td><p>Available</p></td></tr><tr><td><p>Primary. secondary, tertiary</p></td><td><p>--</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Tokens &amp; specs</h2><p>Use the table's menu to select a token set. FAB tokens are organized by size and color. <a href="/m3/pages/design-tokens/overview/" target="_blank">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/41587918e51cca98

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['FAB - Size - Regular', 'FAB - Size - Medium', 'FAB - Size - Large', 'FAB - Color - Tonal primary', 'FAB - Color - Tonal secondary', 'FAB - Color - Tonal tertiary', 'FAB - Color - Primary', 'FAB - Color - Secondary', 'FAB - Color - Tertiary'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['[Deprecated] FAB - Size - Small', 'FAB - Color - Surface', 'FAB - Color - Branded', 'FAB - Size - Regular', 'FAB - Size - Medium', 'FAB - Size - Large', 'FAB - Color - Tonal primary', 'FAB - Color - Tonal secondary', 'FAB - Color - Tonal tertiary', 'FAB - Color - Primary', 'FAB - Color - Secondary', 'FAB - Color - Tertiary', '[Deprecated] FAB - Primary, small', '[Deprecated] FAB - Primary, large', '[Deprecated] FAB - Branded, large', '[Deprecated] FAB - Secondary, large', '[Deprecated] FAB - Secondary, small', '[Deprecated] FAB - Surface, large', '[Deprecated] FAB - Surface, small', '[Deprecated] FAB - Tertiary, large', '[Deprecated] FAB - Tertiary, small']}

<h2>Anatomy</h2>

2 elements of the FAB.

<p>1. Container</p><p>2. Icon</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6cml8-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ANFTHcXuJZA9FSSl3I315pOU3UzwgUh_BZgfudPuvatQY4tLh2hREtb6ESAQZulQZBDe8iHcqQ548uZe2aJd2UGGv-8q2XXCBeGLdERRlXs=s2048

<h2>Color</h2><p>Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens" target="_blank">Learn more about design tokens</a></p>

<h3>Color styles</h3><p>FABs can use several combinations of <strong>color</strong> and <strong>on-color</strong> styles, such as <strong>primary</strong> and <strong>on-primary</strong>. The following color mappings provide the same legibility and functionality, so the color mapping you use depends on style alone.</p>

6 FAB color styles in light and dark themes. Each style has 2 color roles, 1 for the container and icon.

<ol class="decimal"><li><span style="white-space:pre-wrap">Primary container &amp; On primary container (default)</span></li><li><span style="white-space:pre-wrap">Secondary container &amp; On secondary container</span></li><li><span style="white-space:pre-wrap">Tertiary container &amp; On tertiary container</span></li><li><span style="white-space:pre-wrap">Primary &amp; On primary</span></li><li><span style="white-space:pre-wrap">Secondary &amp; On secondary</span></li><li><span style="white-space:pre-wrap">Tertiary &amp; On tertiary</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6diiz-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ZwUAoGfKU_nKPy45dUL885gk5_UbUfDoN2lY0oreRhS7vnkY12iBhnT3a1Fm1LydwMZVkqFYkQhYjVbGHx_hHsPwlmEm2KWwSQ75kOOKSkCsEA=s2048

<h3>Baseline color styles</h3>

<p>Surface FAB color styles are still available, but no longer recommended.</p>

Baseline FAB style in all 3 sizes.

<ol class="decimal"><li><p>Surface FABs</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6empp-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Yt-382N_6b_TEqwyVAFZY_PG3zCmejVTFm6-tfbkUGpTqwgeECy2CNFH8n0bV1Spc6qU-ruc9l-Qja0_LpTeeYatxSxOi7qyzjF5tSeeXuEU=s2048

<h2 id="isPasted">States</h2><p><span style="white-space:pre-wrap" id="isPasted">States are visual representations used to communicate the status of a component or interactive element.<br /><br />When using a non-default color mapping for FABs, make sure the state layer color is the same as the icon color. For example, the state layer color for the <strong>primary</strong> color style should be <span class="inline-code">md.sys.color.primary</span>.</span></p>

4 states of a FAB shown in light and dark themes.

<ol><li><span style="white-space:pre-wrap">Enabled</span></li><li><span style="white-space:pre-wrap">Hovered (8% state layer) - elevation 4</span></li><li><span style="white-space:pre-wrap">Focused (10% state layer)</span></li><li><span style="white-space:pre-wrap">Pressed (10% state layer)</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6fdu1-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/zCVGIf6lxv-ExBpOFiRo9G2yv-hIzjqPkEG0HKniNMzlBuWcEI8tXSvAndc3RL7Q0OOG56i6xP36k1rP1E-Fz92l4TGPZlkzdbNCF67rj2M=s2048

<h2>Measurements</h2>

<h3 id="isPasted">FAB</h3>

FAB size measurements.

<p><span style="white-space:pre-wrap">FAB size measurements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6fz4n-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/bY4SJyZCamFkqUakHco1-HsHBRJ55wn7zAWPhJCBlE9W4aA7wFnRywl8NSl_e7oToqU6JODtUnjeguVn7BJd5irT8DYnHQmq1lQKEvgN3g3Q=s1004

FAB padding measurements.

<p><span style="white-space:pre-wrap" id="isPasted">FAB padding measurements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6gdhg-08-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/beevX-JBo5BT5oaSR6WnfIvvspxwDFUOsGg0TBWuDEAgjCYevFNjOhNnz6om1Pbxkal9dwoBR5HwAeyyn7LB8z1N-NrDjH_F9ZcxN_lEL60=s1004

<h3 id="isPasted">Medium FAB</h3>

Medium FAB size measurements.

<p><span style="white-space:pre-wrap">Medium FAB size measurements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6gu0p-09-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/l-yip97Leh5bLumalSFuxS1DEMG6p3xJlXkUCTioixjvr0uXlzTaKK85zQzLnZPpgD9E72Zajd1yO9VMW1FKpSUVCWXbP5XIxIz6dUiubWALJw=s1004

Medium FAB padding measurements.

<p><span style="white-space:pre-wrap" id="isPasted">Medium</span><span style="white-space:pre-wrap" id="isPasted"> FAB padding measurements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6ha1z-10-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/qQZXXxZh9x9LRJyZI_2tblBDG7aMd-Rx3HQVX-ssihAGa-xSIGuOA2FZNPKeHgfbI-q19SD0IIUCT-xnLHk4Q-P2KSb-KnSm95tRPJQs2rKx=s1004

<h3 id="isPasted">Large FAB</h3>

Large FAB size measurements.

<p><span style="white-space:pre-wrap">Large FAB size measurements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6hrgc-11-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/_1q2AqUdfZfCbC9aKRbQaXHO48GA5OSdH6ywXyyosvlIznXjrr0Wx-WM9xomavwT1qj6RA42qG01crP9I7GQPJ92BWnvJqijQ01UxjQKKcgS=s1004

Large FAB padding measurements.

<p><span style="white-space:pre-wrap" id="isPasted">Large FAB padding measurements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6i508-12-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/PsH6GvakYnsKOw9X05rxaShBXItlCIc3qS-LGjmdITmzFgAnhxdiyhzUEM34i8B0MGtZoBoDdXE7eA1hYAFqcWEqFyipPBdhE0TirWp_HMWxTA=s1004

<h2>Baseline tokens &amp; specs</h2>

<p>Use the table's menu to select a token set. This only includes tokens for small and surface FABs, which are both no longer recommended. It doesn't include other colors, or large or regular FABs, since those are still currently used.</p>

resourceName: designSystems/20543ce18892f7d9/components/41587918e51cca98

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['[Deprecated] FAB - Size - Small', 'FAB - Color - Surface'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['[Deprecated] FAB - Primary, small', '[Deprecated] FAB - Primary, large', '[Deprecated] FAB - Secondary, small', '[Deprecated] FAB - Secondary, large', '[Deprecated] FAB - Tertiary, small', '[Deprecated] FAB - Tertiary, large', '[Deprecated] FAB - Branded, large', '[Deprecated] FAB - Surface, small', '[Deprecated] FAB - Surface, large', 'FAB - Primary', 'FAB - Branded', 'FAB - Secondary', 'FAB - Surface', 'FAB - Tertiary', 'FAB - Size - Large', 'FAB - Size - Medium', 'FAB - Size - Small', 'FAB - Color - Tonal primary', 'FAB - Color - Tonal secondary', 'FAB - Color - Tonal tertiary', 'FAB - Size - Baseline']}

## Guidelines

3 screens with various FAB sizes.

<p>FABs have multiple sizes that scale with the breakpoint</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkapod2e-01.png?alt=media

<h2>Usage</h2>

<p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Use a FAB for the most important action on a screen; it appears in front of all other content.<br /><br />The FAB can be aligned left, center, or right. It can be positioned above the navigation bar, or nested within it.</span></p>

A Compose FAB is positioned above a nav bar on a mobile email inbox.

<p><span style="white-space:pre-wrap">FABs can use dynamic color</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkapp0w4-02.png?alt=media

<p>There are three FAB sizes:</p><ol class="decimal"><li><p>FAB</p></li><li><p>Medium FAB (most recommended)</p></li><li><p>Large FAB</p></li></ol><p>Choose the FAB size based on the visual hierarchy of your layout. <br /><br />Note: The small FAB is no longer recommended.<br /></p>

3 FAB sizes.

<ol><li><span style="white-space:pre-wrap">FAB </span></li><li><span style="white-space:pre-wrap">Medium FAB</span></li><li><span style="white-space:pre-wrap">Large FAB</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkappjdx-03.png?alt=media

<p>The FAB is the smallest size, and is best used in <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact windows</app-froala-tooltip-element> where other actions may be present on screen.<br /><br />The medium FAB is recommended for most situations, and works best in compact and <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium windows</app-froala-tooltip-element>. Use it for important actions without taking up too much space. <br /><br />A large FAB is useful in any window size when the layout calls for a clear and prominent primary action, but is best suited for <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded</app-froala-tooltip-element> and larger breakpoints, where its size helps draw attention.</p>

A medium FAB over an email app UI.

<p>Use a medium FAB in most breakpoints</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkapq84r-04.png?alt=media

A large FAB over an email app UI.

<p><span style="white-space:pre-wrap">Use a large FAB when the primary action needs to be prominent</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkapqn1b-05.png?alt=media

A photo feed with no FAB.

<p><span style="white-space:pre-wrap">FABs are not needed on every screen, such as when images represent primary actions</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkapr8x3-06-do.png?alt=media

A screen with 3 FABs makes it hard to tell what the primary action should be.

<p><span style="white-space:pre-wrap">Don't display multiple FABs on a single screen</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkaps2z9-07-don't.png?alt=media

<p>A FAB can transform into an <app-froala-tooltip-element description="Extended floating action buttons (extended FABs) help people take primary actions." link-label="More on extended FABs" link-url="/m3/pages/extended-fab/overview" should-open-link-in-new-tab="true">extended FAB</app-froala-tooltip-element> on larger screens, or it can transition into a FAB menu when selected. Use a FAB menu when there are many kinds of actions relevant to the FAB. </p><p><a href="/m3/pages/fab-menu" target="_blank">More on FAB menus</a></p>

A extended FAB saying “Share” with a less popular share icon.

<p><span style="white-space:pre-wrap">Use the extended FAB when label text is necessary</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6tcz8-08.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/6gVz4SSpnVYq28cYhUlwX36JiaNZLx-0A1NhL4z0IUA-RwlUz5tsApAkIXx0RAVE780uol-6VkeZZq7jiXRPiGOzEUo_SGVtL7NG3ogNFwg=s656

A FAB menu showing 3 actions related to sharing.

<p>Use the FAB menu when there are many kinds of actions relevant to the FAB</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkc6uyqo-09.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/YtrgWibQJDIheCADkeWKz14g7auX0_zMKtGJ8o45F48iJl9BvPomdwRJGi8bjtOnAH7gtd-8V5ki1gS2Qo-f172n73boNv3__OGeekLj-xg=s656

<h2>Actions</h2>

<p><span style="white-space:pre-wrap" id="isPasted">A FAB can trigger an action on the current screen, or it can perform an action that creates a new screen.<br /><br />A FAB promotes an important, constructive action such as:</span></p><ul><li><span style="white-space:pre-wrap">Create</span></li><li><span style="white-space:pre-wrap">Favorite</span></li><li><span style="white-space:pre-wrap">Share</span></li><li><span style="white-space:pre-wrap">Start a process</span></li></ul>

FABS for 12 common actions including, create, edit, and navigate.

<p><span style="white-space:pre-wrap">Use FABs for primary, positive actions</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkaptzjv-10.png?alt=media

<p>Avoid using a FAB for minor or destructive actions, such as:</p><ul><li><p>Archive or trash</p></li><li><p>Alerts or errors</p></li><li><p>Limited tasks like cutting text</p></li><li><p>Controls better suited to a toolbar, like to adjust volume or font color</p></li></ul>

FABs for 18 minor or destructive actions, such as cut, trash, and volume.

<p><span style="white-space:pre-wrap">Don’t use FABs for minor, overflow, unclear, or destructive actions</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkapug9u-11.png?alt=media

<h2 id="isPasted">Anatomy</h2>

2 elements of a FAB.

<ol class="decimal"><li><span style="white-space:pre-wrap">Container</span></li><li><span style="white-space:pre-wrap">Icon</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkapv2og-12.png?alt=media

<h3 id="isPasted">Container</h3><p><span style="white-space:pre-wrap" id="isPasted">The FAB is typically displayed in a square container. The container shouldn’t be covered by other elements, such as badges.<br /><br />The container must have sufficient color contrast with the surface it’s placed on.</span></p>

A bright colored FAB has high contrast with the background.

<p><span style="white-space:pre-wrap">A FAB container color needs to stand out from its background</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkaq0msf-13.png?alt=media

<h3 id="isPasted">Icon</h3><p><span style="white-space:pre-wrap" id="isPasted">An icon in a FAB should be clear and understandable. When hovering over a FAB on web products, FABs should display a tooltip with an accompanying icon text label. Use a filled icon instead of an outlined icon.<br /><br />A FAB shouldn't contain notifications or actions found elsewhere on a screen.</span></p>

4 FABs each with a simple icon.

<p><span style="white-space:pre-wrap">Use clear and simple icons such as add, message, or edit</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkaq1779-14.png?alt=media

4 FABs each with an ambiguous icon.

<p><span style="white-space:pre-wrap">Don’t use confusing or open-ended icons to symbolize less common actions</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkaq1wxv-15.png?alt=media

<h2>Adaptive design</h2>

<p>In <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium breakpoints</app-froala-tooltip-element>, the best place for the FAB is typically the lower right corner of a screen, since it’s easy to reach and is less likely to cover important content.<br /><br />In <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints</app-froala-tooltip-element>, consider placing the FAB in the upper left corner, like in the <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element>. This positions it as one of the first interactive elements people see when they land on the page.<br /><br />Adjust the size of the FAB based on the context. Use a medium FAB for mobile layouts, and large FAB for tablets and large screens. </p>

Large screen layout showing FAB in upper left region of the screen, below navigation rail icon.

<p><span style="white-space:pre-wrap">For large screens, place the FAB in the upper left corner</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkaq2b6m-16.png?alt=media

A screen layout with several interactive elements. A single FAB is in the navigation rail.

<p>A FAB can be used within a navigation component, such as a navigation rail</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkaq2qmb-17.png?alt=media

A busy screen layout with 8 cards, each with their own FAB.

<p><span style="white-space:pre-wrap">Individual components, such as cards, shouldn’t have their own FAB</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkaq35yc-18.png?alt=media

<h2>Behaviors</h2>

<h3>Appearing</h3><p>When a FAB animates on screen, it expands outward from a central point. The icon within it can be animated as well.<br /><br />While FABs should be relevant to screen content, they aren't attached to the surface on which content appears. FABs move separately from other UI elements because of their relative importance.<br /><br /><strong>Screen transitions <br /></strong>FABs can morph to launch related actions. When a screen changes its layout, the FAB should disappear and reappear during the transition.<br /><br /><strong>Reappearance <br /></strong>The FAB should only reappear if it's relevant to the new screen. It should reappear in the same position, if possible.</p>

FAB appearing from the bottom of the screen, moving to a position above the  navigation bar.

<p>FAB animating on screen</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0e6834q-FAB-A.mp4?alt=media

<h3>Expanding</h3><p>The FAB can expand and adapt to any shape using a container transform transition pattern. This includes a surface that's part of the app structure, or a surface that spans the entire screen.<br /><br />The FAB can also transition into a FAB menu. <br /><br /><a href="/m3/pages/fab-menu" target="_blank">More on FAB menus</a></p>

Compose FAB expands to container size, opening a draft email screen.

<p>FABs can expand and adapt to any shape</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm1l6g0wn-FAB-B-1.mp4?alt=media

<h3 id="isPasted">Scrolling</h3><p><span style="white-space:pre-wrap" id="isPasted">FABs remain in place on scroll.<br /><br />Extended FABs can collapse into a FAB on scroll and expand on reaching the bottom of the view.</span></p>

Extended FAB collapsed into a FAB when scrolling on the page.

<p>FABs stay in place above a scrolling background</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm1l6g857-FAB-C_1.mp4?alt=media

<h3 id="isPasted">Moving across tabs</h3><p><span style="white-space:pre-wrap" id="isPasted">When tabs are present, the FAB should briefly disappear, then reappear when the new content moves into place. This shows that the FAB is not connected to any particular tab.</span></p>

FAB blinks away and reappears with new screen content.

<p><span style="white-space:pre-wrap">The FAB should disappear and reappear when switching pages</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd8w19ca-GM3_Expressive_FAB_Guidelines_FAB-D_v02.mp4?alt=media

<p>Don't animate the FAB with body content.</p>

FAB moves horizontally when scrolling between tabs.

<p>Don’t keep the FAB on screen when switching pages</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd8w1k06-GM3_Expressive_FAB_Guidelines_FAB-E_v02.mp4?alt=media

## Accessibility

<h2 id="isPasted">Use cases</h2>

<p>People should be able to do the following using assistive technology:</p><ul><li><p>Navigate to and activate the FAB </p></li><li><p>Perform an action with the FAB </p></li><li><p>Expand and minimize an <app-froala-tooltip-element description="Extended floating action buttons (extended FABs) help people take primary actions." link-label="More on extended FABs" link-url="/m3/pages/extended-fab/overview" should-open-link-in-new-tab="true">extended FAB</app-froala-tooltip-element></p></li></ul>

<h2><span style="white-space:pre-wrap">Interaction &amp; style</span></h2>

<p><span style="white-space:pre-wrap" id="isPasted">Don't disable the FAB. If the action represented in the FAB is unavailable, the FAB shouldn't appear.<br /></span></p><p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Ensure the icon has a minimum 3:1 contrast ratio with the container.</span></p><p><br /></p>

FAB with highly contrasting bright container and dark icon.

<p>FAB icons are above the 3:1 contrast ratio</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalo050e-1.png?alt=media

FAB with low-contrasting dark container and dark icon.

<p>Avoid using colors with a contrast below 3:1</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmalo08ew-2.png?alt=media

<h2><span style="white-space:pre-wrap">Focus</span></h2>

<p>Ensure the FAB is prioritized in the overall focus order to create an efficient experience for people who navigate UIs with assistive tech. <br /><br />On mobile, the focus order may start with the <app-froala-tooltip-element description="App bars contain page navigation and information at the top of a screen" link-label="More on app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">app bar</app-froala-tooltip-element>, move to the <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element>, and then skip past any other content on the page to land on the FAB.<br /><br />Consider displaying a tooltip when the FAB is focused. This is supported on web.</p>

A focused FAB with a tooltip saying “Compose” appearing below it.

<p><span style="white-space:pre-wrap">Tooltips surface the FAB’s label when focused</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkaqbeez-03.png?alt=media

<h2><span style="white-space:pre-wrap">Layout &amp; position</span></h2>

<p>To make it easier for users of screen readers to reach a primary action such as a FAB on <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints</app-froala-tooltip-element>, consider placing the FAB in the upper left region. <br /><br />However, it’s critical to test placement options with users to see if the upper left region is the best position in all browser windows. For <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium breakpoints</app-froala-tooltip-element>, the best place for the FAB is the lower right corner of a screen.</p>

FAB in the lower right region of a small screen.

<p><span style="white-space:pre-wrap">In compact windows, place the FAB in the bottom trailing edge</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkaqbxv8-04.png?alt=media

FAB in the upper left region of a large screen.

<p><span style="white-space:pre-wrap">In expanded windows, place the FAB in the navigation rail</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkaqcdup-05.png?alt=media

<p>To ensure accessibility for keyboard users on the web, avoid positioning the FAB in a way that completely obscures the focus indicator of an actionable element. <br /><br />It’s okay to partially cover the desired element, as long as the focus indicators are still visible.</p>

FAB in the lower right region doesn’t obscure the focus indicator of an actionable icon.

<p><span style="white-space:pre-wrap">The FAB can partially cover an actionable element, as long as the focus indicator is still clearly visible</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkaqcwm1-06.png?alt=media

FAB in the lower right region obscures an actionable icon and its focus indicator.

<p><span style="white-space:pre-wrap">Don’t completely obscure an actionable element and its focus indicator</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkbecw5o-07.png?alt=media

<h2><span style="white-space:pre-wrap">Keyboard navigation</span></h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:28.4%"><p><strong>Keys</strong></p></th><th style="width:71.6%"><p><strong>Actions</strong></p></th></tr></thead><tbody><tr><th><p><strong>Tab</strong></p></th><td><p>Focus lands on the FAB</p></td></tr><tr><th><p><strong>Space</strong> or <strong>Enter</strong></p></th><td><p>Perform the default action on an item</p></td></tr></tbody></table></div>

<h2><span style="white-space:pre-wrap">Labeling elements</span></h2>

<p>The accessibility label should describe the action that the button is performing, such as <strong>Compose a new message</strong>.</p>

Accessibility label and accessibility role of a FAB.

<p><span style="white-space:pre-wrap">The accessibility label of the FAB with a pencil icon describes the action of composing a new message</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmkaqdy3m-08.png?alt=media
