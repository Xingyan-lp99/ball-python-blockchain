# Design for desktop

Source: https://m3.material.io/foundations/desktop
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/26e4a646-c6c2-4d82-9be7-6bff035b0006.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Create desktop experiences with adaptive layouts and multiple inputs

## Overview

<ul type="disc" style="list-style-type:disc"><li><p>People can use any Android app in a desktop environment by opening it on a Chromebook or Googlebook, docking a tablet to a folio, or connecting a phone to an external monitor</p></li><li><p>Design apps so they’re easy to use on desktop, rather than feeling like a stretched mobile app</p></li><li><p>Take advantage of the expanded space and longer viewing distances, and consider denser layouts that show more information at once</p></li><li><p>Use adaptive <a href="/m3/pages/desktop/components" target="_blank">components</a> and <a href="/m3/pages/layout-overview/adaptive-design" target="_blank">layouts</a> so apps scale smoothly across <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element></p></li><li><p>Support external devices for efficient navigation across every input type, including mice, trackpads, and physical keyboards</p></li></ul>

<h2>Availability &amp; resources</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><tbody><tr><th style="width:26.1529%"><p>Type</p></th><th style="width:50.9018%"><p>Resource</p></th><th style="width:22.8825%"><p>Status</p></th></tr><tr><th rowspan="3" style="width:26.1529%"><p>Design</p></th><td><p><a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">M3 Design Kit</a> (Figma)</p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://developer.android.com/design/ui/desktop" target="_blank">Android design guidelines</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="/m3/pages/layout-overview/overview" target="_blank">Material layout guidelines</a></p></td><td><p>Available</p></td></tr><tr><th rowspan="3" style="width:26.1529%"><p>Implementation</p></th><td><p><a href="https://developer.android.com/guide/topics/large-screens" target="_blank">Android large screen dev docs</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://developer.android.com/jetpack/androidx/releases/compose-material3" target="_blank">Jetpack Compose</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://developer.android.com/develop/adaptive-apps/guides/mediaquery" target="_blank">Android media query API</a></p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Design principles</h2>

<h3>Adaptive from the start</h3><p>Adapting an app to the desktop experience shouldn’t be an afterthought. Design an app's layout and information hierarchy in a flexible and modular way, so it can seamlessly adapt from mobile to a larger screen.</p><p><a href="/m3/pages/layout-overview/adaptive-design" target="_blank">More on adaptive design</a></p>

4 devices: tablet, mobile, laptop, and desktop.

<p>Design layouts to adapt seamlessly from mobile to expanded windows</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvpre9e5-01_VQA.png?alt=media

<h3>More screen, more done</h3><p>Use the expanded window to show more information in a denser layout. Don’t simply scale elements to fill empty space.<br /><br /><a href="/m3/pages/desktop/layout" target="_blank">More on desktop layouts</a></p>

Desktop document editor showing full-page text beside an open comments side panel in a single expanded window.

<p>On desktop, use dense layouts to take advantage of the large screen</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvprefje-02_VQA.png?alt=media

<h3>Refine the motion</h3><p>Desktop transitions can be faster with small elements and short distances because the screen is unobstructed. When moving large elements across long distances, slow down or simplify transitions to prevent visual overwhelm.</p>

In mobile and desktop email views, a navigation rail collapses and expands at different speeds.

<p>Motion duration should adjust based on distance and element size</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvjpxskt-GM3%20-%20Desktop%20-%20Overview%20-%20Refine%20motion%20-%20IA%20-%20v06.mp4?alt=media

<h3>Multitasking at the core</h3><p>People expect to work on more than one thing at a time on desktop. While the multi-window OS supports working across apps, allow people to multitask within an app too.</p>

Overlapping desktop windows showing a multi-pane email app and a video playing in the left corner.

<p>In-app panels and multi-window views support concurrent workflows</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvpremlj-04%20-%20static_VQA.png?alt=media

<h3>Balance efficiency with simplicity</h3><p>While mobile design focuses on simplicity, people expect to accomplish more in fewer steps on desktop.</p><p>Balance shorter task flows with clear layouts to avoid overwhelming people with information.</p>

Desktop photo app with a collapsed navigation rail,  organized multi-column image grid in the primary pane, and item details in a supporting pane.

