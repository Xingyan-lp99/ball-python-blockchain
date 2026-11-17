# Side sheets

Source: https://m3.material.io/components/side-sheets
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/040dabe3-ed0f-4759-824d-812224e78af3.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul type="disc" style="list-style-type:disc"><li><p>Use side sheets to provide optional content and actions without interrupting the main content</p></li><li><p>Two variants: <app-froala-tooltip-element description="Standard side sheets display content without blocking access to the screen’s primary content, such as an audio player at the side of a music app. They're often used in medium and expanded window sizes like tablet or desktop." link-label link-url should-open-link-in-new-tab="false">standard</app-froala-tooltip-element> and <app-froala-tooltip-element description="Modal side sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken. They're often used in compact breakpoints, like mobile, due to limited screen size." link-label link-url should-open-link-in-new-tab="false">modal</app-froala-tooltip-element></p></li><li><p>People can navigate to another region within the sheet</p></li><li><p>Side sheets can contain a back icon for navigation</p></li></ul>

The 2 variants of side sheets.

<ol><li>Standard side sheet
</li><li>Modal side sheet</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmgalv851-01.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/5DQn6-h3w6BIR9DoXAncCck22WNg-86e7uh4meG22SsqcvVMb966220Fp-Ooiwui3eekiqk8p_Uq9BpNZ4wUYSQFPwovt6b_fOdpiU008vQ0Lw=s2048

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/56df27a2f3576bb1

libraryModuleType: STATUS_TABLE

<h2 id="isPasted">Differences from M2</h2>

<ul type="disc" style="list-style-type:disc"><li><p>Right-to-left (RTL) language support with left side sheet</p></li><li><p>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></p></li><li><p>Shape: <app-froala-tooltip-element description="Modal side sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken. They're often used in compact breakpoints, like mobile, due to limited screen size." link-label link-url should-open-link-in-new-tab="false">Modal side sheets</app-froala-tooltip-element> have a 16dp corner radius</p></li></ul>

A modal side sheet showing the 16dp corner radius.

<p>Side sheets have new color mappings to support dynamic color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmgalwhrt-02.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/NcjJRXvRM56DuF0hrulvw3eixw8QXtodshjuhM6OgLXuC54E06Ov7JGxPSynfQiwGnaQspHgMps2all60Y81-oRaznUym7yDF1bg53VC-so8ag=s1352

## Specs

<h2>Tokens &amp; specs</h2><p>Browse the component elements, attributes, tokens, and their values. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/06c2c925cf96adca

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Standard side sheet</h2>

4 elements of a standard side sheet.

<ol><li>Divider (optional)</li><li>Headline</li><li>Container</li><li>Close icon button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmgam1q2e-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/lg2svhv9DuP5FMVqxsmnsLS5m2S1aSqU4fcUuQacBh9lHSy2DiPpaUpGpphS0iiVcuOJvSHp95mF9Z55dmy9F9KeGE5I-_-OOsgSuKRp_feW=s2048

<h3>Standard side sheet color</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview/" target="_self">Learn more about design tokens</a></p>

4 color roles applied to a side sheet in light and dark themes.

<p id="isPasted">Side sheet color roles used for light and dark themes:</p><ol><li>Outline variant</li><li>On surface variant</li><li>Surface</li><li>On surface variant</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmgam3xno-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LqFhUoIZJCxI-xrg-swaOn2vwlyswPNvs2JQfS2oNHhVms4yvkJE1tCBaFLUxKH_B-NWUoZ9Wo5QF2x437thBA0uzYeoBxeJ2NMWg2jmqbgL=s2048

<h3 id="isPasted">Standard side sheet measurements</h3>

Standard side sheet padding and size measurements.

