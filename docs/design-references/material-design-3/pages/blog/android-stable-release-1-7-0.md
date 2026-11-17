# MDC-Android Stable release 1.7.0

Source: https://m3.material.io/blog/android-stable-release-1-7-0
Content endpoint: https://m3.material.io/page-data/Posts/6724211708133376.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/e542d55e05d06e63bbf3dadd467d6f4889a15a6c2c43b46c812a48b6ee2adf7ff126e17cb0d3c04d4d2f24d216f00138ed4cd9cbf209538cb1bd0f4fd7ac7f15

https://lh3.googleusercontent.com/ECgal03qq-GPHfoWRZft82d97qPwwB-M4z1d-igDCWWAMWhJteOVP4HzaU2XhhQVfG9ME-_0DWTFA1eK28kgnTgTHBpSnTIhLK8TQKwE0zyq_lFckrs

James Williams

Material Developer Advocate

mio-example

<p>The latest releases of Material Design Components (MDC) - 1.7.0 brings updates to Material You styling, accessibility and size coherence and new minimum version requirements</p>
<p></p>
<p>MDC 1.7.0 has new minimum version requirements:</p>
<ul>
<li>Java 8 (1.8), previously Java 7 (1.7)</li>
<li>Android Gradle Plugin (AGP) 7.3.3, previously 4.0.0</li>
<li>Android Studio Chipmunk, version 2021.2.1</li>
</ul>
<p>This is a fairly large jump in terms of the Gradle plugin version, so make sure to secure changes in your build files first before moving on to UI code. As always, our release notes contain the full details of what has been updated. There are a couple standout updates we&rsquo;d like to highlight.</p>
<h2>MaterialSwitch component</h2>
<p>The Switch component has undergone a visual refresh that increases contrast and accessibility. The <code>MaterialSwitch</code> class replaces the previous <code>SwitchMaterial</code> class.</p>
<p>It now differentiates between the on and off states more by making the &ldquo;on&rdquo; thumb larger and able to contain an icon in addition to an on state color. The &ldquo;off&rdquo; state has a smaller thumb with less contrast.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>Much of the new component&rsquo;s core API aligns with the obsolete <code>SwitchMaterial</code> class so to get started, you can simply replace the class references.</p>
<p>For more information on how the obsolete component stacks against the new implementation, <a href="https://github.com/material-components/material-components-android/blob/master/docs/components/Switch.md" target="_blank" rel="noopener">check the documentation on GitHub</a>.</p>
<h2>Shape Theming</h2>
<p>A component&rsquo;s shape is one way to express your brand. In addition to providing a custom <a href="https://developer.android.com/reference/com/google/android/material/shape/MaterialShapeDrawable" target="_blank" rel="noopener">MaterialShapeDrawable</a>, there is also a means to more simply customize shape theming using rounded or cut corners.</p>
<p>Material 3 components have been updated to apply one of the seven styles ranging from None to Full. A component&rsquo;s shape is defined by two properties: its Shape family, either rounded or cut, and its value, usually described in dp. Where a &ldquo;none&rdquo; style always results in a rectangular shape, the resulting shape for full depends on the shape family. Rounded returns a rectangle with fully rounded edges, while Cut returns a hexagonal shape.</p>
<p>You are able to set the shape family and value individually and arbitrarily on each edge but there are set intervals and baseline values.</p>
<table style="border-collapse: collapse; width: 99.791%; height: 176px;" border="1">
<tbody>
<tr style="height: 22px;">
<td style="width: 48.5029%; height: 22px;">Shape Style</td>
<td style="width: 48.5029%; height: 22px;">Value</td>
</tr>
<tr style="height: 22px;">
<td style="width: 48.5029%; height: 22px;">None</td>
<td style="width: 48.5029%; height: 22px;">0dp</td>
</tr>
<tr style="height: 22px;">
<td style="width: 48.5029%; height: 22px;">Extra Small</td>
<td style="width: 48.5029%; height: 22px;">4dp</td>
</tr>
<tr style="height: 22px;">
<td style="width: 48.5029%; height: 22px;">Small</td>
<td style="width: 48.5029%; height: 22px;">8dp</td>
</tr>
<tr style="height: 22px;">
<td style="width: 48.5029%; height: 22px;">Medium</td>
<td style="width: 48.5029%; height: 22px;">12dp</td>
</tr>
<tr style="height: 22px;">
<td style="width: 48.5029%; height: 22px;">Large</td>
<td style="width: 48.5029%; height: 22px;">16dp</td>
</tr>
<tr style="height: 22px;">
<td style="width: 48.5029%; height: 22px;">Extra Large</td>
<td style="width: 48.5029%; height: 22px;">28dp</td>
</tr>
<tr style="height: 22px;">
<td style="width: 48.5029%; height: 22px;">Full</td>
<td style="width: 48.5029%; height: 22px;">N/A</td>
</tr>
</tbody>
</table>
<p>Default theming will apply the same shape family and value on all four edges. You can apply shape family and shape style (or alternatively a custom value) independently on each corner.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>The Shape Theming card in the Catalog app allows you to see how different values affect rounded or cut corners.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<h2>What&rsquo;s next for MDC ?</h2>
<p>We&rsquo;re fast at work on the next major version of MDC. You can follow the progress, file <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=bug&amp;template=bug_report.md&amp;title=%5BComponent+name%5D+Short+description+of+issue" target="_blank" rel="noopener">bug reports</a> and <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=feature+request&amp;template=feature_request.md&amp;title=%5BComponent+name%5D+Short+description+of+request" target="_blank" rel="noopener">feature requests</a> on GitHub. Also feel free to reach out to us on <a href="https://twitter.com/materialdesign" target="_blank" rel="noopener">Twitter</a>.</p>

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/a23124ccbe2e5e293b312c4d023f36af6a43d5271b232b6b57e9996142057b99ea96149f537b1486cd277bb3e2fd2fe27511fb58fab32a7714c1838627cbb52c

