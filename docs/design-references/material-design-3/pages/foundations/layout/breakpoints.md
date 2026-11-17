# Breakpoints

Source: https://m3.material.io/foundations/layout/breakpoints
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/16281dc1-7630-4e78-abaf-c9bc8be69663.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Breakpoints ensure layouts work across a wide range of devices

## Overview

<p>Material uses breakpoints to create adaptive designs that work across devices:</p><ul><li><p>There are five main <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element>: compact, medium, expanded, large, and extra-large</p></li><li><p>Layouts typically transition from a single pane to two or three panes as window size increases</p></li><li><p>When moving across breakpoints, decide which elements to reveal, divide, resize, reposition, or swap</p></li></ul>

<h2>Breakpoints overview</h2>

<p>A breakpoint (previously window size class) is the window size at which a layout needs to change to match available space, device conventions, and ergonomics. These apply to Android and web.</p><p>All devices fall into one of five Material breakpoints: </p><ul><li><p>Compact</p></li><li><p>Medium</p></li><li><p>Expanded</p></li><li><p>Large</p></li><li><p>Extra-large</p></li></ul><p>Rather than designing for an ever-increasing number of display states, focusing on breakpoints ensures layouts work across a wide range of devices.</p>

3 breakpoints from small to expanded.

<ol class="decimal"><li><p>Compact</p></li><li><p>Medium</p></li><li><p>Expanded</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3zlnnl-01.png?alt=media

<p>Large and extra-large breakpoints are used on devices like laptops, desktops, and external monitors.</p>

2 devices with large and extra-large breakpoints.

<ol class="decimal"><li><p>Large</p></li><li><p>Extra-large</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3zmg9g-02.png?alt=media

<p><strong>Design for breakpoints instead of specific devices because:</strong></p><ul><li><p>The amount of available window space is dynamic and changes based on user behavior, such as multi-window modes or unfolding a foldable device</p></li><li><p>Devices fall into different breakpoints based on orientation</p></li></ul>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Breakpoint</p></th><th><p>Width (dp)</p></th><th><p>Common devices</p></th></tr></thead><tbody><tr><td><p>Compact</p></td><td><p>Under 600dp</p></td><td><p>Phone in portrait</p></td></tr><tr><td><p>Medium</p></td><td><p>600–839dp</p></td><td><p>Tablet in portrait</p><p>Foldable in portrait (unfolded)</p></td></tr><tr><td><p>Expanded</p></td><td><p>840–1199dp</p></td><td><p>Phone in landscape</p><p>Tablet in landscape</p><p>Foldable in landscape (unfolded)</p><p>Desktop</p></td></tr><tr><td><p>Large</p></td><td><p>1200–1599dp</p></td><td><p>Desktop</p></td></tr><tr><td><p>Extra-large</p></td><td><p>1600dp+</p></td><td><p>Desktop</p><p>Ultra-wide monitors</p></td></tr></tbody></table></div>

<h3>Height breakpoints</h3><p>On Android, compact, medium, and expanded breakpoints are also available for <a href="https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes#window_size_classes" target="_blank">height</a>. These can be used to adjust the layout when available vertical space is unusually small or large. However, since most layouts contain vertically scrolling content, it's rare that layouts need to adjust to available height.</p>

<h2>Designing across breakpoints</h2>

An email app shown at 3 breakpoints: compact, medium, and expanded.

<p>Products should automatically adapt to any breakpoint</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3znkbk-03-a%20-%20USE%20AS%20STATIC%20ASSET.png?alt=media

2 screens at large and extra-large breakpoints.

<p>A product’s layout should adjust to fit each breakpoint. For example, a large window can have two panes, while an extra-large window can have three.  </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3zoh5f-04-a.png?alt=media

