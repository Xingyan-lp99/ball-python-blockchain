# XR components

Source: https://m3.material.io/foundations/xr/components
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/eef0dedf-83d1-41d0-a4b0-7072b620e5ac.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Learn how Material 3 Expressive components adapt to extended reality devices 

## Overview

<ul><li><p>Leverage depth and space to create believable environments</p></li><li><p>Design for comfort to minimize motion sickness and physical strain</p></li><li><p>Map interactions, like gaze and gestures, to real-world expectations</p></li><li><p>Group UI elements on floating spatial panels</p></li><li><p>Provide feedback through spatial audio, haptics, and visual cues</p></li></ul>

Animation showing a toolbar changing from 2D to 3D.

<p>A toolbar’s behavior and placement changes from a 2D to a 3D experience</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxffyh5-toolbars-xr-06%20(2).mp4?alt=media

<h2>Material XR components</h2>

<p>The following Material components are adapted for XR:</p><ul><li><p><a href="/m3/pages/xr-components/app-bars" target="_blank">App bars</a></p></li><li><p><a href="/m3/pages/xr-components/dialogs" target="_blank">Dialogs</a></p></li><li><p><a href="/m3/pages/xr-components/nav-bar" target="_blank">Navigation bar</a></p></li><li><p><a href="/m3/pages/xr-components/nav-rail" target="_blank">Navigation rail</a></p></li><li><p><a href="/m3/pages/xr-components/toolbars" target="_blank">Toolbars</a></p></li></ul>

Side view of an XR dialog showcasing spatial elevation.

<p>A dialog can be spatially elevated on the Z-axis above spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxgb0ta-06.png?alt=media

## App bars

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">XR guidelines are primarily intended for designers. Find what’s implemented in code in the <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">design kit</a>.</div></div></div>

<p>Extended reality (XR) interfaces have special design requirements, like showing apps in 3D space. Material has an XR app bar with custom specs and guidance. See <a href="https://developer.android.com/design/ui/xr/guides/foundations" target="_blank">XR developer documentation</a> for more details.</p>

<h2>Variants &amp; configurations</h2>

<p>There is one app bar <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels." link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiter</app-froala-tooltip-element>. It closely aligns with the <app-froala-tooltip-element description="Small app bars display information and actions in compact layouts. They're often used for scrolled views on subpages that require back navigation and multiple actions." link-label="More on small app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">small app bar</app-froala-tooltip-element>. It can be configured to be center-aligned or left-aligned.</p>

Center and left-aligned app bar orbiters.

<ol class="decimal" id="isPasted"><li>Center-aligned app bar</li><li>Left-aligned app bar</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5ntwab-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/4Vdn-iH-z3fko57KiqLULyRWIN845IFV7T3yC7smqZ9bVb5vXsO3s_-BaAojJNwXIcW6uorvb3qjbFxvnyeWP23NOEldVjMIdxoWm-07oCk=s2048

<h2 id="isPasted">Anatomy</h2>

Diagrams of app bar orbiters identifying 4 internal elements.

<ol class="decimal" id="isPasted"><li>Container</li><li>Headline</li><li>Trailing icons</li><li>Leading icon</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5nuh2w-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/u2YwIRPzgQXNG2dOG6VjZ42_rl1vEV32kphFtG-in9JaGpdtAMOnMZTtyE49JpCTqNB4ZyTFyytePqLOah_QmHUJUUZYM73r7Zw3lr-j9g_J=s2048

<h2 id="isPasted">Color &amp; elevation</h2>

<p>XR uses color to communicate the elevation of UI elements and orbiters. With <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation" target="_blank">spatial elevation</a>, the app bar displays above the <app-froala-tooltip-element description="In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content." link-label="More on spatial panels" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels" should-open-link-in-new-tab="true">spatial panel</app-froala-tooltip-element> on the Z-axis. Elevated app bars can use any of these color options:</p>

3 versions of app bar elevation color strategy.

<ol class="decimal" id="isPasted"><li>Surface container</li><li>Surface container high</li><li>Surface container highest</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5nuy7e-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/0hgrQRQF5mEFNy0s_RbxRDEV7fJYHsWUq0adzDor4Ogpq5nNCNmQrrJA-2hJgwv315HAyAMpxpVwDQe7RrZ7VOR5UGJGSrNE_56L4e2NLGyf=s2048

<h2 id="isPasted">Measurements</h2>

Diagrams with measurements and padding for app bar orbiters.

<p>Measurements and padding for app bar orbiters</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmq7w2v1g-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/IzfAl6XWiO_JPWqGVK4P-7us8V9d_iehPeqgzzROuGZhbpvUMolBMBa9x9BMbL5iNZTTwEHNJsxIA28WUMtKuS501yiQq7_7I6q1RQlDN7Y=s2048

<h2 id="isPasted">Usage</h2>

<p>An app bar can appear in an <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels." link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiter</app-froala-tooltip-element> for a more immersive experience. Currently, this spatial capability is only available in <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components." link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element>. In <app-froala-tooltip-element description="Home space is compatible with mobile and large screen apps, but doesn’t support spatial components." link-label="More on home space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">home space</app-froala-tooltip-element>, use a regular app bar on the same plane as the body content to mimic a 2D experience.</p>

Animation showing an app bar changing from 2D to 3D.

<p>An app bar’s behavior and placement changes from a 2D to a 3D experience</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowvrdts-XR_Top-App-Bar_Usage_01_IA_v03%20(1).mp4?alt=media

