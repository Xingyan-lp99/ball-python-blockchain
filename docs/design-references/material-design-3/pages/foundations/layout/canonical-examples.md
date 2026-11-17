# Canonical layout examples

Source: https://m3.material.io/foundations/layout/canonical-examples
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/23b84814-755b-469b-83a9-771fe027b0c0.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Canonical layout examples are designs for common screen layouts across all breakpoints

## Overview

<p>Canonical layout examples demonstrate how to implement the layout <app-froala-tooltip-element description="A scaffold is a fundamental UI design structure that provides a standard platform for assembling key screen components." link-label="More on scaffold" link-url="/m3/pages/scaffold" should-open-link-in-new-tab="true">scaffold</app-froala-tooltip-element>. They’re also available in code to provide a strong starting point for your product.</p><p>Each layout example considers common use cases and components to address expectations and user needs for how products adapt across <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element> (previously window size classes).</p>

A messaging app on desktop mapping bar, rail, and pane regions.

<p>A layout scaffold can include bar, rail, and pane regions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp72kkvb-LD%20adapt%20C.png?alt=media

<h2>Availability &amp; resources</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Type</p></th><th><p>Resource</p></th><th><p>Status</p></th></tr></thead><tbody><tr><th style="width:18.1491%"><p>Design</p></th><td><p><a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">M3 Design Kit (Figma)</a></p></td><td><p>Available</p></td></tr><tr><th rowspan="3" style="width:18.1491%"><p>Implementation</p></th><td><p><a href="https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts" target="_blank">Jetpack Compose: Canonical layouts</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://github.com/android/user-interface-samples/tree/main/CanonicalLayouts" target="_blank">Android Views (MDC-Android): Canonical layouts</a></p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Examples</h2>

<p>There are three canonical layout examples: feed, list-detail, and supporting pane. Each example has configurations for compact, medium, and expanded breakpoints.</p><p>Use these canonical examples as a starting point to create layouts for a product.</p>

<h3>Feed</h3><p>Use a feed layout to arrange elements like cards in a configurable grid for a quick, convenient view of a large amount of content.  </p><p><a href="/m3/pages/canonical-examples/feed/" target="_self">More on feed layouts</a></p>

A course list in a feed layout at a medium breakpoint. 8 cards in a single pane, with bar above and leading rail.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp72yab6-Feed%20adapt%20B.png?alt=media

<h3>List-detail</h3><p>Use a list-detail layout to display explorable lists of items alongside each item’s details. This layout divides the window into two side-by-side panes.</p><p><a href="/m3/pages/canonical-examples/list-detail/" target="_self">More on list-detail layouts</a></p>

List-detail layout of a messaging app. Pane 1 lists all conversations. Pane 2 shows the selected message.

<p></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp72ypkq-LD%20adapt%20B.png?alt=media

<h3>Supporting pane</h3><p>Use a supporting pane layout to organize content into primary and secondary sections:</p><ul><li><p>Primary display area: Contains the main content and occupies the majority of the window (typically about two-thirds)</p></li><li><p>Secondary display area: Presents supporting content in a panel that takes up the remainder of the space</p></li></ul><p><a href="/m3/pages/canonical-examples/supporting-pane/" target="_self">More on supporting pane layouts</a></p>

Supporting pane layout. The primary pane shows course details. The  secondary pane lists “Lessons in this course”.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp72z1no-SP%20adapt%20B.png?alt=media

<h2>Advanced custom layouts</h2><p>To create a custom layout, build on top of canonical layouts or layer <app-froala-tooltip-element description="A scaffold is a fundamental UI design structure that provides a standard platform for assembling key screen components." link-label="More on scaffold" link-url="/m3/pages/scaffold" should-open-link-in-new-tab="true">scaffold</app-froala-tooltip-element> elements.</p>

<h3>Layering</h3><p>Use the <a href="/m3/pages/scaffold/panes#96bf71b8-04b8-4fff-97c7-9bc782fbf401" target="_blank">levitate</a> adaptive strategy to create a layered layout. Layering panes above other content can create a focused, task-oriented experience such as:</p><ul><li><p>Reviewing a shopping basket</p></li><li><p>Responding to comments</p></li><li><p>Creating a calendar event</p></li></ul>

