# Building a Material Dark Theme on Android

Source: https://m3.material.io/blog/android-dark-theme-tutorial
Content endpoint: https://m3.material.io/page-data/Posts/4897180022996992.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/e441c777f742da42eb43209af95205c906dbe36b50eb39816a70934f73390c7cb57d634f0ff375633257f4955a479dce17d0ead838667c842ba3d9545741bb0f

https://lh3.googleusercontent.com/k0xjBr0cINAEwBuL11bQz9ssl0ITwLbCnWNz72LV-wE8Hwsxkz5AqanNEeBOfN47LtntkVxgHOEsrro27s_dY1MviS3v27IN8-L7_Q

Chris Banes

Android Developer Relations

mio-example

```
<style name="Theme.MyApp"
    parent="Theme.MaterialComponents.DayNight">
    <!-- Other theme attributes -->
</style>
```

```
<com.google.android.material.bottomappbar.BottomAppBar
   style="Widget.MaterialComponents.BottomAppBar.PrimarySurface" />
```

```
<com.google.android.material.bottomappbar.BottomAppBar
   style="Widget.MaterialComponents.BottomAppBar.PrimarySurface" />
```

```
values/themes.xml

<style name="Base.Theme.Tivi"
       parent="Theme.MaterialComponents.DayNight">
    <!-- Your app theme, minus color palette -->
</style>

<style name="Theme.Tivi" parent="Base.Theme.Tivi">
    <item name="colorPrimary">@color/slate_500</item>
    <item name="colorOnPrimary">#000000</item>
    <item name="colorSecondary">@color/orange_500</item>
    <item name="colorOnSecondary">#000000</item>
</style>
```

```
values/themes.xml

<style name="Base.Theme.Tivi"
       parent="Theme.MaterialComponents.DayNight">
    <!-- Your app theme, minus color palette -->
</style>

<style name="Theme.Tivi" parent="Base.Theme.Tivi">
    <item name="colorPrimary">@color/slate_500</item>
    <item name="colorOnPrimary">#000000</item>
    <item name="colorSecondary">@color/orange_500</item>
    <item name="colorOnSecondary">#000000</item>
</style>
```

```
<!-- 👍 Elevation overlay is applied: we're using colorSurface -->
<com.google.android.material.bottomappbar.BottomAppBar
    android:elevation="2dp"
    android:background="?attr/colorSurface" />

<!-- 👍 Elevation overlay is applied: 
        Surface style uses colorSurface -->
<com.google.android.material.bottomappbar.BottomAppBar
    android:elevation="2dp"
    style="@style/Widget.MaterialComponents.BottomAppBar.Surface" />

<!-- ❌ No elevation overlay applied: we're using colorSecondary -->
<com.google.android.material.bottomappbar.BottomAppBar
    android:elevation="2dp"
    android:background="?attr/colorSecondary" />

<!-- ❌ No elevation overlay applied: we're using colorPrimary -->
<com.google.android.material.bottomappbar.BottomAppBar
    android:elevation="2dp"
    style="@style/Widget.MaterialComponents.BottomAppBar.Primary" />
```

```
class CustomSurfaceView : View {
    private val shapeDrawable = MaterialShapeDrawable()

    init {
        background = shapeDrawable
        shapeDrawable.initializeElevationOverlay(context)
    }
    
    override fun onAttachedToWindow() {
        super.onAttachedToWindow()
        // Update the shape drawable with this view's absolute
        // elevation value in the view hierarchy
        MaterialShapeUtils.setParentAbsoluteElevation(this, shapeDrawable)
    }

    override fun setElevation(elevation: Float) {
        super.setElevation(elevation)
        onZChanged()
    }
    
    override fun setTranslationZ(translationZ: Float) {
        super.setTranslationZ(translationZ)
        onZChanged()
    }
    
    override fun setZ(z: Float) {
        super.setTranslationZ(translationZ)
        onZChanged()
    }
    
    private fun onZChanged() {
        // Tell the ShapeDrawable what our new Z value is
        shapeDrawable.z = z
    }
}
```

