# Grids &amp; spacing

Source: https://m3.material.io/foundations/layout/grids-spacing
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/b375cd8c-5506-4ce1-8caa-9cc23eb2d996.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Grids and spacing organize content and actions for any layout

## Overview

<ul><li><p>Grids create a consistent foundation and adapt across <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints/overview" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element> (previously window size classes)</p></li><li><p>Use spacing to group related information and direct people’s attention to key actions</p></li><li><p>Density helps people see and compare more information in data-heavy views</p></li></ul>

Mobile and desktop UIs with grid lines.

<p>Layouts in Material are based on a grid that adapts across all screen sizes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4if1f9-01.png?alt=media

<h2>Availability &amp; resources</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Type</p></th><th><p>Resource</p></th><th><p>Status</p></th></tr></thead><tbody><tr><td rowspan="2" style="vertical-align:top"><p>Design</p></td><td><p><a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">M3 Design Kit (Figma)</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="/m3/pages/spacing/overview" target="_blank">Spacing system &amp; tokens</a></p></td><td><p>Available</p></td></tr><tr><td><p>Implementation</p></td><td><p><a href="https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/Ruler" target="_blank">Jetpack Compose: Rulers</a></p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>What’s new</h2>

<h5><strong>May 2026</strong></h5><ul><li><p>How to use grids and rulers to adapt layouts across devices</p></li><li><p>Expressive spacing guidelines</p></li></ul>

Tablet with content divided into 8 columns. Each pane of content is 4 columns wide.

<p>As screen size increases, additional columns allow for a richer layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4int8e-02.png?alt=media

## Grids

<ul><li><p>Layouts in Material are based on a grid that adapts across all <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element> (previously window size classes)</p></li><li><p>Parts of the layout <app-froala-tooltip-element description="A scaffold is a fundamental UI design structure that provides a standard platform for assembling key screen components." link-label="More on scaffold" link-url="/m3/pages/scaffold" should-open-link-in-new-tab="true">scaffold</app-froala-tooltip-element> like rails and panes are positioned on this grid to create consistent adaptive layouts</p></li><li><p>The structure and spacing values used in a grid can add personality to a product’s layout</p></li></ul>

<h2>How to use grids</h2>

<h3>Start with placing grid columns</h3><p>Grids adapt across <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element>. As the size increases, column count, width, and spacing change as well.</p>

A mockup of grid columns, showing compact, medium/expanded, and large/extra-large breakpoints.

<p>The number and size of columns changes based on breakpoints</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp54500h-03.png?alt=media

<p>When moving between sizes, column count may increase to show more content or controls.</p>

A course listing on a compact screen, with 4 columns.

<p>On compact screens, fewer columns are used to create a focused layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp54dby8-04.png?alt=media

A course listing on a foldable screen, with 8 columns.

<p>As screen size increases, for example when a foldable screen is unfolded, additional columns allow for a richer layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp54ejyh-05.png?alt=media

<h3>Place bars &amp; rails</h3><p>Populate regions of the layout <app-froala-tooltip-element description="A scaffold is a fundamental UI design structure that provides a standard platform for assembling key screen components." link-label="More on scaffold" link-url="/m3/pages/scaffold" should-open-link-in-new-tab="true">scaffold</app-froala-tooltip-element> that are closest to the edges of the screen’s usable space first. This may include:</p><ul><li><p>Bars like the <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element> and <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">rail</app-froala-tooltip-element></p></li><li><p>Components like <app-froala-tooltip-element description="Toolbars display frequently used actions relevant to the current page." link-label="More on toolbars" link-url="/m3/pages/toolbars/overview" should-open-link-in-new-tab="true">toolbars</app-froala-tooltip-element> and <app-froala-tooltip-element description="App bars contain page navigation and information at the top of a screen." link-label="More on app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">app bars</app-froala-tooltip-element></p></li></ul>

A compact screen with a toolbar highlighted.

