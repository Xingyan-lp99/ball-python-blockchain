# Material Design 3 for Compose gets new components and features

Source: https://m3.material.io/blog/material-3-compose-1-1
Content endpoint: https://m3.material.io/page-data/Posts/6692554092445696.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/bbdd87316caaeeeb7f0ba8f298914c9653d7a16cef8f034351c268e85fd026331941b46a777f69dea6a13b98319861c4dffba2626783254baa38f656caf90e97

https://lh3.googleusercontent.com/-O3H7G1zcTK5XGtsdS3Gbvg-p9Nm3Y9j6tbaCWdlc4DKEqOmAyscZFlKEDri5oWEr26yOSoGYY7TA0koKn9_yt7JuvN4_YssrJhKj_XSoBrsWk09neM

Gurupreet Singh

Material Design, Developer Advocate

mio-example

```java
BottomSheetScaffold(
   sheetPeekHeight = 128.dp,
   sheetDragHandle = {},
   sheetContent = {
       // Bottom sheet content
   }
) {
   // Scaffold content
}
```

```java
val modalBottomSheetState = rememberModalBottomSheetState()

ModalBottomSheet(
   onDismissRequest = { /*dismiss request*/ },
   sheetState = modalBottomSheetState,
   dragHandle = { BottomSheetDefaults.DragHandle() },
) {
   // Sheet content
}
```

```java
val datePickerState = rememberDatePickerState()
DatePicker(state = datePickerState)

val dateRangePickerState = rememberDateRangePickerState()
DateRangePicker(state = dateRangePickerState)

// Date picker with initial input display mode
val datePickerState = rememberDatePickerState(
   initialDisplayMode = DisplayMode.Input
)
DatePicker(state = datePickerState)
```

```java
val datePickerState = rememberDatePickerState()
val showDialog = rememberSaveable { mutableStateOf(false) }
if (showDialog.value) {
   DatePickerDialog(
       onDismissRequest = { showDialog.value = false },
       confirmButton = {
           TextButton(onClick = { showDialog.value = false }) {
               Text("Ok")
           }
       },
       dismissButton = {
           TextButton(onClick = { showDialog.value = false }) {
               Text("Cancel")
           }
       }
   ) {
       DatePicker(state = datePickerState)
   }
}
```

```java
val timePickerStateHorizontal = rememberTimePickerState()
TimePicker(
   state = timePickerStateHorizontal,
   layoutType = TimePickerLayoutType.Horizontal
)

val timePickerStateVertical = rememberTimePickerState()
TimePicker(
   state = timePickerStateVertical,
   layoutType = TimePickerLayoutType.Vertical
)
```

```java
var text by rememberSaveable { mutableStateOf("") }
var active by rememberSaveable { mutableStateOf(false) }
SearchBar(
   query = text,
   onQueryChange = { text = it },
   onSearch = { active = false },
   active = active,
   onActiveChange = {
       active = it
   }
) {
   // Search result shown when active
   LazyColumn(
       modifier = Modifier.fillMaxWidth(),
       contentPadding = PaddingValues(16.dp),
       verticalArrangement = Arrangement.spacedBy(4.dp)
   ) {
       items(4) { idx ->
         // Search result

       }
   }
}
```

```java
var text by rememberSaveable { mutableStateOf("") }
var active by rememberSaveable { mutableStateOf(false) }

DockedSearchBar(
   query = text,
   onQueryChange = { text = it },
   onSearch = { active = false },
   active = active,
   onActiveChange = { active = it },
) {
   LazyColumn(
       modifier = Modifier.fillMaxWidth(),
       contentPadding = PaddingValues(16.dp),
       verticalArrangement = Arrangement.spacedBy(4.dp)
   ) {
       // Search result content
   }
}
```

