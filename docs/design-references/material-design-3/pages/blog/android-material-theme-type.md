# Building a Material Theme on Android: Typography

Source: https://m3.material.io/blog/android-material-theme-type
Content endpoint: https://m3.material.io/page-data/Posts/5312679798112256.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/18a6db2775f36a6a1b0cae6a88e8df282b27cf4a9db808be9c693fd35bdd3314798a1545d32d424a38e33f75b203165168f010c199ce63799b5e91d6309969a3

https://lh3.googleusercontent.com/m-PDSndGA4cUhtNjSl4HXPqXIaHxvYG28BPPcal5dnXUge1Po6SJJw2I3RjrIYyKBY6exL4bXnjaDt9dusnuDVO_anSC8lzVK7pCvWo

Nick Rout

Material Developer Advocate

mio-example

```
android:textAppearance=”?attr/textAppearanceBody1”
```

```
<style name=”Theme.MaterialComponents.*” parent=”...”>
    ...
    <item name=”textAppearanceBody1”>
        @style/TextAppearance.MaterialComponents.Body1
    </item>
<style />
```

```xml
<!-- In res/values/type.xml -->
<style name="TextAppearance.App.Headline6" parent="TextAppearance.MaterialComponents.Headline6">
    <item name="fontFamily">@font/roboto_mono</item>
    ...
</style>
<style name="TextAppearance.App.Body2" parent="TextAppearance.MaterialComponents.Body2">
    <item name="fontFamily">@font/roboto_mono</item>
    <item name="android:textSize">14sp</item>
    ...
</style>
<style name="TextAppearance.App.Button" parent="TextAppearance.MaterialComponents.Button">
    <item name="fontFamily">@font/roboto_mono</item>
    <item name="android:textAllCaps">false</item>
    ...
</style>
```

```xml
<!-- (0.25 tracking / 14sp font size) = 0.0178571429 em -->
<style name="TextAppearance.App.Body2" parent="TextAppearance.MaterialComponents.Body2">
    <item name="fontFamily">@font/roboto_mono</item>
    <item name="android:textSize">14sp</item>
+    <item name="android:letterSpacing">0.0178571429</item>
    ...
</style>
```

```
<style name=”Widget.MaterialComponents.*” parent=”...”>
 ...
 <item name=”android:textColor”>?attr/colorOnSurface</item>
 <item name=”android:textAppearance”>?attr/textAppearanceBody1</item>
</style>
```

```xml
<!-- In res/values/attrs.xml -->
<attr name="textAppearanceCustom" format="reference" />

<!-- In res/values/type.xml -->
<style name="TextAppearance.App.Custom" parent="TextAppearance.MaterialComponents.*">
    ...
</style>

<!-- In res/values/themes.xml -->
<style name="Theme.App" parent="Theme.MaterialComponents.*">
    ...
    <item name="textAppearanceCustom">@style/TextAppearance.App.Custom</item>
</style>
```

```xml
<!-- In res/values/themes.xml -->
<style name="Theme.App.Base" parent="Theme.MaterialComponents.*">
    ...
    <item name="textAppearanceHeadline6">
        @style/TextAppearance.App.Headline6
    </item>
    <item name="textAppearanceBody2">
        @style/TextAppearance.App.Body2
    </item>
    <item name="textAppearanceButton">
        @style/TextAppearance.App.Button
    </item>
    <!-- Using default values for textAppearanceSubtitle1, textAppearanceCaption, etc. -->
```
</style>

```xml
<!-- In res/values/attrs.xml -->
<declare-styleable name="AppCustomView">
    <attr name="titleTextAppearance" />
    <attr name="subtitleTextAppearance" />
    ...
</declare-styleable>

<!-- In res/values/styles.xml -->
<style name="Widget.App.CustomView" parent="android:Widget">
    <item name="titleTextAppearance">?attr/textAppearanceHeadline6</item>
    <item name="subtitleTextAppearance">?attr/textAppearanceBody2</item>
    ...
</style>
```

