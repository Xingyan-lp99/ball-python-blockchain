# Building a Material Theme on Android: Shape

Source: https://m3.material.io/blog/android-material-theme-shape
Content endpoint: https://m3.material.io/page-data/Posts/5703648154484736.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/18a6db2775f36a6a1b0cae6a88e8df282b27cf4a9db808be9c693fd35bdd3314798a1545d32d424a38e33f75b203165168f010c199ce63799b5e91d6309969a3

https://lh3.googleusercontent.com/m-PDSndGA4cUhtNjSl4HXPqXIaHxvYG28BPPcal5dnXUge1Po6SJJw2I3RjrIYyKBY6exL4bXnjaDt9dusnuDVO_anSC8lzVK7pCvWo

Nick Rout

Material Developer Advocate

mio-example

```java
app:shapeAppearance=”?attr/shapeAppearanceSmallComponent”
```


```xml
<style name=”Theme.MaterialComponents.*” parent=”...”>
    ...
    <item name=”shapeAppearanceMediumComponent”>
        @style/ShapeAppearance.MaterialComponents.MediumComponent
    </item>
<style />
```


```xml
<shape android:shape="rectangle">
    … 
    <corners android:radius="8dp" />
    <solid android:color="?attr/colorSurface" />
</shape>
```


```xml
<View
    …
    android:background=”@drawable/shape_background” />
```


```xml
<style name=”Widget.MaterialComponents.*” parent=”...”>
    <item name=”backgroundTint”>?attr/colorSurface</item>
    <item name="strokeColor">?attr/colorOnSurface</item>
    <item name="strokeWidth">1dp</item>
    <item name=”shapeAppearance”>?attr/shapeAppearanceLargeComponent</item>
</style>
```

```xml
<!-- In res/values/shape.xml -->
<style name="ShapeAppearance.App.SmallComponent" parent="ShapeAppearance.MaterialComponents.SmallComponent">
    <item name="cornerFamily">cut</item>
    <item name="cornerSize">4dp</item>
    ...
</style>
<style name="ShapeAppearance.App.MediumComponent" parent="ShapeAppearance.MaterialComponents.MediumComponent">
    <item name="cornerFamily">cut</item>
    <item name="cornerSize">6dp</item>
    ...
</style>
<style name="ShapeAppearance.App.LargeComponent" parent="ShapeAppearance.MaterialComponents.LargeComponent">
    <item name="cornerFamily">cut</item>
    <item name="cornerSize">0dp</item>
    ...
</style>
```

```xml
 <!-- In bottomsheet/res/values/styles.xml -->
<style name="Widget.MaterialComponents.BottomSheet" parent="...">
    ...
    <item name="shapeAppearance">?attr/shapeAppearanceLargeComponent</item>
    <item name="shapeAppearanceOverlay">@style/ShapeAppearanceOverlay.MaterialComponents.BottomSheet</item>
</selector>
<style name="ShapeAppearanceOverlay.MaterialComponents.BottomSheet" parent="">
    <item name="cornerSizeBottomRight">0dp</item>
    <item name="cornerSizeBottomLeft">0dp</item>
</style>
```

```xml
<!-- In res/values/themes.xml -->
<style name="Theme.App.Base" parent="Theme.MaterialComponents.*">
    ...
    <item name="shapeAppearanceSmallComponent">
        @style/ShapeAppearance.App.SmallComponent
    </item>
    <item name="shapeAppearanceMediumComponent">
        @style/ShapeAppearance.App.MediumComponent
    </item>
    <item name="shapeAppearanceLargeComponent">
        @style/ShapeAppearance.App.LargeComponent
    </item>
</style>
```

```
// Default constructor
val msd = MaterialShapeDrawable()
// ShapeAppearanceModel constructor
val msdFromSam = MaterialShapeDrawable(shapeAppearanceModel)
// Style/attr resources constructor (reads shapeAppearance and shapeAppearanceOverlay)
val msdFromStyles = MaterialShapeDrawable(context, attrs, defStyleAttr, defStyleRes)
// Cast from widget background
val msdFromWidget = widget.background as MaterialShapeDrawable
```

```
// Default builder
val sam = ShapeAppearanceModel.builder()
    .setAllCorners(CornerFamily.CUT, cornerSize)
    // Also setTopRightCorner, setAllEdges, etc.
    .build()
// Style/attr resources builder (reads shapeAppearance and shapeAppearanceOverlay)
val samFromStyles = ShapeAppearanceModel.builder(context, attrs, defStyleAttr, defStyleRes)
    .build()
// Build from existing ShapeAppearanceModel
val samFromExisting = sam.toBuilder()
    ...
    .build()
```