<p>Each product view should have a layout for the breakpoints most appropriate for your platform and users.</p><p>Different components are recommended for performing the same function across the five layouts.</p>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Breakpoint</p></th><th><p>Panes</p></th><th><p>Navigation</p></th><th><p>Communication</p></th><th><p>Action</p></th></tr></thead><tbody><tr><td><p>Compact</p></td><td><p>1</p></td><td><p>Navigation bar, modal expanded</p><p>navigation rail</p></td><td><p>Simple dialog</p><p>Full-screen dialog</p></td><td><p>Bottom sheet</p></td></tr><tr><td><p>Medium</p></td><td><p>1 (recommended) or 2</p></td><td><p>Navigation bar, modal expanded</p><p>navigation rail</p></td><td><p>Simple dialog</p></td><td><p>Menu</p></td></tr><tr><td><p>Expanded</p></td><td><p>1 or 2 (recommended)</p></td><td><p>Modal or standard expanded</p><p>navigation rail</p></td><td><p>Simple dialog</p></td><td><p>Menu</p></td></tr><tr><td><p>Large</p></td><td><p>1 or 2 (recommended)</p></td><td><p>Modal or standard expanded</p><p>navigation rail</p></td><td><p>Simple dialog</p></td><td><p>Menu</p></td></tr><tr><td><p>Extra-large</p></td><td><p>1 to 3 (recommended)</p></td><td><p>Modal or standard expanded</p><p>navigation rail</p></td><td><p>Simple dialog</p></td><td><p>Menu</p></td></tr></tbody></table></div>

<p>Start by designing for one breakpoint, then adjust the layout for the next size by asking these five questions:</p>

<h3>1. What should be revealed?</h3><p>Parts of the UI that are hidden on smaller devices can be revealed in larger layouts. </p><p>For example:</p><ul><li><p>On mobile, the navigation rail is collapsed by default</p></li><li><p>On an expanded device, the navigation rail can be open by default, revealing more actions and features</p></li></ul>

Email app layouts in compact and expanded windows.

<p>A product’s navigation rail can be revealed in an expanded layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3zwt8a-05.png?alt=media

<p>The same can be applied to <a href="/m3/pages/scaffold/panes" target="_blank">panes</a>. Larger layouts can simultaneously display an inbox pane and a pane containing a selected conversation. Additional space doesn’t just mean making the same thing bigger.</p>

Messaging app layouts in compact and expanded windows.

<p>An expanded layout for a messaging app reveals a second pane with the selected conversation</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3zxlki-06.png?alt=media

<h3>2. How should a screen be divided?</h3><p>When dividing a screen into layout panes, consider the breakpoint: </p><ul><li><p>Compact and medium breakpoints:  A single pane works best</p></li><li><p>Expanded and large breakpoints:  Two panes are recommended</p></li><li><p>Extra-large breakpoints: Consider using three panes </p></li></ul>

A compact and medium window have a single pane. A larger window has 2 panes.

<p>Compact and medium breakpoints should use a single pane, while larger breakpoints can use two</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3zyjaf-07.png?alt=media

<p>At medium breakpoints, two panes are useful when they contain low-density content with clear actions.  </p><p>Don’t use two panes in medium layouts with high information density, as it can reduce usability.</p>

Medium window with 2 panes with low-density content: an email setting menu and a list of setting switches.

<p>A settings view with low-density content and quick actions is a good use of two panes in a medium layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5k02j7-08.png?alt=media

Video app in a medium window has 1 pane in portrait layout and 2 in landscape.

<p>Rotating a device often changes the breakpoint. A layout can have two panes in landscape orientation, and one pane in portrait.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp400qwl-09.png?alt=media

<p>Single-pane layouts can focus attention on one action or view, creating a distraction-free environment for a specific goal such as:</p><ul><li><p>Playing a game</p></li><li><p>Watching a movie</p></li><li><p>Video calls</p></li><li><p>Creative applications</p></li></ul>

Video app in a single-pane landscape layout at an expanded breakpoint.

<p>Consider using an immersive single-pane layout for video calls</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp401fhs-10.png?alt=media

