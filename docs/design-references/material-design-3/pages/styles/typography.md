# Typography

Source: https://m3.material.io/styles/typography
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/f6a1d89a-1bbf-46d1-a177-f13b074897a5.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Use typography to make content readable and beautiful

## Overview

<ul><li id="isPasted">M3 type scale has 30 type styles: 15 baseline and 15 emphasized</li><li>Use variable fonts for more control over expression in editorial treatments</li><li>Use Material tokens to easily define font, line height, size, tracking, weight, and more</li></ul>

Type at different scales.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmac4t99d-1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Ow6KY2aDdXx4z-a13GYltf1azIa1Z7_G14M0uTeS0FODRiM87ScDy0_7hf5FPWHi3K2FhNto9ddP94U7DQ6SxWXOODeYz2gmfdaiz1amwgc=s2048

<h2>Availability &amp; resources</h2>

<p>This shows where the type scale is available and implemented into Material components.</p>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="text-align:center"><p>Type</p></th><th style="text-align:center"><p>Link</p></th><th style="text-align:center"><p>Status</p></th></tr></thead><tbody><tr><th rowspan="2" style="width:24.9716%;text-align:center"><p>Design</p></th><td><p><a href="https://goo.gle/m3-design-kit" target="_blank">Design Kit</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://fonts.google.com/" target="_blank">Google Fonts</a></p></td><td><p>Available</p></td></tr><tr><th rowspan="7" style="width:25%"><p>Implementation</p></th><td><p><a href="https://api.flutter.dev/flutter/material/Typography/Typography.material2021.html" target="_blank">Flutter</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://developer.android.com/develop/ui/compose/designsystems/material3#typography" target="_blank">Jetpack Compose</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/Typography" target="_blank">Jetpack Compose: Expressive</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://github.com/material-components/material-components-android/blob/master/docs/theming/Typography.md" target="_blank">Android Views (MDC-Android)</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://github.com/material-components/material-components-android/blob/master/docs/theming/Typography.md" target="_blank">Android Views (MDC-Android): Expressive</a></p></td><td><p>Available</p></td></tr><tr><td><p><a href="https://github.com/material-components/material-web/blob/main/docs/theming/typography.md" target="_blank">Web</a></p></td><td><p>Available</p></td></tr><tr><td><p>Web: Expressive</p></td><td><p>Unavailable</p></td></tr></tbody></table></div>

<h2>Updates</h2>

<p><strong>Aug 2026</strong></p><h3>Language script height support</h3><p>Material’s type scale can adapt line height automatically based on language script height category: small, medium, large, and extra large.</p><p>Components can then adapt their size based on these language heights.</p><p><a href="/m3/pages/typography/type-scale-tokens#fcae9063-6c70-4512-87f9-3b6e0d8aea04" target="_self">More on language height</a></p>

Different line heights produced by different languages using Roboto Flex.

<p>Line heights for styles like display large can automatically adapt to language height</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsnchyy9-07-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Ql7ueWNCFSLsuK7NfReD5y3mNiMYG7Aj4ElKQwULjQnV8N5GNXa6o9sDVnvlmeC_wKTtiYaZ4OijJ40_TP0ciTxk7siIfp_iC9uCszHMijCkUw=s1352

<h2>M3 Expressive update</h2>

<p><strong id="isPasted">May 2025</strong></p><h3>Updated M3 type scale with emphasized styles</h3><p>Material’s type scale includes fifteen <strong>baseline</strong> type styles, the same as before, and fifteen new <strong>emphasized</strong> type styles. </p><p>The emphasized type styles add more expression to highlighted moments.</p><p>Roboto Flex can be used on its own to show a range of emotional states, but is not yet part of the M3 typescale.</p><p><a href="/m3/pages/typography/type-scale-tokens#0020d4d9-4f5b-4666-b3ce-c26db849bd73" target="_blank" rel="noopener noreferrer">More on how to use emphasized styles</a></p><p><a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank" rel="noopener noreferrer">More on M3 Expressive</a></p>

Type scale showing roles for “display”, “headline,” “title,” “label,” and “body.”

<p>The expressive type scale includes fifteen baseline type styles and fifteen emphasized type styles </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmac5g88o-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/H7HQemhAdElVd6cCDlOyh0FhU3h8iD8kugnlLUFn1ScP8us3nqj1FslGURTVbbimZIHOCkIrjq5jOek3D3ixq8KMwNug0qPwL0lTzv_IgSFFjQ=s1353

<h3>Emphasized type style tokens</h3><p id="isPasted">Design tokens offer an improved way to define typography in products by assigning an element's type style by a configurable value, rather than a set value.</p><p>Emphasized tokens allow for clearer hierarchies and prioritized components within a layout.</p><p>Type roles describe size—such as small, medium, and large—enabling them to adapt and respond to the device or context.</p>

Close crop of markdown text showing type scales referenced as “display-large” and “display-large-emphasized.”

<p>Typography tokens describe scalable size that adapts to devices or settings, including updating the style on boldness</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmac5las9-3.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/FtpfhAnHzRkv9v64Ec7o6iT9LCg4Jz4rj6beaUd0tsyefFzccM8XPfIk8KUC3sKxmzAo86-JF6bqX9KbIDd9hKgLJssWwzkR_qv84q6XKLtGww=s1353

<h3>Google Design: Making Google Sans Flex</h3><p>Learn how seven design problems shaped Google’s iconic typeface — from inception to going open-source.<br /><br /><a href="https://design.google/library/google-sans-flex-font" target="_blank">Read the article on design.google</a></p>

Animation with different Google Sans Flex font styles.

<p>Google Sans Flex can morph into an impressive range of styles, powered by its six variable axes</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmphesmyk-01_GSF-Hero-Light-mode--16x9%205%20(1).mp4?alt=media

<h2 id="isPasted">Previous updates</h2>

<h3>Variable fonts</h3><p id="isPasted"><strong>Roboto Flex, Roboto Serif, &amp; Roboto Mono</strong></p><p>Updated considerations for using variable fonts and different combinations of their customizable <app-froala-tooltip-element description="An axis refers to an attribute of a font, such as weight or width, that can be altered to create visual variations." link-label="Learn more about variable fonts" link-url="https://fonts.google.com/knowledge/introducing_type/introducing_variable_fonts" should-open-link-in-new-tab="true">axes</app-froala-tooltip-element>, including grade, width, weight, slant, and optical size.</p>

Roboto Flex, Roboto Mono, and Roboto Serif type rendered in different weights.

<p>Roboto Flex, Roboto Serif, and Roboto Mono have a fluid range of axes, like weight, across all optical sizes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmac5s4nr-4.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/we3vYf_MjDkGtTCWCHtjyBnTR8ZxGvmuFuINerK11qOETI1nPgsP4BGjVzHed9z-fxsd3CrRow9ZZZ_yiNszFXJ28JMSJXxiHB2dHLoJVeT84g=s1353

<h3 id="isPasted">Style roles</h3><p id="isPasted">Type styles are defined by five roles: display, headline, title, body, and label.</p><p>These names are more descriptive, allowing for easier matching of type style to use case.</p>

Different examples of Roboto scaled to their respective roles: display, headline, title, body, and label.

<p>M3 has five distinct type styles: display, headline, title, body, and label</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmac5vn8t-5.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/1ln7XGlJMAaZg3R5bogSK2Zon8ogE5VFdjtWg8khP2lcT9mS6Vf7zocKBH0gFLcSYCeAPhxsTK0QibKMM8dJpFD7E13YaNMv-JrAO42Gt59I=s1353

## Fonts

<p>Static fonts like <a href="https://fonts.google.com/specimen/Roboto" target="_blank" rel="noopener noreferrer">Roboto</a> are currently applied by default to all Material 3 components. <a href="https://fonts.google.com/knowledge/introducing_type/introducing_variable_fonts" target="_blank" rel="noopener noreferrer">Variable fonts</a> like <a href="https://fonts.google.com/specimen/Roboto+Flex" target="_blank" rel="noopener noreferrer">Roboto Flex</a> have many more axes for expression, but aren't yet part of the M3 typescale.</p>

