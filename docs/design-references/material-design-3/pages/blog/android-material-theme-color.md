# Building a Material Theme on Android: Color

Source: https://m3.material.io/blog/android-material-theme-color
Content endpoint: https://m3.material.io/page-data/Posts/6218501906497536.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/18a6db2775f36a6a1b0cae6a88e8df282b27cf4a9db808be9c693fd35bdd3314798a1545d32d424a38e33f75b203165168f010c199ce63799b5e91d6309969a3

https://lh3.googleusercontent.com/m-PDSndGA4cUhtNjSl4HXPqXIaHxvYG28BPPcal5dnXUge1Po6SJJw2I3RjrIYyKBY6exL4bXnjaDt9dusnuDVO_anSC8lzVK7pCvWo

Nick Rout

Material Developer Advocate

mio-example

```xml
app:backgroundTint=”?attr/colorSecondary”
```

```xml
<!-- 60% alpha = 99 -->

<color name=”navy_700_alpha_60”>#9937596D</color>
```

```xml
val primary60 = AppCompatResources#getColorStateList(
    context, R.color.primary60
)
```

```xml
<!-- In res/values/attrs.xml -->
<attr name="colorCustom" format="color" />

<!-- In res/values/themes.xml -->
<style name="Theme.App" parent="Theme.MaterialComponents.*">
    ...
    <item name="colorCustom">@color/...</item>
</style>
```

```xml
<!-- In res/values/colors.xml -->
<color name="navy_500">#64869B</color>
<color name="navy_700">#37596D</color>
<color name="navy_900">#073042</color>
<color name="green_300">#3DDC84</color>
<color name="green_500">#00A956</color>
```

```xml
<!-- In res/values/themes.xml -->
<style name="Theme.App" parent="Theme.App.Base">
    ...
    <item name="colorPrimary">@color/navy_700</item>
    <item name="colorPrimaryVariant">@color/navy_900</item>
    <item name="colorSecondary">@color/green_300</item>
    <item name="colorSecondaryVariant">@color/green_900</item>
    <!-- Using default values for colorOnPrimary, colorSurface, colorError, etc. -->
</style>

<!-- In res/values-night/themes.xml -->
<style name="Theme.App" parent="Theme.App.Base">
    ...
    <item name="colorPrimary">@color/navy_500</item>
    <item name="colorPrimaryVariant">@color/navy_900</item>
    <item name="colorSecondary">@color/green_300</item>
    <item name="colorSecondaryVariant">@color/green_300</item>
    <!-- Using default values for colorOnPrimary, colorSurface, colorError, etc. -->
</style>
```

```xml
<Button
    ...
-    app:backgroundTint="@color/green_300"
+    app:backgroundTint="?attr/colorPrimary"
-    android:textColor="@color/black"
+    android:textColor="?attr/colorOnPrimary"
    />
```

```xml
<!-- In res/color/primary_60.xml -->
<selector ...>
    <item android:alpha="0.6" android:color="?attr/colorPrimary" />
</selector>
```

```xml
 <!-- In button/res/color/mtrl_btn_bg_color_selector.xml -->
<selector ...>
  <item android:color="?attr/colorPrimary" android:state_enabled="true" />
  <item android:alpha="0.12" android:color="?attr/colorOnSurface" />
</selector>
```

```xml
<!-- In res/values/themes.xml -->
<style name="ThemeOverlay.App.PrimarySecondary" parent="">
    <item name="colorPrimary">?attr/colorSecondary</item>
    <item name="colorOnPrimary">?attr/colorOnSecondary</item>
</style>
```

```xml
<Button
    ...
    <!-- Alternatively apply with android:theme -->
+    app:materialThemeOverlay="@style/ThemeOverlay.App.PrimarySecondary"
    />
```

```xml
<!-- In res/values/attrs.xml -->
<declare-styleable name="AppCustomView">
    <attr name="backgroundTint" />
    <attr name="titleTextColor" />
    ...
</declare-styleable>

<!-- In res/values/styles.xml -->
<style name="Widget.App.CustomView" parent="android:Widget">
    <item name="backgroundTint">?attr/colorSurface</item>
    <item name="titleTextColor">
        @color/material_on_surface_emphasis_high_type
    </item>
    ...
</style>
```