```
// Fill color
msd.setFillColor(fillColorStateList)
// Stroke color
msd.setStrokeColor(strokeColorStateList)
// Stroke width
msd.setStrokeWidth(strokeWidthDimension)
```

```
// Initialize elevation overlays
msd.initializeElevationOverlay(context)
// Pass elevation value to MSD to apply overlay (in dark theme)
msd.setElevation(elevation)
```

```
/**
 * Set shadow compat mode to be one of:
 * - SHADOW_COMPAT_MODE_DEFAULT: Use platform rendering on API 21+, else compat rendering
 * - SHADOW_COMPAT_MODE_NEVER: Use platform rendering always
 * - SHADOW_COMPAT_MODE_ALWAYS: Use compay rendering always
 */
msd.setShadowCompatibilityMode(shadowMode)
```

```
// Set corner interpolation to half of current cornerSize(s)
msd.setInterpolation(0.5f)
```

```xml
<!-- In res/values/attrs.xml -->
<declare-styleable name="AppCustomView">
    <attr name="shapeAppearance" />
    ...
</declare-styleable>

<!-- In res/values/styles.xml -->
<style name="Widget.App.CustomView" parent="android:Widget">
    <item name="android:background">@null</item>
    <item name="shapeAppearance">?attr/shapeAppearanceMediumComponent</item>
    ...
</style>
```

```
class AppCustomView ... {
  
    ...
  
    private lateinit var materialShapeDrawable: MaterialShapeDrawable
  
    override fun setElevation(elevation: Float) {
        super.setElevation(elevation)
        materialShapeDrawable.setElevation(elevation)
    }
}
```

```
<!-- Copyright 2020 Google LLC.
   SPDX-License-Identifier: Apache-2.0 -->

<!-- In res/values/shape.xml -->
<style name="ShapeAppearanceOverlay.App.Image" parent="">
    <item name="cornerSize">0dp</item>
    <item name="cornerSizeTopLeft">50%</item>
</style>

<!-- In layout -->
<com.google.android.material.imageview.ShapeableImageView
    android:layout_width="match_parent"
    android:layout_height="192dp"
    android:scaleType="centerCrop"
    app:srcCompat="@drawable/image"
    android:contentDescription="@string/content_description"
    app:shapeAppearance="?attr/shapeAppearanceMediumComponent"
    app:shapeAppearanceOverlay="@style/ShapeAppearanceOverlay.App.Image"
    app:strokeColor="?attr/colorPrimary"
    app:strokeWidth="2dp" />
```

