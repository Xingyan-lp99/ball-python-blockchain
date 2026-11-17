# Dynamic color schemes

Source: https://m3.material.io/styles/color/dynamic
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/03571013-d450-49cc-8300-4c7ee70bb4ca.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Dynamic color can change a color palette to match user settings, like wallpapers, or in-product content

## Choosing a source

<p>There are two ways your product can get a source color:</p><ol><li><strong>User-generated color</strong> from a user's wallpaper</li><li><strong>Content-based color</strong> from in-app content like a music album or book cover</li></ol><p>Learn <a href="/m3/pages/color/how-the-system-works">how dynamic color works</a></p>

<p>Both types of dynamic color are accessible and personalized, so deciding which type to use is based on what's most important in the product: content or user preference.</p>

<h2 id="isPasted">User-generated color</h2>

<p>Choose a user-generated color source if:</p><ul><li>Your users would benefit from a personalized experience that's tested well</li><li>You want your product to showcase the latest and greatest Material features</li></ul><p><a href="/m3/pages/dynamic/user-generated-source"><strong>Get started with user-generated color</strong></a></p>

Thumbnail of a floral red wallpaper with a line pointing to an app screen with a red color scheme.

<p>An app colored with a dynamic user-generated scheme sourced from the user's red wallpaper.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flnc8u840-01.png?alt=media

<h2 id="isPasted">Content-based color</h2>

<p><span>Choose a content-based color source if:</span></p><ul><li>Content is front-and-center in your product</li><li>Your team can do a bit of advanced customization</li><li>Content-based color would support usability of specific features like media players</li><li>Content-based color is best used for contained screen elements adjacent to the source image, though the source image is not always visible.</li></ul><p><a href="/m3/pages/dynamic/content-based-source"><strong>Get started with content-based color</strong></a></p>

A thumbnail of a teal album art with a line pointing to an app screen with a teal color scheme.

<p>An app colored with a dynamic content-based scheme sourced from the in-app album art.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln4j2i04-02.png?alt=media

<h2 id="isPasted">Multiple color sources</h2>

<p>Choose to use multiple color sources if:</p><ul><li>Your product requirements meet multiple criteria above</li><li>You don't mind doing a bit of advanced customization</li></ul><p><a href="/m3/pages/dynamic/user-generated-source"><strong>Get started with user-generated color</strong></a><strong> before customizing</strong></p>

Thumbnail of green plants with a line (1) indicating green edit buttons in a photo app.
Thumbnail of red wallpaper with a line (2) indicating red share buttons in the same photo app.


<p>An app colored with schemes from multiple sources.</p><ol><li>Content-based color sourced from the in-app photo</li><li id="isPasted">User-generated color sourced from the user's wallpaper</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln4j3qu9-03.png?alt=media

## User-generated source

<p><strong>User-generated color</strong> comes from an Android user's personal wallpaper. The wallpaper is digitally analyzed, a single color is selected as the source color, and tones are chosen and assigned to each color role.</p><p id="isPasted"><strong>With a dynamic user-generated color scheme, end-users see</strong></p><ul><li>Their apps and system UI change to a color pulled from their device wallpaper</li><li>A product that looks personalized</li></ul>

Mobile screenshot of Google Photos

<p>Dynamic color in a work app</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4k2c1o5-4.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/nRGjsdrnAV37pnk6lndvtTpYveBb7FUID7JSKlCWTa8csqBEDNT4bS0J0vGIr7xLxTz0YTXnekJBLDhrKaOR2ioAiQj9C6WerRZaisgFjlCQ=s656

Mobile screenshot of Gmail in light theme.

<p>Dynamic color in a work app</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4k2c5u0-5.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/iNathyd2eaBruZBmo0jpvBs3xxWgGCLJlgubjFw4KEnDTH5aG4m5ddQsDkaDwoJkiSEzeIcQf14jjcVScEH13jZbKZ5lsaMy9e_CtcvpBg31xw=s656

