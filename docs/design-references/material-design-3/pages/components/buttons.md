# Buttons

Source: https://m3.material.io/components/buttons
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/e31df68a-59d4-41dc-8743-8c48b476d4f8.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Two variants: default and toggle</p></li><li><p>Can contain an optional leading icon</p></li><li><p>Five color options: elevated, filled, tonal, outlined, and text</p></li><li><p>Five size recommendations: extra small, small, medium, large, and extra large</p></li><li><p>Two shape options: round and square</p></li><li><p>Keep labels concise and use sentence case</p></li></ul>

5 variants of buttons.

<ol><li><span style="white-space:pre-wrap">Elevated button<br /></span></li><li><span style="white-space:pre-wrap">Filled button<br /></span></li><li><span style="white-space:pre-wrap">Filled tonal button<br /></span></li><li><span style="white-space:pre-wrap">Outlined button<br /></span></li><li><span style="white-space:pre-wrap">Text button</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm1qv5u-01.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/4c66f2c4b2f2cb18

libraryModuleType: STATUS_TABLE

<h2>M3 Expressive update</h2>

<p><strong>May 2025</strong></p><p>Buttons now have a wider variety of shapes and sizes, toggle functionality, and can change shape when selected. <a href="https://m3.material.io/blog/building-with-m3-expressive" target="_self">More on M3 Expressive</a></p>

<p>Variants and naming:</p><ul><li><p>Default and toggle (selection)</p></li><li><p>Color styles are now configurations (elevated, filled, tonal, outlined, text)</p></li></ul><p>Shapes: </p><ul><li><p>Round and square</p></li><li><p>Shape morphs when pressed</p></li><li><p>Shape morphs when selected</p></li></ul><p>Sizes:</p><ul><li><p>Extra small</p></li><li><p>Small (existing, default)</p></li><li><p>Medium</p></li><li><p>Large</p></li><li><p>Extra large</p></li></ul><p>New padding for <strong>small</strong> buttons:</p><ul><li><p>16dp (recommended to match padding of new sizes)</p></li><li><p>24dp (no longer recommended)</p></li></ul>

4 button changes in the expressive update.

<ol class="decimal"><li><span style="white-space:pre-wrap">Five sizes<br /></span></li><li><span style="white-space:pre-wrap">Toggle (selection)<br /></span></li><li><span style="white-space:pre-wrap">Two shapes<br /></span></li><li><span style="white-space:pre-wrap">Two small padding widths</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm1tos0-03.png?alt=media

<h2>Differences from M2</h2>

<ul><li><p>Color: New color mappings and compatibility with dynamic color. Icons and labels now share the same color. Neutral text button is no longer recommended.</p></li><li><p>Icons: Standard size for leading and trailing icons is now 20dp</p></li><li><p>Shape: Fully-rounded corner radius and additional height options</p></li></ul>

Rectangular M2 buttons.

<p>M2: Buttons have a height of 36dp and slightly rounded corner radius</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm1vatd-04.png?alt=media

Round-cornered M3 buttons.

<p>M3: Default buttons are taller at 40dp and have fully rounded corners</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm1vtk3-05.png?alt=media

## Specs

<h2>Variants</h2>

Diagram comparing buttons with toggle buttons.

<ol class="decimal"><li><p>Default button</p></li><li><p>Toggle button</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmnhhn4lk-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/aWhLmNGkz1dTgFMtkYbi73APlAcBdOgT9xviQJI1Riu10oLOdnakrGGJv6HBp6_9LHBw9lPT-lqF_xNp_Es_lsO2J0W-zT4MewEEILa9OQZZzw=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Variant</p></th><th style="text-align:center"><p>M3</p></th><th style="text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td><p>Default</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Toggle (selection)</p></td><td><p>--</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Configurations</h2>

Diagram showing configurations of buttons.

