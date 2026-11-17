# Design for watches

Source: https://m3.material.io/foundations/watches
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/ece8884d-3ef7-4f41-af54-9a402b3bd527.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Watches have special design considerations and interaction patterns

## Overview

<h2>Resources</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:26.5528%"><p>Type</p></th><th style="width:73.3341%"><p>Resource</p></th></tr></thead><tbody><tr><td rowspan="3" style="width:26.5528%;vertical-align:top"><p>Design</p></td><td><p><a href="https://m3.material.io/" target="_self">About M3 Expressive</a></p></td></tr><tr><td><p><a href="https://developer.android.com/design/ui/wear/guides/get-started" target="_blank">M3 Expressive on Wear OS</a></p></td></tr><tr><td><p><a href="https://developer.android.com/design/ui/wear/guides/get-started/design-kits" target="_blank">Figma Design Kits for Wear OS</a></p></td></tr><tr><td rowspan="2" style="width:26.5528%;vertical-align:top"><p>Implementation</p></td><td><p><a href="https://developer.android.com/training/wearables" target="_blank">Android Developers: Wear OS</a></p></td></tr><tr><td><p><a href="https://developer.android.com/training/wearables/compose?version=3" target="_blank">Jetpack Compose for Wear OS</a></p></td></tr></tbody></table></div>

<h2>New in GM3 Expressive</h2><p>Design expressive layouts for watches with harmonious shape, animation, color, and typography treatments. All examples shown here are based on Material for Wear OS. <a href="https://developer.android.com/design/ui/wear/guides/get-started" target="_blank">More on M3 Expressive on Wear OS</a></p>

<h3>Designed for round screens</h3><p>A new shape system with edge-hugging containers and buttons creates variety and visual balance on round screens.</p><p><a href="https://developer.android.com/design/ui/wear/guides/get-started/apply" target="_blank">More on shape system for Wear OS</a></p>

Watch screenshots using rounded buttons, progress bars, and page indicators.

<p>Controls for smartwatches can adapt to the form factor</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4amaej-01.png?alt=media

<h3>Expressive motion &amp; springs</h3><p>A new physics-based system makes interactions and transitions feel more alive, fluid, and natural.<br /><br /><a href="/m3/pages/motion-overview/how-it-works" target="_blank">More on M3 motion physics</a></p>

A settings screen scrolling through options.

<p>Use motion to make interactions intuitive</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmq5i6utk-Platforms%20-%20WearOS%20-%20Overview%2002%20-%20IA%20-V01.mp4?alt=media

<h3>Shape morphing</h3><p>With shape morphing, controls respond to show interaction. Containers change corner radius.<br /><br /><a href="/m3/pages/shape/shape-morph" target="_blank">More on M3 shape morphing</a><br /></p>

A number pad with buttons morphing from rounded to squared as they are pressed.

<p>Selected buttons change shape to show interaction</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmq5i6n4r-Platforms%20-%20WearOS%20-%20Overview%2001%20-%20IA%20-%20v01.mp4?alt=media

<h3>Rich color</h3><p>Dynamic color and deep tonal palettes are applied in a system of <app-froala-tooltip-element description="Material has 26 standard color roles organized into six groups: primary, secondary, tertiary, error, surface, and outline." link-label="More on color roles" link-url="/google-material-3/pages/color-roles#8b68e9f2-2db2-408f-b002-55adba3b6299" should-open-link-in-new-tab="true">color roles</app-froala-tooltip-element> to create depth and variety.</p><p><a href="https://developer.android.com/design/ui/wear/guides/styles/color" target="_blank">More on color for Wear OS</a></p>

A media player on a smartwatch displaying a song title, artist, and playback controls.

<p>The color system includes three main colors and specific color roles to create depth and variety</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4aosfu-04%20alt.png?alt=media

