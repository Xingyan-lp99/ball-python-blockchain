# Lists

Source: https://m3.material.io/components/lists
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/6d4033c2-f92c-4c43-b585-b3bce8468d48.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Use lists to help people find a specific item and act on it</p></li><li><p>Order list items in logical ways, like alphabetical or numerical</p></li><li><p>Keep items short and easy to scan</p></li><li><p>Show icons, text, and actions in a consistent format</p></li><li><p>Choose between standard and segmented styles</p></li></ul>

1 list contains 3 items, each with a label text, supporting text, and trailing text. A music app shows list items with leading images.

<p>A list item's label text, supporting text, image, and trailing icon can be customized to create a variety of lists</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmi8nxjh0-01.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/11cb6b2ed0f6dee4

libraryModuleType: STATUS_TABLE

<h2>M3 Expressive update</h2>

<p>Lists have a new segmented visual style, improved selection treatment, and support for slots. <a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank">More on M3 Expressive</a></p>

<p><strong>December 2025</strong> </p><p>Variants:</p><ul><li><p>Added <strong>expressive</strong> list</p><ul><li><p>Recommended for new designs</p></li></ul></li></ul><ul><li><p>List (<app-froala-tooltip-element description="Baseline variants are the original M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles. " link-label="More on M3 Expressive" link-url="https://m3.material.io/blog/building-with-m3-expressive " should-open-link-in-new-tab="true">baseline</app-froala-tooltip-element>) is still available</p></li></ul><p>New visual styles:</p><ul><li><p>Standard or segmented</p></li><li><p>Highlighted selection states</p></li><li><p>Flexible slots</p></li></ul><p>Supported platforms:</p><ul><li><p><a href="https://github.com/material-components/material-components-android/blob/master/docs/components/List.md#m3-expressive" target="_blank">Android Views (MDC-Android)</a></p></li><li><p><a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ListItem%28kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.material3.ListItemColors,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp%29" target="_blank">Jetpack Compose</a></p></li></ul>

2 party planning lists with 2 completed list items each. In 1 list, the selected items are highlighted.

<p>Expressive lists feature improved selection states</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmi8pwbjv-02.png?alt=media

<h2>Differences from M2 to M3 baseline</h2>

<ul><li><p><strong>Color:</strong> New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></p></li><li><p><strong>Layout:</strong> Padding and spacing rules are updated to be more consistent</p></li><li><p><strong>Height:</strong> The tallest element within a list item determines the list item’s height - either 56dp, 72dp, or 88dp</p></li><li><p><strong>Alignment:</strong></p><ul><li><p>In most cases, elements in a list item are middle-aligned</p></li><li><p>If a list is 88dp or larger, or contains three or more lines of text, elements are top-aligned</p></li></ul></li></ul>

3 variants of lists in M2.

<p>M2: Non-standard heights and alignments</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmi8q1tdh-03.png?alt=media

3 variants of lists in M3 baseline.

<p>M3 (baseline): Standardized heights and alignments</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmi8q2xsp-04.png?alt=media

## Specs

<h2>Variants</h2>

<h3>Expressive lists</h3><p>Use the expressive list variant for more flexible styling, highlighted selection states, and customizable slots. </p>

2 expressive lists: a photos list on a tablet, and a song list on mobile.

<p>An <strong>expressive list</strong> has a segmented style and round corners </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmio97lfj-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/za34_v9MVYFLgx4_LMophxugdmjrYW0gWSPfWtA_ntmDC74Lx_qID9YyOa7IEqJ73xCrYnCAXghjFmDugBK86DdvpEUUKbkfWTYCA2pV5iwt=s2048

<h3>Baseline lists</h3><p><app-froala-tooltip-element description="Baseline variants are the original M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles." link-label="More on M3 Expressive" link-url="https://m3.material.io/blog/building-with-m3-expressive " should-open-link-in-new-tab="true">Baseline</app-froala-tooltip-element> lists are still available to use, but don’t have the latest visual style, selection treatment, and slot functionality.<br /><br />On web, expressive lists are built on top of baseline lists.</p><p><a href="/m3/pages/lists/specs#94cf7f4d-fe29-4fab-9aae-a99e9b754329" target="_self">See baseline list specs</a></p>

3 baseline list items with square corners.

<p><strong>Baseline list items</strong> have square corners and standard colors</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmio98r05-02-3P-VQA.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/N4Dqm-y0qh8NW2KuKAqcRAmf_oyfUyeY2HgR3cHvoCwL-cM6j7fuAg97gGrX73Rs25WTv-POEG1ZSlXeyFPRkjhexmngaaSJMDJV0azeZXhV=s2048

<table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:37.6011%"><p style="text-align:center"><strong>Variants</strong></p></th><th style="width:30.5654%"><p style="text-align:center"><strong>M3</strong></p></th><th style="width:31.7629%"><p style="text-align:center"><strong>M3 Expressive</strong></p></th></tr></thead><tbody><tr><td><p style="text-align:left">Lists (expressive)</p></td><td><p style="text-align:center">--</p></td><td><p style="text-align:center">Available</p></td></tr><tr><td><p style="text-align:left">Lists (baseline)</p></td><td><p style="text-align:center">Available</p></td><td style="width:31.7629%"><p style="text-align:center">Not recommended.  </p><p style="text-align:center">Use expressive lists instead.</p></td></tr></tbody></table>

<h2>Configurations</h2>

<h3>Styles</h3><p>The standard and segmented styles are a visual choice, and don’t affect a list’s behavior.</p>

A standard list and segmented list in dark mode.

<ol class="decimal"><li><p>Standard</p></li><li><p>Segmented</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmio99zjp-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/AjWZ3hS3wVVBYsai8chTl-DhNYum8MkyLgX24Q1dLLV43O6P2gRIbTqcrvQMXwyFG9Jai3R-zExVwkBZ5A3QZGW4EryAzfylOS6N0FB1brD8=s2048

<h3>List selection</h3><p>A list can have only one selection mode at a time. For example, a single-action list can change to a multi-select list, but can’t be both at once.</p>

A single-action list with 4 items and no additional actions.

<p>In a <strong>single-action list</strong>, each item is a single tappable area</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmio9bca0-04-3P-singleaction.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/b5GgNFwCct9zCo3T-5FIclsjz95tsQWzwwptHqyfIs9ooGmMg8C4FLlknKKmivn_ho5bbYRLRnaxophUvZLmKrLqm1bkGF4tEyHNR4_CObV0og=s1004

A list with 4 items. Each item has 2 trailing icons for additional actions.

<p><strong>Multi-action list</strong> items include a primary action, and one or more secondary actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmio9ecsb-05-3P-multiaction.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/YZNJPefhDxEZHejO2AZtRcJlJmExP5SKLT5whDkHInauUNxfIgYBOXhlhXukAnjNfZRDhVUlk5fRz8QNgGAWqUaDPYkKANg3ZJ1vyK0GXZA=s1004

A list with 1 item selected.

<p>A <strong>single-select list</strong> </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmio9x63z-06-3P-singleselect.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/N1XQO63f9X32oDtv-OfmhY2QXVt4JpIIbZVk7BmB_2FcLR7QDWORgKJOQkA81-R5pujkxNiZHTMRgjMuAcytlrMERtLFsohNDJDu888bY3g=s1004

A list with 2 items selected.

