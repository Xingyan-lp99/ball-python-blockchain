# Switch

Source: https://m3.material.io/components/switch
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/a4ad43f1-5c39-44b2-ae15-a7110bdf4fa6.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Use switches (not <app-froala-tooltip-element description="Radio buttons let people select one option from a set of options." link-label="More on radio buttons" link-url="/m3/pages/radio-button/overview" should-open-link-in-new-tab="true">radio buttons</app-froala-tooltip-element>) if the items in a <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> can be independently controlled</p></li><li><p>Switches are the best way to let people adjust settings</p></li><li><p>Make sure the switch’s <app-froala-tooltip-element description="Selection lets users choose specific items to act on." link-label="More on selection" link-url="/m3/pages/selection" should-open-link-in-new-tab="true">selection</app-froala-tooltip-element> (on or off) is visible at a glance</p></li></ul>

A switch in two states, off and on.

<p>Switches can be toggled on and off</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwa9bnl5-1.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/0fe2e78f2f029241

libraryModuleType: STATUS_TABLE

<h2 id="isPasted">Differences from M2</h2>

<ul><li><p>Accessibility: Visual presentation is more accessible</p></li><li><p>Color: New color mappings meet Material's non-text-contrast requirements in addition to compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></p></li><li><p>Icons: Ability to have an optional icon within the switch handle</p></li><li><p>Layout: Track is taller and wider</p></li></ul>

M2 switches in off and on states.

<p>M2: Switches have a circular handle that extends beyond the edge of the track</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg65z0ro-02.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/8Q9gMTX5nAY3wJyezAw1JEzmJ6MbTAT3FkVUc7BIO9RUJ485PUwFFlXz7pAutMPh1eI0ScCnGFUd3nuAEfSb_Uo89uV3wfTPotf3njzsUwfo=s1004

M3 switch shown toggled off and toggled on. When switched on, it has a checkmark icon.

<p>M3: Switches have a taller and wider track, new color mappings, and the ability to show an icon in the handle</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg65zp7b-03.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/P_nhLNZtpt8oAPTScTR_d6oBLsidBWX0xG96t9fCkTURwNMReQpP9Etrpw4rc439wBfOAJBUeGZ39O8goRmRcPk_Ehhnq_wj7qNKFR4Sf70=s1004

## Specs

3 elements of a switch.

<ol><li>Track </li><li>Handle (formerly "thumb")</li><li>Icon</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg66415n-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/a4JkZitJC-KZ1qxKfHvM-B2tuC0JqMsA08tY-fRrBhlXDf6JpvjpQD9IAZ0_zg-R1E0tvzAst-VwpSYDGUkfGABeKMCgHcAtXPwan6iiuNILhA=s2048

<h2>Tokens &amp; specs</h2>

<p>Browse the component elements, attributes, tokens, and their values. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/33b1b2925d9ff561

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Color</h2><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview/" target="_blank">Learn more about design tokens</a></p>

6 color roles of a switch in light and dark themes.

<p id="isPasted">Switch color roles used for light and dark themes:</p><ol><li>Surface container highest</li><li>Outline</li><li>Outline</li><li>Primary</li><li>On primary</li><li>On primary container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg66ckmz-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/0fyIBhV6SPL8tV1Vk7CtpveaYQ1-am9tJ41EVA-QaywC5FoZ6CmY7Cevkh6gG8HklU2Ojaj4r0d4Po-J0MEVg2VLPzYo1R2FUey0lcFBTu-0=s2048

<h3>Adjacent text label color</h3><p>Use the <app-froala-tooltip-element description="Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme." link-label="More on color roles" link-url="/m3/pages/color-roles" should-open-link-in-new-tab="true">color role</app-froala-tooltip-element> <strong>on surface</strong> for adjacent text labels. This remains the same even if interacting with the label or component.</p>

The large body text adjacent to switches uses "on surface" color and the body text uses "on surface variant."

<p>The text label uses <strong>on surface</strong>. Supporting text may use <strong>on surface variant</strong>.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg66fz7u-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/0Xmcv7IiazLYf6Bpg_WWIU0Cnp32mkTymcUwcgN2QxXbvz2KyCIvTMXDW4sOR-m-jzDd4IO3aHqdSxaX4k73lKiVHr3mTXpkCBztSv60pJTM=s1352

<h2>States</h2><p><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element> are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states" target="_blank">Learn more about interaction states</a></p>

5 states of a switch shown in light and dark themes.

