# App bars

Source: https://m3.material.io/components/app-bars
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/4135ef28-314c-44dc-b829-6e94a36b69f2.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Focus on describing the current page and provide 1–2 essential actions</p></li><li><p>Displays labels and page navigation controls at the top of the page. (Use a <app-froala-tooltip-element description="Toolbars display frequently used actions relevant to the current page." link-label="More on toolbars" link-url="/m3/pages/toolbars/overview" should-open-link-in-new-tab="true">toolbar</app-froala-tooltip-element> to display page actions)</p></li><li><p>Four variants: Search app bar, small, medium flexible, large flexible</p></li><li><p>On scroll, apply a fill color to separate from body content</p></li><li><p>Can animate on and off screen with another bar of controls, like a row of <app-froala-tooltip-element description="Chips help people enter information, make selections, filter content, or trigger actions." link-label="More on chips" link-url="/m3/pages/chips/overview" should-open-link-in-new-tab="true">chips</app-froala-tooltip-element></p></li></ul>

4 configurations of app bars stacked vertically to show differences.

<ol class="decimal"><li id="isPasted">Search app bar</li><li>Small</li><li>Medium flexible</li><li>Large flexible</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlktxqjf-01.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/411b03efa2256026

libraryModuleType: STATUS_TABLE

<h2>M3 Expressive update</h2><p><strong>May 2025</strong><br />The new <strong>search app bar</strong> supports icons inside and outside the search bar, and centered text. It opens the <a href="/m3/pages/search/overview" target="_blank">search view</a> component when selected. <br /><br />The new <strong>medium flexible</strong> and <strong>large flexible</strong> app bars come with significant improvements, and should replace <strong>medium</strong> and <strong>large</strong> app bars, which are no longer recommended. The <strong>small</strong> app bar is updated with the same flexible improvements. <br /><br /><a href="https://m3.material.io/blog/building-with-m3-expressive" target="_self">More on M3 Expressive</a></p>

<p>Variants and naming:</p><ul><li><p>Renamed component from <strong>top app bar</strong> to <strong>app bar</strong></p></li><li><p>Added <strong>search app bar</strong></p></li><li><p><strong>Medium</strong> and <strong>large</strong> app bars are no longer recommended</p></li><li><p>Added <strong>medium flexible</strong> and <strong>large flexible </strong>app bars with:</p><ul><li><p>Reduced overall height</p></li><li><p>Larger title text</p></li><li><p>Subtitle</p></li><li><p>Left- and center-aligned text options</p></li><li><p>Text wrapping</p></li><li><p>More flexible elements for imagery and filled buttons</p></li></ul></li><li><p>Added features to <strong>small </strong>app bar:</p><ul><li><p>Subtitle</p></li><li><p>Center-aligned text option</p></li><li><p>More flexible elements for imagery and filled buttons</p></li></ul></li></ul>

4 total app bar configurations.

<ol class="decimal"><li id="isPasted">Search app bar</li><li>Small</li><li>Medium flexible</li><li>Large flexible</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlku5356-05.png?alt=media

<h2>Differences from M2</h2>

<ul><li>Color: New color mappings and compatibility with dynamic color</li><li>On scroll: No drop shadow, instead a color fill creates separation from content</li><li>Typography: Larger default text</li><li>Layout: Smaller default height</li></ul>

M2 top app bar with elevation to separate it from main content.

<p>M2: Elevation and a drop shadow raise the top app bar when content is present underneath</p><p></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmdho0pd-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/cBekWt7xDa8xEu5XXaem1OHo1sbSYkWtpPf8V_6QeBgGzxia-Ba6WoZDfUkaUvywiflh3J89oatLV3Zpqv4DupaDfVyy41vXxkxpDAnEqvaGtw=s1004

M3 app bar with subtle color difference from main content.

<p>M3: On scroll, a color fill overlay separates the app bar from the content beneath</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlkui2vk-07.png?alt=media

## Specs

<h2>Variants</h2>

4 variants of app bars.

<ol class="decimal"><li id="isPasted">Search app bar</li><li>Small</li><li>Medium flexible</li><li>Large flexible</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmagk85x-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/MgtUMHWDy00vUnks39ztFGEG28QfDRkbQeSEcmqqCBT0K5FWc4uP_-7g3LLkrMJC-g76aUQW1xsZQ9AyyGhpc5G3-_Cs_d-CCP7HTCk6LlVi=s2048

<h3>Baseline variants</h3><p>The baseline M3 <strong>medium</strong> and <strong>large</strong> app bars are no longer recommended in M3 Expressive, and should be replaced with <strong>medium flexible</strong> and <strong>large flexible</strong> app bars, which are similar visually, but have multi-line support, a shorter height, and can contain a wide variety of elements, like images. <a href="/m3/pages/app-bars/specs#faec9baf-140f-41dc-8b88-2792e90d9d5d" target="_self">Jump to baseline app bar specs</a></p>

2 baseline app bar variants, medium and large.

<p>Baseline variants</p><ol class="decimal"><li><p>Medium</p></li><li><p>Large</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmar0379-01-deprecated-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/4jbnUGWxs16YDyExE7HfAtikzuBERI0C_O6PT00TGtEezDt5SyYIv-V3mUOU_fOoUYk9hJ4uowBcG1c5bR86ChJqq1RQIhbX8Yp4YTMNnBP7CA=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Variant</p></th><th style="text-align:center"><p>M3</p></th><th style="text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td><p>Search app bar</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td><p>Small</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Center-aligned</p></td><td><p>Available</p></td><td><p>Merged into <strong>small</strong>. <br />Use centered-text configuration.<br /></p></td></tr><tr><td><p>Medium (baseline)</p></td><td><p>Available</p></td><td><p>Not recommended.</p><p>Use <strong>medium flexible</strong></p></td></tr><tr><td><p>Medium flexible</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td><p>Large (baseline)</p></td><td><p>Available</p></td><td><p>Not recommended.</p><p>Use <strong>large flexible</strong></p></td></tr><tr><td><p>Large flexible</p></td><td><p>--</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Configurations</h2>

