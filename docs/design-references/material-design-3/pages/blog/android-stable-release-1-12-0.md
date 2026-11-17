# Material Design Components for Android 1.11.0 and 1.12.0

Source: https://m3.material.io/blog/android-stable-release-1-12-0
Content endpoint: https://m3.material.io/page-data/Posts/5836138581721088.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/e542d55e05d06e63bbf3dadd467d6f4889a15a6c2c43b46c812a48b6ee2adf7ff126e17cb0d3c04d4d2f24d216f00138ed4cd9cbf209538cb1bd0f4fd7ac7f15

https://lh3.googleusercontent.com/ECgal03qq-GPHfoWRZft82d97qPwwB-M4z1d-igDCWWAMWhJteOVP4HzaU2XhhQVfG9ME-_0DWTFA1eK28kgnTgTHBpSnTIhLK8TQKwE0zyq_lFckrs

James Williams

Material Developer Advocate

mio-example

```java
val snapHelper = CarouselSnapHelper()
snapHelper.attachToRecyclerView(carouselRecyclerView)
```

```java
<!-- Primary colors -->
  <color name="m3_sys_color_dynamic_dark_primary">@color/m3_ref_palette_dynamic_primary80</color>
  <color name="m3_sys_color_dynamic_dark_on_primary">@color/m3_ref_palette_dynamic_primary20</color>
  <color name="m3_sys_color_dynamic_dark_primary_container">@color/m3_ref_palette_dynamic_primary30</color>
  <color name="m3_sys_color_dynamic_dark_on_primary_container">@color/m3_ref_palette_dynamic_primary90</color>

<!-- Baseline palette – Primary -->
  <color name="m3_ref_palette_dynamic_primary100">@android:color/system_accent1_0</color>
  <color name="m3_ref_palette_dynamic_primary99">@android:color/system_accent1_10</color>
  <color name="m3_ref_palette_dynamic_primary95">@android:color/system_accent1_50</color>
  <color name="m3_ref_palette_dynamic_primary90">@android:color/system_accent1_100</color>
```

```java
<color name="m3_sys_color_dynamic_light_primary">@android:color/system_primary_light</color>
  <color name="m3_sys_color_dynamic_light_on_primary">@android:color/system_on_primary_light</color>
  <color name="m3_sys_color_dynamic_light_primary_container">@android:color/system_primary_container_light</color>
  <color name="m3_sys_color_dynamic_light_on_primary_container">@android:color/system_on_primary_container_light</color>

<color name="m3_sys_color_dynamic_dark_primary">@android:color/system_primary_dark</color>
  <color name="m3_sys_color_dynamic_dark_on_primary">@android:color/system_on_primary_dark</color>
  <color name="m3_sys_color_dynamic_dark_primary_container">@android:color/system_primary_container_dark</color>
  <color name="m3_sys_color_dynamic_dark_on_primary_container">@android:color/system_on_primary_container_dark</color>
```

