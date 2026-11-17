# Material Design Components for Android 1.4.0

Source: https://m3.material.io/blog/android-stable-release-1-4
Content endpoint: https://m3.material.io/page-data/Posts/5349126482690048.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/18a6db2775f36a6a1b0cae6a88e8df282b27cf4a9db808be9c693fd35bdd3314798a1545d32d424a38e33f75b203165168f010c199ce63799b5e91d6309969a3

https://lh3.googleusercontent.com/m-PDSndGA4cUhtNjSl4HXPqXIaHxvYG28BPPcal5dnXUge1Po6SJJw2I3RjrIYyKBY6exL4bXnjaDt9dusnuDVO_anSC8lzVK7pCvWo

Nick Rout

Material Developer Advocate

mio-example

```java
<!-- In layout -->
<com.google.android.material.navigationrail.NavigationRailView
    android:id="@+id/navigation_rail"
    android:layout_width="wrap_content"
    android:layout_height="match_parent"
    app:menu="@menu/navigation_rail_menu" />

<!-- In navigation_rail_menu.xml -->
<menu xmlns:android="http://schemas.android.com/apk/res/android">
  <item
      android:id="@+id/item1"
      android:enabled="true"
      android:icon="@drawable/icon1"
      android:title="@string/title1"/>
  <item
      android:id="@+id/item2"
      android:enabled="true"
      android:icon="@drawable/icon2"
      android:title="@string/title2"/>
      ...
</menu>

// In code
navigationRail.setOnNavigationItemSelectedListener =
    NavigationBarView.OnNavigationItemSelectedListener { item ->
    when(item.itemId) {
        R.id.item1 -> {
            // Respond to navigation item 1 click
            true
        }
        R.id.item2 -> {
            // Respond to navigation item 2 click
            true
        }
        else -> false
    }
}
```

```java
<style name="Theme.App" parent="Theme.MaterialComponents.*">
    
    …
    
    <!-- Duration attributes, for increasing area/traversal of animation -->
    <item name="motionDurationShort1">75</item>
    <item name="motionDurationShort2">150</item>
    <item name="motionDurationMedium1">200</item>
    <item name="motionDurationMedium2">250</item>
    <item name="motionDurationLong1">300</item>
    <item name="motionDurationLong2">350</item>
    
    <!-- Easing attributes, to define a set of curves to be inflated and used as Interpolators -->
    <item name="motionEasingStandard">
        cubic-bezier(0.4, 0.0, 0.2, 1)
    </item>
    <item name="motionEasingEmphasized">
        path(M 0,0 C 0.05, 0, 0.133333, 0.06, 0.166666, 0.4 C 0.208333, 0.82, 0.25, 1, 1, 1)
    </item>
    <item name="motionEasingDecelerated">
        cubic-bezier(0.0, 0.0, 0.2, 1)
    </item>
    <item name="motionEasingAccelerated">
        cubic-bezier(0.4, 0.0, 1, 1)
    </item>
    <item name="motionEasingLinear">
        cubic-bezier(0, 0, 1, 1)
    </item>
    
    <!-- Path attributes, which control the behavior of animating elements -->
    <item name="motionPath">linear</item>
    
</style>
```

