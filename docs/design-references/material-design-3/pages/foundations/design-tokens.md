# Design tokens

Source: https://m3.material.io/foundations/design-tokens
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/abae98fd-d828-44f8-bb66-9ee8746f6073.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code.

## Overview

<ul><li><p>Tokens point to style values like colors, fonts, and measurements</p></li><li><p>Use design tokens instead of hardcoded values</p></li><li><p>Each token is named for how or where it’s used (for example, <strong>md.comp.fab.primary.container.color</strong> sets the container color for a FAB)</p></li><li><p>Even if a token’s end value is changed, its name and use remain the same</p></li><li><p>Material Design has three classes of tokens: <a href="/m3/pages/design-tokens/overview#6a0933c0-50f5-4dd6-b055-b7c4ff2c1535" target="_self">reference</a>, <a href="/m3/pages/design-tokens/overview#7f084930-cf5f-4b7e-b83c-614888f18a77" target="_self">system</a>, and <a href="/m3/pages/design-tokens/overview#b4d6bb35-ee69-4908-bcb4-b33b0a1997e2" target="_self">component</a></p></li></ul>

FAB container color token in a design mock, code, and product

<p>Using design tokens instead of hardcoded values can streamline the work of building, maintaining, and scaling products with a design system</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmihjfljt-tokens-overview-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/c9vp62g9BTHZ795In-3SH01cvbjuaHUgu67bdrisAMsV34Z_J2DjSxlSbuJj1eKq_lp4na46QCwYpX0HTDXqYWAMdGDn272etcMj8QU__laE2A=s2048

<h2 id="isPasted">Resources</h2>

<div class="table-wrapper"><table><thead><tr><th>Type</th><th style="width:60.668%">Link</th><th style="width:15.2133%">Status</th></tr></thead><tbody><tr><th rowspan="2">Design</th><td><a href="http://goo.gle/m3-design-kit" rel="noopener noreferrer" target="_blank">Design Kit</a> (Figma)</td><td>Available</td></tr><tr><td><a href="https://goo.gle/material-theme-builder-figma" rel="noopener noreferrer" target="_blank">Material Theme Builder Figma plugin</a></td><td>Available</td></tr><tr><th>Implementation</th><td><a href="https://github.com/material-foundation/material-tokens" rel="noopener noreferrer" target="_blank">Material baseline theme and tokens</a> (DSP)</td><td>Available</td></tr></tbody></table></div>

<h2>What’s a design token?</h2>

<p dir="ltr" id="isPasted">Design tokens are small, reusable design decisions that make up a design system's visual style. Tokens replace static values with self-explanatory names.</p><p dir="ltr">A design token consists of 2 things:</p><ol><li><p class="normal">A code-like name, such as <strong>md.ref.palette.secondary90</strong></p></li><li><p class="normal">An associated value, such as <strong>#E8DEF8</strong></p></li></ol><p dir="ltr">The token's value can be one of several things: A color, typeface, measurement, or even another token.</p>

Token md.ref.palette.secondary90 with arrow pointing to lilac color swatch #E8DEF8.

<p>Example of a reference token and its color value</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2bj1kfh-tokens-what-are-tokens.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Bknc9M3GEXT1mJKs0VEe_nz3SYJfp1jIUTB9Zu7QfDehLklj2o8KiaX2bWYh0MO_IkzOyIKHXLW3xuIZaui8e2mKYCAOy8wzg6VYF-m-LAA=s1352

<p id="isPasted">Design tokens meaningfully connect style choices that would otherwise lack a clear relationship.</p><p>For example, if a designer's mock-ups and an engineer's implementation both reference the same token for the “secondary container color,” then they can be confident that the same color is being used in both places. This applies even if the hex value assigned to that token gets updated.</p>

Diagram of FAB indicating system tokens: Secondary for surface color and on secondary for icon color

<p>Example of tokens assigned to the secondary and on secondary color roles of a FAB’s container and icon, respectively</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2bj3fdz-tokens-what-are-tokens-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-2T43IjyCiZsBPO6YWZyjpxusIkShHOR9XwlIRkYdzfv821dNieHThO9QXoqXebE7OtOvUUWQ_5sS2A2uOB-J4sX3-15nngWQvDXuZCWej_Z=s1352

<h2>Why are tokens important?</h2>

