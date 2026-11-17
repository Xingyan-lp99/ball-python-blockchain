# Material Design for XR (Developer Preview)

Source: https://m3.material.io/blog/material-design-xr-dev-preview
Content endpoint: https://m3.material.io/page-data/Posts/4514989311131648.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/2325b688601478bc6278df9a9121ec4a232b1cf908495ead3ba795eb31c55ce687ff559c71c8ce02b27aec462fd4ec4c6cde8f11d872ae286f336f6eb65168be

https://lh3.googleusercontent.com/ZaJP3AXmRdBneMpX_gzK6K-wqcR6xypjYskBCfk4edozBiOh9vJAPsXWbyzIN15gAShPrt_7RVCE9b374Yix26WwQnbwWx251CoNTFTb8fwlg16Yfos

Yasmine Evjen

Senior Product Manager

mio-example

<p>Android is expanding into extended reality, so your app can be viewed in 3D space, whether in virtual reality or blended with the user's surroundings through passthrough.</p>
<p>Today, we&rsquo;re releasing the <a href="https://developer.android.com/develop/xr" target="_blank" rel="noopener">Android XR SDK</a> developer preview, a software development kit to let you build XR apps using familiar Android frameworks and tools. This release also includes <a href="https://developer.android.com/design/ui/xr" target="_blank" rel="noopener">Android XR design guidelines</a> and <a href="https://developer.android.com/develop/xr" target="_blank" rel="noopener">developer documentation</a> to help you create immersive experiences.</p>
<p>The <a href="https://developer.android.com/develop/xr/jetpack-xr-sdk" target="_blank" rel="noopener">Jetpack XR SDK</a> allows you to enhance your existing Android app for XR and see it come to life in the Android XR emulator in <a href="https://developer.android.com/develop/xr/jetpack-xr-sdk/studio-tools" target="_blank" rel="noopener">Android Studio</a>. <a href="https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui" target="_blank" rel="noopener">Jetpack Compose for XR</a> provides an easy onboarding to declaratively build spatial UI layouts, with established concepts such as rows and columns. Material Design for XR provides design guidance and code for spatial adaptations of components and layouts, to help you prepare your apps for this new environment.</p>
<p>In addition, we are launching advanced perception capabilities with <a href="https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore" target="_blank" rel="noopener">ARCore for Jetpack XR</a>, as well as <a href="https://developer.android.com/develop/xr/jetpack-xr-sdk#jetpack-scenecore" target="_blank" rel="noopener">SceneCore</a>, our new 3D scene graph library for custom 3D manipulation.</p>
<h2>Android apps in XR</h2>
<p>Android XR is a flexible platform that lets you bring your app into extended reality. <a href="https://developer.android.com/develop/xr/get-started#app-manifest" target="_blank" rel="noopener">Compatible</a> Android mobile and <a href="https://developer.android.com/docs/quality-guidelines/large-screen-app-quality" target="_blank" rel="noopener">large-screen apps</a> will work with no development lift and are automatically available in the Play Store.</p>
<p>If you already have a mobile or large screen app on Android, the Jetpack XR SDK can extend your app into a new dimension by spatializing existing layouts and enhancing your experiences with 3D models and immersive environments. Learn how to <a href="https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing" target="_blank" rel="noopener">bring your Android app into 3D with XR</a>.</p>
<p>The <a href="https://developer.android.com/design/ui/xr/" target="_blank" rel="noopener">Android XR design guidelines</a> provide a roadmap for creating exceptional XR experiences. Explore key considerations, system foundations, and best practices for designing interactions, spatial UI, 3D content, and immersive environments. Learn how to <a href="https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui" target="_blank" rel="noopener">develop UI with Jetpack Compose for XR</a>.</p>
<p>To help you build integrated and boundless experiences, Android XR includes <a href="https://developer.android.com/design/ui/xr/guides/foundations#design-multimodal" target="_blank" rel="noopener">multimodal inputs</a>, and <a href="http://developer.android.com/design/ui/xr/guides/spatial-ui" target="_blank" rel="noopener">spatial capabilities</a>. Users can experience your app in two modes: <a href="https://developer.android.com/design/ui/xr/guides/foundations" target="_blank" rel="noopener">Home Space</a> and <a href="https://developer.android.com/design/ui/xr/guides/foundations" target="_blank" rel="noopener">Full Space</a>. In Home Space, a user is able to multitask with your app running side by side with other apps. In Full Space, your app takes center stage as the focus of the user's experience with full access to the spatial and 3D capabilities of Android XR.</p>
<p>&lt;mio-col-set cols=2&gt; &lt;mio-column&gt; &lt;mio-image index=0&gt;&lt;/mio-image&gt; &lt;/mio-column&gt; &lt;mio-column&gt; &lt;mio-image index=1&gt;&lt;/mio-image&gt; &lt;/mio-column&gt; &lt;/mio-col-set&gt;</p>
<h2>Material Design for XR</h2>
<p>The Material 3 (or M3) library now includes adaptations to help your app stand out in spatial environments. We've also added design guidance for navigation components and layouts, making it easier to create immersive and user-friendly XR experiences.</p>
<p>When designing for XR, you may want to use <a href="http://developer.android.com/design/ui/xr/guides/spatial-ui" target="_blank" rel="noopener">spatial UI</a> to place content in a user&rsquo;s physical or virtual environment. You can break out your app into spatial panels, orbiters, and add spatial elevation.</p>
<p>Spatial panels allow you to take advantage of the infinite canvas that Android XR provides, breaking out your existing UI content into panels that are resizable and moveable by the user. Orbiters are floating UI elements that control the content within spatial panels. They give the app&rsquo;s main content more space, and users can quickly access features while the content remains visible. Adding spatial elevation to a component raises it above the spatial panel on the Z-axis. This can help get a user's attention, create better visual hierarchy, and improve legibility.</p>
<p>Spatial UI behaviors in Material Design components and adaptive layouts will help your app adapt naturally to 3D space.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<h2>XR adaptations</h2>
<p>Android XR gives you the flexibility to design a spacious UI that adapts seamlessly to an unlimited display. If you&rsquo;re building with the latest alpha of Material Design components and <a href="https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary" target="_blank" rel="noopener">adaptive layouts</a>, you may add the <code>EnableXrComponentOverrides</code>&nbsp;wrapper to opt into XR changes in your app. This includes placing navigation controls in orbiters&mdash;such as the navigation rail and navigation bar&mdash;as well as placing panes into spatial panels.</p>
<h3>Navigation rail</h3>
<p>The navigation rail in any Compose layout including <a href="https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation" target="_blank" rel="noopener"><code>NavigationSuiteScaffold</code></a>&nbsp;will automatically adapt to an XR orbiter. For more information, read <a href="https://m3.material.io/components/navigation-rail/xr" target="_blank" rel="noopener">Material Design guidelines</a>.</p>
<p>&lt;mio-col-set cols=2&gt; &lt;mio-column&gt; &lt;mio-image index=3&gt;&lt;/mio-image&gt; &lt;/mio-column&gt; &lt;mio-column&gt; &lt;mio-image index=4&gt;&lt;/mio-image&gt; &lt;/mio-column&gt; &lt;/mio-col-set&gt;</p>
<h3>Navigation bar</h3>
<p>Likewise, the navigation bar in any Compose layout including <a href="https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation" target="_blank" rel="noopener"><code>NavigationSuiteScaffold</code></a> will automatically adapt to an XR orbiter. For more information, read <a href="https://m3.material.io/components/navigation-bar/xr" target="_blank" rel="noopener">Material Design guidelines</a>.</p>
<p>&lt;mio-col-set cols=2&gt; &lt;mio-column&gt; &lt;mio-image index=5&gt;&lt;/mio-image&gt; &lt;/mio-column&gt; &lt;mio-column&gt; &lt;mio-image index=6&gt;&lt;/mio-image&gt; &lt;/mio-column&gt; &lt;/mio-col-set&gt;</p>
<h3>List-detail layout for XR</h3>
<p><a href="https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive" target="_blank" rel="noopener">Compose Material 3 Adaptive Layouts</a> in XR have a 1:1 mapping where each pane becomes an XR spatial panel. Learn more about <a href="https://developer.android.com/develop/ui/compose/layouts/adaptive/list-detail" target="_blank" rel="noopener"><code>ListDetailPaneScaffold</code></a> and <a href="https://m3.material.io/foundations/adaptive-design" target="_blank" rel="noopener">adaptive design guidelines</a>.</p>
<p>&lt;mio-col-set cols=2&gt; &lt;mio-column&gt; &lt;mio-image index=7&gt;&lt;/mio-image&gt; &lt;/mio-column&gt; &lt;mio-column&gt; &lt;mio-image index=8&gt;&lt;/mio-image&gt; &lt;/mio-column&gt; &lt;/mio-col-set&gt;</p>
<h3>Supporting pane layout for XR</h3>
<p><a href="https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive" target="_blank" rel="noopener">Compose Material 3 Adaptive Layouts</a> in XR also have a 1:1 mapping where each pane becomes an XR spatial panel. Learn more about <a href="https://developer.android.com/develop/ui/compose/layouts/adaptive/build-a-supporting-pane-layout" target="_blank" rel="noopener"><code>SupportingPaneScaffold</code></a> and <a href="https://m3.material.io/foundations/adaptive-design" target="_blank" rel="noopener">adaptive design guidelines</a>.</p>
<p>&lt;mio-col-set cols=2&gt; &lt;mio-column&gt; &lt;mio-image index=9&gt;&lt;/mio-image&gt; &lt;/mio-column&gt; &lt;mio-column&gt; &lt;mio-image index=10&gt;&lt;/mio-image&gt; &lt;/mio-column&gt; &lt;/mio-col-set&gt;</p>
<h2>Start building with Material Design for XR</h2>
<h3>Design with the Material 3 Design Kit for Figma</h3>
<p>In the Figma design kit, you&rsquo;ll be able to start designing with navigation components as orbiters.</p>
<p>Download the <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank" rel="noopener">Material 3 Design Kit</a> to get started</p>
<h3>EnableXrComponentOverrides to adapt your existing app</h3>
<p>All M3 Compose UI inside of the <a href="https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/package-summary#EnableXrComponentOverrides(androidx.xr.compose.material3.XrComponentOverrideEnabler,kotlin.Function0)" target="_blank" rel="noopener"><code>EnableXrComponentOverrides</code></a> wrapper will adapt on XR devices. Add the <a href="https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/package-summary#EnableXrComponentOverrides(androidx.xr.compose.material3.XrComponentOverrideEnabler,kotlin.Function0)" target="_blank" rel="noopener"><code>EnableXrComponentOverrides</code></a> wrapper to <a href="https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design" target="_blank" rel="noopener">adapt your app to Material Design for XR</a>.</p>
<h3>Develop spatial UI with Jetpack Compose for XR</h3>
<p>With Jetpack Compose for XR, you can declaratively build your spatial UI layouts using familiar Compose concepts such as rows and columns, including new components, spatial panels and orbiters. Start building with our <a href="https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui" target="_blank" rel="noopener">new subspace and spatial components</a>.</p>
<h2>Designing the future together</h2>
<p>This is our initial developer preview of the Android XR SDK. We&rsquo;re continuing to extend the design and developer tools you know and love to Android XR. We welcome your feedback, and want to make our developer platform work better for you.</p>
<p><a href="https://developer.android.com/develop/xr/support" target="_blank" rel="noopener">Share your feedback</a></p>

