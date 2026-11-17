# Building a Dark Theme for Google Fonts

Source: https://m3.material.io/blog/google-fonts-dark-theme
Content endpoint: https://m3.material.io/page-data/Posts/5760435980337152.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/2099bdf739f7b00b5752c21dd05600b1de3807ffd6f78b523817f93840dfb753c89816d6a03482f8ddc7929f6f2692a3541ec97b23d51730eeebdbbc0de79619

https://lh3.googleusercontent.com/ht6gKnPt8UyF3olSSt4hVIALArRVl98m3OTL6aPxijeQpOMd5ZxJvftuwdfdFKuyY3pdeucqUn-KdVl3YhYBj5g4BTw1WeZfhwIRb1A

Mariia Subkov

Google Fonts Software Engineer

mio-example

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/cc16664d857c61544adb6032c84ab1d8fe5a72705975f71dcb12963faf7491611eb3ae4c6f67b8441ef359b56496b3aa0998a9ce9ebff521bd5ab3ac416240c2

https://lh3.googleusercontent.com/DmF2Ugy6fwqjNlEjV9JHr0MRSujGoc2vKLuEtVulu7Bf2ldwkFlhq5poxZZVV4uWoCFsIfsaRCdoC4qorDQ0NMlS5_3FwUrNQvzvWw

SeHee Lee

Google Fonts Senior Visual Designer

mio-example

