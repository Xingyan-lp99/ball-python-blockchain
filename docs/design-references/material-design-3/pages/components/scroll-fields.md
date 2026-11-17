# Components

Source: https://m3.material.io/components/scroll-fields
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/1624d6a1-96ea-437d-b846-dc6f00ebb49c.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Components are interactive building blocks for creating a user interface. They can be organized into categories based on their purpose: Action, containment, communication, navigation, selection, and text input.

## Overview

<ul type="disc" style="list-style-type:disc"><li><p>Two different modes of input: scroll and input</p></li><li><p>Three recommended sizes: small (1-2 digits), medium (3 digits), and large (4 digits)</p></li><li><p>Can be finite or an infinitely looping list</p></li><li><p>Can be combined to select different measurements and include multiple values</p></li></ul>

6 variations of the scroll field at varying widths.

<p>Scroll fields come in three sizes: small, medium, and large</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugk3gzq-01.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/5577d088b97dd803

libraryModuleType: STATUS_TABLE

<h2>M3 Expressive update</h2>

<p>The scroll field was introduced in the expressive update. <app-froala-tooltip-element description="M3 Expressive is a major update to Material 3, adding visually stunning features, components, and variants, plus updates to the shape, motion, and typography systems." link-label="More on M3 Expressive" link-url="https://m3.material.io/blog/building-with-m3-expressive" should-open-link-in-new-tab="true">More on M3 Expressive</app-froala-tooltip-element></p>

## Specs

<h2>Tokens &amp; specs</h2>

<p>Select a component variant below to see its elements, attributes, tokens, and their values. <a href="/m3/pages/design-tokens" target="_blank">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/42f95ef205743188

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['High contrast', '3P', 'Medium contrast', 'Light', 'Bold', 'Default', 'Expressive', 'Static', 'Standard', 'Dark', 'None', 'Compose', 'Android', 'Web'], 'showInlineTokenShare': True}

<h2>Anatomy</h2>

Diagram identifying the 6 elements of a scroll field.

<ol type="1" style="list-style-type:decimal"><li><p>Scroll field container</p></li><li><p>Inactive number</p></li><li><p>Active number</p></li><li><p>Selected scroll field container</p></li><li><p>Selected active number</p></li><li><p>Cursor</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwbncawf-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/_NTkAt_axDuVG4sy4o87lZfqjqmR-wFZmhntpyM48JNOHszQutdTnN2P6ZmkY6lEeYLNx_iRIOlr0zkMqVIlhlrEeuMs6xwE4UaDzmUsPX4=s2048

<h2>Color</h2>

<p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens" target="_blank">Learn more about design tokens</a></p>

Side-by-side light and dark diagrams indicating the 6 different color elements of a scroll field.

<p>Scroll field color roles used for light and dark themes:</p><ol type="1" style="list-style-type:decimal"><li><p>Surface container lowest</p></li><li><p>Outline</p></li><li><p>On surface</p></li><li><p>Primary</p></li><li><p>Primary</p></li><li><p>Primary</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwbnddfl-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/QSedqWaqWD9RnylsY_nMtGvaCj4vRMw0_5yRV5D7L6OMRrQM-UAWmfNabWEeM6gzkh-oCTqSr24Un0fIwmPZQ2ncoi_Df4AjAVB0GVilFnWo=s2048

<h2>States</h2>

Side-by-side light and dark diagram showing the 8 interactive states of scroll fields.

<ol type="1" style="list-style-type:decimal"><li><p>Enabled (inactive)</p></li><li><p>Hovered (inactive)</p></li><li><p>Focused (inactive)</p></li><li><p>Disabled (inactive)</p></li><li><p>Enabled (active)</p></li><li><p>Hovered (active)</p></li><li><p>Focused (active)</p></li><li><p>Disabled (active)</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwbneeji-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/p1dPFIVt-Rcxi8oqlvQNn0VSKp7RkNWUZAiZyO4YRhX7cNWASmuKmhCTwMvVqmFOxrx2X4gJTWCS3YgJyPcF_Zdoc6wn3GTwPleVVtejnzw=s2048