<p>A <strong>multi-select list</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmio9xiam-07-3P-multiselect.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ANybLHYX4h2Z9SkeL_p_Pp1K3Wg9plho_Lbg3-Z5d7NwszrsXTlRm434BJIm0mbM1Km5s9XFun2jYrYZqVcj3vRF0rRY-Dk3ZpeQLYrzooMq=s1004

<h3>List interactions</h3>

<p>Lists can:</p><ul type="disc" style="list-style-type:disc"><li><p><a href="/m3/pages/lists/guidelines#90a236ee-b587-4361-8911-34006f25a6f1" target="_blank">Expand and collapse</a></p></li><li><p><a href="/m3/pages/lists/guidelines#01204f7d-ce32-4739-aece-e95db24858c9" target="_blank">Swipe to reveal</a>*</p></li></ul><p><a href="/m3/pages/lists/accessibility#a6f937f5-3e1f-4db4-ba35-ac6dd9fef140" target="_blank">More on list interaction accessibility</a></p>

1 list item expands into a list with 6 items, then collapses.

<p>A list can <strong>expand</strong> to include multiple items</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmshrflwe-GM3%20-%20Expressive%20-%20Specs%2008%20-%203P%20-%20v01%20(2).mp4?alt=media

A list item is swiped, and reveals 3 more actions.

<p>A list item can be <strong>swiped</strong> to reveal more actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmshrgh4t-09-key02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/7CIUKy6Fim2680D81iGn6XanxNoVlnFioAJfyYiwtTyF2xh2_RvyyLsLSFZoUj6LRfn6MVEyvaHyv_W0q2Al0pNkZL2JYjKuWHfF8q1vLvk=s1004

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:23.7089%;text-align:left"><p style="text-align:center"><strong>Category</strong></p></th><th style="width:28.3242%;text-align:left"><p style="text-align:center"><strong>Configuration</strong></p></th><th style="width:24.0276%"><p style="text-align:center"><strong>M3</strong></p></th><th style="width:23.8688%"><p style="text-align:center"><strong>M3 Expressive</strong></p></th></tr></thead><tbody><tr><td rowspan="2" style="width:23.7089%"><p>Styles</p></td><td><p>Standard</p></td><td><p style="text-align:left">Available</p></td><td><p style="text-align:left">Available</p></td></tr><tr><td><p>Segmented</p></td><td><p style="text-align:left">--</p></td><td><p style="text-align:left">Available</p></td></tr><tr><td><p>Selection modes</p></td><td><p>Single-action, multi-action,</p><p>single-select, multi-select</p></td><td><p style="text-align:left">Available</p></td><td><p style="text-align:left">Available</p></td></tr><tr><td><p>Interactions</p></td><td><p>Expand, swipe*</p></td><td><p>Available</p></td><td><p>Available</p></td></tr></tbody></table></div>

<p>* Swipe-to-reveal interactions are only available on Android Views</p>

