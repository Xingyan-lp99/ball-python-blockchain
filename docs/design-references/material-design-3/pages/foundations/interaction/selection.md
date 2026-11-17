# Selection

Source: https://m3.material.io/foundations/interaction/selection
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/0dfa5930-0695-4d99-a58a-2a7705c79d66.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Selection is how people interact with UI elements or choose which items to act on

## Tab 1

<ul><li id="isPasted">Selection is shown through changes to surface color or other visible elements</li><li>An entire component can be selected, or just certain parts in a component</li><li>Selection can be performed via tap, cursor, keyboard, or voice</li></ul>

<h2>Resources</h2>

<div class="table-wrapper"><table id="isPasted" style="margin-right:calc(0%);width:100%"><thead><tr><th style="width:17.093%">Type</th><th style="width:37.907%">Link</th><th style="width:45%">Status</th></tr></thead><tbody><tr><th style="width:17.093%">Design</th><td><a href="http://goo.gle/m3-design-kit" rel="noopener noreferrer" target="_blank">Design Kit (Figma)</a></td><td>Available</td></tr></tbody></table></div>

<h2>Selection indicators</h2>

<p id="isPasted">Selections are displayed using a check mark icon, a checkbox component, a change in surface color, or a combination.</p><p>Selections are inherited by the following components: </p><ul><li>Cards</li><li>Checkboxes</li><li>Chips</li><li>Data tables</li><li>Icon buttons</li><li>List items</li><li>Menu items</li><li>Pickers</li><li>Radio buttons</li><li>Segmented buttons</li><li>Sliders</li><li>Switch</li></ul>

Seven types of selected  components.

<p>Selected components:</p><ol><li>Segmented buttons</li><li>Chips</li><li>List items </li><li>Checkboxes</li><li>Radio buttons </li><li>Switch</li><li>Slider</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm1qhf1tb-1.png?alt=media

<p id="isPasted">The following components use an active indicator to represent which item is currently selected:</p><ul><li>Navigation bar</li><li>Navigation drawer</li><li>Navigation rail</li><li>Tabs</li></ul><p>The color and shape of the active indicator varies between components. In these components, only one item should be selected at a time.</p>

Tabs and navigation drawer with one destination item selected. Selection is identified with an active indicator.

<p id="isPasted">Selected components with active indicators:</p><ol><li>Tab</li><li>Navigation drawer</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwvowprh-2.png?alt=media

<h2><span style="white-space:pre-wrap">Types of selection</span></h2>

<h3>Touch</h3><p id="isPasted">On touch devices, select items using:</p><ul><li>Long press touch or two-finger touch</li><li>Selection shortcut, if available, such as tapping an avatar</li></ul>

Touch used to select 3 list items one after another.

<p>Items in a list selected via touch</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flfwnm6vf-1P-Touch-2x.png?alt=media

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwvoyebi-GM3-Foundations-Interaction-Selection-Guidelines-1-v01.mp4?alt=media

<h3>Entering and exiting selection mode</h3><p id="isPasted">To select an item and enter selection mode, long press the item or use a shortcut, such as tapping the item’s avatar. To select additional items, tap each of them.</p><p>To exit a selection mode, tap each selected item until they’re unselected, or tap an action on the toolbar.</p>

List items are tapped to select and unselect them.

<p>Entering and exiting selection mode</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwvozn9v-GM3-Foundations-Interaction-Selection-Guidelines-2-v02.mp4?alt=media

<h3>Larger selections</h3><p id="isPasted">To select multiple items simultaneously, long press and drag across items. Don’t use this gesture combination if it is already in use to pick up and move items, like cards.</p>

Long press and drag used to select multiple images in a photo feed.

<p><strong>Long press</strong> and <strong>drag</strong> can be used together to select items in batches</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flfwnntlu-1P%20-%20Larger%20selection-do.png?alt=media

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwvp1iai-GM3-Foundations-Interaction-Selection-Guidelines-3-v01.mp4?alt=media

Long press and drag combination used to move cards, but can’t be used to batch select items while in use.

<p>If the <strong>long press</strong> and <strong>drag</strong> combination is already in use to pick up and move components, like cards, then the combined gesture can’t also be used for selecting items in batches</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flfwo38nu-1P%20-%20Larger%20selection-dont.png?alt=media

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwvp2p5n-GM3-Foundations-Interaction-Selection-Guidelines-4-v01.mp4?alt=media

<h3>Click</h3><p id="isPasted">On desktop, checkboxes are always visible when selection is the primary activity. When selection is secondary, checkboxes (or other indicators) are displayed:</p><ul><li>As a single checkbox for that item on hover</li><li>For all items after one item is selected</li></ul><p>To make a selection, hover over an item to reveal a checkbox. The checkbox can then be clicked.</p>

Checkboxes being selected and unselected.

<p>Checkboxes are visible by default in this table because selection is a primary activity</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flfwnp3as-1P%20-%20Click.png?alt=media

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0b935j3-GM3-Foundations-Interaction-Selection-Guidelines-5-v01.mp4?alt=media
