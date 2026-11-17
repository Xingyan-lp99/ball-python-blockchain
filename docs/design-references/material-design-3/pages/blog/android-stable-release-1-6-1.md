# Material Design Components for Android 1.6.1

Source: https://m3.material.io/blog/android-stable-release-1-6-1
Content endpoint: https://m3.material.io/page-data/Posts/5843048915402752.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/e542d55e05d06e63bbf3dadd467d6f4889a15a6c2c43b46c812a48b6ee2adf7ff126e17cb0d3c04d4d2f24d216f00138ed4cd9cbf209538cb1bd0f4fd7ac7f15

https://lh3.googleusercontent.com/ECgal03qq-GPHfoWRZft82d97qPwwB-M4z1d-igDCWWAMWhJteOVP4HzaU2XhhQVfG9ME-_0DWTFA1eK28kgnTgTHBpSnTIhLK8TQKwE0zyq_lFckrs

James Williams

Material Developer Advocate

mio-example

```java
@ColorInt
public static int harmonizeWithPrimary(@NonNull Context context, @ColorInt int colorToHarmonize) {  }


@ColorInt
public static int harmonize(@ColorInt int colorToHarmonize, @ColorInt int colorToHarmonizeWith) {  }
```

```java
val dynamicColorsContext = DynamicColors.wrapContextIfAvailable(requireContext())

val harmonizedOptions = HarmonizedColorsOptions.Builder()
 .setColorResourceIds(intArrayOf(R.color.custom1, R.color.custom2))
 .build();

harmonizedContext =
 HarmonizedColors.wrapContextIfAvailable(dynamicColorsContext, harmonizedOptions)
```

<p>After cooling down from Google I/O, we have a pair of Material Design Components(MDC) releases to share with you: <a href="https://github.com/material-components/material-components-android/releases/tag/1.6.0" target="_blank" rel="noopener">1.6.0</a> and <a href="https://github.com/material-components/material-components-android/releases/tag/1.6.1" target="_blank" rel="noopener">1.6.1</a>. As was the case with MDC 1.5.0, color is again a major theme with new APIs targeting <a href="https://m3.material.io/styles/color/dynamic-color/overview" target="_blank" rel="noopener">dynamic color</a> and <a href="https://material.io/blog/dynamic-color-harmony" target="_blank" rel="noopener">color harmony</a>.</p>
<p>Other notable highlights include Material3 style updates of various components and various bug fixes, like resolving issues on Android Oreo(8) and Pie(9), underscoring our commitment to more than just the most recent release.</p>
<p>Alongside the documentation we host on <a href="https://github.com/material-components/material-components-android/tree/master/docs">Github</a>, the <a href="https://m3.material.io/">Material Design 3 site</a> is an additional source for the styling guidance and availability of components. For components available on MDC Views, the implementation page will contain code snippets showing you how to implement that component and common use cases. Below is some of the code you can find on the <a href="https://m3.material.io/components/chips/implementation">implementation page for Chips</a>.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<h2>Color Harmony</h2>
<p>In the <a href="https://material.io/blog/android-stable-release-1-5">blog post</a> announcing MDC 1.5.0, we discussed using tooling to select colors beyond the core colors that exist in every Material3 theme. Custom or extended color inside of a dynamic theme presents an interesting question: &ldquo;How do we guarantee that a reserved color will look well alongside a dynamic theme AND still be legible?&rdquo;</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>The algorithm we use to create Material3 themes can handle this situation using a concept called color harmony. This harmonization works by shifting a target color towards a source color. Colors that are closer to each other appear more harmonious whereas colors that are further apart appear more discordant.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p>To read more about color science and the whys and hows of color harmony, check out <a href="https://material.io/blog/science-of-color-design" target="_blank" rel="noopener">The Science of Color &amp; Design</a> and <a href="https://material.io/blog/dynamic-color-harmony">Designing Harmony into Dynamic Color</a>.</p>
<h3>Applying Color Harmony On Demand</h3>
<p>Using the functions <a href="https://github.com/material-components/material-components-android/blob/948d5dac03a55971338d36bb52f1f49bd448ebd7/lib/java/com/google/android/material/color/MaterialColors.java#L185" target="_blank" rel="noopener"><code>harmonizeWithPrimary</code></a> and <a href="https://github.com/material-components/material-components-android/blob/948d5dac03a55971338d36bb52f1f49bd448ebd7/lib/java/com/google/android/material/color/MaterialColors.java#L199" target="_blank" rel="noopener"><code>harmonize</code></a>, you can harmonize a given color with the primary color for the theme or an arbitrary color.</p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<h3>Applying Color Harmony Systematically</h3>
<p>In most cases, instead of calculating harmonized colors on demand, you&rsquo;ll want to leverage helper classes in MDC 1.6.0 that can take in a set of attributes or colors and return harmonized versions to your theme seamlessly. HarmonizedColorAttributes and HarmonizedColorOptions are two builder classes you can use to enable harmonization when you retrieve a dynamic color Context.</p>
<p>The snippet below shows how to build a dynamic context that automatically harmonizes to two specified colors.</p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p>For a more detailed discussion of how to apply color harmonization in code, check out the <a href="https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md#using-color-harmonization" target="_blank" rel="noopener">Color Harmonization section</a> of our developer documentation on color or the <a href="https://codelabs.developers.google.com/harmonize-color-android-views#2" target="_blank" rel="noopener">codelab</a> that demonstrates both methods.</p>
<h2>What&rsquo;s next for MDC ?</h2>
<p>We&rsquo;re fast at work on the next major version of MDC. You can follow the progress, file <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=bug&amp;template=bug_report.md&amp;title=%5BComponent+name%5D+Short+description+of+issue" target="_blank" rel="noopener">bug reports</a> and <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=feature+request&amp;template=feature_request.md&amp;title=%5BComponent+name%5D+Short+description+of+request" target="_blank" rel="noopener">feature requests</a> on GitHub. Also feel free to reach out to us on Twitter <a href="https://twitter.com/materialdesign" target="_blank" rel="noopener">@materialdesign</a>.</p>

