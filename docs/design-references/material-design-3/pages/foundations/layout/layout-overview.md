# Layout overview

Source: https://m3.material.io/foundations/layout/layout-overview
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/a12b2de7-b2c4-4a79-8503-d3b1e8d4d601.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Layout is the visual and strategic arrangement of elements on a screen

## Overview

<ul type="disc" style="list-style-type:disc"><li><p>Use layout to organize all elements in a screen, signal hierarchy, and draw attention to key actions</p></li><li><p>Adapt layouts to compact, medium, expanded, large, and extra-large <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element> (previously window size classes)</p></li><li><p>Build from an established <a href="/m3/pages/canonical-examples" target="_blank">canonical layout example</a></p></li><li><p>Design for <a href="/m3/pages/bidirectionality-rtl" target="_blank">bidirectionality</a> to support both left-to-right (LTR) and right-to-left (RTL) languages</p></li><li><p>Apply consistent arrangement, sizing, and spacing to create a functional layout structure</p></li><li><p>Material layout guidance is implemented on Android and applies to web</p></li></ul>

7 elements of layout.

<ol class="decimal"><li><p>Column</p></li><li><p>Fold</p></li><li><p>Margin</p></li><li><p>Bar</p></li><li><p>Drag handle</p></li><li><p>Pane</p></li><li><p>Rail</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3ukjvm-01.png?alt=media

<h2>Availability &amp; resources</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p><strong>Type</strong></p></th><th><p><strong>Resource</strong></p></th><th><p><strong>Status</strong></p></th></tr></thead><tbody><tr><td rowspan="2" style="vertical-align:top"><p>Design</p></td><td><p><a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">M3 Design Kit</a> (Figma)</p></td><td><p>Available</p></td></tr><tr><td><p><a href="/m3/pages/spacing/overview" target="_blank">Spacing system &amp; tokens</a></p></td><td><p>Available</p></td></tr><tr><td rowspan="4" style="vertical-align:top"><p>Implementation</p></td><td><p><a href="https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts" target="_blank">Jetpack Compose: Canonical layouts</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/Ruler" target="_blank">Jetpack Compose: Rulers</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://github.com/android/user-interface-samples/tree/main/CanonicalLayouts" target="_blank">Android Views (MDC-Android): Canonical layouts</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://developer.android.com/guide/navigation/navigation-3/migration-guide" target="_blank">Jetpack Compose: Navigation3</a></p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>What's new</h2>

<p>When creating new layouts, use the layout <app-froala-tooltip-element description="A scaffold is a fundamental UI design structure that provides a standard platform for assembling key screen components." link-label="More on scaffold" link-url="/m3/pages/scaffold/overview" should-open-link-in-new-tab="true">scaffold</app-froala-tooltip-element>, start from a <app-froala-tooltip-element description="Designs for common screen layouts across breakpoints" link-label="More on canonical examples" link-url="/m3/pages/canonical-examples/overview" should-open-link-in-new-tab="true">canonical layout example</app-froala-tooltip-element>, and ensure layouts scale across <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element>.</p>

<h5><strong>May 2026</strong> </h5><p>Layout structure and design:</p><ul><li><p>Introduced layout scaffold, to create adaptive layouts efficiently</p></li><li><p>New adaptive guidelines for mobile, desktop, and spatial devices</p></li><li><p>Updated canonical layout examples</p></li><li><p><a href="/m3/pages/spacing/overview" target="_blank">Spacing system</a></p></li></ul><p>Naming:</p><ul><li><p>Window size classes renamed to breakpoints</p></li><li><p>Responsive layout renamed to <a href="/m3/pages/layout-overview/adaptive-design" target="_blank">adaptive design</a></p></li></ul>

Compact and expanded layouts for differently sized screens.

<p>The Material layout scaffold enables layouts to adapt across different screen sizes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3uxdvt-02.png?alt=media

<h2>Layout terms</h2>

<ul><li><p><strong>Adaptive design</strong>: Techniques that allow an interface to dynamically respond to contexts like user preferences, device type, state, and breakpoints</p></li><li><p><strong>Bars</strong>: Can frame the page to help people navigate through a product, and typically house the app bar and bottom navigation bar</p></li><li><p><strong>Bidirectionality</strong>: A writing system that displays text and content from right-to-left (RTL) </p></li><li><p><strong>Breakpoints</strong>: Opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)</p></li><li><p><strong>Column</strong>: One or more vertical blocks of content within a pane</p></li><li><p><strong>Drag handle</strong>: The component that resizes panes</p></li><li><p><strong>Fold</strong>: A flexible area of the screen or a hinge that separates two displays on foldable devices</p></li><li><p><strong>Gap</strong>: The space between components or elements within a container</p></li><li><p><strong>Margin</strong>: The space between the edge of the screen and any elements inside of it</p></li><li><p><strong>Multi-window mode</strong>: Enables multiple apps to share the same screen simultaneously</p></li><li><p><strong>Pane</strong>: A layout container that houses other components and elements within a single app. A pane can be fixed, flexible, floating, or semi-permanent.</p></li><li><p><strong>Rails</strong>: The perimeter space surrounding panes that holds key elements such as navigation rails, toolbars, and pane control</p></li><li><p><strong>Right-to-left (RTL) language</strong>: Languages written and read right-to-left, such as Arabic, Hebrew, and Farsi, used by <a href="https://www.w3.org/International/questions/qa-scripts.en.html" target="_blank">over 2 billion people</a></p></li><li><p><strong>Rulers</strong>: An opinionated set of global alignment lines that help organize building blocks in a layout</p></li><li><p><strong>Safety region</strong>: Zones reserved for system UI elements outside the application space, such as status bar or gesture bar</p></li><li><p><strong>Scaffold</strong>: A fundamental UI design structure that provides a standard platform for assembling key screen components</p></li><li><p><strong>Spacer</strong>: The space between two panes on a foldable device</p></li></ul>

## Parts of layout

<h2>Parts of layout</h2>

<h3>Windows</h3><p>A window frames and contains an app or product.</p><p>Many systems support multi-window views, which display multiple apps at once.</p><p><a href="https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode" target="_blank">Multi-window support guide for Android</a></p>

