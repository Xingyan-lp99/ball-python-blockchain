# States

Source: https://m3.material.io/foundations/interaction/states
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/b3339b30-4a6d-49b6-9a8b-8e581b2b1204.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

States show the interaction status of a component or UI element

## Overview

<ul><li id="isPasted">States have two visual indicators to ensure accessibility</li><li>States can be combined, such as selection and hover</li><li>Apply states consistently across components</li></ul>

<h2>Resources</h2>

<div align="left" dir="ltr"><div class="table-wrapper"><table class="borderGGrey200" style="margin-right:calc(0%);width:100%"><thead><tr><th style="width:25.385%">Type</th><th style="width:57.2954%">Link</th><th style="width:16.8547%">Status</th></tr></thead><tbody><tr><th style="width:25.385%;text-align:center">Design</th><td><a href="http://goo.gle/m3-design-kit" id="isPasted" rel="noopener noreferrer" target="_blank">Design Kit</a></td><td>Available</td></tr></tbody></table></div></div>

<p id="isPasted">1. <a href="/m3/pages/interaction-states/applying-states#39b2fc90-01db-41b5-b6f8-47be61ed1479">Enabled<br /></a>An enabled state communicates an interactive component or element.</p><p>2. <a href="/m3/pages/interaction-states/applying-states#4aff9c51-d20f-4580-a510-862d2e25e931">Disabled</a><br />A disabled state communicates an inoperable component or element.</p><p><br /></p>

Enabled button has a strong contrast between container and text.

<p>Enabled button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n4rwz-1p-Enabled%20button.png?alt=media

Disabled button has low contrast grey text on grey container.

<p>Disabled button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n5ghx-1p-Disabled%20button.png?alt=media

<p id="isPasted">3. <a href="/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844">Hover</a><br />A hover state communicates when a user has placed a cursor above an interactive element.</p><p>4. <a href="/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f">Focused</a><br />A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice.</p>

Cursor positioned over a button.

<p>Hovered button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2ndeib-1p-Hovered%20button.png?alt=media

The focused button has a strong contrast between container and text.

<p>Focused button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2negg3-1p-Focused%20button.png?alt=media

<p id="isPasted">5. <a href="/m3/pages/interaction-states/applying-states#c3690714-b741-492d-97b0-5fc1960e43e6">Pressed</a><br />A pressed state communicates a user tap.</p><p>6. <a href="/m3/pages/interaction-states/applying-states#c97582c4-5fef-42ce-9c34-71f8dcc5b8ad" id="isPasted">Dragged</a><br />A dragged state communicates when a user presses and moves an element.</p><p><br /></p>

The pressed button has a strong contrast between container and text.

<p><span style="white-space:pre-wrap">Pressed button</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2qd3dz-1p-Pressed%20button.png?alt=media

Dragged chip

<p>Dragged chip</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2qdrga-1p-Dragged%20chip.png?alt=media

## State layers

<h2 id="isPasted">State layers</h2>

<p>A state layer is a semi-transparent covering on an element that indicates its state. State layers provide a systematic approach to visualizing states by using opacity. A layer can be applied to an entire element or in a circular shape and only one state layer can be applied at a given time. </p>

<p>To transition from an enabled style to a stateful style requires the addition of a state layer. </p><p>The state layer is an overlay with a fixed opacity for each state and uses the same color as the content. </p><p>For example, if the enabled style uses the <strong>secondary container</strong> color for the container and <strong>on secondary container</strong> for content, the state layer will be an overlay using the <strong>on secondary container</strong> color.  </p><p>If the enabled style uses the <strong>surface</strong> color for the container and the <strong>primary</strong> color role for content, then the state layer will be an overlay using the <strong>primary</strong> color.</p>

State layer sandwiched between the container and content.

<ol><li>Container</li><li>State layer</li><li>Content</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2qh1yi-1p_State%20Layers_1.png?alt=media

<p>The size of state layers is 40dp while the interactive target size is 48dp.</p>

Interaction target is larger than the state layer.

<ol><li>State layer</li><li>Interactive target</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2qhye4-1p_State%20Layers_2.png?alt=media

