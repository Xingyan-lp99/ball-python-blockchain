# Toolbars

Source: https://m3.material.io/components/toolbars
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/4dc1681d-978a-4927-9ffa-8e2bd3796f64.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Two expressive variants: <strong>docked toolbar</strong> and <strong>floating toolbar</strong></p></li><li><p>Use the vibrant color style for greater emphasis</p></li><li><p>Can display a wide variety of control types, like buttons, icon buttons, and text fields</p></li><li><p>Can be paired with FABs to emphasize certain actions</p></li><li><p>Don’t show at the same time as a navigation bar</p></li></ul>

2 variants of toolbars.

<p><span style="white-space:pre-wrap">Configurations of floating toolbars</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0aionfm-01.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/24b1bcdfc66a3784

libraryModuleType: STATUS_TABLE

<h2 id="isPasted"><span style="white-space:pre-wrap" id="isPasted">M3 Expressive update</span></h2>

<p><span style="white-space:pre-wrap" id="isPasted">The <strong>bottom app bar</strong> is no longer recommended and should be replaced with the <strong>docked toolbar</strong>, which functions similarly, but is shorter and has more flexibility. The <strong>floating toolbar</strong> was created for more versatility, greater amounts of actions, and more variety in where it's placed. </span><span style="white-space:pre-wrap" id="isPasted"><a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank" rel="noopener noreferrer">More on GM3 Expressive</a></span></p>

<p>Variants and naming:</p><ul><li><p>Added <strong>docked toolbar </strong>to replace <strong>bottom app bar</strong></p><ul><li><p>Size: Shorter height</p></li><li><p>Color: Standard or vibrant</p></li><li><p>Flexibility: More layout and element options</p></li></ul></li><li><p>Added <strong>floating toolbar</strong> with the following configurations:</p><ul><li><p>Layout: Horizontal or vertical</p></li><li><p>Color: Standard or vibrant</p></li><li><p>Flexibility: Can hold many elements and components. Can be paired with FAB.</p></li></ul></li><li><p><strong>Bottom app bar </strong>is still available, but not recommended</p></li></ul>

2 examples of toolbar variants.

<ol class="decimal"><li><span style="white-space:pre-wrap">Floating, vibrant color scheme and paired with FAB</span></li><li><span style="white-space:pre-wrap">Docked with embedded primary action instead of FAB</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0aiswog-02.png?alt=media

<h2>Differences from M2</h2>

<ul><li id="isPasted">Color: New color mappings and compatibility with dynamic color</li><li>Elevation: No shadow</li><li>Layout: Container height is taller and the FAB is now contained within the app bar container</li></ul>

M2 bottom app bar.

<p>M2: Bottom app bar had higher elevation of 8dp and didn't contain the FAB</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0e7liab-2.png?alt=media

M3 bottom app bar.

<p>M3: Bottom app bar has new colors, a taller container, no elevation or shadow, and contains the FAB</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0e7mh6v-3.png?alt=media

## Specs

<h2>Variants</h2>

2 variants of toolbars.

<ol><li><span style="white-space:pre-wrap">Docked toolbar</span></li><li><span style="white-space:pre-wrap">Floating toolbar</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma23ultc-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/j7SkkZwP6mNfPUFrpFyRIcGSsfI3_5Kv8VI0whqh3B1cGJq3v0lx_xaG3wOnjjjRl6GIEV4EZATztyOcGm6n3BbHH6QXE4KMPnSmk1EmvGpm=s2048

<h3>Baseline variant</h3>

<p>The baseline bottom app bar is no longer recommended. It should be replaced with the docked toolbar, which is very similar and more flexible.</p>

Baseline bottom app bar, which looks like the docked toolbar, but is not recommended.

<ol class="decimal"><li>Bottom app bar (not recommended)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma24egim-1-deprecated.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/tIdFhkPyYLLkFb4gUvrKPLzfIPcmAx4al6ORcGUGmS8oukJMF7ZzittOV7r-Nxwq0V63i9VTRfaVICziXGg4J8hd5TKaoZaDr28KS-7jQkI=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Variant</p></th><th style="text-align:center"><p>M3</p></th><th style="text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td><p>Docked toolbar</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td><p>Floating toolbar</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td><p>Bottom app bar</p></td><td><p>Available</p></td><td><p>Not recommended.  </p><p>Use <strong>docked toolbar</strong>.</p></td></tr></tbody></table></div>

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">Implementation differs per platform. On Jetpack Compose, the floating toolbar is a separate component from the docked toolbar and bottom app bar.</div></div></div>

<h2 id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Configurations</span></h2>

Color configuration of toolbars.

<ol class="decimal"><li id="isPasted"><span style="white-space:pre-wrap">Standard and vibrant toolbars</span></li><li id="isPasted"><span style="white-space:pre-wrap">Vertical floating toolbar</span></li><li id="isPasted"><span style="white-space:pre-wrap">Floating toolbar with FAB</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma24i061-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/o4tXTZsCpct2GOpIk9NZcIqwhbbw1CLCMMGKI8rjcbmGoiECpJUHMaKtCGRJ_bL-ngPgBlo5zJAj0wdfLm7PRdk93iZI0BvB08Ull7JZB7SqoQ=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:20.6949%"><p>Category<br /></p></th><th style="width:23.175%"><p>Configuration<br /></p></th><th style="width:25.5999%;text-align:center"><p> M3<br /></p></th><th style="width:30.4648%;text-align:center"><p>M3 Expressive<br /></p></th></tr></thead><tbody><tr><td rowspan="2" style="width:20.6949%"><p>Color<br /></p></td><td><p>Standard (default)<br /></p></td><td><p>Available as bottom app bar<br /></p></td><td><p>Available<br /></p></td></tr><tr><td><p>Vibrant<br /></p></td><td><p>--</p></td><td><p>Available<br /></p></td></tr><tr><td rowspan="2" style="width:20.6949%"><p>Floating toolbar layout<br /></p></td><td><p>Horizontal (default)<br /></p></td><td><p>--</p></td><td><p>Available<br /></p></td></tr><tr><td><p>Vertical<br /></p></td><td><p>--</p></td><td><p>Available<br /></p></td></tr><tr><td><p>Other elements</p></td><td><p>With FAB</p></td><td><p>Available as bottom app bar</p></td><td><p>Available*</p></td></tr></tbody></table></div>

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">*Implementation differs per platform. On Jetpack Compose, floating toolbar with FAB is <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#HorizontalFloatingToolbar(kotlin.Boolean,androidx.compose.ui.Modifier,androidx.compose.material3.FloatingToolbarColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.material3.FloatingToolbarScrollBehavior,androidx.compose.ui.graphics.Shape,kotlin.Function1,kotlin.Function1,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,kotlin.Function1)" target="_blank" rel="noopener noreferrer">fully supported</a>. On other platforms, each component needs to be added separately. </div></div></div>

