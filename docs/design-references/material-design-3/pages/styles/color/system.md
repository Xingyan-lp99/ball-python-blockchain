# Color system

Source: https://m3.material.io/styles/color/system
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/89e1e9ce-0d9c-4391-9182-818434527cda.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Create accessible, personal color schemes communicating your product's hierarchy, state, and brand

## Overview

<p><strong>The Material color system includes:</strong></p><ul><li>Built-in set of <app-froala-tooltip-element description="For example, a dark surface color is algorithmically paired with a light text label color so the UI automatically meets contrast requirements." link-label="More on color relationships" link-url="/m3/pages/color/how-the-system-works#e1e92a3b-8702-46b6-8132-58321aa600bd" should-open-link-in-new-tab="true">accessible color relationships</app-froala-tooltip-element></li><li><app-froala-tooltip-element description="Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme." link-label="More on color roles" link-url="/m3/pages/color-roles" should-open-link-in-new-tab="true">26+ color roles</app-froala-tooltip-element> mapped to Material Components</li><li>Built-in <app-froala-tooltip-element description="A dark theme is a low-light version of a UI that displays mostly dark surfaces." link-label link-url should-open-link-in-new-tab="false">dark theme</app-froala-tooltip-element> colors</li><li>Static <app-froala-tooltip-element description="Baseline is the default static color scheme for Material products. It includes colors for both light and dark themes." link-label="More on the baseline color scheme" link-url="/m3/pages/static/baseline" should-open-link-in-new-tab="true">baseline color scheme</app-froala-tooltip-element> with default colors assigned to each color role</li><li><app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">Dynamic color</app-froala-tooltip-element> features including <app-froala-tooltip-element description="User-generated color dynamically creates a color scheme from a user's wallpaper." link-label="More on user-generated color" link-url="/m3/pages/dynamic/user-generated-source" should-open-link-in-new-tab="true">user-generated</app-froala-tooltip-element> and <app-froala-tooltip-element description="Content-based color dynamically creates a color scheme from in-app content like a music album or book cover." link-label="More on content-based color" link-url="/m3/pages/dynamic/content-based-source" should-open-link-in-new-tab="true">content-based color</app-froala-tooltip-element></li></ul><p><a href="/m3/pages/color/how-the-system-works">Learn how the system works</a></p>

Introduction to color guidance

<p>Learn about the value and function of Material 3’s dynamic color system and how it differs from past color systems</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Flinbli4g-MAT020.01-v4.mp4?alt=media

<p><app-froala-tooltip-element description="Welcome to color in Material 3. This video will introduce the purpose of color and Material 3’s algorithmic color system, or “dynamic color”. By the end of this video, you’ll understand the value and function of dynamic color and how it differs from past color systems.
Color is a powerful design tool and part of the Material system along with styles like typography and shape. In products, colors and the way they’re used can be vast and varied. An app’s color scheme can express brand and style, semantic colors can communicate meaning, and color contrast supports visual accessibility.
In many design systems of the past, designers manually picked app colors to support the necessary range of color applications and use cases.
But Material 3 has a dynamic color system, which doesn’t rely on handpicked colors. Instead, it uses color algorithms to generate beautiful, accessible color schemes based on dynamic inputs like a user’s wallpaper. This enables greater flexibility, personalization, and expression all while streamlining work for designers and teams." link-label link-url should-open-link-in-new-tab="false">View transcript</app-froala-tooltip-element></p>

Primary, on primary, primary container, and on primary container roles shown in baseline light theme color scheme.

<p>The baseline color scheme doesn't dynamically change</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4hetcer-4.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/5J0Ys6e-vzMeQPCfAMQcY147g2yFpXFrJEZK-AB8x8wGKMzdeQX3_GxE-xCOwuBANbYWr-g29epip05CF7fTGVz5gTc7wTBzFNp7AzXmdCVX=s656

Diagram showing an input color resulting in a simplified illustration of four roles of a color scheme. Shown in green and yellow in light theme.

<p>A dynamic color scheme changes the UI's colors based on different inputs, like a wallpaper</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln9uoi8a-dynamic%20color.png?alt=media

Diagram showing an orange input color generating a static orange color scheme for an auto heating UI element.

<p>Specific colors, such as semantic colors, can be set to not dynamically change</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln9uorlq-semantic-colors.png?alt=media

