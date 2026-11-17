# Tabs

Source: https://m3.material.io/components/tabs
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/f37f47ba-8e67-4f1e-98a3-3bea94879e52.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Use tabs to group content into helpful categories</p></li><li><p>Two variants: <app-froala-tooltip-element description="Primary tabs display an app's main content destinations. They're are placed at the top of the screen, often under a top app bar." link-label link-url should-open-link-in-new-tab="false">primary</app-froala-tooltip-element> and <app-froala-tooltip-element description="Secondary tabs display related content within a content area. They're always placed below primary tabs." link-label link-url should-open-link-in-new-tab="false">secondary</app-froala-tooltip-element></p></li><li><p>Tabs can horizontally scroll, so a UI can have as many tabs as needed</p></li><li><p>Place tabs next to each other as peers</p></li></ul>

A bar of primary tabs with destinations labeled Flights, Trips, and Explore. And a bar of secondary tabs with destinations labeled Overview and Specifications

<ol><li>Primary tabs</li><li>Secondary tabs</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2kfqg9k-1.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/26aa7eca29c81c71

libraryModuleType: STATUS_TABLE

<h2>Differences from M2</h2>

<ul><li>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></li><li>Layout: Icons and labels are now vertically centered within the container</li></ul>

Bar of primary tabs with destinations labeled Flights, Trips, and Explore

<p>Tab icons and labels are positioned in the vertical center of the container</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k3okei-2.png?alt=media

## Specs

<h2>Tokens and specs</h2><p>Select a component variant below to see its elements, attributes, tokens, and their values.</p>

resourceName: designSystems/20543ce18892f7d9/components/6039f0080a95df1e

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Tabs - Primary navigation', 'Tabs - Secondary navigation'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['Tabs - Primary navigation', 'Tabs - Secondary navigation'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Primary tabs</h2>

6 elements of primary tabs.

<ol><li id="isPasted">Container</li><li>Badge (optional)</li><li>Icon (optional)</li><li>Label</li><li>Divider</li><li>Active indicator</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2lequcy-1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/0bS99kVjUnrfIUIKGAMWl8zeoYciELsgT5jPWeC4JJ9gcDC2cfnKH-p9qOYsX0OJ000ePPYMARw_YXMtax_UeITNCH-W5hn03wKl-nl0Al9scw=s2048

<h3>Primary tabs color</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true" id="isPasted">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

7 color roles applied to primary tabs in light and dark themes.

<p id="isPasted">Primary tab color roles used for light and dark schemes:</p><ol><li id="isPasted">Surface</li><li>Primary</li><li>Primary</li><li>On surface variant</li><li>On surface variant</li><li>Outline variant</li><li>Primary</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2lerpx7-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/dmXLWuK2u_6U_iIQaK_nWtayfYfcfZU6mZyf5IAPmgu9y14-Puo51QN7a74fZJ34z0ESD88OfHOvUOFcnTpSARGU9yDXHPUQrcBqledF6BA=s2048

<h3>Primary tabs states</h3>

Diagram of all primary tab states in both light and dark mode

<ol><li id="isPasted">Enabled (active destination)</li><li>Hover (active destination)</li><li>Focused (active destination)</li><li>Pressed (active destination)</li><li>Enabled (inactive destination)</li><li>Hover (inactive destination)</li><li>Focused (inactive destination)</li><li>Pressed (inactive destination)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8t9w5tr-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/SVFdAJr5_8cGN6FTMVabD3nie8TwI7380y6PuVzSxatYH1YBsdf49aWd1upXNO7uDcsKDd8Uge2WtDUPtTtnuFCKKgIk-q6iraC6rfP8bcY=s2048

<h2>Secondary tabs</h2>

5 elements of secondary tabs.

<ol><li id="isPasted">Container</li><li>Badge (optional)</li><li>Label</li><li>Divider</li><li>Active indicator</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2letsf5-4.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/kyON5nMIlowboe0XsmPdlYKlFdIzCFTab9gzT4uEJtS2WMvRd1uBJHEMDDOKujs1u1iJYlb66cSc7LBfMuN9F3HRwocQhsYw0wvUW2lQxuBM=s2048

<h3>Secondary tabs color</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true" id="isPasted">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

5 color roles applied to secondary tabs in light and dark themes.

