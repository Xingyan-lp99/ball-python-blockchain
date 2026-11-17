# Looking for What’s Missing

Source: https://m3.material.io/blog/asset-people-3
Content endpoint: https://m3.material.io/page-data/Posts/6427919005777920.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/21db23563995e641781f444ddd094e5154485dddb3c09f128a695db6fb24de1b4345c63c5313ed82bc3790a3d0fa9c6c752ba46c83f818a39a940cf2b3a512f5

https://lh3.googleusercontent.com/iH5mSTXtDMA3gH_rJyr6UiHkYvsrKnEFkacVljhxePXwUUjZg9D79sazDXKNVW0rGqQ3EpCV5P9FStdE9usTzywImtCa6flGvr_48woZync_Vr-BWnk

Euphrates Dahout

Material Systems Design Lead

mio-example

<p>When I visit the workshops of friends who are makers and builders, their project areas are surrounded by the tools and supplies they need to get their work done. Hammers, wrenches, and pliers are organized on a pegboard wall or in drawers ready for their moment to drive nails, tighten bolts, and bend wires. Like books in a library, the tools are cataloged and labeled not just for display, but for accessible and unambiguous use. If the tools are misplaced or impossible to find, then projects take longer to make and the experience is fraught with frustration.</p>
<p>The needs of physical-object makers are not wildly different from the needs of digital makers, like those who are building products with Material. Material is a collection of stuff to build things with. If that stuff isn&rsquo;t set up within easy reach from the designer&rsquo;s project space, then things are a lot harder and more frustrating to make.</p>
<p>Our team of designers discovered this for themselves in the process of illustrating different interface scenarios throughout our <a href="https://m3.material.io/">Material 3 guidelines</a>. To help create thousands of images, I had already put together a library of backgrounds, device frames, annotation labels, and touch targets for the team to use as a way to manage consistency across guidelines. However, the designers were still finding themselves improvising on images, names, messages, media, and regional content. They had to insert what they knew from the same few parts of the world because it was much easier and faster than to look through a detached document of vetted content that wasn&rsquo;t organized into the context of their workflow.</p>
<p>The realistic names and backstories that make up <a href="https://material.io/blog/asset-people-1">the collection of new profiles</a> were missing from the easy-to-reach toolkit in the designer&rsquo;s digital workshop. I needed to figure out a way to push the boundaries of Figma, the design software that our team uses, to deliver this content.</p>
<p>In my experience in the field of production design, these kinds of challenges are not rare. It&rsquo;s part of the fun. I play keyboard hot keys like a piano, zipping through complex design software looking for the most clever ways to solve complex technical design problems. It&rsquo;s a niche arena where I get to play with both the technical and the visual to make beautiful things robust, responsive, and alive.</p>
<h2>How to manage content with a design tool</h2>
<p>Figma is a design tool that is set up to serve a visual-to-code process, but not a tool set up for content management. Since I was already using Figma&rsquo;s library feature for the rest of the asset creation workflow, it was clear that was going to be the best place to insert this type of raw content&mdash;I just had to figure out how.</p>
<p><strong>Libraries</strong> in Figma are sets of <strong>components</strong> and styles that are easily searchable. Components are elements connected to a main version that can be duplicated. Edits are made to the main version to then be dispersed to every connected duplicate, which is called an <strong>instance</strong>.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>Including the profiles in a Figma library was an interesting puzzle to solve because it wasn&rsquo;t only a matter of <a href="https://material.io/blog/asset-people-2">supplying licensed images to designers</a>, I also needed to attach text that was tied to specific people, relationships, and scenarios independent from design elements.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>I began by organizing the elements for the <a href="https://material.io/blog/asset-people-1">three profiles</a> to observe patterns and outliers. All three had social circles, news articles, and audio media, but only Lee&rsquo;s profile had a map showing live music venues while Sam&rsquo;s profile included movie posters.</p>
<p>Then I took care of the features that Figma already intuitively supports by following these few steps:</p>
<p>1. Organize component <strong>variants</strong> (different expressions of one component) into categories. Design the categories to be descriptive and straightforward. Our library has a component called Social Circle, for example, which includes avatars for everyone the main person interacts with.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>2. Use component <strong>overrides</strong> to bake in any available options, such as the name and relationship of the chosen social avatar. This will make something like a chat UI much easier to put together. Knowing the relationship between the interacting avatars will also inform the content and context of the scenario.</p>
<p>3. Group each collection of categories by profile so that they can be expanded or collapsed depending on who the designer chooses to use.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>4. Color code the backgrounds of each asset person&rsquo;s components as a supportive visual shorthand.</p>
<p>5. Provide any useful metadata to the components which will appear as hover-activated tooltips. The metadata can hold suggested uses as well as world-building context. For our Music components, which contain the licensed images of mock album covers, the tooltip suggests placing them in search results, media players, lists, and messages. It also includes a note about what kind of music the person prefers, like Sam listens to gentle classical and ambient music.</p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p>While metadata is helpful for context, a designer isn&rsquo;t able to select, copy, and paste it. I wasn&rsquo;t sure at first how I was going to provide easy access to the emails between siblings, message updates from a dog sitter, the tracklist for an album, or news headlines and articles tied to specific photographs.</p>
<p>My solution was to co-opt property overrides to allow the content to appear temporarily within the design space:</p>
<p>6. Provide raw text through property override toggles in the component variant which will place the text temporarily in the file so it can be copied and pasted into the design. Then the toggle can be turned off. This will keep designers in their workspace and not looking for a separate source document. Official edits to the text can still be made to the original component and it will disperse throughout all live instances.</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p>7.&nbsp;Not everything will have extra raw content, so indicate which ones do to increase the ease of discoverability. A designer making an email interface will benefit from knowing who in the social circle has that kind of content available. I chose to indicate them with an asterisk (*) in the variant list and provided a note about the asterisk in the metadata tooltip.</p>
<p>&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">8.&nbsp;</span>Add any additional contextual information to the property panel. This is ideal for content that is important to know, but doesn&rsquo;t need to be copied and pasted, like someone&rsquo;s pronouns or how many episodes a podcast has.</p>
<p>&lt;mio-image index=7&gt;&lt;/mio-image&gt;</p>
<p>The results are three different worlds organized into a concise, robust, customizable, and instructive group of components representing hundreds of unique pieces of content. Being concise is fundamental to usability. No one needs to use their time looking for a needle in a haystack when the needle can easily be threaded with licensed images, corresponding text, and all the metadata needed for designers to begin sewing together thoughtful and consistent designs.</p>
<p>&lt;mio-image index=8&gt;&lt;/mio-image&gt;</p>