Stacked windows with a single taskbar underneath.

<p>Two windows can be shown at once with a taskbar underneath</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3yuwss-01.png?alt=media

<p>On desktop, windows can be resized and moved around freely. They should adapt to various screen sizes.</p><p><a href="/m3/pages/layout-overview/adaptive-design" target="_blank">More on adaptive design</a></p>

2 overlapping desktop windows.

<p>Windows can be moved around, resized, and adapt to different screen sizes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3z1fl4-02.png?alt=media

<h3>Grids</h3><p>The layout grid is the foundation for every layout. It provides a structural framework for organizing components, content, and actions.</p><p>Use the grid to:</p><ul><li><p>Group related information in columns</p></li><li><p>Apply spacing consistently</p></li><li><p>Create focal points for primary actions</p></li><li><p>Align building blocks like bars, rails, and panes</p></li></ul><p><a href="/m3/pages/grids-spacing/grids" target="_blank">More on grids</a></p>

Side-by-side compact and expanded windows with different grid spacing.

<p>Column count, width, and spacing dynamically adjust to different breakpoints</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3z8y9f-03.png?alt=media

<h2>Layout scaffold</h2>

<h3>Bars</h3><p>Bars help people navigate through a product. Use bars to:</p><ul><li><p>Frame the main content</p></li><li><p>Contain an <app-froala-tooltip-element description="App bars contain page navigation and information at the top of a screen." link-label="More on app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">app bar</app-froala-tooltip-element> or <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element></p></li><li><p>Span one or multiple panes  </p></li></ul><p><a href="/m3/pages/scaffold/bars" target="_blank">More on bars</a></p>

A photo app with an app bar below the safety region.

<p>1. App bars are placed at the top of the screen to help people navigate by providing a description of the screen and 1–2 essential actions, like search or back navigation</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp45sv4u-04.png?alt=media

<h3>Rails</h3><p>Rails are the next level in layout after bars, filling the perimeter space surrounding panes, or floating above them. They contain key elements such as <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rails</app-froala-tooltip-element>, <app-froala-tooltip-element description="Toolbars display frequently used actions relevant to the current page." link-label="More on toolbars" link-url="/m3/pages/toolbars/overview" should-open-link-in-new-tab="true">toolbars</app-froala-tooltip-element>, chat inputs, <app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/m3/pages/fab/overview" should-open-link-in-new-tab="true">FABs</app-froala-tooltip-element>, and other primary controls.</p><p><a href="/m3/pages/scaffold/rails" target="_blank">More on rails</a></p>

Mobile layout with a toolbar, and a desktop layout with a start-aligned navigation rail.

<ol class="decimal"><li><p>On mobile, the rail region can contain a toolbar</p></li><li><p>On desktop, the rail region can contain the navigation rail</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp45u0ar-05.png?alt=media

<h3>Panes</h3><p>Just like panes of glass that make up a window in the real world, panes in Material make up most of the layout in a window.</p><p>All content must be in a pane. A layout can contain 1–3 panes of various widths, which adapt dynamically to the <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints/overview" should-open-link-in-new-tab="true">breakpoint</app-froala-tooltip-element> (formerly window size class) and the person’s language setting. For right-to-left (RTL) languages, navigation components will be on the right.</p><p>People can navigate to or between panes. Presenting multiple panes at once can make a product more efficient and easier to use.</p><p><a href="/m3/pages/scaffold/panes/" target="_blank">More on panes</a></p>

2-pane layout on a tablet.

<ol class="decimal"><li><p>First pane</p></li><li><p>Second pane</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp46vx4x-07.png?alt=media

<h4>Containment</h4><p>On most devices, panes can blend in with the background. This is called implicit grouping, and helps show relationships between panes.</p><p>Explicit grouping uses distinct colors or outlines to visually delineate content.</p><p><a href="/m3/pages/grids-spacing/spacing#e7e6d1ac-031a-4757-afcf-b223f23654ea" target="_blank">More on spacing to group content</a></p>

2 panes in an email app, with the same color as the background.

<p>In multiple-pane layouts, use color to show emphasis and close spacing to group related content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp46z833-08.png?alt=media

<p>In spatial environments, panes use a container color to separate them from the passthrough or virtual environment.</p>

2-pane layout in a spatialized environment, with a virtual reality background.

<p>Use contrast between panes and the background to create a spatial effect in XR</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp472v90-08.png?alt=media

<h3>Drag handles</h3><p>Drag handles can be used to resize panes in a layout. They can:</p><ul><li><p>Adjust the width of flexible panes</p></li><li><p>Fully collapse and expand fixed panes to quickly switch between a single and two-pane layout</p></li></ul>

A drag handle is used to collapse a two-pane layout into a single-pane layout.

<p>Drag handles can adjust pane size in a list-detail layout</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4771l5-GM3_Applaying%20Layout_Understanding_Part_11_IA_v01.mp4?alt=media

<h3>Rulers</h3><p>Rulers are a set of global alignment lines. They help to align elements across all layers of the layout.</p><p><a href="https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/Ruler" target="_blank">How to implement rulers in Compose</a></p>

A 2-pane email in box, with rulers.

<p>Rulers ensure global alignment across a product, keeping margins and placement consistent</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp47dohx-10.png?alt=media

## Adaptive design

<h2>What’s adaptive design?</h2>

<p>Adaptive design is a set of techniques to change an interface to fit different contexts. While responsive design scales a single layout to fit any screen, adaptive design customizes a product to optimize the experience on each device.</p><p>Designing adaptive experiences goes beyond customizable properties like color, typography, and shape. The structure, individual components, and entire layouts can adapt based on:</p><ul><li><p>People: Individual preferences and settings</p></li><li><p>Devices: Watch, phone, foldable, tablet, desktop, or XR device</p></li><li><p>Usage: Screens dynamically change as a person resizes windows, changes orientation, or switches device</p></li></ul>

<h2>Designing adaptive experiences</h2>