<p id="isPasted">Tokens make it possible for a design system to have a single source of truth – a repository where style choices are recorded and changes can be tracked.<br /><br />Because tokens are reusable and purpose-driven, they can define system-wide updates to themes and contexts. For example, you can use tokens to systematically apply a high-contrast color palette for improved visibility, or change the typographic scale to ensure that text is legible on a TV screen.<br /><br />By using tokens for design and implementation, style updates propagate consistently through an entire product or suite of products. They also help designers and engineers "speak the same language,” reducing confusion during handoff from design to implementation.</p>

Diagram of how changing the value of a token cascades from design system into a product area and 3 products

As design systems evolve, certain values will change. With design tokens, we can track changes and ensure consistency across our products.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fkudi7oge-kpzr9qtu-tokens-why-importan%20(1).gif?alt=media

<h2 id="isPasted">Deciding if tokens are right for you</h2>

<h4 dir="ltr" id="isPasted"><strong>Tokens will be most helpful if:</strong></h4><ul><li>You plan to update the design of your product or are building a product from scratch</li><li>Your design system is applied across a suite of products or platforms</li><li>You want to make it easy to maintain or update styles in the future</li><li dir="ltr">You want to get the most out of the Material Design system, including features like dynamic color</li></ul>

<h4 dir="ltr" id="isPasted"><strong>Tokens will be less helpful if:</strong></h4><ul><li>You have an existing app using hard-coded values that is unlikely to change in the next year or two</li><li dir="ltr">Your product does not have a design system</li></ul>

<h2>Tokens &amp; Material Design</h2>

<p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">In the past, Material styles were communicated through guidelines, design files, tools, and platform-specific component libraries.<br /><br />With design tokens, you can now download, customize, and apply Material styles and integrate them across your design and development process.<br /><br />Tokens allow decisions to be documented in a platform-agnostic and shareable format.</span></p>

Diagram of design token connected to design tool and platform code

<p>Design tokens provide a central repository for design choices, with a variety of integration points for engineers and designers</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2bj3wia-tokens-ref.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/EKKzA023VSYZyglmlsQaMzNiDHpIB7GJi0JYVqOaKoYpbScua34HgJLWUi4abFbFvL3Nl5Ysyw-VAdugxXzR-FU5zfZ-sZLWoBLr-r5wsRG6=s1352

<p dir="ltr" id="isPasted"><span style="white-space:pre-wrap" id="isPasted">On this site, you’ll see tokens listed in interactive modules.<br /><br />These modules let you quickly look up the default baseline value stored by tokens for color, font, font size, font weight, etc. They also show the relationship between a role, its system token, reference token, and stored pre-set value.</span></p>

A token module for the color system with 4 color swatches for the primary color set.

<p><span style="white-space:pre-wrap">Example of a token module</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2a7ufbh-token-tables_1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/MotwH3S7yKjoXqs5e2mDbXUwU6EoU3pN4RAnRIMDVOUnqoAO5PBSL5iEyu2fG7q7X25CjzVsYiNv1VoblTEfYAQgHZpX0Qd6iGZ5CcQcwhzC=s1352

<p>You’ll also see tokens in the specs tabs of component articles.<br /><br />Tokens are first grouped by <strong>state</strong> (enabled, disabled, hover, etc) and then by <strong>element</strong>, which is the part of the component that a token or value applies to, such as the container or label text.<br /><br />Columns include:</p><ul><li><strong>Name </strong>– The component style aspect that the token applies to, such as color or font</li><li><strong>Token ID</strong> – The token defining the component style aspect</li><li><strong>Description</strong> – Optional descriptive info</li><li><strong>Context/value</strong> – The value stored in the token for a given context</li></ul>

A token module for an elevated button organized by state (enabled, disabled, etc), then element (container, label text).

<p>The diagram and token module for elevated button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2a7upc5-token-tables_2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/blyXX25f2X086gJuC8nsR2Ka_UKdrEdTnHMwB0MmS5OhLAm6Mr1xJ_N1g_SA0SIdh38o_nKitS2dfo3clAVKc3EYFBodlpOScPWVLZQ7Axe-=s1352

<h3 dir="ltr" id="isPasted">How to use token modules</h3><p id="isPasted">Let's say you need to verify the color role for a filled button's label text.</p><p>Navigate to Common buttons &gt; Specs, find the token module for filled buttons, and search for the "label text" tokens under elements.</p><p>Copy the color token and paste it in code, or compare it to the color role in Figma.</p>

How to find the label text color token.

