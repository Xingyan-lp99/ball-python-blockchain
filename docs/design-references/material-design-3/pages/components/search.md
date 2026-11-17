# Search

Source: https://m3.material.io/components/search
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/22081e54-b56a-47b2-b137-9ba82953f05e.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Use search for navigating a product with queries</p></li><li><p>A search bar can include a leading search icon, hinted search text, and optional trailing icons</p></li><li><p>Search can display suggested keywords or phrases as a person types</p></li><li><p>A search bar displays search suggestions or results in a <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element></p></li><li><p>Use a search <app-froala-tooltip-element description="App bars contain page navigation and information at the top of a screen." link-label="More on app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">app bar</app-froala-tooltip-element> to provide an emphasized, global entry-point</p></li></ul>

Mobile UI shows a person typing into an email search bar. It expands to show a list of results.

<p>When inputting text, search suggestions or results appear below the search bar</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlb0x4f4-GM3%20-%20Search%20Bar%20-%20Overview%2001%20-v2.mp4?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/30edd26d5082040a

libraryModuleType: STATUS_TABLE

<h2>M3 Expressive update</h2>

<p>Search has a new visual style, motion, and more flexibility for trailing icons. <a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank">More on M3 Expressive</a></p>

<p><strong>February 2025</strong> </p><p>Naming</p><ul><li><p>Search bar and search view are now collectively named <strong>search</strong></p></li></ul><p>Configurations</p><ul><li><p>Styles: Search can be contained (recommended) or divided</p></li><li><p>Gaps can separate results into groups</p></li></ul><p>Motion</p><ul><li><p>The search bar grows wider when focused</p></li></ul><p>Supported platforms:</p><ul><li><p><a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SearchBar(androidx.compose.material3.SearchBarState,kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SearchBarColors,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp)" target="_blank">Jetpack Compose</a></p></li></ul>

A recipe search with “Search recipes” hinted text, “Mexican dishes” is entered, then results appear in a list.

<p>The <strong>contained</strong> search style features a persistent, filled search container</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlb19j2i-GM3%20-%20Search%20Bar%20-%20Overview%2002%20-v2.mp4?alt=media

<h2>Differences from M2 to M3 baseline</h2>

<ul><li><p>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></p></li><li><p>Elevation: Lower elevation and no shadow by default</p></li><li><p>Name: Search was formerly known as open search bar</p></li><li><p>Variants: Two official variants of search components: search bar and search view</p></li></ul>

M2 open search bar.

<p>M2 open search bars were square and elevated</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlb1gn7s-04.png?alt=media

M3 search bar.

<p>M3 search bars are rounded, use tonal surface, and support dynamic color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlb1hcrs-05.png?alt=media

## Specs

<h2>Variants</h2>

Typing “Ping” into a search bar reveals a list of email results.

<p>When a person executes a <strong>search</strong>, results appear in a list below the search bar</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm28azl5-GM3%20-%20Search%20Bar%20-%20Specs%2001%20-%203P%20-%20v02.mp4?alt=media

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:29.8517%"><p>Variant</p></th><th style="width:30.1227%"><p style="text-align:center">M3</p></th><th style="width:39.955%;text-align:center"><p>M3 Expressive</p></th></tr></thead><tbody><tr><td><p>Search</p></td><td><p style="text-align:center">Available</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Configurations</h2>

<h3>Style</h3>

<p>Search comes in two styles:</p><ul><li><p>Contained: Has an <app-froala-tooltip-element description="M3 Expressive is a major update to Material 3, adding visually stunning features, components, and variants, plus updates to the shape, motion, and typography systems." link-label="More on M3 expressive" link-url="https://m3.material.io/blog/building-with-m3-expressive" should-open-link-in-new-tab="true">expressive</app-froala-tooltip-element> look and feel. It uses a filled container to separate a search bar from a <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/google-material-3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> of suggestions or results</p></li><li><p>Divided (<app-froala-tooltip-element description="Baseline variants and styles are the original M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles. " link-label link-url should-open-link-in-new-tab="false">baseline</app-froala-tooltip-element>): Doesn’t have the latest visual style, motion, or flexibility</p></li></ul>

An email inbox search bar in a contained style.

<p>The contained style has a persistent, filled container, expressive motion, and rounded shape</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17d95o-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/mZviJwGIZh_IpUNqJc4qSUDOLFrmDTpbjX_bufkF90qso_IE6fyfgB1e2VmG5N_E6Picjiw05l7vRqKShb46NyHV0Od2WHuqcVP4my2v5YBZ=s1004

