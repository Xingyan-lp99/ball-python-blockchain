# Introducing Material Theme Builder

Source: https://m3.material.io/blog/material-theme-builder
Content endpoint: https://m3.material.io/page-data/Posts/5876903831142400.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/2325b688601478bc6278df9a9121ec4a232b1cf908495ead3ba795eb31c55ce687ff559c71c8ce02b27aec462fd4ec4c6cde8f11d872ae286f336f6eb65168be

https://lh3.googleusercontent.com/ZaJP3AXmRdBneMpX_gzK6K-wqcR6xypjYskBCfk4edozBiOh9vJAPsXWbyzIN15gAShPrt_7RVCE9b374Yix26WwQnbwWx251CoNTFTb8fwlg16Yfos

Yasmine Evjen

Senior Product Manager

mio-example

<p>Material Theme Builder is a new tool that helps you visualize Material You&rsquo;s dynamic color and create a custom Material Design 3 theme. With built-in code export, it&rsquo;s easy to migrate to Material's new color system and take advantage of dynamic color.</p>
<h2>Quick links</h2>
<p><a href="https://goo.gle/material-theme-builder-figma" target="_blank" rel="noopener">Install Material Theme Builder as a Figma Plugin</a>&nbsp;or try&nbsp;<a href="https://goo.gle/material-theme-builder-web" target="_blank" rel="noopener">Material Theme Builder on the Web</a>, and grab the new&nbsp;<a href="http://goo.gle/m3-design-kit" target="_blank" rel="noopener">Material 3 Design Kit</a>.</p>
<h2>Themes powered by Design Tokens</h2>
<p>Material Design can be customized to represent a variety of stylistic choices. A theme is a set of style choices that define the visual appearance of a product. With Material Design 3, we are introducing design tokens&mdash;small, reusable design decisions that reflect the system&rsquo;s visual style. By building with tokens instead of static values, design and code share a source of truth.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>Our <a href="http://goo.gle/m3-design-kit" target="_blank" rel="noopener">Material 3 Design Kit</a> and <a href="http://m3.material.io" target="_blank" rel="noopener">Material 3 Component libraries</a> have been updated to reflect the new design tokens and their assigned roles. In Figma, Material Theme Builder generates these tokens as Figma styles. Material Theme Builder exports design tokens directly as a <a href="https://github.com/material-foundation/material-tokens" target="_blank" rel="noopener">Design Systems Package (DSP)</a>, and theming code for our Material 3 libraries on Android Views and Jetpack Compose.</p>
<h2>Visualize dynamic color</h2>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>Dynamic color plays a key role in Material You, creating individualized and expressive experiences for your users. Design tokens and their assigned color roles allow apps to seamlessly accept any dynamic color scheme in place of pre-set color values.</p>
<p>Material Theme Builder on the web gives a glimpse into how dynamic color from a wallpaper may represent itself in UI. With the Figma plugin, you&rsquo;ll be able to see how dynamic color represents itself across your design. First, you&rsquo;ll need to manually map the design token Figma styles to your custom components or use components from the Material 3 design kit to build your UI.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>Once you have a UI built with Material Design tokens, select an element or frame of the design and click &ldquo;swap&rdquo; to apply the Material Theme styles, now any changes you make in the Material Theme Builder will be reflected in your UI. While selected, you can switch between light and dark themes, by clicking the moon and sun icon buttons.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<h2>Build a custom theme</h2>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p>In order to take advantage of the latest features introduced with Material You, you&rsquo;ll need to migrate to Material Design 3. Material 3 theme expands on Material 2&rsquo;s color space by introducing new color roles and deprecating others. With Material Theme Builder on the web and Figma, you can easily create a custom color scheme based on your brand or style. Once you have a custom theme, you can export your code to be used with our Material Design 3 libraries for Android Views or Jetpack Compose.</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p>For an in depth guide of the new Material 3 theme updates, check out our <a href="http://material.io/blog/migrating-material-3">migration guide</a>.</p>
<h2>Export to code</h2>
<p>Material Theme Builder allows you to export the theming code to multiple formats: Android Views (XML), Jetpack Compose (Kotlin) and Design System Package (DSP).</p>
<p>Note that the surface colors (Surface 1 - 5) are shown within Material Theme Builder to help visualize surface tonal colors based on elevation. However, these surface tonal colors are not exported in the code. Their actual color values are calculated by setting elevation within Android. For details on how to set elevation in Android see documentation for <a href="https://m3.material.io/libraries/mdc-android/color-theming" target="_blank" rel="noopener">MDC-Android</a> and <a href="https://developer.android.com/jetpack/compose/themes/material#elevation" target="_blank" rel="noopener">Compose Material 3</a>.</p>
<h4>Compose Material 3 (Kotlin)</h4>
<p>&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p>Material Theme Builder exports <code>Theme.kt</code> which sets up your <code>MaterialTheme</code> with the proper design token mapping. <code>Color.kt</code> stores the color values of your custom theme. We strongly recommend referencing the Colors provided to the <code>MaterialTheme</code> composable via <code>MaterialTheme.colors</code> and not the values defined in <code>Colors.kt</code> in your UI. This will allow you to accept dynamic colors and easily switch between light and dark themes.</p>
<h4>MDC-Android (XML)</h4>
<p>&lt;mio-image index=7&gt;&lt;/mio-image&gt;</p>
<p>Material Theme Builder exports colors.xml, and both themes.xml files for light and dark themes. We strongly recommend referencing the Android color attributes, such as <code>?attr/colorPrimary </code>and not the hard coded <code>@color</code> values in your UI. This will allow you to accept dynamic colors and easily switch between light and dark themes.</p>
<h2>Start building</h2>
<p>We are so excited to be bringing you these updates with Material Design 3 and the updated tooling to support designers and developers in the process.</p>
<ul>
<li><a href="https://goo.gle/material-theme-builder-figma" target="_blank" rel="noopener">Install Material Theme Builder as Figma Plugin</a></li>
<li><a href="https://goo.gle/material-theme-builder-web" target="_blank" rel="noopener">Material Theme Builder on the Web</a></li>
<li><a href="https://goo.gle/visualize-dynamic-color" target="_blank" rel="noopener">Design lab: Visualizing dynamic color in your app</a></li>
<li><a href="https://goo.gle/apply-dynamic-color" target="_blank" rel="noopener">Codelab: Applying dynamic color</a></li>
</ul>
<p>Watch our <a href="https://youtu.be/clDuqcKgNBQ" target="_blank" rel="noopener">talk at Schema 2021</a> where Ivy Knight and Rody Davis talk about bringing the Material Theme Builder to life. Subscribe to the <a href="https://www.youtube.com/MaterialDesign" target="_blank" rel="noopener">Material Design YouTube Channel</a> and follow <a href="https://twitter.com/materialdesign" target="_blank" rel="noopener">@MaterialDesign on Twitter</a>.</p>

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/87ec9ab225cee171cd8b6abfaee42907accd9814d40ca5a65ac753bf34354bf7ae1ae4f40dc8aa6a69a718a88007028280354749adebb737cd9c3c98b424afa8

