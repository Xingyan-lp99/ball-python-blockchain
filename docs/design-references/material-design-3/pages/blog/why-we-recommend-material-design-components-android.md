# Why We Recommend Material Components for Android

Source: https://m3.material.io/blog/why-we-recommend-material-design-components-android
Content endpoint: https://m3.material.io/page-data/Posts/5693645939015680.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/88dfb9efdf8466738cfe93126b654129ce7803ff8f51dd34d6ba32f3db2e8cbd830a91b904f8814a8262f834f33158067d3f6acf58f996dc77d400219ef46b57

https://lh3.googleusercontent.com/eJYg-triEugVDgv5PMQ5UM9NOSupuE8OHzMnRs120PJ-mCBICt9PrUeDeLNBd9DCeIoEx1FZnMI2qgK3h6q7Jy96LsrnxIN7uAif

Nick Butcher

Android Developer Relations

mio-example

```
<!-- This standard button will be replaced with a MaterialButton -->
<Button ... />

<!-- You can even use MaterialButton specific attributes -->
<Button ...
    app:icon="@drawable/foo"/>

<!-- Or if you want an AppCompatButton with backported features but not a MaterialButton, you can do this -->
<androidx.appcompat.widget.AppCompatButton ... />
```

```
<!-- Contained button -->
<Button ... 
    style="?attr/materialButtonStyle"/>

<!-- Text button -->
<Button ... 
    style="?attr/borderlessButtonStyle"/>

<!-- Outlined button -->
<Button ... 
    style="?attr/materialButtonOutlinedStyle"/>
```