<p>Desktop workflows should balance density with visual clarity</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvpretu4-05_VQA.png?alt=media

<h3>All input types are equally important</h3><p>People frequently switch between touch, pointer, and physical keyboard inputs while on desktop. Support pointer and keyboard interactions to ensure efficient navigation across every input type.<br /><br /><a href="/m3/pages/desktop/interaction" target="_blank">More on desktop interactions</a></p>

3 inputs: hands using touch on a screen, typing on a physical keyboard, and controlling a mouse.

<p>Support all input types, including touch, keyboard, and pointer</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvprf1h8-06_VQA.png?alt=media

## Layout

<h2>Adaptive desktop layouts</h2>

<p>Desktop apps typically open at medium or large <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element> and can expand to extra-large. The quality bar is higher because of the larger window sizes and people’s expectation for greater information density. Make sure the app makes good use of the expanded space.<br /><br />Use these guidelines to scale a mobile app to a desktop layout.</p>

<h3>Use adaptive pane layouts</h3><p>Consider using multi-column or multi-pane layouts for <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element>, <app-froala-tooltip-element description="Window widths 1200dp to 1599dp, such as desktop." link-label="More on large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">large</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Window widths 1600dp and larger, such as ultra-wide monitors." link-label="More on extra-large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">extra-large breakpoints</app-froala-tooltip-element> to show more content at once.</p><p>If keeping a single pane on desktop, cap and center the content width to avoid looking like a stretched phone UI.</p><p><a href="/m3/pages/scaffold/panes" target="_blank">More on pane layouts</a></p>

A mobile app shown on desktop is capped and centered on the screen.

<p>Cap and center content in single-pane layouts to avoid stretched views</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvprmd1n-01.png?alt=media

<h3>Consider navigation &amp; usability</h3><p>Start with Material canonical layouts to automatically adapt mobile layouts to fill the available space on desktop. These make app navigation simple and predictable:</p><ul type="disc" style="list-style-type:disc"><li><p><a href="/m3/pages/canonical-examples/feed" target="_blank">Feed</a>: For long scrolling pages of content</p></li><li><p><a href="/m3/pages/canonical-examples/list-detail" target="_blank">List-detail</a>: For selecting and opening an item, like chat or email</p></li><li><p><a href="/m3/pages/canonical-examples/supporting-pane" target="_blank">Supporting pane</a>: For showing additional tools or supporting information</p></li></ul><p><a href="/m3/pages/canonical-examples/overview" target="_blank">More canonical layout examples</a></p>

A desktop app has an expanded navigation rail and a supporting pane with a list of “Lessons in this course.”

<p>Add columns or panes to support faster navigation and richer workflows</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvprmjek-02.png?alt=media

<h3>Adapt components</h3><p>Material components can adapt their layout across breakpoints to optimize space and support mouse and keyboard inputs.</p><p>For example, at medium and larger breakpoints, changing the <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element> to a <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element> gives more vertical space to the content.</p><p><a href="/m3/pages/desktop/components" target="_blank">More on adapting components for desktop</a></p>

A clock timer mobile UI has a navigation bar which switches to a navigation rail on a tablet. 

<p>A navigation bar on mobile should adapt to a navigation rail in larger windows</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvprmpsb-03_VQA.png?alt=media

## Components

<h2>Adapt components for desktop experiences</h2><p>Components like <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rails</app-froala-tooltip-element>, <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menus</app-froala-tooltip-element>, <app-froala-tooltip-element description="Side sheets show secondary content anchored to the side of the screen." link-label="More on side sheets" link-url="/m3/pages/side-sheets/overview" should-open-link-in-new-tab="true">side sheets</app-froala-tooltip-element>, <app-froala-tooltip-element description="Dialogs provide important prompts in a user flow." link-label="More on dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">dialogs</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Carousels show a collection of items that can be scrolled on and off the screen." link-label="More on carousels" link-url="/m3/pages/carousel/overview" should-open-link-in-new-tab="true">carousels</app-froala-tooltip-element> are optimized for larger screens and desktop inputs.</p>

