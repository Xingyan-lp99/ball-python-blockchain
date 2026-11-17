# Material Android is Compose-first

Source: https://m3.material.io/material-is-compose-first
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/52808ced-97c2-4719-a022-baf4d5a60509.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Start migrating to Compose to get the latest from Material

## Tab 1

#data-origin-author

<p><strong>Material Android</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmpgoi79o-unnamed%20(1).jpg?alt=media

imageUrlFife: https://lh3.googleusercontent.com/FX52oDfuX9BS3Q8SWlAHzrBkPsBwAIGisPDUhj7RhOPDVYaR5hfIWqtTlf5VhE7Ru8e1eyidIjncoe2ygT_uq-WqxV-dh94K6U6YY3ysEi4=s512

<p>At <a href="https://io.google/2026" target="_blank">Google I/O 2026</a>, we announced that <a href="https://io.google/2026/explore/technical-session-30" target="_blank">Material Android is “all-in” on Compose</a>, alongside the official <a href="https://android-developers.googleblog.com/2026/05/android-ui-development-is-compose-first.html" target="_blank">Android Compose-first announcement</a>, marking a new chapter in Android development.</p><p>Later in 2026, we’ll promote M3 Expressive experimental APIs, making <a href="https://developer.android.com/develop/ui/compose/designsystems/material3?_gl=1*1gllpir*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0Mzk2ODQkajU0JGwwJGgw" target="_blank">Material Compose</a> 1.5.0 stable. Additionally, we’ll be integrating the new <a href="https://developer.android.com/develop/ui/compose/styles?_gl=1*1gllpir*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0Mzk2ODQkajU0JGwwJGgw" target="_blank">Styles API </a>for easier, more flexible customization, and have already integrated <a href="https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation?_gl=1*1gfyy5b*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0Mzk2ODQkajU0JGwwJGgw" target="_blank">Navigation3</a> into the Material adaptive library.</p><p>To focus on Compose going forward, <a href="https://github.com/material-components/material-components-android/releases/tag/1.14.0" target="_blank">Material Views 1.14.0</a> (MDC-Android) will be our final stable release for the Views library. There’s never been a better time to migrate to <a href="https://developer.android.com/develop/ui/compose/migrate/migrate-xml-views-to-jetpack-compose" target="_blank">Jetpack Compose</a>.</p><p></p>

Text: Compose Material 3 is going stable.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmov66zhn-02-IO26_133_TSV.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/eyRCYJ5DO3RV3ytnjO4Em1AW7huZ6GD234RPi1Fmsu1IyV3toeJo9kJ9FMZBqn9vuVc1MVujOSZisan6PYUxDzJUFH1lH-AMfbgJYJaSkLQj=s2500

<h2>The final Material Views release</h2><p>For years, Material Design has been on a journey to redefine how to build UI on Android. We’ve seen <a href="https://developer.android.com/compose" target="_blank">Jetpack Compose</a> grow from an ambitious idea into the engine behind the world’s most beautiful apps. As Android’s modern, declarative toolkit, it’s designed to simplify and accelerate UI development with less code and powerful native tools.</p><p>While Compose continues to accelerate, our updates for Views have become more focused. For the last few years, we’ve been preparing for a fundamental shift in Android development.</p>

A collection of expressive UIs, including media players, loaders, alarms, chat interfaces, and more.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmpgotv3m-16x9_Homepage_Hero_050825.mp4?alt=media

<p>Earlier this month, we reached a major milestone: the stable release of <a href="https://github.com/material-components/material-components-android/releases/tag/1.14.0" target="_blank">Material Views 1.14.0</a> (MDC-Android). This release officially brings Material 3 Expressive to the Views framework, as well as other improvements, unlocking more delightful experiences for Android makers:</p><ul><li><p>Expressive themes</p></li><li><p>Expressive list component</p></li><li><p>Emphasized type scale</p></li><li><p>Expressive styles for 11 existing components, like buttons, sliders, progress indicators, and more</p></li></ul><p>With this release, the Material Views library is now entering <strong>maintenance mode</strong>. It won’t get any new features, but will receive critical bug fixes.</p>

