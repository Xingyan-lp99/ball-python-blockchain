# Static color schemes

Source: https://m3.material.io/styles/color/static
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/247d635f-924c-4e83-8383-94965fe769e2.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Static color schemes are ideal for branded products that should have a consistent, uniform design

## Baseline

<p><strong>Baseline</strong> is the default static color scheme. It uses accessible color pairings and includes colors for both light and dark themes.</p><p><strong>With the baseline color scheme, end-users see</strong></p><ul><li>An accessible UI with static colors </li></ul>

Mobile screenshot of music app.

<p>Music app with the static baseline color scheme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4k1tpg9-5.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/6Qlfeo75opgKmNSYcxRy92aHk4VOLoQrE4VFYmSSfElw9CrWNI12sziVlF4ZPyEjADYSrfLICk2zmSSwBPFIMbnWlvCdL9LN7ko5LyWAaVQ3=s656

Tablet screenshot of a news app.

<p>News app with the static baseline color scheme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmlikbtg5-6.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/_8Vtp4zasYWpnr556HQJFq60r0jwZw9541OZ7JtkFYG0Ol4LmRidQA_ABD2bMWZCYPodMyV3LvVF8Fsq7XU2EB58utMivnnLwPRLgZkri7E=s1352

<h2>Baseline colors</h2><p>Get baseline colors in Figma using the <app-froala-tooltip-element description="Material Theme Builder (MTB) is a Figma plugin that allows markers to emulate the color extraction process for dynamic color and create custom tonal schemes. " link-label="Get the MTB" link-url="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" should-open-link-in-new-tab="true">Material Theme Builder</app-froala-tooltip-element>.</p>

Color swatches showing the entire baseline color scheme and derivative accent colors.

<p>Baseline scheme colors in light theme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flnomy8pz-static-baseline-colors-lt.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/rfxJv95pIoJ3cEZ9ypfimJFC5Ps8sEEVBNWD36C-fy3DYvec8J_VLRosBkwTNsnpSCgSpxWXBypOXT8Ydm4fJOQ2ajWoy7SjocrzJcK7KA8=s2048

Color swatches showing the entire baseline color scheme and derivative accent colors.

<p>Baseline scheme colors in dark theme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flnomz44y-static-baseline-colors-lt-1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/S-tgf061eUWcbEBhyicTYR9PWVDeXSsSgZ2e2yYSr6Jn4W-F9z5czZCG6sv58wgJQODQakVRBDvUX5gaotfq3BuqMDLROrCO4D0Kz9F494LW=s2048

<h2>Baseline color tokens</h2>

resourceName: designSystems/20543ce18892f7d9

libraryModuleType: COLOR

