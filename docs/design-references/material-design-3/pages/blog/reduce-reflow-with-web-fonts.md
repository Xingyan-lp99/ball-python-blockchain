# How to Reduce Layout Reflow When Using Web Fonts

Source: https://m3.material.io/blog/reduce-reflow-with-web-fonts
Content endpoint: https://m3.material.io/page-data/Posts/4901981369663488.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/015bbb2ade0bd4dd24046bc626fa85c38403a3a16faa518c555a457d05f01a2d2b2cf50a4055177528a06d595235e5fd03dfdac1a05f787e24a28a88cbd9e1dc

https://lh3.googleusercontent.com/7p8j5Qhfi5u35kddUdZJ4-y4tCO7bA-YHkfQvkOTE0STQh2LCNLCXvdz9hGVfwe8f4rkpIsN4619dk1hoTWS-U5zPZy072GqBD5OdD9l4QGSOqkmJig

Dave Crossland

Fonts Programmes & Operations Manager

mio-example

<!-- 1: links at top of head -->
<head>
<meta charset="utf-8">
<!-- 2: preconnect -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<!-- 3: use font-display -->
<link href="https://fonts.googleapis.com/css2?family=Roboto&display=optional" rel="stylesheet">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Roboto&display=optional" rel="stylesheet">

<p>Font loading times are becoming more important than ever as they can influence your Google Search page ranking. These loading times are important to visitors because fonts play a part in how often a visitor experiences unexpected layout shifts as pages load. Cumulative Layout Shift (CLS) is a <a href="http://web.dev/cls" target="_blank" rel="noopener">metric for web page quality</a> that quantifies this experience.</p>
<p>When a web font is loaded a little slower than the time it takes to start rendering the page, browsers will either render the text using a fall back font (unstyled) or with a blank area (invisible) until the font has loaded.</p>
<p>This is known as the &ldquo;flash of unstyled text&rdquo; (FOUT) or &ldquo;flash of invisible text&rdquo; (FOIT) and these flashes of text repainting will reduce a CLS score. There are a few different optimization techniques, <a href="https://web.dev/optimize-cls" target="_blank" rel="noopener">described on web.dev</a>. One technique can prevent flashes of text from happening at all, but this is a significant trade-off because many users simply won't see the web fonts at all.</p>
<p>When using Google Fonts there are three key optimizations you should use, and ensure are present in any previous integrations. Here&rsquo;s an example of what to do if you&rsquo;re using Google Fonts&mdash;you can use this HTML to integrate the Google Fonts API.</p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p>The benefits of the three optimizations shown above are:</p>
<h4>1. All GF <code>&amp;lt;link&amp;gt;</code> elements are at the top of <code>&amp;lt;head&amp;gt;</code></h4>
<p>By placing the font link elements immediately after the head element and the mandatory first meta element to define the page&rsquo;s encoding, the browser can start the web font loading process as early as possible.</p>
<h4>2. Preconnect to fonts.googleapis.com and fonts.gstatic.com</h4>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p>These links instruct the browser to open a HTTP connection to the Google Fonts API domains, so that assets loaded from these domains can start downloading faster. You can also use the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link" target="_blank" rel="noopener">Link</a> http header, which is processed even earlier. <a href="https://web.dev/preconnect-and-dns-prefetch" target="_blank" rel="noopener">Learn more on web.dev</a>.</p>
<h4>3. Use font-display</h4>
<p>&lt;mio-code-snippet index=2&gt;&lt;/mio-code-snippet&gt;</p>
<p>This API option requests that the CSS returned by the Google Fonts API will include a <code>font-display</code> property. We advise use of one of the following options, depending on what trade-offs you prefer:</p>
<ul>
<li><strong>optional</strong> - best CLS score, worse typography. Many users will not see the web font at all, since it will only be shown after it is downloaded.</li>
<li><strong>swap</strong> - worse CLS score, better typography. Most users will see the font, but they will experience layout shift if the font arrives late.</li>
<li><strong>fallback</strong> - a middle ground. If the font arrives a little after content is drawn in a fallback font, there is some layout shift, and a worse CLS score.</li>
</ul>
<p>These trade-offs are broad guidelines. Depending on what other content your page loads, the font may consistently be ready in time because other parts of the page take even longer to load. Or, if the font is the only external resource, it may almost never be ready in time. For example, the AMP team <a href="https://bugs.chromium.org/p/chromium/issues/detail?id=1231827" target="_blank" rel="noopener">has found</a> that using &ldquo;optional&rdquo; stops the font being used on the page. AMP pages only allow inline stylesheets, meaning the page is ready to render before the fonts have a chance to download. Therefore setting the API&rsquo;s Display feature to &ldquo;swap&rdquo; may be better in this case.</p>
<p><a href="https://web.dev/preload-optional-fonts/" target="_blank" rel="noopener">Learn more on web.dev</a> and <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display" target="_blank" rel="noopener">MDN</a> to determine what option is right for your use-case. Tools like <a href="https://www.webpagetest.org/" target="_blank" rel="noopener">webpagetest.org</a> can help review the loading characteristics of your page under varied conditions.</p>
<h2>Other Considerations</h2>
<p>The CSS Font Loading API allows you to take direct control over loading and applying fonts. <a href="https://developer.mozilla.org/en-US/docs/Web/API/CSS_Font_Loading_API" target="_blank" rel="noopener">Learn more on MDN</a>.</p>
<p>There&rsquo;s also an advanced technique emerging, to use fallbacks with some new CSS properties for scaling and shifting them, so that when they are replaced by web fonts the resulting layout shift is reduced. This is slightly tricky because not all operating systems have the same set of fonts to fallback to. <a href="https://www.smashingmagazine.com/2021/05/reduce-font-loading-impact-css-descriptors/" target="_blank" rel="noopener">Learn more on Smashing Magazine</a>.</p>
<h2>Conclusion</h2>
<p>These recommendations are relatively new compared to the lifetime of Google Fonts, so there are many older integrations that don&rsquo;t use these techniques yet. If you haven&rsquo;t updated your Google Fonts code this year, take a look and tune up your site to enhance your users&rsquo; experience today!</p>

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/ae6ba94067c2ffad3109d9c5ab845ab3e45b2dd1204f2f4b77367001a2801c67d09cf116437bacc8f28dae065d54eeaee6cf0eef797a336def2ab012e7f2e7f6