<p>The bar region can contain a toolbar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp55v0r6-06.png?alt=media

A large screen with a leading navigation rail highlighted.

<p>The rail region on larger screens usually contains a navigation rail</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp55w2g9-07.png?alt=media

<h3>Place panes</h3><p>Next, populate the main region of the screen with panes with content and components, based on available space and structure.</p><p>See the <a href="/m3/pages/canonical-examples" target="_blank">canonical layout examples</a> for ideas on which panes are appropriate for a product.</p>

Mobile UI with 1 pane. Foldable UI with 2 panes in a supporting pane layout.

<ol class="decimal"><li><p>Primary pane</p></li><li><p>Supporting pane</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp55yqda-08.png?alt=media

<h2>Rulers &amp; alignment</h2>

<p>Rulers are a set of recommended global alignment lines that help create consistent focal points in a product, while keeping content and components consistently aligned.</p><p><a href="https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/Ruler" target="_blank">How to implement rulers in Compose</a></p>

1 compact and 1 desktop UI mapping rulers.

<ol class="decimal"><li><p>Margin</p></li><li><p>Bar or safety region</p></li><li><p>Title</p></li><li><p>Content 1</p></li><li><p>Content 2</p></li><li><p>Content 3</p></li><li><p>Content 4</p></li><li><p>Bar or safety region</p></li><li><p>Rail</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp56n0pg-09.png?alt=media

<h3>Bar &amp; safety rulers</h3><p>Bar and safety rulers reserve space for <a href="https://developer.android.com/training/system-ui" target="_blank">system UI</a> elements like the status bar and gesture navigation.</p><p>They ensure actionable content like <app-froala-tooltip-element description="App bars contain page navigation and information at the top of a screen." link-label="More on app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">app bars</app-froala-tooltip-element> aren’t covered by system UI.</p>

2 mobile UIs showing bar and safety rulers at the top and bottom.

<p>Bar and safety rulers align to the edges of a screen’s usable space, providing a reference for where system UI like the status bar or gesture navigation appear</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp573btr-10.png?alt=media

<h3>Title rulers</h3><p>The title ruler creates consistency for the screen’s title, aligning the text, icons, and other components in an app bar.</p>

1 mobile and 1 desktop UI showing title rulers.

<p>The title ruler aligns with the title in an app bar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp574ab3-11-key02%20-%20TO%20PUBLISH.png?alt=media

<h3>Content rulers</h3><p>Use content rulers to align and anchor key content, such as headlines and <app-froala-tooltip-element description="Carousels show a collection of items that can be scrolled on and off the screen." link-label="More on carousels" link-url="/m3/pages/carousel/overview" should-open-link-in-new-tab="true">carousels</app-froala-tooltip-element>.</p><ul><li><p>First content ruler: Emphasizes major blocks like hero images, headlines, or primary components</p></li><li><p>Secondary rulers: Determine where supplementary text or actions begin</p></li></ul>

1 mobile and 1 desktop UI showing content rulers.

<p>Content rulers offer flexible alignment options to help create a consistent layout across a product</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp575wo3-12-key02%20-%20TO%20PUBLISH.png?alt=media

Carousel and text resizing to align with content rulers, creating a structured layout.

<p>Realigning primary components or content to a content ruler can create strong hierarchy and visual rhythm across a product</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5778zb-GM3%20-Layout%20-%20Grids%20%20-%20Spacing%20-13%20-%20Ruler%20Hero%20-%20IA%20-%20v02.mp4?alt=media

<h3>Ruler options</h3><p>Margin rulers come with some wiggle room to determine how tight or loose a product’s content feels on-screen. The standard ruler can be adjusted to the left or right.</p><p>Choosing a narrower or wider margin can create or remove negative space, or create expressive moments in a content-forward product.</p>

Mobile UI showing a recipe layout where text margins narrow while the hero photo expands.