<h2>Tokens &amp; specs</h2><p>Browse the component elements, attributes, tokens, and their values. <a href="/m3/pages/toolbars/specs#ad142675-3e3b-43b8-ba53-12c1f0b7138d" target="_blank">Jump to baseline bottom app bar specs</a></p>

resourceName: designSystems/20543ce18892f7d9/components/2956a7939bf0879c

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Toolbar - Color - Standard', 'Toolbar - Color - Vibrant', 'Toolbar - Docked', 'Toolbar - Floating', 'Toolbar - Floating - FAB'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['[Deprecated] App bar - Bottom', 'Toolbar - Color - Standard', 'Toolbar - Color - Vibrant', 'Toolbar - Docked', 'Toolbar - Floating', 'Toolbar - Floating - FAB'], 'hideSearchField': False, 'hideVersionName': True}

<h2><span style="white-space:pre-wrap" id="isPasted">Anatomy</span></h2>

2 elements of a toolbar.

<ol class="decimal"><li><span style="white-space:pre-wrap">Container</span></li><li><span style="white-space:pre-wrap">Placed components</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma24poz2-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/q5KTYC5SjXAnSvSVvP72h2InKksCupfh4xqfQsa8eqO3ImcNxSiNEvyVzwrM54a_bgMyYUG2oOrljsquGFjeuEhoQ-lfYIhLhcYRjTURpOs0mQ=s2048

<h3 id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Flexibility &amp; slots</span></h3>

<p id="isPasted">When configuring a toolbar, think of it as a container with several slots. </p><p>Each slot can be a different element. The most common elements are <app-froala-tooltip-element description="When configuring a toolbar, think of it as a container with several slots.  Each slot can be a different element. The most common elements are icon buttons, buttons, and text fields." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/specs" should-open-link-in-new-tab="true">icon buttons</app-froala-tooltip-element>, <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/specs" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Text fields let users enter text into a UI." link-label="More on text fields" link-url="/m3/pages/text-fields/overview" should-open-link-in-new-tab="true">text fields</app-froala-tooltip-element>.</p>

A toolbar with 5 slots, conceptual spaces for UI elements, next to each other.

<p><span style="white-space:pre-wrap">A toolbar is essentially a container with configurable slots</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma25cmf1-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/U8tAffspM1NK0nWpYaxRxJHvPJOXWBX8GEuuEMeW6b-RjRo7OKtlMaYohHO-8Rn9QzwodfT_aJgLSocPQnHQDqhiMpfonWKsTd8XBUj-kKs=s1352

<h2><span style="white-space:pre-wrap" id="isPasted">Color</span></h2>

<p>Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

<h3><span style="white-space:pre-wrap" id="isPasted">Standard</span></h3>

4 color roles in the standard color scheme  of the floating toolbar in light and dark scheme.

<p><span style="white-space:pre-wrap">Standard color schemes and icon button types:</span></p><ol class="decimal"><li><span style="white-space:pre-wrap">Surface container</span></li><li id="isPasted"><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">Filled button (Primary, On primary)</span><br /></span></li><li><span style="white-space:pre-wrap">Toggle tonal button (Secondary container, On </span><span style="white-space:pre-wrap">secondary container)</span></li><li><span style="white-space:pre-wrap">Standard button (Primary)</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma25fg6c-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/vnb-hvZkhHov6Q_xpnqsRpE-v1-ahJAuOOAS49Uw7K1JgYNot331UJ_viioRQnCmG5c_kqdBCgTXYkFkIfdYmd2lUUnIiqJes4VaQa_i30dvYg=s2048

<h3><span style="white-space:pre-wrap" id="isPasted">Vibrant</span></h3>

4 color roles in the vibrant color scheme of the floating toolbar in light and dark scheme.

<p><span style="white-space:pre-wrap">Vibrant color scheme and icon button types:</span></p><ol class="decimal"><li><span style="white-space:pre-wrap">Primary container</span></li><li><span style="white-space:pre-wrap">Filled button (Primary, On primary)</span></li><li><span style="white-space:pre-wrap">Toggle tonal button: (Surface container, On surface)</span></li><li><span style="white-space:pre-wrap">Standard button (On primary container)</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma25hban-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/MSHjbfagavP64_aZ8he_iw3phiUh6IkZDUjRhPkoMvHcSGsAh-0j3khoUTMDeaPdCVcRwhCp9XyMVOQuvKVvIDxcYcqgTe1tZ5YBzAxchYzx=s2048

<h2><span style="white-space:pre-wrap" id="isPasted">Measurements</span></h2>

<p><span style="white-space:pre-wrap" id="isPasted">By default all toolbars are 64dp high, center-aligned, have equal padding between items, and have a minimum outside padding of 16dp.</span></p>

<h3><span style="white-space:pre-wrap" id="isPasted">Docked toolbar</span></h3>

Default internal padding of a docked toolbar.