Woman standing at a table with 3 apps open around her.

In Home Space, a user is able to multitask with your app running side by side with other apps.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/a61dd3ca641e70ca5baf3ec3aeac459cc52702f116524747e04d9df8276edf2753b08eaa133567bd1d8936c3f2736ada6fe1f8ee39cc8007d70b274548235684

https://lh3.googleusercontent.com/SGb0xm8dlDBTnd2euS-dOVAv_j4O6uk_bCMp7BkQB97dDXQuVn72Dcq3IpOVwjyuMMuHh4RyPzcPR6q4UfgLmPXqjL86G_9Nt7I7PRK7A2oi1Aqr5Q

Woman standing in a virtual moon crater with an app open in front of her. The app has four spatial panels, an orbiter, and a 3D pyramid.

In Full Space, your app takes center stage as the focus of the user's experience with full access to the spatial and 3D capabilities of Android XR.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/ad606f39f2f4bf4f2ce2ca01a92b34ef3be08f2cbc5c09dfd9ad168288f1e02ac191fa52e0c8af3f15d52a8f82f6320ac120116f857ada8bb9f7694997fbddd3

https://lh3.googleusercontent.com/Ntu9h5U4fS56NUU75O-hEvs1maLHRESck4dFrtldYJ2zeuAnVuQeXWkXfBxZbqkj84Brp5T_czmDcXIgWLq3iF1mbcES-TRrhpmmSky2060oSh3NkZhM

