# Easing and duration

Source: https://m3.material.io/styles/motion/easing-and-duration
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/1d658c3f-ba19-48be-9b71-872c72c7166e.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Easing and duration create responsive and expressive motion

## Applying easing and duration

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">In the expressive update, components and motion now use the <a href="/m3/pages/motion-overview/">motion physics system</a>, which uses springs. Products should migrate to the new system. The easing and duration system is still used for transitions and can be used by teams that haven't yet updated to GM3 Expressive, but is no longer maintained.</div></div></div>

<h2 id="isPasted">Suggested easing and duration pairs</h2>

<p>Choosing the right combination of easing and duration can be complicated. As a simple starting point, these are sensible defaults that will work for most transitions.</p>

<div class="table-wrapper"><table id="isPasted" style="width:100%"><tbody><tr><th><strong>Easing</strong> </th><td><strong>Duration</strong></td><td><strong>Transition type</strong></td></tr><tr><th>Emphasized</th><td>500ms</td><td>Begin and end on screen</td></tr><tr><th>Emphasized decelerate</th><td>400ms</td><td>Enter the screen</td></tr><tr><th>Emphasized accelerate</th><td>200ms</td><td>Exit the screen</td></tr><tr><th>Standard</th><td>300ms</td><td>Begin and end on screen</td></tr><tr><th>Standard decelerate</th><td>250ms</td><td>Enter the screen</td></tr><tr><th>Standard accelerate<br /></th><td>200ms</td><td>Exit the screen</td></tr></tbody></table></div>

<h2 id="isPasted">Easing</h2>

<p id="isPasted">In the physical world, objects don’t start or stop instantaneously. Instead, they take time to speed up and slow down. Transitions without easing look stiff and mechanical, while a transition with easing appears more natural.</p>

Motion curve with and without easing.

<ol><li>A transition with easing </li><li>A transition without easing</li></ol>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo5kg57-GM3-Styles-Motion-EasingAndDuration-1-v01.mp4?alt=media

<p id="isPasted">Compared to the utilitarian style of M2, M3 easing is more expressive. Transitions have snappy take offs and very soft landings. </p><p>Durations are slightly longer compared to M2. This gives transitions time to come to a gentle rest without feeling abrupt.</p>

Comparison of M2 and M3 easing curves.

<ol><li>M2 easing and duration </li><li>M3 easing and duration</li></ol>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo5kzx8-GM3-Styles-Motion-EasingAndDuration-2-v01.mp4?alt=media

<h3 id="isPasted">Choosing an easing set</h3>

<p id="isPasted">The <a href="/m3/pages/motion-easing-and-duration/tokens-specs#cbea5c6e-7b0d-47a0-98c3-767080a38d95"><strong>Emphasized easing set</strong></a> is recommended for most transitions to capture the style of M3.</p><p>The <a href="/m3/pages/motion-easing-and-duration/tokens-specs#601d5552-a6e6-4d74-9886-ff8f24b9ec35"><strong>Standard easing set</strong></a> can be used for small utility focused transitions that need to be quick. The Standard set is also a fallback for platforms that don't support Emphasized easing, like iOS and Web.</p>

Expanding card in a note taking app.

<p>Emphasized easing is used for this full screen transition</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo5meuq-04%20-%20Emphasized%20easing.mp4?alt=media

Text field selection in an email app.

<p>Standard easing is used for this Text field transition on Web. The simple style fits the utility of this component.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo5ncde-GM3-Styles-Motion-EasingAndDuration-3-2-v01.mp4?alt=media

<h3 id="isPasted">Choosing an easing type</h3><p>Easing types are chosen based on how a transition moves in relation to the screen.</p>

<h4 id="isPasted">Begin and end on screen</h4><p>These transitions use <strong style="box-sizing:border-box;font-weight:700">Emphasized</strong> easing. It speeds up quickly and then comes to a gentle rest in order to emphasize the end of the transition.</p>

Card expanding in a podcast app.

<p>This transition begins and ends on screen so it uses Emphasized easing</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo5oi36-01%20-%20Start%20and%20End%20on%20screen_1.mp4?alt=media