Custom layout. A shopping basket floats above a clothing product page.

<p>Layering panes helps people focus on a specific task</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp731djr-ACL%20Adapt%20B2.png?alt=media

## Feed

<p>A feed layout uses a grid composition to enable quick content browsing and discovery. Key use cases include news, photos, and social media.</p>

Education app using a feed layout.

<p>Feed layouts help people quickly browse and discover content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp736am6-Feed%20adapt%20hero.png?alt=media

<h2>Usage</h2>

<p><span style="white-space:pre-wrap">Use a feed layout to show different pieces of content through cards and lists.<br /><br />Feeds support displays of almost any size as grids can adapt from single to multi-column.<br /></span></p>

An education app has 2 columns on mobile, and 4 columns on a tablet.

<p>Feed layouts can adapt the number of columns across breakpoints</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp51zufq-02.png?alt=media

<h2><span style="white-space:pre-wrap">Dividing space</span></h2>

<p><span style="white-space:pre-wrap">A feed composition is flexible enough to allow for content with varying proportions and sizing.<br /></span></p>

Feed layout in a medium window with 2 panes. 1 pane has 2 columns of small cards and the other has 1 large card.

<p>Feeds can organize content of different sizes, like using small and large cards</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp521zfz-03.png?alt=media

<p>Use size and position to establish relationships among content elements.  </p><p>Feed items should reflow when the amount of available space changes like:</p><ul><li><p>Rotating or unfolding a device</p></li><li><p>Entering multi-window mode</p></li></ul><p>The order of items is determined by their position.   </p><p><a href="/m3/pages/cards/guidelines#99e8d17d-5bde-4bb9-8784-0ca403325b10" target="_blank">More on adaptive design for cards</a></p><p></p>

Lead article image is prominent in a 2-pane news feed.

<p>Feed items can change size to group content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp528i2s-04.png?alt=media

<h2>Across breakpoints</h2>

<h3>Compact</h3><p>A feed layout should stack vertically, like a list of cards with individual items filling the width of the pane.</p>

Cards in 2 feed layouts, compact and expanded.

<p>In compact windows, the cards in a feed stack vertically, filling the full width: </p><ol class="decimal"><li><p>Compact breakpoint</p></li><li><p>Expanded breakpoint</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp52hmfv-05.png?alt=media

<h3>Medium</h3><p>A feed layout can support components with different widths and be split across multiple columns.</p>

In a medium window, 4 equal-width columns of cards in a feed layout.

<p>Feed layouts can add columns in a medium window</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp52jmhc-06.png?alt=media

<h3>Expanded, large, &amp; extra-large</h3><p>A feed layout can support components with different widths and be split across multiple columns. The number of columns should usually increase at expanded breakpoints.</p>

Expanded window has wider columns than a compact window.

<p>Column width can increase at larger breakpoints</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp52lhar-07.png?alt=media

## List-detail

<p>Many layouts can be split into a list view and a detail view.</p><p>Key use cases for this layout include parent-child pairings of information like:</p><ul><li><p>Text message + conversation</p></li><li><p>File browser + open folder</p></li><li><p>Musical artist + album detail</p></li><li><p>Settings + category detail</p></li><li><p>Email inbox + selected email</p></li></ul>

An email app in a list-detail layout at a medium breakpoint.

<ol><li><span style="white-space:pre-wrap">List </span></li><li><span style="white-space:pre-wrap">Detail</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp7394ub-LD%20adapt%20C.png?alt=media

<h2>Usage</h2>

<p>Use the list-detail layout for quickly accessing details of an item from a long list of content.  </p><p>Examples include: </p><ul><li><p>Showing a series of conversations and a text message</p></li><li><p>Browsing files and seeing their details</p></li><li><p>Browsing multiple albums and seeing individual track information</p></li></ul>

Several stacked cards make up the list area on the left pane, while the detail area is a single section on the right pane.

<p>Simplified diagram of:</p><ol class="decimal"><li><p>List area</p></li><li><p>Detail area</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp52v68p-02.png?alt=media

<h3>Dividing space</h3>

Compact windows have 1 pane, while medium and expanded windows can have 2 panes for list-detailed views.