An element converted into a component demonstrating how a change will automatically appear in connected instances in any file that has placed them from a shared library.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/29f1cfeb0c970481db9db08836f47665bb0c919c950ad6d2165ae5b3d18118489aa5266ec35672452f10d600ce39a93ce1a77c17f99a96597be4cff754d9c227

https://lh3.googleusercontent.com/TkLTpTfrC1oGt8ztuzqntR_Ah9PzbsaaKFLvWyCDhfpEeS6MoERJj7rPb5j8kU7Hk1dkQ_-FDgTa3xe2qmsREsuQJVbnXlnjo2dWAr6ckKWLEHtzaFY

Part of the analysis of various elements that make up Lee’s profile

Part of the analysis of various elements that make up Lee’s profile

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/4f288e58282ffc7f23169a627fdb3fc71cfa16e1277128ed2b04aedb97dc5d534ff671e412d07b4f007c1e08490dc69f3e58ac11764c2dabb644721827a445f6

https://lh3.googleusercontent.com/HzZlBq_B2qXkauxlVzKMkhkz0xhslZz1F1xJ8QKFjhQVQ3ReHpOiP3dx46NwMM8sbCuEwW5IglwlRQrNP6l4qZYSajG9Zz081OxGgwj32boMbdr9yXE

This social circle component contains nine image options with corresponding names, message text, relationship context, and other metadata.