An email inbox search bar in a divided style.

<p>The divided (baseline) style uses a divider to separate the search bar from suggestions and results</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17dfzg-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/sA1JTXVXpg8LWSsXFxuxTShN08cJnxWigVkMDRzrHVQT6XnlvmPuvbVrmmeMZ7ZgDpNyRgv6T-zOjMh798bEXeoj0QjURzBE5oSimBCuYgSq4w=s1004

<h3>Layout</h3>

<p>Search suggestions and results appear in customizable lists, with two layout options: full-screen and docked. <a href="/m3/pages/search/guidelines#4f6c921c-795f-4e06-9b12-27ae7d502adb" target="_blank">More on search layouts</a></p>

Full-screen search results with a search bar in the contained style.

<p>Full-screen layout in the contained style</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17dsh8-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/UN8OMCnrmxaASc6CRHtAONOcdeZf71JD03xLHV9sDt8-A6pMWEWH2DxRbjhxM7M8_IE2H7_w8mtdqqE56eamgN0CzGxQ-qpBH7UXsaOKE0c9-g=s1004

Docked search results with a search bar in the contained style.

<p>Docked layout in the contained style</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17e01j-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/SlF8qBuCFFB-x7eQOBSJ6O2BgEmepkVWMQvU1b0gtBUdISdyG2QJbz0MeS6HPrO49nL_AZQaOil5-Rw8_SpIGMGHqioZRMJVOnwocdxXQQiamg=s1004

Full-screen search results with a search bar in the divided style.

<p>Full-screen layout in the divided style</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17e8r8-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/xcvU3lGYJQELKKllc3w1uW68diJE9YJPeiCtbZM8tC9Gzg0qg5TBBzjEiFkl8hYOWcik2XUQfgqpeXvX6hXmHX_oA5_PSHLKNeRZJT3i2NU=s1004

Docked search results with a search bar in the divided style.

<p>Docked layout in the divided style</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17efaq-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/4FjOzW97D9JP3Mvu2GyfQ-PQhbAvpQRPjPjsqj3iM_125CTJgfv8X_u-qeSu4ti3i7ytSIZf4Crkoz5drPm10WS22uGld5GwXbFUhPKPLb1n=s1004

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Category</p></th><th><p>Configuration</p></th><th><p>M3</p></th><th><p>M3 Expressive</p></th></tr></thead><tbody><tr><td><p>Style</p></td><td><p>Contained</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td></td><td><p>Divided</p></td><td><p>Available</p></td><td><p>Not recommended. Use contained.</p></td></tr><tr><td><p>Layout</p></td><td><p>Docked, full-screen</p></td><td><p>Available</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Tokens &amp; specs</h2><p>Use the table's menu to select a token set. The <strong>search bar</strong> set only contains tokens for the unfocused search bar. The <strong>search view</strong> set contains all other tokens when interacting with search, including all styles and layouts. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/07341534518f78d0

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', 'Compose', '3P', 'Web', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Anatomy</h2>

<p>Search includes a search bar and a container for suggestions and results. The container is empty by default. Use the <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> component to add content. In the divided (baseline) style, a divider separates the search bar and results.</p>

6 elements of search.

<ol class="decimal"><li><p>Search bar container</p></li><li><p>Leading icon</p></li><li><p>Supporting text</p></li><li><p>Trailing icon and avatar (optional)</p></li><li><p>Input text</p></li><li><p>Container for search suggestions or results</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17eoxh-08-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/nfgJlo7RsO4mElkJBSEo5E2yo1OPaLlu6o9PxA4lLhre5XuuiXAOj1LsjVPDk01MysoC5dasvtMXqSDJHFc1w6tycmubcpzPTA9uqm9hi-_z=s2048

<h3>Examples</h3><ol class="decimal"><li><p>With avatar</p></li><li><p>With one trailing <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon button</app-froala-tooltip-element></p></li><li><p>With two trailing icon buttons</p></li><li><p>With trailing icon button and avatar</p></li></ol>

4 search bars with different trailing elements.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17exdj-10-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/4DOSj_PCy0dVTh_Mwwa-JmNfmmABObXarzG6mlKcjL7V1kdeh9_yrI9kQM5t1UhpsVOtc4bIq7mUwNYh2F50RDyInwgspspdrk-OHnd3lg=s1352