Material adaptive layout adjusting between home space and full space modes

Material Design adaptive components and layouts for XR

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/4f41f38bab678bcb790712cdea59b9574e085e910b676fde97eb92b34cb1d5e27abebcff7b72f2414ecf10bfc80ccf4ceece21b8dd22a38a8683ee9287c86249

https://lh3.googleusercontent.com/aKNVM5nF1ukFod-lQUc0SQF_6yF-T5P6UwyAPkkxNeWhyN0c48m3AkAkjs3a1gYk_x9gzJN40NHd95x1MCw2aDK0IjxK5pYwu9P7twKkgBX6rIKpGuw

Home space app with navigation rail

Non-spatialized navigation rail

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/ccf5f40f021057ebd9e66d167bc21740406366a07fbb55694b4b07ed7be74d82f677eab08892b44c5995517c8bb5988739a0cd59832469bca22b45e360d94c01

https://lh3.googleusercontent.com/6n2h_icI8q2ESzqESIQNS69kRNmN2ncZdLRdo8oOUO02JbLKLBrZOKRrba_g54FnormKcqZIz-ggW4_mwLjXc8LHWZMteLe-zpuv5wG88RMPRMS4vg

Full space app with navigation rail

Spatialized (XR-adapted) navigation rail

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/60a86d3cd4dc0c8b56f6ce973812259b93476c7062e2ab659383ab3d958df7a6bccf9e8afe602889ae16bc1cd410ee9262a55c87020db1f7514390adf4bfa11f