<h3 id="isPasted">On colors</h3><p style="box-sizing:border-box;font-size:16px;font-weight:400;line-height:1.5rem"><span style="box-sizing:border-box;white-space:pre-wrap"><span style="box-sizing:border-box;white-space:pre-wrap">By default, a component’s state layer color is derived from the color of its content, either the color of an icon or label text if no icon is present.</span></span></p><p style="box-sizing:border-box;font-size:16px;font-weight:400;line-height:1.5rem"><span style="box-sizing:border-box;white-space:pre-wrap"><span style="box-sizing:border-box;white-space:pre-wrap">An </span></span><span style="box-sizing:border-box;white-space:pre-wrap"><span style="box-sizing:border-box;white-space:pre-wrap"><a href="/m3/pages/color-roles#19e75989-7485-4f5b-a769-940c4e4364bc">on color</a></span></span><span style="box-sizing:border-box;white-space:pre-wrap"><span style="box-sizing:border-box;white-space:pre-wrap"> is a color role used by the content. Each container color has its own corresponding on color. <br style="box-sizing:border-box" /><br style="box-sizing:border-box" />For example, if a container color is <strong>secondary container</strong>, the content will use the <strong>on secondary container</strong> color role. </span></span></p>

State layer sandwiched between  the content and container.

<p>Order of surface layers shows the state layer (2) between the container (1) and content (3) layers</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2qisol-1p_on_colors.png?alt=media

<h3>State layer tokens &amp; values</h3><p>The state layer uses a fixed percentage for the opacity for each state. A state layer uses the color used by content (usually the <a href="/m3/pages/color-roles#19e75989-7485-4f5b-a769-940c4e4364bc">on color</a>) and the percentage opacity for its respective state. </p>

The opacity values of four overlay states.

<p id="isPasted">Four overlay states and their values:</p><ol><li>Hover +8% opacity </li><li>Focus +10% opacity </li><li>Press +10% opacity</li><li>Drag +16% opacity</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2qnx2g-1p_state_layer_tokens%26value.png?alt=media

resourceName: designSystems/20543ce18892f7d9

libraryModuleType: TOKEN_TYPE_UNSPECIFIED

moduleConfigurationOverrides: {'tokenSets': ['State opacities']}

<h3 id="isPasted">Activated states</h3><p>Unlike hover, focus, pressed, and dragged states that use state layers, the container and content of activated components change color directly. </p><p>Activated components use the <strong>secondary container</strong> color for the component container and change the content color to <strong>on secondary container</strong>.</p>

Activated flights container with color changed compared to containers for hotels, and restaurants both not in activated state. 

<p>Activated state</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flfrg32kk-1p_Activated.png?alt=media

## Applying states

<h2>Enabled</h2>

<p>An enabled state communicates an interactive component or element. Enabled states use the default styling for each interactive component.</p>

Enabled state of 4 components.

<p id="isPasted">Enabled states for:</p><ol><li>Button</li><li>FAB</li><li>Switch</li><li>Text field</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2qpw4a-1.png?alt=media

<h2>Disabled</h2>

<p id="isPasted">A disabled state communicates when a component or element isn’t interactive. This state is visually communicated through color changes and reduced elevation.</p><p><strong>Disabled states don't need to meet Material's contrast requirements.</strong></p>

Low opacity solitary button labeled disabled, indicates a  disabled/inoperable state.

<p>Disabled button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2qrzig-2.png?alt=media

<p id="isPasted">Disabled states <strong>are</strong> inherited by action, selection, and input components:</p><ul><li>Buttons</li><li>Cards</li><li>Checkboxes</li><li>Chips</li><li>List items</li><li>Radio buttons</li><li>Switches</li><li>Text fields</li></ul>

Inoperable state of 4 components.

<p>Disabled states for:</p><ol><li id="isPasted">Checkbox</li><li id="isPasted">Icon button</li><li id="isPasted">Radio button</li><li id="isPasted">Segmented button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2qtg0r-3.png?alt=media

<p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Disabled states <strong>aren't</strong> inherited by communication, containment, navigation, and some actions components: </span></p><ul><li>App bars</li><li>Badges</li><li>Dialogs</li><li>Floating action buttons (FABs)</li><li>Menus</li><li>Navigation bar, drawer, and rail</li><li>Sheets</li><li>Tabs</li><li>Tooltips</li></ul>

Screen erroneously showing edit FAB in inoperable state, though the edit function is unavailable.

<p><span id="isPasted" style="white-space:pre-wrap">If the action represented in the FAB is unavailable, the FAB shouldn't appear</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2quyuj-4.png?alt=media

<h3 id="isPasted">Behavior</h3><p>Disabled components can’t be focused, dragged, or pressed, and they don’t change state when tapped or hovered over.</p>

A cursor moves over and clicks on an disabled/inoperable button and the button doesn’t change.

<p>A disabled button doesn’t inherit hover or other state layers</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2vtf7p-GM3-Foundations-Interaction-States-DisabledBehavior-v01.mp4?alt=media