<p>Products with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/google-material-3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element> can automatically generate and assign colors to each element in the UI.</p><p>This provides:</p><ul><li>Personalized UI</li><li>Accessible contrast</li><li>User-controlled contrast</li><li>Automatic dark theme</li></ul>

Screen of an email app changing color from red to green to yellow

<p>The UI colors change dynamically</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm0ob8aeg-Untitled%20video%20(1).mp4?alt=media

<h2>Resources</h2><div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:29.8748%"><p>Type</p></th><th style="width:47.4061%"><p>Link</p></th><th style="width:22.7191%"><p>Status</p></th></tr></thead><tbody><tr><th style="width:29.8748%"><p>Design</p></th><td><p><a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">Design Kit</a> (Figma)</p></td><td><p>Available</p></td></tr><tr><th rowspan="3" style="width:29.8748%"><p>Implementation</p></th><td><p><a href="https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md" target="_blank">Android Views (MDC-Android)</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://developer.android.com/develop/ui/compose/designsystems/material3#dynamic_color_schemes" target="_blank">Jetpack Compose</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://pub.dev/packages/dynamic_color" target="_blank">Flutter</a></p></td><td><p>Available</p></td></tr><tr><th style="width:29.8748%"><p>Tools</p></th><td><p><a href="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" target="_blank">Material Theme Builder</a></p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2 id="isPasted">What's new</h2>

<p><span style="white-space:pre-wrap">May 2025</span></p><h3>Three levels of contrast</h3><p>Color roles support three levels of contrast so people can select the one that best suits their vision needs. <span style="white-space:pre-wrap">Contrasts also are tokenized.</span></p>

Email app in standard contrast.

<p>Standard contrast</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmrw9ybms-05.png?alt=media

Email app in medium contrast.

<p>Medium contrast</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmrwa03ny-06.png?alt=media

Email app in high contrast.

<p>High contrast</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmrwa0o3p-07.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">August 2024</span></p><h3><span style="white-space:pre-wrap">More colorful text and icons</span></h3><p><span style="white-space:pre-wrap">The following color roles are updated in light theme to be more colorful while still having accessible color contrast:</span></p><ul><li><span style="white-space:pre-wrap">On primary container</span></li><li><span style="white-space:pre-wrap">On secondary container</span></li><li><span style="white-space:pre-wrap">On tertiary container</span></li><li><span style="white-space:pre-wrap">On error container </span></li></ul><p><span style="white-space:pre-wrap">Affected components:</span></p><ul><li><span style="white-space:pre-wrap">Badges</span></li><li><span style="white-space:pre-wrap">Buttons</span><ul><li><span style="white-space:pre-wrap">Buttons</span></li><li><span style="white-space:pre-wrap">Extended FAB</span></li><li><span style="white-space:pre-wrap">FAB</span></li><li><span style="white-space:pre-wrap">Icon buttons</span></li><li><span style="white-space:pre-wrap">Segmented buttons</span></li></ul></li><li><span style="white-space:pre-wrap">Chips</span></li><li><span style="white-space:pre-wrap">Lists</span></li><li><span style="white-space:pre-wrap">Menus</span></li><li><span style="white-space:pre-wrap">Navigation bar</span></li><li><span style="white-space:pre-wrap">Navigation drawer </span></li><li><span style="white-space:pre-wrap">Navigation rail </span></li><li><span style="white-space:pre-wrap">Switches</span></li><li id="isPasted">Toolbars</li></ul>

Comparison of the color before and after the update, with FAB and button examples.

<p>Colors used for text and icons now appear more colorful</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmrwa1hcg-08.png?alt=media

<p>Oct 2023</p><h3>Reorganized guidelines</h3><p>Same color system, explained in a new way. Updated sections include:</p><ul><li><a href="/m3/pages/color/how-the-system-works">How the system works</a></li><li><a href="/m3/pages/advanced/overview">Advanced customizations</a></li><li><a href="/m3/pages/color-resources">Color resources</a></li></ul>

Diagram illustrating guidelines being reorganized

<p>The guidelines have been reorganized and updated</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln9upnnh-reorganized-guidelines.png?alt=media

