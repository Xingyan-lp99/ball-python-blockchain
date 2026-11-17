# Checkbox

Source: https://m3.material.io/components/checkbox
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/c0332583-8417-4b80-a0a1-e283781d31c6.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li id="isPasted">Use checkboxes (instead of <app-froala-tooltip-element description="Switches toggle the state of an item on or off." link-label="More on switches" link-url="/m3/pages/switch/overview" should-open-link-in-new-tab="true">switches</app-froala-tooltip-element> or <app-froala-tooltip-element description="Radio buttons let people select one option from a set of options." link-label="More on radio buttons" link-url="/m3/pages/radio-button/overview" should-open-link-in-new-tab="true">radio buttons</app-froala-tooltip-element>) if multiple options can be selected from a <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element></li><li>Label should be scannable</li><li>Selected items are more prominent than unselected items</li></ul>

3 checkboxes in a diagram demonstrating all three states.

<p>Unselected, selected (hover), and indeterminate checkboxes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmcyjgb31-01.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/589af604996f7a3e

libraryModuleType: STATUS_TABLE

<h2>Differences from M2</h2>

<ul><li><p>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic-color/overview" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></p></li><li><p><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element>: New indeterminate states as well as error states for unselected, selected, and indeterminate</p></li></ul>

Color mapping of a checkbox in M2.


<p>M2</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmab66psf-2.png?alt=media

Color mapping of a checkbox in M3 with new color.

<p>M3</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmab66tlq-3.png?alt=media

## Specs

<h2>Tokens &amp; specs</h2><p>Browse the component elements, attributes, tokens, and their values.</p>

resourceName: designSystems/20543ce18892f7d9/components/31f16b44fe03b0c0

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Checkbox</h2>

Diagram of checkbox indicating the 2 parts of its anatomy.

<ol class="decimal"><li id="isPasted">Container </li><li>Icon</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmemmstmc-1-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/o7Jd5nbugG-76fMDJwv-WD-ardrEfZF5Nxfq_8Pikz0V6pnzJXvDA6C4NPzOpZ3z39Rjb6tb1yxxQs8GBhn0L11_ozezB4FsTlSHGIQrRFcz=s2048

<h2>Color</h2>

<p id="isPasted">Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

Checkbox color roles in light and dark themes.

<ol class="decimal"><li id="isPasted">Checkbox</li><li>State-layer</li><li>Icon</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmemmtsu5-2-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/tRScc_0bS1gM7jai2Ojj3qDzyhE696wedzZNPry2Pson8ONvZ_S_IoRUO6RwZBC5-YQUmgqLKG0xWldIJ5y_DT6lfRcty3F0JPY7pJvbqkZG=s2048

<h3>Adjacent text label color</h3><p>Use the <app-froala-tooltip-element description="Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme." link-label link-url should-open-link-in-new-tab="false">color role</app-froala-tooltip-element> <strong>on surface</strong> for adjacent text labels. This remains the same even if interacting with the label or component.</p>

Checkboxes with text labels. The text color is the same for checked and unchecked checkboxes.

<p>The text color remains the same regardless if the checkbox is selected or not</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmemmvnkr-3-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/712ygEoSMR9tGvygN9LKJ8DZ7BhOWkzxv1y86AilaXmqdTa30fz5WP68koUEZThkz30akxDDI3CUbIxJh6PeEKIj2HK48__RTspIhYMIFFeX=s1352

<h2>States</h2>

<p id="isPasted">States are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states/overview" target="_blank" rel="noopener noreferrer">Learn more about interaction states</a></p>

Side by side view of states in light and dark themes.

<ol class="decimal"><li id="isPasted">Enabled </li><li>Disabled </li><li>Hovered </li><li>Focused </li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmemmxoan-4-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Yor59BqmDg2qk4vgXtDVI9FzkAcqUFQZ4EjWrwLc_rYafcVTgirLkf-bt1t7JbvpRyPYQYvrP8ZM_ZgYUA17VWtk1h9UJcckiG_W0NPLDled=s2048

<h2>Measurements</h2>