<p id="isPasted">Secondary tab color roles used for light and dark schemes:</p><ol><li>Surface</li><li>On surface</li><li>On surface variant</li><li id="isPasted">Outline variant</li><li>Primary</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2leuvo3-5.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/mrLdFHBC7H_M0bhZxPDT-VaJeoB01vnZMaY_9Pyj_EenTQbIT6OO75CWFdZLyvMxD0ycppRCoWXustGmsKh3K3M8CALUwNj7knXGU6JyrGb5=s2048

<h3 id="isPasted">Secondary tabs states</h3>

Diagram of all secondary tab states in both light and dark mode

<ol><li>Enabled (active destination)</li><li>Hover (active destination)</li><li>Focused (active destination)</li><li>Pressed  (active destination)</li><li>Enabled (inactive destination)</li><li>Hover (inactive destination)</li><li>Focused (inactive destination)</li><li>Pressed (inactive destination)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8t9wue2-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/oEbOwsXXP2m1EE9Sh7tJFcTP1GIHVkX6lbOkKN-gdwnF4WbJnoyezqHEr1rtaeAPTY2cHj6txNpy91YgYRVCBqht87aUU6VlIwJg1rnvvniy=s2048

<h2>Measurements</h2>

Diagram of measurements for four and two tabs per container, including icon and label placement.

<p>Tabs are divided into equal sections, with labels and icons positioned vertically centered. The divider is included in the height, placed inside the container.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm92tisv3-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/KNDnEXfu6HZxqBLD84eQfamUeoe8b_N3wygSYqpk5Hq1MxT7_9RNL34wYce0tPDml6rb6lP7cQO8lYhxEcPOOXIGAmb3ArqY-ay-lDUzbqoW=s2048

Diagram of Primary tab active indicator measurements.

<p>Primary tab active indicators are inset 2dp on each side, have a fully rounded corner radius, and a minimum length of 24dp.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm92thj1h-08-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/lEVgg_QRIKA7HpYLAWEddeY7ZCHa5FmlPc1K3C0yx1c5cmW_wxci7cAmdW_55RvUextO4vEHupXxMrWXSna4BHfO7UcWU9Q_QKrk2LESoMbVoA=s2048

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="text-align:center">Attribute<br /></th><th style="text-align:center">Value<br /></th></tr></thead><tbody><tr><td>Container height (label text only)</td><td>48dp</td></tr><tr><td>Container height (icon and label text)</td><td>64dp</td></tr><tr><td>Icon size</td><td>24dp</td></tr><tr><td>Divider height</td><td>1dp</td></tr><tr><td>Primary active indicator height</td><td>3dp</td></tr><tr><td>Secondary active indicator height</td><td>2dp</td></tr><tr><td>Active indicator shape</td><td>3, 3, 0, 0</td></tr><tr><td>Active indicator minimum length</td><td>24dp</td></tr><tr><td>Padding between inline icon and text</td><td>8dp</td></tr><tr><td>Padding between inline text and badge</td><td>4dp</td></tr><tr><td>Overlap of badge on stacked icon</td><td>6dp</td></tr></tbody></table></div>

## Guidelines

<h2 id="isPasted" style="text-align:left">Usage</h2>

<p><span style="white-space:pre-wrap">Tabs organize groups of related content that are at the same level of hierarchy.</span></p>

Mobile screen with 3 tabs: video, photos and audio. Each tab has an an icon and text.

<p>Tab labels can include icons and text. Text labels should be short.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k0hhto-1.png?alt=media

<p>There are two variants of tabs:</p><ol class="decimal"><li><p>Primary tabs</p></li><li><p>Secondary tabs</p></li></ol><p>Primary tabs are placed at the top of the content <app-froala-tooltip-element description="Panes are layout containers that house other components and elements within a single app. A pane can be: fixed, flexible, floating, or semi permanent." link-label="More on panes" link-url="/m3/pages/understanding-layout/parts-of-layout#667b32c0-56e2-4fc2-a618-4066c79a894e" should-open-link-in-new-tab="true">pane</app-froala-tooltip-element> under an <app-froala-tooltip-element description="App bars display information and actions at the top of a screen." link-label="More on app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">app bar</app-froala-tooltip-element>. They display the main content destinations.<br /><br />Secondary tabs are used within a content area to further separate related content and establish hierarchy.</p>

3 primary tabs above 3 secondary tabs.

<ol><li>Primary tabs
</li><li>Secondary tabs</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2neyv4z-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/idzlIeuy-TH2VM7D0-YvIt28GrEONuzYVwq1Ov4RBs_p3MNmu4Ji52Zx-_b5-AtLHAGyXOiXeTMrQtrkiTwGcyThOwwaKtQc8NbP-UNUpDG_=s1352