<p>Diagram and token table for filled button label color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2jdnd1z-Using-token-tables.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/fpDbiFzrd8uG-JaTJJ8KBzsUeKOAUj3BH8Iv9YwsxGwcB7-jSSf6a127iDeYKS-QvDaL5I6wymDQ8S80XZQCDmqL6uzFQ0rf1WPPWRwk7ta4=s1352

<h2 dir="ltr" id="isPasted">Parts of a token name</h2>

<p dir="ltr">The parts of a token name are separated by periods and proceed from the most general information ("md") to the most specific ("on-secondary").</p><ol><li>All token names in a design system start with the system name (such as “md” for Material Design)</li><li>An abbreviation for the token class: “ref” for reference tokens, “sys” for system tokens, and “comp” for component tokens</li><li>The token ends with descriptive words communicating the token’s role</li></ol>

Diagram of the 3 parts of a design token name: system prefix, token type, and role description

<ol><li>Communicates design system</li><li>Communicates token class</li><li>Communicates token’s purpose</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4mwzkye-tokens-naming-convention.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ELaR3gkzDVBDyQd2BLSaPqSgYm-MbQfELTFmqL2bmbKNWZSWqkDcPmb8c8E68DbF5lVdaJkt7ZXnewSDAHd7NvqZ1K6HEb5VITuO1lsb0AZC=s1352

<h2 id="isPasted">Classes of tokens</h2>

<p><span style="white-space:pre-wrap" id="isPasted">There are three classes of tokens in Material:</span></p><ol><li><span style="white-space:pre-wrap" id="isPasted">Reference tokens</span><br /><span style="white-space:pre-wrap">All available tokens with associated values.</span></li><li><span style="white-space:pre-wrap">System tokens</span><br /><span style="white-space:pre-wrap">Decisions and roles that give the design system its character, from color and typography, to elevation and shape.</span></li><li><span style="white-space:pre-wrap">Component tokens</span><br /><span style="white-space:pre-wrap">The design properties assigned to elements in a component, such as the color of a button icon.</span></li></ol><p><span style="white-space:pre-wrap">With three classes of tokens, teams can update design decisions globally or apply a change to a single component.</span></p>

Color value stored in reference token stored in system token, stored in component token, appearing as the container color of a FAB

<p><span style="white-space:pre-wrap">A button that receives its container color through a system of three tokens that define scalable color values. The color tokens point to a specific hex value that can easily change without impacting the token syntax.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2a7vmvv-tokens-types.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-_3g9qggRt-nlWlYvWdW1T_gpm6ra7Rz9IPWjBjYYkhHJp1Vs0awKPz12P9QQdiwt5hIScJjfbbFeB4nwa0hYgocU0qWdCLOgPZ8ElWwuKqubQ=s1352

<h3 dir="ltr" id="isPasted">Reference tokens</h3><p id="isPasted">These tokens make up all of the style options available in a design system.</p><p>They usually point to a static value – such as a color hex code or font size – but can also point to other reference tokens. Reference tokens don't change based on context.</p><p>By providing a list of options, reference tokens give your team a starting point of approved colors, typography, measurements, etc.</p><p>All reference tokens start with the prefix <strong>ref</strong>.</p>

Token md.ref.palette.secondary90 pointing to #E8DEF8. Toke md.ref.typeface.plain-medium pointing to Roboto Medium

Color and typography reference tokens and their values

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2a7whio-tokens-ref.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/cDiHf197RUviZB0cVugMQ610kBthFcsT6dKRcL62hYeJKXztvKAbHkhYSZ6fG6llh29-wBpe9_LVeqJ709s9v4gRdyHBPxo7PlBfMEfYMYY=s1352

<h3 dir="ltr" id="isPasted">System tokens</h3><p dir="ltr">These are the decisions that systematize the design language for a specific theme or context.</p><p dir="ltr">System tokens define the purpose a reference token serves in the UI.</p><p dir="ltr">This is where theming occurs. The system token can point to different reference tokens depending on the context, such as a light or dark theme.</p><p dir="ltr">Whenever possible, system tokens should point to reference tokens rather than static values. </p><p>All system tokens start with the prefix <strong>sys</strong>.</p>

System token md.sys.color.secondary-container pointing to token md.ref.palette.secondary90 pointing to #E8DEF8. System token md.sys.typescale.label-medium.font pointing to token md.ref.typeface.plain-medium pointing to Roboto Medium

