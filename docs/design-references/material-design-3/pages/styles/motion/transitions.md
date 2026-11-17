# Transitions

Source: https://m3.material.io/styles/motion/transitions
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/2b9bdc79-df8e-4ad2-bdca-e0a3f083cd33.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Transitions help guide people as they navigate an app

## Transition patterns

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">M3 transitions use the legacy easing and duration system. They'll eventually be updated to use the motion physics system.</div></div></div>

<p id="isPasted">Transitions are short animations that connect individual elements or full-screen views of an app. They are fundamental to a great user experience because they help users understand how an app works. Well-designed transitions makes an experience feel high quality and expressive. They should be the top priority for a strong motion implementation. </p><p>These are six common transition patterns:</p><ol><li><a href="/m3/pages/motion-transitions/transition-patterns#b67cba74-6240-4663-a423-d537b6d21187">Container transform</a></li><li><a href="/m3/pages/motion-transitions/transition-patterns#df9c7d76-1454-47f3-ad1c-268a31f58bad">Forward and backward</a></li><li><a href="/m3/pages/motion-transitions/transition-patterns#8d4ec98f-60dc-47a9-901e-88fa2c43f18a">Lateral</a></li><li><a href="/m3/pages/motion-transitions/transition-patterns#f852afd2-396f-49fd-a265-5f6d96680e16">Top level</a></li><li><a href="/m3/pages/motion-transitions/transition-patterns#e1c2a650-d7a4-4a6d-9025-e6b7845291ed">Enter and exit</a></li><li><a href="/m3/pages/motion-transitions/transition-patterns#b39a0641-1b44-4864-83f5-fac38e0bd94a">Skeleton loaders</a></li></ol>

Small, colorful blobs are animated with different motion styles corresponding to the six transition patterns.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfqbdij-GM3-Transitions-TransitionPatterns-1-v01.mp4?alt=media

<h2>Container transform</h2><p>This pattern is used to seamlessly transform an element to show more detail, like a Card expanding into a details page.</p><ul><li><p><strong>Commonly used with:</strong> Cards, lists, image galleries, search boxes, sheets, FABs, and chips</p></li><li><p><strong>Read more:</strong> <a href="https://material.io/blog/motion-research-container-transform" target="_self">UX Research</a>, <a href="/m3/pages/motion-transitions/applying-transitions#50f9fc3f-c7e2-4099-b614-7c36b1c5285d" target="_blank">Guidelines</a>, <a href="https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md#container-transform" target="_blank">Android implementation</a></p></li></ul>

<p id="isPasted">Persistent elements are used to seamlessly connect the start and end state of the transition. The most common persistent element is a container, which is a shape used to represent an enclosed area. It can also be an important element, like a hero image. Of all transition patterns, this one creates the strongest relationship between elements. It's also perceived to be the most expressive.</p>

Podcast app is selected from home screen, then individual card is selected, both taking over the screen.

A container transform is used when opening an app and a card. This makes the relationship between screens clear and gives an expressive quality to the transition.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfqc556-GM3-Transitions-TransitionPatterns-2-v01.mp4?alt=media

<h4 id="isPasted">Between full-screen views</h4>

1-year memory of flowers is selected within a carousel and takes over screen.

<p>A container transform is used to expand this image to a fullscreen view</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfqdipk-GM3-Transitions-TransitionPatterns-3-1-v01.mp4?alt=media

Individual message is selected in messaging app and expands to view complete message.

<p>A container transform is used to expand this List item to a fullscreen view</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfrbw3w-GM3-Transitions-TransitionPatterns-3-2-v01.mp4?alt=media

Grocery list is selected within notes and expands to take over screen.

<p>A container transform is used to expand this Card and Search box to a fullscreen view</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfrcr6e-GM3-Transitions-TransitionPatterns-3-3-v01.mp4?alt=media

<h4 id="isPasted">Within a screen</h4>

Search box for replies within messaging app expands to reveal recent searches and contacts.