<p>Side sheet padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmgam4wao-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/2LAblBbcF_ZBcupC3Q2aXZlYse3imp3Y1ePIVfC3DY5iefsYPzFRDPu20wDJmkgcAxlpprO9NpnBwJdHjBTiA32q7BduBlHaREVzxLLbrKkDwA=s2048

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="text-align:center">Attribute<br /></th><th style="text-align:center">Value<br /></th></tr></thead><tbody><tr><th style="width:50%;text-align:center">Start/end padding<br /></th><td>24dp</td></tr><tr><th style="width:50%;text-align:center">Padding between top elements<br /></th><td>12dp</td></tr><tr><th style="width:50%;text-align:center">Bottom actions height<br /></th><td>72dp</td></tr><tr><th style="width:50%;text-align:center">Bottom actions top padding<br /></th><td>16dp</td></tr><tr><th style="width:50%;text-align:center">Bottom actions bottom padding<br /></th><td>24dp</td></tr><tr><th style="width:50%;text-align:center">Bottom actions alignment (horizontal)<br /></th><td>Left</td></tr><tr><th style="width:50%;text-align:center">Max-width<br /></th><td>400dp</td></tr><tr><th style="width:50%;text-align:center">Margins (when detached)<br /></th><td>16dp</td></tr></tbody></table></div>

<h2>Modal side sheet</h2>

7 elements of a modal side sheet.

<ol><li>Back icon button (optional)</li><li>Headline</li><li>Container</li><li>Close icon button</li><li>Divider (optional)</li><li>Action buttons (optional)</li><li>Scrim</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmgam6adp-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/mCkCbKeP2EQNehrmAoIhTh8csAxLh6TS5YKqEtZWs-p6OhXjXK3OQ-8GxAiPRoDu7tQQ_qh6pdkkvtk5LLT2ACRvlqzzCn6QkW5TORe1go6W=s2048

<h3>Modal side sheet color</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview/" id="isPasted">Learn more about design tokens</a>.</p>

4 color roles applied to a modal side sheet in light and dark themes.

<p>Side sheet color roles used for light and dark themes:</p><ol class="decimal"><li><p>On surface variant</p></li><li><p>On surface variant</p></li><li><p>Surface container low</p></li><li><p>On surface variant</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmgam8seo-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/MCbwK4pOf-VBkCt3qXBvBVReNnD3TzDuwLJdajh_CvxUT_TN3_5Ho5v3QyV0SHhv5IHbZP0V5UbCSy8rXaQFJ79cocKme0PSXGWzZT5HUvU=s2048

<h3>Modal side sheet measurements</h3>

Modal side sheet padding and size measurements

<p>Modal side sheet padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmgamb5rx-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ggmDZsvw6x0ei4ktaEtZbG_D-SvR-dKw59udjcKCr7KdED37SNpjgIxFdBL6ySJrdglC7AeXbchojJM7pgxlhcVmcXVp26aCBCmnQ1utyjDL=s2048

<p><br /></p><div class="table-wrapper"><table><thead><tr><th style="text-align:center">Attribute<br /></th><th style="text-align:center">Value<br /></th></tr></thead><tbody><tr><th>Start/end padding<br /></th><td>24dp</td></tr><tr><th>Start padding with icon</th><td>16dp</td></tr><tr><th>Padding between top elements</th><td>12dp</td></tr><tr><th>Bottom actions height<br /></th><td>72dp</td></tr><tr><th>Bottom actions top padding<br /></th><td>16dp</td></tr><tr><th>Bottom actions bottom padding</th><td>24dp</td></tr><tr><th>Bottom actions alignment (horizontal)<br /></th><td>Left</td></tr><tr><th>Max-width<br /></th><td>400dp</td></tr><tr><th>Margins (when detached)<br /></th><td>16dp</td></tr></tbody></table></div><p><br /></p>

## Guidelines

Side by side comparison of a standard and a modal side sheet.

<ol><li>Standard side sheet
</li><li>Modal side sheet</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqqqohk-01.png?alt=media

<h2><span style="white-space:pre-wrap">Usage</span></h2>

<p><app-froala-tooltip-element description="Standard side sheets display content without blocking access to the screen’s primary content, such as an audio player at the side of a music app. They're often used in medium and expanded breakpoints like tablet or desktop. " link-label link-url should-open-link-in-new-tab="false">Standard side sheets</app-froala-tooltip-element> are supplementary surfaces used mostly in <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> to <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints,</app-froala-tooltip-element> like tablet and desktop. They provide a consistent and predictable surface for contextual actions and information.<br /><br />Standard side sheets display content that complements the screen’s primary content. They remain visible while people interact with primary content.</p><p>Common uses include:</p><ul type="disc" style="list-style-type:disc"><li><p>Displaying a list of actions that affect the screen’s primary content, such as filters</p></li><li><p>Displaying supplemental content and features </p></li></ul>