<p>Margin rulers can adjust to create more or less negative space</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp578joa-GM3%20-Layout%20-%20Grids%20%20-%20Spacing%20-14%20-%20Ruler%20Options%20-%20IA%20-%20v02.mp4?alt=media

<p>Rulers can also be used to create more immersive experiences. For example, a photo grid can take the full width of the screen, while components like <app-froala-tooltip-element description="Search lets people enter a keyword or phrase to get relevant information." link-label="More on search" link-url="/m3/pages/search/overview" should-open-link-in-new-tab="true">search</app-froala-tooltip-element> use wider margins.</p>

Mobile UI for a photo app showing a full-width image grid and a search bar with wide margins.

<p>Rulers allow components and media to use different margin widths</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp579mwo-15.png?alt=media

## Spacing

<ul><li><p>Spacing helps group content, direct attention, and shape the personality of a product</p></li><li><p>A denser layout can feel more serious and focused, while a more spacious layout can feel calm and open</p></li><li><p>Material’s spacing system can adapt to <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element> and density settings. <a href="/m3/pages/spacing/overview" target="_blank">More on the spacing system</a></p></li></ul>

2 screens: 1 mobile with tight spacing, 1 desktop with wider spacing.

<p>Desktop layouts can use more generous spacing than mobile layouts</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp51ef8p-01.png?alt=media

<h2>Spacing to group content</h2>

<p>Grouping connects related elements that share context, such as an image and its caption. Use spacing to visually tie elements together and establish boundaries between unrelated items.</p>

Photo of dumplings with a caption reading “restaurants in the area”.

<p>Placing a caption under an image creates an implicit group</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp51khdt-02.png?alt=media

<p><strong>Explicit grouping</strong> uses visual boundaries like outlines, dividers, and shadows to group related elements in an enclosed area. </p><p>It can also indicate that an item is interactive, such as:</p><ul><li><p>List items between dividers</p></li><li><p>A card displaying an image and its caption</p></li></ul>

A contact grouped in an outlined card with a photo and caption.

<p>Outlines define clear boundaries to explicitly group elements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5334mv-03.png?alt=media

<p><strong>Implicit grouping</strong> uses close proximity and open space (rather than lines and shadows) to group related items. </p><p>For example, the items in a carousel are placed close together, with space around the composition to separate them from other content.</p>

Carousel of food-related photos.

<p>Close spacing implicitly groups carousel images</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5346br-04.png?alt=media

<h2>Spacing to direct attention</h2>

<p>Use rhythm, similarity, and other grouping principles to distinguish and highlight important elements.</p>

<h3>Rhythm</h3><p>Consistent spacing between related elements or groups makes them easier to navigate with the eye.</p>

4 art courses in a row of cards with consistent horizontal spacing and different heights.

<p>Cards should maintain consistent horizontal spacing to establish a strong rhythm when their height varies </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp53c1l8-05.png?alt=media

<h3>Similarity</h3><p>Similar elements should have the same spacing and sizing in a layout to show they’re related.</p><p>Leading elements like thumbnails, avatars, or icons should always be aligned.</p>

3 shopping basket list items with the same thumbnail sizes and text styles.

<p>Thumbnails in a shopping basket should use identical sizes and styles to signal that each one represents a product, even if the original photos have different aspect ratios</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp53g651-06.png?alt=media

<h3>Proximity</h3><p>Place components near each other to create cohesive groups. This helps people understand the relationships between information and actions.</p><p>For example, buttons should be close to the content they’re affecting.</p>

Email message with Reply and Reply all buttons positioned close together.

<p>Placing two buttons as a group near content implies they’ll both affect it in similar ways</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp71sefu-07.png?alt=media

<h3>Continuity</h3><p>Place related elements in a container, row, or column to establish a clear group or relationship.</p>

Clothing product page with a horizontal row of size chips, with 6 selected.

<p>Use a row of chips to signal a single, unified control</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp53i2w6-08.png?alt=media

