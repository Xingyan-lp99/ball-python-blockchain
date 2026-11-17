# Start Here: 5 Exercises to Prepare Your App for Large Screens

Source: https://m3.material.io/blog/5-steps-large-screen-apps
Content endpoint: https://m3.material.io/page-data/Posts/5176362010411008.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/114b4e6d76018c7e7e36de47f8158a7d71794d04f1a575e31408803c59ba962ac3b15579c1534fce4b47bcccb7fb81f590aff7676a92c371b704a7732e05fed7

https://lh3.googleusercontent.com/2AT_TIxyMX0Inqd9Rk4ejaFoRmOOczEwM9E5xz4DfYxaUqgdkXsCRKOX3uHYFOjyU9VwwFzGGCsZnf6BYmkPP0x3OjztRk02SB3O_HOBLz_vXdvoi2g

Liam Spradlin

Senior UX Designer, Material Design

mio-example

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/5b757f2ed7210e779d77346eddc88ed40238418238630c87c9bfd943dd5bf9ccd2adb1df160a9dacb421914e95f89e3458b94cde071ef4f4b7e43a06a6265742

https://lh3.googleusercontent.com/nKT1lKuwsonPY_QPYho3XMi042O7965QmCpIKNq1h3SbkHXCHZ53Z85zoeHmvQDUo8-MJlH3AKdWWPrBq8iRvT9jZRZj40ZeYmL4YvO1aokKmF9AIA

Rody Davis

Material Developer Advocate

mio-example