System tokens, reference tokens, and their values

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2a7wqsm-tokens-sys.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/reBkkzgx8GvOAJHnEJX20XF1y-lxMvYAmVvySpWxhkHSkUX-oU_NAmLxDGPGgLMMnQ1KYkCdfe9EqHIYMddFYnHOY-YHW8rNEQRR_bn8mw4u2Q=s1352

<h3 dir="ltr" id="isPasted">Component tokens (in development)</h3><p id="isPasted">These represent the elements required to compose a component, such as containers, label text, icons, states, and their values such as size, shape, color, or elevation.</p><p>Whenever possible, component tokens should point to a system or reference token, and not contain hardcoded values such as hex codes.</p><p>Not every stylistic choice of a component will be able to be expressed as a token, but whenever a design choice applies to multiple components of similar intent, a token should be used.</p><p>All component tokens start with the prefix <strong>comp</strong>. </p>

Extended FAB component tokens for container color and label text pointing to system tokens, pointing to reference tokens, pointing to resolved values

Component tokens, system tokens, reference tokens, and their values

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2a7xj0c-tokens-comp.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/FGD2VI87BOga9gqJRH3c_n5bOlpJ3fnEfaRcJrx3ewx6NmvRHK5pL4A2yba64JVgd5aDUzN9x_mQ3PDmUt6kBDNHKe26x4DmktH3m9Ubqr6S=s2048

<h2 id="isPasted">Contexts</h2>

<p dir="ltr" id="isPasted">Tokens can point to different values depending on a set of conditions. These conditions are called contexts and their resulting values are called contextual values.<br /><br />Examples of different contexts include: device form factors, dark theme, dense layouts, and right-to-left writing systems.<br /><br />You can think of a context as a kind of tag. If a token value is tagged with dark theme then it will override the default token value in a dark theme context.</p>

Diagram of system token for background color pointing to different values depending on the theme context

<p>The same system token for background color can point to different reference tokens depending on the context: Light theme or dark theme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2a7xyeq-tokens-contexs.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Zcuumtw10MHbA9FVmp00u1rqG--CKiX0l92dlLyWwXv9dJ3aTEEUsO98MkMRHlNEKjNWZ3s74t0ckaAbEt37HBwkBaS2FRk10ArgeVN5l2NDvQ=s2048

<h2>How to use tokens</h2>

<h3>Download Material baseline tokens</h3><p>Material’s baseline theme includes design tokens and default values. <a href="https://github.com/material-foundation/material-tokens" target="_blank" rel="noopener noreferrer">Download the theme</a> as a Design System Package (DSP) to customize, collaborate on, and use in your own designs and product code. <a href="https://github.com/AdobeXD/design-system-package-dsp" target="_blank" rel="noopener noreferrer">Learn about the DSP JSON format</a></p>

<h3>Use tokens in Figma</h3><p>To begin, install the <a href="https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder" target="_blank" rel="noopener noreferrer">Material Theme Builder</a> Figma plugin from the community page.</p>

<h4>Generate tokens</h4><ol class="decimal"><li id="isPasted">Open Figma and navigate to: Plugins &gt; Material Theme Builder &gt; Open Plugin</li><li>Select Get started, this will create material-theme with baseline values by default. Color and text styles will begin populating the right hand design panel. When your tokens are fully generated, your artboard will contain tonal palettes for light and dark color schemes, as well as a default type scale.</li><li>Your tokens are now represented as <a href="https://help.figma.com/hc/en-us/articles/360039238753-Styles-in-Figma" target="_blank" rel="noopener noreferrer">Figma styles</a> that can be used throughout your designs</li></ol>

<h4>Import tokens via DSP</h4><ol class="decimal"><li id="isPasted">Open Figma and navigate to: Plugins &gt; Material Theme Builder &gt; Open Plugin</li><li>Open the theme dropdown and select Import DSP</li><li>Select the token DSP file from your list of files. Color and text styles will begin populating the right hand design panel. When your tokens are fully imported, your artboard will contain tonal palettes for light and dark color schemes, as well as a default type scale.</li><li>Your tokens are now represented as <a href="https://help.figma.com/hc/en-us/articles/360039238753-Styles-in-Figma" target="_blank" rel="noopener noreferrer">Figma styles</a> that can be used throughout your designs</li></ol>

