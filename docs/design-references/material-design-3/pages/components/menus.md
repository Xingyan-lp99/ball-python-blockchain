# Menus

Source: https://m3.material.io/components/menus
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/24b60c3f-1ec7-48df-b175-0d8e011a8106.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li id="isPasted">Use a <strong>menu</strong> to show a temporary set of actions. To show actions on screen at all times, use a <strong><app-froala-tooltip-element description="Toolbars display frequently used actions relevant to the current page." link-label="More on toolbars" link-url="/m3/pages/toolbars/overview" should-open-link-in-new-tab="true">toolbar</app-froala-tooltip-element></strong> instead</li><li>Menus can open from many components, including <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon buttons</app-froala-tooltip-element>, <app-froala-tooltip-element description="The split button opens a menu to give people more options related to an action." link-label="More on split buttons" link-url="/m3/pages/split-buttons/overview" should-open-link-in-new-tab="true">split buttons</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Text fields let users enter text into a UI." link-label="More on text fields" link-url="/m3/pages/text-fields/overview" should-open-link-in-new-tab="true">text fields</app-froala-tooltip-element></li><li><strong>Context menus</strong> provide actions for a specific element, like an image or highlighted text, and usually open with a secondary click</li></ul>

1 vertical menu with vibrant colors opens from a split button, and 1 vertical menu with a submenu.

<p>Vertical menus can include vibrant colors, gaps, dividers, and submenus to organize a list of choices</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhkajj6i-01.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/18d50ef91649dead

libraryModuleType: STATUS_TABLE

<h2>M3 Expressive update</h2>

<p id="isPasted"><strong>November 2025</strong></p><p><strong>Vertical menus</strong> were introduced with new shapes, color styles, selection states, and refined submenu motion. Gaps can be used for a more flexible layout on Android. <a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank" rel="noopener noreferrer">More on M3 Expressive</a></p>

<p id="isPasted">Variants:</p><ul><li>Added <strong>vertical menus</strong>, recommended for new designs</li><li><app-froala-tooltip-element description="Baseline variants are the M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles." link-label="More on M3 Expressive" link-url="https://m3.material.io/blog/building-with-m3-expressive" should-open-link-in-new-tab="true">Baseline</app-froala-tooltip-element> <strong>menu</strong> is still available  </li></ul><p>Color styles: </p><ul><li>Standard</li><li>Vibrant</li></ul>

A vertical menu using shape and vibrant color to show a selected state.

<p>Vibrant colors help selected menu items stand out</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhk9jsmw-02.png?alt=media

<h2 id="isPasted">Differences from M2</h2>

<ul id="isPasted"><li dir="ltr" id="isPasted"><strong>Color</strong>: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></li><li dir="ltr"><strong>Variants</strong>: Dropdown menu and exposed dropdown menu are now both referred to as menu, since they differ only in the element which opens the menu surface</li></ul>

Menu with gray color.

<p>M2: Former menu colors don’t contrast with the background </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi5n1krh-4.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/lRkDtzZzv1cQwgvOMTY_hxx5v6LvsZjXrAo_zSvv-cqgB6vH92PvSw1XJMN925XPqGDdMB1OgVKZcud6-w4b9LZg709o_yEZGMjqyhsgs6Wz=s656

Menu with purple background and outline.

<p>M3: Menus feature new color mappings and dynamic color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhlt7xid-04.png?alt=media

## Specs

<h2>Variants</h2>

<h3>Vertical menus</h3>

<p>Use vertical menus for a more expressive look and feel, including rounded corners, standard and vibrant color styles, more selection states, and submenu motion.</p>

2 vertical menus use shape and color to indicate selected state.

<ol class="decimal"><li id="isPasted">Vertical menu with gap</li><li>Vertical menu with divider</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp3tuy7-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ryW1crRfja9xt_7sPlT_XlF64XPHQjHmk6HkJ91EP23gfGW2Z1TNt8V1RsaAEt4bzOOow6wEtTrB4tk32rzhd4WL2dVMKVlbh3x6ZD3oqdK7=s2048

<h3>Baseline variant</h3>

<p>In M3 Expressive, <app-froala-tooltip-element description="Baseline variants are the original M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles." link-label="More on M3 Expressive" link-url="https://m3.material.io/blog/building-with-m3-expressive" should-open-link-in-new-tab="true">baseline</app-froala-tooltip-element> menu is still available to use, but doesn’t have the latest shapes, color styles, selection states, and motion. <a href="/m3/pages/menus/specs#a80df2f9-8610-4ce0-b3a3-b9ee749d5c98" target="_self">See baseline menu specs</a></p>

A baseline menu variant with square corners and standard colors.