<p>A container transform is used to expand this search box</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfrdrxa-GM3-Transitions-TransitionPatterns-3-4-v01.mp4?alt=media

FAB is selected and expands to reveal  Compose Now action and shortlist of contacts.

<p>This container transform FAB transition has a persistent container and icon</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfrem0q-GM3-Transitions-TransitionPatterns-3-5-v01.mp4?alt=media

Song is selected from banner on bottom of screen and expands to take over.

<p>A container transform is used on an expanding Sheet</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfrf9ld-GM3-Transitions-TransitionPatterns-3-6-v01.mp4?alt=media

<h2 id="isPasted">Forward and backward</h2><p>This pattern is used for navigating between screens at consecutive levels of hierarchy, like navigating from an inbox to a message thread.</p><ul><li><strong>Commonly used with</strong>: Lists, cards, buttons, links</li><li><strong>Read more:</strong> <a href="/m3/pages/motion-transitions/applying-transitions#41b11a78-b88f-4972-904c-880bc348acc8" rel="noopener noreferrer" target="_blank">Guidelines</a>, <a href="https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md#shared-axis" id="isPasted" rel="noopener noreferrer" target="_blank">Android implementation</a></li></ul>

<p id="isPasted">A horizontal sliding motion indicates moving forward or backward between screens. Android and iOS have different default styles:</p><p><strong>1. Android</strong> uses a fade as screens slide. This reduces the amount of motion, since the screens don't have to slide the full width of the device. </p><p><strong>2. </strong><strong>iOS</strong> uses a parallax effect, meaning the background slides slower than the foreground. This also reduces the amount of motion.</p>

Two motions contrasted in messaging app, with top showing Android’s fading movement and bottom showing iOS’s swiftly moving foreground transition.

<ol><li>Android’s default forward and backward transition</li><li>iOS’ default forward and backward transition</li></ol>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfrilua-GM3-Transitions-TransitionPatterns-4-v01.mp4?alt=media

WiFi set-up screen demonstrates Android fade effect when next button is selected.

<p>A filled button on Android uses a forward and backward transition</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfrjhm3-GM3-Transitions-TransitionPatterns-4-1-v01.mp4?alt=media

Music card uses iOS transition to move back to music app.

<p>A card on iOS uses a forward and backward transition</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfrkcfn-GM3-Transitions-TransitionPatterns-4-2-v01.mp4?alt=media

Fading transitions between photos app search bar and selection of Family &amp; friends option.

<p>A search icon button in Android uses a forward and backward transition</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfrldpn-GM3-Transitions-TransitionPatterns-4-3-v01.mp4?alt=media

Email is selected from inbox demonstrating Android transition.

<p>Tapping a list item on a tablet uses a forward and backward transition</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfrmnfg-GM3-Transitions-TransitionPatterns-4-4-v01.mp4?alt=media

<h2 id="isPasted">Lateral</h2><p>This pattern is used for navigating between peer content at the same level of hierarchy, like swiping between tabs of a content library.</p><ul><li><strong>Commonly used with: </strong>Tabs, carousels, and image galleries</li><li><strong>Read more:</strong> <a href="/m3/pages/motion-transitions/applying-transitions#3d5c16ce-7350-4a33-9d2b-598a7591d4e6" rel="noopener noreferrer" target="_blank">Guidelines</a></li></ul>

<p>Lateral transitions use a sliding motion similar to a forward and backward pattern, but it does not use a fade or parallax effect. Instead elements are grouped and slide in unison, creating a strong peer relationship. This also hints at being able to gesturally swipe elements to navigate.</p>

Toggling between tabs for artists and albums in music app reveals lateral movement.

<p>A lateral transition is used when tapping or swiping a Tab component</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfrnslm-GM3-Transitions-TransitionPatterns-5-1-v01.mp4?alt=media

Photos are swiped through horizontally, each filling the screen.