<p>As developers build apps that work on more than one type of device, and with the introduction of new form factors like foldables, the need for responsive apps that work well at every size has never been greater. To that end, Material Design recently introduced a comprehensive update to layout guidance and components that expands the system&rsquo;s adaptive capabilities to help prepare your apps for all kinds of screens.</p>
<p>To accompany <a href="https://events.google.com/io/session/b2f0dee6-b649-4e20-8ad6-69266e353f05?lng=en">our talk at Google I/O 2021</a>, this post will walk through 5 things to prioritize when adapting your app for large screens, without requiring a full redesign or rewrite.</p>
<h2>1: Conceptualize your column grid</h2>
<p>The first step in preparing your app is conceptualizing a column grid. If you&rsquo;re building for the web, the notion of a column grid (and its importance) may already be familiar to you, but if not you may be wondering, &ldquo;why use columns?&rdquo; Columns are a great way to conceptualize interface designs for a few reasons.</p>
<p>First, they create a convenient structure for aligning elements of your layout. Column grids have been in use in print and graphic design for a long time, and that&rsquo;s because they create the structure that print layouts need &ndash; helping make printed materials ergonomic and maximally readable. Printers have used and refined these layouts to help their users &ndash; readers or viewers &ndash; get the most out of the material, and we can use them to the same ends in interface design.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>Right now, many apps consider the screen to consist of one big canvas or column, with elements primarily stacked on top of one another, or constrained to the left or right side of the layout, but ultimately drawn in relation to one another in horizontal and vertical terms. This approach can work well in small or narrow screens, but the problems begin to become obvious at larger sizes.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>Applying a column grid to the layout allows for a large-screen experience that feels more intentionally organized. Elements on screen are organized relative to each other and the overall layout in a way that directs the user&rsquo;s eye along a specified route according to the content&rsquo;s informational hierarchy. This makes the experience feel more organic to the device and context.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>The column grid also helps to respond across screen sizes, large and small. In our example (from Fortnightly, a Material Study app), we can see that the layout comprises three primary regions: the photo, the headline and metadata, and the body of the article.</p>
<p>Since each of these regions spans four or more columns in our large-screen layout, we can easily reflow them into a vertical orientation for mobile, maintaining the same information hierarchy along the way.</p>
<p>To start conceptualizing a column grid in your own layouts, grab our <a href="https://www.figma.com/community/file/778763161265841481">Material Design Kit</a> from the Material Figma Community, as well as your latest mockups. Begin to move your elements onto a sample column grid from the Design Kit, exploring how the elements align.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>Check out our <a href="https://material.io/design/layout/understanding-layout.html"><em>understanding layout</em></a> and <a href="https://material.io/design/layout/responsive-layout-grid.html"><em>responsive column grid</em></a> spec articles for detailed information on designing for full responsiveness.</p>
<p>To implement a column grid you can use flexible layouts. When using a row you can specify weights or flex values for each column in the row to have it flex predictably. On android this can be accomplished using the RecyclerView by creating a horizontal chain. You can visit the <a href="https://developer.android.com/training/constraint-layout">Android Developers site</a> to learn more.</p>
<h2>2: Create a composition that scales</h2>
<p>When adapting your designs for large screens, be sure to keep visual composition in mind. On a larger screen, information hierarchy is crucial. The greater screen space means that more information will naturally be present on screen. Since the information won&rsquo;t all be vertically oriented, it&rsquo;s important to create a visual composition that strengthens information hierarchy, giving users a sense of which elements are related &ndash; through style, proximity, etc. &ndash; and how they fit together in an interactive context.</p>
<h4>Layout regions</h4>
<p>One way that we think about this in Material is to construct a scaling layout using what we call layout regions.</p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p>When working on guidance for large screens, we looked at the most common elements of an app&rsquo;s overall layout, and came up with a way of thinking about them that allows for consistent responsive behavior.</p>
<p>We then divided the screen into three primary regions, with the first being the body region.</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p>In our example from Fortnightly, that would be the article content. This container is based on the column grid from before, and has flexible margins and widths defined by the breakpoints described in the <a href="https://material.io/design/layout/responsive-layout-grid.html#breakpoints"><em>responsive layout grid</em></a> article.</p>
<p>Next is the navigation region, which is comprised of navigational components to move the user between destinations and trigger key actions. It maintains a consistent width of 256dp when expanded and 72dp when collapsed. This container edges into the screen, condensing the dimensions of the body container.</p>
<p>&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p>In our example, you can see how the body of the article is now slightly more narrow to accommodate the fully expanded navigation container.</p>
<p>Finally, we have the app bar, which gives users access to key actions like opening and closing the navigation region, searching, or moving to supporting destinations.</p>
<p>&lt;mio-image index=7&gt;&lt;/mio-image&gt;</p>
<p>Now our example is feeling like a more complete and comprehensive layout. The three regions of the screen are clear, and we can reasonably predict how they&rsquo;ll look at other sizes.</p>
<p>With the basics laid out, it&rsquo;s important to reflect on the internal composition of these layout regions. As screen size increases, screen space increases as well. As more information appears on screen to fill this space, it becomes more important to give that information structure and hierarchy so that the user&rsquo;s mental model of it is maintained.</p>
<p>We&rsquo;ve identified two main techniques for grouping information inside these elements that can be helpful as you think about the layout of your own app.</p>
<h4>Visual grouping</h4>
<p>The first is visual grouping, or putting related elements together&mdash;whether they have similar content, functionality, or meaning&mdash;by the use of open space and typography.</p>
<p>&lt;mio-image index=8&gt;&lt;/mio-image&gt;</p>
<p>You may already be using this technique in your app today if, for example, you&rsquo;re using a ListView or GridView on Android, which can be combined with Material cards or tiles.</p>
<h4>Containment</h4>
<p>The second technique, containment, can be a more explicit approach that relies on clear boundaries, either through elevation or visible dividers, to achieve the same effect as the more implicit visual grouping.</p>
<p>&lt;mio-image index=9&gt;&lt;/mio-image&gt;</p>
<p>Material offers many components that implement containment techniques by default.</p>
<h2>3: Use the right components for the job</h2>
<p>Adapting to large screens means adapting to the ergonomics and size constraints of more form factors. With our recent updates, articles for 14 Material components have been updated to describe how they behave when scaling across devices.</p>
<h4>Visual presentation</h4>
<p>The first method of adaptation described for Material components is &ldquo;visual presentation.&rdquo; This can include changes in scale and placement of the elements on screen, as well as their relationships to one another. For example, a text list on mobile may adjust its margins, vertical spacing, and density to more appropriately fill space on a tablet screen. This type of adaptation is crucial when moving between screen sizes, as it preserves the user&rsquo;s understanding of how each element behaves and maintains usability.</p>
<p>One way this is implemented is through size constraints. Most Material components have minimum and maximum dimensions, and several components (including buttons, text fields, and sheets) have been updated for Android with corresponding default Max Width values.</p>
<p>&lt;mio-image index=10&gt;&lt;/mio-image&gt;</p>
<p>Snackbars, for example, have minimum and maximum dimensions on small and large screens. On small screens, the snackbar can expand upward to accommodate its messaging, while on larger screens, it expands horizontally to keep its content on one line while utilizing available space.</p>
<p>&lt;mio-image index=11&gt;&lt;/mio-image&gt;</p>
<p>Similarly, dialogs can expand horizontally on large screens to support their content, reaching a max width that keeps in mind the readability of longer line lengths. At this max width, it can expand vertically up to a maximum height.</p>
<p>As a developer, you can also take advantage of components&rsquo; ability to use fixed or fluid dimensions, based on what makes sense for your layout, within each component&rsquo;s size constraints.</p>
<h4>Component swapping</h4>
<p>Component swapping is another, more rare type of adaptation in which functionally equivalent components can actually swap with each other to meet the ergonomic expectations of different devices.</p>
<p>&lt;mio-video index=0&gt;&lt;/mio-video&gt;</p>
<p>For example, a bottom navigation bar may switch to a navigation rail on tablets, putting the same nav destinations at easier reach, and opening up more vertical space for your layout on horizontally-oriented screens.</p>
<p>The transformation may continue by swapping to a Navigation Drawer on larger screens to provide quicker access to secondary destinations, with more descriptive labels. On Flutter, this set of transformations can be implemented as an automatic behavior using the <a href="https://pub.dev/packages/adaptive_navigation">adaptive_navigation</a> package.</p>
<p>Components can switch types as well. For example, a full-screen dialog on mobile can&nbsp; be exchanged with a simple dialog on larger screens. This component change maintains the function of the dialog, while also making use of screen space in a way that preserves a user&rsquo;s context by revealing underlying content.</p>
<p>&lt;mio-image index=12&gt;&lt;/mio-image&gt;</p>
<p>Use caution when swapping components by ensuring that the interchangeable components are functionally equivalent. Do not, for example, swap a button for a chip. Use caution when changing between list items and cards. The component swap should always serve a functional and ergonomic purpose for the user.</p>
<h2>4: Ensure your app maintains continuity</h2>
<p>When adapting your app for large screens, make sure the experience does not break when the device configuration changes. There are multiple events to look out for such as screen resize, orientation change, or fold and unfold.</p>
<p>Fold and unfold events will usually trigger the &ldquo;screenLayout&rdquo;, &ldquo;screenSize&rdquo; and &ldquo;smallestScreenSize&rdquo; events. Since your configuration is subject to change, it&rsquo;s important not to cache or hardcode any values about display size, window size or orientation since they will change at runtime.</p>
<p>To ensure the best experience across configuration changes make sure to save info regarding scroll position, text that has been input in text fields, current component state such as a video playback position and other interactive aspects.</p>
<p>For more information on saving UI states in Android, check out the <a href="https://developer.android.com/topic/libraries/architecture/saving-states">Android Developers site</a>.</p>
<h2>5: Test input support for touch, keyboard, mouse, and more</h2>
<p>When adapting for large screens there will be many new forms of input to account for. For example, consider keyboards, mice and trackpads, and the ergonomics of touch input on different screens. When running on some large screens your app could even be interacted with exclusively through a gamepad or a remote control with a directional input.</p>
<p>If you're building for Android, the Android Developers site has more information on accounting for <a href="https://developer.android.com/training/game-controllers">game controllers</a> as well as <a href="https://developer.android.com/training/gestures/movement">mice/pointers</a>.</p>
<p>Testing for these input types will allow you to keep in mind the particular expectations of each form factor. For example, a hardware keyboard will mean that part of your layout will no longer be hidden when a text field is active.</p>
<p>Finally, more input types will also mean more states to account for such as hover and focus.</p>
<p>Have more questions? Reach out to us <a href="https://twitter.com/materialdesign">on Twitter @MaterialDesign</a> any time!</p>