<ol class="decimal"><li>Default margins and padding</li><li>Margins and padding with leading, middle, and trailing content</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma25j41t-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Eovie9hEPA5n7suVT8sw4C5TaWOwLmXIl0J3WBMBVOcBFDGyGqhwTTePHEyqXbPNsWb4kH1PH0QZ0llhRfnV9iozSM-bZFjevV4HNZio2qCD=s2048

2 docked toolbars with different margins and alignment.

<p><span style="white-space:pre-wrap">Alignment and padding can be configured to create unique layouts:</span></p><ol class="decimal"><li><span style="white-space:pre-wrap">Left and right alignment</span></li><li><span style="white-space:pre-wrap">Center-aligned, 8dp padding between items</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma25jqfl-08-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Vsgw_yvIWA9pxAKEs4qmxtfhofUIoJnSXq6bO3_6v_OmMq4BZhQnS5FaT70GZEHJOzMm7DPuYd-ZUVsVtbJ1WuLqVCQ9khS6P6J8EMzlyOo=s2048

<h3><span style="white-space:pre-wrap" id="isPasted">Floating toolbar</span></h3>

Diagram noting margin around edge of floating toolbar.

<p><span style="white-space:pre-wrap">Default padding of floating toolbar</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma25l6kh-09-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/BmOWzjQZ3a-oyRtJT94Nez52vT0DHXNgDWueCiIVnteA35K89UKvwAP_gs8fdqn450QEN9oEnw_yWK0oIKbqEZ9xhqope0Jt4C0lM83X4pc3ng=s2048

Diagram noting layout measurements.

<p><span style="white-space:pre-wrap">Floating toolbar size and padding measurements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma25numd-10-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/OStcy-GlT-NRB63inDLnhvNm3czBqigQcIhixAV3N7fMvikSrBtiJtNJc_r0m8yP6nyxDkzhLQnsxBdp_FG6qDARNyB0S52U-CDXNkkG89E=s2048

Diagram noting layout margins.

<p><span style="white-space:pre-wrap">Floating toolbar margins</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma25or07-11-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/l1zIH0wA5J3kRRwuwvmIpG4gmlFXXYK88L4lF0q5vQ0_ThjPiPwpPJk0mOT8zbMyO20rMum-TPkHfY651sPtrWzVPiiVl7MXQxtWq3IthryT=s2048

<hr /><h2>Bottom app bar (baseline)</h2>

Diagram of bottom app bar indicating the container.

<ol class="decimal"><li><span style="white-space:pre-wrap">Container</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma25qmnu-12-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/XW6h1Afu7o0EPJEU5KC5OEODx1r67sQMqU9pUmqzyOAPy1b_y8-pMDrw-GqoWeSbEXhBR7cA_qDpTDdG8qwlAYoSH0Vc9jh5lviGtvZ76pekyw=s2048

<h3>Tokens &amp; specs</h3>

<p>Bottom app bar tokens are in one token set.</p>

resourceName: designSystems/20543ce18892f7d9/components/2956a7939bf0879c

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Bottom app bar (baseline)', 'Toolbar - Docked', 'Toolbar - Floating', 'Toolbar - Color - Standard', 'Toolbar - Color - Vibrant', 'Toolbar - Floating - FAB'], 'tokenSetOrder': ['Bottom app bar (baseline)', 'Toolbar - Docked', 'Toolbar - Floating', 'Toolbar - Color - Standard', 'Toolbar - Color - Vibrant', 'Toolbar - Floating - FAB']}

<h3>Color</h3>

<p>Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview">Learn more about design tokens</a><br /></p>

Diagram of bottom app bar indicating its color mappings.

<p>Bottom app bar color role used for light and dark themes:</p><ol class="decimal"><li><p>Surface container</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma25vwtc-13-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/RDMrnLfQpoptezvVbHosgCQV_qq-MEVY3hKWH4U1fo8wYZLg0Zv4Z1jqiQT1FxojqUYoCEZ8lekjZ3SYJe3-vuO50wNCzsNx7lBpp6iWgqN0rQ=s2048

<h3>Measurements</h3>

Diagram showing layout values and paddings for bottom app bar.

<p>Bottom app bar padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma25wn0p-14-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/42HaRTtyV44uEgw2rZzgGwWNqlOy1g0mCiaUjMy7iuiG2lAJ4ACu5xe9PEJgOfE2PFIJ_8TjIRqrk75Wc2YmtrtcrYklJzE3nSV8HbBbW7Y=s2048

<h3>Common layouts</h3>

Side by side view of bottom app bars in different configurations.

<ol class="decimal"><li id="isPasted">Icon buttons and FAB</li><li>Icon buttons and no FAB</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma25xkg5-15-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/JvPTixMCyejczwwssuEezKtZO-2y_RmCjTIrMEpHFu5HOAApXlYpEt-Pq3GV4Bd1LJQlgRd4O3PPpK7YpOkaQMUvEo3Sg2E1I8iLh56BNKvC=s2048

## Guidelines

5 toolbars of various colors, elements, and actions.

<p><span style="white-space:pre-wrap">Toolbars can be used for a wide variety of use cases</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7xi1w6d-01.png?alt=media

<h2 id="isPasted">Usage</h2>

<p><span style="white-space:pre-wrap" id="isPasted">Use a toolbar to provide actions related to the current page. </span></p><p><span style="white-space:pre-wrap">Toolbars can contain many actions and can scale to show more actions in larger windows.</span></p>

Vibrant toolbar at bottom of mobile screen.

<p><span style="white-space:pre-wrap">A toolbar provides actions related to the current page</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0akotbi-02.png?alt=media

<p>There are two variants of toolbars:</p><ul><li><p><strong>Docked toolbar</strong> <br />Spans the full width of the window. It’s best used for global actions that remain the same across multiple pages.</p></li></ul><ul><li><p><strong>Floating toolbar</strong> <br />Floats above the body content. It’s best used for contextual actions relevant to the body content or the specific page.</p></li></ul><p>The baseline <strong>bottom app bar </strong>is no longer recommended, but is still supported.</p>

