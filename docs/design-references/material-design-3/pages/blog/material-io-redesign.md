# Magic, utility, and redesigning Material.io

Source: https://m3.material.io/blog/material-io-redesign
Content endpoint: https://m3.material.io/page-data/Posts/6105825437417472.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/5ee154213c656e0b84cd323ba5a7a8ef5f650be5c5a9142a94745e91e86df2aef5d570d989b7b8aae66dfab9e6b125a1ff984b43a69955efbf97b1f07a7c6992

https://lh3.googleusercontent.com/ohpvGFp6YZfLCNN3wr-bQyY2CYTN0cJUNHGTi_ablixcCEVG0Pfnj-wMfzPeZJ6cH2IUjAzUaKWgEaMJAY00dI0v-wqwsY80P7NYAr_S14cBESVOziQ

David Allin Reese

Design Lead, Material.io

mio-example

<p dir="ltr">I often tell people that I am the design lead for Google&rsquo;s design system &ldquo;textbook&rdquo;. Material.io is the online textbook where readers learn, discover and reference design guidelines and is the core of Material Design&rsquo;s public offering. It contains a trove of specialized information about digital product design, written by a group of the smartest and most creative people I have ever met.</p>
<p><span id="docs-internal-guid-38bf68af-7fff-83a9-c094-6db9276f898c"></span></p>
<p dir="ltr">In 2021, Material Design 3 was introduced with an iconoclastic approach to visual expression and inclusive perspective on usability in digital products. In October of 2022, we launched a redesigned Material.io which reinforces Material Design 3&rsquo;s balance between spirit and usability.</p>
<p dir="ltr">For this refresh, the Material.io team showcased new features and components while also demonstrating how Material 3 principles can be extended to solve product-specific use cases, in our case, a rich library of information to help designers and developers build beautiful products.</p>
<p dir="ltr"><a href="https://material.io/" target="_blank" rel="noopener">Click here</a> to check out the new Material.io<br />&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<h2 dir="ltr">Connecting imagery, dynamic color and guidelines</h2>
<p>Dynamic color is a tentpole feature of Material You, a subset of features of Material Design 3 that make digital products feel personal based on a person&rsquo;s device wallpaper or preferences. When designing for Material.io, we considered how we could showcase dynamic color and the new color system while still maintaining the site&rsquo;s use-case as a reference material.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;To achieve this balance, we implemented a sub-feature of dynamic color called <a href="https://m3.material.io/styles/color/dynamic-color/user-generated-color" target="_blank" rel="noopener">content-based dynamic color</a> to modify the colors of Material.io&rsquo;s UI. This is similar to dynamic color, but instead of relying on personal preferences we relied on a beautiful set of imagery ranging in style, color and subject matter. These images were commissioned by <a href="https://material.io/blog/interview-oddfellows-m3-art-style">Oddfellows</a> and <a href="https://material.io/blog/jamie-chung-photography-interview" target="_blank" rel="noopener">Jamie Chung</a> and are styled specifically to compliment the diagrammatic and UI example images found across the site.</p>
<p>The dynamic color transformation creates a holistic visual experience by having the site reflect the content a reader is consuming, and demonstrates Material Design 3&rsquo;s new color system which uses a unique palette of tones and compliments.<br /><br /></p>
<p><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">&lt;mio-video index=11&gt;&lt;/mio-video&gt;</span>Component guideline articles are considered the bread and butter of Material Design&rsquo;s offerings on Material.io. With that in mind, the team wanted to bring the content-based dynamic color story into the reading experience of articles. Following the same theme categories as the component catalog, each component&rsquo;s article assets are themed accordingly, and Material.io&rsquo;s UI transforms to reflect that.</p>
<p dir="ltr"></p>
<h2 dir="ltr">Component catalog</h2>
<p dir="ltr"><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">&lt;mio-image index=3&gt;&lt;/mio-image&gt;A beautiful example of combining imagery, color and utility, the component catalog page assists readers in finding the best component for their use case. Component cards are organized into categories based on their function, and each of these categories has a unique theme color to showcase how the new color system applies to different components.<br /><br /></span>&lt;mio-video index=0&gt;&lt;/mio-video&gt;When a reader hovers over a component card, a beautiful background image appears, and the card&rsquo;s colors transform to match that component&rsquo;s theme. Giving the reader a sense of energetic power, this interaction begins to establish the connection between color and imagery that is a trademark of Material You.<br /><br /></p>
<p dir="ltr">&lt;mio-video index=9&gt;&lt;/mio-video&gt;A highly requested feature from Material.io readers was support for dark mode, and we thought we could take the request and push it a bit further. Each of the component catalog images (along with header images across the site) also respond to dark and light mode, transforming to reflect a reader&rsquo;s preference while also demonstrating Material Design 3&rsquo;s support for a dark context.</p>
<p></p>
<h2 dir="ltr"><strong>Wayfinding and navigation</strong></h2>
<p dir="ltr">When designing for print, the designer is primarily concerned with one interaction: the turning of a page (sometimes supplemented by cross-referencing of indexes, footnotes and glossaries).</p>
<p dir="ltr">In digital products like Material.io, information is inherently hidden behind more complex information architecture, and the user has to perform a number of gestures or actions to reveal it, this is magic. To help readers perform this spellwork, we wanted to provide a consistent wayfinding experience to help them find what they are looking for.</p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;The consistent visual treatment of Material.io&rsquo;s navigation components establishes a functional gestalt through shape and color, signaling to readers that these UI elements are part of a family, and they share a function in helping them traverse the content on the site.<br /><br /><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">&lt;mio-video index=2&gt;&lt;/mio-video&gt;</span>We combined the new navigation rail with the navigation drawer using a simple hover interaction which gives readers a sense of ergonomic speed and quickly provides an overview of the site&rsquo;s content with relative ease.<br /><br /><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">&lt;mio-video index=1&gt;&lt;/mio-video&gt;</span>Tabs allow readers to switch between different pages of an article on Material.io. We took the opportunity to create custom tabs to align with other navigation elements and express Material 3&rsquo;s shape language.<br /><br /><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">&lt;mio-video index=3&gt;&lt;/mio-video&gt;</span>A tertiary form of navigation, the table of contents component allows a reader to traverse up and down an article page. A notable addition to this component is the generous article title, giving readers persistent context for what article they are currently referencing.</p>
<p dir="ltr"></p>
<h2 dir="ltr"><strong>Marginalia</strong></h2>
<p dir="ltr">Marginalia, a beautiful word I learned not too long ago from a colleague which is used to describe elements found in the margins of a page. When redesigning the article experience for Material.io, the team considered some of these small, sometimes invisible details of the reading experience such as bullet points, semantic colors and list numerals.</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;We redesigned Do and Don&rsquo;t labels that avoid the semantic use of red and green, and instead used blue as the affirmative color. Nearly 10% of people struggle with red-green colorblindness (including myself). With that in mind, and with the assurance of 3 signifiers: text, icon, and color, we felt confident in making the call to depart from typical affirmative and negative semantic colors.</p>
<p>&lt;mio-image index=6&gt;&lt;/mio-image&gt;Material 3&rsquo;s shape story is dotted with the use of highly expressive &ldquo;cookie&rdquo; shapes, as the team likes to call them. Applying these shapes to bullet points at such a small scale, and randomly rotating them with some simple CSS provides a sense of understated iconoclasm, pushing visual expression for the sake of expression, rather than strict utility.</p>
<h2 dir="ltr">Expressing spirit through motion</h2>
<p>From full-screen page transitions to navigation component animations, the new Material.io expresses an energetic spirit through its motion, from changes in pixels to entire views.</p>
<p dir="ltr"></p>
<p dir="ltr">&lt;mio-video index=4&gt;&lt;/mio-video&gt;<span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">Top-level pages use a vertical slide transition, to reinforce the vertical nature of the navigation rail and drawer. Whole page transitions provide a sense of speed and cohesion by animating an entire page and its elements together, rather than having them load piece by piece.<br /><br /></span></p>
<p>&lt;mio-video index=5&gt;&lt;/mio-video&gt;<span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">When navigating between article tabs the view transitions using a lateral slide transition to reflect the horizontal layout of the tabs.</span></p>
<p></p>
<h2 dir="ltr">Variable Google Sans and Symbols</h2>
<p>Variable fonts and symbols allowed Material.io to implement them in a way to supplement states, providing distinct visual signals for interaction.</p>
<p dir="ltr"><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">&lt;mio-video index=7&gt;&lt;/mio-video&gt;</span></p>
<p><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">Material Symbols are a new set of variable icons from Google Fonts that feature weight, grade and fill axes. </span>Rather than relying solely on color to indicate state change, readers are also given the visual signals of icon weight and fill. Icons react by increasing in weight while hovering and decreasing in weight upon press; this again again provides a sense of magical energy and utility. For navigation components, icons become filled when an item is selected.<br /><br /></p>
<p>&lt;mio-video index=10&gt;&lt;/mio-video&gt;</p>
<p>Similarly, we implemented a variable version of Google Sans and utilized its grade axes to add another signifier to component states. By using grade rather than weight, text strings don&rsquo;t become longer and remain the same width as it&rsquo;s default state.<br /><br /></p>
<p><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">&lt;mio-video index=8&gt;&lt;/mio-video&gt;</span></p>
<p>As the Material.io design team, our goal is to represent the incredible work that Material Design does at Google as best as possible. So many incredible people are behind this work and it is a pleasure to act as both a steward and a catalyst for one of the most prevalent design systems in the world.</p>
<p><a href="https://material.io/" target="_blank" rel="noopener">Click here</a>&nbsp;to check out the new Material.io</p>
<p>To more systemagic,<br />David Allin, on behalf of the Material.io team</p>

