# Material Design Components for Android 1.3.0

Source: https://m3.material.io/blog/android-stable-release-1-3-0
Content endpoint: https://m3.material.io/page-data/Posts/6503505239736320.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/18a6db2775f36a6a1b0cae6a88e8df282b27cf4a9db808be9c693fd35bdd3314798a1545d32d424a38e33f75b203165168f010c199ce63799b5e91d6309969a3

https://lh3.googleusercontent.com/m-PDSndGA4cUhtNjSl4HXPqXIaHxvYG28BPPcal5dnXUge1Po6SJJw2I3RjrIYyKBY6exL4bXnjaDt9dusnuDVO_anSC8lzVK7pCvWo

Nick Rout

Material Developer Advocate

mio-example

```java
<!-- Linear progress indicator -->
<com.google.android.material.progressindicator.LinearProgressIndicator
    android:id="@+id/linearProgressIndicator"
    ...
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:indeterminate="true"
    app:showAnimationBehavior="outward"
    app:hideAnimationBehavior="inward"
    app:indicatorDirectionLinear="leftToRight" />

<!-- Circular progress indicator -->
<com.google.android.material.progressindicator.CircularProgressIndicator
    android:id="@+id/circularProgressIndicator"
    ...
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:indeterminate="true"
    app:showAnimationBehavior="outward"
    app:hideAnimationBehavior="inward"
    app:indicatorDirectionCircular="clockwise" />
```

```java
val timePicker =
    MaterialTimePicker.Builder()
        .setTimeFormat(TimeFormat.CLOCK_12H)
        .setHour(12)
        .setMinute(10)
        .setTitle("Select Appointment time")
        .build()

timePicker.addOnPositiveButtonClickListener {
    val hour = timePicker.hour
    val minute = timePicker.minute
    // Do something with time
}

timePicker.show(fragmentManager, "tag")
```

```java
val badge = BadgeDrawable.create(context)

// Use badges with custom views
BadgeUtils.attachBadgeDrawable(badge, customView)
BadgeUtils.detachBadgeDrawable(badge, customView)

// Use badges with toolbar menu items
BadgeUtils.attachBadgeDrawable(badge, toolbar, menuItemId)
BadgeUtils.detachBadgeDrawable(badge, toolbar, menuItemId)
```

```java
val transform = MaterialContainerTransform().apply {
    // Tell the container transform which Views to transform between
    startView = fab
    endView = bottomToolbar
    // Ensure the container transform only runs on a single target
    addTarget(endView)
    // Other setup like path motion, scrim color, etc.
}

TransitionManager.beginDelayedTransition(container, transform)
fab.isVisible = false
bottomToolbar.isVisible = true
```

```java
val transform = MaterialContainerTransform().apply {
    // Start/end views, target, path motion, scrim color, etc.
    interpolator = BounceInterpolator()
}
```