```xml
// Resolve color from theme attr
val primaryColor = MaterialColors.getColor(
    view, R.attr.colorPrimary
)

// Layer background color with overlay color + alpha
val overlayedColor = MaterialColors.layer(
    view, R.attr.colorSurface, R.attr.colorPrimary, 0.38f
)
```

<p><a href="https://material.io/design/material-theming/overview.html#material-theming">Material Theming</a> is a way to customize <a href="https://material.io/components">Material Components</a> to align with your brand. A Material theme includes <a href="https://material.io/design/color/">color</a>, <a href="https://material.io/design/typography/">typography</a> and <a href="https://material.io/design/shape/">shape</a> parameters which you can adjust to get near-infinite variations of the components &ndash; all while maintaining their core anatomy and usability.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>On Android, Material Theming can be implemented using the <a href="https://github.com/material-components/material-components-android">Material Components (MDC) library</a>, from version <code>1.1.0</code> onwards. If you&rsquo;re looking to migrate from the Design Support Library or MDC <code>1.0.0</code>, take a look at <a href="https://medium.com/androiddevelopers/migrating-to-material-components-for-android-ec6757795351">our migration guide</a>.</p>
<p>This article will be focusing on <strong>color</strong> theming.</p>
<h2>Color attributes</h2>
<p>Material Design provides 12 color &ldquo;slots&rdquo; that make up the overall palette of your app. Each of these have a design term (eg. &ldquo;Primary&rdquo;) along with a corresponding color attribute that can be overridden in your app theme (eg. <code>colorPrimary</code>). There are default &ldquo;baseline&rdquo; values for both your light theme and dark theme.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>Material Components use these color attributes to tint elements of the widgets.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>They are applied&nbsp;<span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">in layouts and widget styles like this, for example:</span></p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p>You might recognize some of these color attributes like <code>colorPrimary</code>. That&rsquo;s because a few of them are inherited from AppCompat and the platform, while the rest have been newly introduced by MDC. The table below illustrates the origin of each attribute.</p>
<p>&lt;mio-table index=0&gt;&lt;/mio-table&gt;</p>
<h2>Picking colors</h2>
<p>Figuring out which color values to use for each slot may be the responsibility of a designer, or derived from your product&rsquo;s brand. However, it&rsquo;s still useful to know about the role of each color, the relationship between them, and how to meet accessibility requirements:</p>
<ul>
<li><code>colorPrimary</code>&nbsp;and <code>colorSecondary</code>&nbsp;represent the colors of your brand</li>
<li><code>colorPrimaryVariant</code> and <code>colorSecondaryVariant</code>&nbsp;are lighter or darker shades of your brand colors</li>
<li><code>colorSurface</code>&nbsp;is used for &ldquo;sheets&rdquo; of material (like cards and bottom sheets)</li>
<li><code>android:colorBackground</code> is the window background color of your app</li>
<li><code>colorError</code> is, as the name suggests, for errors and warnings</li>
<li>The various &ldquo;On&rdquo; colors (<code>colorOnPrimary</code>, <code>colorOnSecondary</code>, <code>colorOnSurface</code>, etc.) are used to tint foreground content (such as text and icons) displayed on top of the other colors. They need to meet accessibility requirements and have sufficient contrast against the colors they&rsquo;re displayed on.</li>
</ul>
<h2>Color tools</h2>
<p>Material Design provides useful tools for previewing colors and determining suitable variants and &ldquo;On&rdquo; colors:</p>
<ul>
<li><a href="https://material.io/resources/color/">Material color tool</a>: Get light/dark variants of your primary and secondary colors as well as the appropriate &ldquo;On&rdquo; color. Preview how these will look in sample screens.</li>
<li><a href="https://material.io/design/color/the-color-system.html#tools-for-picking-colors">Material palette generator</a>: Generate a full tonal palette (shade 50 - 900) of a color. Get suggestions for complementary, analogous, and triadic colors.</li>
</ul>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<h2>Things to consider</h2>
<ul>
<li>You almost always want to override <code>colorPrimary</code>, <code>colorSecondary</code> and their variants, unless your brand happens to use the exact same purple/teal hex values as the baseline Material Theme.</li>
<li>You don&rsquo;t have to override all colors. Some, such as <code>colorSurface</code>, use neutral colors so relying on the default values is perfectly fine.</li>
<li>If your brand does not define any kind of secondary or accent color, it&rsquo;s ok to use a single color for both <code>colorPrimary </code>and <code>colorSecondary</code>. The same can be said of variants (eg. <code>colorPrimary</code> and <code>colorPrimaryVariant</code> could be the same).</li>
<li>Despite being separate attributes, there&rsquo;s an inherent link between a color, its variant (if one exists), and its &ldquo;On&rdquo; color (eg. <code>colorPrimary</code>, <code>colorPrimaryVariant</code> and <code>colorOnPrimary</code>). Overriding one means you need to check the others to see if they make sense and meet accessibility requirements.</li>
</ul>
<h2>Additional color slots</h2>
<p>Your design system may call for additional color slots outside of the 12 that Material Theming specifies. Thankfully this is relatively easy to do on Android by declaring a color attr:</p>
<p>&lt;mio-code-snippet index=3&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Color resources</h2>
<p>Color values are defined as <code>&amp;lt;color&amp;gt;</code> &nbsp;<span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">resources. For custom colors we recommend two approaches to help separate concerns, and create a single source of truth for color theming values in your app:</span></p>
<ul>
<li>Store all day <code>&amp;lt;color&amp;gt;</code>s in a single res/values/colors.xml file</li>
<li>Use literal names for <code>&amp;lt;color&amp;gt;</code>s that describe the value as opposed to how it's used:
<ul>
<li>Doing so encourages the use of <code>?attr/</code>&nbsp;references when using colors, which is a recommended approach for supporting dark themes</li>
<li>Use names like <code>green_500</code> or <code>brand_name_yellow</code></li>
<li>Avoid semantic names like <code>color_primary</code></li>
</ul></li>
</ul>
<p>&lt;mio-code-snippet index=4&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Overriding colors in an app theme</h2>
<p>Let&rsquo;s take a look at how you can add your chosen color palette to your app theme by overriding relevant attributes.</p>
<p>First, we recommend setting up your theme(s) to gracefully handle light and dark color palettes while reducing repetition with base themes. For more on this topic, take a look at Chris Banes&rsquo; article on <a href="https://medium.com/androiddevelopers/dark-theme-with-mdc-4c6fc357d956">dark theme</a> as well as the "<a href="https://chris.banes.dev/talks/2019/developing-themes-with-style-berlin/">Developing Themes with Style</a>" talk given by him and Nick Butcher.</p>
<p>Once set up, override the color attributes you wish to change in your light and dark themes:</p>
<p>&lt;mio-code-snippet index=5&gt;&lt;/mio-code-snippet&gt;</p>
<p>Material Components will respond to theme-level color overrides:</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<h2>Color reusability and best practice</h2>
<p>There are many circumstances which involve using colors in layouts, drawables, styles, and elsewhere. We&rsquo;re going to go through some approaches to make your code as reusable as possible, regardless of the color values specified in your app theme.</p>
<h2>Prefer attrs</h2>
<p>The most important thing we suggest is to use <code>?attr/</code>&nbsp;color references. This is the recommended approach to creating reusable layouts and default styles that support multiple themes like light/dark.</p>
<p>&lt;mio-code-snippet index=6&gt;&lt;/mio-code-snippet&gt;</p>
<p>Take a look at Nick Butcher&rsquo;s <a href="https://medium.com/androiddevelopers/android-styling-prefer-theme-attributes-412caa748774">&ldquo;Android Styling: Prefer Theme Attributes&rdquo;</a> article for further explanations and some exceptions to the rule.</p>
<h2>Colors with alpha</h2>
<p>There are times when you may want to use one of the colors from your MDC theme with an alpha value eg. <code>colorPrimary</code>&nbsp;at 60%. Examples of this include touch ripples and checked state overlays.</p>
<p>Android&nbsp;<code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">&amp;lt;color&amp;gt; </span></code>&nbsp;<span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">resources do allow for an alpha channel:</span></p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p>However, with this approach we need to maintain separate color resources per alpha value. It also means we can&rsquo;t use these as <code>?attr/</code>s and goes against our single source of truth approach mentioned above.</p>
<p>Rather, we suggest taking advantage of <code>ColorStateList</code>s stored in your res/color directory. A CSL can have a single item which includes a color reference and an alpha value, which is perfect for our use case:</p>
<p>&lt;mio-code-snippet index=7&gt;&lt;/mio-code-snippet&gt;</p>
<p>Using these might cause you to raise an eyebrow &ndash; they&rsquo;re referenced with the <code>@color/primary_60</code> notation &ndash; but this is fine considering we&rsquo;re dealing with a CSL that itself uses <code>?attr/</code>&nbsp;to reference the underlying theme color.</p>
<h2>Colors per state and theme overlays</h2>
<p><code>ColorStateList</code>s are more commonly used to switch between colors (and alpha values) depending on the state of the view. MDC widgets use this generously for disabled states, hovered vs. pressed states and so on. Here&rsquo;s an example of a button&rsquo;s background tint from the MDC <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/res/color/mtrl_btn_bg_color_selector.xml">source code</a>:</p>
<p>&lt;mio-code-snippet index=8&gt;&lt;/mio-code-snippet&gt;</p>
<p>Keeping with the button example, suppose you want to change the main background tint from primary to secondary:</p>
<p>&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p>You <em>could</em> copy the above source file into your codebase and change <code>colorPrimary</code> to <code>colorSecondary</code>, but this is tedious and becomes problematic if the source code happens to change.</p>
<p>A better way to do this is to use theme overlays. Nick Butcher goes into detail about this in his <a href="https://medium.com/androiddevelopers/android-styling-themes-overlay-1ffd57745207">&ldquo;Android Styling: Themes Overlay&rdquo;</a> post. Essentially we can replace the value of a specific theme attribute (<code>colorPrimary</code> in our case) for a particular <code>View</code> or <code>ViewGroup</code>&nbsp;and any descendants (in our case a button).</p>
<p>A basic theme overlay can be seen below. Note the empty parent, which ensures we only override the attrs we wish to change:</p>
<p>&lt;mio-code-snippet index=9&gt;&lt;/mio-code-snippet&gt;</p>
<p>When applying theme overlays in XML, there are two options to consider:</p>
<ul>
<li><code>android:theme</code>: Works with all widgets, doesn&rsquo;t work in default styles</li>
<li><code>app:materialThemeOverlay</code>: Only works with MDC widgets, works in default styles</li>
</ul>
<p>&lt;mio-code-snippet index=10&gt;&lt;/mio-code-snippet&gt;</p>
<h2>API compatibility</h2>
<p>Platform support for <code>?attr/</code>s in CSLs and elsewhere was only added in API 23. If your minSdk is below this, don&rsquo;t worry: compatibility classes do exist! In fact, both MDC and AppCompat widgets make use of these under-the-hood so no additional work is required when using them.</p>
<p>For scenarios where you need to use CSLs programmatically, use <a href="https://developer.android.com/reference/androidx/appcompat/content/res/AppCompatResources"><code>AppCompatResources</code></a>:</p>
<p>&lt;mio-code-snippet index=2&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Color in MDC widgets</h2>
<p>Earlier we said that MDC widgets respond to overrides of theme level color attributes. But how would you know, for example, that a button uses <code>colorPrimary</code> as its background tint and <code>colorOnPrimary</code>&nbsp;for its icon and text label? Let&rsquo;s take a look at a few options.</p>
<h2>MDC developer docs</h2>
<p>The MDC developer docs have recently been refreshed. As part of this we&rsquo;ve included attribute tables which include design terminology and default values used in the library. For example, check out the &ldquo;Anatomy and key properties&rdquo; sections of the updated <a href="https://github.com/material-components/material-components-android/blob/master/docs/components/Button.md">buttons doc</a>.</p>
<p>&lt;mio-image index=8&gt;&lt;/mio-image&gt;</p>
<h2>Source code</h2>
<p>Inspecting the MDC source code is arguably the most reliable approach. MDC uses default styles to achieve Material Theming so it&rsquo;s a good idea to look at these as well as any styleable attrs and the java file(s). For example, check out the <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/res/values/styles.xml">styles</a>, <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/res/values/attrs.xml">attrs</a> and <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/MaterialButton.java">java file</a> for <code>MaterialButton</code>.</p>
<p>&lt;mio-image index=9&gt;&lt;/mio-image&gt;</p>
<h2>Color in custom views</h2>
<p>Your app may include custom widgets you&rsquo;ve built or gotten from an existing library. Making these views responsive to Material Theming is useful when using them alongside standard MDC widgets. Let&rsquo;s take a look at what to keep in mind when supporting color theming for custom widgets.</p>
<h2>Use MDC attrs in &amp;lt;declare-styleable&amp;gt;s and default styles</h2>
<p>Allowing your custom views to be styled involves using a <code>&amp;lt;declare-styleable&amp;gt;</code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">. Reusing attr names from MDC can be useful for consistency. Default styles that use <code>&amp;lt;declare-styleable&amp;gt;</code></span><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">s&nbsp; can also reference MDC theme color attrs for their values:</span></p>
<p>&lt;mio-code-snippet index=11&gt;&lt;/mio-code-snippet&gt;</p>
<h2>MaterialColors&nbsp;utility class</h2>
<p>Resolving theme color attrs programmatically can be done with a handy new MDC class &ndash; <code>MaterialColors</code>&nbsp;&ndash; which may also be useful for custom views:</p>
<p>&lt;mio-code-snippet index=12&gt;&lt;/mio-code-snippet&gt;</p>
<h2>OK Google, what&rsquo;s next?</h2>
<p>We&rsquo;ve been through the process of implementing color theming in your Android app using MDC. Be sure to check out our other posts in this series on <a href="https://medium.com/androiddevelopers/we-recommend-material-design-components-81e6d165c2dd">why we recommend using MDC</a>, <a href="https://material.io/blog/android-material-theme-type">type theming</a>, <a href="https://material.io/blog/android-material-theme-shape">shape theming</a>, <a href="https://medium.com/androiddevelopers/dark-theme-with-mdc-4c6fc357d956">dark theme</a>, and Material&rsquo;s <a href="https://material.io/blog/android-material-motion">motion system</a>.</p>
<p>As always, we encourage you to file <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=bug&amp;template=bug_report.md&amp;title=%5BComponent+name%5D+Short+description+of+issue">bug reports</a> and <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=feature+request&amp;template=feature_request.md&amp;title=%5BComponent+name%5D+Short+description+of+request">feature requests</a> on GitHub. Also be sure to check out our Android <a href="https://github.com/material-components/material-components-android-examples">companion example apps</a>.</p>
<p>If you&rsquo;ve successfully implemented color theming or if you&rsquo;re having trouble doing so, reach out to us on Twitter <a href="https://twitter.com/materialdesign">@MaterialDesign</a>.</p>

