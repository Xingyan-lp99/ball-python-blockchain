# Inputs

Source: https://m3.material.io/foundations/interaction/inputs
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/e82cd926-292d-409b-892a-1553f01be9a8.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Inputs are devices that provide interactive control of an app. Common inputs include a mouse, keyboard, or touchpad.

## Tab 1

<ul><li id="isPasted">Design for touch, keyboard, and mouse interactions</li><li>Embrace multiple input methods and gestures within your app</li></ul>

Editing interface on a large screen device. The selected text is highlighted and the text cursor is visible.

<p>Designing for inputs allows people to use the inputs they prefer, like a mouse to highlight text on a tablet</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwvoasbb-1.png?alt=media

<h2>External inputs for devices</h2>

<p><span style="white-space:pre-wrap" id="isPasted">People can use external inputs like a mouse, keyboard, or stylus with their phone, tablet, foldable, TV, laptop, or desktop computer. When someone connects an external input to their device, they expect it to behave in familiar and useful ways. Designing for different input methods can make a product more usable and accessible on all screen sizes.</span></p>

<h3>Common features of external inputs</h3>

<h4><strong>Mouse</strong></h4><ul><li>Left and right click</li><li>Mouse wheel</li><li>Extra buttons</li></ul>

<h4><strong>Trackpad</strong></h4><ul><li>Left and right click</li><li>Gestures</li><li>Haptics</li></ul>

<h4><strong>Physical keyboard</strong></h4><ul><li>Replaces virtual keyboard</li><li>Media keys</li><li>Modifier keys</li></ul>

Image of a mouse.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4781mpt-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/EDnkwobNdIi9JnBJEISCm5eYhpIWsgVN2S_ZihqgFHsP7nILBYc1UC82xXCpptPSTQ9pgxBTFOGtAV0xHX_TzOrnyu-sstE1aqQhvG61pK4=s656

Image of a laptop keyboard and trackpad.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwvoce8y-3.png?alt=media

Image of a keyboard.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwvocxli-4.png?alt=media

<h3 dir="ltr" id="isPasted">Input device behaviors</h3><p>Depending on the input device, designers and developers can implement behaviors that meet standard conventions and user expectations.</p><div align="left" dir="ltr"><div class="table-wrapper"><table><thead><tr><th style="width:25.4505%">Input device action</th><th style="width:74.5495%">Anticipated behavior</th></tr></thead><tbody><tr><th>Mouse and trackpad movement<br /></th><td>Show a mouse cursor on the screen</td></tr><tr><th>Primary click<br /></th><td>Treat mouse clicks differently than touch events</td></tr><tr><th>Secondary click<br /></th><td>Activate context menus</td></tr><tr><th>Hover<br /></th><td>Change component states</td></tr><tr><th>Highlight</th><td>Allow text to be selected by the mouse cursor</td></tr><tr><th>Mouse wheel and trackpad two finger drag</th><td>Scroll list vertically and horizontally</td></tr><tr><th>Trackpad pinch<br /></th><td>Zoom an element or page</td></tr><tr><th>Physical keyboard<br /></th><td>Hide and show on screen keyboard</td></tr></tbody></table></div></div>

<h2>Mouse and cursor interactions</h2>

<p><span style="white-space:pre-wrap" id="isPasted">When an external mouse input device is used, a mouse cursor should be shown, regardless of the device type. <br /><br />A mouse may be connected to tablets, laptops, phones, foldables, and more. On some devices, it's possible to use an external input device simultaneously with touch input. <br /><br />On devices that don't specifically recognize mouse or stylus input, the mouse is treated as touch input.</span></p>

<h3>Primary click</h3>

<p><span style="white-space:pre-wrap" id="isPasted">A mouse click or stylus tap should demonstrate the same feedback as touch input. One example of this is showing the ripple for a pressed state.</span></p>

A view of a display with a visible mouse cursor.

<p>A visible mouse cursor is seen when the external input is connected</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm47884lw-Frame%201321316889.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Cb5WD95kLIK5F45ql60cUftzpvrvxGv8UxPGKAQCkKOdBFnZJ1zMtrQR8zKkTi7R4Gh_-jmKSWccF5DlfUXp12m7AwMcHfzXmvaj3T9JYDAZ=s1352

