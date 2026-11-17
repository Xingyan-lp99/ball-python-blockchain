# Design for immersive XR

Source: https://m3.material.io/foundations/xr/design
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/95a7d4f6-3a81-47b3-9e99-083b5daf66be.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Resources and guidance for immersive extended reality (XR) devices

## Overview

<ul><li><p>Use depth and expanded space to create believable environments</p></li><li><p>Map interactions, like gaze and gestures, to real-world expectations</p></li><li><p>Group UI elements on floating <app-froala-tooltip-element description="In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content. " link-label="More on spatial panels" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels" should-open-link-in-new-tab="true">spatial panels</app-froala-tooltip-element></p></li><li><p>Design for comfort to minimize motion sickness and physical strain</p></li><li><p>Provide feedback through spatial audio, haptics, and visual cues</p></li></ul>

3 XR apps float in a physical room. The view switches to 1 immersive app.

<p>In home space, an XR app can run side by side with other apps, with the real world in the background. In full space, the XR app takes center stage with immersive, spatial capabilities.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowi4zcr-Full-Space.mp4?alt=media

<h2>Resources &amp; availability</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p><strong>Type</strong></p></th><th><p><strong>Resource</strong></p></th><th><p><strong>Status</strong></p></th></tr></thead><tbody><tr><td><p>Design</p></td><td><p><a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">M3 Design Kit</a> (Figma)</p></td><td><p>Available</p></td></tr><tr><td></td><td><p><a href="https://developer.android.com/design/ui/xr/guides/get-started" target="_blank">Android XR immersive design guidelines</a></p></td><td><p>Available</p></td></tr><tr><td></td><td><p><a href="https://developer.android.com/design/ui/ai-glasses" target="_blank">Design for AI glasses</a></p></td><td><p>Available</p></td></tr><tr><td><p>Implementation</p></td><td><p><a href="https://developer.android.com/develop/xr/get-started" target="_blank">Build for Android XR</a></p></td><td><p>Available</p></td></tr><tr><td></td><td><p><a href="https://developer.android.com/develop/xr/jetpack-xr-sdk" target="_blank">Jetpack XR SDK</a></p></td><td><p>Available</p></td></tr><tr><td></td><td><p><a href="https://developer.android.com/jetpack/androidx/releases/xr-compose-material3" target="_blank">Material Design for XR API reference</a></p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Principles</h2>

<h3>Use familiar patterns</h3><p>Material components like buttons and menus help people navigate spatial apps with confidence.</p>

A button opens to show a 3D Material menu.

<p>In XR, a Material menu uses elevation to appear in 3D</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmoxbsbzn-Spatialize_Components_10.gif?alt=media

<h3>Prioritize comfort</h3><p>Place content in the center of a person’s field of view, and design for different body positions, such as seated, standing, and reclined.</p>

A person sitting in a chair in an immersive XR environment, with lines marking their field of view.

<p>Positioning content in a person’s field of view keeps the UI visible and minimizes the need for excessive head or body movement</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowiikrm-03.png?alt=media

<h3>Embrace depth</h3><p>Use elevation and 3D models to add volume, create a sense of realism, and spatial understanding.</p>

A person stands in front of an XR app with 3 curved panels and a 3D shark.

<p>3D models can be viewed from all angles and moved with natural interactions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowilveb-04.png?alt=media

<h3>Design for accessibility</h3><p>Design apps to work with system-level assistive technologies like screen readers, voice commands, and text resizing. Provide large target sizes, support multimodal inputs, and ensure text is legible against any background. </p>

1 XR settings icon button with labeled target size and offset. 1 microphone icon button with a visible cursor.

<p>In XR, icon buttons should have a 56dp target size and 4dp offset</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowin62l-05.png?alt=media

<h2>Material XR components</h2>

<p>The following Material components are adapted for XR:</p><ul><li><p><a href="/m3/pages/xr-components/app-bars/" target="_blank">App bars</a></p></li><li><p><a href="/m3/pages/xr-components/dialogs" target="_blank">Dialogs</a></p></li><li><p><a href="/m3/pages/xr-components/nav-bar" target="_blank">Navigation bar</a></p></li><li><p><a href="/m3/pages/xr-components/nav-rail" target="_blank">Navigation rail</a></p></li><li><p><a href="/m3/pages/xr-components/toolbars" target="_blank">Toolbars</a></p></li></ul>

Animation showing a toolbar changing from 2D to 3D.

