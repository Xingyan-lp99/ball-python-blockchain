# Unlocking component flexibility with slots in Figma

Source: https://m3.material.io/blog/material-3-slot-components-figma
Content endpoint: https://m3.material.io/page-data/Posts/5965893380472832.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/eb04247d28af59fe5402bd7bf137b2de663d2dfde67043d07231cfd8cdef507a370d984f0d8325e45c83c3fcbfd3f771822838fcc07c9d6bcd10f35174256cab

https://lh3.googleusercontent.com/XJQJJGSv7GsKJZZ0wDb0iamsHCUK6FHE1F76um3buCfn0NJGkqiDN4ygjiDUUSFQsFoFO1PrghEfYQfZ4doJNXco1gX8AN_IRgMvvoEUo0fukZmXWB8

Dillon McCallum

Visual Designer, Material Design

mio-example

<p>Material Design is excited to introduce <strong>Slot Components</strong>, a powerful technique that allows you to create flexible and dynamic layouts with ease in the Material 3 Figma Design Kit.</p>
<p>Slot components unlock local custom component nesting in Figma. With this added flexibility to make changes and edits to components, slot components remove the need to disconnect from the main Material Design Kit. Components can now remain linked to the main library to receive updates and improvements as you change them to suit your needs.</p>
<p>Slot components are a step toward supporting component flexibility that makers need by:</p>
<ul>
<li>Allowing teams to extend component possibilities while still inheriting future updates and fixes.</li>
<li>Designers no longer need to Detach components for unique variants.</li>
<li>Material components are no longer fixed to only preconfigured offerings. Designers can now add custom variations to them!</li>
<li>Material Design components are simpler and more powerful than ever.</li>
</ul>
<p>Adding slots to components enables them to better express the maker&rsquo;s needs. Slots gives designers the flexibility to create new component variations while still using the guidelines of Material&rsquo;s design system.</p>
<p>This aligns with how these container-like components are designed with how they are built&ndash;&ndash; crafting the design toolkit to mimic the component capabilities in code.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<h2>How to use slots</h2>
<p>Explore the Material Slot Component <a href="https://www.figma.com/community/file/1424088109026491617/slots-playground" target="_blank" rel="noopener">Playground file in the Figma Community</a>.</p>
<p>Some container oriented components (i.e. cards) now support Slots.</p>
<p>Each slot enabled component will have a unique instance for activating the slot.</p>
<p>Select the Slot property to change to the Slot placeholder content and reveal options related to the slot</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>The slot can then be swapped for a local instance of another component.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<h2>Prior to slots</h2>
<p>Prior to slots, the design kit offered a robust range of variations and possible component permutations for designs&ndash;&ndash; allowing different aspects to be manipulated or toggled on/off to ensure safe guide-rails and preserve component boundaries and design intent.</p>
<p>Behind the scenes this requires very complex library building to capture all possible iterations, exacerbated by newly introduced component features.</p>
<p>These complex components served as a great &ldquo;jumping off point&rdquo; for most users of the design kit. However for other use cases, subtle deviations (that would otherwise still adhere to guidelines) would require designers to detach from the master library and break these components to accomplish their goals. The result is designers lose their connection to the Material Design Kit library, component variations, state controls, and future library updates.</p>
<h2>Flexibility with slots</h2>
<p>Slots serve as an empty component placeholder that designers can swap for any kind of custom content like Material or local custom components.</p>
<p>Components like Cards, Sheets, Lists, Menus and Toolbars are containers that house other elements within such as buttons and strings of text. Introducing Slots to container components&nbsp; adds the flexibility for components to contain any kind of content rather than having the content fixed or baked into the component itself. This also brings closer alignment with how these components are built in code.</p>
<p>(<a href="https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma" target="_blank" rel="noopener">Guide to components in Figma</a>)</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>The <strong>slot component</strong> technique is a powerful method that can help you create flexible and dynamic layouts with ease. As the Material library grows, more components will offer slot functionality. It's a great addition to <a href="https://www.figma.com/community/file/1035203688168086460/material-3-design-kit" target="_blank" rel="noopener">Material's Figma Design Kit</a> and we encourage you to try it out today!</p>

Material default card component beside slot enabled card

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/adc660c9c052cd0b5dff55e0f39a8507ee1f37031e0cfc77679c370e9b840e4114ba27debca790214d622a031e2b888bed4ce6e81daa620ecfb682bf7635ca3a

https://lh3.googleusercontent.com/oq47vhxQrCvbMPNH9LpLs6DfR-J5wW1wL4u04Re--uv8kf2jMw0FR0uoICaQqPqsBX6hTvHDKrsn5wXrobE8Cv-lRYFh2t0ZE-X5FLVOZRb_huqXaIM

Card component showing figma layout choices to enable slot