<p>A baseline <strong>menu</strong> has square corners, as compared to a <strong>vertical menu’s</strong> round corners and expressive styling</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp47zoj-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/I8AoQRDKlS29lSyVHYVs4-2PKXVQUXC_wlPJx5IT1hWiga7bEC7DZUlNH_OEoICZN5hCf8ii45dpApcg23TY6JhadwCluvznISW6HNfGKHUc=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="text-align:center"><p><strong>Variant</strong></p></th><th style="text-align:center"><p><strong>M3</strong></p></th><th style="text-align:center"><p><strong>M3 Expressive</strong></p></th></tr></thead><tbody><tr><td><p>Vertical menus</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td><p>Menu (<app-froala-tooltip-element description="Baseline variants are the original M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles." link-label="More on M3 Expressive" link-url="https://m3.material.io/blog/building-with-m3-expressive" should-open-link-in-new-tab="true">baseline</app-froala-tooltip-element>)</p></td><td><p>Available</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Configurations</h2>

<h3>Vertical menus layout</h3>

2 menus: 1 standard, and 1 with a gap, creating groups.

<ol class="decimal"><li id="isPasted">Standard</li><li>Grouped</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp4bydj-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/fJlPTJ2NqSiweyHvIr8M0iPk67mplnSmEnq_2SEOW1OvhT31iv4txdTlYrXWpNvmmBVVfJJzaE_lPSakS5hW51-I3oC8XuRu0l2lxGxm7zXi=s2048

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="text-align:center;width:22.7376%"><strong>Category<br /></strong></th><th style="text-align:center;width:31.6459%"><strong>Configuration<br /></strong></th><th style="text-align:center;width:20.5317%"><strong>M3</strong></th><th><div style="text-align:center"><strong>M3 Expressiv</strong><strong>e</strong></div></th></tr></thead><tbody><tr><td rowspan="2" style="text-align:center">Color</td><td>Standard</td><td>Available</td><td>Available</td></tr><tr><td>Vibrant</td><td>--</td><td>Available</td></tr><tr><td rowspan="2" style="text-align:center">Layout</td><td>Standard</td><td>Available</td><td>Available</td></tr><tr><td>Grouped</td><td>--</td><td>Available</td></tr></tbody></table></div>

<h2>Tokens &amp; specs</h2>

<p>Browse the component elements, attributes, tokens, and their values. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/385a28e5d3bb3dd0

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Menus - Common', 'Menus - Color - Vibrant', 'Menus - Color - Standard'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['Menu (baseline)', 'Menus - Common', 'Menus - Color - Vibrant', 'Menus - Color - Standard'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Anatomy</h2>

<h3>Vertical menus</h3>

A diagram of a vertical menu.

<ol class="decimal"><li id="isPasted">Menu item </li><li>Leading icon (optional)</li><li>Menu item text</li><li>Trailing icon (optional)</li><li>Badge (optional)</li><li>Trailing text (optional)</li><li>Container</li><li>Supporting text (optional)</li><li>Label text (optional)</li><li>Gap (optional)</li><li>Divider (optional)</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp4i2in-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/AfTrO7v-T_4xnHi8Fa-xmOOn21wmjYQWZ9CqSCVGaG910Nd8K4lS3FqfcNgYQ0iF4FSY12e_AEjX1WNsFOOM02AuYBuTSGrwaTpCPKxUNBAQ=s2048

<h2>Color</h2>

<p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p>

<p id="isPasted">Menus have two color mappings:</p><ul><li>Standard: Surface-based</li><li>Vibrant: Tertiary-based</li></ul><p>These mappings provide options for lower or higher visual emphasis. Vibrant menus are more prominent so should be used sparingly.</p>

2 vertical menus: 1 with lower visual emphasis, and 1 vibrant menu with bold shades.

<ol class="decimal"><li id="isPasted">Standard color scheme</li><li>Vibrant color scheme</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp4jv7k-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/UQTohIy6KP6b1-pM2Mvhf_SyQW6J3ibpKvf3Z5T8dI48XoYQ6DqhwG5ILCidkiXxCje50h4Tdx6VPzv1-2LVN2sSo_4JfItM9mhfrHEdHV8H=s1352

<h3>Standard colors</h3>

2 vertical menus with standard color roles mapped to 11 elements.

<p id="isPasted">Vertical menus color roles used for light and dark themes:</p><ol class="decimal"><li>On surface variant</li><li>On surface</li><li>On surface (state layer)</li><li>Surface container low</li><li>On surface variant</li><li>On surface variant</li><li>Tertiary container (selected)</li><li>On tertiary container (selected)</li><li>On surface variant</li><li>On surface variant</li><li>On tertiary container (selected)</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp4r65m-08-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/nA4wviKihXfkWje8PlNIZNpYajfpoudcjVm30OYpC8UdMEdquwj9QeSziFOs7KjJ3IR-fioXjTLMlZsyKMaUgi3Bfy70RpHTCCsGaJX5hWkc=s2048

<h3>Vibrant colors</h3>

2 vertical menus with vibrant color roles mapped to 11 elements.

<p id="isPasted">Vertical menus color roles used for light and dark themes:</p><ol class="decimal"><li>On tertiary container</li><li>On tertiary container</li><li>On tertiary container (state layer)</li><li>Tertiary container</li><li>On tertiary container</li><li>On tertiary container</li><li>Tertiary (selected)</li><li>On tertiary (selected)</li><li>On tertiary container</li><li>On tertiary container</li><li>On tertiary (selected)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp4scno-10-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/6B9lmZdfYRC5nkKI-x6hS9U37bZC1o0jRWDkYe90mc-TV-OjPicvEckz5sYKYsoyP2hRO_hR3An76jKHGR-b8qAYp_56q49AgW4kMo8Ez98=s2048

