# Writing and text

Source: https://m3.material.io/foundations/writing
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/672aa1bf-2faf-4bf9-b0b5-7a9d782da071.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Ensure text is helpful, clear, and resilient to change

## Best practices

<h2 id="isPasted">Accessibility text</h2><p><span style="white-space:pre-wrap">Accessibility text refers to text that is used by screen reader accessibility software, such as Google’s TalkBack on Android, Apple’s VoiceOver on iOS, and Freedom Scientific’s JAWS on desktop. Screen readers read aloud the on-screen text and elements (such as buttons), including both visible and nonvisible alternative text.</span></p>

<h3 id="isPasted">Adjacent text</h3><p>To make an image more accessible, the text in and around images should consider presenting key information about the image.</p>

Stacked card with image, caption, and adjacent text identified.

<ol><li>Image</li><li>Caption</li><li>Adjacent text</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj55hv4-8.png?alt=media

<h3 id="isPasted">Captions</h3><p>Captions are the text that appear below an image. They explain contextual information about the image to help the reader understand how it relates to the content. Both sighted and screen reader users rely on captions for descriptions of images.</p>

Stacked card with image, alt text as caption, and adjacent text identified.

<p>Use captions to help readers understand how the image relates to the content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5628d-9.png?alt=media

<h3 id="isPasted">Embedded text in images</h3><p>Screen readers are unable to read text that is embedded in imagery. If there is essential information embedded as text in the image, include the essential information in the <a href="/m3/pages/alt-text">alt text</a>.</p>

Stacked card with image, caption overlayed on image, and adjacent text.

<p>Take caution when embedding essential information anywhere a screenreader can't access, like text inside an image</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj56jdc-10.png?alt=media

<h3 id="isPasted">Alternative text (Alt text)</h3><p>Alt text helps translate a visual UI into a text-based UI. Alt text is a short label (up to 125 characters) in the code that describes an image for users who are unable to see them. Since alt text is only for images, there is no need to add “image of” or “picture of” to the alt text. A screen reader will read the alt text aloud in place of the image. </p><p>Alt text is valuable for sighted users, as well, because alt text appears if an image fails to load. Include targeted keywords to help inform the user about the image. Keywords can also improve search engine optimization (SEO).</p><p><a href="/m3/pages/alt-text">Learn more about writing alt text</a></p>

A DJ standing in front of music equipment with alt text underneath describing image.

Use alt text to convey what the image is showing in an informative, short phrase.
Alt text example: A DJ performs a set under lights and lasers

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj573aa-7.png?alt=media

<h2>Text color</h2>

<h3 id="isPasted">Essential and non-essential elements</h3><p><span style="white-space:pre-wrap">Informative images have essential and non-essential elements. <span style="white-space:pre-wrap" id="isPasted">Essential information should have a 3:1 minimum color contrast for large text and 4.5:1 for small text.</span></span></p>

SIM card installation with essential and non-essential elements.

<p>The illustration contains both essential and non-essential information:</p><ol><li>Essential: The text meets all contrast ratios and size requirements</li><li>Essential: An illustrative visual representation of the instructions that follows color contrast guidelines</li><li>Non-essential: The decorative elements create background and personality for the illustration. They do not relay information and do not have to meet Material's contrast requirements.</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj57nfl-11.png?alt=media

## Text truncation

<h2>Text truncation</h2>

<p><span style="white-space:pre-wrap" id="isPasted">Information should always be available to readers, even if text is truncated or wrapped.</span></p>

<h3><span style="white-space:pre-wrap" id="isPasted">Background</span></h3><p><span style="white-space:pre-wrap" id="isPasted">Increased size of text, increased spacing between text, and translation into longer languages shouldn’t result in losing content. This requires designing for text truncation and creating designs flexible enough to accommodate any viewport size or increase in zoom. Some common methods of designing for larger text include text wrapping, increased height or width of components, and truncation with ellipses and hover or link.</span></p>

<h3 id="isPasted">Requirements</h3><p><span style="white-space:pre-wrap" id="isPasted">Content, understandability, and functionality must not be lost when users modify their type settings. There may be exceptions to these requirements for non-Latin alphabet languages.</span></p>