Docked toolbar example.

<p><span style="white-space:pre-wrap">Docked toolbar shows global controls</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0akx0bq-03.png?alt=media

Floating toolbar example.

<p><span style="white-space:pre-wrap">Floating toolbar show controls relevant to the current page</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0akxxgm-04.png?alt=media

<p>When actions don’t fit in a toolbar, add a <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element>.</p>

Toolbar showing local navigation.

<p><span style="white-space:pre-wrap">Toolbar actions can open a menu</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2ytl4us-05.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">There are two color configurations:<br /></span></p><ul><li><span style="white-space:pre-wrap" id="isPasted"><strong>Standard</strong> </span><br /><span style="white-space:pre-wrap">A low-emphasis color scheme best used for focusing attention on the body content.<br /></span></li></ul><ul><li><span style="white-space:pre-wrap" id="isPasted"><strong>Vibrant</strong> </span><br /><span style="white-space:pre-wrap">A high-emphasis color scheme that draws attention to the controls. It can also indicate a temporary change in the page behavior, such as entering edit mode.</span></li></ul><p><span style="white-space:pre-wrap">Consider using alternative color roles to create greater or lesser emphasis depending on the needs of the app. Experiment with different color roles to achieve different effects. </span></p>

Toolbar with low-emphasis controls.

<p><span style="white-space:pre-wrap">Use the standard color scheme to draw focus to content outside the toolbar</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0al28lo-06.png?alt=media

Toolbar with high-emphasis controls.

<p><span style="white-space:pre-wrap">Use the vibrant color scheme to emphasize controls or actions</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0al3avf-07.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Toolbars &amp; navigation bars</span></h3>

<p>The toolbar and <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element> are both placed at the bottom of the window, so should <strong>not</strong> be shown at the same time. Show the navigation bar on primary pages, and toolbars on subsequent pages with actions.</p>

A navigation bar shown on the main email Inbox page, and a toolbar shown when reading the email.

<ol class="decimal"><li><span style="white-space:pre-wrap">Navigation bar on a primary page<br /></span></li><li><span style="white-space:pre-wrap">Toolbar on a secondary page with contextual actions</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0al4vpg-08.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">Floating toolbars can be used as tabs between related subsequent pages in the product hierarchy. </span></p><p><span style="white-space:pre-wrap">This helps group similar pages together, and shows that the selection affects the body content underneath.</span></p>

Floating toolbar with secondary navigation labels.

<p><span style="white-space:pre-wrap">Keep navigation distinct, and use a toolbar to display local navigation on a specific page</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0alklw0-09.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">Consider the existing app hierarchy when using a toolbar for local navigation. </span><br /><br /><span style="white-space:pre-wrap">Avoid redundant or confusing navigation combinations in the same view.</span></p>

Floating toolbar with secondary navigation labels displaying above a bottom navigation bar.

<p><span style="white-space:pre-wrap">Don’t show a navigation bar and a toolbar with navigation controls at the same time</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0aln2r9-10.png?alt=media

<h2 id="isPasted">Anatomy</h2>

Diagram of toolbar layouts.

<ol><li><span style="white-space:pre-wrap">Container<br /></span></li><li><span style="white-space:pre-wrap">Elements</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7xiiwbe-11.png?alt=media

<h3 id="isPasted">Container</h3><p><span style="white-space:pre-wrap" id="isPasted">The docked toolbar’s container spans the full width of the window. <br /><br />Avoid applying rounded corners to the container. This can imply the container expands or changes upon interaction.</span></p>

Docked toolbar with square corners.

<p><span style="white-space:pre-wrap">Use straight corners for docked toolbars</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0als248-12.png?alt=media

Docked toolbar with rounded corners.

<p><span style="white-space:pre-wrap">Avoid modifying the container shape</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0alr7n0-13.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">As long as there's a minimum of 16dp padding on the leading and trailing edge, arrange controls inside however you see fit. The 32dp padding between items is just the default. </span><br /><br /><span style="white-space:pre-wrap">All elements need a minimum 48x48dp target area to be accessible.<br /><br />Be cautious of including too many controls as it can be overwhelming.</span></p>

Docked toolbar with too many controls.

<p><span style="white-space:pre-wrap">Don’t overwhelm people with too many controls</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0altzpa-22.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">The floating toolbar’s container should be fully visible on screen. If more actions are needed, use an overflow menu.</span></p>

Floating toolbar with overflow menu icon.

<p><span style="white-space:pre-wrap">Choose the most essential actions to show on screen by default</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0alvr9d-14.png?alt=media

Floating toolbar that expands off edge of screen.

<p><span style="white-space:pre-wrap">Floating toolbars shouldn’t exceed the edge of the window or pane</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0alwqwe-15.png?alt=media

<h4>Elevation</h4><p>Floating toolbars have elevation by default. <br /><br />If the content beneath the toolbar is visually distinct, elevation can be removed.</p>

Vibrant floating toolbar that's easy to see in front of a neutral text background.

<p>The elevation on floating toolbars can be removed if on a visually distinct background</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7xiazxd-17.png?alt=media

<h3 id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Flexibility &amp; slots</span></h3><p>When configuring a toolbar, think of it as a container with several slots.<br /><br />These slots can be populated by <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element>, <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon buttons</app-froala-tooltip-element>, images, <app-froala-tooltip-element description="Text fields let users enter text into a UI." link-label="More on text fields" link-url="/m3/pages/text-fields/overview" should-open-link-in-new-tab="true">text fields</app-froala-tooltip-element>, or any kind of custom component.<br /><br /><span style="white-space:pre-wrap">Icon buttons provide an even hierarchy of controls. Mixing in a filled icon button can help add emphasis to a single action.</span></p>