<p><a href="https://material.io/design/material-theming/overview.html#material-theming">Material Theming</a> is a way to customize <a href="https://material.io/components">Material Components</a> to align with your brand. A Material theme includes <a href="https://material.io/design/color/">color</a>, <a href="https://material.io/design/typography/">typography</a> and <a href="https://material.io/design/shape/">shape</a> parameters which you can adjust to get near-infinite variations of the components &ndash; all while maintaining their core anatomy and usability.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>On Android, Material Theming can be implemented using the <a href="https://github.com/material-components/material-components-android">Material Components (MDC) library</a>, from version <code>1.0.0</code> onwards. If you&rsquo;re looking to migrate from the Design Support Library or MDC <code>1.0.0</code>, take a look at <a href="https://medium.com/androiddevelopers/migrating-to-material-components-for-android-ec6757795351">our migration guide</a>.</p>
<p>This article will be focusing on <strong>type</strong> theming.</p>
<h2>Type attributes</h2>
<p>Material Design provides 13 type &ldquo;styles&rdquo; that are applied to all the text in your app. Each of these have a design term (eg. &ldquo;Body 1&rdquo;) along with a corresponding type attribute that can be overridden in your app theme (eg. <code>textAppearanceBody1</code>). There are default &ldquo;baseline&rdquo; values (text size, letter spacing, capitalization, etc.) for each style.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>Material Components use these type attributes to style textual elements of the widgets (those parts that subclass or comprise one or more <code>TextView</code>s).</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>They are applied&nbsp;<span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">in layouts and widget styles like this, for example:</span></p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p>Take a look at Nick Butcher&rsquo;s &ldquo;<a href="https://medium.com/androiddevelopers/whats-your-text-s-appearance-f3a1729192d">What&rsquo;s your text&rsquo;s appearance?</a>&rdquo; article for more information on using this and the order of precedence with other styling techniques.</p>
<p>In the MDC themes these attributes map to styles, eg.</p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p>You might recognize <code>TextAppearance</code>&nbsp;styles from AppCompat or the platform and these are discussed in more detail in the <strong>Type resources</strong> section below. The corresponding attributes are new to MDC and give you the ability to vary typography by theme.</p>
<h2>Picking type</h2>
<p>Figuring out which type styles to use and the values within them may be the responsibility of a designer, or derived from your product&rsquo;s brand. However, it&rsquo;s still useful to know about the role of each style and in which scenarios they should be used:</p>
<ul>
<li><code>textAppearanceHeadline*</code>&nbsp;styles are for headings</li>
<li><code>textAppearanceSubtitle*</code> styles are for subheadings</li>
<li><code>textAppearanceBody*</code> styles are for multiline body text</li>
<li><code>textAppearanceButton</code>&nbsp;is for buttons but also maps to parts of other components like tabs and dialog actions</li>
<li><code>textAppearanceCaption</code>&nbsp;is for smaller text like text field hints and errors</li>
<li><code>textAppearanceOverline</code> is also for smaller text but capitalization and increased letter spacing make it suitable for small titles and labels like date picker headers</li>
</ul>
<h2>Type tool</h2>
<p>Material Design provides a useful tool for previewing type scales, integrating with <a href="https://fonts.google.com/">Google Fonts</a> and exporting code. See "Type scale generator" in the <a href="https://material.io/design/typography/the-type-system.html#type-scale">Material Design type scale guidelines</a>.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<h2>Type resources</h2>
<p>Type resources consist of fonts as well as <code>TextAppearance</code> styles. Let&rsquo;s take a look at what&rsquo;s available on Android and a few things to keep in mind when declaring styles.</p>
<p><strong>XML and downloadable fonts</strong></p>
<p>Fonts are stored in the res/font directory and referenced with <code>@font/</code>&nbsp;notation. You can use either local XML fonts or downloadable fonts. Android Studio offers a built-in wizard to get you started with downloadable fonts including the necessary certificates and manifest metadata. You may also want to check out &ldquo;<a href="https://medium.com/google-design/the-android-developers-guide-to-better-typography-97e11bb0e261">The Android Developer&rsquo;s Guide to Better Typography</a>&rdquo; by Rod Sheeter for a more detailed guide and further optimizations to font preloading.</p>
<p>In general we recommend using downloadable fonts as they reduce the size of your app bundle by leveraging the shared font provider cache. However, downloadable fonts currently only work with those available on Google Fonts. If your app requires a purchased or proprietary font, use XML fonts.</p>
<p>It&rsquo;s also worth mentioning that variable fonts are supported on Android from API 26 onwards. Take a look at Rebbeca Franks&rsquo; &ldquo;<a href="https://medium.com/over-engineering/variable-fonts-in-android-p-c5c918275646">Variable Fonts in Android O 🖍</a>&rdquo; article for more information.</p>
<h2>TextAppearance styles</h2>
<p><code>TextAppearance</code>&nbsp;styles can be seen as the Android equivalent of Material Design type styles. For custom styles, we recommend two approaches to help separate concerns and create a single source of truth for type theming values in your app:</p>
<ul>
<li>Store all <code>TextAppearance</code>&nbsp;styles in a single res/values/type.xml file</li>
<li>Use the MDC <code>TextAppearance</code> styles as parents and adhere to the same naming convention</li>
</ul>
<p>Attributes and values you can use within these styles align with those supported by <code>TextView</code>:</p>
<ul>
<li><code>fontFamily</code> is the font family, typically an <code>@font/</code>&nbsp;resource referring to an XML or downloadable font</li>
<li><code>android:textSize</code>&nbsp;is the size of the text, typically an <code>sp</code>&nbsp;dimension</li>
<li><code>android:textColor</code>&nbsp;is the color of text</li>
<li><code>android:letterSpacing</code>&nbsp;is the spacing between characters</li>
<li><code>android:textAllCaps</code>&nbsp;is a boolean to toggle text capitalization</li>
<li><code>android:textFontWeight</code>&nbsp;is the weight of the font, used to select the closest match from a font family, but is only available on API 28 and above. <code>android:textStyle</code>&nbsp;can also be used to apply transformations such as <code>bold</code>&nbsp;and <code>italic</code>.</li>
</ul>
<p>&lt;mio-code-snippet index=2&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Calculating letterSpacing</h2>
<p>Letter spacing values on Android tend to use a different unit of measurement (em) to those used in design tools like Sketch (tracking). The <a href="https://material.io/design/typography/the-type-system.html#type-scale">Material Design typography guidelines</a> provide a relatively simple equation for determining suitable em values from tracking values:</p>
<p><strong>(Tracking from Sketch / font size in sp) = letter spacing</strong></p>
<p>&lt;mio-code-snippet index=3&gt;&lt;/mio-code-snippet&gt;</p>
<h2>MaterialTextView and lineHeight</h2>
<p>The platform <code>TextView</code> added support for the <code>android:lineHeight</code>&nbsp;attribute in API 28. MDC provides backported support for this via the <code>MaterialTextView</code>&nbsp;class. You don&rsquo;t need to use this class directly in layouts as <code>&amp;lt;TextView&amp;gt;</code>s will get auto-inflated as <code>MaterialTextView</code>s by <code>MaterialComponentsViewInflater</code>.</p>
<p>You can use <code>lineHeight</code>&nbsp;in various scenarios:</p>
<ul>
<li>Included as an item in <code>TextAppearance</code>&nbsp;styles (applied with <code>android:textAppearance="..."</code>)</li>
<li>Included as an item in widget styles with parent <code>Widget.MaterialComponents.TextView</code> (applied with <code>style=&rdquo;...&rdquo;</code>)</li>
<li>Applied directly to <code>&amp;lt;Texview&amp;gt;</code>s in layouts</li>
</ul>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<h2>Things to consider</h2>
<ul>
<li>You don&rsquo;t have to override all type styles. However, bear in mind that default MDC styles use the system font (typically Roboto). Be sure to check which type styles your widgets and <code>TextView</code>s are using.</li>
<li>While <code>TextAppearance</code> does support <code>android:textColor</code>, MDC tends to separate concerns by specifying this separately in the main widget styles:</li>
</ul>
<p>&lt;mio-code-snippet index=4&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Additional type styles</h2>
<p>Your design system may call for additional type styles outside of the 13 that Material Theming specifies. Thankfully this is relatively easy to do on Android by declaring a type attr:</p>
<p>&lt;mio-code-snippet index=5&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Overriding type styles in an app theme</h2>
<p>Let&rsquo;s take a look at how you can add your chosen type styles to your app theme by overriding relevant attributes.</p>
<p>First, we recommend setting up your theme(s) to gracefully handle light and dark color palettes while reducing repetition with base themes. For more on this topic, take a look at Chris Banes&rsquo; article on <a href="https://medium.com/androiddevelopers/dark-theme-with-mdc-4c6fc357d956">dark theme</a> as well as the "<a href="https://chris.banes.dev/talks/2019/developing-themes-with-style-berlin/">Developing Themes with Style</a>" talk given by him and Nick Butcher.</p>
<p>Once set up, override the type attributes you wish to change in your base theme:</p>
<p>&lt;mio-code-snippet index=6&gt;&lt;/mio-code-snippet&gt;</p>
<p>Material Components will respond to theme-level type overrides:</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<h2>Type in MDC widgets</h2>
<p>Earlier we said that MDC widgets respond to overrides of theme level type attributes. But how would you know, for example, that a button uses <code>textAppearanceButton</code>&nbsp;as the style for its text label? Let&rsquo;s take a look at a few options.</p>
<h2>MDC developer docs</h2>
<p>The MDC developer docs have recently been refreshed. As part of this we&rsquo;ve included attribute tables which include design terminology and default values used in the library. For example, check out the &ldquo;Anatomy and key properties&rdquo; sections of the updated <a href="https://material.io/develop/android/components/buttons/#contained-button">buttons doc</a>.</p>
<p>&lt;mio-image index=7&gt;&lt;/mio-image&gt;</p>
<h2>Source code</h2>
<p>Inspecting the MDC source code is arguably the most reliable approach. MDC uses default styles to achieve Material Theming so it&rsquo;s a good idea to look at these as well as any styleable attrs and the java file(s). For example, check out the <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/res/values/styles.xml">styles</a>, <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/res/values/attrs.xml">attrs</a> and <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/MaterialButton.java">java file</a> for <code>MaterialButton</code>.</p>
<p>&lt;mio-image index=8&gt;&lt;/mio-image&gt;</p>
<h2>Type in custom views</h2>
<p>Your app may include custom widgets you&rsquo;ve built or gotten from an existing library. Making these views responsive to Material Theming is useful when using them alongside standard MDC widgets. Let&rsquo;s take a look at what to keep in mind when supporting type theming for custom widgets.</p>
<h2>Use MDC attrs declare-styleables and default styles</h2>
<p>Allowing your custom views to be styled involves using a <code>&amp;lt;declare-styleable&amp;gt;</code>. Reusing attr names from MDC can be useful for consistency. Default styles that use <code>&amp;lt;declare-styleable&amp;gt;</code>s&nbsp; can also reference MDC theme type attrs for their values:</p>
<p>&lt;mio-code-snippet index=7&gt;&lt;/mio-code-snippet&gt;</p>
<h2>OK Google, what&rsquo;s next?</h2>
<p>We&rsquo;ve been through the process of implementing color theming in your Android app using MDC. Be sure to check out our other posts in this series on <a href="https://medium.com/androiddevelopers/we-recommend-material-design-components-81e6d165c2dd">why we recommend using MDC</a>, <a href="https://material.io/blog/android-material-theme-color">color theming</a>, <a href="https://material.io/blog/android-material-theme-shape">shape theming</a>, <a href="https://medium.com/androiddevelopers/dark-theme-with-mdc-4c6fc357d956">dark theme</a>, and Material's <a href="https://material.io/blog/android-material-motion">motion system</a>.</p>
<p>As always, we encourage you to file <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=bug&amp;template=bug_report.md&amp;title=%5BComponent+name%5D+Short+description+of+issue">bug reports</a> and <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=feature+request&amp;template=feature_request.md&amp;title=%5BComponent+name%5D+Short+description+of+request">feature requests</a> on GitHub. Also be sure to check out our <a href="https://github.com/material-components/material-components-android-examples">Android companion example apps</a>.</p>
<p>If you&rsquo;ve successfully implemented type theming or if you&rsquo;re having trouble doing so, reach out to us on Twitter <a href="https://twitter.com/materialdesign">@MaterialDesign</a>.</p>

