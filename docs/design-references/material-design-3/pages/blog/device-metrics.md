# How to Find Device Metrics for Any Screen

Source: https://m3.material.io/blog/device-metrics
Content endpoint: https://m3.material.io/page-data/Posts/6017960135884800.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/114b4e6d76018c7e7e36de47f8158a7d71794d04f1a575e31408803c59ba962ac3b15579c1534fce4b47bcccb7fb81f590aff7676a92c371b704a7732e05fed7

https://lh3.googleusercontent.com/2AT_TIxyMX0Inqd9Rk4ejaFoRmOOczEwM9E5xz4DfYxaUqgdkXsCRKOX3uHYFOjyU9VwwFzGGCsZnf6BYmkPP0x3OjztRk02SB3O_HOBLz_vXdvoi2g

Liam Spradlin

Senior UX Designer, Material Design

mio-example

<p>New devices are always coming online, offering new formats, screen sizes, and pixel densities that you&rsquo;ll want your product to accommodate. If Googling doesn&rsquo;t give you the numbers you need, or you just want to show off your math skills, here&rsquo;s a relatively easy way to determine the relevant metrics for your designs.</p>
<h2>Do it yourself 🛠</h2>
<p>There are six pieces of information you&rsquo;ll want in the end: the screen diagonal measurement, screen dimensions, aspect ratio, pixel resolution, dp (or <a href="https://developer.android.com/training/multiscreen/screendensities">density-independent pixel</a>, Android&rsquo;s logical pixel) and the density bucket to which each device belongs. Some of those specifications can be found on each device&rsquo;s product page, or through other sites that collect information about specific devices.</p>
<p>It&rsquo;s easiest to visualize this information if we have an example. So, to get a feel for the process of finding these values, let&rsquo;s start with the Pixel 4.</p>
<p>&lt;mio-table index=0&gt;&lt;/mio-table&gt;</p>
<p>The screen diagonal, aspect ratio, and pixel resolution can all be found on the <a href="https://store.google.com/product/pixel_4_specs">Pixel 4 product page</a>. For devices that don&rsquo;t have in-depth or easily accessible specification pages, sites like <a href="https://www.gsmarena.com/search.php3">the GSMArena Phone Finder</a> can be a good resource.</p>
<h2>Finding Screen Dimensions 📐</h2>
<p>After filling in the readily available info, we have three more specs to solve for. The first one is the screen&rsquo;s dimensions in terms of width and height. The formulas for this &mdash; which I learned from an <a href="https://www.omnicalculator.com/other/screen-size">Omni Calculator page by Hanna Pamula</a> &mdash; are fairly easy to use, and only require a diagonal measurement and an aspect ratio (AR).</p>
<p><em>Width = diagonal / &radic;(AR&sup2;+1)</em></p>
<p><em>Height = (AR)&times;Width</em></p>
<p>So for our example, we know the screen diagonal is 5.7 and the aspect ratio is 19:9 (which we&rsquo;ll write as 19/9 in the formula).</p>
<p><em>Width = 5.7 / &radic;((19/9)&sup2;+1)</em></p>
<p><strong><em>Width = 2.44&rdquo;</em></strong></p>
<p>And now that we know Width, we can solve for Height.</p>
<p><em>Height = (19/9)&times;2.44</em></p>
<p><strong>Height = 5.15&rdquo;</strong></p>
<p>So our screen dimensions are <strong>2.44&times;5.15&rdquo;</strong></p>
<h2>Finding dp Resolution 📏</h2>
<p>Density-independent pixels are Android&rsquo;s logical pixel. Measuring in dp allows designers and developers to ensure that what they create appears at the same physical size across screens, no matter what density those screens happen to be. So knowing the dp resolution of a device can be really helpful in targeting that device with your design. You can easily set up artboards and assets that focus on specific form factors, and reliably reproduce your design across them.</p>
<p>For this formula (which you can find in the <a href="https://developer.android.com/training/multiscreen/screendensities">Android Developers documentation on pixel density</a>), we need to know the screen&rsquo;s pixel resolution, the dimensions we calculated before, and the screen&rsquo;s ppi. The screen&rsquo;s dpi (written as ppi) should be available at one of the sources mentioned above.</p>
<p><em>px = dp&times;(dpi/160)</em></p>
<p>In our example, we know the screen&rsquo;s pixel resolution is 1080&times;2280px, and its physical dimensions are 2.44&times;5.15&rdquo; so we can plug those values into the formula, starting again with width.</p>
<p><em>1080 = dp&times;(444/160)</em></p>
<p><em>1080 = dp&times;2.775</em></p>
<p><em>dp = 1080/2.775</em></p>
<p><strong><em>dp = 389</em></strong></p>
<p>Next we&rsquo;ll do the same calculation for the screen&rsquo;s height in density-independent pixels.</p>
<p><em>2280 = dp&times;2.775</em></p>
<p><em>dp = 2280/2.775</em></p>
<p><strong><em>dp = 822</em></strong></p>
<h2>Finding the density bucket 🔍</h2>
<p>The <a href="https://developer.android.com/training/multiscreen/screendensities">Android Developers documentation on pixel density</a> also outlines the notion of &ldquo;density qualifiers,&rdquo; which Android uses to serve bitmap drawable resources in an app. If there are non-vector assets like photos or illustrations in your design, it can be useful to know which density buckets you&rsquo;re targeting, serving the right asset to each device to speed up loading and to avoid distortion and &ldquo;out of memory&rdquo; errors.</p>
<p>Finding the density bucket is as easy as looking at the table in the documentation linked above and comparing it to our dpi value. For the Pixel 4&rsquo;s ~444ppi, we would assign the XXHDPI density qualifier.</p>
<p>&lt;mio-table index=1&gt;&lt;/mio-table&gt;</p>
<h2>Putting it all together 🧩</h2>
<p>Having worked through those calculations, we now have a complete set of device metrics for our example device, the Pixel 4.</p>
<p>&lt;mio-table index=2&gt;&lt;/mio-table&gt;</p>
<p>For further reading on pixel density, layout, and how the two interact, see the <a href="https://material.io/design/layout/understanding-layout.html#usage">Material Design guidance on Layout</a>.</p>

