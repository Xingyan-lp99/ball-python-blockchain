# Material Design 3 for Compose version 1.3

Source: https://m3.material.io/blog/material-3-compose-1-3
Content endpoint: https://m3.material.io/page-data/Posts/5479866587021312.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/cd6a91468c5e1477f6b472e3f9ca79f1b3006d1ca757dc7f6690c42edb200c029d2ce8fc15ecf41abe4451650442df3d05ef74da9c6d28f9c798b901ddb24acd

https://lh3.googleusercontent.com/1S-z4h2BezcxC_iPVU4gOCjitu6gNHVL_PYFku9fxsF6pyAH7CWefXK1HW6yF0X570WHgSdfTEXVInO5oxMVRnkw0Q8wtVnsx_paKDIO6fr2LvYlYQ

Rebecca Franks

Developer Relations Engineer, Android

mio-example

```java
@OptIn(ExperimentalMaterial3Api::class)
@Preview
@Composable
private fun CarouselExamples() {
    data class CarouselItem(
        val id: Int,
        @DrawableRes val imageResId: Int,
        val contentDescription: String
    )

    val items = remember {
        listOf(
            CarouselItem(0, R.drawable.cupcake, "cupcake"),
            CarouselItem(1, R.drawable.donut, "donut"),
            CarouselItem(2, R.drawable.eclair, "eclair"),
            CarouselItem(3, R.drawable.froyo,"froyo"),
            CarouselItem(4, R.drawable.gingerbread, "gingerbread"),
        )
    }

    HorizontalUncontainedCarousel(
        state = rememberCarouselState { items.count() },
        modifier = Modifier.fillMaxWidth()
            .wrapContentHeight()
            .padding(top = 16.dp, bottom = 16.dp),
        itemWidth = 186.dp,
        itemSpacing = 8.dp,
        contentPadding = PaddingValues(start = 16.dp)
    ) { i ->
        val item = items[i]
        Image(
            modifier = Modifier.height(205.dp)
                .maskClip(MaterialTheme.shapes.extraLarge),
            painter = painterResource(id = item.imageResId),
            contentDescription = item.contentDescription,
            contentScale = ContentScale.Crop
        )
    }
}
```

```java
HorizontalUncontainedCarousel(
        state = rememberCarouselState { items.count() },
        modifier = Modifier.fillMaxWidth()
            .wrapContentHeight()
            .padding(top = 16.dp, bottom = 16.dp),
        itemWidth = 186.dp,
        itemSpacing = 8.dp,
        contentPadding = PaddingValues(horizontal = 16.dp)
    ) { i ->
        val item = items[i]
        Image(
            modifier = Modifier.height(205.dp)
                .maskClip(MaterialTheme.shapes.extraLarge)
                .maskBorder(BorderStroke(1.dp, MaterialTheme.colorScheme.secondary), MaterialTheme.shapes.extraLarge),
            painter = painterResource(id = item.imageResId),
            contentDescription = item.contentDescription,
            contentScale = ContentScale.Crop
        )
    }
```

```java
@Composable
fun PullToRefreshDemo() {
    var itemCount by remember { mutableIntStateOf(15) }
    var isRefreshing by remember { mutableStateOf(false) }
    val state = rememberPullToRefreshState()
    val coroutineScope = rememberCoroutineScope()

    val onRefresh: () -> Unit = {
        isRefreshing = true
        coroutineScope.launch {
            delay(1500)
            itemCount += 5
            isRefreshing = false
        }
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Title") },
                // Provide an accessible alternative to trigger refresh.
                actions = {
                    IconButton(onClick = onRefresh) {
                        Icon(Icons.Filled.Refresh, "Trigger Refresh")
                    }
                }
            )
        }
    ) {
        PullToRefreshBox(
            modifier = Modifier.padding(it),
            state = state,
            isRefreshing = isRefreshing,
            onRefresh = onRefresh,
        ) {
            LazyColumn(Modifier.fillMaxSize()) {
                if (!isRefreshing) {
                    items(itemCount) {
                        ListItem({ Text(text = "Item ${itemCount - it}") })
                    }
                }
            }
        }
    }
}
```