https://lh3.googleusercontent.com/ru5tKBEJW4eDiLx4Lj8Vh67Lxw0cBm1nmThqeJXoVlhpQrG0R-ub5B0FVnb1hSMvmhrMPfDTVX6Ge8iA1MmH2j1E-5l2m772k524oZUDUX0EgRJOffs

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/075c17e2c8e52e419c19d0d43cc1625e2f99d68e3b980679b87d8d284a087790ebdbecdd5f6853df6aa01879dffcc64155f6b418b77beb9c585427f6c543cd0d

https://lh3.googleusercontent.com/pi5v57OE5qRvS3OAdk4Ifiug9_I0U8OUjRSgSkhQuTQJBcuoAN0AUl3oSsQhd-xKR_th4wO6MSorSnxaVnCBDk52zu-NEA70MeV_hKMPyNuRIPL0aZM

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/1318b2fd8156b35f84ec598d6c3f7bbf30337ccdf4681187710ba13a23d7a9ace41a48e6b4c6d6af88b0458d194bf1029ccc67205de58b4a10ed6887c329b2e5

https://lh3.googleusercontent.com/in9HDVwfSDGN3EwonNk3vHZahIEikmKSyTJW80iHb-2zoARNNsguhUU06h1rwtqBRiIQpmyYelrE8-mUb47to4cThKHoBfqpZNcPK2zia58y0oBv

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e5f5009c0cacde64f4ead3be67694ef67bb7586e058784a96434a717ba8b2e042b6eaa9d366e38bc7fbb094bd32857b49cb55c17a6440312d5c19ff0176f5a16

https://lh3.googleusercontent.com/4x0iIUIImSgACQgMshakt63XQLnH_7hpaPVXNvvWKli6_5Mjl0Xmoc_A214aAaInDoYnHd2buW-Vqko1Iv5UtR5rOxJT7kFJYtbGnS6qMMLNyJk0VQ

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/8cb65e3eaa2f755f2507552d6ff9312736dde35b9281ccdfae85fb1d30cd941814fe43b5a0dbf9875390ba2dd340d900984b48f50be60d9872078faadcae3153