<p>Layouts must be versatile, designed to adapt fluidly across three primary experience types: <strong>mobile</strong>, <strong>desktop</strong>, and <strong>spatial</strong>. Start with mobile and make sure your product's layout and components can scale and adapt seamlessly all the way up to spatial environments. </p><p>While each experience has different primary input methods, designs should be built with all inputs in mind—touch, pointer, and physical keyboard—since users may use your product in a desktop environment regardless of their device type.</p>

<h3>Mobile</h3><p>Mobile experiences include phones, foldables, and tablets.</p><p>On mobile, an app can be shown in several window modes:</p><ul><li><p>Full-screen: The app takes up the entire screen, the default for mobile</p></li><li><p>Split-screen: Two or more apps share the screen simultaneously, common on tablets and foldables</p></li><li><p>Bubbles: Floating windows that let people multitask without leaving their current context</p></li></ul>

A mobile app in full screen mode.

<p>Mobile layouts default to a full-screen window</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3w1k0w-01.png?alt=media

<h3>Desktop</h3><p>Desktop experiences use free-form windows that adapt across <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element>.</p><p>People can use split screens, floating windows, and free-form windows for multi-tasking.</p><p>A tablet can convert to a desktop experience when a physical keyboard and mouse are connected. Similarly, Android mobile devices can transition into a desktop-like environment when connected to an external monitor.</p>

2 desktop layouts adapted to large and medium breakpoints.

<p>A desktop layout can adjust from three to two columns to fit a medium breakpoint</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3w5izv-02.png?alt=media

<h3>Spatial</h3><p>Extended reality (XR) experiences use multiple free-form windows within virtually limitless screens. Immersive modes, such as Android XR’s <a href="https://developer.android.com/design/ui/xr/guides/foundations" target="_blank">full space</a>, allow components to be positioned freely in 3D space.</p><p><a href="/m3/pages/xr-design" target="_blank">More on XR design</a></p>

An XR layout inimmersive full space mode.

<p>In an XR full space layout, a navigation rail can become an orbiter, and float to the side of the main pane</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3wl9n4-03.png?alt=media

<h2>Adaptive layouts</h2>

<p>The Material 3 adaptive system uses <app-froala-tooltip-element description="Panes are layout containers that house other components and elements within a single app. A pane can be: fixed, flexible, floating, or semi permanent." link-label="More on panes" link-url="/m3/pages/scaffold/panes/" should-open-link-in-new-tab="true">panes</app-froala-tooltip-element> and <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element> to organize content into adaptive layouts.</p><p>Panes are the building blocks of layout; a pane is a single destination in the product. For example, in a messaging app, the list of messages is one pane, and and a specific conversation thread is another.</p>

Mobile and tablet in portrait layout with 1 pane. Tablet in landscape layout with 2 panes.

<p>Panes are the primary segments of a layout, and can change based on context</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3wz2eh-04.png?alt=media

<p>As the pane or window resizes—or as someone navigates a product—panes may change size, enter and exit the screen, and reorganize themselves to make the experience more usable or easier to navigate. These patterns are called adaptive strategies. Material has three adaptive strategies that create a cohesive experience across breakpoints: <a href="/m3/pages/scaffold/panes#bbe68948-bc05-4f7c-b870-6254439e4fd8" target="_blank">show and hide</a>, <a href="/m3/pages/scaffold/panes#96bf71b8-04b8-4fff-97c7-9bc782fbf401" target="_blank">levitate</a>, and <a href="/m3/pages/scaffold/panes#e0a573e9-8c62-4772-8d81-47955ff83196" target="_blank">reflow</a>.</p>

A foldable open screen with 2 co-planar panes displayed side by side.

<p>Co-planar: Panes are displayed side by side</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3xrm51-Placeholder.png?alt=media

A  foldable open screen with a floating pane displayed above other elements. 

<p>Floating: A pane is displayed above other panes or content, like a dialog</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3xtdfv-Placeholder%20(1).png?alt=media

A  foldable open screen with a docked pane to the bottom of the screen displayed above other elements. 

<p>Docked: A pane is displayed above other panes and one of its edges extends beyond one side of the screen, like a bottom sheet</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3xuwp5-Placeholder%20(Cmd%2BV%20to%20replace).png?alt=media

<p>In Compose, the <a href="https://developer.android.com/guide/navigation/navigation-3" target="_blank">Navigation 3</a> library allows multiple destinations to be shown on screen at the same time, and enables layouts to adapt seamlessly across window sizes and screens.</p>

A video demonstrating how navigation destinations remain consistent across screen sizes using the Navigation 3 library.

<p>Navigation destinations remain consistent regardless of screen sizes with Navigation 3</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsz6rtgu-Layout%20-%20Adaptive%20Design%20-%20IA%20-%20v01.mp4?alt=media

<h3>Adapting components</h3>

<p>Components can adapt in appearance, placement, and behavior based on factors like:</p><ul><li><p>Where components are placed in relation to their containers, content, and pane boundaries</p></li><li><p>How components use space</p></li><li><p>How components enable usage across different device and input types</p></li></ul><p>Most Material components respond using three main strategies: resizing, showing and hiding, and presentation changes.</p>

<h4>Resizing</h4><p>Components should resize in response to their content and their placement in a layout.</p><p>For example, <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element> may scale along with their parent container, or hug their contents and maintain a left or right alignment.</p>

A card with a button that spans the full width, and a card with a button that’s start-aligned and hugs its contents.

<p>Buttons can hug their contents or span their containers based on context</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3xf0z5-05.png?alt=media

<h4>Showing &amp; hiding</h4><p>Components should show and hide information, or collapse and expand to selectively reveal content that best suits the space.</p><p>For example, <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> items may reveal descriptions or other additional information as their parent container scales.</p>

A list on mobile and on tablet. List items show additional text on tablet.

<p>List items can reveal more text on a tablet</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3xgph2-06.png?alt=media

<h4>Presentation changes</h4><p>Presentation changes include the orientation of elements and changes to specific properties, like color, type, and shape.</p><p>Components can also change configurations. For example, when a window size increases, a <app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/m3/pages/fab/overview" should-open-link-in-new-tab="true">FAB</app-froala-tooltip-element> can change to an extended FAB, and <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rails</app-froala-tooltip-element> can be automatically expanded.</p>

