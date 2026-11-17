# Elevation

Source: https://m3.material.io/styles/elevation
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/38354be9-206b-4988-96a8-0f2a88074511.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Elevation is the distance between two surfaces on the z-axis

## Overview

<ul><li>Elevation is applied to all surfaces and components</li><li>Tokens codify the distance on the z-axis to ensure components appear consistently relative to each other</li><li>Tokens have no shadows or color; each platform determines the specific shadows and values to use at each elevation level</li><li>Elevation can be shown as tonal surface colors or shadows</li><li>Avoid changing the default elevation of Material 3 components</li><li>Stick to using a small amount of elevation levels</li></ul>

<p>Elevation is measured as the distance between components along the z-axis in density-independent pixels (dps).</p>

1 diagram shows a light purple square and a darker purple square. A second one shows a side view of the squares in elevation, showing that the light square is lower in elevation than the dark square.

<p>Elevation represents the distance between elements. The product applies color to represent elevation.</p><ol class="decimal"><li><p>One surface at 1dp elevation and another surface at 8dp elevation, as viewed from the front</p></li><li><p>The difference in elevation between the two surfaces is 7dp, as viewed from the side</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwykafum-1.png?alt=media

<h2>Availability &amp; resources</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:19.0341%"><p></p></th><th style="width:37.7388%"><p>Resource</p></th><th style="width:43.1703%"><p>Status</p></th></tr></thead><tbody><tr><td><p>Design</p></td><td><p><a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">Design Kit (Figma)</a><br /></p></td><td><p>Available</p></td></tr><tr><td><p>Implementation</p></td><td><p><a href="https://api.flutter.dev/flutter/material/ElevationOverlay-class.html" target="_blank">Flutter</a><br /></p></td><td><p>Available</p></td></tr><tr><td></td><td><p><a href="https://developer.android.com/develop/ui/compose/designsystems/material3?_gl=1*zh4ff1*_up*MQ..*_ga*MTQ4NTEwOTIzLjE3NDA0MDY2Njk.*_ga_6HH9YJMN9M*MTc0MDQwNjY2OC4xLjAuMTc0MDQwNjY2OC4wLjAuNjU3NTAyNDY.#elevation" target="_blank">Jetpack Compose</a><br /></p></td><td><p>Available</p></td></tr><tr><td></td><td><p><a href="https://github.com/material-components/material-components-android/blob/d56070586102b66486f7f8697de077c3d7689922/docs/theming/Color.md#using-surface-colors" target="_blank">MDC - Android</a><br /></p></td><td><p>Available</p></td></tr><tr><td></td><td><p><a href="https://github.com/material-components/material-web/blob/919fe12badcfee4dcd72c390c0869dd8f996b51c/docs/components/elevation.md" target="_blank">MWC - Web</a><br /></p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Differences from M2</h2>

<ul><li>Shadows: Instead of applying shadows by default to all levels, use shadows only when required to create additional protection against a background or to encourage interaction</li><li>Color: New color mappings and compatibility with dynamic color</li><li>Levels: Elevation is now described in terms of levels</li></ul>

Diagram of 2 concentric squares. The inner square is at 12dp and has a larger shadow than the outer square, which is at 3dp.

<p>M2: Shadows applied at all levels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwykc8yv-2.png?alt=media

Diagram of 2 concentric squares without shadows. Instead, the inner square is at level and tonally darker than the outer square, which is at level 2.

<p>M3: Using color instead of shadows to communicate elevation</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwykckey-3.png?alt=media

<h2>All surfaces and components have elevation values</h2>

<p>Surfaces at different elevations do the following:</p><ol class="decimal"><li><p>Allow surfaces to move in front of and behind other surfaces, such as content scrolling behind app bars</p></li><li><p>Reflect spatial relationships, such as how a FAB's shadow indicates it's separate from a card collection</p></li><li><p>Focus attention on the highest elevation, such as a dialog temporarily appearing in front of other surfaces</p></li></ol>

2 screens showing surfaces moving in front of and behind other surfaces, the shadow of a FAB, and a dialog appearing at the highest elevation.

<p>Elevation can be depicted using shadows or other visual cues, such as surface fills with a tone difference</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwykjf69-GM3-Styles-Elevation-Overview-1-v01.mp4?alt=media

<h3>Resting elevation (default)</h3>