<h2>Going Compose-first</h2><p>Moving forward, Material Android is transitioning to focus all feature development on the <a href="https://developer.android.com/develop/ui/compose/designsystems/material3?_gl=1*wkss8e*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0NDAyMjUkajYwJGwwJGgw" target="_blank">Material Compose library</a>.</p><p>Later in 2026, Material Android will release Compose 1.5.0, which will promote M3 experimental APIs to stable, including M3 Expressive. M3 Expressive APIs are like an expansion pack to M3; you can opt in to them to deliver more premium Android experiences. This includes Material 3 Expressive components, motion systems, and more from the Expressive update. <a href="https://m3.material.io/blog/building-with-m3-expressive?utm_source=blog&amp;utm_medium=referral&amp;utm_campaign=IO26" target="_self">Read about M3 Expressive</a></p><p>For designers, the <a href="https://www.figma.com/community/file/1035203688168086460/material-3-design-kit" target="_blank">Material 3 Figma Design Kit</a> and our <a href="https://m3.material.io/" target="_blank">design guidelines</a> will continue to reflect the latest of what’s available in the Material Compose library.</p>

<h2>Styles API &amp; adaptive navigation</h2><p>We also announced the upcoming integration of Compose <a href="https://developer.android.com/develop/ui/compose/styles?_gl=1*u33d9*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0NDA4NzUkajQzJGwwJGgw" target="_blank">Styles</a> and the recently-launched <a href="https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation?_gl=1*1o80alu*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0NDA4ODAkajM4JGwwJGgw" target="_blank">Adaptive Navigation </a>update <a href="https://developer.android.com/guide/navigation/navigation-3?_gl=1*1ka87s6*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0NDA5MDAkajE4JGwwJGgw" target="_blank">with the new Navigation3 library</a>.</p>

As Styles API callout is triggered, Material Components callout changes in shape and color.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmowkaw0g-03-Shapes%20(1).mp4?alt=media

<p>The <a href="https://developer.android.com/develop/ui/compose/styles?_gl=1*1ycph1f*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0NDA5MTkkajYwJGwwJGgw" target="_blank">Compose Styles API</a> on Android will make it easier than ever to customize Material components. This will improve overall app performance by skipping the composition phase during style updates and will simplify creating cohesive brand experiences. Integration is ongoing, so stay tuned!</p>

A navigation bar on mobile is a navigation rail on tablet. The color themes change dynamically using styles.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmpgrimcu-04-Shrine%20Color%20Change%20(2%20Loops).mp4?alt=media

<p>For a long time, building adaptive layouts for foldables, tablets, and desktops was complex, requiring makers to manage and switch between navigation frameworks throughout the app. To solve this, we’ve deeply integrated the Material Adaptive library with <a href="https://developer.android.com/guide/navigation/navigation-3?_gl=1*1qvzpce*_ga*NTY0NTY0OTE2LjE3NzkzMzg2Nzg.*_ga_QPQ2NRV856*czE3Nzk0Mzk2NzgkbzckZzEkdDE3Nzk0NDA5OTYkajYwJGwwJGgw" target="_blank">Navigation3</a>. Since the navigation library now understands the intent of your screens through metadata, it handles the heavy lifting for you, making implementation much more efficient. <a href="https://developer.android.com/develop/adaptive-apps" target="_blank">Build adaptive UIs with Material components today</a></p>

An adaptive pane layout transitions all panes to the left when a button is selected on the rightmost pane.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmowkgbwx-05-ADAPTIVE_REFLOW_BUILD_RENDER%20(2).mp4?alt=media

<h2>Migrating from Views to Compose</h2><p>We know how much you’ve built on Views, but there’s never been a better time to <a href="https://developer.android.com/develop/ui/compose/migrate/migrate-xml-views-to-jetpack-compose" target="_blank">migrate to Jetpack Compose</a>. Get started by migrating your apps screen-by-screen with our <a href="https://github.com/android/skills" target="_blank">new migration Android skill</a>, which you can use with Android Studio, Android CLI, or any other AI tool.</p><p>Stay tuned for more updates coming to Material Compose!</p>