<h2>Color</h2>

<p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value.</p>

<h3>Full-screen layout</h3>

6 full-screen search color roles in light and dark themes.

<p>Full-screen search color roles used in light and dark themes:</p><ol class="decimal"><li><p>Surface container low</p></li><li><p>On surface variant</p></li><li><p>On surface variant</p></li><li><p>Surface container high</p></li><li><p>On surface variant</p></li><li><p>On surface</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17f6n2-12-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/GAGCWflTpnmoM0DwwKy1v0DdcEY5uW2zCwZpY8CaR61iuDKk3E7JY7yVPwx3ukkfq4B7qyOQOLInW7c7dRgKHXbbovgH_1bU5kc7pTZHwihLkg=s2048

<h3>Docked layout</h3>

6 docked search color roles in light and dark themes.

<p>Docked search color roles used in light and dark themes:</p><ol class="decimal"><li><p>Surface container high </p></li><li><p>On surface variant</p></li><li><p>On surface variant</p></li><li><p>Surface container high</p></li><li><p>On surface variant</p></li><li><p>On surface</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17g3kb-13.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/nq53ckQlKsYuKPXvcEYzyrhQ7Fevp-zkK7TzePU0X7GjTIveyJLPIHzZrZ3ejyWOGKASNBS7Ir8_si6O61ubAWXRj8r_zYZNHNNpFK5JLTpGWQ=s2048

<h2>States</h2>

<p>States are visual representations used to communicate the status of a component or an interactive element. In <a href="/m3/pages/search/guidelines#a9b2df31-8561-4326-82cd-41ed6532b765" target="_blank">focused search</a>, individual elements maintain their own interaction states. <a href="/m3/pages/interaction-states/overview" target="_blank">Learn more about interaction states</a></p>

<h3>Search bar</h3>

4 search bar states in light and dark mode.

<ol class="decimal"><li><p>Enabled</p></li><li><p>Hovered</p></li><li><p>Focused</p></li><li><p>Pressed (ripple)</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17mvvh-14-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/YhREfAtX7rK4eHN7NEAdJA3S1VPgesRkPzepAVAMJWT7aA0MSV9dxw8A248GG0PwSTS8FjyLqzorX8U4wiSSaFgvjC3mwqVRAW48XjyvexXNnA=s2050

<h3>Search suggestions &amp; results</h3>

<p>Search includes a container for suggestions and results. The container is empty by default. Use the list component to add content. </p>

4 search result states in light and dark mode.

<ol class="decimal"><li><p>Enabled</p></li><li><p>Hovered</p></li><li><p>Focused</p></li><li><p>Pressed (ripple)</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17n640-15-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/r1ddmkgjt_KkZZC-S8XGOaYfxyTvkqH_xLNf6MgWq89lOToWeBm5mEo8Kz2QhMxh3H_FOF_EjatnziEymAHu_ieaLrNcWfVEHkaM3AtgfOvZGQ=s2050

<h2>Measurements</h2>

<h3>Search bar</h3>

Search bar with leading and trailing icon size and padding measurements.

<p>Unfocused search bar with leading and trailing icon measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17ne69-16.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/mGptx_4JUwLVcbHz93O72eFnZN6uaFTxfpTyUe7VfjOxvJQn0kew6pVVDeiAeV4S5rWjZ0xQR-RsZMNC_1ZPJIYVvSeqIh18hIMxI9NpJQ4=s1004

Search bar with trailing avatar size and padding measurements.

<p>Unfocused search bar with avatar measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17njuh-17.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/dURHAt9JC2YGWnXNGRK34cv-wK4xrn9GhPUNnWdQ3ZcgzjMRuwGi5KNwpFaWn19j7Nls-mp9PTDF79hTW8gbm_201W-ZYWlQ1nrpTHCtT6kG=s1004

<p>In M3 Expressive, the search bar expands when focused. The margins change from 24dp to 12dp.</p>

Unfocused search bar margins of 24dp.

<p>Unfocused search bar margin measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17o030-18.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/OfNDMCVyfuBJXmI9HLNp26jlV-aQMKAawCfhfzbzlt-wYn0lR4BxkbXOVbiEP6I2tgz0HFbjC2SY5qvbZ3flpPLc4Ad6I8VdNoZbdvc2rZQ=s1004