Homepage of Material.io

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6ae67c71ea6e58490088f77dbd54db8a831d1ca20984a8954300fb82a63e1510a3c1852c9733a8a2d30d540e2343b9adbed34578dbab720861f696ed8058a344

https://lh3.googleusercontent.com/6aaoMqll-RgC38h6pundoR1u46I6QWJzsGK_r4ONvfy0Omj-7l6ZY9-j0SCYNvcjlOSwme89PLeQskYEj2i9_zMNOix1FwRN7-ZmRSZfq5KBHpV3ky4

Image of themed components against an illustrative background

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/ce4cc87ec3b7be4b938f6f95125444a813c38cd59d85a2efca86b5dd9d37ebde19564cc2bbac53bf0baef5b30debb6726dda0224a8ce8d735506b7437630072b

https://lh3.googleusercontent.com/ZBWTcgEGUl9hiLnxRhFSuNLeWHYP6zv5Y2XhiLY7p0wns-p9jGcpczu_jaKGEOYAtaaCgsc4HnTZ8rRu2uv59WJqlX6s61BtiaitbDHQLjf8Oef4AWY

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/27e43ee241a1432694be7c45bd3cc593516fd5bc73904c7a53a5ddbb16274b012bae5c7d5502ba42ce8c0c6a0ab1780acb9e92a5ae551acb5a3521b3dabb84f9

