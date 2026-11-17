# Motion physics system

Source: https://m3.material.io/styles/motion/overview
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/ccf2c3e9-82b5-4c4a-9570-b0d08d95c0c1.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

The motion physics system makes a UI expressive and easy to use

## How it works

Showcase of expressive components and motion curves.

<p><br /></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm9d3dbjl-00_Hero%20Expressive%20New_Export.mp4?alt=media

<h2>A motion system designed for expression</h2><p id="isPasted"><strong>May 2025</strong></p><p>Material introduced the <strong>motion physics system</strong> with M3 Expressive. This new physics-based system makes interactions and transitions feel more alive, fluid, and natural. It represents a new motion language for Google products, and is easier to implement and customize than ever before. </p><p>The physics system is replacing the previous system based on <a href="/m3/pages/motion-easing-and-duration/applying-easing-and-duration/" target="_blank" rel="noopener noreferrer">easing and duration</a>.</p><p><a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank" rel="noopener noreferrer">More on M3 Expressive</a></p>

<h2>Availability &amp; resources</h2><div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:33.3839%"><p><strong>Type</strong></p></th><th style="width:33.2322%;text-align:center"><p><strong>Link</strong></p></th><th style="width:33.3839%;text-align:center"><p><strong>Status</strong></p></th></tr></thead><tbody><tr><th rowspan="4" style="width:33.3712%"><p>Implementation</p></th><td><p><a href="https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md" target="_blank">Android Views (MDC-Android)</a></p></td><td><p>Available. Not added to components. <a href="https://m3.material.io/styles/motion/overview/specs" target="_blank">See specs</a><br /></p></td></tr><tr><td><p>Flutter</p></td><td><p>Unavailable</p></td></tr><tr><td><p><a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/MotionScheme" target="_blank">Jetpack Compose</a></p></td><td><p>Available</p></td></tr><tr><td><p>Web</p></td><td><p>Compatible with Compose springs. <a href="https://m3.material.io/styles/motion/overview/specs" target="_blank">See specs</a><br /></p></td></tr></tbody></table></div>

<h2>The basics: Motion schemes</h2><p>The physics system has two preset motion schemes: <strong>expressive</strong> and <strong>standard</strong>. The motion scheme you choose defines how your product feels. While most motion in a product should use the same scheme, products can make <a href="/m3/pages/motion-overview/how-it-works#fef83d57-b139-4c40-b538-9f1e9872df1b" target="_blank" rel="noopener noreferrer">advanced customizations</a> to swap the scheme to emphasize key moments.</p>

<p><strong>Expressive</strong> is Material’s opinionated motion scheme, and should be used for most situations, particularly hero moments and key interactions.</p>

A circle moves across the screen with expressive motion. It has a trail showing the level of bounce applied.

<p>The expressive motion scheme overshoots the final values to add bounce</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0g74buu-00_Scheme_Spring%20Expressive%20Export.mp4?alt=media

<p><strong>Standard</strong> feels more functional with minimal bounce, and should be used for utilitarian products.</p>

A circle moves across the screen with standard motion. It has a trail showing the lack of bounce applied.

<p>The standard motion scheme eases into the final values</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0g75t7b-00_Scheme_Spring%20Standard%20Export.mp4?alt=media

<p>Need something other than the preset schemes? <a href="/m3/pages/motion-overview/how-it-works#f4ec8b84-3e39-4699-bba3-0fe7ec5cb79e">Create your own!</a> The physics system makes it easy to create custom motion schemes beyond expressive and standard, while still leveraging theming. Schemes can be easily switched between expressive, standard, or custom as needed.</p>