<p>Material Design Components versions 1.11 and 1.12 come on the eve of our yearly developer conference Google I/O and offer a number of new options for Carousel control, an expansion to color theming, and non-text contrast updates for progress indicators and sliders. The minimum SDK version for MDC Views raises to API 19 in version 1.12, similar to the rest of AndroidX. 1.12 also updates its dependency on androidx.transition (used in SharedElement transitions, Fade, and <a href="https://developer.android.com/guide/navigation/custom-back/support-animations" target="_blank" rel="noopener">Predictive Back animations</a>) to version 1.5.0 from 1.2.0.</p>
<h2>Carousel Updates</h2>
<p>In the <a href="https://material.io/blog/android-stable-release-1-10-0" target="_blank" rel="noopener">last post</a> we announced a new Carousel strategy, HeroCarouselStrategy, that can be used to showcase large, more immersive content. In MDC 1.11, we&rsquo;ve added two new strategies - UncontainedCarouselStrategy and FullscreenCarouselStrategy. Additionally, we&rsquo;ve added the option to center-align any carousel so large, focal items can be placed in the center of the scroll container.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p></p>
<p>&lt;mio-column&gt;&lt;mio-image index=0&gt;&lt;/mio-image&gt;&lt;/mio-column&gt;</p>
<p></p>
<p>&lt;mio-column&gt;&lt;mio-image index=1&gt;&lt;/mio-image&gt;&lt;/mio-column&gt;</p>
<p></p>
<p>&lt;/mio-col-set&gt;</p>
<p><code>UncontainedCarouselStrategy</code> doesn&rsquo;t alter the aspect ratio of the carousel items. This is a useful strategy when altering an item&rsquo;s size could detract from its meaning - for example, a carousel of album covers might benefit from retaining a recognizable 1:1 aspect ratio.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p><code>FullScreenCarouselStrategy</code> allows a single item to take all the available space in a container. This is useful for fully immersive content like video or slideshows where items are interacted with, or viewed, one-at-a-time. We only recommend using this strategy in the vertical orientation.</p>
<p><strong>Item Snapping</strong></p>
<p><code>CarouselSnapHelper</code> allows your carousels to give focus to the nearest item. They can be used on all strategies but are strongly encouraged on hero carousels and full-screen carousels.</p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Color Changes</h2>
<p>API 34 has an <a href="https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md" target="_blank" rel="noopener">expanded color set</a> giving you more ways to personalize your apps. Some of the additions like the new surface options have been incorporated in components. Fixed and Dim colors on the other hand are developer options but not used by the component set at time of writing.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p><strong>System UI access to named color roles</strong></p>
<p>Before API 34, when you used dynamic color, the color was stored as individual tones of the color palettes. MDC would map those colors to <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/color/res/values-v31/tokens.xml" target="_blank" rel="noopener">dynamic color properties and then assign those properties to color roles</a>.</p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p>As of API 34, the traversal is more direct and compact. Material color roles directly map to color resources from <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/color/res/values-v34/tokens.xml" target="_blank" rel="noopener"><code>@android:color</code> namespace</a>.</p>
<p>&lt;mio-code-snippet index=2&gt;&lt;/mio-code-snippet&gt;</p>
<p><strong>Fixed and Fixed Dim</strong></p>
<p>Fixed and Fixed Dim color roles are new additions to the color spec. Fixed color roles do not change between light and dark themes. Dim color roles offer a less emphasized option to the associated color role. Neither of these categories of color roles are used in components but are available to further customize your UIs.</p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p><strong>Surfaces</strong></p>
<p>Previously in Material themes, we provided a single surface color value and calculated interpolated variants of it at runtime by blending with the primary color (based on elevation). This was frustrating for developers and designers when it came to implementing UIs because they were unable to assign those colors directly.</p>
<p>Color roles simulating different elevation levels have been added to theming. There are now three surface color options and five surface container options.</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p>Surface Bright is guaranteed to be the lightest surface color.</p>
<p>Surface is largely unchanged from previous versions.</p>
<p>Surface Dim is equivalent or darker than its relative Surface color role.</p>
<p>Surface Container Lowest, Low, High and Highest are additional color roles that can provide more or less emphasis in contrast to Surface Container.</p>
<p>These components use some of the new surface container color roles:</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p></p>
<p>&lt;mio-column&gt;</p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/buttons/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Elevated Button</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/bottom-app-bar/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Bottom App Bar</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/navigation-bar/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Navigation Bar</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/bottom-sheets/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Bottom Sheet</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/side-sheets/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Modal Side Sheet</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/cards/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Elevated Card</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/chips/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Elevated Chips</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/date-pickers/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Datepicker</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/dialogs/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Dialogs</span></a></p>
<p>&lt;/mio-column&gt;</p>
<p></p>
<p>&lt;mio-column&gt;</p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/floating-action-button/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Surface FAB</span></a><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">/ </span><a style="text-decoration: none;" href="https://m3.material.io/components/extended-fab/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Surface exFAB</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/menus/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Menu</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/navigation-drawer/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Navigation Drawer</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/search/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Search</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/switch/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Switch</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/text-fields/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Text Fields</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/time-pickers/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Timepicker</span></a></p>
<p><a style="text-decoration: none;" href="https://m3.material.io/components/top-app-bar/specs"><span style="font-size: 11pt; font-family: Roboto,sans-serif; color: #1155cc; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">Top App Bar</span></a></p>
<p>&lt;/mio-column&gt;</p>
<p></p>
<p>&lt;/mio-col-set&gt;</p>
<p><span id="docs-internal-guid-47e41fb8-7fff-e4ee-4a40-9b3121029bc4"></span></p>
<p>The new color roles are already available in <a href="https://material-foundation.github.io/material-theme-builder/" target="_blank" rel="noopener">Material Theme Builder</a>.</p>
<p><strong>Non-Text Contrast Updates (NTC) for Progress Indicators and Sliders</strong></p>
<p>Non-text contrast standards involve first evaluating which parts of controls are essential to demark their state, interactivity options, and legibility and secondly making changes to improve the identified attributes and making sure those portions have a minimum contrast ratio (3:1 in standard contrast at time of writing). Progress Indicators and Sliders have been updated to implement these standards.</p>
<p><strong>Progress indicators&nbsp;</strong></p>
<p>The NTC changes to progress indicators include a clearly identified gap between the active and inactive tracks for linear progress indicators. In circular progress indicators, the pre-1.12 version does not by default include a track making it more difficult to estimate its value. An inactive track is now drawn to complete the full circle with gaps on both ends where the track meets the active indicator.</p>
<p>A number of these options such as the size of the gap size and track attributes are addressable in XML code. You can see the full listing <a href="https://github.com/material-components/material-components-android/blob/master/docs/components/ProgressIndicator.md" target="_blank" rel="noopener">here</a>.</p>
<p>&lt;mio-col-set cols=3&gt;</p>
<p>&lt;mio-column&gt;&lt;mio-image index=6&gt;&lt;/mio-image&gt;&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;&lt;mio-image index=7&gt;&lt;/mio-image&gt;&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;&lt;mio-image index=8&gt;&lt;/mio-image&gt;&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<p>&lt;mio-image index=9&gt;&lt;/mio-image&gt;</p>
<p><strong>Sliders</strong></p>
<p>Sliders have undergone similar changes to progress indicators. There are now gaps between the active and inactive tracks.The default thumb for sliders has also changed from a connected filled circle to a vertical bar with configurable gaps on each side. The shape for formatted labels have also undergone a few tweaks to assist with NTC.</p>
<p>As is the case with progress indicators, you can configure these attributes inXML code. You can see the full listing <a href="https://github.com/material-components/material-components-android/blob/master/docs/components/Slider.md" target="_blank" rel="noopener">here</a>.</p>
<p>&lt;mio-col-set cols=3&gt;</p>
<p>&lt;mio-column&gt;&lt;mio-image index=10&gt;&lt;/mio-image&gt;&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;&lt;mio-image index=11&gt;&lt;/mio-image&gt;&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;&lt;mio-image index=12&gt;&lt;/mio-image&gt;&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<h2>What&rsquo;s next for MDC?</h2>
<p>We&rsquo;re hard at work on the 1.13.0 release. The components or features we highlight in these posts are only a fraction of the work that lands in each release. Check out the <a href="https://github.com/material-components/material-components-android/releases/tag/1.12.0" target="_blank" rel="noopener">release notes</a> for a full listing.</p>
<p>You can follow the progress of new versions, file <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=bug&amp;template=bug_report.md&amp;title=%5BComponent+name%5D+Short+description+of+issue" target="_blank" rel="noopener">bug reports</a> and submit <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=feature+request&amp;template=feature_request.md&amp;title=%5BComponent+name%5D+Short+description+of+request" target="_blank" rel="noopener">feature requests</a> on GitHub. Check out the <a href="https://github.com/material-components/material-components-android/releases/download/1.12.0/catalog-debug.apk" target="_blank" rel="noopener">catalog app</a> to see the components in action. Also feel free to reach out to us on Twitter <a href="https://twitter.com/materialdesign" target="_blank" rel="noopener">@materialdesign</a>.</p>