https://lh3.googleusercontent.com/95NJbbjo3Rvp4XIU4q1H76ANliAnf8Y8J6n7lUjF69MNz3-LE6UypCUlf3_yX4oWmLytCn1_B_0bt4w3bQUlTndWb7Jq98o8ApvNQDiOfiNXyp93vqg

{}

Learn about how using web fonts can now reduce your page’s search ranking. Here are best practices for font loading to improve the user experience.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/095006a85e532a7ea1de4ec68cd9ed389878272a0db0b2f196f4506670d3556b3276acbf5de504574b746b982f3b4778e81b67ec2a3fcb81b94156c598cbaee0

https://lh3.googleusercontent.com/XdNtaEZy39yGhUfst2hnRF9Nz_SQ5D80QQR7ZAyXXYhtd4Vy0qPFxmo1x4ynwZDlwPovMehUKqG5tw4WxJBz63k_3DPhFbkAnoexMAzx2SrzimCE2No

How to reduce layout reflow when using web fonts

2021-09-09T09:00:00

reduce-reflow-with-web-fonts

Applying best practices for font loading can help improve the user experience

How to Reduce Layout Reflow When Using Web Fonts

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/10670050668c02a15305405869d10261ae9184c4b9943da19db1f77dfec09cbadff181927e3ee1b025e024736848d2c53950c779e44a033489d2f68c57607b44

https://lh3.googleusercontent.com/-WjjawJvR9AIODJEhrs_slzoG32Y_Ip0a0c_qe04DMIR2zS0UGQxrmY7DU0LH8--_G45NFBmIFEmAdGxbVC31KCl4Zw6h3Yz-L3pff45FVFM8rINVFw

Designing Text for the People Who Read It

/blog/designing-text-visual-acuity-research

Material Blog

Designing Text for the People Who Read It

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/cb89a76898de6e89c4b5871b74a9c5af1dedd18b9d06022242786ac567b924c50a6909ccefec0d5ed1a6a24647942e3eb4d09528b35d6ac3409b02f9ec66d943

https://lh3.googleusercontent.com/73iO8YmQkBvE-z_OPQdm0gRC1XUeIOtUzaw4TlE3EZasN2WSmY1c0Q0Db2ssfcXEFBp12motVhIHff5qk1UEXUrOuzxvpilXXn3w

Google Fonts loves Material Icons

/blog/google-fonts-material-icons

Material Blog

Google Fonts ❤️ Material Icons

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/b3ba7a68fbda805ebc7c5fbd26bd7d5ff2978797b1d733b66819e9b8d1d7771cd1f439e96f766b499ed83b924d677c90132fa71f828b2f0e323528f8d688602f

https://lh3.googleusercontent.com/nLnu3NrhONUqGTIRjC-WCHLE0MAtC6IeU6kTa4CD9QBL943wg29dvvXpO7YRWiyS3lrFGFRaQhR7xtdIRDzt-T1rqw4EQw13YDy3

/design/typography/the-type-system.html

Typography

The type system

mio-example
