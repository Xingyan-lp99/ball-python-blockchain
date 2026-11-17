# Bottom sheets

Source: https://m3.material.io/components/bottom-sheets
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/aa6f9af2-d539-4b22-9af5-838e7cfc4a85.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul type="disc" style="list-style-type:disc"><li><p>Use bottom sheets in <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium breakpoints</app-froala-tooltip-element></p></li><li><p>Two variants: <app-froala-tooltip-element description="Standard bottom sheets display supplementary content without blocking access to the screen’s primary content, such as an audio player at the bottom of a music app." link-label link-url should-open-link-in-new-tab="false">standard</app-froala-tooltip-element> and <app-froala-tooltip-element description="Modal bottom sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken." link-label link-url should-open-link-in-new-tab="false">modal</app-froala-tooltip-element></p></li><li><p>Content should be additional or secondary (not the app’s main content)</p></li><li><p>Bottom sheets can be dismissed in order to interact with the main content</p></li></ul>

Side by side view of standard bottom sheet modal bottom sheet

<ol><li>Standard bottom sheet</li><li>Modal bottom sheet</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp3m82k-1.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/522fd47a354cd2f0

libraryModuleType: STATUS_TABLE

<h2>Differences from M2</h2>

<ul><li>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></li><li>Shape: Bottom sheets have a 28dp top corner radius</li><li>Layout: New max-width of 640dp and an optional drag handle with an accessible 48dp hit target </li></ul>

Diagram of floating sheet set on screen background

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp3mrmz-2.png?alt=media

## Specs

<p><app-froala-tooltip-element description="Modal bottom sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken." link-label link-url should-open-link-in-new-tab="false">Modal bottom sheets</app-froala-tooltip-element> are above a scrim while <app-froala-tooltip-element description="Standard bottom sheets display supplementary content without blocking access to the screen’s primary content, such as an audio player at the bottom of a music app." link-label link-url should-open-link-in-new-tab="false">standard bottom sheets</app-froala-tooltip-element> don't have a scrim. Besides this, both variants of bottom sheets have the same specs.</p>

Diagram of container, drag handle, scrim

<ol><li>Container</li><li>Drag handle (optional)</li><li>Scrim</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flvutved1-1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/zukI3AJrMtdfLMWQT4wlAlMvIUfkIHpc5QmTQNqYJpxh-cV8QEJcVsy9Yc198HJsK1Od4d-cEiCfOKkcY5nhzjVVmtfGd9e3Wy75vUnWqSE=s2048

<h2>Tokens and specs</h2><p>Browse the component elements, attributes, tokens, and their values. <a href="/m3/pages/design-tokens/overview" target="_self"><u>Learn more about design tokens</u></a></p>

resourceName: designSystems/20543ce18892f7d9/components/75e530a1014802b3

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2 id="isPasted">Color</h2><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" id="isPasted">Learn more about design tokens</a></p>

Two diagrams featuring color opposites of scrim, container, drag handle

<p>Bottom sheet color roles used for both light and dark schemes:</p><ol class="decimal"><li><p>Scrim*</p></li><li><p>On surface variant</p></li><li><p>Surface container low</p></li></ol><p>*On Android platforms, the scrim color and opacity is automatically handled by the system UI.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flvutweax-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/DRToa14TKB2-AlRHwUn1aPr1fykKEPGlGiKLDxHYv9B9e5CeupNBR-mM7uQOfp_OK-ZHdqjgboBeyE7GhlNtsThqGvX87OLsiAoci2zkTRBo=s2048

<h2>Measurements</h2>

Bottom sheet on larger device with 56dp top and 56dp side margins

<p>Bottom sheet padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flvutx4kk-3.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/gVNIjqiBu0DjSUv-lwnH3xIvACuZ6S4LWuUrUHe_KA0V_GlU3w-iwKPM-ka_6KfmjFuQJ1k6qrmm2b0y_6ZJcLd4alet31vP-0-nUdrpj_k=s2048