<p>Our latest Google Fonts catalog feature is... a new dark theme! Using the <a href="https://material.io/design/color/dark-theme.html">Material dark theme guidelines</a>, we were able to turn off the lights on the Google Fonts catalog while maintaining both core functionality and the Google Fonts brand.</p>
<p>Besides offering a fresh aesthetic, a dark theme can help users avoid eye strain in a low lighting environment. For the Fonts team, the dark theme feature takes on another important meaning, because we offer ways for users to compare and evaluate font selections. With dark themes becoming more popular, we wanted to showcase how fonts may look in a dark themed environment.</p>
<p>We even have fonts that are specialized for dark themes, like <a href="https://fonts.google.com/specimen/Signika+Negative">Signika Negative</a>. This alternative version of Signika is optimized for situations where light text on a dark background generally seems thicker, such as light emitting displays from computer screens to airport signage panels.</p>
<h2>Designing the dark from the light</h2>
<p>As we all know, color plays an important role in a dark theme. A dark color scheme is layered on top of an existing UI to maintain visibility and legibility of text and other visual elements.</p>
<p>The first step was selecting a darker background color. In our case, dark grey was the color of choice. The Material <a href="https://material.io/design/color/dark-theme.html">dark theme guidelines</a> recommend using dark grey, which can express a wider range of colors, elevations and depths in comparison to pure black.</p>
<p>Next, we modified the primary color to work better with the dark background. In the light theme, we use a blue from Google&rsquo;s brand palette as our primary color across the pages and components. Instead of applying the same blue in the dark theme, we selected a desaturated version to meet the accessibility requirements and to avoid a sense of visual vibration that can come from using intensely saturated colors on dark backgrounds.</p>
<p>We also adjusted text and icon colors, using 3 different shades of grey depending on the level of emphasis and hierarchy. We use lighter greys for primary text and navigational icons, and a darker grey for secondary text.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>Lastly, we added a different treatment for the card component. In light theme, shadows are used to express elevation on hovered, focused and pressed states. But when we applied the same default shadow values for the dark theme, the shadows did not show enough contrast and visual cues for different element states on the dark background. So we added a lighter overlay to the dark themed card components to preserve the same visual expression and experience as the light theme. This also helps with the components&rsquo; legibility and ensures elevation expression that&rsquo;s distinguable from the dark background.</p>
<h2>Implementing the dark from the light</h2>
<h4>Angular Material theming and Angular View Encapsulation</h4>
<p>There is already quite some information about the <a href="https://material.angular.io/guide/theming">Angular Material theming system</a>, which comes with several pre-built theme CSS files and includes the possibility to define a custom theme by creating your own theme file. By doing so, only the Angular Material components will be styled accordingly, not your custom components. To <a href="https://material.angular.io/guide/theming-your-components">style your own components</a> with Angular Material, you can create mixins that take your <code>$theme</code> as an input parameter and define all theme-related styles there. The rest of the styles used by your own components can be included via <code>styleUrl</code> in the corresponding TS files to keep them scoped.</p>
<p>But what should you do if many of your custom components are used only once, and you want to keep all of the related styles scoped? Or, what if in addition to <code>$primary</code>, <code>$accent</code> and <code>$warn</code> color palettes that can be defined in an Angular Material theme, you want to use additional palettes or one-off colors? These were questions we faced when implementing a dark theme on Google Fonts, and <a href="https://blog.angular-university.io/angular-host-context/">the benefits</a> of using <a href="https://angular.io/guide/view-encapsulation">Angular View Encapsulation</a> quickly became obvious: no accidental class collisions, easier maintenance, and shorter, simpler class names.</p>
<h3>Setting up the app</h3>
<p>For the Google Fonts catalog, we have a file with SCSS variables that define a curated palette of color-related semantics, for example <code>$app-primary-palette</code>, <code>$app-secondary-palette</code>, <code>$app-accent-palette</code>, <code>$app-warn-palette</code> and <code>$app-background</code>. Our custom theme definition uses those variables and we theme Angular Material components by creating mixins. Our custom components import this color palette file in their corresponding scoped SCSS files. It means that we can simply change our color-related values in one scss file and it will be changed in the whole app consistently.</p>
<h4>Introducing dark theme throughout the codebase</h4>
<p>So, how did we add a dark theme to such a setup? The challenge is that there is no 1:1 mapping between the light theme and the dark theme. Here&rsquo;s how we tackled it:</p>
<ol>
<li>We created a theme toggle component and a theme toggle service that adds <code>.gf-dark-theme</code> class to the body element.</li>
<li>We created an SCSS file with dark-theme-related color variables, similar to the one we already had.</li>
<li>We defined a custom angular dark theme using the <code>mat-dark-theme</code> Angular Material function and included it inside the <code>.gf-dark-theme</code> class<br /><code>.gf-dark-theme {</code><br /><code>&nbsp; &nbsp;@include mat-dark-theme(...);</code><br /><code>&nbsp; &nbsp;}</code></li>
<li>We added dark theme styles to the theme mixins when needed, by using the <code>$theme</code> config parameter.<br /><code>$is-dark-theme: map-get($color-config, is-dark);</code></li>
<li>In custom scoped components, we used <code>:host-context(.gf-dark-theme)</code> to style them when needed.</li>
</ol>
<p>Finally, we made our existing visual regression tests parameterized, to be able to run them for both light and dark themes. For that we used the <a href="https://github.com/junit-team/junit4/wiki/parameterized-tests">parameterized runner</a>, a JUnit 4 feature. Visual regression tests validate the correctness of the UI changes introduced by a new code by comparing the old and new screenshots of our rendered elements. By adding a theme parameter to them, the exact same set of tests is executed twice &ndash; once when UI elements are rendered in the light theme and once &ndash; in the dark theme.</p>
<h2>See it in action</h2>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>No need to wait any longer: the dark theme for <a href="https://fonts.google.com">Google Fonts catalog</a> is already available! Check it out and share your feedback with us on Twitter <a href="https://twitter.com/googlefonts?lang=en">@GoogleFonts</a>, via email (fonts@google.com) or via the feedback feature in the bottom left corner of our app. We hope you enjoy it! 🌚</p>
<p>And one last thing for developers &ndash; if you are implementing a dark theme in your own application, there&rsquo;s a novel digital technique to enhance your typography: try finessing variable fonts that have weight or grade axes. Learn more over about this over on <a href="https://css-tricks.com/using-css-custom-properties-to-adjust-variable-font-weights-in-dark-mode/">CSS-Tricks</a>.</p>