<h3>3. What should be resized?</h3><p>UI elements that are small on compact screens can grow as breakpoints increase. Panes can also expand to rearrange elements and make better use of space. </p><p>Consider resizing:</p><ul><li><p>Cards</p></li><li><p>Feeds</p></li><li><p>Lists</p></li><li><p>Panes</p></li></ul>

<p>Resizing can highlight imagery and improve text readability. This type of adaptation affects the scale of content and the relationship between objects on screen. For example, a vertical card on mobile can adjust its margins, orientation, text size, and density to better fit a tablet.</p><p>Across all breakpoints, adjust margins and type styles to keep text between 40–60 characters per line.</p>

2 cards in compact and medium layouts. The image and text are rearranged and resized to be more legible in the medium layout.

<p>A small card in a compact layout can be resized larger in a medium or expanded layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp402bv2-11.png?alt=media

<h3>4. What should be repositioned?</h3><p>A UI and its components can reflow or reposition to make use of additional space on expanded screens and in resized panes. Repositioning is also a way to match the ergonomic and input needs that change across device sizes, such as shifting actions from the bottom of a compact window to the leading edge of medium and expanded windows. This method is similar to responsive design on the web.</p><p>Consider:</p><ul><li><p>Repositioning cards</p></li><li><p>Adding a second column of content</p></li><li><p>Creating a more complex layout of photos</p></li><li><p>Introducing more negative space</p></li><li><p>Ensuring reachability for navigation and interactive elements</p></li></ul>

<p>Internal elements can be anchored to the left, right, or center as a parent container scales. Internal elements can also maintain fixed positions, such as a floating action button (FAB) in a navigation rail.</p>

Comparison of compact and medium breakpoints with tabs anchored to the middle of each layout.

<p>Tabs can remain anchored to the middle of a layout at both compact and medium breakpoints</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp40fx5f-12.png?alt=media

<p>In the case of a button, the icon and text label within the button container can remain anchored to each other, staying centered as the button container scales horizontally.</p>

Label text remains the same size and centered as button size increases.

<p>Button icons and label text can remain anchored to each other no matter the width</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp40h750-13.png?alt=media

<h3>5. What should be swapped?</h3><p>As a layout changes across breakpoints, components with similar functions can also be exchanged. This makes it possible to adjust a layout for large-scale changes to the ergonomic and functional qualities of an interface. </p>

<p>For example, a bottom navigation bar in a compact layout can be swapped with a navigation rail in a medium layout.</p>

A compact layout’s navigation bar becomes a navigation rail in an expanded layout.

<p>Swap a navigation bar in a compact layout for a navigation rail in a medium or expanded layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp40iha0-14.png?alt=media

<p>Likewise, a navigation rail can swap from collapsed to expanded at larger breakpoints.</p><p>Use caution when swapping components. Make sure: </p><ul><li><p>The interchangeable components are functionally equivalent</p></li><li><p>The component swap serves a functional and ergonomic purpose</p></li></ul><p>Don’t swap a button for a chip. Be careful when changing between list items and cards.</p>

A compact layout’s navigation rail expands in an extra-large layout.

<p>A collapsed navigation rail in medium or expanded layouts can become an expanded navigation rail in large or extra-large layouts</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp40ja5v-15.png?alt=media

A button is swapped out for a menu in a food delivery app.

<p>Don’t arbitrarily swap components that aren’t functionally equivalent, such as swapping a button with a menu</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4067x5-16.png?alt=media