<h2>Measurements</h2>

<p>Scroll fields hug the contents by default, down to a minimum width and height per size. In larger windows, the fields can fill the container instead, or have a custom fixed size.</p>

Diagram of width and height measurements for scroll fields, by number of digits. 

<ol type="1" style="list-style-type:decimal"><li><p>Small (1-2 digits)</p></li><li><p>Medium (3 digits)</p></li><li><p>Large (4 digits)</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwbnf8lc-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Vwd79EDzb-Dl0_TlVuHorLgACJ4nHhmJK-Si9MjXLCjdTLBKkhUhz7jca0D9rCcESsC-aiadUHZgRtJ639cdyffGCIcCddM6J8M5jLPRXr-5Jg=s2048

<h2>High contrast</h2>

<p>High contrast mode is an accessibility feature that aims to maximize legibility by using a limited color palette, like black and white. <a href="/m3/pages/color/how-the-system-works#0207ef40-7f0d-4da8-9280-f062aa6b3e04" target="_blank">Learn more about high contrast</a></p>

Two fields, one with scroll and one with direct input, using high-contrast mode.

<p>Scroll field in high-contrast mode</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwbng1dh-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/YXU0p0oVV0tEI0cpA4O5O4ydgnGWI9RHaoXcJzrpjLtc6c2yBgC7FQH9T1dkCIQWOlYsmKeCKVYo8JA-P9HzUUB1JzgCSxoqRsUkEugRmWRgSA=s2048

## Guidelines

Close-up of a scroll field component selecting height.

<p>Scroll fields provide a flexible, focused way for people to input or adjust specific measurements and numeric values</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugsv6yd-GM3%20-%20Scroll%20Fields%20-%20Guidelines%2001%20-%20IA%20-%20v01.mp4?alt=media

<h2>Usage</h2>

<p>Scroll fields are an expressive way to select from a list of options. They're best used for numbers, but can be customized to many different use cases.</p>

Fitness app with scroll fields used to set desired heart rate.

<p>Scroll fields are best used for choosing from a list of numbers</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugl9lil-02.png?alt=media

<p>Scroll fields can be used for time selection, as well as other units of measurement like distance, weight, or temperature.</p>

UI displaying scroll fields setting temperature.

<p>Temperature can be set through paired scroll fields</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmuglgf16-03.png?alt=media

<p>Use scroll fields alongside other controls, like <app-froala-tooltip-element description="Button groups organize buttons and add interactions between them" link-label="More on button groups" link-url="/m3/pages/button-groups/overview" should-open-link-in-new-tab="true">button groups</app-froala-tooltip-element>, to set more specific filters or add greater choice.</p><p>If using scroll fields to choose time, use a <app-froala-tooltip-element description="Time pickers help users select and set a specific time." link-label="More on time pickers" link-url="/m3/pages/time-pickers/overview" should-open-link-in-new-tab="true">time picker</app-froala-tooltip-element> instead.</p>

Bottom sheet with an alarm using scroll fields for time, along with button group options for date of week.

<p>Scroll fields can be used along with options for day to add precision</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugln1yz-04.png?alt=media

<p>Multiple scroll fields can be placed side by side. If each scroll field is tracking a different value, clearly label each field.</p>

A timer with three scroll fields aligned to hours, minutes, and seconds.

<p>Add labels to scroll fields affecting different values</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmuglwygr-06.png?alt=media

<h3>Support keyboard input</h3><p>For accessibility, scroll fields should have an option to swap to text input for keyboard users. Place this button near the scroll field.</p><p>In <app-froala-tooltip-element description="The scroll time picker is a compact way to select time." link-label="More on time pickers" link-url="/m3/pages/time-pickers/overview" should-open-link-in-new-tab="true">scroll time pickers</app-froala-tooltip-element>, this button is built-in.</p>

Fitness app displaying a field for calories through scroll, with a keyboard icon to switch to text input.

<p>When scroll fields are present, the keyboard icon allows switching to text input</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmuglrn65-05.png?alt=media