<h3>New type roles</h3><p>Along with an updated and optimized <a href="https://developer.android.com/design/ui/wear/guides/styles/typography/type-scale-tokens" target="_blank">type scale</a>, new styles serve specific use cases for watches:</p><ul><li><p><a href="https://developer.android.com/design/ui/wear/guides/styles/typography/apply#arc-styles" target="_blank">Arc</a> text for curved titles</p></li><li><p><a href="https://developer.android.com/design/ui/wear/guides/styles/typography/apply#numeral-styles" target="_blank">Numeral</a> text for bigger, stylized text</p></li></ul><p><a href="https://developer.android.com/design/ui/wear/guides/styles/typography" target="_blank">More on typography for Wear OS</a></p>

3 smartwatch screens showing a fitness tracker, a timer, and a calendar notification using Roboto Flex.

<p>The baseline type scale is optimized for round screens to keep text legible in a compact space</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4antdv-05.png?alt=media

## Foundations

<h2>Resources</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:19.2202%"><p>Type</p></th><th style="width:80.6667%"><p>Resource</p></th></tr></thead><tbody><tr><td rowspan="3" style="width:19.2202%;vertical-align:top"><p>Design</p></td><td><p><a href="https://m3.material.io/get-started" target="_self">Get Started with M3 Expressive</a></p></td></tr><tr><td><p><a href="https://developer.android.com/design/ui/wear/guides/get-started/design-for-wearables" target="_blank">UI Design for Wear OS</a></p></td></tr><tr><td><p><a href="https://developer.android.com/design/ui/wear/guides/get-started/design-kits" target="_blank">Figma Design Kits for Wear OS</a></p></td></tr><tr><td rowspan="2" style="width:19.2202%;vertical-align:top"><p>Implementation</p></td><td><p><a href="https://developer.android.com/training/wearables" target="_blank">Android Developers: Wear OS</a></p></td></tr><tr><td><p><a href="https://developer.android.com/training/wearables/compose?version=3" target="_blank">Jetpack Compose for Wear OS</a></p></td></tr></tbody></table></div>

<h2>Anatomy</h2>

<h3>The watch face</h3>

<p>Watch faces display the time, as well as  other information and can provide access to other functions through apps and tiles.<br /><br />They can also include complications, self-contained details that can show contextual info like heart rate or progress.<br /><br />Ongoing activities on the watch face show in-progress actions, like a stopwatch countdown or a workout timer.</p>

A watch face with hands showing analog time readout, and complications showing the date in a calendar, heart rate, water consumption, and weather.

<p><strong>Complications</strong> are details on the watch face that can be customized for style or function</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4b8pnm-01.png?alt=media

A watch face with an entry point for an ongoing exercise activity.

<p><strong>1. Ongoing activities</strong>, like timers, media players, or workouts, can be accessed from the watch face</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4b9kvw-02.png?alt=media

<h3>Physical buttons</h3><p>Wearable devices can have a variety input surfaces, which include physical buttons and controls.</p>

3 watch faces with indications showing the locations of a rotating side button, system button, and multifuction button.

<ol class="decimal"><li><p>Rotating side buttons: Used for volume control, or to scroll through options or lists</p></li><li><p>System buttons: Dedicated to OS functions like powering on and off, and cannot be customized</p></li><li><p>Multifunction buttons: Used by apps for custom actions like starting and stopping a stopwatch</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4bb056-04.png?alt=media

<h2>Design principles</h2><ul><li><p>Tailor layouts for different screen sizes with <a href="https://developer.android.com/design/ui/wear/guides/foundations/adaptive-design" target="_blank">adaptive design</a></p></li><li><p>Design for short interactions to conserve battery</p></li><li><p>Focus on one or two tasks at a time rather than a full app experience</p></li><li><p>Test designs in situations that involve movement to make sure the design is usable at a glance</p></li></ul>

Calendar screen with date, time of dentist appointment, and more button.

<p>At-a-glance views allow people to quickly see calendar events</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4bcxbd-05-do.png?alt=media

3 columns with times, dates, and appointment names cut off.

