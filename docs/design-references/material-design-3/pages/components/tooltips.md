# Tooltips

Source: https://m3.material.io/components/tooltips
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/cb07b841-eae0-4959-bbab-25b1971714ca.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Use tooltips to add additional context to a <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">button</app-froala-tooltip-element> or other UI element</p></li><li><p>Two variants: <app-froala-tooltip-element description="Plain tooltips briefly describe a UI element. They're often used for labelling UI elements with no text, like icon-only buttons and fields." link-label link-url should-open-link-in-new-tab="true">plain</app-froala-tooltip-element> and <app-froala-tooltip-element description="Rich tooltips provide additional context about a UI element. They can optionally contain a subhead, buttons, and hyperlinks." link-label link-url should-open-link-in-new-tab="true">rich</app-froala-tooltip-element></p></li><li><p>Use plain tooltips to describe elements or actions of <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon buttons</app-froala-tooltip-element></p></li><li><p>Use rich tooltips to provide more details, like describing the value of a feature</p></li><li><p>Rich tooltips can include an optional title, link, and buttons</p></li></ul>

2 variants of tooltips.

<ol class="decimal"><li>Plain tooltip</li><li>Rich tooltip</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6q4295-01.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/1ddd05a1e6a16969

libraryModuleType: STATUS_TABLE

<h2>Differences from M2</h2>

<ul><li><p><strong>Color</strong>: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></p></li><li><p><strong>Shape</strong>: <app-froala-tooltip-element description="Rich tooltips provide additional context about a UI element. They can optionally contain a subhead, buttons, and hyperlinks." link-label link-url should-open-link-in-new-tab="true">Rich tooltips</app-froala-tooltip-element> have more rounded corners</p></li></ul>

GM2 rich tooltip.

<p>M2: Rich tooltips have slightly rounded corners</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmjh9u4lo-02.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/eJToL16cXcvuWuH7Ajb0sRtM7yFr6qMf_tbIdsR5hAfrIRinT4UfyLsr2Me5goaDHO1RAXuagPp28FvTXNegY6hZ64NOupwt14CTLHZZjsKk=s1004

GM3 rich tooltip.

<p>M3: Rich tooltips have more rounded corners and support dynamic color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6q4dmm-03.png?alt=media

## Specs

<h2>Tokens &amp; specs</h2>

<p>Select a component variant below to see its attributes, tokens, and values.</p>

resourceName: designSystems/20543ce18892f7d9/components/37697297db0555a6

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Tooltip - Plain', 'Tooltip - Rich'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Plain tooltip</h2>

2 elements of a plain tooltip.

<ol class="decimal"><li id="isPasted">Supporting text</li><li>Container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg6beegk-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/zHG-py73NpfFfT9V5YL21rpv8EdODG2H97qgSjjGF4IaiQlAmma5D47553mD-KCljwP7WL8j8lbyEr2zOU4jNeT5uIu4ySegOvopalEVZxQ1=s2048

<h3>Plain tooltip colors</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

2 color roles of a plain tooltip.

<p id="isPasted">Plain tooltip color roles used for light and dark themes:</p><ol class="decimal"><li>Inverse on surface</li><li>Inverse surface</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg6bfggt-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Vf161JCMtFZVXhyzhmfRoDmGW_vYVmOm5QdZOy8djJu0aEPo-gylreVY1ooQuFsAy-VFBqzRHbt1Qp6eF6znt5fJM98s4F43QbuZlmm_NHqR=s2048

<h3>Plain tooltip measurements</h3>

Measurements of a plain tooltip.

<p>Plain tooltip padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg6bgjww-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/abK2uBeEApgbWbQQrMibCEslnADu90AFpFRPbT9RVSeKZfO8baP5s6myVNJKPIUtmc_S-X99Pt046jQuk_MyMPv4IvvtWrRWieaqNLxR0SQ=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="text-align:center"><p>Attribute</p></th><th style="text-align:center"><p>Value</p></th></tr></thead><tbody><tr><th style="width:50%"><p>Container height</p></th><td><p>24dp</p></td></tr><tr><th style="width:50%"><p>Padding</p></th><td><p>8dp</p></td></tr></tbody></table></div>

<h2>Rich tooltip</h2>

4 elements of a rich tooltip.