Mobile screenshot of Gmail.

<p>Dynamic color in a work app</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4k2caip-6.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/DeZMSmblekT7CJla66TuXekJ2mnhrENpzRb1Yjzusj0ZDNB553w6Jhq_gotbSMiyd5AcLLLC5Gn8w4W9EUYuzfYuf5gPsOm06ADeRr08Ly8=s656

<h2>Design with user-generated color</h2>

<p>Because the final colors will be dynamically generated on each user's personal device, <strong>it's more important to understand and apply the system's <app-froala-tooltip-element description="Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme." link-label="More on color roles" link-url="/m3/pages/color-roles" should-open-link-in-new-tab="true">color roles</app-froala-tooltip-element> in your designs</strong> rather than use a particular hex value.</p><p>The easiest way to do this is by using a color scheme generated by the <app-froala-tooltip-element description="Material Theme Builder (MTB) is a Figma plugin that allows markers to emulate the color extraction process for dynamic color and create custom tonal schemes. " link-label="Get the MTB" link-url="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" should-open-link-in-new-tab="true">Material Theme Builder</app-froala-tooltip-element> and focus on applying the color roles to your designs instead of particular hex values. Then you can use the Material Theme Builder to test how well the design functions across potential user-generated color options.</p>

<h3 id="isPasted">Use Material color roles in new design files</h3><p id="isPasted"><strong>First, get the color roles by creating a new theme with the Material Theme Builder</strong></p><ol id="isPasted"><li>Open your Figma file. Select the <strong>Resources</strong> button in the Figma toolbar</li><li>Find the <a href="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" target="_blank" rel="noopener noreferrer">Material Theme Builder plugin</a> and select <strong>Run</strong>. This will open a plugin dialog showing the default color scheme, including Core colors and Extended colors.</li><li>Open the plugin's <strong>Settings</strong> (gear icon at lower right of dialog) and select the checkboxes for both <strong>New theme color diagram</strong> and <strong>Generate State Layers</strong>. This will create a handy visualization of your branded color scheme and also generate state layers essential for designing interactions. <a href="/m3/pages/interaction-states/state-layers" rel="noopener noreferrer" target="_blank">Learn more about state layers</a></li><li>Navigate out of settings</li><li>Open the Current Theme dropdown at the top of the dialog and select <strong>+ ADD NEW THEME</strong></li><li>Give your theme a short name (this name will become the prefix of your color roles in Figma)</li><li>Select <strong>ADD THEME</strong></li><li>With <strong>Custom</strong> selected, select <strong>Primary</strong>. This opens a dialog prompting you to select a custom source color.</li><li>Enter the Hex value for a color and hit <strong>Apply</strong>. This will generate a full color scheme.</li><li id="isPasted">With the Current Theme dropdown at the top of the dialog, select your theme</li><li>Select the frames or components in your file and then hit <strong>Swap</strong> in the bottom right of the dialog. This will automatically update the colors for any M3 Design Kit components.</li></ol><p><br /></p><h3>Apply color roles to an existing file or M3 Design Kit components</h3><p><strong>First, get the color roles into your file</strong></p><ol><li id="isPasted">Copy your preferred scheme's color diagram from your <a href="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" target="_blank" rel="noopener noreferrer">Material Theme Builder</a> file and paste it into your file (this makes the color roles available in the Design panel on the right of the screen as part of your local styles)</li></ol><p><strong>Swap colors in M3 Design Kit components for your preferred colors</strong></p><ol><li>Select the <strong>Resources</strong> button in the Figma toolbar.</li><li>Find the <a href="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" target="_blank" rel="noopener noreferrer">Material Theme Builder plugin</a> and select <strong>Run</strong>. This will open a plugin dialog showing the default color scheme, including Core colors and Extended colors.</li><li>In the Current Theme dropdown at the top of the dialog, select your color scheme</li><li>Select the frames or M3 Design Kit components in your file that need a color update and then hit <strong>Swap</strong> in the bottom right of the dialog. This will automatically update their colors from baseline colors to your selected scheme colors</li></ol><p><strong>Then, update any remaining non-color-role-based colors</strong></p><ol><li>Manually change any hex values or non-color-role-based color styles by selecting all and looking through the Selection colors in the Design panel on the right of the screen</li><li>Any colors that don't start with your selected scheme name need to be replaced with a corresponding color role</li><li>Hover on a non-color-role-based color row in the Design panel and select the <strong>Style</strong> icon (four dots). This opens a selection dialog.</li><li>Search for your scheme name to see the color roles</li><li>Select the color-role-based color that most closely matches that color's use case (see <a href="/m3/pages/color-roles">Color roles</a> for more information on what color to use where) and select <strong>Use style</strong> to apply it to the selected objects</li><li>Repeat until all non-color-role-based colors in the file have been replaced with color roles</li></ol><p><br /></p><h3 id="isPasted">Try out how your designs will look with dynamic color</h3><ol id="isPasted"><li id="isPasted">Select the <strong>Resources</strong> button in the Figma toolbar.</li><li>Find the <a href="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" rel="noopener noreferrer" target="_blank">Material Theme Builder plugin</a> and select <strong>Run</strong>. This will open a plugin dialog showing the default color scheme, including Core colors and Extended colors.</li><li>Select Dynamic</li><li>Add an image, or select the <strong>Shuffle</strong> icon to get a random source color</li><li>Select the frames or components in your file that you want to see with dynamic color and then hit <strong>Swap</strong> in the bottom right of the dialog. This will automatically update their colors to the user-generated dynamic colors.</li><li>Repeat with a range of colors to get a sense of how your product will appear across different users' devices</li></ol><p><br /></p><p><strong>Need to make adjustments to the scheme? Check out <a href="/m3/pages/advanced/overview">Advanced customizations</a></strong></p>