https://lh3.googleusercontent.com/UDB01XsiozdyyBYZV3-KwuTX2DwG1vkKqNi4go13E3u9IrV0-6-bTUO2CdYkH_v7qfqkiXBj_p4ZepQQp2Z_q_GDjZyECiPoIgTRwl8hdWazk5XUSoo

Component catalog page on Material.io

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/76d321a1bb174da661be788689fc2744a4eb6acaa9e900c19d73715da567220a05568b0d72d434cfbc51d7b0ed2b9d6b80545d1cca908f2d0ff42bdc416ad257

https://lh3.googleusercontent.com/hvoUcqePmGD08I30r_OJ9pzPsw7C0Nx5EZRk18Qw0Q4Z8dRJ186EImpJ4zZOzk5h7eVM-TXX-DjEw_Y7YLypAdakn4KJiwT2irwoPAOY27mMDi7KIILE

Juxtaposed view of navigation rail, drawer and tabs on Material.io

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/2963805cfc0ec1ec4bdde3b94bdbd943f2fe88131aebd36b7c48be73b156ef9eb4dd2454eb0492f9700e4c0eeebe6d7392a8f9bdc8396787e1c76b46015f360c

https://lh3.googleusercontent.com/j3pjWkdHIUoL5rdspLQGwuRv9Q8jAcaMRr0qZLLSXmqAlt4GNe0u6_wRx2vHrbIRiUgJcjqbj8bnhJ2XwN7ca4xVeBpZGBIK_t-dPAGXuLAa0Pz_gW4