<p>Version 1.3 of the Compose Material 3 Components is here and with it come a few changes for Material Components and theming!</p>
<p>Version 1.3 introduces:</p>
<ul>
<li>Behavior changes for ripple APIs for performance improvements</li>
<li>A brand-new component: Carousel</li>
<li>Built-in predictive back support for some Material Components.</li>
<li>Color token alignment to be more colorful while still having accessible color contrast</li>
<li>Previously experimental APIs have been stabilized</li>
</ul>
<h2>Breaking API changes</h2>
<p>To improve performance, the Material components have been migrated to use the new Ripple APIs, and no longer query <code>RippleTheme</code>. If you have set a custom ripple in your applications, you will need to perform a migration to use the new APIs as Material will no longer query <code>LocalRippleTheme</code>. See the &ldquo;<a href="https://developer.android.com/develop/ui/compose/touch-input/user-interactions/migrate-indication-ripple" target="_blank" rel="noopener">Migrate to Indication and Ripple APIs</a>&rdquo; documentation for more information about how to migrate your ripple theme.</p>
<h2>Carousel component</h2>
<p style="text-align: center;">&lt;mio-video index=0&gt;&lt;/mio-video&gt;</p>
<p>Material 1.3 introduces two experimental versions of the <a href="https://m3.material.io/components/carousel/overview" target="_blank" rel="noopener">Material 3 Carousel</a> - <code>HorizontalMultiBrowseCarousel</code> and <code>HorizontalUncontainedCarousel</code>.</p>
<p>The <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/package-summary#HorizontalMultiBrowseCarousel(androidx.compose.material3.carousel.CarouselState,androidx.compose.ui.unit.Dp,androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.foundation.gestures.TargetedFlingBehavior,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.PaddingValues,kotlin.Function2)" target="_blank" rel="noopener"><code>HorizontalMultiBrowseCarousel</code></a> shows at least one large, medium, and small carousel item.</p>
<p style="text-align: center;">&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p style="text-align: center;">&lt;mio-video index=1&gt;&lt;/mio-video&gt;</p>
<p>The&nbsp; <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/package-summary#HorizontalUncontainedCarousel(androidx.compose.material3.carousel.CarouselState,androidx.compose.ui.unit.Dp,androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.foundation.gestures.TargetedFlingBehavior,androidx.compose.foundation.layout.PaddingValues,kotlin.Function2)" target="_blank" rel="noopener"><code>HorizontalUncontainedCarousel</code></a>&nbsp; displays its items at a given size and one item at the end that peeks in to show that there are more items in the list.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>Similar to using the <code>HorizontalPager</code>, the Carousel applies a few design specifications on top of the <code>Pager</code>, such as the parallax effect for item content and how the items on each end should size themselves. An example of using the <code>HorizontalUncontainedCarousel</code> can be found below:</p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p style="text-align: center;">&lt;mio-video index=2&gt;&lt;/mio-video&gt;</p>
<p>As part of the Carousel component, we&rsquo;ve added two new modifiers to <code>CarouselItemScope</code> - <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/CarouselItemScope#(androidx.compose.ui.Modifier).maskClip(androidx.compose.ui.graphics.Shape)" target="_blank" rel="noopener">maskClip</a> and <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/CarouselItemScope#(androidx.compose.ui.Modifier).maskBorder(androidx.compose.foundation.BorderStroke,androidx.compose.ui.graphics.Shape)" target="_blank" rel="noopener">maskBorder</a> - to easily add a shape and border to any carousel item. This is needed over the regular <code>clip</code> and <code>border</code> modifiers to be able to apply it on a container level as the item moves inside the Carousel, if you had to apply the standard <code>clip</code> modifier, the items would be statically clipped and not apply the parallax effect that this component introduces.</p>
<p>For example, if you wanted to surround your Carousel items with a border, you can do so by placing the <code>maskBorder</code> modifier onto the individual item, as well as provide a different shape to the items with <code>maskClip</code>:</p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p style="text-align: center;">&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<h2>Component updates</h2>
<p>The following components have been updated to match the Material 3 specification, there are also contrast updates to these components to improve accessibility out of the box.</p>
<p><strong>Progress Indicator</strong></p>
<p>The <a href="https://m3.material.io/components/progress-indicators/overview" target="_blank" rel="noopener">progress indicator</a> components have been updated to a new visual style to match the Material 3 specification:</p>
<p style="text-align: center;">&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<ol>
<li><a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LinearProgressIndicator(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color)" target="_blank" rel="noopener"><code>LinearProgessIndicator</code></a> is a straight line progress indicator, the visual style has changed to use rounded <code>strokeCap</code> by default, this can be changed with the <code>strokeCap</code> parameter. New parameter for specifying the <code>gapSize</code> between the progress indicator and track is now available. To change or disable the visual indicator at the end - use the <code>drawStopIndicator</code> parameter.</li>
<li><a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#CircularProgressIndicator(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp)" target="_blank" rel="noopener"><code>CircularProgressIndicator</code></a> is a circle shaped progress indicator, the visual style has changed to use rounded <code>strokeCap</code>, this can be changed with the <code>strokeCap</code> parameter. New parameter for specifying the <code>gapSize</code> between the progress indicator and track is now available.</li>
</ol>
<p><strong>Slider</strong></p>
<p>The <a href="https://m3.material.io/components/sliders/overview" target="_blank" rel="noopener">slider</a> component has been updated to a new visual style to match the Material 3 specification, including more prominent handles and an updated shape spec that can be customized:</p>
<ol>
<li>Continuous slider: <code>Slider</code><br />&lt;mio-image index=4&gt;&lt;/mio-image&gt;</li>
<li>Discrete slider: <code>Slider</code> with <code>steps</code> parameter set<br />&lt;mio-image index=5&gt;&lt;/mio-image&gt;</li>
<li>Range slider: <code>RangeSlider</code>&nbsp;<br />&lt;mio-image index=6&gt;&lt;/mio-image&gt;</li>
</ol>
<p><strong>Bottom Sheet</strong></p>
<p>Bottom sheets have been updated to fix bugs and offer improvements to the API. <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalBottomSheet(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.SheetState,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,kotlin.Function0,kotlin.Function0,androidx.compose.material3.ModalBottomSheetProperties,kotlin.Function1)" target="_blank" rel="noopener"><code>ModalBottomSheet</code></a> more accurately draws scrim over status bar when edge to edge is enabled.</p>
<p>Modal bottom sheet content can now consume window insets, allowing for visible content above the navigation bar. <code>ModalBottomSheet</code> parameter <code>windowInsets</code> is renamed to <code>contentWindowInsets</code> to specify where the insets will be applied, and the insets are no longer tied to window logic. In addition, the bottom sheet includes predictive back support.</p>
<p><strong>Pull to refresh API changes</strong></p>
<p>The pull to refresh experimental APIs have been overhauled and updated to fix a few bugs with the component. The updated APIs for <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/pulltorefresh/package-summary#PullToRefreshBox(kotlin.Boolean,kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.pulltorefresh.PullToRefreshState,androidx.compose.ui.Alignment,kotlin.Function1,kotlin.Function1)" target="_blank" rel="noopener"><code>PullToRefreshBox</code></a> simplify the state to use fractional values instead of dp units, and separate out the nested scroll connection from <code>PullToRefreshState</code>. A simple example of using pull to refresh:</p>
<p>&lt;mio-code-snippet index=2&gt;&lt;/mio-code-snippet&gt;</p>
<h2>Predictive back support</h2>
<p>Support for predictive back is now built into some of the Material Components.&nbsp; Predictive back allows a user to swipe left or right on certain components as a way to navigate to a previous destination. Before completing the swipe, the user can decide to continue to the previous view or stay in the current view, where the component will indicate a preview of where going back would take the user.</p>
<p style="text-align: center;">&lt;mio-video index=3&gt;&lt;/mio-video&gt;</p>
<p>The following components will now automatically handle predictive back on devices that support it:</p>
<ul>
<li><code>ModalBottomSheet</code></li>
<li><code>SearchBar</code></li>
<li><code>ModalDrawerSheet</code></li>
<li><code>DismissibleDrawerSheet</code></li>
</ul>
<h2>Color Token Alignment / Tonal Surface Colors</h2>
<p><a href="https://material.io/blog/tone-based-surface-color-m3" target="_blank" rel="noopener">Tone-based surface color roles</a> have replaced the previous &ldquo;surfaces at +1 to +5 elevation&rdquo; approach. The new color roles are not tied to elevation, and offer more flexibility and support for color features such as user-controlled contrast. All Material Components will <strong>automatically update to use the new surface container color roles</strong>.</p>
<p>For developers using the previous opacity-based surface model for custom color mappings, we recommend remapping these to the new roles:</p>
<p style="text-align: center;">&lt;mio-image index=7&gt;&lt;/mio-image&gt;</p>
<p>Instead of using <code>ColorScheme.surfaceColorAtElevation()</code>, use the following colors instead:</p>
<ul>
<li><code>surfaceContainerLowest</code> is a new role</li>
<li>Surface at elevation +1 becomes <code>surfaceContainerLow</code></li>
<li>Surface at elevation +2 becomes <code>surfaceContainer</code></li>
<li>Surface at elevation +3 becomes <code>surfaceContainerHigh</code></li>
<li>Surface at elevation +4 and +5 are being deprecated, it is recommended to use <code>surfaceContainerHighest</code> by default as a replacement. As an alternative <code>surfaceContainerHigh</code>, or <code>surfaceDim</code> can be used depending on the specific use case.</li>
<li>Surface Variant becomes <code>surfaceContainerHighest</code></li>
</ul>
<p>For more information on tone-based surface color roles and the exact changes, see <a href="https://material.io/blog/tone-based-surface-color-m3" target="_blank" rel="noopener">the blog post</a>.</p>
<p>In addition to the introduction of tone based surface color roles, the following color roles have been updated in the default <code>lightColorScheme</code> to be more colorful while still having accessible color contrast:</p>
<ul>
<li><code>onPrimaryContainer</code></li>
<li><code>onSecondaryContainer</code></li>
<li><code>onTertiaryContainer</code></li>
<li><code>onErrorContainer</code></li>
</ul>
<p style="text-align: center;">&lt;mio-image index=8&gt;&lt;/mio-image&gt;</p>
<p>Affected components:</p>
<ul>
<li>Badges</li>
<li>Bottom app bar</li>
<li>Buttons</li>
<li>Common buttons</li>
<li>Extended FAB</li>
<li>FAB</li>
<li>Icon buttons</li>
<li>Segmented buttons</li>
<li>Chips</li>
<li>Lists</li>
<li>Menus</li>
<li>Navigation bar</li>
<li>Navigation drawer</li>
<li>Navigation rail</li>
<li>Switches</li>
</ul>
<p>Promotion of experimental APIs to Stable</p>
<p>The experimental Material components continue to be evaluated and adjusted based on your feedback and bug reports. In this release, we&rsquo;ve graduated more APIs and removed the experimental annotations from:</p>
<ul>
<li><code>SegmentedButton</code> and associated APIs are now stable.</li>
<li><code>SwipeToDismissBox</code> and associated APIs are now stable.</li>
</ul>
<h2>Learn more</h2>
<p>The components or features that are highlighted in these posts are only a subset of the work that lands in each release. Check out the <a href="https://developer.android.com/jetpack/androidx/releases/compose-material3" target="_blank" rel="noopener">release notes</a> for a full listing of all the changes.</p>
<p>You can file <a href="https://issuetracker.google.com/issues/new?component=742043&amp;template=1590761" target="_blank" rel="noopener">bug reports</a> and follow <a href="https://issuetracker.google.com/issues?q=componentid:742043%20status:open" target="_blank" rel="noopener">open issues</a> on Buganizer. You can also follow the progress of new versions on <a href="https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/;bpv=1;bpt=0" target="_blank" rel="noopener">cs.android.com</a>. Install the <a href="https://play.google.com/store/apps/details?id=androidx.compose.material.catalog" target="_blank" rel="noopener">catalog app</a> on Google play to see the latest components in action.</p>

