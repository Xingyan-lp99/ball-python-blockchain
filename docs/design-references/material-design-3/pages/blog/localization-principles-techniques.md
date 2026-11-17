# Principles and Techniques for Effective Localization

Source: https://m3.material.io/blog/localization-principles-techniques
Content endpoint: https://m3.material.io/page-data/Posts/5550732958498816.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/369c95fe5019b07e689d250a71b99f23e954b4b1e7288cc521f9534e2f1b26e3402000d0d9b0ec2b449c286617c23522d81fa4a5aad5de6e88a30a6f158b944d

https://lh3.googleusercontent.com/WXzPP98RdDrDneOh7QCxSdNkjwk9_ACKefFU5vhW7DtED5EeHavMyWl7ttNSOzpRiLZqvYoZCQxVwxJ7Bi47CN8h4tj_nqxjuTsH1szGG5nt1dZgwtr1

Susanna Zaraysky

Content Strategist, Fonts

mio-example

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/d62da981995c0d4331abfe6dbf88baec1c5690d9105c0a6e9c9671a3a8cf719149c33647491a7c0dfb56aa0a515a0ff6f8249ddc72ef0c04f71e357643e728c9

https://lh3.googleusercontent.com/7WjPvKtW49-RW8ejdfh3De2YAz1G73YX9vPmyl57UYdAS1jct1pM6ZWxvY0WHufCL-c8Xx7f-7K_7udYSfBKYykSNSUx13ivbJKFan71KH6FmVcYvCNA

Yingdi Qi

Program Manager, Localization Product Strategy

mio-example

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/c2b3e2fc2b38d7ba77fff0752fcf307b7a4bd8103fa42b5f14343c1495ace7270084a75f203771035906281f657f4e717e7b72969a5cb6cf17b17c8dd670bbec

https://lh3.googleusercontent.com/QpoAKEULJRrJFxFPP-wl6cMvR7X6789-FKM0C48Da3DZ7UnOxhhBkdQNlqPPXezkIo74LqW1dLKVaqnQRhtPrh3L6pFBHyy5sJRDqDGhRWuaDpcirMs

Seongji Kim

Program Manager, Localization Product Strategy

mio-example

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/89dfcb525f2c86a2b753a0adc36bbc447afd51e577f5459e40c43fcd0ae503b32a6ee3f2c5db8845a685113c7cbe61d5cadafd0cd5a670355f8fc72164aac56b

https://lh3.googleusercontent.com/Whjqz6FiQu9j6_OJOjv1fygs63iuXW-TWqLAAO8P4T_3qFxVbHcBvQdg8zypUTFXXDeGmvpFH1XunOeGCmNDrfCjU7fvIOjokYOqZRgAntED2r9cxomd

Images by Annie Bartholomew

Material Design RARE Creative Fellow

mio-example