A large desktop window with an extended FAB. A smaller window shows a standard FAB. 

<p>The extended FAB can change to a standard FAB when the window is smaller</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3xiwiu-07.png?alt=media

## Spacing

<h2><span style="white-space:pre-wrap">Grouping</span></h2>

<p>Grouping is a method for connecting related elements that share a context, such as an image grouped with a caption. It visually relates elements and establishes boundaries to differentiate unrelated elements.</p>

Photo of dumplings with a caption reading “restaurants in the area”

<p><span style="white-space:pre-wrap">By placing a caption under an image this composition shows an explicit group</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxwwvqdk-1.png?alt=media

<p><span style="white-space:pre-wrap"><strong>Explicit grouping</strong> uses visual boundaries such as outlines, dividers, and shadows to group related elements in an enclosed area. Explicit grouping can also indicate that an item is interactive, such as list items contained between dividers, or a card displaying an image and its caption.</span></p>

Container of a contact grouped with photo and caption

<p><span style="white-space:pre-wrap">The elements in this card are explicitly grouped</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxwwxa8g-2.png?alt=media

<p id="isPasted"><strong>Implicit grouping</strong> uses close proximity and open space (rather than lines and shadows) to group related items. For example, a headline closely followed by a subhead and thumbnail image are implicitly grouped together by proximity and separated from other headline-subhead-thumbnail groups by open space.</p>

Carousel of images

<p><span style="white-space:pre-wrap">Images in a carousel are grouped by their proximity</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxwwyais-3.png?alt=media

<h2><span style="white-space:pre-wrap">Margins</span></h2>

<p>Margins are the spaces between the edge of a window area and the elements within that window area.<br /><br />Margin widths are defined using fixed or scaling values for each window size class. To better adapt to the window, the margin width can change at different breakpoints. Wider margins are more appropriate for larger screens, as they create more open space around the perimeter of content.<br /><br />See margin measurements for each window class: <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact window size class" link-url="/m3/pages/applying-layout/compact" should-open-link-in-new-tab="true" id="isPasted">compact</app-froala-tooltip-element>, <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium window size class" link-url="/m3/pages/applying-layout/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element>, <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded window size class" link-url="/m3/pages/applying-layout/expanded" should-open-link-in-new-tab="true">expanded</app-froala-tooltip-element>, <app-froala-tooltip-element description="Window widths 1200dp to 1599dp, such as desktop." link-label="More on large window size" link-url="/m3/pages/applying-layout/large-extra-large" should-open-link-in-new-tab="true">large</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Window widths 1600dp and larger, such as ultra-wide monitors." link-label="More on extra-large window size" link-url="/m3/pages/applying-layout/large-extra-large" should-open-link-in-new-tab="true">extra-large.</app-froala-tooltip-element></p>

Screen highlighting vertical blue margin on left side of screen

<p><span style="white-space:pre-wrap">A margin separates the edge of the screen from the elements on the screen</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxwx04xw-1.png?alt=media

<h2>Spacers</h2>

<p>A spacer refers to the space between two <app-froala-tooltip-element description="Panes are layout containers that house other components and elements within a single app. A pane can be: fixed, flexible, floating, or semi permanent." link-label="More on panes" link-url="/m3/pages/understanding-layout/parts-of-layout#667b32c0-56e2-4fc2-a618-4066c79a894e" should-open-link-in-new-tab="true">panes</app-froala-tooltip-element> in a layout. Spacers measure 24dp wide.</p>

Screen highlighting vertical blue margin on left side of screen

<ol class="decimal"><li>A spacer splits two panes from each other</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxwx1ijr-5.png?alt=media

<p>A spacer can contain a <app-froala-tooltip-element description="A drag handle adjusts the layout when there are 2 or more panes." link-label="More on drag handles" link-url="/m3/pages/understanding-layout/parts-of-layout/de6cf3b8-1bf1-4638-99c4-da52d6561ebc#314a4c32-be52-414c-8da7-31f059f1776d" should-open-link-in-new-tab="true">drag handle</app-froala-tooltip-element> that adjusts the size and layout of the panes. The handle's touch target slightly overlaps the panes.</p>

Pane drag handle touch target overlapping two panes.

<ol class="decimal"><li>Drag handle touch target</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxwx2hj1-6.png?alt=media

<h2>Padding</h2>

<p>Padding refers to the space between UI elements. Padding can be measured vertically and horizontally and does not need to span the entire height or width of a layout. Padding is measured in increments of 4dp.</p>

Full screen-width photo with padding below it and text below the padding

<ol id="isPasted"><li id="isPasted">Padding separates a headline from a image above</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxwx3xmp-3.png?alt=media

## Density

<h2>Overview</h2>

<ul><li><span style="white-space:pre-wrap">Information density is the consideration of the amount of information visible on the screen</span></li><li><span style="white-space:pre-wrap">The default target size should be at least 48x48 CSS pixels</span></li><li><span style="white-space:pre-wrap" id="isPasted">Users can change density as long as the density controls are accessible</span></li><li><span style="white-space:pre-wrap" id="isPasted">Apply density thoughtfully; not every layout needs it</span></li><li><span style="white-space:pre-wrap" id="isPasted">Layout and component scaling (component adaptation or component density) can allow users to scan, view, or compare more information at once</span></li></ul>

A website design with a denser arrangement of text and graphics.

<p><span style="white-space:pre-wrap">Information density</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6fec25z-GM3-Components-Density-2-v03.mp4?alt=media

Visual representation of component scaling with multiple size examples.

<p><span style="white-space:pre-wrap">Component scaling</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6fedlg1-GM3-Components-Density-1-v02.mp4?alt=media

<p id="isPasted"><strong>Information density</strong></p><ul><li>Information density can be achieved through layout and design decisions without using component scaling</li><li>Users may not benefit from increased density</li></ul>

<p id="isPasted"><strong>Component scaling</strong></p><ul><li>Components can adapt and change dimensions to allow users to scan, view, or compare different amounts of information</li><li>Don't apply component scaling by default if it would result in a target below 48x48 CSS pixels</li></ul>