<h3>Common swappable components</h3>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:20.6395%"><p>Component type</p></th><th style="width:25.7631%"><p>Compact</p></th><th style="width:25.7631%"><p>Medium</p></th><th style="width:27.6793%"><p>Expanded</p></th></tr></thead><tbody><tr><td><p>Navigation</p></td><td><p><app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">Navigation bar</app-froala-tooltip-element></p></td><td><p><app-froala-tooltip-element description="Collapsed navigation rails take up minimal space and are best for medium windows and larger." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">Collapsed navigation rail</app-froala-tooltip-element></p></td><td><p><app-froala-tooltip-element description="Collapsed navigation rails take up minimal space and are best for medium windows and larger." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">Collapsed navigation rail</app-froala-tooltip-element></p></td></tr><tr><td><p>Navigation</p></td><td><p>Modal <app-froala-tooltip-element description="Expanded navigation rails show text labels and an extended FAB, and can be default or modal." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">expanded navigation rail</app-froala-tooltip-element></p></td><td><p>Modal <app-froala-tooltip-element description="Expanded navigation rails show text labels and an extended FAB, and can be default or modal." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">expanded navigation rail</app-froala-tooltip-element></p></td><td><p>Standard <app-froala-tooltip-element description="Expanded navigation rails show text labels and an extended FAB, and can be default or modal." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">expanded navigation rail</app-froala-tooltip-element></p></td></tr><tr><td><p>Communication</p></td><td><p>Basic or <app-froala-tooltip-element description="Full-screen dialogs fill the entire screen, displaying actions that require a series of tasks to complete. They're often used for creating a calendar entry." link-label="More on full-screen dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">full-screen dialog</app-froala-tooltip-element></p></td><td><p><app-froala-tooltip-element description="Basic dialogs interrupt users with urgent information, details, or actions. They're often used for alerts, quick selection, or confirmation. " link-label="More on basic dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">Basic dialog</app-froala-tooltip-element></p></td><td><p><app-froala-tooltip-element description="Basic dialogs interrupt users with urgent information, details, or actions. They're often used for alerts, quick selection, or confirmation. " link-label="More on basic dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">Basic dialog</app-froala-tooltip-element></p></td></tr><tr><td><p>Supplemental selection</p></td><td><p><app-froala-tooltip-element description="Bottom sheets show secondary content anchored to the bottom of the screen." link-label="More on bottom sheets" link-url="/m3/pages/bottom-sheets/overview" should-open-link-in-new-tab="true">Bottom sheet</app-froala-tooltip-element></p></td><td><p><app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">Menu</app-froala-tooltip-element></p></td><td><p><app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">Menu</app-froala-tooltip-element></p></td></tr></tbody></table></div>

## Compact

<p>Layouts for compact <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element> are for <strong>screen widths smaller than 600dp.</strong></p>

Messaging app at a compact breakpoint.

<p>A compact breakpoint focuses on a single view</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp40sit1-01.png?alt=media

<h2>Navigation</h2>

<p>Use a navigation bar or modal expanded navigation rail.</p><p>Place navigation components close to the edge of the screen where they’re easier to reach.</p>

Navigation bar and FAB are close to the bottom of a mobile app in a compact window.

<p>Place navigation elements near the bottom of a compact window so they’re easy to reach</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp40u2kw-02.png?alt=media

<h2>Panes</h2>

<p>Use a single pane in compact layouts.</p>

The single pane consumes most of the area in a compact window.

<ol class="decimal"><li><p>Single-pane layouts work best for compact breakpoints</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp40uzbp-03.png?alt=media

<h2>Spacing</h2>

<p>Margins are 16dp from the leading and trailing edge of the window.</p>

The left and right margins of a compact window pane are 16dp.

<p>In compact layouts, use 16dp margins</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp40vzj4-04.png?alt=media

<h2>Special considerations</h2>

<p>A compact layout will need to transition dynamically to a medium or expanded layout when:</p><ul><li><p>A foldable device is unfolded</p></li><li><p>A mobile device is rotated from portrait to landscape</p></li><li><p>A tablet exits split-screen mode</p></li><li><p>A product is resized to be larger in multi-window mode</p></li><li><p>A free-form window is resized</p></li></ul>

2 mobile layouts showing a messaging app with a 1-pane list and an expanded navigation rail.

<p>Compact layouts should dynamically transition to larger layouts when a device is unfolded or rotated</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp40wssg-05.png?alt=media

## Medium

<p>Layouts for medium <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element> are for <strong>screen widths from 600dp to 839dp.</strong></p>

A medium breakpoint with a video call app in full-screen mode.