https://lh3.googleusercontent.com/0_eEy3Q32oN80EE37jR_99ZazPpBb6cDvM3NImsqfKiIiKxt4srqT5BNp47XsEeug7pobgPcTVpF-1dKIsvXfYdeA2ze2nX_Umw_qZYZnfrQRGmQmbdW

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/1e798ae59a582d1e6adb58bfd4dc1e78c2fd52c63616a301dd5526b1b11270aa655473e6446cb949314bba45ad9e0747890173875ce606fa4520c6b52d4b00aa

https://lh3.googleusercontent.com/WtZFwRC4kInGlczgoR1iz1yQtq2JlLQPdMTLg6M9FugjDmhH49D6U31FH4cQj6kUUL4of-oi0DiO9T4mCndm9SRlHtoFpjxrm1vkAIOZ3JRK-5yCsviq

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/3fbce36a7f375ee39f1969db3d5d33fb9cb83816b21c0b90510fc8f8f3d38387be075f08b1e6f2979dc68b560dff5825b84349f63c50d9740be0bd5d59e5e01f

https://lh3.googleusercontent.com/zThUgoPFDY4L8WPwyBDMUCXX2C9Iyt04wg8Bhr3GaPTmcu0pvUeOr55vv7ZsRmRCylio-B93o-KfR52TVwtYii6_b7vzBuIx_lu2LgbGO7O46Y5D_mo

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/4a65acf54d674a4582bb445446b2469f3414c4e2c41c986e80ceb2a3cd3e169f3f9c2f00da59b0dfcc9b24ef623fabf4423a14f3807d3fb54d52437db7879ea1

https://lh3.googleusercontent.com/JNSz_5_2WViMK2UQpSvJzhZW-4kGBzxHXfKv5Jc6IyxBKy4XKn26raXhCrY2JExhF9bWX2OT7YprkBbmXWfmFoplDddL5fbEs8ggbHfuiHhzV7Fd1HY

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/4bd3505eeee79a4668ef2e9bca696138d9eabf4813034e702954738b9597fba0107634784abedfc98efdb1c571fe1e78c911d921221afb4c3b9a1c3d914a3b6f

https://lh3.googleusercontent.com/RFeqhT5kDBq9Fo4GyqNq4EE7g1WKi-NBZ_IWBXOf235ribRpuquQmcjEhLfxPd5LycBauHBWoTHFNIo6eFWYEToksbVSaZdHv3fSpcQdNfJVwQP85tvw

 

{}

Material Design 3 shape guidance and improved a11y

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/7f936938440005d5f07f69da069f0a729b1116935a2d1b0e7da50da90f3846343578f04531950abee959d93e35700e78bf61103a8d0a79fbbba22d43e42d88e5

https://lh3.googleusercontent.com/zgYk2A279O1HljyDykmzzSA4D3e8uVhfSH3FR1aeciU3GkbqrvD8Lrqe89SUVyqdy-NgdRY6XPus9jZN90Q6ItLBjJVDQkoSIkUDlSHYElPiDLdspNol

MDC-Android Stable release 1.7.0

2022-10-20T10:00:00

android-stable-release-1-7-0

with Material Design 3 shape guidance and improved a11y

MDC-Android Stable release 1.7.0

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/1481b32fbbfe7bbc4406db4b34f7c52278973f60180c2b54201c20e5e3c6c72750674d4cd007044c360e9a28b64485bc494865dfd6271c48ed7d1d968dcd294d

https://lh3.googleusercontent.com/M5NfUy9_KPMnx3veoaOvu9pTAyHRugVfgeig4R6Li_mKLpEwY4w4f7QB5TuLAoiNRcLVShFyCpzhYu80h0GmC2W1DuRYjFKlFKSpZGi_BFh8wekgDA

/blog/android-stable-release-1-6-1

Material Design Components for Android 1.6.1

Material Blog

Material Design Components for Android 1.6.1

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/431dfac6c5ce89665d484592b44c8066d4b009ee23e07ac7f8e6295313ad9ece46f3b390755cd81685be2f44f2ea784fbe82eefdf5fdd401d8430fc8a4b543cf

https://lh3.googleusercontent.com/hwCFDEfbHlMM92sX1YWje3r5Df9KOiUg-xrF9cZf4YFka-4O83DEv1wYT38uoV509-Oet5dYl0jTXsriDvfN5sTjlLlLbvIsH2vhJNgaZXg3ZCXcwA

/blog/material-3-figma-design-kit

Introducing the M3 design kit for Figma

Material Blog

Introducing the M3 design kit for Figma

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/fec8e400c1a65c9db8aaeca91452084f9d8f0d7c3a0ae9d53c6c179a651b929f0142a01320541c9dfdf5f8affc3c0336a5ea7e700efdbb5d7359353a25858143

https://lh3.googleusercontent.com/GVc9yZ3j5ws-GcfqADXIt6Xe4TycvoP6hQ86oPHOjbjUecgFkn_k2O7SDes10QWc084qwqxtFRBopDQMWZEYa_V2RFRd1uDG6T3Z6kH_Jp1Dr-XjLKc

https://m3.material.io/styles/shape/overview

M3 Shape Guidelines

Material Design 3

Shape

mio-example