<p>Localization is the process of adapting messages, imagery, brand voice, features, and products to achieve a linguistic, cultural, and geographic fit for a given audience. The goal is to make user experiences for everyone as comfortable as possible across different cultural and regional contexts. It is important to consider localization if your product will be used globally, since a poorly or insufficiently localized product or content could create confusion.</p>
<p>The process of localization is often misunderstood to mean translation, but in fact localization deals with much more than word-by-word translation of text and content. Translation strives for a linguistic equivalent, while localization broadly considers adaptation for a market or cultural context.</p>
<p>Localization is also different from <a href="https://developers.google.com/international" target="_blank" rel="noopener">internationalization</a>, a practice and procedure for applications to support different local conventions, such as time, date and phone number formats, currency, measurement, and other data.</p>
<p>This post introduces principles and techniques to ensure that your products and experiences will work well across different contexts. Get to know the considerations and best practices for adapting content, imagery, and more.</p>
<h2>Design flexible and concise messages</h2>
<p>Expect messages to shrink or expand after translation and localization. For some languages, length can expand by 30% or might even double when rendered in a different language. For others, the localized text may be shorter but take up more vertical space. Lengthy text can get cut off, overlap, and lead to an overall poor experience.</p>
<p>To avoid text being cut off or overlapping, consider keeping messages concise while designing an interface that&rsquo;s flexible enough to accommodate different languages.</p>
<p><em>Learn more: For help with flexible size constraints, see our <a href="https://material.io/design/layout/component-behavior.html">guidance on component behavior</a> and <a href="https://medium.com/google-design/to-make-apps-accessible-make-them-compatible-with-different-devices-11298c6d3f06" target="_blank" rel="noopener">making apps compatible with different devices</a>. For ideas on how to make your app as easy-to-understand as possible, read about <a href="https://medium.com/google-design/improving-comprehension-through-intuitive-actions-f7e6336e12e6" target="_blank" rel="noopener">improving comprehension through intuitive actions</a>.&nbsp;</em></p>
<p>If you already know the languages that your product will be translated into, it helps to design for the longest possible translation of a given text. Consider using <a href="http://translate.google.com" target="_blank" rel="noopener">Google Translate</a> for a quick test of translated text length, or consult a localization specialist.</p>
<p>Leave open space around condensed UI components, such as buttons and tabs. Consider building extra room or a buffer into your design to accommodate the overflow of text. For longer text, establish a component&rsquo;s maximum width that allows lengthier passages to wrap.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<h2>Ensure that language and imagery are inclusive</h2>
<p>Whenever possible, edit any jargon, slang, or language that&rsquo;s used by a narrow or specialized group.</p>
<p>When designing for many cultures, use imagery and avatars that display various cultures, backgrounds, ethnicities, and demographic groups.</p>
<p>Avoid imagery and avatars that represent a single culture, gender, or demographic characteristic.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<p><em>Learn more: For help with communicating with international users, see our guidance on <a href="https://medium.com/google-design/writing-for-global-audiences-d339d23e9612" target="_blank" rel="noopener">writing for a global audience</a>.</em></p>
<h4>Icons and emoji</h4>
<p>Although icons and emoji are widely used for applications and websites, not all visual elements are interpreted in the same way across cultures. An icon or emoji might have a positive impact in one culture, but could be offensive in another.</p>
<p>To ensure that the icons you use are understandable for your audience, consult a localization specialist if available, or someone who can serve as a subject matter expert for the target culture or market, such as a local user, an in-market support team, or a translator.</p>
<p>To make text with emoji appropriate for a local context, you may need to move emoji around in the UI, add explanatory text, or change the icon or emoji to one that&rsquo;s better suited for the target region.</p>
<p>For example, in the United States the icons that look like a flame or fire 🔥 might connote &ldquo;trending&rdquo; or &ldquo;exciting.&rdquo; However, fire iconography as a positive value isn&rsquo;t universally understood. For a Polish audience, the up arrow is a more appropriate way to signal &ldquo;trending.&rdquo; It will aid overall comprehension if the trending icon is paired with the word &ldquo;trending.&rdquo;</p>
<p>When words are replaced with many emoji in a single line, it increases the difficulty for someone from a different culture with a different mental model to interpret the meaning. The translation effort becomes more challenging as well. As a result, users may get something that deviates from the original intention of the emoji. Additionally, multiple emoji in a single line can appear cluttered and visually distracting.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<h4>Fonts</h4>
<p>Choosing the right typography can impact how your product text appears in different languages.</p>
<p>System fonts usually support a limited range of weights. However, if your chosen font doesn&rsquo;t support various scripts, text in those scripts may be rendered differently depending upon the operating system and platform. The system default fonts also vary across operating systems. Chinese, Japanese, and Korean (CJK) system fonts (the typefaces that are pre-installed on computers and devices) typically use different font weights when compared to Latin characters.</p>
<p>It&rsquo;s recommended to use <a href="https://www.google.com/get/noto/" target="_blank" rel="noopener">Google&rsquo;s Noto fonts</a> if your product uses CJK or other scripts. Noto&rsquo;s name comes from the phrase &ldquo;no more tofu,&rdquo; because the fonts eliminate the tofu-like boxes (𛲢𛲡𛲠) for missing glyphs that appear when a font is not available for a user&rsquo;s text. <a href="https://www.google.com/get/noto/help/cjk/" target="_blank" rel="noopener">Noto CJK</a>, for example, provides full coverage for CJK characters in four scripts with seven weights: Simplified Chinese, Traditional Chinese, Japanese, and Korean.</p>
<p><em>Learn more about <a href="https://blog.google/outreach-initiatives/accessibility/preserving-endangered-languages-noto-fonts/" target="_blank" rel="noopener">Noto fonts</a>.&nbsp;</em></p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=7&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<h4>Line breaks</h4>
<p>Line breaks can appear incorrectly in languages that do not use spaces between words, such as many CJK languages.</p>
<p><a href="https://github.com/google/budou" target="_blank" rel="noopener">Budou</a> is an open-source tool that automatically creates line breaks for CJK languages, which improves text readability.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=8&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=9&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<p><em>Learn more: <a href="https://w3c.github.io/typography/#line_breaking" target="_blank" rel="noopener">Language enablement line breaks</a> and <a href="https://www.w3.org/International/articles/typography/linebreak.en#table" target="_blank" rel="noopener">approaches to line breaks</a>.&nbsp;</em></p>
<h2>Account for local design practices</h2>
<h4>Color</h4>
<p>Color choice can directly influence an individual&rsquo;s brand perception, While some colors are interpreted across many cultures with relative consistency, others convey a wide variety of symbolic meanings across cultures.</p>
<p>Learn more about applying color in the <a href="https://material.io/design/color/the-color-system.html#color-usage-and-palettes">Material Design color guidelines</a>.</p>
<h4>Information density</h4>
<p>Preferences for information density and design styles vary across regions and cultures. Density and style preferences can be explored with help from a localization specialist or expert in the culture. Within the same product or brand, designs may be changed to better serve audiences with different backgrounds or needs.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=10&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=11&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<h4>Bidirectionality</h4>
<p>Languages such as Arabic, Hebrew, and Farsi are read from right-to-left (RTL). If you&rsquo;re designing for left-to-right languages as the default, take time to ensure that your design is optimally mirrored for RTL languages. Learn more about <a href="https://material.io/design/usability/bidirectionality.html#mirroring-layout">bidirectionality</a>.</p>
<h4>Data formats</h4>
<p>Different regions have varying conventions for data formats, including addresses, phone numbers, names, calendars, measurements, currencies, payment methods, and more.</p>
<p>&lt;mio-image index=12&gt;&lt;/mio-image&gt;</p>
<p>Learn more:</p>
<ul>
<li><a href="http://cldr.unicode.org/" target="_blank" rel="noopener">CLDR</a> (Unicode Common Locale Data Repository): The international standard for automatic formatting of numbers, currency, and more.</li>
<li>Material Design <a href="https://material.io/design/communication/data-formats.html#date-and-time">Data Formats</a> guidance</li>
</ul>
<h2>Create and share guidance or visual references</h2>
<p>If you work with a translator or localization team, creating and sharing documentation around your goals will empower their work. Some examples of helpful documentation include:</p>
<ul>
<li>Product goals, intent, and details</li>
<li>User personas and demographic features</li>
<li>User journeys</li>
<li>Target markets</li>
<li>Brand voice guidelines</li>
<li>Tone and style considerations</li>
<li>Design mocks or sketches at any stage</li>
<li>How much freedom the translator can have in adapting your content. (You may consider <a href="https://borntobeglobal.com/2020/06/02/transcreation/" target="_blank" rel="noopener">transcreation</a>, a process to rewrite messages to fit the target culture.)</li>
</ul>
<h2>Don&rsquo;t forget to test!</h2>
<p>Standard research and testing, such as functional testing done by a professional tester and native speaker, will help reveal technical and functional errors in localized content.</p>
<p>To learn if your product, content, or design is effective and enjoyable across locales, test localized mocks with a small group of your potential users. Ask them to walk through a user journey and learn from their struggles or successes with task completion. Testing provides a better understanding of how likely your product or content resonates with a region or culture, and where any potential risks lie.</p>
<p>Even after launching a product, it&rsquo;s best to continue testing or user interviews to gather feedback as the product evolves. Distill those findings and insights and incorporate them into the next iteration of the product and content. Establish a cycle of research and embrace regional and cultural inclusion when designing and writing for international audiences.</p>