```java
PlainTooltipBox(
   tooltip = { Text("Present now") }
) {
   IconButton(
       onClick = { /* Icon button's click event */ },
       modifier = Modifier.tooltipTrigger()
   ) {
       Icon(
           imageVector = Icons.Filled.FilePresent,
           contentDescription = "Present now"
       )
   }
}
```

```java
val tooltipState = remember { RichTooltipState() }
val scope = rememberCoroutineScope()
RichTooltipBox(
   title = { Text("Add others") },
   action = {
       TextButton(
           onClick = { scope.launch { tooltipState.dismiss() } }
       ) { Text("Learn More") }
   },
   text = { Text("Share this collection with friends...") },
   tooltipState = tooltipState
) {
   IconButton(
       onClick = { /* Icon button's click event */ },
       modifier = Modifier.tooltipTrigger()
   ) {
       Icon(
           imageVector = Icons.Filled.People,
           contentDescription = "Add others"
       )
   }
}
```

```java
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun PinnedTopAppBar() {
   val scrollBehavior = TopAppBarDefaults.pinnedScrollBehavior()
   Scaffold(
       modifier = Modifier.nestedScroll(scrollBehavior.nestedScrollConnection),
       topBar = {
           TopAppBar(
               scrollBehavior = scrollBehavior
           )
       },
       content = { /* Scrollable content */}
   )
}
```

```java
@Composable
fun EnterAlwaysTopAppBar() {
   val scrollBehavior = TopAppBarDefaults.enterAlwaysScrollBehavior()
   Scaffold(
       modifier = Modifier.nestedScroll(scrollBehavior.nestedScrollConnection),
       topBar = {
           TopAppBar(
               scrollBehavior = scrollBehavior
           )
       },
       content = { /* Scrollable content */}
   )
}
```