<p dir="ltr"><a href="https://material.io/design/material-theming/overview.html#material-theming">Material Theming</a> is a way to customize <a href="https://material.io/components">Material Components</a> to align with your brand. A Material theme includes <a href="https://material.io/design/color/">color</a>, <a href="https://material.io/design/typography/">typography</a> and <a href="https://material.io/design/shape/">shape</a> parameters which you can adjust to get near-infinite variations of the components &ndash; all while maintaining their core anatomy and usability.</p>
<p dir="ltr" style="text-align: left;">&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p dir="ltr">On Android, Material Theming can be implemented using the <a href="https://github.com/material-components/material-components-android">Material Components (MDC) library</a>, from version <code>1.1.0</code>&nbsp;onwards. If you&rsquo;re looking to migrate from the Design Support Library or MDC <code>1.0.0</code>, take a look at our <a href="https://medium.com/androiddevelopers/migrating-to-material-components-for-android-ec6757795351">migration guide</a>.</p>
<p dir="ltr">This article will be focusing on <strong>shape theming</strong>.</p>
<p dir="ltr">Most widgets have a background shape, but have you ever thought about the ways that shape influences user behavior? Just like color and typography, shape can guide a user&rsquo;s attention, suggest interaction, and visually distinguish elements in your UI. Material&rsquo;s shape theming gives you the ability to define global shape values that change the style of components across your app &ndash; for example, giving all your cards, dialogs, and menus really friendly rounded corners.</p>
<h2 dir="ltr">Shape attributes</h2>
<p dir="ltr">Material Design provides 3 shape &ldquo;categories&rdquo; that are applied to the shapeable widgets of your app. Each of these have a design term (eg. &ldquo;Small components&rdquo;) along with a corresponding shape attribute that can be overridden in your app theme (eg. `<code>shapeAppearanceSmallComponent</code>`). There are default &ldquo;baseline&rdquo; values (corner size, corner family, etc.) for each category.</p>
<p dir="ltr">&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p dir="ltr">Material Components use these shape attributes to style backgrounds of the widgets.</p>
<p dir="ltr">&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p dir="ltr">They are applied with eg.</p>
<p dir="ltr">&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p dir="ltr">in layouts and widget styles.</p>
<p dir="ltr">In the MDC themes these attributes map to styles, eg.</p>
<p dir="ltr">&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p dir="ltr"><code>ShapeAppearance</code>&nbsp;styles and the corresponding attributes are new to MDC. These are discussed in more detail in the Shape resources section below.</p>
<h2 dir="ltr">Picking shape</h2>
<p dir="ltr">Figuring out which shape categories to use and the values within them may be the responsibility of a designer, or derived from your product&rsquo;s brand. However, it&rsquo;s still useful to know about the role of each category and in which scenarios they should be used:</p>
<ul>
<li dir="ltr"><p dir="ltr" role="presentation"><code>shapeAppearanceSmallComponent</code>&nbsp;is for small-size components like buttons and text fields</p></li>
<li dir="ltr"><p dir="ltr" role="presentation"><code>shapeAppearanceMediumComponent</code>&nbsp;is for medium-size components like cards and dialogs</p></li>
<li dir="ltr"><p dir="ltr" role="presentation"><code>shapeAppearanceLargeComponent</code>&nbsp;is for large-size components like bottom sheets</p></li>
</ul>
<p dir="ltr">See the <a href="https://material.io/design/shape/applying-shape-to-ui.html#shape-scheme">shape guidelines</a> for a complete list of mappings from component to shape categories.</p>
<h2 dir="ltr">Shape tool</h2>
<p dir="ltr">Material Design provides a useful <a href="https://material.io/design/shape/about-shape.html#shape-customization-tool">shape customization tool</a> for previewing shape categories and how changes apply to the corners of various components.</p>
<p dir="ltr">&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<h2 dir="ltr">Shape resources</h2>
<p dir="ltr">Shape resources consist mainly of <code>ShapeAppearance</code> styles. These are analogous to <code>TextAppearance</code>&nbsp;styles for type theming; in this case a &ldquo;style&rdquo; only concerned with shape attributes. Let&rsquo;s take a look at what&rsquo;s available on Android vs. MDC and a few things to keep in mind when declaring styles.</p>
<h2 dir="ltr">XML shapes and android:background</h2>
<p dir="ltr">Prior to MDC, you&rsquo;d typically define a custom background in the res/drawable directory, eg.</p>
<p dir="ltr">&lt;mio-code-snippet index=2&gt;&lt;/mio-code-snippet&gt;</p>
<p dir="ltr">which is applied to a widget like so:</p>
<p dir="ltr">&lt;mio-code-snippet index=3&gt;&lt;/mio-code-snippet&gt;</p>
<p dir="ltr"></p>
<p dir="ltr">This is a simplified example. XML shape drawables can include a number of other elements, like <code>&amp;lt;inset&amp;gt;</code>s, <code>&amp;lt;stroke&amp;gt;</code>s, <code>&amp;lt;gradient&amp;gt;</code>s, etc. or support multiple states.</p>
<p dir="ltr"></p>
<p dir="ltr">There are times when this approach is necessary but there are drawbacks to consider:</p>
<ul>
<li dir="ltr"><p dir="ltr" role="presentation">It lacks many of the useful features of other theming systems (like color and type); predefined attributes to specify shape at the theme level, overlays and the ability to abstract away shape values in styles</p></li>
<li dir="ltr"><p dir="ltr" role="presentation">Material Design&rsquo;s <a href="https://material.io/design/shape/about-shape.html#shaping-material">shape system</a> supports both rounded and cut corners, but there isn&rsquo;t an elegant solution to achieve cut corners in XML or programmatically</p></li>
<li dir="ltr"><p dir="ltr" role="presentation">Applying complex shape treatments, such as the top edge indent on a <a href="https://material.io/components/app-bars-bottom">bottom app bar</a>, would not be possible and would require implementing a custom <code>Drawable</code></p></li>
</ul>
<h2 dir="ltr">ShapeAppearance styles</h2>
<p dir="ltr">MDC offers a new way to define shape. <code>ShapeAppearance</code> styles can be seen as the Android equivalent of Material Design shape categories. They give you a means of defining shape characteristics without needing to deal with drawables directly. They currently only work with MDC widgets and are backed by a new <code>MaterialShapeDrawable</code>&nbsp;class, which is discussed in more detail below.</p>
<p dir="ltr">When defining your shape theme, we recommend two approaches to help separate concerns and create a single source of truth for shape theming values in your app:</p>
<ul>
<li dir="ltr"><p dir="ltr" role="presentation">Store all <code>ShapeAppearance</code>&nbsp;styles in a single res/values/shape.xml file</p></li>
<li dir="ltr"><p dir="ltr" role="presentation">Use the MDC <code>ShapeAppearance</code>&nbsp;styles as parents and adhere to the same naming convention</p></li>
</ul>
<p dir="ltr">Attributes and values you can use within these styles align with those supported by <code>MaterialShapeDrawable</code>:</p>
<ul>
<li dir="ltr"><p dir="ltr" role="presentation"><code>cornerFamily</code>&nbsp;is the family of all corners, either `rounded` or `cut`</p></li>
<li dir="ltr"><p dir="ltr" role="presentation"><code>cornerFamilyTopLeft</code>, <code>cornerFamilyTopRight</code>, <code>cornerFamilyBottomLeft</code> and <code>cornerFamilyBottomRight</code> allow you to change the family of specific corners and take precedence over <code>cornerFamily</code></p></li>
<li dir="ltr"><p dir="ltr" role="presentation"><code>cornerSize</code> is the size of all corners, typically a <code>dp</code>&nbsp;dimension</p></li>
<li dir="ltr"><p dir="ltr" role="presentation"><code>cornerSizeTopLeft</code>, <code>cornerSizeTopRight</code>, <code>cornerSizeBottomLeft</code> and <code>cornerSizeBottomRight</code>&nbsp;allow you to change the size of specific corners and take precedence over <code>cornerSize</code></p></li>
</ul>
<p dir="ltr">&lt;mio-code-snippet index=5&gt;&lt;/mio-code-snippet&gt;</p>
<h2 dir="ltr">ShapeAppearance overlays</h2>
<p dir="ltr">You can also define <code>ShapeAppearance</code>&nbsp;overlays which support all of the same attributes, and act similarly to theme overlays.</p>
<p dir="ltr">These can be applied alongside regular <code>ShapeAppearance</code> styles with <code>app:shapeAppearanceOverlay</code>&nbsp;to change the value of specific corner attributes. Here&rsquo;s an example of a bottom sheet&rsquo;s overlay, which changes the bottom corners to be flush with the screen, from the MDC source code:</p>
<p dir="ltr">&lt;mio-code-snippet index=6&gt;&lt;/mio-code-snippet&gt;</p>
<p dir="ltr"><em><strong>Note</strong>: Some MDC widgets have overlays applied by default which you may need to consider when adjusting their <code>shapeAppearance</code>. Examples of this include <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/floatingactionbutton/FloatingActionButton.java"><code>FloatingActionButton</code></a>and <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/chip/Chip.java"><code>Chip </code></a>which both set their <code>cornerSize</code>&nbsp;to 50% via an overlay.</em></p>
<h2 dir="ltr">Fill and stroke</h2>
<p dir="ltr">Unlike XML drawables, <code>ShapeAppearance</code>&nbsp;styles don&rsquo;t include any notion of fill or stroke. MDC tends to separate concerns by specifying this separately in the main widget styles:</p>
<p dir="ltr">&lt;mio-code-snippet index=4&gt;&lt;/mio-code-snippet&gt;</p>
<p dir="ltr"><em><strong>Note</strong>: <code>ShapeAppearance</code> styles and the backing <code>MaterialShapeDrawable</code> class only support solid colors for fills and strokes. There is currently no support for gradients and you would need to use XML drawables with a <code>&amp;lt;gradient&amp;gt;</code>&nbsp;in this case.</em></p>
<h2 dir="ltr">Overriding shape categories in an app theme</h2>
<p dir="ltr">Let&rsquo;s take a look at how you can add your chosen shape categories to your app theme by overriding relevant attributes.</p>
<p dir="ltr">First, we recommend setting up your theme(s) to gracefully handle light and dark color palettes while reducing repetition with base themes. For more on this topic, take a look at Chris Banes&rsquo; article on <a href="https://medium.com/androiddevelopers/dark-theme-with-mdc-4c6fc357d956">dark theme</a> as well as the <a href="https://chris.banes.dev/talks/2019/developing-themes-with-style-berlin/">"Developing Themes with Style"</a> talk given by him and Nick Butcher.</p>
<p dir="ltr">Once set up, override the shape attributes you wish to change in your base theme:</p>
<p dir="ltr">&lt;mio-code-snippet index=7&gt;&lt;/mio-code-snippet&gt;</p>
<p dir="ltr">Material Design components will respond to theme-level shape overrides:</p>
<p dir="ltr">&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<h2 dir="ltr">MaterialShapeDrawable</h2>
<p dir="ltr">Shape theming is powered by <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/shape/MaterialShapeDrawable.java"><code>MaterialShapeDrawable</code></a>. It&rsquo;s the default background drawable for all MDC widgets and handles rendering shape. Unlike other drawables, it&rsquo;s not usable in XML and needs to be handled programmatically.</p>
<p dir="ltr">&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p dir="ltr">A <code>MaterialShapeDrawable</code>&nbsp;can be instantiated like so:</p>
<p dir="ltr">&lt;mio-code-snippet index=8&gt;&lt;/mio-code-snippet&gt;</p>
<h2 dir="ltr">ShapeAppearanceModel</h2>
<p dir="ltr"><a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/shape/ShapeAppearanceModel.java"><code>ShapeAppearanceModel</code></a>is the programmatic equivalent of a `ShapeAppearance` style and stores data regarding families and sizes of shape corners and edges. <code>MaterialShapeDrawable</code>&nbsp;uses this class to render its shape.</p>
<p dir="ltr">A builder pattern is used to instantiate a <code>ShapeAppearanceModel</code>:</p>
<p dir="ltr">&lt;mio-code-snippet index=9&gt;&lt;/mio-code-snippet&gt;</p>
<p dir="ltr">For a more advanced example involving edges and custom paths, see <a href="https://github.com/material-components/material-components-android/blob/master/catalog/java/io/material/catalog/bottomappbar/BottomAppBarCutCornersTopEdge.java"><code>BottomAppBarCutCornersTopEdge</code></a> from the MDC catalog.</p>
<h2 dir="ltr">Fill and stroke</h2>
<p dir="ltr"><code>MaterialShapeDrawable</code>&nbsp;handles rendering of fill and stroke. A number of methods exist to adjust these properties:</p>
<p dir="ltr">&lt;mio-code-snippet index=10&gt;&lt;/mio-code-snippet&gt;</p>
<h2 dir="ltr">Elevation and overlays</h2>
<p dir="ltr"><code>MaterialShapeDrawable</code>&nbsp;is responsible for rendering overlays to convey elevation in a dark theme. MDC widgets handle this by default. Here&rsquo;s how this functionality is enabled and used:</p>
<p dir="ltr">&lt;mio-code-snippet index=11&gt;&lt;/mio-code-snippet&gt;</p>
<p dir="ltr">Take a look at the <a href="https://material.io/blog/android-material-theme-color">color theming</a> article as well as Chris Banes&rsquo; article on <a href="https://medium.com/androiddevelopers/dark-theme-with-mdc-4c6fc357d956">dark theme</a> for more information.</p>
<h2 dir="ltr">Shadow rendering</h2>
<p dir="ltr">Elevation shadow rendering by the platform is only supported from API 21 onwards. <code>MaterialShapeDrawable</code>&nbsp;offers optional support to backport shadow rendering:</p>
<p dir="ltr">&lt;mio-code-snippet index=12&gt;&lt;/mio-code-snippet&gt;</p>
<h2 dir="ltr">Corner interpolation</h2>
<p dir="ltr"><code>MaterialShapeDrawable</code>&nbsp;offers methods to interpolate the sizes of all corners. This is a [0.0, 1.0] multiplier on the set corner sizes and can be useful for animations and transitions.</p>
<p dir="ltr">&lt;mio-code-snippet index=13&gt;&lt;/mio-code-snippet&gt;</p>
<h2 dir="ltr">ShapeableImageView</h2>
<p>Applying path clips to images is a common use case (eg. Circular avatars). To solve this MDC has a handy class called <code>ShapeableImageView</code>. As the name suggests this is an extension of <code>AppCompatImageView</code> that understands shape theming. It leverages familiar concepts&mdash;<code>ShapeableImageView</code> can read <code>shapeAppearance</code> and <code>shapeAppearanceOverlay</code>, and even supports attributes for applying strokes.</p>
<p>&lt;mio-code-snippet index=16&gt;&lt;/mio-code-snippet&gt;</p>
<h2 dir="ltr">Shape in MDC widgets</h2>
<p dir="ltr">Earlier we said that MDC widgets respond to overrides of theme level shape attributes. But how would you know, for example, that a button uses <code>shapeAppearanceSmallComponent</code>&nbsp;as the style for its container? Let&rsquo;s take a look at a few options.</p>
<h2 dir="ltr">MDC developer docs</h2>
<p dir="ltr">The MDC developer docs have recently been refreshed. As part of this we&rsquo;ve included attribute tables which include design terminology and default values used in the library. For example, check out the &ldquo;Anatomy and key properties&rdquo; sections of the updated <a href="https://material.io/develop/android/components/buttons/#contained-button">buttons doc</a>.</p>
<p dir="ltr">&lt;mio-image index=7&gt;&lt;/mio-image&gt;</p>
<h2 dir="ltr">Source code</h2>
<p dir="ltr">Inspecting the MDC source code is arguably the most reliable approach. MDC uses default styles to achieve Material Theming so it&rsquo;s a good idea to look at these as well as any styleable attrs and the java file(s). For example, check out the <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/res/values/styles.xml">styles</a>, <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/res/values/attrs.xml">attrs</a> and <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/MaterialButton.java">java file</a> for `MaterialButton`.</p>
<p dir="ltr">An interesting observation is how MDC widgets use default styles to ensure <code>MaterialShapeDrawable</code>&nbsp;is the default background. The general approach is:</p>
<ul>
<li dir="ltr"><p dir="ltr" role="presentation">Set <code>android:background</code>&nbsp;to <code>@null</code> or <code>@empty</code> in the widget default style</p></li>
<li dir="ltr"><p dir="ltr" role="presentation">If no background is detected when parsing attributes, instantiate a <code>MaterialShapeDrawable</code>&nbsp;programmatically and set this as the background</p></li>
<li dir="ltr"><p dir="ltr" role="presentation">If a background has been set (eg. in a layout or custom style) then respect this and do not use <code>MaterialShapeDrawable</code></p></li>
</ul>
<p dir="ltr">&lt;mio-image index=8&gt;&lt;/mio-image&gt;</p>
<h2 dir="ltr">Shape in custom views</h2>
<p dir="ltr">Your app may include custom widgets you&rsquo;ve built or gotten from an existing library. Making these views responsive to Material Theming is useful when using them alongside standard MDC widgets. Let&rsquo;s take a look at what to keep in mind when supporting shape theming for custom widgets.</p>
<h2 dir="ltr">Use MDC attrs in &amp;lt;declare-styleable&amp;gt;s and default styles</h2>
<p dir="ltr">Allowing your custom views to be styled involves using a <code>&amp;lt;declare-styleable&amp;gt;</code>. Reusing attr names from MDC can be useful for consistency. Default styles that use <code>&amp;lt;declare-styleable&amp;gt;</code>s&nbsp; can also reference MDC theme shape attrs for their values while also using the <code>@null</code>/<code>@empty</code> approach for <code>MaterialShapeDrawable</code> backgrounds:</p>
<p dir="ltr">&lt;mio-code-snippet index=14&gt;&lt;/mio-code-snippet&gt;</p>
<h2 dir="ltr">Keep elevation and overlays in mind</h2>
<p dir="ltr">If you want your custom view to support elevation overlays or backported shadow rendering, it&rsquo;s a good idea to override the <code>setElevation</code>&nbsp;method and pass the value to the <code>MaterialShapeDrawable</code> background:</p>
<p dir="ltr">&lt;mio-code-snippet index=15&gt;&lt;/mio-code-snippet&gt;</p>
<h2 dir="ltr">OK Google, what&rsquo;s next?</h2>
<p dir="ltr">We&rsquo;ve been through the process of implementing color theming in your Android app using MDC. Be sure to check out our other posts in this series on <a href="https://medium.com/androiddevelopers/we-recommend-material-design-components-81e6d165c2dd">why we recommend using MDC</a>, <a href="https://material.io/blog/android-material-theme-color">color theming</a>, <a href="https://material.io/blog/android-material-theme-type">type theming</a>, <a href="https://medium.com/androiddevelopers/dark-theme-with-mdc-4c6fc357d956">dark theme</a>, and Material's <a href="https://material.io/blog/android-material-motion">motion system</a>.</p>
<p dir="ltr">As always, we encourage you to file <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=bug&amp;template=bug_report.md&amp;title=%5BComponent+name%5D+Short+description+of+issue">bug reports</a> and <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=feature+request&amp;template=feature_request.md&amp;title=%5BComponent+name%5D+Short+description+of+request">feature requests</a> on GitHub. Also be sure to check out our Android <a href="https://github.com/material-components/material-components-android-examples">companion example apps</a>.</p>
<p dir="ltr"></p>
<hr />
<p></p>
<p dir="ltr">If you&rsquo;ve successfully implemented shape theming or if you&rsquo;re having trouble doing so, leave a comment below or reach out to us on Twitter <a href="https://twitter.com/materialdesign">@MaterialDesign</a> and <a href="https://twitter.com/AndroidDev">@AndroidDev</a>.</p>