5 toolbars with slots, and various combinations of buttons, icon buttons, filled icon buttons, and text fields.

<p>Toolbars are made of slots that can contain many kinds of actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0aly7tp-16.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">Visually emphasizing a single action more than others is an effective way to create hierarchy and guide people to controls they use most often. Avoid emphasizing more than one action at a time.<br /><br />Some common ways to add emphasis to toolbar actions include:<br /></span></p><ul><li>Use different <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon button</app-froala-tooltip-element> color styles, such as filled, tonal, and standard</li><li>Customize the <app-froala-tooltip-element description="Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme." link-label="More on color roles" link-url="/m3/pages/color-roles/" should-open-link-in-new-tab="true">color roles</app-froala-tooltip-element> of a single action, such as a primary or secondary palette</li><li><span style="white-space:pre-wrap" id="isPasted">Use wide and narrow icon buttons <br /></span></li><li>Pair the toolbar with a <app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/m3/pages/fab/overview" should-open-link-in-new-tab="true">FAB</app-froala-tooltip-element></li></ul>

2 floating toolbars, 1 with a filled action button and 1 paired with a FAB.

<p><span style="white-space:pre-wrap">Two different ways to create a high emphasis action in toolbars</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0am06ae-18.png?alt=media

Floating toolbar with primary action and FAB.

<p><span style="white-space:pre-wrap">Don’t emphasize multiple buttons with bold, primary colors, such as a button and FAB together. Emphasize one action at a time.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0am2tq8-19.png?alt=media

Floating toolbar with different control designs.

<p><span style="white-space:pre-wrap">Avoid mixing too many different controls in the same toolbar. A consistent control design keeps things clear.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0am3wil-20.png?alt=media

<p id="isPasted">Avoid using square icon buttons in floating toolbars. Their square shape conflicts with the fully-rounded shape of the floating toolbar container.</p><p>Square buttons can be used in the docked toolbar.</p>

A floating toolbar, which is rounded, with squared icon buttons inside.

<p>Don’t use square filled icon buttons in floating toolbars</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7xigk3q-22.png?alt=media

<h3 id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Floating toolbar with FAB</span></h3><p>A <app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/m3/pages/fab/overview" should-open-link-in-new-tab="true">FAB</app-froala-tooltip-element> can be placed next to a floating toolbar to present one high-priority action alongside a unified set of toolbar actions.</p><p><span style="white-space:pre-wrap">Use a FAB for the highest-priority action in the view, or to complement the controls.</span></p>

3 toolbars paired with FABs.

<p><span style="white-space:pre-wrap">Floating toolbars can be paired with FABs</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0am631l-21.png?alt=media

<h2>Position &amp; orientation</h2>

<p><span style="white-space:pre-wrap" id="isPasted">Only place docked toolbars at the bottom of the window. </span></p><p><span style="white-space:pre-wrap">If using other bottom-aligned elements, such as a navigation bar, don't use a docked toolbar.</span></p>

Docked toolbar on mobile.

<p><span style="white-space:pre-wrap">Docked toolbars are always at the bottom of the window</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0ama5z3-22.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">Floating toolbars can be horizontal or vertical. <br /><br />Horizontal toolbars should have a minimum 16dp margin from the edge of the window.</span></p>

Floating toolbar on mobile.

<p><span style="white-space:pre-wrap">Horizontal floating toolbars should be at least 16dp from the edge of the window</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0amca2n-23.png?alt=media

<p>In larger breakpoints, floating toolbars can be vertical and placed on either side of the screen.</p><p>Vertical toolbars should have a minimum 24dp margin.</p>

Vertical floating toolbar with 24dp margin.

<p><span style="white-space:pre-wrap">Maintain at least a 24dp margin for vertical toolbars</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7ximrxw-26.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">To keep vertical toolbars compact, don’t use wide icon buttons. </span></p><p><span style="white-space:pre-wrap">Use narrow or default icon buttons instead.</span></p>

Toolbar showing local navigation.

<p><span style="white-space:pre-wrap">Using wide buttons with vertical toolbars can unnecessarily widen toolbar containers and hide other UI elements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0amgeqc-24.png?alt=media

<p>Vertical toolbars should be positioned opposite the <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element> to balance out the screen and keep actions easy to access.</p><p>When showing a navigation rail and vertical floating toolbar at once, use the centered configuration of the navigation rail.</p>

Large screen UI showing both a navigation rail and vertical floating toolbar.

<p>When a nav rail is visible, the floating toolbar should be vertical on the opposite edge of the window</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0amkwhr-TBD.png?alt=media

<h2>Adaptive design</h2>

<p>Adaptive design allows an interface to respond or change based on context, such as the user, device, and usage. <a href="/m3/pages/layout-overview/adaptive-design" target="_blank">More on adaptive design</a></p>

<h3>Resizing</h3>

<h4>Docked</h4><p>The docked toolbar should always span 100% of the screen width.</p><p>In <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoints</app-froala-tooltip-element>, elements in the toolbar should be evenly spaced.</p><p>In <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium breakpoints</app-froala-tooltip-element> and larger, adjust the padding between controls to create a comfortable layout. This can be achieved by: </p><ul type="disc" style="list-style-type:disc"><li><p>Centering all elements</p></li><li><p>Customizing to center a key action, and aligning other elements to the edges</p></li></ul>

Docked toolbar with evenly spaced elements.

<p><span style="white-space:pre-wrap">Docked toolbar items should be evenly spaced in compact windows</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma2vff01-29.png?alt=media

Docked toolbar with centered elements.

<p>In medium breakpoints and larger, create a spacious layout by centering all elements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma6y2uq6-30.png?alt=media

Docked toolbar with central action and some elements pushed to the edge.

<p><span style="white-space:pre-wrap">Align controls to the edge of the screen to make them easier to reach on tablets, and to better highlight a primary action in the middle</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma6y2g0q-31.png?alt=media