<ol class="decimal"><li id="isPasted">Subhead</li><li>Container</li><li>Supporting text</li><li>Text button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg6bgxay-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/IP6aFfF9CPT86pHLyDQsPlpgpwRfiWWm4SrvrDszC_Mu_Y6iKdMcOlLuBrITk7y8afU-PxXvO26X0iRNTyF4uqvJjw6qmmyI2t7zUCsKbCUbEA=s2048

<h3>Rich tooltip colors</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

4 color roles of a rich tooltip.

<p id="isPasted">Rich tooltip color roles used for light and dark themes:</p><ol><li>On surface variant </li><li>Surface container</li><li>On surface variant </li><li>Primary</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg6bi2oc-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/WodvJBwtv0NFdfsgMkOfxWI698jM_8D6CP7cqU4CmxliBFAtsYOv1CqBQTgkHIP1gkYYLWMaTB9kISoEVnKcS3BCWCtOkm9pIkmmK91Z9yA=s2048

<h3>Rich tooltip measurements</h3>

Measurements of a rich tooltip.

<p>Rich tooltip padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg6big7s-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/pWZE_wQc3sD5MfnKWOQ1zSkmWFK-kLD9AHIu7iUz7DPUnF9xsNdzNhcOLz6f3jTBP-8BSkD-sKs32u3KB-9ButLnL3l_p4DJw-je_waZCy2cZw=s2048

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="text-align:center">Attribute</th><th style="text-align:center">Value</th></tr></thead><tbody><tr><th style="width:50.0000%">Top padding</th><td>12dp</td></tr><tr><th style="width:50.0000%">Bottom padding</th><td>8dp</td></tr><tr><th style="width:50.0000%">Left and right padding</th><td>16dp</td></tr></tbody></table></div>

<h3>Rich tooltip configurations</h3><p><app-froala-tooltip-element description="Rich tooltips provide additional context about a UI element. They can optionally contain a subhead, buttons, and hyperlinks." link-label link-url should-open-link-in-new-tab="true">Rich tooltips</app-froala-tooltip-element> can have a headline, body, and up to two <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element>. The headline and number of buttons can be configured.</p>

5 common configurations of a rich tooltip.

<ol><li id="isPasted">Subhead, supporting text, and two buttons</li><li>Subhead, supporting text, and one button</li><li>Subhead and supporting text</li><li>Supporting text and one button</li><li>Supporting text and two buttons</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg6biuoq-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ugboOBv4d02ZjiINyFUTI_S1IvPfMXxkgoCqYcmns1a23omQzQaAHWU5NzrwD7G96VQpAU3oi6sx14qtL_RTAIbZJXwCS9VAWV7m6NpCLlFm=s2048

## Guidelines

A plain tooltip labeling a button, and a rich tooltip announcing new settings available.

<p>Plain and rich tooltips serve different purposes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6qnzgx-01.png?alt=media

<h2>Usage</h2>

<p id="isPasted">A tooltip provides additional context for a UI element. </p><p><strong>Plain tooltips</strong><br />Plain tooltips briefly describe a UI element. They're best used for labelling UI elements with no text, like icon-only <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element> and fields.</p><p><strong>Rich tooltips</strong><br />Rich tooltips provide additional context about a UI element. They can optionally contain a subhead, buttons, and hyperlinks.</p><p>Rich tooltips are best used for longer text like definitions or explanations.</p>

2 variants of tooltips.

<ol class="decimal"><li id="isPasted">Plain tooltip</li><li>Rich tooltip</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6qs96y-02.png?alt=media

Plain tooltip labeling an icon-only button in Google Meet as "Present now".

<p>Use plain tooltips to label icon-only buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6qu5gx-03-do.png?alt=media

Button with an icon and label text saying "Edit". It has a plain tooltip on hover that also says "Edit".

<p>Plain tooltips aren't needed when the UI element already has label text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6quvhe-04-dont.png?alt=media

Rich tooltip describing a new button for adding people. It has a subhead, description, and a button to learn more.

<p>Use rich tooltips to provide extra information and actions about a UI element or new feature</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6qx7on-05-do.png?alt=media

Rich tooltip explaining that an action is destructive and permanently deletes files.

<p>Don't hide critical information within tooltips as it’s easy to miss. Use an interruptive dialog instead.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6qywbu-6-dont.png?alt=media

<h2>Anatomy</h2>

<h3>Plain tooltip</h3>