<p>The 1.1 release of <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary" target="_blank" rel="noopener">Compose Material 3</a> is here, bringing new components, improved APIs, and many other updates and enhancements you&rsquo;ve been asking us for. Material Design 3 is the next evolution of Material Design, enabling you to build expressive, spirited, and personal apps. Start using <a href="https://m3.material.io/" target="_blank" rel="noopener">Material Design 3</a> in your production apps today!</p>
<p><em>Note: The terms "Material Design 3", "Material 3", and "M3" are used interchangeably.</em></p>
<h2>New components</h2>
<p>With the 1.1 release, Material 3 Compose provides all types of components needed to make your production-ready apps, with additions like bottom sheet, date and time pickers, and many others. Let&rsquo;s dive into some of these additions.</p>
<p><strong>Bottom sheets</strong></p>
<p>There are two variations of bottom sheet available: standard and modal bottom sheet.</p>
<p>The <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#BottomSheetScaffold(kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.material3.BottomSheetScaffoldState,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,kotlin.Function0,kotlin.Boolean,kotlin.Function0,kotlin.Function1,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)" target="_blank" rel="noopener">standard bottom sheet</a> is great for use cases where you need to interact with both the bottom sheet and main UI region. You can use the standard bottom sheet with BottomSheetScaffold by providing sheet UI in the sheetContent parameter. You can also provide an optional drag handle to easily interact with the sheet.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p>The <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalBottomSheet(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.SheetState,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,kotlin.Function0,kotlin.Function1)" target="_blank" rel="noopener">modal bottom sheet</a> overlays the main UI and can be dismissed when users interact outside of the sheet region, similar to a dialog. It provides clear separation from the main UI, making it easy for users to focus on the sheet content.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>You can use the modal bottom sheet as a standalone component and invoke it using <code>ModalBottomSheetState</code>. The component also provides <code>onDismissRequest</code> function to be invoked on dismiss.</p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p><strong>Date pickers</strong></p>
<p>The 1.1 release also brings brand new date selection components: <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DatePicker(androidx.compose.material3.DatePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.DatePickerFormatter,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.DatePickerColors)" target="_blank" rel="noopener"><code>DatePicker()</code></a> and <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DateRangePicker(androidx.compose.material3.DateRangePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.DatePickerFormatter,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.DatePickerColors)" target="_blank" rel="noopener"><code>DateRangePicker()</code></a>.</p>
<p>&lt;mio-code-snippet index=2&gt;&lt;/mio-code-snippet&gt;</p>
<p>Both the date picker and date range picker support date input mode by updating the <code>initalDisplayMode</code> parameter to input type, which sets the initial display mode to input type. The user can switch back to default selection mode by toggle.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>Compose Material 3 also provides a <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DatePickerDialog(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.material3.DatePickerColors,androidx.compose.ui.window.DialogProperties,kotlin.Function1)" target="_blank" rel="noopener"><code>DatePickerDialog()</code></a> composable to show a date picker in&nbsp; a dialog, with the option to confirm or dismiss it.</p>
<p>&lt;mio-code-snippet index=3&gt;&lt;/mio-code-snippet&gt;</p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p><strong>Time pickers</strong></p>
<p>Compose Material 3 also includes new time picker components for choosing the desired time.</p>
<p>There are two versions available: one with a horizontal layout in which users enter the time using the keyboard, and another with a vertical layout in which users can also use a slide dial to select the time.</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p>Compose provides a single <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TimePicker(androidx.compose.material3.TimePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.TimePickerColors,androidx.compose.material3.TimePickerLayoutType)" target="_blank" rel="noopener"><code>TimePicker</code></a> composable function, where you can define the layoutType parameter to choose between a horizontal or vertical layout.</p>
<p>&lt;mio-code-snippet index=4&gt;&lt;/mio-code-snippet&gt;</p>
<p><strong>Search bars</strong></p>
<p>The 1.1 release brings new search bar components, which provide users the ability to search queries and display dynamic search results.</p>
<p>&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p>Material 3 provides two options, <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SearchBar(kotlin.String,kotlin.Function1,kotlin.Function1,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SearchBarColors,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)" target="_blank" rel="noopener">search bar</a> and <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DockedSearchBar(kotlin.String,kotlin.Function1,kotlin.Function1,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SearchBarColors,androidx.compose.ui.unit.Dp,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)" target="_blank" rel="noopener">docked search bar</a>, to give you the flexibility to choose the right fit for your product.</p>
<p>When active, the search bar expands into a search view that displays dynamic results. The active search bar takes up all available space to display the results, and can also expand to full screen.</p>
<p>&lt;mio-code-snippet index=5&gt;&lt;/mio-code-snippet&gt;</p>
<p>The docked search bar is great for medium to large devices where the search view doesn&rsquo;t need to take up all the screen space and results can be shown in a docked view.</p>
<p>&lt;mio-image index=7&gt;&lt;/mio-image&gt;</p>
<p>The implementation of the docked search bar is similar to the search bar to keep both the components consistent.</p>
<p>&lt;mio-code-snippet index=6&gt;&lt;/mio-code-snippet&gt;</p>
<p><strong>Tooltips</strong></p>
<p>Tooltips are another new addition to the latest 1.1 release. Tooltips are informative text labels that provide additional context to a button or other UI element.</p>
<p>Material 3 provides two types of tooltips: <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#PlainTooltipBox(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.PlainTooltipState,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)" target="_blank" rel="noopener">plain tooltip</a> and <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#RichTooltipBox(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.RichTooltipState,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.RichTooltipColors,kotlin.Function1)" target="_blank" rel="noopener">rich tooltip</a>.</p>
<p>Plain tooltips briefly describe a UI element. Plain tooltips are great for labeling UI elements with no text, like icon-only and field elements.</p>
<p>&lt;mio-image index=8&gt;&lt;/mio-image&gt;</p>
<p>You can use the <code>PlainTooltipBox()</code> composable to add a plain tooltip. To apply the tooltip to any component, wrap the component with the tooltip composable and add <code>Modifier.tooltipAnchor()</code> to the component&rsquo;s modifier.</p>
<p>&lt;mio-code-snippet index=7&gt;&lt;/mio-code-snippet&gt;</p>
<p>Rich tooltips are great for longer texts like definitions or explanations. Rich tooltips provide additional context to a UI element and can include a button or hyperlink.</p>
<p>&lt;mio-image index=9&gt;&lt;/mio-image&gt;</p>
<p>You can have either persistent or non-persistent rich tooltips by providing the isPersistent parameter to <code>RichTooltipState()</code>. To dismiss persistent tooltips, you need to tap outside the tooltip area or invoke the dismiss action on tooltip state.</p>
<p>Non-persistent tooltips will be dismissed automatically after a short duration.</p>
<p>To add rich tooltips, you can use the <code>RichTooltipBox()</code> composable and modify tooltip state to control the visibility of the tooltip.</p>
<p>&lt;mio-code-snippet index=8&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Stable components</h2>
<p>With the 1.1 release, many key components have graduated from the experimental stage and are ready for production apps.</p>
<p>Components like Scaffold, Surface, Navigation drawers, and many others are building blocks of your apps, and you can now be assured that they will not have any major breaking changes.</p>
<p>&lt;mio-image index=10&gt;&lt;/mio-image&gt;</p>
<p>When updating to the latest release, you can remove the <code>@OptIn(ExperimentalMaterial3Api::class)</code> annotation from the stable components.</p>
<h2>Motion and animations</h2>
<p>Material 3 components in Compose come with built-in motion and animations to provide interactive and expressive experiences to users.</p>
<p>Components also provide behavior control to give you flexibility in choosing the animation you need for your product.</p>
<p><strong>Top app bar motion and animation</strong></p>
<p>For top app bars, you can choose between pinned scroll behavior or enter always scroll behavior.</p>
<p>In pinned scroll behavior, the top app bar is always pinned at the top, but changes its container color when content is scrolled.</p>
<p>&lt;mio-image index=11&gt;&lt;/mio-image&gt;</p>
<p>To add the behavior to the app bar, define a scroll behavior <code>TopAppBarDefaults.pinnedScrollBehavior()</code> that links to the scaffold&rsquo;s <code>Modifier.nestedScroll()</code> to listen to the scrolling changes.</p>
<p>&lt;mio-code-snippet index=9&gt;&lt;/mio-code-snippet&gt;</p>
<p>In the enter always scroll behavior, the top app bar disappears when the user scrolls through the content, and shows up again when the user scrolls down.</p>
<p>&lt;mio-image index=12&gt;&lt;/mio-image&gt;</p>
<p>To achieve the enter always behavior, define a scroll behavior <code>TopAppBarDefaults.enterAlwaysScrollBehavior()</code> that links to the scaffold&rsquo;s <code>Modifier.nestedScroll()</code> to listen to the scrolling changes.</p>
<p>&lt;mio-code-snippet index=10&gt;&lt;/mio-code-snippet&gt;</p>
<p>Material 3 provides all these animations as part of the components, with easy ways to customize them for your project.</p>
<h2>Resources</h2>
<p>With the latest 1.1 release, Compose Material 3 is ready for production apps. Check out the resources below for more information:</p>
<ul>
<li>Fully Material 3 and Compose sample: <a href="https://github.com/android/compose-samples/tree/main/Reply" target="_blank" rel="noopener">Reply 💌</a></li>
<li><a href="https://developer.android.com/codelabs/jetpack-compose-theming#0" target="_blank" rel="noopener">Theming in Compose</a> codelab</li>
<li>The <a href="https://developer.android.com/jetpack/compose/themes/material3" target="_blank" rel="noopener">Material 3 guidance</a> to start adding Material 3 to your apps</li>
<li>The Material 2 to Material 3 <a href="https://developer.android.com/jetpack/compose/themes/material2-material3" target="_blank" rel="noopener">migration guide</a></li>
<li>The <a href="https://github.com/android/compose-samples" target="_blank" rel="noopener">Jetpack Compose Samples GitHub repository</a>, where you&rsquo;ll find a variety of up-to-date samples using Material 3</li>
<li>The Compose community on <a href="https://stackoverflow.com/questions/tagged/material-design" target="_blank" rel="noopener">StackOverflow</a> and the <a href="http://slack.kotlinlang.org/" target="_blank" rel="noopener">Kotlin Slack group</a></li>
<li>The <a href="https://issuetracker.google.com/issues/new?component=742043" target="_blank" rel="noopener">bug tracker</a>, where you can report an issue and track feature request</li>
</ul>