<ol class="decimal"><li><span style="white-space:pre-wrap">Size<br /></span></li><li><span style="white-space:pre-wrap">Shape<br /></span></li><li><span style="white-space:pre-wrap">Color<br /></span></li><li><span style="white-space:pre-wrap">Small button padding</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmneq41m-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/qtqOoy4NuC3QFb7pfhfLLiZPXFCDrM-rLo38WY2V4ao1NGmIml-wNHF0Gk4ydIEttrZsWWGMlACpZAu5YiQZTrK5NaG52Zqr0PSE4IpQVBoi=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Category</p></th><th><p>Configuration</p></th><th style="text-align:center"><p>M3</p></th><th style="text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td rowspan="2" style="width:25%"><p>Size</p></td><td><p>Small (default)</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>XS, M, L, XL</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td rowspan="2" style="width:25%"><p>Shape</p></td><td><p>Round (default)</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Square</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td><p>Color</p></td><td><p>Elevated, filled (default), tonal, outlined, text</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td rowspan="2" style="width:25%"><p>Small button padding</p></td><td><p>24dp</p></td><td><p>Available</p></td><td><p>Not recommended.</p><p>Use 16dp</p></td></tr><tr><td><p>16dp</p></td><td><p>--</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Tokens &amp; specs</h2><p>Use the table's menu to select a token set. Button token sets are separated into common tokens, color, and size. <a href="/m3/pages/common-buttons/specs#c305d304-a6c0-466a-a48c-8d0718a29ae2" target="_self">View baseline tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/1c4257f8804f9478

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Button - Color - Elevated', 'Button - Color - Filled', 'Button - Color - Tonal', 'Button - Color - Outlined', 'Button - Color - Text', 'Button - Size - Xsmall', 'Button - Size - Small', 'Button - Size - Medium', 'Button - Size - Large', 'Button - Size - Xlarge'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['[Deprecated] Button - Tonal', '[Deprecated] Button - Elevated', '[Deprecated] Button – Outlined', '[Deprecated] Button - Filled', '[Deprecated] Button - Text', 'Button - Color - Elevated', 'Button - Color - Filled', 'Button - Color - Tonal', 'Button - Color - Outlined', 'Button - Color - Text', 'Button - Size - Xsmall', 'Button - Size - Small', 'Button - Size - Medium', 'Button - Size - Large', 'Button - Size - Xlarge', 'Button (baseline)'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Anatomy</h2>

Diagram labeling 3 parts of a button.

<ol class="decimal"><li><span style="white-space:pre-wrap">Container<br /></span></li><li><span style="white-space:pre-wrap">Label text<br /></span></li><li><span style="white-space:pre-wrap">Icon (optional)</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmneqix9-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Vd3wDLwuuQXUGiUdmogIFMY3V4WzpDIz9WvepaTJAmdJhaiKXTxshhrlEwJizdXlvsISt1vMjtSw5AdEr74lkf-uocBR-renjDhE95DrK05r=s2048

<h2>Color</h2>

<p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value.</p><ul><li><p>There are five built-in button color styles: elevated, filled, tonal, outlined, and text</p></li><li><p>The default and toggle buttons use different colors</p></li><li><p>Toggle buttons don’t use the text style</p></li></ul>

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">These color roles were chosen to create design coherence and familiarity. Other color roles can be used as long as the container and text have a 3:1 contrast ratio. For example, tertiary and on tertiary.</div></div></div>

Diagram shows dark and light color schemes for buttons.

<p>A. Elevated, B. Filled, C. Tonal, D. Outlined, E. Text</p><ol class="decimal"><li><span style="white-space:pre-wrap">Default<br /></span></li><li><span style="white-space:pre-wrap">Toggle: unselected<br /></span></li><li><span style="white-space:pre-wrap">Toggle: selected</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmner6e7-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/rniAgyk0C8Ys1AH7Lxciu7xnv8p_HA8iVm0AmoTKx5Ntedg_FdE0W66BG1udiPwCbGek3f0g8R2vlirupxprvRfYX8ID2uslj_bVROAMHgI=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:24.9774%"><p></p></th><th style="width:24.9774%"><p>1. Default</p></th><th style="width:24.9774%"><p>2. Toggle unselected</p></th><th style="width:24.9774%"><p>3. Toggle selected</p></th></tr></thead><tbody><tr><td><p>Elevated container</p><p>Elevated icon &amp; label</p></td><td><p>Surface container low</p><p>Primary</p></td><td><p>Surface container low</p><p>Primary</p></td><td><p>Primary</p><p>On primary</p></td></tr><tr><td><p>Filled container</p><p>Filled icon &amp; label</p></td><td><p>Primary<br />On primary</p></td><td><p>Surface container</p><p>On surface variant</p></td><td><p>Primary</p><p>On primary</p></td></tr><tr><td><p>Tonal container</p><p>Tonal icon &amp; label</p></td><td><p>Secondary container</p><p>On secondary container</p></td><td><p>Secondary container</p><p>On secondary container</p></td><td><p>Secondary</p><p>On secondary</p></td></tr><tr><td><p>Outlined container</p><p>Outlined icon &amp; label</p></td><td><p>Outline variant (outline)</p><p>On surface variant</p></td><td><p>Outline variant (outline)</p><p>On surface variant</p></td><td><p>Inverse surface</p><p>Inverse on surface</p></td></tr><tr><td><p>Text icon &amp; label</p></td><td><p>Primary</p></td><td><p>--</p></td><td><p>--</p></td></tr></tbody></table></div>

<h3>High contrast</h3>

<p><span style="white-space:pre-wrap" id="isPasted">High contrast mode is an accessibility feature that aims to maximize legibility by using a limited color palette, like black and white. Focus rings are shown when buttons are focused.</span></p>

High contrast mode for each variant and style of button.

