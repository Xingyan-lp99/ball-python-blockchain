# Progress indicators

Source: https://m3.material.io/components/progress-indicators
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/9a92bb46-ccc8-4752-a144-b770d47fe1dd.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Two variants: linear and circular</p></li><li><p>Use the same configuration for all instances of a process (like loading)</p></li><li><p>They capture attention through motion</p></li><li><p>Option to apply a wave to the active track for use cases that would benefit from increased expressiveness</p></li></ul>

8 progress indicators configured to show different thickness and shape.

<p>Linear and circular progress indicators have visual configurations for shape and thickness</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmleotj2q-01.png?alt=media

<h2 id="isPasted">Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/2fd9de395ed49bc3

libraryModuleType: STATUS_TABLE

<h2>M3 Expressive update</h2>

<p><strong>Aug 2024</strong></p><p>The progress indicators have configurations for height and wavy shape. Choose the visual style that best fits your product. <a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank">More on M3 Expressive</a></p>

<ul><li>Track height: Configurable</li><li>Shape: Wavy</li></ul>

Progress indicators used when loading a page and for processing a payment.

<p>Progress indicators have a new rounded, colorful style, and more configurations to choose from, including a wavy shape and variable track height</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qvxgu6-Progress-Indicator-Overview.mp4?alt=media

<h2>Previous updates</h2>

<p id="isPasted"><strong>Dec 2023: Non-text contrast (NTC)</strong></p><ul><li>Anatomy: Added an end stop indicator to improve accessibility</li><li>Contrast: Higher contrast between track and active indicator to enhance the perception of progress</li><li>Motion: New motion behavior</li><li>Shape: Rounded corners</li></ul>

GM3 linear and circular progress indicators

<p>Progress indicators have a new rounded, colorful style</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmleov4bo-03.png?alt=media

<h2>Differences from M2</h2>

<p id="isPasted"><strong>July 2022: Added to Material 3</strong></p><ul><li><strong>Color:</strong> New color mappings and compatibility with dynamic color</li></ul>

M2 linear and circular progress indicators.

<p>M2: Progress indicators have a boxier, neutral style</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c2if7i-04.png?alt=media

M3 linear and circular progress indicators.

<p>M3: Progress indicators are compatible with dynamic color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0c2jf26-05.png?alt=media

## Specs

<h2>Variants</h2>

2 variant of progress indicators.

<ol class="decimal"><li id="isPasted">Linear progress indicator</li><li>Circular progress indicator</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmloz0082-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/fLmSSW0vCAz72TSdfqeo9FQY5YlgLT7ktKAZkxs-FEetsANoory1UPDxRd3-jESQSkUeq6xuwEtp1NcR52Mih2QQQiprYecoJ-XI0SDBaL1T=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Variant</p></th><th style="text-align:center"><p>M3</p></th><th style="text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td><p>Linear progress indicator</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Circular progress indicator</p></td><td><p>Available</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Configurations</h2>

4 configurations of the linear determinate progress indicator.

<ol class="decimal"><li id="isPasted">Behavior: Determinate and indeterminate</li><li>Thickness: Default (4dp) and variable</li><li>Shape: Flat and wavy</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmloz0zuq-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Cf6AdPUEQffL-k5D1on9M3H1oyAGh20uJyfa7sbOwip6oRPvmqv7u2MSLKrH70PpyL0bCJdy2fGRNg_13JG9imoQdIMm8935YUMQXQxATKeocA=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:14.8398%"><p>Category</p></th><th style="width:35.1153%"><p>Configuration</p></th><th style="text-align:center"><p>M3</p></th><th style="text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td><p>Behavior</p></td><td><p>Determinate (default), Indeterminate</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td rowspan="2" style="width:14.8398%;vertical-align:top"><p>Track thickness</p></td><td><p>Fixed (4dp) </p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Configurable</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td rowspan="2" style="width:14.8398%;vertical-align:top"><p>Shape</p></td><td><p>Flat (default)</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Wavy</p></td><td><p>--</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Tokens &amp; specs</h2><p>Browse the component elements, attributes, tokens, and their values. <a href="/m3/pages/progress-indicators/specs#c6f484b0-2bc6-4d37-bd75-f859a35a3594" target="_self">View baseline tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/6f51f7ab7775a392

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Progress Indicator - Common', 'Progress indicator - Linear', 'Progress indicator - Circular'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['Progress Indicator', 'Progress indicator - Linear', 'Progress indicator - Circular', '[Deprecated] Progress indicator - Circular', '[Deprecated] Progress indicator - Linear'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Anatomy</h2>