<h3><span style="white-space:pre-wrap" id="isPasted">Text wrapping</span></h3><ul><li><span style="white-space:pre-wrap" id="isPasted">“Wrapped” text extends from one line to another, increasing the height of the text container</span></li><li><span style="white-space:pre-wrap" id="isPasted">Text should be wrapped when it’s critical, to ensure understandability, or when there’s space in the component</span></li></ul>

Body copy  text wrapped  inside a dialogue with an option to expand content.

<p><span style="white-space:pre-wrap">Wrap text, and if it still doesn’t fit, provide a way for users to see more</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5ao0k-18.png?alt=media

Body copy  text wrapped  inside a dialogue, cut off at the bottom, without an option to expand.

<p><span style="white-space:pre-wrap">Don’t cut off text without providing a way for users to view it</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5b36c-19.png?alt=media

<h3>Height and width of components</h3><ul><li><span style="white-space:pre-wrap" id="isPasted">Some components can extend vertically or horizontally for more text</span></li></ul>

Layout of UI- cards of different sizes organized in a stacked grid.

<p><span style="white-space:pre-wrap">Use flexible component containers that change size to fit their content</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5bfye-20.png?alt=media

A stretched UI card  with a small headline and a large photograph. 

<p><span style="white-space:pre-wrap">Avoid setting text size limits that don’t fit the space in a component. Use all space available.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5c5w5-21.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Ellipses with hover or link</span></h3><ul><li><span style="white-space:pre-wrap" id="isPasted">Truncated text can be replaced with an ellipsis if the text is available through a tooltip or link</span></li><li><span style="white-space:pre-wrap" id="isPasted">Links can be used when they’re contained in the text that’s truncated, and when the link displays what's been truncated</span></li><li><span style="white-space:pre-wrap" id="isPasted">If there's an ellipsis, but no way to show the truncated text, it is not accessible</span></li><li><span style="white-space:pre-wrap" id="isPasted">Note that this option can add difficulty for some people</span></li></ul>

A calendar with a cursor hovering  over a day of the week displays a tooltip that reads “Tuesday.”

<p>Use links to reveal truncated text when space is limited, such as the ability to click a linked card to see an expanded view of its text</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5e7k2-GM3-Foundations-WritingAndText-Accessibility-1-v01.mp4?alt=media

On a multiple selection list, the marked checkbox’s label is truncated by an ellipsis.

<p><span style="white-space:pre-wrap">Don’t truncate content without providing users another way to see it</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qvmgvh-24.png?alt=media

## Text resizing

<h2>Text resizing</h2>

<h3>Background</h3><p>People with low vision or those who prefer large text must be able to scale up the size of text in a UI. This adjustment is often performed through a device OS setting or in-app option.</p><p>UIs should support a minimum text increase of 200%.</p>

<p dir="ltr" id="isPasted">Most components behave the same when text is resized:</p><ul><li>Text and line height scale up proportionally, multiplied by scale value</li><li>Padding remains constant at 1x the default size</li><li>Spacing between elements in a component remain constant at 1x the default size</li></ul>

Padding is the same on the top and bottom edges of the buttons.

<p><span style="white-space:pre-wrap">Button text displayed at 1x, 1.3x, and 2x scales. All have top and bottom padding of 8dp.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5gijr-8.png?alt=media

Button text displayed at 1x, 1.3x, and 2x scales. All have left and right padding of 24dp.

Left and right padding remains constant at 24dp as the text size increases.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5gt05-9.png?alt=media

<p>When text resizing isn't controlled by the device OS, offer multipliers such as 1.5x or 2x to allow users to increase the text size. Using multipliers to scale text can result in values with decimals, but this approach is more feasible for implementation.</p><p><span>To calculate a font's size using multipliers, take the </span><strong>default </strong><strong>font size</strong><span> (density = 0) and </span><strong>multiply it by the scale value</strong><span>.</span></p>

Button with label text at 1x and 2x scale.

<p>For example, if a font is 14pt at 1x scale, then the font size should be 28pt when enlarged to 2x scale: (14pt) x (scale value 2) = 28.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5h7wy-10.png?alt=media

<p dir="ltr" id="isPasted">Components that don't include text, like progress indicators, checkboxes, or radio buttons, aren't affected by text resizing.</p>

