# The 24-hour Clock Design Challenge

Source: https://m3.material.io/blog/24-hour-clock-design-research
Content endpoint: https://m3.material.io/page-data/Posts/5937855834750976.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/73bfd8781cd9f1d75338c8ca19f6a358360865c6edbcc442b3d863fdf9e2be7462ff5e4d4122d9b0f47915f946ba68b8f45afe25a1b2c72beeaa9a47efbd0e42

https://lh3.googleusercontent.com/S_cFY1shz9XVw7G0N_CRcWV84TMij9npZJSUs_orMJDaEp2q2dDULWfWGox_9PB5huMB40flftvnKbF6tHj_gcNHL6sJ46gAGyJ2Ojaw1OaZ8TTJElDQ

Julia Feldman

Senior UX Researcher, Material Design

mio-example

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/eb04247d28af59fe5402bd7bf137b2de663d2dfde67043d07231cfd8cdef507a370d984f0d8325e45c83c3fcbfd3f771822838fcc07c9d6bcd10f35174256cab

https://lh3.googleusercontent.com/XJQJJGSv7GsKJZZ0wDb0iamsHCUK6FHE1F76um3buCfn0NJGkqiDN4ygjiDUUSFQsFoFO1PrghEfYQfZ4doJNXco1gX8AN_IRgMvvoEUo0fukZmXWB8

Dillon McCallum

Visual Designer, Material Design

mio-example

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/86a4b9890ad34b4e7f39edb0ed1970713d438a5bdc69f199d8c17c3045114545c75c5d377f4864f750494318f0ce51401d036d1f0bfc4a47df4e9bf7aef81626

https://lh3.googleusercontent.com/BidkPq09M2TXzIkjlGtWnMGvQrFvXuZPKyqf5WiPZzYOgqQeFa_qpVp3tsu1-ph2GU4riPZxqPK7SiA20gV6HE65vxbvOlkt4iTo5ETMEDu5Tr3KWKFo

Andrew Ng

Staff Interaction Designer, Material Design

mio-example

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/5d60e753f0001fb83ad9d525e057a56f1bddb114a16ddc6e6c6e8a514eced94c2aae3c01fdfa05967760a77857a452a00b0c259e085842f56de155b00e6b5786

https://lh3.googleusercontent.com/-cVJ6qd7QoOFzT-KbBKJBEyvC4ODnzy2-oCK1rO3BH6vKea3i0F5Qudiy0dKSs61DEg0FsXTOhOLeSY80skXBZwV9OGTm-tjweMmmA

Michael Gilbert

Staff UX Researcher, Material Design

mio-example

