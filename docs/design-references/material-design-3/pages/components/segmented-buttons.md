# Segmented buttons

Source: https://m3.material.io/components/segmented-buttons
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/409b50be-403a-4846-932c-706a9b2137dd.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">Segmented buttons are no longer recommended in the Material 3 expressive update. For those who have updated, use the <a href="/m3/pages/button-groups/overview/" target="_blank">connected button group</a> instead, which has mostly the same functionality but with an updated visual design.</div></div></div>

<ul><li><p>Segmented buttons can contain icons, label text, or both</p></li><li><p>Two variants: single-select and multi-select</p></li><li><p>Use for simple choices between two to five items (for more items or complex choices, use <app-froala-tooltip-element description="Chips help people enter information, make selections, filter content, or trigger actions." link-label="More on chips" link-url="/m3/pages/chips/overview" should-open-link-in-new-tab="true">chips</app-froala-tooltip-element>)</p></li></ul>

Two variants of segmented buttons.

<ol><li>Single-select segmented button</li><li>Multi-select segmented button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7qvais-1.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/6608f8e8a72ac160

libraryModuleType: STATUS_TABLE

moduleConfigurationOverrides: {'headings': ['Type', 'Resource', 'Status']}

<h2>M3 Expressive update</h2>

<p><strong>May 2025</strong></p><p>The segmented button is no longer recommended. Use the <a href="/m3/pages/button-groups/overview/" target="_blank">connected button group</a> instead. <a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank">More on M3 Expressive</a></p>

<h2 id="isPasted">Differences from M2</h2>

<ul><li><p><strong>Color:</strong> New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></p></li><li><p><strong>Icons:</strong> Optional check icon to indicate selected <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/google-material-3/pages/interaction-states/overview" should-open-link-in-new-tab="true">state</app-froala-tooltip-element></p></li><li><p><strong>Layout:</strong> Taller container height of 40dp</p></li><li><p><strong>Name and variants:</strong> Segmented buttons were previously known as toggle buttons. They now have two official variants: single-select and multi-select.</p></li><li><p><strong>Shape:</strong> Fully rounded corners</p></li><li><p><strong>Typography: </strong>Labels use sentence case instead of all caps</p></li></ul>

Diagram indicating the fully rounded corner radius of a segmented button.

<p><span style="white-space:pre-wrap">Segmented buttons now have a container height of 40dp</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhr0fyz-2.png?alt=media

Segmented buttons with M2 color mappings, all caps text labels, boxy shape, and shorter height.

<p>M2: Segmented buttons had a small corner radius and label text in all caps</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fl20oj7ju-example.png?alt=media

Segmented buttons with M3 color mappings, sentence case text labels, fully round shape, and taller height.

<p>M3: Segmented buttons have fully rounded corners, sentence-case text, different height, and new color mappings</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7ruslm-4.png?alt=media

## Specs

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description"> Segmented buttons are no longer recommended in the Material 3 expressive update. For those who have updated, use the <a href="/m3/pages/button-groups/overview/" target="_blank">connected button group</a> instead, which has mostly the same functionality but with an updated visual design.</div></div></div>

Diagram of segmented button indicating 3 parts of its anatomy.

<ol><li>Container</li><li>Icon (optional for unselected state) </li><li>Label text</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6l9syf-1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/C6AHlXtNzhGMs8gghgCKSba6mwIpYO0fiDnecohrFF3YJraSvBsQL-eXZnCvQJIU9AqRNgtrrvetX0I4UXwI1JyPxy4_rLYmSlkmsr73D_o=s2048

<h2>Tokens and specs</h2>

<p>Browse the component elements, attributes, tokens, and their values. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/67e2613d87ca6f98

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2 id="isPasted">Color</h2><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" id="isPasted" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

Diagram of segmented button indicating its color mappings