The height of the “Accept terms and conditions” button in English (1) is only one-line, and is increased to fit two lines of text in Malayalam (2).

do

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/67b682c5c8b5ff36539fecc6c27dcdee3ff3f88880826a09b838c934f8661737847156bfd7b375accd3827cddb6e8c60bad09ffe27fe67eb05899a7ec271d838

https://lh3.googleusercontent.com/2c32JY8yN6CPHad12GIjOyicpSZJF_zEdjpu2YN6gCr8aIi_u72a-r8CsaPEG9C-LlED3IZduosC7zWeKwnzDQ6belonZ9slh0C9J50mtqx3IBewt3be

The text in Bulgarian (2) is cut off after being translated from English (1).

dont

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/4ece8beaf393ab3227f3c4570b4d5e683733903d081f5a7c8be9a62aa8c9e9c3036c035f395bc6c27307778fffe1af0dc83fd086b366c5d2a8d2ba6119a05b6b

https://lh3.googleusercontent.com/ppomeRpFhsjEKU2tadCYE_TM0kcetR1CuoiLBFLXd744xqUGScmcM_Iz_PLJF0pEZaSLvFZb4yqfEOnHcB2OqwQv_EeDUCBkzXGMabqhWdPE7S4uzltm

Image with text 'Last active users', a search bar and 20 diverse avatars. Each avatar contains a small dot in the lower right corner indicating their activity status.