<p>There can be any number of disabled states in a layout.</p>

Disabled components on a screen.

<ol><li>Disabled redo icon button</li><li>Disabled checklist icon button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyml0ix7-6.png?alt=media

<h2 id="isPasted">Hover</h2>

<p id="isPasted">Hover states are initiated by the user pausing over an interactive element using a cursor.</p><p>The lower-emphasis surface overlay for hover states can be applied to the entire component, elements within a component, or as a circular shape over part of the component.</p>

Cursor moves toward button which reads “enabled” and when the cursor touches the button text changes to “hovered.”

<p>Hovered button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2vwc74-7.png?alt=media

<p id="isPasted">Hover states <strong>are</strong> inherited by action, selection, and input components:</p><ul><li>Buttons</li><li>Cards</li><li>Checkbox</li><li>Chips</li><li>Date and time pickers</li><li>List items</li><li>Slider</li><li>Switch</li><li>Text fields</li></ul>

Hover state of 4 components.

<p>Hovered states for:</p><ol><li>FAB</li><li>Icon button</li><li>Chip</li><li>Segmented buttons</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2vxl8i-8.png?alt=media

<p id="isPasted">Hover states <strong>aren’t</strong> inherited by communication, containment, or navigation components: </p><ul><li>App bars</li><li>Badges</li><li>Dialogs</li><li>Menus</li><li>Navigation bar, drawer, and rail</li><li>Sheets</li><li>Tabs</li></ul>

Mobile screen with the whole  app bar wrongly in hover state.

<p>The individual components that are actionable within the app bar inherit hover states, not the whole app bar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2vymng-9.png?alt=media

<h3>Behavior</h3><p>Hover states are initiated by the user pausing over an interactive element using a cursor.</p>

Button’s text“Enabled”  changes to“Hovered” when cursor moves over the button.

<p>Hover states appear and disappear using a low-emphasis animated fade</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2w0utg-GM3-Foundations-Interaction-States-HoverBehavior-1-v01.mp4?alt=media

<p>Hover states can be combined with focused, activated, selected, or pressed states.</p>

Filter chip text matches state as it's unselected, hovered, and selected by a cursor.

<p>A selected filter chip in both selected and hover states</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmq7s3uq1-03%20-%20GM3-Foundations-Interaction-States-HoverBehavior-2-v02.mp4?alt=media

<p>There can only be one hover state at a time in a layout.</p>

Hover state moves from one card to another with cursor movement. 

<p>Hover state can only be on one element at a time based on cursor position</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2w8zl5-GM3-Foundations-Interaction-States-HoverBehavior-3-v01.mp4?alt=media

<h2 id="isPasted">Focused</h2>

<p id="isPasted">A focused state communicates when a user has highlighted an element using a keyboard or voice. Focus states apply to all interactive components.</p><p>The higher-emphasis surface overlay for focused states can be applied to the entire component, elements within a component, or as a circular shape over part of the component.</p>

A button in focused state.

<p>Focused button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wa79s-13.png?alt=media

<p id="isPasted">Focus states <strong>are</strong> inherited by action, selection, and input components:</p><ul><li>Buttons</li><li>Cards</li><li>Checkbox</li><li>Chips</li><li>Date and time pickers</li><li>List items</li><li>Selection controls</li><li>Text fields</li></ul>

Focus state of 4 components.

<p>Focused states for:</p><ol><li>FAB</li><li>Icon button</li><li>Chip</li><li>Segmented buttons</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wb5y9-14.png?alt=media

<p id="isPasted">Focus states <strong>aren’t</strong> inherited by most communication, containment, or navigation components:</p><ul><li>App bars</li><li>Badges</li><li>Banner</li><li>Card</li><li>Dialogs</li><li>Navigation bar, drawer, and rail</li><li>Sheets</li></ul>

Mobile screen showing  entire app bar in focus state, which is an error.

<p>The individual components that are actionable within the app bar inherit focus states, not the whole app bar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wctgk-15.png?alt=media

<h3>Keyboard focus indicator</h3><p id="isPasted">Many people use the <strong>Tab</strong> key or other shortcut to navigate the interactive elements of a web page, like links, buttons, and chips.</p><p>When an element is tabbed to, it appears in its focused state with a ring-like <strong>keyboard focus indicator</strong>. This indicator helps web users know where they are on the page.</p><p>While focused, an element can be acted on with the keyboard.</p>

A single filled button in focused state, displaying the keyboard focus indicator.

<p><span style="white-space:pre-wrap">Keyboard focus indicator for a filled button</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wdmfh-16.png?alt=media