<h3>Secondary click</h3>

<h4>Context menus</h4><p><span style="white-space:pre-wrap" id="isPasted">A secondary click (whether using a single button or two fingers on a trackpad) should activate a context menu. The context menu shows additional options for the object that's clicked. See </span><span style="white-space:pre-wrap" id="isPasted"><a href="/m3/pages/menus/overview">menus</a></span><span style="white-space:pre-wrap" id="isPasted"> for more usage and guidelines.</span></p>

A context menu pop up from a link with the options: Open link in new window, Save link as, Copy link location, and Inspect.

<p>The context menu should appear when right clicking with a mouse or trackpad</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwvoetuu-6.png?alt=media

<h3>Hover</h3>

<p><span style="white-space:pre-wrap" id="isPasted">When using a mouse cursor, help users discover interactive objects by enabling visual changes. When the mouse rests on an interactive element, the hover state is a valuable cue for interaction. See </span><span style="white-space:pre-wrap" id="isPasted"><a href="/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844">states</a></span><span style="white-space:pre-wrap" id="isPasted"> for styles and guidelines.<br /><br />Hovering with a cursor (or stylus) should also invoke tooltips when applicable. See </span><span style="white-space:pre-wrap" id="isPasted"><a href="/m3/pages/tooltips/overview">tooltips</a></span><span style="white-space:pre-wrap" id="isPasted"> for guidance.</span></p><p><br /></p>

Icon button, floating action button, and menu items in their hovered and not hovered states.

<ol><li>Components without a hover state</li><li>Components with a hover state change applied</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwvofwmm-7.png?alt=media

<h3>Cursors</h3>

<p><span style="white-space:pre-wrap" id="isPasted">Cursors appear when using external input devices like a mouse or trackpad. The cursor can change to communicate more information about interactive elements.</span></p>

<h4>Pointer</h4><p><span style="white-space:pre-wrap" id="isPasted">By default, external input control should be rendered as a pointer.</span></p>

A cursor rendered as a pointer.

<ol class="decimal"><li><span style="white-space:pre-wrap">A pointer provides a visible indicator for input controls</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm478zll6-8.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/MW8dKSHxn8lhooyCbNv66f5sACoziJe1wryABcQYzei0NB1QJHHHVqdgbSGRxVZWTaKG6OQ4cAwu1HAwUEN_eDJNYFdK8kegwkE4wVpABLjK=s1352

<h4>Hand</h4><p><span style="white-space:pre-wrap" id="isPasted">The cursor should appear as a hand to indicate links or linked images.</span></p>

A link cursor (hand) shown when hovering over a linked image.

<ol><li>The hand cursor is used for links and clickable images</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwvogkod-8.png?alt=media

<h4>Resize arrows</h4><p><span style="white-space:pre-wrap" id="isPasted">The cursor should change to resize arrows on the boundaries of resizable elements.</span></p>

A cursor at the edge of the screen as resize arrows.

<ol class="decimal"><li><span style="white-space:pre-wrap">Resize arrows indicate an element can be resized</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4793i0f-8%20(1).png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/aRwe1YYgXEjJUzdpUE4zmut0gi_yxDBXooTLnGjJBam3RQxVhs2a49MKfwHQ8twxxBhfI2BBaK0ND-BaR9fLS1czLbpsxQDpYvUMTnnkGlc=s1352

<h4><span style="white-space:pre-wrap" id="isPasted">I-beam</span></h4><p><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">The cursor should appear as an I-beam when hovering on text. When manipulating editable text, the following interactions apply:<br /></span></span></p><ul><li><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Single click places the cursor<br /></span></span></li><li><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Double click selects a word<br /></span></span></li><li><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Triple click selects a paragraph<br /></span></span></li><li><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Single click deselects text and repositions the cursor</span></span></li></ul>

I-beam cursor hovering over selectable text.

<ol class="decimal"><li><span style="white-space:pre-wrap">An I-beam cursor indicates selectable text</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4798kwo-9.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/E5W_SctCrkKHCihIzCBXv5u805M6wtGVi3yUbX0aLhjAeI20kCi0iiEW7cC9D6ESJCGpjeIj7yxEtXpwaL20A8kzMlwF0yDx6HTcAfD2ZaQ=s1352