carousel component

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/ea8d1bcf1ca309ed9b551efc093aa49bad27793b251be279c3143db427cef39bbfdf03f1f52a683546a135f4691c98064255f000ab9be5041c74b06821557377

https://lh3.googleusercontent.com/DEPT123BmoDhy3YqCUG8pjPYxj7TeLJaQbk2L2XU2SG1pv6CvdV8ZjKZyx8YyJXmnkrHXLkrNvIxlhkKRREEjq9IadiLj4hh1UUrG6iTgPRcNPP4hg

carousel component with equal width items

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/37f5b44b84bbbec9582165e4216cfad5e527be4992020f5d4ab20bc06453a6f805771bcf6af7e62882b8c615c24a738d6b7be6111f9603790929747ca3cb4d32

https://lh3.googleusercontent.com/eD3MsG445cg94jaQ-XdCmvlgmpufz1OdpUqm1coFKg4RyBBlK1_u_oIQPYYzfIkYm4VAEtdjuRFh7_NKseJ6Es-E0C18V3ZYmtcg5Ek_tdJgl_7_EG3U

carousel with bordered items

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e7d92a25567d6f9ac09ecf9d351e1b67560a5f40f3703aec5215572cb1863199b2c74801b7bbb964a92a1e786c509e76d122aee4a9e452a247fe6c4aba199069