<ol class="decimal"><li><p>Enabled </p></li><li><p>Hovered </p></li><li><p>Focused </p></li><li><p>Pressed </p></li><li><p>Disabled</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg66iwsh-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/PnpKeMQPpfXYol0STNFLWY--Fet6iOSy9Skw-SxaiktaHsBbPbHkXNl2RX7aLYHsrUbIN8LwPshZzNEQF4AM1vqbj70iiVmdzzvwC69U64M=s2048

<p><a href="/m3/pages/switch/specs#3708644e-b4d7-4237-bb0a-7afeeae4a9b0" target="_self">State specs are in the token module above</a></p>

<h2>Measurements</h2>

Measurements of switches without icons.

<p>Switches without icons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg66jzjg-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/QjZaSle3gkHOtKy1j-YDhEIIdbjF3_Uy3kVXdJnmx7F4Gt-Af66rcmJpNFIKXrGIUg2NSEb9U4UAJ8kx1s50G9oIbfq_7fphlO8MoJd15uLp=s1004

Measurements of pressed switches without icons.

<p>Pressed switches without icons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg66kbil-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/vFaJZa1Ic9jL9_q6ayhWZw_21xhx2LeDKKJpLRhHisCUpo7tFW-cIHTOdD0mj75_m3ov2BhZQavFK8SqEkAm04X8rP8hE2YynD5so_vjZeev=s1004

Measurements of switches with icons.

<p>Switches with icons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg66mxl5-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/pOvYPjVd1P1HEOyZPLp4jziQmmbT5uMefs4zGCMSHg-fiRFgzXIeAz75RDSyfyZSu3yObf70vL6iiPgRVQtzDTWj8rZVaCR87l-gWjdz66Pr=s1004

Measurements of pressed switches with icons.

<p>Pressed switches with icons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg66nbzr-08-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/wZm_0fDk5iJbWdd6SZL2P6FkEw8Q94mZ9g0laAAb99hOsR4dk08iyhObA6p4OuqUuf8azFV_9Th006NHGZu2A8nw71qCl-DB_SRYOMAeIN4bHQ=s1004

<div class="table-wrapper"><table class="borderGGrey400"><thead><tr><th style="text-align:center"><p>Element</p></th><th style="text-align:center"><p>Attribute</p></th><th style="text-align:center"><p>Value</p></th></tr></thead><tbody><tr><th rowspan="4"><p>Track</p></th><td><p>Height</p></td><td><p>32dp</p></td></tr><tr><td><p>Width</p></td><td><p>52dp</p></td></tr><tr><td><p>Outline width</p></td><td><p>2dp</p></td></tr><tr><td><p>Shape</p></td><td><p><a href="/m3/pages/shape/corner-radius-scale#56e2bfb5-4bec-49bd-b3a3-bd822c8ab88e" target="_blank">md.sys.shape.corner.full</a></p></td></tr><tr><th rowspan="9"><p>Handle</p></th><td><p>Height (unselected)</p></td><td><p>16dp</p></td></tr><tr><td><p>Height - with icon</p></td><td><p>24dp</p></td></tr><tr><td><p>Height (selected)</p></td><td><p>24dp</p></td></tr><tr><td><p>Height (pressed)</p></td><td><p>28dp</p></td></tr><tr><td><p>Width (unselected)</p></td><td><p>16dp</p></td></tr><tr><td><p>Width - with icon</p></td><td><p>24dp</p></td></tr><tr><td><p>Width (selected)</p></td><td><p>24dp</p></td></tr><tr><td><p>Width (pressed)</p></td><td><p>28dp</p></td></tr><tr><td><p>Shape</p></td><td><p><a href="/m3/pages/shape/corner-radius-scale#56e2bfb5-4bec-49bd-b3a3-bd822c8ab88e" target="_blank">md.sys.shape.corner.full</a></p></td></tr><tr><th rowspan="2"><p>State layer</p></th><td><p>Size</p></td><td><p>40dp</p></td></tr><tr><td><p>Shape</p></td><td><p><a href="/m3/pages/shape/corner-radius-scale#56e2bfb5-4bec-49bd-b3a3-bd822c8ab88e" target="_blank">md.sys.shape.corner.full</a></p></td></tr><tr><th><p>Target</p></th><td><p>Size</p></td><td><p>48dp</p></td></tr><tr><th><p>Icon</p></th><td><p>Size (selected)</p></td><td><p>16dp</p></td></tr><tr><th><p>Icon</p></th><td><p>Size (unselected)</p></td><td><p>16dp</p></td></tr></tbody></table></div>

