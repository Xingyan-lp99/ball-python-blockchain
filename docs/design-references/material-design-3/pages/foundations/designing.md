# Designing

Source: https://m3.material.io/foundations/designing
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/d352451b-8348-4816-abac-4d7983f72f88.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Implement intuitive, accessible layouts, considering structure, color, and flow

## Overview

<p>Designing and implementing accessible product experiences involve a range of considerations. The framework Material uses draws on WCAG standards and industry best practices.</p><p>The three stages described in these tabs help <strong>translate a visual UI into a text-based, linear user experience that maps to code</strong>. Color and contrast also support accessible navigation.</p>

<h3 id="isPasted">Accessibility markup</h3><p>Accessibility markup is an integral part of creating documentation for design specs. </p>

Diagram of switches showing the Tab key changing the focus to the second switch and Space/Enter corresponding to changing the state of the switch. 

<blockquote id="isPasted">1. Switch in the on state with visible focus </blockquote><blockquote>2. Switch in the off state with visible focus</blockquote><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj3q0f4-1.png?alt=media

<h3 id="isPasted">Implementing accessibility</h3><p>By using standard platform controls and semantic HTML (on the web), apps automatically contain the markup and code needed to work well with a platform’s assistive technology. Meeting each platform's accessibility standards and supporting its assistive technology (including shortcuts and structure) gives users an efficient experience.<br id="isPasted" /><br /></p>

A dialog in a UI screen requesting user confirmation to discard calendar event

<p>Use native elements, such as the standard platform dialog</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj3qgpa-12.png?alt=media

A banner requesting user confirmation to discard a calendar event

Be wary of using non-standard elements, such as a non-standard platform dialog to perform a standard dialog task. It requires extra testing to work well with assistive technology.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj3qva4-13.png?alt=media

## Color contrast

<h2 id="isPasted">Color &amp; contrast</h2><p>Color and contrast can be used to help users see and interpret your app’s content, interact with the right elements, and understand actions.</p><p>Color can help communicate mood, tone, and critical information. Primary, secondary, and accent colors can be selected to support usability. Sufficient color contrast between elements can help users with low vision see and use your app.</p>

two colors applied to button container and UI surface with contrast that passes 3:1 minimum

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0quwwby-1.png?alt=media

<h3 id="isPasted">Contrast ratios</h3><p>Color contrast is important for users to distinguish various text and non-text elements. Higher contrast makes the imagery easier to see, while low-contrast images may be difficult for some users to differentiate in bright or low light conditions, such as on a very sunny day or at night.</p><p>Contrast ratios represent how different one color is from another color, commonly written as 1:1 or 21:1. The greater the difference is between the two numbers in the ratio, the greater the difference in relative luminance between the colors. The contrast ratio between a color and its background ranges from 1-21 based on its luminance (the intensity of light emitted) according to the World Wide Web Consortium (W3C).</p><p><strong>The W3C recommends the following contrasts for body text and image text</strong></p><div class="table-wrapper"><table style="width:100%"><thead><tr><th style="text-align:center">Text type</th><th style="text-align:center">Color contrast ratio</th></tr></thead><tbody><tr><th>Large text (at 14 pt bold/18 pt regular and up) and graphics<br /></th><td>At least 3:1 against the background</td></tr><tr><th>Small text<br /></th><td>At least 4.5:1 against the background</td></tr></tbody></table></div><p>Disabled states do not need to meet contrast requirements.</p>

<h3 id="isPasted">Clustering elements</h3><p>Some non-text elements, such as button containers, should meet a contrast ratio of 3:1 between their container color and the color of their background. Consider the following patterns for combining elements and tones, which are grounded in Material's research into contrast and functional changes when elements are combined.</p><p><a href="/m3/pages/color/how-the-system-works#e1e92a3b-8702-46b6-8132-58321aa600bd">Learn more about color contrast for accessibility</a></p>

<p id="isPasted">Elements that are clustered with others, such as a group of buttons, require the user to distinguish each one from the group. </p><p>These elements benefit from 3:1 contrast between themselves and the background.</p>

Two colors applied to button container and UI surface with contrast that fails 3:1 minimum.

<p>The contrast of the button container color against the background color is less than Material's required contrast of 3:1</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qux0kv-2.png?alt=media

Two colors applied to button container and UI surface with contrast that passes 3:1 minimum.

<p>The container color exceeds Material's required minimum contrast of 3:1 against background color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qux3pf-3.png?alt=media

