# Snackbar

Source: https://m3.material.io/components/snackbar
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/26cf2750-80f7-43f8-a155-834aa01276df.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li id="isPasted">Snackbars shouldn’t interrupt the user’s experience </li><li>Usually appear at the bottom of the UI</li><li>Can disappear on their own or remain on screen until the user takes action</li></ul>

Diagram of snackbar placement

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwow6ukp-1.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/20c468ba5d00e74d

libraryModuleType: STATUS_TABLE

<h2>Differences from M2</h2>

<ul><li>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></li><li>Behavior: Clarified that snackbars can either appear temporarily (dismissive) or persist until the user takes an action (non-dismissive)</li></ul>

Example of snackbar on screen bottom

<p>Snackbars have new color mappings</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwow95bc-2.png?alt=media

## Specs

Diagram of snackbar indicating the four parts of its anatomy

<ol class="decimal"><li><p>Container</p></li><li><p>Icon (optional close affordance)</p></li><li><p>Action (optional)</p></li><li><p>Supporting text</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkvpjhzt-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/oe-jEgmWKP97u0jsjhWPp2985Zn00p4FweCCB7iQbvx_xh1kkNRctD67TGEeJU_on8ch67ncdBPf84JXcOvaNlSmUXC8ypG3_32cRuGMlhN7=s2048

<h2>Tokens and specs</h2><p>Browse the component elements, attributes, tokens, and their values. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/346ae12a744b45dd

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2 id="isPasted">Color</h2><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" id="isPasted">Learn more about design tokens</a></p>

Diagram of snackbar indicating color and inverse text and labels

<p id="isPasted">Snackbar color roles used for light and dark schemes:</p><ol><li>Inverse surface</li><li>Inverse on surface</li><li>Inverse primary</li><li>Inverse on surface</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flxlhysf9-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/TqN2bvamEg2OcfPTmDLrFjMzDjDhfoX3dVbCgn4qqFArx765sDUaubGeUw0RiTFP6y83dAh3XIhj8zds2PAmADSgaUSkxhWjYLzElENX55ca=s2048

<h2>Measurements</h2>

Diagram of snackbar with action

<p>Snackbar padding and size measurements </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8otc9es-3-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/n1bxJJHcB0rD_PQuOaQL4U-nFlVYJ27WJyM-bsxB1Es0KgiWp-4UDnXLHUIMA42rrSWGNZ7nYCQGRNj5hemAC1g672z6akYe7iX1pv0113Q=s2048

<h2 id="isPasted">Configurations</h2>

5 snackbar configurations.

<ol><li>Single line</li><li>Single line with action</li><li>Two lines</li><li>Two lines with action</li><li>Two lines with longer action</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flxli48dd-5.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Pd1qLYMI80pcYjx89JXrogC_QiOljw2S1pbGruxLf1oJu_bQnZBwoBxb7V3AnPcV-piQUix6mCFtdBH73KWXOmBI-Svt8rcfh8sRwlh6yJ26dg=s2048

## Guidelines

Snackbar at the bottom of a mobile device.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6a9x4e1-1.png?alt=media

<h2><span style="white-space:pre-wrap">Usage</span></h2>

<p id="isPasted">Snackbars inform users of a process that an app has performed or will perform. They appear temporarily, towards the bottom of the screen.</p><p>They shouldn't interrupt the user experience. People can browse the page content without being required to interact with the snackbar.</p><p><strong>Frequency</strong><br />Only one snackbar may be displayed at a time.</p><p><strong>Actions</strong><br />A snackbar can contain a single action. "Dismiss" or "cancel" actions are optional.</p>

Snackbar showing 'Email archived' text with an 'Undo' text button.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6a9y0k8-2.png?alt=media

<h3 id="isPasted">Similar components</h3><p><app-froala-tooltip-element description="Dialogs provide important prompts in a user flow." link-label="More on dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">Dialogs</app-froala-tooltip-element> are also designed to show important messages.</p><p>Choose the right component based on the importance of the message. This component messaging strategy can help avoid overusing snackbars.</p>

Dialog on a phone requiring the user to sign in to continue. Dismissing prevents them from progressing.

<p>Dialogs require immediate action</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8ov80w7-4.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-tiKvQVJlOCfknFRqwRFth2PAQgditPIXPneNZWGR_W7XuQHEfYzHpyZR8lkb7gDWylZmqw6jVl9ExMk2sIrWV5SJEDrph3YWse2wdx1X5fc=s1352