<h3><span style="white-space:pre-wrap">Related content<br /></span></h3><p><span style="white-space:pre-wrap">Use tabs to group related content, not <em>sequential</em> content.</span></p>

Scrolling up and down through content, then swiping left through tabs.

<p>Utilize tabs to categorize related groups of content into clearly defined sets</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k0jkg6-3.png?alt=media

Mobile screen with scrollable tabs of sequential content: Chapter 1, Chapter 2, Chapter 3 and Chapter 4.

Don’t use tabs to move through sequential content that needs to be read in a particular order. Instead, create hierarchy within the content using techniques like typography style and open space.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k0jyu3-4.png?alt=media

<h2><span style="white-space:pre-wrap">Anatomy</span></h2>

Six components of tabs.

<ol><li>Container</li><li>Icon (optional)</li><li>Badge (optional)</li><li>Label</li><li>Divider</li><li id="isPasted">Active indicator</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k0lum1-5.png?alt=media

<h3 id="isPasted"><span style="white-space:pre-wrap">Container</span></h3><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">The container holds multiple tabs. Its contents can be fixed or scrollable.<br /><br />The container should always extend the full width of the window and be divided into equal sections, one for each tab.<br /><br /></span></span>The container is defined by a <app-froala-tooltip-element description="Dividers are thin lines that group content in lists or other containers." link-label="More on dividers" link-url="/m3/pages/divider/overview" should-open-link-in-new-tab="true">divider</app-froala-tooltip-element> on the bottom edge to separate it from the content below. Content may scroll under the container.</p>

Mobile screen with fixed tabs with a dotted border to illustrate the container area.

<p><span style="white-space:pre-wrap">The container is the area that contains the tabs directly under the title above</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k0mdfv-6.png?alt=media

<h3>Icon (optional)</h3><p>Icons communicate the kind of content within a tab. Icons should be simple and recognizable.</p>

Mobile screen with tabs that use both icons and labels.

<p>Tabs can use a combination of labels and icons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k0o3dw-7.png?alt=media

<p id="isPasted">Icons alone aren’t as effective as text labels at communicating complex content.<br id="isPasted" /><br />Use caution when representing tab content with icons alone, as an icon’s meaning may not be clear.</p>

Mobile screen with tabs represented by icons  for “wishlist” and “location”.

<p>Use icons that are globally recognized when using icons alone</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k0sbsy-8.png?alt=media

Mobile screen where "purchases” tab has text only and “wishlist” tab has text and icon.

<p>Don’t use tabs with both icons and text labels on only some tabs, but not others</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k0t3i6-9.png?alt=media

<h3 id="isPasted"><span style="white-space:pre-wrap">Label</span></h3><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">Text labels should clearly and succinctly describe the content within the tab.<br /><br />Tab labels appear in a single row. Labels can use a second line if needed, with truncated text. Alternatively, scrollable tabs can allow room for longer titles.</span></span></p>

Mobile screen with scrollable tabs in a single row.

Tab labels should be short and succinct. There should be a clear relationship to the title above.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k1942z-10.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">When using scrollable tabs, the first visible tab should be offset by 52dp from the left side of the device for both web and mobile. The width of each tab is defined by the length of its text label.</span></p><p><span style="white-space:pre-wrap">Avoid using inconsistent padding on each tab.</span></p>

Screen with scrollable tabs offset from the leading edge by 52dp.

<p>Offset the first scrollable tab 52dp from the leading edge so it's clear that more content is available</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k19jjz-11.png?alt=media

Screen with scrollable tabs, 2 of which are truncated to “Australian” showing how truncation can confuse users.

<p>Don’t truncate labels unless required, as truncated text can impede comprehension</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k1a0sc-12.png?alt=media

<h3 id="isPasted">Badges (optional) </h3><p id="isPasted"><app-froala-tooltip-element description="Badges show notifications, counts, or status information on navigation items and icons." link-label="More on badges" link-url="/m3/pages/badges/overview" should-open-link-in-new-tab="true">Badges</app-froala-tooltip-element> can be used on primary or secondary tabs to show notifications or updates related to a specific tab. Limit badge content to four characters, including a "+".</p><p>Once the user views the relevant content in the tab, the badge value should update or the badge should disappear entirely.</p><p>Small and large badges can both be used with tabs. Read the <a href="/m3/pages/badges/overview" target="_blank" rel="noopener noreferrer">badge guidance</a> for more details. </p>

Mobile screen with tabs that use both icons and labels.