<p>On web and large screens, the docked toolbar can be rounded. Dividers can be used to organize large amounts of items. Only shrink the height and use extra small buttons if vertical space is limited.</p>

Docked toolbar with 15 actions for text editing on large screens, organized with dividers.

<p>On web and other large screens, docked toolbars can be rounded and placed in different parts of the page</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmbv5jv5l-33%20Old.png?alt=media

<h4>Floating</h4><p>The container should only be as big as needed to hold the items inside before reaching the 16dp margin.</p><p>If there’s not enough space for all items, put them in an overflow menu in the trailing slot. As the breakpoint expands, more actions can be revealed.</p><p>The floating toolbar width can also be capped to keep it smaller and hide more elements.</p>

Floating toolbar in compact window with excess padding.

<p><span style="white-space:pre-wrap">Don’t add extra space to a toolbar beyond its necessary items</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma1lkstz-32.png?alt=media

Floating toolbar in expanded window class.

<p><span style="white-space:pre-wrap">At larger screen sizes, the container can display more controls before hitting the 16dp margin</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma1lm7ro-33%20(1).png?alt=media

<p id="isPasted">Vertical toolbars aren’t recommended for compact windows.<br /><br />They take up a significant area of the screen and may feel visually overwhelming, especially on screens with complex layouts.</p><p><span style="white-space:pre-wrap" id="isPasted">Only use them when the screen is simple or when the toolbar has a few controls.</span></p>

Vertical toolbar in a compact window.

<p><span style="white-space:pre-wrap">Vertical toolbars can cover important content in compact windows</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7xmqa2l-34.png?alt=media

<h3>Presentation</h3>

<p>In larger breakpoints, floating toolbars can be aligned to opposite edges of the screen so they're easy to reach and group similar actions. For example, consider placing the undo and redo actions in one toolbar, and editing controls like highlight, erase, and select in another. Stylistic differences can help emphasize each toolbar’s purpose and clarify hierarchy.</p>

2 toolbars, each with distinct stylistic treatment and actions.

<p>Multiple toolbars with different stylistic treatments can create hierarchy and distinguish different kinds of actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0amsqw6-29.png?alt=media

<p>Don’t use multiple toolbars in compact windows. There typically isn’t enough room on screen. <br /><br />Instead, use one toolbar for all actions.</p>

Multiple toolbars in a compact window.

<p><span style="white-space:pre-wrap">Avoid using multiple toolbars in smaller windows</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7xmw01r-36.png?alt=media

<p>Actions at the trailing edge of the toolbar can collapse into an overflow menu at smaller breakpoints, and become visible again at larger sizes. </p>

App bar resizing to wider view.

<p><span style="white-space:pre-wrap">Actions at the trailing edge collapse into an overflow menu</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma1lvic4-GM3_Adaptive_ToolBar_Guidelines_37_IA_V01.mp4?alt=media

<h3>Right-to-left languages</h3><p>In right-to-left (RTL) languages, mirror individual items that need it, like icons and text direction. If the order of actions is important, flip the order of the actions as well.</p>

Next button is on trailing edge for a LTR language.

<p>In LTR languages, the <strong>Next</strong> button is intentionally placed on the trailing (right) edge</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7xmygdb-37.png?alt=media

Next button is now on the trailing edge, at left, for RTL language.

<p>In RTL languages, reverse the order so <strong>Next</strong> remains on the trailing edge when flipped, now on the left. Text is not translated to illustrate mirroring.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7xmz6n4-38.png?alt=media

<h2>Behavior</h2>

<h3 id="isPasted">Scrolling</h3><p><span style="white-space:pre-wrap">Docked toolbars can either remain on the screen during scroll, or animate offscreen.</span></p>

Docked toolbar animating off screen.

<p>Docked toolbars can animate offscreen</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6kw6oe9-Toolbar%20GUidelines%2031a%20-%20RENDER%202x.mp4?alt=media

<p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Floating toolbars can remain on the screen, animate offscreen, or collapse into a single, high-emphasis action on scroll.</span></p>

Floating toolbar animating off screen.

<p>Floating toolbars can animate off screen</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6kwfvv5-Toolbar%20Guidelines%2032a%20-%20RENDER.mp4?alt=media

<p>On Jetpack Compose, the floating toolbar can collapse to a FAB or key action on scroll. </p>

Floating toolbar with several actions animating on scroll to hide all actions except the center one.

<p>Floating toolbars can be customized to do other actions on scroll, like collapse into a single action</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6kwpm0p-Toolbar%20Guidelines%2033a-%20RENDER%202x.mp4?alt=media

<p>Don't collapse actions and scroll at the same time.</p>

A toolbar collapsing to one action, and moving off screen when the page is scrolled.

<p>Toolbars shouldn't both collapse and transition off page</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm9ipmok3-GM3_Expressive_Toolbar_Guidelines_42_IA_v05.mp4?alt=media

## XR

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">This is a rapidly changing space. Guidelines are primarily intended for designers at this time. Find what’s implemented in code in the <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank" rel="noopener noreferrer">design kit</a>.</div></div></div>

<p>Extended reality (XR) interfaces have special design requirements, like showing apps in 3D space. Material has an XR-specific toolbar with custom specs and guidance. Read <a href="https://developer.android.com/design/ui/xr/guides/foundations" target="_blank" rel="noopener noreferrer">XR developer documentation</a> for more details.</p>

<h2>Variants</h2><p>There is one toolbar <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels. " link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiter</app-froala-tooltip-element>. It closely aligns with the <app-froala-tooltip-element description="Floating toolbars float on top of page content and can provide contextual, dynamic actions." link-label="More on toolbars" link-url="/m3/pages/toolbars/overview" should-open-link-in-new-tab="true">floating toolbar</app-froala-tooltip-element>. It can be configured to be horizontal or vertical.</p>