<h2>How it works: Springs</h2><p>Motion schemes use <strong>springs</strong>. A spring is a combination of three attributes which control all motion behavior: <app-froala-tooltip-element description="Stiffness defines the hardness of the spring. Higher stiffness resolves the motion faster." link-label link-url should-open-link-in-new-tab="false">stiffness</app-froala-tooltip-element>, <app-froala-tooltip-element description="Damping defines how fast the bounce wears out. Higher damping stops the bounce faster. A damping value of 1 completely removes spring bounce." link-label link-url should-open-link-in-new-tab="false">damping</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Initial velocity defines the initial speed of the spring, which influences the total spring duration in combination with stiffness and damping." link-label link-url should-open-link-in-new-tab="false">initial velocity</app-froala-tooltip-element>.</p>

<p id="isPasted"><strong>Springs are versatile</strong>. One spring can apply to many situations, such as transitions, button effects, or gestures. This makes the motion and expression feel consistent throughout the product.</p><p><strong>Springs feel natural</strong>. Springs are designed to be predictable, like how objects move and bounce. They handle gestures, interruptions, and retargeting animations seamlessly.</p>

Buttons, FAB menus, and toolbars moving with expressive motion springs.

<p>All component motion is driven by two tokens: expressive fast spatial and expressive fast effects</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0g79o8z-00_Versatile%20Export.mp4?alt=media

<h2>Spring tokens</h2><p>On Jetpack Compose and Android Views (MDC-Android), these springs are available as <a href="/m3/pages/motion-overview/specs/" target="_blank">spring tokens</a><strong>.</strong> Use tokens to easily apply motion to any element, making all motion feel predictable and consistent across multiple platforms. See <a href="/m3/pages/motion-overview/specs" target="_blank">specs</a> for how to convert springs to other platforms like Web.</p>

<p id="isPasted">There are tokens for <strong>spatial</strong> movement and <strong>effects</strong>, with three durations each: <strong>default</strong>, <strong>fast</strong>, and <strong>slow</strong>.</p><p>For example, to apply fast, spatial, expressive motion, call the "expressive" motion scheme, then use the token: <span class="inline-code">md.sys.motion.spring.fast.spatial</span>.</p><p>Notice that the "expressive" scheme isn't part of the token itself. Rather, it's called at the product level and applied to all tokens. This makes it easier to swap schemes without changing assigned tokens.</p>

A chart of the token structure. A scheme has 3 speeds. Each speed has a spatial token and an effects token.

<p id="isPasted">Each scheme (expressive, standard) has three speeds (fast, default, slow) for two types of movement (spatial, effects)</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8or28vc-5.png?alt=media

<h3>Style</h3><p><strong>Spatial</strong> spring tokens are used for animations that move something on screen, for example the x and y position, rotation, size, rounded corners. This spring overshoots the final value and bounces into place.</p>

A moving shape bounces into place.

<p>Spatial springs apply to movement</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0g7et1l-00_Tokens%20Spatial%20Pos%20Export.mp4?alt=media

A spinning shape bounces into place.

<p>Spatial springs apply to rotation</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0g8hvpt-00_Tokens%20Spatial%20Rotation%20Export.mp4?alt=media

<p id="isPasted"><strong>Effects</strong> spring tokens are used to animate properties such as color and opacity animations, where there shouldn’t be any overshoot. </p>

A shape fades in and eases into view.

<p>Effects springs applied to opacity</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0g8j35o-00_Tokens%20Effects%20Opacity%20Export.mp4?alt=media

A shape changes color and eases into the final result.

<p>Effects springs applied to color</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0g8k2bk-00_Tokens%20Effects%20Color%20Export.mp4?alt=media