moduleConfigurationOverrides: {'tokenSets': ['Color schemes', 'Palettes'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Design with baseline</h2>

<h3>Use the Design Kit and M3 baseline colors in new design files</h3><ol class="decimal"><li><p>Create your Figma file. Enable the <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">M3 Design Kit</a> in your Assets panel.</p></li><li><p>Compose screens and layouts using Material Components from the design kit</p></li><li><p>Apply M3 baseline color roles to custom components and UI elements by hovering on the element's color property in the Design panel on the right of the screen and selecting the <strong>Style</strong> icon (four dots). This opens a selection dialog.</p></li><li><p>Search for "M3" to see the baseline color roles</p></li><li><p>Select the baseline color role that most closely matches the use case and intent (see <a href="/m3/pages/color-roles" target="_self">Color roles</a> for more information on what color to use where)</p></li><li><p>Repeat until all custom elements are using M3 baseline color roles</p></li></ol><p></p><h3>Apply baseline colors to an existing file</h3><p><strong>First, get the M3 baseline colors into your file</strong></p><ol class="decimal"><li><p>Open your Figma design file. Select the <strong>Actions</strong> menu (or Ctrl/Command+K). </p></li><li><p>Find the <a href="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" target="_blank">Material Theme Builder plugin</a> and select <strong>Run</strong>. This will open a plugin dialog showing the default color scheme, including Core colors and Extended colors.</p></li><li><p>Open the plugin's <strong>Settings</strong> (gear icon at lower right of dialog) and select the checkbox for <strong>Generate State Layers</strong>. This makes sure there are color for the state layers needed to design interactions. <a href="/m3/pages/interaction-states/state-layers" target="_blank">Learn more about state layers</a></p></li><li><p>Navigate out of settings.</p></li><li><p>With the Current Theme dropdown at the top of the dialog, select <strong>Baseline.</strong></p></li><li><p>Select the frames or components in your file and then hit <strong>Swap</strong> in the bottom right of the dialog. This will automatically update the colors for any M3 Design Kit components.</p></li></ol><p><strong>Then, update any remaining non-M3 color styles</strong></p><ol class="decimal"><li><p>Manually change any hex values or non-M3 color styles by selecting all and looking through the Selection colors in the Design panel on the right of the screen.</p></li><li><p>Any colors that don't start with "M3" need to be replaced with a corresponding baseline color.</p></li><li><p>Hover on a non-M3 color row in the Design panel and select the <strong>Style</strong> icon (four dots). This opens a selection dialog.</p></li><li><p>Search for "M3" to see the baseline color roles.</p></li><li><p>Select the baseline color role that most closely matches that color's use case (see <a href="/m3/pages/color-roles" target="_self">Color roles</a> for more information on what color to use where) and select <strong>Use style</strong> to apply it to the selected objects.</p></li><li><p>Repeat until all non-M3 colors in the file have been replaced with M3 baseline color roles.</p></li></ol><p><strong>Need to make adjustments to the scheme? Check out </strong><a href="/m3/pages/advanced/overview" target="_self"><strong>Advanced customizations</strong></a></p>

## Custom brand

<p>In a brand-based static scheme, the colors are hand-picked by your team to align with your product's brand color. Brand-based schemes are entirely created and maintained by your team, so this approach requires a larger investment of time and effort.</p><p id="isPasted"><strong>With a brand color scheme, end-users see</strong></p><ul><li>An accessible UI with static colors</li><li>A product that "looks like its brand"</li></ul>

Left: A swirling red, magenta and green sphere representing a meditation app logo. Center: A color scheme created from the three brand colors in the sphere. Right: A screen of the meditation app colored in red, magenta, and green UI.

<p>This example meditation app uses a static scheme created from its brand colors.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgm3sandbox%2Fimages%2Fln4ilrfy-brand-baseline.png?alt=media

<h2>Create a custom brand color scheme</h2>

<ol class="decimal"><li><p>Open your Figma design file. Select the <strong>Actions</strong> menu (or Ctrl/Command+K). </p></li><li><p>Find the <a href="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" target="_blank">Material Theme Builder plugin</a> and select <strong>Run</strong>. This will open a plugin dialog showing the default color scheme, including Core colors and Extended colors.</p></li><li><p>Open the plugin's <strong>Settings</strong> (gear icon at lower right of dialog) and select the checkboxes for both <strong>New theme color diagram</strong> and <strong>Generate State Layers</strong>. This will create a handy visualization of your branded color scheme and also generate state layers essential for designing interactions. <a href="/m3/pages/interaction-states/state-layers" target="_blank">Learn more about state layers</a></p></li><li><p>Navigate out of settings.</p></li><li><p>Open the Current Theme dropdown at the top of the dialog and select <strong>+ ADD NEW THEME.</strong></p></li><li><p>Give your theme a short name (this name will become the prefix of your color roles in Figma).</p></li><li><p>Select <strong>ADD THEME.</strong></p></li><li><p>With <strong>Custom</strong> selected, select <strong>Primary</strong>. This opens a dialog prompting you to select a custom source color.</p></li><li><p>Enter the Hex value for your brand color and hit <strong>Apply</strong>.</p></li></ol><p>This will generate a full custom color scheme. You can use the scheme as-is or repeat steps 5 and 6 to set custom sources for the Secondary, Tertiary, Error, Neutral, and Neutral Variant colors.</p><p><strong>Want to further adjust your brand color scheme? Check out </strong><a href="/m3/pages/advanced/overview" target="_self"><strong>Advanced customizations</strong></a></p>

<h2>Design with brand colors</h2>

<h3 id="isPasted">Use brand colors in new design files</h3><ol><li>Create your Figma file. Enable the <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank" rel="noopener noreferrer">M3 Design Kit</a> in your Assets panel.</li><li>Copy your scheme's color diagram and paste it into the file (this makes the color roles available in the Design panel on the right of the screen as part of your local styles)</li><li id="isPasted">Apply your brand color roles to custom components and UI elements by hovering on the element's color property in the Design panel on the right of the screen and selecting the <strong>Style</strong> icon (four dots). This opens a selection dialog.</li><li>Search for your theme's name to see your brand color roles</li><li>Select the brand color role that most closely matches the use case and intent (see <a href="/m3/pages/color-roles">Color roles</a> for more information on what color to use where)</li><li>Repeat until all custom elements are using your brand color roles</li></ol><p><br /></p><h3>Apply brand colors to an existing file or M3 Design Kit components</h3><p><strong>First, get your brand colors into your file</strong></p><ol><li>Copy your scheme's color diagram and paste it into the file (this makes the color roles available in the Design panel on the right of the screen as part of your local styles)</li></ol><p><strong>Swap colors in M3 Design Kit components for your brand colors</strong></p><ol><li id="isPasted">Find the <a href="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" target="_blank" rel="noopener noreferrer">Material Theme Builder plugin</a> and select <strong>Run</strong>. This will open a plugin dialog showing the default color scheme, including Core colors and Extended colors.</li><li id="isPasted">In the Current Theme dropdown at the top of the dialog, select your scheme</li><li>Select the frames or M3 Design Kit components in your file that need a color update and then hit <strong>Swap</strong> in the bottom right of the dialog. This will automatically update their colors from baseline colors to your brand colors</li></ol><p><strong>Then, update any remaining non-brand color styles</strong></p><ol><li>Manually change any hex values or non-brand color styles by selecting all and looking through the Selection colors in the Design panel on the right of the screen</li><li>Any colors that don't start with your theme name need to be replaced with a corresponding brand color</li><li>Hover on a non-brand color row in the Design panel and select the <strong>Style</strong> icon (four dots). This opens a selection dialog.</li><li>Search for your theme name to see the brand color roles</li><li>Select the brand color role that most closely matches that color's use case (see <a href="/m3/pages/color-roles">Color roles</a> for more information on what color to use where) and select <strong>Use style</strong> to apply it to the selected objects</li><li>Repeat until all non-brand colors in the file have been replaced with brand color roles</li></ol><p><br /></p><p><strong>Need to make adjustments to the scheme? Check out <a href="/m3/pages/advanced/overview">Advanced customizations</a></strong></p>

<h2>Develop with brand colors</h2>

<ul><li>Export your branded color scheme from the Material Theme Builder (Available for Jetpack Compose, Android Views, Flutter, Web, or as a JSON file)</li><li>Android: <a href="https://developer.android.com/develop/ui/views/theming/themes#CustomizeTheme" rel="noopener noreferrer" target="_blank">Customize the default theme</a></li></ul>