Material button transforming from baseline style to show off different options for color, shape, typography, and label

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/7afb35623021ab801b0c2a4167178a518d39c1ed27b66f3f2a9edd5b46e36128f78cef78a031f1eb870dd7b0d8e279e6943207bd1b934bf91b4964a5b241749d

https://lh3.googleusercontent.com/WSEx_H0IQA9vu59OUeW2-5rKvdBPip6FGPBQwIPFgGMnmrtAnCKG_1MILDjOzIEvUW-y9O4AwAVfx27ox-cyq2yTuMQ6P-uFwrL0ZQ

MDC color attributes with light baseline values

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/dadf560d055d6973eaeb46f1f450000fcc9ab8dab871bd037d8e41ced558c82eac1fdaf8264063c1df15f724c56a02ea11caa3f3787cc9cb222f9b5df7c48a48

https://lh3.googleusercontent.com/c6rSVlgF6wR6ziI6Xv1fkik7yJ7-P_2F7XoV9yj4gf9y8lMz0iSgKxSbO3PM7i8QqRb1ywWlzl4_5CdMgzUbTY3zkUmp0kPjwTpfDfE

MDC color attributes with dark baseline values

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f085f25687968556218f3d4472b87b70a785650d30534d9da48ebb4288af0946a28176dc87ea4a97aea40f91dcef6d5c98926289c1e597c1732c795d52ea9e0a