<h2>Develop with user-generated color</h2>

<ul><li><p><a href="https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md" target="_blank">Android Views (MDC-Android) – Color docs</a></p></li></ul>

## Content-based source

<p id="isPasted"><strong>Content-based color</strong> comes from in-app content, such as an album thumbnail image, logo, or video preview. </p><p>Like user-generated color, the image is digitally analyzed through quantization, a single color selected as the source color, and tones are chosen and assigned to each color role.</p><p><strong id="isPasted">With a dynamic content-based color scheme, end-users see</strong></p><ul><li>The product (and possibly system UI) change to a color corresponding to on-screen imagery</li><li>A product that looks "smart"</li></ul>

Screenshot of a messaging app on a tablet screen.

<p>Messaging app with content-based color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flnoncne7-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/qkzrtqlq4iJp60o9QNG7Fbl3e8HH4RZHlxkc45WwtZXK29xc19mxYYMsnvfRB0lurUrJSJ3h0wyPqnLj0tcomAV3cPhi3B-QxT7CBGicj86k=s2048

<h2>Design with content-based color</h2>

<ul><li>Apply content color in apps and areas where it can enhance brand identity and convey the spirit of personalization. </li><li>For example, a music app might derive color from a specific album’s artwork to build upon the personal connection to a music library. For a news feed, content-based color may be applied from a given publication to differentiate brands and help users navigate the platform.</li><li>In-app content provides a color source for any content-based color scheme, and can be applied within a specified area of an app, such as a set of components or a particular screen.</li><li>Get started: Use the color tokens and roles built into the Theme Builder. Check that the preferred scheme is selected when using <a href="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" rel="noopener noreferrer" target="_blank">Material Theme Builder</a> to create color schemes from images.</li><li>Explore advanced customizations</li></ul>

<h2 id="isPasted">Develop with content-based color</h2>

<ul><li>MDC-Android – <a href="https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md#content-based-dynamic-colors" rel="noopener noreferrer" target="_blank">Content-based dynamic color</a></li></ul>