This social circle component contains nine image options with corresponding names, message text, relationship context, and other metadata.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/4fabaeba86fc86f8918d2de2332438d4398ee9496c03c8534dc8527f5034115573fbbce8dffa8b06a6080e2babbaa96a4fa75e86e29f91ed3284267236784116

https://lh3.googleusercontent.com/oURaCiRR2WCpo4HdspLExtKEVDFskK2Cxr2V5X0Yza-qvGE5AgWFWqa-UIDUDC7WJJ_HJtqy8BDf08ZaHLdkDqb34c_uUUm7NKoZyu0PY3ihQC1MccQ

Fully expanded library on the left and collapsed view on the right

Fully expanded library on the left and collapsed view on the right

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/207921e5bab7abd1651598b7ef0b55e12867f3786f1c2fa9cb2d56660f0ff1fb17dc66276d0f2298266b548eb6a41709e1b3a5f320fa4f6f034dd386aece5a8c

https://lh3.googleusercontent.com/62HUWsfVrBUFhvlhF_Np5iFg4CphQH728LbBoeYzevhJiPlva2z18udNBELhL2-gZQoYF_EiiiiroWMpKPOSclAyFOJ064dcLTcjx-HumcfWiYZnTPda

A tooltip showing metadata suggesting best uses for Ping’s media type

A tooltip showing metadata suggesting best uses for Ping’s media type

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/96fa1a656b836bb31e006b637757bf0e08e093d1181cc6a22548e4f1ef309bfa6d4f91ebabcfeee1741b3cfe0442c8f27ecec40c51c25e23658b2287335ff30a

https://lh3.googleusercontent.com/G2l58u1u1cfvNSHTzqe98VR8YK4FGz7HbBg2TliCulJszx0UUhhLyaoPtFKZ1aNd6kpSY7tHDMmUOMmzy2g8_bEFk5Wr5cWEgpTqVrAhxmU-lfp-Ew

The extra content toggle selected showing raw selectable text to accompany an album cover.

The extra content toggle selected showing raw selectable text to accompany an album cover

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/377fb862e5fd4e7dd291b911e44f94238b3510ed790458599072c6c9de8fd591d997e76db711851c3c5071e6bf504908e8c5d8efa4e3d38f94c4f3d71d7355c6

https://lh3.googleusercontent.com/jyf-oq06TuWVkm-n1PRwhNa6RSUznxeZRuk-kgHkeRYP62mK_LQRSq4RH3w_EYG0Z2-5kcwBoVtP5DNRDBaZgEah-9Cj5P8z7LU_ltET9kl58A-Arg

Lee’s social circle variant with asterisk selected to indicate there is message text attached

Lee’s social circle variant with asterisk selected to indicate there is message text attached

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/c50d56a4f6e06e76aa657f2361bd2a8e65138a1bf29c7e95e169cd86902a98e553758231ec280993eb7c90239a52b30a0625c4c8f9aad2f9d147ebf75bc5ee3d

https://lh3.googleusercontent.com/tvRj92HDuffcPNpa6RHaqCO60xyqkadnEpLF1E5L-VWJUPNhEnl5fKUdg7MqD7vp8huQXKf9h5fK86GSDlFmuptyItcquajfAZw8BmHAi2TVzjl9pZw

Podcast with ten episodes selected in the variant list supported with contextual information

Podcast with ten episodes selected in the variant list supported with contextual information

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/321b5d43f142468bc3c34e172fe4c4c998f5836456684f8159616bd11f2599918cdeb43c52507acfbc78400ac7f4c4770b26c12124bb49d43fd5a05e0eebe405

https://lh3.googleusercontent.com/mLntQcoDcQ_tK6RPSdKOeJXBW7XiRl65AHPGABBUioPBu2xIS5YG826GTKrWEoFURcm1PyT5JsQ6ZOW2Km8MOWQvHsGqrs4O5UxtuiDdDfMtNgZUxw