carousel component

Start-aligned HeroCarouselStrategy

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/b129c94f47a1e2dab612df05b619c5c8b15ef9e9c0fecb6956435596128dfb5790d144dd6119684115efbc4ef1394bd7702bdc2667c9940a1eb9240d6be0e546

https://lh3.googleusercontent.com/4dfYjomm9jLyZrmrpQj6wbwMw5Zryb1iKscfrxOsijGLEkGJdIOqw2b_xFp-s9E3iwuwl9RY2CYQQSkwSgDb3eETUysLyFtEi6YYjCc4TIaLlaCPppY

Carousel component

Center-aligned HeroCarouselStrategy

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/a5e4bdcf947e2d71ea8e219c7b2151477e0fac622cd3558fba2f71f2bb01a693d67c67e9ec47d0649e8b594cdea9f72d8dbbcbe27eadbb8e80495e336218e09e

https://lh3.googleusercontent.com/Qzm10yEjrS44EMjoNNZq-RrcrICwVAqVCSI84yFnvaDOXwexiH2n-iUVXSBKcNGu2TVn0297L2m4NySjlFO1zUm0TMzKFyrO-BsnVnlsb7PHM7wVq7s

uncontained carousel

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d870de3ec549a4736724fadb3d8fea39bbed5501c256bf17306f743b7a6c66d2d7be2a740601acbadd3036a97a12f7aa7e67a0c14c38043ea5a8bfa7550c7772

https://lh3.googleusercontent.com/VyDL_gQtCboI-XpNHYJoVuaO4xQQNl0NraF8ar2aYy6CnN7u-vHj4beznfhRK0GrqOQTpjD8qKrEhcWWz1DqddJeqNj3XDnU06NJ1q3J1GJOXrw_B6Xg