Multiple apps using Material Design 3 theming

Multiple apps using Material Design 3 theming

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6b6da2ccf770aa416f2f117ee44a9e477ab6e68d1b9bbf6232ebfcfad2471e6ce5477f6ea9b660b2f267bd345027177e1b1ceef1da0209af5704cb99bda8e7fe

https://lh3.googleusercontent.com/Hrt0nHl7R6uHcbFiWbmPa-HosbPdpFT3xYiKiEV3_manYSKoojun_2uv4rB_D77GfJ7goWsfQm8cnat9tvVfLhP7U7LF1UBUthz_cntbVfwls6A4Xs8

Standard bottom sheet

Standard bottom sheet

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/77f7fe17044a2139fd3a86528e4981a8ee3149632bdb694b87c336a71118ef055e0cb7a825948e6477b7210961ce571a6de25577c7fb7b900858449733e51286

https://lh3.googleusercontent.com/rihApNZWg_567r2XkibXaCbPMUoi4ya6gUUkeFBrLAqERVnfh16hc5DtOWrLsBebFqh6hFGX4farNBP02XhaVV19AR5XfKnbu3_MkvnLEM0zTSolZj8

Modal bottom sheet

Modal bottom sheet

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/756f3e28656bba2203b9355e3d9d3d80a21133f6b24d9b31712d32bee44805c291bbcbb26722e34ff644830e61f4c9cb4702cd1b6eb2479e5c287d586a60b36c