<p>Elements that stand on their own and apart from other elements on the screen, such as a FAB, are already distinguishable to users because of their prominence. These elements don’t benefit from 3:1 contrast between themselves and the background.</p>

Two colors applied to the FAB container and UI surface that fail the minimum contrast of 3:1.

<p>Standalone components, such as FABs, don’t need to meet Material's minimum contrast of 3:1 between the container and background colors because of their prominence</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qux82l-4.png?alt=media

<p>When placing components together in a cluster, use components or types of components that each achieve at least 3:1 contrast between themselves and the background.</p>

A cluster of three buttons with the same container color that fails the minimum contrast of 3:1 with the UI surface.

<p id="isPasted">Each button's container color has less than Material's required minimum contrast of 3:1 against the UI background, leading to poor contrast support for users with low vision<br /></p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj3vo5t-5.png?alt=media

A cluster of three buttons with the same container color that passes the minimum contrast of 3:1 with the UI surface.

<p id="isPasted">Each button's container color has contrast of at least 3:1 against the UI background, leading to better contrast support for users with low vision<br /></p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj3vxr1-6.png?alt=media

## Structure

<h2 id="isPasted">Hierarchy</h2>

<p id="isPasted">When navigation is easy, users understand where they are in your app and what’s important. To emphasize which information is important, multiple visual and textual cues like color, shape, text, and motion add clarity.</p>

<h3 id="isPasted">Types of feedback</h3><p id="isPasted">Visual feedback (such as labels, colors, and icons) and touch feedback show users what is available in the UI.</p>

<h3 id="isPasted">Navigation</h3><p id="isPasted">Navigation can have clear task flows with minimal steps, easy-to-locate controls and clear labeling. Focus control, or the ability to control keyboard and reading focus, can be implemented for frequently used tasks.</p><p>Every added button, image, and line of text increases the complexity of a UI. <strong>Y</strong><strong>ou can simplify how your UI is understood by using:</strong></p><ul><li>Clearly visible elements</li><li>Sufficient contrast and size</li><li>A clear hierarchy of importance</li><li>Key information that is discernable at a glance</li></ul>

<h3 id="isPasted">Levels of importance</h3><p><strong>To convey an item’s relative level of importance:</strong></p><ul><li>Place important actions at the top or bottom of the screen (reachable with shortcuts)</li><li>Place related items of a similar hierarchy next to each other</li></ul>

<h3 id="isPasted">Visual hierarchy</h3><p>To enable the screen reader to read out content in the intended order, it’s important for designers to collaborate with developers – both for writing out the HTML in the correct order, and understanding how screen readers will interpret designs.</p><p>While CSS determines the layout and appearance of a page, screen readers rely on the top-down structure of HTML on any platform (mobile or web). This structure creates a map for the screen reader to follow when reading the content.</p>

Example of a mobile app using 4 content cards in a 2 by 2 grid. They reading order is top left, to top right, then bottom left, then bottom right.

<p>An example of how content hierarchy in a screen can be identified in a logical reading order to optimize for the ways assistive tech, such as screen readers, may interpret information</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj3y443-1.png?alt=media

<h2 id="isPasted">Web landmarks and headings</h2>

<p><strong>Define content and UI layout to improve navigation and comprehension.</strong></p><p>Assistive technologies (AT) rely on clear, delineated structures to process page information, navigating primarily through the use of headings and landmarks. Many assistive technologies, such as screen readers, translate a design into a linear experience, which means that many users interact with content in hierarchical, predetermined order. Therefore, thinking through structural decisions in advance can improve the accessibility of a product.</p>

<p id="isPasted"><strong>For web only</strong>: Landmarks and headings help assistive-technology users orient themselves to a web page and allow for easy navigation and traversal across large sections of a document or page. </p><p>By <strong>classifying and labeling sections of a page</strong>, structural information that is conveyed visually through layout design can also be represented in code.</p>

Diagram of a website, showing different regions and their associated landmarks and headings.

<p>Example of a page diagram mapping the areas for a UI in order to consider the relative landmarks and headings</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj3ys8l-2.png?alt=media

<h3 id="isPasted">Identifying landmarks and headings</h3>