<p>Single-pane layouts can focus attention on one action or view, such as a video call</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp413hn4-01.png?alt=media

<h2>Navigation</h2>

<p>Place navigation components close to edges of the window where they’re easier to reach:</p><ul><li><p>Single-pane layouts: <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">Navigation rail</app-froala-tooltip-element></p></li><li><p>Two-pane layouts: <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">Navigation bar</app-froala-tooltip-element></p></li></ul><p>The navigation rail can be hidden in secondary destinations as long as the primary destination can still be accessed using a back button.</p>

The navigation area of a medium breakpoint is a vertical bar at the leading edge, beside a single pane.

<ol class="decimal"><li><p>Navigation area</p></li><li><p>Single pane</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp414ag3-02.png?alt=media

<h2>Panes</h2>

<h3>Single-pane layout  </h3><p>In a medium layout, a single pane is recommended because of limited screen width.</p>

A single pane uses most of the space in a medium window.

<ol class="decimal"><li><p>A single-pane layout is recommended for medium breakpoints</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp417y7j-03.png?alt=media

<h3>Two-pane layout</h3><p>Limit use of two panes for content with lower information density, such as a settings screen.</p><p>Each pane in a two-pane layout should take up 50% of the window width. Avoid setting custom widths. A drag handle can be used to expand or collapse panes to be 100% of the window width.</p>

2-pane layout in a medium window. Both panes fit 50% of the window width by default.

<p>Two-pane layouts should use 50% widths for each pane by default</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp418umv-04.png?alt=media

<p>When adding navigation to a two-pane layout, use a navigation bar. This allows the panes to fully use the available window width.</p>

A navigation bar extends over 2 panes at the bottom of a medium window.

<p>Two-pane layout with:</p><ol class="decimal"><li><p>Navigation bar</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp419dq9-05.png?alt=media

<h2>Spacing</h2>

<p>Medium layouts have margins of 24dp.</p><p>The <app-froala-tooltip-element description="A spacer is the space between two panes. If panes can be resized, the spacer contains a drag handle." link-label link-url should-open-link-in-new-tab="false">spacer</app-froala-tooltip-element> between panes is also 24dp.</p>

2 pane layout with 24dp margins and 24dp space between panes.

<p>Use 24dp for margins and spacer in a medium layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41ahko-06.png?alt=media

<h2>Special considerations</h2>

<p>A medium layout will need to transition dynamically to a compact or expanded layout when:</p><ul><li><p>A foldable device is folded</p></li><li><p>A tablet is rotated from portrait to landscape</p></li><li><p>A product goes from full-screen to split-screen</p></li><li><p>Multi-window mode is initiated</p></li><li><p>A free-form window is resized</p></li></ul>

Email app with 2 panes at  a medium breakpoint.

<p>Think of how a medium layout should change to a compact or expanded layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5kr0vt-07.png?alt=media

<h3>Reachability</h3><p>For horizontal tablets and unfolded foldables, the top 25% of the screen is likely out of reach, unless the grip is adjusted. To accommodate device and hand sizes, limit the amount of interactions that are placed in the upper 25% of the screen.</p>

The hard-to-reach top quarter of a medium breakpoint in landscape mode.

<ol class="decimal"><li><p>Limit interactions in the upper quarter of a screen, as they can be hard to reach</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41cohr-08.png?alt=media

<p>Avoid placing essential interactive elements too close to the bottom edge of the screen. Some users, particularly those with larger hands, might struggle to reach this area.</p><p>Specify interactions in a layout with these ergonomic regions in mind:</p><ol class="decimal"><li><p>Users can reach this area by extending their fingers, which makes it inconvenient</p></li><li><p>Users can reach this area comfortably</p></li><li><p>Reaching this area is challenging when holding the device</p></li></ol>

The 3 ergonomic regions of a medium breakpoint.

<p>Medium breakpoint ergonomic regions: </p><ol class="decimal"><li><p>Inconvenient</p></li><li><p>Comfortable</p></li><li><p>Challenging</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41dv1l-09.png?alt=media