<h2 id="isPasted">States</h2><p><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element> are visual representations used to communicate the status of a component or an interactive element. <a href="/m3/pages/interaction-states/overview" target="_blank" rel="noopener noreferrer">More on interaction states</a><br /><br />Shape morphing in vertical menus creates an expressive active state. As focus moves between submenus, the corner shape changes to highlight the active menu. <a href="/m3/pages/menus/guidelines#7cc1d01b-a454-48c7-8306-e60347ffd17f" target="_blank" rel="noopener noreferrer">More on menu focus</a></p>

6 vertical menu states in light and dark themes.

<ol class="decimal"><li id="isPasted">Enabled</li><li>Disabled</li><li>Hovered</li><li>Focused</li><li>Pressed</li><li>Active (main menu reveals submenu)</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp4upew-14-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/9y63FlzafeIP9Tth6PTh9NKO6wwrYUZqCs6PTUKqIQPfYd7apIWRsvYx91maUHu43E0GoIkm7nDVC_DZA6K-15ItBpV-1KJ550QZCGSHlzo8=s2048

<h2>Measurements</h2>

Vertical menu marked with spacing and padding measurements.

<p>Vertical menu padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi5nwcqt-17-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/SyybBdmLyz7BXoGoAF1kjCwXx7BiZvB0e_I7bpFAIDO-W4YGSJ21CKgtu5PdH7J49aZfYEJbVPyjVFN2E9fWBLfUXDP44mP90E_Unc-g3c8=s2048

<h2>Menu (baseline) </h2>

<p>The <app-froala-tooltip-element description="Baseline variants are the original M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles." link-label="More on M3 Expressive" link-url="https://m3.material.io/blog/building-with-m3-expressive" should-open-link-in-new-tab="true">baseline</app-froala-tooltip-element> menu variant is available and continues to work in existing products. However, M3 expressive vertical menus are recommended for new designs. </p>

<h3>Baseline tokens &amp; specs</h3>

<p>Browse the component elements, attributes, tokens, and their values. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/385a28e5d3bb3dd0

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Menu (baseline)'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h3>Anatomy</h3>

Diagram of 6 elements of a baseline menu.

<ol class="decimal"><li id="isPasted">List item </li><li>List item leading icon </li><li>List item trailing icon </li><li>Container</li><li>List item trailing text</li><li>Divider</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp5x7zn-19-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/j5d1I8gfzjOWuHT_-hl99nkZRsYTe7HewZawtXqtHSrfZhzBSF92oFrF4O2icV5C3AUdsRZTxRIgSGBhA37l-s5SWozyvwe70RLG6OwzZUSoQw=s2048

<h3 id="isPasted">Color</h3>

9 color roles of a baseline menu in light and dark themes.

<p id="isPasted">Baseline menu color roles used for light and dark themes:</p><ol class="decimal"><li>On surface variant</li><li>On surface</li><li>On surface - opacity: 0.08</li><li>Surface container</li><li>On surface variant</li><li>On surface variant</li><li>On surface variant</li><li>Surface container highest</li><li>Outline variant</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp5xzj4-20-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/1vrmeDpf2FtiP2c9fRq9p_aeqONtRV3zqmzYfkoIOaJesocpZ19K_ZUuMj99rTWJxwAW_r9WSMEHiVvKYKjwvUcpYtdJ5Vz60I5nTjnhGSR5=s2048

<h3 id="isPasted">States</h3>

<h4>Default menu items</h4>

Diagram numbering the 5 default states of a baseline menu.

<ol class="decimal"><li>Enabled</li><li>Disabled</li><li>Hovered</li><li>Focused</li><li>Pressed </li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp6035c-21-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/9WZ8E98mBPsfeJqGE1w6ExWLXo1jACCCgppiykccySkhqcZCqFfrTs87Gp_XAlUNSqxRdv04cO62X2W3LQamj64dSRw2mEkG86v7cJaYZAI=s2048

<h4>Selected menu items</h4>

5 states of a selected baseline menu item.

<ol class="decimal"><li id="isPasted">Enabled</li><li>Disabled</li><li>Hovered</li><li>Focused</li><li>Pressed </li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp61n8r-22-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Eg2mSAl6lckNeGZn60i3N6b7ltjvGCbssGUhr-LWmLpa2HDbKhgxvA72PVKqTsT0ho7uQZWaK_buL-Y81PKV7_GpS90CXSbLfCU9JqkRq-Y=s2048

<p><a href="/m3/pages/menus/specs#c811d2fa-469a-4e4e-9d9f-0f535c5c9b4c">State specs are in the token module above</a></p>

<h3>Measurements</h3>

Diagram of a baseline menu’s padding, text alignment, height, and width.

<p>Baseline menu padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp6b6dr-23-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/MRcY8zpznxkaZVmDq-MvnNSUQnLDJ3uftXolOX1MZ7ZczEmBCp4nro5uy3WDlxm8De9S3E9m7yoHTUtCD1IJmm-KOI975AQnrXOePAhR8TWM=s2048