<p>A. Elevated, B. Filled, C. Tonal, D. Outlined, E. Text</p><ol class="decimal"><li><span style="white-space:pre-wrap">Enabled <br /></span></li><li><span style="white-space:pre-wrap">Enabled &amp; focused <br /></span></li><li><span style="white-space:pre-wrap">Selected<br /></span></li><li><span style="white-space:pre-wrap">Selected &amp; focused</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlpy0ie-05.png?alt=media

<h2>States</h2>

<p><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element> are visual representations used to communicate the status of a component or interactive element.</p>

<h3>Elevated button states</h3><p>The elevated button style has an elevation of 1 by default and 0 when disabled.</p>

<h4>Default</h4>

Elevated button states.

<ol class="decimal"><li id="isPasted">Enabled</li><li>Disabled</li><li>Hovered</li><li>Focused</li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmnesmjm-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/n_5apeWPNXiSqDwG3UYvNY5A-FyHJOvbkdqH0Mq47KIxzVbHAq76C6DM1jG_TYTWiHgMPMjgdWA8N3zSKVM2ISe5HiS3MdV5P_u6A8rscjg=s2048

<h4>Toggle</h4>

Toggle elevated button states.

<p id="isPasted">A. Unselected, B. Selected</p><ol class="decimal"><li>Enabled </li><li>Disabled </li><li>Hovered </li><li>Focused </li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmnet1qn-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/GQDxPmCDjJpgGWRA_VTNzseTsmouIs0lh8IVP8woIQk4cgCiAnDMZThBIfxG1GHEqTlUoL585KoCLj8c-1gmGB4OXQJs9qhHkSyjVB0ad6tE=s2048

<h3>Filled button states</h3>

<h4>Default</h4>

Filled button states.

<ol class="decimal"><li id="isPasted">Enabled</li><li>Disabled</li><li>Hovered</li><li>Focused</li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmneu2zl-08-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/RwG9SEB4yIRACbW517DyRW2mUveISG198EE64jJb0f277Q33MLyuP9uiKdCmeWhZeWKXDx_yRiSQtlWlpaFp2kRVRX7LlCN5TWc-QwwqszbX3Q=s2048

<h4>Toggle</h4>

Toggle filled button states.

<p id="isPasted">A. Unselected, B. Selected</p><ol class="decimal"><li>Enabled </li><li>Disabled </li><li>Hovered </li><li>Focused </li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmnhkhbya-09-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/oM057IT2WiygsF0GMglnN22051Pgx_Xop2in-So8huFo-CUC5_gyPnBYksLf-wCXu4r6pZJQ1Qg9tPTvn5MUNHjXHilHCB-dPu7kkAF4PhVc=s2048

<h3 id="isPasted">Tonal button states</h3>

<h4>Default</h4>

Tonal button states.

<ol class="decimal"><li id="isPasted">Enabled</li><li>Disabled</li><li>Hovered</li><li>Focused</li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmneuv7c-10-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/wdF2kYSVD8W-FnPza7kOisTKCDc5FZKUskKzi8j3yZ0m7Ras4cKeoBCwUjpRr4EXjlSia_UfiRWFCCXl4VhbU9ZiwpbpVZetlqdtRGey0LU=s2048

<h4>Toggle</h4>

Toggle tonal button states.

<p id="isPasted">A. Unselected, B. Selected</p><ol class="decimal"><li>Enabled </li><li>Disabled </li><li>Hovered </li><li>Focused </li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmnevsol-11-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/SKh3_709LukNHRLX1h-4h3GWRx_g-PfrLaU28b33QM11qyAwNH2d-NPumu2KYhi9TECvF2QqeQ4ptDYUxgdMvdYTbcTiwmm-dsg6CS8Bd_0=s2048

<h3 id="isPasted">Outlined button states</h3>

<p>The outlined button’s container fill is invisible at rest, but the opacity and state layers behave the same as other button styles when disabled, hovered, focused, or pressed.</p>

<h4>Default</h4>

Outlined button states.

<ol class="decimal"><li id="isPasted">Enabled</li><li>Disabled</li><li>Hovered</li><li>Focused</li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmnewg2s-12-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/0RiSKbIPPzMC64WPAmZrA0Xi2bxyaBAQ8vmzHpEp1yjrhjSJqC0xv3_4jJgYaqh7v4BH7lAJZXkkN_HVyyIupF2JQQWfsYkCl5w2Pd_HEq90=s2048

<h4>Toggle</h4>

Outlined button states.

<ol class="decimal"><li id="isPasted">Enabled</li><li>Disabled</li><li>Hovered</li><li>Focused</li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmnexggd-13-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/U9yJ0EWfejvgr2j2FQRTLwN2Fk4H0pM4JxoYvRkql-jgBFGSqS26j--nqv_a23AL1Fhsjk5GAjgK4E1h_zDezwK_14acNyWL1Gy4_DWIgkY=s2048

<h3 id="isPasted">Text button style states</h3>

