# Sliders

Source: https://m3.material.io/components/sliders
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/4d160e88-c954-4614-8d11-4ec3ed399c92.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Three variants: Standard, centered, range</p></li><li><p>Has five sizes, vertical and horizontal orientation, and an optional inset icon</p></li><li><p>Sliders should present the full range of available values</p></li><li><p>The slider value should take effect immediately</p></li></ul>

A vertical slider changes the brightness of bedroom lights.

<p>Sliders change values along a range</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7ll9aj1-GM3_Expressive_Slider_Overview_01_IA_V01.mp4?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/59e0e5381ea8f766

libraryModuleType: STATUS_TABLE

moduleConfigurationOverrides: {'headings': ['Type', 'Resource', 'Status']}

<h2>M3 Expressive update</h2>

<p><strong>May 2025</strong></p><p>The slider includes expressive configurations for orientation, shape sizes, and an inset icon. <a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank" rel="noopener noreferrer">More on M3 Expressive</a></p>

<p>Updated on Android Views (MDC-Android) and Jetpack Compose.</p><p>Variants and naming: </p><ul><li><p>Changed <strong>continuous</strong> slider to <strong>standard</strong> slider</p></li><li><p>The <strong>discrete</strong> slider is now the <strong>stops</strong> configuration</p></li></ul><p>New configurations: </p><ul><li><p>Orientation: Horizontal, vertical</p></li><li><p>Optional inset icon (standard slider only)</p></li><li><p>Sizes: XS (existing default), S, M, L, XL</p></li></ul>

3 M3 Expressive sliders.

<ol><li>Standard slider</li><li id="isPasted">Centered slider</li><li id="isPasted">Range slider</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lii3kv-02.png?alt=media

<h2>Previous updates</h2>

<h3>Visual refresh to improve non-text contrast</h3><p><strong>Dec 2023:</strong> Updated on Android Views (MDC-Android) and Jetpack Compose.</p><ul><li><p><strong>Configuration:</strong> Added centered configuration and range selection</p></li><li><p><strong>Shape: </strong>New shape for slider tracks and handles. Slider elements change shape when selected.</p></li><li><p><strong>Motion:</strong> Slider handle adjusts width upon selection. Slider tracks adjust in shape when sliding to the edge.</p></li><li><p><strong>Color: </strong>Refreshed color mappings</p></li></ul>

M3 visually-refreshed slider.

<p>M3 visual refresh: Sliders have a stop indicator, larger label text, and a vertical handle that narrows when pressed. Centered sliders start from the middle instead of the leading edge.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lirx37-03.png?alt=media

<h2 id="isPasted">Differences from M2</h2>

<ul><li><strong>Color</strong>: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></li></ul>

M2 slider.

<p>M2: Sliders have a circular handle and a small label when pressed</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7livqfr-04.png?alt=media

Original M3 slider.

<p>M3: Sliders have new color mappings and support dynamic color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7liwct9-05.png?alt=media

## Specs

<h2>Variants</h2>

3 variants of sliders.

<ol class="decimal"><li><p>Standard</p></li><li><p>Centered</p></li><li><p>Range</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6a7kht-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-UgZpnEJ6uET5STSdzpCWEydsoa9cfqtNAbzpuKX9-4jQ3d8IdU0EjRtpfgizjIX8I7XM-ETfXPEnfKi7XNZSQWJTTyKrLHjS95bsb6ZQc7smQ=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="text-align:left"><p>Variant</p></th><th style="text-align:center"><p>M3</p></th><th style="text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td><p>Standard</p></td><td><p>Available as “continuous” slider</p></td><td><p>Available</p></td></tr><tr><td><p>Centered</p></td><td><p>Available (web only)</p></td><td><p>Available</p></td></tr><tr><td><p>Range</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Discrete</p></td><td><p>Available</p></td><td><p>Available as “stops” configuration</p></td></tr></tbody></table></div>

<h2>Configurations</h2>

Orientation and size configurations of sliders.