An email app on desktop with a menu open to change information density between cozy, comfortable, and compact.

<p><span style="white-space:pre-wrap">Information density and component scaling can be used together to provide more information and additional user control</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6feg3jn-GM3-Components-Density-3-v02.mp4?alt=media

<h2>Information density</h2>

<p id="isPasted">Information density refers to the amount of content (such as text, images, or videos) in a given screen space.</p><p>A layout’s spacing dimensions, including margins, spacers, and padding, can change to increase or decrease its information density. High density layouts can be useful when users need to scan, view, or compare a lot of information, such as in a data table. Increasing the layout density of lists, tables, and long forms makes more content available on-screen.</p><p>Consider density settings in the context of a device. Although a user may prefer a denser layout for desktop, they may not for mobile. Density shouldn’t automatically change across window-size classes or device orientation without users changing it.</p>

High density layout

<p>Consider using higher density information design when users need to scan lots of information</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzjckoeo-3.png?alt=media

News website on desktop displaying a high information density. 

<p>Consider the amount and priority of information on-screen. Higher density can be useful for data-rich sites (news, financial portals, dashboards) where users expect lots of information quickly.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzjcmxrs-4.png?alt=media

News website on desktop displaying a low information density. 

<p>Lower density can be better for sites prioritizing aesthetics, a focused message, less information, or easier navigation</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzjcnouc-5.png?alt=media

<h2>Component scaling</h2>

<p id="isPasted">The component density scale controls the internal spacing of individual components.</p><p>The density scale is numbered, starting at 0 for a component’s default density. The scale moves to negative numbers (-1, -2, -3) as space decreases, creating higher density.</p><p>Higher density is typically applied by decreasing the top and bottom padding or overall height by 4dp.</p>

Three buttons, with densities  of +1, 0, and -1.

<p>Buttons in 3 different densities. Apply button density based on the needs and layout of a design.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzje0jnk-7.png?alt=media

<p id="isPasted">Center the grouped element within the component container.</p><p>Text size shouldn’t change as the container size scales.</p>

Stacked element showing 20 dp between label and input

<p>The measurement between the label and input is 20dp</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzje23wv-8.png?alt=media

Parent container showing label above input.

<p>The label and input are centered within their parent container</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzje3e0s-9.png?alt=media

Dropdown menu selectable space  height of 36 dp

<p>Don’t increase density in UIs that involve focused tasks, such as selecting from a menu. It reduces usability by limiting selectable space.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzje4oe2-10-dont.png?alt=media

Single-line snackbar

<p>Don't increase the density in components that alert the user of changes, such as snackbars or dialogs</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzje5tgh-11-dont.png?alt=media

<h3>Avoid applying component scaling by default</h3>

<ul><li id="isPasted">Don't apply component scaling to layouts by default that lower the target size below a default size of 48x48 CSS pixels</li><li>Allow users to opt for a higher density layout or theme, and provide a simple, accessible way to revert to default best practices</li></ul>

<p id="isPasted">People should be able to <strong>opt</strong><strong> in</strong> to dense layouts and components.</p><p>To ensure that density settings can be easily reverted, targets in settings interactions must follow defaults (48x48 CSS pixels).</p>

A density menu with large, medium, and small options to customize the screen layout of a table on desktop. 

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzje9ukn-12a.png?alt=media

<h2>Targets</h2>

<p>Dense components can be less accessible because interactive elements are smaller, so use caution when increasing information density.</p>

Selectable target of only 40 dp

<p>Use caution when applying component scaling where selectable targets will be reduced to less than the 48x48dp best practice and only apply density where it provides a better user experience.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzjqo90o-13-caution.png?alt=media

<p>Use caution when applying density to interaction targets. Following best practices, accessible targets should retain a minimum of 48x48dp, even if their visual element (such as an icon) is smaller.</p>

Settings button is 24 by 24 dp, but has interaction target of 48 x 48 dp.

<p>The target should remain 48x48, even if the icon is smaller.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzk8ysbx-15.png?alt=media

Button with height of 36 dp and interaction target of 48 dp

<p>The interaction target of a common button can be larger, as long as it meets the 48x48dp minimum size.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzjqrzlp-15.png?alt=media

<h2>Pixel density</h2>

<p id="isPasted">The number of pixels that fit into an inch is referred to as pixel density. High-density screens have more pixels per inch than low-density ones. As a result, UI elements of the same pixel dimensions appear larger on low-density screens, and smaller on high-density screens.</p><p>To calculate pixel density:</p><p>Screen density = Screen width (or height) in pixels / Screen width (or height) in inches</p>

Magnified UI element  showing a high number pixels in the focus area

<p>A high-density ui element</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzjquwp8-16.png?alt=media

Magnified UI element  showing the low number of pixels in the focus area 

<p>A low-density UI element</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzjqw7id-17.png?alt=media

<h3>Density-independent pixels</h3><p id="isPasted">Density-independent pixels, written as dp, are flexible units that scale to have uniform dimensions on any screen. They provide a flexible way to accommodate a design across devices. Material design system uses density-independent pixels to display elements consistently on screens with different densities.</p><p>A dp is equal to one physical pixel on a screen with a density of 160.</p><p>To calculate dp: dp = (width in pixels * 160) / screen density</p>

Screen with grid representing  low number of pixels

<p>Low-density screen displayed with density independence</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzjqylun-18.png?alt=media

Screen with grid representing  high number of pixels

<p>High-density screen displayed with density independence</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzjr0140-19.png?alt=media

<div class="table-wrapper"><table style="width:100%"><thead><tr><th>Screen physical width</th><th>Screen density<br /></th><th>Screen width in pixels<br /></th><th>Screen width in dps<br /></th></tr></thead><tbody><tr><td>1.5 in</td><td>120</td><td>180 px</td><td rowspan="3">240 dp</td></tr><tr><td>1.5 in</td><td>160</td><td>240 px</td></tr><tr><td>1.5 in</td><td>240</td><td>360 px</td></tr></tbody></table></div>

## Hardware considerations