<h4 id="isPasted">Enter the screen</h4><p style="box-sizing:border-box;font:400 16px / 1.5rem">These transitions use <strong style="box-sizing:border-box;font-weight:700">Emphasized decelerate</strong> easing. It begins at peak velocity then comes to a gentle rest.</p><p style="box-sizing:border-box;font:400 16px / 1.5rem"><br /></p><h4 id="isPasted">Exit the screen permanently</h4><p style="box-sizing:border-box;font:400 16px / 1.5rem">These transitions use <strong style="box-sizing:border-box;font-weight:700">Emphasized accelerate</strong> easing. It begins at rest and ends at peak velocity. By ending at peak velocity, it gives the impression the exiting component cannot be retrieved.</p>

Card rising from bottom of screen, then retreating quickly back to bottom of screen after being exited.

<p>This Bottom sheet enters with Emphasized decelerate and exits permanently with Emphasized accelerate</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo5p261-02%20-%20Enter%20and%20Exit%20the%20screen.mp4?alt=media

<h4 id="isPasted">Exit the screen temporarily</h4><p>These transitions use <strong>Emphasized</strong> easing. By ending at rest just off screen, it gives the impression the exiting component can be retrieved.</p>

Calendar menu is temporarily collapsed to the left.

<p>This drawer enters and exits temporarily with Emphasized easing</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo5po4q-03%20-%20Exit%20Temporarily.mp4?alt=media

<h2 id="isPasted">Duration</h2>

<p>Transitions shouldn’t be jarringly fast or so slow that users feel as though they’re waiting. The right combination of duration and easing produces smooth and responsive transitions.</p>

Clock icon is expanded to smoothly take over the screen.

<p>A transition with a well tuned duration is quick and easy to follow</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo5s08u-05%20-%20Duration%20-%20Do%202.mp4?alt=media

Clock icon is expanded rapidly, in abrupt fashion, to take over the screen.

<p>Avoid transitions with such a short duration they become jarring</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo5r2t6-04%20-%20Duration%20-%20Dont%202.mp4?alt=media

<h3 id="isPasted">Choosing a duration</h3><p>Durations are chosen based on these criteria:</p>

<h4 id="isPasted">Transition size</h4><p style="box-sizing:border-box;font:400 16px / 1.5rem">Transitions that cover small areas of the screen have short durations. Those that traverse large areas have long durations. Scaling duration with the size of a transition area gives a consistent sense of speed.</p>

A series of radio buttons are selected on the Settings screen.

<p>This transition covers a small area with a short 200ms duration</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7qkkx-06%20-%20Small%20area%202.mp4?alt=media

An album is selected that takes over the screen.

<p>This transition covers a large area with a long 500ms duration</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7qvzl-08%20-%20Large%20area%202.mp4?alt=media

<h4 id="isPasted">Enter vs. exit transitions</h4><p style="box-sizing:border-box;font:400 16px / 1.5rem">Transitions that exit, dismiss, or collapse an element use shorter durations. Exit transitions are faster because they require less attention than the user’s next task.</p><p style="box-sizing:border-box;font:400 16px / 1.5rem">Transitions that enter or remain persistent on the screen use longer durations. This helps users focus attention on what's new on screen.</p>

Pop up screen on an email draft has option to delete or cancel.

<ol><li>An Enter transition has a long duration of 500ms </li><li>An Exit transition has a short duration of 200ms</li></ol>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7rtzk-09%20-%20Enter%20Exit.mp4?alt=media

Bottom sheet uses a longer animation duration to enter and a shorter duration to exit the screen.  

<ol><li>An Enter transition has a long duration of 500ms</li><li>An Exit transition has a short duration of 200ms</li></ol>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7sfc7-10%20-%20Enter%20Exit.mp4?alt=media

## Tokens & specs

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">In the expressive update, components and motion now use the <a href="/m3/pages/motion-overview/">motion physics system</a>, which uses springs. Products should migrate to the new system. The easing and duration system is still used for transitions and can be used by teams that haven't yet updated to GM3 Expressive, but is no longer maintained.</div></div></div>