<p>A toolbar’s behavior and placement changes from a 2D to a 3D experience</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowj1x1f-toolbars-xr-06.mp4?alt=media

<h2>XR terms</h2><ul><li><p><a href="https://developer.android.com/design/ui/xr/guides/3d-content" target="_blank">3D models</a>: Digital objects rendered with depth and volume</p></li><li><p><a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place" target="_blank">Field of view</a>: The area a person can see without turning their head</p></li><li><p><a href="https://developer.android.com/design/ui/xr/guides/foundations#modes" target="_blank">Full space</a>: Android XR’s immersive mode that supports spatial components</p></li><li><p><a href="https://developer.android.com/design/ui/xr/guides/foundations#modes" target="_blank">Home space</a>: Compatible with mobile and large screen apps, but doesn’t support spatial components</p></li><li><p><a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" target="_blank">Orbiters</a>: Floating elements that control the content within spatial panels, full space only</p></li><li><p><a href="https://developer.android.com/design/ui/xr/guides/foundations#give-users" target="_blank">Passthrough</a>: A blended reality where an XR device displays multiple large apps and the user’s physical environment</p></li><li><p><a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation " target="_blank">Spatial elevation</a>: Displays a component above an app on the Z-axis</p></li><li><p><a href="https://developer.android.com/design/ui/xr/guides/environments" target="_blank">Spatial environments</a>: The 360° 3D virtual worlds people see in an immersive app</p></li><li><p><a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels" target="_blank">Spatial panels</a>: A container for UI elements, interactive components, and immersive content, full space only</p></li></ul>

## Interaction

<p>XR interactions should be flexible, comfortable, and intuitive. People expect to interact with digital objects just like they do with physical ones.</p>

XR Google Maps switches from a floating 2D map to a 3D aerial city view, followed by a hand-gesture navigated restaurant tour.

<p>A person should be able to switch between hands, eyes, voice, or controllers depending on their posture and preference</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowkhgek-content-maps.mp4?alt=media

<h2>Natural interactions</h2><p>Natural interactions like gestures allow people to navigate, select, and move content using their hands. Gestures should be:</p><ul><li><p>Easy to learn</p></li><li><p>Follow familiar patterns, such as press, pinch, and swipe on mobile</p></li><li><p>Comfortable to use repeatedly </p></li></ul><p>Support one-handed interactions for essential actions. Don’t require large, repetitive arm movements, as they can cause fatigue.</p><p> <a href="https://developer.android.com/design/ui/xr/guides/foundations#understanding-system" target="_blank">More on Android XR gestures</a></p>

A person uses their hand to hover on and switch between 3 spatial panels.

<p>A person can select items by pinching with the index finger and thumb </p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowkzvav-xr-interaction-02.mp4?alt=media

<h3>System navigation</h3><p>People should be able to open a navigation menu anywhere, anytime.  </p><p>On Android XR, the system-level navigation menu includes:</p><ul><li><p>Go back: Operates the same as the <a href="https://developer.android.com/guide/components/activities/tasks-and-back-stack" target="_blank">back gesture</a> on Android phones</p></li><li><p>Launcher: Goes to the home screen</p></li><li><p>Recents: People can open, close, and switch apps  </p></li></ul>

An animated hand moves its palm up, and pinches the index finger and thumb to open the navigation menu. 

<p>A navigation menu should always be available using a simple gesture, so people don’t get lost</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowwbqda-xr-interaction-03.mp4?alt=media

<h2>Multimodal inputs</h2><p>XR apps should support flexible, multimodal inputs, such as hand and eye tracking, voice, keyboard and mouse, and controllers.  </p><p><a href="https://developer.android.com/design/ui/xr/guides/foundations#design-multimodal" target="_blank">More on Android XR multimodal inputs</a></p>

<h3>Hand &amp; eye tracking</h3><p>Tracking allows people to interact with the virtual world without a controller.</p><p> Hand tracking</p><ul><li><p>Direct: People can touch, grab, or push virtual objects in arm's reach</p></li><li><p>Ray-based: A ray, like a laser pointer, extends from the hand to target distant items, then a pinch selects it</p></li></ul><p>Eye tracking</p><ul><li><p>Enables gaze and dwell interactions</p></li><li><p>Looking at an object triggers a hover state</p></li></ul>

A person uses ray-based hand tracking to move a 3D globe from a table to a credenza. When selected, a highlighted box appears under the globe.