Focused search bar margins of 12dp.

<p>Focused search bar margin measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17o810-19.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/R4k1-IGNQH3zamzgc2laHGU70E3SDajTXtksf4eWJIQO7gmrwoj9PCGHzqhrOju-IKtpdeoOCRi7WqJ5_xLvnUgtneP1ve8Wdj-lFQ5O74An=s1004

<div class="table-wrapper"><table class="borderGGrey400"><thead><tr><th style="text-align:center"><p>Element</p></th><th style="text-align:center"><p>Attribute</p></th><th style="text-align:center"><p>Value</p></th></tr></thead><tbody><tr><th rowspan="7" style="width:14.4499%"><p>Container</p></th><td><p>Width</p></td><td><p>Min: 360dp, max: 720dp</p></td></tr><tr><td><p>Height</p></td><td><p>56dp</p></td></tr><tr><td><p>Label alignment</p></td><td><p>Start-aligned</p></td></tr><tr><td><p>Leading padding</p></td><td><p>Unfocused: 24dp, focused: 12dp</p></td></tr><tr><td><p>Trailing padding</p></td><td><p>Unfocused: 24dp, focused: 12dp</p></td></tr><tr><td><p>Leading icon and label padding (from tap target)</p></td><td><p>4dp</p></td></tr><tr><td><p>Label and trailing icon padding (from tap target)</p></td><td><p>4dp</p></td></tr><tr><th><p>Avatar</p></th><td><p>Size</p></td><td><p>30dp</p></td></tr></tbody></table></div>

<h3>Focused search</h3>

<h4>Contained style</h4>

Full-screen layout size and padding measurements in contained style.

<p>Full-screen search padding and size measurements for contained style</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17on8b-20.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/b0xykJB3s1NEcZz6gQP37YfP-r6S3fbfqNKJaY-XbWy2AyoWViOPlmHhW6Lq6b4IbhmcDYAQJHonH59HvnDeIUdeXeMjIUdoWKNxbjQpN6xk=s1004

Docked layout size and padding measurements in contained style.

<p>Docked search padding and size measurements for contained style</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17oub1-21.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/5Hst6KPsjyxhxQTptCBbkRahderHldeKa_33ucNVW9xZ9svHkx9eBhbhDKYR656D5DkvhdfdMIPhs5L9gWqq2yfEjn_AQvTQQg5Q2Y5WHhJ1=s1004

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p>Element</p></th><th><p>Attribute</p></th><th><p>Value</p></th></tr></thead><tbody><tr><th rowspan="2"><p>Full-screen container</p></th><td><p>Width</p></td><td><p>Full width</p></td></tr><tr><td><p>Height</p></td><td><p>Full height</p></td></tr><tr><th rowspan="2"><p>Docked container</p></th><td><p>Width</p></td><td><p>Min: 360dp, max: 720dp</p></td></tr><tr><td><p>Height</p></td><td><p>Min: 240dp, max: 2/3 of screen height</p></td></tr><tr><th rowspan="6"><p>Search bar container</p></th><td><p>Height</p></td><td><p>56dp</p></td></tr><tr><td><p>Label alignment</p></td><td><p>Start-aligned</p></td></tr><tr><td><p>Leading padding</p></td><td><p>16dp</p></td></tr><tr><td><p>Trailing padding</p></td><td><p>16dp</p></td></tr><tr><td><p>Leading icon and label padding (from tap target)</p></td><td><p>4dp</p></td></tr><tr><td><p>Leading icon and label padding (from tap target)</p></td><td><p>4dp</p></td></tr></tbody></table></div>

<h4>Divided style</h4>

Full-screen layout size and padding measurements in divided style.

<p>Full-screen search padding and size measurements for divided style</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17p24v-22-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/RhpQaBUaokljf6Qv0Pb6sUHofotzoGbLGs7O74snG2B9yjauRk1iv6JFhmSRsHNdUu3nacOIuEmi0RoGtRGrjv8cs9IT5uFzr30IZDU7kge9vw=s1004

Docked layout size and padding measurements in divided style.

<p>Docked search padding and size measurements for divided style</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmm17p7ru-23-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/52yDW7vsdT_ythER_zFPD7eAyH2K5BvU_V9fB4COC5khSNA81CffErRCuS1kxNZkIfPYCWceEYxrnu07HijSkwnq5sIb-oMGHk_PUOu88t4=s1004