<h3>Don’t overstretch components</h3><p>While full-width <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element> and <app-froala-tooltip-element description="Text fields let users enter text into a UI." link-label="More on text fields" link-url="/m3/pages/text-fields/overview" should-open-link-in-new-tab="true">text fields</app-froala-tooltip-element> work well on mobile, they can feel imprecise on large screens. On desktop, maintain default component widths and padding, and don’t stretch these components to fill the pane.</p>

<h3>Use navigation rails</h3><p>If a mobile app uses a <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element>, switch to a navigation rail at <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium breakpoints</app-froala-tooltip-element> and above.   </p><p>At <app-froala-tooltip-element description="Window widths 1600dp and larger, such as ultra-wide monitors." link-label="More on extra-large breakpoints" link-url="/m3/pages/breakpoints/large-extra-large" should-open-link-in-new-tab="true">extra-large breakpoints</app-froala-tooltip-element>, consider expanding the navigation rail by default to improve label readability.</p>

A collapsed navigation rail in a clock app expands and shows more menu items.

<p>Use navigation rails at medium breakpoints and above, and consider expanding them by default at extra-large breakpoints</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvjtxssk-GM3_Expressive_Nav-Rail_Guidelines_27_IA_V07.mp4?alt=media

<h3>Replace bottom sheets</h3><p>On mobile, <app-froala-tooltip-element description="Bottom sheets show secondary content anchored to the bottom of the screen." link-label="More on bottom sheets" link-url="/m3/pages/bottom-sheets/overview" should-open-link-in-new-tab="true">bottom sheets</app-froala-tooltip-element> are easy to reach, and their attachment to the device edge and scrim creates an immersive view.</p><p>However, on desktop, bottom sheets often require excessive cursor travel and can obstruct primary content. For an improved desktop experience, consider replacing bottom sheets with:</p><ul type="disc" style="list-style-type:disc"><li><p>Context menus</p></li><li><p>Side sheets</p></li><li><p>Dialogs</p></li></ul><p>If using a bottom sheet on desktop, it must be detached from the bottom edge of the window. </p>

Mobile map UI with a bottom sheet anchored to the bottom edge with 6 actions.

<p>Bottom sheets provide an easy-to-reach view on mobile devices</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvjtyb09-03.png?alt=media

<h4>Context menus</h4><p>Use right-click <app-froala-tooltip-element description="Context menus provide actions for a specific element, like an image or highlighted text, and usually open with a secondary click." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">context menus</app-froala-tooltip-element> when replacing bottom sheets triggered by press-and-hold or overflow actions on mobile.</p>

Satellite map on desktop with a context menu with 5 actions next to a pointer cursor.

<p>Replace press-and-hold bottom sheets with right-click context menus on desktop</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvl2iup2-04.png?alt=media

<h4>Side sheets</h4><p>Use a <app-froala-tooltip-element description="Side sheets show secondary content anchored to the side of the screen." link-label="More on side sheets" link-url="/m3/pages/side-sheets/overview" should-open-link-in-new-tab="true">side sheet</app-froala-tooltip-element> with no scrim to show complex tools or configuration panels on desktop without obstructing the main content.</p>

Satellite map on desktop with a side sheet with 6 location options.

<p>On desktop, use side sheets to display tools or configuration panels alongside the main content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvl2j87m-05.png?alt=media

<h4>Dialogs</h4><p>Use a <app-froala-tooltip-element description="Dialogs provide important prompts in a user flow." link-label="More on dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">dialog</app-froala-tooltip-element> when replacing modal bottom sheets that require a decision, since attention on desktop is focused higher on the screen.</p>

Satellite map on desktop with a centered dialog displaying pin coordinates and 2 action buttons.

<p>On desktop, use a dialog to keep important decisions in the person's line of sight</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvl2jobv-06.png?alt=media

<h3>Ensure carousels work with desktop inputs</h3><p>For better cursor and keyboard interaction control, <app-froala-tooltip-element description="Carousels show a collection of items that can be scrolled on and off the screen." link-label="More on carousels" link-url="/m3/pages/carousel/overview" should-open-link-in-new-tab="true">carousels</app-froala-tooltip-element> can display direct targets for navigation when <app-froala-tooltip-element description="A hover state communicates when a user has placed a cursor above an interactive element." link-label="More on hover state" link-url="/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844" should-open-link-in-new-tab="true">hovered</app-froala-tooltip-element>. <br /><br />Only hero carousels have built-in next and previous actions. If adding these buttons to other carousels, they should appear when the carousel is hovered or focused. <br /><br />Consider adding a <strong>Show all</strong> button near the carousel to give people a persistent way to view all items.</p>

