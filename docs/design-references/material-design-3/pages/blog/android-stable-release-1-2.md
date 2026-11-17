# Material Components for Android 1.2.0

Source: https://m3.material.io/blog/android-stable-release-1-2
Content endpoint: https://m3.material.io/page-data/Posts/5174296018944000.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/18a6db2775f36a6a1b0cae6a88e8df282b27cf4a9db808be9c693fd35bdd3314798a1545d32d424a38e33f75b203165168f010c199ce63799b5e91d6309969a3

https://lh3.googleusercontent.com/m-PDSndGA4cUhtNjSl4HXPqXIaHxvYG28BPPcal5dnXUge1Po6SJJw2I3RjrIYyKBY6exL4bXnjaDt9dusnuDVO_anSC8lzVK7pCvWo

Nick Rout

Material Developer Advocate

mio-example

```java
<!-- fragment_a.xml -->
<View
    android:id="@+id/start_view"
    android:transitionName="start_container" />
<!-- fragment_b.xml -->
<View
    android:id="@+id/end_view"
    android:transitionName="end_container" />
// FragmentB.kt
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    ...
    sharedElementEnterTransition = MaterialContainerTransform()
}
// FragmentA.kt
fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    ...
    exitTransition = Hold()
}
...
val directions = FragmentADirections.actionFragmentAToFragmentB()
val extras = FragmentNavigatorExtras(startView to "end_container")
findNavController().navigate(directions, extras)
```

```java
// FragmentA.kt
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    ...
    reenterTransition = MaterialSharedAxis(
        MaterialSharedAxis.Z, /* forward = */ false)
    exitTransition = MaterialSharedAxis(
        MaterialSharedAxis.Z, /* forward = */ true)
}
// FragmentB.kt
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    ...
    enterTransition = MaterialSharedAxis(
        MaterialSharedAxis.Z, /* forward = */ true)
    returnTransition = MaterialSharedAxis(
        MaterialSharedAxis.Z, /* forward = */ false)
}
```

```java
// FragmentA.kt
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    ...
    exitTransition = MaterialFadeThrough()
}
// FragmentB.kt
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    ...
    enterTransition = MaterialFadeThrough()
}
```

```java
val fade = MaterialFade()
TransitionManager.beginDelayedTransition(container, fade)
view.visibility = View.VISIBLE // Use View.GONE to fade out
```

```java
<!-- In layout -->
<com.google.android.material.slider.Slider
    android:id=”@+id/slider”
    ...
    android:valueFrom="0.0"
    android:valueTo="100.0"
    android:stepSize="10.0" />
    ...
<com.google.android.material.slider.RangeSlider
    android:id=”@+id/rangeSlider”
    ...
    android:valueFrom="0.0"
    android:valueTo="100.0"
    android:stepSize="10.0"
    app:values="@array/initial_slider_values" />
<!-- In res/values/arrays.xml -->
<resources>
    ...
    <array name="initial_slider_values">
        <item>20.0</item>
        <item>70.0</item>
    </array>
</resources>
// In code
slider.addOnChangeListener { slider, value, fromUser ->
    // Respond to change in slider's value
}
...
val values = rangeSlider.values
```

```java
<!-- res/values/shape.xml -->
<style name=”ShapeAppearanceOverlay.App.CornerSize50Percent”
    parent=””>
    <!--
    Sets size of corners to be 50% of min(width, height) of widget
    -->
    <item name=”cornerSize”>50%</item>
</style>
<!-- res/values/styles.xml -->
<style name=”Widget.App.ShapeableImageView”
    parent=”Widget.MaterialComponents.ShapeableImageView”>
    <item name=”shapeAppearance”>
        ?attr/shapeAppearanceSmallComponent
    </item>
    <item name=”shapeAppearanceOverlay”>
        @style/ShapeAppearanceOverlay.App.CornerSize50Percent
    </item>
    <item name=”strokeWidth”>1dp</item>
    <item name=”strokeColor”>?attr/colorPrimary</item>
</style>
<!-- In layout -->
<com.google.android.material.imageview.ShapeableImageView
    ...
    style=”@style/Widget.App.ShapeableImageView”
    app:srcCompat=”@drawable/image” />
```