<ol class="decimal"><li>Orientation: Horizontal, vertical</li><li id="isPasted">Size: XS, S, M, L, XL</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6a86b2-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/PUKZpvA88_wvpKTUHRmGx0XIOjDEUAFWbO14A9AMUDyX-mu0w9qTo7ywQTKCcm8ERhdQHoohHwHt3Z-Tqo29eVw4_KyVf3pn-Z-UIcsszrYc=s2048

Optional anatomy configurations of sliders.

<ol class="decimal"><li>Inset icon</li><li>Stops </li><li id="isPasted">Value indicator</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6a8q7u-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/QFc1hXc78XHCuqhH4no1fQLDRvSzLaW1K8El5jIW1v3K3sNXjMquxEGcaq22u48Mq5kCqGRoPSCD7m8H37sAwyP_XyI6xY4AJp2GGW3e7-hs=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="text-align:left"><p>Category</p></th><th style="text-align:left"><p>Configuration</p></th><th style="text-align:center"><p>M3</p></th><th style="text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td rowspan="2" style="width:17.0863%"><p>Inset icon</p></td><td><p>No (default)</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Yes</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td rowspan="2" style="width:17.0863%"><p>Orientation</p></td><td><p>Horizontal (default)</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Vertical</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td rowspan="2" style="width:17.0863%"><p>Size</p></td><td><p>XS (default)</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>S, M, L, XL</p></td><td><p>--</p></td><td><p>Available on Android Views (MDC-Android).<br />Available as tokens on other platforms.*<br /></p></td></tr><tr><td><p>Stop indicators</p></td><td><p>No (default), Yes</p></td><td><p>Available as “discrete” slider</p></td><td><p>Available</p></td></tr><tr><td><p>Value Indicator</p></td><td><p>No (default), Yes</p></td><td><p>Available</p></td><td><p>Available</p></td></tr></tbody></table></div>

<blockquote>*Configurations only available using tokens don’t have implemented presets in code. To change the size, swap the default size tokens <span class="inline-code">md.comp.slider.<strong>xsmall</strong>.[...]</span> with those of the desired size.</blockquote>

<h2>Tokens &amp; specs</h2><p>Slider tokens are organized into a common token set, and token sets for each size. Switch token sets from the table’s menu. <a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/0045edb815f2325e

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Anatomy</h2>

6 elements of a slider.

<ol class="decimal"><li id="isPasted">Value indicator (optional)</li><li>Stop indicators (optional)</li><li>Active track</li><li>Handle</li><li>Inactive track</li><li>Inset icon (optional)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6a99lg-04-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Tj-xqiQbRv2zhsiRQmk6ZkdhFwQgK6qEZx40m4TMy8W7B8ulEiPsHemm1KcY6ejMeYjYFnJF2GHGnWzVq-v8yDHTRon1k-oZGg9VuIa2C4Q=s2048

<h2 id="isPasted">Color</h2>

9 color roles of a slider.

<p>Slider color roles used for light and dark schemes:</p><ol class="decimal"><li id="isPasted">Inverse surface</li><li id="isPasted">Inverse on surface</li><li id="isPasted">Primary</li><li id="isPasted">On primary</li><li id="isPasted">Primary</li><li id="isPasted">Secondary container</li><li id="isPasted">On secondary container</li><li id="isPasted">On secondary container</li><li id="isPasted">On primary</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6aa21o-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/CV3PfOlQdK3A_3O8RLyu_r-GjqW7NK-qgzQmKuo5M5tWBmI6eDGdNfq7p8bTvQbP1jYCpk8WaRktgSsCrKD9Lp1vbaeCtE2einRTw6e1J7dbGA=s2048

<h2>States</h2>

5 states of sliders in light and dark schemes.

<ol><li>Enabled</li><li id="isPasted">Disabled</li><li>Hovered</li><li>Focused</li><li>Pressed</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6aaode-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/PgYCQrkBSJUOlzQMXu0BmIe16Fho4X9NdvdYYSOtE1tIl0aucZejoImkNIfdTpbPity3lWJxxg2WSoilrjogEOWTcVhxyGN0aYZl0sRWQuMpJA=s2048

<h2>Measurements</h2>

