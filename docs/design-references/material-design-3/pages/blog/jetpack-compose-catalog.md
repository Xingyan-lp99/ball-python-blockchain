# Introducing the Compose Material Catalog

Source: https://m3.material.io/blog/jetpack-compose-catalog
Content endpoint: https://m3.material.io/page-data/Posts/5254593229094912.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/18a6db2775f36a6a1b0cae6a88e8df282b27cf4a9db808be9c693fd35bdd3314798a1545d32d424a38e33f75b203165168f010c199ce63799b5e91d6309969a3

https://lh3.googleusercontent.com/m-PDSndGA4cUhtNjSl4HXPqXIaHxvYG28BPPcal5dnXUge1Po6SJJw2I3RjrIYyKBY6exL4bXnjaDt9dusnuDVO_anSC8lzVK7pCvWo

Nick Rout

Material Developer Advocate

mio-example

<p>We&rsquo;re excited to announce a new canonical reference of Material Design components, theming, dark theme, and how to implement these features in Jetpack Compose: the Compose Material Catalog.</p>
<p>If you&rsquo;d like to learn more about the Material Design features of Compose, check out our <a href="https://material.io/blog/jetpack-compose-beta">blog post</a>.</p>
<div style="text-align: center; position: relative; padding-bottom: 56.25%; max-width: 100%; height: 0;"><iframe style="border-radius: 16px; position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://www.youtube.com/embed/G3EPHgEKKcA" frameborder="0" allowfullscreen=""></iframe></div>
<h2>Catalog features</h2>
<p>The catalog consists of three main screens: the home screen, the component screen, and the example screen. At any point you can launch the theme picker or &ldquo;more&rdquo; menu from the top app bar. The app also supports dark theme.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<h4>Home screen</h4>
<p>The home screen consists of a responsive grid of Material Components available in Compose&mdash;from floating action buttons to navigation drawers. Tapping on a component launches the component screen.</p>
<h4>Component screen</h4>
<p>The component screen consists of a description of the Material Component and a list of relevant examples implemented in Compose. Tapping on an example launches the example screen.</p>
<h4>Example screen</h4>
<p>The example screen contains an interactive example of the Material Component implemented in Compose.</p>
<h4>Theme picker</h4>
<p>The theme picker and &ldquo;more&rdquo; menu are accessible via the top app bar from any screen.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>The theme picker allows you to pick Material Theming values&mdash;including color, typography, and shape. These values are applied (by animating between the current theme and the new theme) to examples and the app itself, so you can see how components respond to the changes.</p>
<h4>&ldquo;More&rdquo; menu</h4>
<p>The &ldquo;more&rdquo; menu contains links to design guidelines, developer docs, source code, and the issue tracker. These links are specific to the screen you&rsquo;re on&mdash;eg. The source code link shows the source of a composable on the component screen, and the source of a sample on the example screen.</p>
<h4>Dark theme</h4>
<p>The app responds to the system dark theme. You can see Material Dark Theme features in action, like elevation overlays and limited color accents.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<h2>In sync and up-to-date</h2>
<p>The app is available alongside the source code of Compose libraries, ensuring you&rsquo;ll have the latest Compose API changes. Built directly from the code snippets in the API reference docs, you&rsquo;ll receive the latest samples directly in the catalog.</p>
<p>Let&rsquo;s take a look at an example:</p>
<ul>
<li><a href="https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material/material/samples/src/main/java/androidx/compose/material/samples/ButtonSamples.kt" target="_blank" rel="noopener">The compilable <code>ButtonSample</code>&nbsp;stored in AOSP</a></li>
<li><a href="https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material/material/src/commonMain/kotlin/androidx/compose/material/Button.kt" target="_blank" rel="noopener">The <code>@sample</code> tag reference to <code>ButtonSample</code> in the <code>Button</code>&nbsp;KDoc</a></li>
<li><a href="https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#button" target="_blank" rel="noopener">The <code>Button</code> API reference doc showing the <code>ButtonSample</code>&nbsp;code snippet</a></li>
<li><a href="https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material/material/integration-tests/material-catalog/src/main/java/androidx/compose/material/catalog/library/model/Examples.kt" target="_blank" rel="noopener">The app using the <code>ButtonSample</code>&nbsp;as an example for buttons</a></li>
</ul>
<h2>Get the catalog</h2>
<p>You can get access to the app in a variety of formats:</p>
<ul>
<li>Get the app on <a href="https://play.google.com/store/apps/details?id=androidx.compose.material.catalog" target="_blank" rel="noopener">Google Play</a></li>
<li>Download APKs from the <a href="https://github.com/android/compose-samples/releases" target="_blank" rel="noopener">Jetpack Compose samples GitHub repository releases page</a></li>
<li>View the source code on AOSP using <a href="https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/integration-tests/material-catalog/" target="_blank" rel="noopener">Android Code Search</a> or the <a href="https://github.com/androidx/androidx/tree/androidx-main/compose/integration-tests/material-catalog" target="_blank" rel="noopener">synchronized Android Jetpack repository on GitHub</a>. You can also run the app if you&rsquo;ve checked out the code and opened it in Android Studio.</li>
</ul>
<p>Found the catalog helpful? Let us know on <a href="https://twitter.com/MaterialDesign" target="_blank" rel="noopener">Twitter</a>!</p>