<h3>Behavior</h3><p id="isPasted">Focus states are initiated by the user by pressing the <strong>Tab </strong>key on the keyboard (or equivalent).</p><p>Focus states can be represented in combination with hover, activated, or selected states.</p>

A single filter chip simultaneously in selected state and focus state.

<p>A selected filter chip in both selected and focused states</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wf3qd-17.png?alt=media

<p>There can only be one focus state at a time in a layout. </p>

Cursor moving from one card in focus state to another card moves the focus state to the second card. 

<p>A focus state applied to one card at a time</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2whda4-GM3-Foundations-Interaction-States-FocusedBehavior-v01.mp4?alt=media

<h2>Activated</h2>

<p id="isPasted">Activated states indicate which item from a set of options is currently being viewed. They are initiated either by default or user choice, using input methods such as a tap, cursor, keyboard, or voice input. </p><p><span style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)">Activated states are higher emphasis and signified by an overlay, color change, or other visual treatments applied to elements or segments within a component.</span></p>

The activated tab has a different color and shape than the enabled tabs.

<p>Activated tab</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flfolqn12-3p_activated_1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/PrC0KJRphE13vuSXtEjO2cO4nn26oY9nGQz0sjlgswCRj-mshMrXTDkzdXBszEKiji8QjGuU_StfxrxQAi2dakFPbV8N7y0ivGKrH_ub-y44aw=s1006

<p id="isPasted">An activated state differs from a selected state because it communicates a highlighted destination.</p><p><span style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)">Activation states </span><strong style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)">are</strong><span style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)"> inherited by items within some navigation components: </span></p><p>✓ Navigation bar, drawer, and rail<br /><span style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)">✓ Tabs</span></p>

The tab and navigation drawer are both in activated states.

<p>Tab (1) and navigation drawer (2) with activated states</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flfolsseo-3p_activated_2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/4nEJDl0aWZwwyifrFIfvWmnrHib-GP0elJ2eNtOS_CEwAHmIbv72yGQYGSBRZUK7Yknn5qhWA_fUa2xH5vN5Ttmb0hwaSxJ_p3_7m7MZ4_o=s1004

<p id="isPasted">Activation states <strong>aren’t</strong> inherited by action, communication, containment, selection, or input components: </p><p>✗ App bars<br /><span style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)">✗ Badges</span><br /><span style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)">✗ Buttons</span><br /><span style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)">✗ Checkbox</span><br /><span style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)">✗ Chips</span><br /><span style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)">✗ Dialogs</span><br /><span style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)">✗ Sheets</span><br /><span style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)">✗ Sliders</span><br /><span style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)">✗ Switch</span><br /><span style="font-size:1rem;background-color:initial;color:rgb(65, 65, 65)">✗ Text fields</span></p>

Activated state applied to a button in error.

<p>Activated states are applied to navigational components, like tab items, to indicate a destination, not action components, like a button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flfolueb4-3p_activated_3.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/sNdOI56GC4avCi3214qCHLBWA7tPWTr-6F13CYqcsvnL0y2gyOshzRDHLdvgJ6FUQVaGGhZkDilbpBimMZ2-b8L-XlWJqj3Etch0QG08BRnSEA=s1004

<h3 id="isPasted">Behavior</h3><p>Activated states can be represented in combination with hover and focus states.</p>

A cursor hovers over unselected button in a hovered state.  On a click it switches to active state.

<p><span style="white-space:pre-wrap">Activated states appear in user-initiated order</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flfom53fi-3P-activated%20behavior.mp4?alt=media

<p>Activated states can be represented in combination with hover and focus states.</p>

Screen showing inbox in focus and activated states.

<p>Activated states can be represented in combination with hover and focus</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flfom7o2z-3p_activated_behavior_2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/vrtQQz6zBdiObT4J_FFlEVvcWr3J0xb1n_fDc2TQjpMhv1atalwuodz9bWxW6TWwun29Tn9hiQz5NDEL7dJ6mz3hm76IZ4nK90lmCgHmf-QK=s2048

<p>Within a single set of options, only one activated state may be present at a time.</p>

Email settings navigation list “inbox”is activated. The selection components has one activated state as well.

<p>This activated navigational list differs from the selection components in the same layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flfomaa0z-3p_activated_behavior_2x_3.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/YAKYoWW_J4nyMs_Xz2Rm8RTnOr6751kiT4nJDdj1pDqqEZsJQDgsA-q4oKS3CBrsrw6pZUbntv8LpPLM_ETdtRjYFHXb2nFtiQ8kUNuzpWNBoQ=s2008

