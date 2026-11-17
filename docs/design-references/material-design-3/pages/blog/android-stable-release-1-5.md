# Material Design Components for Android 1.5.0

Source: https://m3.material.io/blog/android-stable-release-1-5
Content endpoint: https://m3.material.io/page-data/Posts/5731438242299904.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/e542d55e05d06e63bbf3dadd467d6f4889a15a6c2c43b46c812a48b6ee2adf7ff126e17cb0d3c04d4d2f24d216f00138ed4cd9cbf209538cb1bd0f4fd7ac7f15

https://lh3.googleusercontent.com/ECgal03qq-GPHfoWRZft82d97qPwwB-M4z1d-igDCWWAMWhJteOVP4HzaU2XhhQVfG9ME-_0DWTFA1eK28kgnTgTHBpSnTIhLK8TQKwE0zyq_lFckrs

James Williams

Material Developer Advocate

mio-example

```java
* accent
* onAccentColor
* accentContainer
* onAccentContainer
```

```java
ColorRoles getColorRoles(@ColorInt int color,
   boolean isLightTheme);
```

```java
  val button = view.findViewById<Button>(R.id.button_first)
  val green = resources.getColor(R.color.green, null)
                // or Color.parseColor("#FF1BA132")
  val roles = MaterialColors.getColorRoles(green, true)

  button.setBackgroundColor(roles.accentContainer)
  button.setTextColor(roles.onAccentContainer)
```

<p>Back in October, at <a href="https://developer.android.com/events/dev-summit">Android Dev Summit</a>, we released a preview of Material Design 3 for Material Design Components (MDC).</p>
<p>Now we&rsquo;re ready to announce the stable release of MDC 1.5.0 with more Material Design 3 support, component fixes and more color utilities. You can check out the release notes <a href="https://github.com/material-components/material-components-android/releases/tag/1.5.0">here</a>.</p>
<p>If you held off on migrating last year, now is a great time to explore the new design system. Beyond the resources listed above, some areas you should focus your attention on are the Material 3 Catalog App and extended color utilities.</p>
<h2>Material 3 Catalog App</h2>
<p>Our engineering team uses the Material Catalog app to verify and show example implementations of new components and features relating to Material Design. It&rsquo;s a great source for discovering the new system.</p>
<p>If you haven&rsquo;t yet migrated to Material 3 and dynamic color, the catalog app offers a settings area allowing you to see how a default light, dark, or user-generated theme will look throughout the app.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<p>You can download the apk file <a href="https://github.com/material-components/material-components-android/releases/download/1.5.0/catalog-debug.apk">here</a>. For each screen, there&rsquo;s also source code to <a href="https://github.com/material-components/material-components-android/tree/master/catalog/java/io/material/catalog">check out</a>, organized by component.</p>
<h2>Extended Color Utilities</h2>
<p>Also at Android Dev Summit, we launched the Material Theme Builder for <a href="https://www.figma.com/community/plugin/1034969338659738588/Material-Theme-Builder">Figma</a> and <a href="https://material-foundation.github.io/material-theme-builder/">the web</a>. It provides designers and developers a means to experiment with dynamic color and Material 3 themes with the option to export as code.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>We've been pleasantly surprised by the community adoption of Material Theme Builder. We've also heard from you that you want to incorporate color roles from more than the standard key colors. At present, we only export the seed color for each extended (non-key) color, despite showing a visualization of them.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>In anticipation of more color features coming in the library, MDC 1.5.0 has a function in the MaterialColors class named <code>getColorRoles</code> that will return:</p>
<ul>
<li><code>accent</code></li>
<li><code>onAccentColor</code></li>
<li><code>accentContainer</code></li>
<li><code>onAccentContainer</code></li>
</ul>
<p>The full signature is as follows:</p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p>With this ColorRoles object, you could retheme a component at runtime. In the following snippet, we change the colorContainer and onColorContainer values for a button. Always remember to reassess the onColorContainer(text) tone when altering the colorContainer tone to ensure text has proper contrast and readability.</p>
<p>&lt;mio-code-snippet index=2&gt;&lt;/mio-code-snippet&gt;</p>
<p>&lt;mio-col-set cols=3&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<h2>What&rsquo;s next for MDC?</h2>
<p>We&rsquo;re fast at work on the next major version of MDC. You can follow the progress, file <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=bug&amp;template=bug_report.md&amp;title=%5BComponent+name%5D+Short+description+of+issue">bug reports</a> and <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=feature+request&amp;template=feature_request.md&amp;title=%5BComponent+name%5D+Short+description+of+request">feature requests</a> on GitHub. Also feel free to reach out to us on Twitter <a href="https://twitter.com/materialdesign">@materialdesign</a>.</p>

Home screen of Material Components Catalog App

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/c18bdefa9aad92cd5057c6b23d6030dff7a9255874ff630d6ace8f79a77809f1f5286d007d16d00d972af52a608096e805917d35ec16b78de6cccfa022eba6a6

https://lh3.googleusercontent.com/tRsZvSk4VuvHJmxG6czy4eljvcVjV2RmPxQ5UBfkMuLy_vuzMrbLyfs2CNYY7G0Mc9qrfGaeMTlcPCVkK_G_ZaqSwOdB68h7Tgvtq6OH21nzcMR2QGg