<h3>Text alignment</h3>

4 variants of app bars with different left and center aligned text headlines.

<p>Text labels, including supporting text, can be aligned to the leading edge or centered</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmah1clb-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/BOvvsqx3bdHcU0IHwgEXTkgiwJuhU9DOQ6kiQLIdTQ8qiU9YfauXCNFb6HxOTs-PbX7r-OTeqQBlOav0aNXzUSe6JfDHP8zw2jDorA65wQo=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Category</p></th><th><p>Configuration</p></th><th style="text-align:center"><p>M3</p></th><th style="text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td rowspan="2" style="width:25%;vertical-align:top"><p>Text alignment</p></td><td><p>Leading edge (default)</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Centered</p></td><td><p>--</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Tokens &amp; specs</h2><p>Select a token set to view in the table's menu. App bar token sets are organized into a common token set, and size-specific tokens. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/3ec622835c7987b5

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['App bar - Common', 'App bar - Size - Small', 'App bar - Size - Medium Flexible', 'App bar - Size - Large Flexible'], 'contextTags': ['Static', '3P', 'Android'], 'tokenSetOrder': ['App bar - Common', 'App bar - Size - Small', 'App bar - Size - Medium', 'App bar - Size - Large', 'App bar - Size - Medium Flexible', 'App bar - Size - Large Flexible', '[Deprecated] App bar - Top, small', '[Deprecated] App bar - Top, medium', '[Deprecated] App bar - Top, large', '[Deprecated] App bar - Top, center-aligned'], 'hideSearchField': False, 'hideVersionName': True}

<h3>Search component tokens &amp; specs</h3><p>The default <app-froala-tooltip-element description="Search lets people enter a keyword or phrase to get relevant information." link-label="More on search" link-url="/google-material-3/pages/search/overview" should-open-link-in-new-tab="true">search</app-froala-tooltip-element> component tokens are used in the search app bar.</p>

resourceName: designSystems/20543ce18892f7d9/components/07341534518f78d0

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Anatomy</h2>

5 elements of the component.

<ol class="decimal"><li id="isPasted">Container</li><li>Leading button</li><li>Trailing elements</li><li>Headline</li><li>Subtitle</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmahcxrn-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/UCS56fBRH7I7KiKUuK_vBKPDUCV85-8G25OIOM9PxyVN3dgUEozWDPgj2liGjw8OI7X5PTD6n2Icr1V7sZOS-nxTjMPTIth4wlj9KfX7kUth=s2048

<p id="isPasted">App bars can be customized to include:</p><ul><li>An image or logo</li><li>A subtitle</li><li>A filled icon button</li></ul><p>Avoid customizing the size of the heading and subtitle, or adding too many actions. </p>

3 app bars: 1 with a newspaper logo, 1 with a subtitle, and 1 with a filled icon button.

<p>The app bar can have different layouts depending on which elements are shown</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmahfvsg-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Fwsip8AL-32WvFsouymOxtfDAK9nsgZu6JggbrZsEe1uIQ8Tm8E48NLKY4SPX1C687pcmu65V9xyHu3pme-1kwEyl5YsC1OFfJAKZlLlAGmI=s1352

<h3>Search</h3>

<p>The search app bar can include trailing actions inside and outside the search bar. When the search bar is selected, it should open the <app-froala-tooltip-element description="The search view is a full-screen modal often used to display a list of search results. It can also be opened by selecting a search icon." link-label="More on search view" link-url="/m3/pages/search/overview" should-open-link-in-new-tab="true">search view</app-froala-tooltip-element> component.</p>

5 elements of the search app bar.

<ol class="decimal"><li id="isPasted">Container</li><li>Leading icon button</li><li>Hinted search text</li><li>Trailing icon or avatar</li><li>Search container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmahnmz2-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/OCgIkeJ9Mk6ibxz6tz0uSYOLL4zgYINQJdBhE0uqKG_KivTrv_i-4wbgiz0sNLxmAymZPsvXyPnH2i49hWvgI39jvCv0yra8PF-vnxPR3xFt=s2048

3 layouts of icons in the search app bar.

<ol class="decimal"><li id="isPasted">A leading element and a trailing element outside search</li><li>A leading element, a trailing element inside search, and a trailing element outside search</li><li>A leading element and two trailing elements outside search</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmahv36y-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/T7dF8lnMsgF-ctH-bJxhvlTFNYfNCtaKFJ3_kWhNeWOT70jVcz5e2K6dcCMdvyTEMMwCh0VusP7U_cQT5PbY5eBTpwClU8jQPYWIUhRPfLImPA=s2048

<h3>Image </h3><p>An image can be placed in the app bar. In small app bars, this can replace the label text.</p>

Graphic replacing text headline content.

<p>Images can be added to app bars and can replace label text on small app bars</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmaiawq3-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/rM0ncqi1MU1B-iUCqpNvS1r6GIsPwybXwHKtPEB0hAo1k3NMLM3dqUpH_NK-k9vOlihsEFSneMWwVTYCaF5nWJOEPpRUupcrtmDHCB0C3d8a=s2048

<h3>Filled trailing icon button</h3><p>The app bar's trailing icon buttons can be replaced with a single, primary, or tonal filled icon button in default or wide sizes. </p>

App bars configured with filled trailing icons.

<p>The trailing icons can be configured to be a single filled icon button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmaiezk5-08-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-4xgb9ld5H8Q6HnmK-ld1O5qM0mfNJy_2WtE_WggmW1lbxjvzZp6GwimCbCZ92GiXuzdak-pBH-hlzbZ-oyphKRiho2Myrlsaal8-7UtKjqa=s2048