<p>Don't create complex and detailed apps such as a calendar grid</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4bdrul-06-dont.png?alt=media

<h3>Always relevant</h3><p>Watches are always with people. Consider how to update app content based on context, such as time, place, and activity.</p>

A map search for a garden’s location on a watch and on a phone.

<p>Navigation on a watch complements the experience on a phone</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4befpv-07.png?alt=media

<h3>Works offline</h3><p>Design for slow connections and offline use, such as exercising and commuting.</p>

2 watches: 1 with offline music downloads list. 1 with a dialog about no internet connection with dismiss and accept buttons.

<p>The network state can be communicated through:</p><ol class="decimal"><li><p>An offline icon</p></li><li><p>A dialog</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4bf7c4-08.png?alt=media

<h2>Interaction patterns</h2>

<h3>Cross-device experiences</h3><p>Watches are often dependent on connected phones for functionality or complex interactions. In some cases, a watch and a phone are used together to accomplish different parts of the same task.</p><p>Consider how experiences can be consistent and complement the strengths of each device.</p><p><a href="https://developer.android.com/multi-device-development" target="_blank">More on multidevice development for Android</a></p>

A contact entry shown on a phone and a watch, with options to call or message.

<p>Consider which actions are appropriate for each device</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4bg988-09-do.png?alt=media

<h3>Always on displays</h3><p>Watches can have always on displays, which allow ambient content to be shown when the watch isn’t in use.</p><p>This are especially helpful for ongoing experiences like a timer or a workout that should remain in view. Because they remain on the screen for long time periods, consider limiting the number of pixels that are illuminated.</p><p><a href="https://developer.android.com/training/wearables/always-on" target="_blank">More on always-on apps and system ambient mode in Wear OS</a></p>

A watch face showing progress through a task and the current time.

<p>Limit the number of illuminated pixels for a display that's always on</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4bgxlg-10.png?alt=media

## Styles

<h2>Resources</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:20.5776%"><p>Type</p></th><th style="width:79.3092%"><p>Resource</p></th></tr></thead><tbody><tr><td rowspan="4" style="width:20.5776%;vertical-align:top"><p>Design</p></td><td><p><a href="https://developer.android.com/design/ui/wear/guides/get-started" target="_blank">M3 Expressive on Wear OS</a></p></td></tr><tr><td><p><a href="https://developer.android.com/design/ui/wear/guides/styles/typography" target="_blank">Typography for Wear OS</a></p></td></tr><tr><td><p><a href="https://developer.android.com/design/ui/wear/guides/styles/color" target="_blank">Color for Wear OS</a></p></td></tr><tr><td><p><a href="https://developer.android.com/design/ui/wear/guides/get-started/apply#shape-motion" target="_blank">Motion for Wear OS</a></p></td></tr><tr><td rowspan="2" style="width:20.5776%;vertical-align:top"><p>Implementation</p></td><td><p><a href="https://developer.android.com/training/wearables" target="_blank">Android Developers: Wear OS</a></p></td></tr><tr><td><p><a href="https://developer.android.com/training/wearables/compose?version=3" target="_blank">Jetpack Compose for Wear OS</a></p></td></tr></tbody></table></div>

<h2>Typography</h2><p>GM3 Expressive adds two type styles specially designed for watches. <a href="https://developer.android.com/design/ui/wear/guides/styles/typography/type-scale-tokens" target="_blank">More on the type scale for Wear OS</a></p>

<h3>Numerals</h3><p>Numeral text styles display numbers, usually only a few digits at a time. This text can take on more expressive properties at larger display sizes without the accommodations usually required by text that must be localized.</p>

A watch face with an indication for the numeral text style used to show the time.

<ol class="decimal"><li><p>Numeral Large</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4bxhlf-22.png?alt=media

<h3>Arc text</h3><p>Arc text is specially designed for text following a curved path on a round screen, such as page titles, confirmation overlays, or a call to action. It optimizes character spacing for text displayed along a curve at the top or bottom of a round screen.</p>