Photo carousel on desktop that scrolls horizontally. When a pointer hovers on it, previous and next buttons appear at the leading and trailing edges.


<p>When hovered, a multi-browse carousel can show next and previous buttons</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvju3y1g-GM3-%20Desktop%20-%20Components%20-%20Carousel%20-%20IA%20-%20V02.mp4?alt=media

<p>Hero and full-screen carousels can also include pagination dots for quicker navigation. <br /><br /></p>

Photo carousel on desktop with a hero-centered item and dot pagination showing 5 total items. 

<p>A hero-centered carousel can show dot pagination</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvju2q8t-08.png?alt=media

<h4>Scrolling carousels on desktop</h4><p class="body-large">People can use a mouse wheel to scroll vertical hero carousels, or hold <strong>Shift</strong> to scroll horizontal carousels. On touchpad, people can scroll using a two-finger swipe. A single-pointer alternative is also required.  </p>

## Interaction

<h2>Support desktop interactions &amp; inputs</h2><p>People navigate desktop apps using touch, pointer devices, and physical keyboards. To make sure interactions like drag and drop, zoom, and refresh work across inputs:</p><ul type="disc" style="list-style-type:disc"><li><p>Provide single-click controls</p></li><li><p>Support keyboard shortcuts</p></li><li><p>Show clear hover and focus states</p></li></ul>

<h2>Drag &amp; drop</h2><p>Drag and drop allows people to quickly move or copy files, text, <app-froala-tooltip-element description="Cards display content and actions about a single subject." link-label="More on cards" link-url="/m3/pages/cards/overview" should-open-link-in-new-tab="true">cards</app-froala-tooltip-element>, <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> items, or <app-froala-tooltip-element description="Input chips represent discrete pieces of information entered by a user, such as Gmail contacts or filter options within a search field." link-label="More on input chips" link-url="/m3/pages/chips/overview" should-open-link-in-new-tab="true">input chips</app-froala-tooltip-element>.</p>

<h3>Provide clear visual feedback</h3><p>Use Material <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">states</app-froala-tooltip-element> to give clear feedback throughout a drag-and-drop interaction:</p><ul type="disc" style="list-style-type:disc"><li><p>When dragging starts, apply the <app-froala-tooltip-element description="A dragged state communicates when a user presses and moves an element." link-label="More on dragged state" link-url="/m3/pages/interaction-states/applying-states#c97582c4-5fef-42ce-9c34-71f8dcc5b8ad" should-open-link-in-new-tab="true">dragged state</app-froala-tooltip-element> and <app-froala-tooltip-element description="Elevation is the distance between two surfaces on the z-axis." link-label="More on elevation" link-url="/m3/pages/elevation/overview" should-open-link-in-new-tab="true">elevation</app-froala-tooltip-element> to create depth and focus</p></li><li><p>Make the dragged item translucent so drop targets are visible beneath it</p></li><li><p>Highlight valid drop targets with a border or insertion point when an item hovers above them</p></li></ul><p>All drag-and-drop actions should include a single-click alternative, like a + <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon button</app-froala-tooltip-element> that opens a <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element> to upload an image without dragging.</p>

Laptop with photo and chat apps open. A hand cursor drags a semi-transparent photo tile into the chat attachment field.

<p>Represent dragged items with translucent images to keep drop targets visible</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvps4r9t-01_VQA.png?alt=media

<h3>Show clear error states</h3><p>Display a prohibitive cursor symbol when hovering over invalid drop targets. </p><p>If an item is dropped where the action can't be completed, it should return to its original location or visually dissolve. </p>

A cursor with a red blocked badge drags a photo tile over a read-only pane in a desktop photo app.

<p>Display a prohibitive cursor symbol over invalid drop targets</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvps8nfj-02.png?alt=media

<h3>Make pointer dragging instant</h3><p>Pointer dragging should be instantaneous, unlike touch interactions that often require a long press.</p>

On a laptop, a clock app time is dragged and dropped instantly into a new location, compared to a long press on mobile. 

