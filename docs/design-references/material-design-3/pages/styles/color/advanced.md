# Advanced customizations

Source: https://m3.material.io/styles/color/advanced
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/eee5a035-c309-4c67-afb5-6b4c6dd8ec4e.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Apply, define, or adjust colors to create a fine-tuned, unique color experience

## Overview

<p>From changing a component’s default color mapping to creating additional color roles, advanced customizations fall within one of three general actions: applying, defining, or adjusting colors.</p>

Collage of green primary color mapped to a custom volume component; a custom teal tertiary color role applied to a weather widget; a custom orange caution color; and an illustration of an avatar in yellow, red, and green color themes

<p>Advanced customizations include the ability to remap colors on components; define new colors in addition to the scheme; define custom color roles; and apply dynamic color to imagery.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt29uqj-1.png?alt=media

<h2>Apply colors</h2><p>You can apply colors in places or ways that aren’t provided by default.</p><p><a href="/m3/pages/advanced/apply-colors#5ceacf6b-364e-4dab-83db-299c691cb21d">Combine multiple color schemes</a><br />Use multiple color schemes in the same app experience, such as a baseline scheme combined with a dynamic content-based scheme.</p><p><a href="/m3/pages/advanced/apply-colors#d15f5373-c03b-4282-a309-db569975d395">Map or remap colors onto UI elements</a><br />Change a component’s default color mapping, or apply colors to your own custom components.</p>

<h2>Define new colors</h2><p>You can add colors to your color scheme, extending the default color roles.</p><p><a href="/m3/pages/advanced/define-new-colors#f13116d1-3023-44b9-b0b5-2ee07dc1af5f">Define static colors</a> (formerly known as custom colors)<br />Add colors to a dynamic color scheme that stay static, which are useful for semantic colors.</p><p><a href="/m3/pages/advanced/define-new-colors#baed14ce-4be8-46aa-8223-ace5d45af005">Define custom color roles</a><br />Create new color roles to use alongside the 26+ standard color roles.</p>

<h2>Adjust existing colors</h2><p>You can control the color algorithm’s output to adjust the appearance of dynamic colors.</p><p><a href="/m3/pages/advanced/adjust-existing-colors#c6810874-a320-4684-8df6-3869887ea49c">Define your own baseline scheme</a><br />You can input colors to define your own baseline scheme.</p><p><a href="/m3/pages/advanced/adjust-existing-colors#e169ea0f-a190-4cd1-b0d4-4e3616964129">Define your own dynamic scheme</a><br />You can define color algorithm rules to produce your own custom dynamic scheme.</p><p id="isPasted"><a href="/m3/pages/advanced/adjust-existing-colors#cb49eeb4-3bbd-4521-9612-0856c27f91ef">Use color fidelity</a><br />You can apply color fidelity to make scheme colors better match your input colors.</p>

## Apply colors

<p>You can apply colors in places or ways that aren’t provided by default.</p>

<h2 id="isPasted">Combine multiple color schemes</h2>

<p>Use multiple color schemes in the same app experience, such as a baseline scheme combined with a dynamic content-based scheme.</p>

Smart home control screen showing media controls, light controls, and wifi and thermostat controls. Annotation 1 points to the media controls, which are colored in a teal scheme. Annotation 2 points to the remaining controls, colored in a red scheme.

<p>This smart home control screen combines two color schemes:</p><ol><li>A teal content-based color scheme from the local album art, applied to media controls</li><li>A red user-generated color scheme from the user's wallpaper, applied to the rest of the UI</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt7bogx-1.png?alt=media