<h2 id="isPasted">Behavior</h2>

<h3 id="isPasted">Global context</h3><p>When placed in global context, the orbiter is centered at the top of the app it controls. </p><p>It stays anchored to the app during layout or content changes. </p><p>This ensures navigation elements are always easy to find and use.</p>

An app bar orbiter placed in global context.

<p>Global app bar orbiters should be centered and anchored to the top of the app</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowvuyn4-XR_Top-App-Bar_Behavior_01_IA_v03%20(1).mp4?alt=media

<h3 id="isPasted">Local context</h3><p>When placed in local context, the orbiter is centered at the top of the spatial panel it controls. </p><p>It repositions in response to layout or content changes.</p>

An app bar orbiter placed in local context.

<p>Local app bar orbiters should be centered and anchored to the top of the panel. However, this is less common, so make sure that it contains actions that only affect its anchored panel.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowvzhjn-XR_Top-App-Bar_Behavior_02_IA_v03%20(1).mp4?alt=media

<h3 id="isPasted">Additional app bars</h3><p>In most cases, apps should only have one app bar orbiter, placed in global context.</p>

An app switches between 1 and 2 app bar orbiters.

<p>Limit the use of multiple app bars to rare cases when additional spatialization improves usability</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoww3e8a-XR_Top-App-Bar_Behavior_03_IA_v03%20(1).mp4?alt=media

<h2 id="isPasted">Placement</h2>

<h3>Offset &amp; inset positioning</h3>

<p>In full space, an app bar orbiter can be positioned:</p><ul><li><p>Offset 20dp from the spatial panel</p></li><li><p>Inset 12dp, overlapping spatial panel without obstructing content</p></li></ul>

App bar orbiter with offset positioning.

<p>An app bar orbiter with a 20dp offset creates visual separation from the spatial panel</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowwbs16-09.png?alt=media

App bar orbiter with inset positioning that obstructs content..

<p>Don’t overlap the app bar orbiter and spatial panel more than 12dp</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowwe02f-10.png?alt=media

<h3>Horizontal alignment</h3>

An app bar orbiter placed within the bounds of its spatial panel.

<p>Always align the app bar orbiter within the bounds of nearby spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowwevxe-11.png?alt=media

An app bar orbiter that extends beyond the width of its spatial panel.

<p>The app bar orbiter shouldn’t exceed the width of adjacent spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowwgpq6-12.png?alt=media

<h3>Spatial panel alignment</h3><p>By default, app bar orbiters are center-aligned to the spatial panel. Their width and placement can be adjusted to accommodate specific user needs, such as improved ergonomics or <a href="/m3/pages/bidirectionality-rtl" target="_blank">right-to-left (RTL) languages</a>.</p>

App bar orbiter alignment options in relation to spatial panels: left, center, and right-aligned.

<p>App bar orbiters can align to the center, left, or right of the spatial panel</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowxpzvt-XR_Top-App-Bar_Spatial-pane-alignment_01_IA_v03%20(1).mp4?alt=media

<h3>Width boundaries</h3><p>An app bar orbiter’s width should adjust to stay in a person’s <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place" target="_blank">field of view</a>. </p><p>This makes crucial navigation elements easy to find.</p>

An app bar orbiter with a width that fits in a person’s field of view.

<p>Adjust the width of the app bar orbiter to fit in a person’s field of view</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowy6885-14.png?alt=media

<p>It’s not recommended to increase the width of an app bar orbiter beyond a person’s natural <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place" target="_blank">field of view</a>. </p><p>This creates a visual imbalance and makes it difficult to find navigation elements.</p>

An app bar orbiter that exceeds the panel’s width and a person’s field of view.

<p>Avoid expanding the app bar orbiter beyond the adjacent panel’s width and a person’s field of view</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowy73ja-15.png?alt=media

<h3 id="isPasted">Adaptable width</h3><p>When placed in a local context, an app bar orbiter can expand to the width of its adjacent spatial panel.   </p><p>Be sure the orbiter stays in a person’s field of view, and test for usability.</p>

2 app bar orbiters with the same width as their adjacent spatial panels.

<p>Use caution before expanding the app bar’s width to match its spatial panel. The orbiter may not fit in a person’s primary field of view.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp1yzz8i-XR_Top-App-Bar_Adaptable-width_01_IA_v03.mp4?alt=media

<h2 id="isPasted">Accessibility considerations</h2>

<p><a href="/m3/pages/xr-design/accessibility" target="_blank">XR accessibility</a> guidelines are still evolving. XR app bars should follow applicable Material <a href="/m3/pages/app-bars/accessibility" target="_blank">app bar accessibility standards</a>.</p>

## Dialogs

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">XR guidelines are primarily intended for designers. Find what’s implemented in code in the <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">design kit</a>.</div></div></div>

<p>Extended reality (XR) introduces spatial capabilities, such as using depth to make dialogs stand out from the background. Currently, <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">spatial dialogs</a> are only available in <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components." link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element>. For <app-froala-tooltip-element description="Home space is compatible with mobile and large screen apps, but doesn’t support spatial components." link-label="More on home space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">home space</app-froala-tooltip-element>, follow Material’s general <a href="/m3/pages/dialogs/overview" target="_blank">dialog guidance</a>.</p>

<h2>Color &amp; elevation </h2>

