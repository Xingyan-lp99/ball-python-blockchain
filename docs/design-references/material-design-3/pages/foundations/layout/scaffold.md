# Scaffold

Source: https://m3.material.io/foundations/layout/scaffold
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/7490d3ef-a222-47be-870a-3050bfcc5c59.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

A fundamental UI design structure that provides a standard platform for assembling key components

## Overview

<ul><li><p>The layout scaffold structures every piece of an adaptive layout into bars, rails, and <app-froala-tooltip-element description="Panes are layout containers that house other components and elements within a single app. A pane can be: fixed, flexible, floating, or semi permanent." link-label="More on panes" link-url="/m3/pages/scaffold/panes" should-open-link-in-new-tab="true">panes</app-froala-tooltip-element></p></li><li><p>Bars can frame the page to help people navigate through a product</p></li><li><p>Rails create the perimeter space surrounding panes, creating space for elements like navigation and toolbars</p></li><li><p>Panes hold a product’s primary content, adapting to <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element> (previously window size classes) and other conditions</p></li></ul>

<h2>Availability &amp; resources</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Type</p></th><th><p>Resource</p></th><th><p>Status</p></th></tr></thead><tbody><tr><td><p>Design</p></td><td><p><a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">M3 Design Kit (Figma)</a></p></td><td><p>Available</p></td></tr><tr><td></td><td><p><a href="/m3/pages/spacing" target="_self">Spacing system &amp; tokens</a></p></td><td><p>Available</p></td></tr><tr><td><p>Implementation</p></td><td><p><a href="https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/Ruler" target="_blank">Jetpack Compose: Rulers</a></p></td><td><p>Available</p></td></tr></tbody></table></div>

2 diagrams of mobile and desktop layouts, identifying the parts of a scaffold.

<ol class="decimal"><li><p>Safety region</p></li><li><p>Bar</p></li><li><p>Pane</p></li><li><p>Rail</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3n7x8n-01.png?alt=media

## Bars

<h2>Bars</h2>

<p>Bars frame the screen to help people navigate through a product. They typically contain an <app-froala-tooltip-element description="App bars contain page navigation and information at the top of a screen." link-label="More on app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">app bar</app-froala-tooltip-element> or bottom <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element>.</p><p>Bars can span a single pane or across the full width of a window.</p>

Navigation bar on mobile and app bar on desktop.

<ol class="decimal"><li><p>A navigation bar occupies the bottom bar region on mobile</p></li><li><p>An app bar occupies the top bar region on the web</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3nck82-01.png?alt=media

<p>App bars are placed at the top of the screen to help people navigate, providing a title and 1–2 essential actions like search or back.</p>

A photo app with an app bar below the safety region and above a grid of photos.

<ol class="decimal"><li><p>The app bar sits at the top of the screen, outside of the safety region</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3nejq3-02.png?alt=media

<p>Navigation bars let people switch between 3–5 primary UI views at <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact</app-froala-tooltip-element> or <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> breakpoints.</p>

A photo app with a navigation bar below a grid of photos.

<ol class="decimal"><li><p>The navigation bar sits at the bottom of the screen, above the safety region</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3ng1v5-03.png?alt=media

<h3>Safety region</h3><p>Bars are placed adjacent to the safety regions, which contain <a href="https://developer.android.com/develop/ui/compose/system/system-bars" target="_blank">system UI</a> elements.</p><p>The safety region shouldn’t contain primary content.</p>

A photo app with a safety region above an app bar and grid of photos.

<ol class="decimal"><li><p>The safety region—at the top and bottom edges of the screen on compact devices—protect system UI elements</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3nk11i-04.png?alt=media

## Rails

<h2>Rails</h2><p>Rails are the next level in layout after bars, filling the perimeter space surrounding panes or floating above them.</p>

Rail regions highlighted, a bottom toolbar on mobile, and a leading and trailing rail on desktop.

<p>Rails occupy the spaces immediately adjacent to bars:</p><ol class="decimal"><li><p>A toolbar sits above the navigation bar</p></li><li><p>A navigation rail and companion rail occupy the leading and trailing sides of a large window</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3nmktk-01.png?alt=media

