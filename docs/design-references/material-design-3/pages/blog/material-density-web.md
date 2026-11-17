# Using Material Density on the Web

Source: https://m3.material.io/blog/material-density-web
Content endpoint: https://m3.material.io/page-data/Posts/6660569227329536.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/f2456dbf9834c81e287286c61c151032e73d9892138f943a9d588cf02e8f125576fd31508dadb527d40cc5f56d4d91212c6312793ee4fc95a4180b63813b3971

https://lh3.googleusercontent.com/J3SDcKnU4gCPZoeNlzYVHXLiNygU7BAX1fcDSJpaiXRsXcVoU8xMRUpvmf_ic0xZvWMYKyje8YNcrmIq267paboAGBRyYgOafWS1

Una Kravets

Developer Advocate

mio-example

```
$height: $mdc-button-height + $mdc-density-interval * $density-scale
/// @example 36px + 4px * (-3) => 24px
```

```
npm install @material/button
```

```
<button class=”mdc-button”>
  <div class=”mdc-button__ripple”></div>
  <span class=”mdc-button__label”>Button</span>
</button>
```

```
@import “@material/button/mdc-button”;
@import “@material/button/mixins”;
.my-button {
  // This is where you set your density value
  @include mdc-button-density(-3);
}
```

<p>A common issue for any front-end developer is layout and spacing. How dense should your user interface be? Can a design system really account for all the different layouts in a product? Material is here to help.</p>
<p>The latest update to our density guidelines includes <a href="https://material.io/design/layout/applying-density.html">a new systematic approach to applying density</a> and spacing in digital products. Now, you can change the spacing of your product to suit layouts for different use cases, such as data-heavy layouts vs. a layout with a single call-to-action.</p>
<blockquote><strong>Just as you use Material Theming to systematically apply color, typography, and shape to your UI, now you can systematically apply density.</strong></blockquote>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>Global density changes affect the spacing between all elements at a macro level. However, you can also apply bespoke density values to any individual component.</p>
<p>Material Design&rsquo;s density scale includes three levels of density: <strong>default</strong>, <strong>comfortable</strong>, and <strong>compact</strong>.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<h2>The Rules of Applying Density</h2>
<p>Compact density can be great in data-rich applications that need to display a lot of information in a small amount of space. For example, data tables or long forms may benefit from an increase in density. This would allow more information to be seen on the page, giving the user important relational context at any given time.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>However, an increased density display may be less useful in layouts that involve focused tasks or small user inputs. For example, date pickers need ample space for the user to be able to accurately make a selection. High density spacing can also make alerts and messages difficult to notice and read.</p>
<p>An increase in density can also decrease the accessibility of your UI in some cases, so make sure you&rsquo;re applying density in places where user feedback is not affected. This dense calendar UI is an example of how increasing density could make it harder to use an application.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>It&rsquo;s important to keep accessibility in mind when you&rsquo;re applying density to your UI. <strong>No matter the density, all touch targets should be at least `48px` in size.</strong></p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p>For the buttons in dense layouts, we&rsquo;ve applied external padding so that even when they appear smaller and condensed, they still have an accessible touch target size.</p>
<p>It&rsquo;s important to maintain a good design equilibrium in dense layouts, so when increasing component density you should also <em>decrease</em> your layout or grid density. This means that the more dense your components become, the larger your margins and gutter widths should be. This helps keep your UI legible.</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<h2>Using Density on the Web</h2>
<p><strong>The Density Scale</strong></p>
<p>Density is defined by a scale starting at 0 for default density. The scale moves to negative numbers (-1, -2, -3) as the space between components decreases, resulting in a higher density layout. Each increment also decreases the height of a component by 4px. But it does not affect the horizontal spacing within the component. For example, in an icon button, increasing the density will not make the icon appear closer to the text.</p>
<p>The height or size of a component is calculated with the following formula:</p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p><strong>Let&rsquo;s See Some Code</strong></p>
<p>When you update to the latest version of MDC (4.0.0 or greater), density is included as mixins within the components. You can apply a density of `-3` (the most dense option) to a button by applying the following code:</p>
<p>In your terminal, install an MDC button via :</p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p>In your HTML, Add the following button markup:</p>
<p>&lt;mio-code-snippet index=2&gt;&lt;/mio-code-snippet&gt;</p>
<p><em>Note: this markup is different than the previous version of MDC (3.0.0)</em></p>
<p>In your Sass file, Import the button mixins and apply the density as a mixin to your custom button:</p>
<p>&lt;mio-code-snippet index=3&gt;&lt;/mio-code-snippet&gt;</p>
<p>&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p>The following components currently provide density Sass mixins:</p>
<ul>
<li><a href="https://material.io/components/web/catalog/buttons/#sass-mixins">Button</a></li>
<li><a href="https://material.io/components/web/catalog/input-controls/checkboxes/#sass-mixins">Checkbox</a></li>
<li><a href="https://material.io/components/web/catalog/chips/#sass-mixins">Chip</a></li>
<li><a href="https://material.io/components/web/catalog/data-tables/#sass-mixins">Data Table</a></li>
<li><a href="https://material.io/components/web/catalog/buttons/icon-buttons/#sass-mixins">Icon Button</a></li>
<li><a href="https://material.io/components/web/catalog/lists/#sass-mixins">List</a></li>
<li><a href="https://material.io/components/web/catalog/input-controls/radio-buttons/#sass-mixins">Radio</a></li>
<li><a href="https://material.io/components/web/catalog/input-controls/switches/#sass-mixins">Switch</a></li>
<li><a href="https://material.io/components/web/catalog/tabs/tab-bar/#sass-mixins">Tab Bar</a></li>
<li><a href="https://material.io/components/web/catalog/input-controls/text-field/#sass-mixins">Text Field</a></li>
</ul>
<p>We recommend customizing density using the provided density mixins rather than arbitrarily applying component height.</p>
<p>That&rsquo;s pretty much it! You can check out the <a href="https://material.io/design/layout/applying-density.html">updated design guidance</a> for more details, but applying the density scale is a breeze with the new MDC 4.0. If you added density to your application, reach out to us on Twitter <a href="https://twitter.com/materialdesign"><span style="text-decoration: underline;">@MaterialDesign</span></a>. We&rsquo;d love to see it.</p>