<p>Feb 2023</p><h3>Tone-based surface colors</h3><p><a href="https://material.io/blog/tone-based-surface-color-m3" target="_self">Tone-based surface color roles</a> have replaced the previous approach of surfaces at +1 to +5 elevation.  The new color roles are not tied to <app-froala-tooltip-element description="Elevation is the distance between two surfaces on the z-axis." link-label="More on elevation" link-url="/m3/pages/elevation/overview" should-open-link-in-new-tab="true">elevation</app-froala-tooltip-element> and offer more flexibility and support for color features, such as <app-froala-tooltip-element description="User-controlled contrast is a dynamic color feature enabling users to choose from one of three levels of color contrast: standard, medium, and high." link-label="More on user-controlled contrast" link-url="/m3/pages/color/how-the-system-works#0207ef40-7f0d-4da8-9280-f062aa6b3e04" should-open-link-in-new-tab="true">user-controlled contrast</app-froala-tooltip-element>.</p>

Simplified tablet UI showcasing the application of surface roles, shown in light theme

<p>New tone-based surface colors offer more flexibility and support</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln9urd5o-%5B1P%5D%20what-is-new-surface.png?alt=media

<p id="isPasted">Technical changes were made to align the color system with Android SysUI:</p><ul><li>Updated the default light theme surface from tone 99 to tone 98</li><li>Updated the chroma for the neutral palette, increasing it from 4 to 6</li><li>Slightly darkened surface roles in dark theme</li></ul>

Before and after swatch of the default light theme surface, showcasing the difference in chroma and tone

<p>Changes in tone and chroma in the default light theme surface</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln9urxta-chroma-tone-update.png?alt=media

<p>Feb 2023</p><h3 id="isPasted">Additional accent colors</h3><p>Additional accent colors in the scheme provide more flexibility and choice for color application. In particular, a new set of <app-froala-tooltip-element description="Fixed colors keep the same color value in light and dark themes, as opposed to regular container colors, which change tone between themes, or static colors, which don't change at all." link-label="More on fixed colors" link-url="/m3/pages/color-roles/tab-1#26b6a882-064d-4668-b096-c51142477850" should-open-link-in-new-tab="true">fixed colors</app-froala-tooltip-element> for the <strong>primary</strong>, <strong>secondary</strong>, and <strong>tertiary</strong> accent groups provide colors which stay the same across light and dark themes.</p>

Fab and star icon show in fixed and fixed dim roles, in both light and dark theme

<p>Additional accent colors provide more choice for color application</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln9utr1z-whats-new-fixed-colors.png?alt=media

## How the system works

<h2>It's like paint-by-number</h2>

<p>Imagine your product screen as a paint-by-number canvas:</p><ul><li>Each element on the screen has a number</li><li>Each number is assigned a color</li></ul>

UI in "x-ray" view where each element has a number instead of a color

<p>Each part of a UI is assigned a "number," and each "number" is assigned a color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4mxjs2l-1.png?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">You can hand-pick a color for every "number" to create a static color scheme.</span></p>

Green icon button in the UI, assigned a hand-picked color using a color picker

<p>Static colors are hand-picked, like this green icon button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4mxjwiz-2.png?alt=media

<p>But now, you can also use Material's dynamic color system to automatically generate an entire palette of accessible colors for each "number" from a single source.</p><p>This source can be a user's wallpaper, or in-app content like imagery. If the source changes, the product colors update to match.</p>

Image showcasing how a source color is automatically applied to each "number"

<p>Colors are generated dynamically from a user's wallpaper or in-app content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4mxk5mu-3.png?alt=media

<p>You can customize how dynamic color appears in your product by:</p><ul><li>Setting the color source</li><li>Adding static or harmonized colors</li><li>Changing which "numbers" are assigned to which elements</li></ul><p><a href="/m3/pages/advanced/define-new-colors">Learn about advanced customizations</a></p>

Image showing a color wheel where a light red color is picked, which then populates the UI. In this example, some UI elements have been mapped to different "numbers"

<p>The color source can be changed, automatically changing the color scheme. The UI elements can have other "numbers" assigned to them.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm4mxkasm-4.png?alt=media

<h2>Essential terms</h2>