https://lh3.googleusercontent.com/4Mv5AUboQH_OCRrnI5VMutyelAGAvPcM6ydy7PhgOqhihNr0XcxVJOQZfgp6ep6xRakUPJ7w5kc_iEMyxXAHMXUgcYWafPeOzqATriJhG5_WG7dIV-sT

linear and circular progress indicators

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/03e8c13ec798e9b52be28f839ed94e49a3e679e99e5d10dbea7644133613e877bb72707e7edf0e5180bd288040439a9ff59fdd7bc04e936fdb8b024b109fd5cc

https://lh3.googleusercontent.com/jjoVgAzqpayTA72T5Y3mTnR4Ql-5ASIcslSN2ckzWFMzQUncxj7_R4RsZd9yhHLfKX9tJG4D50dQZkD7-C0bf_M5AChp2XG2DzRqbx_MclLJtiKmqNA

continuous slider

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/b4507e6c7f4a989d26149bb84a5fbe9f40b561d5466ae4884af130f70b45d073d91f76ef4b8499615fb70bb310d555ae968531019a481dfa2fcd663ab0c262ae

https://lh3.googleusercontent.com/1OU9xdvZ1ouk40epthZkt3tXGZVQjhrFrsrSQaMWQUHB0NnqG31O9xpNNEVt3r7OHcctqRgdl8ch4KZ8J_UUrpmmtSXtkdYEJ59iroXNMJAT2ey_zAE