<p>Badges are used to highlight notifications related to tab specific content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k1yl6w-13.png?alt=media

<h3 id="isPasted"><span style="white-space:pre-wrap">Active indicator</span></h3><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">To differentiate an active tab from an inactive tab, apply an underline and color change to the active tab’s text and icon.</span></span></p>

Selecting a tab creates an underline below the  icon and text, both which have changed color to show the tab is active.

<p>An underline and color change differentiate an active tab from the inactive ones</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60drx93-GM3-Components-Tabs-Guidelines-1-v01.mp4?alt=media

<h2>Choosing the tab variant</h2>

<p><app-froala-tooltip-element description="Primary tabs display an app's main content destinations. They're are placed at the top of the screen, often under a top app bar." link-label link-url should-open-link-in-new-tab="false">Primary tabs</app-froala-tooltip-element> should be used when just one set of tabs are needed.</p><p><app-froala-tooltip-element description="Secondary tabs display related content within a content area. They're always placed below primary tabs." link-label link-url should-open-link-in-new-tab="true">Secondary tabs</app-froala-tooltip-element> are necessary when a screen requires more than one level of tabs. These tabs use a simpler style of indicator, but their function is identical to primary tabs.</p>

Mobile screen with primary tabs near the top of the screen.

<p>Tabs can be joined with components like app bars, embedded in a specific UI region, or nested within components like cards and sheets. Tabs control the UI region displayed below them.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k20o4c-15.png?alt=media

<h2><span style="white-space:pre-wrap">Placement</span></h2>

<p><span style="white-space:pre-wrap">Tabs are displayed in a single row, with each tab connected to the content it represents. As a set, all tabs are unified by a shared topic.<br /><br /></span><app-froala-tooltip-element description="Secondary tabs display related content within a content area. They're always placed below primary tabs." link-label link-url should-open-link-in-new-tab="false">Secondary tabs</app-froala-tooltip-element> should always be placed below <app-froala-tooltip-element description="Primary tabs display an app's main content destinations. They're are placed at the top of the screen, often under a top app bar." link-label link-url should-open-link-in-new-tab="false">primary tabs</app-froala-tooltip-element>.</p>

Mobile screen with secondary tabs below the primary tabs.

<p>Secondary tabs are found within other content to assist users with greater detail</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k217y6-16.png?alt=media

<h2><span style="white-space:pre-wrap">Responsive layout</span></h2>

<p>For fixed tabs, the maximum width for each tab should be determined by the width of the widest tab. The group of tabs should use a fluid <app-froala-tooltip-element description="Margins are the spaces between the edge of a nested element and its parent element, such as the space between a button's label text and the edge of its container." link-label="More on margins" link-url="/m3/pages/understanding-layout/spacing#38a538d7-991f-4c39-8449-195d32caf397" should-open-link-in-new-tab="true">margin</app-froala-tooltip-element> and align to the center or leading edge of the body region.</p><p><span style="white-space:pre-wrap" id="isPasted">Avoid using more than four tabs at once. At five or more tabs, the container becomes cramped.</span></p>

Four fixed tabs spaced to match one another.

<p>Tabs can grow in width in relation to the number of items contained within</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm6fa9q27-17.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/FyF1DB36V4-1BUcdhWode9xWyMAv8dxbQI41nyqeelttSpQive9jjYbxjC6qmmZCq7-7OKSAtlkWeFG0ufcBT-KVUFHAniHePE3F4ZcTy382=s1352

<h2><span style="white-space:pre-wrap">Behavior</span></h2>

<h3><span style="white-space:pre-wrap">States</span></h3><p>By default, tabs inherit <app-froala-tooltip-element description="An enabled state communicates an interactive component or element." link-label="More on enabled state" link-url="/m3/pages/interaction-states/applying-states#39b2fc90-01db-41b5-b6f8-47be61ed1479" should-open-link-in-new-tab="true">enabled</app-froala-tooltip-element> <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/google-material-3/pages/interaction-states/overview" should-open-link-in-new-tab="true">states</app-froala-tooltip-element> with one active state.The inactive and active states of a tab can inherit a <app-froala-tooltip-element description="A hover state communicates when a user has placed a cursor above an interactive element." link-label="More on hover state" link-url="/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844" should-open-link-in-new-tab="true">hover</app-froala-tooltip-element>, <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f" should-open-link-in-new-tab="true">focus</app-froala-tooltip-element>, and <app-froala-tooltip-element description="A pressed state communicates a user tap." link-label="More on pressed state" link-url="/m3/pages/interaction-states/applying-states#c3690714-b741-492d-97b0-5fc1960e43e6" should-open-link-in-new-tab="true">pressed</app-froala-tooltip-element> states. </p>

