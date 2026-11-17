# Jetpack Compose: Now in Beta

Source: https://m3.material.io/blog/jetpack-compose-beta
Content endpoint: https://m3.material.io/page-data/Posts/6465524856520704.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/18a6db2775f36a6a1b0cae6a88e8df282b27cf4a9db808be9c693fd35bdd3314798a1545d32d424a38e33f75b203165168f010c199ce63799b5e91d6309969a3

https://lh3.googleusercontent.com/m-PDSndGA4cUhtNjSl4HXPqXIaHxvYG28BPPcal5dnXUge1Po6SJJw2I3RjrIYyKBY6exL4bXnjaDt9dusnuDVO_anSC8lzVK7pCvWo

Nick Rout

Material Developer Advocate

mio-example

```
// Add dependency in module build.gradle
implementation “androidx.compose.material:material:$compose_version”
```

```
// In Colors.kt

val Navy500 = Color(0xFF64869B)
val Navy700 = Color(0xFF37596D)
val Navy900 = Color(0xFF073042)
val Green300 = Color(0xFF3DDC84)
val Green900 = Color(0xFF00A956)

val LightColors = lightColors(
  primary = Navy700,
  primaryVariant = Navy900,
  secondary = Green300,
  secondaryVariant = Green900
  // Using default values for onPrimary, surface, error, etc.
)

val DarkColors = darkColors(
  primary = Navy500,
  primaryVariant = Navy900,
  secondary = Green300
  // secondaryVariant == secondary in dark theme
)
```

```
// In Type.kt

val H6 = TextStyle(
  fontWeight = FontWeight.Medium,
  fontSize = 20.sp,
  letterSpacing = 0.15.sp
)
val Body2 = TextStyle(
  fontWeight = FontWeight.Normal,
  fontSize = 14.sp,
  letterSpacing = 0.25.sp
)
val Button = TextStyle(
  fontWeight = FontWeight.Medium,
  fontSize = 14.sp,
  letterSpacing = 1.25.sp
)

val Typography = Typography(
  h6 = H6,
  body2 = Body2,
  button = Button,
  defaultFontFamily = FontFamily(Font(R.font.roboto_mono))
  // Using default values for subtitle1, caption, etc.
)
```

```
// In Shape.kt

val Shapes = Shapes(
    small = RoundedCornerShape(percent = 50),
    medium = RoundedCornerShape(0f),
    large = CutCornerShape(
        topStart = 16.dp,
        topEnd = 0.dp,
        bottomStart = 16.dp,
        bottomEnd = 0.dp
    )
)
```

```
// In Theme.kt

@Composable
fun MyTheme(
  darkTheme: Boolean = isSystemInDarkTheme(),
  content: @Composable () -> Unit
) {
  val colors = if (darkTheme) {
    DarkColors
  } else {
    LightColors
  }

  MaterialTheme(
    colors = colors,
    typography = Typography,
    shapes = Shapes,
    content = content
  )
}
```

```
class MyActivity : ComponentActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    setContent {
      MyTheme {
        // Material components like Button, Checkbox, Card, etc.
      }
    }
  }
}
```

```
val scaffoldState = rememberScaffoldState()
val scope = rememberCoroutineScope()
Scaffold(
  scaffoldState = scaffoldState,
  drawerContent = { Text("Drawer content") },
  topBar = {
    TopAppBar(
      title = { Text("Top app bar") },
      navigationIcon = {
        IconButton(
          onClick = {
            scope.launch { scaffoldState.drawerState.open() }
          }
        ) {
          Icon(Icons.Filled.Menu, contentDescription = stringResource(R.string.label_nav_menu))
        }
      }
    )
  },
  floatingActionButtonPosition = FabPosition.End,
  floatingActionButton = {
    ExtendedFloatingActionButton(
      text = { Text("Extended FAB") },
      onClick = { /* Handle FAB click */ }
    )
  },
  content = { innerPadding ->
    LazyColumn(contentPadding = innerPadding) {
      items(count = 20) {
        Card(
          modifier = Modifier
            .fillMaxWidth()
            .wrapContentHeight()
            .padding(16.dp)
        ) { /* Card content */ }
      }
    }
  }
)
```

```
// Background color of components that are primary in light theme, and surface in dark theme 
val primarySurface = MaterialTheme.colors.primarySurface

// Utility for applying elevation overlays to colors
val elevationOverlay = LocalElevationOverlay.current
val color = MaterialTheme.colors.surface
val elevation = 4.dp
val overlaidColor = elevationOverlay.apply(color, elevation)
```