<p>The text button’s container is invisible at rest, but the opacity and state layers behave the same as other button styles when disabled, hovered, focused, or pressed. There is no toggle text button.</p>

Default text button style states.

<ol class="decimal"><li id="isPasted">Enabled</li><li>Disabled</li><li>Hovered</li><li>Focused</li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmneyf25-14-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/BYjS_Tdp0yXd5Dh1aupX_ELYzONtiZU21cT0y1kA5Pb3ne2T43AcIQ85r6jYIkHW6yRp0kQb7TNPiw5qKB9OuAyLUK1GKAa84krq1YOktFnf=s2048

<h2>Shape morph</h2>

<h3>Pressed state</h3><p>When pressed, buttons can morph to become more square. Both round and square buttons should have the same pressed shape.</p><p>The corner radius value differs for each button size. <a href="/m3/pages/common-buttons/specs#b1f39738-6f3a-409b-8f08-4cab6d78d756" target="_self">See full button corner measurements</a></p>

Shape changes of a button.

<p id="isPasted">A. Round button, B. Square button</p><ol class="decimal"><li>Enabled</li><li>Hovered</li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmneyrwe-15-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Si9asaI7X7SFuvDU46W5nHcZ9p9EVqCsu1Tb4Qfp1iPp2ho_kp85z_RXtK9EcyBqT5eoV-A4i8sJSQeDlY-tBGTl21KSLqLGpzM66hTvyZ67=s1352

<h3>When selected</h3><p id="isPasted">In addition to changing shape when pressed, toggle buttons also change the resting shape from round (unselected) to square (selected). </p><p>If the resting unselected shape is square, the selected shape should be round.</p>

Shape changes of a toggle button.

<p>A. Round button, B. Square button</p><ol class="decimal"><li><p>Enabled</p></li><li><p>Hovered</p></li><li><p>Pressed</p></li><li><p>Selected</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmnezbyl-16-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/5hC5Vdz-txbFAuGYY8Bkij-tCNyyjHc1B2zDoFQ5WWkR9Aw6yCNB8hKYi3CO0DJ2xlNab2JbXSPsm4HrByy21SU6_KVLN7PYaiSOeDlSmsbc=s1352

<h2>Measurements</h2>

Diagram of measurements of all button sizes.

<p><span style="white-space:pre-wrap">Padding and size measurements of each button size</span></p><ol class="decimal"><li><span style="white-space:pre-wrap">Extra small<br /></span></li><li><span style="white-space:pre-wrap">Small<br /></span></li><li><span style="white-space:pre-wrap">Medium<br /></span></li><li><span style="white-space:pre-wrap">Large<br /></span></li><li><span style="white-space:pre-wrap">Extra large</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmnf0bsj-17-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/JI2E9iCMwHgDDeC9fzCaTP1M974jPyBdpsV1OJoM83PKO0IINS4OUaPbdn9iT6ogQQqtFeBYb_IBT_sycEUkj3S6t4KEjZbGE1xT7-RL0JDX=s2048

<h3>Target areas</h3>

<p id="isPasted">Extra small and small icon buttons must have a target size of 48x48dp or larger to be accessible.</p>

Diagram of small button target areas.

<p id="isPasted">A. Extra small  B. Small</p><ol class="decimal"><li>Round button </li><li>Button with icon</li><li>Square button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmnf0o8e-18-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/35JMIvVuBd4UPv4LMpZ6rM_Hkn4S2UZlra92CcqY20cPp9334PxNr8KPaR-1P1d8q6Emonifwrp79hmxD5e2Ia_FQBDuKQhTKptbwn8uvPNZUQ=s1352

<h3>Corner sizes</h3>

Diagram of corner radii of buttons.

<p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmnf14u5-19-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/sULNWNl9-8wPo3EiYHaqeFSTE3FnFXFotQmIJzabpV-JJPCaSWvwhK3u82A6CeaMqBYmQz3dyWBArTDULDf2FRWfTYV2ZtrX0IA2na9bdbJa=s2050

<div class="table-wrapper"><table style="width:100%"><thead><tr><th><br /></th><th style="text-align:center">XS<br /></th><th style="text-align:center">S<br /></th><th style="text-align:center">M<br /></th><th style="text-align:center">L<br /></th><th style="text-align:center">XL<br /></th></tr></thead><tbody><tr><td>A. Round button</td><td>Full</td><td>Full</td><td>Full</td><td>Full</td><td>Full</td></tr><tr><td>B. Square button</td><td>12dp</td><td>12dp</td><td>16dp</td><td>28dp</td><td>28dp</td></tr><tr><td>C. Pressed state</td><td>8dp</td><td>8dp</td><td>12dp</td><td>16dp</td><td>16dp</td></tr></tbody></table></div>

<h2>Baseline tokens</h2>

<p>Use the table's menu to switch token sets. The baseline button token sets are organized by color. </p>

