# Shape

Source: https://m3.material.io/styles/shape
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/5e04e8f6-7da6-475e-a1b0-3818021c0cea.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

The M3 shape system includes original shapes, a corner radius scale, and built-in shape morphing

## Overview & principles

<ul><li>Use abstract shapes thoughtfully to add emphasis and decorative flair</li><li>Leverage Material shapes for built-in shape morphing</li><li>Rectangular shapes are fully rounded in all corners by default</li><li>Individual corners can be adjusted to create asymmetrical rectangular shapes</li></ul>

Illustration of range of irregular shapes.

<p>Abstract shapes can help people express themselves</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c35amt-1.png?alt=media

<h2>Availability &amp; resources</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:24.3386%"><p>Type</p></th><th style="width:42.328%"><p>Resource</p></th><th style="width:33.3333%"><p>Status</p></th></tr></thead><tbody><tr><td><p>Design</p></td><td><p><a href="http://figma.com/community/file/1035203688168086460/material-3-design-kit" target="_blank">Shape library</a> (Figma Design Kit)<br /></p></td><td><p>Available</p></td></tr><tr><td rowspan="2" style="width:24.3386%"><p>Implementation</p></td><td><p><a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/MaterialShapes" target="_blank">Jetpack Compose</a> (Shape Library)</p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://github.com/material-components/material-components-android/blob/master/docs/theming/Shape.md" target="_blank">Android Views (MDC-Android)</a></p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>M3 Expressive update</h2>

<p id="isPasted"><strong>May 2025</strong></p><p>Added 35 <strong>new shapes</strong> and <strong>shape morphing</strong> to <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank" rel="noopener noreferrer">Material Shape Library</a> (Figma Design Kit) and <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/MaterialShapes" target="_blank" rel="noopener noreferrer">Jetpack Compose</a>.</p><p>Added new shape principles and a refreshed art direction.</p><p>Added corner radii tokens:</p><ul><li>Large increased (20dp)</li><li>Extra large increased (32dp)</li><li>Extra extra large (48dp)</li><li>Updated fully rounded corners to use <strong>full</strong>. Previously, this was defined using 50% of the component size.</li></ul><p><a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank" rel="noopener noreferrer">More on M3 Expressive</a></p>

Animation of available Material shapes.

<p>Overview of Material shapes</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8q813wo-01%20-%20shape-Overview%20%26%20principles%202.mp4?alt=media

<h2>Shape library</h2>

35 shapes in the shape set.

<p>M3 has 35 shapes to easily apply to designs</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c3rf47-3.png?alt=media

<h2>Use shapes and text in harmony</h2><p id="isPasted">Shapes are expressive elements of Material 3 that echo key visual attributes of <a href="/m3/pages/typography/overview/">M3 typography</a>. </p><p>Use shape and type together for products to feel cohesive and polished.</p>

Fonts and mock UI screens showing a wide range of square, round, thin, and thick shapes.

<p>M3 shapes and Google Sans Flex share roundness visual attributes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7pa01q8-4.png?alt=media

While a person taps water and squeezes a soft cube, a button in the middle responds similarly.

<p>Shape morphing should respond to user interaction</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fc1aun-03%20-%20shape-Overview%20%26%20principles-5.mp4?alt=media

<h2>Morph shapes to connect function and feeling</h2><p id="isPasted">Shapes should morph to improve understanding and add moments of delight. Use shape morph to better communicate:</p><ul><li>Interaction states, like when a button is selected</li><li>Actions in progress, like a friend typing, or a page loading</li><li>Changes in the environment, like sound, temperature, or time of day</li></ul><p>Think about how shapes could react to different interactions, such as tapping, swiping, scrolling, releasing, and long pressing.</p>

<h2>Be bold and dare to embrace tension</h2><p id="isPasted">Tension happens when the shape story changes unexpectedly, such as when contrasting shapes are used. This can be created using both square and rounded shapes, unconventional shapes, and other contrasting elements.</p><p>Material historically focused on rounded shapes. However, using sharp shapes, thereby adding tension, creates more dynamic design, one that’s more memorable and expressive.</p><p>This tension can be used in many ways, like conveying states, drawing attention to an element, or to improve the visual aesthetic.</p>

Round and square shape side-by-side.

<p>Create tension by using a combination of round and square shapes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fc4dnp-6.png?alt=media

Use different types of shape in loading indicators to show progress.

<p>Shapes and motion can communicate actions in progress</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7p9sea1-GM3_Expressive_Shape_Overview%20and%20Principles_7_v17.mp4?alt=media

<h2>Shape is versatile, not semantic</h2><p id="isPasted">Avoid making shapes literal or assigning a specific function or meaning to a single shape.</p><p>For example, the <app-froala-tooltip-element description="Loading indicators show the progress of a process with a short wait time." link-label="More on loading indicators" link-url="/m3/pages/loading-indicator/overview" should-open-link-in-new-tab="true" id="isPasted">loading indicator</app-froala-tooltip-element> can be wavy, but the waveform is not a strict symbol of progression. Progress could just as easily be shown using rotating shapes or shape morph. <br /><br />Plus, waveforms could be used in other places unrelated to progress, like button containers.</p>