Screens in the Compose Material Catalog

Screens in the Compose Material Catalog

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/52783f9086e4abe9ff459cf66512aa06e9d9b87a58d450ffa5741dd20cb84c58e969aa2e0f362bf4d5461cff90278edaa05d8f18b0a78b8aed11b92685c78565

https://lh3.googleusercontent.com/cu90fkIIhQt6dUFBynmoXpBiC_EQDSDmocEd8oFHPtBlWeagHL9m9wbDHUdgD371oR_nrxs3wcik020Vn5bJCXzR7XYr_hnYxCaVGk51XImCg_ftgGg

Theme picker in the Compose Material Catalog

Theme picker in the Compose Material Catalog

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/65ba79920beec836e750bc8d1cf28569e011c9e495690ecd17367119265d5daadf9d78a3db5c5c783f7b571ca049f2c6ccb6614c9e9857152467262d739cf9a1

https://lh3.googleusercontent.com/bgVADi_We_Ncs0GcPReNEgA8K1yKHoytRbMwMZQ0kPATeadb1WZM8LJwRZs-N_SSPq6XlFBO91rN6Tzf_V-4j4T1DILxTmZjIktl_06LCAYU24eWU0E

Dark theme in the Compose Material Catalog

Dark theme in the Compose Material Catalog

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/073ed707ec87d164b8397fd54ae38c2d5bf7416bba8f8dac952b3bf0b0474678bdd86a08ef3029ae740b48fd92e33bead4bad6434c99df36e9b8c91429e0c11b

https://lh3.googleusercontent.com/xyweyVkypn20erzyYn9GN2T-t4sv1SLDi3zBS_3u0x9XD92HZap__ktET11kcA0IzZxuZ3Q8R52nMP7p6Mm1oN15_atYt-eYQHASDEJJln1RQaGM17A

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/662d7826f5c59fe0784e5ccb75730fb90e6013a0b1c4013f1711d47bbab782d9ed47842273cb3fbb15bd4ad3f8bcad2184bdb137e43282cd97de20e4ff4d05d5

https://lh3.googleusercontent.com/EQuO-xaJrUVqix8E0Va2vWxmUWzEUU4rK7uQT_zfmdJaftbcM2g_kDDrJQavRjWpG1emn4uHlaA9AwptudrM_vSXzIbrUOz6NyBixnjGEF_rRTMISlk3

jetpack compose

{}

Discover the latest toolkit for building user interfaces with Jetpack Compose. An overview of the new Material Design catalog for Jetpack Compose.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/cb597c55f553517e69b657edf4ee4d12e07eda6195cf3b4173070790c227055069fd4fb2d6b49e87a8b9ee3e35b4482bbdfab73acf6aa3d58165d6de1e28efff

https://lh3.googleusercontent.com/1XrM4aBqOXnDtEcvzCN3JAck6Xqzj_Clr-ME6Na5QstqMbChZyCrYrR2bETwWT7MSVETgET1qvkR4Q9Hbzq6yq2cXkcA_6ZNF-dERkr9stt-GIfQkQ

Introducing the Compose Material Catalog

2021-05-19T10:30:00

jetpack-compose-catalog

An overview of the new Material Design catalog for Jetpack Compose

Introducing the Compose Material Catalog

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/625f4a428ad5c253046849c2ec9b37d1b2161397d731d4b67348daee7e6ebf4802b1a396f839ce0282c41af24667c5fc6146065f73ddbab5b507635af20c5b09

https://lh3.googleusercontent.com/bwsm18VHLdNCuZejDy5V0HgevLpxGkjHahXXppaX353Bv0g9XxCRFNaxwrN6PirgTshr-VU_ZfnABKJi0rYhWdFGBAUaS3ZDC0VlL9oxbTrX8WLtz5U

/blog/jetpack-compose-beta

Jetpack Compose: Now in Beta

Material Blog

Jetpack Compose: Now in Beta

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/2c074358aa6746e15f10bd31e0cfde430cfd5115c1ff5a28d713d48fcc6b93cc8c7dc2480aa2def8a8f87bf4622d9f8d52404fb226521eedd8c3cc02103e258e

https://lh3.googleusercontent.com/YNs1goLszlHJUXmeQDmp1EmixeNAwvRjwZLMjI78up2AakfLIs0VKX3I0GJtAKbg6Yi-Xm1vbr25gtmt3Ea4NBa7T28ZZKhHYlnj5ETq9uSLMe01v5tW

/blog/material-design-for-large-screens

Introducing Material Design Guidance for Large Screens

Material Blog

Introducing Material Design Guidance for Large Screens

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/a1855288959ded75fda792ccd596416ebd205ee16f68a8b0b1e054aed0240c99c6b13d8bcbe457f859725e39d5f378f63b35246b27bbea55c6489002308fb0e2

https://lh3.googleusercontent.com/7mfszg9J4kovhWrDPVhuc2B59blfpaYgjGRkcXdJwiLePSL5k-aEtmHvZnvBokMbcxss_OUP3LlcjGv_GYf0oi9cqBJmeyVcklA0pbZXkrvVT7kYiA

/blog/material-google-io21

Material Design at Google I/O 2021

Material Blog

Material Design at Google I/O 2021

mio-example