Screenshot from material.io

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/40c162fcca1d73b584de9bf0eb81d9c51de2763cde2eab5e4811daf42cf66ae075e2b171c4ba6c31a01f7c7c38059d97ad6e3d26fbdad833ce5e7db57706e702

https://lh3.googleusercontent.com/vGK0OPM_NKfC3c5wny9p5kkdUYysXlK8uWsXPpmcXZz0i6Ntq0H4Lnsc5Po6RhkMsTR4QjQQ0UljDNa5WWdeinnSUeuWlWkfmrsYm1GyYbo4D4sJBls

Screenshot from material.io

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/11efbfd65d3e96d35ac9153a73e18813aa6fb722b28669dba441d3db2b139df1598c2f1144f48e46cb6743c39e7a265714cd109261d4674bac86a2c602d7ab45

https://lh3.googleusercontent.com/2njPukopZEBNPC7t3JgT26y4wJXjIWVqTXpbXeGNfNG6pZZ-ESwkL3Fn6_jGHkqazhqH9oLRgm6r15c0hO007-yo1Yj1O6insDRuAyG5kwMTo15UHJU

Two swatches of yellow selected from a spectrum from yellow to green.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/b101545458af9184d09c39bf018d64629e9cfe088d03e40d965d74a2b7fa5a2173cdfefe3fa34ddd49164e07b1c3bd7d0d13f5fda7dcb75e02180cc8370e9b2f

https://lh3.googleusercontent.com/EC9mZRSbwP_aAQTHL4z8Rn5Gaw7THGeSKGDcIkzPAXrPJLMWdwbfQ79Xc8xtpoY3xmWr7XKRWl5jZb_y93Mb4AMFIzuwaCddZY5B_2z1u8kQCqKFY2E

Comparison of harmonious and less-harmonious color swatches.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d1fa5e5ee6733ca37ac507a8f77943c86d61b9c91fde6477df166b952cf851294cfc5486794bd22a0d8eb58882581bcf6224cb96adb789e7dca48ec5d58f82c2