Screenshot of Google Fonts website in light and dark themes

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/9efebd43b3aa374c59682520d58638914d11349f926346cf803792b8bf1ac6b8c20954fc7cdd1ca292169a7940c7a4b8e1dc85c317c83606e54a8747a4d4fd8d

https://lh3.googleusercontent.com/hCrqDkj_XwfIRMp0MsZqxy61dlIIIizBTCF4WJmKBo3L_5CT9qQTZ4seg-mZEBDQda-_V2p_fY-KqD-8D5_te78o9gjJAqBzcqiBuw

GIF showing Google Fonts dark theme toggling on and off

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f4ef3421603dba30a614a644f3e68d9e0f5f33eacfdbe1d6cf4b0de3dee02e000110e55ba4d8700583e4dc566c3da4c74f9940f3ff96460a448a06d19269f73a

https://lh3.googleusercontent.com/iTiNCaHTGGTCPtmMB5ABF6PhYk_ujzvDIVkL1eqYjmIOsrWiGXmdb-lIkf7Z-r2V9mKw5--k6bGKMRlsgPnQHwI-Th7u04k80-y26g

illustration of the Google Fonts homepage

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/60adde145b72e4ed938fd617650e8b4b4f040aedb760a98d16adcde173f1dee28c71c2f0862ad71fbe4352f9dc8d776483ace6f35fcd00e66e72ffeeb778251f

https://lh3.googleusercontent.com/XyYL1gtZmsH8yqGNcybRTDjeFw9cwez-3m5GL0dQF2zUW5yolzoq7j7mXtNigUMD91YmGVMpM3sfSUypLK3n9n2BzJr7vB4lvkT1eg

News Fonts Design

 

{}

How Google Fonts implemented a dark theme in its Angular App

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6464063bd0236c1915dc815923214887b5dd7017cd9912c5029232366d80eff497922a7849338aa08d5962d96e6ed87af11e2f33a1121901d9e6dbbb76c4b0e9

https://lh3.googleusercontent.com/gTZpul8qSOGWU-Zjb4niygSmoDCyF2GSc59tflh_V9Dt-L2A_EZRJdi8r7cnsiiAEE8rQYA1gWdhhwIr8oi6oOWAUobfru5OQtvSAA

Building a Dark Theme for Google Fonts

2021-02-22T13:00:00

google-fonts-dark-theme

How Google Fonts implemented a dark theme in its Angular App

Building a Dark Theme for Google Fonts

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/502ccc669d4c0bff192474b068fc1f5af92668f8cb8879754afecdb3a6055310b1798ef88e295e895d35cb96298f6aa95181b0f95225d1ef6625377db772bd8d

https://lh3.googleusercontent.com/ODRj3P2s6YpA15xGqEBu6DKkTZshwpUdgpxeYZGPpEz8GQQqrn1lsS3SwWS2ulZKSZHokp0sJEk7pyUqZhNDs_S5GdVzz099MqTV8A

/design/color/dark-theme.html

Color

Dark theme

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/8d86c03a697cda71fef8a635511beaac0afd8cc1525bf9a58c463604c04d94043442e5514c69c0b290fbed89e0381818b473f41f31caa2ff6cd5e83c31a5b0ce

https://lh3.googleusercontent.com/P5yuAkqJt699qGbcw1uLTOHMdzLMnMI6m7I_Ig75FALDP3eS4m0mYKkxfespu53DvHtu16YorQznqZuaLYVI8eDsTCjn3p_zXGdI-g

/blog/dark-theme-design-tutorial-video

Material blog

Craft a Dark Theme

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/7bbd8dbc40e9bb70ada1a87ec1d452185fa1bd23acf217dfa51f2b67d3e72a68eb03d290d7e9597fd4b2df021c1576b89b9fb505ec454d2b9c9392a50b683326

https://lh3.googleusercontent.com/1T6DD1rCMym64PMEPWDZkXntz8DRWfB7ac7RWS2k_nH1goLXbSZLkQbYBcj2zk3hXyUI9NLkuE-bINnvvb6-STbawnxnzVlsd4mx

/blog/design-material-theme-type

Material Blog

Designing a Material Theme: Typography

mio-example