<p id="isPasted"><span style="white-space:pre-wrap"><strong>When to use snackbars</strong><br />Snackbars communicate messages that are minimally interruptive and don’t require user action.</span></p>

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="width:33.3%;text-align:center" class="fr-cell-handler ">Component</th><th style="width:33.3%;text-align:center">Priority</th><th class="fr-cell-fixed " style="text-align:center">User action</th></tr></thead><tbody><tr><th>Snackbar</th><td>Low priority</td><td>Optional: Snackbars disappear automatically</td></tr><tr><th>Dialog</th><td>High priority</td><td>Required: Dialogs block app usage until the user takes a dialog action or exits the dialog (if available)</td></tr></tbody></table></div>

<h3 id="isPasted">Accessibility requirements for web</h3><p>On web, auto-dismissing snackbars are inaccessible for people with low vision or who require additional time to perceive information. This can be solved in 2 ways:</p><h4>1. Add inline feedback</h4><p>Information in auto-dismissing snackbars must also be communicated using another accessible method inline or near the action that triggered the snackbar. </p><p>For example, update the label on a "Save" <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">button</app-froala-tooltip-element> to “Saved”, and trigger an auto-dismissing snackbar that communicates the same message. </p><h4>2. Make the snackbar actionable</h4><p>Alternatively, add actions to the snackbar so it doesn't dismiss until acted on.</p>

A button labelled "Save" changes to "Saved" after a moment. A snackbar confirms all changes are saved.

<p>Also communicate snackbar information near the action that triggered the snackbar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoxyec0-5.png?alt=media

<h2><span style="white-space:pre-wrap">Anatomy</span></h2>

4 elements of a snackbar.

<ol><li>Container</li><li>Supporting text</li><li>Action (optional)</li><li>Close button (optional)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoy0ibw-6.png?alt=media

<h3>Text label</h3><p>Snackbars contain a text label that directly relates to the process being performed. In <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoints</app-froala-tooltip-element>, the text label can contain up to two lines of text.</p>

Snackbar on a mobile device reading: "Saved in Vacation album".

<p>Text labels are short, clear updates on processes that have been performed</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoy1q93-7.png?alt=media

Snackbar on mobile with one line of content.

<p>Keep the snackbar text label to one line long when possible</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoy2p4f-8.png?alt=media

Snackbar on mobile with two lines of content.

<p>On mobile, the text label can be up to two lines long</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoy3zcx-9.png?alt=media

Snackbar on mobile with an icon and one line of content.

<p>Avoid adding icons to snackbars. If your message needs an icon, consider using a different component such as a dialog.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoy4zjx-10.png?alt=media

Snackbar on mobile with bolded and hyperlinked words.

<p>Avoid using stylized text or inline links in snackbars; they can add unwanted complexity. If your message needs a link, add a button instead, or use a different component.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoy6dj7-11.png?alt=media

<h3>Container</h3><p><span style="white-space:pre-wrap">Snackbars are displayed in rectangular containers with a grey background. Containers should be completely opaque, so that text labels remain legible.</span></p>

Snackbar showing a light text label on a black color container.

<p>Snackbar containers use a solid background color with a shadow to stand out against content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoy7luk-12.png?alt=media

A snackbar with button text the same color as supporting text.

<p>The text label shouldn’t share the same color as the text button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkvoz7q4-13.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/4ZjkkltqgNzA13m457i7C95ZkoGaUoXwgffmVQBnSzhDn_qqntogMKz1zoZ3atzRsf9Iu83GJ9KxWN36I8FPXrBHeStry3i6Y-QPP1AAcSL5RQ=s1004

A snackbar with the action in elevated style.

<p>Don’t use a filled or elevated button in a snackbar, as it draws too much attention</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkvoydmj-14.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/b3InMdZt65Rjhh2v0XIVdSSStbaGd_Hzb2lnxzGsqpOgwaGnTk-i5f4uZrNBwjViXGXis6FZhuu7ZbP73NMc0fLH6jPdDIgemxqSwr4ImN-P=s1004

An extended snackbar on tablet with a long text label. 

<p>In wide layouts, extend the container width to accommodate longer text labels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoyabsh-13.png?alt=media

Snackbar with a slightly transparent container and a clearly visible text label.

<p>An app can apply slight transparency to the container background, as long as text remains clearly legible</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoyc9yp-14.png?alt=media

<p>Avoid significantly altering the shape of a snackbar container</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoydoed-15.png?alt=media