Standard side sheet showing supplementary information about a photo.

Information about a photo in a standard side sheet

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqr6mnd-02.png?alt=media

<p><app-froala-tooltip-element description="Modal side sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken. They're often used in compact breakpoints, like mobile, due to limited screen size." link-label link-url should-open-link-in-new-tab="false">Modal side sheets</app-froala-tooltip-element> are preferred in <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoints</app-froala-tooltip-element>, like mobile, due to limited screen size. </p><p>They can display the same kinds of content as standard side sheets, but must be dismissed in order to interact with the underlying content.</p>

Modal side sheet showing filter controls.

Modal side sheet with filter controls

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqrab5f-03.png?alt=media

<p>Side sheets have a fixed width and typically span the height of the screen. </p><p>Their dimensions depend on how the app’s <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/understanding-layout/overview" should-open-link-in-new-tab="true">layout</app-froala-tooltip-element> is subdivided into UI regions.</p>

A modal sheet at the right of a screen, with the correct inset.

<p id="isPasted">Place side sheets along the edge of the screen, usually on the right side to avoid interference with any navigational components on the left edge. They can be slightly inset by 16dp.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqrlvws-04-do.png?alt=media

A modal side sheet at the right of the screen with the wrong inset.

<p>Don’t inset a side sheet from the screen edges far beyond the recommended margin. This makes the sheet’s position and scroll behavior unclear, while obscuring primary content.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqrngv8-05-don't.png?alt=media

<h2><span style="white-space:pre-wrap">Anatomy</span></h2>

4 elements of a standard side sheet.  

<ol><li>Divider (optional)</li><li>Headline</li><li>Container</li><li>Close icon button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqrqfpt-06.png?alt=media

7 elements of a modal side sheet.

<ol><li>Back icon button (optional)</li><li>Headline</li><li>Container </li><li>Close icon button</li><li>Divider (optional) </li><li>Action buttons (optional) </li><li>Scrim</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqrrjh7-07.png?alt=media

<h3><span style="white-space:pre-wrap">Container</span></h3><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">Side sheet containers hold all side sheet elements. Their size is determined by the space those elements occupy.<br /> <br />The container is the only required element of a side sheet.</span></span></p>

A modal side sheet’s container.

<ol><li>Container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqsampe-08.png?alt=media

<h3>Back icon button (optional)</h3><p><app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">Icon buttons</app-froala-tooltip-element> can provide ways to exit a side sheet or move to a different experience.<br /><br />Because the primary content behind or beside a side sheet is always visible, it’s important to provide affordances for leaving a side sheet and returning to the primary content.</p>

Back icon button on the upper left of a modal side sheet.

<ol><li>Back icon button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqsgqgs-09.png?alt=media

<h3>Close icon button (optional)</h3><p>A close affordance provides a consistent method for dismissing a side sheet. </p><p>A close icon button is highly recommended, increases <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview/principles" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element>, and makes <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element> side sheets easier to close.</p>

Close icon button on the upper right of a modal side sheet.

<ol><li>Close icon button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqsns8t-10.png?alt=media

<h3>Action buttons (optional)</h3><p><app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">Buttons</app-froala-tooltip-element> represent actions available from a side sheet. Examples: <strong>Save</strong>, <strong>Edit</strong>, <strong>Download</strong></p><p>Use <app-froala-tooltip-element description="Elevation is the distance between two surfaces on the z-axis" link-label="More on elevation" link-url="/m3/pages/elevation/overview" should-open-link-in-new-tab="true">elevation</app-froala-tooltip-element>, fill, and <app-froala-tooltip-element description="Tone is how light or dark a color appears. Tone is sometimes also referred to as luminance." link-label="More on hue, chroma, and tone" link-url="/m3/pages/color/how-the-system-works#dc7848f3-b094-4f9a-9e50-bfa5a5029617" should-open-link-in-new-tab="true">tone</app-froala-tooltip-element> to call attention to specific actions.</p>