<p><strong><app-froala-tooltip-element description="Window size classes are opinionated breakpoints where layouts need to change to optimize for available space, device conventions, and ergonomics." link-label="More on window size classes" link-url="/m3/pages/applying-layout/window-size-classes" should-open-link-in-new-tab="true">Window size classes</app-froala-tooltip-element></strong> provide the foundation for top level layout decisions, but display-specific considerations are also needed.</p>

<h2>Display cutout</h2>

<p id="isPasted">A display cutout is an area on some devices that extends into the display surface. It allows for an edge-to-edge experience while providing space for important sensors on the screen of the device. </p><p>Applications can extend around display cutouts or other features, but some parts of the UI might be obscured.</p>

Content safe area shown in portrait and in landscape mode.

<p>A mobile device’s content-safe area around a display cutout for the front-facing camera</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2cfdc-1.png?alt=media

<h2>Foldable devices</h2>

<p>Foldable devices use a folding mechanism to fold and unfold. They have unique characteristics to consider when designing layouts.</p>

<h3>Fold</h3><p id="isPasted">The fold of a foldable device divides the screen into two portions, either horizontally or vertically. The fold can be a flexible area of the screen or, on dual-screen devices, a hinge that separates two displays.</p><p>A flexible fold is barely visible, although some users may feel a tactile difference on the screen surface. Content can flow over the fold fairly easily.</p>

Center fold of a foldable device layout.

<ol class="decimal"><li>Folds are typically found in the center of the device screen and can present a seamless experience</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2dejk-2.png?alt=media

<p>On devices with a physical hinge, designing the screen as two distinct sections (separate window areas or panes) allows a composition to work well across the hinge and screens.</p>

Center fold on a foldable device with a physical hinge.

<p>A physical hinge separates two parts. There is no display hardware in this region.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2eac2-3.png?alt=media

<h3>Device state</h3><p>Foldable devices can have several physical states: folded, open flat, and tabletop.</p>

<h4>Folded</h4><p>The folded state can include a front screen, which often fits in the compact window size class, just like a mobile phone in portrait orientation.</p>

Compact window of a folded device.

<p>The front screen of a foldable device</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2fbwo-4.png?alt=media

<h4>Open flat</h4><p>An open flat state refers to the fully opened screen, which usually increases the window size class to medium or expanded. An open device can be used in landscape or portrait orientations.</p>

Open portrait state of a mobile device.

<p id="isPasted">In an open portrait state, the longer device edge is vertical while the shorter edge is horizontal</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2g4q8-5.png?alt=media

Open landscape state of a mobile device.

<p id="isPasted">In an open landscape state, the longer device edge is horizontal while the vertical edge is shorter</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2gth1-6.png?alt=media

<h4>Tabletop</h4><p id="isPasted">Tabletop refers to a half-opened state forming a rough 90 degree angle, with one half of the device resting on a surface. This posture resembles a laptop.</p><p>UI controls near the fold can be difficult for users to access, and text overlaying the fold can be hard to read.</p>

Tabletop state of a mobile device showing camera ;ems  on the vertical plane.

<p id="isPasted">If camera hardware is present, a tabletop device is best positioned on a side without any protruding hardware elements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2hz6b-7.png?alt=media

<h3>Interaction</h3>

<h4>App continuity</h4><p id="isPasted">When running on a foldable device, an app can transition from one screen to another automatically. After the transition, the app should resume in the same state and location, and the current task should continue seamlessly.</p>

A news app in compact mode compared to the open landscape state where the news app expands with a new column next to the compact news feed.

<p>A news app shows a feed in a compact and expanded window class when a foldable device switches device state</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2j1zj-8.png?alt=media

<h4>Scrolling and multiple panes</h4><p id="isPasted">Depending on how your app uses panes, the scroll behavior of a folded design may change in the unfolded design. </p><p>If you expand a pane, you can decide whether the whole window will scroll together or if each side (each pane) scrolls independently. </p>

A foldable device screen in open landscape mode with a single pane showing vertical scroll arrows.

<p>A single pane can scroll its inside content vertically and horizontally</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2khfi-9.png?alt=media

<p><span style="white-space:pre-wrap">If your design has multiple panes, each pane can operate as an independently scrollable area.</span></p>

A foldable device screen in open portrait mode with double panes each with a vertical scroll arrow.

<p>Multiple panes can scroll inside content independently of one another</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2lo3u-10.png?alt=media

<h2>Multi-window mode</h2>

<p id="isPasted">Multi-window mode is an Android system feature for <strong>displaying multiple apps on the same screen. </strong>This can be especially useful for multi-tasking, or workflows that depend on comparing information.</p><p>Note: This concept should not be confused with using multiple panes to display content from a single app. For more on that, see: Panes.</p>

2 apps appear side-by-side with a task bar below spanning the width of the screen.

<p>Screen displaying an email app and a contacts app in multi-window mode</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2mmo2-1.png?alt=media

<h3>User needs</h3>

<p id="isPasted">The ways that windows are created, arranged, and adjusted should feel straightforward for all users and across any window size class. Methods for seamless window management include:</p><ul><li>Apply smooth transitions as described in motion guidance</li><li>Ensure that users can create multiple windows easily and move between them as needed</li><li>Keep mental models and interaction patterns simple so that users aren’t required to think about which mode is appropriate for each task</li><li>Design and implement window dynamics consistently across variations in foldable hardware, including those with a hinge that separates two displays</li></ul>

<h3>Window creation and behavior</h3>

<p>Android provides several ways for users to create a multi-window view.</p>

<h3>Taskbar</h3><p id="isPasted">The taskbar provides a launching point for pinned and suggested apps to easily become a separate window. </p><p>To create a new window, a user selects and drags an app from the taskbar and moves the app icon to indicate where the new window should be displayed.</p>

The taskbar is positioned at the bottom of a screen.

<p>Android taskbar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2qc2a-2.png?alt=media

<h3>Context menu</h3><p id="isPasted">Users can also create multiple windows through the overview by the app context menu.</p>

2 apps appear side-by-side with a task bar below spanning the width of the screen.

<p>Multi-window mode can have vertical positioning</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2rmbq-3.png?alt=media