## Guidelines

A mobile UI search with hinted text “Search recipes”, “Mexican dishes” is entered, and a list of recipe results appear.

<p>When focused, a search bar can show a list of search suggestions. As text is entered, search results appear.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfkefwf-GM3%20-%20Search%20Bar%20-%20Guidelines%2001%20-%20v02.mp4?alt=media

<h2>Usage</h2>

<p>Search helps people find information quickly.<br /><br />Use search for products with many items to manage, such as files or messages.</p><p></p>

Mobile UI shows a search bar at the top of a message inbox.

<p>Search helps people find information in large inboxes like messages or emails</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfkhcoi-02.png?alt=media

<h3>Different ways to search</h3>

<p>The search entry point is dependent on a product’s needs, and should be easy to find:</p><ul><li><p><app-froala-tooltip-element description="The search bar is a persistent and prominent search field at the top of the screen." link-label link-url should-open-link-in-new-tab="false">Search bar</app-froala-tooltip-element>: Use to search contents in a specific view, like <strong>Search your messages</strong></p></li><li><p><app-froala-tooltip-element description="Search app bars provide an emphasized entry-point to open search." link-label="More on search app bars" link-url="/m3/pages/app-bars/guidelines#ed1f4c54-fc2d-4544-b1ed-ac667181dabe" should-open-link-in-new-tab="true">Search app bar</app-froala-tooltip-element>: Use this <app-froala-tooltip-element description="App bars contain page navigation and information at the top of a screen." link-label="More on app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">app bar</app-froala-tooltip-element> variant when search is the primary, global function</p></li><li><p>Search <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon button</app-froala-tooltip-element>: Use when search is a secondary action or not the main focus</p></li></ul>

A mobile app with a search bar below the page title.

<p>Add a <strong>search bar</strong> below a title to search specific content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfkodgz-03.png?alt=media

A mobile app with a search app bar.

<p>For global search, use a persistent <strong>search app bar</strong>, integrated into an app bar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfkpcee-04.png?alt=media

A mobile app with a magnifying glass icon on the leading side of the app bar.

<p>Use a <strong>search</strong> <strong>icon button</strong> when search is a secondary action</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfkq5y2-05.png?alt=media

<h3>Focused search</h3><p>When a search entry point is selected, it opens <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element> search.  </p><ul><li><p>Search suggestions can appear before text is entered</p></li><li><p>Search results can show as someone is typing or after a search is executed</p></li><li><p>Individual elements maintain their own interaction <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">states</app-froala-tooltip-element> when search is focused</p></li></ul><p><a href="/m3/pages/search/specs#65c58b10-4569-43d6-9c11-64a5b02f3099" target="_blank">More on search states</a></p>

Focused search with a list of suggestions on a mobile screen.

<p>When focused, a search bar expands to show search suggestions or results in a list</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfkz1fo-06.png?alt=media

<p>If search is the primary action, focused search can be a standalone destination reached from a <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element>.</p>

Focused search on a mobile screen with a list of suggested contacts.

<p>Focused search can be a standalone destination, reached by selecting an item in a navigation bar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfkth1m-07.png?alt=media

<h3>Search suggestions &amp; results</h3><p>Search suggestions and results both appear in a <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> component by default.<br /><br />To help people find information quickly, consider adding variety and context, such as:</p><ul><li><p>Leading icons related to suggestions</p></li><li><p>Category labels, like <strong>Recent</strong>, <strong>Contacts</strong>, or <strong>Suggestions</strong></p></li><li><p>Avatars or other high-priority items</p></li><li><p>Filter chips to narrow down results</p></li></ul>

Search with suggestions organized in a column, ending with a row of 5 contact avatars with names.

<p>Include high-priority items like avatars in search suggestions or results</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlflqra9-09.png?alt=media

<h3>Gaps</h3><p>Use gaps to separate a list of suggestions or results into groups.<br /><br /><a href="/m3/pages/lists/guidelines#9e96fd72-5bf3-49df-9baf-e025dcca344d" target="_blank">More on using gaps in lists</a></p>

A gap separates the location and calendar list items from people and pets avatars.

<p>To separate list items into distinct groups, use a gap</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfm1yld-10.png?alt=media

<h2>Placement</h2>

<p>A search bar is typically placed at the top of a screen to remain prominent and accessible. Its location depends on whether search is the primary focus of a product or a secondary action.</p>

