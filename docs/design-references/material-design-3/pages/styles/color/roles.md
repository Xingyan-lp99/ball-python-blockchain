# Color roles

Source: https://m3.material.io/styles/color/roles
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/ced25aa3-a367-44c6-a47e-439bc9e59d68.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

There are 26 standard color roles organized into six groups: primary, secondary, tertiary, error, surface, and outline

## Tab 1

<h2>What are color roles?</h2><p>Color roles are like the "numbers" in a paint-by-number canvas. They're the connective tissue between elements of the UI and what color goes where.</p><ul><li><strong>Color roles are mapped to Material Components</strong><br />You'll use these color roles whether you're using the static <app-froala-tooltip-element description="Baseline is the default static color scheme for Material products. It includes colors for both light and dark themes." link-label="More on baseline color" link-url="/m3/pages/static/baseline" should-open-link-in-new-tab="true">baseline scheme</app-froala-tooltip-element> or <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element>. If your product contains custom components, they'll need to be properly mapped to this set of color roles.</li><li><strong>Color roles ensure accessibility</strong><br />The color system is built on <app-froala-tooltip-element description="For example, a dark surface color is algorithmically paired with a light text label color so the UI automatically meets contrast requirements." link-label="More on color relationships" link-url="/m3/pages/color/how-the-system-works#e1e92a3b-8702-46b6-8132-58321aa600bd" should-open-link-in-new-tab="true">accessible color pairings</app-froala-tooltip-element>. These color pairs provide an accessible minimum 3:1 contrast.</li><li><strong>Color roles are tokenized</strong><br />Roles are implemented in design and code through tokens. A <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design token</app-froala-tooltip-element> represents a small, reusable design decision that’s part of a design system's visual style.</li></ul>

Example color swatches for all 45 color roles including Primary, Secondary, Tertiary, Error, Surfaces, Inverse roles, Scrim and Shadow roles.

<p>Diagram of all Material color roles, including optional add-on roles for surface colors and fixed accent colors</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2ms4t2-1.png?alt=media

<h2>General concepts</h2><p>Here are helpful-to-know words you'll see in the names of color roles:</p><ul><li><strong>Surface </strong>– A role used for backgrounds and large, low-emphasis areas of the screen.</li><li><strong>Primary, Secondary, Tertiary</strong> – Accent color roles used to emphasize or de-emphasize foreground elements.</li><li><strong>Container</strong> – Roles used as a fill color for foreground elements like buttons. They should not be used for text or icons.</li><li><strong>On</strong> – Roles starting with this term indicate a color for text or icons <em>on top</em> of its paired parent color. For example, <strong>on primary</strong> is used for text and icons against the <strong>primary</strong> fill color.</li><li><strong>Variant</strong> – Roles ending with this term offer a lower emphasis alternative to its non-variant pair. For example, <strong>outline variant </strong>is a less emphasized version of the <strong>outline </strong>color.</li></ul>

<h3>Pairing and layering colors</h3><p>To ensure accessible visual contrast in your app, apply colors only in the intended pairs or layering orders described in the following sections.</p><p>Combining colors improperly may break contrast necessary for visual accessibility, particularly when colors are adjusted through <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element> features such as <app-froala-tooltip-element description="User-controlled contrast is a dynamic color feature enabling users to choose from one of three levels of color contrast: standard, medium, and high." link-label="More on user-controlled contrast" link-url="/m3/pages/color/how-the-system-works/#a360c176-b99e-4804-8034-9884833009c8" should-open-link-in-new-tab="true">user-controlled contrast</app-froala-tooltip-element>.</p>

Pair of buttons shown at three different contrast levels. At every level, the text on the button is legible because the color roles are properly applied to the buttons.

<p>Pair and layer color roles as intended to ensure expected visual results and accessibility. In this example, the two buttons mapped with (1) <strong>primary</strong>, (2) <strong>on primary</strong>, (3) <strong>secondary container</strong>, and (4) <strong>on secondary container</strong> stay legible as the contrast level changes.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2msstb-2.png?alt=media

Pair of buttons shown at 3 different contrast levels. The text on the button becomes illegible because the color roles are improperly applied to the buttons.