resourceName: designSystems/20543ce18892f7d9/components/1c4257f8804f9478

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['[Deprecated] Button - Elevated', '[Deprecated] Button - Filled', '[Deprecated] Button - Tonal', '[Deprecated] Button – Outlined', '[Deprecated] Button - Text'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['[Deprecated] Button - Elevated', '[Deprecated] Button - Filled', '[Deprecated] Button - Tonal', '[Deprecated] Button – Outlined', '[Deprecated] Button - Text', 'Button - Color - Elevated', 'Button - Color - Tonal', 'Button - Color - Outlined', 'Button - Color - Text', 'Button - Size - Xlarge', 'Button - Size - Large', 'Button - Size - Small', 'Button - Size - Xsmall', 'Button - Size - Medium', 'Button - Color - Filled', 'Button'], 'hideSearchField': False, 'hideVersionName': True}

## Guidelines

Buttons in various shapes and sizes.

<p>Buttons and icon buttons come in many shapes, styles, and sizes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlqkp7g-01.png?alt=media

<h2>Usage</h2>

<p>Buttons communicate actions that people can take. They are typically placed throughout the UI, in places like:</p><ul><li><p><app-froala-tooltip-element description="Dialogs provide important prompts in a user flow." link-label="More on dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">Dialogs</app-froala-tooltip-element></p></li><li><p>Modal windows</p></li><li><p>Forms</p></li><li><p><app-froala-tooltip-element description="Cards display content and actions about a single subject." link-label="More on cards" link-url="/m3/pages/cards/overview" should-open-link-in-new-tab="true">Cards</app-froala-tooltip-element></p></li><li><p><app-froala-tooltip-element description="Toolbars display frequently used actions relevant to the current page." link-label="More on toolbars" link-url="/m3/pages/toolbars/overview" should-open-link-in-new-tab="true">Toolbars</app-froala-tooltip-element></p></li></ul><p>They can also be placed within <app-froala-tooltip-element description="Standard button groups add interactions between adjacent buttons when they're pressed." link-label="More on button groups" link-url="/m3/pages/button-groups/overview" should-open-link-in-new-tab="true">standard button groups</app-froala-tooltip-element>.</p>

Video call app with prominent filled button to join and end a call.

<p>Use visually-prominent filled buttons for the most important actions</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlqnl0b-GM3%20-%20Commom%20Buttons%20-%20Guidelines%2002%20-%20v01.mp4?alt=media

<p>Buttons are just one option for representing actions in a product and shouldn’t be overused. Too many buttons on a screen can disrupt the visual hierarchy.<br /><br />Consider placing additional actions in a <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rail" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element>, set of <app-froala-tooltip-element description="Chips help people enter information, make selections, filter content, or trigger actions." link-label="More on chips" link-url="/m3/pages/chips/overview" should-open-link-in-new-tab="true">chips</app-froala-tooltip-element>, text links, or <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon buttons</app-froala-tooltip-element>.</p>

1 button placed on bottom right of screen.

<p>Use buttons for discrete actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlqpj6e-03-do.png?alt=media

3 buttons side by side on bottom of screen.

<p>Don’t clutter your UI with too many buttons. Consider presenting low-priority actions in overflow menus or as icon buttons.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlqpykn-04-don't.png?alt=media

Filled button on menu screen.

<p>A button container’s width is dynamically set to fit its label text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlqs2ix-05-do.png?alt=media

Filled button as wide as layout grid.

<p>Button container width can be responsive, which allows it to stretch horizontally</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlqslcx-06-do.png?alt=media

Filled button with label text overflowing the container. 

<p>A button container’s width shouldn’t be narrower than its label text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlqt8jf-07-don't.png?alt=media

Diagram of button styles and toggle behaviors.

<p id="isPasted"><span style="white-space:pre-wrap">A: Default button; B: Toggle (unselected); C: Toggle (selected) for five button styles, in order of emphasis:</span></p><ol class="decimal"><li><span style="white-space:pre-wrap">Elevated button<br /></span></li><li><span style="white-space:pre-wrap">Filled button<br /></span></li><li><span style="white-space:pre-wrap">Filled tonal button<br /></span></li><li><span style="white-space:pre-wrap">Outlined button</span></li><li><span style="white-space:pre-wrap">Text button</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlquaj1-08.png?alt=media

<p>A <app-froala-tooltip-element description="Button groups organize buttons and add interactions between them" link-label="More on button groups" link-url="/m3/pages/button-groups/overview" should-open-link-in-new-tab="true">button group</app-froala-tooltip-element> is a collection of buttons that relate to each other and can respond to one another. Both buttons and icon buttons can be used inside a button group.<br /><br />In some cases, there are primary and secondary actions within a button group. Buttons with primary actions should have a higher visual emphasis through size, color, or shape.</p><p><a href="/m3/pages/button-groups/overview" target="_self">More on button groups</a></p>

Audio app with play, next, and back buttons.