Horizontal and vertical toolbar orbiters.

<ol class="decimal"><li id="isPasted">Horizontal floating toolbar</li><li>Vertical floating toolbar</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmffkg5cl-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/NPkjrCVlcMYcFjhskyX68C6Ajzx22mjakvKDZAVUHBJw8EP_xCeJMvYK864Ddwt9X84QyVHllfVaEdPwFYAmtqjrhAQI_fh7tgy9m0nu5U30lg=s2048

<h2>Anatomy</h2>

2 elements of a toolbar orbiter: container and placed components. 

<ol class="decimal"><li id="isPasted">Container</li><li>Placed components</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmffkgmzs-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/x86RozsiCz4_T4cUwrQkf3UJneRZFflJsRYhfLXCzxOVE5zBfBtXAYmBQ9ri8SlRvOTv-XyBPFsGN5SYSiq_YuEOZYq0ahBdmGs4PssOnO-6=s1024

<h2>Color &amp; elevation</h2><p>XR uses color to communicate the elevation of UI elements and orbiters. With <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation" target="_blank" rel="noopener noreferrer">spatial elevation</a>, the toolbar displays above the <app-froala-tooltip-element description="In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content. " link-label="More on spatial panels" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels" should-open-link-in-new-tab="true">spatial panel</app-froala-tooltip-element> on the Z-axis. Elevated toolbars can use any of these color options:</p>

4 versions of toolbar elevation color strategy.

<ol class="decimal"><li id="isPasted">Surface container</li><li>Surface container high</li><li>Surface container highest</li><li>Tertiary container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmffkgx1z-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/OILSCxFAWoe1XfIXg31uAZc78UpNfv62wl-DJVb4TAdCizAikgblMpziUQPW1muEROAz91Ae36E5OpoddORkfhpjpFN272ft671jgrL9wSkgaw=s2048

<h2>Measurements</h2>

Diagram with measurements for toolbar orbiters.

<p>Measurements for toolbar orbiters</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmffkhel2-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/syZmjQHwtPXmvN0xfW_CSo3XrQw2K1PuwEfevjaOJfRXJSt3F1jWtQ6tDNyTxyByiw1I8LHGeYrGJc2zE43QZsIAAckSsTMhOPawWVVLDrE=s2048

Diagram with 12dp padding for toolbar orbiters.

<p>Padding for toolbar orbiters</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmffkhmg5-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/sgQJWHiCNlNhFSu2kBf-ju1LPD-IIM0Qr0X7z2-IpqNJ1yhhZ6QWyEjcNEsMDv8aBSvxBrShLl-F1NjGmhSTmy-Iq7zXkarK1tBElHgpOMU=s2048

<h2>Usage</h2><p>A toolbar can appear in an <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels. " link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiter</app-froala-tooltip-element> for a more immersive experience. Currently, this spatial capability is only available in <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components." link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element>. In <app-froala-tooltip-element description="Home space is compatible with mobile and large screen apps, but doesn’t support spatial components." link-label="More on home space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">home space</app-froala-tooltip-element>, use a regular toolbar on the same plane as the body content to mimic a 2D experience.</p>

Animation showing a toolbar changing from 2D to 3D.

<p>A toolbar’s behavior and placement changes from a 2D to a 3D experience</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmf2kzdta-toolbars-xr-06.mp4?alt=media

<h2>Behavior</h2>

<h3>Local context (recommended)</h3><p id="isPasted">When placed in local context, the toolbar orbiter is centered at the bottom of the spatial panel it controls. </p><p>It repositions in response to layout or content changes.</p>

A toolbar orbiter placed in local context.

<p>In most cases, toolbars should be placed in local context. The orbiter is centered and anchored to the bottom of the panel it controls.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmf2kzsyd-toolbars-xr-07.mp4?alt=media

<h3>Global context</h3><p id="isPasted">When placed in global context, the toolbar orbiter is centered at the bottom of the app. </p><p>It stays anchored to the app during layout or content changes. </p><p><br /></p>

A toolbar orbiter placed in global context.

<p>In global context, toolbar orbiters are centered and anchored to the bottom of the app. This use case is less common, as toolbars usually contain actions that control a specific panel.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmf2l0gt9-toolbars-xr-08.mp4?alt=media

<h3>Expand &amp; collapse</h3><p id="isPasted">Toolbar orbiters with more than five items can expand and collapse to reveal or hide additional content.</p><p>When a toolbar orbiter expands, it stays within the bounds of the adjacent spatial panel.</p><p>Alternatively, more complex toolbars can be split into multiple toolbars.</p>

A spatial panel with a Google document has a toolbar orbiter that expands from 5 to 10 items.

<p>Toolbar orbiters can expand to reveal additional content, but should stay within the bounds of the adjacent spatial panel</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmf2l10hs-toolbars-xr-09.mp4?alt=media

<h3>Additional toolbars</h3><p>In some cases, full space apps can have more than one toolbar orbiter, placed in either global or local context. </p>

An app switches between 1 and 2 toolbar orbiters.

<p>Limit the use of multiple toolbars to rare cases when additional spatialization improves usability</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmf2l1cvh-toolbars-xr-10.mp4?alt=media

<h2>Placement</h2>

<h3>Offset &amp; inset positioning</h3><p>In full space, a toolbar orbiter can be positioned adjacent to or overlap a spatial panel. </p>

Toolbar orbiter with offset positioning.

<p id="isPasted">The recommended toolbar orbiter position from the spatial panel is: </p><ul><li>Offset by 20dp or </li><li>Inset by 12dp</li></ul><p><br /></p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmemeu04x-11-do.png?alt=media

Toolbar orbiter with inset positioning above 12dp that obstructs content on the spatial panel. 

<p>To prevent content obstruction, don’t overlap the toolbar orbiter and spatial panel above a 12dp inset threshold</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmemevhx8-12-don't.png?alt=media