<h2 id="isPasted">Configurations</h2>

<ol id="isPasted"><li>Without icons</li><li>Icon on selected switch</li><li>Icon on selected and unselected switch</li></ol>

3 example switches with and without icons in on and off states. 

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg66of2m-09-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/yZbAEZRgNI6uOkunAfaXCx8NAExJ8RsY6DkIjWJMH0DanJdyakTEzO8YFyw1bd3AZdvfJv229_maPQKBRGGddH4NZm7PsouKM_oTEBs3-Bin=s1352

## Guidelines

A switch in 2 states, off and on.

<p>Switches change settings and other options immediately</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7sxhp8-01.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/x0AqjOgoDcYjaJyG017Y59vOzTxcqS5NfZ761rJ-Utb8JVw8_RZskFZTYAbBECIFqE23WBpO0Xufv97hXyAerK4lcsli48s_czxN65LlMLk=s2048

<h2 id="isPasted">Usage</h2>

<p>Switches are best used to adjust settings and other standalone options. </p><p>They make a binary <app-froala-tooltip-element description="Selection lets users choose specific items to act on." link-label="More on selection" link-url="/m3/pages/selection" should-open-link-in-new-tab="true">selection</app-froala-tooltip-element>:</p><ul><li><p>On and off</p></li><li><p>True and false</p></li></ul><p>The effects of a switch should start immediately, without needing to save.</p>

Toggling a switch turns on dark mode in Settings on a mobile device.

<p>Use a switch to turn an option on and off</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwa9phy3-GM3-Components-Switch-1-v01.mp4?alt=media

<p id="isPasted"><span style="white-space:pre-wrap">Use switches to:</span></p><ul><li><span style="white-space:pre-wrap">Toggle a single item on or off</span></li><li><span style="white-space:pre-wrap">Immediately activate or deactivate something</span></li></ul>

Switch used in notification settings to turn on and off the "play over notifications" function.

<p>Switches are commonly used on mobile to turn settings on or off</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7txet6-03.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/1tz8VDpVt3FDyf3v9iiqdxIEuIffJuOaXLSfHDYAN83CaPiKc_YZfO7KnZ2yVTmLNA-gmvxmdsHyXEjArew74BAk5HzKiM350ZagEXfzQ4qaWw=s1352

<p><span style="white-space:pre-wrap">Switches should be used instead of radio buttons if each item in a set can be independently controlled.</span></p>

Radio buttons used to select Wi-Fi or Bluetooth in the Settings app on a mobile device.

Use radio buttons to toggle items on or off. Radio buttons convey that a set of items are options and can only be selected one at a time. Instead use switches.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7tz5pr-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ri1tqY4CwpEqB-DkNZQe-P9niTffhljbYUVssp5O2xGLLPs5r8xPWMCDgYBpl2LTmGXkGLe7xw9tMtGAreZh1c49RD_mtwg0YQE4OKfM0zE=s1352

<p>Switches control binary options, not opposing ones. A binary option represents a single <app-froala-tooltip-element description="Selection lets users choose specific items to act on." link-label="More on selection" link-url="/m3/pages/selection" should-open-link-in-new-tab="true">selection</app-froala-tooltip-element> that's either on or off.</p><p>Opposing options are when only one option in a set can be selected at a time, like a <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> or map view. Use a <app-froala-tooltip-element description="Connected button groups have smaller inner corners and are best used for selection." link-label="More on button groups" link-url="/m3/pages/button-groups/overview" should-open-link-in-new-tab="true">connected button group</app-froala-tooltip-element> instead.</p>

A connected button group with options of List View and Map View.

<p>Use a connected button group to choose between opposing options</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7uio91-05%20-%20do.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/jH1Tkfo_kEijiXDqUqQIT2VMLZB213Hl414Jrmsh6jr0o_QYlwgLsm_8ikjo_XqhgeRa4wI5FrbMcdpLLgCx33GAabL-wWRJaNJDLSyPs5aV=s656

A switch with non-binary options of List View and Map View.

<p>Avoid using switches to toggle between opposing options</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7ukia8-06%20-%20dont.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/muDDs8mxZm8vsI9Bu335VCwdRY6E9Yx8mEUNab4_4FlUdRbaNPSFJCfWKOHTEcH6qj6R8p_E0wTt9xfp3nrbvXx0k_NWqpJYp97ZkEAoiMz_2Q=s656