<p>Distant elements can be moved using hand and eye tracking</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowojjby-Spatialize_3D-Content_5%20(2).mp4?alt=media

<h3>Voice, keyboard, mouse, &amp; controller inputs</h3><p>XR apps should also support voice and physical inputs including:</p><ul><li><p>Voice for hands-free text entry on virtual keyboards</p></li><li><p>Voice commands for common actions like <strong>Open Settings</strong> or <strong>Go back</strong></p></li><li><p>Mouse &amp; keyboard inputs for precision and text-heavy workflows</p></li><li><p>Six degrees of freedom (6DoF) controllers for gaming or complex 3D manipulation</p></li></ul>

<h2>Motion</h2>

<p>In XR, motion sickness can happen when visual cues disconnect from the inner ear's sense of balance.</p><p>To keep people comfortable:</p><ul><li><p>Use <a href="https://m3.material.io/m3/pages/motion-easing-and-duration/tokens-specs#601d5552-a6e6-4d74-9886-ff8f24b9ec35" target="_blank">standard easing</a> and <a href="https://m3.material.io/styles/motion/easing-and-duration/tokens-specs#48bf653e-46f9-48f5-87e0-eaf8ea3fe716" target="_blank">long duration</a> motion tokens</p></li><li><p>Maintain a stable horizon line</p></li><li><p>Limit continuous motion. To switch locations, use teleportation or instant jump instead.</p></li><li><p>Use tunnel vision or vignetting to reduce the field of view while in motion</p></li></ul>

A person walking in a spatial environment, with a steady visual horizon.

<p>Limit use of continuous motion. If required, keep the horizon line stable.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowqbjui-xr-accessibility-01.mp4?alt=media

<h2>Feedback</h2><p>Since virtual objects lack physical resistance, use visual, audio, and sensory feedback to confirm interactions.</p>

<h3>Visual cues</h3><p>Use hover icons, focus indicators, ripples, text labels, and elevation changes to show an object’s interaction <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">state</app-froala-tooltip-element>.  </p><p>To indicate an item is targeted, use <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation " target="_blank">spatial elevation</a> or a highlight state.</p>

When a person uses hand tracking to target a 3D model, a focus indicator appears.

<p>Use visual clues to show when a spatial element is hovered, focused, or selected</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowqhvfh-Spatialize_3D-Content_3%20(1).mp4?alt=media

<h3>Spatial audio</h3><p>Sound emitters can be positioned in 3D space and provide audio confirmation of an action. For example, add a <strong>click</strong> sound when a button is pressed.</p>

As sound emits from 1 of 4 spheres, a person looks toward the active sphere.

<p>Spatial audio can help signify where a person should look or that an action was taken</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowqk798-spatial%20audio.mp4?alt=media

<h3>Haptics</h3><p>For controllers, allow people to turn vibration on or off to simulate the feel of touching or grabbing an object.</p>

## Layout

<p>In XR, a layout extends beyond the screen into the physical world. Spatial panels, 3D models, and an immersive environment can be arranged anywhere on an infinite canvas.</p><p>Unlike mobile layouts which are constrained by screen edges, XR layouts must account for:</p><ul><li><p>Depth on the Z-axis</p></li><li><p>Viewing distance</p></li><li><p>A person's field of view</p></li></ul><p><a href="https://developer.android.com/design/ui/xr/guides/spatial-ui" target="_blank">More on Android XR layouts</a></p>

A video of a family plays against an immersive, mountainous background.

<p>An XR headset display can fully occlude the real world. This allows for complete immersion, with the physical environment replaced by a virtual one.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowquax6-XR%20Headsets.mp4?alt=media

<h2>XR layout basics</h2><p>The fundamental building block of an Android XR app is the spatial panel. Panels serve as containers for UI elements and can be spatially elevated alongside <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels. " link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters  " should-open-link-in-new-tab="true">orbiters</app-froala-tooltip-element>, 3D models, and environments.</p>

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">Spatial panels are available in <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components." link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element> only. They aren't currently available in <app-froala-tooltip-element description="Home space is compatible with mobile and large screen apps, but doesn’t support spatial components. " link-label="More on home space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">home space</app-froala-tooltip-element>.</div></div></div><p></p>

<h3>Spatial panels</h3><p>In full space, <app-froala-tooltip-element description="In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content." link-label="More on spatial panels" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels" should-open-link-in-new-tab="true">spatial panels</app-froala-tooltip-element> are flexible canvases that can contain UI elements, media, and spatial video.</p><p>They often serve as the anchor for 3D models and orbiters.</p>