Diagram of a selected checkbox with a container width and height of 18dp and a state-layer width and height of 40dp.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmemn204f-5-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/CcUqIZiHlrkBXYmqL54pCjCjsNpVnHsMf6QdUXITGzV89PkHrNbV84_w9I5ZgcNPlMFcCVbTxYhZzVbMESebqg2wWiSlqbYaRNstFOLT5P-s=s2048

<div class="table-wrapper"><table style="margin-right:calc(0%);width:100%"><thead><tr><th style="width:50.7425%;text-align:center">Attribute</th><th style="width:49.1676%;text-align:center">Value</th></tr></thead><tbody><tr><th><p>Container size</p></th><td><p>18dp</p></td></tr><tr><th><p>Container corner shape</p></th><td><p>2dp</p></td></tr><tr><th><p>Icon size</p></th><td><p>18dp</p></td></tr><tr><th><p>Icon alignment</p></th><td><p>Center-aligned</p></td></tr><tr><th><p>Target size</p></th><td><p>48dp</p></td></tr><tr><th>State-layer size</th><td>40dp</td></tr></tbody></table></div>

## Guidelines

A list of burger additions represented with checkboxes.

<p>Checkboxes in a list of items</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0yt1n6-1.png?alt=media

<h2>Usage</h2>

<p id="isPasted">Use checkboxes to: </p><ul><li>Select one or more options from a list</li><li>Present a list containing sub-selections</li><li>Turn an item on or off in a desktop environment</li><li>Visually group similar options together</li></ul>

List of 80's songs indicating choice through checkbox selection.

<p>Checkboxes select multiple, related options</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0vnl39-2.png?alt=media

<p>Checkboxes should be used instead of <app-froala-tooltip-element description="Switches toggle the state of an item on or off." link-label="More on switches" link-url="/m3/pages/switch/overview" should-open-link-in-new-tab="true">switches</app-froala-tooltip-element> if multiple, related options can be selected from a list. Checkboxes visually group similar items effectively and take up less space than switches.</p>

List indicating choice with checkbox selection.

<p>Checkboxes let users select one or more options from a list. A parent checkbox allows for easy selection or deselection of all items.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0vok05-3_do.png?alt=media

A list with multiple switches selected.

<p>If a list consists of multiple options, don't use switches. Instead, use checkboxes. Checkboxes imply the items are related, and take up less visual space.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0vwf9n-4_dont.png?alt=media

<h3>Alternate selection controls</h3><p>Checkboxes, <app-froala-tooltip-element description="Radio buttons let people select one option from a set of options." link-label="More on radio buttons" link-url="/m3/pages/radio-button/overview" should-open-link-in-new-tab="true">radio buttons</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Switches toggle the state of an item on or off." link-label="More on switches" link-url="/m3/pages/switch/overview" should-open-link-in-new-tab="true">switches</app-froala-tooltip-element> are the three main  selection controls. They all help people make choices, like selecting options or switching settings on or off.</p><ul><li><p>Use checkboxes to select multiple related options in a list.</p></li><li><p>Use radio buttons to select a single option in a list.</p></li><li><p>Use switches to select standalone or more verbose options in a list, like settings.</p></li></ul>

Diagram of 2 radio buttons, one selected and one unselected.

<p>Radio buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmcypcjyf-5.png?alt=media

Diagram of 2 switches, one selected and one unselected.

<p>Switches</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0vwj88-6.png?alt=media

<h2>Anatomy</h2>

Diagram of checkbox indicating the 2 parts of its anatomy.

<p id="isPasted">1. Container</p><p>2. Icon</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmcypfx6t-7.png?alt=media

<h2>Responsive layout</h2>

<p>In <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints</app-froala-tooltip-element>, placing checkboxes within a contained region such as a <app-froala-tooltip-element description="Side sheets show secondary content anchored to the side of the screen." link-label="More on side sheets" link-url="/google-material-3/pages/side-sheets/overview" should-open-link-in-new-tab="true">side sheet</app-froala-tooltip-element> can help group related controls and available actions.</p>

Desktop screen showing music albums and a side sheet containing checkboxes for filtering music genres.

<p>A side sheet can group related controls on larger screens</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0vp83b-8.png?alt=media

<h2>Behavior</h2>

<p>Multiple checkboxes in a list can be selected.</p>