<div class="table-wrapper"><table style="margin-right:calc(0%);width:100%"><thead><tr><th style="text-align:center">Attribute<br /></th><th style="text-align:center">Value<br /></th></tr></thead><tbody><tr><th>Container width<br /></th><td>112dp min, 280dp max</td></tr><tr><th>Corner radius<br /></th><td>4dp</td></tr><tr><th>Vertical label text alignment<br /></th><td>Center-aligned</td></tr><tr><th>Horizontal label text alignment<br /></th><td>Start-aligned</td></tr><tr><th>Left/right padding<br /></th><td>12dp</td></tr><tr><th>Left/right padding with-icon<br /></th><td>12dp</td></tr><tr><th>List item height<br /></th><td>48dp</td></tr><tr><th>Padding between elements within a list item<br /></th><td>12dp</td></tr><tr><th>Divider top/bottom padding<br /></th><td>8dp</td></tr><tr><th>Divider height<br /></th><td>1dp</td></tr><tr><th>Divider width<br /></th><td>Dynamic</td></tr><tr><th>Leading/trailing icon size<br /></th><td>24dp</td></tr></tbody></table></div>

<h3>Configurations</h3>

<p id="isPasted">A baseline menu appears when a person interacts with a button, action, or other control. </p><p>A few examples:</p><ol class="decimal"><li><app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">Button</app-froala-tooltip-element></li><li><app-froala-tooltip-element description="Text fields let users enter text into a UI." link-label="More on text fields" link-url="/m3/pages/text-fields/overview" should-open-link-in-new-tab="true">Text field</app-froala-tooltip-element></li><li><app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">Icon button</app-froala-tooltip-element></li><li>Selected text</li></ol>

Examples of 4 baseline menu inputs.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhp6c83m-24-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/qaQR6Vom4qUYAtiLZOaGC34kpj4PCzx3--sowDis88NJ1VOQiwhipAIlwryE8_cYmOrso8ZXJ8O56o-PeU4ZC0SvopP5Ej5WB23rBIQmn9kL=s1004

## Guidelines

2 vertical menus, 1 with vibrant colors, 1 with standard colors and grouped items.

<p>A menu in the <strong>vibrant</strong> color style is more expressive, and one with <strong>standard</strong> colors is more utilitarian</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhlk1jwz-GM3_Menus_Guidelines%2001_IA_v01.mp4?alt=media

<h2 id="isPasted">Usage</h2>

<p>Use a menu to show a temporary set of actions. To show actions on screen at all times, use a <app-froala-tooltip-element description="Toolbars display frequently used actions relevant to the current page." link-label="More on toolbars" link-url="/m3/pages/toolbars/overview" should-open-link-in-new-tab="true">toolbar</app-froala-tooltip-element> instead. </p><p>A menu takes up less space than a set of <app-froala-tooltip-element description="Radio buttons let people select one option from a set of options." link-label="More on radio buttons" link-url="/m3/pages/radio-button/overview" should-open-link-in-new-tab="true">radio buttons</app-froala-tooltip-element> or <app-froala-tooltip-element description="Chips help people enter information, make selections, filter content, or trigger actions." link-label="More on chips" link-url="/m3/pages/chips/overview" should-open-link-in-new-tab="true">chips</app-froala-tooltip-element>. </p><h3>Color options</h3><p>Menus have two color mappings:</p><ul><li><p>Standard: Surface-based, lower visual emphasis</p></li><li><p>Vibrant: Tertiary-based, higher visual emphasis</p></li></ul><p>Vibrant menus are more prominent, and should be used sparingly.</p>

Menu shows item “Line spacing” opening a submenu. In the second menu, “Custom 1.2” is selected with vibrant color.

<p>On web, menus can open submenus</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi5nyyrq-02.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/MfCxNMg5F-PVblTlXd6HMYiZd-Lw5KIY6xwvm7F0Pn_sCm-wiLtOMX8xTxOztwb_4xY__6nSEFl-E1txwgI6GJ2awsvnRaTuMiK0t15jyUQ=s1352

<h3>Opening menus</h3><p>Menus temporarily appear in front of all other permanent UI elements.</p><p>A menu should open when a person:</p><ul><li><p>Selects an element, such as an icon, <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">button</app-froala-tooltip-element>, or text field</p></li><li><p>Performs a specific action to trigger the menu, like right-click or press-and-hold</p></li></ul><p>Use menus in situations that need extra actions, like: </p><ul><li><p>Overflow menus</p></li><li><p>Text field dropdown menus</p></li><li><p>Select menus</p></li><li><p>Context menus</p></li></ul>

A grouped menu with Undo, Redo, Cut, Copy, and Paste options appear over highlighted text in an ebook.

<p>Menus appear in front of all other UI elements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhlkhju5-04.png?alt=media

<h3>Menu groups</h3><p id="isPasted">Vertical menu items can be grouped by adding a divider or small gap. Use groups to bundle similar actions together.  </p><p><a href="/m3/pages/menus/guidelines#d75ac70c-9122-4b4c-bd60-b856bc66c9bc">Gaps and dividers guidelines</a></p>