Slot enabled components will provide a layout override

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6b847416ad963049c6f558e4bbd109ca62f8c06f2cf9628c7d3489842fdef13e229370b3e9ae50f162dae874afe0a98ba9d2134f498e31a13f5feec5b353d6ba

https://lh3.googleusercontent.com/hMrc5mbn8t_fzhVKuSiyzM7md0Jz3Dzq5vs-1mB5iiCFWNTUK1kotqjlnoTSrLbs4bI6HDZPbUYr6QdmR3v2PZt8E0t_Sfe5ZGPJqY-ILhDomrd_jLs

Slot component showing Figma instance swap functionality

Slot swap allows for quick replacement for local components

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/5b89819bf11bff6e8ab89759caeb6dd397d08702e195cdd9ba2bb4f6cdf298b610dce793ef128fa95c4e693cd658c7fa408e637cd25af23e81cdc91cb521c251

https://lh3.googleusercontent.com/J3Hi9r0ELFo6DKy00RoNQ4R_yp7QJW8Q_92wpLC0Fh7j492ub16ZBZ0n-R_i6uwlmsm_TbMzJlmoCxsraHrA7hx_BRJy22edBWAXoMeKOZnRBclpfw

Local component of grouped avatars replacing a leading slot position of a list item

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/63a2217840d5ee58f4616173be0e9156404890d689d284bb21e9c9ab7e32b8f362554e5c4a90da734f5820de67c59df25082afaa395d703b20f55f3081c4c14b

https://lh3.googleusercontent.com/Bh8f6ZE_Ijpuar1XcbbFawIfvZNWybPMpMQZI12HPA_cMQLZcPA_Gh3NtiJETt-Ev8PR9F8830migCgJzx0L5Va6BMbaayYX24g26v4gFh17Ehw9Qn8

abstract diagrammatic illustration

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6683ce727d3dd049d2e60ba34b52ca20fb73088a21b697d24814373470b5500ec9ad58f31e4a1130d7534c977a25a49f145da17090c4ad74d8e6957fc1ed003e

https://lh3.googleusercontent.com/ZEXG-W7U-laQVPWKv9dDO63A3X4_53Wye7OjxT287BY0D66dpxl7bsT3FX5MxkjYUIgWfVjJkBSqy9w7XX67qvtbAF8sgx1QWzTSe2dieKq4sOSodJg

slot,figma,update,design,material,components,workflow

{}

One less reason to “detach instance”

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/295e5257d0852e59f21aa6a931f952490a0692ca036bbdbac39e450ba34838d728f35a9613edffcccea8dcb4bd4f2fb88a50e178d85e61139902464cb473ab71

https://lh3.googleusercontent.com/uatn3lHge7xnOa0DO3IMBhicBOPtrou62WURmIC65Zd2ofHcXxSl5EGCkteb5GB68juHhkpm5fhWuX0q012SywZNbuqm1BhFW07dNtBmss1bxQjqq68

Unlocking component flexibility with slots in Figma

2024-11-04T13:00:00

material-3-slot-components-figma

One less reason to “detach instance”

Unlocking component flexibility with slots in Figma

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/f76a10ef20aa3042fc461583cb2a0ac1ce5df95cdd3478424b0e318c5d8ed57cf9492e0503c8f7a07cf19185a453e248c8b840fd2bacf8f608bf5f18e47a9271

https://lh3.googleusercontent.com/thChzTWq1-LKKAjRUXGxrTTahkLJxqAWrUeSBQdDjM3bGInZtXNffv4t81qGiRuWLyZ15Esjpso-EPYanAZ1seXIfrOnG4qyRtUT5u_5zAkmYL_qwQ

/blog/material-3-carousel-research-design

Material Blog

Reinventing the Carousel

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/47da200c393227f92314ec1902957b5c59e00177b03d8a0cc0001bd9149d55dc0781ded2a04705d2eb4564a19897d15633f0f696af869e52c13b9dd9fea0e1b2

https://lh3.googleusercontent.com/29VES8VMI2aMdi8A3pVXUoBAtHRCwwJta8G9Nn5nPRIYRVe88FIWFORh5mKiKIX98AiMSrj2eZ74yaJM4FbThzIWi2nzU-b9kC1EDfsaqKbDxh4aFQQy

/blog/google-io-2024

Material Design at I/O 2024

Material Blog

Material Design at I/O 2024

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/cd8c9e0ca5aa68ef80c0a31efa58c001aa94297e2d136d9cf8f3f3ed343d38c0acc83e523c982a5ca93688f2f31d9bb8b2ec0983afe492c5f279bdb486892112

https://lh3.googleusercontent.com/m5z1z1wKD9x1FNKc0WyO1vMQjH8jrxs3eSkealr2NW3JI-we22rhV787nJc7lbPrxWqzaoiS-JUsuTTztMUJ8t18AoTWmq2ZWVtia4inx_H-MoLqeg

/blog/tone-based-surface-color-m3

Material Blog

Introducing Tone-based Surfaces in Material 3

mio-example
