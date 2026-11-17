# Spacing

Source: https://m3.material.io/styles/spacing
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/36e81931-9b87-406f-9ec5-c0cc049564d8.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Spacing is the distance around and between component and layout elements

## Overview

<ul><li><p>Apply spacing tokens to the margins, padding, and gaps of a component, UI element, or layout</p></li><li><p>Adapt spacing to different values based on context, like mobile vs desktop, or density settings</p></li><li><p>The spacing system is measured on an 8dp scale, where <strong>space100 = 8dp</strong></p></li><li><p>Spacing is applied to the flow of elements (horizontal, vertical), or in relation to the elements (leading, trailing, top, bottom, gap)</p></li><li><p><a href="/m3/pages/grids-spacing" target="_blank">More details on grid &amp; spacing design principles</a></p></li></ul>

Bottom padding of small and large buttons is space200 and space400. Leading padding is space300 and space600.

<p>Spacing should adapt to component size, layout, form factor, and other contexts</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp45pjnu-01.png?alt=media

<h2>Availability &amp; resources</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:23.1574%"><p>Type</p></th><th style="width:42.8696%"><p>Resource</p></th><th style="width:33.8977%"><p>Status</p></th></tr></thead><tbody><tr><td rowspan="4" style="width:23.1574%"><p>Implementation</p></td><td><p>Android Views (MDC-Android)</p></td><td><p>Unavailable</p></td></tr><tr><td><p>Jetpack Compose</p></td><td><p>Available</p></td></tr><tr><td><p>Web</p></td><td><p>Unavailable</p></td></tr></tbody></table></div>

<h2>Spacing units</h2>

<p>Spacing units follow an 8dp scale. Rather than defining every value, Material only defines the most recommended spacing unit values on the scale. The system can be extended to add more spacing units and patterns as needed. <a href="/m3/pages/spacing/tokens/" target="_self">More on spacing tokens</a></p>

A spacing scale shows 2, 4, 6, and 8 at the bottom range and 48, 56, 64, and 72 at the top of the range.

<p>Spacing units are are created as a multiplier from the baseline unit of 8dp, which is space100</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp46hu30-02.png?alt=media

<h3>Component layouts</h3><p>In <strong>components</strong>, spacing units define the padding and gaps between individual elements of a component, such as text, icons, and controls.</p>

Padding and gaps applied to a mobile layout and 2 components.

<p>Spacing concepts for components:</p><ol class="decimal"><li><p>Vertical padding (top &amp; bottom)</p></li><li><p>Vertical gap</p></li><li><p>Horizontal padding (leading &amp; trailing)</p></li><li><p>Horizontal gap</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp46iygv-03.png?alt=media

<h3>Page layouts</h3><p>In <strong>layouts</strong>, spacing units standardize the overall composition of the page, like where text, UI elements, and components go. <br /><br />Layouts use:</p><ul><li><p><app-froala-tooltip-element description="Panes are layout containers that house other components and elements within a single app. A pane can be: fixed, flexible, floating, or semi permanent." link-label="More on panes" link-url="/m3/pages/understanding-layout/parts-of-layout#667b32c0-56e2-4fc2-a618-4066c79a894e" should-open-link-in-new-tab="true">Panes</app-froala-tooltip-element>, <app-froala-tooltip-element description="A spacer is the space between two panes. If panes can be resized, the spacer contains a drag handle." link-label="More on spacers" link-url="/m3/pages/grids-spacing/spacing" should-open-link-in-new-tab="true">spacers</app-froala-tooltip-element>, and margins to structure the page</p></li><li><p>Padding and gaps to organize content within the panes.</p></li></ul>

Padding and gaps applied to a mobile layout and 2 components.

<p>Spacing concepts for layouts:</p><ol class="decimal"><li><p>Margin</p></li><li><p>Top padding</p></li><li><p>Horizontal padding (leading &amp; trailing)</p></li><li><p>Spacer (gap)</p></li><li><p>Vertical gap</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp46qg1t-04.png?alt=media

<h2>Parts of spacing</h2>