<h3>Text selection</h3><p><span style="white-space:pre-wrap" id="isPasted">When selecting text using a mouse, trackpad, or stylus:<br /></span></p><ul><li><span style="white-space:pre-wrap" id="isPasted">Highlight the selected area using a single color<br /></span></li><li><span style="white-space:pre-wrap" id="isPasted">Don’t show touch controls next to the highlighted area</span></li></ul>

Highlighted text in a single color.

<ol><li><span style="white-space:pre-wrap">Selected text shows a visible highlight</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm479c91z-12%20(1).png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/eubJ_19rLe9XCTY6isagTFwSDbS7CJ7cX0Cq1RREujdf6UYnHObBD2JkGz243IXVgGvLHghQxkZ7dGF4VlOxz9_q1wjLdf7XgiJlIXPv17OW7Q=s1352

<h3><span style="white-space:pre-wrap" id="isPasted">Text selection with touch control</span></h3>

<p><span style="white-space:pre-wrap" id="isPasted">When interacting using touch, always show touch controls, even if other inputs are connected.<br /><br />When using a mouse, trackpad, or stylus, show the I-beam and context menu, even if it's a touch device.</span></p>

Touch controls are produced on selected text, with mouse and trackpad detected.

<p><span style="white-space:pre-wrap">When using a touchscreen to select text, show touch controls</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm48p2zdz-13%20(2).png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/xoKyWfrnOMhrSuigyo4npW9rNQIFurShW01IyOXNrkuYzbIrcj68iuZkXMDrO-aziTXQhk5ZOT-SPutDWlR9wumV1VjP6lTq5jwE2cpEPleH=s1020

Selected text with a context menu, with mouse and trackpad detected.

<p><span style="white-space:pre-wrap">When using a mouse, trackpad, or stylus to select text, use the right-click context menu</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm48p38qk-14%20(2).png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/kalcMGlh7aH93geQ13BxCGUrfw2CvcwnPgHoh-XOSBfE-1g9ZCPCkv1fT84HLFASoOnWFb6MjXSBNiEFEGWXCDHourlTUpsxFwIEVFfCn13l=s1020

<h3><span style="white-space:pre-wrap" id="isPasted">Stylus input</span></h3><p><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">When using a stylus, cursors are usually not necessary, unless they communicate tool properties such as brush size or shape.</span></span></p>

A cursor rendered as a circle.

<ol class="decimal"><li><span style="white-space:pre-wrap">The circle cursor indicates the selected stylus tool and size</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm48p68lr-12%20(2).png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/3EzjVm189HykitEGTOdtrYA8VZNhYTSJwWcXtLiP2DzGuC2vxDeeR21k8ixi3Dl1BSlkS7Z0-BhYiHyDqKWJc73KpFG8lg-XWkQUL88MMUli=s1352

<h2>Mouse wheel and trackpad gestures</h2>

<p><span style="white-space:pre-wrap" id="isPasted">When an external mouse or touchpad is used, the mouse wheel and trackpad gesture allow more actions.</span></p>

<h3>Vertical scroll</h3><p>When a cursor is positioned on a list, the mouse wheel and two-finger touchpad gesture should allow vertical scrolling of the list.</p>

Stationary cursor over a scrolling field controlled by a mouse wheel or trackpad.

Scrolling a vertical list using the mouse wheel or trackpad gestures. Note that only the detail panel under the cursor scrolls.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwyimd28-GM3-Foundations-Interaction-Inputs-Guidelines-1-v01.mp4?alt=media

<h3>Touch scroll &amp; mouse text selection</h3><p>Upon touch and drag gesture, the text area will scroll. With a mouse interaction, dragging in a text area will select the text.</p>

Animation of a swipe gesture to scroll the screen.

<p>On a touch screen, dragging upward scrolls the field down</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwyinkvl-GM3-Foundations-Interaction-Inputs-Guidelines-2-1-v01.mp4?alt=media

Animation showing a dragging gesture with a mouse to select text and image.