2 vertical menus: a standard menu with no gap and a grouped menu with 1 gap.

<p id="isPasted">Menu items can be grouped to be more scannable:</p><ol class="decimal"><li>Standard vertical menu</li><li>Grouped vertical menu</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi5o0xc8-05.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/6e3Jr7pvYamV89OCHR395lTYFRLLVJsUseXpeuESUaJGC8qKEa1geMsIaYbWGi2O0l2OjBKn5rznan6ZXFBXTCAtf6e3IrBCNPyif9t2Hv5G=s1352

<h3>Context menus</h3>

<p>Context menus provide a list of additional actions a person can take on an item. A secondary click, like a right-click on a mouse or a two-finger tap on a trackpad, opens a context menu. </p>

A context menu pops up from a newspaper link. The menu items are: Open in new window, Save link as, Copy address, and Inspect.

<p>A context menu appears when right clicking with a mouse or trackpad. It can reveal key actions related to the associated content.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhlkwxab-06.png?alt=media

<h2 id="isPasted">Anatomy</h2>

Diagram outlining 11 elements of a menu’s anatomy.

<ol class="decimal"><li id="isPasted">Menu item </li><li>Leading icon (optional)</li><li>Menu item text</li><li>Trailing icon (optional)</li><li>Badge (optional)</li><li>Trailing text (optional)</li><li>Container</li><li>Supporting text (optional)</li><li>Label text (optional)</li><li>Gap (optional)</li><li>Divider (optional)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmigxx4lp-07.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/23G6to4Ij-HsQF2iAQsFg737t4f1InY3ANqqt-NYDrCj4ajmDFHSL7o3BTM7CHvUGdR8bTgcGg-OWPY5sp5qepK-LfRRWNZg8b1gwuq3gjU=s2048

<h3>Menu items</h3>

<p id="isPasted">Menu items can include label text, leading icons, trailing icons, and keyboard commands. </p><p>When a menu item can only be used under specific conditions, it should appear <app-froala-tooltip-element description="A disabled state communicates a non-interactive component or element." link-label="More on disabled state" link-url="/m3/pages/interaction-states/applying-states#4aff9c51-d20f-4580-a510-862d2e25e931" should-open-link-in-new-tab="true">disabled</app-froala-tooltip-element> rather than be removed.</p>

Menu shows 1 item that’s  disabled, “Redo”. The text color of the disabled item is lighter than the active items.

<p>The <strong>Redo</strong> action is disabled when that action isn’t available</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhll6qil-08.png?alt=media

<h3 id="isPasted">Gaps &amp; dividers (optional)</h3><p id="isPasted">Gaps and dividers can be used to separate and group menu items.</p><p><strong>Gaps </strong></p><p>Use a gap to visually divide menu items into distinct groups. Gaps are more expressive than dividers and make the relationship between items clear.</p><ul><li>Avoid changing the size of the gap</li><li>Limit the number of gaps in a menu to one or two</li><li>Don’t use gaps in scrollable menus </li></ul>

2 vertical menus with 5 items. A gap separates items into a group of 3 and group of 2.

<p>Gaps separate menu items using expressive shapes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi5o2orv-09.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/nziJZIcye1oWsr-CrUorKQfgSBAvZMJQWCIaL-tKUJQA2oDY0EbExVpZu3EAaZSC8iljeK6nDpywWbMkK3mSwPrPm7r6JAVwtzHODDztJ9LdXw=s1352

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">Gaps are not currently available on web</div></div></div>

<p id="isPasted"><strong>Dividers</strong> </p><p>Dividers create a more subtle separation between items. Use a divider for:</p><ul><li>Scrollable menus</li><li>Text fields with a dropdown menu, where a grouped treatment isn’t appropriate</li></ul><p>On web, use a divider to separate menu items. </p>

A menu on a web interface with items separated by a divider line.

<p>Dividers separate menu items in baseline menus and on web</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmigxyr8q-10.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/cguRYPI0KSnDbH8G-NsW_ChXLpqPsALNJLlbJiTLKfq99BgdHykJsf40GtSSBeubhxXoiDV74Gjhy3LlmJV8QlE3ZYHAteUNjkNheqp0V2h-=s1352

<h2>Flexibility &amp; slots</h2>

<p id="isPasted">Menus have custom slots that support more flexible item layouts.</p><p>When creating a complicated menu, think of the menu item as a container with a swappable slot.</p><p>Slots work best with simple content such as:</p><ul><li>Images</li><li>Progress indicators</li><li>Color swatches</li></ul>

A menu showing an undefined slot that could be used for a different element, such as an image.

<p>Slots can appear anywhere in a menu</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhllndkg-11.png?alt=media