https://lh3.googleusercontent.com/z8haeB4KGw8L0GsKnA1ZmokvtnM_Is3vriHC8SbW48bCzDNURkAjNRVwOUA99P_9BVxGKQ5E_njZRBEh1QEE2mFEPluVkSTHMjh10UMnpMPtdet5NlY

Compact layout in home space mode with nav bar

Non-spatialized navigation bar

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/87815ae598cb03824b87dad7fe2453cd48a2572cd8b86bf32c888e7505553976cb2cea23d8ca2240244039ba3f0c459d3784c294384de97f805cc9d2c4fd55ac

https://lh3.googleusercontent.com/oJcnR0EUitzuHwx7o15Pk101VywYBL8aVJsDF-175GTlZ6kUqcJhMW-f8HZ7uoTNZ_i9QWj1OQAtlHbjcfw6EMk_9-KzAYzlkFl2cQdAxlxiw9aipA

Expanded layout in full space with nav bar

Spatialized (XR-adapted) navigation bar

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/4e55bb3291583700ffed5347c4deb078d1f6786e599e669a6e9baab40e9bd82fdbb66e4f2827cd782fd8e4f1fc2f0ec25dbf352fa3fba970abd6904b38acace1

https://lh3.googleusercontent.com/oB6Czgh-4EbsCabSbemY9uBHoAQlbONHRz9AOCwXbVzBwL8dW2mgqCikjkVmQIfkS3FWVPvJWZWvnGXWdGPNot4N6UN4Id5FXcELvIGqAJhYszHWAA

List-detail layout in home space

Non-spatialized ListDetailPaneScaffold

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/3977178467808691b6b6a07062541f8720764b88adadf0e2788e8f752ad22227fb573e7e610f2c8eb15977d1c9a6563ec71b856343f36f7306eda73193dae73b

https://lh3.googleusercontent.com/UQNZ7IU2o0QU_UdKJsqehLTRQNUDnZS_hOoDkQhu8VnSlUcYuWF7ohD5GH_rBbwA8sUOMb8QsjYu_KhQDw57j_HYkA3meoR4bxie8BFOz3NhpGGdbw

List-detail layout in full space

Spatialized (XR-adapted) ListDetailPaneScaffold

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e0bf22722dedf191291177f0922d2b4f6200ba39a7443a458ebedaf57e87da69b3c74b5fb44f615ee09a7cc391e1cf10f3f2cb555b158af6c373e083c38c7cfd