Layout organized in a single column

Layouts that consider the screen as one big canvas often arrange elements only in relation to one another, rather than to an underlying structure.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/416d829360036d445d6b64cc7a55ab42428677c242c4a3af1145904526f5c8e73e9c66c767fbe706ddc0a9d4b8846480e08936ce48e77693faf6f8cb77825765

https://lh3.googleusercontent.com/HTJEmQvSXdNsI1MN7oJAPbkYfsf9y62V0p5ukJkUj1QuFv815XMIQXnwcQfTQMGFgCvf1Yy3PPCvGXk_N8OZaLwSk6X33DiFM4w39wAVWDUWem9z6PI

Layout arranged into multiple columns

A layout that uses a column grid can better organize elements on screen.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/518be063e870122bd18830992828c386bf7dbf9532619eb712ff287e9167cd9ede87eaafd1c0666742e0381ea7de942d6e5f76583b64b134337dd416556944d6

https://lh3.googleusercontent.com/agyP5i_2bR0xJSQAvhpHz4LHTSs4yJAQcAoVR7E3FJzstYjiOwQ9XKMQknd7m0W353Lt2dscLdrkLJly1QTu1_T6V69EiDoCowSG0IRc1c6yKvQbNeA

Large screen layout next to the same layout adapted for mobile

The responsive column grid allows layouts to easily adapt across screen sizes.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/b5d11688f88e9173e4c13627b5746933ce65a61e99fa4d8acfccba4cd59ac22ef7be84a56c7a9cb4572f68af6d9e2c3ee531c47549e5b15a75a5ae3e492beb5d