<h5><em>Android users expect your app to look and behave in a way that&rsquo;s consistent with the platform. You should follow material design guidelines for visual and navigation patterns&hellip; <br />&mdash; <a href="https://developer.android.com/design">d.android.com/design</a></em></h5>
<p>Since your app exists alongside other apps installed on a user&rsquo;s phone, it&rsquo;s recommended that applications follow the <a href="https://material.io/design/introduction">Material Design guidelines</a> to ensure that apps operate consistently, and that patterns learned in one app can be used in another.</p>
<p>To implement this, you can use the <a href="https://github.com/material-components/material-components-android">Material Components for Android</a> (MDC) library. This post outlines the many benefits of using MDC, explaining why it&rsquo;s our recommended solution.</p>
<h2>Widgets</h2>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>MDC provides styled versions of standard widgets making it easy to implement Material styling. For example Material offers styled versions of <code><a href="https://material.io/develop/android/components/buttons">Button</a></code>s, <code><a href="https://material.io/develop/android/components/app-bars-top">Toolbar</a></code>s, <code><a href="https://material.io/develop/android/components/checkboxes">CheckBox</a></code>es and more. If you use a <code>MaterialComponents</code> theme, then Material widgets will be instantiated instead of the stock components when you inflate a layout (by MDC&rsquo;s <a href="https://developer.android.com/reference/com/google/android/material/theme/MaterialComponentsViewInflater">View Inflater</a>) so it&rsquo;s easy to achieve Material styling without having to make large updates to your layouts:</p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p>All Material widgets extend their relevant <code>AppCompat</code> counterparts so they benefit from the same backported functionality or bug fixes.</p>
<p>Material widgets offer extra styling and functionality over their platform or <code>AppCompat</code> counterparts, for example <a href="https://material.io/develop/android/components/buttons"><code>MaterialButton</code></a> offers a number of different display styles:</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p>One of my favorite additions is <code>TextView</code>s being replaced with <a href="https://material.io/develop/android/components/material-text-view"><code>MaterialTextView</code></a>s which add support for specifying line heights in <code>TextAppearance</code>s. Handy.</p>
<p>As well as adding to existing widgets, MDC offers a number of new widgets, not available in the platform or <code>AppCompat</code>. You&rsquo;ve likely seen <a href="https://material.io/develop/android/components/bottom-navigation-view/">Bottom Navigation</a>, <a href="https://material.io/develop/android/components/bottom-sheet-behavior/">Bottom Sheet</a> and <a href="https://material.io/develop/android/components/floating-action-button/">Floating Action Buttons</a> but might not have come across <a href="https://material.io/develop/android/components/chip/">Chips</a>, <a href="https://material.io/develop/android/components/picker">Date Picker</a> or <a href="https://github.com/material-components/material-components-android/blob/master/docs/components/TimePicker.md">Time Picker</a>.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>For a complete list of components offered by the library, see the <a href="https://material.io/components">components section</a>.</p>
<h2>Material Theming</h2>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p><a href="https://material.io/design/material-theming/">Material Theming</a> is a systematic way to customize Material Design to reflect your product&rsquo;s brand. A Material Theme comprises <a href="https://material.io/design/color/">color</a>, <a href="https://material.io/design/typography/">typography</a> and <a href="https://material.io/design/shape/">shape</a> attributes. Customizing these will be automatically reflected in the components you use to build your app.</p>
<p>You can think of Material Theming as a design system for creating design systems 🤯. You configure the color, type and shape inputs and get out a complete design system for your brand.</p>
<p>Nick Rout goes in depth into each of the three sub-systems in the following posts:</p>
<p><a href="https://material.io/blog/android-material-theme-color">Building a Material Theme on Android: Color</a><br /><a href="https://material.io/blog/android-material-theme-type">Building a Material Theme on Android: Typography</a><br /><a href="https://material.io/blog/android-material-theme-shape">Building a Material Theme on Android: Shape</a></p>
<h2>Dark Theme</h2>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p>MDC widgets implement Material&rsquo;s <a href="https://material.io/design/color/dark-theme.html">dark theme guidance</a>, with many widgets adapting their colors to dark themes and offering elevation overlays to communicate elevation when shadows don&rsquo;t read.</p>
<p>Chris Banes goes in depth about MDC's dark theme support in <a href="https://material.io/blog/android-dark-theme-tutorial">another post</a>.</p>
<h2>Material Motion</h2>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p>Material Design provides <a href="https://material.io/design/motion/the-motion-system.html">guidance</a> for screen transitions. Better than guidance alone, MDC now implements these patterns as Transitions ready to be dropped into your app. Hunter Stich introduces you to the material motion library in <a href="https://material.io/blog/android-material-motion">this post</a>.</p>
<h2>Get Composed</h2>
<p><a href="https://developer.android.com/jetpack/compose">Jetpack Compose</a> is Android&rsquo;s next-generation UI toolkit, currently in alpha. While it is not yet stable, it will offer an implementation of material components and material theming. Adopting MDC now will prepare your codebase for later adopting Jetpack Compose &mdash; it uses the same concepts, design vocabulary and components. It even becomes possible to ease your migration with libraries like <a href="https://github.com/material-components/material-components-android-compose-theme-adapter">MDC-Android Compose Theme Adapter</a> which converts an MDC XML theme into a Compose <a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#materialtheme">MaterialTheme</a>.</p>
<h2>Material Recommendation</h2>
<p>Hopefully it&rsquo;s clear to see why we recommend building Android UI with <a href="https://github.com/material-components/material-components-android">Material Components for Android</a>. We&rsquo;ve recently updated the <code>File &gt; New Project</code> template in Android Studio to use MDC and set up a material theme for you, making it even easier to get started. If you haven&rsquo;t already migrated to MDC, then check out <a href="https://material.io/blog/migrate-android-material-components">our migration guide</a>.</p>

Grid of baseline purple Material Components including banners, bottom navigation, buttons, floating action buttons, card, and chips.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/0decdca16b3fedcb692961f111a928fdc1f948532d041281902a0a1c50bd14d4248ab912be729839f7b9f38102076d0e4bd0442981f0c7621b217fb119a5ea16

https://lh3.googleusercontent.com/Y0bNV0tJr9AbuQGzOHwb4dJcesUxg0YY0ZL21f4gcVi09N1ikkUUsRBe6ZdLeoqQHj_Na0RKC27q_4-5EATlG2DmdpMPrHz4gs-UHA

Three baseline purple Material buttons with a filled style, text style and outlined style.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/7f17a7de4a51681b8b1f88c2ca4c9725f7976649d6352e63f68e42576bef67ea3e0f927380e51ed2147c84e1d221c998389c85481d07e1a7b1957a9b04ba5ad2

https://lh3.googleusercontent.com/X_GpLf-IrLScJgm3zTMe_KyFHPyZklfGXZ0vMVxojNV0tUHYD1e8HHS-E7ow0iyeuDrvE-1XLqVKf_0CdERMNmHxM3ZWm-nc-B86