<p id="isPasted"><strong>Slot accessibility</strong><br /><br />Use caution when adding slots to menus:</p><ul><li>Make sure the menu remains accessible</li><li>Elements must follow the rules and interaction patterns of the menu component</li><li>Keep the same menu item padding</li><li>Targets should be 48x48dp or larger</li></ul><p>Don't add buttons, switches, or other direct actions into the menu item. Nested elements should only perform one action. Adding multiple actions can break keyboard navigation and screen reader functionality.</p><p><a href="/m3/pages/menus/accessibility/" target="_blank" rel="noopener noreferrer">More on required accessibility guidelines</a></p>

1 diagram and 1 menu showing icons in each item’s leading slot.

<p>Reserve the use of slots for use cases that maintain the menu’s accessibility and functionality </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhllqs3p-12-alt.png?alt=media

<h2>Placement</h2>

<p id="isPasted">A menu is positioned relative to the window edge. It typically appears below, next to, or in front of the element that generates it.</p><p>If a menu is in a position to be cut off, it should automatically reposition to appear to the left, right, or above the element that generates it.</p>

6 abstract shapes showing how a menu can extend from the edge of the screen.

<p>Menus can appear around or in front of the element that opened them</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhllv77j-13.png?alt=media

<h3>Submenus</h3><p id="isPasted">Submenus should open next to the parent menu item without overlapping it.</p><p>Submenus are best used on large screens where there's space. <a href="/m3/pages/menus/guidelines#e588ae16-7a76-4bf9-8532-8d931a13ca35">See adaptive guidance</a> for alternatives on mobile.  </p>

A submenu opens to the right of its parent menu item, and doesn’t cover it. A selected submenu item includes a checkmark and vibrant highlight.

<p>Position submenus to the side of the parent item</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhlm1f1q-15.png?alt=media

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">Submenus are not currently available on Jetpack Compose</div></div></div>

<h2>Adaptive design</h2>

<h3>Compact breakpoints</h3><p>Consider adapting menus into <app-froala-tooltip-element description="Bottom sheets show secondary content anchored to the bottom of the screen." link-label="More on bottom sheets" link-url="/m3/pages/bottom-sheets/overview" should-open-link-in-new-tab="true">bottom sheets</app-froala-tooltip-element> on small screens. They have more space to display additional items and longer labels. </p>

A bottom sheet shows longer labels and improved readability on a compact window.

<p>A bottom sheet can replace a menu on smaller screens</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhlm7yx1-16.png?alt=media

<h3>Other breakpoints</h3><p>On <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded</app-froala-tooltip-element> windows, menus are most effective as they appear in context with the content. On larger screens, menus can also display more items, and can use submenus to organize complex sets of options.</p>

A menu with vibrant color on a mid-size screen, with the same elements as a bottom sheet.

<p>On large screens, a menu is often more appropriate than a bottom sheet</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhlmbxni-17.png?alt=media

<h2>Behavior</h2>

<h3 id="isPasted">Appearing</h3><p id="isPasted">A menu can appear when a person interacts with an element on the page, like a button, text field, filter chip, or highlighted text.</p><p>A menu’s position on screen affects where and how it appears. If opened at the top of the screen, it expands downwards to avoid being cropped.</p>

A menu activated at the top of the screen expands downwards, then a menu opened at the bottom of the screen expands upward.

<p>Menus at different positions on a screen open in different directions, adapting to the available space</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhln3y77-GM3_Menus_Guidelines%2018_IA_v02.mp4?alt=media

A menu expands downward from the top of the screen, appearing below a split button.

<p>A menu can open from a split button</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhln8qym-GM3_Menus_Guidelines%2019_IA_v01.mp4?alt=media

A menu expands both above and below a line of selected text, separated by a gap.

<p>A menu can appear in context, like next to highlighted text or a selected image</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhlna20p-GM3_Menus_Guidelines%2020_IA_v02.mp4?alt=media

Selecting the “Phone type” text field reveals a menu with multiple options: Business, Mobile (selected), and Home.

<p>A menu can open from a text field</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhlnd4tn-GM3_Menus_Guidelines%2021_IA_v01.mp4?alt=media

A filter chip for “Cycling” in a map UI reveals more menus items: Running, Walking, and Hiking.

<p>A menu can open from a filter chip</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhlnelhq-GM3_Menus_Guidelines%2022_IA_v02.mp4?alt=media

<p id="isPasted"><strong>Motion</strong></p><p>Menus use an enter and exit transition. This animation creates a relationship between the menu and the element that generates it.</p><p>When a menu expands, the trigger element becomes pressed. When an item is selected, a ripple appears on touch.</p>

An animation for entering a new contact’s address. The state selection menu expands and the state California is selected.

<p>A menu expands when opened, and has a ripple when an item is selected</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhlnmpgd-GM3_Menus_Guidelines%2024_IA_v02.mp4?alt=media

<p>In dense products, such as on desktop, menus can open instantly to reduce motion.</p>

A menu for changing a font type opens instantly on a desktop UI.

<p>Desktop menus can open instantly</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhlnu8z2-GM3_Menus_Guidelines%2023_IA_v01.mp4?alt=media

<h3 id="isPasted">Filtering</h3><p id="isPasted">A menu can include a text field to filter options. This pattern is also known as autocomplete. </p><p>As someone types, the list of menu options filters to show relevant results. This helps people quickly find the right option from a long list. </p><p>Menu items ease into their new position as the menu is filtered.</p>