<h4 id="isPasted"><strong>1. Define landmarks </strong></h4><p>Landmarks are large blocks of content that establish the high-level structure of your layout. They're a set of Accessible Rich Internet Applications (ARIA) roles that provide easy access to, and important meaning for, common content areas of a web page. </p><p>There are eight landmark roles: <strong>navigation, search, main, banner, complementary, contentinfo, region, and form</strong>. </p><p>The eight landmark roles in the W3C ARIA guidelines include:</p><ol><li><strong>Navigation</strong>: Contains lists of navigation links (there can be multiple, in which case you should differentiate in label)</li><li><strong>Search</strong>: A search field</li><li><strong>Main</strong>: The main content area as defined by UX. There should be only one.</li><li><strong>Banner</strong>: Typically the header; content repeated from page to page, often contains navigation and toolbars. There should be only one.</li><li><strong>Complementary</strong>: A sidebar or aside to main content that can stand alone without the main content</li><li><strong>Contentinfo</strong>: Typically the footer; contains information describing the site and its content (for example,  copyright). There should be only one.</li><li><strong>Region</strong>: Content regions are important content blocks. They can be nested inside the “main” landmark. Regions should be labeled with names that make the purpose of that region clear. </li><li><strong>Form</strong>: Takes and stores user info.</li></ol>

<h4 id="isPasted"><strong>Add accessibility labels </strong></h4><p>Add <strong>clear and specific labels</strong> to any landmark roles that appear multiple times (regions or navigation typically). This will help users differentiate information. </p><p>Labels should be added to <strong>all regions</strong>, as well as any landmark where a label will enhance meaning. For example, explaining the contents or purpose of a sidebar. </p><p><strong>Don't repeat the landmark role within a label</strong>.</p>

Diagram labeling two regions with a navigation role with the labels primary and pagination

This layout has two areas assigned the navigation role. Each landmark should get a unique label to help users tell the difference between elements.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj3z6py-3.png?alt=media

<h4 id="isPasted"><strong>2. Define headings</strong></h4><p>Assistive technology users often navigate web pages with the help of headings. They create a clear hierarchy to help users navigate and take action.</p><ul><li>Identify headings based on content hierarchy, rather than visual styling</li><li>Headings should not skip a level, for example, don't go from H2 to H4 without using an H3 </li><li>Map content on your pages to headings (H1–H6) in sequential order based on the hierarchy of your content</li><li>A single H1 for the page title is recommended</li></ul>

Diagram labeling different headings

Example of headings marked up in code

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj3znk9-4.png?alt=media

<h4 id="isPasted"><strong>Consider hierarchy in addition to style</strong></h4><p><strong>Ensure that headings correspond with meaningful titles</strong>. If they don't, consider changing the titles in the UI to benefit the experience of all users or adding a label for assistive tech.</p><p>Heading levels are informed by the layout's information architecture—the structural hierarchy that’s applied to a set of items. The page’s visual styling does not need to match the heading levels in terms of prominence and visual hierarchy.</p>

<h2>Target sizes</h2>

<p id="isPasted">Material Design’s target guidelines can help users who aren’t able to see the screen, or who have difficulty with small touch targets, to tap elements in your app.</p>

Target guidelines on buttons for easy accessibility.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj401i4-2.png?alt=media

<h3 id="isPasted">Touch and pointer target sizes</h3><p>Touch targets are the parts of the screen that respond to user input, extending beyond the visual bounds of an element. For example, an icon may appear to be 24 x 24dp, but the padding surrounding it comprises the full 48 x 48dp touch target.</p><p>For most platforms, consider making touch targets at least 48 x 48dp. A touch target this size results in a physical size of about 9mm, regardless of screen size. The recommended target size for touchscreen elements is 7-10mm. It may be appropriate to use larger touch targets to accommodate a larger spectrum of users.</p><p>Note: iOS recommends 44 x 44dp targets. </p>

A row of four 24dp icons and one 40dp icon

<p id="isPasted">Icons: 24dp</p><p>Star icon: 40dp</p><p>Touch target on both: 48dp</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qv75bo-3-3p.png?alt=media

<h3 id="isPasted">Pointer targets</h3><p>Pointer targets are similar to touch targets, but are implemented by motion-tracking pointer devices such as a mouse or a stylus. </p><p>Consider making pointer targets minimums 44 x 44dp.</p>

A row of four icon buttons in the bottom app bar.

Recommended target size for pointers: 44dp

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qv7adh-5.png?alt=media

<h3 id="isPasted">Target spacing</h3><p>In most cases, targets separated by 8dp of space or more promote balanced information density and usability.</p>

Three icons in a row with 48dp touch target size and three icons in a row with 8dp padding between icons.

<p id="isPasted">Two groups of icons showing their overall spacing and the spacing between each other</p><p>Touch target size: 48dp</p><p>Padding: 8dp</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qv7efk-6.png?alt=media

## Flow