<h3>Color role </h3><p>Like the "numbers" on a paint-by-number canvas, color roles are assigned to specific UI elements. They have semantic names like <strong>primary</strong>, <strong>on primary</strong>, and <strong>primary container,</strong> and matching color tokens. <a href="/m3/pages/color-roles" target="_blank" rel="noopener noreferrer">See all color roles</a></p><h3>Dynamic color</h3><p>Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI. If the user's wallpaper or the in-app content changes, the colors in the UI will change to match.</p><h3>Static color</h3><p>UI colors that don't change based on the user's wallpaper or in-app content. Static colors can be hand-picked or generated in design tools like the <app-froala-tooltip-element description="Material Theme Builder (MTB) is a Figma plugin that allows markers to emulate the color extraction process for dynamic color and create custom tonal schemes." link-label="Material Theme Builder" link-url="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" should-open-link-in-new-tab="true">Material Theme Builder</app-froala-tooltip-element>. Once assigned to their respective color roles and UX elements, the colors remain constant.</p><h4><strong>Baseline static color</strong></h4><p>The default static color scheme for Material products. <a href="/m3/pages/static/">See the baseline color scheme</a></p>

Diagram illustrating the steps from source color to key colors to tonal palettes to color roles to the UI

<p>The dynamic color process is automatic. A single source color is used to generate five key colors, which are used to make tonal palettes. Tones from the palettes are then assigned to color roles, which are in turn assigned to elements of the UI.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln9uzzb5-from-source-color-to-UI.png?alt=media

How dynamic color schemes are created.

<p>The system generates dynamic color schemes using colors from images like wallpapers and in-app content</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Flinbo537-MAT020.03-v3.mp4?alt=media

<h2>How dynamic color generates color schemes</h2>

<h3>1. It starts with a source color</h3><p>There are three ways to get a source color.</p>

<h4><strong>A. Generate it from a wallpaper</strong></h4><p id="isPasted">User-generated color is sourced from a user's personal wallpaper. The wallpaper is digitally analyzed through a process called quantization, and a single color is selected as the source color.</p>

Red source color is extracted from a wallpaper

<p>Source color from a user's wallpaper</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln9v1jfc-wallpaper-source-color.png?alt=media

<h4 id="isPasted" style="box-sizing:border-box;font:400 16px / 1.5rem"><strong>B. Generate it from in-app content</strong></h4><p>Content-based color is sources from in-app content, like an album thumbnail image, logo, or video preview. </p><p>Like user-generated color, the image is digitally analyzed through quantization, and a single color selected as the source color.</p>

Blue source color is extracted from an podcast cover

<p>Source color from in-app-content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln9v2356-in-app-content.png?alt=media

<h4 id="isPasted" style="box-sizing:border-box;font:400 16px / 1.5rem"><strong>C. Pick it by hand</strong></h4><p id="isPasted">A hand-picked source color is deliberately selected by a designer.</p><p><strong>Did you know? </strong>The <app-froala-tooltip-element description="Baseline is the default static color scheme for Material products. It includes colors for both light and dark themes." link-label="More on baseline color" link-url="/m3/pages/static/" should-open-link-in-new-tab="true">baseline static color scheme</app-froala-tooltip-element> uses a hand-picked source color.</p>

Green source color selected from a color picker

<p>Source color hand-picked by a designer </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln9v32x5-hand-picked-color.png?alt=media

<h3 id="isPasted">2. Feed the source color into an algorithm</h3><p>Dynamic color is powered by the <a href="https://github.com/material-foundation/material-color-utilities" rel="noopener noreferrer" target="_blank">Material Color Utilities</a> (MCU), a set of color libraries containing algorithms and utilities that develop color themes and schemes in your app.</p><p>There are many color algorithms, but the most common ones are:</p><ul><li><strong>User-generated color algorithm<br /></strong>Uses personal wallpaper to identify source color. Maps colors of specific tones (lighter or darker) into the scheme according to a combination of system design choices and user preferences.<br /><br /></li><li><strong>Content-based color algorithm</strong><br />Uses image for source color. Tones are adjusted to match the appearance of the source image, while maintaining accessible contrast. <br /><br /></li><li><strong>Custom colors </strong><br />Colors closely match the chosen input colors, such as those representing brand or semantic meaning.</li></ul>

Color palette made by the user-generated algorithm

<p>1. When run through the <strong>user-generated color</strong> algorithm, the source color is turned into a full color scheme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln9v56si-content-vs-user-left-user.png?alt=media

Color palette made by the content-based algorithm