<p>A lateral transition is used when swiping through a photo album</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfroshf-GM3-Transitions-TransitionPatterns-5-2-v01.mp4?alt=media

Carousel is scrolled through horizontally without use of fades.

<p>A lateral transition used with a Carousel component</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfrpmn2-GM3-Transitions-TransitionPatterns-5-3-v01.mp4?alt=media

<h2 id="isPasted">Top level</h2><p>This pattern is used to navigate between top-level destinations of an app, like tapping a destination in a Navigation bar.</p><ul><li><strong>Commonly used with:</strong> Navigation bar, navigation rail, and navigation drawer</li><li><strong>Read more:</strong> <a href="/m3/pages/motion-transitions/applying-transitions#ab8885f6-5517-419d-80de-bea50cd10467" rel="noopener noreferrer" target="_blank">Guidelines</a>, <a href="https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md#fade-through" rel="noopener noreferrer" target="_blank">Android implementation</a></li></ul>

<p>The exiting screen quickly fades out and then the entering screen fades in. Since the content of top level destinations isn't necessarily related, the motion intentionally does not use grouping or persistent elements to create a strong relationship between screens.</p>

Home and Music options in the navigation are toggled between with fading indicating distinctness of items.

<p>A navigation bar uses a top level transition</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfrrw39-GM3-Transitions-TransitionPatterns-6-1-v01.mp4?alt=media

Inbox menu item selected fades to reveal inbox contents.

<p>Tapping an item in a navigation drawer uses a top level transition to move between destinations</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfs0nn2-GM3-Transitions-TransitionPatterns-6-2-v01.mp4?alt=media

Chat and Mail options in navigation both produce swift transitions.

<p>A navigation rail uses a top level transition</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfs1jfp-GM3-Transitions-TransitionPatterns-6-3-v01.mp4?alt=media

<h2 id="isPasted">Enter and exit</h2><p>This pattern is used to introduce or remove a component on the screen. Components can enter and exit within the screen bounds, like a dialog appearing over an app. They can also enter and exit by crossing the screen bounds, like a navigation drawer or bottom sheet that slides on and off screen.</p>

<h3 id="isPasted">Within screen bounds</h3><ul><li><strong>Commonly used with:</strong> FABs, dialogs, menus, snackbars, time pickers and tooltips</li><li><strong id="isPasted">Read more: </strong><a href="/m3/pages/motion-transitions/applying-transitions#56675bd6-5e69-4fa8-b075-d694e8cb3ad4" rel="noopener noreferrer" target="_blank">Guidelines</a></li></ul>

<p id="isPasted"><strong>Android</strong> components expand and collapse along the x or y axis as they enter and exit. Scale and z-axis motion is avoided since they imply elevation change, which doesn't match M3's reduced elevation model.</p><p><strong>iOS</strong> components uniformly scale as they enter and fade out to exit.</p>

Message to permanently delete an email pops up without elevation for both Android and iOS.

<ol><li>Android enter and exit transitions </li><li>iOS enter and exit transitions</li></ol>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfs2znj-GM3-Transitions-TransitionPatterns-7-1-v01.mp4?alt=media

<p>The direction a component enters is informed by their location on screen, expanding away from the device edge. A menu at the top of the screen expands downwards, and a snackbar at the bottom of the screen expands upwards.</p>

Image menu in upper right corner expands downward.

<p>A menu at the top of the screen expands downwards as it enters</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfs4dk9-GM3-Transitions-TransitionPatterns-7-2-v01.mp4?alt=media

A snackbar alert pops up from bottom of inbox screen and FAB emerges from lower right.

<p>A snackbar and FAB use an enter and exit transition</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfs56ki-GM3-Transitions-TransitionPatterns-7-3-v01.mp4?alt=media

<h3 id="isPasted">Beyond screen bounds</h3><ul><li><strong>Commonly used with: </strong>App bars, banners, navigation bar, navigation rail, navigation drawer, and sheets</li><li><strong>Read more:</strong> <a href="/m3/pages/motion-transitions/applying-transitions#1b704202-167d-48d5-bca1-614cf050de1b" rel="noopener noreferrer" target="_blank">Guidelines</a></li></ul>