Various Material themes created by adjusting color, shape, and typography.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e71620c02f06e150abe3b274b0c641ede706e0b2504b93f6fa847e5dbe90883a67be028d0ac30dd0c1d57c647976c860cf265e7d257288ccac655ed43a245bf9

https://lh3.googleusercontent.com/F8hhbo6k-xtQobrVXyVPq5sMtq55LdYNK-vF1FuoiHNAskmChocIq25FY_5zwXKhEfBTv9v1FDSo9z9ajBT4C_w5waSj0WLtBO-kQg

A demo of Material’s density scale in action, created by engineer Abhinay Omkar.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/0a5bf4cfe57725a7b7ae433e57b40c8a60d6a753285b5ef715e3aca0b90d28f61d96afa90ef9b20f8cb95fd698609025ae46a1814f89b21300272a7302179f49

https://lh3.googleusercontent.com/EVnaNboEUFzvG7vAgiB1ms8RVVq_eoEnbWeIL-qANCNshmQPlYnOz0MZ83iJUyyKy1AmELd2DdsKQJXHv1lJbBsuRjUMMq7OnkJgTw

List items and text fields shown in default, comfortable, and compact densities

https://material.io/design/layout/applying-density.html#usage

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/a331b2fbf8f137e17de0d5f35140ee05f00997d853a03b601ab2fe8d095c048435e646b9ff3e4565ad796aa78249726aea7334e8d6cdd8feb04f8a2fd55b6bbb

https://lh3.googleusercontent.com/SvqXdrALyOlRHQnYC4HtXjAjlgKg8wmlyWI7_IoSGhJtWYnA7_stDRe2RcAHGdLmuZ44gxQomC3Ou892hRxnJWIHOdoh9dO98OBI

Date picker displaying September and October, with highlighted dates

An example of where not to use a higher density display. The increased density makes it more difficult for users to interact with the dates in this calendar.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6ebb708168ec7ab496c16229f888f6464cf21fb1144144f0688be9d039e1d128252de57b9c8cd907d99536adfdc873d4be45fd81956076b6f17065e3b99b86f2

https://lh3.googleusercontent.com/6LmJ81p_ndW4jg3xhQX71w38pETsqLzveFlWS-FUlft6y9UH_VfBogRFc1L7VfUe7i4pVfsUDv7uxsl7LM9XwCmmNm6jzFnxDvfX8g