An animation showing a text field being typed into. As text is added, the list of menu items below filters down to show only matching options.

<p>As a person types in the text field, the menu options filter to match the input</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhloarxl-GM3_Menus_Guidelines%2025_IA_v01.mp4?alt=media

<h3 id="isPasted">Scrolling</h3><p id="isPasted">Menus can scroll when all menu items can’t display at once. In this state, menus show a persistent scrollbar.</p><p>Don’t use gaps if a menu scrolls; this is currently unsupported.</p>

A font menu on a document shows a scrollbar to access font options not currently visible.

<p>When content is scrollable, menus display scrollbars</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhloe6n0-GM3_Menus_Guidelines%2027_IA_v01.mp4?alt=media

<h3 id="isPasted">Selecting</h3><p id="isPasted">When a menu is opened, the corresponding <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">button</app-froala-tooltip-element> or <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon button</app-froala-tooltip-element> should remain the same visually, with the addition of a pressed state.</p><p>This should happen even when opening from a keyboard shortcut.</p><p><br /></p>

The overflow icon remains the same, even after the menu is opened.

<p>Tapping the icon triggers a menu. Choosing a menu option doesn’t change the icon generating the menu.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhlohkz8-28.png?alt=media

<h3>Single- and multi-select menus</h3><p id="isPasted">Menus can allow either single-select or multi-select actions:</p><ul><li><strong>Single-select</strong> menus can have one item selected at a time. When a new item is selected, the previously selected item is automatically unselected.</li><li><strong>Multi-select</strong> menus can have many selected items. They stay open until the person dismisses the menu.</li></ul><p><a href="/m3/pages/menus/accessibility#149778c9-eb42-4a56-8a0b-9932181ac2cd" target="_blank" rel="noopener noreferrer">More on selection accessibility requirements</a></p>

1 menu for dietary options shows a single selection, Vegan. Another menu shows Vegan and Nut-free selections at the same time. 

<p>Menus can be single- or multi-select</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhkpbo8d-30.png?alt=media

<h2>Focus</h2><p id="isPasted">When a menu has multiple submenus, focus follows the current hovered or focused submenu. </p><p><strong>Shape morphing </strong></p><p>As a person moves from one submenu to the next, the corners of the focused submenu become more rounded, while the unfocused submenu becomes less rounded. This adds a dynamic quality to menu interactions.</p>

On a submenu next to a main menu, a selected item’s corner shape expands for added emphasis.

<p>On a custom menu, the corner shape changes to indicate focus as the cursor moves across submenus</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhloky2g-GM3_Menus_Guidelines%2031_IA_v01.mp4?alt=media

<h2>Density</h2>

<p>On web only, density levels control the spacing between elements. Increasing density decreases the top and bottom padding. <a href="/m3/pages/understanding-layout/density" target="_blank">More on layout density</a></p>

4 menus becoming increasingly dense and compressed.

<p>Density of menus from 0 to -3</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhloonkj-32.png?alt=media

## Accessibility

<h2 id="isPasted">Use cases</h2>

<p id="isPasted">People should be able to do the following using assistive technology:</p><ul><li>Navigate to, open, and close a menu</li><li>Navigate between and select menu items</li></ul>

<h2>Interaction &amp; style</h2>

<p id="isPasted">Menu items need certain cues to clearly show when they're selected: </p><ul><li>By default, menu items change shape and color when selected</li><li>The default color contrast is 3:1 between selected and unselected menu items</li><li>It's recommended to include another visual cue, like a checkmark</li></ul><p><br /></p><p><br /></p><p><br /></p>

A state dropdown menu with the selected item Alaska highlighted in a vibrant color, with a checkmark icon.

<p>Use multiple visual cues like color, shape, and icons to show that an item is selected</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi5oa1gs-01.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/sQHnduUnTdZmXVul2Np64bpBWRigAhD_49ObKd4Ks5y6nO0DHiY9tADgizMA9vOTkfNS_w-InRysGae7hxIwcyap_iuISouSE2W03bRdQWM=s1352

<h2>Flexibility &amp; slots</h2>

<p id="isPasted">Use caution when adding slots to menus:</p><ul><li>Make sure the menu remains accessible</li><li>Elements must follow the rules and interaction patterns of the menu component</li><li>Keep the same menu item padding</li><li>Targets should be 48x48dp or larger</li></ul><p>Don't add buttons, switches, or other direct actions into the menu item. Nested elements should only perform one action. Adding multiple actions can break keyboard navigation and screen reader functionality.</p><p><a href="/m3/pages/menus/guidelines#8a1684bb-99a5-4a73-91a0-068d0b406127" target="_blank" rel="noopener noreferrer">More on slots in menus</a></p>

1 diagram and 1 menu showing icons in each item’s leading slot.

<p>Reserve the use of slots for use cases that maintain the menu’s accessibility and functionality</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhkskcq8-02-caution.png?alt=media

<h2>Focus</h2>