discrete slider

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/dba36de65569073ee5e24f407e238f1e4791b2015a1775c6a788e8d4215990f45844a54cb836a2a4313f9870061fde9d027b8c575eaf4eb19c054f6d3a346c12

https://lh3.googleusercontent.com/6JQqGQk4PPb1DizJTjNnThLMQZ6AYvXBh920Jwm5D493QB9FPVL4oYoO3h-otGmHdRpntKFJ2nJLPKS9rrhhASGuGTP-t-7dW5Z5yaUf8OvtHTItZ8Y

range slider

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/3990064589afc1cdf089cfc1c54a07737496ef7e23303a94cd6a210337102e9ee6e3c8056ef152353060f487ee5d75afa8c6a20e26172551090ba0dfdfd28b58

https://lh3.googleusercontent.com/671iyxq3rm67ducjeWnafRj1dWm2LOcmFPdZ2UwJMOdSPRQs4FcOhMinu3B8AY0_QCylAyc3xxEFpHm5SgfQphSi20GS7dVeIzi9hpRRniLxyrPi20E

updated color mapping diagram

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/0bbac53abd055f139f3a97c2be95800bbc934701739390bd9d29c9e5af20e37b407f748066750d3338244b72d21b8d139995b3f766c33ff0ba4ccfe9a9a7e7e9

https://lh3.googleusercontent.com/b94lGmuynALaLTkcyC-d7x8T0eTb9JC-0qZ0aDrTRGpJFwNXTd119F02BaaaTGdPSEf7ndQ3AV60s91UivV_vDzmqW4aK_d0T-12-IcLMjDQvlOnbGk

updated color scheme applied to components

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/fd620db58d5b22c83de19cc8fc4945faaea4d4e08eeed50e371e11b173ee729b22d5a034ceeaaebf50e7c50ef08746fd7c81d23b46dd11e7496df3e92db5f81e

https://lh3.googleusercontent.com/V_JToogTe7oilw8FmfBShEKDTXv_I0lf1rcaLBr6R5yO5wVChnBdmL1LE-dzlDoWQ5Js7eRwQwUAgRuNnCmTxTtR5oaCSiMOdY9qQNoMah5806Ueig

compose_material_3_v1_3_carousel_header.mp4

https://storage.googleapis.com/material-io-design/m2/assets/downloads/f642afa49f4a9005de10c8fe3b55346b3df54172b96d7c6d86282577a42010beff6c79d0b7f8ba1d21d69c6ca3c695504e218cc12aabe6f45bc85a1266ffa338.mp4

