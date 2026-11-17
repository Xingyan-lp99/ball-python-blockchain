# Material Design Components for Android 1.9.0

Source: https://m3.material.io/blog/android-stable-release-1-9-0
Content endpoint: https://m3.material.io/page-data/Posts/5473462043934720.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/e542d55e05d06e63bbf3dadd467d6f4889a15a6c2c43b46c812a48b6ee2adf7ff126e17cb0d3c04d4d2f24d216f00138ed4cd9cbf209538cb1bd0f4fd7ac7f15

https://lh3.googleusercontent.com/ECgal03qq-GPHfoWRZft82d97qPwwB-M4z1d-igDCWWAMWhJteOVP4HzaU2XhhQVfG9ME-_0DWTFA1eK28kgnTgTHBpSnTIhLK8TQKwE0zyq_lFckrs

James Williams

Material Developer Advocate

mio-example

```java
<com.google.android.material.carousel.MaskableFrameLayout
  xmlns:android="http://schemas.android.com/apk/res/android"
  xmlns:app="http://schemas.android.com/apk/res-auto"
  xmlns:tools="http://schemas.android.com/tools"
  android:id="@+id/carousel_item_container"
  android:layout_width="130dp"
  android:layout_height="match_parent"
  android:layout_marginStart="4dp"
  android:layout_marginEnd="4dp"
  android:foreground="?attr/selectableItemBackground"
  app:shapeAppearance="?attr/shapeAppearanceCornerExtraLarge">
  <ImageView
    android:id="@+id/carousel_image_view"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:scaleType="centerCrop"
    tools:ignore="ContentDescription" />
</com.google.android.material.carousel.MaskableFrameLayout>

<p>Fast on the heels of Google I/O, we&rsquo;re happy to announce the release of Material Design Components for Android (MDC-Android) 1.9.0.</p>
<p>The new Carousel component allows you to create experiences like photo galleries and interact with lists of items in more flexible ways than a <code>RecyclerView</code>.</p>
<p>&lt;mio-video index="0"&gt;&lt;/mio-video&gt;</p>
<p>It uses <code>RecyclerView</code> as a core so you can rest assured that it will be performant and integrate easily into your designs.</p>
<h2>Making your RecyclerView a Carousel</h2>
<p>To use a <code>Carousel</code>, start with a working <code>RecyclerView</code> and wrap each of your item layout files with a <code>MaskableFrameLayout</code>. They will instruct the Carousel how to adjust items in relation to each other.</p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p>Next, instead of using a <code>LinearLayoutManager</code>, use a <code>CarouselLayoutManager</code>.</p>
<p>Masking in <code>MaskableFrameLayout</code> ranges from 0% to 100% (0.0 to 1.0 in the code). When the layout manager needs to mask an image, it calculates a masking rectangle. The image below shows different masks applied to the same image and how each will reduce the image&rsquo;s visible area.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>If you are using images in your Carousel with a custom image matrix or other components such as text, verify these objects work well with Carousel&rsquo;s masking or optionally let them react to changes in mask size using an <code>OnMaskChangedListener</code> on your <code>MaskableFrameLayout</code>.</p>
<h2>How Items in A Carousel Are Masked</h2>
<p><code>MultiBrowseCarouselStrategy</code> allows a carousel to optimally display large, medium, and small items in the allotted space. It attempts to find the optimal amount of large items that will fit into the display with the least amount of size adjustment. After that it will add medium and small items.</p>
<p>In the images below, at the start of the carousel, we can see two large items, a medium item and a small item. At the end of the carousel, the arrangement shifts to become one small item, followed by a medium item, and finally two large items.</p>
<table style="border-collapse: collapse; width: 99.4334%;" border="0" cellpadding="0">
<tbody>
<tr>
<td style="width: 45.9929%;">&lt;mio-image index=1&gt;&lt;/mio-image&gt;</td>
<td style="width: 45.9929%;">&lt;mio-image index=2&gt;&lt;/mio-image&gt;</td>
</tr>
</tbody>
</table>
<p>For more information on integrating the new Carousel component into your app, check out the full <a href="https://github.com/material-components/material-components-android/blob/master/docs/components/Carousel.md" target="_blank" rel="noopener">developer documentation</a>.</p>
<h2>What&rsquo;s next for MDC ?</h2>
<p>We&rsquo;re hard at work on the 1.10.0 release with updates targeting Android U. The components or features we highlight in these posts are only a fraction of the work that lands in each release. Check out the <a href="https://github.com/material-components/material-components-android/releases/tag/1.9.0" target="_blank" rel="noopener">release notes</a> for a full listing.</p>
<p>You can follow the progress of new versions, file <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=bug&amp;template=bug_report.md&amp;title=%5BComponent+name%5D+Short+description+of+issue" target="_blank" rel="noopener">bug reports</a> and submit <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=feature+request&amp;template=feature_request.md&amp;title=%5BComponent+name%5D+Short+description+of+request" target="_blank" rel="noopener">feature requests</a> on GitHub. Check out the <a href="https://github.com/material-components/material-components-android/releases/download/1.9.0/catalog-debug.apk" target="_blank" rel="noopener">catalog app</a> to see the components in action. Also feel free to reach out to us on Twitter <a href="https://twitter.com/materialdesign" target="_blank" rel="noopener">@materialdesign</a>.</p>

diagram of how images are masked in a carousel

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f70b6f1de6c969344f6c760ad4600ea83732f3855a181f2d9279ff713038f2bfc2dd240754c17e311e8f2009c41c111ff73ffd59cfaeb591a71e239d4d8a7840

https://lh3.googleusercontent.com/6IdEWOsFfVrq_d0Yr-NSgnP0iMH-2jsQxlt0pB3hbWTUvVsevd3TdlUWS32V8ZloH9ymGp4zOjQR5XciIDrSvdpVwhY2kz9WQhc7Vok0xAUIsKTqhFk

screenshot of carousel in catalog app with scroll position at 0

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/8a6545d4199765d94839745480deae916b4109e6158820cabbbb3672cce0b8a612e6f0b0370c361785c388b4bb6b1650f7a381b9e0fff8c09ae2165c0e605a4f

https://lh3.googleusercontent.com/Q5PAFl0kJtvPGHel0TWAXN21Ym5Bal6SlaAkk33imuaKmDaQarDmkn6EgtPE31w0mMYFouo7R92edY5Iae_W81NHqWyv0rXF3mqFuNHVMrzICiLVTQk

screenshot of carousel in catalog app with scroll position at 100

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/b34a5b397e12f4b8220d12b91d4cc356ca553d4575def5d4a598da41970f337bfbca440130a417cdbea907191f515a63bbfd77c014be3768617bb635f5af7fb1

https://lh3.googleusercontent.com/6vKpHerJbKyf8Xm_3u8Kzkg_LpA-AEjxDuzzkK5hhfqbIkqA_oqJlAZ5E1p14Sus8Y7mRRhb4f1MVM7GzlGj4VtV18PeSRd4bcSSWNL1frlFC1jGSfM

animated carousel

carousel-animation.mp4

https://storage.googleapis.com/material-io-design/m2/assets/downloads/e584c6e0e54dc6c7e5fe4b80fcc93a6f1de49fce23eb4ea7473134ea848dbf99285e512a2b855519185cb7a5fb22f1555abb63d3760396c0e1c66721ed698b1c.mp4

abstract illustration of a plant sprout emerging from a cube

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/bf792f0ec4233c933811f2cbefb531ba58e2cc7296514c0f47bcb49d0d058a7686a108291692a31035a2afc841602100eeb90def119aa281f73899606cdb7f6b

https://lh3.googleusercontent.com/4lVyZj_pYByZSDxuL1o-us6nihWwgD9F5d6HjS6IyP4uxtSO-P3WNqA48hWSVq70q5riU9cJGXCGjbrmFp6KCk-G9MAXyZGehRqgnndJxZrEbCMRiXc

news,releases,mcd,android,stable

 

{}

New ways to navigate in and interact with your applications

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/a3f1f8e12aff0782a770d06f7cbe392c5df06d8f52f85f758f9e36d4a2144c939e94c796dbf9c9a17d3eb3ec6899d4f1126690e0f91e4c78e6eb20a8e2a10ad6

https://lh3.googleusercontent.com/BpllrB4LBgEDX7X3enGKrjQFEsfBxDYT3PYeRE4ytEPMHL-ZB5QMN0RzQ31h-_yat3znuKTfDlx97BM2CjPIJJV1I-Nmg9s90k1of86M_Sx7ITTOBTwq

Material Design Components for Android 1.9.0

2023-05-17T13:00:00

android-stable-release-1-9-0

New ways to navigate in and interact with your applications

Material Design Components for Android 1.9.0

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/bfad53d691a1f43e9cea15cfd332e17e3b9822fdf1a3615c2f425e515eb203d6deda45a602902a68649aa40b9949ebfd5f53fa44753a65a90f482e3b28ad8fa3

https://lh3.googleusercontent.com/akWbxMk7Ej8LzrOeta5H4yIskf77vyHpXbwovyFrWEPe2WKTr8uRMldrZsPKTsMWPPrai8PQODLt8qDBftgcGfdS7yJJLSBHIKqHnEbvJ6gvmBoiPw

/blog/material-google-io23

Material Blog

Material Design at I/O ‘23

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/f76a10ef20aa3042fc461583cb2a0ac1ce5df95cdd3478424b0e318c5d8ed57cf9492e0503c8f7a07cf19185a453e248c8b840fd2bacf8f608bf5f18e47a9271

https://lh3.googleusercontent.com/thChzTWq1-LKKAjRUXGxrTTahkLJxqAWrUeSBQdDjM3bGInZtXNffv4t81qGiRuWLyZ15Esjpso-EPYanAZ1seXIfrOnG4qyRtUT5u_5zAkmYL_qwQ

/blog/material-3-carousel-research-design

Material Blog

Reinventing the Carousel

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/b0af7868f875886b47f96f80ab4407beda3fb0fefdb5450451cc6de73c862c30820708f813fb9e74076de28ab3c8a2e1b07d025c73b987764ae1285eafe31d76

https://lh3.googleusercontent.com/CHpOx1NNo2e-TMDp_j8doShD-REUb2VcLXEgWzBoD9Lmii239pOQ-oIs0qgg3ngAaZzLYCpopvIGwOQNCchzfq806eplz-HIlv51dYdhE8eJc1QQRw

/blog/24-hour-clock-design-research

Material Blog

The 24-hour Clock Design Challenge

mio-example
