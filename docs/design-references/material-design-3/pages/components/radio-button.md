# Radio button

Source: https://m3.material.io/components/radio-button
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/091d4b7c-1ab2-4050-963a-4e2558ee5d08.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li id="isPasted">Use radio buttons (not <app-froala-tooltip-element description="Switches toggle the state of an item on or off." link-label="More on switches" link-url="/m3/pages/switch/overview" should-open-link-in-new-tab="true">switches</app-froala-tooltip-element>) when only one item can be selected from a <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/google-material-3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element></li><li>Label should be scannable</li><li>Selected items are more prominent than unselected items</li></ul>

1 radio button is selected from a list of 4 radio buttons of different ringtones.

<p>Radio buttons can be selected</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc92gkg1-01.png?alt=media

<h2 dir="ltr" id="isPasted">Resources &amp; availability</h2>

resourceName: designSystems/030656e0a1083ef1/components/18e98bbdcbc43596

libraryModuleType: STATUS_TABLE

<h2 id="isPasted">What’s new</h2>

<ul><li>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/google-material-3/pages/dynamic-color/overview" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element><p><br /></p></li></ul>

App screen with 1 active button selected from list of 3 buttons.

Radio buttons feature new color mappings

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0z3b8a-02.png?alt=media

## Specs

Diagram of enabled radio button.

<ol><li>Radio button icon</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmd8jp5v6-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/dhK9o6CpKl0rU0nNthzBHEz_WjPB264BCIZiXJisj5qoYSGwynygzLH2JUgl2RyYjyArXkZNMdlpDOC6MEm1gY36QdhZED-VFVcPsQuff1rHZg=s2048

<h2>Tokens &amp; specs</h2><p><a href="/m3/pages/design-tokens/overview" id="isPasted" style="box-sizing:border-box;text-decoration:underline;color:rgb(26, 115, 232)" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/6acb269a58d5f93f

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2 id="isPasted">Color</h2>

<p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

Diagram of selected and unselected radio button colors.

<p id="isPasted">Radio button color roles used for light and dark themes:</p><ol><li>Primary</li><li>On surface variant</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmd8jpn14-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/AiZMdjDtHEF9acx935WgjONj_Kvnb5Zl00C7Q1pxV56QjHx29o9tmyo4ACyJzafBGMDlrnOQBqScIiZY2mk205cbNAtBBqmtDAQR2ya7bcny=s2048

<h3>Adjacent text label color</h3><p>Use the <app-froala-tooltip-element description="Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme." link-label="More on color roles" link-url should-open-link-in-new-tab="true">color role</app-froala-tooltip-element> <strong>on surface</strong> for adjacent text labels. This remains the same even if interacting with the label or component.</p>

Radio buttons with labels. The labels are the same color for both selected and unselected radio buttons.

<p>The text color remains the same regardless if the button is selected or not</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmd8jq2c4-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/aFf7EK2cXKvdJegnbGx-u44UtDR9NZkQxw81UNCX4Q_D6_dvx_psq5rttJYfH9qytzYEkAxpFiNcej-7JO8Q0Mu6ySIq2h6sfDJN-BHFygZr=s1352

<h2>States</h2><p><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element> are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states/overview" target="_blank" rel="noopener noreferrer">Learn more about interaction states</a></p>

Diagram of radio button states including enabled, hover, focus, pressed, and disabled.

<ol><li>Enabled </li><li>Hover </li><li>Focus </li><li>Pressed</li><li>Disabled</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmd8jqfvs-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/batG4K9NgonMPOe8NtbqKBf_5HbQhLrGbpIrPzKU2lPdbMfVm8nbualfdj3tFA5cfGE9OLgj4lxybNV6a8-d90gixbpw7mm11V6ky0s5-ik=s2048

<p><a href="/m3/pages/radio-button/specs#3eef19a6-cdcb-4ecf-b1af-2b8095d485ac">State specs are in the token module above</a></p>

<h2>Measurements</h2>

Diagram of radio button layout values.

<p>Radio button size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmd8juo16-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Mix21eJwewQUVsSEPZiI8V9QtuoPH_Fw_CYVBaXX1vwpGyYgkN0dC8tdrO6WXjS-ADSW8GMMsDP5MNkMUF1i4izhNjHk7lsA8tAHRlZZ-L8H=s2048

<div class="table-wrapper"><table style="margin-right:calc(0%);width:100%" class="fr-table-selection-hover"><thead><tr><th style="text-align:center;width:69.6591%">Attribute<br /></th><th style="text-align:center;width:30.2273%">Value<br /></th></tr></thead><tbody><tr><th style="width:69.6591%">Icon size<br /></th><td>20dp</td></tr><tr><th style="width:69.6591%">State layer size<br /></th><td>40dp</td></tr><tr><th style="width:69.6591%">Target size<br /></th><td>48dp</td></tr></tbody></table></div>