<p>In previous blog posts, Nick Rout went through the basis of Material Theming and the pillars of color, typography and shape.</p>
<p><a href="https://material.io/blog/android-material-theme-color">Building a Material Theme on Android: Color</a><br /><a href="https://material.io/blog/android-material-theme-type">Building a Material Theme on Android: Typography</a><br /><a href="https://material.io/blog/android-material-theme-shape">Building a Material Theme on Android: Shape</a></p>
<p>This post is going to build upon that to see how we can adapt our apps to support dark themes.</p>
<p>User selectable dark themes were added to the Android platform in Android 10, but that does not mean they&rsquo;re new to app developers. The default theme for Android devices was dark up until Android 5.0 (Lollipop)!</p>
<p>The difference last year was that the platform added a device-wide setting. Meaning that the user has additional control over the theme of the device, but also of apps.</p>
<p>Alongside the recent device-wide setting, we now also have comprehensive design guidance on material.io, which we will talk about later in this blog post.</p>
<h2>Why support dark theme?</h2>
<p>First up, why support a dark theme at all? The material.io <a href="https://material.io/design/color/dark-theme.html#usage">page on Dark Theme</a> has a good summary on some of the technical benefits (emphasis mine):</p>
<p><em>Dark themes reduce the luminance emitted by device screens [&hellip;]. They help <strong>improve visual ergonomics</strong> by reducing eye strain, adjusting brightness to current lighting conditions, and <strong>facilitating screen use in dark environments</strong> &mdash; all while <strong>conserving battery power</strong> [for OLED displays].</em></p>
<p>The most important reason though is that your users want it. The Android team added the system-wide dark theme setting because it consistently came up as a top requested feature by users.</p>
<p>Now that I&rsquo;ve convinced you to support dark themes in your app, let&rsquo;s look at how you add one&hellip;</p>
<h2>Quick start</h2>
<p>To add a dark theme to your app, use <a href="https://material.io/develop/android/">Material Components for Android</a> (MDC) for Android&rsquo;s support:</p>
<h4>#1: Change your theme</h4>
<p>You need to change your theme to extend from one of the <code>Theme.MaterialComponents.DayNight</code>&nbsp;themes:</p>
<p>&lt;mio-code-snippet index="0"&gt;&lt;/mio-code-snippet&gt;</p>
<h4>#2: Choose what mode to be in (optional)</h4>
<p>This step is optional, but allows you to support devices running versions of Android before Android 10. Since most devices before Android 10 do not have a system-level dark theme setting*, apps can provide their own in-app setting to allow users to choose what theme to use per-app.</p>
<p style="text-align: left;">&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>This is also still useful on Android 10+, as it allows users to override the system setting as they wish. As an example, imagine that the user sets their device theme to be controlled on a time schedule, but they know that they always want their social apps to use a dark theme.</p>
<p>To help with this, <a href="https://developer.android.com/jetpack/androidx/releases/appcompat">AppCompat</a> (which MDC uses) provides an API to set the chosen mode: <code>AppCompatDelegate.<a href="https://developer.android.com/reference/androidx/appcompat/app/AppCompatDelegate#setDefaultNightMode(int)">setDefaultNightMode()</a></code>. Commonly this would be called whenever a preference changes.</p>
<p><em>* Not strictly true. Some device manufacturers have added a system-level dark theme to their devices which are running Android 9 (and below). Unfortunately there&rsquo;s no way to determine this at runtime.</em></p>
<p>If you would like to read more about how the night mode feature in AppCompat works, have a look at <a href="https://medium.com/androiddevelopers/appcompat-v23-2-daynight-d10f90c83e94">this blog post</a>.</p>
<h4>#3: Test!</h4>
<p>And there we have the basis of a dark theme! It&rsquo;s time to test it out by checking each part of the app in both light and dark themes. Look out for any dark text on dark backgrounds, and hardcoded colors which do not have enough contrast against the dark backgrounds (typically, greys).</p>
<p>If you are using hard coded color values in your app, I recommend reading <a href="https://medium.com/androiddevelopers/android-styling-prefer-theme-attributes-412caa748774">this blog post</a> by Nick Butcher, which talks about preferring theme attributes. We also cover this in <a href="https://www.youtube.com/watch?v=Owkf8DhAOSo">our &lsquo;Theming with Style&rsquo; talk at Android Dev Summit &lsquo;19</a>.</p>
<h2>Material Dark Theme</h2>
<p>Now let&rsquo;s take a look at the design characteristics of dark theme which are described on Material.io.</p>
<h4>Grey vs black</h4>
<p>The first thing you might notice is that the default background for apps in dark theme is not black, but instead a dark grey: <code>#121212</code>.</p>
<p>There&rsquo;s lots of discussions about why we chose grey vs black, especially since the platform in Android 10 uses a black background. This is largely a trade-off between usability vs power savings.</p>
<p>Using a pure black <code>#000000</code> color as the background in the platform, allows the system apps and surfaces to use as little power as possible when they&rsquo;re open on OLED displays. These system surfaces tend to be quite simple, typically just text and simple icons, so to battle contrast issues we can adjust the text and icon colors to suit.</p>
<p>In apps though, your surfaces can contain anything: complex colorful vector animations, bright imagery, contrasting branded surfaces and lots more. Placing these against a pure black background means that the resulting contrast is much higher, which can increase eye strain. Unlike text and icons we mentioned above, it is often difficult or unwanted to tint/re-color these types of content to reduce the contrast, meaning that a lighter background is the solution.</p>
<h4>Color palette</h4>
<p>Next up, let&rsquo;s look at your app&rsquo;s color palette. It&rsquo;s likely that your app&rsquo;s color palette has been chosen based on the assumption of a light/white background, so we likely need to make some tweaks to the color palette when the app is running in a dark theme.</p>
<h4>Recap on Material color system</h4>
<p>We&rsquo;re going to be talking about color tones a lot below, so here&rsquo;s a quick recap on the Material color system. It defines colors as a series of tones within each color. The tones are numbered from 50 (lightest, least saturated tone), to 900 (darkest, most saturated tone). Here&rsquo;s the baseline teal and indigo color tones:</p>
<p style="text-align: left;"><span style="text-align: center;">&lt;mio-image index=1&gt;&lt;/mio-image&gt;</span></p>
<p style="text-align: left;">You can also play around in the <a href="https://material.io/resources/color/">Material color tool</a> to get an idea of how the tones for different colors vary. Nick Rout also wrote up <a href="https://medium.com/androiddevelopers/material-theming-with-mdc-color-860dbba8ce2f">a deep-dive on the color system</a>.</p>
<h4 style="text-align: left;">colorPrimary</h4>
<p style="text-align: left;">Your app&rsquo;s primary color is the most displayed color (other than background and surface colors), so we need to make sure that it is legible in dark themes. Typically in a light theme, your light theme would be a 500 tone of a color, whereas in a dark theme we recommend a less saturated and more luminous tone, typically 200, but can be up to 50 depending on the hue.</p>
<p style="text-align: left;">For your <code>colorPrimaryVariant</code>, we recommend using the <code>colorPrimary</code> from your light theme. As a rough guide:</p>
<p style="text-align: left;">&lt;mio-table index=0&gt;&lt;/mio-table&gt;</p>
<p style="text-align: left;">These values are just a starting point though. You should ensure that the chosen colors have a <a href="https://www.w3.org/WAI/standards-guidelines/wcag/">WCAG AA</a> contrast ratio of at least 4.5:1 against the background/surface color at all used elevation levels (more on that later).</p>
<p style="text-align: left;">&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p><a href="https://material.io/resources/color/">The Material color tool</a> is handy for experimenting with colors.</p>
<h4>colorSecondary</h4>
<p>For your secondary color, it&rsquo;s the same process as <code>colorPrimary</code>, by using a less saturated and more luminous tone of the same color.</p>
<p>The baseline Material dark theme treats the <code>colorSecondaryVariant</code> a little differently to <code>colorPrimaryVariant</code>, using the same tone for both <code>colorSecondary</code> and <code>colorSecondaryVariant</code>.</p>
<p>Again, as a rough guide:</p>
<p>&lt;mio-table index=1&gt;&lt;/mio-table&gt;</p>
<h4>Surface colors</h4>
<p><a href="https://material.io/design/color/applying-color-to-ui.html#sheets-and-surfaces">Bold colored surfaces</a> can be a great way to express your brand in commonly used components, such as cards. While vivid and bold colors work great against a white background, their legibility against a dark background isn&rsquo;t so great.</p>
<p>If the device and/or app has been set to use a dark theme, the app should read this as an intention from the user that they want a muted, less vivid color scheme at that moment.</p>
<p>With that intention in mind, even if we use muted <strong>50&ndash;200</strong> color tones for branded surfaces, it can still be too bold and emit too much light for a dark theme:</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>So what should you do? There are two options, which can be used together:</p>
<h4>Use primary surface</h4>
<p>The first step is the obvious one of not using bright, colorful surfaces when in dark theme. MDC makes this simple with its <code>PrimarySurface</code> styles, which switch between the <code>Primary</code> color in light theme and `Surface` color in dark theme.</p>
<p>Let&rsquo;s look at an example. Say we have a bottom app bar like the above example, we can use the <code>Widget.MaterialComponents.BottomAppBar.PrimarySurface</code> style:</p>
<p>&lt;mio-code-snippet index="1"&gt;&lt;/mio-code-snippet&gt;</p>
<p>If you have a non-MDC view which you would like to be treated similarly, you can use the <code>?attr/colorPrimarySurface</code> theme attribute:</p>
<p>&lt;mio-code-snippet index="2"&gt;&lt;/mio-code-snippet&gt;</p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<h4>Branded surface color</h4>
<p>To subtly express your brand color on all of your app&rsquo;s surface, you can set your <code>colorSurface</code> to be a calculated color of `colorPrimary` with 8% opacity, composited over `colorSurface`, when in dark theme.</p>
<p>For an example using the baseline theme&rsquo;s values:</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p>This allows your brand to subtly be applied across the app, while still keeping the intention of a muted, low light color palette.</p>
<h4>Crafting dark theme example</h4>
<p>If you&rsquo;d like to see an example of taking a light-themed app and adding a dark theme, watch <a href="https://material.io/blog/dark-theme-design-tutorial-video">Liam Spradlin&rsquo;s video</a>, where he crafts a dark theme for the <a href="https://material.io/design/material-studies/reply.html">Reply Material Study app</a>.</p>
<p>We&rsquo;ve just gone through a lot of information about choosing colors, but how should you set these in your Android app?</p>
<p>We&rsquo;re going to rely on some organisation of our themes. We&rsquo;re going to use a theme structure like this:</p>
<p>&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p>This structure enables us to easily vary the theme in light and dark themes, while also allowing us to re-use common content in the base theme.</p>
<p>If you&rsquo;d like to know more about this structure, I recommend watching the <a href="https://chris.banes.dev/talks/2019/developing-themes-with-style-berlin/">Developing Themes with Style talk</a> which Nick Butcher and I gave last year.</p>
<p>&lt;mio-code-snippet index="3"&gt;&lt;/mio-code-snippet&gt;</p>
<p>&lt;mio-code-snippet index="4"&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Elevation overlays</h2>
<p>Earlier in this post, we mentioned in a few places about testing contrast against all elevation levels. You might have been wondering why that is, when elevation is about lifting surfaces to cast shadows, right? Well yes, elevation is about lifting surfaces, but it&rsquo;s not just about casting shadows.</p>
<p>Shadows in the Material system are cast by numerous <a href="https://material.io/design/environment/light-shadows.html#light">light sources</a>, and as we lift surfaces (using elevation property), we are lifting them towards the light sources. Just like the world around us, shadows occur when those light sources are blocked by surfaces. Similarly, the closer that a surface is to a light source the more that the surface is lit, changing its perceived color.</p>
<p>For light surface colors, such as white, that change is imperceptible since it is already light. For dark surfaces though, it can have a large effect:</p>
<p>&lt;mio-image index=7&gt;&lt;/mio-image&gt;</p>
<p>This is where elevation overlays come into play. The behavior of lightening the surface color is expressed as compositing a translucent white overlay of onSurface, over the surface color. The greater the elevation, the more opaque the overlay.</p>
<p>Going back to address the earlier points, this is why you need to test at the different elevations. As the visual surface changes based on the elevation, you need to make sure that any foreground colors provide enough contrast. Ideally you set a single <code>onSurface</code> color which works for all of the elevation values used in your app.</p>
<h2>Widget support</h2>
<p>All of the components in Material Design Components support <a href="https://material.io/design/color/dark-theme.html#properties">elevation overlays</a> automatically, including: Top App Bar, Bottom App Bar, Bottom Navigation, Tabs, Cards, Dialogs, Menus, Bottom Sheet &amp; Navigation Drawer.</p>
<p>This means that using the standard elevation APIs will automatically apply an elevation overlay, as long as the background is set to <code>?attr/colorSurface</code>&nbsp;(either explicitly or using a surface style variant). Going back to our earlier example:</p>
<p>&lt;mio-code-snippet index="5"&gt;&lt;/mio-code-snippet&gt;</p>
<p>There are some theme attributes which you can set to change the behavior of elevation overlays:</p>
<ul>
<li><code>?attr/elevationOverlayEnabled</code>&nbsp;allows you to turn on/off elevation overlays for your theme. This defaults to true in dark theme, false in light theme.</li>
<li><code>?attr/elevationOverlayColor</code> allows you to change the color of any elevation overlays. This defaults to <code>?attr/colorOnSurface</code>.</li>
</ul>
<p>You shouldn&rsquo;t really need to change these values though.</p>
<h2>Custom views</h2>
<p>So that&rsquo;s great, but what if you&rsquo;ve got a custom view which needs to support elevation overlay? Well you&rsquo;re in luck. All of the elevation overlay support is built into <a href="https://developer.android.com/reference/com/google/android/material/shape/MaterialShapeDrawable">MaterialShapeDrawable</a>, with a bit of plumbing in your view:</p>
<p>&lt;mio-code-snippet index="6"&gt;&lt;/mio-code-snippet&gt;</p>
<h2>OK Google, goodnight 🌚</h2>
<p>Hopefully by the end of the blog post you&rsquo;ve gained an understanding of what you need to do to add a dark theme to your app. If there&rsquo;s anything you found difficult when implementing a dark theme, leave a comment below or reach out to us on Twitter <a href="https://twitter.com/materialdesign">@MaterialDesign</a> and <a href="https://twitter.com/androiddev">@AndroidDev</a>.</p>
<p></p>