https://lh3.googleusercontent.com/4tEM--mM93iOqZ-4O1JBTarOaF4SiF3nb1nK9hA9mKY33DgLw6RK9t3YRaWhfUUUA9VRdEELyhycc89mqiphANGJdcPyoHhK7caQ_9cbjcMwNUR2gGA

Selection of date pickers

Left: Date picker in input mode, Middle: Date picker in display mode, Right: Date range picker

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/78a266163cf4514bd0c8a3f1f1f82c5389d79b5e34db0e9f927504acf3d3508c6d1b0e90be469ac7053cf1347bb8c465a44d9cd4a1331d34d790c8e7d5752ad2

https://lh3.googleusercontent.com/t_lB-9MPlXlLlkTtQG9fKLeqDvBikAK8E8s50o0qt5BWcv42k-qiem7Ga-LqqF-nutSMg0YqXriP3b0QVKp2xJq0UyHk9iFduGXSpYGrCiUFXR89Rw

Date picker dialog switching between picker and input display mode

Date picker dialog switching between picker and input display mode

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e178ddba94e73f0fb71dc143d5e3911f9c488c58c5abc98a7c1c890c0f09afbb54fb5605f42217403b60beacfb5f7f076d7b8cbf7d00326c852374e05a7d157f

https://lh3.googleusercontent.com/qkNHOHz6ZFWossHsS4STzxlmihni9sqWO6M8nzHfrEYu7yeLSM1C2whRQ8W_q4nJj7f7aTQ02wgquCOIQZqVB2xA1woAKmXewuWNra-xd5CxFYHc_Q

Left: Time picker in vertical layout, Right: Time picker in horizontal layout

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/a5c23f017c4c4af9d03be43951249de322e9b03a009b2bcfc6d8321771930647c5ad3d9bba289787560a5659a2af0823ab1591912978214f4aaf9ab36801bd21