Common slider padding and size measurements.

<p>Padding and size measurements for common sliders</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6abaty-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/WLMws1Xen6XFUKvbCJS2NM4jwTMVmQxFlh8QhTslZGI-TR2eoFPXUp-ck8i0FhO_U2cy0cW5qnNP6Qkrsu1kJ-eztl1sJ_o5lHzXSUtr4FAMPw=s2048

Slider padding and size measurements at each size configuration, XS to XL.

<p>Padding and size measurements for XS, S, M, L, and XL sliders</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fma6absmo-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/FH3TsHZ1NpVLh--XKKb2ygB9rd0bgZ6ig1vGxWhQu5HOFVbk_8CXIxMAVdJnPxKj3fojh8jFh6qDqm41tD0R3YRaK0luWcktoURO5RZfBsuO=s2044

<div class="table-wrapper"><table style="margin-right:calc(0%);width:100%"><thead><tr><th style="width:19.8591%;text-align:center">Attribute</th><th style="width:13.5131%;text-align:center">XS</th><th style="width:16.9416%;text-align:center">S</th><th style="width:18.9776%;text-align:center">M<br /></th><th style="width:15.4648%;text-align:center">L</th><th style="width:15.9875%;text-align:center">XL</th></tr></thead><tbody><tr><th style="width:19.8591%">Track height</th><td>16dp</td><td>24dp</td><td>40dp</td><td>56dp</td><td>96dp</td></tr><tr><th style="width:19.8591%">Label container height<br /></th><td colspan="5">44dp</td></tr><tr><th style="width:19.8591%">Label container width</th><td colspan="5">48dp</td></tr><tr><th style="width:19.8591%">Handle height<br /></th><td>44dp</td><td>44dp</td><td>52dp</td><td>68dp</td><td>108dp</td></tr><tr><th style="width:19.8591%">Handle width<br /></th><td colspan="5">4dp</td></tr><tr><th style="width:19.8591%">Track shape</th><td>8dp</td><td>8dp</td><td>12dp</td><td>16dp</td><td>28dp</td></tr><tr><th style="width:19.8591%">Inset icon size</th><td>--</td><td>--</td><td>24dp</td><td>24dp</td><td>32dp</td></tr></tbody></table></div>

## Guidelines

Photo editor with sliders labeled pop, sharpen, and denoise being adjusted.

<p>Sliders can adjust values in real time, such as image attributes</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7m4gc9t-slider%20motion.mp4?alt=media

<h2>Usage</h2>

<p>Sliders are used to select values along a track. They’re ideal for adjusting settings such as volume and brightness, or changing the intensity of image filters.<br /><span style="white-space:pre-wrap"><br />Sliders can use icons or labels to represent a numeric or relative scale. </span></p>

Sound settings screen with continuous sliders labeled call volume and alarm volume.

<p>Use sliders to pick a value from a range, like volume loudness</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmabg8tbj-02.png?alt=media

<p>Changes made with sliders must take effect immediately, so people can understand the effects of their selection as they're moving the slider.</p>

The brightness slider changes the screen’s brightness in real time.

<p>Selection changes are immediate</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7llbz94-GM3_Expressive_Slider_guideline_3b_IA_V02%20.mp4?alt=media

<p>There are three different variants of sliders: <strong>standard</strong>, <strong>centered</strong>, and <strong>range:</strong><br /><br />Standard sliders select one value from a range of values. Use this when the slider should start from zero or the beginning of a sequence.</p>

Horizontal standard slider with an end stop indicator.

<p>Horizontal standard slider </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lk01w5-04.png?alt=media

Vertical standard slider  with an end stop indicator.

<p>Vertical standard slider </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lk1j0t-05.png?alt=media

<p>Centered sliders select a value from a positive and negative value range. Use this when zero, or the default value, is in the middle of the range.</p>

Horizontal centered slider with a negative value and visible stop indicators at each end.

<p>Horizontal centered slider</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lk3lyv-06.png?alt=media

Vertical centered slider with a negative value and visible stop indicators at each end.