2 apps are stacked in landscape mode with a task bar below spanning the width of the screen.

<p>Multi-window mode can have horizontal positioning</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2uu5h-4.png?alt=media

<h3>Adjusting window sizes</h3><p id="isPasted">By default multiple windows are created as a 50/50 side-by-side split.</p><p>The windows can be adjusted further to 1:3 or 2:3 proportions. These ratios provide a primary and secondary window dynamic, offering greater flexibility and allowing focus on one application as needed.</p><p>When in a multi-window mode, the available screen area often changes from medium or expanded window class to compact. Layouts should adapt accordingly.</p>

2 apps appear side-by-side with the left-side app using two-thirds of the screen, and the right app one-third.

<p>The screen handle can be dragged and released to create the desired window ratio. The handle automatically adjusts to the closest snap point.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxx2y99m-5.png?alt=media

## Bidirectionality & RTL

<p><a href="https://www.w3.org/International/questions/qa-scripts.en.html" target="_blank" rel="noopener noreferrer">Over 2 billion people</a> read and write in right-to-left (RTL) languages like Arabic, Hebrew, Farsi and Urdu. Layouts should support both left-to-right (LTR) and RTL languages through mirroring and other best practices to ensure content is easy for global audiences to understand and navigate. Consider the holistic experience including <a href="/m3/pages/global-writing/overview#0d0f8403-e5ff-4579-be74-0c4dbcef7fcb" target="_blank" rel="noopener noreferrer">global writing</a>, localizing voice and <a href="/m3/pages/icons/designing-icons#1056d971-81ca-4abe-b931-42185dd76638" target="_blank" rel="noopener noreferrer">design principles for culturally appropriate icons</a>. Material's components are built to support RTL, such as naming elements and tokens as "leading" and "trailing." However, extra configuration may be needed to achieve specific RTL situations.</p>

<h2>Mirroring</h2>

<p>When a layout is changed from LTR to RTL (or vice-versa), and flipped horizontally, it’s often called mirroring. UI elements and text that typically appear on the left in LTR aligns to the right. Reading flow starts from the top right corner, instead of the top left.<br /><br />Not all elements mirror with RTL languages. For example, graphs and charts maintain a LTR directionality for Persian and Urdu.</p>

Layout in LTR and mirrored for RTL language.

<p>A mirrored layout in an RTL language reverses the alignment and ordering of elements.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rr3ndk-1.png?alt=media

<h2>Text rendering</h2>

<p>Correct text rendering is foundational for a great user experience and it’s critical for readability and usability. Text rendering has two parts:</p><ol class="decimal"><li>Alignment: How the edges of the text box are placed alongside other elements.</li><li>Directionality: How text and other elements flow within a text box, like left-to-right, or right-to-left.</li></ol><p>In RTL languages, text is usually right-aligned, and elements flow from right-to-left.   Common issues with RTL language rendering are text entry, cursor position, punctuation, phone numbers, and URLs.   Improperly rendering text in RTL languages can create cognitive overload and negatively impact user sentiment and trust.</p>

Text field incorrectly displaying the word order of an email address and cursor placement.

<p>Don't reverse the order of the email username and domain (@google.com). The domain should always be to the right of the username.  Usernames can still be written RTL, with the cursor moving to the left.<br /><br />Note this example is not translated to illustrate a common issue with text rendering </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rr60jz-2%20-%20A.png?alt=media

Dialog window incorrectly displaying word order decreasing readability.

<p>Don’t apply LTR directionality to RTL content because it may scramble word order. To ensure readability across all languages. The content should have both RTL alignment and directionality.</p><p><br />Note this example is not translated to illustrate a common issue with text rendering</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm7cj5hjy-2%20-%20B.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LF2lHKz-y2dHfC1eRLilwX8m2_AGCUvSt_bgVe-Qai7o129OK1nKLNHd1_1cdpjOO_YBM9wcGPce855LPc2eXl6IbUc2LhVGKvoF5RAZjEZm=s1312

<h2>Icons and symbols</h2>

<p>In RTL languages, directional UI icons, like back and forward, should be mirrored. However, in Hebrew timelines and media controls on a page should retain left-to-right directionality.<br /><br />The meaning of icons and symbols can vary significantly across cultures.</p>

Back and forward icons in LTR and RTL.

<p>Back and foward icons are mirrored in RTL</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rre3h2-3%20-%20A.png?alt=media

Send and question mark in LTR and RTL.

<p>Send buttons are mirrored in RTL. Help icons are mirrored in some RTL languages, like Urdu and Persian.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rrfly7-3%20-%20B.png?alt=media

<h2>Time</h2>

<p>Linear representations of time are often mirrored in RTL language experiences. <br /><br />Linear progress indicators should move from right to left for most RTL languages, except Hebrew where it should remain LTR.<br /><br />Circular representations of time remain the same.</p>

RTL linear progress indicators filling from right to left  and circular progress indicators filling clockwise .

<ol class="decimal"><li>RTL linear progress indicator starts to fill progress from the right </li><li>Circular progress indicators move clockwise</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rrip79-4.png?alt=media

<h3>Media players</h3><p>Media controls for video or audio players are always LTR.</p>

Media player with control and progress in LTR and all other content is RTL.

<p>In Urdu, controls and progress for media and a podcast title are shown in LTR, while all other content is RTL.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rt3wci-5_urdu.png?alt=media

<h3>Clock</h3><p>For RTL languages, the directionality of time remains LTR, and clocks still turn clockwise. However, the AM/PM symbols for 12h clocks should be placed to the left. The 24-hour clock is often used in countries where the primary language is not English.<br /><br />Clock icons, circular refresh icons, and progress indicators with arrows pointing clockwise should not be mirrored.</p>

24 hour clock in RTL.

<p>24-hour clocks in RTL move clockwise, but mirror elements such as buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rt5hlh-6%20-%20A_hebrew.png?alt=media

12 hour clock in RTL. 

<p>12-hour clocks in RTL move clockwise, but mirror UI elements such as AM/PM and buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rt6mj7-3%20-%20B_arabic.png?alt=media