Use diverse avatars in imagery

do

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/1035caa5c806b62a75aaf46c312b92e2731c26651db8cd2d98346e37349f498188c3881d922938dbc4cfcf4774d5e0386f59a29411d32fd3602c826ff2be2711

https://lh3.googleusercontent.com/HGq7Z9Gjyj3Sh44lxpi_ZTAfk0Nqo9XgrTCoDlSS7hIrQYWtBSUba3XfmBbp143nFCXy7lg1iV-XkyTC6ruRauaBLgX5CfPw3_3zfqYclEjiNmzSpg

Image with text 'Last active users' , a search bar and 20 avatars who appear to be white. Each avatar contains a small dot in the lower right corner indicating their activity status.

Use avatars and images of just one gender or race.

dont

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/9801c0e24961fb056feca3b36423ee8bd78fd79b672a43d351638da61b41e5ce1d467d486047c5d4032061c685f79ba6c943e9de6deaeb20aaa1d15c02dc203c

https://lh3.googleusercontent.com/9oYgU8K4qB_dN9BzIBhEP1HhpW1K_XD5V1648h1PZ-C5mWr54mLrdcyvuNfZCZDtktFixdben3q-B8qoon7ayIhCP4y3JEZ-LxHhP6OxThuk0M3Xw6c

Photos of cat overlaid with text and open trunk of station wagon

By combining the flame icon with “Trending Posts,” the symbol is more likely to be understood.

do

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/7c42c2e01e5fb07b422c4a9107b4945fa4b6fe87dc772d1e761bfc9f484701593493ba5d92de0b44d57eea399740e7aa2320fcf24ca141d9cfe4f31c16795be7

https://lh3.googleusercontent.com/h-JG_Z38wxYLrKQ4jhJ-Tm7vmsFv4zLcs5UhpfEysikULJqYhuubaVuAZmnSXxNyH_NWvxVIQkw5yj36Ic4tv5NbMMgEL63h0wyO_gSVrVh-fE5wSw

Photos of cat overlaid with text and open trunk of station wagon

Replace words in a sentence with emoji.

dont

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/802d7c630fa95c0812ba318e2968a7b8c13ef9a57582c62528b000aca2a66d4b0fd19c4940167d07f43dc08da9883f3f26058351785cca6ca5b795b888da7006

