# Introducing Tone-based Surfaces in Material 3

Source: https://m3.material.io/blog/tone-based-surface-color-m3
Content endpoint: https://m3.material.io/page-data/Posts/5454212709351424.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/ea2d55abc15b27397602fd58395bf0c45b999a17e3fc5ed9521858d64c41645f5a223b188df0a7e17ccb4689bdbeaecee4658f09a299a72062c92d3cfcfc5974

https://lh3.googleusercontent.com/K0HbYtmqtU06VS_Af-ue7d7mAvhiInDwRRecfaGxKBRq3lKb1TZIBbIFvxVCgL5AK0rpBPR8thnnfOLLQA0ZWE_C0my-eWeMIwE1MNm1fHzKEkAR7oY

Christian Moser

Senior Interaction Designer, Material Design

mio-example

<p>The previous way makers could achieve tinted surfaces, which are a hallmark of the M3 design language, was to assign the color role &ldquo;surface&rdquo; to a component, and increase its elevation to achieve the desired tinting which was applied via an opacity layer.</p>
<p>&lt;mio-video index=0&gt;&lt;/mio-video&gt;</p>
<p>The update introduces dedicated surface color roles that are no longer tied to elevation. Makers will be able to choose the right surface roles based on the containment needs of their products, and now have more layout flexibility for larger screens.</p>
<p>&lt;mio-video index=1&gt;&lt;/mio-video&gt;</p>
<p>The new <strong>surface container roles</strong> and tokens include five colors.</p>
<p>&ldquo;Surface container&rdquo; is the recommended default color role for a contained area against the &ldquo;surface&rdquo; color role. It provides good contrast and can be flexibly combined with all other surface container roles ranging from &ldquo;surface container lowest&rdquo; with the lowest emphasis against the &ldquo;surface&rdquo; role,&nbsp; to &ldquo;surface container highest&rdquo; with the highest emphasis against the &ldquo;surface&rdquo; role.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<h2>Migrating to the new surface color roles</h2>
<p>All Material Components will automatically update to use the new surface container color roles. For makers using the previous opacity-based surface model for custom color mappings, we recommend remapping these to the new roles.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<ul>
<li>Surface Container Lowest is a new role</li>
<li>Surface at elevation +1 becomes Surface Container Low</li>
<li>Surface at elevation +2 becomes Surface Container</li>
<li>Surface at elevation +3 becomes Surface Container High</li>
<li>Surface at elevation +4 and +5 are being deprecated, it is recommended to use Surface Container Highest by default as a replacement. As an alternative Surface Container High, or Surface Dim can be used depending on the specific use case.</li>
<li>Surface Variant becomes Surface Container Highest</li>
</ul>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>Both methods will co-exist for an extended transition period, giving makers time to migrate to the new model.</p>
<p>This update also changes:</p>
<ul>
<li>The default light theme surface role from tone 99 to tone 98</li>
<li>The chroma for the neutral palette is increased from 4 to 6</li>
<li>Surface roles in dark theme are slightly darkened</li>
</ul>
<p>To learn more about applying the new color roles in your products, visit the <a href="https://m3.material.io/styles/color/the-color-system" target="_blank" rel="noopener">color system guidance</a>.</p>

two color palettes

New color roles in light and dark theme

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/497ee0e0001c75081a54f9f813433f0ec69a2e6257ab63002606e789e8e94ab749afa944277e57fff6ceba25909dad3f260db8fac363d60663a13e4f2a03d951

https://lh3.googleusercontent.com/Q5Jcvl4yPN_vcdif9enFF4waHTi7OCeL4pxk4YwV3C6pBQq_DlOdeSJG337YIIOCHgx-Ixs_aAspS44pS6-6LVNW1NGqSfIrMX8Zra9QTMAPsTetuQno

diagram showing how color roles have been remapped

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/0784d7d81c63e7d691908d58d90f393bc8863259efbc63630a8d54dd6a0c99d20afd492f9bd56738e9e1d5d6c003de314d570aee735abaa910d0dd8ed018ab34

https://lh3.googleusercontent.com/hV_-3MUEyg3e1lK09oWMcJidImOYRnJ_n81Z9cJUy5xSkIerF8-006gDKHGAt9bn00KV_L_yR7AC4XO21C_kax6CSve7xzGKkCCUpNprkgmGjXJL6A