A close-up of a watch face with arc text showing “check your phone” hugging the bottom bevel of a round screen.

<ol class="decimal"><li><p>Arc Large</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4byceo-23.png?alt=media

<h2>Color</h2><p>Material for Wear OS provides a custom <a href="https://developer.android.com/design/ui/wear/guides/styles/color/system" target="_blank">color system</a> to create vibrant experiences and clear visual hierarchy.</p>

<h3>Build from black</h3><p>Watches are designed with a black background, instead of the tinted background that phones use.</p>

2 watch screens showing sleeping app and a number picker.

<p>Watches use a black background to conserve battery</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4bz1nw-1.png?alt=media

<h3>Color roles</h3><p>Since watches are used throughout the day, color <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/google-material-3/pages/design-tokens/overview" should-open-link-in-new-tab="true">tokens</app-froala-tooltip-element> for Wear OS are specifically tailored for dark themes in low-light environments and light themes for daylight environments.</p><p><a href="https://developer.android.com/design/ui/wear/guides/styles/color/roles-tokens" target="_blank">More on color roles for Wear OS</a></p>

3 examples of “Accept” and “Decline” buttons that are legible.

<p>Buttons with (2) <strong>on primary</strong> on (1) <strong>primary</strong> and (4) <strong>on</strong> <strong>primary container</strong> on (3) <strong>primary container</strong> stay legible as the contrast level changes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4bzy9c-21.png?alt=media

Buttons with (2) primary dim on (1) primary or (4) primary dim on (3) primary container become illegible as contrast levels shift

<p>Buttons with (2) <strong>primary dim</strong> on (1) <strong>primary</strong> or (4) <strong>primary dim</strong> on (3) <strong>primary container</strong> become illegible as contrast levels shift</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4c1f7y-22.png?alt=media

<h3>Recommended color combinations for Wear OS</h3><p>Below are some common color pairings that can help establish priority, function, and elevation.</p><ul><li><p>Use <strong>primary dim</strong> to highlight important elements and <strong>tertiary</strong> to provide standout feedback, such as tap responses</p></li><li><p>When the main action isn't clear, use <strong>tertiary</strong> and <strong>primary</strong> for main actions and <strong>secondary container</strong> for complementary actions</p></li><li><p>Use <strong>secondary</strong> and <strong>primary container</strong> to show two equally important options or containers, while maintaining contrast</p></li></ul>

Three buttons, with the center one in Primary and side ones in Primary Dim. 

<ol class="decimal"><li><p>Primary</p></li><li><p>Primary dim</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4c3ekq-23.png?alt=media

 A number pad with most keys in Primary Dim and the pressed key in Tertiary. 

<ol class="decimal"><li><p>Primary dim</p></li><li><p>Tertiary</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4c4fsb-24.png?alt=media

Call button in tertiary color, open button in primary color and open on phone button in secondary-container.

<ol class="decimal"><li><p>Tertiary</p></li><li><p>Primary</p></li><li><p>Secondary container</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4c72hg-28.png?alt=media

accept button in primary and delete button in primary container.

<ol class="decimal"><li><p>Primary</p></li><li><p>Tertiary</p></li><li><p>Primary container</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4c6oau-30.png?alt=media

Plus button in primary color, date button is in tertiary color and appointment summary is in primary container color.

<ol class="decimal"><li><p>Primary dim</p></li><li><p>Tertiary dim</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4cam7e-27.png?alt=media

Bicycle button in primary, weight button in tertiary dim.

<ol class="decimal"><li><p>Primary</p></li><li><p>Tertiary dim</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4c7zvn-31.png?alt=media

<h2>Motion and transitions</h2><p>Expressive motion makes interactions feel more alive, fluid, and natural. Use transitions give intuitive feedback to show how an app works, such as standard patterns for changes in state or hierarchy.<br /><br /><a href="https://developer.android.com/design/ui/wear/guides/get-started/apply#shape-motion" target="_blank">More on shape and motion for Wear OS</a></p>