<p id="isPasted">Bottom sheets span the full window width up to 640dp. When the window width exceeds 640dp, bottom sheets adjust to have a top margin of 56dp and side margins of 56dp. </p><div align="left" dir="ltr"><div class="table-wrapper"><table style="border:none;border-collapse:collapse;margin-right:calc(0%);width:100%"><thead><tr><th style="width:51.7743%">Attribute</th><th style="width:48.1358%">Value</th></tr></thead><tbody><tr><th style="width:51.7743%"><p>Drag handle alignment (horizontal)</p></th><td><p>Center</p></td></tr><tr><th style="width:51.7743%"><p>Drag handle padding top/bottom</p></th><td><p>22dp</p></td></tr><tr><th style="width:51.7743%"><p>Top margin</p></th><td><p>72dp</p></td></tr><tr><th style="width:51.7743%">Top margin (window width &gt; 640dp)</th><td>56dp</td></tr><tr><th style="width:51.7743%"><p>Start/end margin (window width &gt; 640dp)</p></th><td><p>56dp</p></td></tr><tr><th style="width:51.7743%"><p>Width</p></th><td><p>Full width, up to max-width 640dp</p></td></tr><tr><th style="width:51.7743%">Height</th><td>Variable</td></tr></tbody></table></div></div>

## Guidelines

Two variants of bottom sheets.

<ol><li id="isPasted">Standard bottom sheets</li><li>Modal bottom sheets</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp7eqa7-1.png?alt=media

<h2>Usage</h2>

<p>Bottom sheets display supplementary content and actions on a mobile screen.</p>

Photo sharing bottom sheet with contact list, app icons, and action buttons.

<p>Bottom sheet containing contacts and applications</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp7jb72-2.png?alt=media

<p>Bottom sheets are a versatile component that can contain a wide variety of information and <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/layout-overview/overview" should-open-link-in-new-tab="true">layouts</app-froala-tooltip-element>, including <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element> items (in <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> or grid layouts), actions, and supplemental content.</p>

Bottom sheet displaying 3 menu options.

<p>Bottom sheet with menu items in a list</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp7jy07-3.png?alt=media

<h2>Anatomy</h2>

<p>A container is the only required element of a bottom sheet. Bottom sheet <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/layout-overview/overview" should-open-link-in-new-tab="true">layouts</app-froala-tooltip-element> can vary widely to support the kinds of content they contain.</p>

3 elements of a bottom sheet.

<ol><li id="isPasted">Container</li><li>Drag handle (optional)</li><li>Scrim (modal only)</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp7l25p-4.png?alt=media

<h3>Container</h3>

<p id="isPasted">Bottom sheet containers hold all bottom sheet elements. Their size is determined by the space those elements occupy.</p><p>The container is the only required element of a bottom sheet. All other elements are optional.</p><p><br /></p>

Empty bottom sheet container.

<p>Bottom sheets are flexible containers that adapt to their content and available space</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp7llpd-5.png?alt=media

<h3>List items (optional)</h3>

<p><app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">Lists</app-froala-tooltip-element> are a continuous group of text or images. List items can include label text, icons, and text <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element>, among other elements.</p>

A bottom sheet displaying a list of actions for a song.

<p>Bottom sheet containing a list with icons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp7m0a5-6.png?alt=media

<h3>Dividers (optional)</h3>

<p><app-froala-tooltip-element description="Dividers are thin lines that group content in lists or other containers." link-label="More on dividers" link-url="/m3/pages/divider/overview" should-open-link-in-new-tab="true">Dividers</app-froala-tooltip-element> can be used to separate related content in bottom sheets.</p>

Bottom sheet with image action buttons and contact list separated by an inset divider.


<p>Bottom sheet with a divider separating kinds of actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp7t324-7.png?alt=media

<h3>Media (optional)</h3>

<p id="isPasted"><strong>Thumbnail</strong><br />Bottom sheets can include thumbnails for an avatar or logo.</p><p><strong>Image</strong><br />Bottom sheets can include photos, illustrations, and other graphics, such as weather icons.</p><p><strong>Video</strong><br />Bottom sheets can include video.</p>

A bottom sheet displaying various media formats, including thumbnails, images, and video.