Dark Theme settings screen with dark grey background and purple switch toggle.

Example in-app dark theme setting

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/908ec773b3a9519cc4a54a8c5a2e497644ad6d6d8b76b90cbdd90bfc34a57e841b5c7a8232b3d481240ce95a8cd8033a2fcf4131abbaa974c3a8b0a17cb3caa8

https://lh3.googleusercontent.com/fj735Xvllsyev9581m3U8iqFqkA3mQoJtc4cVxWlM1ZNcrKCqr6WAjCKsXNkDSWfhJwXZybObNdKUCrIQWJhUMIVg9XGlG2_G4ad_Yc

Two rows of square purple and turquoise colors over a light grey background increasing in lightness from dark purple to light purple, and dark turquoise to light turquoise.

Baseline Material color palettes

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/66903b9e9822a1726ebc2202e70aadff738a56b12ca50d026de0286cfee4993fd9389ddeff17d35fc6641c4092485db6e66142ab86ca3f2ceb1ec7a50e1c588f

https://lh3.googleusercontent.com/_dSFAyUwtgMvXkelYY0YzkHw4IHl0NBqoD-VtPbXtVehCxnCqjFXmCvcMCG2KkK-yz2YQUt2qsrTP_knfF9nnukVKPSJcYFDhQx2Ow