https://lh3.googleusercontent.com/PkUNbE2Gtxc6xEILVQGRGCtwELhTIJx8DKV5a_ZLm-kJHC8EN08En3lqTkJnyvJ2jJfaDXKmiJ1p2BQCvGRAEIpWK8f-6FPoX5FQ4RlMs3jp8aPJ_IA

Google in Latin text and Japanese characters

With Noto fonts, both the Latin and Japanese text have the same weight.

do

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/46e14a7ce9ef3e02c830ddca5511c0a5c8517a9cd9793f40aeb0596520a0526c903cfeecebb7ead31e9aa62cb1a402e1dd6d62967cb69a273f52d7c4f8e3e3f6

https://lh3.googleusercontent.com/G7N0Dntib78CqzLKcq0L4iyKPqVaV4dl827NPr_JtJvrOJEQmj8h0Hb_3nYYQsYU0qx-BDJD8iDkIw2I-yODlE-1CBMjlxBGmivBBhTI_FMGoVRZIJ0_

Google in Latin text and Japanese characters

Avoid mixing font weights in the same sentence. The Latin type used for “Google” is rendered in a thin font weight, while the Japanese characters are rendered in a bolder weight.

dont

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/efb98aa5f817882d26bb420be8886b0cd00b3890bb796b7d1c19b3e64920cca2a3d341c80397f644e15b843d39b7f06380774e4dcb7ba2df2c10ec87bb8e74f4

https://lh3.googleusercontent.com/WChAxtWkiiOW10vR7AaP5WPyh9nBrTUeDCknCP8HEVg2Yj4v4n5aHpQAVTVQ8d8bWFLed0hAAo_3k7uHCj1HM27gF1uqv3_bHHA9c9m_fH1ep63L8Q

dialog in Japanese on top of photos and text in Japanese

Budou makes correct line breaks in Japanese. The first line says “Chatter Privacy” and the second line says “Policy.”

do

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d6e0fb21bb83cc0f86968f14f5714ceb2c8870f35d30dcebf96923bc7038ff1ccd110aea0fc58f8da1272ca34ff1bc3f2eed97fd275bf53da40ece88203da5b7

https://lh3.googleusercontent.com/5EZBwjROoA5MBrpwkxIzOOp6HSasji0g45byIROc7rOziSuve1hPkAoRwtSCG11BQmwoSpwfNwM9wQuNLXmtcSeXYV-pugop75GbsSJy1Pv2eayjQR0

dialog in Japanese on top of photos and text in Japanese

Don’t break words. The Japanese word for “policy” is split in half across the line break.

dont

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/159085534e72d95703b2293b706912b13500e11f25739b8d035f26980a678272e8efce67423c865442cbd0fe735da73c533593e933a42038b6815674862ccd82

https://lh3.googleusercontent.com/zgRec7Z9t7Kxs2fxUKe2604zYFAM38I2gEzpm6kNsOp_3e1BZXQngWck6iPREIoo0R2GYwjdKI6E2gtCIMOQXAfDpZNT8yZUm9_LULpwfzEAxidtyA

9 photos with text in Japanese

This page in Japanese uses a dense UI,small photos, and a text menu on the right side of the page.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f6ec7803c859c4ad448d50bd1afdb5af74f8f077d96304fb6aa4307fd326b38b05bcae2f67597683b99cdfa0bc141afe19a899fd024c02b7beb3b3ca9e5de935

https://lh3.googleusercontent.com/zVyfuwg8pl8uGXorg9te6J5fmn9eGBcaBC24EV4xAt4pR_O5uY8Bj4N-3Y5Oq17SYeWb9DsOUCKo4Gaf4bZLrJyYFjFdeRl_v9f2UtL3ez5Up2GlP1s

6 photos with Trending posts title at the top

The same car page in English uses medium-sized photos, no text, and a menu icon for more information.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d281c2409a4ace7942bd74559517439772f237c22f866e8fbb22d47dc2a1b0437efd4d822b32ac4445037a3b5c480731567fb4015edcdca72ec5be231acecdfc