<h3>Alternate selection controls</h3><p><app-froala-tooltip-element description="Checkboxes let users select one or more items from a list, or turn an item on or off." link-label="More on checkboxes" link-url="/m3/pages/checkbox/overview" should-open-link-in-new-tab="true">Checkboxes</app-froala-tooltip-element>, <app-froala-tooltip-element description="Radio buttons let people select one option from a set of options." link-label="More on radio buttons" link-url="/m3/pages/radio-button/overview" should-open-link-in-new-tab="true">radio buttons</app-froala-tooltip-element>, and switches are the three main kinds of selection controls. They help people make choices, like selecting options or turning settings on and off.</p><p>Use checkboxes to select multiple related options in a list.</p><p>Use radio buttons to select a single option in a list.</p><p>Use switches to select standalone or more verbose options in a list, like settings.</p>

2 checkboxes, 1 unchecked and 1 checked.

<p>Checkboxes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7ul4t0-07.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/xAewYZioxNc7YhmPjwIC4XEG7_8tdA6130j_66kfuFM3H3h2HH0wx8U1kVxPeNz4StMXWMJG0ICxNai-woryizyuiGfJyFBrvUfFqh2DrQ33=s656

2 radio buttons, 1 in an enabled state, 1 in a disabled state.

<p>Radio buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7ulhxp-08.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Xcgd1ZKjqsdww-in_mgrJ56JkF9t5rIVuJGByhtHWgjPDKPGYFRHlV_UU-HKcBCYbW3F9L9mZEwkmXlRl0JdLwUpTsklLQpiVfw_-dWEi80=s656

Mobile screen with checkboxes to select list items and call to action button to update the list.

<p>Use checkboxes (not switches) to let people select one or more options from a list</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7ustxv-09_Do.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/EeKlgEcp1KJ-9NfC7YPlsc0sQITFitnLnF1iY76rHsZKNPmeu0J5-a3xlnpj_tPlVvoEuQjX2pVze8dqv2WknsVejVR5idvAltny8CMraed79w=s1004

Mobile screen with checkboxes to select list items and call to action switch to update the list.

<p>A switch can't replace a button. People expect a call to action to be a button, not a switch.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7ut60g-10_Don't.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/wjSLtGs-C59hMUplsvCnFm1IjCYlMNcNUGUsnKoR28RxhApBz0YhW6AlO257nPdJ48NIUTezejDl3h3B3ZbgE4iBHQPMdu39mDkcLZ2VGze3=s1004

Radio buttons used to select a language for a mobile app.

<p>Use radio buttons (not switches) when only one item can be selected from a list</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7uvzmf-11_do.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/RP-OY6cXjDCXhDkZfdNQmY4crSy5rLCujf8DCTUaNSByNPt1XJYvpWHOZm0d5hLprgl_wfU9YZBGoh8ciq38frIAqP64CddYsZWCLQ4tHGA=s1004

Mobile screen with switches to select list items and call to action button to update the list.

<p>Avoid using a switch to select multiple options that require people to save. Switches should be immediate. Use checkboxes instead.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7vc3q1-12_don't.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/qhcoEcCH8obBM4P2DNuKMOOKaOgdApSQW-0OZVSc5UD46Ttzdkb_GproXkVIIVsl7jOklP8-8RZf0EzaIOZTUhOi16ruTe4LpFgQwPDnrvLQqQ=s1004

<h2 id="isPasted">Anatomy</h2>

3 elements of a switch. 

<ol><li>Track</li><li>Handle</li><li>Icon (optional)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7vge0i-13.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/3lI8U8eFaJEBDsf5YJz4e07h87cub5XTw2qWR3w7BbarbCWicdNE9AF4ewEp_r3qh_evjs105-t5KwM0OdO-ZEeC4-HFV75DIrHi3PyJE1-J=s2048

<h3 id="isPasted">Icon (optional)</h3><p>The switch handle can contain an optional icon.</p>

A checkmark appears on the filled circle of a handle when the switch is toggled on.

<p>The icon within the handle should always communicate the switch's selection</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwabkmev-GM3-Components-Switch-2-v01.mp4?alt=media

<p>Icons can be used to visually emphasize the switch’s <app-froala-tooltip-element description="Selection lets users choose specific items to act on." link-label="More on selection" link-url="/m3/pages/selection" should-open-link-in-new-tab="true">selection</app-froala-tooltip-element>. The icon’s meaning should be clear and unambiguous to help the people understand whether switch is on or off.</p>