<p>XR uses <app-froala-tooltip-element description="Material has 26 standard color roles organized into six groups: primary, secondary, tertiary, error, surface, and outline." link-label="More on color roles" link-url="/m3/pages/color-roles?s=m3" should-open-link-in-new-tab="true">color roles</app-froala-tooltip-element> to communicate the elevation of UI elements. Dialogs can use two color options: <strong>surface container high</strong> or <strong>surface container highest</strong>.</p><div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">Color and elevation for spatial dialogs aren’t available in Jetpack Compose yet. These need to be customized manually.</div></div></div>

2 spatially elevated dialogs with surface-container-high and surface-container-highest color roles.

<ol class="decimal"><li id="isPasted">Surface container high</li><li>Surface container highest</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5rmvr7-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/EjSLZTrL4uodRu2zxhzKEha1u7_lD_9F6-U3c1_IoEMey42K7eFCP-emC0YOBvl-xcHnJuNoSk_h-Nb-hvJAhQmBKbZTt-Xqt-H60sClLJ6cgw=s2048

<p id="isPasted">For effective visual hierarchy, a dialog should be the most prominent element. </p><p>Add a scrim behind a dialog to improve its visibility. Scrims prevent other content from being selected until the dialog action is complete.</p>

Dialog with surface-container-highest color and a scrim.

<p>Make sure a spatial dialog’s color is higher than all other UI elements, and use a scrim</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmox7g5yi-02.png?alt=media

<p id="isPasted">The dialog should have the highest elevation in the product.</p><p>For example, if the dialog is <strong>surface container high</strong>, don’t use <strong>surface container highest</strong> for any other elements.</p>

Dialog with surface-container-high color and no scrim. An orbiter is at a higher elevation than the dialog.

<p>If a dialog’s color is <strong>surface container high</strong>, don’t use <strong>surface container highest</strong> for any other element</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmox7nrut-03.png?alt=media

<h2>Usage</h2>

<p>Only use <a href="/m3/pages/dialogs/guidelines#97ac3858-3932-4084-ae8e-73e42b7cb752" target="_blank">basic dialogs</a> in XR. This keeps the required action in the person’s <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place" target="_blank">field of view</a>. </p>

Basic dialog in XR.

<p>A basic dialog elevated above an app in home space </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmox7s3sr-04.png?alt=media

Full-screen dialog in XR.

<p>Avoid using full-screen dialogs in XR. Required actions could appear beyond a person’s field of view.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmox7ytt7-05.png?alt=media

<h2>Spatial dialogs</h2>

<p>In <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components. " link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element>, dialogs can be <app-froala-tooltip-element description="Spatial elevation displays a component above an app on the Z-axis." link-label="More on spatial elevation" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation " should-open-link-in-new-tab="true">elevated spatially</app-froala-tooltip-element> via <a href="https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design#use-enablexrcomponentoverrides" target="_blank">overrides</a>. This helps dialogs stand out from their background in XR.</p>

Side view of basic dialog showcasing spatial elevation.

<p>Side view of a basic dialog with spatial elevation in full space</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmox83eps-06.png?alt=media

<h2>Behavior</h2>

<h3>Effect</h3><p id="isPasted">The spatial dialog should scale uniformly. It also fades in when appearing, and fades out when disappearing. </p><p>The dialog's scrim only fades in and out.</p><p><br /></p>

A direct view of a spatial dialog appearing and disappearing.

<p>Front view of a spatial dialog in motion in full space</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmox8cric-XR_Dialog_Behavior_01_IA_v02%20.mp4?alt=media

<h3>Movement</h3><p>When activated, the spatial dialog rises from the app to the highest resting level on the Z-axis. </p><p>When the action is complete, it returns to a normal resting level.</p><p>The dialog's scrim stays at the app content level at all times.</p><p>To prevent motion sickness, use <a href="/m3/pages/motion-easing-and-duration/tokens-specs#601d5552-a6e6-4d74-9886-ff8f24b9ec35" target="_blank">standard easing</a> and <a href="/m3/pages/motion-easing-and-duration/tokens-specs#48bf653e-46f9-48f5-87e0-eaf8ea3fe716" target="_blank">long duration</a> motion tokens.</p>

A spatial dialog elevating on the Z-axis, as seen from a side angle.

<p>Side view of a spatial dialog in motion in full space</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmox8drwx-XR_Dialog_Behavior_02_IA_v02%20.mp4?alt=media

<h2>Placement</h2>

<p>Consider factors like field of view, viewing distance, and possible interactions when deciding where to place dialogs in XR.<br /><br />A dialog’s placement can be adjusted to accommodate specific needs, such as improved ergonomics or <a href="/m3/pages/bidirectionality-rtl" target="_blank">right-to-left (RTL) languages</a>.</p>

<h3>Elevation: Highest resting level</h3><p>Display spatial dialogs at the <strong>highest resting level</strong>. When setting the depth value of the highest resting level, make sure the elevated dialog is at a comfortable viewing distance from the person. <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation" target="_blank">More on spatial elevation</a></p>

An animated side view of a dialog moving from the lowest to the highest resting level.

<p>A spatial dialog moves to the highest resting level in full space</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmox8ubbg-GM3_XR_Dialogs_Motion_Placement_01_IA_v03.mp4?alt=media

<h3>Center spatial dialogs in field of view</h3><p>Spatial dialogs should be centered in a person’s <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place" target="_blank">field of view</a>. If the dialog <strong>can’t</strong> track head movements, position it in the center of the app’s content. </p><p>If the dialog <strong>can</strong> track head movements, configure it with a lazy follow behavior. This keeps the dialog anchored to the center of a person’s field of view until an action is taken.</p>