<p id="isPasted"><strong>Android</strong> components expand and collapse along the x or y axis as they slide on and off screen. This emphasizes their shape, making an otherwise simple transition more expressive.</p><p><strong>iOS</strong> components slide on and off screen without changing shape.</p>

Android and iOS demonstrations of navigation emerging from left edge and new message alert emerging from top edge.

<ol><li>Android enter and exit transitions </li><li>iOS enter and exit transitions</li></ol>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyfs6out-GM3-Transitions-TransitionPatterns-7-4-v01.mp4?alt=media

<p>Components like a side sheet can also enter and exit at the same elevation as the main content. Coplanar sheets shrink the available area for content.</p>

Selection of comments icon shrinks the main draft field.

<p>A coplanar side sheet uses an enter and exit transition</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygxnh2p-GM3-Transitions-TransitionPatterns-7-5-v01.mp4?alt=media

<p>Components can enter and exit from beyond the screen bounds based on a scroll gesture. This allows for more screen space to browse.</p>

Top Stories header disappears as user scrolls deeper into news.

<p>A top app bar slides off and on screen during a scroll</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygxorck-GM3-Transitions-TransitionPatterns-7-6-v01.mp4?alt=media

Scrolling lower through photos hides navigation, saving room for browsing.

<p>A navigation bar slides off and on screen during a scroll</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygxpdy1-GM3-Transitions-TransitionPatterns-7-7-v01.mp4?alt=media

<p id="isPasted">The location components enter and exit help establish a coherent spatial model of an app:</p><ol><li>A <strong>notification</strong> enters from the top indicating the notification drawer can also be pulled down from the top</li><li>A <strong>nav drawer</strong> enters from the left helping users understand where it's located when it's off screen</li><li>A <strong>bottom sheet</strong> and the keyboard enters from the bottom of the screen. This is a sensible default location for sheets to enter since the bottom of the screen is easiest to reach.</li></ol>

Email notification emerges from top of screen, navigation emerges from left, and keyboard enter from below, all in sequence.

<p>The direction of enter and exit transitions help establish a coherent spatial model</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygxqtbv-GM3-Transitions-TransitionPatterns-7-8-v01.mp4?alt=media

<h2>Skeleton loaders</h2><p>This pattern is used to transition from a temporary loading state to a fully loaded UI.</p><ul><li><p><strong>Read more</strong>: <a href="/m3/pages/motion-transitions/applying-transitions#b82b5150-609b-4540-903b-2b900ef830aa" target="_blank">Guidelines</a></p></li></ul>

<p id="isPasted">Skeleton loaders are UI abstractions that hint at where content will appear once it's loaded. They're used in combination with other transitions to reduce perceived latency and stabilize layouts as content loads.</p>

Music app is selected, producing a skeleton soon populated by individual music items in each corresponding outline.

<p>A skeleton loader is used after an app launches to indicate content is loading</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygxs24v-GM3-Transitions-TransitionPatterns-8-1-v01.mp4?alt=media

<p id="isPasted">Skeleton loaders have a subtle pulsing animation to indicate indeterminate progress. It starts at the top left of the screen and moves down to the bottom right.</p><p>Once content is loaded, it quickly fades in on top of the skeleton loader.</p>

<p>A pulsing animation indicates indeterminant loading</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygxtkjx-GM3-Transitions-TransitionPatterns-8-2-v01.mp4?alt=media

<p>Content quickly fades in once it's loaded</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygxuime-GM3-Transitions-TransitionPatterns-8-3-v01.mp4?alt=media

## Applying transitions

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">M3 transitions use the legacy easing and duration system. They'll eventually be updated to use the motion physics system.</div></div></div>

<h2 id="isPasted">What makes a good transition?</h2>