Save and cancel buttons at the bottom of a modal side sheet.

<ol><li>Action buttons</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqsw3fe-11.png?alt=media

<h3>Divider (optional)</h3><p><app-froala-tooltip-element description="Dividers are thin lines that group content in lists or other containers." link-label="More on dividers" link-url="/m3/pages/divider/overview" should-open-link-in-new-tab="true">Dividers</app-froala-tooltip-element> can separate different kinds of content and create distinct regions in a side sheet. <br /><br /></p><p>Use a divider to separate:</p><ul><li><p>Action buttons from content</p></li><li><p>User-generated content from system-generated content</p></li></ul>

Horizontal divider on a modal side sheet.

<ol><li>Divider</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqsz2ma-12.png?alt=media

<h3>Content (optional)</h3><p>Side sheets can display a wide variety of content and <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/understanding-layout/overview" should-open-link-in-new-tab="true">layouts</app-froala-tooltip-element>, ranging from a <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> of actions to supplemental content in a tabular layout.</p>

2 side sheets with different content displayed side by side.

Form controls shown in a side sheet for app settings

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqt0pai-13.png?alt=media

As a small screen changes to a larger size the modal side sheet transitions to a standard side sheet.

<p>Modal side sheets on smaller screens can transition to standard side sheets at larger screen sizes</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw8ytzch-GM3-Components-SideSheets-Guidelines-1-v01.mp4?alt=media

<h2>Adaptive design</h2>

<p>Side sheets have a default width, but can be resized depending on the needs of the <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/understanding-layout/overview" should-open-link-in-new-tab="true">layout</app-froala-tooltip-element>. <br /><br />When a <app-froala-tooltip-element description="Standard side sheets display content without blocking access to the screen’s primary content, such as an audio player at the side of a music app. They're often used in medium and expanded breakpoints like tablet or desktop. " link-label link-url should-open-link-in-new-tab="false">standard side sheet</app-froala-tooltip-element> opens, the body area shrinks to accommodate the sheet’s width while maintaining a <app-froala-tooltip-element description="Margins are the spaces between the edge of a nested element and its parent element, such as the space between a button's label text and the edge of its container." link-label="More on margins" link-url="/m3/pages/understanding-layout/spacing#38a538d7-991f-4c39-8449-195d32caf397" should-open-link-in-new-tab="true">margin</app-froala-tooltip-element> on the body’s trailing edge.</p>

Body area of a screen adjusts to accommodate entrance and exit of side sheet. 

<p>Entrance of standard side sheets will cause the body area to adjust and accommodate the new content</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw8yw08l-GM3-Components-SideSheets-Guidelines-2-v01.mp4?alt=media

<h3>RTL language support</h3><p>In right-to-left (RTL) languages, side sheets should appear on the left edge of the window with all elements reversed.</p>

Side sheet along the left edge of a screen. All buttons and icons are reversed.

<p>Side sheet elements are reversed in RTL languages</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmeqwb27c-16.png?alt=media

<h2><span style="white-space:pre-wrap">Behavior</span></h2>

<p>Side sheets can vertically scroll independent of the rest of the UI. </p><p>This allows their scroll position and content to persist while the page is scrolled, and vice versa.<br id="isPasted" /><br />Side sheets cannot scroll horizontally.</p>

Animation showing a side sheet being scrolled vertically to view all the options.

<p>Side sheets can vertically scroll internally when their content exceeds the screen height</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw8yz6fq-GM3-Components-SideSheets-Guidelines-3-v01.mp4?alt=media

A side sheet appears to scroll horizontally.

<p>Don’t allow horizontal scrolling or lay out the side sheet in a way that suggests horizontal scrolling. A side sheet’s narrow width leaves limited space to fully view items.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw8z3x56-19_don't.png?alt=media

<h3>Predictive back</h3>