<h3>Why</h3><p>If your app features content-rich moments, such as a media player, it can enhance a user’s experience by applying local color based on that content.</p><h3>How</h3><ul><li id="isPasted">Start from a <a href="/m3/pages/static/baseline">baseline</a> or <a href="/m3/pages/dynamic/user-generated-source">user-generated dynamic</a> scheme to create a consistent color foundation in your app.</li><li>On top of this foundation, <a href="/m3/pages/dynamic/content-based-source">map content-based color roles to contained spaces</a> to emphasize or celebrate content. For example, a music app might derive color from a specific album’s artwork to build upon the personal connection to a music library.</li></ul><h3>Best practices</h3><ul><li id="isPasted">Consider where content exists in the UI and where content-based color can enhance a person’s experience. Your existing app structure can suggest contained areas for content-based color to live.</li><li><strong>Build hierarchy &amp; direct attention:</strong> When many types of information and actions share a screen, use content-based color to add hierarchy and draw attention to the content.</li><li><strong>Link and associate content on a screen:</strong> In lists and collections of repeated items that benefit from differentiation, content-based color can help associate related elements. This helps people quickly distinguish and pair related information, such as a list item and its associated action.</li><li><strong>Immerse users in content color:</strong> Full-screen content-based color moments can orient users within a content-driven experience, such as a media control or a purchase flow. </li><li><strong>Pair content-based color with its source content:</strong> Keep the source for content-based color visible on a screen using the content color. This way users are shown where a content-based color originates. Avoid applying content-based color in spaces where the content itself isn’t visible.</li><li><strong>Limit the number of color source types per screen:</strong> Limit a screen to two color schemes from different source types. Too many color schemes on the same screen may lead to confusion and visual disarray. For example, a baseline or user-generated color scheme can be combined with one type of on-screen content (such as album art).</li><li><strong>Don’t replace semantic colors:</strong> Use caution when applying content-based color in places where a semantic color or conventional color meaning is important for usability. For example, a common red error message or a common green positive action shouldn’t be replaced with dynamic content-based color because it may interfere with someone’s understanding.</li></ul>

Photo options screen in a red theme. Photo editing controls are displayed underneath the photo, and are colored in a teal scheme sourced from the photo.

<p>When many types of information and actions share a screen, use content-based color to add hierarchy and draw attention to the content. This screen uses a content-based scheme sourced from the photo to draw attention to the photo editing controls.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt7czj9-2.png?alt=media

A feed of cards listing different activities. The first card shows an image of a yellow tape cassette, and its UI is colored in a yellow scheme. The second card shows an image of a green plant, and its UI is colored in a green scheme.

<p>In lists and collections of repeated items that benefit from differentiation, content-based color can help associate related elements. This helps people quickly distinguish and pair related information, such as a list item and its associated action. In this list of activities, each card is colored with a scheme sourced from its main image.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt7dkn6-3.png?alt=media

Media control screen where a podcast called Early Aughts is playing. The screen displays a teal colored album art for the podcast. The entire screen is colored in a teal scheme.

<p>Full-screen content-based color moments can orient users within a content-driven experience, such as a media control or a purchase flow. This media control screen is colored entirely in a scheme sourced from the in-context album art.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt7dy9t-4.png?alt=media

<h2 id="isPasted">Map or remap colors on UI elements</h2>

<p>You can change a component’s default color mapping, or apply colors to your own custom components.</p>

A custom volume slider component next to a design software UI palette displaying a list of color roles. The primary color role is linked to the mute button on the volume slider.

<p>Colors can be remapped on existing Material components, or can be mapped as desired to custom-built components, such as this unique volume slider.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt7eaxg-5.png?alt=media

<h3>Why</h3><p>You want to map colors to a custom-built component or change a Material Component’s default color mapping to improve its function (such as visual contrast) or style.</p><h3>How</h3><p>Choose an appropriate color role based on how the color is used (see <a href="/m3/pages/color-roles">color roles</a>) and how well the role supports your intended design expression.</p><h4>Design</h4><ul><li>In Figma, select the component or element you want to remap so that you see its colors in the Design panel on the right of the screen</li><li>To remap a color, hover on the color row in the Design panel and select the <strong>Style</strong> icon (four dots). This opens a selection dialog.</li><li>Search for your theme name to see the available color roles</li><li>Select the color role that most closely matches that color's use case in the component. For example, the background color of a component could be replaced with the <strong>surface</strong> color role and the color for text or icons could be <strong>on surface</strong>. See <a href="/m3/pages/color-roles">Color roles</a> for more information on what color to use where.</li><li>Select <strong>Use style</strong> to apply that color to the selected objects</li><li>Repeat until all colors in the component have been replaced with color roles from your scheme</li></ul><h3>Best practices</h3><ul><li id="isPasted">Make sure to use color roles that support Material's contrast requirements for the component. Any color roles starting with "on-" are guaranteed to have sufficient contrast with the corresponding color role. Other color role pairs may not meet the 4.5:1 (small text) and 3:1 (large text) Material contrast requirements.</li><li>If you’re applying a dynamic scheme, test how the color on the component appears under different themes (such as light and dark; red, yellow, green and blue) to ensure it looks as desired in dynamic color</li><li>Always apply color roles rather than static values or tonal palette values, as these colors will break with light and dark themes, contrast control, and other features. If the color in a role does not meet your needs, you can define new colors or adjust existing colors.</li></ul>