Material button transforming from baseline style to show off different options for color, shape, typography, and label

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6af83f923d6d02f7e7b7509a1551fd72196bca77536aec1e71c7d9a46f132a92d7fa000b5a84348ab02f05d419098a7b8bfa920aa92d9657098eb91baea028ea

https://lh3.googleusercontent.com/VCtdEjXvwAg3Gdgje_AEvZEfwaB6__Cwq5ZeTrVV6DJJzo1SCEWDOZXLjYqkCXa7bZzdE4qtprD4x6pt6VQJAJX3-hFYsMXSGm2LoA

ShapeAppearanceSmallComponent with rounded, 4 dp corners. ShapeAppearanceMediumComponent with rounded, 4 dp corners. ShapeAppearanceLargeComponent with rounded, 0 dp corners.

MDC shape attributes with baseline values

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/9c62941f3b5d0f829fdcaaa91f2a231a550e50bb8bbeb63822cec28d9c37985c00a4b0dad91dd16f7ab048d6ecf63521f48a9bb6558e51b75ce1ac8f23ccde55

https://lh3.googleusercontent.com/GaJLAG38YYsUT05HM9DWhFl06KQcKOHQ5g-eQ0wQpNqVGtF7FrePVUOHxwn2cTTEntTMqT2hJnP6IxP8B4CjmmoaWxAwzhFeAu2RbQ