https://lh3.googleusercontent.com/AqxNVkIrZ5zZfOBclmWoilz62CVP3slvtf9sxXO1GorK-P4omr2w2VsiQFQqZMqAhYY3ZMzo7vArP25a4jrzcR7O5q9Yx5K33j_WFA

Button color attributes: ?attr/colorOnPrimary for + icon and button text, ?attr/textAppearanceButton for button text, ?attr/shapeAppearanceSmallComponent for button shape, ?attr/colorPrimary for background color

Color attributes used by a button

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/abaaa56de6c33d2c17ae5737d8272f56368f577a4bfc4bbdac831f893116cb4d09448f6322fde0122bf71bdca91a3d6f74e18ee3995ab40c76728466de694bc3

https://lh3.googleusercontent.com/9rKRhZ0G1kkjF4zHDhdQOEV96itrBYsek1aiudofB72zqDSLL9-AtrIWZ7_HFTmwT4t2N2l4soobdSukX1jqWfAZvkKACZNTRBCodA

Material color tool (left) and Material palette generator (right)

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/9c1b478f6d9c471ae150488ee46c297ef3b3d99f874b4d53b339fb837d4d2f14a9c0f046c7eb6580f33e4f5069243f33ecadb4c041a96d428eb23018b4a4b1f6