<p>Bottom sheets can contain thumbnails, images, and video</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp7tqb3-8.png?alt=media

<h2>Standard bottom sheets</h2>

<p id="isPasted">Standard bottom sheets co-exist with the screen’s main UI region and allow for simultaneously viewing and interacting with both regions, especially when the main UI region is frequently scrolled or panned.</p><p>Use a standard bottom sheet to display content that complements the screen’s primary content, such as an audio player in a music app.</p>

Bottom sheet with music player controls visible while browsing albums.

<p>The music player in this standard bottom sheet allows people to control their music while browsing albums</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp7ubva-9.png?alt=media

<p id="isPasted">At full-screen height, standard bottom sheets contain a collapse icon in an app bar to return to their initial position.</p><p>Standard bottom sheets can contain supplementary content that continues below the screen, such as location information over a map.</p>

<p>A bottom sheet can have preset positions from full-screen height to preview</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flb1hpr8k-Bottom_sheet_fully_expanded.png?alt=media

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvpbsatl-GM3-Components-BottomSheets-Guidelines-1-v01.mp4?alt=media

<h2>Modal bottom sheets</h2>

<p>Like <app-froala-tooltip-element description="Dialogs provide important prompts in a user flow." link-label="More on dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">dialogs</app-froala-tooltip-element>, modal bottom sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken.</p>

A modal sheet with filter options to categorize files in the app. 

<p>A modal bottom sheet must be interacted with or dismissed. Its blocking behavior makes it suitable for a menu, such as in this files app, to help people focus on their available choices.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp7yz9g-11.png?alt=media

<p id="isPasted">Use a modal bottom sheet as an alternative to inline <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menus</app-froala-tooltip-element> or simple <app-froala-tooltip-element description="Dialogs provide important prompts in a user flow." link-label="More on dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">dialogs</app-froala-tooltip-element> on mobile, especially when offering a long <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> of action items, or when items require longer descriptions and icons.</p><p>Modal bottom sheets are used in mobile apps only.</p>

A modal bottom sheet displayed as an alternative to a traditional menu, presenting a list of actions.

<p>Modal bottom sheets can be used instead of menus to present additional actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvqcnuc5-12.png?alt=media

<h3>Visibility</h3>

<p id="isPasted">To provide access to its top actions, the initial vertical position of <app-froala-tooltip-element description="Modal bottom sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken." link-label link-url should-open-link-in-new-tab="false">modal bottom sheets</app-froala-tooltip-element> is capped at 50% of the screen height.</p><p>Modal bottom sheets whose contents exceed 50% of the screen height can then be pulled across the full screen and scrolled internally to access their remaining items.</p>

A modal bottom sheet covering half of the screen, so both images and actions are accessible.

<p>The initial vertical position of modal bottom sheets can't exceed 50% of the screen height</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flwb1px3f-13.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/0hAPkL3uzyvqMvvRWFno-49bG4xDEWveRgFgP06QiwL9TTPtIatzwZnFBVZI70GmAn_NyU9lVQQ-8JkRQ8Zo7385AFopIBou3f5sD8YuZLIT=s1352

<p id="isPasted"><app-froala-tooltip-element description="Modal bottom sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken." link-label link-url should-open-link-in-new-tab="false">Modal bottom sheets</app-froala-tooltip-element> appear when triggered by a user action, such as tapping a <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">button</app-froala-tooltip-element> or an overflow icon. They can be dismissed by:</p><ul><li>Tapping a <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element> item or action within the bottom sheet</li><li>Tapping the scrim</li><li>Swiping the sheet down</li><li>Using a close affordance within the bottom sheet’s <app-froala-tooltip-element description="App bars display information and actions at the top of a screen." link-label="More on app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">app bar</app-froala-tooltip-element>, if available</li></ul><p>Display a close affordance in a full-screen modal bottom sheet.</p>

A modal bottom sheet disappearing by tapping the scrim.

<p>Tapping the scrim dismisses a modal bottom sheet</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp80k55-14.png?alt=media

A modal bottom sheet disappearing by swiping the sheet down.

<p>A modal bottom sheet can be dismissed by swiping the sheet down</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp81a31-Bottom_sheet_dismiss_swipe.png?alt=media