<h3>Speed</h3><p>Spatial and effect spring tokens come in three speeds: <strong>default</strong>, <strong>fast</strong>, and <strong>slow</strong>. Most motion should use the default speed, while smaller elements may use fast and larger elements may use slow.</p>

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="width:14.5531%">Speed<br /></th><th style="width:42.5291%">Spatial example<br /></th><th style="width:42.8574%">Effects example<br /></th></tr></thead><tbody><tr><th style="width:14.5531%">Default<br /></th><td>Animations that partially cover the screen, such as <app-froala-tooltip-element description="Bottom sheets show secondary content anchored to the bottom of the screen." link-label="More on bottom sheets" link-url="/m3/pages/bottom-sheets/overview" should-open-link-in-new-tab="true">bottom sheet</app-froala-tooltip-element> and <app-froala-tooltip-element description="Expanded navigation rails show text labels and an extended FAB, and can be default or modal." link-label link-url should-open-link-in-new-tab="false">expanded navigation rail</app-froala-tooltip-element></td><td>Opacity of the content within a <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element></td></tr><tr><th style="width:14.5531%">Fast<br /></th><td>Small components, such as <app-froala-tooltip-element description="Switches toggle the state of an item on or off." link-label="More on switches" link-url="/m3/pages/switch/overview" should-open-link-in-new-tab="true">switches</app-froala-tooltip-element> and <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element></td><td>Color change of the <app-froala-tooltip-element description="Switches toggle the state of an item on or off." link-label="More on switches" link-url="/m3/pages/switch/overview" should-open-link-in-new-tab="true">switch</app-froala-tooltip-element> handle</td></tr><tr><th style="width:14.5531%">Slow<br /></th><td>Full-screen animations</td><td>Full-screen content refresh</td></tr></tbody></table></div>

Effects motion in fast, default, and slow speeds

<p>Spatial motion in fast, default, and slow speeds</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0g8v98f-00_AllSpeeds_Expressive%20Export.mp4?alt=media

Spatial motion in fast, default, and slow speeds

<p>Effects motion in fast, default, and slow speeds</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0g8u69a-00_AllSpeeds_Standard%20Export.mp4?alt=media

<p>Spring tokens work across devices. For example, the spatial fast token will always be faster than default or slow, but the exact values of each token differ depending on if the device is a wearable, phone, or tablet. This ensures the movement feels fast in the context of the device.</p>

<h2>Application</h2>

<h3>Components</h3><p>On Jetpack Compose, 21 Material components use the motion physics system by default. Android Views (MDC-Android) support is coming soon. To add the motion physics system to other components, including custom-built components, use spring tokens. <a href="/m3/pages/motion-overview/specs" target="_blank">View full specs</a></p>

A collection of expressive components in motion.

<p>Material components use the physics motion system to feel more expressive</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0g8ypfu-00_Components%20Export.mp4?alt=media

<h2>Advanced customizations</h2><p>There are a few different levels for applying motion. Choose the level that applies best to your product or specific component.</p>

<h3 id="isPasted">Level 1: Use a default motion scheme</h3><p>The expressive and standard schemes should be sufficient for all motion needs. On Jetpack Compose, components use these schemes by default.</p>

Switch using the expressive motion scheme.

<p>Switch using the expressive motion scheme</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0g90urt-00_Customization%20Switch%20Expressive%20Export.mp4?alt=media

Switch using the standard motion scheme.

<p>Switch using the standard motion scheme</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qp1jmp-00_Customization%20Switch%20Standard%20Export.mp4?alt=media

<h3 id="isPasted">Level 2: Create a custom motion scheme</h3><p>On Jetpack Compose, to change the default motion scheme that all components and transitions use, create a custom MotionScheme object, and return different AnimationSpec for each property of the motion scheme.</p>

FAB menu with an extra stiff custom scheme.

<p>FAB menu with an extra stiff custom scheme</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0g93afq-00_Customization%20Fab%20Instant%20Export.mp4?alt=media

FAB menu with a minimally stiff custom scheme.

<p>FAB menu with very low stiffness custom scheme</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0g946r2-00_Customization%20Fab%20Soft%20Export.mp4?alt=media