Material button transforming from baseline style to show off different options for color, shape, typography, and label

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/8be25756e6357202f1c5447605da52a2fb22066aaab36e3dabb551c18efe76021eb6b6a4d6bdd94eabe87e6febf453f0360653ed348bf4eff492a885bf895388

https://lh3.googleusercontent.com/U91QcPXwd4vZy5mqgfKRmrq0glL82XeN-xPOqUzo_kbALtFkQpGoqh8eWUwNx3Injktu5M9NwBQwSOICAmGRthgvD7s0oeky9CniMQ

MDC type attributes with examples from different text sizes

MDC type attributes with baseline styling

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/12bfe63b54d5349a5188d9386d61a82dc0cb5f651c98a72f5af652b0abc82ca2c983331a3be8207d36d54924f4f548c3df9c78484d9f5b24e7e052719871a233

https://lh3.googleusercontent.com/rnDV8xpr0i6fN_tEZTR-mrZij-SYvqglfBhyrsyjgbfs5VZmxkf0LM1CGH6dUSZ_ecmMHYSp8Wp5A-YnVgoa3kLhS3kKvUcSbInN

Button color attributes: ?attr/colorOnPrimary for + icon and button text, ?attr/textAppearanceButton for button text, ?attr/shapeAppearanceSmallComponent for button shape, ?attr/colorPrimary for background color