<h3>Action</h3><p>Snackbars can display a single text button that lets users take action on a process performed by the app. Snackbars shouldn’t be the only way to access a core use case, to make an app usable.</p>

A snackbar container with rounded corners.

<p>To distinguish the action from the text label, text buttons should display colored text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoyf085-16.png?alt=media

Snackbar with a long text button displayed on a third line.

<p>If an action is long, it can be displayed on a third line</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxktjsxn-19.png?alt=media

Snackbar with a single text button labeled undo.

<p>To allow users to amend choices, display an "Undo" action</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoz8scg-20.png?alt=media

Snackbar with a single text button labeled dismiss.

<p>A dismiss action is unnecessary, as snackbar disappears on their own by default</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoza8yz-21.png?alt=media

<h2><span style="white-space:pre-wrap">Placement</span></h2>

<h3 id="isPasted">At the bottom of a UI</h3><p>Snackbars should be placed at the bottom of a UI, in front of the main content. In some cases, snackbars can be nudged upwards to avoid overlapping with other UI elements near the bottom, such as <app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/m3/pages/fab/overview" should-open-link-in-new-tab="true">FABs</app-froala-tooltip-element> or <app-froala-tooltip-element description="Docked toolbars (formerly bottom app bars) are placed at the bottom of the page." link-label link-url should-open-link-in-new-tab="false">docked toolbars</app-froala-tooltip-element>.</p><p>Avoid placing a snackbar in front of frequently used touch targets or navigation.</p>

Snackbar appearing in front of photo content. 

<p>Place a snackbar in front of the main content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6aa5hcy-22.png?alt=media

Snackbar placed in front of the navigation components.

<p>Avoid placing snackbars in front of navigation components</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6aa6688-23.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">To ensure accessibility for keyboard users on the web, avoid positioning the snackbar in a way that completely obscures actionable elements. Blocking elements makes it difficult to know what is being focused and selected.</span></p>

Thin snackbar in front of a focused element that is still visible.

<p><span style="white-space:pre-wrap">Adjust the size of the snackbar to avoid blocking elements in focus</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkvpb7sp-24.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/vg5GlpuWuNMO4YWdc0KGUyWNHahzYhB8tTa-uXWzkLg62Et6WGYvmeoY4A8iT5fW17tRL3aeUfWxEpl6Wyaz6hqqqfFp3ZuYeuhjmDhRvgSx=s1312

Larger snackbar that is obscuring a focused element.

<p><span style="white-space:pre-wrap">Don’t let the snackbar fully cover elements in focus</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkvpbire-25.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/kpbBuDWBK_Ys0lIMzxCNuXCENtyVH4hR1fZew7Plf3CLFO6w5xF-w_3BdgmDkR2FUBahDMfcS1Hj9KqjAmhyog4PmEHnUy9tF9BBS92Y13Q=s1312

<p id="isPasted">Snackbars can span the entire width of the screen only when a UI does not use persistent navigation components like app bars or <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/google-material-3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bars</app-froala-tooltip-element>.</p><p>Snackbars that span the entire width of a UI can push up <app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/google-material-3/pages/fab/overview" should-open-link-in-new-tab="true">FABs</app-froala-tooltip-element> when they appear.</p>

Snackbar spanning the width of a mobile device is placed in front of the navigation components and FAB.

Snackbars can span the entire width of a UI. However, they should not appear in front of navigation or other important UI elements like floating action buttons.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6aa171j-26.png?alt=media

<p><strong>Snackbars and floating action buttons (FABs)</strong></p><p>Snackbars should appear above <app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/m3/pages/fab/overview" should-open-link-in-new-tab="true">FABs</app-froala-tooltip-element>.</p>

Snackbar placed above a FAB on a mobile device.

<p>Snackbar above a FAB</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6aa25mm-27.png?alt=media

Snackbar placed in front of a FAB on a mobile device.

<p>Don’t place a snackbar in front of a FAB</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6aa35y8-28.png?alt=media

Snackbar placed behind a FAB on a mobile device.

<p>Don’t place a snackbar behind a FAB</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6aa41vd-29.png?alt=media

<h2><span style="white-space:pre-wrap">Responsive layout</span></h2>

<h3>Compact breakpoint</h3><p>In <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoints</app-froala-tooltip-element>, snackbars should expand vertically from 48dp to 64dp to accommodate one or two lines of text, while maintaining a  fixed distance from the leading, trailing, and bottom edges of the screen.</p>