color diagram

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/53255a9910f7904d0a5c4a9f97e644152f196879229e062925ad6534cdad79a9cc561e4e444b5e30da2adb1d314e269b965c27c37d188530d027b6821561350b

https://lh3.googleusercontent.com/wYC9nZ_piBDhi6_F2NsM0jZlb5od5BIUgMwDrrqs0Nu7Xw-SgmUF-acVqSv0YbuV6Xb1iLlT6ijcLPCyIrzENcSh0Ft3pmCOYoASvu-qLnZ3dsWfgg

section of color scheme

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/36958aaf13678cb833b52b975cfa0dc678325f19a411223e7ab8d0be53d19e7a9e884f8b5462b504c886bd8d02547ac8cecbb96c2d3b44d312065d914e32dae7

https://lh3.googleusercontent.com/AE-jIS-uUK7UrS9_VI-2oofB11xaJINbpE9WfnpPFpZtMtkJHq5O_KvqEq8dtRuY7lKb1oUXQ3FV_6LCpIWpvl7CU3XHw3lmB6PtSNT-V14YWY2JLQ

surface color scheme

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/04a23dae592a6bf50650ffda4466d5f3bb3ee4f3b03fb0da42034a35f252d69678554d1c2f01b1faaa1e3e391231d0e635e9b7c500e56defaf5034b1a365794f

https://lh3.googleusercontent.com/zy97lo94vUh9MCZfE0XWNCxRSzUuWF5wZUNQ4eN6eQbwFjNLZkwwL4TV9WSonT4a2CVDdQC-svbuLd1P02NH_Zrc8497nFl4zqkALxKvKMnq2cHAJXXU

Progress indicator settings in the catalog app

MDC 1.11 version of Progress Indicators

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/9620cbe97c12c19a81dbb1d2fb905f703fd71c9d1c74dc3944369004436b2fdf9af6f60c10fe43dd5412f0bb48c0d1e371fecb22b137372bfa7d139ecb9ae008

https://lh3.googleusercontent.com/ncTB3e-Q3A8plLzHS2sH4piRbW1w7OI8vLYZ9q34NESUKdFTm34QQ4odOVtVPLl6GqL6lasgNx-Avt6lzRub9yL2uWboV1X4RYn8iqNEfwevhzTUCpw

Progress indicator settings in the catalog app

Basic Progress Indicator Options

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/7dfe43386abb7be2ec01a37beafed2f7449e516140ed3fb5fe9903270f1395c4c3e7f6d63260bac43f192d6407a1206db825eb8e7ee04b2b8a7d7a82118d8273

https://lh3.googleusercontent.com/Pq1pggutQySy_7ypKoBQBmPCHDj1-WJefUrXJXtaFp0QAGAx7VNUsjOK7litWYK7xHrOO9TINDMzoj-EDczkdA2hPDNiC8QC-sNJa9eVn1x7_5s5ulmT

Progress indicator settings in the catalog app

Advanced Progress Indicator Options

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/2f8a36d240ce944bd4687cb1a53ee069cec2a229438ccfa7f27fe6d87880ba9b73208eeed3514cb4d956af02e6277e5e1e5a7b8da3698c25894abe53b7abe913

https://lh3.googleusercontent.com/m6Pr8FsvUY5P2kRJjpDgVZFjILIAdAuTRVgfi6TcXrZ4KzBJWZy1SN14jI8TpGwtG3Xga2ub1ueG_L0hmlVY3MTZ4g6Lvuu3ze8GRgbDhlL95-tFwkQ

customized progress indicators in catalog app

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/2dae82499acde7d6c3cd4bf9fd65150956df24b9fbbc09048b9f931a31c2de1a9f3dc978fa3919ae6f23ae893ee4ec64b7cccdd8bd87309fbfb916be40d342a2

https://lh3.googleusercontent.com/nHgpH1gWgauA9PxCVnLk0DNPIUlH1oXZM0m_vQFa_E7T7u2iwomZvilM4i7jrZsW40D-meLWsTtabwD5FlR34t1VdmzPDivgi1crm8RLLGccpEtVlckq

sliders in catalog app

MDC 1.11 version of Sliders

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/91bfd69a82cff2be59fa843f6c1e5f0685a54cd96e832789a5cd4017a789b1e3433238500290fe9e20d576d5d0c41e1620122f14f492384bfe78f4b0acc87e5e

https://lh3.googleusercontent.com/KN49PRsabGnC4SgVdwwtma86NiP2KZa8Hj3HPc-GgC2b_TBTH89TVtj8SaMOCv4kvPBT0fosafHdPcAJAl7ZZQn1XtpMOKjqUc2OBz_XPRsEtfpXqwM