<p id="isPasted">2. When run through <strong>content-based color</strong> algorithm, the same source color creates a slightly different color scheme. Some tones are adjusted to better match the appearance of the source image.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln9v5j63-content-vs-user-right-content.png?alt=media

Color palette made by the custom color algorithm

<p id="isPasted">3. Custom colors, such as brand colors, can individually run through the algorithm to create a custom scheme that matches the brand</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flnc8pq3o-content-vs-user-right-content.png?alt=media

<h3>3. The algorithm generates key colors</h3>

<p>Material's color algorithms manipulate the source color's <app-froala-tooltip-element description="Hue is the perception of a color as red, orange, yellow, green, blue, violet, and so on." link-label="More on hue, chrome, and tone" link-url="/m3/pages/color/how-the-system-works#395813c8-b314-48d1-bb55-266f421eb3a4" should-open-link-in-new-tab="true">hue</app-froala-tooltip-element> and <app-froala-tooltip-element description="Chroma is how colorful or neutral (grey, black or white) a color appears." link-label="More on hue, chrome, and tone" link-url="/m3/pages/color/how-the-system-works#395813c8-b314-48d1-bb55-266f421eb3a4" should-open-link-in-new-tab="true">chroma</app-froala-tooltip-element> to generate <strong>five complimentary key colors</strong>.</p><ol><li>Primary</li><li>Secondary</li><li>Tertiary</li><li>Neutral</li><li>Neutral variant</li></ol>

Diagram of a source color generating five key colors: primary, secondary, tertiary, neutral and neutral variant

<p>A source color generates five key colors</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln9w1sps-from-source-color-to-key-colors.png?alt=media

<h3>4. The algorithm creates tonal palettes</h3><p>The system then manipulates <app-froala-tooltip-element description="Tone is how light or dark a color appears. Tone is sometimes also referred to as luminance." link-label="More on hue, chroma, and tone" link-url="/m3/pages/color/how-the-system-works#dc7848f3-b094-4f9a-9e50-bfa5a5029617" should-open-link-in-new-tab="true">tone</app-froala-tooltip-element> and <app-froala-tooltip-element description="Chroma is how colorful or neutral (grey, black or white) a color appears." link-label="More on hue, chroma, and tone" link-url="/m3/pages/color/how-the-system-works#e4d1c787-e92f-4d6e-a757-cd6d5c3b298e" should-open-link-in-new-tab="true">chroma</app-froala-tooltip-element> values to create a <strong>tonal palette</strong> for each key color. Colors in these palettes are given a number from 0 to 100 in increments of 10, as well as 95, 98, and 99. Some palettes include more values.</p>

Primary, secondary, tertiary, neutral and neutral variant tonal palettes, consisting of 13 tonal steps

<p>The smaller the tonal value, the darker the color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm612xcmj-13.png?alt=media

<h3>5. The algorithm assigns tones to color roles</h3><p>The algorithm uses <app-froala-tooltip-element description="For example, a dark surface color is algorithmically paired with a light text label color so the UI automatically meets contrast requirements." link-label="More on color relationships" link-url="/m3/pages/color/how-the-system-works#e1e92a3b-8702-46b6-8132-58321aa600bd" should-open-link-in-new-tab="true">accessible color relationships</app-froala-tooltip-element> to <strong>assign specific tones to the 26 </strong><strong><app-froala-tooltip-element description="Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme." link-label="More on color roles" link-url="/m3/pages/color-roles" should-open-link-in-new-tab="true">color roles</app-froala-tooltip-element></strong> in both light and dark theme.</p>

<p>For example, the algorithm assigns the color tone primary40 to the <strong>p</strong><strong>rimary</strong> role and the tone primary100 to the <strong>o</strong><strong>n primary</strong> role.</p><p><a href="/m3/pages/color-roles" target="_blank" rel="noopener noreferrer">See all color roles</a></p>

Diagram mapping color tones to roles

<p>Tones from the tonal palette are assigned to different roles</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm612xkza-14.png?alt=media

Diagram of tonal palettes mapped to all color roles across light and dark themes

<p>Colors from the five tonal palettes are assigned to color roles. For example, primary roles are picked from the primary tonal palette, while surface roles are picked from the neutral tonal palette.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm612xrj4-15.png?alt=media