<p>We&rsquo;re excited to announce the release of Material Design Components (MDC) 1.3.0! A host of exciting new features have been added along with many bug fixes and accessibility improvements. Get the rundown below.</p>
<p>Be sure to check out the&nbsp;<a href="https://github.com/material-components/material-components-android/releases/tag/1.3.0">release notes</a>. If you&rsquo;re using MDC for the first time, also take a look at our&nbsp;<a href="https://material.io/develop/android/docs/getting-started">getting started guide</a>.</p>
<h2>What&rsquo;s new in 1.3.0?</h2>
<p>A fair bit has changed since we launched&nbsp;<a href="https://material.io/blog/android-stable-release-1-2">1.2.1</a>&nbsp;in September last year &ndash; we added the progress indicator and time picker components, made extensive internationalization and localization string updates, and more. The things you loved from the alpha, beta, and RC releases of 1.3.0 are now officially stable. If you haven&rsquo;t yet started using 1.3.0 of MDC, there&rsquo;s never been a better time to update.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<h2>ProgressIndicator</h2>
<p><a href="https://material.io/components/progress-indicators">Progress indicators</a>&nbsp;inform users about the status of ongoing processes, such as loading an app, submitting a form, or saving updates. They communicate an app&rsquo;s state and indicate available actions, such as whether users can navigate away from the current screen.</p>
<p>MDC 1.3.0 allows you to use progress indicators in your Android app with the&nbsp;<code><a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/progressindicator/LinearProgressIndicator.java">LinearProgressIndicator</a></code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">and&nbsp;</span><a style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;" href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/progressindicator/CircularProgressIndicator.java"><code>CircularProgressIndicator</code></a><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">&nbsp;widgets. They&rsquo;re similar to&nbsp;</span><code>ProgressBar</code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">&nbsp;but have additional features and support&nbsp;</span><a style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;" href="https://material.io/design/material-theming/overview.html">Material Theming</a><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">.</span></p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p>Learn more about how to implement progress indicators in&nbsp;<a href="https://material.io/components/progress-indicators/android">our documentation</a>.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<h2>MaterialTimePicker</h2>
<p>Time pickers allow users to enter a specific time value. They can be used for a wide range of scenarios such as setting an alarm or scheduling a meeting. Mobile time pickers are displayed in dialogs and can be used to select hours, minutes, and a period of time.</p>
<p>MDC 1.3.0 allows you to use time pickers in your Android app with the&nbsp;<code>MaterialTimePicker</code>&nbsp;class, which extends&nbsp;<code>DialogFragment</code>. It&rsquo;s similar to&nbsp;<code>TimePicker</code>&nbsp;but has additional features and input methods, and supports&nbsp;<a href="https://material.io/design/material-theming/overview.html">Material Theming</a>.</p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p><em><strong>Note:</strong> MaterialTimePicker can be used with the Navigation component using the </em><em style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;"><code>&amp;lt;dialog&amp;gt;</code>&nbsp;tag. Learn more about navigating to dialog destinations here.</em></p>
<p>Learn more about how to implement time pickers in&nbsp;<a href="https://material.io/components/time-pickers/android">our documentation</a>.</p>
<h2>Internationalization and localization</h2>
<p>Certain MDC components include strings as part of their anatomy&mdash;think of the &ldquo;Choose a date&rdquo; title and &ldquo;OK&rdquo; button in date pickers. Additionally there might be built-in strings for accessibility so that screen readers can announce actions and content descriptions.</p>
<p>As part of MDC 1.3.0 these strings have been translated for all languages supported by Android! The affected components include&nbsp;<a href="https://github.com/material-components/material-components-android/commit/af375eb31a0037a6b30bc3e7ba43f2b5eee83de8">date picker</a>,&nbsp;<a href="https://github.com/material-components/material-components-android/commit/c1a290edb97ae9fc6c47e99df05e39bbe3099df8">time picker</a>,&nbsp;<a href="https://github.com/material-components/material-components-android/commit/9d1d9773cd9418bdef740fa67ae4a2da4436f7bc">bottom sheet</a>,&nbsp;<a href="https://github.com/material-components/material-components-android/commit/467bb88650ab9c54463c58f4eb7ece75fe60d4b4">text field</a>,&nbsp;<a href="https://github.com/material-components/material-components-android/commit/0845dfe0d143f77be75b67e09b22950546b17bcf">chips</a>,&nbsp;<a href="https://github.com/material-components/material-components-android/commit/23018e1fbfa4587a23a8465d1b6b0dd4941bcd54">badges</a>, and&nbsp;<a href="https://github.com/material-components/material-components-android/commit/cf3c091c7a9bac003650ad12c419682b1e9f0f9e">dialogs</a>.</p>
<h2>BadgeUtils</h2>
<p>The&nbsp;<a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/badge/BadgeUtils.java"><code>BadgeUtils</code></a>&nbsp;utility class was made public in MDC 1.3.0. It gives you a variety of useful static methods to use when dealing with badges in custom&nbsp;<code>View</code>s. New methods were also added for adding badges to&nbsp;<code>Toolbar</code>&nbsp;menu items.</p>
<p>&lt;mio-code-snippet index=2&gt;&lt;/mio-code-snippet&gt;</p>
<p><em><strong>Note:</strong>&nbsp;<code>BadgeUtils</code>&nbsp;is considered experimental and the APIs are subject to change. You&rsquo;ll need to use the&nbsp;<code>@ExperimentalBadgeUtils</code>&nbsp;annotation when accessing this class.</em></p>
<p>Learn more about how to implement badges in&nbsp;<a href="https://material.io/develop/android/supporting/badge">our documentation</a>.</p>
<h2>Material Motion updates</h2>
<p>MDC transitions received a number of updates to improve stability as well as compatibility with all Android API levels. In particular there are a couple of notable changes for&nbsp;<code>MaterialContainerTransform</code>.</p>
<p>We now recommend specifying a target for&nbsp;<code>View</code>-to-<code>View</code>&nbsp;container transform transitions to ensure they only run on a single&nbsp;<code>View</code>. We&rsquo;ve added this to&nbsp;<a href="https://github.com/material-components/material-components-android/commit/76cba45d62f38947f59914cab7ef070660624ada">our documentation</a>.</p>
<p>&lt;mio-code-snippet index=3&gt;&lt;/mio-code-snippet&gt;</p>
<p>An exciting addition is that&nbsp;<code>MaterialContainerTransform</code>&nbsp;<a href="https://github.com/material-components/material-components-android/commit/ad1d1730180c850330949a7187a14ef402378e88">now supports additional interpolators</a>&mdash;<code>OvershootInterpolator</code>,&nbsp;<code>AnticipateOvershootInterpolator</code>,&nbsp;<code>BounceInterpolator</code>, and any subclasses.</p>
<p>&lt;mio-code-snippet index=4&gt;&lt;/mio-code-snippet&gt;</p>
<p>Learn more about how to implement motion in&nbsp;<a href="https://material.io/develop/android/theming/motion">our documentation</a>.</p>
<h2>&hellip; and more</h2>
<p>A variety of smaller features and bug fixes made it into this release. Check out the&nbsp;<a href="https://github.com/material-components/material-components-android/releases">releases page</a>&nbsp;as well as the&nbsp;<a href="https://github.com/material-components/material-components-android/compare/1.2.1...1.3.0">diff between 1.2.1 and 1.3.0</a>&nbsp;for a full list.</p>
<p>Here are some of the highlights:</p>
<ul>
<li><a href="https://github.com/material-components/material-components-android/commit/5fb796437291ce6b7d43b3beba13a42256db6eac">Show/hide&nbsp;<code>Slider</code>&nbsp;tick marks in discrete mode</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/e6f05bca7e32751e3d480427912bfd9895e40514">Shape theming in&nbsp;<code>NavigationView</code></a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/4a0f60c62d5acb29841540d16ab24c313df7c55b">A getter method to check if an&nbsp;<code>AppBarLayout</code>&nbsp;is lifted</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/6951bd517940dd3d2a2f9d15370f3a046443d260">Elevation overlay support in&nbsp;<code>Chip</code>s</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/5c83026c176e291157c2cf3ca4cfc9cb76f12820">Initial show animation in&nbsp;<code>ExtendedFloatingActionButton</code></a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/99c6a28b104b804694a9b3225208cac2bc326c40">Flipped password icon behavior in&nbsp;<code>TextInputLayout</code></a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/8ec11a1460f59cb4e6e60f67af76d0d1c90f812a">Updated&nbsp;<code>BottomNavigationView</code>&nbsp;menu item selection animation to match spec</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/391d1f8ac5d560b1e97c67e129967bbe88cc6163">Updated&nbsp;<code>Snackbar</code>&nbsp;dimensions to match spec</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/c4f7de167f21d92265a39a21368beeda45c02e05">Support for content padding in&nbsp;<code>ShapeableImageView</code></a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/0df77248d508ee59d0f2d9966e88f08f73a89610">Better support for system gesture nav insets in&nbsp;<code>BottomSheetBehavior</code></a></li>
</ul>
<h2>What&rsquo;s next for MDC?</h2>
<p>The next feature release of MDC&mdash;1.4.0&mdash;is expected to land in alpha soon! Exciting new updates include&nbsp;<a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/navigationrail/NavigationRailView.java"><code>NavigationRailView</code></a>,&nbsp;<a href="https://github.com/material-components/material-components-android/commit/186d5ed023a69176af3bcd0f69c635cf60285bba">motion theming</a>, and various improvements to existing components. As always, we encourage you to file&nbsp;<a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=bug&amp;template=bug_report.md&amp;title=%5BComponent+name%5D+Short+description+of+issue">bug reports</a>&nbsp;and&nbsp;<a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=feature+request&amp;template=feature_request.md&amp;title=%5BComponent+name%5D+Short+description+of+request">feature requests</a>&nbsp;on GitHub. Also be sure to check out our Android&nbsp;<a href="https://github.com/material-components/material-components-android-examples">example apps</a>&nbsp;and&nbsp;<a href="https://material.io/resources/build-a-material-theme/">Build a Material Theme</a>.</p>
<p>We highly encourage trying out MDC 1.3.0. If you&rsquo;re using its features in your Android app, reach out to us on Twitter&nbsp;<a href="https://twitter.com/materialdesign">@materialdesign</a>. We&rsquo;d love to see it.</p>
<p></p>

