# The Science of Color & Design

Source: https://m3.material.io/blog/science-of-color-design
Content endpoint: https://m3.material.io/page-data/Posts/6502590191501312.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/2afa37f5c7d703c50563a276b0cbb1409a33c9f7369d51659d02acf6981e99deb9f3cf86de967ff29a45cafe0feae72a5e179e45ec0e437f0a1228b983ee7d2c

https://lh3.googleusercontent.com/_fhU39fgxIirQ30QC3vgWrA3HxeF9Db4r2o6zviUs5G7XRNrZ4KgXY0mo39SK1GHen-CgEyKb80geoy09PlxkKTHdDRZpyhth4jGf_z3vbvBsqRgRfo

James O'Leary

Color Scientist, Platforms & Ecosystems

mio-example

<p>I joined Google as a software engineer with a background in print and digital design. My first project was helping build a new user interface for the Assistant in Android 10. A challenging part of the design was the background&mdash;it was unclear where to place text to make sure it was legible, and there was debate over whether it was visually pleasing as it faded from black to translucent.</p>
<p>Miranda Kephart, a fellow engineer on the project, pointed out whether it was visually pleasing was based solely on the perceived smoothness of the color distribution while transitioning from black to transparent.</p>
<p>My initial reaction was this couldn&rsquo;t be the case. Designers never talked about color distribution like that, or even talked about altering it, it must be correct already. As soon as I said that, I was struck by the questions it raised: What if design and engineering aren&rsquo;t completely separate? What does it even mean for a set of colors to be &lsquo;smooth&rsquo;? What does it mean for colors to be organized smoothly? Are there even answers to those questions? If we can get answers to those big questions, do they even help us know where to put the text?</p>
<p>Finding answers to those questions took me a couple years and a deep dive into the history of color, both scientifically and in design. The answers pointed to a new color space that would empower designers creatively, and improve everything we do with color.</p>
<h2>Toward a perceptually accurate color system</h2>
<p>The way to construct a smooth distribution of colors is to use a perceptually accurate color system. These systems organize colors in a 3D space by matching how people see them, and they are built by creating formulas to fit data gathered from surveying thousands of people in thousands of experiments over decades. These experiments, generally, show people two colors and ask them to choose the one that is lighter / more colorful.</p>
<p>The three dimensions the eye uses to organize colors are hue, colorfulness, and lightness. Hue tells us what angle on the color wheel to use, say, red versus purple. Colorfulness describes how vibrant or neutral (close to gray) a color looks&mdash;the further away colors are from the center of the color space, the more colorful it is. Lightness describes how close to white or black a color appears. In color space, lightness is vertical, like floors in a building.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>The color system used by designers today is HSL, or hue, saturation, lightness. HSL isn&rsquo;t remotely accurate, and doesn&rsquo;t try to be: it was built to make computing colors fast on 1970s computers.</p>
<p>Our brand new, perceptually accurate, color system is called HCT, which stands for hue, chroma, tone.</p>
<p>Even though HCT is brand new, it is built on existing work: color science defines many perceptually accurate color spaces. For simplicity, let&rsquo;s focus on two of them: L*a*b, also known as LCH, (lightness, chroma, hue) and CAM16.</p>
<p>HCT&rsquo;s lightness measure, tone, is the same as L*a*b*&rsquo;s lightness. Using that lightness measure, along with some math tricks, meant we could measure contrast with HCT, directly integrating contrast checker algorithms and accessibility requirements.</p>
<p>HCT&rsquo;s hue and colorfulness measures, hue and chroma, are the same as CAM16&rsquo;s hue and chroma. You may wonder why we didn&rsquo;t just use L*a*b*&rsquo;s hue and chroma measures, then, we could have just use L*a*b*! However, when we tried using it in design, L*a*b* was too inconsistent perceptually.</p>
<p>For the first time, designers have a color system that truly reflects what users see, taking into account a range of variables to ensure appropriate color contrast, accessibility standards, and consistent lightness/colorfulness across hues.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<h2>Exposing and solving for contrast</h2>
<p>Color contrast has long been a challenge for design.</p>
<p>When I was a print designer, contrast meant whether there was enough difference between colors to be readable. Put simply, black text on a black background had no contrast because there was no difference between the colors.</p>
<p>When I became an engineer at Google, I was shocked to learn there is a precise definition and formula for contrast: the difference in luminance, or, perceptually accurate lightness, between two colors. Also, design was bound by contrast: any software we ship must meet minimum contrast standards. (<a href="https://material.io/design/usability/accessibility.html#color-and-contrast">Material has an excellent page diving into this more</a>)</p>
<p>In the past, designers would plug color pairs into a contrast checker, receiving a number called a contrast ratio that would indicate whether or not there was an appropriate difference between colors. Adjusting the paired colors to meet the requirement wasn&rsquo;t easy: no color system could adjust lightness while maintaining colorfulness and hue, leaving designers to guess new colors that would meet contrast ratio.</p>
<p>The HCT color system makes meeting accessibility standards much easier. Instead of using the unintuitive measure of a contrast ratio, the system converts those same requirements to a simple difference in tone, HCT&rsquo;s measure of lightness. Contrast is guaranteed simply by picking colors whose tone values are far enough apart&mdash;no complex calculations required.</p>
<p>For example, to meet <a href="https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html" target="_blank" rel="noopener">WCAG contrast requirements</a>, smaller elements (less than &frac14;&rdquo; or 40 dp) require a tone difference of 50 with their background, larger elements require a tone difference of 40. This principle works consistently for any pair of colors.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<h2>Creating a scalable design system</h2>
<p>Just as design systems enable design at scale, HCT supports color at scale. HCT&rsquo;s simplification and integration of contrast via tone, makes the color system the right foundation for any scalable design system.</p>
<p>When creating a design system, colors are given names, so they can be referenced in design specifications of screens and UI elements. An example in Material Design is &ldquo;primary,&rdquo; which refers to a color used for buttons.</p>
<p>Then, the tone of each color is defined. Colors work in pairs in a user interface, such as a button color and button text color, and tones are chosen to ensure contrast between those pairs.</p>
<p>The other components of color, hue and chroma, are open to any values, enabling more creativity. Material You completes its design system by determining hue and chroma dynamically based on the user&rsquo;s wallpaper, creating a dynamic, personalized color system.</p>
<h2>Dynamic color: Personalized color at scale</h2>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p>Material You&rsquo;s colors are dynamic: it chooses colors in the user's wallpaper, lets the user pick one, then creates an entire UI theme around that color. All of the algorithms behind this are infused with creativity and a designer&rsquo;s eye, creating a beautiful theme for any color.</p>
<p>First, the wallpaper is quantized, reducing the thousands of colors in it to a smaller number by merging them in color space. The reduced color set is small enough to run statistical algorithms against with efficiency. These algorithms are used to score and filter colors; Android 12 gives colors points for colorfulness and how much of the image they represent, and it filters out colors close to monochrome.</p>
<p>One color, defaulting to the top-ranked color by the algorithm, or chosen by the user in the wallpaper picker, becomes the source color. Its hue and chroma influence the overall color scheme, enabling a vibrant blue scheme, or a muted green one, based on the user&rsquo;s choice of color.</p>
<p>Using the source color, we create the core palette, which is a set of 5 tonal palettes. A tonal palette is defined by a hue and chroma; the colors in the palette come from varying tones. These tonal palettes reduce cognitive load for designers when creating a design system: instead of specifying hue and chroma for each role, a tonal palette can be substituted.</p>
<p>Finally, we fill out the table that defines the hue chroma and tone of each color role, then use those values and HCT to create the colors used in the theme.</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<h2>A bright future, built with you</h2>
<p>A design system is only as strong as the tools provided to implement it, and Google firmly believes in sharing our work through open source code.</p>
<p>Material Color Utilities is a cross-platform code library for color, containing everything needed to implement Material You. It was initially built for Pixel; as covered in a <a href="https://android-developers.googleblog.com/2022/02/material-you-coming-to-more-android.html" target="_blank" rel="noopener">blog post</a> last week, Android phone manufacturers use it as well. The library is open source, anyone, inside or outside of Google, can contribute to it. The library will be expanded to include new platforms and modules in the near future. We have <a href="https://github.com/material-foundation/material-color-utilities" target="_blank" rel="noopener">Dart, Java, and Typescript libraries</a>, and we will open source libraries for iOS, CSS via SASS, and GLSL shaders.</p>
<p>We'll continue updating this tool and adding new code modules as we develop new color features. <a href="https://material.io/blog/dynamic-color-harmony">Color harmony</a>, available today, adjusts colors to dynamically fit the source.&nbsp;By the end of March, Material Color Utilities will add modules for:</p>
<ul>
<li>Legible text on any background&mdash;HCT&rsquo;s tone integrates with opacity, unifying contrast with scrims &amp; shadows</li>
<li>Image filters and blend modes that use HCT, maintaining creative intent and legibility, and a GLSL shader for HCT.</li>
<li>A new type of gradient that blends realistically, like our work on color harmony. Using HCT produces accurate blends that behave like paints, avoiding issues present in other color spaces.</li>
</ul>
<p>&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p>&lt;mio-image index=7&gt;&lt;/mio-image&gt;</p>
<p>Behind all of these features, current and future, is our HCT color system. It makes designing with color easier and more successful, from generating wallpaper-based color schemes to adjusting colors for accessibility requirements. HCT drives the tools our designers and engineers use, Material Theme Builder and Material Color Utilities&mdash;the same tools used inside Google&mdash;which let you deliver consistent, beautiful, colors everywhere, every time.</p>
<p>Have fun, we can&rsquo;t wait to see what you make with it! Breaking the stasis of unfeeling minimalism in the flat design era will allow people to create things we can&rsquo;t even imagine. Paraphrasing <a href="https://sexpigeon.tumblr.com/post/16729718345/path-puts-a-silly-amount-of-trust-in-its-avatars" target="_blank" rel="noopener">Tag Savage</a>: &ldquo;Modern museums are pretty in a designy way, but eventually, the particulars around them fall out of fashion. This is good for the museum. Now they can really mess up the place.&rdquo;</p>
<h2>Resources</h2>
<ul>
<li>Mark Fairchild&rsquo;s <a href="https://onlinelibrary.wiley.com/doi/book/10.1002/9781118653128" target="_blank" rel="noopener">Color Appearance Models</a> provides a strong foundation and survey of color science.</li>
<li>Andrew Elliot, Mark Fairchild, and Anna Franklin&rsquo;s <a href="https://www.cambridge.org/core/books/handbook-of-color-psychology/5A29A2BBA251510F1DCB9CBB746EE7D5" target="_blank" rel="noopener">Handbook of Color Psychology</a> is a compilation of research on many color topics</li>
<li>Josef Albers&rsquo; <a href="https://yalebooks.yale.edu/book/9780300179354/interaction-color" target="_blank" rel="noopener">Interaction of Color </a>discusses color science phenomena from design&rsquo;s perspective</li>
<li>Bruce Lindbloom&rsquo;s <a href="http://www.brucelindbloom.com/" target="_blank" rel="noopener">website</a> has reference equations for converting between color spaces.</li>
<li>Nico Schlomer&rsquo;s work, such as the <a href="https://github.com/nschloe/colorio" target="_blank" rel="noopener">colorio library</a> and <a href="https://arxiv.org/abs/1802.06067" target="_blank" rel="noopener">algorithmic improvements to CAM16</a></li>
<li>Jacob Rus&rsquo; <a href="https://observablehq.com/@jrus/cam16" target="_blank" rel="noopener">CAM16 live document</a></li>
</ul>
<p>&sup1; <a href="https://munsell.com" target="_blank" rel="noopener">Munsell.com</a></p>
<p>&sup2; <a href="https://commons.wikimedia.org/wiki/File:Munsell_1943_color_solid_cylindrical_coordinates.png">Image source</a></p>
<p>&sup3; <a href="https://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0 License</a></p>