https://lh3.googleusercontent.com/r9uHWAqLRgHwQOQMjSqZlldGdpM82FfenTiPv2f-ZonlSDyY4HSUcA5H79kL74MugaokXB3AvDQv1R-VedaSKozAJMfQ3fZrydkBXFTnTZ4KevPAo8k

Search bar and search result view

Search bar and search result view

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/997a01a29241658415eccefb73ec7be7012c0e4ce645471a0092e6d724c595d843fd71b7b1d91421f718226f634f78cc7ecb06ee1e65ff31255e3bc2d4b24988

https://lh3.googleusercontent.com/AAQu2xACSSDqMw8zPEiQhvT9KGCOvAr47gpB8ujE02E_CxyrUojzbX22y5eibklRQbT7inNqtV9ReCo75BMZwrhSFa94Ds9VLL-WlxwWTWyeL4fZeNA

Docked search bar and search view on a tablet

Docked search bar and search view on a tablet

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/451f3be785c0199f71d25870ce957de200f7961ce0fa8cb8b97acc34380608cfa4dea7e5fab5651b37262c0bc25e3e2bc4a774484377f5624df992f18173e555

https://lh3.googleusercontent.com/A5BFskNiJtnpu2xJYw9cevEukwyTCVQ1ntR42B7GMBn1r8-lxsMA1CtNlxOrD7-NXTsn9LA28zpsGcyuiiS1O-5gBkie550NiMrLnOH3ULlZ-2l05Nx2

Plain tooltip on an icon button

Plain tooltip on an icon button

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/7286b3a2b8eacc9d3c2726e00deabc788d6bb374006d1da9f9e7d4e20afa29b4de5298ecb18b821be4d82dcce24a54b8026a2f35932af4a42bae86b5193f672e

https://lh3.googleusercontent.com/0be1_Ojz3qPiI2xZJj3oirD5dTbt_FMnXqop8u1LvHwTylXo0OIMed-KI076eJCGfjdoj7P84DdM8z9dbQVwBqhMBu-6nsgGkqJpR6i44tvdTKPxtf-p

Rich tooltip with description and text button as action

Rich tooltip with description and text button as action

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/46939090d1340bd16b262e2e36a69eb17d738ea40d9e78b7097c00e98ef629c706719c2fa014059af350a723620d6111a0c772788d845de2186d92a27b50af23

https://lh3.googleusercontent.com/oaCfOW1cPFvGlLFvokdfBtDlxbx5jkQCJqUZfurMh0so6n6Mg-bGWjgr0uYKKm-vQUmsWzJxMVwqD2pxXYeFLHc7Ql-D9RwtAknu0kRLQgvTvBDjKi8

Navigation rail and Navigation drawer

Navigation rail and Navigation drawer

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/c745f0c64a7b83f7e21d416833f691ab19188f7086f137e7eb0803d5dc85c309f090c2d2138b16116450d8a0cd25b95e735c5c5bac1b94a358a9fb0e415e58bf

https://lh3.googleusercontent.com/Hm0xbN7qc4H49z88n1yv4foM80eieMA5SRQCV88E3gdwjEF6dIUGqdj4mBK7TcaCdNAdTe2eOUALWPBKKY_56DwWrV0ay_Jap4vYt0XtsfWpjeaJJYY

Top app bar with pinned scroll behavior

Top app bar with pinned scroll behavior

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/ceaab27d0b5e26042a83f36989b89a7defffbec12707e81ab9b9e64c19f239fe55c2faa362d4da718997f60e173788e9797032467c98160211141f2701f8f231

https://lh3.googleusercontent.com/U1gUUb8937W5VphSnJ3N3zp8UWxcHifADhVNdUwm5slE9SCz0B7lP4AuHvR2KmkUyH-TqcJDhtEOlDiyFQtuVpSF_p8VevQonPixlLK7abUHPV05iGF2

Top app bar with enter-always scroll behavior