GIF of linear and circular progress indicators

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/432201d5f84f8e1794e09fb275d89b827a3eb283e0ad157c90950695064ea58df22fd3cf0fd4c6bfd447ca95a2ff3772dd3337d087651610b0f4ea6405784e94

https://lh3.googleusercontent.com/Nvg43GoQdU1BBQh9PPTDaCqb3-XzbzCqvYvVDekL_d3NekjQLvQXZhqavPKqRZoEbyAr7GZt5qPZ33VS9kd_z33OLgl7v6L1qfHG-g

Illustration of a Material time picker

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e85bc048bd16c7079bcafcaa3ffeb3fc7410e4835db49dcb9e8cdde824611de61e7baf7da9b5af5c4b4b398d2bb5c1daa8e8cc1d534e6066feca0f2b78243b52

https://lh3.googleusercontent.com/D18QEw8kvf3p30wikbp6QbOFAUH7_Evlf-fa1YdutNgNRUfFveQEr9lIIcaKX-rWdUnl2PL_p8tygMlXXL7yJSHDK-fg9oIfGPI0OXU

illustration showing Material time picker and app bar

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6eaced3266e44de074da1a9355ec85e3523d2d0828d6f8da9866aa811dff8964df7b8644cee8269c07475bbbf5ac164a50e89d9b34856613332166ae64dbc053

