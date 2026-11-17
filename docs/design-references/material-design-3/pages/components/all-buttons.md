# All buttons

Source: https://m3.material.io/components/all-buttons
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/276f1bd7-d048-49fd-8483-f267f2ece13d.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

When choosing the right button for an action, consider the level of emphasis each button type provides

## Tab 1

<h5><span style="white-space:pre-wrap" id="isPasted">There are 10 types of buttons in Material 3. </span></h5>

10 types of buttons.

<ol><li><span style="white-space:pre-wrap">Button<br /></span></li><li><span style="white-space:pre-wrap">Toggle button<br /></span></li><li><span style="white-space:pre-wrap">Icon button<br /></span></li><li><span style="white-space:pre-wrap">Toggle icon button<br /></span></li><li><span style="white-space:pre-wrap">Split button<br /></span></li><li><span style="white-space:pre-wrap">Standard button group<br /></span></li><li><span style="white-space:pre-wrap">Connected button group<br /></span></li><li><span style="white-space:pre-wrap">Floating action button (FAB) <br /></span></li><li><span style="white-space:pre-wrap">Extended FAB<br /></span></li><li><span style="white-space:pre-wrap">FAB menu</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4kdl8gi-1.png?alt=media

<h2>Choosing buttons</h2><div class="table-wrapper"><table class="borderGGrey400"><thead><tr><th style="width:22.4465%;text-align:left"><p>Level of emphasis</p></th><th style="width:13.6474%;text-align:left"><p>Component</p></th><th style="width:51.0869%;text-align:left"><p>Rationale</p></th><th style="width:12.6322%;text-align:left"><p>Example actions</p></th></tr></thead><tbody><tr><th rowspan="4" style="width:22.4638%;vertical-align:top"><p>High emphasis: For the primary, most important, or most common action on a screen</p></th><td><p><a href="/m3/pages/extended-fab/overview/" target="_blank">Extended FAB</a>, <a href="/m3/pages/fab/overview/" target="_blank">FAB</a>, and <a href="/m3/pages/fab-menu/overview" target="_blank">FAB menu</a><br /></p></td><td><p>The FAB and extended FAB are the largest and most visually prominent buttons. They’re designed for a page’s primary action. The extended FAB is best on large screens. The FAB menu provides multiple options.<br /></p></td><td><p>Create <br />Compose<br />New thread<br />New file<br /></p></td></tr><tr><td><p><a href="/m3/pages/common-buttons/guidelines#9ecffdb3-ef29-47e7-8d5d-f78b404fcafe" target="_blank">Button (filled)</a><br /></p></td><td><p>The filled button’s primary color palette makes it the most prominent button after the FAB. It’s used for final or unblocking actions in a flow.<br /></p></td><td><p>Save<br />Confirm<br />Done<br /></p></td></tr><tr><td><p><a href="/m3/pages/split-button/overview" target="_blank">Split button</a><br /></p></td><td><p>The split button’s primary color palette and menu icon are best used for key actions with multiple options.<br /></p></td><td><p>Send<br />Add<br />Create<br /></p></td></tr><tr><td><p><a href="/m3/pages/button-groups/overview" target="_blank">Button group</a><br /></p></td><td><p>The standard button group uses color, motion, and shape to capture attention. Use it to show multiple key actions.<br /></p></td><td><p>Back, Pause, Next<br /><br /></p></td></tr><tr><th rowspan="3" style="vertical-align:top"><p>Medium emphasis: For important actions that don’t distract users from the main task</p></th><td><p><a href="/m3/pages/common-buttons/guidelines#07a1577b-aaf5-4824-a698-03526421058b" target="_blank">Button (tonal)</a></p></td><td><p>The tonal button has a secondary color palette, making it less visually prominent than a regular, filled button. It can be used for final or unblocking actions, or for supporting actions.<br /></p></td><td><p>Save<br />Confirm<br />Done<br /></p></td></tr><tr><td><p><a href="/m3/pages/common-buttons/guidelines#4e89da4d-a8fa-4e20-bb8d-b8a93eff3e3e" target="_blank">Button (elevated)</a></p></td><td><p>The elevated button has a secondary color palette and a shadow. Only use it when a button requires visual separation from a patterned background.<br /></p></td><td><p>Reply<br />View all<br />Add to cart<br />Take out of trash<br /></p></td></tr><tr><td><p><a href="/m3/pages/common-buttons/guidelines#3742b09f-c224-43e0-a83e-541bd29d0f05" target="_blank">Button (outlined)</a><br /></p></td><td><p>Use an outlined button for actions that need attention but aren’t the primary action, such as “See all” or “Add to cart.” This is also the button to use for giving someone the opportunity to change their mind or escape a flow.</p></td><td><p>Reply<br />View all<br />Add to cart<br />Take out of trash<br /></p></td></tr><tr><th rowspan="3" style="vertical-align:top"><p>Low emphasis: For optional or supplementary actions with the least amount of prominence</p></th><td></td><td><p>The connected button group shows multiple related options. Use it for changing the content visible on a page.<br /></p></td><td><p>Walk, Bike, Drive<br /></p></td></tr><tr><td><p><a href="/m3/pages/common-buttons/guidelines#c9bcbc0b-ee05-45ad-8e80-e814ae919fbb" target="_blank">Button  (text)</a></p></td><td><p>The text button has no outline or fill. It should be used for actions not essential to the user journey.<br /></p></td><td><p>Learn more<br />View all<br />Change account<br />Turn on<br /></p></td></tr><tr><td><p><a href="/m3/pages/icon-buttons/overview" target="_blank">Icon button</a></p></td><td><p>The most compact and subtle type of button, icon buttons are used for optional supplementary actions such as “Bookmark” or “Star.”<br /></p></td><td><p>Add to Favorites Print<br /></p></td></tr></tbody></table></div>