<p>Pointer drag interactions should be performed instantly</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvjutkyl-GM3%20-%20Desktop%20-%20Interaction%20-%20Pointer%20efficientcy%20-%20IA%20-v05.mp4?alt=media

<h2>Zooming &amp; panning</h2><p>Support zooming and panning across pointer, keyboard, and touch inputs so people can efficiently navigate large-scale content. </p>

<h3>Provide multiple ways to zoom</h3><p>On desktop, people should be able to zoom with keyboard shortcuts, scroll actions, and touch gestures:</p><ul type="disc" style="list-style-type:disc"><li><p>Zoom-first content: Scroll to zoom in and out on a map</p></li><li><p>Pan-first content: Hold <strong>Control</strong> or <strong>Cmd</strong> while scrolling a canvas</p></li><li><p>Single-pointer control: Include dedicated + and - icon buttons</p></li><li><p>Touchpads: Support a two-finger pinch-to-zoom gesture</p></li></ul>

Satellite map window with a location card, and trailing zoom + and - icon buttons.

<p>Include dedicated <strong>+</strong> and <strong>-</strong> buttons as an accessible single-pointer zoom alternative</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvps8wx6-04.png?alt=media

<h3>Adapt panning interactions</h3><p>For zoom-first content, people should be able to pan by clicking and dragging with a mouse or touchpad once zoomed in.</p><p>For pan-first content, people should be able to pan by:</p><ul type="disc" style="list-style-type:disc"><li><p>Scrolling vertically, or holding <strong>Shift</strong> and scrolling horizontally</p></li><li><p>Swiping with two fingers on a touchpad</p></li></ul>

Satellite map window showing a pointer over alpine terrain. The map is zoomed in then pans. 

<p>People should be able to swipe, scroll, or click and drag to pan zoomed-in content</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvjv5650-GM3%20-%20Desktop%20-%20Interaction%20-%20Panning%20-%20IA%20-v02.mp4?alt=media

<h2>Secondary actions</h2><p>To save screen space and reduce visual complexity on desktop, consider hiding secondary actions and revealing them only when necessary.</p>

<h3>Use context menus</h3><p>A <app-froala-tooltip-element description="Context menus provide actions for a specific element, like an image or highlighted text, and usually open with a secondary click." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">context menu</app-froala-tooltip-element> helps people maintain focus in the main window during element-specific tasks, like copy and paste.</p><p>Context menus should open with a secondary click, a long press, or an overflow icon button.</p>

Satellite map window showing a floating menu of 6 actions beside the pointer and a trailing location card.

<p>Context menus open with a secondary click, a long press, or an overflow icon</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvps9gug-06.png?alt=media

<h3>Reveal actions on hover</h3><p>Secondary actions can also appear when a cursor or stylus hovers over an area. </p><p>Don’t use hover as the only way to access these actions.</p>

On a satellite map, a hand cursor hovers over Tremorgio Lake to reveal a location card with a "Save to atlas" button.

<p>Secondary actions can appear on hover</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvps9nla-07.png?alt=media

<h2>Making multiple selections</h2><p>Multi-select helps people complete bulk actions.</p>

<p>On desktop, people can use the following pointer and keyboard interactions to select multiple items:</p><ul type="disc" style="list-style-type:disc"><li><p>Select one-by-one: <strong>Control</strong> + click. or <strong>Cmd</strong> + click (Mac)</p></li><li><p>Select a range: <strong>Shift</strong> + click</p></li><li><p>Select a group: Click + drag</p></li><li><p>Select all: <strong>Control</strong> + A, or <strong>Cmd</strong> + A (Mac)</p></li></ul>

Desktop journal app with 3 items selected. 

<p>People can select multiple items using <strong>Shift</strong> + click</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvps9ueq-08.png?alt=media

<h2>Refreshing</h2><p>When designing a refresh action, make sure to consider all input types.</p>

<p>On desktop, people can refresh a page by pressing <strong>Control</strong> + R, or <strong>Cmd</strong> + R on Mac.</p><p>Include a dedicated button so people using non-touch pointer devices or assistive technologies can refresh content with a single click.</p>

Browser window showing a course page with a selected reload icon in the search bar.

<p>Include a dedicated button for people to refresh content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmvpsa34l-09.png?alt=media