https://lh3.googleusercontent.com/jYzl7MY0Jk0KTZuzu9TCyH7c_5exgEQhOSUqDtfy2jiwHgDoR3oL1BuBOxeoGlblrsRdWnEnZexFyxeVOzD4eeKxMoi-zCLgFUN2QQ

Android Release

{}

We’re excited to announce the release of Material Design Components (MDC) 1.3.0. ProgressIndicator, MaterialTimePicker, i18n / l10n, and more.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/b5e10b33c07e956d849f7d3531c44e62ef6a612a318b52fbeb9c1e816db39425c7287a98c1f4996f7e5046bee625378c9ba649270080db3c03538926c90cb1d8

https://lh3.googleusercontent.com/go4JD2k7vqFN0rSJA9gUHG72LtTEFdqCY5SnH6xLe4zDRxMXCV3Vp7QZbTPHXx6KM94J4ACqK6jx5DwiiWzOktBQMmfRXinOgSUR

Material Design Components for Android 1.3.0

2021-02-18T13:00:00

android-stable-release-1-3-0

ProgressIndicator, MaterialTimePicker, i18n / l10n, and more

Material Design Components for Android 1.3.0

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/c4ec06781aadfc756a4b6821f6ae26e14756fbd5971507d276fd24205fa847e006afce690fbc54c71717b37b27db666e3f966a28b5f6b29cef64f74219af5843

https://lh3.googleusercontent.com/4pnYePc3AZbXhsNSaDE3SEej6vWxJxvoXBmvAMvCPY4f1zuLwMOsGzVOcZ_BrosztF_mUKAm_IjN6enkyfAqjz4FrphMY59sgEMrbA

/blog/android-stable-release-1-2

Material Blog

Android Stable Release 1.2.0

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/7f7a16e9dfeda6060e1c4f5bdedc94a231343e41c774c1e550ed9602faf37412a004c02558c2957244a25f020437bd813931f8e48a4eed61cb35b270afd082c1

https://lh3.googleusercontent.com/Wxts4cOyvF3jFuCHoe1w8QAm_RIlOqXA5tppbAIeOhcWksSdtHf2KuiglwKkczZp3hAz-BHwzwwohnk0rxeh7Nh4i4kTtT2ecVHN

/blog/migrate-android-material-components

Material Blog

Migrating to Material Components for Android

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/6cf22561c1cf6685fd88b87dba9262d0317bea10b616f2eae32fd44768613c0f1f3185ea98b2a4ab42311f301fa690ce8437af2fe3ce84686aee159c38e952f6

https://lh3.googleusercontent.com/sug69DZgHwvlMkv3T0Wa3x2ZHYqQDdZiI8VJiVMdoInbwBUeJZT48jKAHZqLxsHuQnoMR1NMVOmvIPfA_CjxEQYjfpCNqcYLeOhjzw

/resources/tutorials

Resources

All Developer Tutorials

mio-example