<p>Well-designed transitions should have these characteristics:</p>

<h3 id="isPasted">Follows accessibility settings</h3><p>Most platforms have a reduced animation setting to help users with a sensitivity to motion. If that setting is on, transitions should:</p><ul><li>Use subtle fades instead of intense sliding or scaling animations</li><li>Disable decorative effects like parallax or shape morphing</li></ul>

Podcast is selected and exited quickly on the left, while a podcast is selected and exited more slowly on the right.

<ol><li>Transitions with a default motion setting </li><li>Transitions with a reduced motion setting turned on</li></ol>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygy2t4f-GM3-Styles-Motion-Transitions-ApplyingTransitions-1-v01.mp4?alt=media

<h3 id="isPasted">Consistent</h3><p>Consistently applying the right type of transition helps make apps feel cohesive and predictable to use.</p>

Multiple apps move in tandem with the same motion effect, appearing in sync.

<p>These four Android apps use the same forward and backward transition, making them feel like a cohesive family of apps</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygy4536-GM3-Styles-Motion-Transitions-ApplyingTransitions-2-v01.mp4?alt=media

<h3 id="isPasted">Stable layouts</h3><p>Use skeleton loaders so that UI elements are coherent and stable during a transition. Avoid content shifting positions or instantly popping in as it loads. It can be distracting and frustrating to use.</p>

Podcast window opens with pulsing outline that frames content added slowly.

<p>Transitions should use skeleton loaders with a subtle pulsing animation to stabilize a layout as it loads</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygy6hgi-GM3-Styles-Motion-Transitions-ApplyingTransitions-3-1-v01.mp4?alt=media

Podcast window opens with no outline, and content added into haphazard clusters.

<p>Content should not pop in and shift locations during a transition</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygy75ou-GM3-Styles-Motion-Transitions-ApplyingTransitions-3-2-v01.mp4?alt=media

<h3 id="isPasted">No jarring jump cuts</h3><p>Jump cuts should generally be avoided as a default setting since they can be disorienting. Instantly transitioning from one screen to the next offers no clues to help a user orient themselves.</p><p>If pure efficiency is a top priority, like opening a menu in a productivity app, a jump cut may be preferred.</p>

Items in a music library are smoothly transitioned between.

<p>Animated transitions help users orient themselves as they navigate</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygy7y9g-GM3-Styles-Motion-Transitions-ApplyingTransitions-4-1-v01.mp4?alt=media

Items in a library are selected with stark, quick transitions.

<p>For most common transitions, jump cuts are jarring and disorienting</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygy8zr2-GM3-Styles-Motion-Transitions-ApplyingTransitions-4-2-v01.mp4?alt=media

<h3 id="isPasted">Coherent spatial model</h3><p>Transitions are used to establish a coherent spatial model. This helps users understand the physical layout of an app.</p>

An image within a horizontal carousel is also scrolled horizontally.

<p>These carousel transitions have a coherent spatial layout while navigating between a collapsed and expanded view</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygya5u9-GM3-Styles-Motion-Transitions-ApplyingTransitions-5-1-v01.mp4?alt=media

An image within a horizontal carousel is scrolled vertically.

<p>Switching between horizontal and vertical carousel layouts creates a confusing spatial model</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygyav9v-GM3-Styles-Motion-Transitions-ApplyingTransitions-5-2-v01.mp4?alt=media

<h3 id="isPasted">Unified direction</h3><p>A transition should have a unified direction of movement. Elements are grouped and move along a primary axis instead of moving in independent directions. Only important elements like hero images remain persistent throughout the transition. This helps guide a users focus.</p>

Selected song expands in a cohesive upward direction, marked by two blue lines showing unified movement.

<p>This transition has a simple vertical motion that’s easy to follow</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygybwyn-GM3-Styles-Motion-Transitions-ApplyingTransitions-6-1-v01.mp4?alt=media

Selected song expands in a jarring manner with multiple elements moving in different directions, marked by multiple red lines.