<p>The most basic list-detail views for compact, medium, and expanded layouts</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp52wfuu-03.png?alt=media

<p>A list-detail layout uses two panes.  Depending on the breakpoint, the two panes may appear together in the same layout or across separate layouts.  </p><p>List-detail layouts use the same pane guidance as all single and two-pane layouts, including special behavior for foldables.</p>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p><strong>Breakpoint (dp)</strong></p></th><th><p><strong>Visible panes</strong></p></th></tr></thead><tbody><tr><th style="width:50%"><p>Compact (0-599)</p></th><td><p>1 pane</p></td></tr><tr><th style="width:50%"><p>Medium (600-839)</p></th><td><p>1 (recommended) or 2 panes</p></td></tr><tr><th style="width:50%"><p>Expanded (840+)</p></th><td><p>2 panes</p></td></tr><tr><th style="width:50%"><p>Large (1200-1599)</p></th><td><p>2 panes</p></td></tr><tr><th style="width:50%"><p>Extra-large (1600+)</p></th><td><p>2 panes</p></td></tr></tbody></table></div>

<h2>Across breakpoints</h2>

<h3>Compact</h3><ul><li><p>Use a single-pane layout</p></li><li><p>Only one view is visible at a time, either list or detail</p></li></ul>

Single-pane layout on 3 devices at compact breakpoints.

<ol class="decimal"><li><p>Phone in portrait orientation</p></li><li><p>Closed foldable</p></li><li><p>Tablet in split-screen mode</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp533vzf-04.png?alt=media

<h3>Medium</h3><ul><li><p>Use a single-pane layout for information-dense content or deep focus</p></li></ul>

Single-pane layout on a foldable open flat and a tablet in portrait orientation.

<ol class="decimal"><li><p>Foldable open flat</p></li><li><p>Tablet in portrait orientation</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp535cbt-05.png?alt=media

<ul><li><p>Use a two-pane layout to browse collections and switch between items quickly</p></li><li><p>To maximize horizontal space for two-pane layouts, use a bottom <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/google-material-3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element> or modal <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/google-material-3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element></p></li></ul>

2-pane layout on a foldable open flat and a tablet in portrait orientation.

<ol class="decimal"><li><p>Foldable open flat</p></li><li><p>Tablet in portrait orientation</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp537scf-06.png?alt=media

<h3>Expanded, large, &amp; extra-large</h3><ul><li><p>Use a two-pane layout</p></li></ul>

2-pane layout on a phone and tablet, both in landscape orientation.

<ol><li><span style="white-space:pre-wrap">Phone in landscape orientation</span></li><li><span style="white-space:pre-wrap">Tablet in landscape orientation</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp538uu5-07.png?alt=media

<h2><span style="white-space:pre-wrap">Behavior</span></h2>

<h3>Single vs two-pane</h3><ul><li><p>Back button: Appears in detail view only for single-pane layouts</p></li><li><p>Selected state: Appears only in list view for two-pane layouts</p></li><li><p>Visual focus: Use <a href="/m3/pages/grids-spacing/spacing#e7e6d1ac-031a-4757-afcf-b223f23654ea" target="_blank">explicit and implicit grouping</a> to direct focus in two-pane layouts</p></li></ul>

A 2-pane layout shows a selected list item. A single-pane layout uses a Back button to return to the list.

<ol class="decimal"><li><p>Use a selection state in two-pane layouts only</p></li><li><p>Use a back button in single-pane layouts only</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp53b085-08.png?alt=media

<h3>Transitioning between layouts</h3><p>The amount of available space is dynamic and changes based on how someone uses a device, such as rotating or unfolding it, or entering multi-window mode.</p>

Device rotating from landscape to portrait mode, reducing layout panes from 2 to 1.

<p>A two-pane layout adapts to a single-pane layout when a device rotates from an expanded to medium breakpoint</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp53duna-lxygxf8i-Canonical_List-Detail_1.mp4?alt=media

<h4>No selected list item</h4><p>A single-pane layout shows a list view, while a two-pane layout shows placeholder content in the detail pane.</p><p>In some cases, such as multi-select, the most recently used pane should stay visible when switching to single-pane layout.</p>