## Define new colors

<p>You can add colors to your scheme to extend the color roles provided by Material out of the box.</p>

<h2 id="isPasted">Define static colors</h2>

<p><em>Formerly known as custom colors</em></p><p>You can define additional colors in your scheme that stay static even when other colors dynamically change. When you input a desired reference color, Material will return four derived color roles that align with the design of existing roles in the color scheme.</p>

Diagram showing (1) a green circle, with an arrow leading from it to (2) a set of four color chips named Success, On Success, Success Container, and On Success Container. Below (3 and 4), the green Success colors are applied to a home control UI.

<p>In this example, a static green color called Success is defined in addition to the scheme, and applied to UI to indicate a success state.</p><ol><li>Green source color used to generate color values for four new color roles</li><li>A set of new "Success" color roles derived from the source color</li><li><strong>On success container</strong> color applied to the WiFi icon</li><li id="isPasted"><strong>Success container </strong>color applied to a card container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt7wrjx-1.png?alt=media

<h3 id="isPasted">Why</h3><p>You may need to apply static colors in your app for brand expression or to communicate semantic meaning, like a green success state. By defining these colors using the Material system, they'll work with existing Material colors and support features like dynamic color and user-controlled contrast.</p><h3>How</h3><p>Use the <app-froala-tooltip-element description="Material Theme Builder (MTB) is a Figma plugin that allows markers to emulate the color extraction process for dynamic color and create custom tonal schemes. " link-label="Get the MTB" link-url="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" should-open-link-in-new-tab="true">Material Theme Builder</app-froala-tooltip-element> to input a custom color. Material will return four color roles derived from that reference color. The main color, on-main color, container color, and on-container color all follow the conventions of the accent colors in the main scheme, and can be applied to your UI according to the same relationships. See <a href="/m3/pages/advanced/apply-colors#d15f5373-c03b-4282-a309-db569975d395"><u>map or remap colors on UI elements</u></a> for more information.</p><h3>Best practices</h3><ul><li>If the colors provided back from your input color appear differently than expected, you can enable or disable color fidelity. <a href="/m3/pages/advanced/adjust-existing-colors#cb49eeb4-3bbd-4521-9612-0856c27f91ef">Color fidelity</a> is a feature that adjusts colors’ tones to match that of your input color.</li><li>Material provides the red Error color out of the box as an example of a static color, so you do not need to define your own static color for a semantic red color.</li><li>If you are using static colors in a dynamic scheme, you can choose to <a href="/m3/pages/advanced/adjust-existing-colors#1cc12e43-237b-45b9-8fe0-9a3549c1f61e">harmonize your static colors</a> to the scheme’s primary color. This will shift your static colors’ hues slightly warmer or cooler for a more harmonious overall appearance, while retaining the semantic meaning associated with the colors’ hue range.</li></ul>

Green card in a home control UI shown under three different color schemes: purple, red, and yellow. In each scheme, the green card color appears slightly shifted to look more harmonious with the overall color.

<p>Static colors can be harmonized with dynamic color to appear harmonious with the overall color scheme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt7xb07-2.png?alt=media

Transit app UI with orange, green, and red color-coded subway lines and icons. The same screen is shown under a purple, red, and yellow scheme. In each screen, the subway line colors appear the same.

<p>Colors can stay completely static and forgo harmonization if their values are tied to literal sources, such as brand colors or real-world signage</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt7xlqa-3.png?alt=media

<h2 id="isPasted">Define custom color roles</h2>