Button color attributes: ?attr/colorOnPrimary for + icon and button text, ?attr/textAppearanceButton for button text, ?attr/shapeAppearanceSmallComponent for button shape, ?attr/colorPrimary for background color

Shape attributes used by a button

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/3ba73146a328d2d5425dd32def476040bda05b541409ad27e2e3cadfc6d26b751ea378fb55996173e5d1ab8623299a2d0bffa0446dc27571becb681678e1af48

https://lh3.googleusercontent.com/tfDkjI_T9f9pqZCE96_A_94k5vvogrG6FKM-If4UIRDiehK5iMd7X0a1D5eHQPHthjr28AwPX5d2yhQkHtran3othj3S3lSYxeZXog

Shape customization tool

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/433304db9129f24c6df0ff58da48135eb34e0a75a5d617bbf5cdfcdfac1b532b117f4f11f9cc652059f9c2330cbefc97e11c7acb248819fbbd1d09242d252999

https://lh3.googleusercontent.com/yaLZ_6n-zgJcQNo4HTlO6GQLqO1CtdzLXpBEnw2zrKjvdT__Oa2b0MNCk5MUFhsjYW9gbRC2NVnacmgrCtjl1hU_SLumbagRD6XPQg

UI components changing from baseline shape to cornerFamily=cut, with corner sizes 8 dp, 12 dp, 16 dp.