In the early 1900s, MassArt professor Albert Munsell created the perceptually accurate color system¹
Source by SharkD, derivative work of Datumizer²
CC BY-SA 3.0 license³

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/262e6c01b07221bf06fc43fea2f41c7b0443290a6e1b3cc818f7aca5154abb8ed7ce7da4e93a3afdd9131e80d685cd45342d9a6d4a564d46ddf663e13e11f81d

https://lh3.googleusercontent.com/wB5PDoi6DRex1AOSXv9F-Pr_0QxVnJ8C6kUB-UEqrQ35Hb5vMtyWWtKOBolpoyMhEJuDVs07rEUnOEJqdPsEhRblGDs3eFrHpN8BINeCNrxpxjuh9I0

At HSL “lightness” 50, accurately measured lightness ranges from 33 to 96!

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6a91ee510fb16e3a16a95e9ab7a1cc00194621a334b69ace04f28a23a20c48165f05347f05c51b4893db40fddf0519558dd79287476d1ea6a0d053cd402165b0

https://lh3.googleusercontent.com/PWM-JWdCtOxcGHHoiZfm1HkSNNcMRXyGE4CRapU1lrFHo93W1dqHACB24x7FCuqFKA-6LTBMhEtSHsMkZcu8EsOrNaUWE6ixtknM1Sv7hhpHwvLWcG1-