<p><span style="white-space:pre-wrap">Different sized buttons in a button group help emphasize the main action from secondary actions</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm3t81e1q-9.png?alt=media

<h2 id="isPasted">Toggle buttons</h2>

<p id="isPasted">Toggle buttons should be used for binary selections, such as <strong>Save</strong> or <strong>Favorite</strong>. When toggle buttons are pressed, they can change color, shape, and labels.</p><p>Toggle buttons should use an outlined icon when unselected, and a filled version of the icon when selected. If a filled version doesn’t exist, increase the weight instead.</p><p><span style="white-space:pre-wrap" id="isPasted">By default, toggle buttons change from round to square when selected.</span></p>

Toggle “stop” button in timer app.

<p>Use toggle buttons for binary actions</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlt2zdp-GM3%20-%20Commom%20Buttons%20-%20Guidelines%2010%20-%20v01.mp4?alt=media

<p>If the label changes on selected or unselected states, be mindful of the character count. Changing the label significantly is disruptive to the user and the page layout.</p>

Toggleable “start” and “reset” buttons.

<p>When using toggleable buttons, keep the label character count a similar length for both states</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlt4ivd-11-do.png?alt=media

Toggleable “start” and “reset back to beginning” buttons.

<p>The label length shouldn’t change dramatically to be longer or shorter</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlt52gk-12-dont.png?alt=media

<h2 id="isPasted">Anatomy</h2>

3 parts of a button.

<ol><li>Label text</li><li>Container</li><li>Icon (optional)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlt6b63-13.png?alt=media

<h3 id="isPasted">Label text</h3><p><span style="white-space:pre-wrap">Label text is the most important element of a button. It describes the action that will occur if someone taps a button. It should be very brief, ideally 1–3 words.</span></p><p><span style="white-space:pre-wrap">Use sentence case, which only capitalizes the first word and proper nouns. This allows the text to distinguish proper nouns, for example: <strong>Book with Flights</strong>, not <strong>BOOK WITH FLIGHTS</strong>.</span></p><p><span style="white-space:pre-wrap">Don’t truncate or wrap label text. It should always be fully visible on a single line.</span></p>

Button with label text “See all recipes.”

<p>Use sentence case for button label text, capitalizing the first word and proper nouns</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlt7k3u-14-do.png?alt=media

Button with wrapped label.

<p>Don’t wrap text. For maximum legibility, label text should remain on a single line.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlt7yj0-15-dont.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">Buttons with the <strong>outlined</strong> and <strong>text</strong> color style depend on the colors to be recognizable from other text and elements. Use caution when putting these buttons next to visually similar elements, such as chips or large text.</span></p>

Chips next to an outlined button, highlighting their similarities.

<p>The outlined button style is very similar to chips. Consider using a filled or tonal button instead.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlt97u1-16-%20caution.png?alt=media

<h3>Container</h3><p>Button containers hold the label text and optional icon. Buttons with the <strong>text</strong> color style have a visible container only when hovered, focused, or pressed.</p><p>Buttons with a round shape have containers with fully rounded corners.</p>

Round button.

<p>Round buttons have containers with fully rounded corners</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmltabq2-17.png?alt=media

<p>Buttons with a square shape have containers with more subtle rounding that changes based on button size.</p>

Square buttons with different radii.

<p>Square buttons have square containers and change radius as the button size changes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmltba1r-18.png?alt=media

Button with the label text “Edit playlist” within the container.

<p><span style="white-space:pre-wrap">A button’s width dynamically adjusts to the label text</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmltc6hg-19-do.png?alt=media

Button with text larger than its container.

<p>Avoid setting a fixed width smaller than the label text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmltdu8d-20-dont.png?alt=media

<h3>Icon (optional)</h3><p>Icons visually communicate the button’s action and help draw attention. They should be placed on the leading side of the button, before the label text.</p>

Filled button with the icon to the left of the label in a left-to-right language.

<p>Place the icon to the left of the label in buttons with text in left-to-right languages</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmltfge9-21-do.png?alt=media

Filled button with the icon to the right of the label in a right-to-left language.

<p>Place the icon to the right of the label in buttons with text in right-to-left languages</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmltfyz4-22-do.png?alt=media

Button with shopping cart icon and text label “Add to cart”.

<p>Use icons that clearly communicate their meaning</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlthjj7-23-do.png?alt=media

Button with Plus icon vertically above the text label “Add to watch list”.

<p>Don’t vertically align an icon and text in the center of a button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmltnhb2-24-dont.png?alt=media

Button with two icons.

<p>Don’t use two icons in the same button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmltof7i-25-dont.png?alt=media

<h2>Color styles</h2>

<h3>Elevated style</h3>

<p>The <strong>elevated</strong> button style is the same as the tonal button, but with a shadow. </p><p>To avoid overusing shadows, use the elevated style only when absolutely necessary, such as when the button requires visual separation from a visually prominent background.</p>

