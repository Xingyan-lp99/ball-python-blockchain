# Material Design 3 for Compose is now stable

Source: https://m3.material.io/blog/material-3-compose-stable
Content endpoint: https://m3.material.io/page-data/Posts/5527854674739200.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/bbdd87316caaeeeb7f0ba8f298914c9653d7a16cef8f034351c268e85fd026331941b46a777f69dea6a13b98319861c4dffba2626783254baa38f656caf90e97

https://lh3.googleusercontent.com/-O3H7G1zcTK5XGtsdS3Gbvg-p9Nm3Y9j6tbaCWdlc4DKEqOmAyscZFlKEDri5oWEr26yOSoGYY7TA0koKn9_yt7JuvN4_YssrJhKj_XSoBrsWk09neM

Gurupreet Singh

Material Design, Developer Advocate

mio-example

```
// Add dependency in module build.gradle
 
implementation “androidx.compose.material3:material3:$material3_version” 
```

```
// Dynamic color is available on Android 12+
val dynamicColor = Build.VERSION.SDK_INT >= Build.VERSION_CODES.S
val colorScheme = when {
   dynamicColor && darkTheme -> dynamicDarkColorScheme(LocalContext.current)
   dynamicColor && !darkTheme -> dynamicLightColorScheme(LocalContext.current)
   darkTheme -> darkColorScheme(...)
   else -> lightColorScheme(...)
}

MaterialTheme(
   colorScheme = colorScheme,
   typography = typography,
   shapes = shapes
) {
  // M3 App content
}
```

```
Switch(
      checked = isChecked,
      onCheckedChange = { /*...*/ },
      thumbContent = {
          Icon(
              imageVector = Icons.Default.Check,
              contentDescription = stringResource(id = R.string.switch_check)
          )
      },
  )
```

```
ModalNavigationDrawer {
    ModalDrawerSheet(
        drawerShape = MaterialTheme.shapes.small,
        drawerContainerColor = MaterialTheme.colorScheme.primaryContainer,
        drawerContentColor = MaterialTheme.colorScheme.onPrimaryContainer,
        drawerTonalElevation = 4.dp,
    ) {
        DESTINATIONS.forEach { destination ->
            NavigationDrawerItem(
                selected = selectedDestination == destination.route,
                onClick = { ... },
                icon = { ... },
                label = { ... }
            )
        }
    }
}
```

```
 CenterAlignedTopAppBar(
          title = {
              Text(stringResources(R.string.top_stories))
          },
          scrollBehavior = scrollBehavior,
          navigationIcon =  { /* Navigation Icon */},
          actions = { /* App bar actions */}
      )
```

```
val typography = Typography(
   titleLarge = TextStyle(
       fontWeight = FontWeight.SemiBold,
       fontSize = 22.sp,
       lineHeight = 28.sp,
       letterSpacing = 0.sp
   ),
   titleMedium = TextStyle(
       fontWeight = FontWeight.SemiBold,
       fontSize = 16.sp,
       lineHeight = 24.sp,
       letterSpacing = 0.15.sp
   ),
   ...
}
```

```
bodyLarge = TextStyle(
   fontWeight = FontWeight.Normal,
   fontFamily = FontFamily.SansSerif,
   fontStyle = FontStyle.Italic,
   fontSize = 16.sp,
   lineHeight = 24.sp,
   letterSpacing = 0.15.sp,
   baselineShift = BaselineShift.Subscript
)
```

```
val shapes = Shapes(
   extraSmall = RoundedCornerShape(4.dp),
   small = RoundedCornerShape(8.dp),
   medium = RoundedCornerShape(12.dp),
   large = RoundedCornerShape(16.dp),
   extraLarge = RoundedCornerShape(28.dp)
)
```

```
// Add dependency in module build.gradle
 
implementation "androidx.compose.material3:material3-window-size-class:$material3_version"
```

```
Scaffold(
    contentWindowInsets = WindowInsets(16.dp)
) {
    // Scaffold content
}
```