<p>Improper color mappings can produce unintended visual results and break accessibility. In this example, the two buttons mapped with (1) <strong>primary</strong>, (2) <strong>primary container</strong>, (3) <strong>secondary container</strong>, and (4) <strong>on surface</strong> become illegible as the contrast level changes.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2mt0z5-3.png?alt=media

<h2><span style="white-space:pre-wrap" id="isPasted">Accent color roles</span></h2>

<p><span style="white-space:pre-wrap" id="isPasted">Accent color roles include primary, secondary, and tertiary. Assign them to elements in the UI based on importance and needed emphasis. Use caution when changing color roles for visual effect.</span></p>

<ul><li><p><strong>Primary roles</strong> are for important actions and elements needing the most emphasis, like a FAB to start a new message.<br /></p></li><li><p><strong>Secondary roles</strong> are for elements that don’t need immediate attention and don’t need emphasis, like the selected state of a navigation icon or a dismissive button.<br /></p></li><li><p><strong>Tertiary roles </strong>are for smaller elements that need special emphasis but don't require immediate attention, such as a badge or notification.</p></li></ul>

A mail app showing a mix of primary, secondary, and tertiary accent colors used across the screen.

<ol class="decimal"><li><span style="white-space:pre-wrap">Primary colors are used for the most important elements, like a starred message and FAB to start a new message<br /></span></li><li><span style="white-space:pre-wrap">Tertiary colors are used for smaller emphasized elements, like a badge suggesting a follow up<br /></span></li><li><span style="white-space:pre-wrap">Secondary colors are used for less urgent elements, like the background of an inactive star icon and the selection state of an inbox icon</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm7atpmau-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/zBAGamdJZfsDyiTUOll5jETI5pAQCimbOVfWX3IOqit-JKa_213YRHjLwhlcDDFt5CE5ACu6NDc_jAO3EWPiQ0hhV_jAnipweoAiUcZ8OyU=s1352

<h2>Primary</h2>

<p id="isPasted"><span>Use primary roles for the most prominent components across the UI, such as the FAB, high-emphasis buttons, and active states.</span></p>

<ul><li><p><strong>Primary:</strong> High-emphasis fills, texts, and icons against surface<br /><br /></p></li><li><p><strong>On primary:</strong> Text and icons against primary<br /><br /></p></li><li><p><strong>Primary container:</strong> Standout fill color against surface, for key components like FAB<br /><br /></p></li><li><p><strong>On primary container: </strong>Text and icons against primary container</p></li></ul>

4 color swatches: primary, on primary, primary container and on primary container.

<p>Primary color roles include <strong>primary</strong> and <strong>primary container</strong>, with their respective “On” colors</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2mtbil-4.png?alt=media

Primary color used for filled button, and "on primary" color used for the text within that button.

<ol><li>On primary </li><li>Primary</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2muo2k-5.png?alt=media

"Primary container" color used for FAB and "on primary container" color used for the text and icon within.

<ol class="decimal"><li>On primary container </li><li>Primary container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2kwfth2-6.png?alt=media

<h2>Secondary</h2>

<p id="isPasted"><span>Use secondary roles for less prominent components in the UI such as filter chips.</span></p>

<p id="isPasted"><span>There are four secondary roles:</span></p><ul><li><strong>Secondary:</strong> Less prominent fills, text, and icons against surface<br /><br /></li><li><strong>On secondary:</strong> Text and icons against secondary<br /><br /></li><li><strong>Secondary container:</strong> Less prominent fill color against surface, for recessive components like tonal buttons<br /><br /></li><li><strong>On secondary container:</strong> Text and icons against secondary container</li></ul>

4 color swatches: secondary, on secondary, secondary container, and on secondary container.

<p>Secondary color roles include <strong>secondary</strong> and <strong>secondary container</strong>, with their respective "On" colors</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2mvccz-7.png?alt=media

An icon button using "secondary container" color, and an icon using "on secondary color."

<ol><li>Icon: On secondary container </li><li>Button: Secondary container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2mvlj0-8.png?alt=media

<h2>Tertiary</h2>