An XR app with 1 large spatial panel, and 3 orbiters with UI elements and photos.

<p>Navigation UI can float in orbiters outside of a spatial panel</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowrcjbe-developer.android.com_hero%20(2).mp4?alt=media

<h4>Size &amp; position</h4><p>Full space supports panel placement in both passthrough and virtual environments.</p><p>By default, spatial panels launch:</p><ul><li><p>Size: 1024x720dp</p></li><li><p>1.75 meters away from a person</p></li><li><p>With 32dp rounded corners</p></li></ul><p>In full space, panels have no minimum size. The maximum panel size is 2560x1800dp.<br /><br />When people switch from full space to home space, spatial panels usually stay in the same predictable position.</p>

A visualization of a spatial panel 1.75 meters from a person.

<p>At a 1.75 meter launch distance, a spatial panel's size is 1024x720dp</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowrftn5-03%20-%20option%20b.png?alt=media

A diagram of a person looking at a spatial panel 5 degrees below eye level.

<p>Place the panel's vertical center 5° below eye level to maximize comfort</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowrhano-04.png?alt=media

An XR panel in the center 41 degrees of a person’s field of view.

<p>Place primary content in the center 41° of a person’s field of view</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowrjlzr-05.png?alt=media

<h4>Adaptive design</h4><p>Spatial panels dynamically scale based on their distance from a person.</p><p>Material 3 components use <a href="/m3/pages/layout-overview/adaptive-design" target="_blank">adaptive design</a> to ensure content automatically scales and reflows to remain legible and comfortable at any distance or angle.</p><p>To avoid system UI conflicts, stay within default movement limits:</p><ul><li><p>Minimum depth: 0.75 meter</p></li><li><p>Maximum depth: 5 meters</p></li></ul>

A person uses a 1 arm gesture to make an XR UI larger. The size dynamically scales in relation to the person.

<p>A person can scale a spatial panel up or down so it's large enough to see clearly, no matter the distance. When they move the panel, Android XR automatically scales its size.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowrrhdk-spatial-ui-scale.mp4?alt=media

<h4>Grouping panels</h4><p>In <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components." link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element>, an app can be broken up into multiple spatial panels, arranged in a flat, curved, or arbitrary layout.</p>

3 spatial panels in a flat, straight line in front of a person.

<p>Flat layout: Panels are arranged in a straight line. Best for comparing information side by side.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowrvz0k-07.png?alt=media

3 spatial panels curved around a person.

<p>Curved layout: Panels curve around the person. Best for immersive media or wide-format dashboards.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowrwm48-08.png?alt=media

3 spatial panels, each in a unique position, angle, and size.

<p>Arbitrary layout: Panels are placed freely in space. Best for multi-tasking.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmows5o73-09.png?alt=media

<h3>Orbiters</h3><p>An <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels. " link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters  " should-open-link-in-new-tab="true">orbiter</app-froala-tooltip-element> is a floating element that accompanies a spatial panel.</p><p>Use orbiters for navigation UI that needs to stay accessible without obscuring the main content.</p><p>Material <a href="/m3/pages/xr-components/overview" target="_blank">XR components</a> automatically adapt into orbiters.</p>

A nav rail appears as an orbiter to the left of an XR email app.

<p>A navigation rail transforms into an orbiter in XR to give the UI more space</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmows9uwa-navrail_proto_2x_01%20(1).mp4?alt=media

<h3>Spatial elevation &amp; depth</h3><p>Use the Z-axis to create volumetric UI. Unlike 2D elevation which uses shadows, volumetric UI uses actual depth.</p><ul><li><p><a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation" target="_blank">Spatial elevation</a> can create hierarchy, bring active elements forward, and push background elements back</p></li><li><p>Layering can separate UI layers physically. For example, a scrim can float several centimeters behind a dialog box.</p></li></ul>

A dialog switches from 2D to 3D, using spatial elevation.

<p>A dialog using spatial elevation in Android XR</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowuw75p-Spatialize_Components_8%20(1).mp4?alt=media

<h2>Behavior</h2>

<h3>Anchoring</h3><p>In <a href="https://developer.android.com/design/ui/xr/guides/foundations#give-users" target="_blank">passthrough</a>, layouts can interact with the physical world: </p><ul><li><p>World-locked: Panels stay in a specific spot in the room, like a music player anchored to a table </p></li><li><p>Head-locked: Avoid locking UI directly to the person's head view, as it can feel jarring. Instead, use a lazy follow behavior where the UI gently drifts to catch up with the person's movement.</p></li></ul>