https://lh3.googleusercontent.com/C0fyWFF3nfOOXyGYS_sOHo_KVmFuvI-aJaVYDeQkHnXhjVBdJTuwEnGbAAcHRAyN3CLtEJFbVQ29fPX-DweQe1jtaizAql4WKoHBlP6da3VAZvQVmtU

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/b6007ab4868670f3debd80b03f962571a62e41718ed74839b3142516779acab862c7f33c5ac77977dfdd7df9ff5d0399d6d2301c81589907c7c63b61565e4d55

https://lh3.googleusercontent.com/ZNy-DSNdWoXNwerefZa-QImSGcy87htA1ytLMIa6ASFda1xcm_17eCtru7bsmv-px4rgcn1XuzXtAKGdDgAWC1sAuYrbhtzCidOl06fCWjpmc6d733Ey

App directory within Android Studio, showing ui.theme and Color.kt, Theme.kt

Within Compose Material 3, ui/theme directory hosts your theming files

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/de0a269d4a8fa02cc0c88851ab5ae43f6b114aef5130a328454987f6b98f2f5c1c20bd6ac976c7aff9bc5ba7b99fbfe2aa67f1d4dae76ccf8724dec108220111

https://lh3.googleusercontent.com/BJ1UTCG9NFC_XI05sa3_Z2CsTRjhkorR_7cKoo0zVspdXb8pz7qrB7VdyKzH6WhbVU0ptnH2rsESeDg37DBj-d2eytpOdjGYYWnNxbIi9bRZ_YdK3w

App directory within Android Studio, showing values and values-night with colors.xml and themes.xml

Within MDC-Android, res/values and res/values-night directories host your theming files

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/1d0a4f54bb95e5f7a76e71b1e4a38cff0dbf471edd979eb5ae5c2eddbbe988425e5830e5e78b3908ae9e48a7d7c79ef2cf3a7a020426b53d1dd68fa6ce4ce391

https://lh3.googleusercontent.com/enEHy4KTgyzmvVDNy5XgOBNAMVaefY9Kz_chuXG-2JIxA7oCEKLqy6GsMH2Hgnajar9xQa2wQN0huSi-4Fd0KhfGdH9EXSiOG1pguVET3_Kt0LeYQNk

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/c56909f9bf9f7ecdd89569d0afbc88a0abb5355f54d5ae152b2f816cad0605817b650c37df5b111a8dcb0f44d57082c3e320b0952f816e41888e5eecf86a261f

https://lh3.googleusercontent.com/rKjjYo5u2SmXb8kfJvGrN8OAlwbBBZ24hyMWY5PCvt6V4iVhs-R9GvQjpgGm7-P8uAcC3BcmyIBmPgFtASL2nr5HO1H4r0LcL3EOwCyeoVM3X54-aJs

{}

Material Theme Builder is a plugin that can recolor your designs using Material 3 dynamic color, create a custom color theme, and export to code.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/2bb8f48e54fedbe61ce67f782c574c2c2981a6aafd9a22cf5a926219bb1cdf765af1f3ed7e27bc7ad01b3b2ec4fec7512a3a02a3eb8885294b3c9b8ae73ac7fa

https://lh3.googleusercontent.com/qeX-hBJlQAtsRloocqOblupKxIYuafLTKDRsfmxAOmJ77_hLGc775NUlfRxXiYB6sujZlaM8SbPQxqqVq7Vd3HYlwKrC0KCkW3ZisNPaokWPQLV5HUsE

Introducing Material Theme Builder - Material Design Blog

2021-10-27T09:15:00

material-theme-builder

Visualize dynamic color, build a custom theme, and export to code

Introducing Material Theme Builder

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/362302fcebd869d647a92554dbe8a7b1e06b1eeb8ce46a6e67bfc5403441aea79237facc6dfe929599f4fb4bc8e6e836d2efbccab8abed1fca121d67d244aac4

https://lh3.googleusercontent.com/rME0woOrBvWQqpvpmd_QteVRux9dw9pT7HhbEVneGV5yyo1WzljxXgwf4wynieJPHPs--tPySUe7uoMiJwuYj-oNzXC8PwwXE1wK7Dyv9_UDhyce5A

Start building with Material You

/blog/start-building-with-material-you

Start building with Material You

Material Blog

Start building with Material You

mio-example

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

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/264a443d1e54b4ff4827d1c22552881b81e2fa872f16d65d10a8720f512633cefd0e6f116318d75c4c9e6ecc158af2bca9ef5dde4f35bd9754a8fb2d2da49170

https://lh3.googleusercontent.com/79I_k3QufXk598pk_Rmgl011wP9DDnn-gkJY49XZ_2kDArzQnL_4rnitH2W8t-wLJT8L_SV7jXbpil6MGS-483LsurzCXyXjeQR1JDdeGL0i2lVnScY

Unveiling Material You

/blog/announcing-material-you

Unveiling Material You

Material Blog

Unveiling Material You

mio-example