<p>When using a mouse, dragging upward selects text and images</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwyioh3s-GM3-Foundations-Interaction-Inputs-Guidelines-2-2-v01.mp4?alt=media

<h3>Horizontal scroll</h3><p>Mouse users should be able to scroll with a mouse wheel to navigate horizontally scrolling fields. Trackpad users should be able to scroll using a two-finger horizontal gesture. </p>

A news feed of horizontally scrolling cards.

<p>Carousels can scroll horizontally using a scroll wheel or trackpad</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwyipb8r-GM3-Foundations-Interaction-Inputs-Guidelines-3-v01.mp4?alt=media

<h2>Physical keyboard</h2>

<p>When a physical keyboard is connected to a device, either externally or as a built-in laptop keyboard, users should be able to perform any actions that the virtual keyboard provides, and more.</p>

<h3>Show and hide virtual keyboard</h3><p>A virtual keyboard should appear or hide in response to the presence of a physical keyboard.</p>

Text being entered into a field with no on-screen keyboard displayed.

<p>When a physical keyboard is attached, hide the virtual keyboard</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0b7vzhy-19.png?alt=media

Text being entered into a field with an on-screen keyboard.

<p>When a physical keyboard is removed, show the virtual keyboard</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0b7w8fa-20.png?alt=media

<h3>Common keyboard interactions</h3>

<h4>Enter key</h4><p>People typically expect the <strong>E</strong><strong>nter</strong> key on a physical keyboard to be enabled by developers to allow a common function like sending a message. </p>

A message being typed into a chat, and sent using the Enter key.

<p>The<strong> Enter </strong>key typically triggers actions like sending a message</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwyiq9rm-GM3-Foundations-Interaction-Inputs-Guidelines-4-v01.mp4?alt=media

<h4>Spacebar control</h4><p><span style="white-space:pre-wrap">People typically expect the <strong>Spacebar</strong> (or available media keys) to be enabled to play and pause music or video.</span></p>

A video being paused and resumed by pressing the Spacebar. 

<p>Pressing <strong>Space</strong> usually pauses and plays media</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwyirw27-GM3-Foundations-Interaction-Inputs-Guidelines-5-v01.mp4?alt=media

<h4>Tab focus</h4><p><span style="white-space:pre-wrap" id="isPasted">When keyboard users navigate a page using <strong>Tab</strong>, the focus on interactive items must follow a logical order. On most pages, that means left to right, top to bottom.<br /><br />When focused from a keyboard or other input device, the focus state includes a ring-like keyboard focus indicator.</span></p>

Tab focus is on “small,” which is one of four size options for sweatshirts at an online store.

<p><span style="white-space:pre-wrap">Tab focus includes a visible keyboard focus indicator</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0b7yvt7-23.png?alt=media

Tab focus is on “medium,” which is one of four size options for sweatshirts at an online store.

<p><span style="white-space:pre-wrap">The focus state moves elements as the user presses <strong>Tab</strong> on their keyboard</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0b7zlqx-24.png?alt=media

<h4 id="isPasted"><span style="white-space:pre-wrap">Escape key</span></h4>

<p><span style="white-space:pre-wrap" id="isPasted">People typically expect the <strong>Escape</strong> key on a physical keyboard to dismiss elements, remove focus, or clear selections.</span></p>

Escape key dismisses menu.

<p><span style="white-space:pre-wrap">The <strong>Escape</strong> key should dismiss any visible modal elements like menus, dialogs, or bottom sheets</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmb9r9yci-G_Foundations_Interaction%2BInputs_1_IA_v04%20(1).mp4?alt=media

Escape key removes focus indicator from icon.

<p><span style="white-space:pre-wrap">The <strong>Escape</strong> key should remove any visible focus indicators and set the focus order to 0</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmb9rakzb-G_Foundations_Interaction%2BInputs_2_IA_v02%20(1).mp4?alt=media

Escape key dismisses text cursor and leaves text itself unchanged.

<p><span style="white-space:pre-wrap">The <strong>Escape</strong> key should remove the text cursor when typing, but should not remove already-typed text</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmb9rbhsj-G_Foundations_Interaction%2BInputs_3%20_IA_v02%20(1).mp4?alt=media