https://lh3.googleusercontent.com/fPUTCNko0Reqxs5F1jBfEjfRoChAgxVvSLi9ZyY4D6BtM2wokuo9za5I1COjpVPLeEM3pgvmBm4pgipA7BmbXAll89Wvj6BtAAEjhXc9HCXnFHAoFgxC

Example layout grid from the Material Design Kit

Sample layout grids have columns, margins, and layout regions that correspond to Material guidance.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/33293fa012340ed59592f9004ff6e8c4b6983f16921ab5a7dea8702ddcf1c9c13daa2d5c04f993e2ce10f88efdebd0fba5ab0c5537ada312811eb7eda50dd9ce

https://lh3.googleusercontent.com/NcVgDQiMD8lmLG66Tg6tRF9aLzg6qe1kXOKBEb2APkBGYQJdkiRk300X6BxK9QlkBcArB8dXovECYR_b1yqqAUvROt5lbYSs-B3Y7b3KXgzVfdt7mA

Diagram of three layout regions

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/85b5fc5eb29d2095d10be6787d70b011b9d7677ec98744277221cbfa283f1f1c270d41cbb04d66d30ed4219b417a53e1e69badb320bb0ae6949cc3ea3bad6510

https://lh3.googleusercontent.com/p2g-lbdnIM7_hSDuAvZucHJdOEDbKG2QOKo4jxRIKCDao70r3MRuBvQ8ZVY_IQy1gh8bD0c11a1Cb38-_kcazdd5sz58P1Bi-MbLCDErZHquxPKPUt8

Sample layout with only the body region

Fortnightly's article content comprises its body region

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/db03db75de7761e353601d7e2495ca83101156208da0010455323445331382e8729ab4ad8fcc73634896d8ff3f336fbc58c8ff12d26a3685071332f2830155cd

https://lh3.googleusercontent.com/WAav5X47sOqP2CONOUM12XbgRJff3usN5e3cEDOIMXXo8Uq5Ul-0wyDNvVV-Fpx4JVQK8bhu_8LfDDXfyd5ZQVWD7LTmv_XCZhURN0l3wNNyBMth9w

Sample layout with body and navigation regions

Fortnightly's navigation region allows users to move between sections of the app.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/5981e4cd5087ed6920864cb53bc6e5150396ba4c60c23cf8e4a1bc79dd44a53e63094fe024419d9bd4dcfa88cdbd96421009b41ffaff5e103a558d285d2b5349

https://lh3.googleusercontent.com/5InlToHTWzHokPZd74ZJD9rAKV_poZMvMzVtX6Ciwg4r83WMN38HC4rbfP5ipIV0B4IKOWMjl-m8aWXMAPKRvEdGnkxYs-Ke5DFom3foUWHlIFJXG-4

Sample layout with body, navigation, and app bar regions

Fortnightly's app bar adds controls for the navigation region and other actions.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/827de644960854f8e9d9d823c5a6485e3b187f5f927cc9db64476dfccba80b5fecb8e0e2236a806ae2715e5616c9448a5b6a723ec60a9888178efd813c61756a

https://lh3.googleusercontent.com/NqL6VO-rJcuYtBM2bUs1ai9c4-X_B5lAAC1Lm5DkKk_nAhTwHI5rvdmxTJiANygV3NrBMP3L3zwH3_E-Gy8O1wMdEawcpczpdf09lv2ADJw5IBVbcsUP

Sample layout with items visually grouped using open space and typography

Fortnightly groups some news items using open space and typography.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f561f5d2225ebf46f56c546ea9ecc8a0b61f3a7937694af4274dd5df2d0aef0c4b5fa3f52d7b994eb77e3cb6734fa88ab909d31652be68d4a4d6fdbc1703f5b1

https://lh3.googleusercontent.com/NzQcEITLAASk0MiPUUSxu12yFwopV2RemkIS1mo5ahDV7G2vqszZLy6EJdx_IpxKncCwuaiWJLIyRKGD-nX3aFzIEzSh11qGAOMHhoH8iwtBNBAdOA

Sample layout with items grouped using explicit containers

Fortnightly groups some news items using explicit dividers.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/43b6327f9078067f286a1ac165d0c6965bd993caed763eb8e55730f363050ad291aa2034fde81ba1a430372f8ee43eb2c0348d91b5e897bac638934185d8086c