A dialog follows a person’s head movements, remaining centered in their field of view.

<p>A dialog in full space stays centered in a person’s field of view</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmox8yi7x-GM3_XR_Dialogs_Motion_Placement_02_IA_v05.mp4?alt=media

<h2>Accessibility considerations</h2>

<p><a href="/m3/pages/xr-design/accessibility" target="_blank">XR accessibility</a> guidelines are still evolving. Spatial dialogs should follow applicable Material <a href="/m3/pages/dialogs/accessibility" target="_blank">dialog accessibility standards</a>.</p>

## Nav bar

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">XR guidelines are primarily intended for designers. Find what’s implemented in code in the <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">design kit</a>.</div></div></div>

<p>Extended reality (XR) interfaces have special design requirements, like showing apps in 3D space. Material has an XR navigation bar with custom specs and guidance. See <a href="http://developer.android.com/design/ui/xr/guides/foundations" target="_blank">XR developer documentation</a> for more details.</p>

<h2>Anatomy</h2>

Diagram of navigation bar orbiter identifying 7 internal elements of the component.

<ol><li>Container</li><li>Icon</li><li>Active indicator </li><li>Small badge (optional)</li><li>Large badge (optional)</li><li>Large badge label (optional)</li><li>Label text</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5rw7th-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/klVeOaaaMwxNa_W3IC8bbQPBzm2px87bnuY0WeMxdlt-V2oqj-7FMUFQ19AOe84qGspMekq2coIMmERquGEMzaWB4-emdoM_BrcxyGzrnQt76w=s2048

<h2>Color &amp; elevation</h2>

<p>On XR, color is used to highlight elevated UI elements and <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels." link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiters</app-froala-tooltip-element>. With <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation" target="_blank">spatial elevation</a>, the navigation bar displays above the <app-froala-tooltip-element description="In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content. " link-label="More on spatial panels" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels" should-open-link-in-new-tab="true">spatial panel</app-froala-tooltip-element>, on the Z-axis. Color communicates elevation on UI elements and orbiters. Elevated nav bars can use any of these color options:</p>

4 versions of elevation color strategy.

<ol><li>Surface container</li><li>Surface container high</li><li>Surface container highest</li><li>Tertiary container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5rwtar-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ErJmjTcE4AIy4dr7PHYehMqYEn0UI580rBDsKd6qUXYRysNmAT-b3rynVJESfaxN0Hiz_u_13CrGH2uZSgOiHMTHcYH720nqpUj0owOCb18g=s2048

<h2>Measurements</h2>

Measurements and padding for navigation bar orbiter.

<p><span style="white-space:pre-wrap">Navigation bar orbiter padding and measurements</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5rxeyw-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/BcrwOJqRJbnxwXFBGwH96tPEyUbd-dcc-t6Kl466KmDu-pe0M40HvWFGkBlPtX2CdKWIRafPD43o-xTvsNexNEt-mYCZ7FEAqPXBZMkSGy_i=s2048

<h2>Usage</h2>

<p>In <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components. " link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element>, a navigation bar can appear in an <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels." link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiter</app-froala-tooltip-element> for a more immersive experience. Currently, spatial capabilities, such as orbiters, are only available in full space. In <app-froala-tooltip-element description="Home space is compatible with mobile and large screen apps, but doesn’t support spatial components." link-label="More on home space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">home space</app-froala-tooltip-element>, use a regular navigation bar on the same plane as the body content to mimic a 2D experience.</p>

Interface showcasing navigation bar behavior and placement when transitioning from a 2D to 3D experience.

<p><span style="white-space:pre-wrap">Navigation bar behavior and placement changing when going from a 2D to a 3D experience</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cj01s5-navbar_01.mp4?alt=media

<h2>Behavior</h2>

<h3>Global context</h3><p>When placed in global context, the navigation bar orbiter is centered at the bottom of the app it controls. It stays anchored to the app during layout or content changes. This ensures navigation elements are easy to find and use.</p>

A navigation bar orbiter placed in global context.

<p><span style="white-space:pre-wrap">A navigation bar orbiter centered and anchored to the bottom of the app</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp0xfkl2-navbar_07.mp4?alt=media

<h3>Local context</h3><p><span style="white-space:pre-wrap" id="isPasted">When placed in local context, the navigation bar orbiter is centered at the bottom of the spatial panel it controls. It repositions in response to layout or content changes.</span></p>

A navigation bar orbiter placed in local context.

<p><span style="white-space:pre-wrap">Use caution before placing a navigation bar in local context. If it contains navigation elements that affect the overall app, a navigation bar orbiter should be placed in global context.</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma4aas8k-XR_Nav-Bar_Behavior_02_V02.mp4?alt=media

<h2>Placement</h2>

<h3>Navigation context</h3><p>The position of the navigation bar orbiter should communicate its navigational context:</p><ul><li><p>Use <strong>offset positioning</strong> for global actions that affect the overall app experience</p></li><li><p>Use <strong>inset positioning</strong> for local actions that are specific to a spatial panel</p></li></ul><p>A navigation bar orbiter can either overlap or be positioned adjacent to spatial panels with a 20dp margin for visual separation.</p>

Navigation bar orbiter offset and inset positioning.

<p><span style="white-space:pre-wrap">Position the navigation bar orbiter to reflect context: offset for global actions, inset for spatial panel-specific actions</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxalxwd-navbar_02.mp4?alt=media