https://lh3.googleusercontent.com/EigP05Ra3PUo30vDwbmlzcAvSpc8FMf-Rskm-2krDFcqpY4UTEPgox1iLbwJzJAOars4fJRpv9skJ1Q3Jq0RiIqeN2YKDBrn8N_V3F_F9xHlQBTcJw

contact form with name, address

Canadian and French address forms are formatted differently to conform with regional norms.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/3a7f738bcfde9d38487ffe035ca82cff84dcac7b8dbb1764ae1e8f8d933f1904e126be36b5c08772974ad44e8c08e4e2ba468f064ef31fd3dbe340ba2fc2d14e

https://lh3.googleusercontent.com/ttq1s7H521wkNAtkgCI7NQTyd34sYIJqfXyeUount8zdm9BapvCGTeKIr4Q02trFOlgckBXcOKjrim7tdAqszO060wOZpjUgZZn50NaBfTs000ftzOc

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/85327bb112d1e96a381b0e2e6dd8ef49a90a366a3dad92f6f27056994c470cc57e4374ece2a6e9ceb77b3a12a78a7ce0b89149356d3857f27c3c4e21127b7745

https://lh3.googleusercontent.com/JyAlIoZ7WIdN6N61L5CMHMWcMmKzO51edjGN1oiNHMRaXhlpZlpXEXPI8lXnhX8MLSD_WDvKQ0_W-veWXqk3iNZNSYWEuBZ5EvuiluCDWis8yLC0qNBG

{}

Localization is the process of adapting messages, imagery, brand voice, features, and products to achieve cultural, and geographic fit for a given audience.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/1ae18c59611edfaf9313a64b87ee8af6d2767ef3c58bd9a87f014dd1925b7a216c6c637901392f7def895d55bacbe6759b70b29408e8842f9bf40d8dd6bbffe4

https://lh3.googleusercontent.com/QKdr37niTZE4J3ukioizTPm7XON4mHVLNJXIr_K7mI_DM0UTwX6HE2gHwauV7QzPKHUIByDf3q1UsNUDldeNnJlwzhd-u4hXih6uCIoZLLIqhGhBMw

Principles and Techniques for Effective Localization

2021-08-30T09:00:00

localization-principles-techniques

Going beyond translation to create more inclusive experiences

Principles and Techniques for Effective Localization

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/10670050668c02a15305405869d10261ae9184c4b9943da19db1f77dfec09cbadff181927e3ee1b025e024736848d2c53950c779e44a033489d2f68c57607b44

https://lh3.googleusercontent.com/-WjjawJvR9AIODJEhrs_slzoG32Y_Ip0a0c_qe04DMIR2zS0UGQxrmY7DU0LH8--_G45NFBmIFEmAdGxbVC31KCl4Zw6h3Yz-L3pff45FVFM8rINVFw

Designing Text for the People Who Read It

/blog/designing-text-visual-acuity-research

Material Blog

Designing Text for the People Who Read It

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/61721ca9c7dba79a0edc8fa874afc4b83f0bfcb878fa513fb3841e8eb0e9a3c4abb0774c0699bbec1b6a4545b900bb207bea8be55168efd9be21965253107cfb

https://lh3.googleusercontent.com/5Kk4oIGKBCYRZ5FcDwnv2inn-RtHo94IaVk7FzGUU0e9BqGP2WTHXKhCY6NZ7V4x6hD24bFKFzWnMxl7hYllcEO2MdQhKt1JjfLOEw

/design/shape/about-shape.html

Shape

About shape

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/be2e7ff3a51d71054364b0e999cac188e75af3bfb612e88d176bf6119f91ce3847d3a5d348209e886c5c679fc651f03b34198691fed75542959fd7b163d8ea2d

https://lh3.googleusercontent.com/Dzr3GFdm_f_vCXiZX24gCY9Is1XW5d2WoCkdVsSKB_0EB8_5z3ij-mL4fnG2JIme0gJtIEzlkuFjQvehVJYu4-AoKtgcFPEgR6CdsZU

/design/communication/data-formats.html

Communication

Data formats

mio-example