```java
// Resolve color from theme attr
val primaryColor = MaterialColors.getColor(
    view, R.attr.colorPrimary)
// Layer background color with overlay color + alpha
val overlayedColor = MaterialColors.layer(
    view, R.attr.colorSurface, R.attr.colorPrimary, 0.38f)
```

```java
<!--
Note: Button is auto-inflated as
MaterialButton by MaterialComponentsViewInflater
-->
<Button
    ...
    android:background=”@drawable/custom_background”
    app:backgroundTint=”@empty” />
```

<p id="f5f1" data-selectable-paragraph="">We&rsquo;re excited to announce the release of&nbsp;Material Components for Android (MDC-Android)&nbsp;<code>1.2.0</code>! A host of exciting new features have been added along with many bug fixes and accessibility improvements. Get the rundown below.</p>
<p id="4138" data-selectable-paragraph="">Be sure to check out the&nbsp;<a href="https://github.com/material-components/material-components-android/releases/tag/1.2.0" target="_blank" rel="noopener nofollow">release notes</a>. If you&rsquo;re using MDC for the first time, also take a look at our&nbsp;<a href="https://material.io/develop/android/docs/getting-started" target="_blank" rel="noopener nofollow">getting started guide</a>.</p>
<h2 id="e5e9">What&rsquo;s new in 1.2.0?</h2>
<p id="5176" data-selectable-paragraph="">A fair bit has changed since we launched&nbsp;<code><a href="https://medium.com/google-design/material-design-components-for-android-1-1-0-are-now-available-45e1d576037c" target="_blank" rel="noopener">1.1.0</a></code>&nbsp;in February &mdash; we added the motion system, slider component, a widget for image shape theming, and more. The things you loved from the alpha, beta, and RC releases of&nbsp;<code>1.2.0</code>&nbsp;are now officially stable. If you haven&rsquo;t yet started using version&nbsp;<code>1.2.0</code> of MDC, there&rsquo;s never been a better time to update.</p>
<p data-selectable-paragraph="">&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<h2 id="c4e5" data-selectable-paragraph="">Material motion</h2>
<p id="6c80" data-selectable-paragraph=""><a href="https://material.io/design/motion/the-motion-system.html" target="_blank" rel="noopener nofollow">Material&rsquo;s motion system</a>&nbsp;includes a set of four transition patterns. They can help users understand and navigate an app, and reinforce relationships between components or full-screen views. The transition patterns are:</p>
<ul>
<li id="63f0" data-selectable-paragraph=""><a href="https://material.io/design/motion/the-motion-system.html#container-transform" target="_blank" rel="noopener nofollow">Container transform</a></li>
<li id="c3f4" data-selectable-paragraph=""><a href="https://material.io/design/motion/the-motion-system.html#shared-axis" target="_blank" rel="noopener nofollow">Shared axis</a></li>
<li id="1a81" data-selectable-paragraph=""><a href="https://material.io/design/motion/the-motion-system.html#fade-through" target="_blank" rel="noopener nofollow">Fade through</a></li>
<li id="0bdf" data-selectable-paragraph=""><a href="https://material.io/design/motion/the-motion-system.html#fade" target="_blank" rel="noopener nofollow">Fade</a></li>
</ul>
<p id="8a60" data-selectable-paragraph="">MDC&nbsp;<code>1.2.0</code> enables Material motion in your Android app. The four transition patterns are implemented as classes built on top of both the AndroidX Transition library (<code>androidx.transition</code>) (<code>androidx.transition</code>), available in the&nbsp;<code>com.google.android.material.transition&nbsp;package</code>, and the Android Framework Transition library (<code>android.transition</code>), available in the&nbsp;<code>com.google.android.material.transition.platform</code>&nbsp;package. They can be used to transition between Fragments (including&nbsp;<a href="https://developer.android.com/guide/navigation" target="_blank" rel="noopener nofollow">Jetpack Navigation</a>), Activities, and Views.</p>
<p id="fceb" data-selectable-paragraph="">Container transform between Fragments (using Jetpack Navigation)</p>
<p data-selectable-paragraph="">&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p id="aa7f" data-selectable-paragraph="">Shared Z-axis between Fragments</p>
<p data-selectable-paragraph="">&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p id="e99c" data-selectable-paragraph="">Fade through between Fragments</p>
<p data-selectable-paragraph="">&lt;mio-code-snippet index=2&gt;&lt;/mio-code-snippet&gt;</p>
<p id="e66b" data-selectable-paragraph="">Fade a target View (using&nbsp;<code>TransitionManager</code>)</p>
<p data-selectable-paragraph="">&lt;mio-code-snippet index=3&gt;&lt;/mio-code-snippet&gt;</p>
<p id="4c26" data-selectable-paragraph="">Learn more about&nbsp;<a href="https://material.io/develop/android/theming/motion" target="_blank" rel="noopener">how to implement motion for Android</a>.</p>
<p data-selectable-paragraph="">&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<h2 id="a8f9" data-selectable-paragraph="">Slider</h2>
<p id="ceea" data-selectable-paragraph=""><a href="https://material.io/components/sliders" target="_blank" rel="noopener nofollow">Sliders</a>&nbsp;allow users to make selections from a range of values. They are ideal for adjusting settings such as volume, brightness, or applying image filters.</p>
<p id="7430" data-selectable-paragraph="">MDC&nbsp;<code>1.2.0</code>&nbsp;allows you to use sliders in your Android app with the&nbsp;<code><a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/slider/Slider.java" target="_blank" rel="noopener nofollow">Slider</a></code>&nbsp;and&nbsp;<code><a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/slider/RangeSlider.java" target="_blank" rel="noopener nofollow">RangeSlider</a></code>&nbsp;widgets. They&rsquo;re similar to&nbsp;<code>SeekBar</code>&nbsp;but have additional features and support&nbsp;<a href="https://material.io/design/material-theming/overview.html" target="_blank" rel="noopener nofollow">Material Theming</a>.</p>
<p data-selectable-paragraph="">&lt;mio-code-snippet index=4&gt;&lt;/mio-code-snippet&gt;</p>
<p data-selectable-paragraph="">Learn more about&nbsp;<a href="https://material.io/develop/android/components/slider" target="_blank" rel="noopener nofollow">how to implement sliders</a>.</p>
<p data-selectable-paragraph="">&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<h2 id="79fc" data-selectable-paragraph="">ShapeableImageView</h2>
<p id="f98e" data-selectable-paragraph="">The new&nbsp;<code><a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/imageview/ShapeableImageView.java" target="_blank" rel="noopener nofollow">ShapeableImageView</a></code>&nbsp;widget is an extension of&nbsp;<code>AppCompatImageView</code>&nbsp;which understands shape theming. A common use case is to apply circular clips to rectangular source images. However, it also supports varying corner sizes, cut corners, as well as different stroke widths and colors.</p>
<p data-selectable-paragraph="">&lt;mio-code-snippet index=5&gt;&lt;/mio-code-snippet&gt;</p>
<h2 id="9c7c" data-selectable-paragraph="">MaterialColors</h2>
<p id="dc8a" data-selectable-paragraph="">The&nbsp;<code><a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/color/MaterialColors.java" target="_blank" rel="noopener nofollow">MaterialColors</a></code>&nbsp;utility class was made public in MDC&nbsp;<code>1.2.0</code>. It gives you a variety of useful static methods to use when dealing with colors programmatically in your app.</p>
<p data-selectable-paragraph="">&lt;mio-code-snippet index=6&gt;&lt;/mio-code-snippet&gt;</p>
<h2 id="b0c3" data-selectable-paragraph="">Support for&nbsp;materialThemeOverlay&nbsp;in all components</h2>
<p id="9bba" data-selectable-paragraph="">The&nbsp;<code>materialThemeOverlay</code>&nbsp;attribute allows you to apply&nbsp;<a href="https://medium.com/androiddevelopers/android-styling-themes-overlay-1ffd57745207" target="_blank" rel="noopener">theme overlays</a>. Unlike&nbsp;<code>android:theme</code>, it can be used in default component styles (e.g.,&nbsp;<code>materialButtonStyle</code>). By default it can only be used with MDC; full support for all components was added in&nbsp;<code>1.2.0</code>. You can use&nbsp;<code><a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/theme/overlay/MaterialThemeOverlay.java#L61" target="_blank" rel="noopener nofollow">MaterialThemeOverlay#wrap</a></code>&nbsp;to add this functionality to custom views.</p>
<h2 id="6040" data-selectable-paragraph="">MaterialButton respects android:background</h2>
<p id="4385" data-selectable-paragraph=""><code><a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/MaterialButton.java" target="_blank" rel="noopener nofollow">MaterialButton</a></code>&nbsp;previously ignored custom background drawables applied with&nbsp;<code>android:background</code>. This has been fixed in MDC&nbsp;<code>1.2.0</code>. A&nbsp;<code><a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/shape/MaterialShapeDrawable.java" target="_blank" rel="noopener nofollow">MaterialShapeDrawable</a></code>&nbsp;will still be used as the default background if no custom background is set.</p>
<p id="43e4" data-selectable-paragraph=""><em>Note:&nbsp;The default style for&nbsp;<code>MaterialButton</code>&nbsp;includes a&nbsp;<code>backgroundTint</code>&nbsp;which will also be applied to a custom background drawable. You may need to change this to a different color or set it as&nbsp;<code>@empty</code>&nbsp;to remove it.</em></p>
<p data-selectable-paragraph="">&lt;mio-code-snippet index=7&gt;&lt;/mio-code-snippet&gt;</p>
<h2 id="ac7f">What&rsquo;s next for MDC?</h2>
<p id="f10d" data-selectable-paragraph="">The next feature release of MDC&mdash;&nbsp;<code>1.3.0</code>&nbsp;&mdash; is well underway with multiple&nbsp;<a href="https://github.com/material-components/material-components-android/releases/" target="_blank" rel="noopener nofollow">alpha releases</a>&nbsp;out at the time of writing. Exciting new updates include&nbsp;<code><a href="https://github.com/material-components/material-components-android/blob/master/docs/components/ProgressIndicator.md" target="_blank" rel="noopener nofollow">ProgressIndicator</a></code>,&nbsp;<code><a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/timepicker/MaterialTimePicker.java" target="_blank" rel="noopener nofollow">MaterialTimePicker</a></code>, and various improvements to existing components. As always, we encourage you to file&nbsp;<a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=bug&amp;template=bug_report.md&amp;title=%5BComponent+name%5D+Short+description+of+issue" target="_blank" rel="noopener nofollow">bug reports</a>&nbsp;and&nbsp;<a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=feature+request&amp;template=feature_request.md&amp;title=%5BComponent+name%5D+Short+description+of+request" target="_blank" rel="noopener nofollow">feature requests</a>&nbsp;on GitHub. Also be sure to check out our Android&nbsp;<a href="https://github.com/material-components/material-components-android-examples" target="_blank" rel="noopener nofollow">example apps</a>&nbsp;and how to&nbsp;<a href="https://material.io/resources/build-a-material-theme/" target="_blank" rel="noopener nofollow">Build a Material Theme</a>.</p>
<p data-selectable-paragraph="">We highly encourage trying out MDC&nbsp;<code>1.2.0</code>. If you&rsquo;re using its features in your Android app, reach out to us on Twitter <a href="https://twitter.com/materialdesign" target="_blank" rel="noopener nofollow">@materialdesign</a>. We&rsquo;d love to see it.</p>

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/a41e6694735cf0ddc330a9198370b92dc4fee01e7f8a17db3174fd7636557f7dd51d19fa06b1c0e64d245b909fa224cac3cc233c936d750f511c934ccedd4a68