<h3>Inset positioning</h3><p><span style="white-space:pre-wrap" id="isPasted">Don’t obstruct content. To ensure a balanced and uncluttered layout, a navigation bar orbiter should overlap spatial panels by 12dp and no more than half their height.</span></p>

Navigation bar orbiter inset positioning beyond the 12dp recommendation.

<p><span style="white-space:pre-wrap">Avoid overlapping an inset a navigation bar orbiter by more than half its height</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxaokg7-navbar_04.mp4?alt=media

<h3>Horizontal alignment</h3><p><span style="white-space:pre-wrap" id="isPasted">The navigation bar orbiter placement shouldn't exceed the width of adjacent spatial panels.</span></p>

Nav bar orbiter placement that exceeds the width of its spatial panel.

<p><span style="white-space:pre-wrap">The navigation bar orbiter shouldn’t exceed the width of the spatial panel</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxaqxbc-navbar_05.mp4?alt=media

<h3>Spatial panel alignment</h3><p>A navigation bar orbiter should always be placed at the bottom of a spatial panel and within the immediate field of view (FOV).</p><p>Their placement can be adjusted to accommodate specific needs, such as improved ergonomics or <a href="/m3/pages/bidirectionality-rtl" target="_blank">right-to-left (RTL) languages</a>.<br /><br />Avoid placing the navigation bar orbiter at the top of a spatial panel, as this area is typically reserved for app bar orbiters or other critical UI elements.</p>

Nav bar orbiter incorrectly placed above a spatial panel.

<p><span style="white-space:pre-wrap">Don't position a navigation bar orbiter at the top of a spatial panel. Position it at the bottom in the field of view to maintain usability and minimize interaction effort.</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxaupni-navbar_06.mp4?alt=media

<h2>Accessibility considerations</h2>

<p>XR navigation bars should follow applicable Material <a href="/m3/pages/navigation-bar/accessibility" target="_blank">nav bar accessibility standards</a>. <a href="/m3/pages/xr-design/accessibility" target="_blank">More on XR accessibility</a></p>

## Nav rail

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">XR guidelines are primarily intended for designers. Find what’s implemented in code in the <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">design kit</a>.</div></div></div>

<p>Extended reality (XR) interfaces have special design requirements, like showing apps in 3D space. Material has an XR navigation rail with custom specs and guidance. See <a href="http://developer.android.com/design/ui/xr/guides/foundations" target="_blank">XR developer documentation</a> for more details.</p>

<h2>Variants</h2>

<p>There are two variants of navigation rail <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels." link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiters</app-froala-tooltip-element>: the contained FAB and spatialized FAB navigation rails.</p>

Navigation bar orbiters with a contained FAB and a spatialized FAB.

<ol class="decimal"><li>Contained FAB rail</li><li>Spatialized FAB rail</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5sirou-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LTbAfuniDUxE5CSE6GZ6jbZIfZm1ve6oIy0VM0dLlOHrKwOwK673gmbTbQccfUqR3VzntYUsiumoJjVPGf2enwIgn6Zdg357hqxsVw2e0jw=s2048

<h2>Anatomy</h2>

Diagram of navigation rail orbiter identifying 9 internal elements of the component.

<ol><li>Container</li><li>Active indicator</li><li>Large badge (optional)</li><li>Badge (optional)</li><li>Large badge label (optional)</li><li>Label text</li><li>Icon</li><li>Embedded or spatialized FAB (optional)</li><li>Menu icon (optional)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5sjxq7-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/QXw8Vtmzpdjkr8pT7-YI9BsDLetxKSQ_SgG92DhzpcSU19BI4E4wumNJFLo6RlwdQdFbKTp1s_X_i-uonqulQZHZhkTwofW3IZ1NL0bk3BTy=s2048

<h2>Color &amp; elevation</h2>

<p>On XR, color is used to highlight elevated UI elements and orbiters. With <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation" target="_blank">spatial elevation</a>, the navigation bar displays above the <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels" target="_blank">spatial panel</a>, on the Z-axis. Color communicates elevation on UI elements and orbiters. Elevated nav rails can use any of these color options:</p>

4 versions of elevation color strategy.

<ol><li>Surface container with tertiary FAB</li><li>Surface container high with tertiary fixed dim FAB</li><li>Surface container highest with tertiary fixed dim FAB</li><li>Tertiary container with primary FAB</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5smtp2-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/PUP9hRb--aOh9alxfJ8GTosaseAIpkMhRlrOCZvN-HzA_vUJ94qMvbAkikPv-OmXmm93qceIK8q28Xg4BY359zhg95TE3PNJWbYoG7X7keQA=s2048

<h2>Measurements</h2>

Measurements and padding for navigation rail orbiter with contained FAB.

<p>Navigation rail orbiter padding and measurements with contained FAB</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5sl333-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/CFyQGJBT04A8x0XA9GIvKWTxYwd37_eA4Qr0A_cFbr4vl5gXTIyRsSnjEzqqtw2BFFW63JPiSegqtZGGJFnCjMV17slaSxa6l_RXDBPErQWJ=s1004

Measurements and padding for navigation rail orbiter with spatialized FAB.

<p><span style="white-space:pre-wrap">Navigation rail orbiter padding and measurements with spatialized FAB</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5slo7l-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/dkFQ1ILUuuM_LNF15rl-Qg4pGr9WX3hLZYgo9hqNoqEsbJPY6VuimtA4d6jzNDeSFwJ6YpjytNUQULppjQNjAw-hlGiUmEwshHlqCz843qf4=s1004