https://lh3.googleusercontent.com/3SZDiYGeMQ6OcrI_jplqKKUuVdhRlh-e6x-8Of-5BWv-8B7hIOW8w8khkYpubXqArQ5h2MXT06XNKcHN7v8jNvasK1OAMf__wUGA7N6fNKcK6dwsFkA

supporting pane layout in home space

Non-spatialized SupportingPaneScaffold

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/a6589a2ebf491bc3181387e68dc70598d5ce92d3be37cac0113a418b2e6e0cd3abe54200d7bf6d81f8ef96d4d5fc00b660b508cf1f308f031acece49ffd1eb0c

https://lh3.googleusercontent.com/B-JqNbwGerfkdwPGe_S407ZHnxcWiObalnK0qBRPfDiSaDew2ScsZqYkybNUz961qd7IhADr67eJDxeVIIQ4nYcYfg4IlfMFjSiGqMUTcllM22Wr828

supporting pane layout in full space

Spatialized (XR-adapted) SupportingPaneScaffold

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/117d9e3da08aaa638b669701fc0f4ca65c25935eaba5768f529a9c1677b889ba7c43f17727e665d8be633669f948a2d99362d86e408aa14aea21ad22c33d01d4

https://lh3.googleusercontent.com/UD_39RYFdzRYFthsxXXgBmjdLOuoT_E3OetgJF9MEHUx1wQxq9aq11NNbeKvdKXQGeFXTzg2Bp8wvJHCW-EeP97_HoNehlL7ruT0gazFOIKp2PpD8kfZ

Featured

spatialized material design layout

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/32b9c080ce9c8c5b975ea492fbe725f4cea10d5a06275c18a3fa94a6c30ec516188742ec41527ed6b928bb27548fe1386094578c47ae078f7aaa502df634d5f8

https://lh3.googleusercontent.com/LmC6YZQHA_FFP9yZNFbLYTedVEd0Yg3CGCd4XLkllaafZWYb6paPqED0tEFAx7o-uLwAEX2gBUqnUs5B8I8-XPCbQ5E1pfJ2usXj8d92AzQ_988aQg8

xr android news material adaptive layout components

{}

Building UI that adapts for XR with familiar frameworks and tools

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f7dac1e0f10a16c766aff0ec71f46c00db6af689ef031ea38c004def4ef3371d90fbb3108237218789b34343a054a831b46fb8f0643089b33541b8bcdeebc706

https://lh3.googleusercontent.com/sVICN2nb1_SgiYrRDKEgVQ5FiW6OJ4MIcTTJc4WDNJGVN3VfKB6EeuJHKCHEkKP8uZW2i0vrOBURzDtj0Z2nWRizKFOhFtQchuj3HPJ-6mmbhDXlGtM

Material Design for XR (Developer Preview)

2024-12-12T13:00:00

material-design-xr-dev-preview

Building UI that adapts for XR with familiar frameworks and tools

Material Design for XR (Developer Preview)

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/431dfac6c5ce89665d484592b44c8066d4b009ee23e07ac7f8e6295313ad9ece46f3b390755cd81685be2f44f2ea784fbe82eefdf5fdd401d8430fc8a4b543cf

https://lh3.googleusercontent.com/hwCFDEfbHlMM92sX1YWje3r5Df9KOiUg-xrF9cZf4YFka-4O83DEv1wYT38uoV509-Oet5dYl0jTXsriDvfN5sTjlLlLbvIsH2vhJNgaZXg3ZCXcwA

/blog/material-3-figma-design-kit

Introducing the M3 design kit for Figma

Material Blog

Introducing the M3 design kit for Figma

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/7abbcfa5ee839d89879701fe8793fabcad6eee0d7b68804464e58dac78821eb2ecb9bdbb8a82972a40f056b867e966897618f36d6d63631b200146b59b8a1d56

https://lh3.googleusercontent.com/khMx4Ahoh9hQi-mXDDhKmK_kRoE0qpYj5dBATOTBKjsCRVJD3cz8UQ4bkTaAZxHuGvjlrGs0WssQzu_icP75PIlmwLuqgxVrBrXkZw7JysAOpZ9D_2a1

/blog/material-3-compose-1-1

Material Blog

Material Design 3 for Compose gets new components and features

mio-example