<h2>Anatomy</h2>

<p>The scroll field has different parts that can be customized.</p>

Diagram of scroll field listing container, inactive value, and active value.

<ol type="1" style="list-style-type:decimal"><li><p>Scroll field container</p></li><li><p>Inactive value</p></li><li><p>Active value</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugm0z3u-07.png?alt=media

Diagram of scroll field elements with an active value and a container using a highlight and cursor.

<ol type="1" style="list-style-type:decimal"><li><p>Selected scroll field container with highlight</p></li><li><p>Selected active value</p></li><li><p>Cursor</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugm2pcw-08.png?alt=media

<h2>Behavior</h2>

<h3>Scrolling</h3><p>To scroll between values in a field, swipe the field, or tap the inactive value above or below to navigate to it.</p>

ISO values are listed on a camera app, with inactive values scrollable by swiping or selecting the values themselves.

<p>Scroll through values by swiping or tapping the inactive values</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugsxvyc-GM3%20-%20Scroll%20Fields%20-%20Guidelines%2009%20-%20IA%20-%20v01.mp4?alt=media

<h3>Motion</h3><p>Scrolled items snap to always be vertically centered. The active value is darker with an increased font size.</p>

Month and day in separate scroll fields being used for date selection.

<p>The item in the center of the container snaps into place</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugt1cdm-GM3%20-%20Scroll%20Field%20-%20Guidelines%2010%20-%20IA%20-%20v01.mp4?alt=media

<h3>Input behavior</h3><p>When text input is selected, the numeric or standard keyboard can be used to select values.</p><p>For strings, the selection should auto-complete based on the initial character entered.</p><p>Any errors should appear below the scroll fields, and should highlight the incorrect value.</p>

UI for logging water shows numeric values added by keyboard after first selecting keyboard icon.

<p>Choosing text input swaps the focused scroll field to a text field</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugt5bp2-GM3%20-%20Scroll%20Field%20-%20Guidelines%2011%20-%20IA%20-%20v01.mp4?alt=media

<h2>Sizing</h2>

<p>Material recommends only using up to four digits in scroll fields. However, more digits can still be added as needed. There are three size options with their own minimum widths:</p><ul type="disc" style="list-style-type:disc"><li><p>Small (1-2 digits): 100dp</p></li><li><p>Medium (3 digits): 144dp</p></li><li><p>Large (4 digits): 186dp</p></li></ul>

Three different sizes of scroll fields: small with 2 digits, medium with 3 digits, and large with 4 digits.

<ol type="1" style="list-style-type:decimal"><li><p>Small (1-2 digits)</p></li><li><p>Medium (3 digits)</p></li><li><p>Large (4 digits)</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugmu4uu-12.png?alt=media

<p>Avoid very long lists in scroll fields, such as consecutive numbers with five or more digits. Values should be quick to scroll to.</p><p>To avoid excessive scrolling time, add intervals between values, or use a different component for precise entry, like a <app-froala-tooltip-element description="Text fields let users enter text into a UI." link-label="More on text fields" link-url="/m3/pages/text-fields/overview" should-open-link-in-new-tab="true">text field</app-froala-tooltip-element>.</p>

A banking app set to transfer money with the dollar amount running to five digits on a scroll field.

<p>Using five or more digits implies a long scroll time, unless values aren’t consecutive</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugmypl9-13-dont.png?alt=media

<h2>Placement</h2>

<h3>Inline is preferred</h3><p>Whenever possible, place scroll fields inline with content. When scroll fields are inline, people can easily see surrounding content.</p>

Camera app showing values for aperture and shutter speed above a scroll field to select ISO value.

<p>Inline scroll fields are ideal for multiple values that should be set together, like ISO, shutter speed, and aperture camera settings</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugn8qe3-14.png?alt=media

<h3>Non-modal dialog</h3><p>When scroll fields can’t be placed inline, use a popup container like a non-modal <app-froala-tooltip-element description="Dialogs provide important prompts in a user flow." link-label="More on dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">dialog</app-froala-tooltip-element>.</p>