An example of a do and don't on Material.io using blue and red as semantic colors

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/a9188a78c02d288967a049a94efdf6bf7e6de8b29a6ae7d2230b0b1a4d329cbd36fae26792ce31bac9a5b3785e74e04e894f85b2361175c7880dd2e00b418fb9

https://lh3.googleusercontent.com/Q-DgxCIfJG0OmK9wo6FaCX6ugHS9XMYn6aS_48F-wFV_tLGk5t6R2bmeOEAmqF2WmW5Uuo17mWo3z7bQiQPGkmU7sL7SMcg4d0cFp0c-6CF0CPfibw

Example of custom, star shaped bullets on material.io

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/18565306d66cc6aab369d20163cf430d5bafb40d92ca84f3ad7ac837e90d93ba8274cf8db9d10883bb70da8a5eed1ea743185fbd96b8d1f1c93a1c2dcb77a84d

https://lh3.googleusercontent.com/WyHHFm8QKPYsw_7qEdU3e2FtQ1kE3oHEReMoJJEG343LN1FW4T5-nciw0sUqXK4JBeL780AEyl0g7ULf8iziAbI5JBsl2QUws7A0OOyofY-7gYOsLFI

Component card animating between default and hovered states

component-card.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/3e7a9630e450205a0f985fca33abfa1899c3e732558150511a294d08e130eb59941d0b0163d66d5bf92e2a802c5952cb04a28cd2475cbb3b8fabef5f026a3b3d.mov

Guideline article tabs expanding and contracting upon scrolling

mio-tabs.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/df8f76985c2b22f04044f29863291e8f9a24f26e4239194e20ba7d900d622414b60b96a6cebb15f3fcde0f0d985953ba26516435e698e89c1b687fea136b074e.mov

Hovering over navigation rail items to expand the navigation drawer

nav-drawer-1080.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/b5a3d7f3f1f79fa543507f26a30d26508c3c9959763498be1bdea20cd382fe58ba8a7631cbba6fded193ae42d1dcda3494dc12ebc8c30be6fbe42eabe4d467a3.mov

Guideline article table of contents shifting up and down between article sections

toc.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/044c77ead50edde218a0f4966cf2b7fe8e304331e126cdd4249b6a89eeb72d45c207ef177a4eb7eae706e6dfcdb1e25b111dc17a4d91cbecfdd10e4dcc159c4a.mov

Material.io pages transitioning with a vertical slide animation

top-level-transition.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/da11b66042f6d377d27481f3dab0aab1727b1a9e1819fcf7d429313755887f91b0b99682e47a42253476faea78cdea762d265a1c0dde35b39da6062b206a4ec0.mov

Article pages transitioning using a horizontal slide animation

tabs-transition.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/9d6b254ce3e3b27a130447c966e350787cabbe406ce561ea520ac5e1e925b6920fb559384e72739b11c3a3eb913826302b2c0e04670eb91709b0c76674aabeb5.mov

Symbol increasing in weight upon hover and decreasing upon press

symbols-animation.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/bf130120593cad8e5c8166133f38cb614c86aacbb9f7edd1496be3b24f1d36b6065f36d71b9a2ee938438a24f45f7927c124c2370b7cbe989e9269660aa1a449.mov

Symbols in navigation rail increasing in weight upon hover and decreasing upon press