No item selected on a folded device. When unfolded, the detail pane is empty.

<p>If no item is selected when a foldable opens, the detail pane displays an empty state</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxyh497r-Canonical_List-Detail_2.mp4?alt=media

<h4>Selected list item</h4><p>When switching from a single- to two-pane layout, both panes should be shown and the selected item’s details are visible.</p><p>When going from a two- to single-pane layout, the view depends on the product:</p><ul><li><p>The detail pane should typically show in a single-pane layout, and an app bar appears</p></li><li><p>If the product supports selection without deep navigation, like multi-select, the list view can show with the item selected</p></li><li><p>Consistency is key: If a layout showed the list view previously, it should return to that view when returning to a single pane</p></li></ul>

Item selected on a folded device. When unfolded, the detail view shows the item.

<p>If an item is selected when a foldable opens, the detail pane shows that item</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp54burn-lxyh80t8-Canonical_List-Detail_3.mp4?alt=media

Item selected on an unfolded device. When folded, only the detail view shows.

<p>When a foldable closes with an item selected, the single pane shows the detail view</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxyhcqmk-Canonical_List-Detail_4.mp4?alt=media

<h4>Persistent states</h4><p>In most cases, a state should be saved when navigating between detail views. This includes read and unread content.</p>

Scroll position is kept after folding or unfolding the device.

<p>Detail views should retain their scroll position when navigating to other items</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp54fy4m-lxyhgczm-Canonical_List-Detail_5.mp4?alt=media

## Supporting pane

<p>The supporting pane layout organizes content into primary and secondary areas.   </p><p>The primary area contains the main content and occupies the majority of the space. The secondary area contains supporting content.  </p><p>Key use cases for supporting pane layouts include:</p><ul><li><p>Productivity</p></li><li><p>Document editing and commenting</p></li><li><p>Content and media browsing</p></li></ul>

A video app has the main content in the primary area and “up next” content is listed in the secondary area.

<p>Supporting pane layouts organize content into primary and secondary areas</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp54jbnh-01.png?alt=media

<h2><span style="white-space:pre-wrap">Usage</span></h2>

<p>Use the supporting pane layout when the secondary content is only meaningful in relation to the primary content.   </p><p>For content with a parent-child relationship, use a <a href="/m3/pages/canonical-layouts/list-detail/" target="_blank">list-detail layout</a> instead.</p>

The supporting pane has vertically stacked cards.

<p>Supporting panes provide contextual info for the primary area</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp54n3m1-02.png?alt=media

<h2><span style="white-space:pre-wrap">Dividing space</span></h2>

<p>The window is divided between a focus pane and a supporting pane.  </p><p>Depending on the breakpoint, the supporting pane may appear below or beside the focus pane.</p>

The cards of a supporting pane scroll horizontally across the bottom of the screen.

<p>Supporting panes can appear beside or below the primary area</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp54omgc-03.png?alt=media

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Supporting pane placement</p></th><th><p>Pane width</p></th><th><p>Breakpoint</p></th></tr></thead><tbody><tr><th><p>Below</p></th><td><p>Flexible</p></td><td><p>Compact or Medium</p></td></tr><tr><th><p>Leading or trailing</p></th><td><p>Fixed (360 dp)</p></td><td><p>Expanded</p></td></tr></tbody></table></div>

<h2>Across breakpoints</h2>

<h3>Compact</h3><p>The supporting pane should appear below the focus pane. <br /><br />A bottom sheet can be useful for keeping focus on the primary pane while providing access to supporting information.</p>

2 layouts showing  bottom sheets at a compact breakpoint.

<p>Bottom sheets can provide supporting information in compact windows</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp73c5cw-04.png?alt=media

<h3>Medium</h3><p>The supporting pane should appear below the focus pane.</p>

3 cards in a supporting pane are horizontal across the bottom of a tablet.

<p>Supporting panes appear below the focus pane in medium windows</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp54tfu7-05.png?alt=media

<h3>Expanded</h3><p>The supporting pane should appear on the leading or trailing side of the focus pane.</p>

The supporting pane is to the right of the primary focus pane on 2 screens.

<p>Supporting panes appear beside the focus pane in expanded windows</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp73dr78-6.png?alt=media