https://lh3.googleusercontent.com/vN3rn-qxpd5mZAsxqq43fC088mMCtYFjOiCo1Ig-LFR6hEWlD44pna0YaOG2LIMZ9Fkf5xRQ1D5iN9p8c-d-9rdCH_QjKChdIe1M

Baseline slider component with indicator moving from 37 to 89

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/cf613b18c89d297c59db1a258f121aa6643189e1b95da3d15d688509ab7f7eb5786a71ad29b8363ec7ad9825a77364abbd25021ae7c5d52a77598e848396f58e

https://lh3.googleusercontent.com/fI5NTbHaTtm72CwrxbkMBgfUqiHNm9D7K-SsUSsrvP4sTVCuIv7stIn-yrruWnIeOKM0ClAJqp6wjxmE9GTGTqHa2Jk1a3dh6kBd8g

9 shapes illustrating the range of options from very rounded to slightly rounded, sharp, and cut

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e8977a65fa939a6f2bfb334bc257441e6d3689ee71918b8b1b5ff9c64336c8feae034ccd95eed0b9e617e47053a75b5ce24394e7ea87f43d5f0657ae5ed518ce

https://lh3.googleusercontent.com/VeQa8SnPQaKm_VvdkajEdiv4coIUGnhW-YKILlGRXnTyhaIbdTAcKT2fG7VOO3uwAe4MSOz8BDCxS7b-JFDA4qHwfOUrh7dUepfgb3g