<p>Segmented button color roles used for light and dark schemes:</p><ol><li>On surface</li><li>Outline</li><li>Secondary container</li><li>On secondary container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6lafzx-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/YDundjWkMlYTm9ZC1RERNdV1PS0i86yel8Qe8OjWM7OEoMRC2frzBJzmqAywQu1BSW2eAP2ITtJk4A5aKZTS8GtaMqkR4uipO8VZMqGvMzAg=s2048

<h2>States</h2><p><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element> are visual representations used to communicate the status of a component or interactive element.  <a href="/m3/pages/interaction-states/overview" id="isPasted" target="_blank" rel="noopener noreferrer">Learn more about interaction states</a></p>

<h3 id="isPasted">Unselected</h3>

Side by side view of segmented buttons with 5 unselected states.

<p id="isPasted">Unselected button states:</p><ol><li>Enabled </li><li>Disabled </li><li>Hovered </li><li>Focused </li><li>Pressed</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6law70-3b.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-uNJiGxEkqwavKi0rqCcQ6_NTV7HdAQ9_eZ9b40fw_6Ij00V60BU3iLu88EgzvFUO0prwPdmKRKoc6KiuVmTZLUTsStYc8PArd4Y2C6G6ts=s2048

<h3>Selected</h3>

Side by side view of segmented buttons with 4 selected states.

<p>Selected button states:</p><ol><li>Selected </li><li>Hovered on selected</li><li>Focused on selected</li><li>Pressed on selected</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6lbdzb-4b.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/PMYMRAaXu4kiEdyI_9iuWFzh9CDRnmy7VqZ7H34w8Y2jeJy0KUUZekkTUR35ISHPJxnChOXSeLwkG2VHsL8vT3CayNNfqNbNr1ptUwhBbG4=s2048

<h2>Measurements</h2>

Diagram indicating layout values, paddings, and target size for segmented buttons

<ol><li>Padding and container size </li><li>Target size</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmp8rn0c-5-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/0shX8UYtu_19Pa79pXEjmEc2GW6UOTINXPAw9K9HoaRUWiUqDJsLbSBiPTvL3Nd315qjZapICkjO0AaTXM93Vx9H_0EOocZddx1YsbmzG38_=s2049

<div class="table-wrapper"><table border="1" cellpadding="0" cellspacing="0" dir="ltr" style="margin-right:calc(0%);width:100%"><thead><tr><th style="text-align:center">Attribute</th><th style="text-align:center">Value</th></tr></thead><tbody><tr><th>Container width<br /></th><td>Dynamic based on labels</td></tr><tr><th>Segment width</th><td>Container width / total segments (Example: 1/3)</td></tr><tr><th>Height<br /></th><td>40dp</td></tr><tr><th>Outline width</th><td>1dp</td></tr><tr><th>Label alignment<br /></th><td>Center</td></tr><tr><th>Left/right padding<br /></th><td>Min 12dp</td></tr><tr><th>Padding between elements<br /></th><td>8dp</td></tr><tr><th>Target size</th><td>48dp</td></tr></tbody></table></div>

<h3>Density</h3><p>Density can be used in denser UIs where space is limited. Density is only applied to the height. </p>

Side by side view of segmented buttons with 4 different density heights

<p>Each step down in density removes 4dp from the height</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6lc5hl-6.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/gaOReQpJgFqk-nmLLFHu7hpIFV9BQ6hqnVt8oSC0ZsgpMaeDzc9y-FIcDnkTciniAxMCpPfWD4RMFaEsz33-jSVweXp8mTxgiiL1tPiAATSUWw=s1352

<h2>High contrast</h2>

<p>High contrast mode is an <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/accessibility/overview" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> feature that aims to maximize legibility by using a limited color palette. </p>

Side by side view of segmented buttons in high contrast mode

<ol><li>Enabled </li><li>Selected </li><li>Focused</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6lcjus-7.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-uwWm7CjTlWXCcMBqm78wd4vIsq9kPWr90b6Lq06IVUuejN_KLmjvXil514E2P5wCZr8X2G6k-sHNsfV39zOWwkqWFC7dw-smjpwT7oR1b0=s1352