<p>Don’t animate many persistent elements independently. The various moving parts are distracting</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygycnpj-GM3-Styles-Motion-Transitions-ApplyingTransitions-6-2-v01.mp4?alt=media

<h3 id="isPasted">Clean fades</h3><p>Fully fade out content before fading new content in. This avoids the overlap of partially transparent elements resulting in distracting and messy frames.</p><p>If a cross fade needs to occur, keep it quick and hide it during the fastest part of the transition.</p>

Selected restaurant information fades out as it shrinks to reveal Google Map beneath..

<p>Fade content out before fading new content in to maintain a clean design</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygydts6-GM3-Styles-Motion-Transitions-ApplyingTransitions-7-1-v01.mp4?alt=media

Restaurant information remains visible as it shrinks and reveals the map beneath.

<p>Avoid showing cross faded content, the overlap of partially transparent elements can result in messy and distracting frames</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygyekln-GM3-Styles-Motion-Transitions-ApplyingTransitions-7-2-v01.mp4?alt=media

<p>Don't slowly fade components on top of other content as they enter or exit. This creates distracting cross faded frames. If a fade is needed, like with a Dialog entering in the middle of the screen, the fade should use a short duration to hide that part of the transition.</p>

Message window remains transparent with details visible as it shrinks causing text beneath to become obscured.

<p>Don't fade a bottom sheet as it enters and exits, it creates distracting cross faded frames</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygyfxw6-GM3-Styles-Motion-Transitions-ApplyingTransitions-8-v01.mp4?alt=media

<h3 id="isPasted">Simple style</h3><p>Transitions are not receptive to highly stylized motion. They're frequent, often occupy large portions of the screen, and are primarily meant to help users accomplish a task.</p>

Calendar event expands evenly and quickly comes to a rest.

<p>Transitions should have a simple style</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygyi588-GM3-Styles-Motion-Transitions-ApplyingTransitions-9-1-v01.mp4?alt=media

Calendar event expands with window bouncing momentarily and bouncing again on collapse.

<p>Common transitions should not use overt style effects like bouncy springs</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygyja80-GM3-Styles-Motion-Transitions-ApplyingTransitions-9-2-v01.mp4?alt=media

<h2 id="isPasted">Choosing a transition pattern</h2>

<p>Consider the following to choose the right transition for a given use case:</p>

<h3>Container transform</h3>

<p id="isPasted">This pattern is highly effective at creating a relationship between elements. It's also the most dramatic pattern in terms of style and should be reserved for the right context. Consider using it for:</p><ol><li>Hero moments that should be expressive</li><li>Shallow hierarchies where you expand an element for more detail then collapse it</li><li>Creating a seamless connection between elements</li></ol><p><strong>Read the research for the benefits of container transform</strong><strong> <a href="https://material.io/blog/motion-research-container-transform" target="_self">here</a>.</strong></p>

Image within a carousel is selected and expands to fill the screen.

A container transform creates a clear connection between the thumbnail and expanded image. It also makes this hero transition more expressive.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygykdgf-GM3-Styles-Motion-Transitions-ApplyingTransitions-10-1-v01.mp4?alt=media

Battery life menu item among many setting options is selected and expanded to fill the screen.

Don't use container transform in apps with deep hierarchies, the motion becomes excessive. The expressive style also doesn't fit this utility focused navigation.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygyl1ui-GM3-Styles-Motion-Transitions-ApplyingTransitions-10-2-v01.mp4?alt=media

<p>Use a container transform transition for hero moments rather than a forward and backward transition.</p>

A One-Year-Ago photo memory is selected and expanded to take over the screen.

<p>Don't use forward and backward transitions on hero moments like opening a photo memory</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygyn2vj-GM3-Styles-Motion-Transitions-ApplyingTransitions-11-v01.mp4?alt=media

<h3 id="isPasted">Forward and backward</h3>