<p>Today marks the first stable release of <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary" target="_blank" rel="noopener">Compose Material 3</a>. The library allows you to build Jetpack Compose UIs with Material Design 3, the next evolution of Material Design. You can start using <a href="https://m3.material.io/" target="_blank" rel="noopener">Material Design 3</a> in your apps today!</p>
<p>Note: The terms "Material Design 3," "Material 3," and "M3" are used interchangeably.</p>
<p>Material 3 includes updated theming and components, exclusive features like dynamic color, and is designed to be aligned with the latest Android visual style and system UI.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>You can start using Material Design 3 in your apps by adding the Compose Material 3 dependency to your <code>build.gradle</code> files:</p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p>Note: See the latest M3 versions on the <a href="https://developer.android.com/jetpack/androidx/releases/compose-material3" target="_blank" rel="noopener">Compose Material 3 releases page</a>.</p>
<h2>Color schemes</h2>
<p>Material 3 brings extensive, finer grained color customisation, and comes with both light and dark color scheme support out of the box. The <a href="https://m3.material.io/theme-builder#/dynamic" target="_blank" rel="noopener">Material Theme Builder</a> allows you to generate a custom color scheme using core colors, and optionally export Compose theming code. You can read more about <a href="https://m3.material.io/styles/color/the-color-system/key-colors-tones" target="_blank" rel="noopener">color schemes and color roles</a>.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<h2>Dynamic color</h2>
<p>Dynamic color derives from the user&rsquo;s wallpaper. The colors can be applied to apps and the system UI.</p>
<p>Dynamic color is available on Android 12 (API level 31) and above. If dynamic color is available, you can set up a dynamic <code>ColorScheme</code>. If not, you should fall back to using a custom light or dark <code>ColorScheme</code>.</p>
<table style="border-collapse: collapse; width: 99.8095%;" border="1">
<tbody>
<tr>
<td style="width: 48.6358%;">&lt;mio-image index=2&gt;&lt;/mio-image&gt;</td>
<td style="width: 48.6358%;">&lt;mio-image index=3&gt;&lt;/mio-image&gt;</td>
</tr>
</tbody>
</table>
<p>The <code>ColorScheme</code> class provides builder functions to create both dynamic and custom <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#dynamiclightcolorscheme" target="_blank" rel="noopener">light</a> and <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#dynamicdarkcolorscheme" target="_blank" rel="noopener">dark</a> color schemes:</p>
<p>Theme.kt</p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Material components</h2>
<p>The Compose Material 3 APIs contain a wide range of both new and evolved Material components, with more planned for future versions. Many of the Material components, like <code>Card</code>, <code>RadioButton</code> and <code>CheckBox</code>, are no longer considered experimental; their APIs are stable and they can be used without the <code>ExperimentalMaterial3Api</code>annotation.</p>
<p>The M3 <code>Switch</code> component has a brand new UI refresh with accessibility-compliant minimum touch target size support, color mappings, and optional&nbsp; icon support in the switch thumb. The touch target is bigger, and the thumb size increases on user interaction, providing feedback to the user that the thumb is being interacted with.</p>
<p style="text-align: center;">&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p>&lt;mio-code-snippet index=2&gt;&lt;/mio-code-snippet&gt;</p>
<p>Navigation drawer components now provide wrapper sheets for content to change colors, shapes, and elevation independently.</p>
<table style="border-collapse: collapse; width: 99.791%;" border="1">
<tbody>
<tr>
<td style="width: 48.5029%;"><strong>Navigation drawer component</strong></td>
<td style="width: 48.5029%;"><strong>Content</strong></td>
</tr>
<tr>
<td style="width: 48.5029%;">ModalNavigationDrawer</td>
<td style="width: 48.5029%;">ModalDrawerSheet</td>
</tr>
<tr>
<td style="width: 48.5029%;">PermanentNavigationDrawer</td>
<td style="width: 48.5029%;">PermanentDrawerSheet</td>
</tr>
<tr>
<td style="width: 48.5029%;">DismissableNavigationDrawer</td>
<td style="width: 48.5029%;">DismissableDrawerSheet</td>
</tr>
</tbody>
</table>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p>&lt;mio-code-snippet index=3&gt;&lt;/mio-code-snippet&gt;</p>
<p>We have a brand new <code>CenterAlignedTopAppBar</code> in addition to already existing app bars. This can be used for the main root page in an app: you can display the app name or page headline with home and action icons.</p>
<p>&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p>&lt;mio-code-snippet index=4&gt;&lt;/mio-code-snippet&gt;</p>
<p>See the latest M3 components and layouts on the <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#overview" target="_blank" rel="noopener">Compose Material 3 API reference overview</a>. Keep an eye on the <a href="https://developer.android.com/jetpack/androidx/releases/compose-material3" target="_blank" rel="noopener">releases page</a> for new and updated APIs.</p>
<h2>Typography</h2>
<p>Material 3 simplified the naming and grouping of typography to:</p>
<ul>
<li>Display</li>
<li>Headline</li>
<li>Title</li>
<li>Body</li>
<li>Label</li>
</ul>
<p>There are large, medium, and small sizes for each, providing a total of 15 text style variations.</p>
<p>The <code>Typography</code> constructor offers defaults for each style, so you can omit any parameters that you don&rsquo;t want to customize:</p>
<p>&lt;mio-code-snippet index=5&gt;&lt;/mio-code-snippet&gt;</p>
<p>You can customize your typography by changing default values of <a href="https://developer.android.com/reference/kotlin/androidx/compose/ui/text/TextStyle" target="_blank" rel="noopener"><code>TextStyle</code></a> and <a href="https://developer.android.com/reference/kotlin/androidx/compose/ui/text/font/package-summary" target="_blank" rel="noopener">font-related properties</a> like <code>fontFamily</code> and <code>letterSpacing</code>.</p>
<p>&lt;mio-code-snippet index=6&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Shapes</h2>
<p>The Material 3 shape scale defines the style of container corners, offering a range of roundedness from square to fully circular.</p>
<p>There are different sizes of shapes:</p>
<ul>
<li>Extra small</li>
<li>Small</li>
<li>Medium</li>
<li>Large</li>
<li>Extra large</li>
</ul>
<p>&lt;mio-image index=7&gt;&lt;/mio-image&gt;</p>
<p>Each shape has a default value but you can override it:</p>
<p>&lt;mio-code-snippet index=7&gt;&lt;/mio-code-snippet&gt;</p>
<p>You can <a href="https://m3.material.io/styles/shape/overview" target="_blank" rel="noopener">read more about applying shape</a>.</p>
<h2>Window size classes</h2>
<p>Jetpack Compose and Material 3 provide window size artifacts that can help make your apps adaptive. You can start by adding the Compose Material 3 window size class dependency to your <code>build.gradle</code> files:</p>
<p>&lt;mio-code-snippet index=8&gt;&lt;/mio-code-snippet&gt;</p>
<p>Window size classes group sizes into standard size buckets, which are breakpoints that are designed to optimize your app for most unique cases.</p>
<p>&lt;mio-image index=8&gt;&lt;/mio-image&gt;</p>
<p>See the <a href="https://github.com/android/compose-samples/tree/main/Reply" target="_blank" rel="noopener">Reply Compose sample</a> to learn more about adaptive apps and the window size classes implementation.</p>
<h2>Window insets support</h2>
<p>M3 components, like top app bars, navigation drawers, bar, and rail, include built-in support for window insets. These components, when used independently or with <code>Scaffold</code>, will automatically handle insets determined by the status bar, navigation bar, and other parts of the system UI.</p>
<p><code>Scaffold</code> now&nbsp; supports the <code>contentWindowInsets</code> parameter which can help to specify insets for the scaffold content.</p>
<p>Scaffold insets are only taken into consideration when a <code>topBar</code> or <code>bottomBar</code> is not present in <code>Scaffold</code>, as these components handle insets at the component level.</p>
<p>&lt;mio-code-snippet index=9&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Resources</h2>
<p>With Compose Material 3 reaching stable, it&rsquo;s a great time to start learning all about it and get ready to adopt it in your apps. Check out the resources below to get started.</p>
<ul>
<li>Fully Material 3 and Compose sample <a href="https://github.com/android/compose-samples/tree/main/Reply" target="_blank" rel="noopener">Reply</a></li>
<li>The <a href="https://developer.android.com/jetpack/compose/themes/material3" target="_blank" rel="noopener">Material 3 guidance</a> to start adding Material 3 to your apps</li>
<li>The Material 2 to Material 3 <a href="https://developer.android.com/jetpack/compose/themes/material2-material3" target="_blank" rel="noopener">migration guide</a></li>
<li>The <a href="https://github.com/android/compose-samples" target="_blank" rel="noopener">Jetpack Compose Samples GitHub repository</a>, where you&rsquo;ll find a variety of up-to-date samples using Material 3</li>
<li>The Compose community on <a href="https://stackoverflow.com/questions/tagged/material-design" target="_blank" rel="noopener">StackOverflow</a> and the <a href="http://slack.kotlinlang.org/" target="_blank" rel="noopener">Kotlin Slack group</a></li>
<li>The <a href="https://issuetracker.google.com/issues/new?component=742043" target="_blank" rel="noopener">bug tracker</a>, where you can report an issue and track feature requests</li>
</ul>
<p></p>
<p></p>