Elevated button on a scrim background.

<p>Elevated buttons provide separation from a visually prominent background</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmltpyn5-26.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">Buttons at higher elevations typically have more emphasis in a design, and should be used sparingly. For high emphasis, consider the filled style instead.</span></p>

Elevated button in a shopping experience.

<p>Higher elevation increases the emphasis of a button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmltrnw9-27-caution.png?alt=media

<h3 id="isPasted">Filled style</h3>

<p>The <strong>filled</strong> button style has the most visual impact after the <app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/m3/pages/fab/overview" should-open-link-in-new-tab="true">FAB</app-froala-tooltip-element>, and should be used for important, final actions that complete a flow, like <strong>Save</strong>, <strong>Join now</strong>, or <strong>Confirm</strong>.</p>

Filled button reading “Make payment.”

<p>Filled buttons have high visual impact when used for important actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlz52ml-28.png?alt=media

<p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Since they have such strong emphasis, the filled style should be used sparingly, ideally for only one action on a page.</span></p><p>In some cases, filled buttons can use tertiary colors.</p>

Filled “pause” button in a music app.

<p>Filled buttons can be responsive to the layout grid and help emphasize main actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmlz6rew-29.png?alt=media

<h3>Tonal style</h3>

<p><span style="white-space:pre-wrap" id="isPasted">The <strong>tonal</strong> button style is useful in contexts where a lower-priority button requires slightly more emphasis than an outline would give, such as <strong>Next</strong> in an onboarding flow. Tonal buttons use the secondary color mapping.</span></p>

Shopping app with 2 tonal-style filled buttons.

<p><span style="white-space:pre-wrap">The tonal style has less emphasis than filled or emphasis</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0gmxc-30.png?alt=media

<h3 id="isPasted">Outlined style</h3>

<p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">The <strong>outlined</strong> style is ideal for medium-emphasis buttons which contain actions that are important, but aren’t the primary action in a product.</span></p><p><span style="white-space:pre-wrap" id="isPasted">Outlined buttons pair well with filled buttons to indicate alternative, secondary actions.</span></p>

Outlined buttons for less important actions, including a back button and a button that reads “Next movie.”

<p>Outlined buttons contain less important supporting actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0loal-31.png?alt=media

<p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Outlined buttons display a stroke around the button container, and have no fill by default. <br /><br />They should be placed on simple backgrounds, not visually prominent backgrounds such as images or videos. </span></p>

Outlined button for “add to cart” in shopping app.

<p>Outlined buttons display a stroke around the button container</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0mtua-32.png?alt=media

Outlined button labeled Add to calendar on a pink/purple background.

<p>Outlined buttons can be used on backgrounds with a color gradient</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0nymp-33-do.png?alt=media

2 photos, each with an outlined button with a custom fill.

Use caution when placing outlined buttons on top of images. Customizing the button to have a contrasting container fill can help ensure legibility of label text. Or, use a filled button instead.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0oqjx-34-caution.png?alt=media

<h3 id="isPasted">Text style</h3>

<p>The text button style should be used for the lowest priority actions, especially when presenting multiple options.</p><p>They should be placed on simple backgrounds, not visually prominent backgrounds such as images or videos. The container isn’t visible until someone interacts with the button.</p><p>Don’t underline the text button. Use hyperlinked body text instead to emphasize links. <a href="/m3/pages/typography/applying-type#24856f70-f759-45df-a06c-92018f286083" target="_self">More on hyperlinks</a></p>

Example calendar screen with 2 text buttons and 1 split button.

<p>Use text buttons for the lowest priority actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0q822-35.png?alt=media

<p>Text buttons are often placed within components such as <app-froala-tooltip-element description="Cards display content and actions about a single subject." link-label="More on cards" link-url="/m3/pages/cards/overview" should-open-link-in-new-tab="true">cards</app-froala-tooltip-element>, <app-froala-tooltip-element description="Dialogs provide important prompts in a user flow." link-label="More on dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">dialogs</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Snackbars show short updates about app processes at the bottom of the screen." link-label="More on snackbars" link-url="/m3/pages/snackbar/overview" should-open-link-in-new-tab="true">snackbars</app-froala-tooltip-element>. Since text buttons don’t have a visible container in their default <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">state</app-froala-tooltip-element>, they don’t distract from nearby content.</p><p>However, since there’s no container, the label text color must always be recognizable from non-button text and elements.</p>

Text button labeled “Retry” in a snackbar.

<p>Text button in a snackbar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0rpw4-36.png?alt=media

Text button labeled “View album” on an album cover background.

<p>Text button against an image background</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0s6c1-37.png?alt=media

<p>In cards, text buttons help maintain an emphasis on card content.</p>

Text button labeled “Learn more” in an information card about sourdough bread.

<p>Text button in a card</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0tlmd-38.png?alt=media