<p id="isPasted">Both Android and iOS should use platform defaults for forward and backward navigation. It's easy to implement and stays current as platforms update. They have a simple motion style suitable for such a common transition.</p>

Individual message is selected with simple motion, and moves back with simple motion.

<p>Platform default forward and backward transitions are a sensible choice for common navigation</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygyo6nk-GM3-Styles-Motion-Transitions-ApplyingTransitions-12-1-v01.mp4?alt=media

Individual message is selected, causing a more radical take-over of the screen.

<p>Container transform transitions require custom implementations and the motion may feel excessive when used frequently</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygyoxdg-GM3-Styles-Motion-Transitions-ApplyingTransitions-12-2-v01.mp4?alt=media

<h3 id="isPasted">Lateral</h3>

<p id="isPasted">Lateral transitions are used to browse peer content that's part of the same set, like navigating between tabs in a media library. By sliding content horizontally, it hints at being able to swipe the content area to navigate between peers.</p>

Tabs in a music app shift horizontally without interruption when selected.

<p>A tab component uses a lateral transition type</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygyq7yo-GM3-Styles-Motion-Transitions-ApplyingTransitions-13-1-v01.mp4?alt=media

Tabs in a music app fade as they rotate horizontally.

Fading content as it slides makes the peer relationship and swipe gesture less obvious. The style also may be confused with a forward and backward transition.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygyr0oo-GM3-Styles-Motion-Transitions-ApplyingTransitions-13-2-v01.mp4?alt=media

<p>Don't use a Lateral transition for navigating hierarchical screens. Sliding content the full width of the screen is excessive for a high frequency transition. It also implies an equal peer relationship which isn't accurate to the hierarchy of the screens.</p>

Message selected within messaging app moves laterally.

<p>A lateral transition should not be used for common forward and backward navigation as it results in an excessive amount of motion</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygysi3q-GM3-Styles-Motion-Transitions-ApplyingTransitions-14-v01.mp4?alt=media

<h3 id="isPasted">Top level</h3>

<p id="isPasted">When tapping a navigation bar, rail or drawer, a quick fade is used to transition to a new destination. Top level destinations aren't necessarily related, so the motion intentionally does not create a connection between screens.</p><p>A lateral transition pattern is not recommended for this type of navigation. It implies you can swipe between top level destinations which conflicts with other components like carousels or swipe-able list items.</p>

Navigation between home and music app occurs with a quick fade, suggesting that items in each are distinct.

<p>A top level transition type is used with a navigation bar, rail and drawer</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygytotc-GM3-Styles-Motion-Transitions-ApplyingTransitions-15-1-v01.mp4?alt=media

Navigation between home a music app occurs in a seamless lateral scroll, falsely suggesting that items in each are connected.

Don't use a lateral transition to move between top level destinations. The gesture conflicts with carousel and list item gestures.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygyuc8i-GM3-Styles-Motion-Transitions-ApplyingTransitions-15-2-v01.mp4?alt=media

<h3 id="isPasted">Enter and Exit</h3>

<p id="isPasted">This transition pattern is used to introduce a component in context of the screen’s main UI. It can be modal, like a dialog requiring a user to take action. Or it can allow for simultaneously using both regions of the UI, like a standard bottom sheet over a map.</p><p>Don't use this pattern for navigating hierarchical screens. Sliding content the full height of the screen is excessive and it creates an unclear relationship between screens.</p>

Animation showing a standard bottom sheet using the enter and exit transition over a map.

<p>This bottom sheet uses an enter and exit transition pattern</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygyvia4-GM3-Styles-Motion-Transitions-ApplyingTransitions-16-1-v01.mp4?alt=media

Animation showing a card expanding to a full screen on click and using the enter and exit transition. 

<p>Don't use an enter and exit pattern for navigating hierarchical screens</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flygywcfr-GM3-Styles-Motion-Transitions-ApplyingTransitions-16-2-v01.mp4?alt=media