https://lh3.googleusercontent.com/MAmKwjV4z13vVbNGNeW3XgegBXDDAGJzC6OUDWgINp9LSKziWM90NwmzA46ox3Zd3cc7JnHaUkDzyGN_ehqFKRSjPBTtNVb8HuMaeQ

UI components changing from baseline colors to navy and dark green

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e521f768caecf6e142c0241dba890378b971bbe49a4838928241f72df29801a3d36e84ae280fd62ef3e23d074f276d41625e323fdbf44b9141fa7688bffb70f9

https://lh3.googleusercontent.com/COT53HX7UojIhPnhJQG4tnsFmooxO9OoYXP1uQmhFI1JY6wxNqyz_jVH-7FgAy3lnHJhmNOtvrEpu1r7WbxfaCI6Y9hU7lOd75pWzxM

Primary button with green background and black text. An arrow points to a secondary button with navy background and white text

Primary button (left) and secondary button (right)

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/761283c1aaf6908858433cd181fce93800f03192e6ff7a63b21f2b1aaa22a04730babda6a5de4c47da7b5b629c98673bdd23e2b50c9852709a8b64e9752cb824

https://lh3.googleusercontent.com/jjQy3wbrigJjqel0UJVAh3OcgM-MfUQ-a0H7uS1t9sI6QMeW_RI3Kp1mclZ-4m0DIywAlKNMyTkXBpNGLsdjomH8I6pnDq8G8elP7g