<p>On compact screens, the top and bottom rail regions can be used for components like:</p><ul><li><p><app-froala-tooltip-element description="Toolbars display frequently used actions relevant to the current page." link-label="More on toolbars" link-url="/m3/pages/toolbars/overview" should-open-link-in-new-tab="true">Toolbars</app-froala-tooltip-element></p></li><li><p>Chat inputs</p></li><li><p><app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/m3/pages/fab/overview" should-open-link-in-new-tab="true">FABs</app-froala-tooltip-element></p></li><li><p>Other primary controls related to an individual screen</p></li></ul>

A mobile photo app highlighting a toolbar above a navigation bar.

<ol class="decimal"><li><p>On mobile, a toolbar can float in the rail region</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3nowjr-02.png?alt=media

<p>On larger screens, there are rails on the sides of the screen (as well as top and bottom). The leading side rail region commonly holds the <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element>.</p>

A photo app on desktop, highlighting an expanded navigation rail.

<p>At larger breakpoints, the leading rail region can be occupied by an expanded navigation rail</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3thuiz-03.png?alt=media

<p>The rail region on the trailing side of a large screen can hold supporting controls or actions that modify or relate to the content in a pane.</p>

A photo app on desktop, highlighting a trailing vertical toolbar.

<p>The rail region can also be occupied by a vertical toolbar or other controls</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3nu4r2-04.png?alt=media

<p>In <a href="/m3/pages/xr-design/overview/" target="_blank">XR</a>, rail components can become <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" target="_blank">orbiters</a>, which float outside the visible content area. </p>

A photo app in immersive XR, with a navigation rail floating outside the pane.

<p>In full space, an XR navigation rail can float outside the main content as an orbiter</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3nvyg3-05.png?alt=media

## Panes

<h2>Panes</h2><p>All layouts are made up of 1–3 panes. The type of layout and amount of panes you choose should depend on the <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoint</app-froala-tooltip-element> (previously window size classes) and the type of product being built.</p>

A two-pane layout on desktop.

<p>Layouts often include multiple panes that work together</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3nyytv-13-key01.png?alt=media

<p>All layouts are made up of 1–3 visible panes. The type of layout and amount of panes you choose should depend on the <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoint</app-froala-tooltip-element> and the type of product you're building.</p>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Breakpoint</p></th><th><p>Recommended pane total</p></th><th><p>Other pane totals</p></th></tr></thead><tbody><tr><td><p>Compact</p></td><td><p>1</p></td><td><p>--</p></td></tr><tr><td><p>Medium</p></td><td><p>1</p></td><td><p>2</p></td></tr><tr><td><p>Expanded</p></td><td><p>2</p></td><td><p>1</p></td></tr><tr><td><p>Large</p></td><td><p>2</p></td><td><p>1</p></td></tr><tr><td><p>Extra-large</p></td><td><p>2</p></td><td><p>1, 3</p></td></tr></tbody></table></div>

<p>Panes can be:</p><ul><li><p>Fixed: Width doesn’t change based on available space</p></li><li><p>Flexible: Width changes based on available space, and can grow and shrink</p></li></ul><p>All layouts need at least one flexible pane.</p>

A device with 2 panes: 1 fixed and 1 flexible. 

<ol class="decimal"><li><p>Fixed pane</p></li><li><p>Flexible pane</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3o5axo-01.png?alt=media

<p>Panes can be permanent or temporary. Temporary panes can appear and be dismissed when necessary, affecting the layout and size of other panes.</p>

2 permanent panes.

<p>Panes can be displayed permanently side by side</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3o6q96-02.png?alt=media

Right pane with a close button being dismissed. The left pane fills the available space.

<p>Temporary panes can be dismissed</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3o8609-GM3_Applying%20Layouts_Co-planar%20semi-permanent%2006_IA_v01.mp4?alt=media

<h3>Single-pane layouts</h3><p>Single-pane layouts use one flexible pane that extends to fit the available space in a layout’s width. They can be used at any <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoint</app-froala-tooltip-element>, but are recommended for <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element>.</p>

A mobile screen with 1 flexible pane.

<p>A single flexible pane adapts to fit any breakpoint</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3oanue-04.png?alt=media

<h3>Two-pane layouts</h3><p><strong>Split-pane layout</strong></p><p>A split-pane layout keeps the spacer visually centered. It’s best for foldable devices and dynamic layouts.</p><p>When a <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element> or <app-froala-tooltip-element description="Navigation drawers let people switch between UI views on larger devices. In the expressive update, use an expanded navigation rail." link-label="More on navigation drawers" link-url="/m3/pages/navigation-drawer/overview" should-open-link-in-new-tab="true">drawer</app-froala-tooltip-element> is present, it only reduces the size of one pane. The other pane remains at 50% of the window width.</p>