Viewing LCH & HCT color spaces from the top, we can visualize Lab’s more inconsistent scaling

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d9cad68c2e54b3abad047762b68f7ea62e49c3ba82ed43b3cd32504a8561d6c088647554952e52a78af6af052153128ff7ebdcd491e05b1e750b7263d26514df

https://lh3.googleusercontent.com/V8hsEuYzWThQiqE6FdY0IHRwLsWjrmsOlNUEDMIsO_1LQyunBLiX71BM7VmnXam9V7sxTr6RZFcoit0-kD0TgZh3NG9VFxTkr4gHwBoZ_UFbyPGgsg

Claude Monet’s “Impression, Sunrise” shows why contrast measures legibility for all, not just non-standard vision: the sun and sky have exactly the same luminance, creating a hazy effect that makes the sun hard to focus on. When viewing the image in black and white, only seeing luminance, the sun disappears completely.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/9d3ee405d81850a2ad6929c181fdf8060fe607420b668f1d6eaf1ed71c2c259e4f0cd5bff713322716c96625bda570607f212edeca5f0b8b483089e3928953f1

https://lh3.googleusercontent.com/UwzVMjQUmpgj6k3F8oAb_7TuyjL7RqrVFTJtwdnu36DMq8tNiF40AFe59CDjP4YvNMWFK9Xh5FjJQY1QLu2bF5Y7LlVRxWxEbDTqnCg0U-v2SXk30nw

