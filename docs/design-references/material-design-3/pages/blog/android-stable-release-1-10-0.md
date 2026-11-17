# Material Design Components for Android 1.10.0

Source: https://m3.material.io/blog/android-stable-release-1-10-0
Content endpoint: https://m3.material.io/page-data/Posts/4743734110060544.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/e542d55e05d06e63bbf3dadd467d6f4889a15a6c2c43b46c812a48b6ee2adf7ff126e17cb0d3c04d4d2f24d216f00138ed4cd9cbf209538cb1bd0f4fd7ac7f15

https://lh3.googleusercontent.com/ECgal03qq-GPHfoWRZft82d97qPwwB-M4z1d-igDCWWAMWhJteOVP4HzaU2XhhQVfG9ME-_0DWTFA1eK28kgnTgTHBpSnTIhLK8TQKwE0zyq_lFckrs

James Williams

Material Developer Advocate

mio-example

<p>We&rsquo;re happy to announce the release of Material Design Components for Android (MDC-Android) 1.10.0. It offers a mix of functional changes and updates so make sure to check the release notes for a complete listing.</p>
<h2>(In-App) Predictive Back</h2>
<p>Predictive back allows a user to see where the swipe gesture will take them before they execute the action, usually by scaling the view to reveal the destination. At any time during the gesture, the user can cancel and remain at the current destination.</p>
<p>Starting with Android 14/API level 34, Android supports predictive back inside your app between destinations in addition to the predictive back-to-home introduced in Android 13/API 33.</p>
<p>The general steps to opt-in to predictive back are:</p>
<ul>
<li>Implementing the &ldquo;back callback&rdquo; APIs (<a href="https://developer.android.com/reference/android/window/OnBackAnimationCallback" target="_blank" rel="noopener"><code>OnBackAnimationCallback</code></a>, <a href="https://developer.android.com/reference/androidx/activity/OnBackPressedCallback" target="_blank" rel="noopener"><code>OnBackPressedCallback</code></a>, <a href="https://developer.android.com/reference/androidx/activity/OnBackPressedDispatcher" target="_blank" rel="noopener"><code>OnBackPressedDispatcher</code></a>, etc)</li>
<li>Setting the <code>android:enableOnBackInvokedCallback</code> manifest flag to true</li>
<li>Moving away from legacy back navigation (<code>Activity#onBackPressed</code>, <code>KeyEvent.KEYCODE_BACK</code>, etc)</li>
</ul>
<p>&lt;mio-video index=0&gt;&lt;/mio-video&gt;</p>
<p>Once your app is migrated, destinations involving supported components will get predictive back navigation gestures and animations for free.</p>
<p>At the time of writing, they are :</p>
<ul>
<li>Search Bar / SearchView</li>
<li>Bottom sheet</li>
<li>Side sheet</li>
<li>Navigation drawer / NavigationView</li>
</ul>
<p>To follow a detailed guide to implementing predictive back in your apps, please check out the documentation on <a href="http://developers.android.com" target="_blank" rel="noopener">developers.android.com</a>.</p>
<p>Our MDC <a href="https://github.com/material-components/material-components-android/blob/master/docs/foundations/PredictiveBack.md" target="_blank" rel="noopener">Predictive Back documentation page</a> is the best place to learn about the growing number of components that support predictive back and future slated components.</p>
<h2>Updates and Changes</h2>
<p>Starting with this release the minimum <code>compileSdkVersion</code> is 34.</p>
<p><strong>Side Sheet</strong></p>
<p>Side sheets, first mentioned in the blog post announcing version <a href="https://material.io/blog/android-stable-release-1-8-0" target="_blank" rel="noopener">1.8.0</a>, contain supplementary information related to a screen. They were previously anchored only to the right side of the screen. Starting with version 1.10.0, they may be anchored to either side of the screen. To learn more about the different side sheet types, refer to that <a href="https://material.io/blog/android-stable-release-1-8-0" target="_blank" rel="noopener">blog post</a> or the <a href="https://github.com/material-components/material-components-android/blob/master/docs/components/SideSheet.md" target="_blank" rel="noopener">documentation page</a> for side sheet.</p>
<p><strong>Changes to Carousel</strong></p>
<p>Carousels, introduced in the <a href="https://material.io/blog/android-stable-release-1-9-0" target="_blank" rel="noopener">1.9.0 announcement post</a>, have a new variant (<code>HeroCarouselStrategy</code>) that aligns content to the start and uses a &ldquo;hero&rdquo; strategy, allocating most of the space in the carousel to one main element.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p><strong>BadgeDrawable</strong></p>
<p>BadgeDrawables, often used to annotate items in navigation components with text such as a new/unread message count or unlabeled shape, have undergone a small tweak.</p>
<p>Previously, you could align the badge to any of the four corners of the anchor view. That has been reduced to two alignments: <code>TOP_START</code> and <code>TOP_END</code> (default).</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p><code>BOTTOM_START</code> and <code>BOTTOM_END</code> are deprecated and usage is discouraged. To read more about the changes, please see the <a href="https://github.com/material-components/material-components-android/blob/master/docs/components/BadgeDrawable.md" target="_blank" rel="noopener">BadgeDrawable developer documentation</a>.</p>
<h2>What&rsquo;s next for MDC?</h2>
<p>We&rsquo;re hard at work on the 1.11.0 release with some clarifying updates to how we use color in components. The components or features we highlight in these posts are only a fraction of the work that lands in each release. Check out the <a href="https://github.com/material-components/material-components-android/releases/tag/1.10.0" target="_blank" rel="noopener">release notes</a> for a full listing.</p>
<p>You can follow the progress of new versions, file <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=bug&amp;template=bug_report.md&amp;title=%5BComponent+name%5D+Short+description+of+issue" target="_blank" rel="noopener">bug reports</a> and submit <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=feature+request&amp;template=feature_request.md&amp;title=%5BComponent+name%5D+Short+description+of+request" target="_blank" rel="noopener">feature requests</a> on GitHub. Check out the <a href="https://github.com/material-components/material-components-android/releases/download/1.10.0/catalog-debug.apk" target="_blank" rel="noopener">catalog app</a> to see the components in action. Also feel free to reach out to us on Twitter <a href="https://twitter.com/materialdesign" target="_blank" rel="noopener">@materialdesign</a>.</p>

carousel in the material catalog app

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/5785be12467c8d648db4dd7c958351449d0cc188432eabc3017fe07c92ce42ae9f1fbbb50908ff6b2f0e9a742f1a28cacdccfdd11858cecdbc97a74f88019cd2

https://lh3.googleusercontent.com/CCu0KuZwrZXgfaI_z1tvyzOpx1iip6IK7vXp9HD1iLRplnJGk5TE9LepSC7OvilkEz4tlfWVf-q4hdo0acUMkOW_GS_C0_2FcwuSmnC06zUbV1xj5FW3

Bottom nav bar with badges

TOP_START Alignment

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/7d5e682d5dcf85c4661cc28b04a365ab208c261ccc88dbd426188d1260f7f751fdf34a446dd3cb848dfc8e92252728e106c315195ee55062a12d763c1c6b6304

https://lh3.googleusercontent.com/I2FShTZJ7bV7dszsQ437Y8Zu3u0CTdb_T0JJB-zE6EZB0TxpR74ULHo5tqKlByJlu1K97PeHyOzCCTbg8-ahllLzedwwLGXYkVmP3Gupm_vjW1NUaw

Bottom nav bar with badges

TOP_END Alignment (Default)

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6f9a3e8e07e6eb974593315ea6db201ea1f31a3c66007a4e445d04dfae329cbea1912557670fcd109718ab677e61606c242171a84c87dd7a26b88e9c6edaf623

https://lh3.googleusercontent.com/B24uqNiYvH9lJnZf6UnjbNx5VCQ-yGb8xbHsewo91MfBC0n0cQx5d4h891OLAYqTWvDrBSomScR6O5u1A0kWCr9V8MdZqZCVhrH3YEDgdEZuxusbDQ

predictive-back animation on android

lg549708-3P-Bottom_Sheet_Predictive_Back.mp4

https://storage.googleapis.com/material-io-design/m2/assets/downloads/12607e68170650bb6a3e8279fb697f03347a022216efbc3c004183b912a657587fbf61a339729a76dae17a7efd61423dded1a17e7a8dbdf7e66f11197f991fd6.mp4

abstract flower and leaf illustration

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/8d4523e0afbaee132992816d92c69f9991c929d20c6dd42e9d93a5918721fc4054274114b9eaf03ba62ce895a1422b1268dd945dd52385e16ee5e55438ed1183

https://lh3.googleusercontent.com/pR75LC3YTcz6E8rmRyB0FvLZPrvqzHwa-cHtTrrBe3yrNo1YUZLXQzHzvOKVGZZjjoc75U-KG8cvGFUthsfuYBugrUm5MKZNwvH37cw4NqM8EzkPCBI

{}

MDC-Android 1.10.0 is released! Get the latest updates on Predictive Back, Side Sheets, Carousels, and more.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/3f34e820325175a38f01ee6ae5bb1f49c6bb50e5fa47bc8fbd69f257f9c5ce83586e5f1c1789aae898ec0a7c120b0e865ae3e364ada1fe6e44ec84846da43dc9

https://lh3.googleusercontent.com/ByZMg7DwG7yZaO0-mK_SQOALRg5xcrpDzSnSUvVvIFymBTY4e-KLbJdoXQyN8ZZUy4NsPoYAs6SSH-DqQPzRVnJzMrSaXaHywfJzNV3X3wXlGnWY-A

Material Design Components for Android 1.10.0

2023-10-25T13:00:00

android-stable-release-1-10-0

Updates, refinements and a new way to transition between destinations

Material Design Components for Android 1.10.0

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/f76a10ef20aa3042fc461583cb2a0ac1ce5df95cdd3478424b0e318c5d8ed57cf9492e0503c8f7a07cf19185a453e248c8b840fd2bacf8f608bf5f18e47a9271

https://lh3.googleusercontent.com/thChzTWq1-LKKAjRUXGxrTTahkLJxqAWrUeSBQdDjM3bGInZtXNffv4t81qGiRuWLyZ15Esjpso-EPYanAZ1seXIfrOnG4qyRtUT5u_5zAkmYL_qwQ

/blog/material-3-carousel-research-design

Material Blog

Reinventing the Carousel

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/99182de04736c3fc751e0e7213b57639dd48357b11a6bea852e1c807e8205f75a2cc4f0b1c467d4ce382266d94d6c0131ca1c89734b72cb25839c716566e863c

https://lh3.googleusercontent.com/RLsL-V8nlqAXqyYOhasGThLb8Pj3EhXWEApdOh6brJHN15xf8gQGQrP_svzKzHMr0_UYiUZsAD1oqdo_gQXceb7p-VZrOGuflSaCySb9_qrK3AUxyXs

/components/side-sheets/overview

Components

Side Sheet

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/bfad53d691a1f43e9cea15cfd332e17e3b9822fdf1a3615c2f425e515eb203d6deda45a602902a68649aa40b9949ebfd5f53fa44753a65a90f482e3b28ad8fa3

https://lh3.googleusercontent.com/akWbxMk7Ej8LzrOeta5H4yIskf77vyHpXbwovyFrWEPe2WKTr8uRMldrZsPKTsMWPPrai8PQODLt8qDBftgcGfdS7yJJLSBHIKqHnEbvJ6gvmBoiPw

/blog/material-google-io23

Material Blog

Material Design at I/O ‘23

mio-example