<h3>Horizontal alignment</h3>

A horizontal toolbar orbiter placed within the bounds of its spatial panel.

<p>Always align the toolbar orbiter within the horizontal bounds of nearby spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmemey1hz-13-do.png?alt=media

A horizontal toolbar orbiter that extends beyond the width of its spatial panel.

<p id="isPasted">The toolbar orbiter shouldn’t exceed the width of adjacent spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmemez2e1-14-don't.png?alt=media

<h3>Vertical alignment</h3>

A vertical toolbar orbiter placed within the bounds of its spatial panel.

<p>Always align the toolbar orbiter within the vertical bounds of nearby spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmemf0q6h-15-do.png?alt=media

A vertical toolbar orbiter that extends beyond the height of its spatial panel.

<p id="isPasted">The toolbar orbiter shouldn’t exceed the height of adjacent spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmemfyo8f-16-don't.png?alt=media

<h3>Spatial panel alignment</h3><p>By default, toolbar orbiters are center-aligned to the spatial panel. Their placement can be adjusted to accommodate specific user needs, such as improved ergonomics or <a href="/m3/pages/understanding-layout/bidirectionality-rtl" target="_blank" rel="noopener noreferrer">right-to-left (RTL) languages</a>.</p>

Toolbar orbiter alignment options in relation to spatial panels.

<p>Depending on the configuration (horizontal or vertical) of the toolbar orbiter, it can align to the center, left, right, top, or bottom of a spatial panel</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmemfvpq3-17.png?alt=media

<p>Avoid placing a vertical toolbar orbiter between spatial panels. <br /><br />This negatively affects the interface structure and can make it difficult to find.</p>

A vertical toolbar orbiter is placed between 2 spatial panels.

<p>Don't place a vertical toolbar orbiter between spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmemfx943-18-don't.png?alt=media

<h2>Accessibility considerations</h2><p><a href="https://developer.android.com/design/ui/xr/guides/get-started#make-app" target="_blank" rel="noopener noreferrer">XR accessibility</a> guidelines are still evolving. XR toolbars should follow applicable Material <a href="/m3/pages/toolbars/accessibility" target="_blank" rel="noopener noreferrer">toolbar accessibility standards</a>.</p>

## Accessibility

<h2 id="isPasted">Use cases</h2><p><span style="white-space:pre-wrap" id="isPasted">People should be able to the following with assistive technology:<br /></span></p><ul><li><span style="white-space:pre-wrap" id="isPasted">Navigate and activate any actions in the toolbar<br /></span></li><li><span style="white-space:pre-wrap" id="isPasted">Select a destination from a menu<br /></span></li><li><span style="white-space:pre-wrap" id="isPasted">Activate a back button<br /></span></li><li><span style="white-space:pre-wrap" id="isPasted">Maintain access to toolbar controls when the content is scrolled or collapsed</span></li></ul>

<h2 id="isPasted">Interaction &amp; style</h2><p><span style="white-space:pre-wrap" id="isPasted">The toolbar has no interactions by default. All interactions are with the elements placed inside. </span></p>

<p id="isPasted"><span style="white-space:pre-wrap"><strong>Touch</strong></span></p><ul><li><span style="white-space:pre-wrap" id="isPasted">When tapping on an icon button in the toolbar, a touch ripple appears, indicating interaction feedback.</span></li></ul>

An animation of the user tapping on an action item and the ripple effect being shown.

<p>Touch: Tap</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma798ukw-GM3_Toolbar_Accessibility_1_IA_v02.mp4?alt=media

<p id="isPasted"><strong>Cursor</strong></p><ul><li><span style="white-space:pre-wrap" id="isPasted">When hovered, the hover state provides a visual cue to the user that the element is interactive. <br /></span></li><li><span style="white-space:pre-wrap" id="isPasted">When clicked (in both active and inactive states), a ripple appears, showing the user feedback.</span></li></ul>

A mouse hovering over a button in the top app bar, then clicking.

<p>Cursor: Hover, Click</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma7996zt-GM3_Toolbar_Accessibility_2_IA_v02.mp4?alt=media

<h3 id="isPasted">Initial focus</h3><p><span style="white-space:pre-wrap" id="isPasted">Focus lands on the first interactive element. </span></p><p><span style="white-space:pre-wrap">Use <strong>Tab</strong> to navigate through all other actions.</span></p>

Navigating the top app bar using arrow or tab on a keyboard.

<p><span style="white-space:pre-wrap">Use <strong>Tab</strong> to navigate through interactive elements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0anu1gy-3.png?alt=media

Activating actions in the top app bar using space or enter on a keyboard.

<p><span style="white-space:pre-wrap">Use <strong>Space</strong> or <strong>Enter</strong> to activate actions</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0anv4t7-4.png?alt=media

<h2>Keyboard navigation</h2><div class="table-wrapper"><table style="width:100%"><tbody><tr><th>Keys</th><td>Actions</td></tr><tr><th><span style="white-space:pre-wrap" id="isPasted">Tab or Arrows</span><br /></th><td><span style="white-space:pre-wrap" id="isPasted">Navigate between interactive elements</span></td></tr><tr><th><span style="white-space:pre-wrap" id="isPasted">Space or Enter</span><br /></th><td><span style="white-space:pre-wrap" id="isPasted">Activate the focused element</span></td></tr></tbody></table></div>

<h3 id="isPasted">Labeling elements</h3><p><span style="white-space:pre-wrap" id="isPasted">On web, the toolbar container should have the <strong>toolbar</strong> role. </span></p><p><span style="white-space:pre-wrap">On mobile, it can be a generic container. </span></p><p><span style="white-space:pre-wrap">All actions inside the toolbar should follow their respective accessibility guidelines.</span></p>

A toolbar on web, with a “toolbar” role label.

<p><span style="white-space:pre-wrap">On web, use the <strong>toolbar</strong> role</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0anynmv-5.png?alt=media