<p>Vertical centered slider</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lk4tsn-07.png?alt=media

<p>Range sliders select two values on one slider to create a range. Use this when defining a minimum and maximum value.<br /><br />Avoid using range sliders vertically, as this can add too much cognitive load. People are used to most sliders being horizontal.</p>

Horizontal range selection slider with 2 values selected, and a stop indicator at each end.

<p>Horizontal range slider</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lk6981-08.png?alt=media

Vertical range slider with 2 values selected, and a stop indicator at each end.

<p>Because of the additional cognitive load of a range slider, avoid using it in vertical orientation.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7ln45vm-09%20-%20don't.png?alt=media

<h2><span style="white-space:pre-wrap">Anatomy</span></h2>

6 elements of a slider.

<ol><li>Value indicator (optional)</li><li>Stop indicators (optional)</li><li>Active track</li><li>Handle</li><li>Inactive track</li><li>Inset icon (optional)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7m553sk-04-1.png?alt=media

<h3>Track</h3><p id="isPasted">The track shows the full range of values that can be selected on the slider. It has two sections: active and inactive.</p><ul><li>The <strong>active </strong>section of the track is from the minimum value to the handle. For range sliders, the active track is between the two handles.</li><li>The <strong>inactive</strong> section of the track is from the handle to the maximum value, or outside the two handles of a range slider.</li></ul><p>For left-to-right (LTR) languages, the values increase from left to right. For right-to-left (RTL) languages, this is reversed.</p>

Sliders for font size and display size with stop indicators along the track.

<p>The track on a slider shows the available range</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lk9dsb-11.png?alt=media

<h3>Handle</h3><p id="isPasted">The handle can be moved along the track to choose a value.<br /><br />When sliders have two handles, the handles choose the minimum and maximum values in a range.<br /><br />The handle changes shape to indicate when it’s pressed.</p>

The handle is a vertical line on the current value of the slider. It shrinks in width when selected.

<p>A handle changes shape when it's being pressed or dragged</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lkaurk-12.png?alt=media

2 unselected handles on a slider with range selection.

<p>Two handles are used for sliders with range selection </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lkbdhm-13.png?alt=media

<h2 id="isPasted">Configurations</h2>

<h3>Value</h3><p id="isPasted">The value displays the specific value that corresponds with the handle’s placement. <br /><br />A value appears when interacting with the corresponding handle. For range sliders, only one value should be shown at a time.<br /><br />If the value is shown elsewhere, the indicator is not required.</p>

A value of 50 is above a slider handle in the middle of the track.

<p>A value can appear while the handle is being pressed or dragged</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx1s2vu5-13.png?alt=media

A value of 75 is above the pressed range slider handle. The unselected slider doesn’t show the value.

<p><span style="white-space:pre-wrap">For range sliders, the value only appears on one handle at a time</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lkclo7-14.png?alt=media

<p>Instead of showing the built-in value label, a separate text input field can be added outside of the slider. If this is added, the slider and value in this text field should automatically update to match each other.</p><p>Make sure people can tab to the text field directly after the slider.</p>

Navigating to an adjacent text label, changing the value to 100 using arrow keys. The slider auto-updates based on input value.

<p>Use <strong>Tab</strong> to navigate to values that are shown outside the slider, like a text input field</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx2tgm3i-GM3-Components-Sliders-3-v01.mp4?alt=media

<h3>Stop indicators</h3><p id="isPasted">Stop indicators show which predetermined values can be chosen on the slider. The slider handle snaps to the closest stop. <br /><br />Avoid having too many stop indicators on a slider, because it can become visually crowded and difficult to adjust the value.<br /><br />All sliders have stops at the end of the inactive track to ensure at least a 3:1 contrast with the background. If the inactive track has this level of contrast already, the end stops can be removed.</p>

Stop indicators are equally spaced out on a slider.

<p>Stop indicators show each available value on a slider</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx1s1ozg-10.png?alt=media

<p>Icons or text can be added outside the slider to indicate the range of values and make the slider more accessible. This can be used instead of a stop indicator.</p>

Plus and minus icons on each end of the slider.