An option to select a “custom amount” produces 2 scroll fields as a non-modal dialog to select total amount in ounces or liters.

<p>When space is limited, scroll fields can be placed in a non-modal dialog</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugpm1gf-15.png?alt=media

<h3>Modal dialog</h3><p>Modal dialogs should be used rarely, when the UI is too cluttered for a non-modal dialog.</p>

A modal listing temperature settings through two scroll fields.

<p>Scroll fields can be placed in modals if needed</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugpp75h-16-caution.png?alt=media

<h2>Adaptive design</h2>

<p>On larger screens, consider increasing scroll field height and width to more comfortably fill the containers they’re placed within.</p>

Scroll fields adapt to smaller or larger device size, filling the space.

<p>A taller and wider scroll field better fits the larger layout</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugtau30-GM3%20-%20Scroll%20Field%20-%20Guidelines%2017%20-%20IA%20-%20v01.mp4?alt=media

<h3>Customizations</h3>

<p>Scroll fields can be customized to have a fixed size, or to adapt in size depending on the space they’re placed in. To preserve usability:</p><ul type="disc" style="list-style-type:disc"><li><p>Visually crop inactive values to indicate that more values are available by scrolling</p></li><li><p>Corner radius shouldn't be less than 16dp</p></li></ul>

Custom widths for a scroll field.

<p>Scroll fields are customizable to fit panes of any size</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugpyfqy-18.png?alt=media

## Accessibility

<h2>Use cases</h2>

<p>People should be able to use assistive technology to: </p><ul type="disc" style="list-style-type:disc"><li><p>Select or enter values and units of measurement</p></li><li><p>Enter measurement selection manually using input fields</p></li></ul>

<h2>Interaction &amp; style</h2>

<h3>Include both swipe &amp; text input options</h3><p>Any scroll field needs a way to also input text with a keyboard, like a <app-froala-tooltip-element description="Toggle buttons can be selected and unselected." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">toggle button</app-froala-tooltip-element> next to the scroll fields, or a separate <app-froala-tooltip-element description="Text fields let users enter text into a UI." link-label="More on text fields" link-url="/m3/pages/text-fields/overview" should-open-link-in-new-tab="true">text field</app-froala-tooltip-element>.</p><p>Material's <app-froala-tooltip-element description="The scroll time picker is a compact way to select time." link-label="More on time pickers" link-url="/m3/pages/time-pickers/overview" should-open-link-in-new-tab="true">scroll time picker</app-froala-tooltip-element> has a built-in button that toggles to an <app-froala-tooltip-element description="Input time pickers allow people to set a time using a keyboard. This option is accessible from any mobile time picker interface via the keyboard icon." link-label="More on time pickers" link-url="/m3/pages/time-pickers/overview" should-open-link-in-new-tab="true">input time picker</app-froala-tooltip-element>. Consider using a similar pattern.</p>

The keyboard toggle on a scroll field activates input mode and allows direct entry of liters.

<p>Scroll fields are always paired with an input toggle in time pickers to allow text input</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmuguspn0-GM3%20-%20Scroll%20Field%20-%20Guidelines%2011%20-%20IA%20-%20v01.mp4?alt=media

<h3>Targets</h3><p>Targets for inactive values need to maintain a minimum height of 48dp, which stretches outside the container by default.</p>

Diagram showing scroll field’s tap targets.

<p>All inactive values present should have a minimum 48dp height</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugql74i-02.png?alt=media

<h2>Keyboard navigation</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><tbody><tr><td><p>Keys</p></td><td><p>Actions</p></td></tr><tr><td><p><strong>Tab</strong></p></td><td><p>Focus lands on scroll field</p></td></tr><tr><td><p><strong>Space</strong> or <strong>Enter</strong></p></td><td><p>Activates the scroll field</p></td></tr><tr><td><p><strong>Up</strong> / <strong>Down</strong></p></td><td><p>Selects option above or below in scroll field’s list</p></td></tr></tbody></table></div>