<p>You can define custom color roles in addition to those already existing in the color scheme. By defining these roles the same way Material does (specifying a reference palette, starting tones, and contrast requirements), these roles can achieve colors more specific to your needs while working seamlessly with features such as user-controlled contrast.</p>

(1) a palette of Primary color chips in tones labeled 0 to 100, with tone 50 circled. (2) The chosen color against the primary container color, with 3:1 labeled on the border. (3) The chosen color applied to a large weather icon in a weather widget.

<p>Example of creating a custom color role:</p><ol><li>The primary tonal palette, with tone 50 specified as the <strong>primary graphic</strong> default value</li><li>Color swatch showing an accessible 3:1 contrast between <strong>primary graphic</strong> and <strong>p</strong><strong>rimary container</strong></li><li>The <strong>primary graphic</strong> color role is applied in a weather widget against the <strong>primary container</strong></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt7y1c2-4.png?alt=media

<h3 id="isPasted">Why</h3><p>You may need to define your own custom color roles if the scheme’s existing colors or additional static colors don’t meet your product’s needs. In particular, you should create them within the Material system to respect dynamic colors and unlock other features like user-controlled contrast.</p><h3>How</h3><p>Abstract your new color into a color role by specifying the following criteria:</p><ul><li><strong>Palettes and reference tones:</strong> For each color role, you must assign its value from a Material palette (primary, secondary, tertiary, neutral, neutralVariant, error) and a reference tone (for example: primary70, primary80, primary90…) for both light and dark themes.</li><li><strong>Color pairings:</strong> You must specify any visual relationships in your design, such as color pairs that are used together as foreground and background, or which should retain a tone delta between them (difference in lightness or darkness).</li><li><strong>Contrast:</strong> Confirm that custom foreground and background color pairings meet <a href="/m3/pages/designing/color-contrast">Material's contrast minimums</a>.</li></ul><p>Once the above criteria are known, you can define the new color roles in your own dynamic color object. For each color role, you may then call Material Color Utilities (MCU) to generate the color value dynamically, according to different conditions such as user theming or contrast level.</p><h3>Best practices</h3><p>Defining custom color roles should be considered only if you cannot achieve your desired colors with other Material color solutions.</p><p><br /></p>

## Adjust existing colors

<p>You can control the color algorithm’s output to adjust the appearance of colors within the roles provided by default.</p>

<h2 id="isPasted">Define your own baseline scheme</h2><p>You can input colors to define your own baseline scheme.</p>

<h3 id="isPasted">Why</h3><p>You may want to define your own baseline scheme so your app’s colors stay static (ie. does not change with dynamic color), such as to reflect your brand colors. By providing your own custom input colors for the primary, secondary, tertiary, and neutral colors in the scheme, Material will provide back the scheme’s regular color roles with values derived from your reference colors.</p>

Above, a logo of two trees featuring dark green, orange, and pale blue colors. Below, each of those colors is show as a circle, with an arrow pointing from it to a set of chips showing color roles produced from the original color.

<p>You can input your own colors to produce a static baseline scheme. In this example, colors from the logo are inputted to produce primary, secondary, and tertiary colors.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt7zkg8-1.png?alt=media

<h3>How</h3><p>Using the <app-froala-tooltip-element description="Material Theme Builder (MTB) is a Figma plugin that allows markers to emulate the color extraction process for dynamic color and create custom tonal schemes. " link-label="Get the MTB" link-url="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" should-open-link-in-new-tab="true">Material Theme Builder</app-froala-tooltip-element>, input your own colors for primary, secondary, tertiary, neutral, and neutral variant. The Theme Builder will generate a color scheme with values based on your inputs, and the given color roles can be used in the same manner as those from any other Material scheme.</p><h3>Best practices</h3><ul><li>Conventionally, primary and tertiary colors are the most visually prominent in the scheme, with tertiary appearing complementary to primary by changing its hue. Secondary, neutral variant, and neutral colors match primary in hue but are progressively less chromatic in that order. Input your colors into the appropriate category to maintain similar relationships as designed by Material, and ensure expected and visually pleasing results when those colors are mapped to components.</li><li>If the colors provided back from your input color appear differently than expected, you can enable or disable <a href="/m3/pages/advanced/adjust-existing-colors#cb49eeb4-3bbd-4521-9612-0856c27f91ef">color fidelity</a>. Color fidelity is a feature that adjusts colors’ tones to match that of your input color.</li><li>If the 26+ standard color roles do not meet your needs, you may need to <a href="/m3/pages/advanced/define-new-colors#baed14ce-4be8-46aa-8223-ace5d45af005">define custom color roles</a>.</li></ul>