A settings screen scrolling through options.

<p>Use expressive motion to show items selected</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmq5ib9cq-Platforms%20-%20WearOS%20-%20Overview%2002%20-%20IA%20-V01.mp4?alt=media

<h2>Haptics</h2><p>Haptics are tactile effects used to grab a person’s attention for something important, or add emphasis to an interaction on the screen. You can use haptics to provide responsive feedback to scrolling and selecting items from a list, or controlling volume.</p>

<p>Use system-defined patterns and tokens (when available) to reinforce interaction expectations. Synchronize haptics with UI motion and sound to provide richer feedback.</p><ul><li><p>Use stronger haptics for key interactions, such as a payment confirmation</p></li><li><p>Use subtler haptics for precision interactions, such as scrolling through a list</p></li></ul><p><a href="https://developer.android.com/develop/ui/views/haptics/haptics-principles" target="_blank">More on haptics for Wear OS</a></p>

2 watch faces with lines indicating haptics for a payment being accepted and scrolling through notifications.

<p>Use stronger haptics for key interactions and subtler feedback for precision interactions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4c8vp7-x.png?alt=media

## Layout

<h2>Resources</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:21.4755%"><p>Type</p></th><th style="width:78.4113%"><p>Resource</p></th></tr></thead><tbody><tr><td rowspan="4" style="width:21.4755%;vertical-align:top"><p>Design</p></td><td><p><a href="https://developer.android.com/design/ui/wear/guides/foundations/common-layouts" target="_blank">Wear OS common design layouts</a></p></td></tr><tr><td><p><a href="https://developer.android.com/design/ui/wear/guides/foundations/adaptive-design" target="_blank">Adaptive layout for Wear OS</a></p></td></tr><tr><td><p><a href="https://www.figma.com/community/file/1506418396052412186" target="_blank">Figma Design Kit for Wear OS Apps</a></p></td></tr><tr><td><p><a href="https://www.figma.com/community/file/1507852095734722321/m3-wear-os-tiles-design-kit?fuid=1348995927136540612" target="_blank">Figma Design Kit for Wear OS Tiles</a></p></td></tr><tr><td><p>Implementation</p></td><td><p><a href="https://developer.android.com/training/wearables" target="_blank">Android Developers: Wear OS</a></p></td></tr></tbody></table></div>

<h2>Layout principles</h2>

A social networking scrolling screen showing Followers, sorting and search.

<p><strong>Prioritize content</strong></p><p>Place the most important information at the top of the screen.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4d4yba-01.png?alt=media

An audio interface showing headphones are connected with volume indicator and controls.

<p><strong>Limit choices</strong></p><p>Reduce the number of actions to prevent decision fatigue. Focus on critical tasks to help people get things done within seconds.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4d5pli-02.png?alt=media

A dialog confirming device access to call log and contacts.

<p><strong>Simplify navigation</strong></p><p>Use a clear, shallow hierarchy so people don't get lost in complex menus. Aim to display content and navigation inline.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4d6ew9-03.png?alt=media

<h2>Standard layouts</h2>

<p>For scrolling and non-scrolling apps:</p><ul><li><p>The time is shown on most app screens</p></li><li><p>Edge-hugging buttons are used for round screens</p></li><li><p>Show an indicator if more content is available on a scrolling apps</p></li></ul><p>Wear OS offers <a href="https://developer.android.com/design/ui/wear/guides/get-started/design-kits" target="_blank">Figma Design Kits</a> for standard layouts, with components, styles, and variables.</p>

A watch screen showing a social media app and a watch screen showing a timer with element indicators.

<ol class="decimal"><li><p>Time text</p></li><li><p>Page title</p></li><li><p>Scroll indicator</p></li><li><p>Action button</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4d7u52-04.png?alt=media