<p><app-froala-tooltip-element description="A dark theme is a low-light version of a UI that displays mostly dark surfaces." link-label link-url should-open-link-in-new-tab="false">Dark theme</app-froala-tooltip-element> colors are also automatically assigned so that apps receive both light and dark themes through a single set of color roles.</p>

Diagram of dark theme colors

<p>The same color roles are used in light and dark themes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flnem28e4-color-roles-dark-theme.png?alt=media

<h3>6. The new colors are applied to the UI</h3><p>The 26 standard color roles are already assigned to elements of the UI. When a new source color is picked, the UI dynamically changes color.</p>

Diagram of all the color roles with an example of how it would look applied to a UI

<p>Color roles assigned to the UI</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Flna5nn2o-color-roles-UI-elements.png?alt=media

<h2>Color roles support three levels of contrast</h2>

<p id="isPasted">In addition to light and dark theme, color roles also support three levels of contrast. This helps people select the contrast setting that best suits their vision needs:</p><ul><li>Standard (default)</li><li>Medium</li><li>High</li></ul><p>The standard contrast emphasizes visual hierarchy using high and low contrast elements. People with vision disabilities may choose medium or high contrast options for better support.</p>

Email app in standard contrast.

<p><strong>Standard contrast</strong></p><p>The baseline color scheme already uses mixed levels of contrast to reduce cognitive load</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmrwa95yk-18.png?alt=media

Email app in medium contrast.

<p><strong>Medium contrast</strong></p><p>Provides a minimum contrast ratio of 3:1 for those who need more contrast, but may experience visual discomfort with higher contrasts from effects like halation.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmrwa99t2-19.png?alt=media

Email app in high contrast.

<p><strong>High contrast</strong></p><p id="isPasted">Further emphasizes essential elements with a 7:1 contrast ratio to reduce visual distractions and enable users to focus. For example, high contrast is applied to the content in a card but not the card container.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmrwa9f4u-20.png?alt=media

<p>The contrast settings are automatically applied to both light and dark themes. </p>

The same mail app at three contrast levels, all in light theme.

<p>Light theme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmrwa9ldv-21.png?alt=media

The same mail app at three contrast levels, all in dark theme.

<p>Dark theme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmrwa9q8s-22.png?alt=media

<p>Custom components can support contrast levels by using Material's appropriate <app-froala-tooltip-element description="Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme." link-label="More on color roles" link-url="/m3/pages/color-roles" should-open-link-in-new-tab="true">color roles</app-froala-tooltip-element>. For example, use <strong>primary container</strong> and <strong>on primary container</strong>.</p><p>Use <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on design tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true" id="isPasted">design tokens</app-froala-tooltip-element> to apply color roles to custom components.</p>

Custom volume slider component using Primary Container and On Primary Container roles, whose colors change automatically at standard contrast.

<p>A custom volume slider can use <strong>p</strong><strong>rimary container</strong> and <strong>on primary container </strong>color roles to support contrast levels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Flna5s0mi-user-controlled-contrast_12.png?alt=media

Custom volume slider component using Primary Container and On Primary Container roles, whose colors change automatically at standard contrast.

<p><span style="white-space:pre-wrap">At medium and other contrast levels, those color roles apply the necessary new color values</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Flna5shuk-user-controlled-contrast_13.png?alt=media

<h2>Pairing accessible tones</h2>

<p>The system manipulates hue, chroma, and tone (<app-froala-tooltip-element description="HCT is a color space which defines all colors by assigning number values for three dimensions: hue, chroma, and tone." link-label="More on hue, chroma, and tone" link-url="/m3/pages/color/how-the-system-works#395813c8-b314-48d1-bb55-266f421eb3a4" should-open-link-in-new-tab="true">HCT) values</app-froala-tooltip-element> to <strong>create a tonal palette for each color</strong> with tones ranging from 0 to 100.</p><p>Color has physical limitations—whether it's actual physics, our own biological visual limitations, or the limitations of on-screen color rendering. For example, some hues cannot exist with certain chroma or tones. Color limitations are the reason colors such as bright light blue or bright light red are not quite possible. This is why the chroma value may increase or decrease for some tones in a tonal palette.</p>

13 tones derived from a key color. 

<p>Tonal values range from 0 (black) to 100 (white). The smaller the tonal value, the darker the color.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm612y8rt-25.png?alt=media