## Guidelines

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">Segmented buttons are no longer recommended in the Material 3 expressive update. For those who have updated, use the <a href="/m3/pages/button-groups/overview/" target="_blank">connected button group</a> instead, which has mostly the same functionality but with an updated visual design.</div></div></div>

Two types of segmented buttons.

<ol><li>Single-select </li><li>Multi-select</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7mlxdq-1.png?alt=media

<h2>Usage</h2>

<p>Segmented buttons help people select options, switch views, or sort elements.</p>

A segmented button for switching between restaurants and bar options. 

<p>A segmented button can help switch between viewing restaurant and bar options</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7mnnk2-2.png?alt=media

<p>There are 2 variants of segmented buttons:</p><ol class="decimal"><li><p>Single-select</p></li><li><p>Multi-select</p></li></ol>

Side by side view of single and multi-select segmented buttons

<ol><li>Single-select segmented button can only have 1 segment selected</li><li>Multi-select segmented button can have multiple segments selected</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7mz9ev-3.png?alt=media

<h2>Anatomy</h2>

Diagram of segmented button indicating 5 parts of its anatomy

<ol><li>Segment</li><li>Container</li><li>Icon (optional)</li><li>Label text (optional)</li><li>Selected icon</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7n59nt-4.png?alt=media

<h3>Segments</h3><p>Segmented buttons can have 2-5 segments. Each segment is clearly divided and contains label text, an icon, or both.</p>

Side by side view of segmented buttons each with additional segment starting from 2 to 5

<p>There can be anywhere from 2 to 5 segments in single-select and multi-select segmented buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7nap4m-5.png?alt=media

Mobile UI of data usage screen with segmented button

<p>Segmented buttons are best used for selecting between 2 and 5 choices</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7ngd39-6_do.png?alt=media

Incorrect use of segmented button with 6 segments

<p>Don’t use more than five segments in a single segmented button. Choices should be scoped. If you have more than five choices, consider using another component, such as chips.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7o4u2i-7_dont.png?alt=media

<h3>Container</h3><p>Like <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label link-url should-open-link-in-new-tab="true">common buttons</app-froala-tooltip-element>, segmented buttons have fully rounded corners by default.</p>

Close up detail of segmented button with fully rounded corners

<p>Segmented buttons have fully rounded corners</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7o7un8-8.png?alt=media

<h3>Icons</h3><p id="isPasted">Icons may be used as labels by themselves or alongside text. </p><p>If an icon is used without label text, it must clearly communicate the option it represents. </p>

Side by side view of segmented buttons with different configurations of icons and label text

<p>Segmented buttons can include icons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7okkk9-9.png?alt=media

<h3>Label text</h3><p id="isPasted">Labels should be short and succinct. If a label is too long to fit within its segment, consider using an icon alone.</p>

Mobile UI of music app showing a segmented button with options for music, albums, podcasts

<p>Use labels that are as clear and short as possible</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7omu8a-10.png?alt=media

Segmented button with options for day, week, month

<p>Keep labels short and consistent in length</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7pqz1e-11_do.png?alt=media

Segmented button with 4 segments. 3 are next to each other. The 4th is wrapped on a new line.

<p>Don’t allow segments to wrap onto a new line</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7prory-12_dont.png?alt=media

Segmented button with text labels reading day, week, month

<p>Use consistent label types</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7psieh-13_do.png?alt=media

Segmented button with icons only labels for walking, transit, driving

<p>Icons can be used in place of labels, but they must clearly communicate their meaning</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7pt9gl-14_caution.png?alt=media

Segmented button with 2 icon only options indicating favorite and bookmark and 3rd option with text label reading recent

<p>Avoid mixing icon-only labels with text labels. Choose one label type and use that type for all segments.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7ptzzf-15_dont.png?alt=media

<h2>Single-select</h2>

<p id="isPasted">Use a single-select segmented button to select one option from a set, switch between views, or sort elements from up to five options. </p><p>For example, use a single-select segmented button to choose one of a set of sizes, such as this beverage size selector.</p>