3 elements of a progress indicator.

<ol class="decimal"><li id="isPasted">Active indicator</li><li>Track</li><li>Stop indicator</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmloz1qik-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/d1mWcS4gytQf_XcgwvUqsNTf47P5BT9PUo-Ivi-7Ld1_Vc_HAtLGPARxwbqUcN7gdc-JH4iXM0nRH1374g23CnABP7i8eP9CnGq6UNpAnJ4=s2048

<h2>Color</h2>

2 color roles of a linear progress indicator in light and dark themes: the active indicator and stop indicator are primary and the track is secondary container.

<p>Progress indicator color roles used for light and dark schemes:</p><ol class="decimal"><li><p>Primary</p></li><li><p>Secondary container</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmloz2lzv-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/CrzKce-9x2GrD2SOdyYCmDhdK37XcZoiMv9mT6N0NjUybL1GwXLN52_LbXb1AKfzmLUna1jMew5x0skKpMBEHrBJ82d-tJRr5DvoaUeR_J4=s2048

<h2>Measurements</h2>

<p>Wavy indicators use <strong>amplitude</strong> and <strong>wavelength</strong> to determine the shape of the wave. The height is the overall container height.</p>

Definitions of wave measurements for height and amplitude.

<p><strong>Amplitude</strong> measures from the center of the resting position to the center of the peak</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmloz3iks-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Aii3LLGqfr5jLHSdMLKx4rMUceBixyyXu77IqvYcUoMGwV8MxqqZgcB0XU6nx7GpVeU7_sqdq6ScJE4eic6v4dP1Abaq4TtF3MSZNxB2HifI=s1004

Definitions of wave measurements for wavelength.

<p><strong>Wavelength</strong> measures the distance between two adjacent peaks</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmloz3ss3-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/hYbEOpy3GfIuFxLUfMLU_r3VijC9KNldOlFhXM3oEYputn_p6YvzArLiC3dZWgzuuzVOfrsX2LUhP6BQP57NF_RD265PRui1VtLzxURvCDzMOg=s1004

Linear progress indicator measurements.

<p>Size measurements for linear progress indicators. The thicker variants are provided as sample measurement for makers to adjust the default version based on their use cases. </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmloz4e98-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/M-64WwKIqgmV6lWqTh7Ar7vJuUsvjqLTnOJcMLrFPbW4nxRmYITD4GbXXEGCjwK2eJLUBGlfD1rtb86saREi68enxN3Galq9ZUPa-pgFIm-QlA=s2048

Circular progress indicator measurements.

<p>Size measurements for circular progress indicators. The thicker variants are provided as sample measurement for makers to adjust the default version based on their use cases. </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmloz4zbx-08-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/8oX70XRFeRqxFH1vBkx8z4hy6nKrvShQvQsQuR8emIWoXRKU8OWnK5pdFx-Q8ZwF0d4w8qDLi5NqPYAqxekWoHy9ytjz-lz7Leo9TFNlWU8s=s2048

4dp padding on the left and right of the linear progress indicator.

<p>The linear progress indicator is inset from the edge of the screen by 4dp</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmloz5p1v-09-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/6_sdBcuvKe2j9XDUC70bzaxi8QsZW1507V6pQ9ZQstst3B_Y8w26_5Yuz504uIxL_GcrMfNhJFvNiQotKPPEPlRgCczoR5ys0e8wM7Lv6L19=s2048

<h2>Baseline tokens</h2>

<p>The circular and linear progress indicator had separate token sets. These are no longer recommended.</p>