https://lh3.googleusercontent.com/bCav1hV4fr9zldiZZJMkw_-zEp7JDwMPN8sHD2-Ib0tGlIDtPYu7bNDb6yKf9IvjEJUCUjcCpC59AKcqZMd1wpaPJreB2_l62vi7x-hQ15A7RvAVjQPi

Diagram of color swatches moving toward user-selected color.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/885faf75bec82816478dd77c538f51d21cabc4b81cf05ecc4bf3319e2313eb99b3bfbc7ac28ec675de116b05a2ce8489cdb0190a0793263cd557973e881f7633

https://lh3.googleusercontent.com/xgmGm0y5iMAixInKsXrdFo15UcR9ThHeM81xlRDVpXTYU3QDLJ6yyOfg3V2Y_icSD0tCQDjXhjrsSPI6KFhlbaAM5MICE0cZlRUHu82NYqXCWhhKUE6N

Abstract illustration

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/be9499969853567c7c3fca4474a5e69e8ec310acd2f4b67944afe553423094a0f46beb7b17e682455ebd2a3fd755f615ef4751d43d42aaa212aa55a0bf973ca0

https://lh3.googleusercontent.com/C-K_3-tg7BllaegZIAESRLUWBTFk81T1ErVoVDVX7IP_c_BJxPFdUu8tz-SKCwBVySdNWVqhWUPxY1tSZd7mQRS_SOIZRigCnyjvYRktzqdEPJRizQ

news releases mdc android

{}

Learn about Material Design 3 with MDC 1.6.1. Explore the new color harmony features, improved component styles for Android app's user experience.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6657a462ffbcefea095baf82d1cdde2e550be382d285b9fa6764f446e49ee98e4e69af80fafa3c2b3c95b5983cbc0b589788c32f9d2a2110319febc5b4301a37

https://lh3.googleusercontent.com/FT3no8pkVeN9j6IRmIoiW1ezOZH3vbUrZv7urWdhOisBFBNJ8SNccLHlWfjd3pCp_HyLTwqyD59MjKkvdtW0jk-vcNjZL5iriv0qFrhUvmX_VMQi569A

Material Design Components for Android 1.6.1

2022-07-07T12:59:00

android-stable-release-1-6-1

With color harmony and Material Design 3 refinements

Material Design Components for Android 1.6.1

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/2ac5132cf499f5e4be8b845646d44b611ee51f2395155da747410e09dbc002c2defb13b46e477f5ec2017190412cb7a5888ddb3de816ef73adc754cb30682ebc

https://lh3.googleusercontent.com/GOsSmlbb-lQREXRGYtvmfrANBZA9FbIz6bjkZegnm-3vh0-RjP2yVxA6ftRE2QZl_Yr-tQKPKCBHnbe4fNZ4e0XGZrGc6UO-p00vY5a1sIKIM_LhBBM

/blog/dynamic-color-harmony

Designing Harmony into Dynamic Color

Material Blog

Designing Harmony into Dynamic Color

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/2a9f578ce95c17ec93b1fe68e0aaf09a31485c930856cc9bff4b9078729d5176ecfde464df9b48b7acee1142130575f7109d74630b886fbc58ce5b7292099699

https://lh3.googleusercontent.com/o60K_0LJTxbo1c-5SP-ZRrDTOU1lUyzujbsE63jDyFgN52AsTK0eEsdPsciQkjO8nJ6iTG9K8U5nZbJtgbYSpHGMsVBzBiWDAcoKK0u9AtdraOSCHWs

Migrating to Material Design 3

/blog/migrating-material-3

Migrating to Material Design 3

Material Blog

Migrating to Material Design 3

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/362302fcebd869d647a92554dbe8a7b1e06b1eeb8ce46a6e67bfc5403441aea79237facc6dfe929599f4fb4bc8e6e836d2efbccab8abed1fca121d67d244aac4

https://lh3.googleusercontent.com/rME0woOrBvWQqpvpmd_QteVRux9dw9pT7HhbEVneGV5yyo1WzljxXgwf4wynieJPHPs--tPySUe7uoMiJwuYj-oNzXC8PwwXE1wK7Dyv9_UDhyce5A

Start building with Material You

/blog/start-building-with-material-you

Start building with Material You

Material Blog

Start building with Material You

mio-example