<h2>Usage</h2>

<p>In <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components. " link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element>, a navigation rail can appear in an orbiter for a more immersive experience. Currently, spatial capabilities, such as <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels." link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiters</app-froala-tooltip-element>, are only available in full space. In <app-froala-tooltip-element description="Home space is compatible with mobile and large screen apps, but doesn’t support spatial components." link-label="More on home space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">home space</app-froala-tooltip-element>, use a regular navigation rail on the same plane as the body content to mimic a 2D experience.</p>

Interface showcasing navigation rail behavior and placement when transitioning from a 2D to 3D experience.

<p><span style="white-space:pre-wrap">Navigation rail orbiter behavior and placement changing when going from a 2D to a 3D experience</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxcb5no-navrail_01.mp4?alt=media

<h2>Behavior</h2>

<h3>Global context</h3><p><span style="white-space:pre-wrap" id="isPasted">Intended for global navigation, a nav rail orbiter should be centered along the left or right edge of the app it controls. It stays anchored to the app during layout or content changes to ensure controls are easy to find. </span></p>

A navigation rail orbiter placed in global context.

<p><span style="white-space:pre-wrap">A navigation rail orbiter should be placed in global context, centered and anchored to the left or right of the app</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma4acdxe-XR_Nav-Rail_Behavior_01_V02.mp4?alt=media

<h3>Local context</h3><p>Don’t place a navigation rail orbiter in local context or <a href="/m3/pages/xr-components/nav-rail#d965ae72-bd1b-45a9-b4d3-d1d542e72087" target="_self">between spatial panels</a>. Local placement can make controls hard to find. Nav rails are designed for app-level navigation, so should only use the global context.</p>

A navigation rail orbiter placed in local context.

<p><span style="white-space:pre-wrap">Avoid placing a navigation rail orbiter in local context. It can be hard to find if placed between two spatial panels.</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fma4acsak-XR_Nav-Rail_Behavior_02_V02.mp4?alt=media

<h2>Placement</h2>

<h3>Navigation context</h3><p>The position of the navigation rail orbiter should communicate its navigational context:</p><ul><li><p>Use <app-froala-tooltip-element description="Offset positioning is when orbiters are placed adjacent to spatial panels without overlap." link-label="More on offset positioning" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true"><strong>offset positioning</strong></app-froala-tooltip-element> for global actions that affect the overall app experience</p></li><li><p>Use <app-froala-tooltip-element description="Inset positioning is when orbiters overlap with spatial panels." link-label="More on inset positioning" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true"><strong>inset positioning</strong></app-froala-tooltip-element> for local actions that are specific to a spatial panel</p></li></ul><p>A navigation rail orbiter can either overlap or be positioned adjacent to spatial panels with a 20dp margin for visual separation.</p>

Navigation rail orbiter offset and inset positioning.

<p><span style="white-space:pre-wrap">Position the navigation rail orbiter to reflect context: offset for global actions, inset for spatial panel-specific actions</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxck8bj-navrail_02.mp4?alt=media

<h3>Inset positioning</h3><p><span style="white-space:pre-wrap" id="isPasted">Don’t obstruct content. To ensure a balanced and uncluttered layout, a navigation rail orbiter should overlap spatial panels by 12dp and no more than half their width.</span></p>

Nav rail orbiter overlapping content by more than half its width.

<p><span style="white-space:pre-wrap">Avoid overlapping an inset navigation rail orbiter by more than half its width</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxcmy1y-navrail_03.mp4?alt=media

<h3>Vertical alignment</h3><p><span style="white-space:pre-wrap" id="isPasted">A navigation rail orbiter can be aligned to the top, middle, or center of spatialized panels, providing different levels of visual prominence and accessibility.<br /><br />Align the navigation rail orbiter based on the specific design and user experience goals for the application.</span></p>

Nav rail orbiter positioning moving from the top, to middle, to center of spatialized panels.

<p>Align the navigation rail orbiter at the top or center of spatialized panels</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxcqi3i-navrail_04.mp4?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">The navigation rail orbiter placement shouldn't exceed the height of adjacent spatial panels.</span></p>

A nav rail orbiter positioning above its spatial panel.

<p><span style="white-space:pre-wrap">The navigation rail orbiter shouldn’t exceed the height of the spatial panel</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxd1s5j-navrail_05.mp4?alt=media

<h3>Spatial panel alignment</h3><p>Avoid placing a navigation rail orbiter between spatial panels. This negatively affects the interface structure.</p><p>Navigation rail placement can be adjusted to accommodate specific needs, such as improved ergonomics or <a href="/m3/pages/bidirectionality-rtl" target="_blank">right-to-left (RTL) languages</a>.<br /><br />For layouts that span more than two spatial panels, consider using a <a href="/m3/pages/xr-components/nav-bar" target="_blank">navigation bar orbiter</a>.</p>

A nav rail orbiter incorrectly positioned between spatial panels.

<p><span style="white-space:pre-wrap">Don't place a navigation rail orbiter between spatial panels</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxdaai7-navrail_06.mp4?alt=media

<h2>Spatialized FAB</h2>