<!-- Copyright 2020 Google LLC.
   SPDX-License-Identifier: Apache-2.0 -->
| Screen Diagonal | Screen Dimensions | Aspect Ratio | Pixel Resolution | dp Resolution | Density Bucket |
| --------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| `5.7"` | `~` | `19:9` | `1080×2280` | `~` | `~` |

<!-- Copyright 2020 Google LLC.
   SPDX-License-Identifier: Apache-2.0 -->
| Density Qualifier | Denisty Value | Scale | Description |
| --------------- | ----------------- | ----------------- | ----------------- |
| `ldpi` | `~120dpi` | `0.75x` | `Resources for low-density (ldpi) screens.` |
| `mdpi` | `~160dpi` | `1x` | `Resources for medium-density (mdpi) screens. (This is the baseline density.)` |
| `hdpi` | `~240dpi` | `1.5x` | `Resources for high-density (hdpi) screens.` |
| `xhdpi` | `~320dpi` | `2x` | `Resources for extra-high-density (xhdpi) screens.` |
| `xxhdpi` | `~480dpi` | `3x` | `Resources for extra-extra-high-density (xxhdpi) screens.` |
| `xxxhdpi` | `~640dpi` | `4x` | `Resources for extra-extra-extra-high-density (xxxhdpi) uses.` |
| `nodpi` | `n/a` | `n/a` | `Resources for all densities. These are density-independent resources. The system does not scale resources tagged with this qualifier, regardless of the current screen's density.` |
| `tvdpi` | `~213dpi` | `1.33x` | `Resources for screens somewhere between mdpi and hdpi; approximately 213dpi. This is not considered a "primary" density group. It is mostly intended for televisions and most apps shouldn't need it—providing mdpi and hdpi resources is sufficient for most apps and the system will scale them as appropriate. If you find it necessary to provide tvdpi resources, you should size them at a factor of 1.33*mdpi. For example, a 100px x 100px image for mdpi screens should be 133px x 133px for tvdpi.` |