compose_material_3_v1_3_carousel_multi_browse_short.mp4

https://storage.googleapis.com/material-io-design/m2/assets/downloads/65ab7ea86de837fd6bfc7171d4350d30d260087f3727ae7d94b3b977010fc3b935487616a8177b331ff04155dc32a0e2dade3a172969648cd551e999987bb628.mp4

compose_material_3_v1_3_carousel_uncontained_short.mp4

https://storage.googleapis.com/material-io-design/m2/assets/downloads/6c041e35c36164d0f08f8cf4f79f58d0707fb887d2482b4587496624671235002f8d8c7a8efb29606bd56de5828db7cc515551016c299f24407ff9d0c46a3268.mp4

lpu8t23e-Bottom_Sheet-Back-3P-1.mp4

https://storage.googleapis.com/material-io-design/m2/assets/downloads/601d3cdba9de5c8790825f1f9edcf6a6ab18a59e11a31700fb822985e494699051a1a986a06f45f210520603fb263972e795810c860c73d180c0ccc123177dee.mp4

Latest releases

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/347fea9807496aa5ad7d28702ca6dcb8727f204af584e53fa35c1d4e4671e2157b43fbd0cf8189f18827088ab3287a7c7395a64fbca6cf225de62fd8e4e15f42

https://lh3.googleusercontent.com/DrLnPC8-STsu-5P55vb_gt03HeiUMVfx4k_KPbiGueXrh1XOuuYzAcacYSFVwlwngMK7IO8rqEZnA0Yge84tQpjWnJsLJo9kzz6ndQ7UJ-TJrE97oRU

news update release libraries compose

{}

Exploring the 1.3 release of Material Design 3 for Compose

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/2351acfd7c4027620589f5d320dc4c9b5dfb83646620de1c87a972ba5fa80384a97ea31aa373d5a8d01d460fc03ab3f163ad52ed03985ecc9703a527e49de68d

https://lh3.googleusercontent.com/6cFXdkRxxo2tMPJV8WwDFQ_O2gWBXbOB8NNXqr-SZlL-12xSXujNrOX6c07UQkdAO8Ck-BII-eCZY-lHgdTv2U8R0O0hGFoleSx-jTBqQuj61wZR7MY

Material Design 3 for Compose version 1.3

2024-09-10T13:00:00

material-3-compose-1-3

Exploring the 1.3 release of Material Design 3 for Compose

Material Design 3 for Compose version 1.3

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/cd8c9e0ca5aa68ef80c0a31efa58c001aa94297e2d136d9cf8f3f3ed343d38c0acc83e523c982a5ca93688f2f31d9bb8b2ec0983afe492c5f279bdb486892112

https://lh3.googleusercontent.com/m5z1z1wKD9x1FNKc0WyO1vMQjH8jrxs3eSkealr2NW3JI-we22rhV787nJc7lbPrxWqzaoiS-JUsuTTztMUJ8t18AoTWmq2ZWVtia4inx_H-MoLqeg

/blog/tone-based-surface-color-m3

Material Blog

Introducing Tone-based Surfaces in Material 3

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/f76a10ef20aa3042fc461583cb2a0ac1ce5df95cdd3478424b0e318c5d8ed57cf9492e0503c8f7a07cf19185a453e248c8b840fd2bacf8f608bf5f18e47a9271

https://lh3.googleusercontent.com/thChzTWq1-LKKAjRUXGxrTTahkLJxqAWrUeSBQdDjM3bGInZtXNffv4t81qGiRuWLyZ15Esjpso-EPYanAZ1seXIfrOnG4qyRtUT5u_5zAkmYL_qwQ

/blog/material-3-carousel-research-design

Material Blog

Reinventing the Carousel

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/431dfac6c5ce89665d484592b44c8066d4b009ee23e07ac7f8e6295313ad9ece46f3b390755cd81685be2f44f2ea784fbe82eefdf5fdd401d8430fc8a4b543cf

https://lh3.googleusercontent.com/hwCFDEfbHlMM92sX1YWje3r5Df9KOiUg-xrF9cZf4YFka-4O83DEv1wYT38uoV509-Oet5dYl0jTXsriDvfN5sTjlLlLbvIsH2vhJNgaZXg3ZCXcwA

/blog/material-3-figma-design-kit

Introducing the M3 design kit for Figma

Material Blog

Introducing the M3 design kit for Figma

mio-example