<p>We&rsquo;re excited to announce the release of Material Design Components (MDC) 1.4.0! A host of exciting new features have been added along with many bug fixes and accessibility improvements. Get the rundown below.</p>
<p>Make sure to check out the <a href="https://github.com/material-components/material-components-android/releases/tag/1.4.0" target="_blank" rel="noopener">release notes</a>, and if you&rsquo;re using MDC for the first time, take a look at our <a href="https://material.io/develop/android/docs/getting-started">getting started guide</a>.</p>
<h2>What&rsquo;s new in 1.4.0?</h2>
<p>A fair bit has changed since <code>1.3.0</code> launched in February &ndash; we added the navigation rail component, added support for motion theming, and more. The things you loved from the alpha, beta, and RC releases of <code>1.4.0</code> are now officially stable. If you haven&rsquo;t yet started using <code>1.4.0</code> of MDC, there&rsquo;s never been a better time to update.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<h4>NavigationRailView</h4>
<p>Navigation rails provide ergonomic movement between primary destinations in apps. The rail is a side navigation component that displays three to seven app destinations and, optionally, a Floating Action Button. Each destination is represented by an icon and a text label.</p>
<p>MDC <code>1.4.0</code> allows you to use navigation rails in your Android app with the <code>NavigationRailView</code> widget. It has a similar API to <code>NavigationView</code> but has additional features to support Material Design Guidance for Large Screens.</p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p>Learn more about how to implement navigation rails in our <a href="https://material.io/components/navigation-rail/android">documentation</a>.</p>
<p>&lt;mio-video index=0&gt;&lt;/mio-video&gt;</p>
<h4>Motion theming</h4>
<p><a href="https://material.io/design/motion/the-motion-system.html">Material motion</a> provides a set of transition patterns that help users understand and navigate an app.</p>
<p>We introduced material motion in MDC <a href="https://material.io/blog/android-stable-release-1-2"><code>1.2.1</code></a> and have added many improvements since then. MDC <code>1.4.0</code> allows you to specify duration, easing, and path values for the Material motion classes &mdash; <code>MaterialContainerTransform</code>, <code>MaterialSharedAxis</code>, <code>MaterialFadeThrough</code>, and <code>MaterialFade</code> &mdash; with new theme attributes, similar to color, typography, and shape attributes.</p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p>Learn more about how to implement motion and how the new theme attributes map to the relevant classes in our <a href="https://material.io/develop/android/theming/motion">documentation</a>.</p>
<h4>&hellip; and more</h4>
<p>A variety of smaller features and bug fixes made it into this release. Check out the <a href="https://github.com/material-components/material-components-android/releases" target="_blank" rel="noopener">releases page</a> as well as the <a href="https://github.com/material-components/material-components-android/compare/1.3.0...1.4.0" target="_blank" rel="noopener">diff</a> between <code>1.3.0</code> and <code>1.4.0</code> for a full list.</p>
<p>Here are some of the highlights:</p>
<ul>
<li><a href="https://github.com/material-components/material-components-android/commit/b163458a3a7919d7b7c76de81a7a9b5c940c8def" target="_blank" rel="noopener">Updated the way BottomSheet handles insets</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/1fb57bcaa274f9de70553184e5eed35daf8153c8" target="_blank" rel="noopener">Updated "indicatorSize" in CircularProgressIndicatorSpec to be never less than twice of "trackThickness"</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/036cff7c33b6ce285ee5a4d49d2612249e0bce1a" target="_blank" rel="noopener">Updated CollapsingToolbarLayout to support framework android.widget.Toolbar (&amp;lt;Toolbar)</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/6015a4e901dc55a02f86e12703820d520684f95e" target="_blank" rel="noopener">Adjusted background of collapsed hint to not overlap with edit text's background</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/3e799428717a8f82b27f753c49f9748175b24121" target="_blank" rel="noopener">Localized numbers in MaterialDatePicker month</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/cbf528e3a6deaa2bc39d0836b3a850b27c2ada49" target="_blank" rel="noopener">Added support for centering MaterialToolbar title and subtitle</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/9c75ad07f7323387c7dae59455ea6ebc711b5f12" target="_blank" rel="noopener">Added support for CollapsingToolbarLayout fade out/in title collapse mode</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/948738e618416783694c9e4691454beb9701eeee" target="_blank" rel="noopener">Fix badge offset bug when attached and detached from a menu item on a toolbar</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/ffb2ad14ffaeb82901ff31ec79051f3c1ac068a3" target="_blank" rel="noopener">Fixed issues with MaterialButtonToggleGroup uncheck and check methods</a></li>
<li><a href="https://github.com/material-components/material-components-android/commit/eb5453cd7ee0cc8e0610b57d39b44b26cd95f31e" target="_blank" rel="noopener">Updated Material Button style to set the preferred maximum width to 320dp</a></li>
</ul>
<h4>What&rsquo;s next for MDC?</h4>
<p>The next feature release of MDC &mdash; <code>1.5.0</code> &mdash; is expected to land in alpha soon! Exciting new updates include <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/divider/MaterialDivider.java" target="_blank" rel="noopener"><code>MaterialDivider</code></a> and <a href="https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/divider/MaterialDividerItemDecoration.java" target="_blank" rel="noopener"><code>MaterialDividerItemDecoration</code></a>, and various improvements to existing components. As always, we encourage you to <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=bug&amp;template=bug_report.md&amp;title=%5BComponent+name%5D+Short+description+of+issue" target="_blank" rel="noopener">file bug reports</a> and <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=feature+request&amp;template=feature_request.md&amp;title=%5BComponent+name%5D+Short+description+of+request" target="_blank" rel="noopener">feature requests</a> on GitHub. Also be sure to check out our Android <a href="https://github.com/material-components/material-components-android-examples" target="_blank" rel="noopener">example apps</a> and <a href="https://material.io/resources/build-a-material-theme/">Build a Material Theme</a>.</p>
<p>We highly encourage trying out MDC <code>1.4.0</code>. If you&rsquo;re using its features in your Android app, leave a comment below or reach out to us on Twitter <a href="https://www.twitter.com/materialdesign">@materialdesign</a>. We&rsquo;d love to see it.</p>