2 flexible panes in a split-pane layout.

<p>The navigation and first pane should be 50% of the window width to keep the spacer centered</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3ocqkb-05.png?alt=media

<p>With a <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element>, or no navigation, both panes span 50% of the window width by default.</p>

2 flexible panes at 50% width, with a navigation bar below them spanning the whole window.

<p>With no navigation rail visible, split-pane layouts set each pane to 50% width by default</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3oeb3e-06.png?alt=media

<p><strong>Fixed-and-flexible layout</strong></p><p>This layout is common for <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded</app-froala-tooltip-element>, <app-froala-tooltip-element description="Window widths 1200dp to 1599dp, such as desktop." link-label="More on large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">large</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Window widths 1600dp and larger, such as ultra-wide monitors." link-label="More on extra-large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">extra-large</app-froala-tooltip-element> breakpoints. The fixed-and-flexible panes can appear in whichever order is best for the content.</p><p>The fixed pane is often temporary, and used for side sheets or lists with light information density.</p>

Fixed and flexible panes arranged 2 different ways.

<ol class="decimal"><li><p>Fixed pane</p></li><li><p>Flexible pane</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3ogbeu-07.png?alt=media

<h3>Three-pane layouts</h3><p>While less common, the extra-large breakpoint supports using a standard <app-froala-tooltip-element description="Side sheets show secondary content anchored to the side of the screen." link-label="More on side sheets" link-url="/m3/pages/side-sheets/overview" should-open-link-in-new-tab="true">side sheet</app-froala-tooltip-element> as a third pane. When the side sheet is present, the expanded navigation rail can remain visible, change into a collapsed navigation rail, or hide completely. Don't use more than three panes. </p><p>Note: Fixed panes at this breakpoint are recommended to be 412dp, but side sheets have a default maximum width of 400dp. </p>

Extra large breakpoint with 2 panes and a side sheet acting as a third pane.

<ol class="decimal"><li><p>A standard side sheet can be used as a third pane</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3ojkaq-08.png?alt=media

<h2>Pane expansion &amp; resizing</h2>

<p>Panes can be resized, expanded, and collapsed using <app-froala-tooltip-element description="A drag handle adjusts the layout when there are 2 or more panes." link-label="More on drag handles" link-url="/m3/pages/layout-overview/parts-of-layout#314a4c32-be52-414c-8da7-31f059f1776d" should-open-link-in-new-tab="true">drag handles</app-froala-tooltip-element>. </p><ul><li><p>In a split-pane layout, both flexible panes can be freely adjusted, or can snap to certain widths.</p></li><li><p>In a fixed-and-flexible layout, the drag handle can fully collapse and expand the fixed pane. This makes it easy to switch between a single-pane and two-pane layout.</p></li></ul><p>The drag handle should also toggle between layout sizes when selected. This can be a tap, double tap, or long press.</p>

A drag handle is used to collapse a two-pane layout into a single-pane layout.

<p>Drag handles can adjust pane size in a list-detail layout</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3omlsl-GM3_Applaying%20Layout_Understanding_Part_09_IA_v01.mp4?alt=media

<p>At expanded, large, and extra-large breakpoints, two-pane layouts can be customized to snap to set widths when resized.</p><p>The recommended custom widths are:</p><ul><li><p>360dp</p></li><li><p>412dp</p></li><li><p>Split-pane with spacer centered visually</p></li></ul>

A drag handle adjusts the panes to recommended custom widths.

<p>Panes can snap to custom widths when releasing the drag handle</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3ooyrc-GM3_Applaying%20Layout_Understanding_Part_10_IA_v01.mp4?alt=media

<h3>Persistent pane resizing</h3><p>The persistent resizing behavior remembers a person's pane width preference. Use this for most resizable layouts.</p>

Resizing the panes and then resetting the app preserves the set width.

<p>Pane widths persist even after a person closes the app</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3org16-GM3_Applaying%20Layout_Understanding_Part_11_IA_v01.mp4?alt=media

<p>The width persists even after a <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoint</app-froala-tooltip-element> change. This means that if a two-pane layout is collapsed to one pane at any size, it’ll remain collapsed even when changing breakpoints.</p>