Multiple apps using Material Design 3 theming

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/dbeba6c9f26da97a6edd1857a99036cacb48608c996aef76e7643fc32f9135d0e691dc426524bc5ce4877a54a150d6b11519ad628e4f9cb49fae7f8a09ee651b

https://lh3.googleusercontent.com/uqNajkKx7YKEhRZRWUvZGjuoziPV7zqyw5rBZW3OnpAynrqiWwTDEzrprVB9Ip1wktkBJ5BuQQ1Vcx9BsOL6Q3tIOsGFkPLWI1pznkAm6TWZ4DJUvQ

Material Theme Builder to export Material 3 color schemes

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/12e33373a6393e17b13c27393cd2d96dfa5c2c06c3e566157a8faf2a569c2ddd6eab82c9d2072df0118b8126f845f6f4f8b82c277eb80d93b458fc8fc25ea0f9

https://lh3.googleusercontent.com/BT8EcorV03uUW4SdPpdh3gw4d9qV1GTuL01gZglszBZoLDiO7DTy8XEPlguPXQ__zMm7qKrQmyCF4EM-6j9juIYbB5q66kSxdRObF_x7Xa7NG1ZI6A

Reply Dynamic theming from wallpaper

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/23ddbbe9638989fd9aef6989310668cf6611a5393e72f3d30c40065692e0ec3e32932fd635c34ec004fb9d29a5c23495bcf937400ea352b5b161323a4c8edce2