## Expanded

<p>Layouts for expanded <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element> are for <strong>screen widths from 840dp to 1199dp.</strong></p>

Supporting pane layout of a video app. The large, primary pane has the video, title, and actions. The secondary pane has queued videos.

<p>Two-pane layouts are often best for expanded breakpoints</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41hvbo-01.png?alt=media

<h2>Navigation</h2>

<p>Place navigation components close to edges of the window where they’re easier to reach. Use a <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element>, either collapsed or expanded.</p><p>The navigation rail can be hidden in secondary destinations as long as the primary destination can still be accessed using a back button.</p><p>For sorting, filtering, or secondary navigation, use tabs or other components directly in the pane.</p>

The navigation area is a vertical bar at the left of the screen. To its right, the body pane fills the rest of the window.

<ol class="decimal"><li><p>Navigation area</p></li><li><p>Single pane</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41iro5-02.png?alt=media

<h2>Panes</h2>

<p>Use a single-pane or two-pane layout.</p><p>A two-pane layout is often best for expanded breakpoints. However, a single-pane layout can work when displaying visually- or information-dense content, such as videos.</p>

A single pane covers most of the expanded screen except for the navigation area and margins.

<p>At an expanded breakpoint, reserve single-pane layouts for information-dense content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41jkb5-03.png?alt=media

<p>When using a <a href="/m3/pages/scaffold/panes#92371c3b-587d-4c6f-8105-05b69dcec81a" target="_blank">fixed-and-flexible</a> layout, the fixed pane should have a width of 360dp by default.</p>

A 2-pane layout at an expanded breakpoint. The fixed pane starts at 360dp, then expands to a single-pane layout.

<p>In a fixed-and-flexible layout, the fixed pane is 360dp by default</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41knzh-GM3_Applaying%20Layout_Understanding_Part_10_IA_v01.mp4?alt=media

<p>A <a href="/m3/pages/scaffold/panes#dc7982b7-754c-410a-9e88-18a54557c87b" target="_blank">split-pane layout</a> uses two flexible panes and visually centers the spacer by default. </p>

A nav rail and a pane fill 50% of the window. A second pane fills the remaining 50%.

<p>The navigation and first pane are 50% of the window width to keep the spacer visually centered</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41lyj0-ly7433ph-GM3-Styles-Foundations-Layout-ApplyingLayout-2-v01.mp4?alt=media

<h2>Spacing</h2>

<p>Expanded layouts have a leading and trailing margin of 24dp.</p><p>The spacer between panes is 24dp.</p>

2 pane layout with 24dp margins and 24dp space between panes.

<p>Use 24dp for margins and spacer in an expanded layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5l3xgt-06.png?alt=media

<h2>Special considerations</h2>

<p>An expanded layout will need to transition dynamically to a compact or medium layout when:</p><ul><li><p>A foldable device is folded</p></li><li><p>A tablet is rotated from landscape to portrait</p></li><li><p>The app goes from full-screen to split-screen</p></li><li><p>Multi-window mode is initiated</p></li><li><p>A free-form window is resized</p></li></ul>

Email app moves from 2-pane expanded layout to medium to 1-pane small layout.

<p>Consider how an expanded layout should change at medium and compact breakpoints</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41ofdd-GM3_Applaying%20Layout_Expanded_07_IA_v01.mp4?alt=media

## Large & extra-large

<p>These breakpoints are most useful for creating web experiences tailored to laptop and desktop devices. Some products may not need large and extra-large breakpoints. Consider your platform’s conventions and users when making decisions on which breakpoints to design for.</p><ul><li><p>Layouts for large <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element> are for screen widths <strong>from 1200dp to 1599dp</strong></p></li><li><p>Layouts for extra-large breakpoints are for screen widths of <strong>1600dp and larger</strong></p></li></ul>

Large window with a video app in 2 pane layout.

<p>A two-pane layout is recommended for large and extra-large breakpoints</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41v09e-01.png?alt=media