symbols-animation-nav.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/cc896ec8a2878448fd0e7c2c6ce733a9d4ac13408d177e6b796dcc9bc4f00cd4722bbc48a09dfc6d7751d73ae1ea365442ed8c2096f9ae9ad0ca12e8cd804331.mov

Illustrative video with a heart gently floating in a sea of blue and green grain texture

bookend-opt.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/5f9536152a11fbb965890615f00d06a980b4d5d3402a9773e07215584a0111aa443abff9da4da9a3925345e384fe46f100564af50b03d05f1ad781fc852ce238.mov

Component catalog cards switching between light and dark mode

dark-mode-cards.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/0033c898edbfdbad24c7914628bd1a2d83f6ae0b76e9df4c5fa89527aa69e0c37af70c18ac937660a9089f4980a7602a3fc7d03455a3ce79d0e2cd6a134d2050.mov

Google Sans increasing in weight upon hover and decreasing upon press

gs-text.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/cab6ec3d6d20bfedae7a988e5f806839274811f4d001ce285b753825e320c4ae2488ab2b2e309c638c4a3c96a951d72f2272315653c48a98d3187716180d29bf.mov

Examples of article pages sliding in and out of view

colors-articles.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/7cca6e2b0861dbd1f923f76995c874006b2632caf87f0550feff926e1e48794f41d47de7c0e16380f051560b8e2597e61dbb4293b015abec710db9e40df71005.mov

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/ba840129969103b278202d6868f32d21e5f56c733034205cef49d95f62ca2459c651da686477bd935383b86ac6560abb134fb19f63241906b64a88d897362fd3

https://lh3.googleusercontent.com/n1AFrqnEqCS6Ntd1UZtqoFZOgSmhYk_YX-CQa9J69XFZoChDhW1tyui1uGpBfh-VJOIJXYbDGfsVrFJfD0Lx9KpaHRguiAo_wG87UMyXc3VJSuwHHxTR

{}

Discover the exciting redesign of Material, pushing visual and interactive expression in design guidelines with Material Design 3.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/1a67d638a41c61910afb79d4c12bc95b7e36df1d30e27baa820db9ff4012176598ffef17adcfef2dcd418a66eeb57f9d5761af1df66a97b99748c70981fbc9df

https://lh3.googleusercontent.com/rUF2wlHfpAvvRlW1YHc4l5L3mpzScqwqNX1VjzAHBmoYilMRpkjczvfbv_FKiF75ZSTJCgqcZNX4anFS3068G_AFWXcVeiMkiRu34ZUdkWC1p7QKe00

Magic, utility, and redesigning Material.io

2022-10-18T10:00:00

material-io-redesign

Pushing visual and interactive expression in design guidelines with Material Design 3

Magic, utility, and redesigning Material.io

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/33c2831cc5a5bcbac0e3bcb0f286cb7c44d5d879d1648fcb3a6a4ba708490077cf17fb99002401938a03bdfbf6e8ced320b5fcb1117c7b2706ca80df70018c96

https://lh3.googleusercontent.com/p0F4A2gllcAMlnmvX6UDAzMmRbslUuDrCKovUcxmoZ0iB3C8Xpq-A_IgYej7QRgfrYYZM0lZOskk0TazYYhC90S7s2R1fJ8FMPahu6e2VmVQ7IEOTI8

https://material.io/blog/jamie-chung-photography-interview

Jamie Chung’s Artful, Abstract Photographs for Material Design

Material Blog

Jamie Chung’s Artful, Abstract Photographs for Material Design

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/6e1b33b4459260f611ad53abc79882c8b07c29ea5666480695b7ae7c7ced4753630b1200e7fee3d037144e614f520a48e5fde71da2ff40e4ee2a2403e9a7b29a

https://lh3.googleusercontent.com/yx1oQ8Lrfl4f07SbKimuQJheMhMxMrENYR9qX-Fc4FuCR1fdjT2WrF3ODg0DZQoWw2JMUTBhAxXXqACfwBzlf12BQnHbS2FhlQQhn_XubJY4neLNsIo

/blog/m3-a11y

Design for everyone

Material Blog

Design for everyone

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