Resizing the panes and then rotating a tablet back and forth preserves the set width.

<p>When a two-pane layout is resized to a single full-width pane, that pane should remain at full-width after switching breakpoints</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3otau7-GM3_Applaying%20Layout_Understanding_Part_12_IA_v02.mp4?alt=media

<h3>Temporary pane resizing</h3><p>The temporary resizing behavior doesn't remember a person’s preferences for pane width. This is primarily used in supporting pane layouts where resizing is uncommon.</p>

Resizing the panes and then closing the second pane resets the set width when expanded again.

<p>Supporting pane layouts can have a pane drag handle to temporarily resize the secondary content</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5bgps3-GM3_Applaying%20Layout_Understanding_Part_13_IA_v01.mp4?alt=media

<p>With temporary resizing, panes should always return to the default layout after the pane or product is closed and reopened. This ensures content is a suitable size for most interactions.</p>

Layouts with temporary resizing reset any custom widths to the default.

<p>The pane width can be temporarily adjusted using the drag handle, but will return to the default layout</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5bk7hu-lxx28ijn-GM3-Styles-Foundations-Layout-UnderstandingLayout-Parts-6-v02.mp4?alt=media

<h2>Displaying multiple panes</h2>

<p>Multiple panes can be displayed in three ways: co-planar, floating, or docked. The layout depends on breakpoint, what the pane does, and how people interact with it:</p><ul><li><p>Co-planar: Two side-by-side panes. To stay accessible, persistent utilities like tool panels should be co-planar with primary content.</p></li><li><p>Floating: A small pane displays above larger panes. Temporary tasks should remain floating regardless of breakpoint, such as a dialog.</p></li><li><p>Docked: A small pane pinned to the edge of a window. For example, a <app-froala-tooltip-element description="Bottom sheets show secondary content anchored to the bottom of the screen." link-label="More on bottom sheets" link-url="/m3/pages/bottom-sheets/overview" should-open-link-in-new-tab="true">bottom sheet</app-froala-tooltip-element> can be docked to show additional actions.</p></li></ul>

A foldable open screen with 2 co-planar panes displayed side by side.

<p>Co-planar: Panes are displayed side by side</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3ow4kk-15.png?alt=media

 A foldable open screen with a floating pane displayed above other elements. 

<p>Floating: A pane is displayed above other panes or content, like a dialog</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3oxadg-16.png?alt=media

A foldable open screen with a docked pane to the bottom of the screen displayed above other elements. 

<p>Docked: A pane is displayed above other panes and one of its edges extends beyond one side of the screen, like a bottom sheet</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3oxtwa-17.png?alt=media

<h2>How panes adapt</h2>

<p>Pane layouts can adapt using three strategies: <strong>show and hide, levitate,</strong> or <strong>reflow</strong>. When a window is resized or changes orientation, these strategies allow panes to reorganize themselves to preserve context and meaning.</p>

<h3>Show and hide</h3><p>As the <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoint</app-froala-tooltip-element> size or orientation changes, panes can enter and exit the screen or appear next to one another.</p>

1 pane animates off-screen when the device is vertical, then reappears when horizontal.

<p>A pane can be shown or hidden depending on the available space and orientation</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3p0wwo-GM3_Applying%20Layouts_Understanding_Parts_Reflow_17_IA_V01.mp4?alt=media

<h3>Levitate</h3><p>Panes can be elevated above other content as <strong>floating</strong> or <strong>docked</strong> panes. This strategy helps panes appear relative to their triggers.</p><p>Floating panes:</p><ul><li><p>Appear in front of the body content</p></li><li><p>Can be customized to be dragged or resized</p></li></ul><p>When adding controls that resize or move a floating pane, provide accessible controls.</p>

1 pane floats on top of the other when the device changes to a vertical orientation.

<p>A co-planar pane can float when switching breakpoint or orientation</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3p3knn-GM3_Applying%20Layouts_Understanding_Parts_Reflow_18_IA_v01.mp4?alt=media

<p>On large screens:</p><ul><li><p>Floating panes are the default</p></li><li><p>The scrim behind a floating pane is optional</p></li></ul>

2 ways of showing floating panes on large screens, with and without a scrim.

<ol class="decimal"><li><p>Floating pane with a scrim</p></li><li><p>Floating pane without a scrim</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3p9uz9-20.png?alt=media