<!-- Copyright 2020 Google LLC.
   SPDX-License-Identifier: Apache-2.0 -->
| Screen Diagonal | Screen Dimensions | Aspect Ratio | Pixel Resolution | dp Resolution | Density Bucket |
| --------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| `5.7"` | `2.44×5.15` | `19:9` | `1080×2280` | `392×822dp` | `XXHDPI` |

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/867c97ea686201a075558426afed9f2f1af12301de8abd40e27e8ac2889ec45d8ae3dbf8f3a214ec4766a8138abe01bed00895fc0e41d91c99385c071cc0b8ea

https://lh3.googleusercontent.com/VSXJYJl6FT8-ehDuH_XzkjkJmlGbHJMu9hBQQa0aTCHEC51Jf5eb8mHYs5OPF3V_ifEriOvE8pkq0uLpfs_Jjho8fp5ii5KeGyS3Nws

How-to

{}

Learn how to calculate the right measurements for design across devices with Material Design. Maximizing web design for optimal device metrics.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d8fe2e27788b9e3304ba1b0244cdc037528358fccf01daee81e57a819e929753ed31330474cc14dbd46a62489f46cc172451890a24b6272c5c48056692b4c89e

https://lh3.googleusercontent.com/CAd3BpA2r4f42bkEoylEAK8-lGga0xM-Pu4Ql7Ilrvh4fPswQUOgt3B-1v__DOTK_E1qKfb-vZwmUNNLPIROo5MWmYcev_QcGB3odQ

Device Metrics for Any Screen - Material Design 3

2020-05-19T13:00:00

device-metrics

Calculate the right measurements for design across devices

How to Find Device Metrics for Any Screen

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/8edb584a4387b71d80b844b0ee09bc258045b78d9811489b51029623df94f3c1104c2499280d8914da26e195b6f87f1a6451b6e0dbf941848c054b142440a3cd

https://lh3.googleusercontent.com/wOXMyiYXehxIegai0fl2zhlwJVAOGy3tONR0Gs9QNwHI0mxsZY8Y956dEe8uOND0hufo5MskmAhkSaGp1xJVvYoDAB7tR_KophBC2Q

/blog/material-density-web

Material blog

Using Material Density on the Web

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/7856674c89b7593762c271225d507d1bcd85a95aba42df6b31353d55b212c73b38347ddad5081667b3c6b21ba72ecadcf4f9876607842b4ebc30dda1dd695227

https://lh3.googleusercontent.com/HqzCRYlqY13E3AOr2PRbEqWAZyr5TMAQ06DXkQZneYChrZ0l9SXaC3oAT7XWD64ObZHHftW1ZwkB2wpfo1Yrn-A3RoQUedx8mgo4mWY

/blog/google-material-custom-theme

Material Blog

How Google created a custom Material theme

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/6f6a97a70961c27b3ce68a3d2379523ba098f177ab545e4f7f65cba84e81cbcf292ec1b2e0a4e8c7bbf6796837412c05f309f4e0d5bfeef1a961505ac73dc582

https://lh3.googleusercontent.com/32QVXJlStUJhkr7aylDQUKiIONcfRdpI_QBxa79rDTLEFTVjQCsTCn3PEKAQy0JWrtlYoJaXIa0MDggYcXI5ub4gyiz9Y56hfBOsmg

/blog/material-design-blog-welcome/

Material blog

Welcome to the Material Blog—A Letter from the Editor

mio-example