Theme and Dynamic Color Settings Selection in Material Components Catalog App

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/2c1930e9466e0e2c0f5068ab1dd880d41892218e0243320b216bcf1eaf5c6ce532863f5a86d610d099918d2852fd4733135fce0fbc104981c646a2ee2a5a380d

https://lh3.googleusercontent.com/xwFFAMhc52NEO9Ke0v_ysbqXlppp3hRlqc5bXBZx4Z015-y41-Yt7x-GeRZnqqoelzz222yIt-05A8StJzEf6qafjl06b2qvp9PM-7FPDIvN19enI9Ob

Default UI of Material Theme Builder

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/82e13b70968bd60c7c6dc5794aac5eb50d5827845a75a9e0cd476bc72adf4be1516aea3e830357a67d29795625dcd37a559670869a95df45bfe643a0ce15b7cf

https://lh3.googleusercontent.com/H-6OuN26_CI982zVAnuoad9l-fERsmDObwT9h-gi24QZDbOnsIbsMtxdMJUiF9v1qN96NW8qILKy3b9StPsRjPj-Y1iofgU8Y4wJD_5FoJ61062OWT9r

Material Theme Builder view with extended colors visualized

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/60b83396ce45c1c7656544240d05ebbb4e034be192eb1ede7ba14951ecf3edea1f1b11e15c9c68142f7b9fca2d2d657a5f885440e6265cf83062d8b968bd9513

https://lh3.googleusercontent.com/ropJhw9RhD5BedUUPJKIAgN0XzOj7Ooe0T0A7bD7pwj91son28V9Ntuutets019kc4Jte-OGAvcAkg4A-1l3B8UpqVJqqlEnSR5xQl0W__LWrXRGhqA

Android sample project with no modifications applied

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e4966a213827b02bd0c541e186a8d7aa125c26fbfb83ec694718434917d3bdca8d43715aacd9111f94cca0d840c66e8a11b6bb23b41b6272431d1f18aedba7f9

https://lh3.googleusercontent.com/63qXR7bKdN0wh6-P1i4HlFvSerCFRLTPWZ4KzbDHSUSsvvh1hMyuZX8f3OzdWmwriX2uqVy2-hzRo3nRy8hfszPbvyZ10UGAH2dOUYOG5DxWbGAGEZA

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/2b397a4c341d6ad44bc8acee94d6c4d7f261ca5e589c6434035f1157984ec8f358537697bdea5dbc2569e9bc5343fedb268cf09da7ed7551e7200924f0ae1482

https://lh3.googleusercontent.com/wHVjc6HRf1Ma-Igg2EpY2LJAwKTP48lQ7q6o5qJAcoPaKr2NaI4MePW1c2X70W0-lcRb6uIKv_J0UrzdbPKbIYs_vSTitINl9DDhVkVjkXjjjsUl5Lo

Runtime generation of green light theme color roles applied to a button

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/76d5bde047f4e80a167c093be240564c061cab6c9f74d49d2251b97bd8ca5a5abc8433eae720dfe037a626aeb240dbe18bd3b75b5fdbb07833574c0ba8b1c630

https://lh3.googleusercontent.com/caEM6pKSg8hUfzEy0V2gmat5t6d5dMrHqtge5_FjI5OcA01lp_dj8FjcsPXN8L5lORmolB3MpwaKsGFcrox95enE8s3ZnQZreFNSSecHTHWdB5H1eRc

Illustration of a plant sprouting through an abstract form

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/1fa33daa16004128e023bd67397ff445e1be3dad7858e6899590803221f449a0231384f25465d39ae587f04b038fe37f9901bc069440d3713b13a0b930fc4e22

https://lh3.googleusercontent.com/S2BoUveRJNGtg2eQEJX4WGF0_PoalerbcfsvmjePTcqg0kK5aDB3i4mfUnueIPOatM6RKVWHbbhSAaB7NoaGshb9IfryPGKlfL2TTaHdNjS6qw3_6ZA

 

{}

With Material Design 3 refinements and more color utilities

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/406b03dd9144064c1ff7e795485fc2ceae4d4377507eb08e480aed68d8655921003fad7316b4fcea0f052e85ca480ac6aa2bafd448bdbd9c38abcfd5f0e218ba

https://lh3.googleusercontent.com/t315gtXe-NaZuJYZATNVkEkkElrX6L34HwZHaZFvL8uNw-z0xgizPfX-8Gw3rLUP6uMXnz4x2OILJsh4ew-ys7XgWqd8YfdMsLQQFOG_9TB1Rfl2fnE

Material Design Components for Android 1.5.0

2022-02-17T13:00:00

android-stable-release-1-5

With Material Design 3 refinements and more color utilities

Material Design Components for Android 1.5.0

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

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/b14f83531e0ded0b48ab6c6e03d8645b76f3a34d7abe4a849ea689a09b0ab4dbd5b52ffda0e00d05c9cc3d0aafa490251c132c68911265a6b25b3b74cf67876a

https://lh3.googleusercontent.com/Aj_PgNvXar9dTxMmBoCjGE5OG1jhEZyjoXUI3mOJMdhY68LvL1LYuI5aL0r8e3lESTZWL6mqhRPY30qYd9VDIPx6lXdomuw4orxQ6T_mlAGJvggS6Bc

Introducing Material Theme Builder

/blog/material-theme-builder

Introducing Material Theme Builder

Material Blog

Introducing Material Theme Builder

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