<h2>Use abstract shapes sparingly</h2><p id="isPasted">Be intentional when using shapes in product UI. Don’t compromise clarity for the sake of visual design.</p><p>When incorporating diverse shapes, think about how they fit into the overall design and consider how they balance with the entire composition. Ensure that shapes resonate with the product's narrative. Consider the 'why' behind their inclusion and the value they contribute to the overall user experience. </p><p><br /></p>

8 shapes with icons.

<p>Shapes without clear meaning behind why they’re different can add more visual clutter than delight</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c73wle-8.png?alt=media

Shapes morphing to indicate different states.

<p>Essential shapes can use shape morph to communicate change</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7pa308e-GM3_Expressive_Shape_Overview%20and%20Principles_9_v17%20(1).mp4?alt=media

Shapes being applied as masks on photos to make them more interesting.

<p>Use abstract shapes on imagery and decorative UI</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7pa3b28-GM3_Expressive_Shape_Overview%20and%20Principles_10_4x_V03.mp4?alt=media

<h2>Emphasize aesthetic moments with shape</h2><p id="isPasted">Get creative when using shape in graphics, for photography cropping, personalized avatar masking, and other non-interactive elements.</p><p>Decorative moments offer the most flexible and creative uses of shape.</p>

<h2>Shape can be 2.5D</h2><p>When effectively used, shape and motion can make 2D visuals feel 3D. They provide the illusion of depth and volume, making visuals more eye-catching and natural.</p>

Shapes spinning and a weather icon transforming into the current temperature.

<p>Apply motion and shape differently on each layer to give it the illusion of depth</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmnxek75a-GM3%20-%20Shape%20-%20Overview%2012%20-%20v12.mp4?alt=media

## Corner radius scale

<p>Material components use a corner radius scale to define all rectangular shapes, such as buttons, carousels, and dialogs.</p>

Illustration of range of shapes.

<p>M3 defines corner radii using a shape scale. This can be used to create both uniform and asymmetrical shapes.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c80f7i-1.png?alt=media

<h2 id="isPasted">Shape tokens</h2><p>Material has shape corner tokens to define all corners, and corner-value tokens for individual corners. <a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9

libraryModuleType: TOKEN_TYPE_UNSPECIFIED

moduleConfigurationOverrides: {'tokenSets': ['Shape'], 'hideSearchField': False, 'hideVersionName': True}

<h3>Corner radius scale</h3>

<p id="isPasted">The Material 3 shape system uses a size-based scale with ten styles. Styles are assigned to components based on the desired amount of roundedness. </p><ol class="decimal"><li>None - 0dp</li><li>Extra small - 4dp</li><li>Small - 8dp</li><li>Medium - 12dp</li><li>Large - 16dp</li><li>Large increased - 20dp</li><li>Extra large - 28dp</li><li>Extra large increased - 32dp</li><li>Extra extra large - 48dp</li><li>Full - fully rounded corners</li></ol><p><a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Apply shape styles using tokens</a></p>

10 corner radii styles.

<p>Steps on the scale are named for the amount of roundedness applied to the corner</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c881mj-1.png?alt=media

Components illustrating the old 3-level shape scale.

<p>M2: Three-level shape scale based on the size of the component container</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fc5xxg-3.png?alt=media

Components illustrating the new 10-level shape scale.

<p>M3: Ten-level shape scale based on the roundedness of shape corners</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fc5nak-4.png?alt=media

<h2>Symmetry</h2>

<p id="isPasted">Components can have either symmetric or asymmetric corner shapes. Symmetric shapes have the same values for all corners, while asymmetric shapes can have corners with different values.</p><p>Both symmetric and asymmetric shapes use the same 10-step scale.</p><p>Asymmetrical shapes are used in M3 components with closely-grouped items, such as menus and split buttons. These are called <strong>inner corners</strong>.</p>

3 shapes illustrating symmetrical and asymmetrical styles.

<p><strong>Inner corner </strong>component tokens always map to individual corner shape tokens</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c8fgh9-2.png?alt=media

<h2 id="isPasted">Customizing shapes</h2>

<p>Generally, products should consistently use the Material 3 shape styles. However, customization is sometimes necessary, and even encouraged, for hero moments or custom components. Shapes can be customized at the <strong>style</strong> or <strong>component</strong> level.</p>

<h3 id="isPasted">Style changes</h3><p>The corner radius shape style, like <strong>medium</strong>, can be customized to be a different size.</p><p>This applies the change to all components mapped to that shape style, unless they have an override.</p>

Shapes with different corner radii.

<p>Customizing the corner size of the <strong>medium</strong> style applies the change to all components using this style, such as cards and small FABs</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fbcwaf-08%20-%20Shape%20-%20Corner%20Radius%20Scale%206.mp4?alt=media

<h3 id="isPasted">Component changes </h3><p>The style of a specific component, such as a button, can be changed by customizing which corner radius shape style it maps to.</p><p>For example, by default, buttons are mapped to the <strong>full</strong> corner radius shape style. If your product needs a less rounded shape, remap the token to another style in the shape scale, such as <strong>small</strong> or <strong>medium</strong>.</p>