## Guidelines

1 radio button is selected from a list of 4 radio buttons of different ringtones.

<p>Radio buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc92xj30-01.png?alt=media

<h2><span style="white-space:pre-wrap">Usage</span></h2>

<p id="isPasted">Radio buttons are the recommended way to allow users to make a single <app-froala-tooltip-element description="Selection lets users choose specific items to act on." link-label="More on selection" link-url="/m3/pages/selection" should-open-link-in-new-tab="true">selection</app-froala-tooltip-element> from a list of options. </p><p>Only one radio button can be selected at a time.</p>

1 of 3 languages is chosen using radio buttons. Selecting a language deselects the previous 1.

<p>Radio buttons should always be accompanied by clear inline labels</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmcelfjb2-GM3_Radio-button_Guidelines_02_IA_v01.mp4?alt=media

<p id="isPasted">Use radio buttons to:</p><ul><li>Select a single option from a set</li><li>Expose all available options</li></ul>

2 radio buttons are used for allowing or turning off notifications. 2 checkboxes are used for microphone and location access.

<p>Radio buttons are single-select, unlike checkboxes which are multi-select</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc93t2tz-03.png?alt=media

Filter page with 4 sort by options as radio buttons. Relevance is selected.

<p>Use radio buttons when only one option can be selected from a list</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc93whon-04-do.png?alt=media

Meal options page with the Additions item selected, along with 4 nested checkboxes for selecting various toppings. All checkboxes are selected.

<p>Use checkboxes when multiple options can be selected from a list</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc93wr1q-05-do.png?alt=media

<p>Avoid nesting radio buttons or using radio buttons to select multiple options.</p>

Selected radio button with 2 nested radio buttons.

<p>Don’t nest radio buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc93ykkg-06_dont.png?alt=media

2 radio buttons selected at once from a list of 3 buttons.

<p>Don’t allow radio buttons to select multiple options</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc93z4ss-07_dont.png?alt=media

<h3>Alternate selection controls</h3><p id="isPasted">Radio buttons are one of several <app-froala-tooltip-element description="Selection lets users choose specific items to act on." link-label="More on selection" link-url="/m3/pages/selection" should-open-link-in-new-tab="true">selection</app-froala-tooltip-element> controls, which allow people to make choices such as selecting options or switching settings on or off.</p><p><app-froala-tooltip-element description="Switches toggle the state of an item on or off." link-label="More on switches" link-url="/m3/pages/switch/overview" should-open-link-in-new-tab="true">Switches</app-froala-tooltip-element> and <app-froala-tooltip-element description="Checkboxes let users select one or more items from a list, or turn an item on or off." link-label="More on checkboxes" link-url="/m3/pages/checkbox/overview" should-open-link-in-new-tab="true">checkboxes</app-froala-tooltip-element> are alternative selection controls that can be used to change settings or preferences.</p>

A selected and unselected switch.

Switches

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc942yik-08.png?alt=media

An unselected and selected checkbox.

Checkboxes

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc942but-09.png?alt=media

<p id="isPasted">Use radio buttons when there are five or fewer options.</p><p>Consider using a drop-down <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element> instead of radio buttons when it’s important to save space on a screen. However, drop-down menus require additional steps for a person, both in the number of clicks and cognitive effort. </p>

A filter UI with 1 radio button selected from a list of 3 buttons.

<p>Use radio buttons when there are five or fewer options</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc944w0k-10-do.png?alt=media

A dropdown menu with a list of 4 options.

<p>Consider using a drop-down menu instead of radio buttons when space is constrained</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc945hgt-11-do.png?alt=media

<h2>Anatomy</h2>

3 elements of a radio button.

<ol><li>Selected icon</li><li>Adjacent label text</li><li>Unselected icon</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0z4md9-12.png?alt=media

<h3>Adjacent label text</h3><p id="isPasted">Always pair radio buttons with an adjacent label describing what the radio button selects.</p><p>Because only one radio button can be selected at a time, each choice must have its own label.</p>

Checkout page with 2 radio buttons for home and office addresses. The labels are "Home" and "Office."

<p>Radio button always need label text</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmcelh3zd-GM3_Radio-button_Guidelines_13_IA_v01.mp4?alt=media

<h2>Placement</h2>

<p>Radio buttons are often arranged in stacked <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/understanding-layout/overview" should-open-link-in-new-tab="true">layouts</app-froala-tooltip-element>.</p>