<p id="isPasted">Dialogs use text buttons because the absence of a container helps unify the action with the dialog text.</p><p>Align text buttons to the trailing edge of dialogs, on the right for left-to-right languages and on the left for right-to-left languages.</p>

Modal dialog with the title “Subscribe to our newsletter?” and trailing buttons “Cancel” and “Subscribe”.

<p>Text buttons in a dialog</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0v0go-39.png?alt=media

<h2><span style="white-space:pre-wrap" id="isPasted">Adaptive design</span></h2>

<h3><span style="white-space:pre-wrap" id="isPasted">Resizing</span></h3>

<p><span style="white-space:pre-wrap" id="isPasted">When scaling layouts for large screen devices, buttons can adapt their visual presentation, size, alignment, and arrangement to fit different contexts and user needs.</span></p>

<p>Choose the best button position based on screen size.</p>

Flights app in compact screen with buttons below flight information.

<p><span style="white-space:pre-wrap">Filled buttons are end-aligned below flight information in a compact window</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0vwgx-41.png?alt=media

Flights app in large screen with buttons to the left of flight information.

<p><span style="white-space:pre-wrap">Filled buttons are start-aligned beside flight information in a large window</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0wuqe-40.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">The icon and label text in a button stay centered and grouped as the button's width changes.</span></p>

2 buttons with horizontally centered text labels.

<p><span style="white-space:pre-wrap">Keep the icon and label text grouped and centered</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0y1g6-42-do.png?alt=media

1 button with centered text label, 1 button with icon and label aligned to opposite edges.

<p>Don't ungroup the icon and label text or let them anchor to opposite sides of the button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0yith-43-dont.png?alt=media

<p>Buttons can be customized to change size and scaling behavior across different <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element>. </p><p>To avoid creating very long buttons in large windows, constrain button width or place buttons beside other elements.</p>

Button width is over-stretched with screen width.

<p>Don’t allow the button to stretch in a way that creates long, flat buttons with very little content inside</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm0zsof-44-dont.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Presentation</span></h3>

<p>The size and placement of buttons can change as parent containers, such as cards, adapt for larger screens. </p><p><span style="white-space:pre-wrap" id="isPasted">Keep items, including buttons, in the same order between large and small screens to provide a consistent experience for screen readers and keyboard navigation.</span></p>

2 buttons scaling to accommodate different device sizes.

<p><span style="white-space:pre-wrap">Buttons can move in the layout, but elements should remain in the same order</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm11hfb-45.png?alt=media

## Accessibility

<h2 id="isPasted">Use cases</h2><p>People should be able to do the following with assistive technology: </p><ul><li>Use a button to perform an action</li><li>Navigate to and activate a button  </li></ul>

<h2>Interaction &amp; style</h2>

<h3>Color contrast</h3><p><span style="white-space:pre-wrap" id="isPasted">Enabled buttons need a 3:1 contrast ratio with the background to meet accessibility best practices. </span></p><p><span style="white-space:pre-wrap">This is measured from the container for elevated, filled, and tonal button styles, and the label text for outlined and text button styles.</span></p>

Diagram of color contrast ratios for buttons.

<p>Higher contrast helps differentiate elements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm13hkn-01.png?alt=media

<h3>200% text size</h3><p>Avoid excessive text wrapping or truncation by choosing concise strings. </p><p>On Android, button labels should be kept concise enough to fit within two lines after the text size is increased to 200%. If a button label exceeds this limit and gets truncated, provide an alternative way to access the full content in a single tap.</p>

200% text size on a mobile screen. The overly long button text wraps to a second line: “Download playlist for offline access”.

<p>Avoid excessive text wrapping or truncation by choosing concise strings</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm14hok-02-caution.png?alt=media

<h3>Rapid clicks</h3><p>On the web, you can use a modified motion curve to avoid resonant effects from overlapping animations. This provides a smoother experience for interactions where you anticipate multiple clicks or taps in succession.</p>

A media player where the “next track” button is clicked rapidly, and is transformed with a smooth motion effect.

<p>Use the modified motion curve if rapid click or pointer interactions are expected</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm15x7t-GM3_Buttons_Accesibility%2004%20-%20v02.mp4?alt=media

<h2 id="isPasted">Keyboard navigation</h2>

<div class="table-wrapper"><table style="margin-right:calc(0%);width:100%" class="fr-table-selection-hover"><thead><tr><th style="width:26.3889%">Keys</th><th style="width:73.4903%">Actions</th></tr></thead><tbody><tr><th style="width:26.3889%">Tab</th><td>Navigate to a button</td></tr><tr><th style="width:26.3889%">Space or Enter</th><td>Activate a button</td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<p>The <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label link-url should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> label for a button should match the visible label text on the button such as <strong>Done</strong>, <strong>Send</strong>, or <strong>Reply</strong>. </p><p>It can contain extra contextual information if necessary.</p>

Accessibility tags for a text-only button.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmmm17kt7-03.png?alt=media