2 switches, the unselected state icon is an X, and the selected state is a checkmark.

<p>Use icons that clearly communicate whether the switch is on or off, such as an X and a checkmark</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7vjfr0-15_Do.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/n_YcGWfROt1o6Ig3SUMsoD2AJnR1ONaC0AjgVUR9CIQ0_zAlMNw-wWfpshgAv5mru4RBPlzTym7BIW8-QZy0ZJMGqXwQ-mMXWP8suAgNL19G=s656

A switch’s unselected handle icon is a moon and the selected state icon is a pencil.

<p>Avoid using more ambiguous or non-binary icons, such as a moon or edit icon</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7vpyog-16_Don't.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LPCQ-Do-7xjhcg4Q-ocCdWlGZiku8V4RY86JpOCxYReqXVAswVegZ-TLmgF7ogz6UjS_zysFsBwyASHQbI4urmMnrKpdXxV0EEq4p8922SLRGQ=s656

<h3 id="isPasted">Label text</h3><p>Switches should always be paired with an inline label describing what the switch controls when selected.</p>

Switch label text: 1. Permission manager, App has access to your data. 2. Camera access, app has access to your camera. 3. Show password.

<p>Keep labels short and direct. A label should describe what the control does when the switch is on.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7vyj3y-17_do.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/A3Tr_ujhshFdU05BqNPGYMK-n-IYTjRkYIMgLkKqGfjYI5H3uU5oMweusuojA6wu8Xzn9TWID_iSe30uoYweAvECisDP0YKVG-ZEGHKUaT4=s1352

On a mobile screen’s privacy settings, 2 switches have “On” label text and checkmark icons. The last switch has “Off” label text and no icon.

<p>Don't add label text into the switch; the font size would be too small to be accessible. Use an appropriate icon instead.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7vz4xm-18_don't.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Yeafv6eDK5lXb6MUK2aXoRw6D8bo7TFoO62JYzQjQDdojRTeYEDf5iCU8M_MdA67qDGCoaqrAke1B0V_AQYSQy1ISTpT8kykUIKhjk2FvYcSzw=s1352

<h2 id="isPasted">Placement</h2>

<p>Switches are often arranged in stacked <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/understanding-layout/overview" should-open-link-in-new-tab="true">layouts</app-froala-tooltip-element>.</p>

Screen showing labels and stacked switches in varying on/off modes.

<p>Settings screens are common places to use switches</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg7xvplw-19_placement.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ZsqrkLA9mtmq2b2QpUDR2rtnKj9uidOEDais9zRVYzpypNMDiPrcugFoM26TU2BfwIEU2f8ayFkOCJTuuor-EnkTfcRC5AhzhoeJl0_5QK3OBg=s1352

<h2>Behavior</h2>

<p id="isPasted">A switch is successfully toggled when the handle slides to the other side of the track after an interaction.</p>

A switch is toggled to turn on airplane mode and Wi-Fi switch automatically turns off.

<p>When selected, the switch handle slides to the opposite end of the track</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwabqhfg-GM3-Components-Switch-3-v01.mp4?alt=media

<p>When a person toggles a switch, its handle size changes and the corresponding action takes effect immediately.</p>

When selected the switch’s handle gets larger and a checkmark appears on the filled circle.

<p>The <strong>on</strong> state of the switch is indicated by a larger handle size</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwabqzdx-GM3-Components-Switch-4-v01.mp4?alt=media

## Accessibility

<h2>Use cases</h2><p>People should be able to do the following with assistive technology:</p><ul><li><p>Navigate to a switch with a keyboard or switch input</p></li><li><p>Toggle the switch on and off</p></li><li><p>Get appropriate feedback based on input type documented under <a href="/m3/pages/switch/accessibility#c0e9fae1-48df-428b-b028-4f7be071ada3" target="_self">Interaction &amp; style</a></p></li></ul>

<h2>Interaction &amp; style</h2>