2 elements of a plain tooltip.

<ol class="decimal"><li id="isPasted">Container</li><li>Supporting text</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6r0a08-07.png?alt=media

<h3>Supporting text</h3>

Plain tooltip for an icon-only button shaped like a gear. The tooltip text is "Settings".

<p>Briefly describe a UI element</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6r2ci0-08-do.png?alt=media

Plain tooltip for the account switcher. The supporting text includes the user's name and email address on new lines.

<p>Avoid wrapping text to multiple lines or including many pieces of information</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6r3rse-09-caution.png?alt=media

<h3>Rich tooltip</h3>

4 elements of a rich tooltip.

<ol><li id="isPasted">Subhead (optional)</li><li>Container</li><li>Supporting text</li><li>Text button (optional)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmk6kierd-10.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Qrg3y9UWvNZtKfeefdMriNm0BUWNB_4KL5lW4pDAdtSVGnRbdnJq_bOmpBVvYt7o6eS-pUOtaKvGpPpVvtZqoueoaGb3xCJjE1zXjuYvf1o3=s2048

<h3 id="isPasted">Subhead (optional)</h3><p id="isPasted">Keep subheads brief, ideally to one line. They should summarize or describe the message of the <app-froala-tooltip-element description="Rich tooltips provide additional context about a UI element. They can optionally contain a subhead, buttons, and hyperlinks." link-label link-url should-open-link-in-new-tab="true">rich tooltip</app-froala-tooltip-element>.</p><p>Subheads are important to include when the rich tooltip appears automatically, like when the page loads.</p>

Rich tooltip with a brief subhead, supporting text, and a text button.

<p>Summarize the message in a few words</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6r9edz-11-do.png?alt=media

Rich tooltip with a subhead wrapping to multiple lines.

<p>Avoid wrapping to more than one line</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6ra39j-12-dont.png?alt=media

<h3>Text buttons (optional)</h3><p id="isPasted">Rich tooltips can have up to two text <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element>. These should be brief and relevant to the message in the supporting text.</p><p>Keep buttons short so they can be side by side. Avoid stacking them when possible.</p>

Rich tooltip with 2 buttons stacked on each other.

<p>Avoid stacking buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6rdax0-13-Caution.png?alt=media

<h2>Placement</h2>

<h3>Plain tooltips</h3><p id="isPasted">By default, plain tooltips are positioned directly above the parent element. </p><ul><li>If there's a visual boundary, like a button, the distance is 4dp</li><li>If there's no visual boundary, like with text baselines, the distance is 8dp</li></ul><p>If the element is in an <app-froala-tooltip-element description="App bars contain page navigation and information at the top of a screen." link-label="More on app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">app bar</app-froala-tooltip-element>, the plain tooltip appears below the element at the same distance.</p>

Plain tooltip appearing 4dp below a button with a clear visual boundary.

<p>Plain tooltip with a 4dp distance between the target and tooltip</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6rg1hz-14.png?alt=media

<h3>Rich tooltips</h3><p id="isPasted">By default, rich tooltips are positioned to the bottom right of the parent element. They adjust position to avoid going off screen.  Tooltips shouldn't cover the parent element. </p><p><strong>Dynamic positioning</strong><br />The position of the tooltip adjusts in increments of 8dp to avoid going off-screen.</p><p><strong>Desktop placement</strong><br />On desktop, tooltips may appear centered below the parent element and remain visible while moving within the target region.</p>

A rich tooltip in 4 different corners. It   changes position to remain fully on screen.

<p>Four different rich tooltip locations based on dynamic positioning</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6riq0z-15.png?alt=media

<h2>Behavior</h2>

<p>To show a tooltip, <app-froala-tooltip-element description="A hover state communicates when a user has placed a cursor above an interactive element." link-label="More on hover state" link-url="/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844" should-open-link-in-new-tab="true">hover</app-froala-tooltip-element> on the parent element on desktop, or tap and hold the element on mobile. Persistent <app-froala-tooltip-element description="Rich tooltips provide additional context about a UI element. They can optionally contain a subhead, buttons, and hyperlinks." link-label link-url should-open-link-in-new-tab="true">rich tooltips</app-froala-tooltip-element> only appear when clicked or tapped.</p>