<p id="isPasted"><strong>Initial focus</strong></p><p>When a menu opens, focus should be placed on the first menu item. This allows people using a keyboard or other assistive technologies to begin navigating the menu immediately.</p><p><strong>Exiting a menu</strong></p><p>People expect to exit a menu by:</p><ul><li>Selecting an option</li><li>Tapping <strong>Escape</strong> or outside of the menu </li><li>Using the system back <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">button</app-froala-tooltip-element></li></ul><p>Where focus is placed after closing the menu depends on the app.</p>

4 common keyboard navigation methods for menus on Android and web.

<p id="isPasted">Keyboard navigation on Android and web:</p><ol class="decimal"><li><strong>Tab</strong> to select a menu item</li><li><strong>Space</strong> or <strong>Enter</strong> to open a menu</li><li><strong>Space</strong> or <strong>Enter</strong> to select a menu item</li><li><strong>Escape</strong> to close a menu</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhkewf5t-03.png?alt=media

<h2><span style="white-space:pre-wrap">Keyboard navigation</span></h2>

<div class="table-wrapper"><table style="width:100%"><thead><tr><th><strong>Keys</strong><br /></th><th><strong>Actions</strong><br /></th></tr></thead><tbody><tr><td><strong>Tab</strong></td><td>Focus lands on menu</td></tr><tr><td><p id="isPasted"><strong>Space </strong>or<strong> Enter</strong></p></td><td><p id="isPasted">For closed menus: Opens menu or submenu</p><p>For open menus: Selects a menu item</p></td></tr><tr><td><strong>Up</strong> and <strong>Down</strong> arrows</td><td><p id="isPasted">For closed menus: Opens menu </p><p>For open menus: Moves focus to the next item</p></td></tr><tr><td><strong>Left</strong> and <strong>Right</strong> arrows</td><td>Opens or closes a submenu</td></tr><tr><td><strong>Letters</strong></td><td>Focus moves to the next menu item starting with letter</td></tr><tr><td><strong>Escape</strong></td><td>Closes menu</td></tr></tbody></table></div>

<h2><span style="white-space:pre-wrap">Interactability</span></h2>

<p id="isPasted"><app-froala-tooltip-element description="A disabled state communicates a non-interactive component or element." link-label="More on disabled state" link-url="/m3/pages/interaction-states/applying-states#4aff9c51-d20f-4580-a510-862d2e25e931" should-open-link-in-new-tab="true">Disabled</app-froala-tooltip-element> menu items can receive focus but aren't selectable.</p><p>Dividers and gaps can't receive focus.</p>

A disabled menu item “Share” is in focus.

<p>Disabled menu items can receive focus</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhkkp9r3-05-do.png?alt=media

A divider with focus.

<p>A divider or gap can’t receive focus</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhkkqmt3-05-don't.png?alt=media

<p id="isPasted">On web, submenus have a <strong>magic triangle</strong> behavior for more intuitive mouse navigation. </p><p>This keeps the submenu open when the mouse moves within a triangular area between the triggering item and the submenu.</p><p><a href="/m3/pages/menus/guidelines#5b3a92ec-a694-4ea7-87ad-0fbf87344cab" target="_blank" rel="noopener noreferrer">More on submenus</a></p>

A menu opens a submenu, and the pointer moves in a triangular area to the submenu item “Custom font family” without closing the menu.

<p>The <strong>magic triangle</strong> keeps a submenu open when the pointer travels outside the triggering item</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhkkuch7-GM3_Menus_Accesibility%2006_IA_v02.mp4?alt=media

<h2><span style="white-space:pre-wrap">Labeling elements</span></h2>

<p id="isPasted"><app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview/principles" should-open-link-in-new-tab="true">Accessibility</app-froala-tooltip-element> labels are used with assistive technology devices like screen readers. </p><p>The accessibility label should be the same as the menu item text.</p><p>The role is <a href="/m3/pages/menus/accessibility#9c562e2c-da3a-4212-a2e3-ac91ba450b65">dependent on platform</a>.</p><p><br /></p>

A “Preview” menu item has an accessibility label of ”preview”.

<p>The menu item’s accessibility label aligns with the UI text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhkl2sea-07.png?alt=media

<div class="table-wrapper"><table style="width:100%"><thead><tr><th><div style="text-align:center"><strong>Element</strong></div></th><th><p id="isPasted" style="text-align:center"><strong>A11y label</strong></p></th><th><p id="isPasted" style="text-align:center"><strong>Role (Web)</strong></p></th><th><div style="text-align:center"><strong>Role (Android Views)<br /></strong></div></th><th style="text-align:center"><p id="isPasted"><strong>Role (Jetpack Compose)</strong></p></th></tr></thead><tbody><tr><td>Menu item text</td><td>Preview</td><td>Menu item</td><td>Generic actionable element</td><td>Generic actionable element </td></tr></tbody></table></div>

<p id="isPasted">For menu items with text and an icon, the icon’s accessibility label should be marked as <strong>decorative</strong> to avoid redundant verbalizations.</p>

A menu item icon of an eye next to the word “preview” has a note of “Decorative.”

<p>For menu items with text and an icon, the icon’s accessibility label is <strong>decorative</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmhkkynea-08.png?alt=media