resourceName: designSystems/20543ce18892f7d9/components/6f51f7ab7775a392

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['[Deprecated] Progress indicator - Circular', '[Deprecated] Progress indicator - Linear'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

## Guidelines

Primary colored horizontal line fills a contrasting track from left to right and reaches the end when the app is loaded.

<p>Progress indicators communicate the status of an ongoing process</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm37ri5xn-Progress-Indicator-A_1.mp4?alt=media

<h2 id="isPasted"><span style="white-space:pre-wrap">Usage</span></h2>

<p id="isPasted">Use progress indicators to show the status of ongoing processes, such as loading an app, submitting a form, or saving updates.</p><p>When multiple items are loading, use a single progress indicator to show progress for the group. Don’t add progress indicators to every activity.</p>

One progress indicator showing the loading progress for a page of podcasts.

<p>Indicate overall progress of a group of items</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0h3mssg-Progress-Indicator-B.mp4?alt=media

Two progress indicators showing the loading progress of two podcasts.

<p>Don’t show the progress of each activity in a group</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0h3n5x5-Progress-Indicator-C.mp4?alt=media

<p>Choose a <app-froala-tooltip-element description="Loading indicators show the progress of a process with a short wait time." link-label="More on loading indicators" link-url="/m3/pages/loading-indicator/overview" should-open-link-in-new-tab="true">loading</app-froala-tooltip-element> or <app-froala-tooltip-element description="Progress indicators show the status of a process in real time." link-label="More on progress indicators" link-url="/m3/pages/progress-indicators/overview" should-open-link-in-new-tab="true">progress indicator</app-froala-tooltip-element> that corresponds to the expected wait time and kind of process. </p><p>If the wait is very long, consider allowing people to navigate away from the page while the process finishes up. </p>

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="width:50%"><strong>Expected wait time</strong><br /></th><th style="width:50%"><strong>Recommendation</strong></th></tr></thead><tbody><tr><td>Instant (under 200ms)</td><td>No indicator</td></tr><tr><td>Short (between 200ms and 5s)</td><td>Loading indicator</td></tr><tr><td>Long (Over 5s)</td><td>Progress indicator</td></tr></tbody></table></div>

Screen without latency without progress indicator.

<p><strong>Instant (under 200ms):</strong> Display the content immediately</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0h3nu79-Progress_Indicator-C.mp4?alt=media

Screen with slight lag with loading indicator.

<p><strong>Short (between 200ms and 5s):</strong> Use a loading indicator</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0h3o5um-Progress_Indicator-D.mp4?alt=media

Screen with long lag and progress indicator.

<p><strong>Long (over 5s): </strong>Use a progress indicator</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm37rcxcs-Loading-Indicator-E_2.mp4?alt=media

<p>There are two variants of progress indicators:</p><ol class="decimal"><li><p>Linear</p></li><li><p>Circular</p></li></ol><p><strong>Linear</strong> indicators are best when placed on the edge of a container.</p><p><strong>Circular</strong> indicators are best when centered in an element.</p><p>A process should be represented by the same variant of progress indicator throughout the product. For example, if refreshing uses a circular indicator in one place, it should use circular indicators everywhere.</p>

1. A primary colored horizontal line fills a contrasting track from left to right. 2. A circle appears from 0 to 360 degrees.

<ol class="decimal"><li id="isPasted">Linear indicator  </li><li>Circular indicator</li></ol><p><br /></p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlep5ivu-07.png?alt=media

<p id="isPasted">Progress indicators behave differently based on the time of progress being tracked:</p><ul><li><strong>Determinate</strong>: Known progress and wait time</li><li><strong>Indeterminate</strong>: Unknown progress and wait time</li></ul><p>When using a <strong>determinate</strong> indicator, the indicator must accurately represent the progress of what it's measuring. </p><p>Use <strong>indeterminate</strong> indicators to show that a process is happening, but the wait time is unknown.</p>

Linear and circular progress indicators show both determinate and indeterminate progress.

<ol class="decimal"><li id="isPasted">Determinate progress indicators fill from 0% to 100%</li><li>Indeterminate progress indicators move along a fixed track, growing and shrinking in size</li></ol>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qw0hzu-Progress-Indicator-G.mp4?alt=media

<p>As more information about a process becomes available, a progress indicator should change from <strong>indeterminate</strong> to <strong>determinate</strong>.</p>

On a track, a contrasting primary-colored horizontal line grows and shrinks, then fills it from left to right as app loads.

<p>A linear progress indicator changes from indeterminate to determinate while loading a screen</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qw2h3o-Progress-Indicator-K.mp4?alt=media

<h2 id="isPasted">Anatomy</h2>

1. The track is a horizontal line. 2. A primary colored line over the contrasting colored track is the progress indicator.

<ol class="decimal"><li id="isPasted">Active indicator</li><li>Track</li><li>Stop indicator</li></ol>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qw333o-Progress-Indicator-H.mp4?alt=media

<h3>Active indicator</h3><p id="isPasted">The active indicator shows the progress that has been made so far. </p><p>In indeterminate processes, it grows and shrinks along the track repeatedly.</p>

A primary colored horizontal line fills a contrasting line from left to right.  

<p>Linear indicators animate from the leading to the trailing edge along the track. Circular indicators animate from the top of the track, clockwise by default.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qw3uto-Progress-Indicator-I.mp4?alt=media

<p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">The active indicator appears as soon as progress begins. At low percentages where space is limited, this should appear as a dot to help people understand that there’s progress underway.</span></p>

A linear and circular progress indicator at 1% progress, where the active indicator has only just appeared.

<p><span style="white-space:pre-wrap">When progress first begins, the active indicator appears as a dot</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlep6b3j-12.png?alt=media

<p id="isPasted">The active indicator has two shape options: <strong>flat</strong> and <strong>wavy</strong>. Use the shape that best fits the product’s tone.</p><p>The wavy shape can make longer processes feel less static and is best used when a more expressive style is appropriate.</p><p>When using the wavy shape, the overall height of the component changes. At very small sizes, the wavy shape may not be as visible.</p>

Examples of flat and wavy active indicator.

<p id="isPasted">Wavy linear indicators increase the height of the overall container</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qw4l6g-Progress-Indicator-J.mp4?alt=media

<h3>Stop indicator</h3><p id="isPasted">The stop indicator is a 4dp circle that marks the end of a linear determinate progress indicator to meet Material's accessibility standards.</p><p>It's not used for indeterminate or circular progress indicators.</p><p>The stop indicator is required if the track has a contrast below 3:1 with its container or the surface behind the container.</p>

A primary colored horizontal  line fills a contrasting line from left to right.

<p id="isPasted">Use a stop indicator when placing the progress indicator inside a container with low contrast</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlep7pxt-16.png?alt=media

An invisible circular track fills with color from 0 to 360 degrees.

<p id="isPasted">Only remove the end stop indicator if there's a visual contrast of at least 3:1 with surrounding surfaces</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlep87pn-17.png?alt=media

<h2>Placement</h2>

<p id="isPasted">Place a linear progress indicator along the edge of a container that’s loading. If the container changes shape, place it on the edge that animates. It can also be placed in the middle of a container.</p><p>Use a single progress indicator at the top of a page to show progress of the whole group. Don’t add one for every element unless they’re activated independently.</p>

Progress indicator at top of screen, indicating page content is loading.


<p>When at the top of a screen, a progress indicator shows that all of the page content is loading</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qw57zf-Progress-Indicator-L.mp4?alt=media

Progress indicator on a card, indicating that the card's content is loading.

<p>When attached to a card, a progress indicator shows that just the card content is loading</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qw6vq0-Progress-Indicator-M.mp4?alt=media

Linear indicator shows the loading progress of a selected news article in a list.

<p>A progress indicator on the expanding edge of a card shows that the edge may expand to show the loaded content</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm37rivp2-Progress-Indicator-N_1.mp4?alt=media

<p id="isPasted">Circular progress indicators should be centered directly on the container or page that's loading, such as a button or card.</p><p>When loading more items on a page, place the circular progress indicator in the empty space where the new content will appear, not overlapping existing content.</p><p>However, if the content does not take long to load, consider using a loading indicator instead.</p>

As content loads, the screen is blank except for a circular progress indicator.

<p>A circular progress indicator can show that the page is loading</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qw7zgb-Progress-Indicator-O.mp4?alt=media

As container content loads, the container is blank except for a circular progress indicator.

<p>A circular progress indicator can show where new items will appear on a page. A loading indicator also works well in this space.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qw8fla-Progress-Indicator-P.mp4?alt=media

<h3 id="isPasted">Progress indicators in buttons</h3><p id="isPasted">A circular indicator can be placed in a button to show that the button’s action is currently in progress.</p><p>In very small buttons, use the flat shape since the wavy shape is not as visible at that size.</p><p>To ensure a minimum 3:1 contrast ratio, change the active indicator color to be the same color as the button’s icon or label text, and remove the track.</p>

Determinate circular indicator active for 2 seconds after download button is selected, reflecting download progress.

<p>Use circular indicators for short, indeterminate activities under 5 seconds</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qwbhkm-Progress-Indicator-Q.mp4?alt=media

Shows idea of indeterminate circular indicators active on multiple buttons as  cluttered and confusing.

<p>Avoid applying progress indicators to every button in a list</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qwbvqt-Progress-Indicator-R.mp4?alt=media

<h2>Responsive layout</h2>

<h3>Right-to-left languages</h3><p id="isPasted">Linear progress indicators should be mirrored horizontally for products using right-to-left (RTL) languages. </p><p>Circular progress indicators don’t need to be mirrored.</p>

Mirrored right-to-left progress indicator.

<p>Linear progress indicators can flow from right to left in right-to-left (RTL) languages</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlep96rs-25.png?alt=media

<h3>Large screens</h3><p>Circular progress indicators have flexible sizes. They can range from 24dp to 240dp, depending on the placement and the breakpoint. Avoid exceeding the minimum and maximum sizes.</p><p>Reserve very large progress indicators for large and extra-large windows, such as desktop.</p>

Circular progress indicators can range in size from 24dps to 240dps.

<p>The waveform should scale with the size so the proportions look the same across sizes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlep9qg1-26.png?alt=media

<p id="isPasted">Linear progress indicators dynamically adjust to fit the width of the window or element they’re placed within, such as a card. They shouldn’t be used in any elements smaller than 40dp.</p><p>The padding on each end should be 4dp minimum, but can be modified.</p>

Linear progress indicators can dynamically adjust to any width.

<p>The linear progress indicator should always span the width of the UI element it’s placed within</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlepa8w9-27.png?alt=media

## Accessibility

<h2>Use cases</h2>

<p id="isPasted">People should be able to do the following using the assistive technology:</p><ul><li>Navigate to the progress indicator</li><li>Understand what progress the indicator is communicating</li></ul>

<h2><span style="white-space:pre-wrap">Interaction &amp; style</span></h2>

<p>The active indicator, which displays progress, provides visual contrast of at least 3:1 against most background colors.</p>

Dark line of progress indicator stands out against the lighter colored track.

<p id="isPasted">The progress indicator and stop indicator provide visual contrast of at least 3:1 against most background colors</p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlepc1r2-01.png?alt=media

<p>When integrated into another component, such as a button, make sure that the active indicator provides visual contrast of at least 3:1 against the other component. </p><p>For the active indicator, use the same color as the label text or icon. The track should be removed.</p>

Circular indicator on button passes 3 to 1 contrast test.

<p>Ensure the indicator’s color provides at least 3:1 contrast against the surface it's on</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlepcmau-02.png?alt=media

Circular indicator on button fails 3 to 1 contrast test.

<p>Avoid using a color below 3:1 contrast</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlepd6dk-03.png?alt=media

<p id="isPasted">For linear progress indicators, the stop indicator is required if the track has a contrast below 3:1 with its container or the surface behind the container.</p><p>Essentially, the end of the track must be easy to identify.</p>

Bright container holding the progress bar is on a dark surface, passing the 3:1 color contrast.

<p>Only remove the stop indicator when the linear progress indicator has at least a 3:1 color contrast with surrounding containers and surfaces</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlepdozy-04.png?alt=media

Bright container holding progress indicator is on a bright surface, failing the 3:1 color contrast.

<p>Avoid removing the stop indicator if any adjacent containers or surfaces are below the 3:1 color contrast</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlepe18t-05.png?alt=media

<h2>Labeling elements</h2>

<p>Since the progress indicator is a visual cue, it needs an accessibility label to describe the kind and amount of progress made.</p><p>Use the <strong>progress bar </strong>accessibility role, and write an accessibility label that describes the purpose of the progress indicator. The label should include the process, such as "loading,” and the affected content, such as a page, article, or episode. For example: "Loading news article" or "Refreshing page."</p>

Determinate linear progress indicator has an accessibility label of “loading news article” and role of “progressbar”.

<p>Progress indicator labels should explain which items are loading</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlepereg-06.png?alt=media

Indeterminate linear progress indicator has an accessibility label of “loading my episodes” and role of “progressbar.”

<p>A label on an intedeterminate progress indicator on a screen which is loading a set of podcast episodes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlepf1vr-07.png?alt=media