A row of square purple colors over a dark grey background increasing in lightness from dark purple to light purple

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/1cac868f85f959375d86e7d863aac6ec0210eb9634b85b83d0b81dbb3a34ff9c254b62b9139d0d9ef272efdd0def7b940796542e0bbca4cd09b850a00c187316

https://lh3.googleusercontent.com/dzVEmxUUQDz1IF27ccyMgDwUS112OR1ssWkhw03uYdBa5A3OaxZOb7D0jWHhLtVJb8YOWrEjUFyzeXRascLR5O1VTavnqIMedQhl

A bottom app bar component with a light purple background covered by a floating action button component with a dark grey background and white plus icon.

Avoid filling large regions with vivid colors.

caution

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/527bfd2c007ec546f3628c9bf941bbe66250a151fcc6b89636ce2b221d869e5e5f7acfacaa9db0f05359dcdda7da2bb566dc6c6c3b7fd32c7a6de95559170548

https://lh3.googleusercontent.com/msOcZ1La-avPL1xS4jxwUTTZ4F7nZrdq8AGaAiAS6dNNTJafxDK2bSRS_zWgzFcvnSVlazr_N0lf_GUzSezLDcP-H--rT4ruf1CmA50

Two phone screens showing a blue background on the left and a dark grey background on the right.