<p>Setting a clock on a digital device is something that, at this point, many of us are familiar with. However, the way we set the clock is deeply shaped by mental models that differ between 12-hour and 24-hour clocks. We encountered this difference between mental models that led to an opportunity to rethink from the ground up how people interact with a component as familiar as the ubiquitous time picker.</p>
<p>Let&rsquo;s back up and give you an explanation &amp; context for our 24 hour analog clock redesign.</p>
<p>First, what is a time picker? A Time picker enables users to specify a time value. You may have used time pickers to set your phone alarm in the morning or maybe you&rsquo;ve used it to schedule a meeting, book a flight, bus, or hotel, or even when searching for movie tickets to catch the new Marvel superhero movie.</p>
<p>Consider the first example - setting an alarm on your phone. How might that experience look?</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>If you are a 12 hour user you can imagine that a 12 hour analog clock has the number 6 at the bottom and 12 at the top. You have both a minute hand and hour hand as well as an am/pm selection that affords you to take a single glance at the clock and know the time.</p>
<p>How might this dial look for a 24 hour analog clock?</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<h2>The Original 24 hour Analog Design</h2>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>The first Material Design 24 hour clock (diagram 1) was released in October 2020 and featured two rings - an inner and outer ring each representing a set of 12 hours to total to the full 24 hours in a day.</p>
<p>The second 24 hour analog clock (diagram 2) aimed to address a handful of concerns related to accessibility and collision points of inner ring numbers. To address those concerns, Material moved towards a single-ring model (diagram 2). This design presented a single-ring with 12 on the bottom and 24 at the top. All &ldquo;even&rdquo; numbers up to 24 are displayed and there is a space in-between for odd numbers.&nbsp; Upon setting the hour, the clock then switches to a minute mode to set the minutes.</p>
<p>As the new design was released, feedback from the community was overwhelmingly positive except for the 24hr dial, in which we heard &ldquo;Bring back the system's two inner &amp; outer circles.&rdquo; Users who commonly use 24 hour selection were having difficulty using the new Time-picker&rsquo;s 24hr single-ring dial. Users had become accustomed to the dual-ring design, this new convention didn't follow the user's anticipated mental model, and at first glance it wasn't clear how to select odd numbers which were represented by spaces in-between the even numbers that were displayed.</p>
<p>Although the updated design addressed key accessibility concerns, there was still a disconnect between users' mental models and the new 24 hour analog dial.</p>
<h2>The Design Challenge</h2>
<p>We met many challenges related to accessibility and making sure our users understand the analog clock dial.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>Our designs explored both dual-ring and single-ring solutions. We explored the designs on small screens and found collision points of previous patterns resulted in numbers overlapping and the clock face becoming unreadable.</p>
<p>In addition, the 24 hour analog clock design presents unique design challenges, particularly with the user's mental model and expectations for number positions on an analog clock face.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>To tackle this challenge, Material prototyped over 50 unique designs not just exploring different visual treatments (single and dual ring), but also interaction such as long tap/hold, sliding, ring swaps, etc.</p>
<p>The team narrowed it down to 4 optimal designs that capture the spirit of Material 3, met our accessibility expectations, and addressed our user&rsquo;s concerns. We went on to test the designs at scale in an international study evaluating the usability of each.</p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<h2>The Research Study</h2>
<p>We conducted two mixed-method research studies to investigate the usability of 24 hour analog clock designs (a single ring and a dual ring design) compared to a digital input clock design. Data was gathered from over 50 people in 6 countries (India, Indonesia, Brazil, Germany, France, UK) to understand perceptions among users who use 24-hour clocks, 12-hour clocks or both. 10% of our participants considered themselves low vision users.</p>
<p>Both behavioral data (quantitative) and user opinions (qualitative) were collected to make the research recommendation. Our motivation was twofold: we wanted to know which design would 1) lead to fewer errors when setting times, and 2) be considered least confusing by participants. To evaluate this we asked participants to set the clocks to different times throughout the day (10am/1000, 5:30pm/1730,&nbsp; 2am/0200) on each version. Success rates were collected along with observational data as we watched participants set the times and recorded delays in setting the time. We also gathered rich qualitative data of the perceived negative &amp; positive aspects of each design as well as which design was considered least confusing.</p>
<h2>The Results</h2>
<p>What did we find?</p>
<p>Even participants who currently use 24 hour clocks found all 24 hour analog designs unfamiliar and confusing. A 24 hour analog clock seems to be simply uncommon and breaks the mental model even in countries where people use the 24-hour digital clock.</p>
<p>Considering the analog clock designs, participants made the widest range of errors with the single ring design and only 4% of participants called it the &lsquo;least confusing&rsquo; design. However, even the dual ring designs also resulted in errors as users were uncertain how to select time throughout the day.</p>
<p>An overwhelming majority of participants perceived a simple digital input as the least confusing and indeed made fewer errors on this design. We did notice that there would still be value in clarifying if it's a 24 or 12 hour clock with a digital input design.</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<h2>Conclusion</h2>
<p>The research strongly supports moving to the direct-input digital format to make it easier for 24 hour users.</p>
<p>Since Material has historically offered an analog option still in use by many today, we will move towards the digital input by default for 24hr users while still providing the option for users to enable the 24hr analog (dual-ring) presentation if desired. We also will use the user&rsquo;s input to impact the default. That means if a user manually switches to the new 24 hour analog clock it will remember that preference the next time the app is opened and will default to it.</p>
<p>Material will continue to evaluate usage of 24hr analog time picker to better understand our users and continue to support research driven design decisions. We plan to continue to provide experimentation to push towards more usable, more accessible, and more beautiful design for all our products and all of users. We strive to better understand how people interact with even the tiniest aspects of digital technology such as the hands on a 24 hour analog clock, to make interactions with Google products, fundamentally, more human-centered.</p>

a twelve-hour time picker clock

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/97a8c20088d24d729b8c5de1ad83ad30c7046ef2b6240af59ee6fc765cdb0e9868478ab9b0f23d199fb6ecd8ef5915f39c499d0f2394780979dfb4be7443dc75

https://lh3.googleusercontent.com/m9x1uHLj-KKuvWx9S9zo0OtWj3aadbAmzzwWutdYAKpefs4pvOWZWGfQ0TqhRCkYWp2YJ3GdbEn3SvYrmwEOgh6_1cuDSMHTsFkUvVvkarvB6pNVvQ

Original time picker designs showing 24-hour and 12-hour versions

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/6811e3c97d43dd166ff13451f3451bb0582c887809b1a1f77b72e87f38a179841f4e3d6f1a04fc90b2b5487f060f5553e2162aa8dd41dcf77babf74725083222

https://lh3.googleusercontent.com/gs1cv34uuTr4X6dflFgy2nQLD6ZmuJG_EotPdoSeKKoMJZP7rO9ja412ZvXwOlSmWl8HneeYMgwQKojUjYoaXBsw3Sk8rdxsNoEtVviO1jOlQimgHAKt