Illustrated UI frames with Android bots

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/031af855213732b6ab76bebb8273d435fe1a11623127985c727414d723bd88799b3ce0a5a2a2bafd94876becd46fa12579f4ce2aa1b4809d54a1620cc60ec787

https://lh3.googleusercontent.com/kMVUmItZ96jyShlKNdRVPf3Xpt9BKDRMxc919C2imRjLozwk8fWO4jaAoe4_fAGzDZ0gyP5tZaNSqr-IKQbBwzShHyKR2BD2Etru

Android, Release

 

{}

Including the Material motion system, Sliders, ShapeableImageView, and more

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/a25e37ae740108f68638e8b26a998fc50c085af8940f90f04b69f17d65c0aeb2057b10d8707c56cd9abacc6bc207c587d27ef1b1deeedf90be2986fb93bd6050

https://lh3.googleusercontent.com/4ECRbQog1TZ2ziMMfmesR_-S16fhMjgTttHSxdXetkFYLjBvoJzy4bs6ceI2vdNKaDnUiDxpKB_6Q6rFMZWXlimo_nnq9r7BAF3Z

Material Components for Android 1.2.0

2020-08-04T13:00:00

android-stable-release-1-2

Material motion system, Sliders, ShapeableImageView, and more

Material Components for Android 1.2.0

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/94ccae5400c110b59e0a752e8e67a0d911b9ba63ce354ed4a9411a36992dc5866db038eea65fabe74ccef3b02bf04cd09f852f40647e788c30d1ad4501fc7c20