<h4>Update token values</h4><p id="isPasted">Using the Material Theme Builder Figma plugin (updates colors only)</p><ol class="decimal"><li>Open Figma and navigate to: Plugins &gt; Material Theme Builder &gt; Open Plugin</li><li>With Custom selected, choose colors. Updated color and text styles will begin populating the right hand design panel.</li><li>Your updated tokens are now represented as <a href="https://help.figma.com/hc/en-us/articles/360039238753-Styles-in-Figma" target="_blank" rel="noopener noreferrer">Figma styles</a> that can be used throughout your designs</li></ol><p><br /></p><p id="isPasted">Using Figma styles</p><ol class="decimal"><li>In Figma, navigate to the file in which the tokenized style is defined. Shortcut: right click the style in the right hand sidebar and select Go to style definition.</li><li>In the right hand sidebar, hover over the style you want to update and select the adjust icon when it appears. Or, right click the style in the style picker and select Edit style.</li><li>Make your changes to the token name, description, properties, etc. using the Edit style panel. Close the panel when finished.</li></ol>

<h4>Use tokens in product mock-ups</h4><p>Instead of manually setting the color or typography for elements in a layout, apply the <a href="https://help.figma.com/hc/en-us/articles/360039238753-Styles-in-Figma" target="_blank" rel="noopener noreferrer">Figma styles</a> representing your design tokens. This helps ensure that developers will correctly understand and apply your design choices.</p>

<h4>Use tokens with the Material Design Kit</h4><ol class="decimal"><li id="isPasted">Duplicate the Material Design Kit in Figma</li><li>Navigate to Plugins &gt; Material Theme Builder &gt; Open plugin</li><li>With components selected, select swap. This will swap the baseline Material token style values with your own generated token style values.</li></ol>

<h4>Export tokens</h4><ol class="decimal"><li id="isPasted">Open Figma and navigate to: Plugins &gt; Material Theme Builder &gt; Open Plugin</li><li>Navigate to the Export tab. Select the format you want to export for (Android, Jetpack Compose, DSP)</li><li>Name your .zip file and select Save</li></ol><p>Your tokens are ready to share!</p>

## How to use tokens

<h2 id="isPasted">Download Material baseline tokens</h2>

<p dir="ltr">Material Design’s baseline theme includes design tokens and default values. <a href="http://github.com/material-foundation/material-tokens" rel="noopener noreferrer" target="_blank">Download the theme</a> as a Design System Package (DSP) to customize, collaborate on, and use in your own designs and product code.  <a href="https://github.com/AdobeXD/design-system-package-dsp" rel="noopener noreferrer" target="_blank">Learn about the DSP JSON format</a></p>

<h2 id="isPasted">Use tokens in Figma</h2>

<p dir="ltr">To begin, install the <a href="https://goo.gle/material-theme-builder-figma" rel="noopener noreferrer" target="_blank">Material Theme Builder</a> Figma plugin from the community page.</p><p><br /></p><h3 dir="ltr">Generate tokens</h3><ol><li>Open Figma and navigate to: <strong>Plugins</strong> &gt; <strong>Material Theme Builder</strong> &gt; <strong>Open Plugin</strong></li><li>Select <strong>Get started</strong>, this will create <strong>material-theme</strong> with baseline values by default. Color and text styles will begin populating the right hand design panel. When your tokens are fully generated, your artboard will contain tonal palettes for light and dark color schemes, as well as a default type scale.</li><li>Your tokens are now represented as <a href="https://help.figma.com/hc/en-us/articles/360039238753-Styles-in-Figma" rel="noopener noreferrer" target="_blank">Figma styles</a> that can be used throughout your designs</li></ol><p><br /></p><h3 dir="ltr">Update token values</h3><h4 dir="ltr">Using the Material Theme Builder Figma plugin (updates colors only)</h4><ol><li>Open Figma and navigate to: <strong>Plugins</strong> &gt; <strong>Material Theme Builder</strong> &gt; <strong>Open Plugin</strong></li><li>Choose the colors. Updated color and text styles will begin populating the right hand design panel.</li><li>Your updated tokens are now represented as <a href="https://help.figma.com/hc/en-us/articles/360039238753-Styles-in-Figma" target="_blank" rel="noopener noreferrer">Figma styles</a> that can be used throughout your designs</li></ol><p><br /></p><h4 dir="ltr">Using Figma styles</h4><ol><li>In Figma, navigate to the file in which the tokenized style is defined. Shortcut: right click the style in the right hand sidebar and select <strong>Go to style definition.</strong></li><li>In the right hand sidebar, hover over the style you want to update and <strong>select the adjust icon when it appears</strong>. Or, right click the style in the style picker and select <strong>Edit style</strong>.</li><li>Make your changes to the token name, description, properties, etc. using the <strong>Edit style panel</strong>. Close the panel when finished.</li></ol><p><br /></p><h3 dir="ltr">Use tokens in product mock-ups</h3><ol><li>Instead of manually setting the color or typography for elements in a layout, apply the <a href="https://help.figma.com/hc/en-us/articles/360039238753-Styles-in-Figma" rel="noopener noreferrer" target="_blank">Figma styles</a> representing your design tokens. This helps ensure that developers will correctly understand and apply your design choices.</li></ol><p><br /></p><h3 dir="ltr">Use tokens with the Material Design Kit</h3><ol><li>Duplicate the Material Design Kit in Figma</li><li>Navigate to <strong>Plugins</strong> &gt; <strong>Material Theme Builder</strong> &gt; <strong>Open plugin</strong></li><li>With components selected, <strong>select swap</strong>. This will swap the baseline Material token style values with your own generated token style values.</li></ol><p><br /></p><h3 dir="ltr">Export tokens</h3><ol><li>Open Figma and navigate to: <strong>Plugins</strong> &gt; <strong>Material Theme Builder</strong> &gt; <strong>Open Plugin</strong></li><li>Navigate to the <strong>Export tab</strong>. Select the format you want to export for (Android, Jetpack Compose)</li><li>Name your .zip file and select <strong>Save</strong></li></ol><p dir="ltr">Your tokens are ready to share!</p>