Snackbar with its label text extending to the second line and maintaining fixed distance from the edges of a mobile device.  

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxktk5oy-28.png?alt=media

<h3>Medium &amp; expanded breakpoints</h3><p>On <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints</app-froala-tooltip-element>, like tablet and desktop, snackbars should scale horizontally to accommodate longer text strings, keeping in mind that the ideal line length for text is typically between 40-60 characters.</p><p>Snackbars use a flexible distance from the trailing edge of the screen. Whenever possible, snackbars on medium and large displays should aim for a single line of text with an  optional <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">button</app-froala-tooltip-element>.</p>

A horizontally expanded snackbar placed at the bottom of screen on a medium-size device.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwoztb40-29.png?alt=media

<p>In wider <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/understanding-layout/overview" should-open-link-in-new-tab="true">layouts</app-froala-tooltip-element>, snackbars can be left-aligned or center-aligned if they are consistently placed on the same spot at the bottom of the screen.</p>

A left-aligned snackbar placed at the bottom of screen on a medium-size device.

<p>Left-aligned snackbar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwozw4lz-30.png?alt=media

A center-aligned snackbar placed at the bottom of screen on a medium-size device.

<p>Center-aligned snackbar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwozx768-31.png?alt=media

Snackbar displayed at the left edge of the screen, near the bottom, on a medium-sized device.


<p>Don’t place snackbars flush to one edge of the layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkvpdu5k-34.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/31lW1WIYT75nNWrdmMIpaPc3F1li8pdovxS-wfb4EPMkAyZOwTPcOhw2EmNvQ7IsBKjkF-BnlA8ciLYiewbuRaf_A7fM3279CbPZEZkhgEw-=s2048

2 snackbars placed side-by-side at the bottom of the screen on a medium-size device.

<p>Don’t place consecutive snackbars side by side or next to one another</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmkvpefif-35.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/OfYvxPiin9tChm76P70MCXk-eBs2mdE5Lg-EIsARo0YiUY5UDsthxozOFefNXX0RhhW-SJ7mKpeHpofakdr6uN5i2XBdNcNYjgv_MNXvlCT4=s2048

<h2>Behavior</h2>

<h3>Appearing and disappearing</h3><p dir="ltr" id="isPasted">Snackbars appear without warning, but they don’t block users from interacting with page content.</p><p dir="ltr">Snackbars without actions can auto-dismiss after 4–10 seconds, depending on platform. Avoid using auto-dismissing snackbars on web unless there's also inline feedback.</p>

Snackbar without an action button appearing and disappearing within 4 seconds from the screen of a mobile device.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwp03p7p-GM3-Components-Snackbar-Guidelines-1-v01.mp4?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">Snackbars with actions should remain on the screen until the user takes an action on the snackbar, or dismisses it.</span></p>

Snackbars with actions should remain on the screen until the user takes an action on the snackbar, or dismisses it.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm7ca02x7-m6f92ux5-GM3-Components-Snackbar-Behavior-1-v01.mp4?alt=media

<h3>Consecutive snackbars</h3><p dir="ltr" id="isPasted">Consecutive snackbars must appear one at a time. </p><p dir="ltr">Snackbars without actions appear and disappear automatically, while those with actions remain on screen until dismissed. However, a snackbar with updated information can immediately replace an outdated snackbar.</p>

Two snackbars appear sequentially on a mobile device. The first includes an action button.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwp06c42-GM3-Components-Snackbar-Guidelines-2-4-v02.mp4?alt=media

2 snackbars appear sequentially on a mobile device and are stacked on top of one another. The first includes an action button.

<p>Don’t stack snackbars on top of one another</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwp08dxf-GM3-Components-Snackbar-Guidelines-3-v01.mp4?alt=media

FAB's position is displaced when a snackbar enters the screen of a mobile device.

<p>Don’t animate other components along with snackbar animations, such as the floating action button</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwp0a03k-GM3-Components-Snackbar-Guidelines-2-3-v01.mp4?alt=media

## Accessibility

<h3>Use cases</h3><p>Users should be able to:</p><ul><li id="isPasted">Be alerted, but not disrupted, when a snackbar appears</li><li>Move focus to an actionable snackbar</li><li>Take action on a snackbar using assistive technology</li></ul>