<h2>Responsive layout</h2>

<h3>Compact breakpoint</h3><p>In <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoints</app-froala-tooltip-element>, like mobile devices, bottom sheets extend across the width of a screen and are elevated above the primary content.</p>

A bottom sheet extended to the width of a mobile screen.

<p>Bottom sheets should extend to the width of the screen on mobile</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp86bt1-15.png?alt=media

<h3>Medium and expanded breakpoints</h3><p>For larger screens with <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints</app-froala-tooltip-element>, bottom sheets have a default max-width to prevent undesired <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/layout-overview/overview" should-open-link-in-new-tab="true">layouts</app-froala-tooltip-element> and awkward spacing. However, this can be overridden if needed. For more complex tasks and flows, consider using a non-transient surface such as a <app-froala-tooltip-element description="Floating sheets show secondary content on a surface that can be anchored to the screen or moved." link-label link-url should-open-link-in-new-tab="false">floating sheet</app-froala-tooltip-element>.</p>

A bottom sheet extended to its max-width on a large screen device, not spanning the full screen.

<p>Bottom sheets on larger screens like tablet have a max width that can be overridden</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp86pgb-16.png?alt=media

<p>On larger <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints</app-froala-tooltip-element>, like desktop, a bottom sheet can be swapped for a <app-froala-tooltip-element description="Side sheets show secondary content anchored to the side of the screen." link-label="More on side sheets" link-url="/m3/pages/side-sheets/overview" should-open-link-in-new-tab="true">side sheet</app-froala-tooltip-element> that shows similar content.</p>

A side sheet on desktop.

<p>Side sheets can contain the same content as bottom sheets and may be more suitable for desktop</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp877lp-17.png?alt=media

<h2>Behavior</h2>

<p>Bottom sheets can offer an expansion option where the sheet is fully raised and toggled between a collapsed and expanded <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">state</app-froala-tooltip-element>. This provides a more predictable footprint of the sheet, and can be set by the system or toggled by the user.</p>

Bottom sheet fully raised, showing photo actions, sharing options, and albums to add the photo to.

<p>A bottom sheet for sharing can appear fully raised if needed</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp87qvd-18.png?alt=media

Collapsed bottom sheet, showing focused set of options.

<p>Alternately, a bottom sheet for sharing can appear collapsed for a more focused set of actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp8870t-19.png?alt=media

<h3>Custom positioning</h3>

<p><span style="white-space:pre-wrap" id="isPasted">The drag handle can be dragged or selected to change the bottom sheet height. <br /><br />Sheets should be able to cycle through preset heights and close completely without dragging. Selecting the drag handle should toggle through preset heights or close the sheet, while selecting the scrim should always close the bottom sheet.<br /><br />If the bottom sheet has multiple preset heights but can’t use a drag handle, Material requires the inclusion of a single-pointer alternative to change height.</span></p>

Bottom sheet with a visible drag handle that can be used to adjust its height.

<p>Interacting with the drag handle can quickly move a bottom sheet through preset heights</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp8argg-20.png?alt=media

Bottom sheet resized using the visible drag handle.

<p>A bottom sheet can automatically resize to another height after interacting with the drag handle</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp8b6u5-21.png?alt=media

<h3>Scrolling</h3>

<p>Bottom sheets can be horizontally scrolled, independent of the rest of the screen’s content.</p>

Bottom sheet that can be scrolled horizontally.

<p>Bottom sheets should be scrollable when their content exceeds the initial viewable height</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp8bo42-22.png?alt=media

<h3>Back</h3>

<p id="isPasted">On Android, a <app-froala-tooltip-element description="Gestures are all the ways people interact with UI elements using touch." link-label="More on gestures" link-url="/m3/pages/gestures" should-open-link-in-new-tab="true">gesture</app-froala-tooltip-element> called predictive back allows a user to swipe left or right on the bottom sheet. </p><ul><li><span style="white-space:pre-wrap">Bottom sheet detaches from the left and right edges of the screen to signal it will close</span></li><li><span style="white-space:pre-wrap">Previous screen is revealed in a preview<br /></span></li></ul><p><span style="white-space:pre-wrap">A list of compatible components is available in the </span><span style="white-space:pre-wrap"><a href="/m3/pages/gestures">gestures article</a></span><span style="white-space:pre-wrap">.</span></p>