Top app bar with enter-always scroll behavior.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/fad145c4dc9c73f36058a42b12555759b00838640c1c485850eda41a57b475d1cabe1d9062ab0b3cdaabd708c13539d70ac44216c70a59f30f1f434cee0c7371

https://lh3.googleusercontent.com/rb0EIvJyXg44CDwYkDuRtGQ2aHpa8jAkiSbf0ybtFxRW8ufCPSkIyk67sMko4HX1nwzJ8XlsegNeDIQUW-aLUWWy8unmDAQJKPC4kyi4fiAQUsWfFw

Animated top app bar

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e1104c6b005ae5416c1c7e8942a523612cc23be0b5bfc3ba030638c047bf694c055a7834175b801323bc354e19a2491e5c917f4012fcc2a328d48ac9edd31e9f

https://lh3.googleusercontent.com/luOy6tCtv9Q6bJsVMD4jbQYdk_vBOTeemCcI5Zp2m88X_Z4FtrobQ7prtNkSevt1O-zZwg-vO5VAo-MGwzCG0IOqf-AkGuqrSmyOHFTtaiAPBvWkViKN

how-to news updates compose components

{}

Explore the latest features and enhancements in version 1.1 and elevate your app's design with Material 3 Compose.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f7d83e61757ba50ca238cd3d123d140b80c3c16052668f4ca4936466221ff16dc2b1e8cc91966967d7216a28a37c984d650bab8f82c65771f5f60422afdae4ca

https://lh3.googleusercontent.com/irhc8X4sPYztq-tZAUMA8dlU9zaxCMvze_jone5F2F6h9IPOXSDNw4uDtAd6IIXrLH28UI1Q7n5zzY-r_RQF2fFdxp-ADncvbDwRvMPs1OTPpdQmj3c

Material Design 3 for Compose gets new components and features

2023-05-10T13:00:00

material-3-compose-1-1

Exploring the 1.1 release of Material Design 3 for Compose

Material Design 3 for Compose gets new components and features

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/65eb24e15db793a9979b3362479941e134cf7e84a8c02f1540c76285b9f5056fa73ee4c8509539daaec7f04f45e7c679939207093d563da44070be712b24ba3f

https://lh3.googleusercontent.com/hDfP5g5Ut41VqyixQKIcr13kE1eayotW7oFOcdXCaZNvtZqC30XZAuIIq2yP_bFx6eBf1sPsFzTEOZ_ij5yWLhKrwhnO3KLzEa8zEgkPUZSPV2lJzg

/blog/material-3-compose-stable

Material Design 3 for Compose is now stable

Material Blog

Material Design 3 for Compose is now stable

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/81bc31677758f8fb3d9290c0e069372520fcc958031a42913a7538b54c8375fad5d1f69f1c6394959a91d99e83ae29a408620b14d98aaa71813a0afdd4ad60df

https://lh3.googleusercontent.com/1bE495Z6UCD8NGSYagtDpIh6qW_plIr8QexRWrWZBvra92ShW_WI8XIJr7X208r1fBSpUwHMNW40rjrG7EHXBsbgDIwPoDIelV7p4eEHu3wuDCYwikSN

/blog/relay-in-alpha

Announcing Relay Alpha

Material Blog

Announcing Relay Alpha

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/431dfac6c5ce89665d484592b44c8066d4b009ee23e07ac7f8e6295313ad9ece46f3b390755cd81685be2f44f2ea784fbe82eefdf5fdd401d8430fc8a4b543cf

https://lh3.googleusercontent.com/hwCFDEfbHlMM92sX1YWje3r5Df9KOiUg-xrF9cZf4YFka-4O83DEv1wYT38uoV509-Oet5dYl0jTXsriDvfN5sTjlLlLbvIsH2vhJNgaZXg3ZCXcwA

/blog/material-3-figma-design-kit

Introducing the M3 design kit for Figma

Material Blog

Introducing the M3 design kit for Figma

mio-example