<p><span style="white-space:pre-wrap">All components have a default resting elevation. Avoid changing the default elevation of Material components.</span></p>

A floating action button with a shadow.

<p>All components have a default elevation which should be used</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwykcxkh-5.png?alt=media

<h3>Changing elevation</h3>

<p>Components should change elevation in response to system events or user interaction, like hovering. This elevation change should be consistent across all similar elements.</p><p>For example, hovering a FAB temporarily increases the elevation by 1 level, from level 3 to level 4. All Material buttons increase elevation by 1 level when hovered.</p>

FAB elevation from the top and side showing the button elevation changing from 5dp to 8dp on hover.

<p>Hovering over a button increases its elevation to show user interaction</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwykkk4p-GM3-Styles-Elevation-Overview-2-v01.mp4?alt=media

## Applying elevation

<p>Material 3’s elevation system is deliberately limited to just a handful of levels. This creative constraint means you need to make thoughtful decisions about your UI’s elevation story.</p>

Diagram showing the 5 elevation levels and their respective dp values.

Material uses six levels of elevation, each with a corresponding dp value. These values are named for their relative distance above the UI’s surface: 0, +1, +2, +3, +4, and +5. An element’s resting state can be on levels 0 to +3, while levels +4 and +5 are reserved for user-interacted states such as hover and dragged.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwyl8vgl-1.png?alt=media

<h2>Depicting elevation</h2>

<p>Elevation can be depicted using shadows or other visual cues, such as surface fills with a tone difference or scrims.</p>

<p id="isPasted">To successfully depict elevation, a surface must show:</p><ul><li>Surface edges, contrasting the surface from its surroundings</li><li>Overlap with other surfaces, either at rest or in motion</li><li>Distance from other surfaces</li></ul>

3 images. The first shows a violet square overlapping a white square. The second shows 2 overlapping squares with the same color, but with shadows beneath the top square. The third shows a violet square overlapping a dark gray square.

<ol><li>Two overlapping surfaces with distinct tonal values</li><li>Two overlapping surfaces with the same tonal values separated via shadow</li><li>Two overlapping surfaces with the same tonal values separated via scrim</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwyl9cz5-2.png?alt=media

<h3>Tonal difference</h3>

<p>Tonal difference between surfaces helps to express the tactile quality of Material surfaces. They show where one surface ends and another begins by separating different parts of a UI into identifiable components. For example, the edges of an app bar show that it's separate from a grid list, communicating to the user that the grid list scrolls independently of the app bar.</p><p>By default, Material 3's surfaces use tonal difference to indicate separation. Other methods can be used to indicate edges, such as:</p><ul><li><p>Giving surfaces a drop shadow</p></li><li><p>Placing a scrim behind a surface</p></li></ul>

Elevation, scrim, and tonal differences used to indicate separation.

<ol class="decimal"><li><p>A FAB's elevation helps separate it from body content</p></li><li><p>A scrim appears below a modal to communicate importance</p></li><li><p>Tonal differences between a navigation bar and body content indicate separate surfaces</p></li></ol><p></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwynetr7-3.png?alt=media

<p><span style="white-space:pre-wrap">For interactive components, edges must create sufficient contrast between surfaces (by meeting or exceeding accessible contrast ratios) for them to be seen as separate from one another.</span></p>

FAB separated from the surface beneath it using a shadow.

<p>Ensure floating elements have sufficient contrast with surfaces beneath</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwynhr1z-5_do.png?alt=media

FAB without shadows, insufficiently separated from the surface beneath it.

Don't use colors with insufficient contrast. The relationship between surfaces must be clear.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwyni1qa-4_dont.png?alt=media

<h3>Surface color roles &amp; elevation</h3>

<p>You can pick from a range of surface and surface container color roles. These roles are not tied to elevation, and provide flexibility for defining containment areas.<br /><br />Any overlapping containment areas or components should have different color roles in order to visually communicate separation.<br /><br /><a href="/m3/pages/color-roles/tab-1#89f972b1-e372-494c-aabc-69aea34ed591" target="_blank">More on surface color roles</a></p>

Diagram of email home screen with "1" indicating the list item background color and "2" indicating the navigation bar background color.

<ol><li id="isPasted">Surface</li><li>Surface container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwynjnhh-6.png?alt=media

<h2>Shadows</h2>