<h2 id="isPasted">Use tokens in VSCode</h2>

<p dir="ltr">To begin, install the <a href="https://marketplace.visualstudio.com/items?itemName=Adobe.xd&amp;ssr=false#overview" rel="noopener noreferrer" target="_blank">Adobe XD extension for Visual Studio Code</a>. This enables you to directly integrate a DSP file into your product.</p><p><br /></p><h3 dir="ltr">Import tokens</h3><ol><li><span id="isPasted" style="color:rgba(0, 0, 0, 0.87)">Get the DSP file from your designer or </span><span id="isPasted" style="color:rgba(0, 0, 0, 0.87)"><a href="https://github.com/material-foundation/material-tokens" rel="noopener noreferrer" target="_blank">download the Material baseline theme</a></span></li><li>Unzip the DSP file</li><li>Open <strong>VSCode</strong>. Drag the opened DSP folder into the environment window, copying it into your workspace</li></ol><p><br /></p><h3 dir="ltr">Update token values</h3><ol><li>Navigate to your DSP file, <strong>dsp.json</strong>.</li><li>Open the Adobe XD extension and select <strong>Tokens</strong> from the menu. This shows you a list of all tokens and token values.</li><li>Select <strong>Start Editing</strong></li><li>Find the token you want to edit and select the <strong>pencil icon</strong> to the right of its card</li><li>Make any changes to the token type, ID, value, or description</li><li>Select the checkbox to the right of the token’s card</li><li>Select <strong>Finish Editing,</strong> which recompiles the tokens</li><li dir="ltr">Hot refresh your code. You’ll be able to see the updated token reflected in your preview.</li></ol>

<h4 dir="ltr" id="isPasted">Learn more about the Adobe XD extension for VSCode</h4><ul><li>Video: <a href="https://www.youtube.com/watch?v=5MhfwvlGkfA" rel="noopener noreferrer" target="_blank">The Adobe XD Visual Studio Code Plugin (Crash Course)</a> by <a href="https://www.youtube.com/redirect?event=video_description&amp;redir_token=QUFFLUhqbWhsc3dXRUVqM0dVanp1VUNQdUpSNjJ1YUxfQXxBQ3Jtc0ttVWJoMlBEOXhPZHVhdkh3SmFtaTR2dUI3bEhPZjNnR0xRQ1FVbXRXcEdFVEtYVnBqZVBnU2x1ajFZUk90RU9qY3doSmNjWGU5YXdod0xGS3ZxblNfNldGMERmSTNwcG81TVk2bnQybzc2ZnNJRDVsTQ&amp;q=https%3A%2F%2Fdesigncourse.com" rel="noopener noreferrer" target="_blank">DesignCourse</a></li><li>Playlist: <a href="https://www.youtube.com/playlist?list=PLCrals-Cpb1YloFnrsgU7PWdvTprLSzD3" rel="noopener noreferrer" target="_blank">Adobe XD x VSCODE Pro Tips</a> by Matt Rae</li></ul>