<p>Plus and minus icons, or text, can be added to the left and right of the slider</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lkfou6-17.png?alt=media

<h3>Orientation</h3><p>Sliders can be oriented either horizontally or vertically, depending on what is best for your use case.</p>

Horizontal slider.

<p>Standard slider in horizontal orientation</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lkhuu1-18.png?alt=media

Vertical slider. Zero is at the bottom.

<p>Standard slider in vertical orientation</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lkj1b8-19.png?alt=media

<h3>Inset icon</h3><p>Standard sliders that are M, L, or XL can include an icon within the track. This icon should illustrate what the slider controls. Avoid adding inset icons to XS or S sliders.<br /><br />When there’s not enough space for the icon on the active track, like at a low value, the icon moves to the inactive track.<br /><br />Consider swapping which icon is displayed at zero, like a volume icon becoming a mute icon.</p>

Inset icon on the active track when the handle is at 50%, and on the inactive track when the handle is at 0.

<p>Inset icons change placement based on the handle</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lkmte8-20.png?alt=media

An inset icon on an XS slider. The icon bounds are cut off by the slider container.

<p>Don’t use an inset icon with sliders that have track thicknesses under 40dp</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lni1k4-21%20-%20don't.png?alt=media

<p>Don’t use inset icons on centered or range sliders. It makes it unclear where the start of the slider is.</p>

Centered slider with an inset icon on one end, and a stop indicator on the other.


<p>Don’t use an inset icon on a centered slider</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lnlfie-22%20-%20don't.png?alt=media

Range slider with an inset icon on one end, and a stop indicator on the other.


<p>Don’t use an inset icon on a range slider</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lnor7e-23%20-%20don't.png?alt=media

<h3>Size</h3><p>Sliders come in different sizes: XS, S, M, L, and XL. Use larger sizes to increase the targets and provide a larger visual emphasis.<br /><br />The active and inactive tracks should always be the same size.</p>

5 sizes of sliders.

<ol><li id="isPasted">XS: 16dp</li><li>S: 24dp</li><li>M: 40dp</li><li>L: 56dp</li><li>XL: 96dp</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lkolpk-24.png?alt=media

<p>XL sliders should be reserved for hero moments, where the slider itself is the most important element on the page.</p>

An XL slider used to adjust living room temperature on mobile. No other controls are on screen.

<p>XL sliders should be the focus of the page</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm7lkr4j4-25.png?alt=media

<h2>Behaviors</h2>

<h3>Select &amp; drag</h3><p>Select a value by dragging the handle.</p>

Slider handle moves smoothly. The value increases and decreases by single digits.

<p><strong>Standard slider</strong>: The handle drags smoothly</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx2tddmn-GM3-Components-Sliders-4-1-v01.mp4?alt=media

Slider handle snaps to the nearest multiple of 10 when moved.

<p><strong>Slider with stop indicators:</strong> The handle snaps to the closest stop indicator while dragged</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx2tdv5o-GM3-Components-Sliders-4-2-v01.mp4?alt=media

<h3><span style="white-space:pre-wrap">Select jump</span></h3><p><span style="white-space:pre-wrap" id="isPasted">Select a value by selecting part of the track. </span></p>

Slider handle moves smoothly to selected value of the slider.

<p><strong id="isPasted">Standard</strong><strong> slider</strong>: The handle moves to the selected location</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx2tec5h-GM3-Components-Sliders-5-1-v01.mp4?alt=media

Slider handle moves smoothly to the closest stop indicator value.

<p><strong id="isPasted">Slider with stop indicators:</strong> The handle moves to the closest stop indicator</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx2tep43-GM3-Components-Sliders-5-2-v01.mp4?alt=media

<h3>Select &amp; arrow</h3><p>Select a value using the keyboard.<br /><br /><strong>Tab:</strong> Focus lands on handle <br /><br /><strong>Arrows: </strong>Selected value increases or decreases by one value or stop indicator<br /><br /><strong>Space &amp; arrows:</strong> Selected value increases or decreases by a larger interval or stop indicator</p>

Tab selects the slider, and arrow keys move the value by 1.