<h2>Spacing as expression</h2>

<p>Give the most important content, tasks, or actions visual prominence with generous spacing and the brightest surfaces.</p>

<h3>Focal points</h3><p>Consistent placement of key actions and information helps build recognizable focal points across a product.</p>

2 mobile screens showing carousels with identical layouts and title placement.

<p>Carousel images, categories, and titles should appear in a consistent location across pages</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp53roq5-09.png?alt=media

<h3>Negative space</h3><p>Allow negative space to give form and meaning to elements on screen. Framing important actions or content with generous spacing creates emphasis.</p>

A mobile screen shows  generous negative space around carousel images.

<p>Negative space gives shape and emphasis to the course header</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp53ttu6-10.png?alt=media

## Density

<ul><li><p>Information density is the consideration of the amount of information visible on the screen</p></li><li><p>The default target size should be at least 48x48 CSS pixels</p></li><li><p>People can change density as long as the density controls are accessible</p></li><li><p>Apply density thoughtfully; not every layout needs it</p></li><li><p>Layout and component scaling (component adaptation or component density) can allow people to scan, view, or compare more information at once</p></li></ul>

A website design with a denser arrangement of text and graphics.

<p>Information density can change based on context and preference</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5c4fqq-m6fec25z-GM3-Components-Density-2-v03.mp4?alt=media

5 components scaling with multiple size examples.

<p>Consider whether components should scale</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5c5sj5-m6fedlg1-GM3-Components-Density-1-v02.mp4?alt=media

<p><strong>Information density</strong></p><ul><li><p>Information density can be achieved through layout and design decisions without using component scaling</p></li><li><p>Some people may not benefit from increased density</p></li></ul>

<p><strong>Component scaling</strong></p><ul><li><p>Components can adapt and change dimensions to help people scan, view, or compare different amounts of information</p></li><li><p>Don't apply component scaling by default if it would result in a target below 48x48 CSS pixels</p></li></ul>

An email app with “Appearance settings” open to change information density between cozy, comfortable, and compact.

<p>Information density and component scaling can be used together to provide more information and additional user control</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5but2k-m6feg3jn-GM3-Components-Density-3-v02.mp4?alt=media

<h2>Information density</h2>

<p>Information density refers to the amount of content (such as text, images, or videos) in a given space.</p><p>A layout’s spacing dimensions, including margins, spacers, and padding, can change to increase or decrease its information density. High density layouts are useful when people need to scan, view, or compare a lot of information, such as in a data table. Increasing the layout density of lists, tables, and long forms makes more content available on-screen.</p><p>Consider density settings in the context of a device. Although a person may prefer a denser layout for desktop, they may not for mobile. Density shouldn’t automatically change across <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element> or orientation unless a person changes it.</p>

2 layouts: 1 with low density and 1 with high density.

<p>Consider using higher density information design when people need to scan lots of information</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5bjd4j-03.png?alt=media

News website on desktop displaying a high information density. 

<p>Consider the amount and priority of information on-screen. Higher density can be useful for data-rich products where people expect to scan lots of information quickly. Examples: News, financial portals, dashboards</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5bh69d-04.png?alt=media

News website on desktop displaying a low information density.

<p>Lower density can be better for sites prioritizing aesthetics, a focused message, less information, or easier navigation</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5bi6cs-05.png?alt=media

<h2>Component scaling</h2>

<p id="isPasted">The component density scale controls the internal spacing of individual components.</p><p>The density scale is numbered, starting at 0 for a component’s default density. The scale moves to negative numbers (-1, -2, -3) as space decreases, creating higher density.</p><p>Higher density is typically applied by decreasing the top and bottom padding or overall height by 4dp.</p>

3 buttons with densities  of 0, -1, -2.

<p>Apply component density based on the needs and layout of a design</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5b9chq-07.png?alt=media

<p id="isPasted">Center the grouped element within the component container.</p><p>Text size shouldn’t change as the container size scales.</p>