```
// Add dependency in module build.gradle
implementation “androidx.compose.material:material-icons-extended:$compose_version”
```

```
Icon(Icons.Default.Add) // Default == Filled
Icon(Icons.Outlined.Notifications)
Icon(Icons.Rounded.ArrowForward)
Icon(Icons.TwoTone.Menu)
Icon(
   Icons.Sharp.Edit,
   tint = MaterialTheme.colors.primary
)
```

```
// Add dependency in module build.gradle
implementation “com.google.android.material:compose-theme-adapter:$compose_version”
```

```
class MyActivity : AppCompatActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    setContent {
      // We use the MdcTheme composeable instead of MaterialTheme
      // This extracts Material Theming definitions from the current Context
      MdcTheme {
        MyComposable(/*...*/)
      }
    }
  }
}
```

```
// Add dependency in module build.gradle
implementation "dev.chrisbanes.accompanist:accompanist-appcompat-theme:$accompanist_version"
```

```
// Add dependency in module build.gradle
implementation “androidx.compose.animation:animation:$compose_version
```

<p>Today marks the first <a href="http://goo.gle/Compose-Beta-Blog">beta release</a> of <a href="https://developer.android.com/jetpack/compose">Jetpack Compose</a>, Android&rsquo;s modern, declarative toolkit designed to simplify and accelerate UI development. With Jetpack Compose, you can quickly bring your apps to life with less code, powerful tools, intuitive Kotlin APIs, and built-in support for Material Design, dark theme, animations, and more.</p>
<h2>Compose Material</h2>
<p>Jetpack Compose offers an implementation of Material Design and <a href="https://developer.android.com/jetpack/androidx/releases/compose-material">provides</a> all the components you need to create beautiful apps, following the guidance described at <a href="https://material.io">material.io.</a></p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Material Theming</h2>
<p>Jetpack Compose implements <a href="https://material.io/design/material-theming/overview.html">Material Theming</a> and supports <a href="https://material.io/design/color/dark-theme.html">dark theme</a> by default. You can customize color, typography, and shape theming values to fit your product's brand, and get access to convenient functions for working with <a href="https://developer.android.com/guide/topics/ui/look-and-feel/darktheme">system dark theme</a> (like <a href="https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#issystemindarktheme"><code>isSystemInDarkTheme</code></a>, <a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#lightcolors"><code>lightColors</code></a>, and <a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#darkcolors"><code>darkColors</code></a>).</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p>&lt;mio-code-snippet index=2&gt;&lt;/mio-code-snippet&gt;</p>
<p>&lt;mio-code-snippet index=3&gt;&lt;/mio-code-snippet&gt;</p>
<p>&lt;mio-code-snippet index=4&gt;&lt;/mio-code-snippet&gt;</p>
<p>When creating new screens in Compose, you should ensure that you apply your custom <code>MaterialTheme</code> <em>before</em> any UI-emitting Material composables. The Material components (<code>Button</code>, <code>Checkbox</code>, <code>BottomNavigation</code>, etc.) depend on a <code>MaterialTheme</code> being in place and their behavior is undefined without it.</p>
<p>&lt;mio-code-snippet index=5&gt;&lt;/mio-code-snippet&gt;</p>
<p>Check out the <a href="https://developer.android.com/jetpack/compose/themes">Theming in Compose guide</a> for more information, and try the <a href="https://developer.android.com/codelabs/jetpack-compose-theming">Jetpack Compose Theming codelab</a>.</p>
<h2>Material Components</h2>
<p>Jetpack Compose offers implementations of <a href="https://material.io/components">Material Components</a>. See the table below for composables available in the beta release, or check out the full list in the <a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary">API reference</a>.</p>
<table style="border-collapse: collapse; width: 99.6875%; height: 315px;" border="1">
<tbody>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/app-bars-bottom">App bars: bottom</a></td>
<td style="width: 47.84%; height: 21px;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#bottomappbar"><code>BottomAppBar</code></a></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/app-bars-top">App bars: top</a></td>
<td style="width: 47.84%; height: 21px;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#topappbar"><code>TopAppBar</code></a></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/backdrop">Backdrop</a></td>
<td style="width: 47.84%; height: 21px;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#backdropscaffold"><code>Backdrop</code></a></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/banners">Banners</a></td>
<td style="width: 47.84%; height: 21px;"><em>Not available yet</em></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/bottom-navigation">Bottom navigation</a></td>
<td style="width: 47.84%; height: 21px;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#bottomnavigation"><code>BottomNavigation</code></a></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/buttons">Buttons</a></td>
<td style="width: 47.84%; height: 21px;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#button"><code>Button</code></a><br /><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#outlinedbutton"><code>OutlinedButton</code></a><br /><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#textbutton"><code>TextButton</code></a></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/buttons-floating-action-button">Buttons: floating action button</a></td>
<td style="width: 47.84%; height: 21px;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#floatingactionbutton"><code>FloatingActionButton</code></a><br /><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#extendedfloatingactionbutton"><code>ExtendedFloatingActionButton</code></a></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/cards">Cards</a></td>
<td style="width: 47.84%; height: 21px;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#card"><code>Card</code></a></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/checkboxes">Checkboxes</a></td>
<td style="width: 47.84%; height: 21px;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#checkbox"><code>Checkbox</code></a><br /><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#tristatecheckbox"><code>TriStateCheckbox</code></a></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/chips">Chips</a></td>
<td style="width: 47.84%; height: 21px;"><em>Not available yet</em></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/data-tables">Data tables</a></td>
<td style="width: 47.84%; height: 21px;"><em>Not available yet</em></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/date-pickers">Date pickers</a></td>
<td style="width: 47.84%; height: 21px;"><em>Not available yet</em></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/dialogs">Dialogs</a></td>
<td style="width: 47.84%; height: 21px;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#alertdialog"><code>AlertDialog</code></a></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/dividers">Dividers</a></td>
<td style="width: 47.84%; height: 21px;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#divider"><code>Divider</code></a></td>
</tr>
<tr style="height: 21px;">
<td style="width: 47.6832%; height: 21px;"><a href="https://material.io/components/image-lists">Image lists</a></td>
<td style="width: 47.84%; height: 21px;"><em>Not available yet</em></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/lists">Lists</a></td>
<td style="width: 47.84%;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#listitem"><code>ListItem</code></a></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/menus">Menus</a></td>
<td style="width: 47.84%;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#dropdownmenu"><code>DropdownMenu</code></a><br /><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#dropdownmenuitem"><code>DropdownMenuItem</code></a></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/navigation-drawer">Navigation drawer</a></td>
<td style="width: 47.84%;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#modaldrawerlayout"><code>ModalDrawerLayout</code></a><br /><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#bottomdrawerlayout"><code>BottomDrawerLayout</code></a></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/navigation-rail">Navigation rail</a></td>
<td style="width: 47.84%;"><em>Not available yet</em></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/progress-indicators">Progress indicators</a></td>
<td style="width: 47.84%;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#circularprogressindicator"><code>CircularProgressIndicator</code></a><br /><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#linearprogressindicator"><code>LinearProgressIndicator</code></a></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/radio-buttons">Radio buttons</a></td>
<td style="width: 47.84%;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#radiobutton"><code>RadioButton</code></a></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/sheets-bottom">Sheets: bottom</a></td>
<td style="width: 47.84%;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#bottomsheetscaffold"><code>BottomSheetScaffold</code></a><br /><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#modalbottomsheetlayout"><code>ModalBottomSheetLayout</code></a></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/sheets-side">Sheets: side</a></td>
<td style="width: 47.84%;"><em>Not available yet</em></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/sliders">Sliders</a></td>
<td style="width: 47.84%;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#slider"><code>Slider</code></a></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/snackbars">Snackbars</a></td>
<td style="width: 47.84%;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#snackbar"><code>Snackbar</code></a><br /><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#scaffold"><code>Scaffold</code></a></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/switches">Switches</a></td>
<td style="width: 47.84%;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#switch"><code>Switch</code></a></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/tabs">Tabs</a></td>
<td style="width: 47.84%;"><code><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#tab">Tab</a></code><br /><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#tabrow"><code>TabRow</code></a><br /><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#scrollabletabrow"><code>ScrollableTabRow</code></a></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/text-fields">Text fields</a></td>
<td style="width: 47.84%;"><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#textfield"><code>TextField</code></a><br /><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#outlinedtextfield"><code>OutlinedTextField</code></a></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/time-pickers">Time pickers</a></td>
<td style="width: 47.84%;"><em>Not available yet</em></td>
</tr>
<tr>
<td style="width: 47.6832%;"><a href="https://material.io/components/tooltips">Tooltips</a></td>
<td style="width: 47.84%;"><em>Not available yet</em></td>
</tr>
</tbody>
</table>
<p>These components can be combined&mdash;using layouts and composables like <code>Scaffold</code>&mdash;as the building blocks for beautiful UIs.</p>
<p>&lt;mio-code-snippet index=6&gt;&lt;/mio-code-snippet&gt;</p>
<p>Check out the <a href="https://developer.android.com/jetpack/compose/layout">Layouts in Compose guide</a> for more information.</p>
<h2>Dark theme</h2>
<p>Material composables that make use of a <code>Surface</code> (like <code>Card</code>, <code>TopAppBar</code>, etc.) automatically include dark theme properties like desaturated colors for accessibility, elevation overlays, and limited color accents. You can also incorporate these in custom scenarios.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>&lt;mio-code-snippet index=7&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Material Icons</h2>
<p>Jetpack Compose also provides a convenient means of using icons listed in the <a href="https://material.io/resources/icons">Material Icons tool</a>, including all icon styles&mdash;filled, outlined, rounded, two-tone, and sharp. With this artifact, you can use icons directly, without the need to download SVGs and convert them to <code>VectorDrawable</code>s in Android Studio.</p>
<p>&lt;mio-code-snippet index=8&gt;&lt;/mio-code-snippet&gt;</p>
<p>&lt;mio-code-snippet index=9&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Interoperability</h2>
<p>Jetpack Compose is designed to work with Android Views. If you're building a new app, the best option might be to implement your entire UI with Compose. But if you're modifying an existing app, you might not want to migrate your app straight away. Instead, you can combine Compose with your existing UI design and adopt it at your own pace.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>If you&rsquo;re using <a href="https://github.com/material-components/material-components-android">Material Components for Android</a> in your app&mdash;in particular <a href="https://material.io/develop/android/theming/theming-overview">Material Theming</a>&mdash;the <a href="https://github.com/material-components/material-components-android-compose-theme-adapter">MDC-Android Compose Theme Adapter library</a> allows you to easily re-use the color, typography and shape definitions from your existing XML themes, from within your composables, so you don&rsquo;t need to declare them again and have a single source of truth.</p>
<p>&lt;mio-code-snippet index=10&gt;&lt;/mio-code-snippet&gt;</p>
<p>&lt;mio-code-snippet index=11&gt;&lt;/mio-code-snippet&gt;</p>
<p>If you&rsquo;re using <a href="https://developer.android.com/jetpack/androidx/releases/appcompat">AppCompat</a>, you can access similar functionality by using the <code>AppCompatTheme</code> composable from the <a href="https://github.com/chrisbanes/accompanist/tree/main/appcompat-theme">AppCompat Compose Theme Adapter library</a>.</p>
<p>&lt;mio-code-snippet index=12&gt;&lt;/mio-code-snippet&gt;</p>
<p>Check out the <a href="https://developer.android.com/jetpack/compose/interop">Compose interoperability guide</a> for more information.</p>
<h2>Resources</h2>
<p>With Jetpack Compose reaching beta, it&rsquo;s a great time to start learning all about it and get ready to adopt it in your apps. Check out the resources below to get started.</p>
<ul>
<li>Develop knowledge and skills at your own pace with the <a href="https://developer.android.com/courses/pathways/compose">Jetpack Compose Pathway</a>, through sequential learning experiences that include articles, codelabs, quizzes, and videos.</li>
<li>Visit the <a href="https://github.com/android/compose-samples">Jetpack Compose Samples GitHub repository</a>, where you&rsquo;ll find a variety of up-to-date samples including Material Studies like <a href="https://github.com/android/compose-samples/blob/main/Owl">Owl</a>, <a href="https://github.com/android/compose-samples/blob/main/Crane">Crane</a>, and <a href="https://github.com/android/compose-samples/blob/main/Rally">Rally</a>.</li>
<li>Get setup using the <a href="https://developer.android.com/jetpack/compose/setup">Android Studio with Jetpack Compose guide</a>.</li>
<li>View the <a href="https://www.youtube.com/watch?v=7alO6TQDWQQ">Converting an existing app screen to Jetpack Compose video</a> on the Material Design YouTube channel.</li>
<li>Join the Compose community on <a href="https://stackoverflow.com/questions/tagged/android-jetpack-compose">StackOverflow</a> and the <a href="http://slack.kotlinlang.org/">Kotlin Slack group</a>.</li>
<li>Report an issue and track bugs on the <a href="https://issuetracker.google.com/issues/new?component=612128">bug tracker</a>.</li>
</ul>
<p></p>