<h3>Non-scrolling layouts</h3><p>Non-scrolling layouts are for focused tasks or single-screen interactions where all content fits within the display, such as: </p><ul><li><p>Media players</p></li><li><p>Pickers and switchers</p></li><li><p>Fitness tracking screens</p></li><li><p>Confirmation dialogs </p></li></ul><p><a href="https://developer.android.com/design/ui/wear/guides/surfaces/apps/layouts/scrolling" target="_blank">More on non-scrolling layouts for Wear OS</a></p>

A non-scrollable timer with current time 9:30, timer set for 00:25:52, and a start button.

<p>Use non-scrolling layouts for focused tasks like a timer</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4d8mdi-05.png?alt=media

<h3>Scrolling layouts</h3><p>Scrolling layouts can show content that exceeds the screen height, such as lists or dialogs. These might include:</p><ul><li><p>Message threads</p></li><li><p>Contact lists</p></li><li><p>Menu options</p></li></ul><p><a href="https://developer.android.com/design/ui/wear/guides/surfaces/apps/layouts/scrolling" target="_blank">More on scrolling layouts for Wear OS</a></p>

A scrollable layout with current time, search button, 1st follower and avatar on screen, and two followers off screen.

<p>Lists use scrolling layouts to show additional options</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4d98d6-06.png?alt=media

<h3>Tiles</h3><p>Tiles (or widgets) are designed for glanceability. Use them to show timely updates or to help people perform frequent tasks quickly, such as checking progress towards a goal or viewing the weather.</p><p>Tiles are accessible with a swipe from the watch face. They have a fixed screen height and don't scroll.</p><p><a href="https://developer.android.com/design/ui/wear/guides/foundations/common-layouts/tiles" target="_blank">More on tiles for Wear OS</a></p>

Icon buttons for meditation, running, cycling, and a More button

<p>Use tiles for quick access to to a few key options</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4dbada-07.png?alt=media

<h3>Notifications</h3><p>Notifications can be expanded to offer more interactions, such as replying to a message, opening a location on a map, or playing a song.</p><p>Wear OS provides notification templates for instant messaging and calendar events.</p><p><a href="https://developer.android.com/training/wearables/notifications" target="_blank">More on notifications for Wear OS</a></p>

A message notification shown in a drawer with dimmed notifications above and below.

<p>Notifications should offer easy access to more interactions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4dbzlj-08.png?alt=media

<h3>Adaptive layout</h3><p>Adaptive design allows apps to adapt to different screen sizes and device contexts. On Wear OS, this means apps scale and reorganize to maximize the available space on both small and large round displays. <a href="https://developer.android.com/jetpack/androidx/releases/compose-material3?_gl=1*1ntglil*_ga*NzMzMjg1Nzc1LjE3NDg5MTM2NjI.*_ga_QPQ2NRV856*czE3NjQ3MDkwMjUkbzc2JGcxJHQxNzY0NzEwNjAyJGo0MCRsMCRoMA.." target="_blank">The Material 3 Compose component library</a> has built-in adaptive behavior.</p><ul><li><p>Design for small screens first: Start by designing for the smallest common screen size</p></li><li><p>Use percentages: Define margins and padding using percentages rather than fixed pixel values. This prevents clipping and ensures content remains centered and proportional as the screen size increases.</p></li><li><p>Add value on larger screens: Use the extra space on screens larger to show more content, such as additional buttons, text lines, or data visualizations</p></li><li><p>Test all font sizes: Font scaling and accessibility settings such as bold text may cause changes in the size of UI elements</p></li></ul><p><a href="https://developer.android.com/design/ui/wear/guides/foundations/adaptive-design" target="_blank">More on adaptive layout for Wear OS</a></p><p></p>

5, 10, and 15 minute alarm buttons plus an edge-hugging more button.

<p>Design for small screens first, starting with a 192dp size watch</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4dcvb2-09.png?alt=media

5, 10, 15, 20 &amp; 30 minute alarm buttons plus an edge-hugging more button.

<p>Show more content on devices that are larger than 225dp</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4dg8dm-10.png?alt=media