<p>Shadows can express the degree of elevation between surfaces in ways that other techniques can't.</p><p>Both a shadow’s size and amount of softness or diffusion express the degree of distance between two surfaces. For example, a surface with a shadow that's small and sharp indicates a surface’s close proximity to the surface behind it. Larger, softer shadows express more distance.</p>

Podcast app with each show displayed as a card separated from the background using small dark shadows.

<p>Smaller, sharper shadows indicate a surface’s close proximity to the surface behind it</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwynkcgy-7.png?alt=media

Podcast app with each show displayed as a card separated from the background using more fuzzy and diffused shadows.

<p>Larger, softer shadows express more distance between a surface and the one behind it</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwynkpp5-8.png?alt=media

<p><span style="white-space:pre-wrap">When it comes to applying shadows, less is more. The fewer levels in your UI, the more power they have to direct attention and action.</span></p>

<h3><span style="white-space:pre-wrap">When to use visible shadows</span></h3>

<h4><strong>Protect elements</strong></h4><p>When a background is patterned or visually busy, the hairline style might not provide sufficient protection. In these cases, use elevation to separate and emphasize elements such as cards, chips, or buttons.</p>

Buttons with shadows separating them from a background image.

<p>Interactive elements are emphasized with elevation</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwynle77-9.png?alt=media

<h4><strong>Encourage interaction</strong></h4><p>Elements can temporarily lift on focus, selection, or another kind of interaction, like swipe. A raised element can also lower when a higher element appears.</p>

Screen in an email app in which sliding over an email card allows you to delete it.

<p>Elevation encourages interaction</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwynmywr-GM3-Styles-Elevation-Applying_Elevation-1-v01.mp4?alt=media

<h2>Scrims</h2>

<p>A scrim can bring focus to specific elements by increasing the visual contrast of a large layered surface. Use the scrim beneath elements like modals and expanded navigation menus.</p><p>Scrims use the scrim <app-froala-tooltip-element description="Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme." link-label link-url should-open-link-in-new-tab="false">color role</app-froala-tooltip-element> at an opacity of 32%.</p>

Large screen news app with a navigation rail separated from the body content by a scrim.

<p>Scrims help bring focus to important elements like the navigation rail</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwynlv1e-11.png?alt=media

## Tokens

<h2>Tokens</h2>

<p>Elevation levels can be implemented with tokens. Surface tint color is deprecated. Use elevation level tokens (0–5) instead. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9

libraryModuleType: ELEVATION

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light']}

<h2>Component elevation</h2>

<p>Most components have a default elevation. Component elevation is only used to determine where the component sits in relation to other components, including when hovered or focused (which usually raises elevation by one level). Elevation has no shadow or value of its own by default.</p>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Resting level</p></th><th><p>Component</p></th><th><p>DP Height</p></th></tr></thead><tbody><tr><th><p>5</p></th><td><p>(not assigned as resting level) </p></td><td><p>12dp</p></td></tr><tr><th><p>4</p></th><td><p>(not assigned as resting level)</p></td><td><p>8dp</p></td></tr><tr><th><p>3</p></th><td><p>Date pickers</p><p>Dialogs (modal)</p><p>Extended FAB</p><p>FAB</p><p>FAB menu (close button)</p><p>Search</p><p>Time pickers</p></td><td><p>6dp</p></td></tr><tr><th><p>2</p></th><td><p>App bar (scrolled)</p><p>Menu</p><p>Navigation bar</p><p>Rich tooltip</p><p>Toolbar</p></td><td><p>3dp</p></td></tr><tr><th><p>1</p></th><td><p>Banner</p><p>Bottom sheet (modal)</p><p>Button (elevated)</p><p>Card (elevated)</p><p>Chips (elevated)</p><p>Navigation drawer (modal)</p><p>Side sheet (modal)</p></td><td><p>1dp</p></td></tr><tr><th><p>0</p></th><td><p>App bar (not scrolled)</p><p>Buttons (filled, tonal, outlined)</p><p>Button groups</p><p>Cards (filled, outlined)</p><p>Carousel</p><p>Chips</p><p>Dialog (full-screen)</p><p>Extended FAB (in navigation rail)</p><p>FAB (in navigation rail)</p><p>FAB menu (list items)</p><p>Icon buttons</p><p>List</p><p>Navigation rail</p><p>Segmented button</p><p>Side sheet (docked)</p><p>Slider</p><p>Split button</p><p>Tabs</p></td><td><p>0dp</p></td></tr></tbody></table></div>