Mobile UI with a search bar directly below a Settings headline.

<p>A search bar can be the primary focus of a page</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfmbc2s-21.png?alt=media

Mobile UI with a search bar centered at the top of the screen, above a row of Favorites avatars.

<p>Search bars should usually be placed at the top of the content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfmc255-22.png?alt=media

A photos app with a search icon.

<p>Search can be a secondary action</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfmcmiv-23.png?alt=media

<h3>Focused search layouts</h3><p>When focused, search suggestions and results appear in a list below the search bar.  <br /><br />There are two layout options:</p><ul><li><p><strong>Docked</strong> opens a list below the search bar, with a scrim covering main content</p></li><li><p><strong>Full-screen</strong> expands to fill the screen</p></li></ul><p><a href="/m3/pages/search/guidelines#eb45ccc4-d1b5-4ea1-bee5-ea1c3d1c5436" target="_self">More on adaptive design</a></p>

Tablet UI shows a list of search results docked below the search bar.

<p>Docked layout on a tablet</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfmf49n-08.png?alt=media

Mobile UI shows a list of search results filling the screen.

<p>Full-screen layout on mobile</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfmg7bg-07.png?alt=media

<h2 id="isPasted">Anatomy</h2>

6 elements of search.

<ol class="decimal"><li><p>Search bar container</p></li><li><p>Leading icon</p></li><li><p>Supporting text</p></li><li><p>Avatar or trailing icon (optional)</p></li><li><p>Input text</p></li><li><p>Container for search suggestions or results</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlgr3p93-11.png?alt=media

<h3>Search bar container</h3><p>In the contained style, the search bar container remains the same shape in both the unfocused and focused states. Avoid changing the container behavior. <br /><br />The container’s margins should be:</p><ul><li><p>Unfocused: 24dp</p></li><li><p>Focused: 12dp</p></li></ul><p>In the divided (baseline) style, a divider separates the search bar and results.</p>

Side-by-side comparison of a search container in unfocused and focused states.

<p>Search bar containers have persistent, rounded corners</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfmu14l-13.png?alt=media

<h4>Container color</h4><p>Search bars use the <strong>surface container high</strong> <app-froala-tooltip-element description="Material has 26 standard color roles organized into six groups: primary, secondary, tertiary, error, surface, and outline." link-label="More on color roles" link-url="/m3/pages/color-roles?s=m3" should-open-link-in-new-tab="true">color role</app-froala-tooltip-element>. This role applies when the screen background is white or a tonal <strong>surface</strong> color, ensuring the container has clear contrast.</p>

2 mobile UIs show search bars on white and tonal backgrounds.

<p>Search bars use <strong>surface container high</strong> to provide clear contrast</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfmvyj4-14.png?alt=media

<p>Avoid using a <strong>surface container high</strong> color on a <strong>surface container</strong> background. This can cause the search bar to blend in, making it difficult for people to find.<br /><br />To ensure proper contrast, use surface container roles that are more than one step apart. </p>

A “surface container high” search bar on a “surface container” background.

<p>Using a <strong>surface container high</strong> color on a <strong>surface container</strong> background reduces contrast and may affect accessibility</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfn371r-15.png?alt=media

<h3>Icons &amp; icon buttons</h3><h4>Leading icons</h4><p>The leading side of a search bar should include either: </p><ul><li><p>A navigational icon button, such as a menu or arrow</p></li><li><p>A non-functional search icon</p></li></ul>

A search bar on a tablet screen contains a non-functional search icon and a trailing avatar.

<p>A search bar can contain a non-functional search icon</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfn8hr6-16.png?alt=media

<h4>Trailing icons</h4><p>A search bar should have one or two trailing icons or icon buttons.<br /><br />Trailing actions can include:</p><ul><li><p>Additional modes of searching like voice search</p></li><li><p>A separate high-level action such as current location or profile</p></li><li><p>An overflow menu</p></li><li><p>A decorative search icon</p></li></ul>

A search bar with 2 trailing icon buttons: a microphone and an overflow menu.

<p><span style="white-space:pre-wrap">Use a maximum of two trailing icons</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfnb1td-17.png?alt=media

A search bar with a trailing microphone icon and avatar.

<p>Combine an avatar with up to one other trailing icon button</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfncrm8-18.png?alt=media

Focused search with a trailing x icon to clear input text.