closeup example of a navigation rail

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/7356ba902120ac9a5f0d3a74e51d96d9dff5b47482dc973634adb1fdc47f03c59cd36063b51a72314c7f15e5178cf0d91de54b2933318366b9464600c1aa2dd9

https://lh3.googleusercontent.com/5VzYIwV_8ou2j22qFy-9Oftt5qTt4EcR3pPK25bSBNlI7wx7CYzsDxzliGOyWWk6ClDr7nQ4yrXdGNHw7EnMaE2fbnSWR4YSAkuTG2MPyIwRx1B83M0

example animations from the Material motion library

material-motion.mp4

https://storage.googleapis.com/material-io-design/m2/assets/downloads/3f02013896d66b3c549d00dc7a08e945975aa1dbf737716139e1663e84d49ec785e07787bbc8384612d418346513c19a1cf858fc8f905f8004609863b7aa300b.mp4

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e747bfa3b691fc848baa8f03d807e5ca2789826630ca12047dafd116ed605a0026cf8afa04fc9418e96b916a0962b0f0996f7de4dc07b446eb65b29852a59c07

https://lh3.googleusercontent.com/iT2cU1VgnPw3KhRpDdRPCMvy86s4AR-SQxUORT_bCxmGF5UoZG_hezxrAYbEG4If_4VKM75Bo6sEVmyKQatN-b1CBaAyceoP20WJNSfaId21yi4qWQ

news updates android releases motion

{}

Experience the latest and most stable version of Android with the release of 1.4 from Material.io. NavigationRailView, motion theming, and more.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/0168b366a4d8f6134406e7699e781cd230a3f97e791cab8cc2ce4c87a7710e3bac0663726af4a9688f05f20d7b3371c2362fa2971853f0eb2bb397669ada2eb7

https://lh3.googleusercontent.com/1NMvmG3-lo_TeO2iS7OTB-sQV_OxtIZBjiTbnZ5HsWwOF_5EEdX6FateiwhF-19yFRbHGX9QTlEOcPM7zQ0E2lvEFEHKo1Uml-jrVn3zyg6d1mhI3w

Material Design Components for Android 1.4.0

2021-07-07T13:00:00

android-stable-release-1-4

NavigationRailView, motion theming, and more

Material Design Components for Android 1.4.0

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/1874c95e4db43e5eae3359036cd4467e17aee76cb434027311e07b0395fe8ffd4219ddaddd3ae53486637e78360c81ffd4ee80d7d2e7acb0f89ad71f7ff50f76

https://lh3.googleusercontent.com/hDpsCCt29gKQ-IpNynhQEy5fSKc6SX51ykRIM-zRDNlOVAqyFHu1XvM3MX58BrX0qQW6bJsp0g4vqPFo4uXrgJKmVnfFbUJLu4sq

/design/motion/the-motion-system.html

Motion

The motion system

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/94ccae5400c110b59e0a752e8e67a0d911b9ba63ce354ed4a9411a36992dc5866db038eea65fabe74ccef3b02bf04cd09f852f40647e788c30d1ad4501fc7c20

https://lh3.googleusercontent.com/TeLZea0Z3_3eKsf_VU8bMh3Nn_HNmY3gLNl915hP41iP3X6ZVaCZt3UO-n1PbYVSIN09dOanns3gqMM5bJhJ3es1bJt5Zk7Zq_6F8Q

/blog/android-material-motion

Material Blog

Building Beautiful Transitions with Material Motion for Android

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/d5675ebe9bf0ae48ff2b2ceb4a398f520213988fa29ed8d4880d6eeb8e3e90dbd86b984159e2351c3f09f5d2d7291abd2021470cb175bb5f33e5d6ea1bd56c34

https://lh3.googleusercontent.com/S7tRETMugOfyEoN-MQzELK44qZiBuIVxspkZgbOSK2qkJo-X9IqfZkTt0lonUHtzmD9ZYuXA6LlTUMZwu3Mxi5mmKBdPFF9F0MQ82w

/components/navigation-rail

Components

Navigation rail

mio-example