https://lh3.googleusercontent.com/TeLZea0Z3_3eKsf_VU8bMh3Nn_HNmY3gLNl915hP41iP3X6ZVaCZt3UO-n1PbYVSIN09dOanns3gqMM5bJhJ3es1bJt5Zk7Zq_6F8Q

/blog/android-material-motion

Material Blog

Building Beautiful Transitions with Material Motion for Android

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/7f7a16e9dfeda6060e1c4f5bdedc94a231343e41c774c1e550ed9602faf37412a004c02558c2957244a25f020437bd813931f8e48a4eed61cb35b270afd082c1

https://lh3.googleusercontent.com/Wxts4cOyvF3jFuCHoe1w8QAm_RIlOqXA5tppbAIeOhcWksSdtHf2KuiglwKkczZp3hAz-BHwzwwohnk0rxeh7Nh4i4kTtT2ecVHN

/blog/migrate-android-material-components

Material Blog

Migrating to Material Components for Android

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/1a22d1f6b1218d5a2e18535bbdf793f184a27980c1b8063006968aac95a521b95baddadeb3c14a6a2e07398ab15d597c962454f22abdb5f8a8d1e233725cd5d3

https://lh3.googleusercontent.com/Xvk1QwDoH9IbK1BQIKCiF08ViXB3y9X9CRNZ_CiPM2XrgjCzF9ZJHBPlhH15ylunDGKg_AwatpSGTE3JkZnQyyzlTHgBTRFpqjVQ

/blog/android-material-theme-shape

Material blog

Building a Material Theme on Android: Shape

mio-example