GIF showing a Material Design button changing color and shape

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/3c735cd06e202b11f589a29753686402d73575272cfe82a419a1873b27c00dee8f88bd397bca5fe657bc6f83a78092d5f370edc9704be4752f0a4349c84b41a6

https://lh3.googleusercontent.com/vLxDu0mrTDm234ff2xoxEKAG2xSDBTYByQ9TF8LyulfKL5nGB7z7PHVrKu3kRoJHj0OPGQHMTYT4_B0ck3XbuCcYETBS1waVNWVuUA

Illustration of a UI showing light theme and dark theme

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/a35417b2f5149cd246dfcd53cdee893dd78584380905347ac8100c20246edf4e16e4531e2e892af5277d2569a83960727444aaeca73aafa174c0b984ebf82161

https://lh3.googleusercontent.com/x4KQQg07DrfuqIaz3E2XwAROxv8uIl202z1IXXV0o0ew5lFwpgZiBAQW_WxQwFELX3DSj8DANWGQHDGyFW_P9mWfk05u1JSismQdmQ

Diagram describing the MDC-Android Compose Theme Adapter

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6cc760d13b620742da7459ffab182afd58309b8fbca5089c52065483c4ff6ba8c943c57a00a51830f06b5966f0b424522bef436636b08f6fac837010523966a7