Design explorations of single- and dual-ring time pickers, showing circular touch targets

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/fc1a8ce5b563de9d17e0ec1149474f3fa99048b3193080caf606b941e8adc4d5f9879fc7a2fdac7706098906fadec015db78191318e6f97b0d2cb1576e6a388f

https://lh3.googleusercontent.com/wL-TD2HoVcecl2-XQHM-EsMTZRRaAiUDGn1632w8nqCRjMVccc9t03MFSBau0BiFrkLWle7_qDBxSwJEfxZZkRdTxVEI0u98ERiEhr06EeFc9zwsTw

Illustration of many design explorations for the time-picker ring

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/ddbdc1921b276ec2aca144391661baa60c2acc805161f03ea25bf4d54e2e65785250e8c20846c615202d281fd392d992866f2251defb70f5f25ad3d6f1d940c9

https://lh3.googleusercontent.com/WA8IkxD3irZNF2OXGHi_EsaYDgz_Q77PfNrQ0g1VBkUwDW584wa5WliMrgXP4IWpAYnT3oXVRzANm0GgrXMUr17ux2j170BOuZA45gfdt2hjVVO8nlc

Illustration showing different options for researching time picker usability

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/8cc1ce1d719f8fd0f842f1a66e4df4156c9e2cb606d66fa88e743569e44eb4e671d4ee730b62c21f2ea1a1d76c6677a10d32c1b8ea942c29e380b2d5f1fa6938

https://lh3.googleusercontent.com/OmMLe78-2zGxB2rt7ElPGDu1hAvGgrsoraxWoSxXg9SLjAih6frVLV5MGygZ4YJ7JAYmHxlYwYzm9XsfqdKEbk7dCkgUj1B2EI79CH2_DrmIXtSbXA

Images showing the final time picker designs on a phone screen

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d45844cbfa54c139a01f2312679967518f49ec4eaa299531401e74306619a4277bea8785038188d0ac9f07a0193e58141156a15483e73699e850f6013bd021a5

https://lh3.googleusercontent.com/kInZ79ESkqiZVw2oqvHhHxZ4WsPQDe9cJbNbfHrv7rPZq7eBlVqkYKtxEtp_ZrjEIg6PMCiBE_tXwqYHbDn0vbqfrwDeGphlnNWwBwwXuMSLIoNdmg

Time picker component on an abstract background

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/54395a5858f589ebceb21369a7cd5aca23d52f8122299c2f55e6f158f05a362d705fbdb264c534bb2feb7c65a7f36e6a5e1d03b61e7107ab67bb16bce6bfd342

https://lh3.googleusercontent.com/oA1APblnxoASlmabYI8yCDjNjlIv2SAMA8u9O9CBXnm8W9L4mtUNlEorrUz6bbYlqbqNilLcTrxtz2No9PV6L9hzGkoQR3M7dfETahus7qq4hf4i9A

design research components

 

{}

Design and research create an accessible and user-friendly time picker

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/ecdba65922c2d15b5e98e55ee806c74b08edb7a21cac38df63984457c14f63e2e4e7e1207ba447fc978026df99cdea889378fe5d78097a2d64e6ae371d1dd20b

https://lh3.googleusercontent.com/awqU8wkZbnucN_ns4dyrL_qyiLreJX4K-mjBNaNFthQ1OP9CVCUmfcvANYFeawPmkf7463T_vI-AH5DuBdvdWb4F9O526sosnV7hsVbvGZWyzDzGOSc

The 24-hour Clock Design Challenge

2022-12-01T13:00:00

24-hour-clock-design-research

Design and research create an accessible and user-friendly time picker

The 24-hour Clock Design Challenge

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/7988151124048178cc96306b65796531d65b3bf79d709446cfdcdaff03cc9ecb36e2ab5c4413698a3d6a4ad8146a1bbee56e136527fb9e42c8964a1f29300634

https://lh3.googleusercontent.com/5J71k4ejdHyRkjMdbUf6nE02HknqhTkuyHIV5QcLzRbnrF0YiPd2W23GGQj-zKDsU4B5TVrrpVgR3MB8FwDbv-O45ai27Zi9fXHEfCB1ltzj3tyDIxo

https://material.io/blog/material-io-redesign

Magic, utility, and redesigning Material.io

Material Blog

Magic, utility, and redesigning Material.io

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

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/10670050668c02a15305405869d10261ae9184c4b9943da19db1f77dfec09cbadff181927e3ee1b025e024736848d2c53950c779e44a033489d2f68c57607b44

https://lh3.googleusercontent.com/-WjjawJvR9AIODJEhrs_slzoG32Y_Ip0a0c_qe04DMIR2zS0UGQxrmY7DU0LH8--_G45NFBmIFEmAdGxbVC31KCl4Zw6h3Yz-L3pff45FVFM8rINVFw

Designing Text for the People Who Read It

/blog/designing-text-visual-acuity-research

Material Blog

Designing Text for the People Who Read It

mio-example