Components with different corner radii.

<p>Remapping the shape for a component to a different style applies the change to just that component across the UI</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fbdqeg-09%20-%20Diagram%20Corner%20Rounding.mp4?alt=media

<p>The shape style family can be customized from <strong>rounded</strong> to <strong>cut</strong>. This makes the corner a straight line instead of curved.  </p><p>Add extra padding to avoid cutting off content in information-dense components.   </p><p>For example, a large cut corner on a card will clip content and images in the area more than a rounded corner of the same size.</p>

Card with text and full corners.

<p>Be careful not to apply large or full corners to information-dense components, such as cards</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma463q2b-10%20-%20shape%20-%20Corner%20Radius%20Scale%208.mp4?alt=media

Carousel with images with rounded corners.

<p>Shapes can be intentionally rounder to add more visual variety</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c9cdvx-8.png?alt=media

Carousel with full rounded shapes.

<p>Add unexpected moments by switching between square and fully rounded shapes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c9bsb5-9.png?alt=media

<h3>Adjust for optical roundness</h3><p id="isPasted">When nesting rounded objects, avoid using the same corner radii for both objects. This can make the corners look unbalanced.</p><p>Instead, adjust the corner radii to be proportional to each other; this is called optical roundness. To calculate optical roundness:</p><ul><li>Outer radius - padding = inner radius</li><li>For example: 48dp - 14dp = 34dp</li></ul>

3 parts of corner radii to adjust.

<ol class="decimal"><li id="isPasted">Padding</li><li>Outer radius</li><li>Inner radius</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c9fged-6-1.png?alt=media

Nested carousel with optical roundness.

<p>Use different corner radii values for nested components so they have optical roundness</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c9h8uv-6.png?alt=media

Nested radii with the same roundness as its container.

<p>Avoid using the same corner radius value for nested objects</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c9j8dt-7.png?alt=media

<h3 id="isPasted">Using the shape library</h3><p>The Material 3 shape library can be used to create more interesting containers. Use the shape library for mostly visual elements. Avoid applying unconventional shapes to text-heavy containers. </p><p>Shapes should be used sparingly to provide a stronger emphasis and moments of delight.</p>

Unexpected shapes in carousel.

<p>Leverage the Material shape library for moments of delight</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c9mtiu-Frame%202134280407.png?alt=media

## Shape morph

<p><span style="white-space:pre-wrap" id="isPasted">The Material shape library supports easy transitioning, or morphing, between shapes. </span>Shape morph is leveraged in the <app-froala-tooltip-element description="Standard button groups add interactions between adjacent buttons when they're pressed." link-label="More on button groups" link-url="/m3/pages/button-groups/overview" should-open-link-in-new-tab="true">standard button group</app-froala-tooltip-element> and <app-froala-tooltip-element description="Loading indicators show the progress of a process with a short wait time." link-label="More on loading indicators" link-url="/m3/pages/loading-indicator/overview" should-open-link-in-new-tab="true" id="isPasted">loading indicator</app-froala-tooltip-element> components.</p>

<h2 id="isPasted"><span style="white-space:pre-wrap">Using shape morph</span></h2>

<p><span style="white-space:pre-wrap" id="isPasted">Access to the Material shape library and the shape morph functionality are available through a platform-specific API.<br /></span></p><ul><li id="isPasted"><span style="white-space:pre-wrap" id="isPasted">For Android, use the </span><span style="white-space:pre-wrap" id="isPasted"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/MaterialShapes" target="_blank" rel="noopener noreferrer">Shapes in Compose API</a></span></li><li id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Web is not currently available</span></li></ul><p>Shape morphing uses the <app-froala-tooltip-element description="The motion physics system has two schemes: standard for utilitarian movement, and expressive for more bouncy movement." link-label="More about motion schemes" link-url="/m3/pages/motion-overview/how-it-works" should-open-link-in-new-tab="true">expressive motion scheme</app-froala-tooltip-element> by default. This can be switched to the standard motion scheme as needed.</p>

Shapes available in the shape morph API library.

<p>The Material shape library contains many types of shapes that can all morph seamlessly into each other</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0f9yqna-11-shape_Shape%20morph%201.mp4?alt=media

<p>Material uses shape morphing in the <app-froala-tooltip-element description="Standard button groups add interactions between adjacent buttons when they're pressed." link-label="More on button groups" link-url="/m3/pages/button-groups/overview" should-open-link-in-new-tab="true">standard button group </app-froala-tooltip-element>and <app-froala-tooltip-element description="Loading indicators show the progress of a process with a short wait time." link-label="More on loading indicators" link-url="/m3/pages/loading-indicator/overview" should-open-link-in-new-tab="true">loading indicator</app-froala-tooltip-element> components.</p>

Morphing buttons react to user clicking.

<p>The standard button group uses shape morph to show interaction</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0fa2ql9-12%20-%20Shape%20Morph%202.mp4?alt=media

Loading indicator with shape morph.

<p>The loading indicator uses shape morph to show progress</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0faip5r-13%20-%20Shape%20Morph%203.mp4?alt=media