<h3 class="placeholder--hidden">Transient by default</h3><p id="isPasted">Both <app-froala-tooltip-element description="Plain tooltips briefly describe a UI element. They're often used for labelling UI elements with no text, like icon-only buttons and fields." link-label link-url should-open-link-in-new-tab="true">plain</app-froala-tooltip-element> and rich tooltips disappear 1.5 seconds after navigating away from the target region.</p><p>Triggering a new tooltip immediately closes any other open tooltip.</p>

Hovering and moving from a button with a plain tooltip.

<p>Tooltips disappear after a 1.5 second delay when no other element is hovered</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj9io0m-GM3-Components-ToolTips-Guidelines-1-v01.mp4?alt=media

2 buttons both showing plain tooltips at once.

<p>Only display one tooltip at a time</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6ro0ii-17-dont.png?alt=media

<h3 id="isPasted">Persistent rich tooltips</h3><p id="isPasted">Persistent rich tooltips appear when either:</p><ul><li>The parent element is clicked</li><li>The page loads and a new feature is being explained</li></ul><p>Persistent rich tooltips remain active even when leaving the target region. They only disappear once a person interacts with another UI element. Hovering doesn't trigger the tooltip.</p><p>When appearing on page load, the tooltip can introduce and explain new features on various parent elements.</p><p>Avoid using persistent rich tooltips on icon buttons.</p>

Persistent rich tooltip about a new sharing feature in the Photos app. The button says  "Learn more.”

<p>Don’t use a persistent rich tooltip on icon buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6rq50p-18-dont.png?alt=media

## Accessibility

<h2>Use cases</h2>

<p id="isPasted">People should be able to do the following using assistive technology:</p><ul><li>Receive a tooltip message</li><li>Activate a tooltip with a keyboard or switch input</li></ul>

<h2 id="isPasted">Interaction &amp; style</h2>

<p>Plain and rich tooltips without required actions should remain on screen long enough for people to receive the information without disrupting their existing flow or task. </p>

A cursor hovers over an icon that identifies it as a star, which remains after moving away.

<p><span style="white-space:pre-wrap">Plain tooltips should remain on the screen temporarily after the cursor moves away</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm1i00uln-lwj9io0m-GM3-Components-ToolTips-Guidelines-1-v01.mp4?alt=media

<p id="isPasted">Tooltips can appear when an actionable element, like a button or navigation rail, is hovered or focused. However, this tooltip shouldn’t hide crucial information.</p><p>Rich tooltips can also appear by selecting an element instead of hovering or focusing on it.</p>

A cursor hovers over a favorite button producing text about finding this item later in favorites.

<p>Tooltips can appear on hover or focus to explain actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6ru5uh-02.png?alt=media

An information button in a selected state produces text about finding this item later in favorites.

<p>Rich tooltips can appear when an element is selected</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6ruf33-03.png?alt=media

<h2>Focus order</h2>

<p id="isPasted">Tooltip containers should not block important information or prevent a person from completing an action. </p><p>Focus order within the rich tooltip moves top to bottom between interactive elements. </p><p>Avoid trapping screen reader and keyboard focus on rich tooltips.</p><p>People should be able to move linearly through the rest of the page.</p>

Different elements of a rich tooltip are given a focus order, moving from parent element to inline link to text button.

<ol class="decimal"><li id="isPasted">Parent element</li><li>Inline link</li><li>Text button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmjha0vdq-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/KCWqivAVbjIzMGBp1AVQbceVT02tQdKQSNJOd-FA_ARUYwMLQX2GUYZi55K0wxG_c2dYdGFnsBnB-_1n-m8thxhCgVavyU0W9_Dz5C9aVBLEdA=s1352

<h2>Keyboard navigation</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p><strong>Keys</strong></p></th><th style="text-align:center"><p><strong>Actions</strong></p></th></tr></thead><tbody><tr><td><p><strong>Tab</strong></p></td><td><p>Focus lands on button, if available</p></td></tr><tr><td><p><strong>Space</strong> or <strong>Enter</strong></p></td><td><p>Activates the focused element</p></td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<p id="isPasted">Tooltips should have the <strong>Tooltip</strong> role, or similar. </p><p>Label all elements in the tooltip according to their own accessibility guidance.</p>

A rich and plain tooltip with all elements matched to accessibility labels.

<p>The tooltip container should have the <strong>Tooltip</strong> role</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme6ry9ry-05.png?alt=media