<h2 id="isPasted">Pressed</h2>

<p id="isPasted">A pressed state communicates a user-initiated tap or click via cursor, keyboard, or voice input. This state applies to all interactive components.</p><p>Pressed states trigger a change in composition and should be high-emphasis.</p><p>A ripple overlay signifies a pressed state. It can be applied to an entire component or elements within a component, or as a circular shape over part of the component.</p>

Button using a ripple overlay to signify it’s in a pressed state.

<p><span style="white-space:pre-wrap">Pressed button</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wj03t-25.png?alt=media

<p>Some components, such as buttons or cards, can inherit elevation to signify a pressed state.</p>

Button using elevation to signify it’s in a pressed state.

<p><span style="white-space:pre-wrap">Pressed button with elevation</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wk46q-26.png?alt=media

<p id="isPasted">Pressed states <strong>are</strong> inherited by action, selection, and some containment components: </p><ul><li>Buttons</li><li>Cards</li><li>Checkbox</li><li>Chips</li><li>List items</li><li>Text fields</li></ul>

Four components shown in pressed state.

<p>Pressed states for:</p><ol><li>FAB</li><li>Icon button</li><li>Chip</li><li>Segmented button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wl23l-27.png?alt=media

<p id="isPasted">Pressed states <strong>aren’t</strong> inherited by communication, navigation, or some containment components: </p><ul><li>App bars</li><li>Badges</li><li>Bottom navigation</li><li>Dialogs</li><li>Menus</li><li>Sheets</li><li>Tabs</li></ul>

Mobile screen showing  entire app bar in pressed state is an error.

<p>The individual components that are actionable within the app bar inherit pressed states, not the whole app bar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wo5k7-28.png?alt=media

<h3 id="isPasted">Behavior</h3><p>Pressed states are initiated by user keyboard or voice input on an interactive element.</p>

Enabled state activated to pressed state.

<p>Activated states appear in user-initiated order</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wqo0t-GM3-Foundations-Interaction-States-PressedBehavior-1-v01.mp4?alt=media

<p>Pressed states can be combined with hovered, focused, activated, or selected states.</p>

Hovered state activated to a pressed state.

<p>Activated states can be represented in combination with hover and focus</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wrufa-GM3-Foundations-Interaction-States-PressedBehavior-2-v01.mp4?alt=media

<p>There may only be a single pressed state at a time in a layout.</p>

Pressed state on one card at a time.

<p><span style="white-space:pre-wrap">A pressed state applied to one card at a time</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wt4k8-GM3-Foundations-Interaction-States-PressedBehavior-3-v01.mp4?alt=media

<h2>Dragged</h2>

<p id="isPasted">A dragged state occurs when a user presses and moves an element or component. Dragged states should be low emphasis, to avoid distracting users from their task.</p><p>Dragged states use a lower emphasis overlay. It can be applied to the entire component or to elements within a component.</p><p>Some components, such as list items, chips, or cards, can inherit elevation to signify a dragged state.</p>

List item shown in dragged state.

<p id="isPasted">Dragged list item</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wu37e-32.png?alt=media

<p id="isPasted">Dragged states <strong>are</strong> inherited by some containment and selection components: </p><ul><li>Cards</li><li>Chips</li><li>List items</li><li>Sliders</li></ul>

A chip and a card both shown in dragged state.

<p>Dragged states for:</p><ol><li>Chip</li><li>Card</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wv77r-33.png?alt=media

<p id="isPasted">Dragged states <strong>aren’t</strong> inherited by action, communication, navigation, or some containment components: </p><ul><li>App bars</li><li>Badges</li><li>Buttons</li><li>Dialogs</li><li>Menus</li><li>Navigation bar, drawer, and rail</li></ul>

Mobile screen with app bar in dragged state is an error.

<p>Components like an app bar that require consistent placement should not inherit dragged states</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2ww2lq-34.png?alt=media

<h3 id="isPasted">Behavior</h3><p>Dragged states are initiated when users touch and hold elements, using an input method such as a tap or click.</p>

Going through the states of a draggable list item:  enabled, hovered, dragged.

<p>A list item in a dragged state</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wxglg-GM3-Foundations-Interaction-States-DraggedBehavior-1-v01.mp4?alt=media

<p>There may only be a single dragged state at a time within a layout.</p>

Cursor dragging cards one at a time.

<p>Dragged state applied to one card at a time</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2wyr5e-GM3-Foundations-Interaction-States-DraggedBehavior-2-v01.mp4?alt=media