<p><span style="white-space:pre-wrap">Preview of the result of the gesture, <strong>release</strong> to commit, <strong>fling</strong> to commit, and <strong>cancel</strong> </span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvpbtr1r-GM3-Components-BottomSheets-Guidelines-2-v01.mp4?alt=media

## Accessibility

<h2>Use cases</h2>

<p>Users should be able to:</p><ul><li id="isPasted">Resize bottom sheets without having to rely on touch gestures</li></ul>

<h2><span data-buffer="&lt;!--(figma)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(/figma)--&gt;">Interaction &amp; style</span></h2>

<h3><span style="white-space:pre-wrap">Touch target area</span></h3><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">The top 48dp portion of the bottom sheet is interactive when user-initiated resizing is available and the drag handle is present.</span></span></p>

Touch target area of a bottom sheet.

<p>To ensure touch target accessibility, the top portion of a bottom sheet can be reserved for resize interactions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp8g5p9-1.png?alt=media

<h3>Initial focus</h3><p><span><span>The optional drag handle can be <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element> in the tab order and interacted with using non-touch <app-froala-tooltip-element description="Inputs are devices that provide interactive control of an app. Common inputs are a mouse, keyboard, and touchpad." link-label link-url should-open-link-in-new-tab="false">inputs</app-froala-tooltip-element>, such as keyboard or <app-froala-tooltip-element description="Switches toggle the state of an item on or off." link-label="More on switches" link-url="/m3/pages/switch/overview" should-open-link-in-new-tab="true">switch</app-froala-tooltip-element> controls.</span></span></p>

Focus on the drag handle of a bottom sheet.

<p>Visible focus shown on the drag handle affordance</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp8gmd5-bottom-sheet-focus.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Dragging</span></h3><p id="isPasted">Include a single-pointer alternative for any action that can be completed by dragging.</p><p>Drag handles should cycle the bottom sheet through available heights when selected. If a drag handle can’t be used, add a button to do this action.</p>

Bottom sheet with focused drag handle at lower preset height.

<p><span style="white-space:pre-wrap">Interacting with the drag handle can quickly move a bottom sheet through preset heights</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm33eulyj-20.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/oTYgjX2EiyzXtztzy6pKLtl4orLwt83InSn2nHXrJuSKwwBhO-R1pllkNzYnilWk-qI5_eNNob5zUMIP1SSUAOOPOspSu6g7aWhV4--hKz0=s656

Bottom sheet with drag handle at higher preset height.

<p><span style="white-space:pre-wrap">A bottom sheet can automatically resize to another height after interacting with the drag handle</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm33euvu0-21.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Qbh70YFT_L81Y-982OVil6qLEB90imUJs9wbRQLdxVkcYIPlYik995maTieLEuP8Oc-T1-2WrcTuO_ZBCd2kwc9yD-9SgngSP2FvrpqzCubGcw=s656

<h2 id="isPasted">Keyboard navigation</h2>

<div class="table-wrapper"><table style="width:100%"><thead><tr><th><div style="text-align:center">Keys</div></th><th><div style="text-align:center">Actions</div></th></tr></thead><tbody><tr><td>Tab</td><td>Focus lands on drag handle</td></tr><tr><td>Space / Enter</td><td>Toggles between available heights</td></tr></tbody></table></div>

<h2 id="isPasted">Labeling</h2>

<p>Label only the drag handle. The <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> role for the drag handle is “button.” </p>

Labeled drag handle with role of button.

<p><span style="white-space:pre-wrap">Label the drag handle</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4bunmcg-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/rQnID5aS5_ORuWh7Yp2LhBOLLPZQrEvPmowQpgTLFeBfTwyBEMJjvvOYIo991CA4BiA9o4uEZBALyTu1klLA5adv9b49GO3gJuCp_2IIQxsBVQ=s1352