Four states of a tab.

<p>Active, hover, focused, and pressed states</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k2312r-18.png?alt=media

<h3><span style="white-space:pre-wrap">Fixed tabs</span></h3><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">Fixed tabs display all tabs in a set simultaneously. They are best for switching between related content quickly, such as between transportation methods in a map. To navigate between fixed tabs, tap an individual tab, or swipe left or right in the content area.</span></span></p>

Mobile screen with fixed tabs, text only.

<p>Fixed tabs allow users to see all possible kinds of content available</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60dtw9m-GM3-Components-Tabs-Guidelines-2-v01.mp4?alt=media

<h4><span style="white-space:pre-wrap">Tap a tab</span></h4><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">Navigate to a tab by tapping on it.</span></span></p>

Tapping a tab selects it.

<p>Tapping on a tab directly</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60duq4j-GM3-Components-Tabs-Guidelines-3-v01.mp4?alt=media

<h4><span style="white-space:pre-wrap">Swipe within the content area</span></h4><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">To navigate between tabs, users can swipe left or right within the content area.</span></span></p><p><br /></p>

Swiping left or right on the content area moves the focus between fixed tabs.

<p>Users can swipe between fixed tabs to see related content quickly</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60dvuo4-GM3-Components-Tabs-Guidelines-4-v01.mp4?alt=media

<p>Use caution when placing other swipeable content (such as interactive maps or <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> items) in the content area.</p>

Scrolling up and down through content, then swiping left through tabs.

<p>Use different gesture directions when using tabs</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60dwpex-GM3-Components-Tabs-Guidelines-5.1-v01.mp4?alt=media

Swiping to change tabs accidentally swipes to delete a list item in the UI instead.

<p>Avoid placing swipeable items in the content area of a UI that has tabs, as the user may mistakenly swipe the wrong component</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60dxhwe-GM3-Components-Tabs-Guidelines-5.2-v01.mp4?alt=media

<h3><span style="white-space:pre-wrap">Scrollable tabs</span></h3><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">When a set of tabs cannot fit on screen, use scrollable tabs. Scrollable tabs can use longer text labels and a larger number of tabs. They are best used for browsing on touch interfaces.</span></span></p>

Scrolling left and right on scrollable tabs.

<p>Padding should remain the same when using scrolllable tabs and long labels</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60dygta-GM3-Components-Tabs-Guidelines-6-v01.mp4?alt=media

<h3><span style="white-space:pre-wrap">Scrolling content</span></h3><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">When a screen scrolls up and down through content, tabs can either be fixed to the top of the screen, or scroll off the screen. If they scroll off the screen, they will return when the user scrolls upward.</span></span></p>

Scrolling through content with fixed tabs  at top of the screen.

<p>Tabs can be use to create elevation</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60dz0ae-GM3-Components-Tabs-Guidelines-7-v01.mp4?alt=media

<p>  </p>

When scrolling up through content, tabs scroll off screen, then reappear when scrolling back down.

<p>Tabs can scroll offscreen on scroll, and reappear when the page is scrolled up</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60dztv7-GM3-Components-Tabs-Guidelines-8.1.mp4?alt=media

When scrolling up through content, tabs scroll behind the app bar then reappear when scrolling back down.

<p>Don’t scroll tabs behind an app bar. When tabs are attached to a component, they should appear and move as a single unit.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60e0d2q-GM3-Components-Tabs-Guidelines-8.2.mp4?alt=media

## Accessibility

<h2>Use cases</h2>

<p><span style="white-space:pre-wrap">Users should be able to:</span></p><ul><li><span style="white-space:pre-wrap">Undertake actions or invoke navigation to a new destination with assistive tech</span></li><li><span style="white-space:pre-wrap">Select an action or destination from an off screen tab with assistive tech</span></li><li>Maintain access of primary actions when the content is in a scrolled <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">state</app-froala-tooltip-element></li></ul>

<h2>Interaction &amp; style</h2>

<p><strong>Touch</strong></p><ul><li>When a user taps on an <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon button</app-froala-tooltip-element>, a touch ripple appears, indicating interaction feedback</li><li>The selected indicator becomes active and shifts into position once the touch has been engaged</li></ul>

The ripple effect resulting from tapping on an action item.