sliders in catalog app

Basic Slider Options

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f62d2f0618bd621dd0ab36f2898b1a317d569821cdd2780d5a20dc30bb830ca17f6a4aa518e6e550e495653e914571061be324d98f3809ba3efaa3b11b12a092

https://lh3.googleusercontent.com/eDcSrLuTFtSdUxxzohbn16CKGeRF-htwKt_wS2KDld8nBL-C47GC1IobF6YCDcPzsxF-KlovQy0fg4DFPbz_LaIk3rb1Pip_cYC0a3gNOymmg_rdwyZe

sliders in catalog app

Advanced Slider Options

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/13563901d221a554afb77ad66f31015a3e9115a1ca5211a2228f1585888b0b208b125e1757e0c3ee8b543b0a77c6c6670cbfaf47f3cd19c06f8b7eb5358916ca

https://lh3.googleusercontent.com/zTR9b-1YWFR6bRePHuGgBfpuzK0Bek93AKrWZsdHX6AeRE6S02U9V71WAap31gAvIxiUDt-Gxsgs3GGdRONr1vMWI5pOaOm9fJRKjKAP3i70HAl-weYZ

Latest releases

carousel component

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f22172953c6932eb7562f9034735266ba1813d9ea3b48e254acf3a830bd5f74aa3459079e805aae203e9d0c6ee800294d95fcb0814fc4d03a8f2acbe7d818017

https://lh3.googleusercontent.com/fR3azAhK8xGmNL3cRg9f66GxSymGKh-WVmNQxzmoOvTa19vUrN2QNj8pjbw27466c4SIRGGZyTCYmTd8n7GnmbbJ75aw6n_zC3cFfR2dvh4pvt8RVA

updates libraries

{}

Get ready to experience Material Design Components for Android 1.11.0 and 1.12.0.  New color options and carousel refinements.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/840cc4958353a43be4c35ac6721aa6e3e6f7bb4fb477d4ab02e742909a08429593dfd2e97cca159ca3d48a791790f31fa1002cd253d1a925279019f375afad4a

https://lh3.googleusercontent.com/ETIfYZGY1PsTta4IFCVeMCMLTvoh5tYRncISKTvw-tqNHq3h1EiP8MgHnZXE80KAixZ0YPeSom1H-2IRrX1EiKFOIyX7hrKIi8Z5Gaz4Bw-94F_tABw

Material Design Components for Android 1.11.0 and 1.12.0

2024-05-08T13:00:00

android-stable-release-1-12-0

New color options and carousel refinements

Material Design Components for Android 1.11.0 and 1.12.0

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/47da200c393227f92314ec1902957b5c59e00177b03d8a0cc0001bd9149d55dc0781ded2a04705d2eb4564a19897d15633f0f696af869e52c13b9dd9fea0e1b2

https://lh3.googleusercontent.com/29VES8VMI2aMdi8A3pVXUoBAtHRCwwJta8G9Nn5nPRIYRVe88FIWFORh5mKiKIX98AiMSrj2eZ74yaJM4FbThzIWi2nzU-b9kC1EDfsaqKbDxh4aFQQy

/blog/google-io-2024

Material Design at I/O 2024

Material Blog

Material Design at I/O 2024

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/f76a10ef20aa3042fc461583cb2a0ac1ce5df95cdd3478424b0e318c5d8ed57cf9492e0503c8f7a07cf19185a453e248c8b840fd2bacf8f608bf5f18e47a9271

https://lh3.googleusercontent.com/thChzTWq1-LKKAjRUXGxrTTahkLJxqAWrUeSBQdDjM3bGInZtXNffv4t81qGiRuWLyZ15Esjpso-EPYanAZ1seXIfrOnG4qyRtUT5u_5zAkmYL_qwQ

/blog/material-3-carousel-research-design

Material Blog

Reinventing the Carousel

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/2ac5132cf499f5e4be8b845646d44b611ee51f2395155da747410e09dbc002c2defb13b46e477f5ec2017190412cb7a5888ddb3de816ef73adc754cb30682ebc

https://lh3.googleusercontent.com/GOsSmlbb-lQREXRGYtvmfrANBZA9FbIz6bjkZegnm-3vh0-RjP2yVxA6ftRE2QZl_Yr-tQKPKCBHnbe4fNZ4e0XGZrGc6UO-p00vY5a1sIKIM_LhBBM

/blog/dynamic-color-harmony

Designing Harmony into Dynamic Color

Material Blog

Designing Harmony into Dynamic Color

mio-example