<h2>Tokens &amp; specs</h2><p>Use the table's menu to select a token set. The <strong>common</strong> set combines baseline tokens with new expressive shapes and sizes. The <strong>expand</strong> set has tokens for the expand interaction. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/6c818a16475113bd

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['List - Common', 'List - Expand'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['List - Common', 'List - Expand', 'List - Reorder', 'List - Reveal'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Anatomy</h2>

Diagram with 10 elements that can be included in lists.

<p>Container and label text are required. All other elements are optional:</p><ol class="decimal"><li><p>Container</p></li><li><p>Overline</p></li><li><p>Label text</p></li><li><p>Trailing text</p></li><li><p>Supporting text</p></li><li><p>Trailing icon</p></li><li><p>Divider</p></li><li><p>Leading avatar</p></li><li><p>Leading icon</p></li><li><p>Leading media - image or video</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioasn71-11-3P-VQA.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Sa8xghsBnkEPnF8eS5BsRjuohsdTmqbkr_f1sENLSXj6Vvj60a-fAE32n9nUI8ErJeIbxkQPPl7wExD8qwxOM1aUbjPPV60s-E5vfR6EN6i7=s2048

<h3>Flexibility &amp; slots</h3><p>The <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">M3 Design Kit</a> includes lists with custom slots for designing flexible item layouts. Think of a custom list as a container with three different slots: leading, content, and trailing. Each slot can hold a different element.</p><h4><strong>Slot accessibility</strong></h4><p>Slots are not accessible by default. Consider the following:</p><ul><li><p>Elements must follow the rules, structure, and interaction patterns for lists</p></li><li><p>Use standard list item padding</p></li><li><p>Target size must be at least 48x48dp</p></li><li><p>Don't add interactive elements that make the list item difficult to navigate, especially for people using screen readers</p></li></ul><p><a href="/m3/pages/lists/accessibility#538f23f7-689c-4516-bfc8-5f6933a43f5e" target="_blank">More on required accessibility guidelines</a></p>

A diagram with leading, content, and trailing slots.

<p>Reserve the use of slots for use cases that maintain the list’s accessibility and functionality</p><ol class="decimal"><li><p>Leading slot</p></li><li><p>Content slot </p></li><li><p>Trailing slot</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioecnyy-12-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/xpDca9BbXlTiv20zpU4gfBwt6MkKXaY5ZNLRcxAljGC5QsVXgH3mKaHiaEI6okSs2gUhacnLEdM2zCIC5raKpqBZl476yJ8Qchx5bxvt6Kywwg=s1352

<div class="fr-banner caution"><div class="fr-banner-icon">warning</div><div class="fr-banner-content caution"><div class="fr-banner-label">Caution:</div><div class="fr-banner-description">Slots require custom code implementation that you must create and maintain</div></div></div>

<p>The <strong>leading</strong> and <strong>trailing</strong> slot positions must be a smaller width than the <strong>content</strong> section.</p><p>1. <strong>Leading slots</strong> can contain:</p><ul><li><p>Visual elements: Avatar, icon, image, or video thumbnail</p></li><li><p><app-froala-tooltip-element description="Selection lets users choose specific items to act on." link-label="More on selection" link-url="/m3/pages/selection" should-open-link-in-new-tab="true">Selection</app-froala-tooltip-element> controls: Checkbox, radio button, or switch</p></li><li><p>Customizations: Badge or larger image</p></li></ul><p>2. <strong>Content slots</strong> must be the largest-width slot and can contain:</p><ul><li><p>Default content: Label text, supporting text</p></li><li><p>Optional add-ons: Badge, icon, in-line label, or more text elements</p></li><li><p>Avoid long lines of text to preserve readability</p></li></ul><p><br />3. <strong>Trailing slots</strong> can contain:</p><ul><li><p>Action elements or text: Icon, icon button, or trailing text</p></li><li><p>Selection controls: Checkbox, radio button, or switch</p></li></ul>

Slot diagram showing slot placement in the middle of the list.

<p>The content slot must be the largest section, placed in the middle of the list item</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioefhsu-13-3P-VQA.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/jx4zxtSR4RN6N-1sCYapnbcg_EJOMuolnJBIPdx5aR9tEJ3PB1VtfNmemVGd-IKUMyPhpg1xj2FOUwBYzeekhv1rOIX4bE33jmMPNbV10RTL8w=s1352

<h4>Selection lists</h4><p>For selection lists, use only one selection interaction per list item.</p>

A selected list item with a checkmark in the leading slot.

<p>Use only one selection interaction per list item</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioehno9-14-do-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/_cCLtqaTv3_VJ2Su5-NcT91PPqYvyAFZeK-5w0av-NbLChQrKPvD3HSBWsc6adlc9M1DQGkIVd_eisASsmoVyA_2nO23ObPXfcuLp6O9sMU=s656

A selected list item with both a checkmark in the leading slot and a bookmark in the trailing slot.

<p>Don't use multiple selection interactions in one item</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioek6y5-15-dont-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/7ikqKMFSD3KqUsrjy_D0FguVESN7UimX34YCtDgR8Cqm5sbof9nysVBBnBgjQukuuXjAQooDRC5mtopWMuGcpNL6TIQDNjGzQ3fkSDJVFfLZrg=s656

<h2>Color</h2>

<p>Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p>

10 list element color roles in light mode and dark mode.

<p>List color roles used for light and dark themes:</p><ol class="decimal"><li><p>Surface   </p></li><li><p>On surface variant</p></li><li><p>On surface  </p></li><li><p>On surface variant</p></li><li><p>On surface variant </p></li><li><p>On surface variant</p></li><li><p>Outline variant</p></li><li><p>Primary container</p></li><li><p>On primary container</p></li><li><p>On surface variant</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmion9qya-16-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ARd2jFHJp7QY8tjQqnTd9qITF5sD6WqWXpapVsC25_-ej0okbpB1kkGYkJ8V7jSl-iFv0cW18ZGseOUM3x1CqZflXxkdU7T4znEQ0bJ3qCvx=s2048

<h2>States</h2>

<p>States are visual representations used to communicate the status of a component or an interactive element. <a href="/google-material-3/pages/interaction-states/overview" target="_blank">Learn more about interaction states<br /><br /></a><a href="/m3/pages/lists/accessibility#f7e067e1-722f-40c5-a95a-63929869bf3e" target="_blank">More on list focus</a></p>

<h3>Default list items</h3>

6 default list states in light and dark mode.

<ol class="decimal"><li><p>Enabled </p></li><li><p>Disabled</p></li><li><p>Hovered</p></li><li><p>Focused</p></li><li><p>Pressed</p></li><li><p>Dragged</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmionai1i-17-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/WfsQdzz9ydTMtaG8lRdHEb8GmuDilZ3RVX7fNys6QemgIc3Euv0bnB2eKnFMZNxvApj-l2ZNNVTtCrgdS3CfuR6FmBFEv8ppLObmmykaM6yO=s2048

<h3>Selected list items</h3>

6 selected list states in light and dark mode.

<ol class="decimal"><li><p>Enabled </p></li><li><p>Disabled</p></li><li><p>Hovered</p></li><li><p>Focused</p></li><li><p>Pressed</p></li><li><p>Dragged</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioncezo-18-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/plktb9RXA8a9SyxyQIpnF8qX_hMwZP0_SIXh-vuSRreRX9e8DbpLs90qXW4rIrtZyNyTmEbJTYmenlpK0EjS_q6HyaoZmb4ERojsZU2trNc=s2048

<h2>Measurements</h2>

Size and padding measurements for list items.

<p>List item alignment, padding, and size measurements. The icon button height is dynamic, and automatically adjusts to fill the list item height.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmiondj5y-19-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/i93JWmCnwH8J71-rjNfpGP1SCy_v1gjfHOkLAph3y86kvhmpo9uT_x75vfDsKz_NxDbnt9C5GWA4xX0rba-hRzTmxtfWPw-zncFBcbmzKiLm=s2048

<h3>Shape morphing</h3><p>When a list item is selected, the corner shape changes to highlight the active item:</p><ul type="disc" style="list-style-type:disc"><li><p>Unselected corner radius: 4dp inner, 16dp outer</p></li><li><p>Selected corner radius: 16dp</p></li></ul><p></p>

A 3-item list. The middle item is unselected, with a 4dp corner radius.

<p>Unselected list items have a 4dp inner corner radius, and 16dp outer corner radius</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsghyywm-20-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ZP5JjdhEst35JLSuCdpnHvXs58yyjQdBREYdsNON0wtg-iHRjNtjvaPF6ekO3e3ceRrJWfJrP0ZfMVZ2EKbIqmfaRTuupnuHkDOkn1zwGORY=s656

A 3-item list. The middle item is selected, with a 16dp corner radius.

<p>Selected list items have a 16dp corner radius all around</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsgi2yv8-21-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/UeCgyEiHh76y34mk1S7ebdWal471s5Yjj34uWFbNb0sEgl-iICDps6JeHuje-47Lb8h1F1ii1GsWSra-8nEeqSH5Mp1R4KVCD_ff9IU9Bagi=s656

<h2>List (baseline)</h2>

<p>The <app-froala-tooltip-element description="Baseline variants are the original M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles." link-label="More on M3 Expressive" link-url="https://m3.material.io/blog/building-with-m3-expressive" should-open-link-in-new-tab="true">baseline</app-froala-tooltip-element> list variant is available and continues to work in existing products. However, the <a href="/m3/pages/lists/specs#ebf87f58-d5bf-4cb5-a856-d2bb104eec4d" target="_self">expressive list</a> variant is recommended for new designs.</p>

<h3>Tokens &amp; specs</h3><p>Baseline list <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">tokens</app-froala-tooltip-element> are in the <strong>common</strong> token set. Note: This set also includes several expressive tokens.</p>

resourceName: designSystems/20543ce18892f7d9/components/6c818a16475113bd

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['List - Common'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['List - Common', 'List - Expand', 'List - Reorder', 'List - Reveal'], 'hideSearchField': False, 'hideVersionName': True}

<h3>Color</h3><p>Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p>

9 baseline list element color roles in light and dark mode.

<p>List color roles used for light and dark themes:</p><ol class="decimal"><li><p>Surface</p></li><li><p>On surface</p></li><li><p>On surface variant</p></li><li><p>On surface variant</p></li><li><p>On surface variant</p></li><li><p>Outline variant</p></li><li><p>Primary container</p></li><li><p>On primary container</p></li><li><p>On surface variant</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmiq3n8p4-20-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/c7bwcYNZe1HFiYuQW2r1uEEhDr_8PMPrgH911ney_P2AQnEZ64a34YKs47JbQnNjPbrtMfhw0FA7oQ3T1Euqx9HQ45ItoppUNl_7LUN5dX8=s2048

<h3>States</h3><p>States are visual representations used to communicate the status of a component or interactive element.</p>

6 baseline list states in light and dark mode.

<p>1. Enabled</p><p>2. Disabled</p><p>3. Hovered</p><p>4. Focused</p><p>5. Pressed</p><p>6. Dragged</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmiq3rr3p-21-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/5lf9R5VeSpT9MZ52tQ1Gr9G6LJSo3T61BAkwRTHYYL4e0_ymdXq3TFfAieV8fBpokbyEkAP1dql3Z23YsmOgHwTzZclYa1v5eLG9J7lTYcJu=s2048

<h3>Layout</h3><h4>One-line lists</h4>

Alignment, padding, and size specifications for baseline list items with 1 line of text.

<p>Baseline one-line list alignment, padding, and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmiofu0i1-22-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/z9QvwXHZzQCURyxwHxCKWIzN9bFCueiLYqnmwebzTymL8CQV6SfHPmE39ptDMlyCdxfAYa3ymS7TFM3eWfJEHnzXOq7ndUBAoqGr211VXq-K=s2048

Measurements for a 3-item list with 1 line each.

<p>Baseline list item measurements and padding</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmiogaa9o-23-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/khpu5JdGUDNFXqPEgOJ5ZWoXXvptYxD57jKRlck-ECQ1ge8a4pIcPdajOsbR3theeOCNLC8HoON7F71IWL5LsM5dFl_74zbveiiwPsZnriIqtQ=s2048

<h4>Two-line lists</h4>

Alignment, padding, and size specifications for baseline list items with 2 lines of text.

<p>Baseline two-line list alignment, padding, and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmiogazt3-24-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LxLM2jQt0STwJFF6mM7jaAxeP09Gu8KXxM8a2gg_tCprAziEoUSMbqhONXIWU-yKoahTjXATtmhpqTaSxfe7x7UoAhhTD157g0YkJwJS-tse=s2048

Measurements for a 3-item list with 2 lines each.

<p>Baseline list item measurements and padding</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmiogcld0-25-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/UIM_5cKOrqy1Jgy2wF6ND6qMT0cXmrXlqkqpSr1hUtJoShVECpFJt1jn39e7aoczco9L3ABwR7O4gd366Fdwg7tfQnWGas_8LRAM0LWM7z0NRg=s2048

<h4>Three-line lists</h4>

Alignment, padding, and size specifications for baseline list items with 3 lines of text.

<p>Baseline three-line list alignment, padding, and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmiogdayj-26-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/eoubrmM-Nl9VlpagzZuJBlQ7Ze1c-LjzmdIfk2sIxw16gjTgSUXdPTTLa1P1o1klSZk9SP6JZjG3BrVkBCnvatvekRTyo1Qkq2SoN5eSHEWy=s2048

Measurements for a 3-item list with 3 lines each.

<p>Baseline list item measurements and padding</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmiogduex-27-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/mX9bAsTDGyRcmgR60R9k2JBak4FqR4Iq5BHj_D9vHhsd3GwzcWjsnjvUzz4UDdrcd4KZE27gqKYtovW1ejGeDrnmqzdeoUULLnR8dLqTLZsf=s2048

<div class="table-wrapper"><table style="border:none;border-collapse:collapse;margin-right:calc(0%);width:100%"><thead><tr><th style="text-align:center;width:51.9542%">Attribute</th><th style="text-align:center;width:47.9559%">Value</th></tr></thead><tbody><tr><th style="width:51.9542%"><p>Label alignment</p></th><td><p>Center</p></td></tr><tr><th style="width:51.9542%"><p>Label alignment when height is 88dp or taller</p></th><td><p>Top</p></td></tr><tr><th style="width:51.9542%"><p>Label left padding</p></th><td><p>16dp</p></td></tr><tr><th style="width:51.9542%"><p>Leading element alignment (vertical)</p></th><td><p>Center</p></td></tr><tr><th style="width:51.9542%"><p>Leading element alignment (vertical) when height is 88dp or taller</p></th><td><p>Top</p></td></tr><tr><th style="width:51.9542%"><p>Leading element left padding</p></th><td><p>16dp</p></td></tr><tr><th style="width:51.9542%"><p>Leading icon alignment (vertical)</p></th><td><p>Top</p></td></tr><tr><th style="width:51.9542%"><p>Leading icon top padding</p></th><td><p>8dp</p></td></tr><tr><th style="width:51.9542%"><p>Leading icon top padding when height is 88dp or taller</p></th><td><p>12dp</p></td></tr><tr><th style="width:51.9542%"><p>Trailing element alignment (vertical)</p></th><td><p>Center</p></td></tr><tr><th style="width:51.9542%"><p>Trailing element alignment (vertical) when height is 88dp or taller</p></th><td><p>Top</p></td></tr><tr><th style="width:51.9542%"><p>Trailing element left padding</p></th><td><p>16dp</p></td></tr><tr><th style="width:51.9542%"><p>Trailing element right padding</p></th><td><p>24dp</p></td></tr><tr><th style="width:51.9542%"><p>Padding above/below divider</p></th><td><p>0dp</p></td></tr><tr><th style="width:51.9542%"><p>Targets</p></th><td><p>48dp</p></td></tr><tr><th style="width:51.9542%"><p>Divider full-width</p></th><td><p>100%</p></td></tr><tr><th style="width:51.9542%"><p>Divider inset left padding</p></th><td><p>16dp</p></td></tr><tr><th style="width:51.9542%"><p>Divider inset right padding</p></th><td><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt">24dp</p></td></tr></tbody></table></div>

<h3>Configurations</h3>

<h4>Leading avatar</h4>

1, 2, and 3-line list items with and without a leading avatar and trailing checkbox, in dark mode.

<ol class="decimal"><li><p>With leading avatar</p></li><li><p>With leading avatar and trailing checkbox</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioh5e7e-28-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/YtV6g40j9-XQCPCAVu67QZhyyBxdzXse8Aq4zgVnIWxg5eL0YP-62b5XRWhoQFLGZ77XDbPLnnLnc6cQrbdVy0vdd5Qop9rt2L0vbVMrGlw=s2048

<h4>Leading image or thumbnail</h4>

1, 2, and 3-line list items with and without a leading image and trailing checkbox, in dark mode.

<ol class="decimal"><li><p>With leading image</p></li><li><p>With leading image and trailing checkbox</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioh5246-29-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/7K4R5eQvQLtvBGZ8iDlPrwl6-HftUdcPx0S6MRj8QLMuQMLlHQXj0EYkvlawvcIQOlaTsf1CAq8GIXC-zPanjI8B5o0Wznt8P_Os0Bir_Fq92A=s2048

<h4>Leading video</h4>

1, 2, and 3-line list items with and without a leading video and trailing checkbox, in dark mode.

<ol class="decimal"><li><p>With leading video</p></li><li><p>With leading video and trailing checkbox</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioh4nys-30-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/811g1L2vKGQ0BTtqAoZPO-jApLgGPEDiV-7oi308iwDk-GrwrWTuQmCkNSok5-5XqCp7iNaldpc6cnpOL2Xe1RfUSfURXuucBF8O5k5WUomf=s2048

<h4>Leading icon</h4>

1, 2, and 3-line list items with and without a leading icon and trailing checkbox, in dark mode.

<ol class="decimal"><li><p>With leading icon</p></li><li><p>With leading icon and trailing checkbox</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioh3zha-31-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/F_D2HGWtWYSMxDVgfkIRpfgvy8O26m5Gq1uzE8tvEuo9m9sMLfRhcnuVfZSE6hyxoICYNuSzjIfA1yRVpcXvaJG1b02lEpkYn-l0scGCQTmt=s2048

<h4>Text-only</h4>

1, 2, and 3-line text only list items with and without a trailing checkbox, in dark mode.

<ol class="decimal"><li><p>With text only</p></li><li><p>With text and trailing checkbox</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioh3lil-32-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/0D-xONvUbyoPV0EMlMrBItgWHQXbW1IV2dBVpIslSFeHc0mUoHbJsP3y9on5ym7Ch1ICbFcFH7026UzSdnQvTABrsRQhYe8yRiG2imFaK00=s2048

<h4>Leading checkbox</h4>

1, 2, and 3-line list items with and without a leading checkbox and trailing text, in dark mode.

<ol class="decimal"><li><p>With leading checkbox</p></li><li><p>With leading checkbox and trailing text</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioh2vwf-33-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/3pOgKx-2m1N3ewCJ-joHRZ0IFwf-GHaxzimTyF_4-SYx_80TL6UnaBywa7ogFoCCil_KQgEFXoNmwKuXP_6dGsFC0uMqCLGE5qQpUqHOGdrxZQ=s2048

<h4>Leading radio button</h4>

1, 2, and 3-line list items with and without a leading radio button and trailing text, in dark mode.

<ol class="decimal"><li><p>With leading radio button</p></li><li><p>With leading radio button and trailing text</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioh2gxb-34-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-Eph6i5PJ8k8D5ABIpITkh-WLe2a-gMsM-sq2qCDM1cFBVfQN3FGAYAwiryrXRkrF8-8Q3Exypco2Ir4iP0s0IRbZ_n-ZvFI2ZTuNUzz7bs=s2048

<h4>Trailing switch</h4>

1, 2, and 3-line list items with and without a leading icon and trailing switch, in dark mode.

<ol class="decimal"><li><p>With trailing switch</p></li><li><p>With leading icon and trailing switch</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmioh0mgk-35-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/6qcPlbTkPuUN2vByfw3QiZU3_haTWYgitgstbbYGI9ugO1r8LknZ2RPovveQ18B9EOKQNu5robyVqrQs0AvZchLuQXeckUeWZEn2meby2vkA=s2048

## Guidelines

3 list items show different layout options, with varying sizes of elements in the leading slot.

<p>Lists can include a range of layout combinations:</p><ol class="decimal"><li><p>Leading images, videos, icons, or avatars</p></li><li><p>Trailing text, icons, or icon buttons</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiewlynz-01.png?alt=media

<h2>Usage</h2>

<p>Lists are vertical groups of text, icons, images, and other elements, optimized for reading comprehension.</p><p></p><p>List items can contain multiple actions at once, like selection, icon buttons, overflow menus, and more.</p>

3 list items with avatars using different expressive shapes.

<p>A clear visual hierarchy makes lists easy to scan and read</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiewcuoc-02.png?alt=media

<p>Use lists for communicating or selecting discrete items, such as choosing from a set of colors.</p>

A list of colors with Periwinkle selected.

<p>Lists are an organized way to add imagery and supporting elements to selection. In this color selection example, the list contains color swatches, color names, and a checkbox action.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiewi9tz-03.png?alt=media

<p>A list should be easy to scan. Any element can be used to anchor and align list item content.</p><p>Place supporting visuals and primary text in the same position in each list item.</p><p>Don’t vary the position of elements within a list.</p><p></p>

4 versions of the same list highlighting avatar and text alignment.

<ol><li>Sample list</li><li>Content placement in a row</li><li>Supporting visuals are aligned for easy scanning</li><li>Primary text is aligned for easy scanning</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiewmxat-04.png?alt=media

<p>List items can adapt to different lengths of text:</p><p><strong>Label text only <br /></strong>A list item can contain a single line of label text. If the text doesn’t fit on one line, it can wrap or be truncated.</p><p><strong>Label text with supporting text <br /></strong>A list item can include supporting text below the label text. Both the label and supporting text can wrap or be truncated.</p>

3 lists show items with label text only, label text with 1-line of supporting text, and label text with 2-lines of supporting text.

<p>Three examples of list item sizes:</p><ol class="decimal"><li><p>Label text only</p></li><li><p>Label text with supporting text on one line</p></li><li><p>Label text with supporting text that wraps to two lines</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiewpdzm-05.png?alt=media

<h2>Anatomy</h2>

List diagram with 10 elements.

<p>Container and label text are required. All other elements are optional:</p><ol class="decimal"><li><p>Container</p></li><li><p>Label text</p></li><li><p>Supporting text</p></li><li><p>Trailing text</p></li><li><p>Trailing icon</p></li><li><p>Trailing selection control - checkbox, radio button, switch</p></li><li><p>Leading avatar container</p></li><li><p>Leading avatar text</p></li><li><p>Leading icon</p></li><li><p>Leading media - image or video</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiewsyte-06.png?alt=media

<h3>Container</h3><p>List containers hold all list items and their elements. List item size is determined by the tallest element within the list item. <a href="/m3/pages/lists/specs#1824b94d-7d17-4a29-889f-d277037a1313" target="_blank">See layout measurements</a>  </p><p>When a list item features an image, consider customizing the container color to use a content-based color scheme. This should be applied to either the enabled state or for an interaction.</p>

A song list with a leading images. When selected, a list item’s container matches the image’s color scheme.

<p>A list item can include a leading image and a vibrant color</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiewwh4p-GM3%20-%20Expressive%20-%20Guidelines%2007%20-%20v02.mp4?alt=media

<h3>Label &amp; supporting text</h3><p>Keep label text brief.   <br /><br />To ensure list items are scannable:</p><ul><li><p>Limit supporting text to one to three lines</p></li><li><p>Truncate supporting text, depending on screen size</p></li></ul><p><a href="/m3/pages/lists/guidelines#561cc637-aa43-4055-be1e-0716faeef7af" target="_self">See adaptive guidance</a></p>

A list item with a leading image, concise label text “Art events”, and 2 lines of truncated supporting text.

<p>Limit supporting text to one to three lines</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiex0v5m-08.png?alt=media

<h3>Icons</h3><p><strong>Leading icon</strong><br />A leading icon should provide a quick visual cue that relates to the item's label text, helping people scan the list.</p><p><strong>Trailing icon</strong> <br />A trailing icon is often used to communicate status or indicate an action, like <strong>Show more</strong>.</p>

Leading icons should relate to the label text 
A list of items with leading and trailing icons on a mobile device.

<ol class="decimal"><li><p>Leading icons should relate to the label text</p></li><li><p>Trailing icons can communicate an action</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiexc5t2-9.png?alt=media

<h3>Leading media</h3><p>List items can contain a leading avatar, image, or video. Anchor visuals to the leading edge of the list to improve scannability.</p><p>Leading video thumbnails can open a video player or even play within the list.</p><p></p>

A list of plants with images at leading edge.

<p>Place supporting visuals, like thumbnails, at the leading edge of a row to improve scannability</p><p></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiexhs7r-10.png?alt=media

A list of plants with an image in the middle of the row makes it difficult to align the name and price.

<p>Avoid placing visuals in the center of a row because it makes the list difficult to scan</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiexip9k-11.png?alt=media

<h4>Avatars</h4><p>List items can include images in circular or expressive shapes to represent a person or entity.</p><p>Use square or rectangular images for other content, such as products or videos.</p>

List of contacts with avatars with a circular, expressive crop to indicate a person.

<p>Use an expressive, circular avatar to represent a person or entity</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiexkoay-12.png?alt=media

<h4>Primary &amp; secondary actions</h4><p>Use spacing to draw attention to the most important aspect of the list item, usually the primary action area or key content.</p>

A folder icon in the primary action area takes up the full height of the list item.

<p>The primary action takes up more space:</p><p>1. Primary action area</p><p>2. Secondary action area</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiexnuvs-13.png?alt=media

A list item has an avatar in the more distinguishing content position on the left, and “15 min” trailing text on the right.

<p>Align content by importance:</p><p>1. More distinguishing content</p><p>2. Less distinguishing content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiexoaw7-14.png?alt=media

<h3>Trailing text</h3><p>Trailing text can provide additional meta-information about a list item, such as a price, count, or other details.</p>

The date “Nov 17” as trailing text in a concert ticket list item.

<p>Use trailing text for supplemental details, like a price, count, or date</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiextt91-15.png?alt=media

<h3>Selection controls</h3><p><app-froala-tooltip-element description="Selection lets users choose specific items to act on." link-label="More on selection" link-url="/m3/pages/selection" should-open-link-in-new-tab="true">Selection</app-froala-tooltip-element> controls display list item actions. Position controls at the leading or trailing end of a list item:</p><ul><li><p>Use <app-froala-tooltip-element description="Checkboxes let users select one or more items from a list, or turn an item on or off." link-label="More on checkboxes" link-url="/m3/pages/checkbox/overview" should-open-link-in-new-tab="true">checkboxes</app-froala-tooltip-element> to select multiple items</p></li><li><p>Use <app-froala-tooltip-element description="Switches toggle the state of an item on or off." link-label="More on switches" link-url="/m3/pages/switch/overview" should-open-link-in-new-tab="true">switches</app-froala-tooltip-element> to toggle settings on or off</p></li><li><p>Use <app-froala-tooltip-element description="Radio buttons let people select one option from a set of options." link-label="More on radio buttons" link-url="/m3/pages/radio-button/overview" should-open-link-in-new-tab="true">radio buttons</app-froala-tooltip-element> to select a single item</p></li></ul>

3 lists with different selection controls.

<p>List items with: </p><ol class="decimal"><li><p>Checkboxes</p></li><li><p>Switches </p></li><li><p>Radio buttons</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiexzfsy-16.png?alt=media

<h3>Gaps &amp; dividers</h3><p>Gaps or dividers can separate lists into items and groups:</p><ul><li><p>Use <strong>gaps</strong> for contained lists. Gaps leverage expressive shape and containment tactics.</p></li><li><p>Limit <strong>dividers</strong> to uncontained or complex lists, only when a stronger visual separation is necessary.</p></li></ul>

Filled list items in an inbox separated by gaps.

<p>Use <strong>segmented gaps</strong> and filled list items to define a list group</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiezuscb-17_do.png?alt=media

An uncontained list with city names separated by dividers.

<p>Limit the use of <strong>dividers</strong> to uncontained lists</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiezvi6d-18caution.png?alt=media

<h2>Adaptive design</h2>

<h3>Line length</h3><p>In fluid <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/layout-overview/overview" should-open-link-in-new-tab="true">layouts</app-froala-tooltip-element>, avoid excessively long lines of text when expanding containers and text-heavy components. This often means changing <app-froala-tooltip-element description="Margins are the spaces between the edge of a nested element and its parent element, such as the space between a button's label text and the edge of its container." link-label="More on margins" link-url="/m3/pages/spacing/overview#753cb18a-b6ba-4727-87b3-cb1b7b497a9a" should-open-link-in-new-tab="true">margins</app-froala-tooltip-element> and typography properties as the container scales.</p>

4 list items with 2-line supporting text have adjusted margins to preserve readability.

<p>Adjust margins to create a more comfortable line length for reading</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiezxs4c-19_do.png?alt=media

<p>Adapt the width of the list container based on a line’s length, or by switching to a multi-column layout.</p>

List items in a 2-column layout, with each item showing text preview.

<p>A multi-column layout can help break up content when needed</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiezzrzc-20_do.png?alt=media

<p>The ideal line length for text is typically between 40 to 60 characters, but large-screen devices can accommodate up to 120 characters per line. If a line of text is close to 120 characters in length, consider increasing the line height to improve readability .</p>

List items with elongated line length.

<p>Don’t scale components without adjusting other affected areas of the screen, such as text length. This can result in line lengths that make reading difficult.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif01yxf-21_dont.png?alt=media

<p>A list with a <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoint</app-froala-tooltip-element> can become part of a two-column layout at an <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoint</app-froala-tooltip-element>, adjusting the amount of information shown in each list item.</p>

Animation of a list on mobile and the same list adapted into a 2-column layout on desktop.

<p>Reduce the amount of information shown at compact breakpoints</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif043uk-GM3%20-%20Expressive%20-%20Guidelines%2022%20-%20v02.mp4?alt=media

<h3>Adapt list elements &amp; layout</h3><p>Lists can change their layout to adapt to different <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element>. This affects the size and placement of content.</p><p>For example, a list at a compact breakpoint can adjust margins, spacing, or density to better fit an expanded window.</p>

Photo list on mobile expands to allow larger images and longer descriptions on a tablet.

<p>On larger screens, lists can show more content, like supporting text and larger imagery</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif0dffm-GM3%20-%20Expressive%20-%20Guidelines%2023%20-%20v02.mp4?alt=media

<h3>Swap components</h3><p>Lists are just a compact composition of images, text, and actions. Other components, like cards and carousels, use the same elements but take up more space.   </p><p>At larger breakpoints, consider swapping a list to a component with a similar purpose to take advantage of available space.</p>

A mobile photo list changes into cards in a larger window.

<p>Information displayed in list items on mobile can change to cards on tablet and desktop</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif0fb1t-GM3%20-%20Expressive%20-%20Guidelines%2024%20-%20v02.mp4?alt=media

<h3>Compact breakpoints</h3><p>Lists should extend edge-to-edge in compact windows. Selecting a list item should open a page with the details.</p>

When opened, a mobile photo list item expands to fill the width of the screen.

<p>On small screens, people can navigate between lists and full-screen detailed views</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif0hg20-GM3%20-%20Expressive%20-%20Guidelines%2025%20-%20v01.mp4?alt=media

<h3>Medium &amp; expanded breakpoints</h3><p><app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">Medium</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints</app-froala-tooltip-element>, such as tablet and desktop screens, can display primary and secondary content in the same view.</p><p>For example, a list and the detailed information can appear side-by-side.</p>

A larger screen displays list items and a detailed expansion of one item on the same screen.

<p>On larger screens, a list-detail view can be more appropriate</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif0jzwl-26.png?alt=media

<p>At a larger breakpoint, a list may transform into a carousel.</p>

A photo list with thumbnails in a compact window expands into a carousel with large images in an expanded window.

<p>Lists can transform into carousels in expanded windows</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif0mtl7-GM3%20-%20Expressive%20-%20Guidelines%2027%20-%20v02.mp4?alt=media

<p>Lists can also show more or less content as they scale up and down in size.</p><p>For example, a list item can reveal more content when the component expands.</p>

A list expands from a compact to a medium window. The expanded items show supporting text.

<p>List items reveal supporting text at expanded breakpoints</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif0onle-GM3%20-%20Expressive%20-%20Guidelines%2028%20-%20v02.mp4?alt=media

<h2>Behavior</h2>

<h3>List selection modes</h3><p>The selected state applies to the entire list item. For example, when an item with a checkbox is selected, both the list item and the checkbox show a selected state.</p>

<h4>Single-select</h4><p>Lists can feature a single-selection component such as a <app-froala-tooltip-element description="Radio buttons let people select one option from a set of options." link-label="More on radio buttons" link-url="/m3/pages/radio-button/overview" should-open-link-in-new-tab="true">radio button</app-froala-tooltip-element>.</p><p>Single-select list items:</p><ul type="disc" style="list-style-type:disc"><li><p>Don’t support multi-actions</p></li><li><p>Can’t have secondary nested actions</p></li><li><p>Shouldn’t use checkboxes</p></li></ul><p></p>

A 3-item list with radio buttons, with 1 item selected.

<p>Use radio buttons to allow a single selection in a list</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmielqxgm-29.png?alt=media

<h4>Multi-select</h4><p>Multi-select lists allow for multiple list items to be toggled on.</p><p>Multi-select list items:</p><ul type="disc" style="list-style-type:disc"><li><p>Pair well with checkboxes and switches</p></li><li><p>Can’t have secondary nested actions</p></li><li><p>Shouldn’t use radio buttons</p></li></ul>

A 3-item list with checkboxes and 2 items selected.

<p>Use checkboxes or switches for multi-select lists</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmielw5u4-30.png?alt=media

<h4>Single-action</h4><p>In a single-action list, the entire list item performs one action, such as navigating to a new page.</p><p>Single-action list items:</p><ul type="disc" style="list-style-type:disc"><li><p>Can’t have secondary nested actions</p></li><li><p>Can’t be toggled into a persistent selected state</p></li></ul>

A 3-item list where each item is a single tappable area.

<p>Use a single-action list for a primary action, like navigation</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmielzpxu-31.png?alt=media

<h4>Multi-action</h4><p>Multi-action lists can support multiple nested actions within a list item.</p><p>The primary action should take up the majority of the space in the leading and content positions.</p><p>Place supplementary actions, like a bookmark or menu, in the trailing position.  </p><p><a href="/m3/pages/lists/accessibility#b69b89a9-7ca0-4249-b25b-2d0c85a41dc0" target="_blank">More on multi-action accessibility</a></p>

A 3-item song list where each item has 2 trailing icons: a bookmark and overflow menu.

<p>Place supplementary actions in the trailing position of a list item</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiem2107-32.png?alt=media

<h4>Non-interactive</h4><p>Non-interactive lists can organize information in a scannable way. They don’t perform any actions and can’t be selected.</p>

A 3-item non-interactive list showing a historic timeline of space travel.

<p>Use non-interactive lists to make information easy to scan</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiem457u-33.png?alt=media

<h3>List interactions</h3>

<h4>Expand &amp; collapse</h4><p>List items containing other list items can expand and collapse in a folder-like manner, to reveal or hide content. </p><p>Tapping a list item expands it vertically across the entire screen using a container transform transition pattern.</p>

On a to do list, an item expands, revealing nested child items.

<p>To expand a list item, display a parent-child transition</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmiem9cox-GM3%20-%20Expressive%20-%20Guidelines%2034%20-%20v02.mp4?alt=media

<h4>Swipe</h4><p>On Android, list items can reveal buttons on swipe. Use a mix of button styles for visual interest and hierarchy.  </p><p>The primary action must be the final end-aligned option. A full swipe triggers this action, clearing the list item and all other actions off-screen. </p><p>Swipeable list items should include alternative ways to access hidden actions, such as a more icon.</p><p><a href="/m3/pages/lists/accessibility#32f5115c-b15e-4af6-8c1a-4807bee2bf7a" target="_blank">More on swipe accessibility</a></p>

List of recipes with “Fresh baked breads” swiped to reveal a archive icon.

<p>When a list item is swiped, it can be archived or reveal more actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmshq8qm6-35-key03.png?alt=media

## Accessibility

<h2>Use cases</h2>

<p>People should be able to do the following with assistive technology:</p><ul><li><p>Navigate to a list item </p></li><li><p>Select a list item</p></li></ul>

<h2>Indicate selection with more than color</h2>

<p>To make selected items clear for everyone, don't rely on color as the only visual cue.   </p><p>Use an additional indicator that an item is selected such as:</p><ul><li><p><app-froala-tooltip-element description="Radio buttons let people select one option from a set of options." link-label="More on radio buttons" link-url="/m3/pages/radio-button/overview" should-open-link-in-new-tab="true">Radio buttons</app-froala-tooltip-element> or <app-froala-tooltip-element description="Checkboxes let users select one or more items from a list, or turn an item on or off." link-label="More on checkboxes" link-url="/m3/pages/checkbox/overview" should-open-link-in-new-tab="true">checkboxes</app-froala-tooltip-element></p></li><li><p>Leading or trailing icons</p></li><li><p>A visual style not related to color, like underlined text</p></li></ul>

A selected list item with a colored background, and a check as the leading icon.

<p>Use two visual cues to show a list item is selected, like a leading checkmark and filled color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif14iza-01.png?alt=media

<h2>Interaction &amp; style</h2>

<h3>Touch</h3><p>When a person taps on a list item, a touch ripple appears, indicating interaction feedback.</p>

A 3-item list shows a touch ripple animation as the second item is tapped and selected.

<p>A ripple appears when a person taps on a list item to select it</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif1hthv-GM3%20-%20Expressive%20-%20Accessibility%2002%20-%20v01.mp4?alt=media

<h3>Cursor</h3><p>When hovered, the <app-froala-tooltip-element description="A hover state communicates when a user has placed a cursor above an interactive element." link-label="More on hover state" link-url="/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844" should-open-link-in-new-tab="true">hover</app-froala-tooltip-element> state provides a visual cue that a list item is interactive.</p>

A list with the second item visually altered while hovered over, with a cursor and darker fill.

<p><span style="white-space:pre-wrap">Cursor: Hover</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif1lpwx-03.png?alt=media

Selected list item with cursor, colored fill, and checked box.

<p><span style="white-space:pre-wrap">Cursor: Selected</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif1n85t-04.png?alt=media

<h3>Keyboard &amp; switch</h3><p>When a person tabs to a single-action list, a focus indicator appears, providing a visual cue that the first list item is now <app-froala-tooltip-element description="
A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element> and action can be taken.</p><p>When a person interacts with the focused list item via <strong>Space</strong> or <strong>Enter</strong>, the action is performed.</p>

A focus indicator appears on the first item of a 3-item list, which is then selected.

<p><strong>Tab</strong> key navigates to the list. <strong>Space</strong> or <strong>Enter</strong> keys activate items.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif1rzoz-GM3%20-%20Expressive%20-%20Accessibility%2005%20-%20v01%20with%20Keyboards.mp4?alt=media

<h3>Swipe</h3><p>List items that can be swiped should include alternative ways to access hidden actions, such as a <strong>more</strong> icon.   <br /><br />Swipe alternatives can be:</p><ul type="disc" style="list-style-type:disc"><li><p>Single tap</p></li><li><p>Double tap</p></li><li><p>Long press</p></li><li><p>Other single-point interactions </p></li></ul><p></p>

A list item has a “more” button selected to reveal additional actions.

<p>List items can reveal more actions from swiping or using an accessible secondary action such as a double tap</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmshqfb4p-07-key04.png?alt=media

<h2>Focus</h2>

<h3>Single-action lists</h3><p>The first element in a list should always receive focus, unless the list has a selected element. In that case, focus should go to the selected list item instead.<br /><br />After an element is <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element>, a person should be able to navigate within the list using arrow keys.</p>

The first list item is automatically focused.

<p><strong>Tab </strong>key focuses on the first item or the selected item </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif1yik5-08.png?alt=media

A second list item focused using an arrow key.

<p><strong>Arrow </strong>keys navigate up and down through list items</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif1z0du-09.png?alt=media

<p>All list items must be able to be activated using the <strong>Space</strong> or <strong>Enter</strong> key.  <br /><br /><a href="/m3/pages/lists/guidelines#3e45f939-457a-44a8-8551-a2354c521d26" target="_blank">More on single-action lists</a></p>

List item with focus indicator and filled checkbox, selected using the Space or Enter key.

<p><strong>Space</strong> or <strong>Enter</strong> keys activate an element in a list</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif21ldt-10.png?alt=media

<h3>Multi-action lists</h3><p>Multi-action list items contain a primary action and at least one supplementary action.  <br /><br />The list item as a whole isn't selectable; only the individual actions are.</p><p> A person should be able to use a keyboard to:</p><ul><li><p><strong>Tab</strong> to the list item, which focuses the first element</p></li><li><p>Move between between all focusable elements in the list using the <strong>Up</strong>, <strong>Down</strong>, <strong>Left</strong>, and <strong>Right</strong> arrow keys</p></li><li><p>Activate a focused element using <strong>Space</strong> or <strong>Enter</strong>   </p></li></ul><p><a href="/m3/pages/lists/guidelines#db85439b-0e67-43b0-a2dc-61395738af64" target="_blank">More on multi-action lists</a></p>

The first element in a multi-action list is focused automatically.

<p><strong>Tab</strong> brings the focus to the first action</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmi8um9bl-11-VQA.png?alt=media

The list action, a bookmark, is focused using the Down or Right arrow.

<p><strong>Down</strong> and <strong>Right</strong> arrow keys move focus to the next action of the list item, or to the first action in the next item</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmi8uomf0-12-VQA.png?alt=media

A trailing bookmark icon is focused in the second list item.

<p><strong>Up</strong> and <strong>Left</strong> arrow keys move focus to the previous action of the list item</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmi8uwmgu-13-VQA.png?alt=media

Label text and supporting text of the second list item is in focus using the Up or Left arrow.

<p>If the focus is on a list item’s first action, the <strong>Up</strong> and <strong>Left</strong> arrows move focus back to the last action of the previous item</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmi8v0dqs-14-VQA.png?alt=media

The Space or Enter key activates an overflow menu on a list item.

<p>The <strong>Space</strong> or <strong>Enter</strong> key activates a selected action in a list</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmi8v14y1-15-VQA.png?alt=media

<h2><span style="white-space:pre-wrap">Keyboard navigation</span></h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p><strong>Keys</strong></p></th><th><p><strong>Actions</strong></p></th></tr></thead><tbody><tr><td><p><strong>Tab</strong></p></td><td><p>To move focus to the first list item, last list item, or outside of the list component</p></td></tr><tr><td><p>Down and right arrow keys</p></td><td><p>Moves to the next element in the list; if the focused element is the last in the list, it wraps back to the top of the list</p></td></tr><tr><td><p>Up and left arrow keys</p></td><td><p>Moves to the previous element in the list; if the focused element is the first in the list, it wraps back to the bottom of the list</p></td></tr><tr><td><p><strong>Space</strong> or <strong>Enter</strong></p></td><td><p>To select a list item not yet selected</p></td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<p><app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview/principles" should-open-link-in-new-tab="true">Accessibility</app-froala-tooltip-element> labels are used with assistive devices like screen readers.</p><p>The accessibility label for a list item is typically the same as the <strong>label text</strong> and <strong>supporting text</strong>.</p><p>Some labels, roles, and states are <a href="/m3/pages/lists/accessibility#09e32b7d-78a1-45c1-be12-4c6646cfe1d1" target="_self">dependent on platform</a>.</p>

List item selected to show label of “Bread, sourdough or wheat”.

<p>A list item’s <strong>label text</strong> and <strong>supporting text</strong> is used for its accessibility label</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif3ecf9-16.png?alt=media

<h3>Platform-specific labels </h3>

<h4>Single-select lists</h4><table class="borderGGrey400" style="width:100%"><thead><tr><th><p style="text-align:center"><strong>Trait</strong></p></th><th><p style="text-align:center"><strong>Web</strong></p></th><th><p style="text-align:center"><strong>Android Views (MDC-Android)</strong></p></th><th><p style="text-align:center"><strong>Jetpack Compose</strong></p></th></tr></thead><tbody><tr><td><p>Aria label</p></td><td><p>Container label: Should describe selection type</p><p>List item: Should match the visible label text </p></td><td><p>List item: Should match the visible label text </p></td><td><p>List item: Should match the visible label text </p></td></tr><tr><td><p>Role</p></td><td><p>Container: List box  List item: Option</p></td><td><p>List item: Radio button</p></td><td><p>List item: Radio button</p></td></tr><tr><td><p>State</p></td><td><p>Selected or Not-selected</p></td><td><p>Checked or Not-checked</p></td><td><p>Checked or Not-checked</p></td></tr></tbody></table>

<h4>Multi-select lists</h4><table class="borderGGrey400" style="width:100%"><thead><tr><th><p style="text-align:center"><strong>Trait</strong></p></th><th><p style="text-align:center"><strong>Web</strong></p></th><th><p style="text-align:center"><strong>Android Views (MDC-Android)</strong></p></th><th><p style="text-align:center"><strong>Jetpack Compose</strong></p></th></tr></thead><tbody><tr><td><p>Aria label</p></td><td><p>Container label: Should describe selection type</p><p>List item: Should match the visible label text </p></td><td><p>List item: Should match the visible label text</p></td><td><p>List item: Should match the visible label text </p></td></tr><tr><td><p>Role</p></td><td><p>Container: List box  List item: Option</p></td><td><p>List item: Checkbox</p></td><td><p>List item: Checkbox</p></td></tr><tr><td><p>State</p></td><td><p>Selected or Not-selected</p></td><td><p>Checked or Not-checked</p></td><td><p>Checked or Not-checked</p></td></tr></tbody></table>

<p>On web, a list container’s accessibility label describes the type of selection that can be made, and the role is <strong>List box</strong>.</p>

A list container is selected, showing a label of “Select either bread, pita, or rice” and role of “List box.”

<p>On web, a list container’s role is <strong>List box</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmi8wfvkj-17.png?alt=media

<p>On Jetpack Compose, the role applies to the list item as a whole.</p><p>If a list isn't selectable, the label text is read out without a role.</p>

A selected list item shows a label of “Bread, sourdough, or wheat” and role of “Checkbox.”

<p>When selectable, the role <strong>Checkbox </strong>applies to the entire list item on Jetpack Compose</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmi8wgxsf-18.png?alt=media

<p>On Android Views (MDC-Android), components contained within the list should be labeled according to that component’s specific guidelines:</p><ul><li><p><a href="/m3/pages/checkbox/accessibility" target="_blank">Checkbox</a></p></li><li><p><a href="/m3/pages/radio-button/accessibility" target="_blank">Radio button</a></p></li></ul><p></p>

Checkbox of a selected list item shows label of “Bread, sourdough or wheat” and role of “Checkbox.”

<p>On Android Views (MDC-Android), the accessibility label and role are applied to the interactive component by default</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmif3mprn-19.png?alt=media