From left to right: 1.) Original image, 2.) Image quantized using Google’s previous algorithm, 3.) Image quantized using Google’s implementation of M. Emre Celebi’s quantization algorithm (arxiv.org/abs/1101.0395), performance enables many more colors, retaining colorfulness.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/52ae2fc05490135c4d2c4fb80a1bb1a11607519c5820f914eac04b2095170c49436c6852d9e1af766f67dca89e42647a52cf24dd659890f6725e8a1bf3d22292

https://lh3.googleusercontent.com/lpMERRSJV0-EYstnNp-H6UIc_kfyhLFTXP8j9lvIIS8XkmDxAXxbZswwOp9pLaq8Z50zFJKPRWRlH0GZKJvLSYpcmonsiGXs9Du0glI03BLIZb6kRVc

Tonal palettes generated from Google Blue, #4285F4

Tonal palettes generated from Google Blue, #4285F4

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/b797415d26e16445cb02555d63c78a24dc6d0087d63be8ba977cc8cca5b5f199f55cf8936ee3c0f75b50093d07396adb0d6463f54577a8dee2eb6f7092fabfa2

https://lh3.googleusercontent.com/25H1ut2RHsWhTK6Nr9jFuwBYpaXyOJtBlGhOTBcNhDWE4q8VoNWRExUxtLYyPyM4swITzlLYJF3pJ5WipEcVr9xdvyHtaCAA8zPn8v2h6Lcru5-tAh0