<h3>Subtitle</h3>

App bars configured with subtitles below their headlines.

<p id="isPasted">The medium flexible and large flexible app bars hug the text contents, so they are taller when a subtitle is visible</p><ol class="decimal"><li>Small</li><li>Small with subtitle</li><li>Medium flexible</li><li>Medium flexible with subtitle</li><li>Large flexible</li><li>Large flexible with subtitle</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmao48ka-09-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/v37338PXuQO2QKzvv6eDPG3ATToEprV5f1RbgAP6J85Kkk5uUpqPb3M3U7L3YgKxNTDd_UlhkKMBrpc3PYRL8WgyTS5aax6L2gOQWYwxfsRo=s2048

<h2>Color</h2><p>Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p><p>All app bars share the same color roles. On scroll, the container changes color to <strong>surface container</strong>.</p>

4 color roles of the leading edge app bar in light and dark scheme.

<p id="isPasted">App bar color roles used for light and dark themes:</p><ol><li>Surface</li><li>On surface</li><li>On surface variant</li><li>On surface</li><li>On surface variant</li><li>Surface container (on scroll)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmaoaorq-10-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/xpRALH4p7nwRTCrQbJRWXJjjKyr6SI9Lcz7DShFjgvTK8Zsvl45I69Y-m1OfJcWkp9Cc3cOV4UyCqZzo60kRaRSgGeatz80PbrGnGv1DQpXO=s2048

4 color roles of the center-aligned app bar in light and dark scheme.

<p>Search app bar color roles used for light and dark themes:</p><ol class="decimal"><li><p>Surface </p></li><li><p>On surface variant</p></li><li><p>On surface variant</p></li><li><p>On surface variant</p></li><li><p>Surface container</p></li><li><p>Surface container</p></li><li><p>Surface container highest</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmaod25k-11-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/VsxxC6080HgD_QsQ6TLzafi0UFXVHAU3R4k2NDE144aZQBU9CYNjEOCd7tPTV3ur_gcYzZJO3LezRLYaNLoPcQnYpyuyQyH-C8KLRv1eIC2C=s2048

<h3>Scroll states</h3>

Color roles for app bars when flat and on scroll.

<p id="isPasted">The app bar changes color when flat or on scroll. The search bar can also change color on scroll.</p><ol class="decimal"><li>Flat</li><li>On scroll</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmaof4ew-12-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/tRaHBa-YYJoR3wAF4m6Sr9plFPu3juGtThHBYYsKPfs-6nHxwPrhg7vEpJfwSA6hfyjHrl6k4Tzh4Z6WC95kDllNp9Q5nYiRXO_KpYBKsrIqiQ=s2048

<h2>Measurements</h2>

<h3>Search app bar</h3>

Search app bar size and padding measurements.

<p>Search app bar padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmaonw2d-13-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/GLzA-Bs2FesMv8_iNKDnGK-rmtF4_QBlkamCvjO3g0PR4Ohvu51Whqg_8UDbMF2Be0V0fNt2yy_YIYhbkBa3RaH32GCEcE7CYs7Qk7aJDWg=s2048

<h3>Small app bar</h3>

Small app bar size and padding measurements.

<p>Small app bar padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmaoprdb-14-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ZwtGrnk6IwZVeEjENYgXaaBm1o78pMZeWbKEvSKrXMaC4EsY1x5d6AyMOmeP5xBxsEtomfWPfRQeyjo9aj5TUCZfqTZ6DExOrrf4lPD6skGwOQ=s2048

<h3>Medium flexible app bar</h3>

Medium flexible app bar padding and size measurements.

<p>Medium flexible app bar padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmap4u9c-15-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/tO6HUsX_WzDWijRcUovy7YHYqXB9nFkpIdJ1rb9xRF1f53fb5lfigX2U4DhrYnf54WpJxf_VMpqs2fVNtnQwzv1gxreCwgyge4K5p9WC71BK=s2048

<h3>Large flexible app bar</h3>

Large flexible app bar padding and size measurements

<p>Large flexible app bar padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmapnkl4-16-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LZMvu4Uh6hlTMMN4lXncpG5Pl1yEm5A90QCK9BFFHrKogTsNr1PAWKpJ0su8E4BmXMOdKMzH3jk2BGZJcqrSGZ1AFOK40R6D9QHkBuhtEqgI=s2048

<hr /><h2>Baseline app bars</h2>

<p>The <strong>medium</strong> and <strong>large</strong> app bars are no longer recommended in M3 Expressive. Use the <strong>medium flexible</strong> and <strong>large flexible</strong> app bars in their place.</p>

4 elements of medium and large app bars.

<p id="isPasted">Medium and large app bars have the same elements:</p><ol class="decimal"><li>Container</li><li>Leading button</li><li>Trailing icons</li><li>Headline</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmaqk9ki-17-deprecated-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/spB1ibTSmb0Q0vxy5WCz5hWULWcRYZTwf1gzkHBzBAOOx1kjBmF9_rN3rFooHw8wbZdYdo2piv_rickk6jDEeIefd5ZOWM6Gq7kaaLqNRZib=s2048

<h3>Tokens &amp; specs</h3>