colorPrimarySurface applied across light and dark themes

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6f796f775b4a01f3307866d6fb9af28d8c146388697e5b49f7ca0095d9b27aa1daee4c470af4c07b5d8619b73ae3dc026bef1d5447777888b9bec7cc99dd71cc

https://lh3.googleusercontent.com/SgXfHggIrxdROUQs8lcMOZgFqCf5-txosXBhbhfOX5vjzN_X8au4N8fmoyK03TefsWvePW8dl8DQu2ioC6r1WO8EdiWTjC62y4SS4w

A diagram showing two surfaces, translucent purple and dark grey, being composited vertically over each other.

A custom colorSurface can be expressed as a calculated color based on a composition of colorPrimary over a dark theme's colorSurface

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/b1340428b5fec5a4ea962cf777b2543961acc95c9478252881422daa7fdfcc5c792028d5eb2bb87a7d959e27c8a4a8683f7ef5ae4d4a45726a4e76140d39ca9d

https://lh3.googleusercontent.com/NBedPZaXuj5x-DTzxExI3u-1nO_4FRGWR-zQV1VEZkj45Cj2gIJLj_K8TqCychRP7Uy-xHSwRz6JV3KtWGEPiXnfosem_l3wUWjM

A diagram with yellow, green, and red blocks indicating a platform, base, and app theme hierarchy.