https://lh3.googleusercontent.com/rptD0QAcpqglEJpcQRzi0z4s-Pa6T_53kwZTh7q4OrcULe6OUtrI1o-nxNOLdl1qQtwh-Nkgh239G8iGsa-3vW1-yyxS1b6fqbZcZiUIQr_eYkrEDXs

Diagram of snackbar size constraints on tablet and mobile screens

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6706ac36189af874f81c2b449eacf126937c41243cbfccc4ba638522930868c5cde006239fcedd5bfea6acfd7f79ca0e54ab65949f55f144715e5ad8daa25f1c

https://lh3.googleusercontent.com/K7RzFHBBHTcIBQa1iMLVJXyVcZ6PkzOZ20flGZ1oa8jKXOYX6QPQbFYQ0znixG-5mrBwAYayfjTjsEGuTRaZfDgJ2HwkWHaz4VU3uHwjQhloCRA_wHM

Diagram of a dialog at its maximum size

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/3ca654feb8824914f68efa82ef764e5311eef85314188860038777b4d5edea1abe37d7817d9ea5fb994832f4b519d47fe2aa5d1820a434ff446e80c2ba300785

https://lh3.googleusercontent.com/gs6kR69R30TyIQAd5y_YdWvvjnOFCareTuUwOCVZNXENRETEEJSX9-ZFCrDbZ-QqqLo60lHXA9LgH_99aR9NAIJqKV-G4Ex-qHaDFUI-iLZX5Tf5zuZy

Example of a full-screen dialog on mobile and simple dialog on tablet, both with the same content

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/9f39c2ccb37b49c3c09df5a5fde982cc0c641cb0ba85d9a31b824d288c982ec3e0a551e0fc92257d9db14105fc961bde170403db2052d41abeaa11566f147a1f

https://lh3.googleusercontent.com/uNzhLODJe2pcjJ96Kad-mLok84YJnT6izhbbUn4Py4dtISgV7J6oskQ2L9aY-GxqXuu64b31ALZB8nDGxHWSSVU-3XyA__gzRqJ6gfcw7B5PTGdRWjc

Example UI adapting from mobile to large screen, swapping nav components

mio-staging_mio-components_1584058305895_assets_1n49HQ1AjiDC5aqG38DrtswaJFrR3exKf_rail-adaptation-1.mp4

https://storage.googleapis.com/material-io-design/m2/assets/downloads/8e5938591ed55cfa290357cc229b0fc2610da447067aa88fbe80511863a265199aac605992e5fbf634c151dcbda70821d98bc62decfb8fc169e0e8cc5e6ec3f7.mp4

Illustration of abstract shape morphing within 5 boxes

Illustration by Simone Noronha

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/07cf31e52f0f03c1ea9c7f2f870f26f52b2424ccd78dc76bbcae793ebe084fea5a02a1d3255adb3f269f77207ea64ac1c9c076515b7cd8776db242c9a01c01c2

https://lh3.googleusercontent.com/pN5xtyQvPk3HXVVz-gVDc0YYvJ-UzjfFjMcEemwIKWfVmZGCcyV4XNEAjehGLIA9VnuCRzSC0HDNy6p0tDChJvEWjRVsqCvBWJ56sKjP-YvWxWfXdg

how-to design development material-components

 

{}

What to prioritize when building a responsive experience

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/3ca415eceb641fa4cfa95ca357bea0c12d0dbd5c8701b295a1955f311c3fcb78a8b789bfbe351ee1687687f797815ba9eb53161207cdc1324a80d6d14fbf8568

https://lh3.googleusercontent.com/P54dhrGSWx3BvnP00OD7TPipPM_KWQALYCVQs7fX849Awl04TuW1uTAkpr76k_nx3IrK3xYB0e3EkiHqvWF0dsH8XTZNcQzVFzU33JsQEfxSN8Fsg3g

5 Exercises to Prepare Your App for Large Screens

2021-05-19T13:00:00

5-steps-large-screen-apps

What to prioritize when building a responsive experience

Start Here: 5 Exercises to Prepare Your App for Large Screens

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

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/07da15b59caa9b4de3df69a7c9844e840e33c1b1f4e4d84d52baff9a5a1f6f4ede0ad1c693d1b0182be597cd33b9c734d2931298028a6075baa7983f64cc4f8e

https://lh3.googleusercontent.com/cy76FByvLxBjTxXDEks32gNkv16eT65jjF_DWN8HqMiBRRmU7XD3bTRUECgJAL3XBVE8vZmcPkNZXOMeDxxYZBkalvW6HBX8fPPJfkdqYYPu75kKr9E

Figma Baseline Design Kit

https://www.figma.com/community/file/778763161265841481

Figma Baseline Design Kit

Resources

Figma Baseline Design Kit

mio-example