Icon button with the icon shown at 1x scale and incorrectly at 2x scale.

<p>When designing for text resizing, don't resize components without text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5hl59-11.png?alt=media

Menu with labels at 1x scale.

<p>UI text displayed at 1x</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5hzv6-12.png?alt=media

Menu with labels at 2x scale.

<p>UI text displayed at 2x in which only text and line height is enlarged; the padding between components remains the same as in the 1x UI.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5iftq-13.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Designing for large type</span></h3>

<p><span style="white-space:pre-wrap" id="isPasted">Large type is used regularly by people with low vision and those with difficulty processing written words. They tend to increase text size:<br /></span></p><ul><li><span style="white-space:pre-wrap" id="isPasted">To make it easier to read<br /></span></li><li><span style="white-space:pre-wrap" id="isPasted">To limit interruptions and focus on one task<br /></span></li><li><span style="white-space:pre-wrap" id="isPasted">To avoid overwhelming their senses</span></li></ul><p><span style="white-space:pre-wrap" id="isPasted">Use these methods to design a product to handle large type properly.</span></p>

Menu with labels at 2x scale.

<p>Text that is too small and dense can appear overwhelming and difficult to read</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4bi7b7k-13-b.png?alt=media

Menu with labels at 1x scale.

<p>Larger text can help people focus on one decision at a time and improve understanding</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4bi7fz7-13-a.png?alt=media

<h3>Methods</h3><p>Avoid common text resizing issues by increasing container size, reflowing layout, enabling scrolling, and adding tooltips.</p>

 Side by side of 4 commonly found issues when resizing text up.

<ol><li><span style="white-space:pre-wrap">Unresponsive container; unintentionally clipped text</span></li><li><span style="white-space:pre-wrap">Unresponsive text</span></li><li><span style="white-space:pre-wrap">Overlapping elements</span></li><li><span style="white-space:pre-wrap">Unwanted truncation</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5iwyv-14.png?alt=media

<h4 id="isPasted"><strong>Increase container size</strong></h4><p>Resizing containers can prevent text from overlapping, clipping, or truncating.</p><p>Consider how text might reflow in a way that allows the eye to follow the end of one line to the beginning of the following line.</p><p><br /></p><h4 id="isPasted"><strong>Reflow the layout</strong></h4><p>Consider reflowing the layout, especially when components grow very long. To accommodate larger text, components can be stacked on top of one another, rather than fixed side-by-side.</p>

 left: buttons placed side-by-side. Right: buttons stacked on top of one another.

<ol><li><span style="white-space:pre-wrap">UI displayed at 1x: buttons positioned side-by-side in a standard layout</span></li><li><span style="white-space:pre-wrap">UI displayed at 2x: buttons stacked to fit the limited horizontal width after text is resized</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5jdor-15.png?alt=media

<h4 id="isPasted"><strong>Enable content to scroll</strong></h4><p>When long strings of enlarged text don’t fit on one screen, consider adding a scrollbar to provide access to more content.</p><p>Vertical scrolling is preferable to horizontal. Users should only be asked to scroll in one direction, rather than both vertically and horizontally.</p>

Dialog with a lot of text at 2x size. The text is cut off but accessible when scrolling.

<p>Some screens may not be able to resize and display necessary content. In this situation a scrollbar can be used to access more text.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5ldz9-16.png?alt=media

<h4 id="isPasted"><strong>Use touch &amp; hold tooltips to provide enlarged labels</strong></h4><p>Some components, such as app bars and navigation bars, position text in spaces with stricter space and character limits. In these situations, you can add a tooltip to display enlarged content in the UI.</p><p>In this case, the text size in the component remains displayed at 1x while the scaled up text is displayed in a tooltip on touch &amp; hold.</p><p id="isPasted">Tooltips are the best choice for displaying enlarged text in:  </p><ul><li>Top app bar</li><li>Navigation bar</li><li>Navigation rail</li><li>Tabs, when fixed to the top of a screen and don’t move off-screen upon scrolling</li></ul>

Tooltip on navigation rail displays scaled up label text.

<p>Scale up text in an adjacent tooltip to maintain space in a UI for consuming content.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj5lr50-17.png?alt=media
