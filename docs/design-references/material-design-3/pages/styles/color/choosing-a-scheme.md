# Choosing a scheme

Source: https://m3.material.io/styles/color/choosing-a-scheme
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/a4aa0cf5-4017-4dea-ae51-edb8e950bd2c.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Static color schemes emphasize brand and uniformity, while dynamic schemes emphasize content or user settings to make products feel more personal

## Tab 1

<p>A <strong>color scheme</strong> describes all of a product's colors, color roles, and color relationships across light and dark themes.</p><p>There are two kinds of color schemes in Material:</p><ol><li><app-froala-tooltip-element description="Static colors are UI colors that don't change based on the user's wallpaper or in-app content. Once assigned to their respective color roles and UI elements, the colors remain constant." link-label="Jump to static color" link-url="/m3/pages/choosing-a-scheme/tab-1#3e05eecf-d91d-446f-b478-47cd144cce17" should-open-link-in-new-tab="true">Static</app-froala-tooltip-element></li><li><app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="Jump to dynamic color" link-url="/m3/pages/choosing-a-scheme/tab-1#00d5b65d-dd10-42c5-baaf-cd129cc2c1b5" should-open-link-in-new-tab="true">Dynamic</app-froala-tooltip-element></li></ol>

Types of color schemes in Material Design 3.

<p>Discover when and how to use different color schemes, including static baseline, dynamic user-generated, and dynamic content-based color schemes</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Flinbzkgu-MAT020.05-v2%20Internal.mp4?alt=media

<h2 id="isPasted">Static color</h2>

<p><span>Working with static color will be the most like other color workflows you may have used. Static colors won't ever change based on user input or in-app content.</span></p><p>Material provides a static baseline color scheme including default color assignments and mappings.</p>

Email UI in blue baseline scheme, shown in dark and light theme.

<p>Colors are static in the baseline color scheme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4ad7ppb-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/j-JLmGXG9zrnK7fJ7-FsVu1lEpz9oLlYVlRAmaTA3tcI_BYxJETtJ2ukAB5EPokqWwzsKHdBEFBYY11G4tm4BmP64HNPxwybufl2eozWyTE=s1352

<p><strong>What you get:</strong></p><p id="isPasted">✓ Accessible colors<br />✓ Pre-made baseline color scheme<br />✓ Colors that won't break an M2 app<br />✓ Ability to easily update to dynamic color in the future</p>

<p><strong>What you <em>don't</em> get:</strong></p><p id="isPasted">✗ Personalized colors<br />✗ Colors that change based on user's wallpaper or in-app content<br />✗ User-controlled contrast settings</p>

<p><strong>Products using baseline</strong> (as of Oct 2023)</p><ul><li>Maps</li><li>Search App (Android)</li><li>Home</li><li>Play Store</li><li>Primitives</li></ul>

<h3 id="isPasted"><strong>Use static (baseline) color if</strong></h3><ul><li>You're not ready to implement dynamic color (though it'll be easy to switch when you are)</li><li>Your product is migrating from M2 and you want to get M3 features without breaking your app</li><li>Your product is for enterprise users who wouldn't benefit from personalized color or user-controlled contrast settings</li><li>Your product is built for iOS</li></ul><p><br /></p><p><strong id="isPasted">Choosing baseline? </strong><a href="/m3/pages/static/baseline"><strong>Start designing with the baseline colors</strong></a></p>

<h2>Dynamic color</h2><p>Dynamic color will automatically create an accessible color scheme based on a specific source color.</p><p>Because the UI could end up with any number of different source colors, it's best to initially design it using the baseline color scheme so you can ensure the right color roles are mapped to the right components in your product. You'll use the <app-froala-tooltip-element description="Material Theme Builder (MTB) is a Figma plugin that allows markers to emulate the color extraction process for dynamic color and create custom tonal schemes. " link-label="Get the MTB" link-url="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" should-open-link-in-new-tab="true">Material Theme Builder</app-froala-tooltip-element> to see how your UI mocks look across a range of source colors and adjust it as-needed.</p>

Email UI changing from yellow, to red, to green color schemes,  shown in light and dark theme.

<p>While the actual colors may change, the color role mappings remain the same across dynamic color schemes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Flmb3ofmk-dynamic-color-animation.gif?alt=media

<p><strong>What you get:</strong></p><p id="isPasted">✓ Accessible colors<br />✓ Personalized colors that change based on a user's wallpaper or in-app content<br />✓ Ability to use advanced customizations like chroma fidelity to alter the dynamic color output<br />✓ User-controlled contrast settings</p>

<p><strong>What you <em>don't</em> get:</strong></p><p id="isPasted">✗ Exact same UI colors across all devices</p>

<p><strong>Products using dynamic color</strong> (as of Oct 2023)</p><ul><li>Gmail</li><li>Photos</li><li>Keep</li><li>Docs / Slides / Sheets</li><li>Meet</li><li>Assistant</li><li>Translate</li></ul>

<h3 id="isPasted"><strong>Use dynamic color if</strong></h3><ul><li>You want your product to showcase personalization</li><li>You want the colors to change base on a user's wallpaper or in-app content</li><li>You want your product to offer user-controlled contrast settings</li><li>You aren't sure if you'll need to also use a mix of dynamic and static colors (you can customize your color scheme to include static colors as your work progresses)</li></ul><p style="box-sizing:border-box;font:400 16px / 1.5rem"><br /></p><p style="box-sizing:border-box;font:400 16px / 1.5rem"><strong>Choosing dynamic color? Next </strong><a href="/m3/pages/dynamic/choosing-a-source"><strong>pick a dynamic color source</strong></a></p>