<p>The switch handle increases in size to indicate interactivity for both touch and cursor control interactions.</p><p><strong>Touch</strong><br />When tapped or <app-froala-tooltip-element description="A dragged state communicates when a user presses and moves an element." link-label="More on dragged state" link-url="/m3/pages/interaction-states/applying-states#c97582c4-5fef-42ce-9c34-71f8dcc5b8ad" should-open-link-in-new-tab="true">dragged</app-froala-tooltip-element>, the handle size grows, providing interaction feedback.</p><p><strong>Cursor</strong><br />When hovered (in both on and off <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">states</app-froala-tooltip-element>), the <app-froala-tooltip-element description="A hover state communicates when a user has placed a cursor above an interactive element." link-label="More on hover state" link-url="/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844" should-open-link-in-new-tab="true">hover</app-froala-tooltip-element> area grows, providing a visual cue that the handle is interactive. When clicked, the handle size grows.</p>

The switch handle increases in size when tapped and dragged.

<p>Touch: Tap, Drag</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg68ycaw-01.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/W9k8FZDab4FlAZdkKblIJVtCzjSJ48pu4wxgFourwAHfPsYc5RPK8gTPW4H7hVTj-hJNoR4iqQpZwdnoE14XBpGYLSk2_zBG7hWDC5YNt3r2ew=s656

The cursor changes from an arrow to a hand pointer when hovering over and clicking the switch.

<p>Cursor: Hover, Click</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg68z1uk-02.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/1waGLXuMxUHtjHjDVCcLWQF2ioH5mGvSRVlVJn9IO1rTSeiTTUE6pG2zQ6VskRok4RHejMQHucCfuiTKcoczKrjuyWT_hsyrERdMS7fJmp5P=s656

<h3 id="isPasted">Avoid applying density by default</h3><p>Don't apply density to switches by default — this lowers their targets below our best practice of 48x48 CSS pixels. Instead, give people a way to choose a higher density, like selecting a denser layout or changing the theme.</p><p>To ensure that this density setting can easily be reverted when it's active, keep all targets to change it at a minimum 48x48 CSS pixels each.</p>

<h2 id="isPasted">Initial focus</h2>

<p>Initial focus lands directly on the switch’s handle, since it’s the primary interactive element of the component. </p>

The focus is on the switch handle, which is toggled on.


<p>Focus lands on the switch handle</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg692flh-03.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ncRMKB_fQpAaCrlUNBYQ-UXNOAdAP-bmIlZy3hiiGoTic1gTMurPu6wqzFLKBTWIMrhDa3bhrLT4J9Ppg8OLP7BOxKLEKLWvo5egYkDEL8Gw=s656

Space or Enter is used to toggle the switch off.

<p>The switch is toggled using <strong>Space</strong> or <strong>Enter</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg692zv4-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/zJYFK9dmp7xQR83LnteRstjk0HCH3wuryW_dm29AYmjj3K4U6GM91uuwHh9CLjlV49GMndpgnSlYNMgXwR5_OCNySgR7eHvBJgU2MmWXjofVfw=s656

<h2 id="isPasted">Keyboard navigation</h2>

<div class="table-wrapper"><table style="margin-right:calc(0%);width:100%"><thead><tr><th>Keys</th><th>Actions</th></tr></thead><tbody><tr><th><strong>Tab</strong></th><td>Focus lands on the switch handle</td></tr><tr><th><strong>Space </strong>or<strong> Enter</strong></th><td>Toggles the handle on and off</td></tr></tbody></table></div>

<h2 id="isPasted">Labeling elements</h2>

<p>The <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> label for a switch uses the adjacent label text if implemented correctly. </p><p>Assistive tech such as a screen reader will read the UI text followed by the component’s role.</p>

“Dark theme” is the switch’s adjacent label text and the accessibility label.

<p>A switch’s accessibility label can incorporate its adjacent UI text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg695w5m-05.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/uQCgvmrYgUn5jsyprqaHwVc9uV4Jgg0cJR11xFDTeF-WdA4w1h72Cm-S3xtz6IwTdRUEpj7rt3vloFZFENV8Q1FVUjffGOptoHDsJYVpQKcqUg=s1352

<p>When the visible UI text is ambiguous, accessibility labels need to be more descriptive. For example, a switch visibly labelled <strong>Photo album</strong> would benefit from additional information to clarify the switch’s function.</p><p>Consider making the adjacent label text more descriptive when possible. This reduces the need for different accessibility text.</p>

The accessibility label for the switch is “Photo album access” though the label text is “photo album.”

<p>While the visible label text reads <strong>Photo album</strong>, the accessibility label for this switch clarifies its function: <strong>Photo album access</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg698bn2-06.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/RL42kRexZDwly3y3IIMPDdcDUEkd7C4jOQuq9me0IQa3vkWH9zl08KjI5yLcp6KCZIM7S8f56Oa4q3FHDC6TgTCJUVngGOWBalNaMtkAJekq=s1352