An overview of the final library containing 28 components that represent 218 unique pieces of visual and written content

An overview of the final library containing 28 components that represent 218 unique pieces of visual and written content

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f4da94b7dcb424d27eb7246d96b303a0ef25f6a7cd183bc4f79230103a13568297977126d43bd3c20a89f9fb044e59e7b29a42a80cc8d6c977bf5914a841207c

https://lh3.googleusercontent.com/zRulxput0Bv3Xfrfm8oVf21BXkylZtKVZ7sO36GPFsPpjf5uRUMD9Ch7bom-x9wsRCRaJphD6BUrswLH6F1cmW8KEpen_ZO7Lwz66VrCnELQ4b4XLw

Art by David Allin Reese

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/82865c02a86ca5fef3e0dab73be0ec50861ccc343d0278d3e6f827c44ebcb37d6d015ca1f7c85dcdd81dd9127a0eaa61cf94f8516ca99a7073960dc6fe9ae55c

https://lh3.googleusercontent.com/xuAQngD7mW3Ay_UFZEMhnqlx52Jn0J6whGNAWG7j_fNp1-NyI10G2ObYzSe3W3rJOjXpYxwhneuCLNryBty_WTIXuGZAaxkCGc3dbiO66O-0VhPgMw

 

{}

A guide to including world-building narratives in a designer’s toolkit

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/33c3cd7bd893ca67b5a6bd675844828099760195a853e9ff2602e4885eb16d26eb01e92cbf2cf9a82222b64b469e50e097a2b6e2edd7a558041480dafedd1cbf

https://lh3.googleusercontent.com/ASy5LGgqD5j3vdbsEZZiFfJtGphEYKa4bBonx3MuBTcfnhe3GsqmNrJmp36-ZKwCcJVBpxdBJh21_je5MrMJl9mDERFbMY1HPVhk8dDMlCWe1lAzxEI

Looking for What’s Missing

2022-03-31T12:00:00

asset-people-3

A guide to including world-building narratives in a designer’s toolkit

Looking for What’s Missing

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/f5dfcbc0e58d329536f35f550d3045ce74693de1248f1bba61be0cb8f36524ae6d740a457562f2ec442c56cfedde81db7e1829385e5e04bc65ad33b5fac985cc

https://lh3.googleusercontent.com/Bi7oDPu4sAThijGH18IKGlSfRWvrjOfBoTVTNGTf0w_wSbzVvwTyzAcmOgSZpObYxxXYgtC1yhT5G2NTu7GMyZqzUSS1BIgxyF0b8R9miM0Z3uxfUMY

/blog/asset-people-1

Replacing “Users” with People

Material Blog

Replacing “Users” with People

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/fbddf252bcf6a5eedc2ca62849909de0242a1431d3ae1560f176ba0a436d642b2603d0076ffaf7a8fe1886a7d3541b1a4788f42e8ba36aa040a6c682f715c4c8

https://lh3.googleusercontent.com/9HSqMUCp664tcc5NQRRn8vbR73AoZ7uU2dh3YeqvulDD1QWWWy7Srzb6struVUthZvINchZ_JtVvjk1vWmBUfckIABy9b-uf3vZFHGs9u9d_49g0iCg

/blog/asset-people-2

From Placeholders to Genuine Avatars

Material Blog

From Placeholders to Genuine Avatars

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/7020836e335f8d40760df71d092d5bd5f244eaf61766f2fe300e4b7d0c0319d8c7864be56c88d2386552675ea0d580d4570954e529e236565601063978629408

https://lh3.googleusercontent.com/yXkkZBCAfbdufNoHIYc5l0AZdQIe72WVopmhlkIkIkMHxIaBD4qK2vR_tUbaiU_wxMPNvYHsSTBApY18HGNkHGqQiIdh_bnLqSe058sv8aJZlA4raH8

/blog/inclusive-imagery-at-google

Adjusting the Focus

Material Blog

Adjusting the Focus

mio-example