Type attributes used by a button

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/aea9518cc2614a8784a02277f3f37ef41394c159cc845ea190371ffb09c51c29604eb3a2e058f00072f55df145bb9fc16bd54a523d5e88f6aca2976c6fbcc8b6

https://lh3.googleusercontent.com/9kGrGMUJPNYUO8H0bYGNE64YuP_GQSKBCV7bcjq8EfWjLhrGoY3-CeeGU-JNKpEOLG2tZOS4b0BDiAUMB9M0e2zPhZo9SGq8wxs72w

Google Fonts (left) and Type scale generator (right)

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f0f9afa5e15d33566457d378fd9ce50b12e765e6a8645f493b4ba59c3d96865f4d1af59bc905e68ea7bfdba26e217f5c987161a1e1e9dc6a9594a621f83066a2

https://lh3.googleusercontent.com/jZcVyxHpKXR6YpDok5dfjDmUDKr9PCq5eWoCQTXL6NpLbW7oXTJflgQHukq-e9Gt9dTEhjVX8pKbkQ4Fi22kGMxGFdlQ3Qrusk6v4zo

Different lineHeight values

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e310aa2567eaa96fd3fec7bb23669ae03448e64a1bdec5dcab0ddcab95c1262b7a1db6e78e2faf09bad8845f1bab1391e97edcf5e84d464cf711cb23c2eaef56