<h2>Default typefaces</h2>

<h3>Roboto</h3><p id="isPasted"><a href="https://fonts.google.com/specimen/Roboto" target="_blank" rel="noopener noreferrer">Roboto</a> is the default typeface for Android, and is used in the <a href="/m3/pages/typography/type-scale-tokens#6a9f9f26-99bb-4185-82fc-a49725da0d01">M3 typescale</a>. </p><p>Roboto includes over 3,300 glyphs for representing hundreds of languages around the world.</p>

A type specimen of Roboto.

<p>Roboto is the default typeface in Android and Material 3</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmac6ta60-1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/EkQ4Y0uqlLElvat_6ww9vzPrWILAT3Vmp3N5K4fsgMwOoxdBEmscWHqdqigR2wP6paFXmpLmPryht8MUzVfvYsKv4uAd7_uGZOG_TnBKnUY=s1352

<h3>Roboto Flex</h3><p id="isPasted"><a href="https://fonts.google.com/specimen/Roboto+Flex" target="_blank" rel="noopener noreferrer">Roboto Flex</a> is a variable font which adds more flexibility to typography. It has an extended range of weights, widths, and additional customizable attributes (like size-specific designs), and includes over 900 glyphs with support for Latin, Greek, and Cyrillic.</p><p><a href="https://fonts.google.com/specimen/Roboto+Flex" target="_blank" rel="noopener noreferrer">Roboto Flex is available</a> as a standalone font.</p>

A type specimen of Roboto Flex.

<p>Roboto Flex includes the styles of Roboto plus many more weights and widths optimized for larger and smaller sizes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmac6xqph-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/2aZeUHyOXe0yaUcZk4yCg774-k1UiVi02FyOfoVMwRc1hJTsOhERLuU7fzXgJsTmmT6Hkv8Ds-c_c-T3pS1LwR1EZ_72IuKHTINCta9jux8yww=s1352

<h3>Roboto Serif</h3><p><a href="https://fonts.google.com/specimen/Roboto+Serif" target="_blank" rel="noopener noreferrer">Roboto Serif</a> is another variable font family, designed to create a comfortable reading experience. Minimal and highly functional, it can be used anywhere (even in app interfaces) due to its extensive set of weights and widths across a broad range of sizes.</p>

A type specimen of Roboto Serif.

<p>Roboto Serif offers a functional set of weights and widths</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmac73g8d-3.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/X-iJXo_zFMwPCclGNPUUQqHm-184vE84Tavs2SsYupdFJJBIAP0O5Bg5lyCtlVAFBlWuyLLUtylgWg7PaPfDnG9q1ScWji7GqYu0-OsOSkyw=s1352

<h3>Roboto Mono</h3><p id="isPasted"><a href="https://fonts.google.com/specimen/Roboto+Mono?query=roboto" target="_blank" rel="noopener noreferrer">Roboto Mono</a> is a monospaced version of the classic Roboto design. Being monospaced means each letter has equal space, and letterforms are adjusted to properly fill the space. </p><p>Monospaced fonts are easier to scan vertically, so are particularly useful for code and keeping numbers aligned. <a href="/m3/pages/typography/applying-type#f0f79df7-3174-4012-871e-93ce9a89d08b" target="_blank" rel="noopener noreferrer">Learn more about monospaced numbers</a></p>

A type specimen of Roboto Mono.

<p>Equal sizing for each character keeps uniformity of spacing</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaca32t3-4.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LMaircDfjO77VgbiKJNAz8UcxIc3kRufjePle2i7oLH9_kbvgEGcxU8IjCuv73lMDsSubbBX6YIz5VwFKDMwVmnFMDR7IJjROyxshjuvS-o=s1352

<h3>Noto Sans</h3><p id="isPasted"><a href="https://fonts.google.com/noto/specimen/Noto+Sans" target="_blank" rel="noopener noreferrer">Noto Sans</a> is a global font collection for all modern and ancient languages.</p><p>Each Noto Sans family is compatible with Roboto and Noto Sans supports more than 150 scripts and thousands of languages. It is used as a “fallback” font, when a language is unsupported.</p><p><a href="https://m2.material.io/design/typography/language-support.html#language-considerations" target="_blank" rel="noopener noreferrer">Learn more about typography language considerations</a></p>

A type specimen of several Noto Sans fonts.

<p>Several Noto Sans fonts for different writing systems</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaca7fj8-5.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/pfAhMuBM9hfiSa6uPDzCRHCivlqUZ6jZufCyaijjSuTHmKxJwz-x5YthTtaa9bJWQCPgLrFzlDRtf4rVtbr1d_CvvZ05ULtnMuTvDlogxv8=s1352

<div class="table-wrapper"><table style="width:100%" class="fr-table-selection-hover"><thead><tr><th class="fr-cell-handler ">Variable font<br /></th><th class="fr-cell-fixed ">Available axes<br /></th></tr></thead><tbody><tr><td>Roboto Flex</td><td><p id="isPasted">Slant, Width, Weight, Grade, Optical Size. </p><p><strong>Advanced axes</strong><strong>: </strong>Thick stroke (XOPQ), thin stroke (YOPQ), counter width (XTRA), uppercase height (YTUC), lowercase height (YTLC), ascender height (YTAS), descender depth (YTDE), figure height (YTFI)</p></td></tr><tr><td>Roboto Mono</td><td>Weight, Italic</td></tr><tr><td>Noto Sans</td><td>Width, Weight, Italic</td></tr></tbody></table></div>

<h2>Fallback protection with variable fonts</h2>

<p>Font fallback is when a similar font is used as a replacement when the current font doesn't support the text's characters.</p>

<p id="isPasted">For example, products using the variable font Roboto Flex should apply font fallback in the following order:</p><ol class="decimal"><li>Roboto Flex</li><li>Roboto</li><li>Noto Sans font collection</li></ol><p>This ensures that text will have a consistent visual style regardless of font support. Designers should connect with their product and engineering partners to confirm that font fallback is available.</p>

Text examples from Roboto Flex, Roboto, and Noto Sans all show similar styling.

<p>Font branding is preserved when moving from Roboto Flex to Roboto to Noto Sans Japanese</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacamced-6.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/YAKWH5m4gHCZZlFNYswkO0AkAzGy39AcNVu1zG3poVn-n0jXXQy7nKpgT-w_ftH9tYe9ezdfEoanZrlhRsCDlgujAbHLrZuk-3wJD3i0K5Y3qA=s1352

## Type scale & tokens

<h2 id="isPasted">Type scale</h2>

<p>A <strong>type scale</strong> is a selection of type styles used across a product to ensure consistency.</p>

<h3>M3 type scale</h3>

<p id="isPasted">Material 3 has one <strong>type scale</strong> containing two sets of <strong>type styles: 15 baseline</strong> and <strong>15 emphasized</strong>. Both of these style sets follow the same scale from Display Large to Label Small.</p><p>The <strong>emphasized</strong> styles were added in the <app-froala-tooltip-element description="The expressive update is a major update to Material 3, adding visually stunning features, components, and variants, plus updates to the shape, motion, and typography systems." link-label="More on M3 Expressive" link-url="https://m3.material.io/blog/building-with-m3-expressive" should-open-link-in-new-tab="true">expressive update</app-froala-tooltip-element>. They have a higher weight and other minor adjustments compared to the baseline styles, and are best applied to bold, selection, and other areas of emphasis. Baseline and emphasized styles are meant to be used together.</p>

Diagram of the M3 type scale.