<p>On Android, a <app-froala-tooltip-element description="Gestures are all the ways people interact with UI elements using touch." link-label="More on gestures" link-url="/m3/pages/gestures" should-open-link-in-new-tab="true">gesture</app-froala-tooltip-element> called <a href="https://github.com/material-components/material-components-android/blob/master/docs/foundations/PredictiveBack.md" target="_blank">predictive back</a> allows a person to swipe left or right on the side sheet. </p><p>When predictive back is used:</p><ul><li><p>The side sheet detaches from the top and bottom edges of the screen to signal it will close</p></li><li><p>The previous screen is revealed in a preview</p></li><li><p>The side sheet and its content always scales in the direction of the gesture</p></li></ul><p><a href="/m3/pages/gestures#22462fb2-fbe8-4e0c-b3e7-9278bd18ea0d" target="_blank">Find a list of compatible components</a></p>

Swiping to go back shows a preview of the previous screen.

<p><span style="white-space:pre-wrap">Preview of the result of the gestures: <span style="font-weight:bold;white-space:pre-wrap">release</span> to commit, <span style="font-weight:bold;white-space:pre-wrap">fling</span> to commit, and <span style="font-weight:bold;white-space:pre-wrap">cancel</span></span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw8z7v0k-GM3-Components-SideSheets-Guidelines-4-v02.mp4?alt=media

## Accessibility

<h2>Use cases</h2>

<p id="isPasted">People should be able to dismiss the side sheet using assistive technology.</p>

<h2><span style="white-space:pre-wrap">Interaction &amp; style</span></h2>

<p>Material requires that a close affordance, such as a close <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon button</app-froala-tooltip-element>, is always present within a side sheet.</p>

Side sheet correctly designed with close icon in upper right corner.

<p>A close icon button makes the side sheet easy to dismiss </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmgamgh0c-01-do.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/0LSf0hnC19HAyDDf88fqzUUo62971bFb2XWjHguURc3jJbZpy8ejGuIyFR-2MSFM27gLA3LjupVjSj8E5kEuDJG7IqeHD17NaXUOXKsEHdP8=s656

Side sheet incorrectly designed with no close icon button.

<p>Without a close icon button, people can’t predict the opening and closing flow of side sheets, or know if the sheet is transient or permanent</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmgamhoet-02-don't.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/bGugN52A6j4bvI4smHp21cQzZbZv4qaF9YBYdKZDD51XL6yAkHSY_KVtpUF7HkL6G04T2w61MQeJo-E8SqmPJx6OuO9YMeBqpjP7AOhc_yNi=s656

<h2>Initial focus</h2>

<p>Actions within a side sheet can be <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element> by tab order using a keyboard or switch control.</p>

Side sheet diagram showing the focus order of headline, close, save, cancel.

<p>Visible focus shown on the available actions within a side sheet:</p><ol class="decimal" id="isPasted"><li>Headline</li><li>Close</li><li>Cancel</li><li>Save</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmgamkh0k-03.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/MuS9aCeC3P_ukbbopUpL7M9rV8VhBbirg3UofV-_SA7g-v4ABLSE8zgMWQOlHo7WP5XEd7s-KyR15aPB360mGPFofc_F3uKb1Sy7iQ8iOZ0dGA=s1352

<h2>Keyboard navigation</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:18.3%"><p>Keys</p></th><th style="width:81.7%"><p>Actions</p></th></tr></thead><tbody><tr><th style="width:18.3%"><p><strong>Tab</strong></p></th><td><p>Focus lands on (non-disabled) icon button<br /></p></td></tr><tr><th style="width:18.3%"><p><strong>Space</strong> or <strong>Enter</strong></p></th><td><p>Activates the (non-disabled) icon button</p></td></tr></tbody></table></div>

<h2>Labeling</h2>

<p><span style="white-space:pre-wrap">The accessibility role for a side sheet is <strong>Dialog</strong>.</span></p>

Side sheet showing the accessibility role as dialog.

<p>The role for side sheets is <strong>Dialog</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmgamoe2t-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ogti7RlWzhZNIER0PGHxR2hM--wMncqBhexq_aLUiY6OPM1C5NeuaWV29SOOqi5gjdr7dGbCFrlPMnQ2hX5pgrWhVUrQVhUmESeeg09ZQhdB=s1352