<p>Material's color algorithms use these palettes to find and <strong>pair contrasting tones, </strong>creating accessible color combinations.</p>

<p id="isPasted">Because tone can describe the lightness or darkness of a color, it's used to define accessible color relationships. Those relationships are built into Material's color algorithms.</p><p>For example, the algorithms assign a dark tone to a button's container color and a light tone to its label color, ensuring that the colors have a 3:1 contrast.</p>

Colors of tones 50 and 98 used for button fill color and background fill color, which create a contrast greater than 3:1 between a button and its background.

<p>Using tones 50 and 98 for a button and its label creates an accessible 3:1 contrast</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm612yd3c-26.png?alt=media

<p>For even more contrast, the algorithms assign tones even farther apart, achieving a 7:1 contrast.</p><p>This is the concept powering <strong>user-controlled contrast</strong> features.</p>

Colors of tones 30 and 98 used for button fill color and background fill color, which create a contrast greater than 7:1 between a button and its background.

<p>Using colors of tones 30 and 98 for a button and its label create a 7:1 contrast</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6134eza-27.png?alt=media

<h2>Defining colors with hue, chroma, and tone (HCT)</h2>

<p id="isPasted"><strong>The system uses a color space called HCT</strong>, which defines all colors using three dimensions: hue, chroma, and tone.</p><p>Changing HCT values lets you manipulate colors in flexible but predictable ways. Unlike other color spaces (like HSL or RGB), HCT allows the manipulation of a color's hue and chroma without affecting its tone. Watch to learn more:</p>

Animated video explaining the three color dimensions (hue, chroma, and tone) and how they relate to accessible color schemes.

<p>Hue, chroma, and tone are the three color dimensions used to create accessible color schemes</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Four-fake-design-system%2Fimages%2Flfmpm0pq-MAT020.02-v3.mp4?alt=media

<h3>Hue</h3><p>Hue is the perception of a color as red, orange, yellow, green, blue, violet, and so on. Hue is quantified by a number ranging from 0-360 and is a circular spectrum (values 0 and 360 are the same hue).</p>

The hue spectrum looks like a rainbow circle.

<p>360 degree <strong>hue</strong> spectrum</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Flna5w3u0-hue.png?alt=media

<h3>Chroma</h3><p>Chroma is how colorful or neutral (grey, black or white) a color appears. Chroma is quantified by a number ranging from 0 (completely grey, black or white) to infinity (most vibrant), though Chroma values in HCT top out at roughly 120.</p><p>Because of biological and screen rendering limitations, different hues and different tones will have different maximal chroma values.</p>

Diagram showing chroma range from 120 (maximum intensity) to 0 (pure grey). A second diagram shows how pure black and pure white also correspond to 0 chroma

<ol><li><span style="white-space:pre-wrap">The higher the color purity, the higher the <strong>chroma</strong></span></li><li><span style="white-space:pre-wrap">Note how lightening and darkening a hue also affects its <strong>chroma</strong> value</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Flna5x1is-chroma.png?alt=media

<h3>Tone</h3><p>Tone is how light or dark a color appears. Tone is sometimes also referred to as luminance. Tone is quantified by a number ranging from 0 (pure black, no luminance) to 100 (pure white, complete luminance).</p><p>Tone is crucial for visual accessibility because it determines contrast. Colors with a greater difference in tone create higher contrast, while those with a smaller difference create lower contrast.</p>

Gradient showing the range of tones from 1 (black) to 100 (white)

<p>The 100 <strong>tone</strong> is always 100% white, the lightest <strong>tone</strong> in the range; the 0 <strong>tone</strong> is 100% black, the darkest<strong> tone</strong> in the range</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Flna5xncz-tone.png?alt=media

<h3>HCT isn't interchangeable with other color spaces</h3><p>Values from models like hue, saturation, and lightness (HSL) won't perfectly map to Material's hue, chroma, and tone (HCT). Don’t conflate color spaces when inspecting or adjusting colors.</p><p>For example, colors with the same perceived brightness share the same tone value in HCT, but can have different HSL lightness values.</p>

3 color dots with the same HCT tone of 78, and varying HSL lightness values of 83, 65, and 77.

<p>HCT tone values remain constant when they have the same perceived brightness, while HSL lightness values can vary</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmrwafnpo-31.png?alt=media