<h2>Navigation</h2>

<p>Use a <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element>, either collapsed or expanded, depending on the amount of content.  </p><p>For sorting, filtering, or secondary navigation, use tabs or other components directly in the pane.</p>

Large web browser with a small navigation area on the leading edge with 1 pane filling the rest of the window.

<ol class="decimal"><li><p>Collapsed navigation area</p></li><li><p>Single-pane layout</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41w5ix-02.png?alt=media

<p>An expanded navigation rail is best suited for extra-large windows, where there's still plenty of room for content. Consider collapsing the navigation rail when space is needed, or when on pages deeper in the page hierarchy.</p>

Extra-large web browser with an expanded navigation area and 1 pane filling the rest of the window.

<ol class="decimal"><li><p>Expanded navigation area</p></li><li><p>Single-pane layout</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41xhwl-03.png?alt=media

<h2>Panes</h2>

<p>A two-pane layout is often best for large and extra-large breakpoints.   </p><p>However, a single-pane layout can work when displaying visually- or information-dense content, such as videos.</p>

The single pane covers most of a large screen except for the navigation area and margins.

<p>Only use a single-pane layout for dense content or media</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41y2za-04.png?alt=media

<p>When using a <a href="/m3/pages/scaffold/panes#92371c3b-587d-4c6f-8105-05b69dcec81a" target="_self">fixed-and-flexible</a> layout, the fixed pane should have a width of 412dp by default. </p>

A 2-pane layout with 1 pane fixed at 412dp.

<p>Fixed panes should be 412dp in large and extra-large layouts</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41yyza-05.png?alt=media

<p>When using a <a href="/m3/pages/scaffold/panes#dc7982b7-754c-410a-9e88-18a54557c87b" target="_self">split-pane layout</a>, the spacer should be visually centered by default, even when using an expanded navigation rail. </p>

An expanded nav rail and the first pane take up 50% of the window, and the second pane takes up 50%. 

<p>In split-pane layouts, navigation components shrink the leading pane, so the spacer remains centered</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp41zo3h-06.png?alt=media

<h2>Additional panes</h2>

<p>The extra-large breakpoint supports using a <app-froala-tooltip-element description="Standard side sheets display content without blocking access to the screen’s primary content, such as an audio player at the side of a music app. They're often used in medium and expanded window sizes like tablet or desktop. " link-label="More on side sheets" link-url="/m3/pages/side-sheets/overview" should-open-link-in-new-tab="true">standard side sheet</app-froala-tooltip-element> as a third pane. When the side sheet is present, the navigation rail can remain visible, collapse, or hide completely. Don't use more than three panes.   </p><p>Note: Fixed panes in this window size are recommended to be 412dp, but side sheets have a default maximum width of 400dp. </p>

Extra-large window with 2 panes and a side sheet acting as a third pane.

<ol class="decimal"><li><p>Standard side sheet (third pane)</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp420iqc-07.png?alt=media

<h2>Spacing</h2>

<p>Large and extra-large layouts have a leading and trailing margin of 24dp.</p><p>The <app-froala-tooltip-element description="A spacer is the space between two panes. If panes can be resized, the spacer contains a drag handle." link-label link-url should-open-link-in-new-tab="false">spacer</app-froala-tooltip-element> between panes is 24dp.</p>

2 pane layout with 24dp margins and 24dp space between panes.

<p>Use 24dp for margins and spacers in large and extra-large layouts</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp5lfdh0-08.png?alt=media

<h2>Special considerations</h2>

<p>Large and extra-large layouts will need to transition dynamically to a smaller layout when:</p><ul><li><p>The app goes from full-screen to split-screen</p></li><li><p>Multi-window mode is initiated</p></li><li><p>A free-form window is resized</p></li></ul><p>Pay attention to typographic elements such as line length to ensure readability on large and extra-large layouts.</p>

An email app with 2 panes in a large layout.

<p>Consider how a large layout should change at smaller breakpoints</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp42206a-09.png?alt=media