<h2 id="isPasted">Define your own dynamic scheme</h2><p>You can define color algorithm rules to produce your own dynamic scheme.</p>

<h3>Why</h3><p>Control the appearance of your app’s colors while respecting dynamic color. For example, you may want your app to match the user’s wallpaper theme, but appear more vibrant than the default dynamic theme colors.</p>

Thumbnail of a red floral wallpaper with two arrows leading out of it, labeled 1 and 2. Arrow 1 leads to a set of red colors chips produced from the wallpaper. Arrow 2 points to another set of red color chips, which appear more vibrant than the first.

<p>You can define your own dynamic scheme to reflect a user's wallpaper but control other aspects such as the colors' vibrancy.</p><ol><li>Colors produced dynamically from a user's red wallpaper following default specs</li><li>Colors produced dynamically from the same wallpaper following custom-defined specs</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt809t2-2.png?alt=media

<h3 id="isPasted">How</h3><ul><li>Material generates the color scheme by following hue and chroma values specified for each group of colors (primary, secondary, tertiary, neutral, and neutral variant). For more information, see <a href="/m3/pages/color/how-the-system-works">how the system works</a>. To adjust the appearance of these colors and produce your own dynamic scheme, you must provide your own hue and chroma values for each of these color groups.</li><li>Once these values are known, you may define your own scheme variant and call <app-froala-tooltip-element description="Material Color Utilities (MCU) are a set of color libraries containing algorithms and utilities that make it easier for you to develop dynamic color themes and schemes in your app." link-label="More on MCU" link-url="https://github.com/material-foundation/material-color-utilities" should-open-link-in-new-tab="true">Material Color Utilities (MCU)</app-froala-tooltip-element> to dynamically generate the scheme and provide color values for each role in the scheme.</li></ul><h3>Best practices</h3><ul><li>Defining custom color roles should be considered only if you cannot achieve your desired colors with other Material color solutions.</li><li>If the colors provided back from your input color appear differently than intended, you can enable or disable <a href="/m3/pages/advanced/adjust-existing-colors#cb49eeb4-3bbd-4521-9612-0856c27f91ef">color fidelity</a>. Color fidelity is a feature that adjusts colors’ tones to match that of your input color.</li><li>If the color roles provided by Material out of the box do not meet your needs, you may need to <a href="/m3/pages/advanced/define-new-colors#baed14ce-4be8-46aa-8223-ace5d45af005">define custom color roles</a> for greater control over their appearance.</li></ul>

<h2 id="isPasted">Use color fidelity</h2><p>You can apply color fidelity to make scheme colors better match your input colors.</p>

<h3>Why</h3><p>Material scheme colors are mapped to tones (lightness or darkness) to achieve visually accessible color pairings with sufficient contrast between foreground and background elements. In some cases, these tones can prevent colors from appearing as intended, such as when a color is too light to appear vibrant. Color fidelity is a feature that adjusts tones in these cases to produce the intended visual results without harming visual contrast.</p><p><br /></p>

Above, a dark purple circle with an arrow labeled 1 pointing to a set of color chips, whose colors appear similarly dark.
Below, a dark purple circle with an arrow labeled 2 pointing to a set of color chips, whose colors appear lighter.

<p>Color fidelity adjusts tones in color roles to produce the closest match to your input color. In this example, colors are produced from a dark purple input with and without color fidelity.</p><ol><li>Color roles produced with color fidelity</li><li>Color roles produced without color fidelity</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt80nic-3.png?alt=media