<p id="isPasted"><span>Use tertiary roles for contrasting accents that balance primary and secondary colors or bring heightened attention to an element such as an input field. </span></p>

<p>There are four tertiary roles:</p><ul><li><strong>Tertiary:</strong> Complementary fills, text, and icons against surface<br /><br /></li><li><strong>On tertiary:</strong> Text and icons against tertiary<br /><br /></li><li><strong>Tertiary container:</strong> Complementary container color against surface, for components like input fields<br /><br /></li><li><strong>On tertiary container: </strong>Text and icons against tertiary container</li></ul>

4 color swatches: tertiary, on tertiary, tertiary container, and on tertiary container.

<p>Tertiary color roles include <strong>tertiary</strong> and <strong>tertiary container</strong>, with their respective "On" colors</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2mzjt8-9.png?alt=media

<p>The tertiary color roles can be applied at the designer's discretion. They're intended to support broader color expression.</p>

A selected element using Tertiary Container as a background color and On Tertiary Container for text. 

<ol><li>On tertiary container</li><li>Tertiary container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n0pba-10.png?alt=media

<h2>Error</h2>

<p style="box-sizing:border-box;font:400 16px / 1.5rem">Use error roles to communicate error states, such as an incorrect password entered into a text field.</p>

<p style="box-sizing:border-box;font:400 16px / 1.5rem">There are four error roles:</p><ul><li style="box-sizing:border-box;font:400 16px / 1.5rem"><strong>Error:</strong> Attention-grabbing color against surface for fills, icons, and text, indicating urgency<br /><br /></li><li style="box-sizing:border-box;font:400 16px / 1.5rem"><strong>On error:</strong> Text and icons against error<br /><br /></li><li style="box-sizing:border-box;font:400 16px / 1.5rem"><strong>Error container:</strong> Attention-grabbing fill color against surface<br /><br /></li><li style="box-sizing:border-box;font:400 16px / 1.5rem"><strong>On error container:</strong> Text and icons against error container</li></ul><p style="box-sizing:border-box;font:400 16px / 1.5rem">Error is an example of a static color (it doesn't change even in dynamic color schemes). Error color roles are made static by default with any dynamic color scheme. They still adapt to light and dark theme.</p>

4 color swatches: Error, On error, Error container and On error container roles.

<p>Error color roles include <strong>error</strong> and <strong>error container</strong> with their respective "On" colors.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n10jv-11.png?alt=media

<h2>Surface</h2>

<p>Use surface roles for more neutral backgrounds, and container colors for components like cards, sheets, and dialogs.</p>

<p>There are three surface roles:</p><ul><li><strong>Surface: </strong>Default color for backgrounds<br /><br /></li><li><strong>On surface:</strong> Text and icons against any <strong>surface</strong> or <strong>surface container </strong>color<br /><br /></li><li><strong>On surface variant:</strong> Lower-emphasis color for text and icons against any <strong>surface</strong> or <strong>surface container</strong> color</li></ul>

3 color swatches: Surface, On surface and On surface variant.

<p><strong>Surface</strong> and <strong>on surface</strong> roles in light theme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n1cbu-12.png?alt=media

<p>There are also five surface container roles named based on their level of emphasis:</p><ul><li><p><strong>Surface container lowest:</strong> Lowest-emphasis container color<br /><br /></p></li><li><p><strong>Surface container low:</strong> Low-emphasis container color<br /><br /></p></li><li><p><strong>Surface container:</strong> Default container color<br /><br /></p></li><li><p><strong>Surface container high:</strong> High-emphasis container color<br /><br /></p></li><li><p><strong>Surface container highest:</strong> Highest-emphasis container color</p></li></ul><p><strong>Surface container</strong> is the default role, but the others are especially helpful for creating hierarchy and nested containers in <a href="/m3/pages/breakpoints/expanded" target="_blank">layouts for expanded screens</a>.</p>

4 color swatches in light and dark theme: Surface container lowest, Surface container low, Surface container, Surface container high and Surface container highest.

<p>The five <strong>surface container</strong> roles, shown in light and dark theme</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2njabe-GM3-Styles-Color-Color_roles-1-v01.mp4?alt=media

<p>The most common combination of surface roles uses <strong>surface</strong> for a background area and <strong>surface container</strong> for a navigation area.</p><p>Text and icons typically use <strong>on surface </strong>and<strong> on surface variant </strong>on all types of surfaces.</p>

Email app using Surface for the main background color and Surface Container for the navigation bar background

<ol><li id="isPasted">Surface</li><li>Surface container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n20l4-14.png?alt=media

<p>All color mappings – but especially surface colors – should remain the same for layout regions across <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element>. For example, the body area will use the <app-froala-tooltip-element description="Color role used for the default color for backgrounds." link-label link-url should-open-link-in-new-tab="false"><strong>surface</strong></app-froala-tooltip-element> color and the navigation area will use the <app-froala-tooltip-element description="Default color role used for container color." link-label link-url should-open-link-in-new-tab="false"><strong>surface container</strong></app-froala-tooltip-element> color on both mobile and tablet.</p>

Mobile and tablet screens both using Surface for main background and surface container for navigation background.

<ol><li id="isPasted">Surface</li><li>Surface container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n2btl-15.png?alt=media

<p>Depending on necessary hierarchy, feature area, and design logic, you can use <a href="/m3/pages/color-roles/tab-1#63d6db08-59e2-4341-ac33-9509eefd9b4f">add-on surface colors</a> in larger window class sizes as long as colors are consistently applied.</p>

Mobile, foldable, and tablet screens showing how the body and navigation regions have the same color roles across window sizes.

<p>In this example, the body and navigation regions have the same color roles across breakpoints (<strong>surface</strong> and <strong>surface container</strong>, respectively) with the addition of other surface container colors at larger sizes.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2nit0j-GM3-Styles-Color-Color_roles-2-v01.mp4?alt=media

<p><span>By default, neutral-colored components such as navigation bars, menus, or dialogs are mapped to specific surface container roles, but these </span><span><a href="/m3/pages/advanced/overview" target="_blank" rel="noopener noreferrer">roles can be remapped</a></span><span> by makers to suit user needs.</span></p>

Surface container low applied to an elevated button and card, surface container applied to the top and bottom bar, surface container high applied to the FAB and basic dialog, surface container highest applied to an input label and off switch.

<p id="isPasted">Default surface container roles applied to components:</p><ol><li style="font-weight:bold"><strong>Surface container low</strong></li><li style="font-weight:bold"><strong>Surface container </strong></li><li style="font-weight:bold"><strong>Surface container high</strong></li><li style="font-weight:bold"><strong>Surface container highest</strong></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n2wcp-17.png?alt=media

<h3 id="isPasted">Inverse colors</h3><p>Inverse roles are applied selectively to components to achieve colors that are the reverse of those in the surrounding UI, creating a contrasting effect.</p><ul><li><strong id="isPasted">Inverse surface: </strong>Background fills for elements which contrast against surface<br /><br /></li><li><strong>Inverse on surface:</strong> Text and icons against inverse surface<br /><br /></li><li><strong>I</strong><strong>nverse primary:</strong> Actionable elements, such as text buttons, against inverse surface</li></ul>

3 color swatches: Inverse surface, inverse on surface and inverse primary roles.

<p><span style="white-space:pre-wrap"><strong>Inverse surface</strong>, <strong>inverse on surface</strong>, and <strong>inverse primary</strong> roles in the color scheme, shown in light theme</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n4uvc-24.png?alt=media

Snackbar component using inverse surface for its background, inverse on surface for its text and inverse primary of its text button, shown in light theme

<p id="isPasted">A snackbar which uses:</p><ol><li><strong>Inverse surface</strong> for its background</li><li><strong>Inverse on surface</strong> for its text</li><li><strong>Inverse primary</strong> for its text button</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n6f78-25.png?alt=media

<h2>Outline</h2>

<p>There are two outline colors to be used against a surface:</p><ul><li><strong>Outline:</strong> Important boundaries, such as a text field outline<br /><br /></li><li><strong>Outline variant:</strong> Decorative elements, such as dividers, and when other elements provide 4.5:1 contrast</li></ul>

2 color swatches: Outline and outline variant

<p><strong>Outlin</strong><strong>e</strong> and <strong>outline variant</strong> roles in the color scheme, shown in light theme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n6s89-18.png?alt=media

Diagram comparing used of outline and outline variant.

<ol><li id="isPasted">A text field which uses <strong>outline </strong>for its container border</li><li>A list item which uses <strong>outline variant</strong> for its divider line</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n7081-19.png?alt=media

Outline color incorrectly used for dividers

<p>Don’t use the <strong>outli</strong><strong>ne</strong> color for dividers since they have different contrast requirements. Instead, use <strong>outline variant</strong>. </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n7i8q-20_dont.png?alt=media

Outline color incorrectly used for cards.

<p>Don’t use the <strong>outline</strong> color for components that contain multiple elements, such as cards. Instead, use <strong>outline variant</strong>. </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n7yd0-21_dont.png?alt=media

Outline variant color incorrectly used for input and filter chips.

<p>Don’t use the <strong>outline variant</strong> color to create visual hierarchy or define the visual boundary of targets. Instead, use the <strong>outline</strong> color or another color providing 3:1 contrast with the surface color.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm38uvq2h-23_dont.png?alt=media

Outline variant incorrectly color used for chips.

<p>The <strong>outline variant</strong> color can be used for the border of targets like chips and buttons, provided that those targets contain elements inside them that provide visual contrast. In this example of chips and buttons, the icons and text inside the targets meet 4.5:1 contrast.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4iofvjf-23_caution.png?alt=media

<h2>Add-on color roles</h2>

<p>Most products won't need to use these add-on color roles. However, some products require the greater flexibility and control that add-on roles provide. If you aren't sure whether your product should use the add-on roles, it probably shouldn't and you can ignore them.</p>

<h3 id="isPasted"><span style="white-space:pre-wrap">Fixed accent colors</span></h3><p><strong>Primary fixed, secondary fixed, </strong>and <strong>t</strong><strong>ertiary fixed</strong> are fill colors used against surface. These colors maintain the same tone in light and dark themes, as opposed to regular container colors, which change in tone between these themes. The fixed color role may be used instead of the equivalent container role in situations where such fixed behavior is desired.</p><p>The <strong>primary fixed dim</strong>, <strong>secondary fixed dim</strong>, and <strong>tertiary fixed dim</strong> roles provide a stronger, more emphasized tone relative to the equivalent fixed color. They may be used where a deeper color but the same fixed behavior is desired.</p>

6 color swatches: Primary, secondary and tertiary fixed swatches, along with their darker Dim counterparts, shown in both light and dark theme.

<p><strong>Fixed</strong> and <strong>fixed dim</strong> color roles for the <strong>primary</strong>, <strong>secondary</strong>, and <strong>tertiary</strong> color groups, shown in both light and dark themes. Note how the colors stay the same between themes.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n8qum-26.png?alt=media

FAB in light and dark theme, using the primary fixed role for its container fill color.

<p>A FAB which uses <strong>primary fixed</strong> (1) for its container fill color, shown in light and dark themes. Note how the container color stays the same between themes.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n922v-27.png?alt=media

FAB in light and dark theme, using the primary container role for its container fill color.

<p>For comparison, a FAB which uses <strong>primary container</strong> (2) for its container fill color, shown in light and dark themes. Note how the container color changes tone between themes.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n9b76-28.png?alt=media

2 email app screens using primary fixed and primary fixed dim.

<p id="isPasted">Examples of fixed and fixed dim colors in use:</p><ol><li><strong>Primary fixed</strong> for a FAB container color</li><li><strong>Primary fixed dim</strong> for an icon button container</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n9m0g-29.png?alt=media

Permissions screen with Surface used for the background and Primary Fixed incorrectly used for the button fill.

<p id="isPasted">Fixed colors don't change based on light or dark theme, so they're likely to cause contrast issues. Avoid using them where contrast is necessary.<br /></p><p id="isPasted"><br /></p><p id="isPasted"><br /></p><p><br /></p><p><br /></p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2n9vnb-30_dont.png?alt=media

Permissions screen with Surface used for the background and Primary correctly used for the button fill.

<p id="isPasted">Use <strong>primary</strong>, <strong>secondary</strong>, and <strong>tertiary</strong> roles for accent colors where contrast is needed</p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2na1i9-31_do.png?alt=media

<h3>On fixed accent colors</h3><p id="isPasted"><strong>On fixed</strong> colors are used for text and icons which sit on top of the corresponding Fixed color. For example, <strong>on </strong><strong>primary fixed </strong>is used for text and icons against the <strong>primary fixed </strong>color. The same usage applies for the equivalent secondary and tertiary colors.</p><p><br /></p><p><strong>On fixed variant</strong> colors are used for text and icons needing lower emphasis against the corresponding fixed color. For example, <strong>on primary fixed variant </strong>is used for low emphasis text and icons against the <strong>primary fixed </strong>color. The same usage applies for the equivalent secondary and tertiary colors.</p>

6 color swatches for on fixed and on fixed variant

<p><strong>On fixed</strong> and <strong>on fixed variant</strong> color roles for the <strong>primary</strong>, <strong>secondary</strong>, and <strong>tertiary</strong> accent groups, shown in both light and dark themes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2nacto-32.png?alt=media

Banner in a news app using on primary fixed variant and on primary fixed

<p>A customized banner which uses <strong>on primary fixed variant</strong> (1) for its deemphasized text and (2) <strong>on primary fixed</strong> for its emphasized text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2nappf-33.png?alt=media

<h3 id="isPasted">Bright and dim surface roles</h3><p>There are two add-on surface roles:</p><ul><li><strong>Surface dim:</strong> Dimmest surface color in light and dark themes</li><li><strong>Surface bright:</strong> Brightest surface color in light and dark themes</li></ul>

3 color swatches: Surface dim, surface, and surface bright

<p><strong id="isPasted">Surface dim</strong>, <strong>surface</strong>, and <strong>surface bright</strong> in light theme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2nb208-34.png?alt=media

3 color swatches: Surface dim, surface, and surface bright

<p><strong>Surface dim</strong>, <strong>surface</strong>, and <strong>surface bright</strong> in dark theme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2nbbzl-35.png?alt=media

<p>While the default <strong>surface</strong> color automatically inverts between light and dark themes (it’s a light color in light theme and it flips to a dark color in dark theme), the <strong>surface bright</strong> and <strong>surface dim</strong> colors invert in a slightly different way. More precisely, they keep their relative brightness across both light and dark theme.</p><p>For example, in an interface using the default <strong>surface</strong> role, the mapped area is the brightest in light theme and the dimmest in dark theme. In an interface using the <strong>surface bright</strong> role, the mapped area is the brightest in both light and dark theme.</p>

UI with surface role applied to the body area and surface container applied to the navigation area, shown in light theme.

<p id="isPasted">Light theme</p><ol><li style="font-weight:bold"><strong>Surface</strong></li><li style="font-weight:bold"><strong>Surface container</strong></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2nf2l7-36.png?alt=media

UI with surface role applied to the body area and surface container applied to the navigation area, shown in dark theme.

<p id="isPasted">Dark theme</p><ol><li style="font-weight:bold"><strong>Surface</strong></li><li style="font-weight:bold"><strong>Surface container</strong></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2nfaia-37.png?alt=media

UI with surface bright role applied to the body area and surface container applied to the navigation area, shown in light theme.

<p id="isPasted">Light theme</p><ol><li style="font-weight:bold"><strong>Surface bright</strong></li><li style="font-weight:bold"><strong>Surface container</strong></li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2nfhyc-38.png?alt=media

UI with surface bright role applied to the body area and surface container applied to the navigation area, shown in dark theme.

<p id="isPasted">Dark theme</p><ol><li style="font-weight:bold"><strong>Surface bright</strong></li><li style="font-weight:bold"><strong>Surface container</strong></li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2nep5x-39.png?alt=media

Large screen chat UI. The surface dim role is applied to the left navigation rail and the surface bright role is applied to the chat window.

<ol id="isPasted"><li>Navigation rail with <strong>surface dim</strong> background</li><li>Chat window with <strong>surface bright</strong> background</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fly2nfqah-40.png?alt=media