Scrims and shadows that ensure text is legible on any background.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/913125b8694848359888c5432f6c56c5cc13ab66cbcc405957c0b0ecc7d255ec36a1c4643333007fdd75b6265ef88375e57c07fcf92d95eed8e8b847dc550bce

https://lh3.googleusercontent.com/E_Te2ABKYJaO9sHwRChTB2JNgnpS_RMhqI79XAZfRb0aGCf__Wtm4drYJ2SdaRP9GNJBOCVODy66wPNU2ERQnlUSWQKPU__6hwnJ2_TeneTNap6ZjYQ

Gradients in HCT respect colorfulness and maintain legibility

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/255aa1139d26f92590826c8dd6ce00429888c334b418c11440b3152e80a333a8cfdd46e04bbfc9e3beb012914d7b7f6a31eb11f1094b29ec82670db62a35f5c2

https://lh3.googleusercontent.com/459crB0shmfQBhnWHtw5UPjX1x42hQ_1GNBxOjiwYootCbqzxno4rleDZ4e8ceuB1RDqyvyrtJTP7QkANIreOmp6Jwefk_yNGL42ZDSnXXCHmuXpvA

HCT, a new color space developed by Google for design

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d27e77dbcd15ca0303eebd2f30e22196d0fe858c93a267048edc2cf2dea5f09b3a59242b3c07fed624f347216cd9b55235c5a110cecc9be20ce2a93a9b46145a

https://lh3.googleusercontent.com/FgfF6od_qjYXbXowPPgL3IQ8T0QnEAZnoehlRcXHSXK7QXfHe_LvBm3SeYIkxhSRn3gBjjH4GEO6DYOex8btaN34lVDSzP7ZULMMSqoE7bsxyCWA0Q

{}

How Material used color science to make design easier and more expressive than ever before.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/b20932fa2616b180fedac7e23d41b6fcdcc4979eac1da3bbe53611965f18ec053050b6f04a44df9b74542649f078fb47ce88470f74ce370ef5521e054e175b07

https://lh3.googleusercontent.com/mNtv2QtIa-UluBtULbrhNsE54DlsjGLvIaKW7jSeAnHSDANT8rYDZTxdCRly2g69CSNxD-nrSW9BmXQYI8YmoSum1Z0h5rlY7inwjsiZh8MtNICaTa4f

The science of color & design - Material Design 3

2022-02-17T10:00:00

science-of-color-design

How Material used color science to make design easier and more expressive than ever before

The Science of Color & Design

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/2ac5132cf499f5e4be8b845646d44b611ee51f2395155da747410e09dbc002c2defb13b46e477f5ec2017190412cb7a5888ddb3de816ef73adc754cb30682ebc

https://lh3.googleusercontent.com/GOsSmlbb-lQREXRGYtvmfrANBZA9FbIz6bjkZegnm-3vh0-RjP2yVxA6ftRE2QZl_Yr-tQKPKCBHnbe4fNZ4e0XGZrGc6UO-p00vY5a1sIKIM_LhBBM

/blog/dynamic-color-harmony

Designing Harmony into Dynamic Color

Material Blog

Designing Harmony into Dynamic Color

mio-example

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

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/318785e7385b8e7a3922a39bb37b52bb2520ef6c4dbe4967ef952c12e53375193f039ae07c906e1fedc135314e38c5b14c0f340a48a53764727e401b29836eaa

https://lh3.googleusercontent.com/EFglKz-sfEB8uDeN-bzUFFxWVAlgpIYiiDJejQY1QLtZaLCZJhg9BtXJzz63s4_pbw9gcuywKWYLmucDgxGo1ABAw6UReRiWCQneUteHStmGTYKwHRo

https://m3.material.io/styles/color/the-color-system/key-colors-tones

M3 Color system

mio-example