<p>The scale is a range of contrasting styles that support the needs of various product contexts and content. No single product will use all the styles. Instead, select styles from the scale that are most appropriate.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacb26zl-1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/amY56CFDJ81aqWy-r-zpQAOH7D0J7NcLDAwmuuikQnZjnYA4NWUs_V2C8LbxFeekKK7u4itaTFKgnRcXm-QFA56Uoe0N4Jvw38RM5tb5Pas=s2048

<h2>Type scale tokens</h2>

<p>Each of the 30 styles has a single <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">token</app-froala-tooltip-element> that captures all the default properties. Tokens are separated into the <strong>baseline</strong> and <strong>emphasized</strong> sets. Each axis and property, such as font, line height, size, tracking, and weight, also has an individual token for greater customization. <a href="/m3/pages/design-tokens/overview" target="_blank" rel="noopener noreferrer">Learn more about design tokens</a></p>

<h3>Baseline type style tokens</h3>

resourceName: designSystems/20543ce18892f7d9

libraryModuleType: TYPOGRAPHY

moduleConfigurationOverrides: {'tokenSets': ['Type scale'], 'contextTags': ['Static', '3P', 'Android'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Emphasized type styles</h2>

<p>The M3 type scale has 15 emphasized type styles. Use both baseline and emphasized type styles together to achieve expressive experiences. Material recommends using emphasized styles for selection, actions, headlines, and other <a href="/m3/pages/typography/editorial-treatments#19e5796e-9db8-4687-b20c-c6cee77e7df8">editorial treatments</a>.</p>

<h3>Emphasized type style tokens</h3>

resourceName: designSystems/20543ce18892f7d9

libraryModuleType: TYPOGRAPHY

moduleConfigurationOverrides: {'tokenSets': ['Type scale - Emphasized '], 'contextTags': ['Static', '3P', 'Android'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Where emphasized styles can be used</h2>

<h3>Components</h3><p id="isPasted">When used in components, emphasized type styles can communicate hierarchy or importance, such as an active or selected component, or an unread message. The emphasized styles work well with:</p><ul><li>Badges</li><li>Buttons (for primary actions)</li><li>Extended FAB</li><li>Selected list items</li><li>Selected menu items</li></ul><p>Material components don’t use emphasized type styles by default. To use an emphasized type style, swap the baseline token for the emphasized token of the same style. For example:</p><ul><li>Baseline: <span class="inline-code">md.sys.typescale.display-large</span></li><li>Emphasized: <span class="inline-code">md.sys.typescale.<strong>emphasized</strong>.display-large</span></li></ul>

<h3>Weight</h3><p>Use the emphasized styles on text that already uses weight (such as medium, bold) to communicate hierarchy.</p><h3>Context</h3><p id="isPasted">Use emphasized styles to draw attention to specifics aspects of components, such as selected states, unread messages, or key interactions.</p><p>Emphasized context and weight can be used at the same time.</p>

Diagram showing emphasized styles being applied in and UI of an active call with live translation turned on.

<ol class="decimal"><li>Weight: Apply emphasized styles to text already bolded for an expressive style</li><li>Context: Apply emphasized styles to text in selective places to better communicate hierarchy or state</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacdkln0-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/BgMRvZc8eDdo9v86kNxhCNOiSw1Wv7fkVbYTLq_bY9QZXLfKuC-AaQn9_JmKDhbOBqdxmYoznv1ZlBhyigk8PYfuwAsrtaBtp7YqDQadYcs=s1352

<h2>Customize the typeface</h2>

<p id="isPasted">The M3 type scale has the option to set different typefaces at different sizes. </p><ul><li>The <strong>brand</strong> typeface is used for larger type styles, like Headline and Display, to focus on expression. </li><li>The <strong>plain</strong> typeface is used for smaller type styles, like Body and Label, to focus on readability. </li><li>Roboto is the default for both typefaces.</li></ul><p>Consider replacing Roboto with different typefaces to boost brand expression in your product. On emphasized styles, this can help important text stand out even more.</p>

Diagram showing emphasized styles being applied in a UI of an active call with live translation turned on.

<p>Roboto can be replaced with another font, like Roboto Flex</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmace0z70-3.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/g9DqjzaO9IE8RDby0QNqBhA2ORXpJ6LzeQitQ8ql9vjVgAq-HdXrE2H6miAmVUmPg8StgGRTuivI4jbi07oOlgwaGbRqHWXxJ_WFpgEKroE=s1352

<h3>Brand and plain typeface tokens</h3>

resourceName: designSystems/20543ce18892f7d9

libraryModuleType: TYPOGRAPHY

moduleConfigurationOverrides: {'tokenSets': ['Fonts & weights'], 'contextTags': ['Static', '3P', 'Android'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Language height support</h2>

<p>The type scale can adapt line height automatically based on language height category: small, medium, large, and extra large.</p><p>Development considerations:</p><ul type="disc" style="list-style-type:disc"><li><p>It’s recommended to default to <strong>medium language height</strong>, as most languages fall in that category, and switch to other sizes based on detected language.</p></li><li><p>Material components that use <strong>vertical padding</strong> should adapt to language height automatically. Components with fixed heights are built for <strong>small</strong> values and may not adapt by default.</p></li><li><p>Ignoring language height can lead to overlapping text and broken UI elements, leading to major internationalization issues and failing readability standards.</p></li></ul>

Different font stylings produced by Google Sans Flex.

<p>Line heights for styles like <strong>display large</strong> can automatically adapt to language height category</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsnco8tv-07-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/u7Z-_b4B26KtA8LDUvPsn5c7v1Nro5RKxDhlSi5lo9fZdbcTgka8YsFe37XfoBs2eUKKb4_4wlnVuXj9FHqBlSPxpRSUBCOYSjBP6nsl9io8=s1352

<h3>Language script categories</h3><ul type="disc" style="list-style-type:disc"><li><p><strong>Small (base)</strong>: Cyrillic, Greek, Hebrew, Latin-based languages (except Vietnamese)</p></li><li><p><strong>Medium (~7% taller)</strong>: Amharic, Arabic, Armenian, Bangla, Chinese, Gujarati, Hindi, Japanese, Kannada, Khmer, Korean, Lao, Malayalam, Odia, Punjabi, Sinhala, Tamil, Thai, Vietnamese, most other languages.</p></li><li><p><strong>Large (~30% taller)</strong>: Burmese, Telugu</p></li><li><p><strong>Extra large (~100% taller)</strong>: Nastaliq</p></li></ul>

<h3>Language height tokens</h3><p>To view the language height tokens:</p><ul type="disc" style="list-style-type:disc"><li><p>Open the line height folder (Note: Other tokens like fonts and weights are in the same token set)</p></li><li><p>Change the language height context at the top of the token module</p></li></ul>

resourceName: designSystems/20543ce18892f7d9

libraryModuleType: TYPOGRAPHY

moduleConfigurationOverrides: {'tokenSets': ['Fonts & weights'], 'contextTags': ['Small', 'Large', 'Medium', 'Extra large', 'Default', 'Static', '3P', 'Android'], 'showInlineTokenShare': True}

<h2>Customizing type styles</h2>

<p id="isPasted">To customize existing type styles, follow these steps:</p><ol class="decimal"><li>If using a different typeface, change the <strong>brand</strong> and <strong>plain</strong> typeface tokens. </li><li>Adjust properties like line height and letter spacing to refine the appearance. Avoid changing the type size; this can affect how components render and reflow.</li><li>Repeat for both baseline and emphasized type styles. Try to keep emphasized styles visually consistent, like all wider than baseline.</li></ol><p>Heavier fonts may require wider letter spacing, while fonts with long ascenders and descenders will require different line heights. Axes can be further adjusted as necessary.</p><p><strong>Note: </strong>Customizing the M3 type scale or individual styles may prevent you from receiving typography token updates from Material.</p>

Example type scales with custom typefaces and weights.

<p>Adjust variable axes, like weight and width, to customize fonts like Roboto Flex</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmace6o98-4.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/_m1zTD4Gi4KPsQMGUpK7qL86M3rIVacDUvNQ7i5HaJo8NdSeOhwaENqa5-3h64LQvXvMvYBavxmc3Av1xXsjzrXprS94NLoWXW8f9U9Hgmc=s1352

<p>Different typefaces can be used for baseline and emphasized type styles. </p>

Example type scales with custom typefaces and weights.

<p>Custom typefaces can be used together, like Baskervville and Jacquard</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaceaanz-5.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/sGMcrXhB7QJhOFzV-xacTe303tOTltCuwv8Q2SukZmhV3NQHnq_iG8PFNUFO4vZcsvw8yXBfbZKrBSDUVfLNHD8MLGkADAkEZlMmt-x0X3Xv=s1352

<h2>Customizing your type scale</h2>

<p>When different sizes from the defaults are needed, such as for different devices, you can customize the <strong>type scale</strong> by adding or removing styles, and even swapping out Roboto for a font of your choice.</p>

<p>Material Design uses the <a href="https://cieden.com/book/sub-atomic/typography/different-type-scale-types#:~:text=with%2520dense%2520content.-,Major%2520Second%2520(1.125),-The%2520Major%2520Second" target="_blank" rel="noopener noreferrer">Major Second</a> type scale with 14 as its key base size. This anchors to the most essential style used most often for typesetting body text.</p>

Material Design’s default type scale; showing display, headline, and title sizes shown next to the Major Second type scale.

<p>The Material Design type scale uses the Major Second scale (1.125)</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaceu8zs-6.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/sFRSmvfHXtfmkTWjKolzUx_FVsx1Wk7TdhlEbZghSzOlE5PUUIZyuZzTrrDnjNz4KdHsfIYmNkl0AOzDU_0b-gyFAoQGEmrc59K-DCffHOuQqg=s1352

<p>Sizes on the rendered type scale should aim to provide impactful contrast between sizes by avoiding small differences. </p>

Material Design’s default type scale; showing display, headline, and title sizes shown next to the Major Second type scale 

<p>Material’s default typescale of 15 styles allows distinction between each</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmafu03rn-7.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Nx97D2MglZAzPxplWfi3WPeAEFe25ZcDawcLFYNtEUgipcPuIYlBhu9UJz1Om37aaNNJsedqc2_GtAyGQbJ18cnN_d7NBbgCyzVNefFK11OP=s1352

 Display, headline, and title sizes shown next to the Major Second type scale.

<p>Your product likely will not need all 15 default styles from the Material Design type scale. In this example, five sizes are chosen for a reduced set while the rest are removed.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmafu0asd-8.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/QE19ztycbnNNUFjh8L-ZuduDXTf9wRLL1-C6LF7AObKQfHIp-EarhDb5oFJasPUifApzn7hvKoJv4O9HXril3zO7T6MUvXp45RRsGqGHtHnt=s1352

A size modification of Material Design’s default type scale where display medium is a larger size than the original scale.

<p>If the default sizes from the Material Design type scale do not meet your needs, values can be changed instead. Here the default size of display medium is adjusted to another size from the Major Second type scale.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmafu0fju-9.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/TBQySbWTWvPfIelbkG1IzExEagGmvKGd4J0oXsqaHgR6RhY5hYjMTgEox8AAMKpPAMlSSemH_usJBkUdqgjrdP6DcNqPyFLaM7tf_CyrC-tB=s1352

<h3 id="isPasted">Font size units</h3><p>The following units are used to express font size on Android and the web.</p>

<div class="table-wrapper"><table style="width:100%"><thead><tr><th>Platform</th><th>Android</th><th>Web</th></tr></thead><tbody><tr><th>Font size unit</th><td>sp</td><td>rem</td></tr><tr><th>Conversion ratio</th><td>1.0</td><td>0.0625</td></tr></tbody></table></div><p>Web browsers calculate the REM (the root em size) based on the root element size. The default for modern web browsers is 16px, so the conversion is SP_SIZE/16 = rem.</p>

<h4>Example conversions</h4><div class="table-wrapper"><table style="width:100%;margin-right:calc(0%)"><thead><tr><th style="width:50%">Android</th><th style="width:50%">Web</th></tr></thead><tbody><tr><th>10sp</th><td>0.625rem</td></tr><tr><th>12sp</th><td>0.75rem</td></tr><tr><th>24sp</th><td>1.5rem</td></tr><tr><th>60sp</th><td>3.75rem</td></tr></tbody></table></div>

<h3 id="isPasted">Letter spacing units</h3><p>The following units are for spacing letters in a UI.</p>

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="width:35.982%">Platform<br /></th><th style="width:29.5352%">Android<br /></th><th style="width:34.4828%">Web<br /></th></tr></thead><tbody><tr><th>Letter spacing unit<br /></th><td>em</td><td>rem</td></tr><tr><th>Conversion ratio<br /></th><td>(Tracking value in px / font size in sp) = letter spacing</td><td>(Tracking value in px / font size in sp) = letter spacing</td></tr></tbody></table></div>

<h4>Letter spacing examples</h4><div class="table-wrapper"><table><thead><tr><th>Android</th><th>Web</th></tr></thead><tbody><tr><th>(.2 tracking / 16sp font size) = 0.0125 em<br /></th><td>(.2 tracking / 16px font size) = 0.0125 rem</td></tr></tbody></table></div>

## Applying type

<h2>Applying type</h2>

<p>The Material 3 type scale organizes styles into five roles that are named to describe their purposes: display, headline, title, label, body. Each role has three sizes: large, medium, and small. These roles and sizes create clear page hierarchy and work across many devices.</p>

<h2>Roles</h2>

<h3 id="isPasted">Display</h3><p id="isPasted">There are three display styles in the default type scale: Large, medium, and small. As the largest text on the screen, display styles are reserved for short, important text or numerals. They work best on large screens.</p><p>For display type, consider choosing a more expressive font, such as a handwritten or script style.</p><p>If available, set the appropriate optical size to your usage.</p><p><br /></p>

Example display typeface.

<p>An expressive typeface can be used for display styles, as shown here with Bagel Fat One</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacjmd1h-01.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/8H5ycQ1-OMDMOpm5DgFFWidq_Okpm6BM17OLchSyKl2LZFXzjGM9A6dRFOJFPwqNAb_h-sM6j2gLBkqVX8r0G1PnSFfBOnA_i0cSJMQ2pb0U=s1353

Card featuring display size font.

<p>A card using a display size</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacjqddd-02.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/VKnwTJQVXxmdP4HLu06Lpsd_tzims7cWUebvUbzaIRbqyAsJ8PgHE5sE1Xw6R6E_jEOJRhudmdDjcJM1fT_wQcxrQ9RN-JjE0MOExEH6IIyF=s1005

Large expressive typeface set above text.

<p>An expressive typeface can entice readers to engage with an eye-catching design, as shown here with Anton</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacjwt1d-03.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/gBZ5ABDVZLrxKfGgYFQwgF15iCaVlXFv_AbYNhood8JTuhjN-Ge-oO5Kvw-vv9vYY5iGFQ7JRrJQhCdGN2hmr8QT-89WUq1apSyaA-_OabA=s1005

<h3 id="isPasted">Headline</h3><p id="isPasted">Headlines are best-suited for short, high-emphasis text on smaller screens. These styles can be good for marking primary passages of text or important regions of content.</p><p>Headlines can also make use of expressive typefaces, provided that appropriate line height and letter spacing is also integrated to maintain readability.</p>

Example expressive headline typeface on phone screen.

<p>Expressive typefaces can be used for headlines styles as well, as shown here with Anton </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacjyz7x-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/nME8j5BDEOvfxHL88Boi8xquwyjTGfY2BO1sHRlKiFyxp6oAe7ZXOz5rdd8b2ec7mhpf3m2f78Llxk1ObaBNSc8843DQ6DqRURNMsqDdFghK=s1353

The name Ana Russo in headline style in a contact card.

<p>Headline style used for short text on a small screen</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmack0w9r-05.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/9gDfz6o18x2TZ_CwtmIUlwZGMDuYtvEALaw7NNfPkyVjXC7ohfVQNHAGO6hsHOBjqyVGAde_h9ZqL4Z7axGvbY0nNZyuJ4aFeLBBdlRzJn0K1A=s1005

Headline style set above body text.

<p>Dialog using a headline style</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmack28hn-06.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/WgoT1XvqTt4wZhUpmGfNdEPfzpIwynAczo074zAPDqGDh1zgevOnEBr7NBzygCZwDOMFgAhQMxy6vqfG5v_pPpjsgSLlMKCJCUpxIKQgp8TW=s1005

<h3 id="isPasted">Title</h3><p id="isPasted">Titles are smaller than headline styles, and should be used for medium-emphasis text that remains relatively short. For example, consider using title styles to divide secondary passages of text or secondary regions of content.</p><p>For titles, use caution when using expressive fonts, including display, handwritten, and script styles.</p>

An article card using title style for the article title.

<p>A news article title using the title style to capture attention, as shown here with Bebas Neue</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmack408c-07.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/5G71cITshP3sV3xndkrvWC-qCR4KIpdNQvZX02xhz0UbkMnoiizvlOGjADZw89VSYWhToOArHVkmgHQ4DZze2UAQ8xHQrlTEik7_Y7zyj70rEA=s1353

Top app bar using title style for the contact name, Aki Aro.

<p>App bar using title style</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmack6viy-08.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ut0Cn4jh3w2EXk_xbcH6qxLhTDArU8B2ujqURlHJO2AIJhN_ROI9HLRP1JVeVIYq_uAqFsVNshblhlefeMzqXtIVZoTrp5J_Veo8AcNse9j8Mg=s1005

Title style stating ‘Top News’ above headlines.

<p>Example of title style applied to a category header: Top News</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmack8igb-09.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/PmeB6Sb4pU6IWk4zdomBh172gtNSXDNKKxYmozS8wejGX-PrRleZViqtUiZAw1th1K3rQ3OQzw5BdCjP3junPZzB84HIGKB8uV9CglMC13k=s1005

<h3 id="isPasted">Body</h3><p id="isPasted">Body styles are used for longer passages of text in your app.</p><p>Use typefaces intended for body styles, which are readable at smaller sizes and can be comfortably read in longer passages.</p><p>Avoid expressive or decorative fonts for body text because these can be harder to read at small sizes.</p>

Body-style typeface.

<p>Body styles must be readable for long passages</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmackbvpu-10.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/4wCbM5DljexhIPLTZFvjaWRYHzSxV7CbB0EAR8C5Jd8_NEFVJUmsQVu4RZP4EohwY1Xn5waxFIw--co_wEViXOYg9GBUVTVLweYYEnQJ1hg=s1353

Body style text in article.

<p>Body style used throughout an article about pesto</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmackfzlx-11.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/jiXtjNSWMzkij9Tg6MWqQWGbu5ynGPuZygOcoE9KQH_zCJVPKhwT8h5pqbcEfqo8x71U6LPZ8Mn2LyDwPWnYW7n1jP4C1vALM0y8GTJUFZxR=s1005

Three stacked examples of body style in app setup flow.

<p>Example of body style used throughout a setup flow</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmackjtaf-12.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/nPH5mSOx4oou5T1tL0ejKZgTfRZa-kJGE4yZVUtyikQCi8WpJAY3nyrXdWyS0snoE4A6s11xx8HaETNT0n-4oFdHb2dGSvZymlsUI-S5rR89DA=s1005

<h3 id="isPasted">Label</h3><p id="isPasted">Label styles are smaller, utilitarian styles, used for things like the text inside components or for very small text in the content body, such as captions.</p><p>Buttons, for example, use the label large style.</p>

Several label-style buttons on compact window.

<p>Label styles should enable quick reading at small sizes, such as in buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm845h3dq-13-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/XuTl5skaB_JIORrVcCDmo_Y_XStoycO_IRnuIcpIS8T2V2cFJp5Xxq42rg6Si3tibDFsxm_SJ3rePNwt3Zvj4JvKDLijnl2OEaXwAfsWKepZyw=s1352

Music player timecode featuring label style.

<p>A music player using label style for the timecode</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmackqp3j-14.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/NQhKlAFb1pQR0_FithdIHxbrXSaK3l7cSuURn9AYJ_gr97XaQ-BwqlewnDm1u6X1MT0WkROeOfkCcGdsYQpj2mVivtnhqk34KqsReF2x5Vk=s1005

Five labels set horizontally across the navigation bar.

<p>A navigation bar using label style for the destination text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmafuf50h-15.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/NlIJB8O4GVLye38a7knugkMHgnsPN_JwctP0QTjy1jVi3S8_-bpCLo91_SOgM5VMhHzptxz0kd3pBYGYjWup8kTeGeCbjntcCVZEU1OJAyuLng=s1005

<h2 id="isPasted">Typesetting</h2>

<p id="isPasted">Vertical typesetting relies on padding, bounding boxes, and baselines to ensure text legibility at any size.</p><p>Take engineering considerations and the conventions of your platform into account when making decisions for typesetting, text resizing, density, and using text in adaptive layouts.</p>

<h3 id="isPasted">Using padding and bounding boxes</h3><p>Use this method for web products, and iOS products, where applicable. Note that some design tools also use bounding boxes for typesetting, but their methods vary and will need to be reconciled with the engineering implementation.</p>

<p id="isPasted">In web UIs, the line height and bounding box height are the same. Text is vertically centered within the bounding box, following the “<a href="https://www.w3.org/TR/css-inline-3/#leading-trim" target="_blank" rel="noopener noreferrer">half-leading</a>” behavior established by CSS.</p><p>The vertical position of the text isn’t controlled directly, but through the combination of the bounding box and font metrics.</p>

Diagram of bounding box equaling line height.

<p>The bounding box height is defined by the line height specified, with equal space placed above and below the text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmackyuk9-16.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/kVdAGQXhGi2W9YfH3N0ZX9KJkKnpc-bsjOAg3tWtYeHr8x--uTrk_Y49tvDT3rwtVE12G-je8FG3rd6DywqSfWXwBk2M7pAulya83Ml3wjGB1A=s1353

<p>Padding is the space between UI elements, such as between an image and a bounding box, or between the inner edge of the bounding box and the text.</p>

Diagram of 20 dp padding above text.

<p>The padding surrounding the text bounding box</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacl0ia5-17.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ofazdaoe9Y2mL4Oefj7g_L7-yaRVZecYmExPhqw0CMVWbzn18xGdzzxkXOak_FQ8oszI1XH-BUgAsd3eiDWomwVhGZlkdlB1sdcEtlV0Vtg=s1353

<p>Specify the distance of UI elements from fixed reference points, such as the container edge. For the web, automate this calculation using Sass or CSS.</p>

Measurements of label text padding.

<p>Use line-height, padding, and container measurements for setting typography on the web and iOS</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacl33y5-18.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/c-Xd3srZz38eMpP89GGFUqL6ibDUlvLILbWmE3SyIadz3v6osx2jNpQzXuXwj30_jUHhPSkP5ALsu_hOJGi3k-JrXkk5WXglGiz0dILEruNp=s1353

<p id="isPasted">Vertical alignment using padding and bounding boxes:</p><ol class="decimal"><li><strong>Line height</strong> <br />Measure the height of the bounding box.</li><li><strong>Centering</strong> <br />Ensure equal top and bottom padding around the inner edge of the bounding box by using center align</li><li><strong>Spacing</strong> <br />Use the height of the bounding box, and top and bottom padding to determine spacing</li></ol>

Diagram of using padding and bounding boxes to measure line height, alignment, and spacing,

<p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacl7cnr-19.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/gR_zZUnknndcR-NJEotK-rshizgc54jUA7qzp0TDrYV1sNjprNeUNsoETn72KqcrWT61bX5nIXUDpVr035eFbh_KkJgB8uP1J-7ExXAZ6BS6=s1353

<h3 id="isPasted">Using the baseline</h3><p>Use this method for Android products or platform-agnostic specs.</p>

<p>The baseline is the invisible line upon which a line of text rests. In Material Design, the baseline is an important specification in measuring the vertical distance between text and an element.</p>

Diagram indicating the baseline of text.

<p>A line of text rests on the invisible baseline</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacldncz-20.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/I5c-Uge53PpSAf_V5JUBMML3_1ouix0TL99xVBLgNv5BNuQrxb1UhPEvP2TzubpCPApEwSredZQ6hDxVhAe0luStrcv4LddwoThxLQUfyEU=s1353

<p id="isPasted">For Android, specifying distances relative to baseline enables accurate implementation.</p><p>The baseline can also be used to communicate text position between designers in a way that's agnostic to the platform or design tool.</p>

Diagram of the distances between overline and container edge, plus subhead, overline, and caption text.

<p>Android screens rely on distance to baselines for spacing</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmafug7pc-21.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/CgXx25YXSe1l2T7QqEmDtLD-9vptGuT9ONqs_Z_ymaTncdxWIBMIrPzO3Svt_DL2zooqVZLGPsfN4MvZtE79JI6iSEm51TC3bI3eejLy34A=s1353

<p id="isPasted">Vertical alignment using the baseline: </p><ol class="decimal"><li><strong>Line height </strong><br />Measure distance from the text baseline of one line to the text baseline of the next line</li><li><strong>Centering</strong> <br />Specify center alignment as a reference instead of measuring the distance to the text baseline</li><li><strong>Spacing</strong> <br />Use the distance from a reference point to the text baseline</li></ol>

Diagram of using distance to baseline to measure line height, alignment, and spacing.

<p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacln6jx-22.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/3yEErrAiImN-qxnPPc_ln0WeE416pEN7iHaRcQPlzMluvla5w0ZoK09oTGefSQrgIaj29bUZrFG1T0sVHpTdOWUxGge1g9wQZideSuhMrUoSHw=s1353

<h2>Ensuring readability</h2>

<p id="isPasted"><strong>Line height</strong></p><p>Line height is the space between each line of text and is directly connected to type size.</p><p>Material’s type tokens are optimized for intended size and use.</p>

An example of larger type with a line height ratio of 1.2

<p>For larger type legibility using styles like title, headline, and display, we recommend a line height ratio of 1.2 times the type size</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacludjq-23.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LFuKIi2aGlf72f_A3yvGE-ncHvn7nQ3yj7M7zHCEljgjxJaWDtMrgjuHKy557yVppBOtlIEVl2SVHTbr_8QaHGPqSLdk6ZTPFvcXuoxIFJfs=s1353

An example of body type with a line height ratio of 1.5.

<p>For smaller body copy using styles like body and label, we recommend a line height ratio around 1.5 times the type size. If your line height is too tight, you’ll undermine the flow of the text. Too loose, and the lines won’t feel cohesive.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaclv7q4-24.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/TFXkp4WANGrF2VJ6AbJuYKFWa7QOOTDp-uchUNK6nBhk9-Qp2gg2V96xdgH8U3yjYoJCVNa2ln1-em5gCbw2bqSZWL1Pf5w7Iawhzi5Cf8p3=s1353

<p id="isPasted"><strong>Tabular numbers</strong></p><p>Use tabular figures (also known as monospaced numbers) rather than proportional digits in tables or places where values may change often, such as clocks.</p><p>Use monospaced tabular numbers to keep values optically aligned for better scanning.</p>

Vertical view showing the spacing variation in proportional numbers versus monospacing of tabular numbers.

<ol class="decimal"><li id="isPasted">Proportional numbers</li><li>Monospaced tabular numbers</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmacly990-25.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/BskG7G1_XEXDjk548Xw7DT4xxmlW8ePL0ZOQdihQTM6AsDSWbuh1FCaOKu_ZpCrhev8DeIHKo42vtcOG5zsrFOJ5aXdzxysJfoAfXNpQaFA=s657

Times displayed in tabular numbers.

<p>Use tabular numbers to prevent layout shifting when values change, such as in a clock UI</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaclzivd-26.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/iHKpHXTPSACBPeqMQw5d7GXnBYWQAH9j4B-8UqXZXH37-TISFiAqYf-tgnbb1URd992HF0u8KH9ed0AdrRysgEbV6Dnk8dKCFtiUBH5npG0l=s985

<h2>Using Material Symbols with typography</h2>

<p>Properly aligning typography with Material Symbols can improve cohesion and unity in your product. <a href="/m3/pages/icons/applying-icons#f9db4adc-ca78-473f-85eb-a351b73c39ac" target="_blank" rel="noopener noreferrer">Learn more about matching icons and text</a></p>

<h2>Accessibility</h2>

<h3>Color &amp; contrast</h3><p id="isPasted">Support visual accessibility by choosing the appropriate <strong>color contrast</strong> between your product’s text and background. Contrast is the perceived difference between the lightness or darkness of two colors, and is quantified by a <strong>contrast ratio</strong>.</p>

Contrast between two colors, quantified by a contrast ratio, supports visual accessibility.

<p>Label styles should enable quick reading at small sizes, such as in buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadkak1u-27.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/goFACyp-thAmu70hw0vYZBOFWv7OySfYv9HRNwXvZMIQ9P2WCiyHyfgsCJE35fGXFpwSskOWX_XLoWaA7uz97PuPZ1lh_jw9sH0eaRiFGtc2=s1353

<p id="isPasted">Text should achieve sufficient contrast between its color and that of its background. </p><p>Material aims for two main text contrast levels:</p><ul><li>3:1 for large text</li><li>4.5:1 for small text</li></ul><p><a href="/m3/pages/designing/color-contrast#b248ecd2-9abd-4877-8f5e-ebfbb87e2048" target="_blank" rel="noopener noreferrer">Learn more about contrast ratios</a></p>

Large text should achieve a contrast ratio of 3:1.

<p>Large text should achieve a contrast ratio of 3:1</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadpdpks-28.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/BQrWDyWcMYdh73-KDAcTBnrN6snUfkRYAk9jBe5H_H-sW2D7QoGhfd2JyDkshiNIegJcCCFFzUAxOCJ5nOL1CyynkzZIi0h80ORRJWlTH6bs=s657

Small text should achieve a contrast ratio of 4.5:1.

<p>Small text should achieve a contrast ratio of 4.5:1</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadpf3uf-29.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/rm7l0bh9fJXOLnItYdu2yaS-j4Gf-4E2vUOL8lxqDUKc4iIquoSwzQyYC-a_bm_g7cMyoPoZAcWTRfRGUHDTVpRJDT-7kPeBABfgkropDVS7=s657

<p>The default color for typography is <strong>on surface</strong>, although <strong>on surface variant</strong> is a strong alternative.</p>

Diagram showing the default color for text is "on surface."

<p>Default typography colors</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadpks74-30.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ayTGM2gQl4WO4HvOrLK5f70D7Y0VT99OWKYt9hlElb-p0I_osOhWKGEW6bsvl-n-WRXm5dJLa6Q2EIEH2TyfG0lpBuvbxKv_jIIEAGHdUWDK=s1353

<p id="isPasted">For hyperlinked text appearing on top of a <app-froala-tooltip-element description="Color role used for the default color for backgrounds." link-label link-url should-open-link-in-new-tab="false">surface color</app-froala-tooltip-element>, use <app-froala-tooltip-element description="High-emphasis fills, texts, and icons against surface." link-label link-url should-open-link-in-new-tab="false">primary</app-froala-tooltip-element>. However, <app-froala-tooltip-element description="Complementary fills, text, and icons against surface." link-label link-url should-open-link-in-new-tab="false">tertiary</app-froala-tooltip-element> can be used to make links less prominent.</p><p>Hyperlinked text must also be underlined.</p>

In a paragraph, md.sys.color.primary color is applied to an underlined hyperlink. 

<p>Hyperlinks should be underlined and use primary or tertiary color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadprtta-31.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/H_inQMJPALlTfpigo59TGxaJOCDjGokqyP8bDE-QBzvRu7vSbbgTS43k-iIM6ReCC2N3WWJG4DiFGdCNS8UVTVICpnXRPHs5FrCfE140VQw=s1353

<h2>Scaling type</h2>

<p>Maintain hierarchy and scaling across devices by modifying certain elements as you scale.</p><p><strong>Scaling from watch to mobile</strong>: Increase the size of <strong>headlines</strong>, <strong>display</strong>, and<strong> body</strong>.</p><p><strong>Scaling from mobile or tablet to desktop: </strong>Increase the size of <strong>display</strong> and <strong>headline</strong>.</p>

<p>Roles of the same name can scale with the device size.
</p><ol><li>Display
</li><li>Body</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fkuhiupqv-Watch%20phone.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/mK32BtuqIhseHxjWVUmFOVsznjZZ--FOlGPZ6kuA27yX0PAZLvLGSc0E-D4SvZFF3yOZR_FVNwdMhf3cdwpQqZNRjsM_uv3a169JrjqYMJB6=s1352

<p>When scaling between a desktop and TV display, increase the size of headlines and body type.</p>

<p>Tablet (left) and desktop (right) both use:
</p><ol><li>Headline
</li><li>Body</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fkuhiw34t-Tablet%20TV%20(1).png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LUhGJMGK2capjl2cYgtYhyHQgZMAr2Ht7G0SayIK_95XECcneerDBkIQeJgEx3TbBQ_4hQadjcY2n6aIJsB-smrrJtMrdjxOUEgOWVz0PgPY=s2048

<h3>Multi-column scaling</h3><p>As your layout adapts to different device sizes, consider maintaining the focus of an area by increasing the type size of that element. This example shows a column configuration scaling from a closed mobile device to an unfolded mobile device. The most prominent card (1) scales to maintain hierarchy.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fkuob7g0r-Multi-column%20scaling.png?alt=media

<p>(removed per b/304969883)</p><p id="isPasted"><strong>Line length</strong></p><p>Line length is how many characters are on a single line of text. </p><p>For longer body text, the recommended line length is between 40 to 60 characters.</p><p>For shorter lines of text, the ideal length is 20 to 40 characters.</p>

Range of longer text lengths from 0 to 90 characters per line, with ideal set at 40–60 characters per line

<p>For longer lines of English text, the ideal line length is 40–60 characters per line</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fl1fee676-type-length.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/e3iXYSVluHN3XYqUyfKbKGw2DJS5Llqu_qdEdiSbBmE8zCF6lU1sedLF5jG4rgT4lCaZ5bJZhzp-Hm3KrtGEcJR1qfocEbjFvnNlHIjq7MeD=s2048

Range of shorter text lengths from 0 to 50 characters per line, with ideal set at 20–40 characters per line

<p>For shorter lines of English text, the ideal line length is 20–40 characters per line</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fl1fehc9v-type-length-short.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-tIQTUsWSLg9LcriJ0FdR-8_VvP7LyKXh5Ul39xmq1itoDjwwZig9yf2Km_G5Y-9sY2BQd48mRyYXVy-IYJsxPfGpgNNKupB8KZiilJOSlSu=s1352

## Editorial treatments

<h2>Editorial treatments</h2>

<p id="isPasted">Editorial treatments are standalone, showcase moments driven by type. They involve dynamic, attention-grabbing use of custom sizes, which can involve larger display type or a blockier look and feel. They should depart from purely functional layouts or basic stages in a user flow. </p><p>In the expressive system, editorial treatments can be combined with elements such as motion, shape, or color, to create product-wide hero moments. </p>

A series of editorial moments making dynamic use of type, including a calculator, lock screen, and temperature.

<p>In editorial treatments, type can freely dominate the screen</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadq1nd5-01type.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ev53UZRK0CWfnDhs22jim_yhZFnSolBEPg5IwuUJGgwWnqZA3iT58c-MAmi7YIOejurCjFd0EYTpAZ1POQsLbGMtdLiHE9gZMvp3csxwtt4T=s2048

<h2>Examples of editorial treatments</h2>

<p>Use editorial treatments in three key ways: to celebrate content, to highlight the voice of the user, or to draw attention to bespoke functionality within the product.</p>

<h3>Celebrating content</h3><p id="isPasted">Editorial treatments can dramatically take over the screen to mark a particular user action, memory, or preference.</p><p>Try matching the text to the tone of the product or a strong emotion, like a narrow, thin style for serenity, or a bolder, italicized style for liveliness.</p>

Large type reading “Mesa Verde National Park” with a hiker in the foreground.

<p>Use an exuberant cover image for a photo album, here shown with Roboto Flex</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadq59l2-02.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/_f96Z-GV-cAbQmpKCj-Keg6s4rM6TfNLrZzkjpFVRS2wnACMbvScj90pXQqDVkQsrXv3HuwAPI2GoFFbLjYhfTlFp66pmIY7VFy7BBxvwglCCA=s1352

<h3>Voice of the user</h3><p id="isPasted">Express the voice of the user by letting them personalize the appearance of typography or by adjusting text based on their input.</p><p>Use customization selectively to frame a user’s mood and make it stand out.</p>

A text exchange in which one party is responding enthusiastically in extremely large letters.

<p>A response with the right type treatment can convey ecstatic emotion. Here, the text is shown in Roboto Flex and PT Serif Caption.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadq8d7w-03.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/aIWtxiI3mObxA5vNa0tgNA8a89V2FRGKJIPDwOFDDjqkYNShmdmFAnqptxLK4bmFCFEPvZSZw9vJ2dWwT_R00KolfVj8le1Iu-yZexlmpimB9Q=s1352

<h3>Bespoke functionality</h3><p>Editorial treatments can also be used to help express moments of unique functionality within the product experience.</p>

A slider to adjust bedroom lights. The characters increase in width and weight as the brightness is increased.

<p>The increase in the bedroom light brightness prompts an algorithmic response in the width and weight axes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadqb4ho-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/MOKMcp4KQUKuarOagUBezjsmfRUftgg4bZuIe7ss8B-RpdEBvAAintWivpRfcCCukxxgqDKpP3EoaJLD6HfOEg3KMQBlEK2n-NRxLLWcqFEmJQ=s1352

<h2>Editorial treatment best practices</h2>

<p id="isPasted">As there is intentionally much room for choice in developing editorial treatments, there are a few guard rails that will prevent inconsistency, illegibility, or distracting design.</p><p>These best practices include:</p><ul><li>Ensuring consistency between similar-looking editorial moments, creating tokens for each where needed</li><li>Matching the emotional tone of text to the task at hand</li><li>Not mixing multiple or clashing styles in the same layout</li><li>Not mimicking personalization theming</li></ul>

A UI showing two instances of editorial treatments with consistent styling.

<p>Create tokens for editorial treatments to apply them consistently in your product</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadqewpk-05.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Hq2u6GmGN0yhP8it7ZGnfq7l-Sz8WJI9dtf_X2yoQcR-bABUUYLFkSvA5u2Kwg8UsW4eFmWsLfHVvLYPYnvkGk5aHUKtOgxhqOrLE4hqQy33=s1004

A UI featuring a name in which the first is using a different custom type treatment than the last.

<p><span style="white-space:pre-wrap">Use caution when mixing different editorial treatments in the same layout. Try to keep them consistent.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaeb01ji-06.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/cgEb-7BELW0DgVCVjNDR09llaf4g6CODZmX1BFJMIFGgYjW_799tmagHG-VY3DONxmeawi1nOji7NiZqi2oLYuz3Dn3TIr0Sxj8q4iSdMlxG=s1004

<h2>Use variable axes to make editorial treatments</h2><p>Adjust variable font axes like weight, grade, width, and optical size to match the font to the feeling. Baseline and emphasized type styles can still be used. Though, editorial treatments shouldn’t be used in labels or just to give information.</p>

<h3>Weight</h3><p id="isPasted">Weight is the primary attribute that defines the overall thickness of a typeface’s strokes in any given font. The most common weights are regular and bold, but weights can cover extremes from the very light to the very heavy.</p><p>If the typeface is variable, it provides a full, continuous range of stroke thicknesses, making the number of weights effectively unlimited.</p><p><a href="https://fonts.google.com/knowledge/choosing_type/exploring_typefaces_with_multiple_weights_or_grades" target="_blank" rel="noopener noreferrer">Learn more about weight on Google Fonts</a></p>

Many examples of Roboto Flex weights.

<p><span style="white-space:pre-wrap">A variable font, Roboto Flex offers a fluid range of weights</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaeb490s-07.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/_ZH0Kaelt3AZp6-KW-_8iAzJpqXcmjFDowWlVM8kdesekBF7fRPS7YoVYtNw7CBck4R4YUGb-tPiDMqwGJeK8qtEb9JscawmvErJ9mTZ09Q=s1352

Light text in use as body text.

<p>Be careful when using very light weight for body text. Lower-resolution displays can struggle to show thin typography, especially at small sizes. Instead, consider lighter weights at larger font sizes, such as display type.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadqr5nh-08.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/c_gKfZUEwNoMuE_swIkrig6cXFWytTkRd1ZgI2m5mVSsJBiEc9TTlcy0CLJ8HlIEfj4ZfunjBfob6jM0h0oC9hny61MIjrECjNBRSbT2WBE0=s1004

Navigation bar using bold typography for label text, making it challenging to read.

<p><span style="white-space:pre-wrap">Excessive weight at smaller sizes can make text harder to read</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaebxgxh-09.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/JxEboJh8oUw3JAa08wTj7Yl8CndLBoOChr9amAJTMlo2v6WBmFGEqQwYMI54QJPq3D0mNC9mpltggO0NWeOato8W2AUEH_x5_APOOUkGX4w=s1004

<h3>Grade</h3><p id="isPasted">Grade is a secondary modifier of a typeface’s optical weight, independent of the weight axis. Both weight and grade axes affect a letter’s thickness, but adjustments with grade are much more granular and don’t change any letter widths or line breaks.</p><p><a href="https://fonts.google.com/knowledge/choosing_type/exploring_typefaces_with_multiple_weights_or_grades" target="_blank" rel="noopener noreferrer">Learn more about grade on Google Fonts</a></p>

Three ampersands set in Roboto Flex without grade over Roboto Flex with 150 grade.

<p>Roboto Flex offers a positive grade of 150 and a negative grade of 200</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadqz6gm-11.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/3HqXaLryPKUIj1IaC5Rfnzdcj2s1OVUJKRqjKUBPXN3TB9Q4x_1sCfQcEmsNsb0CI5OHaSGT-IugniC48bWebADFxLnygmoQp10QlzBHNPc=s1352

A light and dark screen each showing the letter B.

<p>When switching between dark and light mode, the same text may appear heavier despite having the same settings. Consider using a negative grade to counteract this.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadr3fuu-12.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/nNOT6dZnhO35p9L6JJOMBGxqzuugbja6Bm13PdwoVG5JRWeRH9SY7gs5R929Q4Mn97C6VxJ0ZzG8so1MbJ0dKH2iLgPJqCWkkQqNzvmlyUM=s1004

A list of amenities where the filter chip for “Elevator” and “Cats OK” are selected and have a heavier grade applied.

<p><span style="white-space:pre-wrap">Grade can change the emphasis without reflowing text</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaec8aam-13.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/GPx4clVPV4vwGL6n3YNWAOYKhjSlFdl5OkrPdr5P-DM2-QVqrcHiU_DDT2OfiqaN3UsVXr_nDftRzvLDJZBAeb3UQCqy3jVaFDOSuXItueSN=s1004

<h3>Width</h3><p id="isPasted">Width is the result of how much horizontal space is taken up by a typeface’s characters.</p><p>A narrow width allows more characters to fit per line while a wider width may offer more personality.</p><p><a href="https://fonts.google.com/knowledge/glossary/width" target="_blank" rel="noopener noreferrer">Learn more about width on Google Fonts</a></p>

The letter ‘N’, set in Roboto Flex, rendered in varying widths.

<p><span style="white-space:pre-wrap">Roboto Flex offers a fluid range of widths, from 25 to 150</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaecbedx-14.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/fcsjvoTZQgt3S4tEgcJeKkFdxwB7j0kq4rPwSzLExgjzb5GXXaI46dDHnYhSnpdXubMSsV60bO7gd0FHWMHX1neKkRNqysx6pndBj6cYfMSzYg=s1352

A bottom navigation bar with four icons using narrow label text under the icons.

<p>A thinner width can allow for more characters to fit at small sizes, such as in a label</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadrfrnd-15.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/U2pTAHsQjDUKou_PgGuB99jyO_WaBdo3P287QfNNh-mh8zKncXzsZlscbMtSinYtKxkOVd_atokOqK3DAJxl_oa97CvlIdN6yuSeyi4UtH3a7w=s1004

Top app bar with the title best thrift stores in wide type next to three icons.

<p><span style="white-space:pre-wrap">Since wider styles take up more space, avoid using them for areas with limited space, such as in a top app bar</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaecc80f-16.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/iedj4O9hpECTR7nWovYfgsGQE7EsIUxodkH8BdtsXlgJNExF-6VUqjo_DFpfRYt5NW-3tCT1ajOGORVqMO3eFrDG-N2GtNwsNc4teoGITws6-g=s1004

<h3>Optical size</h3><p id="isPasted">Optical sizes are different versions of a typeface optimized for use at different sizes.</p><p>Small size designs focus on enhancing readability, while large size designs can show off the intricacies of the letter forms and offer many more weights and widths.</p><p><a href="https://fonts.google.com/knowledge/choosing_type/choosing_typefaces_that_have_optical_sizes" target="_blank" rel="noopener noreferrer">Learn about choosing typefaces that have optical sizes.</a></p><p><br /></p>

The word hello at a small optical size overlaid over the word hello at a large optical size.

<p><span style="white-space:pre-wrap">The typeface Literata has a continuous range of optical size, from 7pt to 72pt</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaecgvtl-17.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/q145wn11t-bnGKRS9FqXq2XgXL2_zm_vcdzXtRMQj6lhcDjnhss8l3-z4BdWwmrhezO-Nuy-Kyioo2GNnuAhDS0PE8v96c3rxursoJNbhyEK=s1352

The words “massive” and “tiny” with optical sizes that match their type size.

<p>Use an optical size that matches your type size</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadru5uv-18.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/dndDtroXkLO4HSXTtHRwG2SGuUY5X_BhDYYv3jVs6_d73j60NzIiwsuvE3w6uVRulU5gkaab4RGqqcAK2IkHmT72DFVDkQPAUnfL0c2uz4Xi=s1004

Two paragraphs of text set with an optical size larger than the type size.

<p><span style="white-space:pre-wrap">Don’t use large optical type sizes at small sizes. Instead use a smaller optical size, if available.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmaechab8-19.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Dok3HjtThxwrT-s81brs9uAb9koXEA6Zt3CIi-27BWQmypqPMzDfVNYfsrXLmsj43ppF4tN9Z8ouvK2M8GP8TTFT7tqzO17UGdbsRnVpDbJnSA=s1004