example UI using new color roles

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/cee658825acb1764bf899ce23209c9e8ddb3c5fd2a173558b6e7826f05713e438b9174a47ce7fe182ad3efc9b5ec2e7a5204f182dc13164cc32993a5c93062c0

https://lh3.googleusercontent.com/cr46Jts0LQ9m4w5atTsCnxQ1rQib3TD7WspzgBZDW40bwCdyU4X0duBu-JV2trExfMftuVNQrrhxiayCQyfaocvLQUhk4458i0wiNt-qmkUX9t6rS64

Pre-update: A tinted overlay communicated the elevation of a component surface

surface-blog-sequence-old.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/1e0f17dfb71849ec88febb9d60f7d97b4ca49dad62550843be95a097dd21cbfab5c8a6f57373db166a1047783626736efe4a6ae7c08da6bac67a2e015e9751e4.mov

surface-blog-sequence-new.mov

https://storage.googleapis.com/material-io-design/m2/assets/downloads/4ab6ab93782b98d929cd5692a479693dcf7e4c49221db5c6c7c4aaa39ef002702ffce711f630d37482cead19797a30b3159960834eb9186567bc70e73f61c1ad.mov

three skeleton UIs on a pink background

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/c470422b13ff8496171ddc49968be8f1ca3b18a6a41508b9fd2becf6acc6f57483fb52f7e78db1a5356af289ea8894c2ba45b16176d55465354eea4d70f69f32

https://lh3.googleusercontent.com/JsPGxLo5hiZrvqOpxpQWrKjOPOwBpJN-Rz8yWdmE-RBnFZX4VmZwnopcsoKW-9iRlh9_pdkcAky1XMs3tbAcoxpDsZCJNejcWgCK1xIHjNSwzy6B4GA

color design update

{}

Tone-based surface color roles offer more flexibility for large screens and rich color features in Material 3.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/5f548d9680b3057278785f4897fb831f1436cfa1ea842ecea186258680c10693c79913d081fdd518589c4114c1f1c5ec37d9129dc0e5813b3d704707288875e6

https://lh3.googleusercontent.com/2E3Itwa633zeNZmWDILIO1YiSoJJiMSXhh2AKsIuENUydJfNltj4-E7xAVoe7F9_zODpnhIjHn7rYr61du8jYrKEMm0Twa-MrRnYpzqmNsHi3gQ-4w

Learn About Tone-based Surfaces in Material 3

2023-03-23T13:00:00

tone-based-surface-color-m3

New surface color roles offer more flexibility for large screens and rich color features

Introducing Tone-based Surfaces in Material 3

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/318785e7385b8e7a3922a39bb37b52bb2520ef6c4dbe4967ef952c12e53375193f039ae07c906e1fedc135314e38c5b14c0f340a48a53764727e401b29836eaa

https://lh3.googleusercontent.com/EFglKz-sfEB8uDeN-bzUFFxWVAlgpIYiiDJejQY1QLtZaLCZJhg9BtXJzz63s4_pbw9gcuywKWYLmucDgxGo1ABAw6UReRiWCQneUteHStmGTYKwHRo

https://m3.material.io/styles/color/the-color-system/key-colors-tones

M3 Color system

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/431dfac6c5ce89665d484592b44c8066d4b009ee23e07ac7f8e6295313ad9ece46f3b390755cd81685be2f44f2ea784fbe82eefdf5fdd401d8430fc8a4b543cf

https://lh3.googleusercontent.com/hwCFDEfbHlMM92sX1YWje3r5Df9KOiUg-xrF9cZf4YFka-4O83DEv1wYT38uoV509-Oet5dYl0jTXsriDvfN5sTjlLlLbvIsH2vhJNgaZXg3ZCXcwA

/blog/material-3-figma-design-kit

Introducing the M3 design kit for Figma

Material Blog

Introducing the M3 design kit for Figma

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/65eb24e15db793a9979b3362479941e134cf7e84a8c02f1540c76285b9f5056fa73ee4c8509539daaec7f04f45e7c679939207093d563da44070be712b24ba3f

https://lh3.googleusercontent.com/hDfP5g5Ut41VqyixQKIcr13kE1eayotW7oFOcdXCaZNvtZqC30XZAuIIq2yP_bFx6eBf1sPsFzTEOZ_ij5yWLhKrwhnO3KLzEa8zEgkPUZSPV2lJzg

/blog/material-3-compose-stable

Material Design 3 for Compose is now stable

Material Blog

Material Design 3 for Compose is now stable

mio-example