<h2 id="isPasted">Tokens</h2>

<p>Motion easing and duration can be implemented using easing and duration tokens. <a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9

libraryModuleType: TOKEN_TYPE_UNSPECIFIED

moduleConfigurationOverrides: {'tokenSets': ['Motion'], 'contextTags': ['Standard', 'Expressive', 'Compose', 'Web', 'Android']}

<h2 id="isPasted">Easing</h2>

<h3 id="isPasted">Emphasized easing set</h3><p>This set is the most common because it captures the expressive style of M3.</p>

A line graph illustrating an emphasized easing pattern.

<p>Emphasized</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7ug8i-GM3-Styles-Motion-Easing_Duration-Tokens-1-1-v01.mp4?alt=media

A line graph illustrating an emphasized decelerate easing pattern.

<p>Emphasized decelerate</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7uv91-GM3-Styles-Motion-Easing_Duration-Tokens-1-2-v01.mp4?alt=media

A line graph illustrating an emphasized accelerate easing pattern.

<p>Emphasized accelerate</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7v6ah-GM3-Styles-Motion-Easing_Duration-Tokens-1-3-v01.mp4?alt=media

<div class="table-wrapper"><table id="isPasted" style="width:100%"><thead><tr><th style="width:12.7091%">Info/Platform</th><th style="width:40.7284%">Emphasized</th><th>Emphasized decelerate<br /></th><th>Emphasized accelerate<br /></th></tr></thead><tbody><tr><th>Token</th><td>md.sys.motion.easing.emphasized</td><td>md.sys.motion.easing.emphasized.decelerate</td><td>md.sys.motion.easing.emphasized.accelerate</td></tr><tr><th>Android</th><td><a href="https://developer.android.com/reference/android/view/animation/PathInterpolator" rel="noopener noreferrer" target="_blank">pathInterpolator(M 0,0 C 0.05, 0, 0.133333, 0.06, 0.166666, 0.4 C 0.208333, 0.82, 0.25, 1, 1, 1)</a></td><td><a href="https://developer.android.com/reference/android/view/animation/PathInterpolator" rel="noopener noreferrer" target="_blank">PathInterpolator(0.05f, 0.7f, 0.1f, 1f)</a></td><td><a href="https://developer.android.com/reference/android/view/animation/PathInterpolator" rel="noopener noreferrer" target="_blank">PathInterpolator(0.3f, 0f, 0.8f, 0.15f)</a></td></tr><tr><th>CSS</th><td>N/A (Use Standard as a fallback)</td><td><a href="https://www.w3schools.com/cssref/func_cubic-bezier.asp" rel="noopener noreferrer" target="_blank">cubic-bezier(0.05, 0.7, 0.1, 1.0)</a></td><td><a href="https://www.w3schools.com/cssref/func_cubic-bezier.asp" rel="noopener noreferrer" target="_blank">cubic-bezier(0.3, 0.0, 0.8, 0.15)</a></td></tr><tr><th>Flutter</th><td><a href="https://api.flutter.dev/flutter/animation/Curves/easeInOutCubicEmphasized-constant.html" target="_blank" rel="noopener noreferrer">easeInOutCubicEmphasized</a></td><td><a href="https://api.flutter.dev/flutter/animation/Cubic-class.html" rel="noopener noreferrer" target="_blank">Cubic(0.05, 0.7, 0.1, 1.0);</a></td><td><a href="https://api.flutter.dev/flutter/animation/Cubic-class.html" rel="noopener noreferrer" target="_blank">Cubic(0.3, 0.0, 0.8, 0.15);</a></td></tr><tr><th>iOS</th><td>N/A (Use Standard as a fallback)</td><td><a href="https://developer.apple.com/documentation/quartzcore/camediatimingfunction" rel="noopener noreferrer" target="_blank">ControlPoints:0.05f:0.7f:0.1f:1.0f];</a></td><td><a href="https://developer.apple.com/documentation/quartzcore/camediatimingfunction" rel="noopener noreferrer" target="_blank">ControlPoints:0.3f:0.0f:0.8f:0.15f];</a></td></tr><tr><th>After Effects</th><td colspan="3" style="width:87.1867%">Use <a href="https://storage.googleapis.com/material-io-static/resources/material-easing-1.1.3.zxp" id="isPasted" rel="noopener noreferrer" target="_blank">After Effects Easing Panel</a> (download)</td></tr></tbody></table></div>