Material Time Picker with a digital clock showing 07:00, an AM/PM toggle, and a circular time picker.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/3707e59f2abd97d9cb2efa2ee87e0d836880cd793d6d02b0f188e5a5fee78999995f533cc9ad8e531f77b33303f3811fe322bcae2bacbd2cde93618c4504e048

https://lh3.googleusercontent.com/ckPw0BqCjpOW5-YqRDf2WVP9twTlL82mMCOQ1Xu7JYQyvao1WDCsTp8xW-mEhYOiYSNHIf68vKhNSSja8ANmcYLxRxQuw-LOxjogpYw

Various apps demonstrating Material Theming, including a purple baseline app, a pink “Shrine” shopping app, a dark purple and red “Crane” travel app, and a grey and orange “Reply” inbox app.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/c3ddbfc3f9c37a34c79ddb1afc7173c052574746094ab42cc91155a32118161d92ec90ab675240ebc2bbb9bacdc1810cab86b2356cbd9b54c40424dca21ff272

https://lh3.googleusercontent.com/JFBeD_3tKAJescoKiWBDW3SS2ZBIY7UKEMVknQWCLSswP9iXbTiU78PdJMz1wIC5giWqT0OkX9FTp8WxCQHJA_rnqPcDfxeCEEAH

Various screens showing grids, lists and details, each animating to demonstrate container transform, shared axis, fade through, and fade transitions.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/572bf05a32382ba1ac7ad46dc100f6e0b8b6350309b98a2742033f6d6fa5763acc8f9bd9132ba682df2af348b4d91b64b6b0f2699f3d381d992c29e6c077d44b

https://lh3.googleusercontent.com/HcUay0xLeUoYBEDScQ61lMuC9bTlWCPWagTZHqtH_0vyobpouF_yZAgb-T_LAwMpNir1oSmIjMXQI4ChGfEM6eNdyFCvmY9ThZSA

Light and dark versions of a stats app using baseline Material purple.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/47dcd93079f87441d8ba4d710136885d332f37c45384b6673bbae11f11998cc0cddb3c18bce8efbd9ba64b5e0e8d5cc4d29d4595d4d288e85340b15d0263e38a

https://lh3.googleusercontent.com/9Y1NM2YQyI9p_tx4bzGuQr-bAGxfGbQJM7vzV3Ah2C82si22V8BisTafAXkex6hKxzPMQZorwJ207dxeny6MyWNkgDlebH1XvjwO

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/fdb010354d6710cbb15411c69c09d3b4a42f67b41cf99376103293c80ba7638a501d85a772f9c4be9632385e259ec5463258bbb39d102202f4a4d394d1be2b4e

https://lh3.googleusercontent.com/m79E6A7AVxB-mJ5yzx1aPqxbo2QyiEoAzMJhpbmyIGU9brgB0d4hZUDdXIt6suQFDOB6g7RcBcXAq8H_jfwTOhbTd3-yZ2MCcyuvC5k

{}

Discover the benefits of implementing Material Design Components for your Android app and how it can improve user experience.

Why We Recommend Material Components for Android

2020-08-25T13:00:00

why-we-recommend-material-design-components-android

Ensuring that patterns learned in one app can be used in another

Why We Recommend Material Components for Android

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/322f01ff2da66ef8d840aa17c0488c1fc16607708532e5f7368081ea4338d44dba54bd48c2126c6c0b8ded52e71d6ca8a5a703347e11a03f62cc7165524de507

https://lh3.googleusercontent.com/bfMMbed8nKlqbMiG9hWNElSG3sJSQdRAh1BxNNKVjumHRzwqMjn8JATE5YlgtiAfFZjyBeD4XLgNsT19JubwOawwvoC7AyGDNRBFmzQ

/blog/android-material-theme-color

Material Blog

Building a Material Theme on Android: Color

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/7f7a16e9dfeda6060e1c4f5bdedc94a231343e41c774c1e550ed9602faf37412a004c02558c2957244a25f020437bd813931f8e48a4eed61cb35b270afd082c1

https://lh3.googleusercontent.com/Wxts4cOyvF3jFuCHoe1w8QAm_RIlOqXA5tppbAIeOhcWksSdtHf2KuiglwKkczZp3hAz-BHwzwwohnk0rxeh7Nh4i4kTtT2ecVHN

/blog/migrate-android-material-components

Material Blog

Migrating to Material Components for Android

mio-example