<p>Spacing has three categories: <strong>padding</strong>, <strong>gaps</strong>, and <strong>margins</strong>.</p><ul><li><p>Padding: Space inside an element</p></li><li><p>Gap: Space between elements in a grid or container</p></li><li><p>Margins: Space outside an element</p></li></ul><p>The position of the spacing can be <strong>vertical</strong>, <strong>top</strong>, <strong>bottom</strong>, <strong>horizontal</strong>, <strong>leading</strong>, or <strong>trailing</strong>.</p><ul><li><p><strong>Leading</strong> and <strong>trailing</strong> edges swap sides in right-to-left (RTL) languages. <a href="/m3/pages/bidirectionality-rtl" target="_blank">More on RTL layout design</a></p></li></ul><p>For example, the <a href="/m3/pages/search/specs" target="_blank">search</a> container has:</p><ul><li><p>8dp vertical padding</p></li><li><p>8dp horizontal gaps</p></li><li><p>24dp horizontal margins (12dp when focused)</p></li></ul>

Default search spacing.

<p>Search horizontal margins are 24dp by default to ensure accurate placement from the screen edge</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp46u5o7-05.png?alt=media

Active search spacing.

<p>Search margins change to 12dp when focused, while the container padding and horizontal gaps remain the same</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp46ujx2-06.png?alt=media

<h3>Padding</h3><p>Padding is the spacing inside an element. It adds a buffer from the container edge to the content, like text and icons.</p>

Examples of each possible padding value.

<p>Padding can be horizontal or vertical, or on a specific edge: leading, trailing, top, or bottom</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmpcmizsr-07.png?alt=media

<h3>Gaps</h3><p>Gaps are the spaces between elements in a grid or container. Horizontal gaps are between side-by-side elements, and vertical gaps are between stacked elements. </p><p>Use a <strong>horizontal gap</strong> and <strong>vertical gap</strong> for simple components where gaps are always the same size.</p><p>Complex components with many different gaps should define them by the elements on each side, like an <strong>icon-label gap.</strong></p>

Examples of each possible gap value.

<p>Gaps can be horizontal, vertical, or defined by the elements around it</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp46wxwi-08.png?alt=media

<h3>Margins</h3><p>Margins are the spacing outside an element. They add a buffer between the element and the parent container or screen edge.</p><p><strong>Use padding &amp; gaps before using margins:</strong></p><ul><li><p>Material rarely uses margins in components; padding and gaps tend to apply spacing in a more uniform way</p></li><li><p>Only use margins to apply further spacing beyond the parent container’s padding, or in layouts</p></li></ul>

Examples of each possible margin value.

<p>Margins can be horizontal or vertical, or on a specific edge: leading, trailing, top, or bottom</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp46ywq1-09.png?alt=media

Button with uniform container horizontal padding.

<p>Define padding and gaps on the parent container to organize all elements inside</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp46yjrr-10.png?alt=media

Button icon with different leading and trailing margin values.

<p>Avoid defining margins on child elements as they usually aren’t uniform, and require more tokens</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp46z9b3-11.png?alt=media

## Applying spacing

<p>Material’s spacing system is intentionally designed to be a simple linear scale. Unlike the color system, which adjusts light and dark theme logic across all components at once, tailored spacing logic is built within each component. </p>

Component and system token mapping for the leading padding of three different icon buttons.

<p>Components have padding tokens that map to system tokens, which resolve to final values</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp472g1b-01.png?alt=media

<h2>What to use</h2>

<h3>Pre-tokenized components</h3><p>Some Material components map to spacing system tokens out of the box. This mapping can be customized by products to adapt to form factor or density.</p><p>Note: Work is ongoing to hook up all Material components to spacing tokens.</p><h3>System tokens</h3><p>Spacing system tokens define the recommended values. Apply these to your product’s custom components and layouts, replacing any hardcoded values.</p><p>If the right system token doesn’t exist, <a href="/m3/pages/spacing/applying-spacing#f1a6df59-f03d-4949-b1e6-d2dd4422c730" target="_self">customize the system</a> and add your own.</p>

Button with spacing tokens for all padding and gaps.

<p>Many Material components map to spacing system tokens </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp475gv4-02.png?alt=media

A list of spacing system tokens from 100 to 400.

<p>System tokens define all spacing values recommended by Material</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp475tmf-03.png?alt=media

<h3>Spacing complements text scaling</h3><p>When text is scaled up to 200%, the same spacing should be preserved by default.</p>

A button with text scaled to 200% uses the same spacing tokens as an unscaled button.

<p>Keep the same spacing when text scales</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp4783qn-04.png?alt=media

<h2>Customizing the system</h2><p>The spacing system is meant to capture Material’s design intent, but customization is expected and often necessary. How you customize the system depends on your needs:</p>