Changes in color values in Build a Material Theme

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d169bb0bd6b8804a284306af5ef203087dc4d0228d6fcde56946a0389bd61ae8dbc883ae1aaa1ce4a0f8428a7211bcdb11ae3c9d7d966928cca3454fdbbe03ca

https://lh3.googleusercontent.com/QMpi1rkSIWRWot0XJZhCm7DZPxur2AM9ze2vHBan0cp0ZDroAMf9mwqiBdtfRKxadWgnEj0bzI7WKAyuFGOffTY9tVQ7qTPVZQuSZ5Q

MDC button dev doc attribute table with default color values

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/16438c532bd666122d3efd8272a7adf54b31a14eff6446bfd13a750e8fb22f03304630f7f71d5e2c0713f5f929ec1b999615b4f4db709d300070713746dd08d3

https://lh3.googleusercontent.com/k4xePGofQjSnzipMkSXxc2lz6WhETD-wMhAkF7Yid__0nj7kNy4ggdzsyyLMSwANGJv1IZRMYFI1VXIEr4KuDezTY1CJOfbj84cvYQ

MDC button default style with color values

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d16ac9b027f556bdb84b6f91e7a9d8748600be561842b5aaef158209e8191fcc441518b857eab836b61e44698ef8067832b5c97a4d2fd5306ff7a0a6223a2141