<p>Docked panes are usually at the bottom of the window, like a <app-froala-tooltip-element description="Bottom sheets show secondary content anchored to the bottom of the screen." link-label="More on bottom sheets" link-url="/m3/pages/bottom-sheets/overview" should-open-link-in-new-tab="true">bottom sheet</app-froala-tooltip-element>.</p><p>At <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints</app-froala-tooltip-element>, docked panes can adapt into floating panes.</p>

A docked pane on mobile turning into a floating pane on desktop.

<p>A docked pane can adapt into a floating pane at medium and expanded breakpoints</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3rcrfk-GM3_Applying%20Layouts_Understanding_Parts_Bottom%20Sheet%20to%20Floating%20Pane_19_IA_v01.mp4?alt=media

<p>Alternatively, at medium and expanded breakpoints, a docked pane can adapt into a co-planar pane. </p>

A docked pane on the lower half of a mobile screen changes to a co-planar pane on a larger screen.

<p>A docked pane can also adapt into a co-planar pane at medium and expanded breakpoints</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3rfkvn-GM3_Applying%20Layouts_Understanding_Parts_Bottom%20Sheet%20to%20Co-planar%20Pane_20_IA_v01.mp4?alt=media

<p>On large screens, consider changing docked panes into co-planar panes.</p>

A docked pane on mobile and a co-planar pane on a tablet.

<ol class="decimal"><li><p>A compact screen can have a docked pane</p></li><li><p>On a large screen, it should change to a co-planar pane </p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3riptw-23.png?alt=media

<h3>Reflow</h3><p>Panes can be reorganized on screen as the breakpoint or orientation changes, also known as reflow. </p><p>For example, in a vertical orientation, the supporting pane can move underneath the primary pane.</p>

A supporting pane changes orientation and location as the screen changes orientation. 

<p>In a vertical orientation, the supporting pane can move below the primary pane</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3skf28-GM3_Applying%20Layouts_Understanding_Parts_Reflow_23_IA_v01.mp4?alt=media

<p>Reflow also applies to breakpoints. When there’s not enough horizontal space for panes, they can stack vertically instead.</p>

A supporting pane on the right side of a large horizontal screen moves to the bottom of a vertical small screen.

<p>Panes can change size, location, and orientation when switching screen sizes</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3smk3l-GM3_Applying%20Layouts_Understanding_Parts_Reflow%20wsc%20Change%2024_%20IA_v01.mp4?alt=media

<h2>Spatial panels</h2><p>On XR devices, pane layouts can be presented in disconnected <app-froala-tooltip-element description="In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content. " link-label="More on spatial panels" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels" should-open-link-in-new-tab="true">spatial panels</app-froala-tooltip-element>. These panels must have clear containment to make them easy to see on any background.</p>

<p>The content in a spatial panel can use <app-froala-tooltip-element description="Implicit grouping uses close proximity and open space to group related items." link-label="More on implicit grouping" link-url="/m3/pages/grids-spacing/spacing#f3b19166-fead-462f-8adb-7153cd72af6b" should-open-link-in-new-tab="true">implicit grouping</app-froala-tooltip-element> when the pane has an explicit container to distinguish it from the environment.</p>

2-pane layout in XR with implicit content grouping and a virtual reality background. 

<p>When a pane uses explicit containment, content can use implicit grouping</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3sp9gc-07-key01.png?alt=media

<h2>Accessibility considerations</h2>

<p><strong>Coplanar panes</strong></p><ul><li><p>The focus order should match the visual arrangement of the panes on screen</p></li></ul><p><strong>Floating panes</strong></p><p>Modal floating pane:</p><ul><li><p>When active, the elements behind it can’t be interacted with</p></li><li><p>Focus moves automatically to the first element in the pane, and when the pane is closed, focus moves back to the element that triggered it, like a dialog</p></li><li><p>If triggered automatically, focus should still move to it, but when it’s closed, focus should go to the next most logical element on screen</p></li><li><p>It disappears when a person interacts with something behind it.</p></li></ul><p>Non-modal floating pane:</p><ul><li><p>When open, other parts of a product can be interacted with</p></li><li><p>Focus should be able to move to and from the pane</p></li><li><p>The pane should be available in a logical reading order of the screen</p></li></ul><p><strong>Docked panes</strong></p><ul><li><p>Have the same focus requirements as modal and non-modal panes</p></li><li><p>The focus order should match the visual arrangement of the panes on screen</p></li></ul>