<h2>Canonical layout examples</h2>

<h3>List-detail</h3><p>The <a href="/m3/pages/canonical-layouts/list-detail" target="_blank" rel="noopener noreferrer">list-detail</a> layout divides the app window into two side-by-side panes, and is mirrored in RTL.</p>

RTL list layout.

<p>List-detail mirrored for RTL, where text and other elements are aligned to the right and flow from right to left</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rt95z5-7_hebrew.png?alt=media

<h3>Feed</h3><p>Use a <a href="/m3/pages/canonical-layouts/feed" target="_blank" rel="noopener noreferrer">feed layout</a> to arrange content elements like cards in a configurable grid for quick, convenient viewing of a large amount of content. The feed layout is mirrored in RTL.</p>

RTL feed layout.

<p>Feed layout mirrored for RTL, where the order of text, grid, and other elements align to the right and flow from right to left</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rtc29p-8.png?alt=media

<h3>Supporting pane</h3><p>Use the <a href="/m3/pages/canonical-layouts/supporting-pane" target="_blank" rel="noopener noreferrer">supporting pane</a> layout to organize app content into primary and secondary display areas. The supporting pane layout is mirrored in RTL.</p>

RTL supporting pane in a RTL language.

<p>Supporting pane to the left of the primary content. Text and other elements within the pane are aligned to the right and flow from right to left.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rtekg5-9_urdu.png?alt=media

<h2>Component examples</h2>

<h3>Badges</h3><p>Change the position and alignment of <a href="/m3/pages/badges/specs" target="_blank" rel="noopener noreferrer">badges</a> for RTL languages.</p>

Small badge on the top left of the icon.

<p>Small badge appears on the top left of the icon</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rtgvbk-10%20-%20A_urdu.png?alt=media

Large badge on the top left of the icon.

<p>Large badge appears on the top left of the icon</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rtjdwz-10%20-%20B_urdu.png?alt=media

<h3>Toolbar</h3><p><a href="/m3/pages/toolbars/guidelines" target="_blank" rel="noopener noreferrer">Toolbars</a> provide actions related to the current page. For RTL languages, mirror the order of the tools.</p>

RTL floating toolbar

<p>Mirrored floating toolbar, where the FAB appears on the left of the screen</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmall2gyv-11.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/vJXzgBPOhjldo7WY5RopuHczELv2Q6gFFOV9qfzbScgrdaaPlNe-tfWaDy1ExbeYJokecz57a9NcPlKJVJ-_Ax-4kUbCuKUbnPZXzwZYhd__Pw=s1352

<h3>App bar</h3><p><a href="/m3/pages/app-bars/overview" target="_blank" rel="noopener noreferrer">App bars</a> are placed at the top of the screen to help people navigate through a product.<br /><br />Mirror app bar layout in RTL, and flip appropriate icons, such as arrows.</p>

3 app bars in RTL.

<ol class="decimal"><li>RTL center-aligned/small </li><li>RTL medium flexible </li><li>RTL large flexible</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rtqm4b-12_urdu.png?alt=media

<h3>Navigation drawer</h3><p><a href="/m3/pages/navigation-drawer" target="_blank" rel="noopener noreferrer">Navigation drawers</a> that open from the side are always placed on the leading edge of the screen, on the left for LTR languages, and on the right for RTL.</p>

RTL navigation drawer, including a mirrored icons.

<p>RTL navigation drawer, including a mirrored icon for outbox</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rttjl0-13_arabic.png?alt=media

<h3>Navigation rail</h3><p>The <a href="/m3/pages/navigation-rail/guidelines" target="_blank" rel="noopener noreferrer">navigation rail</a> is placed on the leading edge of the screen, on the left side for LTR, and on the right for RTL.</p>

Nav rail in the right side for RTL languages, and left side for LTR languages.

<p>Based on the language being used, a navigation rail is set on a screen’s leading edge. This is the right side for RTL languages, and left side for LTR languages.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rtvteh-14_hebrew.png?alt=media

<h3>Text fields</h3><p>Icons in <a href="/m3/pages/text-fields/guidelines#5c8a5f07-b1a5-455f-bf76-7ff0d724f6b0" target="_blank" rel="noopener noreferrer">text fields</a> are optional. Leading and trailing icons change their position based on LTR or RTL contexts.</p>

Text fields in RTL with leading and trailing icons.

<p>Icons, symbols and label text for RTL: </p><ol class="decimal"><li>Icon signifier </li><li>Valid or error icon </li><li>Clear icon </li><li>Voice input icon </li><li>Dropdown icon </li><li>Image</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6rtykdl-15.png?alt=media

<h3>Chips</h3><p>The leading icon of input chips can be an icon, logo, or circular image.<br /><br />The trailing icon is always aligned to the end side of the container. It’s placed on the right for LTR and on the left for RTL.</p>

Filter chips in RTL layout.

<p>Filter chips shown in an RTL layout. Note this example is not translated to help illustrate mirroring.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8rhslpk-16.png?alt=media

<h2>Swipe gestures</h2>

<p>Gestures are the ways people interact with UI elements using touch or body motion.<br /><br />People can navigate horizontally between peer views like tabs, and to complete actions. <br /><br />RTL swiping and gestures should mirror their counterparts in LTR. If an app includes a "delete" icon revealed when swiped from the right for LTR languages, the same should be possible on the left for RTL languages. </p>

RTL list layout with swipe gesture revealing additional actions.

<p>Swiping reveals additional action in RTL list layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6ru2ith-17.png?alt=media

<p>On Android, <a href="https://github.com/material-components/material-components-android/blob/master/docs/foundations/PredictiveBack.md" target="_blank" rel="noopener noreferrer">predictive back</a> allows people to swipe left or right on the screen to go back or dismiss modal components.<br /><br />RTL predictive back features should mirror those found in a LTR context.</p>

Back swipe for RTL languages. The back swipe on a bottom sheet takes user back to previous screen of a photo feed.

<p>Preview of the result of the gesture for RTL languages</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8p23uu6-GM3_Bidirectionality_Interaction%20Gestures_6_IA_v02.mp4?alt=media