https://lh3.googleusercontent.com/XEbUmo28RCg7uD9xGXDBfRhYmnLmuXsr3JOhaNnFM2D3aAWSWgZhxiwWyZk7OGGKP16_QHes75C7v5jm4j29nh2AgMaSfPf6zRwI

UI components changing from baseline typography to fontFamily=roboto_mono and textAppearanceButton. textAllCaps=false.

Material Design components responding to theme-level type overrides

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d7e778e15507fe4e618e83630fc710af53f4c093b99f2b818370757ab700388d2e03fce80f2d0ce94c230af205d1d7b8c9001ec0e1b99b3bf6b57a93f314bf3e

https://lh3.googleusercontent.com/gVJklJ4z31ZhHhSoM2v4Ygzn9UZ1U3HPagBbdc1qMqV5XFI06PGjWsFoliXLFHS-3pPffwIT1utpJx0BglyjnAKfoizzO4q4yJ517A

Changes in type values in Build a Material Theme

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/a1fe2dd2e295682f7e40be97cc803f52a231240e1b0f01a1e691ea4f6eab6b31b07d2c2e5b8abda5e9811e79a35c17132b339b227440d5181eb48c5c2b8bd8c7

https://lh3.googleusercontent.com/d1bK_8Gu3VJuFJmxv7W4Qn_5SqNVrLwnqLvUn0wuPo-dP5GXIrXFmv7EEToWFMVJeUSka0QkaRqpjMyhZDyiKnvIHmgKRxDmrWO7