Mobile UI for ecommerce app with segmented button with 3 beverage size options

<p>A single select segmented button for choosing beverage size</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7puwq3-16.png?alt=media

<h2>Multi-select</h2>

<p id="isPasted">Use a multi-select segmented button to select or sort from two to five options. Unlike single-select, selection is not required and a user may concurrently select anywhere from all to none of the options. </p><p>For example, multi-select segmented buttons can be used to filter by price range when searching for a restaurant. </p>

Mobile UI for ecommerce app with multi-select segmented button with 4 price range options 

<p>A multi-select segmented button for filtering restaurant search options</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7pvpf7-17.png?alt=media

<h2>Placement</h2>

<p>Segmented buttons should have adequate <app-froala-tooltip-element description="Margins are the spaces between the edge of a nested element and its parent element, such as the space between a button's label text and the edge of its container." link-label="More on margins" link-url="/m3/pages/spacing/overview" should-open-link-in-new-tab="true">margins</app-froala-tooltip-element> from the edge of the viewport or frame. </p><p>On larger screens, set a maximum padding for all button segments so the set doesn't fill the screen.</p>

Mobile UI with 2-segment segmented button and 4-segment segmented button each with same margins to the viewport edge.

<p>Allow adequate space for margins. The button container shouldn’t reach the edge of the viewport.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7pwh9i-18.png?alt=media

Game store UI with a segmented button the proper width

<p><span style="white-space:pre-wrap">Set a maximum padding within the segments to ensure usability on larger screens</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7pxu9q-18-a_do.png?alt=media

Game store UI with a segmented button improperly spanning the entire width of the screen

<p><span style="white-space:pre-wrap">Don’t allow segmented buttons to span the full width of larger screens or panes. This can leave too much padding on either side of the segment label, making the button less usable.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7pyzy1-18-b_dont.png?alt=media

<p>Segmented buttons can be placed on other components, such as <app-froala-tooltip-element description="Bottom sheets show secondary content anchored to the bottom of the screen." link-label="More on bottom sheets" link-url="/m3/pages/bottom-sheets/overview" should-open-link-in-new-tab="true">bottom sheets</app-froala-tooltip-element> or <app-froala-tooltip-element description="Full-screen dialogs fill the entire screen, displaying actions that require a series of tasks to complete. They're often used for creating a calendar entry." link-label link-url should-open-link-in-new-tab="false">full-screen dialogs</app-froala-tooltip-element>. </p>

Mobile UI with segmented button in bottom sheet

<p>A segmented button can be placed on a bottom sheet</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7q0vrm-19.png?alt=media

<h2>Behavior</h2>

<p>When using both icons and label text in segmented buttons, the icon label is replaced by the checkmark icon when the segment is selected. </p>

Segmented button with icon and text labels with checkmark icon in selected segment

<p>Icons become checkmarks when selected in buttons that also use label text</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmq6a9huq-GM3%20-%20Buttons%20-%20Segmented%20Buttons%20-%20Guidelines%2001%20-%20IA%20-%20v02.mp4?alt=media

## Accessibility

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">Segmented buttons are no longer recommended in the Material 3 expressive update. For those who have updated, use the <a href="/m3/pages/button-groups/overview/" target="_blank">connected button group</a> instead, which has mostly the same functionality but with an updated visual design.</div></div></div>

<h2>Use cases</h2>

<p><span style="white-space:pre-wrap">Users should be able to:</span></p><ul><li><span style="white-space:pre-wrap">Navigate to and activate segmented buttons with assistive tech</span></li><li><span style="white-space:pre-wrap">Understand what each segment selection will do</span></li></ul>

<h3>Interaction &amp; style</h3><p>For keyboard navigation, <strong>Tab</strong> navigates to the button, and arrow keys navigate between the individual segments.</p><p>For single-select segments, <strong>Space</strong> or <strong>Enter</strong> will select or unselect the <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/google-material-3/pages/interaction-states/applying-states#bfc1624f-6bcc-4306-b0c1-425e2d8a1bf9" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element> segment. </p><p>For multi-select segments, <strong>Space</strong> or <strong>Enter</strong> will:</p><ul type="disc" style="list-style-type:disc"><li><p>Select an unselected segment</p></li><li><p>Select all of the segments</p></li><li><p>Unselect a selected segment </p></li></ul>