<p>There are two variants of navigation rail orbiters with different FAB treatments:</p><ul><li><p><strong>Contained FAB rail:</strong> A contained FAB within the rail. This offers a compact and familiar layout.</p></li><li><p><strong>Spatialized FAB rail:</strong> The FAB becomes an orbiter of its own and is placed outside the navigation rail orbiter. Use this for higher emphasis and a distinct spatial effect.</p></li></ul><p>Use the spatialized FAB rail to emphasize key actions and leverage XR hierarchy. Use the contained FAB rail to be more subtle, and align the experience with the baseline navigation bar.</p>

Interface showing the difference between a navigation rail orbiter with a contained FAB and spatialized FAB.

<p><span style="white-space:pre-wrap">Choose between a navigation rail orbiter with a contained FAB or a spatialized FAB</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxd8z8l-navrail_07.mp4?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">To maintain visual association, place the spatialized FAB in close proximity to the navigation rail orbiter. Material recommends a 20dp margin.<br /><br />The spatialized FAB can be placed above or below the navigation rail orbiter.</span></p>

Spatialized FAB positioned close to the navigation rail orbiter.

<p><span style="white-space:pre-wrap">Position the spatialized FAB close to the navigation rail orbiter</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxdgsuy-navrail_08.mp4?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">While the spatialized FAB and navigation rail orbiter are typically positioned together, their placement is adaptable.</span></p>

Spatialized FAB positioned with excessive spacing between itself and the navigation rail orbiter.

<p><span style="white-space:pre-wrap">Use caution when positioning spatialized FABs. Keep them within the height of adjacent spatial panels</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4cn0kcj-navrail_09.mp4?alt=media

<h2>Accessibility considerations</h2>

<p><a href="/m3/pages/xr-design/accessibility" target="_blank">XR accessibility</a> guidelines are still evolving. XR navigation rails should follow applicable Material <a href="/m3/pages/navigation-rail/accessibility" target="_blank">nav rail accessibility standards</a>.</p>

## Toolbars

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">XR guidelines are primarily intended for designers. Find what’s implemented in code in the <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">design kit</a>.</div></div></div>

<p>Extended reality (XR) interfaces have special design requirements, like showing apps in 3D space. Material has an XR toolbar with custom specs and guidance. Read <a href="https://developer.android.com/design/ui/xr/guides/foundations" target="_blank">XR developer documentation</a> for more details.</p>

<h2>Variants</h2><p>There is one toolbar <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels." link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiter</app-froala-tooltip-element>. It closely aligns with the <app-froala-tooltip-element description="Floating toolbars float on top of page content and can provide contextual, dynamic actions." link-label="More on toolbars" link-url="/m3/pages/toolbars/overview" should-open-link-in-new-tab="true">floating toolbar</app-froala-tooltip-element>. It can be configured to be horizontal or vertical. <a href="https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/package-summary#HorizontalFloatingToolbar(kotlin.Boolean,androidx.compose.ui.Modifier,androidx.compose.material3.FloatingToolbarColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.material3.FloatingToolbarScrollBehavior,kotlin.Function1,kotlin.Function1,kotlin.Function1)" target="_blank">Go to XR toolbar API reference</a></p>

Horizontal and vertical toolbar orbiters.

<ol class="decimal"><li id="isPasted">Horizontal floating toolbar</li><li>Vertical floating toolbar</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5sscqe-01-1P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ds2nZJkQR-ChJVdNLWz0le3T0Qrn7_7xC3m88jQKzP0vtewiS711HSyShuX5Z7CS9izVcwCl3jqtb723qZpmFp8ufYsaP3jSAPnFkdcoT7o7=s2048

<h2>Anatomy</h2>

2 elements of a toolbar orbiter: container and placed components. 

<ol class="decimal"><li id="isPasted">Container</li><li>Placed components</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5stimq-02-1P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/wPnd0meDx_6WgA0RcmAh3jBLHG0iuYG-GonjBTpRZXx8jbGK2mhttARyxdipcS3kS2iSHJFhSFb3eXw_k8DPr__ywvHli4PENaLIVfmYLaYjrA=s2048

<h2>Color &amp; elevation</h2><p>XR uses color to communicate the elevation of UI elements and orbiters. With <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation" target="_blank">spatial elevation</a>, the toolbar displays above the <app-froala-tooltip-element description="In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content. " link-label="More on spatial panels" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels" should-open-link-in-new-tab="true">spatial panel</app-froala-tooltip-element> on the Z-axis. Elevated toolbars can use any of these color options:</p>

4 versions of toolbar elevation color strategy.

<ol class="decimal"><li id="isPasted">Surface container</li><li>Surface container high</li><li>Surface container highest</li><li>Tertiary container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5sum97-03-1P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/w6VacobEqegZ2sNrmTh9bvGoH7GlIqFV0rkepmfEObuvNceGyegLbNeOQKw6DnY0PBwm-knNvVozQEhanqE7R96pjD97g5OM6PKUq5sK8w0=s2048

<h2>Measurements</h2>

Diagram with measurements for toolbar orbiters.

<p>Measurements for toolbar orbiters</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5svaqo-04-1P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/QKzN5tAxYlmJ3FQZI3BGI6GDG249mlMDhzYL0PQBj2ABlwwZ25a465b1e7KuZujPAXcSFIpWEZA0_wvh45s7ZHRq-uBsZiyEC74zuaStolX8=s2048

Diagram with 12dp padding for toolbar orbiters.