MDC button dev doc attribute table with default type values

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/5eb1171c20882698f7a8c75a8ddd0d2951f3f09f973496f64e16c12f2df65a14644f168ae4931e978713c47f609e2ac47cbd0e750e86a313fdd6521362f6f9bb

https://lh3.googleusercontent.com/vnGxmsUU83cC-oODzqEnx0zUmYUyJGugivWuMRZ-qrrtBZJB9jzc687Ghgj4Jdqzj0M4P-7KbDZ0Uq-_uikZ4x5H1jJXD569PfCm

MDC button default style with type values

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/93924663a2afabfbf2b7ea9a17067f11adc061dcc7f00bb18166f68f73bb777d602a5ea12e18b30716fed85e3214ae766454f17e3625f95fa600807ef550bf9c

https://lh3.googleusercontent.com/6f8oySsomvC-CdaCeRzHUleoflDzBWmcQEpUHHoDemEPu94bJV6TTCTzqKX4jecgt1hZOpbS2IEldm8kGemc8lL5ifTA3wdC0R2eqw

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/688f38af0c646d351700f54ccc1745d1e7ccb6f1b05b60b9315d51ada1ebb8e51becf0b23480657adde97616ceea2fee3772560eab77d697d36694ab3d1b097f

https://lh3.googleusercontent.com/QYmMEVMQnST3qpYC1r5OEFSdyvZDQHI-RawscL-YRf1eJaNkJeGoImxSfb1jmIIcHEjrv96pq-HOsUIf7EkKuT6yJMwegbDuzHk1sw

Android, Material Theming, Typography, How-to

{}

Match your brand to Material Design components using Material theming on Android with 13 type styles that Material Design provides.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e24c0df3dc1fce2a6763fcebeac0f97eef9263bdeaf274ad9d63cf7cdb3ab13f62fcc4dc3eb149f29b4351d8dbb91f8e6f63885368ff2da8cdf9ee5fc3f2302e

https://lh3.googleusercontent.com/CAWGli8WuYO5Z1EQymqkf0Wo0dsQhC1oiIRNuB3XympOumZMjhui29AWf_H2fOH1AIxogJTq2K93hAvXJ9ZbMsu45eAzqBeLk2nk9Q

Building a Material Theme on Android: Typography

2020-09-01T13:05:00

android-material-theme-type

Type theming on Android using the MDC library

Building a Material Theme on Android: Typography

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/7bbd8dbc40e9bb70ada1a87ec1d452185fa1bd23acf217dfa51f2b67d3e72a68eb03d290d7e9597fd4b2df021c1576b89b9fb505ec454d2b9c9392a50b683326

https://lh3.googleusercontent.com/1T6DD1rCMym64PMEPWDZkXntz8DRWfB7ac7RWS2k_nH1goLXbSZLkQbYBcj2zk3hXyUI9NLkuE-bINnvvb6-STbawnxnzVlsd4mx

/blog/design-material-theme-type

Material Blog

Designing a Material Theme: Typography

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/b3ba7a68fbda805ebc7c5fbd26bd7d5ff2978797b1d733b66819e9b8d1d7771cd1f439e96f766b499ed83b924d677c90132fa71f828b2f0e323528f8d688602f

https://lh3.googleusercontent.com/nLnu3NrhONUqGTIRjC-WCHLE0MAtC6IeU6kTa4CD9QBL943wg29dvvXpO7YRWiyS3lrFGFRaQhR7xtdIRDzt-T1rqw4EQw13YDy3

/design/typography/the-type-system.html

Typography

The type system

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/6f6a97a70961c27b3ce68a3d2379523ba098f177ab545e4f7f65cba84e81cbcf292ec1b2e0a4e8c7bbf6796837412c05f309f4e0d5bfeef1a961505ac73dc582

https://lh3.googleusercontent.com/32QVXJlStUJhkr7aylDQUKiIONcfRdpI_QBxa79rDTLEFTVjQCsTCn3PEKAQy0JWrtlYoJaXIa0MDggYcXI5ub4gyiz9Y56hfBOsmg

/blog/material-design-blog-welcome/

Material blog

Welcome to the Material Blog—A Letter from the Editor

mio-example