This example theme structure works well for dark themes

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/0f9b21f9946207b991dd9f9143f40e8814de1e8478f54a461e63ccd0d1f5195d5799241d3bfd0fd4cc8ed35c1a5dda060632cf5f1b1b8b996d6ac98700f95513

https://lh3.googleusercontent.com/7hHe6QpYb7DIJZF3nOFiMREl9yyPdyVyeBSYLKdbOQgcKT6fI1S1HOFoVP8FfQ_Av2po-V7h_5-GzBrB6dwK623LDyueBm5AeFbN5A

A square surface and a dial. The surface gets lighter as the dial increases its elevation.

Elevation overlays lighten as the elevation value increases

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/94bc2b32eeceec57f45812e48da4f2666a044f1648ed9e5d262451cdddc27b780ceb07b0f041dd10d459eeaa03e562f32fe885ea19951cfde130e19e79b3dd98

https://lh3.googleusercontent.com/LowBLDd5VzR1-rd2zk1qZySKubJRoXOMy8kzPcvKVJs7p2mmUzDgUM94ZeOtXntj67pcRv1XbmM3BXQ7tcEWwX4ybwT-dg4Qg0nu76o

| Theme | colorPrimary | colorPrimaryVariant  |
|-------|--------------|----------------------|
| Light | 500 tone     | colorPrimary +/- 200 |
| Dark  | 50-200 tone  | 500 tone             |