<p>Padding for toolbar orbiters</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmp5sw649-05-1P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/mrquic0M5r5AkyYCEdVNfNfr6sTJwfTLOOO6y0-G4bIIMOKCoqXOt15g5aJHGa8OCeh6ubTElhCaN1nnKsy_ldeb3L13b6YTK7QHQIKSLXMh=s2048

<h2>Usage</h2><p>A toolbar can appear in an <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels. " link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiter</app-froala-tooltip-element> for a more immersive experience. Currently, this spatial capability is only available in <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components." link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element>. In <app-froala-tooltip-element description="Home space is compatible with mobile and large screen apps, but doesn’t support spatial components." link-label="More on home space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">home space</app-froala-tooltip-element>, use a regular toolbar on the same plane as the body content to mimic a 2D experience.</p>

Animation showing a toolbar changing from 2D to 3D.

<p>A toolbar’s behavior and placement changes from a 2D to a 3D experience</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxe8vd0-toolbars-xr-06%20(1).mp4?alt=media

<h2>Behavior</h2>

<h3>Local context (recommended)</h3><p id="isPasted">When placed in local context, the toolbar orbiter is centered at the bottom of the spatial panel it controls. </p><p>It repositions in response to layout or content changes.</p>

A toolbar orbiter placed in local context.

<p>In most cases, toolbars should be placed in local context. The orbiter is centered and anchored to the bottom of the panel it controls.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp0wl8ix-toolbars-xr-07.mp4?alt=media

<h3>Global context</h3><p id="isPasted">When placed in global context, the toolbar orbiter is centered at the bottom of the app. </p><p>It stays anchored to the app during layout or content changes. </p><p><br /></p>

A toolbar orbiter placed in global context.

<p>In global context, toolbar orbiters are centered and anchored to the bottom of the app. This use case is less common, as toolbars usually contain actions that control a specific panel.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp0woole-toolbars-xr-08.mp4?alt=media

<h3>Expand &amp; collapse</h3><p id="isPasted">Toolbar orbiters with more than five items can expand and collapse to reveal or hide additional content.</p><p>When a toolbar orbiter expands, it stays within the bounds of the adjacent spatial panel.</p><p>Alternatively, more complex toolbars can be split into multiple toolbars.</p>

A spatial panel with a Google document has a toolbar orbiter that expands from 5 to 10 items.

<p>Toolbar orbiters can expand to reveal additional content, but should stay within the bounds of the adjacent spatial panel</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp0wrkvj-toolbars-xr-09.mp4?alt=media

<h3>Additional toolbars</h3><p>In some cases, full space apps can have more than one toolbar orbiter, placed in either global or local context. </p>

An app switches between 1 and 2 toolbar orbiters.

<p>Limit the use of multiple toolbars to rare cases when additional spatialization improves usability</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp0wtnt4-toolbars-xr-10.mp4?alt=media

<h2>Placement</h2>

<h3>Offset &amp; inset positioning</h3><p>In full space, a toolbar orbiter can be positioned adjacent to or overlap a spatial panel. </p>

Toolbar orbiter with offset positioning.

<p id="isPasted">The recommended toolbar orbiter position from the spatial panel is: </p><ul><li>Offset by 20dp or </li><li>Inset by 12dp</li></ul><p><br /></p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxer5rt-11-do.png?alt=media

Toolbar orbiter with inset positioning above 12dp that obstructs content on the spatial panel. 

<p>To prevent content obstruction, don’t overlap the toolbar orbiter and spatial panel above 12dp</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxetpx5-12-don't.png?alt=media

<h3>Horizontal alignment</h3>

A horizontal toolbar orbiter placed within the bounds of its spatial panel.

<p>Always align the toolbar orbiter within the horizontal bounds of nearby spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxewjln-13-do.png?alt=media

A horizontal toolbar orbiter that extends beyond the width of its spatial panel.

<p id="isPasted">The toolbar orbiter shouldn’t exceed the width of adjacent spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxeyben-14-don't.png?alt=media

<h3>Vertical alignment</h3>

A vertical toolbar orbiter placed within the bounds of its spatial panel.

<p>Always align the toolbar orbiter within the vertical bounds of nearby spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxf0mbw-15-do.png?alt=media

A vertical toolbar orbiter that extends beyond the height of its spatial panel.

<p id="isPasted">The toolbar orbiter shouldn’t exceed the height of adjacent spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmemfyo8f-16-don't.png?alt=media

<h3>Spatial panel alignment</h3><p>By default, toolbar orbiters are center-aligned to the spatial panel. Their placement can be adjusted to accommodate specific user needs, such as improved ergonomics or <a href="/m3/pages/bidirectionality-rtl" target="_blank">right-to-left (RTL) languages</a>.</p>

Toolbar orbiter alignment options in relation to spatial panels.

<p>Depending on the configuration (horizontal or vertical) of the toolbar orbiter, it can align to the center, left, right, top, or bottom of a spatial panel</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmemfvpq3-17.png?alt=media

<p>Avoid placing a vertical toolbar orbiter between spatial panels. <br /><br />This negatively affects the interface structure and can make it difficult to find.</p>

A vertical toolbar orbiter is placed between 2 spatial panels.

<p>Don't place a vertical toolbar orbiter between spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmemfx943-18-don't.png?alt=media

<h2>Accessibility considerations</h2><p><a href="/m3/pages/xr-design/accessibility" target="_blank">XR accessibility</a> guidelines are still evolving. XR toolbars should follow applicable Material <a href="/m3/pages/toolbars/accessibility" target="_blank">toolbar accessibility standards</a>.</p>