<p><strong id="isPasted">Standard</strong><strong> slider</strong>: The handle moves one value</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx2tf2t6-GM3-Components-Sliders-6-1-v01.mp4?alt=media

Tab selects the slider, and arrow keys move the value by 10.

<p><strong id="isPasted">Slider with stop indicators: </strong>The handle moves to the next stop indicator</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx2tffc3-GM3-Components-Sliders-6-2-v01.mp4?alt=media

## Accessibility

<h2>Use cases</h2>

<p id="isPasted"><span style="white-space:pre-wrap">People should be able to do the following using assistive technology</span><span style="white-space:pre-wrap">:</span></p><ul><li>Navigate to a slider </li><li>Select a range by controlling a handle along a track</li><li>Get appropriate feedback based on input type</li></ul>

<h2>Interaction &amp; style</h2>

<p id="isPasted">The slider handle shrinks in width and the value appears to provide a visual cue to the user that the handle is being pressed.</p><p><strong>Touch</strong></p><p>When tapped or dragged, the handle width shrinks to provide interaction feedback, and the value appears.</p><p><strong>Cursor</strong></p><p>When hovered, the cursor changes. When clicked and dragged, the handle width shrinks, and the value appears.</p>

Dragging a slider using a mouse cursor and by touch. Handle width shrinks when dragged.

<p>The slider handle changes width during interaction</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx2tjccg-GM3-Components-accessibility-Sliders-1-v01_1.mp4?alt=media

<h3 id="isPasted">Focus and navigation</h3><p>Initial focus lands directly on the handle, since it’s the primary interactive element of the slider.</p><p>The slider value can then be adjusted using the arrow keys or other keyboard navigation options.</p>

Using keyboard navigation on a slider. Tab to the handle, and use arrow keys to change the value.

<p>Use arrow keys to change the slider value</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx2tk5qd-GM3-Components-accessibility-Sliders-2-v01.mp4?alt=media

<h2>Color contrast</h2>

<p id="isPasted">Use visual anchors so the end of the slider’s inactive track has at least 3:1 contrast with the background. The stop indicator makes the end easily visible on most backgrounds.</p>

The inactive track has contrast below 3:1 with the background. The stop indicator is above 3:1. Slider is accessible.

<p>A stop indicator on the inactive track makes it easier to identify the end of the slider on a low-contrast background</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx1s6sg3-3.png?alt=media

<p>Alternatively, icons or other elements that have a 3:1 contrast with the background can be used to indicate the ends of the slider’s inactive track.</p>

The inactive track has contrast ratio below 3:1 with the background. The icon is above 3:1. The slider is accessible.

<p>Icons make it easier to identify the ends of the slider on a low-contrast background</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx1s73wl-4.png?alt=media

<h2>Keyboard navigation</h2>

<div class="table-wrapper"><table style="width:100%" class="fr-table-selection-hover"><thead><tr><th style="width:25.6643%">Keys<br /></th><th style="width:74.3357%">Actions<br /></th></tr></thead><tbody><tr><th style="width:25.6643%">Tab<br /></th><td>Moves focus to the slider handle</td></tr><tr><th style="width:25.6643%">Arrows<br /></th><td>Increase and decrease the value by one value or one stop indicator</td></tr><tr><th style="width:25.6643%">Space &amp; Arrows<br /></th><td>Increase and decrease the value by one interval or one stop indicator</td></tr><tr><th style="width:25.6643%">Home or End<br /></th><td>Set the slider to the first and last values on the slider</td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<p id="isPasted">The accessibility label for a slider is typically the same as the slider's adjacent text label. It should have the <strong>slider</strong> role.</p>

Annotated aria tags of a slider.

<p>A slider’s accessibility label should match the adjacent UI text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0o6wp1l-5.png?alt=media

<p>If the UI text is correctly linked to the slider, assistive tech (such as a screenreader) will read the UI text followed by the component’s role.</p>

Annotated aria tags of a slider with stepper icons.

<p>Icon buttons placed outside the slider should have the button role</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm3601h6w-6.png?alt=media