https://lh3.googleusercontent.com/hbc3QhQITj-iic8Ju7WYvvWGIY7XSuM5SU0ipdy2xtlypGna4sYYMKTpXAPElpMH8Ho-6hWUmxbolCpWAGlxELNQ3CRS6mB1UNTvH44

abstract illustration

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/3a04e4395e727469ead49ebede1675d02dda05375e4c790d33b3b8270707d01a4307062d9bc2abdd66c9dbc33bf9d4ca375268cf3f024cf9b77c56ce93ab1a43

https://lh3.googleusercontent.com/IGVvFnjHRRbphKVi5QL8VrdI1ou4bgUIdWpt0CCHXweVBIwydrpun88kL73-kFg0UeGL2mxwxv6K1EIVIBn4IYiV_2bWT-853MCB

Android News Beta Releases Material-Components Theming

 

{}

Exploring the first beta release of Android’s modern, declarative toolkit for UI development

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/005ec31018cec2e96e6bdee90aac2ed71baab67178b1ca39e190f93057259223b4904d3563f429ebd2d411269c45d37d3110e7e27cf71a4bc49efa62f4038e25

https://lh3.googleusercontent.com/qQp1eE3El4FapGaNPVtDhZKRRhtPEmAir3Nvl7ItENTTM_Lvs-4JgryYqMQtNOSqCpuWL7i-gu5gavsXwkMCQqbqIk2ONqXsk0zA