| Theme | colorSecondary | colorSecondaryVariant  |
|-------|----------------|------------------------|
| Light | 500 tone       | colorSecondary +/- 200 |
| Dark  | 50-200 tone    | 50-200 tone            |

Illustration of a bottom navigation bar next to a stylized sunset.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/9a1c23d4b60599686377834775349c6dcf2577b430eea1c3c4e700a1065bcba18febc6937b82f136f2f399f835afafc59c9b520b80e137aa203c69cc042340f0

https://lh3.googleusercontent.com/G7zEHSzJ1gx4YqOXImcWFm1zyfeHl5vcZooH5rMiKDleGAfk6W8HW2SoMcQZibcU8RGjCpSbM_-FLi6FZ0VN_oXyCJmbWl8QOLa9tQ

how-to,color,theming,development,android,material-components

 

{}

How to turn out the lights on Android using the MDC library

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/4a376480a203757d40c349d5ab5f71faa109665dd1eea0e8ec1cbd0073f4d5a7ff90a081e1da43923ca066ccc0d1fe9e320ffd099301e1e0de3ec6269a9effea

https://lh3.googleusercontent.com/faTgDEo8Xo0iDTyJ7p94_ZSHszQaPZiRzDBMPndXnOFyr4RB-yyQPCRxBU8XuuHmsA30oWWCOBc6tKPb-V941zSg5Tk4vRQvNWB0Y_M

Building a Material Dark Theme on Android

2020-08-26T13:00:00

android-dark-theme-tutorial

How to turn out the lights on Android using the MDC library

Building a Material Dark Theme on Android

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/322f01ff2da66ef8d840aa17c0488c1fc16607708532e5f7368081ea4338d44dba54bd48c2126c6c0b8ded52e71d6ca8a5a703347e11a03f62cc7165524de507

https://lh3.googleusercontent.com/bfMMbed8nKlqbMiG9hWNElSG3sJSQdRAh1BxNNKVjumHRzwqMjn8JATE5YlgtiAfFZjyBeD4XLgNsT19JubwOawwvoC7AyGDNRBFmzQ

/blog/android-material-theme-color

Material Blog

Building a Material Theme on Android: Color

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/2f95c86bdc1b02ce73d92619c01d8e49eed9376d66b001fefc3322502ceab9d6e0a58b35639ea0777289ba6163c3a79dd95f3108d519fafbc9eea399cb404b58

https://lh3.googleusercontent.com/uX7KzRFGZKbProyCEHQKohPAN8DFI-IJqbRrvvzEMqnoVp06w7g_LW7d5HfKXPXtObG_OD0GVBl69yWS8eWP8DjfnJVHijIApnSW

/blog/android-material-theme-type

Material Blog

Building a Material Theme on Android: Typography

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/1a22d1f6b1218d5a2e18535bbdf793f184a27980c1b8063006968aac95a521b95baddadeb3c14a6a2e07398ab15d597c962454f22abdb5f8a8d1e233725cd5d3

https://lh3.googleusercontent.com/Xvk1QwDoH9IbK1BQIKCiF08ViXB3y9X9CRNZ_CiPM2XrgjCzF9ZJHBPlhH15ylunDGKg_AwatpSGTE3JkZnQyyzlTHgBTRFpqjVQ

/blog/android-material-theme-shape

Material blog

Building a Material Theme on Android: Shape

mio-example