<p>Focused search can show an optional <strong>clear</strong> icon to remove input text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfndiyw-19-VQA.png?alt=media

<h3>Text</h3><h4>Hinted search text</h4><p>Provide a short description of the information people can search, like <strong>Search replies</strong> or <strong>Search your messages</strong>.</p><h4>Input text</h4><p>When a person starts typing, the hinted text is replaced with the input text.  </p>

A search bar labeled “Search replies”. “Peanut is entered and “Quick results” appear.

<p>Hinted search text is replaced when a search query is entered</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfngra0-GM3%20-%20Search%20Bar%20-%20Guidelines%2020%20-%20v02.mp4?alt=media

<h2>Adaptive design</h2>

<p>The search bar position and alignment should scale with the layout, and stay close to the searchable content.<br /><br />In most cases, a search bar should:</p><ul><li><p>Stay in its pane and scale in width accordingly</p></li><li><p>Internal elements anchor to the left and right as the parent container scales</p></li></ul><p><a href="/m3/pages/layout-overview/" target="_blank">More on applying layout</a><br /></p>

A search bar keeps its layout region and scales with different window sizes and layouts.

<p>Keep the search bar close to the content a person can search</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfnplfk-GM3%20-%20Search%20Bar%20-%20Guidelines%2024%20-%20v01.mp4?alt=media

<h3>Focused search</h3><p>When focused, search can switch between showing suggestions or results in a:</p><ul type="disc" style="list-style-type:disc"><li><p><strong>Docked layout</strong>: Best for <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded</app-froala-tooltip-element> windows</p></li><li><p><strong>Full-screen layout</strong>: Default for <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoints</app-froala-tooltip-element></p></li></ul><p><a href="/m3/pages/search/specs#fc12e839-f356-4f48-9bd5-0ed210565bfe" target="_blank">More on search layouts</a> </p>

Search suggestions in docked and full screen layouts.

<ol class="decimal"><li><p>A docked layout on a large screen</p></li><li><p>A full-screen layout, the default for compact screens</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfnv4wh-25.png?alt=media

<p>Search suggestions or results should swap from full-screen in compact windows to docked in larger <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element>.  </p>

Animation shows search suggestions adapting from full-screen on mobile to a docked layout as the window size increases.

<p>Search suggestions and results should adapt to fit different window sizes</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlfo0cyf-GM3%20-%20Search%20Bar%20-%20Guidelines%2026%20-%20v02.mp4?alt=media

<h2>Behavior</h2>

<h3>Focused search</h3>

<p>When a search bar is selected, search becomes focused and can:</p><ul><li><p>Show historical suggestions before typing</p></li><li><p>Show suggestions or results as someone is typing</p></li><li><p>Wait to show suggestions or results until a search is queried </p></li></ul><p>The <strong>back</strong> icon releases focus, dismisses any suggestions or results, and returns the search bar to its original state.</p>

When a search bar is tapped, it becomes focused, and suggestions appear in a list. 

<p>When focused, a list of search suggestions can appear</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlgr7r58-GM3%20-%20Search%20Bar%20-%20Guidelines%2027%20-%20v02.mp4?alt=media

A person searches a photo app. The back icon returns the search bar to its original state.

<p>Focus is released when the back icon is selected</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlgr95m2-GM3%20-%20Search%20Bar%20-%20Guidelines%2030%20-%20v01.mp4?alt=media

<h3>Scroll</h3><p>Depending on needs, a search bar can: </p><ul><li><p>Scroll away with content, then reappear when a person begins scrolling up </p></li><li><p>Remain fixed at the top of the screen</p></li></ul>

Scrolling up hides the search bar. It reappears when scrolling down.

<p>A search bar can scroll up with content, then reappear when a person scrolls down</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlgrahif-GM3%20-%20Search%20Bar%20-%20Guidelines%2029%20-%20v01.mp4?alt=media

<h3>Search results</h3><p>To execute a search, a person can:</p><ul><li><p>Type a query and press <strong>Enter</strong></p></li><li><p>Select a suggestion or result without querying a search</p></li></ul><p>Search results appear in a <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> below the bar, and scroll beneath the bar.   <br /><br />For accessibility, focused search needs a clear status indicator that it’s searching content, like a search icon or <strong>Results</strong> label. <a href="/m3/pages/search/accessibility/" target="_blank">More on search accessibility</a></p>

“Peanut” is the entered search query and the first suggestion in the list.