<h3>Interaction &amp; style</h3><p id="isPasted">Snackbars with actions shouldn't auto-dismiss. This way, users can read and interact with it at their own pace.</p><p>Snackbars without actions can auto-dismiss after a sufficient amount of time, however this can still present difficulties on web without additional feedback. </p><p>Each platform has its own requirements for auto-dismiss durations, however common acceptable durations are 4–10 seconds.</p>

A snackbar saying "Email marked as read" with no button.

<p>Auto-dismissing snackbars should remain on screen long enough to read the information</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwp0j72d-1.png?alt=media

<p>Snackbars use a color intended to stand out against UI elements. Use the default color mapping to avoid color conflict issues.</p>

Snackbar with a dark container on a UI page in light theme.

<p>Snackbar should visually stand out</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwp0k0la-2.png?alt=media

<h3>Accessibility requirements on web</h3><p id="isPasted">On web, auto-dismissing snackbars can be difficult to navigate for people with low vision or who require additional time to perceive information. This information can be made clearer for all users in two ways:</p><h4>1. Add inline feedback</h4><p>Information in auto-dismissing snackbars must also be communicated inline or near the action that triggered the snackbar.</p><p>For example, update the label on a "Save" button to “Saved”, and trigger an auto-dismissing snackbar that communicates the same message.</p><h4>2. Make the snackbar actionable</h4><p>Alternatively, add actions to the snackbar so it doesn't dismiss until acted on. Actionable snackbars shouldn't auto-dismiss.</p>

A "save" button changes to say "saved", alongside a snackbar that confirms changes were saved.

<p>Communicate snackbar information near the action that triggered the snackbar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwp0kqjx-3.png?alt=media

<p><strong id="isPasted">Note: Material Web doesn't yet include the snackbar component. This guidance still applies to custom-made snackbars.</strong></p>

<h3>Focus</h3><p id="isPasted">Snackbars have the following focus requirements:</p><ul><li>When a snackbar appears, announce the message but don't move focus.</li><li>Don't automatically move focus.</li><li>Don't trap focus in the snackbar. Users should be able to freely navigate in and out.</li><li>On web, a shortcut should exist for users to move focus to snackbars with actions (like Alt+G). Ensure that this shortcut is clearly documented, like in a help article.</li></ul>

Taking a menu item action moves focus to a snackbar. Moving focus out of the snackbar returns it to the same menu item.

<p>Focus returns from the snackbar (1) to the previously focused element (2)</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwp0eako-GM3-Components-Snackbar-Accessibility-1-v01.mp4?alt=media

<p id="isPasted">Focus exits the snackbar differently per platform:</p><ul><li>Ideally, focus should either return to the element that triggered the snackbar, or go to the next most logical element on the page. </li><li>On Android Compose, focus may move to the nearest visible element, or to the first actionable item on the page.</li></ul>

Confirming in a dialog moves focus to a snackbar. Moving focus out of the snackbar returns it to a page element.

<p>If the previously focused element is no longer on the page, focus should move from the snackbar (1) to the next most logical element (2)</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwp0g1ed-GM3-Components-Snackbar-Accessibility-2-v01.mp4?alt=media

<h3>Keyboard navigation</h3><div class="table-wrapper"><table style="width:100%"><thead><tr><th style="width:19.6256%;font-weight:500"><div style="text-align:center">Keys</div></th><th style="width:80.2536%;font-weight:500"><div style="text-align:center">Actions</div></th></tr></thead><tbody><tr><td>Tab</td><td class="placeholder--hidden" style="width:80.2536%">Moves focus between interactive elements</td></tr><tr><td>Esc</td><td class="placeholder--hidden" style="width:80.2536%">Dismisses the snackbar when in focus</td></tr></tbody></table></div>

<h3>Labeling elements</h3><p id="isPasted">Snackbars should be announced once they appear on the screen, but shouldn’t grab focus or prevent people from completing their current task. </p><ul><li>On Android and web, use a live region with a polite (queued) announcement instead of an assertive announcement.</li><li>On iOS 17+, snackbars use polite announcements by default.</li></ul><p>If a snackbar appears when the app is launched, it should be announced after the page’s title, but not receive focus. </p>

Snackbar accessibility label examples.

<p>Snackbars are announced when they appear, but don't trap focus</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmff15na8-06.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/T_KwPf_rpSE3ree_3mFMt2C53xtXu1NZ67-FWB7-dRxb8jIeyk4T3J2-evC6G3Jly9WNV_gjKI-h98xqnBN3F_1npn_okXgBAUS4eo495UM=s1352