Using checkboxes to select a list of extra ingredients, like pickles and tomatoes, to add to a meal.

<p>Selecting multiple items in a list using checkboxes</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj3f7ot-GM3-Components-Checkbox-Guidelines-1-v01.mp4?alt=media

<p id="isPasted">Checkboxes can have a parent-child relationship with other checkboxes.</p><ul><li>When the parent checkbox is checked, all child checkboxes are checked</li><li>If a parent checkbox is unchecked, all child checkboxes are unchecked</li><li>If some, but not all, child checkboxes are checked, the parent checkbox becomes an indeterminate checkbox. Checking an indeterminate checkbox checks all child items.</li></ul>

Checking parent checkbox also checks child items. Unchecking one child item makes parent indeterminate.

<p>Use a parent checkbox to make it more efficient to select many items</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj3h4ri-GM3-Components-Checkbox-Guidelines-2-v01.mp4?alt=media

<p id="isPasted">When selected, a checkbox clearly and instantly communicates its selected state.</p><p>If used to turn something on or off, the action should be immediately executed.</p>

Selecting a checkbox for turning on dark mode immediately changes the phone theme.

<p>Turning an item on or off using a checkbox</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj3iba1-GM3-Components-Checkbox-Guidelines-3-v01.mp4?alt=media

## Accessibility

<h2>Use cases</h2>

<p>People should be able to use assistive technology to:</p><ul><li><p>Navigate to a checkbox   </p></li><li><p>Toggle the checkbox on and off</p></li><li><p>Get appropriate feedback based on input type documented under <a href="/m3/pages/checkbox/accessibility#6a2f55e5-2fa0-4204-b6d1-62362dda89c7" target="_blank">Interaction &amp; style</a></p></li></ul>

<h2>Interaction &amp; style</h2>

<p>Users should be able to select either the text label or the checkbox to select an option.</p>

In a list, checkboxes for 2 items are selected via their text labels.

<p>A checkbox selected via the text label</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0vkh7s-1.png?alt=media

<p id="isPasted">The parent checkbox has three states: selected, unselected, and indeterminate. </p><p>Checkboxes can be selected or unselected regardless of the state of the other checkboxes in a group. </p><p>If some, but not all, child checkboxes are checked, the parent checkbox becomes indeterminate. Selecting an indeterminate parent checkbox will check all of its child checkboxes.</p>

In a list, a child checkbox for 1 item is selected and the parent checkbox is in indeterminate state.

<p>An indeterminate selection indicating that at least one checkbox is selected within a group</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmcyq4z51-2.png?alt=media

<h2 id="isPasted">Avoid applying density by default</h2>

<p id="isPasted">Don't apply density to checkboxes by default — this lowers their targets below our best practice of 48x48 CSS pixels. Instead, give people a way to choose a higher density, like selecting a denser layout or changing the theme.</p><p>To ensure that this density setting can be easily reverted when it's active, keep all the targets to change it at minimum 48x48 CSS pixels each.</p>

<h2>Keyboard navigation</h2>

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="width:17.15%">Keys</th><th style="width:82.85%">Actions</th></tr></thead><tbody><tr><td><strong>Tab</strong></td><td>Moves focus to <app-froala-tooltip-element description="An enabled state communicates an interactive component or element." link-label="More on enabled state" link-url="/m3/pages/interaction-states/applying-states#39b2fc90-01db-41b5-b6f8-47be61ed1479" should-open-link-in-new-tab="true">enabled</app-froala-tooltip-element> chip or chip group</td></tr><tr><td><strong>Space</strong> or <strong>Enter</strong></td><td>Activates, selects, or deselects the focused chip</td></tr><tr><td><strong>Backspace</strong> or <strong>Delete</strong></td><td>Removes currently <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element> input chip</td></tr><tr><td><strong>Arrows</strong></td><td>Moves focus between chips</td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<p>If the UI text is correctly linked to the checkbox, assistive tech (such as a screen reader) will read the UI text followed by the component’s role.</p><p>The <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview/principles" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> label for an individual checkbox is typically the same as its adjacent text label.</p>

Accessibility labels of a checkbox.

<p>The accessibility label clearly states the text label of the checkbox</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0vlqi0-3.png?alt=media