A person uses a 1 arm gesture to anchor a spatial panel to a physical desk.

<p>In passthrough, a spatial panel can be attached to a specific location in the real world, such as a table</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowv0qt4-spatial-ui-anchor.mp4?alt=media

<h3>Color contrast &amp; dimming</h3><p>When using standard <strong>surface</strong> <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">tokens</app-froala-tooltip-element>, panels automatically handle contrast: </p><ul><li><p>Passthrough: If the physical room is bright, the system dims the background to ensure the UI remains legible </p></li><li><p>Virtual environments: Panels adapt to the lighting of the virtual world</p></li></ul><p><a href="https://developer.android.com/design/ui/xr/guides/visual-design#colors" target="_blank">More on XR colors</a></p>

An XR video of a family at the dinner table. The dimming setting adjusts from an opaque virtual background to passthrough.

<p>Use bright, high-contrast colors to ensure the UI stands out against different backgrounds</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowv8jsw-Dimming%20(1).mp4?alt=media

## Accessibility

<h2>Use cases</h2><p>XR presents unique physical constraints. Designing accessible XR products means accounting for different bodies, postures, and sensory abilities.</p><p>People should be able to do the following with assistive technology:</p><ul><li><p>Navigate and interact with spatial content using their preferred input method</p></li><li><p>Understand the spatial environment and select interactive elements</p></li><li><p>Customize the experience to fit their physical posture and comfort</p></li></ul><p><a href="https://developer.android.com/design/ui/xr/guides/get-started#make-app" target="_blank">More on Android XR accessibility</a></p>

<h2>System-level accessibility</h2><p>Android XR adapts familiar Android assistive technologies for spatial environments.</p><p>To ensure an inclusive experience, design XR apps to work with system-level features like Google's <a href="https://developer.android.com/guide/topics/ui/accessibility/testing" target="_blank">TalkBack</a> screen reader, voice to text, live captions, <a href="https://support.google.com/accessibility/android/answer/7071579" target="_blank">dwell control</a>, magnification, and color inversion and correction.  </p><p><a href="https://developer.android.com/docs/quality-guidelines/android-xr" target="_blank">Android XR app quality guidelines</a></p>

<h2>Text accessibility &amp; color contrast</h2>

<p>Make sure text and UI are legible in different lighting conditions and environments. For example, in passthrough, the background might be a bright window or a dark room. </p><ul><li><p>Use a minimum 14dp body font size</p></li><li><p>Ensure high contrast between text and background</p></li><li><p>Use standard background <app-froala-tooltip-element description="Material has 26 standard color roles organized into six groups: primary, secondary, tertiary, error, surface, and outline." link-label="More on color roles" link-url="/m3/pages/color-roles?s=m3 " should-open-link-in-new-tab="true">color roles</app-froala-tooltip-element> like <strong>surface container</strong>, rather than custom colors, so they dim automatically</p></li><li><p>Support light and dark themes</p></li></ul>

5 container color roles change from light to dark themes.

<p>Use color roles to dim backgrounds automatically</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowvgn9f-GM3%20-%20Color%2001%20-%20v1.mp4?alt=media

<h2>Physical accessibility</h2>

<p>To support different mobility levels, provide flexible input methods and positions:</p><ul><li><p>Actions should be achievable with one hand, voice, or eye control</p></li><li><p>Don’t require two-handed gestures</p></li><li><p>Design for seated, standing, and reclined positions</p></li><li><p>Allow people to recenter and pull UI closer to them</p></li></ul>

A person uses 1 arm to push a spatial panel further out then closer in.

<p>Offer adjustable input methods and viewing positions</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowvrmua-Spatialize_SpacialPanels_2.mp4?alt=media

<h2>Target size </h2>

<p>Use large target sizes to make XR interactions precise and accessible.  <br /><br />Interactive elements should have:</p><ul><li><p>56x56dp or larger target</p></li><li><p>48x48dp or larger visual affordance</p></li><li><p>4dp offset</p></li></ul><p>Don’t overlap targets of different elements.</p><p>Targets and icons should scale with their parent container or label text.</p>

A gear icon with a 56dp target size and 4dp offset.

<p>Use 56dp or larger target sizes for interactive elements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmowvwpjp-04.png?alt=media