<h3 id="isPasted">How</h3><ul><li>In the <app-froala-tooltip-element description="Material Theme Builder (MTB) is a Figma plugin that allows markers to emulate the color extraction process for dynamic color and create custom tonal schemes. " link-label="Get the MTB" link-url="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" should-open-link-in-new-tab="true" id="isPasted">Material Theme Builder</app-froala-tooltip-element>, you can toggle the “match color” option on your input color to enable or disable fidelity. By default, fidelity is enabled when you use Theme Builder to <a href="/m3/pages/advanced/adjust-existing-colors#c6810874-a320-4684-8df6-3869887ea49c">create a custom baseline scheme</a> or <a href="/m3/pages/advanced/define-new-colors#f13116d1-3023-44b9-b0b5-2ee07dc1af5f" target="_blank" rel="noopener noreferrer">define static colors</a>.</li><li>In code, you can flag color roles in your scheme with a boolean which will enable or disable fidelity for those colors.</li></ul><h3>Best practices</h3><ul><li>When producing a custom baseline scheme or defining static colors, you may wish to toggle fidelity on and off to determine which setting better suits your desired design.</li><li>Because color fidelity adjusts tones (lightness or darkness of colors), to ensure accessible contrast, remember to pair appropriate <a href="/m3/pages/color-roles">colors roles</a> together, such as a background color with its corresponding foreground “on” color.</li></ul>

<h2>Harmonize colors</h2><p>In dynamic schemes, you can automatically adjust the hue of static colors so they look better alongside the scheme’s primary color.</p>

<h3>Why</h3><p id="isPasted"><app-froala-tooltip-element description="Static colors are UI colors that don't change based on the user's wallpaper or in-app content. Once assigned to their respective color roles and UI elements, the colors remain constant." link-label="More on static color" link-url="/m3/pages/static/baseline/" should-open-link-in-new-tab="true">Static colors</app-froala-tooltip-element> may visually clash with a  scheme’s dynamically changing colors. To improve visual harmony, Material provides an optional ‘harmonize’ function that slightly adjusts static colors to look better in dynamic schemes.</p><p>Colors that are closer in <app-froala-tooltip-element description="Hue is the perception of a color as red, orange, yellow, green, blue, violet, and so on." link-label="More on hue, chroma, and tone" link-url="/m3/pages/color/how-the-system-works/#199a8fa2-6510-4bca-b22a-3387f857a580" should-open-link-in-new-tab="true">hue</app-froala-tooltip-element> appear more pleasing together than colors with hues farther apart. Based on this principle, harmonization adjusts the hue of static colors, making them closer to the hue of the scheme’s primary color.</p>

Diagram comparing static colors in an app to harmonized static colors

<ol class="upper-alpha"><li>In this example, the color scheme has:<ol><li>Green as the primary color</li><li>Static blue </li><li>Static orange</li></ol></li><li>When harmonized, those static colors change hue, moving closer to the primary color on the color wheel. The resulting colors appear more visually pleasing together because they are closer in hue.</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt814il-4.png?alt=media

<p>To preserve the semantic meaning of static colors (such as a red to communicate errors), harmonization limits the amount that a color’s hue can change. Harmonized colors will become warmer or cooler in hue without appearing like another type of color.</p>

Diagram showing the limited range of harmonized hues

<p>To preserve the semantic meaning of colors, harmonization limits the amount that a color’s hue can change. For example, a red color (1) can become cooler (2) or warmer (3) in hue, but will not appear purple or orange.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwt81svm-5.png?alt=media

<h3>How</h3><ul><li id="isPasted">In the <app-froala-tooltip-element description="Material Theme Builder (MTB) is a Figma plugin that allows markers to emulate the color extraction process for dynamic color and create custom tonal schemes. " link-label="Get the MTB" link-url="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" should-open-link-in-new-tab="true">Material Theme Builder</app-froala-tooltip-element>, you can toggle harmonization on and off within the overflow menu for each static color you have added to the scheme.</li><li>In code, use the ‘Blend’ function from <a href="https://github.com/material-foundation/material-color-utilities" target="_blank" rel="noopener noreferrer">Material Color Utilities</a> to harmonize colors</li></ul><h3>Best practices</h3><ul><li id="isPasted">Harmonization will adjust a static color differently depending on the scheme’s primary color, so check the results under a variety of schemes to see the range of how they can appear in dynamic color.</li><li>Don’t harmonize colors whose appearance should stay absolutely consistent, such as brand colors.</li></ul>