https://lh3.googleusercontent.com/isYinQaWjIX0jX1aZY4i0QWOaKF-EQur83BI6AezKaQVSZ2poPCQi2BPQPvSeSQxmu7Sr_k4iubDvoKARRLSAhY1O0c0jB7K-v2VgefJEyPYqucK1r0

Default Reply app theming

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d0a4f492d9926365b74522ec883672c14f92a78edba37488821cd9b3050650dc1fec8efea087d3b7c3a70f3c228356d6f3564861747b88aea93850f78eb0c88e

https://lh3.googleusercontent.com/WxI5lRgubhlav9dG6WU6-yeSe3lAWuJQ0xuo7l2fMm1HWfcrGhzEbXlGngr99mWaLfvffiAIhhF45KkoopvokP9jOlP0ZVj809u6ZHwuigmlO4rd0i13

Material 3 Switch thumb interaction

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/29b7240faffad1c0e454c3219db2ac2cfefc672defee23694244cc9ce708edb0da463ff165d0ec279b88a0cb8b2b256eb6d5ca815bc7e9492d16b923c50b7b81

https://lh3.googleusercontent.com/9ZWLzSdlen3IzreM8RuT06sQZff--nbaR5vAzxZC8CwQgBit5eIxhGAVT66hmwGZFOn8lgPVx0xbpLJSvOl2-85iOOIHoro0jq1G5MsLK8VYwYJNp2A

ModalNavigationDrawer with content wrapped in ModalDrawerSheet

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/2b853ee1e9a13cfbc6f7a228ab9acdfa23087de61277b2de62345c48ae0a782666ab8db90005bb4deba093a4efdf8424c50a82b25f202dc6b8d0fb322c25cdc9

https://lh3.googleusercontent.com/7ZoGjkeViQgxDGkDzS0kzS5CofQ1RO1c0WL292JLfJE9Kk5Hqu_vCJ4tDGZ2W2opJj9CDJEqAV8kPVyfnlB_6n1l1NnIDnC3tQ0qx4jBmMUwu4QQw5A

Material CenterAlignedTopAppBar with home and action items

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/b6ff5522d8615144687aa155766e0478d2d30faba308c9fb558982cc07fbc7693c6d4b1f09d686abd3c9b5d820c1450499bc18ecddfcec84a288c04efbf65c4e

https://lh3.googleusercontent.com/Z9-ggjETlvW8AR4YsYN8R0L3ooMkhl61Q0ytyUZYgEBj2K-jbl9wY0AIb-qfI98O_RPduFi6aI-ULCBBP0YMg7vXKR2cRvG1tW8oip-NSEoDey0UvecE