https://lh3.googleusercontent.com/d5qv8fRyb6QuacMZ-3DzdnjXqOF8wgVgrDouJS5dDCyu01h3WeutmL5QlyZ86xvOr0SFY8oOADKnS5HsDE2Sp4_uKMJ6diEL10hAJQ

<!-- Copyright 2020 Google LLC.
   SPDX-License-Identifier: Apache-2.0 -->
| Color attribute | Source |
| --------------- | ------ |
| `colorPrimary` | AppCompat |
| `colorPrimaryVariant` | MDC |
| `colorOnPrimary` | MDC |
| `colorSecondary` | MDC |
| `colorSecondaryVariant` | MDC |
| `colorOnSecondary` | MDC |
| `colorSurface` | MDC |
| `colorOnSurface` | MDC |
| `android:colorBackground` | Platform |
| `colorOnBackground` | MDC |
| `colorError` | AppCompat |
| `colorOnError` | MDC |

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f5288b0f75574a9e5b50ebee234c3bf363a0a6c998bc2b53be18ed594ee6637bcf943412fa19590593244c4f8622a8ba8ce2da6ecca10b6cc89ce0ae382c7293

https://lh3.googleusercontent.com/1xWolfPsT-609CJjfZQkU0YpR69DVltAb4IL4NVbcxNKbnya_LvQmo4csc_tQjbyUBw6JKLiMX82veLqYzDq7IC06UJE48kAZBJ-HIk

Android, Material Theming, Color, How-to

{}

Learn how to create a color theme on Android using the MDC library to enhance your Android app design.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/180fce5883bbd3c7f94c105d6e6bcbbaaddad278d23ad931830e5a103c0438cf1bdd2b470b39d78219f63546d8a11bdf6d8eaa3e5bf2c9354908747fcfcdc31d

https://lh3.googleusercontent.com/pnroKYjUAhtySi6WZ_3y2JVhu_VxpLsbBHADgdUKpmccNxeTamtEBRE2AVPlSK4waYgb4Q5xbSlnJjDRLFpGzt69ziaJL_mZDiVv

Building a Material Theme on Android: Color

2020-09-01T13:07:00

android-material-theme-color

Color theming on Android using the MDC library

Building a Material Theme on Android: Color

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/71b873d3c00ebb9924495297d956b10a057a9bc599d50a0cfd141fb26afb14acc4926b20bd9b32dc491db0aed5c5270426f2c9de5d18d5c70269dca2cefb3ed1

https://lh3.googleusercontent.com/nUJTOrsF4VN5m2UMBM-J4lVD_W7wujCjUKLU8xH4wzikNlr6gdNRmga2okU7_lABELi5Ss3AjDyhSQc7Ay7vCZZ5gZahzB9Use8T3w

/blog/design-material-theme-color

Material Blog

Designing a Material Theme: Color

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/63ca609598a74ff7d698e7c18f733fd512de130ec2623ea3e2856d545833a9358ad8c9123851886ce656488ac0899ab53e302607e9e061ce78a5f6190f49c234

https://lh3.googleusercontent.com/vhqX-ByMFGwFfIGRku93SxIQqk4AAsLgDFl_yN8nRUZuZUNRx5ljltuF4CbtbAGsRuov7hxDzuV2n20i070lFbhMWiUxadGHTTE8tg

/design/color/applying-color-to-ui.html

Color

Applying color to UI

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/6f6a97a70961c27b3ce68a3d2379523ba098f177ab545e4f7f65cba84e81cbcf292ec1b2e0a4e8c7bbf6796837412c05f309f4e0d5bfeef1a961505ac73dc582

https://lh3.googleusercontent.com/32QVXJlStUJhkr7aylDQUKiIONcfRdpI_QBxa79rDTLEFTVjQCsTCn3PEKAQy0JWrtlYoJaXIa0MDggYcXI5ub4gyiz9Y56hfBOsmg

/blog/material-design-blog-welcome/

Material blog

Welcome to the Material Blog—A Letter from the Editor

mio-example