<p>Select a token set to view in the table's menu. Baseline app bar token sets are organized into medium, large, and older baseline token sets. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/3ec622835c7987b5

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['App bar - Size - Medium (baseline)', 'App bar - Size - Large (baseline)', '[Deprecated] Top app bar - Small', '[Deprecated] Top app bar - Medium', '[Deprecated] Top app bar -  Large', '[Deprecated] Top app bar - Small, Center-aligned'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h3>Color</h3>

<p>Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p>

4 color roles of the medium top app bar in light and dark scheme.

<p id="isPasted">Medium top app bar color roles used for light and dark schemes:</p><ol class="decimal"><li>Surface</li><li>On surface</li><li>On surface</li><li>On surface variant</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmaqrta6-18-deprecated-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/a4e5waYXECuiUcxK2FX7nimSG7veFWYYiISRWkojPDXodUOqnLT2npaBpJhmc1AUBfOr9G3hcZ4TmUi9jLCRUdP0IqDw5pTdSCFYgc-zXcs=s2048

<h3>Measurements</h3>

<h4>Medium app bar</h4>

Diagram of medium app bar padding and size measurements.

<p>Medium app bar padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmaquor6-19-deprecated-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/iJPK4tOaZD9dNaqh6nZnimQR2kRKofGNS-fhCmjPY4mo8cyDKbIJg5nY8Osnxa7EVzTNNSIkA_3OqGAYWX8FJbOMxCThqTI6CocN1Ltci4sSaA=s2048

<h4>Large app bar</h4>

Diagram of large app bar padding and size measurements.

<p>Large app bar padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmaqwh2h-20-deprecated-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/JaHOGKnlXOrSArCuG_UGfPN8Muth2rZ_WwBu0ZlvUPFvU8HdVdkDWZoz1M3pm1GB7vw8o_IUE-So65otchOt2cHBpzKsOJTdm2N5uw2aBc-A=s2048

## Guidelines

4 app bars with headlines and action icons.

<p>App bars show information about the page, key actions, and navigation actions like <strong>Back</strong> or <strong>Menu</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnt9v4x-01.png?alt=media

<h2 id="isPasted">Usage</h2>

<p id="isPasted">Use an app bar to provide content and actions related to the current page, such as page navigation actions, headlines, images, and 1–2 essential actions.</p><p>The information and actions in the app bar should be contextual and specific to a page, but can also include global product controls, such as search or notifications.</p>

App bar with navigation icon buttons and a 2-line title.

<p>App bars provide content and actions related to the current page</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlntdon8-02.png?alt=media

<p>App bars should only have one action, two if necessary. </p><p>The primary action should alter or exit the entire page, like <strong>Send</strong>, <strong>Save</strong>, or <strong>Edit</strong>.</p><p>If the product has many actions, place those in a <app-froala-tooltip-element description="Toolbars display frequently used actions relevant to the current page." link-label="More on toolbars" link-url="/m3/pages/toolbars/overview" should-open-link-in-new-tab="true">toolbar</app-froala-tooltip-element>. Avoid placing an overflow menu in the app bar when possible.</p>

App bar with content below.

<p>App bars can display one high visibility action to boost its prominence</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnth1j3-03.png?alt=media

<p>To boost visibility of a primary action, change the style of the icon button to filled or tonal, and consider using a wide icon button.  </p><p>Avoid using multiple filled or tonal buttons.</p>

App bar with 1 filled button.

<p>Use a filled or tonal button for important actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlntiy4b-04-do.png?alt=media

App bar with 2 filled buttons, side by side.

<p>Don’t put multiple filled or tonal buttons in the app bar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlntjjnv-05-dont.png?alt=media

<p>The four variants of app bars are:</p><ol class="decimal"><li><p><strong>Search app bar</strong><br />Use on home pages when search is key to the product. <br /><br /></p></li><li><p><strong>Small</strong><br />Use in dense layouts or when a page is scrolled.<br /><br /></p></li><li><p><strong>Medium flexible</strong><br />Use to display a larger headline. It can collapse into a small app bar on scroll.<br /><br /></p></li><li><p><strong>Large flexible</strong><br />Use to emphasize the headline of the page.</p></li></ol>

The 4 app bar variants.

<ol class="decimal"><li id="isPasted">Search app bar</li><li>Small</li><li>Medium flexible</li><li>Large flexible</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlntmieq-06.png?alt=media

<h3>Baseline app bars</h3><p>There are two baseline app bars that are no longer recommended:</p><ol class="decimal"><li><p><strong>Medium</strong><br />Replace with medium flexible.<br /><br /></p></li><li><p><strong>Large</strong><br />Replace with large flexible.</p></li></ol><p style="text-align:left"></p>

2 baseline app bars.

<ol class="decimal"><li id="isPasted">Medium </li><li>Large </li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlntnwot-07.png?alt=media

<h2>Search app bar</h2>

<p id="isPasted">Use a search app bar to provide an emphasized entry-point to open the search view.</p>

A search bar within an app bar.

<p>Search app bars have a search field instead of heading text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlntr0ls-08.png?alt=media

<p><app-froala-tooltip-element description="The search bar is a persistent and prominent search field at the top of the screen." link-label="More on search bars" link-url="/m3/pages/search/overview" should-open-link-in-new-tab="true">Search bars</app-froala-tooltip-element> should always include the word <strong>Search</strong>. They can use various capitalization styles depending on the product.</p><ol class="decimal"><li><p><strong>Search</strong></p></li><li><p>Searching a specific area<br />Example: <strong>Search inbox</strong></p></li><li><p>Search [Product] <br />Example: <strong>Search Photos</strong></p></li></ol>

3 examples of search text in an app bar.

<p>Use proper capitalization depending on what’s being searched</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlntrvt2-09.png?alt=media

<h3>Buttons in search app bar</h3><p id="isPasted">In addition to a trailing avatar, search app bars can have up to two trailing icons on mobile. </p><p>Trailing icons can be placed inside or outside the search bar. </p>

2 icons placed in the search bar.

<p>Put the most used actions on the left and least used on the right</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlntvpyq-10.png?alt=media

<p>The leading element of a search app bar can be used for a product’s logo to brand the app’s overall experience. <br /><br />This logo can be purely cosmetic, or can trigger an action like returning to the home screen or refreshing it. </p><p>Avoid using a logo to open an <app-froala-tooltip-element description="Expanded navigation rails show text labels and an extended FAB, and can be default or modal." link-label link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">expanded navigation rail</app-froala-tooltip-element>.</p>

A search app bar with a logo, search bar, and avatar.

<p>The leading element can be a product logo</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlntz91y-11.png?alt=media

<p>Don’t use more than two trailing icon buttons with an avatar. <br /><br />If more actions are needed, place them in a <app-froala-tooltip-element description="Toolbars display frequently used actions relevant to the current page." link-label="More on toolbars" link-url="/m3/pages/toolbars/overview" should-open-link-in-new-tab="true">toolbar</app-froala-tooltip-element> instead.</p>

3 icons placed in a search app bar.

<p>Don’t use three icons and an avatar in a search app bar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnu01cf-12-Dont.png?alt=media

<h3>Large screens</h3><p>The search app bar dynamically adapts to available width. There should be up to four trailing icons on larger screens. </p>

4 actions placed in a search app bar on a large screen.

<p>Increased horizontal space on larger screens allows for up to four trailing icons.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnu4je0-13.png?alt=media

<h3>Alternate color options</h3><p>By default, search containers in app bars use the <strong>surface container</strong> color to distinguish it from the app background. If the background is darker, use a lighter container color on the search bar, like <strong>surface bright</strong>.</p><p>When choosing alternate colors, make sure the search text and container have at least 3:1 contrast for readability.</p>

App bar with a light search container color.

<p>Search app bars can use different colors, like <strong>surface bright</strong>, for improved contrast with surrounding elements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnu68g2-14.png?alt=media

<h2 id="isPasted">Anatomy</h2>

 Diagram of app bar layout.

<ol class="decimal"><li id="isPasted">Container</li><li>Headline</li><li>Trailing icons</li><li id="isPasted">Subtitle</li><li>Leading button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnub2xp-15.png?alt=media

<h3 id="isPasted">Container</h3><p id="isPasted">The app bar container holds all information and actions at the top of a screen, including navigation icons, headlines, and buttons. </p><p>Avoid changing the position or shape of the container.</p><p><br /></p>

App bar with square corners.

<p>Use straight corners for app bars</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnuf0r2-16-do.png?alt=media

App bar with curved corners.

<p>Don’t use curved shapes. This implies that the container can expand upon interaction.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnugbt5-17-dont.png?alt=media

<p>Always use the default height of the app bar, and make it span the full width of the window. </p>

App bar at default height.

<p>Default heights were chosen to ensure readability of on-screen elements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnuiiym-18-Do.png?alt=media

App bar with reduced height.

<p>Don't make an app bar shorter than its default height</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnuja9a-19-Don't.png?alt=media

<h3>Adding logos</h3><p>Image logos can be used in app bars to bolster brand identity or visual appeal. </p><p>The image should be high quality and pertinent, and shouldn’t disrupt the app bar's functionality.</p>

A logo added to an app bar.

<p>Image logos can replace all text in small app bars, and appear above the text in other app bars</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnuliot-20.png?alt=media

<h3>Leading button</h3><p>The leading button should be used for navigating the product. </p><p>It typically is one of the following:</p><ul><li><p>A menu icon, which opens a modal <app-froala-tooltip-element description="Expanded navigation rails show text labels and an extended FAB, and can be default or modal." link-label link-url should-open-link-in-new-tab="false">expanded navigation rail</app-froala-tooltip-element></p></li><li><p>A back arrow, which returns to the previous screen</p></li></ul>

Leading navigation icon aligned on left of app bar

<ol class="decimal"><li>Leading <strong>Back</strong> button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnumedg-21.png?alt=media

<h3 id="isPasted">Headline</h3><p id="isPasted">The headline can describe:</p><ul><li>The current page</li><li>The current section</li><li>The product</li></ul><p>Headline text should be brief enough to easily fit in the app bar. </p><p>In medium flexible and large flexible app bars, the headline can wrap to a second line. </p><p>Don’t truncate the headline text.</p>

App bar headline text set in 2 lines.

<p>If headline text is long, use a medium flexible or large flexible app bar and wrap the headline to two lines maximum</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnurf1u-22-Do.png?alt=media

Small app bar headline text wrapped on 2 lines.

<p>Don’t wrap text in a small app bar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnus8yg-23-Don't.png?alt=media

<p>Headlines can be aligned to the leading edge or centered.</p><p>The headline’s typography size and style change depending on the app bar variant.</p>

Search, small, medium and large flexible app bars with headline styles.

<p id="isPasted">Headline typography style for each app bar</p><ol class="decimal"><li>Search: Body large</li><li>Small: Title large</li><li>Medium flexible: Headline medium</li><li>Large flexible: Display small</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnuwnod-24.png?alt=media

<h3>Subtitle</h3><p>Subtitles can add additional context to a page. </p><p>These can be leading-aligned or center-aligned with the headline text.</p>

Small to large flexible app bars with headline and subtitle styles.

<p id="isPasted">Subtitle typography style for each app bar:</p><ol class="decimal"><li>Small: Label medium</li><li>Medium flexible: Label large</li><li>Large flexible: Title medium</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnvaru4-25.png?alt=media

<h3>Trailing icon buttons</h3><p>Up to two icon buttons can be placed after the headline, aligned to the trailing edge of the app bar. Place most-used actions closest to the leading edge.</p><p>Avoid using these buttons to open a menu with more actions. If more actions are needed, place them in a <app-froala-tooltip-element description="Toolbars display frequently used actions relevant to the current page." link-label="More on toolbars" link-url="/m3/pages/toolbars/overview" should-open-link-in-new-tab="true">toolbar</app-froala-tooltip-element> instead.</p><p>If changing the icon button color style to filled or tonal, only use one icon button.</p>

2 icons placed to right of headline, from most to least used.

<p>Put the most used actions on the left and least used on the right</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnvbo80-26.png?alt=media

<p>Use filled icons when possible for the best visibility. Outlined icons can also be used, particularly for unselected toggle <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element>.</p>

App bar with 2 filled icons, “save” and “download.”

<p>Use filled icons for clear, visible actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnvcdyc-27-Do.png?alt=media

App bar with 2 outlined icons, “save” and “download.”

<p>Outlined icons can be used as needed, or when using toggle buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlnvcyu3-28-Caution.png?alt=media

<h2>Adaptive design</h2>

<p>Adaptive design allows an interface to respond or change based on context, such as the user, device, and usage. <a href="/m3/pages/layout-overview/adaptive-design" target="_self">More on adaptive design</a></p>

<h3>Resizing</h3><p>The width of the app bar container responds to the view or device width. </p><p>It should always span 100% of the window width.</p>

App bar resizing to wider view.

<p>The app bar’s container responds to always fill the window width</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlp67nmz-GM3%20-%20Top%20App-Bar%20-%20Responsive%20-%201P%20-%20v01.mp4?alt=media

<p>Resizing may cause actions at the trailing edge of the app bar to collapse into an overflow menu at smaller breakpoints. </p><p>These actions become visible again at larger sizes.</p>

Trailing icons in app bar collapse into overflow when screen size shrinks.

<p><span style="white-space:pre-wrap">Actions at the trailing edge collapse into an overflow menu</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmaco62fo-GM3_Adaptive_AppBar_Guidelines_25_IA_V01.mp4?alt=media

<p>The search container of the search app bar should fill 100% of the space between leading and trailing app bar elements until it reaches 312dp. Then, it should only grow further to fill 50% of that space.</p>

Search app bar resizing to wider view.

<p>The search field adapts to the amount of space between other elements in the app bar</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlp6cznn-GM3%20-%20App-bar%20-%20Guidelines_31%20-%20IA%20-%20v05.mp4?alt=media

<h3>Presentation</h3><p>The app bar automatically supports right-to-left (RTL) languages by aligning the layout of elements to the leading and trailing edges of the container. </p><p>This means that in RTL languages, the layout of the app bar is mirrored.</p>

App bar in RTL with Hebrew text.

<p>The app bar’s layout is mirrored for right-to-left (RTL) languages</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlp6doc5-32.png?alt=media

<h2>Behavior</h2>

<h3 id="isPasted">Scrolling</h3><p id="isPasted">App bars should initially be the same color as the background, then fill with a contrasting color on scroll to provide visual separation from the background.</p><p>The app bar can remain on a page at all times, or can hide and reappear when scrolling.</p>

Scrolling app bar container fills with contrasting color.

<p>Upon scrolling, an app bar container fills with contrasting color to create a visual separation</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlp6geio-GM3%20-%20App-bar%20-%20Guidelines%2033%20-%20v01.mp4?alt=media

<p>To focus more on body content, consider setting the app bar container to be transparent on scroll. This allows the buttons to float above the content. </p><p>Make sure icon buttons have a container fill. </p><p>Consider using narrow-width <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/google-material-3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon buttons</app-froala-tooltip-element> for actions, like <strong>Back</strong>, to reduce the amount of space they take up.</p>

Medium flexible app bar compresses to transform into transparent small app bar.

<p>Upon scrolling, an app bar container remains transparent and actions inside become filled icon buttons</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlp6hnuc-GM3%20-%20App-bar%20-%20Guideline%2034%20-%20IA%20-%20v03.mp4?alt=media

<p>Selecting the search bar should open the <app-froala-tooltip-element description="The search view is a full-screen modal often used to display a list of search results. It can also be opened by selecting a search icon." link-label="More on search view" link-url="/m3/pages/search/overview" should-open-link-in-new-tab="true">search view</app-froala-tooltip-element> component.</p>

A search app bar opening the search view component when selected.

<p>When selected, a search app bar opens a search view</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlp6jluz-GM3%20-%20App-bar%20-%20Guidelines%2034%20-%20IA%20-%20v01.mp4?alt=media

<p>When scrolled, <strong>medium flexible</strong> and <strong>large flexible</strong> app bars can transform into <strong>small</strong> app bars. They should remain small until the page is scrolled back to the top. Don’t transform app bars into a <strong>search app bar</strong>.</p>

Scrolling top app bar compressing to scroll upwards or downward.

<p>The app bar can hide when scrolling up and reveal when scrolling down</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlp6o2a1-GM3%20-%20App-bar%20-%20Guidelines%2036%20-%20v01.mp4?alt=media

Medium app bar compresses to transform into Compact top app bar.

<p>Medium and large flexible app bars can use the compress effect to transform into small app bars when scrolled</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlp6pkl9-GM3%20-%20App-bar%20-%20Guidelines%2037%20-%20v01.mp4?alt=media

## XR

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">This is a rapidly changing space. Guidelines are primarily intended for designers at this time. Find what’s implemented in code in the <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank">design kit</a>. </div></div></div>

<p>Extended reality (XR) interfaces have special design requirements, like showing apps in 3D space. Material has an XR-specific app bar with custom specs and guidance. See <a href="https://developer.android.com/design/ui/xr/guides/foundations" target="_blank">XR developer documentation</a> for more details.</p>

<h2 id="isPasted">Types &amp; configurations</h2>

<p>There is one app bar <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels." link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true">orbiter</app-froala-tooltip-element>. It closely aligns with the <app-froala-tooltip-element description="Small app bars display information and actions in compact layouts. They're often used for scrolled views on subpages that require back navigation and multiple actions." link-label="More on small app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">small app bar</app-froala-tooltip-element>. It can be configured to be center-aligned or left-aligned.</p>

Center and left-aligned app bar orbiters.

<ol class="decimal" id="isPasted"><li>Center-aligned app bar</li><li>Left-aligned app bar</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmdgsmfp-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/PYHwyx3K5m9cJiev6I-MKCs6A60Tc5AZcpBzBcqqGQLSQMnOmNCuR1s8uzfsiZI_Yh3_LoLN1rFIo5dUEv89LWBnr3n7Qobo3yHChEb5_MJK_A=s2048

<h2 id="isPasted">Anatomy</h2>

Diagrams of app bar orbiters identifying 4 internal elements.

<ol class="decimal" id="isPasted"><li>Container</li><li>Headline</li><li>Trailing icons</li><li>Leading icon</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmdh2chl-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/O1YVMPmvL54Qi15A17QmKNzQhv18CgDcmtGdGFtfK60IHEQNqSPp3BAdAJjZugpdBhS_ZoF3t3xcuyZcTP9McxR1FEaLkkluyBbkYPRVDnLduQ=s2048

<h2 id="isPasted">Color &amp; elevation</h2>

<p>XR uses color to communicate the elevation of UI elements and orbiters. With <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation" target="_blank" rel="noopener noreferrer" id="isPasted">spatial elevation</a>, the app bar displays above the <app-froala-tooltip-element description="In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content." link-label="More on spatial panels" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels" should-open-link-in-new-tab="true">spatial panel</app-froala-tooltip-element> on the Z-axis. Elevated app bars can use any of these color options:</p>

3 versions of app bar elevation color strategy.

<ol class="decimal" id="isPasted"><li>Surface container</li><li>Surface container high</li><li>Surface container highest</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmdh5h5z-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/7PoV7x7SsxMju6tTGEHlmT5PdcZ8VVSnzTFYcEIZlLBeIUXbp9RB9T0zphIoaYJFyzQfZyOa2AOpYIANWae0FLpDv1_lqMawI9R0TgXvjcA5=s2048

<h2 id="isPasted">Measurements</h2>

Diagrams with measurements and padding for app bar orbiters.

<p>Measurements and padding for app bar orbiters</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmdh7azy-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/_ROPguXE9EGmEjUSfBAPGksGu_cWhxmyKG7GLSG_qlgGQIpuD8cgrumMEgAPKdaXuxLWFZOqfUEnu6WAqapCHjBPbx1ytlUpSG7_nD0LgA2Z=s2048

<h2 id="isPasted">Usage</h2>

<p>An app bar can appear in an <app-froala-tooltip-element description="Orbiters are floating elements that control the content within spatial panels." link-label="More on orbiters" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters" should-open-link-in-new-tab="true" id="isPasted">orbiter</app-froala-tooltip-element> for a more immersive experience. Currently, this spatial capability is only available in <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components." link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element>. In <app-froala-tooltip-element description="Home space is compatible with mobile and large screen apps, but doesn’t support spatial components." link-label="More on home space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">home space</app-froala-tooltip-element>, use a regular app bar on the same plane as the body content to mimic a 2D experience.</p>

Animation showing an app bar changing from 2D to 3D.

<p>An app bar’s behavior and placement changes from a 2D to a 3D experience</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmagty4xv-XR_Top-App-Bar_Usage_01_IA_v03.mp4?alt=media

<h2 id="isPasted">Behavior</h2>

<h3 id="isPasted">Global context</h3><p>When placed in global context, the orbiter is centered at the top of the app it controls. </p><p>It stays anchored to the app during layout or content changes. </p><p>This ensures navigation elements are always easy to find and use.</p>

An app bar orbiter placed in global context.

<p>Global app bar orbiters should be centered and anchored to the top of the app</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmagu23jp-XR_Top-App-Bar_Behavior_01_IA_v03.mp4?alt=media

<h3 id="isPasted">Local context</h3><p>When placed in local context, the orbiter is centered at the top of the spatial panel it controls. </p><p>It repositions in response to layout or content changes.</p>

An app bar orbiter placed in local context.

<p>Local app bar orbiters should be centered and anchored to the top of the panel. However, this is less common, so make sure that it contains actions that only affect its anchored panel.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmagu4hwu-XR_Top-App-Bar_Behavior_02_IA_v03.mp4?alt=media

<h3 id="isPasted">Additional app bars</h3><p>In most cases, apps should only have one app bar orbiter, placed in global context.</p>

An app switches between 1 and 2 app bar orbiters.

<p>Limit the use of multiple app bars to rare cases when additional spatialization improves usability</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmagu3r6g-XR_Top-App-Bar_Behavior_03_IA_v03.mp4?alt=media

<h2 id="isPasted">Placement</h2>

<h3 id="isPasted">Offset and inset positioning</h3>

App bar orbiter with offset positioning.

<p>Include a 20dp margin. This visually separates the app bar orbiter from the spatial panel, and prevents content obstruction.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmagu63wr-01-do.png?alt=media

App bar orbiter with inset positioning.

<p>Don’t overlap the app bar orbiter and spatial panel</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmagu6wj2-01-dont.jpg?alt=media

<h3 id="isPasted">Horizontal alignment</h3>

An app bar orbiter placed within the bounds of its spatial panel.

<p>Always align the app bar orbiter within the bounds of nearby spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmagu80gp-02-do.png?alt=media

An app bar orbiter that extends beyond the width of its spatial panel.

<p>The app bar orbiter shouldn’t exceed the width of adjacent spatial panels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmagu91ed-02-dont.png?alt=media

<h3 id="isPasted">Spatial panel alignment</h3><p>By default, app bar orbiters are center-aligned to the spatial panel. Their width and placement can be adjusted to accommodate specific user needs, such as improved ergonomics or right-to-left (RTL) languages.</p>

App bar orbiter alignment options in relation to spatial panels: left, center, and right-aligned.

<p>App bar orbiters can align to the center, left, or right of the spatial panel</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmaguagfz-XR_Top-App-Bar_Spatial-pane-alignment_01_IA_v03.mp4?alt=media

<h3 id="isPasted">Width boundaries</h3><p>An app bar orbiter’s width should adjust to stay in a person’s <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place" target="_blank" rel="noopener noreferrer">field of view</a>. </p><p>This makes crucial navigation elements easy to find.</p>

An app bar orbiter with a width that fits in a person’s field of view.

<p>Adjust the width of the app bar orbiter to fit in a person’s field of view</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmaguc0nf-01-do.png?alt=media

<p id="isPasted">It’s not recommended to increase the width of an app bar orbiter beyond a person’s natural <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place" target="_blank" rel="noopener noreferrer">field of view</a>. </p><p>This creates a visual imbalance and makes it difficult to find navigation elements.</p>

An app bar orbiter that exceeds the panel’s width and a person’s field of view.

<p>Avoid expanding the app bar orbiter beyond the adjacent panel’s width and a person’s field of view</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmagv5qxq-02-dont.png?alt=media

<h3 id="isPasted">Adaptable width</h3><p>When placed in a local context, an app bar orbiter can expand to the width of its adjacent spatial panel.   </p><p>Be sure the orbiter stays in a person’s field of view, and test for usability.</p>

2 app bar orbiters with the same width as their adjacent spatial panels.

<p>Use caution before expanding the app bar’s width to match its spatial panel. The orbiter may not fit in a person’s primary field of view.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmagv6fky-XR_Top-App-Bar_Adaptable-width_01_IA_v03.mp4?alt=media

<h2 id="isPasted">Accessibility considerations</h2>

<p><a href="https://developer.android.com/design/ui/xr/guides/get-started#make-app" target="_blank">XR accessibility</a> guidelines are still evolving. XR app bars should follow applicable Material <a href="/m3/pages/app-bars/accessibility" target="_self">app bar accessibility standards</a>.</p>

## Accessibility

<h2 id="isPasted">Use cases</h2><p id="isPasted">People should be able to do the following using assistive technology:</p><ul><li>Understand what page they’re currently visiting</li><li>Take actions or navigate to a new page destination</li><li>Maintain access to app bar actions when the content is scrolled</li></ul>

<h2 id="isPasted">Interaction &amp; style</h2>

<h3><span style="white-space:pre-wrap">Touch</span></h3><p>When tapping on an icon button, a touch ripple appears, indicating interaction feedback.</p>

An animation of the user tapping on an action item and the ripple effect being shown.

Touch: Tap

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlosdik1-GM3%20-%20App-bar%20-%20Accessibility%2001%20-%20IA%20-%20v01.mp4?alt=media

<h3>Cursor</h3><p>When hovered, the hover state provides a visual cue to the user that the element is interactive.</p><p>When clicked (in both active and inactive states), a ripple appears to indicate feedback.</p>

A mouse hovering over a button in the app bar, then clicking.

Cursor: Hover, Click

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlosc4c9-GM3%20-%20App-bar%20-%20Accessibility%20-%2002%20-%20IA%20-%20v01.mp4?alt=media

<h3 id="isPasted">Keyboard or switch</h3><p>When navigating to an interactive element, a focus indicator appears to show that action can be taken.</p><p>When the element is selected, an action is then performed.</p><p><br /></p>

An example of how to navigate the app bar using a keyboard.

<p>Interactive elements should have focus rings</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlosad0z-GM3%20-%20App-bar%20-%20Accessibility%20-%2003%20-%20IA%20-%20v01.mp4?alt=media

<h3>Initial focus</h3><p>Focus should initially land on the leading button, since it’s the first interactive element of the app bar.</p>

The tab button is used to navigate from the first button to the second button in the app bar.

<p>Use <strong>Tabs</strong> to navigate through interactive items</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlos7r6g-04.png?alt=media

The space or enter button activates the second action.

<p>Use <strong>Space</strong> or <strong>Enter</strong> to activate actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlos8gq8-05.png?alt=media

<h2>Color</h2>

<p id="isPasted">On search app bars, use the default color roles when possible.</p><ul><li>Search container: <strong>surface container</strong></li><li>Search label: <strong>on surface variant</strong></li></ul><p>On darker backgrounds, search bar containers can use the <strong>surface bright</strong> role to maintain strong visual contrast. </p><p>If mapping to other color roles, make sure the text and container have 3:1 contrast to ensure readability.</p>

A search app bar with default dark text on a light container background.

<p>Make sure search bars and their labels have at least 3:1 contrast. Use the default colors when possible.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlos5etv-06-do.png?alt=media

A search app bar with custom light text on a light container background.

<p>Avoid using custom color roles for the search bar container and search label text. If custom roles are necessary, make sure they have contrast of at least 3:1.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlos65h6-07-dont.png?alt=media

<h2 id="isPasted">Keyboard navigation</h2><div class="table-wrapper"><table style="width:100%" class="fr-table-selection-hover"><tbody><tr><th>Keys</th><td>Actions</td></tr><tr><th>Tab</th><td>Move focus to the next interactive element</td></tr><tr><th>Space or Enter</th><td>Activate the focused element</td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<p id="isPasted">The accessibility label for a title should be the same as the content within the title. If needed, add additional context to the accessibility label to ensure users understand what page they’re on or what content is being shown.</p><p>Screen readers will read the UI text followed by the component’s role.</p>

The headline has accessibility role “Title”.

<p>An app bar’s accessibility label can incorporate its UI text as well as additional context</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlos1na5-08.png?alt=media

<p>Label icon buttons according to their <a href="/m3/pages/icon-buttons/accessibility" target="_self">accessibility guidelines</a>.</p>

The app bar icon button has the accessibility role “Button”.

<p>An icon button should be clearly labeled on the action it takes, like <strong>View on map</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlos0avb-09.png?alt=media