<h3 id="isPasted">Level 3: Swap the default motion scheme per element</h3><p>Why use just one scheme when you can use multiple? On Jetpack Compose, to use one scheme for most of the product, such as <strong>expressive</strong>, but on certain elements swap it for another scheme, like <strong>standard</strong>, override the CompositionLocal for that particular composable, screen, or element. </p>

## Specs

<h2>Cross-platform experiences</h2><p>The motion physics system is available on Jetpack Compose and Android Views (MDC-Android), and can be easily adapted to other platforms.</p>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:15.873%"><p>Platform</p></th><th style="width:29.7316%"><p>Status</p></th><th style="width:54.2756%"><p>How to apply</p></th></tr></thead><tbody><tr><th style="width:15.873%"><p>Jetpack Compose</p></th><td><p>Available</p></td><td><p>Use built-in components and spring tokens.</p></td></tr><tr><th><p>Android Views (MDC-Android)</p></th><td><p>Available. Not  added to components.</p></td><td><p>Use built-in spring tokens.</p></td></tr><tr><th style="width:15.873%"><p>Web</p></th><td><p>Compatible</p></td><td><p>Use springs when possible, otherwise use curves that mimic the springs for animations without interruptions or gestures. <a href="/m3/pages/motion-overview/specs#e3e4f10b-6314-47b7-9051-988066081fa0" target="_self">View web conversion table</a><br /></p></td></tr></tbody></table></div>

<h2>Tokens and specs</h2><p>The <strong>spring composite </strong>tokens are used in the motion physics system. These composites combine two <strong>spring</strong> tokens (damping and stiffness) into a single token for ease of use. The <strong>easing</strong>, <strong>duration</strong>, and <strong>path</strong> tokens are used by the legacy system, so can be ignored.</p>

resourceName: designSystems/20543ce18892f7d9

libraryModuleType: TOKEN_TYPE_UNSPECIFIED

moduleConfigurationOverrides: {'tokenSets': ['Motion'], 'contextTags': ['Standard', 'Expressive', 'Compose', 'Web', 'Android']}

<h2>Web: Convert springs to curves</h2>

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="width:24.7764%">Spring<br /></th><th style="width:75.1028%">Curve<br /></th></tr></thead><tbody><tr><td>Expressive fast spatial</td><td>0.42, 1.67, 0.21, 0.90. Duration =  350ms</td></tr><tr><td>Expressive default spatial</td><td>0.38, 1.21, 0.22, 1.00. Duration =  500ms</td></tr><tr><td>Expressive slow spatial</td><td>0.39, 1.29, 0.35, 0.98. Duration =  650ms</td></tr><tr><td>Expressive fast effects</td><td>0.31, 0.94, 0.34, 1.00. Duration =  150ms</td></tr><tr><td>Expressive default effects</td><td>0.34, 0.80, 0.34, 1.00. Duration =  200ms</td></tr><tr><td>Expressive slow effects</td><td>0.34, 0.88, 0.34, 1.00. Duration =  300ms</td></tr><tr><td>Standard fast spatial</td><td>0.27, 1.06, 0.18, 1.00. Duration =  350ms</td></tr><tr><td>Standard default spatial</td><td>0.27, 1.06, 0.18, 1.00. Duration =  500ms</td></tr><tr><td>Standard slow spatial</td><td>0.27, 1.06, 0.18, 1.00. Duration =  750ms</td></tr><tr><td>Standard fast effects</td><td>0.31, 0.94, 0.34, 1.00. Duration =  150ms</td></tr><tr><td>Standard default effects</td><td>0.34, 0.80, 0.34, 1.00. Duration =  200ms</td></tr><tr><td>Standard slow effects</td><td>0.34, 0.88, 0.34, 1.00. Duration =  300ms</td></tr></tbody></table></div>

<h2>Easing and duration</h2><p>The original easing and duration tokens are still available to use as a fallback, and are currently used for animating transitions. <a href="/m3/pages/motion-easing-and-duration/applying-easing-and-duration" target="_blank">View easing and duration system</a></p>