<p>Touch: Tap</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60bkpen-GM3-Components-Tabs-Accessibility-1-v01.mp4?alt=media

<p><strong>Scrollable</strong></p><ul><li>When a set of tabs cannot fit on screen, scrollable tabs are used. They are best used for browsing on touch interfaces.</li><li>To navigate between scrollable tabs, users swipe the set left or right. Users can also use arrow/tab to navigate through.</li><li>It's <strong>not recommended</strong> to loop a tab set where it scrolls infinitely. This can trap users who are navigating linearly with a screen reader.</li><li>To select an individual tab, users tap or press space/enter.</li><li id="isPasted">Horizontal scrolling tabs meet accessibility requirements because they need to increase in width to respond to label text without affecting the layout, and horizontal scrolling is necessary to view those labels.</li></ul>

Swiping right and left scrolls through tabs when scrolling is enabled.

<p id="isPasted">Scrollable: Scrollable Tabs</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60bllqp-GM3-Components-Tabs-Accessibility-2-v01.mp4?alt=media

<p id="isPasted"><strong>Cursor</strong></p><ul><li>When hovered, the <app-froala-tooltip-element description="A hover state communicates when a user has placed a cursor above an interactive element." link-label="More on hover state" link-url="/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844" should-open-link-in-new-tab="true">hover state</app-froala-tooltip-element> appears, providing a visual cue that the <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon button</app-froala-tooltip-element> is interactive. When clicked (in both active and inactive states), a ripple appears and the indicator shifts into position, showing the user feedback.</li></ul>

Hover state appears when hovering over tabs, clicking on them changes the state to active. 

<p id="isPasted">Cursor: Hover, Click</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60bmbt7-GM3-Components-Tabs-Accessibility-3-v01.mp4?alt=media

<p id="isPasted"><strong>Keyboard/Switch </strong></p><ul><li>When tabbed, a focus indicator appears, providing a visual cue to the user that the destination is now selected</li><li>When the user engages with the selected tab via Space/Enter in active <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">states</app-froala-tooltip-element>, the user is taken to a new destination</li><li>Within the tab menu, the user is able to arrow/tab through the menu items, Space/Enter to select an item, or tab to exit the active state</li></ul>

Tabbing through navigation items. The focus indicator appears when an item is selected.

<p id="isPasted">Keyboard/Switch: Tab, Space/Enter, Arrow</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60bmwk8-GM3-Components-Tabs-Accessibility-4-v01.mp4?alt=media

<h3 id="isPasted">Avoid applying density by default</h3><p>Don't apply density to tabs by default — this lowers their targets below our best practice of 48x48 CSS pixels. Instead, give people a way to choose a higher density, like selecting a denser layout or changing the theme.</p><p>To ensure that this density setting can be easily reverted when it's active, keep all the targets to change it at minimum 48x48 CSS pixels each.</p>

<h2>Initial focus</h2>

<p>On arrow/tab in a tab <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element>, the active indicator appears on the first interactive element, providing feedback to the user that it is selected. The user is then able to tab to additional interactive elements until all available items are complete within the tab menu.</p>

Arrow or Tab being used to navigate through a tab menu.

<p id="isPasted">Use Arrow/Tab to navigate through items</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60bo0sa-GM3-Components-Tabs-Accessibility-5.1-v01.mp4?alt=media

Space or Enter being used to navigate through a tab menu.

<p id="isPasted">Don't use Space/Enter for navigating tabs. Space/Enter is only used for completing actions.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm60bot9i-GM3-Components-Tabs-Accessibility-5.2-v01.mp4?alt=media

<h2>Keyboard navigation</h2>

<div class="table-wrapper"><table id="isPasted" style="margin-right:calc(0%);width:100%"><thead><tr><th>Keys</th><th>Actions</th></tr></thead><tbody><tr><th>Arrow</th><td>Focus lands on the next available navigation destination</td></tr><tr><th>Space / Enter</th><td>Activates the <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element> navigation destination</td></tr><tr><th>Arrow</th><td>Allows navigation through <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element> items</td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<p>When the visible UI text is ambiguous, or there is no visible UI text, <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> labels need to be more descriptive. For example, an <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon button</app-froala-tooltip-element> that visually represents a “video camera” requires additional information in its accessibility label to clarify the icon’s intent.</p>

Small device screen  with the tab highlighted and the label and role illustrated.

<p>While the icon visually represents a “Video camera,” the accessibility label for this tab clarifies its function: “Video format media content”</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2k3h2mn-7.png?alt=media