Material Design 3 shapes used in various components as default value

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/066c2f42ec2465ad98c207c07c3ec10d3ccb3b1e60905c609f2d14e13bbeb0cfe487f95a68deef94ea054164bd6c4e95584652151c73586c4c62c9c77d3ece5e

https://lh3.googleusercontent.com/Gt8j2lkXa_bMtgZSvKh8GoC8iRjQ9uYlcHXe5NfvBxmXqxGgUFD9AsR9dubzaZKvUeB0SQieplUmpaqW_3fobMs3Dni6ZG4em6_kssnjKoR2sHQHnw

WindowWidthSize Class for grouping devices in different size buckets

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/48cb15bc2b065fe0067a51a62cd548d89feaca4026592a5ad5f4efcb908eed7993e8bd8d62e6d1cee90347d15e2665027391dde4b7f7f02a13cec73bfe9c445f

https://lh3.googleusercontent.com/v8BRFtSQBn-K4TTqtIh5rzjjj6hZSU0bx-2yaZEEMjjswx-IsswH7XIOeOVxfEYibE5GZXEdASkkGTKM86PJ-VE4KhX2B4wHskearQUaOZuJNkKyJVc

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/33ea29222174ae40c2d9d23d3e57bcea4c9d905d1ddd456552c241b3d828cb0aac73c737dc3443f036f074ae5220e906f97cbaed94ed1944d7e2a542fa5d7e91

https://lh3.googleusercontent.com/yYfg__SGRj3ELVT3kcpto_hEBpyDEShR2HyKztmxiYxBIg2AKBokBC03XX8M72Zi2mX4bADa4pcg6PaWGJJ-qyDFAMK0rUJn1eBzdZXilA7cw74K70c

{}

Build Jetpack Compose UIs with Material Design 3 using the Compose Material 3 library, covering color schemes, dynamic color, typography, and shapes.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/9ba519fbd484d143259f4af5cccbf44decb338bfebadbfaf39586d92ffa17e5546027c89ed4267b211a433fe655ef6634430d24b674beba1c3994a15f1a68e04

https://lh3.googleusercontent.com/4fj-dQopOA3exw1wAW4uPlp7AhuYrHFB-ILo3nMuHh-auuyP1XFGk7X45Q7rLql3ZDVLRxxTB61f1ukUoDoiSOTvbv6KWCdjUenjlbRCAmn997cpyQ

Material Design 3 for Compose is now stable

2022-10-24T08:00:00

material-3-compose-stable

Exploring the first stable release of Material Design 3 for Compose

Material Design 3 for Compose is now stable

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/81bc31677758f8fb3d9290c0e069372520fcc958031a42913a7538b54c8375fad5d1f69f1c6394959a91d99e83ae29a408620b14d98aaa71813a0afdd4ad60df

https://lh3.googleusercontent.com/1bE495Z6UCD8NGSYagtDpIh6qW_plIr8QexRWrWZBvra92ShW_WI8XIJr7X208r1fBSpUwHMNW40rjrG7EHXBsbgDIwPoDIelV7p4eEHu3wuDCYwikSN

/blog/relay-in-alpha

Announcing Relay Alpha

Material Blog

Announcing Relay Alpha

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/7988151124048178cc96306b65796531d65b3bf79d709446cfdcdaff03cc9ecb36e2ab5c4413698a3d6a4ad8146a1bbee56e136527fb9e42c8964a1f29300634

https://lh3.googleusercontent.com/5J71k4ejdHyRkjMdbUf6nE02HknqhTkuyHIV5QcLzRbnrF0YiPd2W23GGQj-zKDsU4B5TVrrpVgR3MB8FwDbv-O45ai27Zi9fXHEfCB1ltzj3tyDIxo

https://material.io/blog/material-io-redesign

Magic, utility, and redesigning Material.io

Material Blog

Magic, utility, and redesigning Material.io

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/625f4a428ad5c253046849c2ec9b37d1b2161397d731d4b67348daee7e6ebf4802b1a396f839ce0282c41af24667c5fc6146065f73ddbab5b507635af20c5b09

https://lh3.googleusercontent.com/bwsm18VHLdNCuZejDy5V0HgevLpxGkjHahXXppaX353Bv0g9XxCRFNaxwrN6PirgTshr-VU_ZfnABKJi0rYhWdFGBAUaS3ZDC0VlL9oxbTrX8WLtz5U

/blog/jetpack-compose-beta

Jetpack Compose: Now in Beta

Material Blog

Jetpack Compose: Now in Beta

mio-example