<h3 id="isPasted">Standard easing set</h3><p>This set is used for simple, small, or utility-focused transitions.</p>

A line graph illustrating a standard easing pattern.

<p>Standard</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7vu4c-GM3-Styles-Motion-Easing_Duration-Tokens-2-1-v01.mp4?alt=media

A line graph illustrating a standard decelerate easing pattern.

<p>Standard decelerate</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7w7mt-GM3-Styles-Motion-Easing_Duration-Tokens-2-2-v01.mp4?alt=media

A line graph illustrating a standard accelerate easing pattern.

<p>Standard accelerate</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7wjde-GM3-Styles-Motion-Easing_Duration-Tokens-2-3-v01.mp4?alt=media

<div class="table-wrapper"><table id="isPasted" style="width:100%"><thead><tr><th><br /></th><th style="width:24.7678%">Standard</th><th>Standard decelerate</th><th style="width:32.0718%">Standard accelerate</th></tr></thead><tbody><tr><th>Token</th><td>md.sys.motion.easing.standard</td><td>md.sys.motion.easing.standard.decelerate</td><td>md.sys.motion.easing.standard.accelerate</td></tr><tr><th>Android</th><td><a href="https://developer.android.com/reference/android/view/animation/PathInterpolator" rel="noopener noreferrer" target="_blank">PathInterpolator(0.2f, 0f, 0f, 1f)</a></td><td><a href="https://developer.android.com/reference/android/view/animation/PathInterpolator" rel="noopener noreferrer" target="_blank">PathInterpolator(0f, 0f, 0f, 1f)</a></td><td><a href="https://developer.android.com/reference/android/view/animation/PathInterpolator" rel="noopener noreferrer" target="_blank">PathInterpolator(0.3f, 0f, 1f, 1f)</a></td></tr><tr><th>CSS</th><td><a href="https://www.w3schools.com/cssref/func_cubic-bezier.asp" rel="noopener noreferrer" target="_blank">cubic-bezier(0.2, 0.0, 0, 1.0);</a></td><td><a href="https://www.w3schools.com/cssref/func_cubic-bezier.asp" rel="noopener noreferrer" target="_blank">cubic-bezier(0, 0, 0, 1);</a></td><td><a href="https://www.w3schools.com/cssref/func_cubic-bezier.asp" rel="noopener noreferrer" target="_blank">cubic-bezier(0.3, 0, 1, 1);</a></td></tr><tr><th>Flutter</th><td><a href="https://api.flutter.dev/flutter/animation/Cubic-class.html" rel="noopener noreferrer" target="_blank">Cubic(0.2, 0.0, 0, 1.0);</a></td><td><a href="https://api.flutter.dev/flutter/animation/Cubic-class.html" rel="noopener noreferrer" target="_blank">Cubic(0, 0, 0, 1);</a></td><td><a href="https://api.flutter.dev/flutter/animation/Cubic-class.html" rel="noopener noreferrer" target="_blank">Cubic(0.3, 0, 1, 1);</a></td></tr><tr><th>iOS</th><td><a href="https://developer.apple.com/documentation/quartzcore/camediatimingfunction" rel="noopener noreferrer" target="_blank">ControlPoints:0.2f:0.0f:0.0f:1.0f</a></td><td><a href="https://developer.apple.com/documentation/quartzcore/camediatimingfunction" rel="noopener noreferrer" target="_blank">ControlPoints:0.0f:0.0f:0.0f:1.0f</a></td><td><a href="https://developer.apple.com/documentation/quartzcore/camediatimingfunction" rel="noopener noreferrer" target="_blank">ControlPoints:0.3f:0.0f:1.0f:1.0f];</a></td></tr><tr><th>After Effects</th><td colspan="3">Use <a href="https://storage.googleapis.com/material-io-static/resources/material-easing-1.1.3.zxp" id="isPasted" rel="noopener noreferrer" target="_blank">After Effects Easing Panel</a> (download)</td></tr></tbody></table></div>