<h2>Hierarchy</h2>

<p dir="ltr"><strong>One high emphasis button</strong></p><p dir="ltr" id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Each screen should contain a single prominent button for the primary action. This high-emphasis button commands the most attention. The arrangement of on-screen elements should clearly communicate that other buttons are less important.</span></p><p dir="ltr"><br /></p><p dir="ltr"><strong>Other buttons</strong></p><p dir="ltr"><span style="white-space:pre-wrap" id="isPasted">A product can show more than one button at a time in a layout. Use different color styles to create visual hierarchy and indicate the importance of each button.</span></p>

3 types of hierarchy: high emphasis, medium emphasis, and low emphasis.

<p>A button’s level of emphasis helps determine its appearance, typography, and placement</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0gpi7ar-2.png?alt=media

<h2 dir="ltr" id="isPasted">Placement</h2>

<p dir="ltr" id="isPasted"><span style="white-space:pre-wrap">Use a combination of button styles on the same screen to focus attention on a primary action, while offering alternatives.</span></p>

Newsfeed screen with 3 different types of buttons following the emphasis hierarchy.

<ol><li><span style="white-space:pre-wrap">A filled button for a high-emphasis action<br /></span></li><li><span style="white-space:pre-wrap">A text button for a low-emphasis action<br /></span></li><li><span style="white-space:pre-wrap">An extended FAB for the highest emphasis action</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4k8798m-3.png?alt=media

Text button to the left of a filled button.

<p>For multiple actions, choose a higher-emphasis button for the more important action, such as a filled button next to a text button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4k87hb1-4.png?alt=media

Outlined button to the left of a filled button.

<p>When using multiple buttons, you can place an outlined button (medium emphasis) next to a filled button (high emphasis)</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4k87km1-5.png?alt=media

Text button to the left of an outlined button.

<p>When using multiple buttons, you can place a text button (low emphasis) next to an outlined button (medium emphasis)</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4k87oz2-6.png?alt=media

Single filled button at the bottom of a mobile screen.

<p>Use a filled button on its own for a single important action</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4k87stt-7.png?alt=media

Filled button stacked above a text button.

<p>Avoid placing a button below another button if there's space to place them side-by-side</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4k87x4t-8.png?alt=media