<p>Show search results in a compact, organized list, with an indicator like <strong>Quick results</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlgrceqs-32.png?alt=media

<p>When search results are queried, the input text should remain visible, but not in focus.</p>

“Pla” is entered into the search bar, “Plants” is suggested and selected.

<p>Search suggestions and results display in a list, and the input text remains visible</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlgrdhl9-GM3%20-%20Search%20Bar%20-%20Guidelines%2033%20-%20v02.mp4?alt=media

<h3>Predictive back</h3><p>On Android, <a href="https://github.com/material-components/material-components-android/blob/master/docs/foundations/PredictiveBack.md" target="_blank">predictive back</a> allows a person to swipe left or right on search. </p><ul><li><p>Search detaches from the screen edge to signal the full-screen layout will minimize</p></li><li><p>The previous screen is revealed in a preview</p></li></ul><p><a href="https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture" target="_blank">More predictive back design guidance</a></p>

Swiping left on search causes the Android screen to scale left.

<p>The search surface and content scale back in the direction of the gesture</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlgrejsr-GM3%20-%20Search%20Bar%20-%20Guidelines%2034%20-%20v02.mp4?alt=media

## Accessibility

<h2 id="isPasted">Use cases</h2>

<p>People should be able to use assistive technology to:</p><ul><li><p>Navigate to and focus on a search bar</p></li><li><p>View the hinted search text or persistent label</p></li><li><p>Input text and complete a search</p></li><li><p>Interact with a list of search suggestions and results </p></li><li><p>Clear the input text</p></li></ul>

<h2 id="isPasted">Interaction &amp; style</h2>

<h3>Autosuggest</h3><p>When search suggestions and results appear, the screen reader must announce the change. This lets people know list items are available for selection.</p>

Hinted search text and autocomplete results on a mobile screen.

<p>Autocomplete results should be announced by the screen reader</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlgrjdxa-01.png?alt=media

<h2 id="isPasted">Initial focus</h2>

<p>Initial <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f" should-open-link-in-new-tab="true">focus</app-froala-tooltip-element> lands on the first interactive element. This is often a leading <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon button</app-froala-tooltip-element> or <app-froala-tooltip-element description="Text fields let users enter text into a UI." link-label="More on text fields" link-url="/m3/pages/text-fields/overview" should-open-link-in-new-tab="true">text field</app-froala-tooltip-element>. A leading icon button usually activates search directly or opens a navigation component.</p>

Search bar with a focused leading icon. 

<p>Initial focus can land on a leading icon</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlgrkpb6-02.png?alt=media

Search bar with no leading icon. The text field is focused.

<p>If there’s no leading icon, focus lands on the text field</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlgrl9ca-03.png?alt=media

<h2 id="isPasted">Keyboard navigation</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th><p><strong>Keys</strong></p></th><th><p><strong>Actions</strong></p></th></tr></thead><tbody><tr><th><p><strong>Tab</strong> or <strong>Shift</strong> + <strong>Tab</strong></p></th><td><p>Navigate between interactive elements</p></td></tr><tr><th><p><strong>Space</strong> or <strong>Enter</strong></p></th><td><p>Activate the search text field for input</p></td></tr><tr><th><p><strong>Arrows</strong></p></th><td><p>Navigate between search result items</p></td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<p>The hinted search text should be used as the accessibility label describing the search bar.  <br /><br />The role for the input field should be:</p><ul><li><p>Android: <strong>Text field</strong></p></li><li><p>iOS: <strong>Search field</strong></p></li></ul>

Search bar with “Label: Search messages” and “Role: Text field”.

<p>The accessibility label should match the hinted search text</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlgrql4p-04.png?alt=media

<p>Leading and trailing icon buttons should be labeled according to their <a href="/m3/pages/icon-buttons/accessibility" target="_blank">accessibility guidance</a>.</p>

A search bar with accessibility labels for its leading icon button and trailing avatar.

<p>Use icon labels for icon buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlgrt6xt-05.png?alt=media

<p>Search suggestions and results use the list component. Screen readers automatically announce the results as a list.<br /><br />For accessibility labels, follow the <a href="/m3/pages/lists/accessibility" target="_blank">list accessibility guidelines</a>.</p>

A search bar on mobile, showing search results in a list.

<p>Search suggestions and results are created using lists</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmlgrwf25-06.png?alt=media