Material Design components responding to theme-level shape overrides

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/df0ae72e6574613d471cb235616d571dc19e1d61ff60b2694be7545a9cc301ce0b97982fdc085d121fea9d03e8f5c8c6fc1099d97dc70b3fdc8c1bdb2e2f6e72

https://lh3.googleusercontent.com/gnKKrcjEX9IBXFAMTn_9YMa-ECxn3FBHsw__UTqAowjlttLEBwY9kRp0eizEyiunRs12IzywO6u69zRa_qvZXgam8p-HMnDTW3hmJw

MaterialShapeDrawable and ShapeAppearanceModel visualized

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/1ed6b4c5f2a07c6ffdcbd934b1ad0b04e17c8ca079d22cdcf492ac1acd8be46136f93a4690ddd92b060fb2054c6746296fcd638f096407920330e212b282d7ae

https://lh3.googleusercontent.com/27Uy-sb7tyds8kgaooepHk1KcwizdC-UYZLqW_MqkYFjOFG4_Ijiymvyz-TsU33b1Ccw8_AbXSUaujrT9K5FRKK2iz5fqcyvn9Vj

Changes in shape values in Build a Material Theme

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/03ee29af84e19123fe2e45b533b9b7c4683bfea3df2dc8115928a0d2e98a43eb1cce65a3a74773096ba6c654c8ffe8f90f6a546937dcbc333e67bd64f8a8948c