Text field showing 20dp between label and input

<p>The measurement between the label and input is 20dp</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5b68d4-08.png?alt=media

Parent container showing label above input.

<p>The label and input are centered within their parent container</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5b7f5f-09.png?alt=media

Dropdown menu with high density items and selectable space height of 38dp.

<p>Don’t increase density in UIs that involve focused tasks, such as selecting from a menu. It reduces usability by limiting selectable space.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5b2pqp-10-dont.png?alt=media

Single-line snackbar with high density.

<p>Don't increase the density in components that alert a person of changes, such as snackbars or dialogs</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5b47ji-11-dont.png?alt=media

<h3>Avoid applying component scaling by default</h3>

<p>People should be able to <strong>opt in</strong> to dense layouts and components.</p><p>To ensure density settings can be easily reverted, settings interactions must use default target sizes (48x48 CSS pixels).  </p><p>Don't scale layouts below 48x48dp by default.</p>

A density menu with large, medium, and small options to customize the screen layout of a table on desktop.

<p>People can opt in to dense layouts in settings</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7fb8wiw-GM3_Expressive_Density_12a_IA_v03.mp4?alt=media

<h2>Targets</h2>

<p>Dense components can be less accessible because interactive elements are smaller, so use caution when increasing information density.</p>

Selectable target of only 40dp.

<p>Use caution when applying component scaling where selectable targets will be reduced to less than 48x48dp. Only apply density where it provides a better experience.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp58kiob-13-caution.png?alt=media

<p>Use caution when applying density to interaction targets. Accessible targets should retain a minimum of 48x48dp, even if the visual element, such as an icon, is smaller.</p>

Settings button icon is 24x24dp, but has interaction target of 48x48dp.

<p>The target should remain 48x48dp, even if the icon is smaller</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp58gdij-14.png?alt=media

Button with height of 36dp and interaction target of 48dp.

<p>The interaction target of a common button can be larger, as long as it meets the 48x48dp minimum size</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp58i79t-15.png?alt=media

<h2>Pixel density</h2>

<p>Pixel density is the number of pixels per inch. High-density screens have more pixels per inch than low-density ones. Elements with the same pixel dimensions appear larger on low-density screens and smaller on high-density screens.</p><p>To calculate pixel density:</p><p>Pixel density = Screen width (or height) in pixels / Screen width (or height) in inches</p>

Magnified UI element  showing a high number of pixels in the focus area.

<p>High-density elements have more pixels per inch</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp586kzq-16.png?alt=media

Magnified UI element  showing a low number of pixels in the focus area.

<p>Low-density elements have fewer pixels per inch</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp587qzn-17.png?alt=media

<h3>Density-independent pixels</h3><p>Density-independent pixels, written as dp, are flexible units that scale to have uniform dimensions on any screen. They provide a flexible way to accommodate a design across devices. The Material design system uses density-independent pixels to display elements consistently on screens with different densities.</p><p>A dp is equal to one physical pixel on a screen with a density of 160.</p><p>To calculate dp: <br />dp = (width in pixels * 160) / screen density</p>

Screen with grid representing a low number of pixels.

<p>Low-density screen displayed with density independence</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp57upl7-18.png?alt=media

Screen with grid representing a high number of pixels.

<p>High-density screen displayed with density independence</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp57w9fy-19.png?alt=media

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Screen physical width</p></th><th><p>Screen density</p></th><th><p>Screen width in pixels</p></th><th><p>Screen width in dps</p></th></tr></thead><tbody><tr><td><p>1.5 in</p></td><td><p>120</p></td><td><p>180 px</p></td><td rowspan="3" style="width:25%"><p>240dp</p></td></tr><tr><td><p>1.5 in</p></td><td><p>160</p></td><td><p>240 px</p></td></tr><tr><td><p>1.5 in</p></td><td><p>240</p></td><td><p>360 px</p></td></tr></tbody></table></div>