<h2 id="isPasted">Focus order &amp; key traversal</h2><p>People should be able to navigate and interact with your app without the use of a traditional mouse or touch screen. To support navigation by keyboard, screen reader, or other assistive technology, goals should be achievable by using <strong>tab</strong>, <strong>arrow</strong>, <strong>and other common navigation keys</strong>. </p><p>Simplify your flows by: </p><ul><li>strategically ordering tab stops </li><li>reducing overall page complexity</li></ul>

<h3>Use defaults</h3>

<p>Avoid adding more work for yourself by using <strong id="isPasted">predefined tab ordering,</strong> unless a user journey needs special tailoring. The <strong>default order follows the DOM</strong> (the order of content as it's written in the source code) and <strong>generally flows from left to right</strong>; <strong>top to bottom</strong>. Keyboard navigation (key traversal) may be pre-defined within common components. Use the defaults unless you have a UX pattern or custom component that breaks from the default pattern.</p>

<h3>Determining user flows</h3>

<h4 id="isPasted"> <strong>1. Group product use cases</strong></h4><p>Group product use cases into primary and secondary user journeys. The priority of your use cases should influence the decisions you make about the priority of user flows.</p>

<h4 id="isPasted"><strong>2. Define initial focus and component-level focus</strong></h4><p>Focus refers to which control is currently the active target of user interactions, such as mouse clicks or keyboard taps. Generally, the <strong>tab</strong> key moves focus between interactive elements. </p><p>Define the <strong>initial focus</strong> when a user loads a screen, as well as initial focus for components with multiple interactive elements, like a complex card or a dialog.</p>

A Google home screen showing the initial focus on the search bar.

<p>In the case of the Google homepage, even though there are links and buttons above and surrounding the search field on the page, it makes sense to put the user's initial focus on the element that supports the most common user goal</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0qvgj8o-5.png?alt=media

<p id="isPasted">Focus is particularly important when an element is activated by the user or the user changes context. </p><p>For example, when a dialog is triggered, check for the following:</p><ul><li>Focus is set to the dialog component, likely to a specific interactive element within the dialog such as a text input field or edit button</li><li>When the user closes or cancels the dialog, focus returns to the interactive element that initiated the action</li></ul>

Diagram showing changing points of focus as a user opens and closes a calendar card.

<ol><li>Define initial focus and component-level focus</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj43qm4-6.png?alt=media

<h4 id="isPasted"><strong>3. Define any atypical key traversal through the page and components</strong></h4><p>Users should be able to complete the primary and secondary user journeys using tab, arrow keys, and other keyboard shortcuts. </p>

Card with three interactive elements in the top right corner.

Navigating the interactive elements on a card via tab 

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj441r3-7.png?alt=media

<p id="isPasted"><strong>Tab</strong> typically moves focus between interactive elements and is often used as primary navigation. <strong>Tab +</strong> <strong>Shift</strong> reverses direction.</p><p><strong>Arrow keys</strong> are typically used to navigate within components (for example, moving between cells in a form or traversing items in a menu.)</p><p><strong>Enter</strong> activates a link or button, or sends a form when a form item has focus.</p>

Diagram showing a group of three sub-elements, with navigation within the group assigned to arrow keys.

<p>In the case of unique layouts and use cases, it can help to group a collection of interactive elements as one tab stop, and use arrow keys to traverse sub-elements</p><ol><li>Using Tab navigation to focus group</li><li>Using arrrow key to traverse sub-elements</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj44h3h-8.png?alt=media

<h2>Keyboard shortcuts</h2>

<p><span style="white-space:pre-wrap">Keyboard shortcuts help users access menus and app functions without using a mouse on desktop apps and websites.</span></p>

<h3 id="isPasted">Requirements</h3><p><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">These requirements are important for helping speech users avoid activating multiple shortcuts at once and for keyboard-only users to minimize unwanted actions.</span></span></p><ul><li>Keyboard shortcuts should use a combination of two or more keys by default.</li><li>Include a tutorial, list, or help center page of all custom keyboard shortcuts in your product. For example, Cmd+Z (Ctrl+Z) to undo deleting an event in Google Calendar.</li><li><span style="white-space:pre-wrap">If a keyboard shortcut is activated with a single key, provide users with a way to take at least one of these actions:</span><ul><li><strong>(Most preferred) </strong>Remap the shortcut to include one or more non-printable keyboard keys.</li><li><strong>(Preferred)</strong> Activate the shortcut only when a relevant component is focused.</li><li><strong>(Not preferred, only use as a temporary solution)</strong> Turn off the keyboard shortcut.</li></ul></li></ul>

## Elements

<h2>Labeling elements</h2>

<p>Elements can be defined and labeled to enhance understanding of their function and reduce confusion for those navigating with assistive technology. Add accessibility labels to define roles and indicate decorative elements.</p>

<h3 id="isPasted">Visual elements that need labels</h3><ul><li id="isPasted">Interactive icons or buttons with no visible text or not enough context in the text (for example, an edit button with a pencil icon)</li><li>Interactive images</li><li>Visual cues (including progress bars and error handling)</li><li>Meaningful icons (such as status icons)</li><li>Meaningful images (for example, diagrams, substantive photos, and illustrations)</li></ul>

<h3 id="isPasted">Text elements need labels to add additional context</h3><ul><li>Generic links (for example, "Learn more")</li><li>Buttons with generic text (for example, "Save" when there are multiple such buttons on a page)</li></ul>

<h3 id="isPasted">Elements that do not need labels</h3><ul id="isPasted"><li id="isPasted">Non-interactive UI text, as this will be automatically read by the screen reader</li><li>Buttons with sufficient text (for example, "Download image")</li></ul>

<h3 id="isPasted">Do not include the element name in labels</h3><p id="isPasted">Do not use an element role (for example, button or menu) in your label. This identifier is automatically added when the element is assigned its proper role, typically by a developer.</p>

<h3 id="isPasted">Label language style</h3><p>This article uses the general term accessibility label to refer to several different types, including ARIA labels and alt tags. When accessibility labels are implemented in code, they'll be translated to the appropriate type for the intended platform. Additionally, the term <strong>role</strong> is used to cover both general component control types and ARIA roles for web apps. <a href="/m3/pages/alt-text">Learn more about writing alt text</a></p>

<h3>How to add labels</h3>

<h4 id="isPasted"><strong>1. Label elements</strong></h4><p><a href="/m3/pages/alt-text">Accessibility labels</a> assist users who cannot rely on a product's visual interface. Thoughtful labels help make the text-based experience as usable as the visual experience. Labels should concisely describe an element's content, purpose and behavior. </p>

Diagram showing the labels and roles assigned to on-screen icon buttons.

Example: The accessibility labels for these icons describe their purpose—NOT what the icon looks like (for example, "magnifying glass")

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm5r5d64m-9%20(1).png?alt=media

<h4 id="isPasted"><strong>2. Add labels for meaningful images and interactive elements</strong></h4><p>Add labels to visuals that convey meaning or enhance content. </p><p><strong>Labels should be concise, descriptive, and convey the content and context of the image.</strong></p><p>This applies to infographics and other instructive images found in support docs. </p>

A microphone icon with the accessibility label "Voice Search."

<p>The label “voice search” describes the user task (search) paired with the input method (voice)</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm5r5dvfi-10%20(1).png?alt=media

A microphone icon with the accessibility label "Microphone."

Don't include the element type (button, menu, etc.) in your label. This will automatically be added by assigning the element the proper role. 

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwj47jj9-11.png?alt=media

<h4 id="isPasted"><strong>Hiding images</strong></h4><p>Decorative icons and images that don't enhance the experience for a visually-impaired user should be annotated as decorative in order to hide them in code. </p>

Group of icons in a menu collectively described by the accessibility label N/A Hide Images.

Mark decorative visual elements to "hide"

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm5r5epn6-12.png?alt=media

<h4 id="isPasted"><strong>3. Assign a role to interactive elements</strong></h4><p style="box-sizing:border-box;font:400 1rem / 1.5rem">ARIA roles apply to web apps and specify how to increase the accessibility of web pages on top of HTML. </p><ul><li style="box-sizing:border-box;font:400 1rem / 1.5rem">For web, assign ARIA roles for all interactive elements </li><li style="box-sizing:border-box;font:400 1rem / 1.5rem">For non-web, assign roles based on your design system components (button, slider, menu, etc.)</li></ul><p>Assign ARIA roles (web) or component type (mobile) to communicate desired interaction patterns into engineering action. Note that some visual elements may look the same, but are intended to behave differently. </p><p>Defining an interactive element's category by assigning it a role helps users of assistive technology establish expectations for how to interact with that element and anticipate what is likely to happen upon interaction.</p>

Element with the label "Got it button" and the role "Button."

<p>Don't include the control type in the label. Screen readers automatically add the control, so you’d be having it repeat (for example, “Got it button button”).</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwkb4332-13.png?alt=media