https://lh3.googleusercontent.com/x-AU4n3Jc1XTZvoFX1swfk_xCLlRrDN-GH5eSUfBAWcg6MsGN0huvG4a04ZZpqLwvdWjNOzA1EwoP7yTvau7B5B1WmkF2I8gjjg8oQ

MDC button dev doc attribute table with default shape values

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6486e3d9659c9f5f09afbfb6556ac14ed50b629a03e924c0927d49ea33c4aeb4c3858d1ff668d31919ba557204844ce15e1f7729ac32bd05470f3ea36047d406

https://lh3.googleusercontent.com/Y9sF_I0nve-cuSFQ4DHPuJXZG994yrDDg-Aea8E7HmHqIYr7PJLpDe9cvpaWLBYl1TzYeHRkYD-kLb81ET0krvUwjsWGLwbN2mVdKw

MDC button default style with shape values

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/ef614a0c45f99991aa8c1be2a0e31ca912938837b79733377dbf2de878c40ed385a3766a403fbebdb0a94200ef458195d143d006dbc1ecb98aa3b3f7d29284c6

https://lh3.googleusercontent.com/mNnyGGni-I24PhbGl5XH6VLYRlaPlIUDAPULyRcSRdVQkMJbbe_QHvGm-MCfPF1r--qOSwRsyrab91FCqJ0qwZhiQw5vU8J3ETV4WBg

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/dde22909c7ab4c4d906d587ebea9765a3151ee519b7ab8708ac8743ba5018e9ccf398ecaf0e018891fba88ec100934d145717202273cc8e710df60496c33adcb