<h2 id="isPasted">Duration</h2>

<h3 id="isPasted">Short durations</h3><p>These are used for small utility-focused transitions.</p>

<div class="table-wrapper"><table style="width:100%"><tbody><tr><th style="text-align:center"><strong>Token</strong></th><td><strong>Value</strong></td></tr><tr><th>md.sys.motion.duration.short1</th><td>50ms</td></tr><tr><th>md.sys.motion.duration.short2</th><td>100ms</td></tr><tr><th>md.sys.motion.duration.short3</th><td>150ms</td></tr><tr><th>md.sys.motion.duration.short4</th><td>200ms</td></tr></tbody></table></div>

Animation showing a 200ms duration and standard easing curve applied to selection control interactions.

<p>Selection controls have a short duration of 200ms with Standard easing</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7xbhz-GM3-Styles-Motion-Easing_Duration-Tokens-3-v01.mp4?alt=media

<h3 id="isPasted">Medium durations</h3><p>These are used for transitions that traverse a medium area of the screen.</p>

<div class="table-wrapper"><table style="width:100%"><tbody><tr><th style="width:74.5655%;text-align:center"><strong>Token</strong></th><td><strong>Value</strong></td></tr><tr><th style="width:74.5655%">md.sys.motion.duration.medium1</th><td>250ms</td></tr><tr><th style="width:74.5655%">md.sys.motion.duration.medium2</th><td>300ms</td></tr><tr><th style="width:74.5655%">md.sys.motion.duration.medium3</th><td>350ms</td></tr><tr><th style="width:74.5655%">md.sys.motion.duration.medium4</th><td>400ms</td></tr></tbody></table></div>

Animation showing a FAB expanding into a sheet with a 400ms duration and Emphasized easing.

<p>A FAB expanding into a Sheet uses a 400ms duration with Emphasized easing</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7xucu-GM3-Styles-Motion-Easing_Duration-Tokens-4-v01.mp4?alt=media

<h3 id="isPasted">Long durations</h3><p>These durations are often paired with Emphasized easing. They're used for large expressive transitions.</p>

<div class="table-wrapper"><table style="width:100%"><tbody><tr><th style="text-align:center"><strong>Token</strong></th><td><strong>Value</strong></td></tr><tr><th>md.sys.motion.duration.long1</th><td>450ms</td></tr><tr><th>md.sys.motion.duration.long2</th><td>500ms</td></tr><tr><th>md.sys.motion.duration.long3</th><td>550ms</td></tr><tr><th>md.sys.motion.duration.long4</th><td>600ms</td></tr></tbody></table></div>

Animation showing a card expanding into a full screen with a 500ms duration and emphasized easing.

<p>A Card expanding to full screen uses a long 500ms duration with Emphasized easing</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7ysp0-GM3-Styles-Motion-Easing_Duration-Tokens-5-v01.mp4?alt=media

<h3 id="isPasted">Extra long durations</h3><p>Though rare, some transitions use durations above 600ms. These are usually used for ambient transitions that don't involve user input.</p>

<div class="table-wrapper"><table style="width:100%"><tbody><tr><th style="text-align:center"><strong>Token</strong></th><td><strong>Value</strong></td></tr><tr><th>md.sys.motion.duration.extra-long1</th><td>700ms</td></tr><tr><th>md.sys.motion.duration.extra-long2</th><td>800ms</td></tr><tr><th>md.sys.motion.duration.extra-long3</th><td>900ms</td></tr><tr><th>md.sys.motion.duration.extra-long4</th><td>1000ms</td></tr></tbody></table></div>

Animation showing the transition of an ambient carousel auto-advancing with a 1000ms duration and emphasized easing.

<p>An ambient carousel auto-advance transition uses an extra long 1000ms duration with emphasized easing</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flxo7z9jk-GM3-Styles-Motion-Easing_Duration-Tokens-6-v01.mp4?alt=media