Settings page with 3 stacked radio buttons for selecting a language.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc949gf8-14.png?alt=media

<p id="isPasted">Radio buttons should be vertically listed and have one option always selected.</p><p><br /></p>

3 radio buttons with 1 option selected.

<p>Radio buttons should always have one option pre-selected</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc94bpsi-16_do.png?alt=media

2 radio buttons side by side with 1 option selected.

<p>Avoid using horizontal radio button lists</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwg86p38-16_caution.png?alt=media

<h2>Behavior</h2>

<p id="isPasted">A radio button is successfully selected when a person clicks or taps either the radio button icon or the label.</p>

Selecting the radio button for dark theme instantly changes the screen to dark theme.

<p>Radio buttons should take effect immediately, unless they're in a dialog or page that needs to be saved</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmcelja73-GM3_Radio-button_Guidelines_17_IA_v01.mp4?alt=media

## Accessibility

<h2>Use cases</h2><p>People should be able to do the following with assistive technology:</p><ul><li><p>Navigate to a radio button</p></li><li><p>Select a radio button</p></li><li><p>Get appropriate feedback based on <app-froala-tooltip-element description="Inputs are devices that provide interactive control of an app. Common inputs are a mouse, keyboard, and touchpad." link-label link-url should-open-link-in-new-tab="false">input</app-froala-tooltip-element> type</p></li></ul>

<h2 id="isPasted">Interaction &amp; style</h2><p id="isPasted">A radio button can be either selected or unselected. Selecting one radio button deselects any others. A radio group can start with one radio button selected, or none selected.</p><p>Once a radio button is selected, the group can’t be deselected. To let people opt out of their selection, either provide a <strong>Not applicable</strong> or <strong>No option</strong> radio button, or provide a separate way to deselect all radio buttons, like <strong>Clear selection</strong>.</p><p>People should be able to select either the text label or the radio button to select an option.</p>

Selecting between radio buttons for a home and office address.

<p>Only one radio button is selected at a time</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmcelaxg0-GM3_Radio-button_Accessibility_01_IA_v01.mp4?alt=media

<h3 id="isPasted">Avoid applying density by default</h3><p id="isPasted">Don't apply density to radio buttons by default. This lowers their targets below Material's recommendation of 48x48 CSS pixels. Instead, give people a way to choose a higher density, like selecting a denser layout or changing the theme.</p><p>To ensure this density setting can be easily reverted when it's active, keep all targets to change it at a minimum of 48x48 CSS pixels each.</p>

<h2>Initial focus</h2>

<p id="isPasted">When outside the radio group, <strong>Tab</strong> moves focus directly to the selected radio button, or the first one if none are selected. </p><p><strong>Shift+Tab</strong> instead focuses on the last radio if none are selected. </p><p>Use the <strong>arrows</strong> to navigate between options.</p>

The Tab key focuses on the first of 2 stacked radio buttons.

<p>Tab brings the focus to the initially selected item or the initial radio option </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmc94qafr-02.png?alt=media

The up and down arrow keys move through a list of stacked radio buttons.

<p>Arrows move to next element in a list</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0z51u6-03.png?alt=media

<h2 id="isPasted">Keyboard navigation</h2>

<div class="table-wrapper"><table id="isPasted" style="width:100%"><thead><tr><th style="width:15.3125%">Keys</th><th style="width:84.5976%">Actions</th></tr></thead><tbody><tr><th style="width:15.3125%"><strong>Tab</strong></th><td>Moves focus into the group to the selected radio button, or the first if none are selected</td></tr><tr><th style="width:15.3125%"><strong>Shift</strong> + <strong>Tab</strong></th><td>Moves focus into the group to the selected radio button, or the last if none are selected</td></tr><tr><th style="width:15.3125%"><strong>Arrows</strong></th><td>Moves focus and selects the previous or next radio button. Wraps focus and selection between the first and last radio buttons.</td></tr><tr><th style="width:15.3125%"><strong>Space</strong></th><td>Selects a focused radio button. If already selected, does nothing.</td></tr></tbody></table></div>

<h2 id="isPasted">Labeling elements</h2>

<p>If the UI text is correctly linked to the radio button, assistive tech such as a screenreader will read the UI text, followed by the component’s role.</p><p>The <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview/principles" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> label for a group of radio buttons is typically the same as its title. The role is <strong>Radio group</strong>.</p>

Accessibility tags for a radio button group.

<p>Label the radio group based on the category title</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd3jpo7w-04.png?alt=media

<p>The <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview/principles" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> label for an individual radio button is typically the same as its adjacent text label.</p>

Accessibility tags for a radio button.

<p>Label the radio button based on its label text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0z56zm-05.png?alt=media