Tab moves the focus through segments of a segmented button.  Space or enter selects and unselects segments.

<p>Use <strong>Tab</strong> to navigate through segments, and <strong>Space </strong>or <strong>Enter</strong> to select and unselect</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7q4935-1.png?alt=media

<h3>Color contrast</h3><p id="isPasted">Segmented buttons are clusters of similar components, so the outline should have at least a 3:1 contrast ratio with the background or surface. This helps distinguish each button.</p><p>Both a checkmark icon and a color change are used to distinguish selection. Make sure color isn’t the only way to show selection.</p>

The outline of segmented buttons on the surface passes the minimum contrast of 3:1.

<p id="isPasted">Use an outline with a surface contrast of at least 3:1</p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7q6k39-2_do.png?alt=media

The outline of segmented buttons on the surface fails the minimum contrast of 3:1.

<p>The segmented button shouldn't have a contrast outline less than 3:1</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7q87p2-3_dont.png?alt=media

<h3 id="isPasted"><span style="white-space:pre-wrap">Initial focus</span></h3><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">Focus will start in the first segment. Depending on the direction of the language, it is either the most left or the most right segment.</span></span></p><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">For single select and multi-select, the first segment will be focused regardless of selection state.</span></span></p>

Segmented button focus starts on the left for left-to-right languages and on the right for right-to-left languages.

<p><span style="white-space:pre-wrap">Focus begins on the left for left-to-right languages and on the right for right-to-left languages</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7q9t4x-4.png?alt=media

<h3 style="text-align:left">Keyboard navigation</h3><div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:28.5379%;text-align:left"><p>Keys</p></th><th style="width:71.4031%;text-align:left"><p>Actions</p></th></tr></thead><tbody><tr><td><p><strong>Tab</strong></p></td><td><p>Navigate between buttons</p></td></tr><tr><td><p>Arrow keys</p></td><td><p>Navigate inside the component</p></td></tr><tr><td><p><strong>Space</strong> or <strong>Enter</strong></p></td><td><p>Activate a focused button</p></td></tr></tbody></table></div>

<h3><span style="white-space:pre-wrap">Labeling elements</span></h3><p>The <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview/principles" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> label for a segmented button comes from the visible label text on such as <strong>Relevance</strong> and <strong>Distance</strong>.<span style="white-space:pre-wrap"> <br /><br />If the segmented button displays icons without label text, the accessibility label describes the action that the button is expressing, such as <strong>Inexpensive</strong> for one currency symbol.</span></p>

The the text and accessibility role for the left-most section of a segmented button following “sort by” is  is “relevance.”

<p><span style="white-space:pre-wrap">The label for segmented button matches the text label</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7qcq3h-5.png?alt=media

<p id="isPasted">Single-select segmented buttons behave like <app-froala-tooltip-element description="Radio buttons let people select one option from a set of options." link-label="More on radio buttons" link-url="/m3/pages/radio-button/overview" should-open-link-in-new-tab="true">radio buttons</app-froala-tooltip-element>: only one option can be selected at a time. The label is <strong>Radiogroup</strong>.</p><p>Multi-select buttons behave like <app-froala-tooltip-element description="Checkboxes let users select one or more items from a list, or turn an item on or off." link-label="More on checkboxes" link-url="/m3/pages/checkbox/overview" should-open-link-in-new-tab="true">checkboxes</app-froala-tooltip-element>: more than one option can be selected. The label is <strong>Checkbox</strong>.</p>

Selected price range segmented buttons range from $ to $$$$. The accessibility label of the $ button is “inexpensive.”

<p><span style="white-space:pre-wrap">The role for the multi-select segmented button is <strong>Checkbox</strong></span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw7qpwe0-6.png?alt=media