Even though density can visually decrease, it’s important for touch targets to remain at least 48px in size.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/3aa8f66699964ad9aeb312c168ac364efab8dc564da14c8bef22117d4f7e2d40e67bf09b3c9eae2ca520019bc1374aa9e6fde34931298e9abb6505c387565959

https://lh3.googleusercontent.com/Vi-Xzj_EFwXoGr5AXM_EAlH3fD1mRpUSHLJx-Q_46M_jRBNtFmX1U3kP0D8E7bvmlZ8VdPbi4sjBSK7AqcAVq9_bSZb0UWMXrefZYg

Dense app overlaid with columns illustrating its wider horizontal spacing

Increase horizontal spacing as you decrease vertical spacing.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/15d9bfd5de80181e078721932dba76e7d52b1e176bf8ba5f95933df982711dda058906080f0516f54799c911f9d01ae86ba5544a43a8e0f39cc1a8765c19c659

https://lh3.googleusercontent.com/j516C0DxGclTIpdxPWDWVXMKdOggEuO0Bd4_ZRuCFUW8XTkc-EA6L1O0KgxA8fOBddURVPNR2iZnHytWCnCgzKcPSZR-vNtuFMTPi6M

Various density values change the vertical spacing in the button component.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/cd9119587245c852b3c0cb7dbe8ab02f3b04b3f8a648d9e94a8d3364f254554f2aeb242aaa4e453f014a601a9f01f2ee3b031332e3868419b753e8207cdf515e

https://lh3.googleusercontent.com/HxVn_7TPzEqlIktSr3gXhkAt6gmQxjZ251Qyr9MzV6PtEffngRdgyaNztV8_2UunNabj6m6cQ2eN-HunK7-PaiJ0i4W0GXe07jTrUA

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/86dedc41c33abb8c3fe08f334f7b6cbf8f4685068e844131e717337311f5b3acf539d0eda2435a2066d8f2bc4d67a0ae98a980cb89b5e7efbafcf8693ec75d82

https://lh3.googleusercontent.com/qGEdgWMxq2N_sW_BueogGolL8ogI1OH-bGMzhZNeLW7eWTMFgIuECRquT-to3lVaPz2xB0Of1gkclBGRM_crDbuQksdm8JxZ5fqN

Density, How-to

 

{}

A hands-on guide to applying default, comfortable, and compact density to your application

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/4618e705c0d29f0ea3f869ffc11ce71b1f40c6b93ac98333315c4406854738a4e6fde6ca3fa6ba72294a756869316572c3d47f8955443f70a0b2ab10d5d31582

https://lh3.googleusercontent.com/IJcO4jYFGqfyqJyZuVg3R4VWVqXHCgQnA9Xqi-5lk2OYaGJc4DKBx7U3HkCuyF77W6zSuGvKXrpuUZ7AITF81dzbqalNlzkX8KaEQFA

Use Material Density on the Web

2020-01-16T13:00:00

material-density-web

A hands-on guide to applying default, comfortable, and compact density to your application

Using Material Density on the Web

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/c6ab36f153959e497a2a31d1335c5d732dc082acff79ced7c248a545e60e1d6cef9d89e5cf63ec7bd0b873255f54aae040d63c4d157d4bc7a2e9e11d4d3f1261

https://lh3.googleusercontent.com/cV1zATkGghablr-00xFY45NQLUBScMtq0zC5DcMQu6lajMKyQsUKlwfa2qmaF8IU2PXPilLD-1Rk-3O6mEmaxJ9uQp_NOgEssprWAn8

/design/layout/applying-density.html

Layout

Density

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/7bbd8dbc40e9bb70ada1a87ec1d452185fa1bd23acf217dfa51f2b67d3e72a68eb03d290d7e9597fd4b2df021c1576b89b9fb505ec454d2b9c9392a50b683326

https://lh3.googleusercontent.com/1T6DD1rCMym64PMEPWDZkXntz8DRWfB7ac7RWS2k_nH1goLXbSZLkQbYBcj2zk3hXyUI9NLkuE-bINnvvb6-STbawnxnzVlsd4mx

/blog/design-material-theme-type

Material Blog

Designing a Material Theme: Typography

mio-example