Jetpack Compose: Now in Beta

2021-02-24T09:30:00

jetpack-compose-beta

Exploring the first beta release of Android’s modern, declarative toolkit for UI development

Jetpack Compose: Now in Beta

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/60c164acbca4d5313fd9d84450270d614cc28c31cb44ab37e0632fb97450f3b3d852948575a0b0350da13116e96d60469c7433c2d1a1f702fbf191e91565bb02

https://lh3.googleusercontent.com/FWxaH8D0_U1-GqevsM7mw2ESdajTqa7W5MDb6rjZEqnKlW94JSuxpDIKcBlfEA9s9BqvcMB962KR6Zj9OLmF2n1inkReDg1fRLEf3p4

/components

Components

Material Components

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/5819e7635398fe701440954c645d29e6dce64b9fc5f8a42a4b3ad42d96ac2bdc51f26c4d0f4ea2746af4b7501945f9fe5733c354690c1664a9ea95a9ad1e4163

https://lh3.googleusercontent.com/sXsu9m_NFwnYBOfbUlfn2bPDr2r3MfXKg6wTExfeZgnOflBUnmR5SARk-teM-kE2UxQpKSlAV35SKUaRw2kWAEOYgEIrSe44lpAPXQ

/design/material-theming/overview.html

Material Theming

Theming overview

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/8d86c03a697cda71fef8a635511beaac0afd8cc1525bf9a58c463604c04d94043442e5514c69c0b290fbed89e0381818b473f41f31caa2ff6cd5e83c31a5b0ce

https://lh3.googleusercontent.com/P5yuAkqJt699qGbcw1uLTOHMdzLMnMI6m7I_Ig75FALDP3eS4m0mYKkxfespu53DvHtu16YorQznqZuaLYVI8eDsTCjn3p_zXGdI-g

/blog/dark-theme-design-tutorial-video

Material blog

Craft a Dark Theme

mio-example