<h3>Customize Material’s existing component spacing</h3><p>Use this approach to customize how the base component appears across the entire product. </p><ul><li><p>For example, change the “button top padding” mapping from <strong>space125</strong> to <strong>space200</strong> for a taller default button.</p></li></ul>

A button’s vertical padding is changed from space125 to space200.

<p>Customize component spacing to change it across the entire product</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp47e5lm-08.png?alt=media

<h3>Add custom system spacing &amp; patterns</h3><p>Use this approach when you need spacing units beyond what Material provides, or have common adaptive spacing patterns in your product. </p><ul><li><p>Follow the multiplier pattern for new space tokens, so <strong>space225 = 18dp</strong> (8dp x 2.25).</p></li><li><p>Spacing patterns unique to your product can be tokenized.</p></li><ul><li><p>For example, if cards and sheets adapt horizontal content padding the same way, you could create a <strong>surface content horizontal padding</strong> token for that pattern. </p></li></ul></ul>

An outlined card and a bottom sheet both use the surface-content.padding.horizontal spacing pattern token.

<p>For products that adapt spacing the exact same way, consider creating a token for that pattern</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp47j8c0-09.png?alt=media

<h3>Add adaptive layout &amp; density</h3><p>Use this approach when you want the same core component, but want it to appear differently in specific situations, like screen sizes and density settings.</p><ul><li><p>Adaptive layout: Map the spacing to different system tokens for each device type, such as mobile or desktop</p></li><li><p>Density: Adapt vertical padding to different spacing values for each setting</p></li></ul>

A button’s spacing changes based on if it’s on mobile, desktop, cars, XR, or TVs.

<p>Components can be customized to adapt spacing to each form factor</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp47k75s-GM3%20-%20Spacing%20-%20Applying%2001%20-%20%20IA%20-%20v01.mp4?alt=media

A list item’s spacing changes based on density settings of 0 to -4.

<p>Components can be customized to adapt spacing to density settings</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp47kp67-GM3%20-%20Spacing%20-%20Applying%2002%20-%20%20IA%20-%20v01.mp4?alt=media

## Tokens

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">The spacing system tokens are only used on Jetpack Compose.</div></div></div>

<h2>System spacing tokens</h2>

resourceName: designSystems/20543ce18892f7d9

libraryModuleType: MEASUREMENT

moduleConfigurationOverrides: {'tokenSets': ['Spacing'], 'tokenSetOrder': ['Spacing', 'State - focus indicator']}

<p>System spacing tokens are a linear range of spacing values recommended by Material. They’re intended to cover the majority of spacing needs within the design system. The base unit of measurement <strong>md.sys.measurement.space100</strong> is <strong>8dp</strong>. <a href="/m3/pages/design-tokens/overview/" target="_blank">Learn more about design tokens</a></p>

The spacing system tokens, built from 8dp (1x). The range covers 0x to 9x.

<p>The main spacing units are multiples of 8dp</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp47oayx-01.png?alt=media

<h3>Nested units</h3><p>Values other than multiples of 8 are also used in layouts and Material components, like 2dp, 4dp, 6dp, and 10dp. Material only defines the most recommended nested units.</p>

The spacing system defines tokens for 0.25x, 0.5x, 0.75x. 1.25x nested units.

<p>Material only defines nested units that are actively used in common layouts or Material components</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp47p71x-01.png?alt=media

<h2>Component spacing</h2>

<p>Most Material component spacing attributes will map to system spacing tokens. Spacing logic, like adaptive design or density, should be applied to the component attribute.</p><p>Component attributes follow a new naming strategy:</p><ul><li><p>Going forward, all component spacing attributes will use <strong>padding</strong>, <strong>margin</strong>, and <strong>gap</strong>, and positional language: <strong>horizontal</strong>, <strong>vertical</strong>, <strong>leading</strong>, <strong>trailing</strong>, <strong>top</strong>, and <strong>bottom</strong></p><ul><li><p>Example: “Medium button: leading padding”</p></li></ul></li></ul><ul><li><p>Past component spacing tokens use “<strong>space</strong>” to describe all padding, gaps, and margins, like <strong>leading-space</strong>, <strong>trailing-space</strong>, <strong>top-space</strong>, <strong>bottom-space</strong>, and <strong>between-space</strong>.</p><ul><li><p>Example: “Medium button: leading space”</p></li></ul></li></ul>