https://lh3.googleusercontent.com/xDCjGLXfjLAHyaA1ZYQrDNPUm8P6zVsK4Zk6AFDzxpnKe10X-FrECxi10pB3hTWxzl-pyJ8SY3ZBreGZpD3lhHBWK-mrFL5H_FH2zg

Android, Material Theming, Shape, How-to

{}

Learn how to create a beautiful Android Material Theme Shape with M3. Shape theming on Android using the MDC library.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f2bcbc36a256b30693e40c2aae501d000a8247fa4e61bf133240d01156718617eadc7f5ff3e0ee6227fcd4a755fc83af771d7f94be20d1756452ab1d58b96a67

https://lh3.googleusercontent.com/T1TXVVZ3L3C8OE_eqUjG0roGWJ5a_n0Us90_oPKg_dzkuJGVLQvFOEOcCxUpN_JVhqwpHOmamkXnT8eb96NCNA3LRHmOcCt8OiYDZQ

Building a Material Theme on Android: Shape

2020-09-01T13:03:00

android-material-theme-shape

Shape theming on Android using the MDC library

Building a Material Theme on Android: Shape

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/81e02b0999c78b0a285af267b6a8952596e3dc56bd599065f68a24575c2606e3b5a8f447ef22b4ea49a4c2f5b7ed37e61e5c3ef183fe971d7ad3e299006dd22c

https://lh3.googleusercontent.com/dyFlUcqekPdNBSw6XHAC_jyCd36hCtiWsMuJY4uNid7SpBTr7Wx4gQFP2c5C7A5uGfElGfRYSKJ_8FvYKG22JhPIiTYfCuBg6dN4

/blog/design-material-theme-shape

Material Blog

Designing a Material Theme: Shape

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/61721ca9c7dba79a0edc8fa874afc4b83f0bfcb878fa513fb3841e8eb0e9a3c4abb0774c0699bbec1b6a4545b900bb207bea8be55168efd9be21965253107cfb

https://lh3.googleusercontent.com/5Kk4oIGKBCYRZ5FcDwnv2inn-RtHo94IaVk7FzGUU0e9BqGP2WTHXKhCY6NZ7V4x6hD24bFKFzWnMxl7hYllcEO2MdQhKt1JjfLOEw

/design/shape/about-shape.html

Shape

About shape

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/6f6a97a70961c27b3ce68a3d2379523ba098f177ab545e4f7f65cba84e81cbcf292ec1b2e0a4e8c7bbf6796837412c05f309f4e0d5bfeef1a961505ac73dc582

https://lh3.googleusercontent.com/32QVXJlStUJhkr7aylDQUKiIONcfRdpI_QBxa79rDTLEFTVjQCsTCn3PEKAQy0JWrtlYoJaXIa0MDggYcXI5ub4gyiz9Y56hfBOsmg

/blog/material-design-blog-welcome/

Material blog

Welcome to the Material Blog—A Letter from the Editor

mio-example
