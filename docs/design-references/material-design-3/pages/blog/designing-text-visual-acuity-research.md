# Designing Text for the People Who Read It

Source: https://m3.material.io/blog/designing-text-visual-acuity-research
Content endpoint: https://m3.material.io/page-data/Posts/4654308022550528.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/5d60e753f0001fb83ad9d525e057a56f1bddb114a16ddc6e6c6e8a514eced94c2aae3c01fdfa05967760a77857a452a00b0c259e085842f56de155b00e6b5786

https://lh3.googleusercontent.com/-cVJ6qd7QoOFzT-KbBKJBEyvC4ODnzy2-oCK1rO3BH6vKea3i0F5Qudiy0dKSs61DEg0FsXTOhOLeSY80skXBZwV9OGTm-tjweMmmA

Michael Gilbert

Staff UX Researcher, Material Design

mio-example

<h5><em>This article was written in collaboration with Kenichi Yoneda, Ben Lucas, and Julia Feldman. Illustrations by <a href="https://shuhuaxiong.com/">Liz Xiong</a>.</em></h5>
<p>As a long-time wearer of glasses and contacts, I&rsquo;ve been familiar with the chart shown below from a pretty young age. If you&rsquo;ve never taken an eye exam with one of these, it generally goes something like this: first, the eye doctor would have you sit across the room from this chart. You would be asked to cover one eye and then read each line, from top to bottom, until you couldn&rsquo;t make out the letters anymore. After one eye, you would test the other. The lowest line you could read in this chart with either eye would provide you with a measure of your visual acuity. In the US, this is commonly expressed as a fraction like 20/20, 20/40, etc. A nice high level overview of this process is available in this (very brief!) presentation from the National Institute of Health: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2040251/02/2020">Testing distance vision using a Snellen chart</a> [1].</p>
<p style="text-align: center;">&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>There are two points to call out here. First, the size of the chart matters. If the characters are giant, your ability to read the text will understandably be impacted. Second, your distance from the chart matters. Both of these may seem obvious, but they&rsquo;re worth pointing out because if you want to measure visual acuity you&rsquo;ll have to control for both at the same time. The reason for this is all boils down to our first observation &ndash; visual acuity is a measure of an angle over a distance.</p>
<h2>Observation #1: Visual acuity is a measure of an angle over a distance</h2>
<p style="text-align: center;">&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p>Or, if we want to be more precise, we can consult The Organization of the Retina and Visual System [2]: &ldquo;visual acuity is the spatial resolving capacity of the visual system. This may be thought of as the ability of the eye to see fine detail.&rdquo; Generally, as the subtended angle (you can think of this as the distance your eye travels to see from the top to the bottom of an object) required to observe any specific artifact decreases &ndash; for example, when the artifact moves away from the observer &mdash; the amount of visual acuity required to distinguish characteristics of that artifact increases.</p>
<p>An example might make this more concrete. Consider the image below, where a specific artifact (in this image, a banana, for scale) is perceived by a viewer at two different distances.</p>
<p style="text-align: center;">&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>In the top image, the distance between viewer and object is denoted by d1, the angle subtended by that object is a1, and the height of that object is denoted by h. In the bottom image, the distance is d2, the angle is a2, and the actual height of the object is (still) h (although the perceived height of the object is of course smaller, but more on that below).</p>
<p>We can take away two main points from this illustration (I mean, we could probably take away more than that, of course, or learn a lot about bananas. But for the sake of this article we&rsquo;ll limit to two). First, the relationship between distance ( d) and perceived height is proportional. Anytime you double the distance between an observer and an object, the perceived height of that object drops by half. In the example above, this can be seen in that the perceived height of bananas on the lower half of the image would be about half the perceived height of the bananas on top, even though (from an outsider's perspective) the actual height of the bananas doesn&rsquo;t change (of course).</p>
<p>Second, the relationship between angle (a) and perceived height is also proportional. Again, in the example above this could be seen from the fact that the perceived height of the lower image (e.g., how large the bananas appear to an observer from farther away) will subtend half the angle compared to the bananas on the top image, that are half as far away.</p>
<p>You can test this really easily with just a couple of post-it notes. All you have to do is:</p>
<p>Step 1: Place one post-it note on the wall, folded so that half the post-it note is sticking out from the wall.</p>
<p>Step 2: About an arms-width away from that first post-it note, place two more, one directly above the other, both folded so that they stick out from the wall.</p>
<p>Step 3: Place your head about an arms-width in the other direction from the first post-it note.</p>
<p>When you&rsquo;re done, it should look like Figure 3 below. The stacked post-its at right, at exactly twice the distance, will appear to be exactly the same height as the single post-it closer to you.</p>
<p style="text-align: center;">&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>&ldquo;But what does this have to do with visual acuity!?&rdquo; you may ask. And rightly so! Thank you for keeping me on track. As stated above, visual acuity refers to the ability to resolve detail at a given angle, where that angle can be a function of the size of an object or it&rsquo;s distance from the observer. In our examples above, resolving detail may mean the ability to differentiate one post-it from two, stacked on top of one another (i.e., Figure 3) or one banana from a bunch of bananas (for instance, in Figure 2). It&rsquo;s like seeing the proverbial forest for the trees, but in this case it&rsquo;s not proverbial and it&rsquo;s backwards &ndash; we really are talking about the ability to differentiate trees in the forest. Similarly, for most eye tests, resolving detail means resolving the characteristics of letters &ndash; for instance, the individual strokes that make up an uppercase &ldquo;E&rdquo;.</p>
<p>Once again quoting The Organization of the Retina and Visual System [2], &ldquo;Visual Acuity (VA) in Snellen notation is given by the relation: VA = D&rsquo;/D where D&rsquo; is the standard viewing distance (usually 6 metres) and D is the distance at which each letter of this line subtends 5 minutes of arc (each stroke of the letter subtending 1 minute; figure 4).&rdquo;</p>
<p style="text-align: center;">&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p>Ultimately this means that it&rsquo;s possible to estimate the visual acuity of any individual given their ability to identify features of an object at a known size or distance. Of course, we already know this in general (that&rsquo;s what a vision test is all about, after all!), but the detail provided here sets us up for Observation #2.</p>
<h2>Observation #2: Text can be scaled over multiple distances</h2>
<p style="text-align: center;">&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>The prior observation really boils down to two main things. First, one way to understand how we perceive objects is by measuring the angle it takes to subtend that object. If you move the object farther away from the observer, the angle decreases as the perceived size of the object also decreases. The math involved here is probably already familiar to you if you remember high school trigonometry (oh, those happy days!), but don&rsquo;t worry if you don&rsquo;t remember &ndash; we&rsquo;ll cover what you need to know next. And second, that visual acuity (generally speaking) is a metric that describes how any individual perceives objects that subtend a specific angle.</p>
<p>What this means, however, is that we can scale content to be perceived as any size, given any distance. For a concrete example, imagine you&rsquo;re looking at a menu at a coffee shop. You can clearly see the line for what you want to order &ndash;</p>
<blockquote>
<p><strong style="text-align: center;">Everything bagel with cream cheese</strong></p>
</blockquote>
<p>(I&rsquo;m in New York, after all, and a good everything bagel with cream cheese is hard to top). Let&rsquo;s say that the text on the menu is 14pt Roboto. This is equivalent to a real text size of about 4.94mm.</p>
<p>As introduced above, the angle required to perceive that line on the menu depends on two things &ndash; the size of the actual text, and its distance from you. For the sake of this example, let&rsquo;s say that the text is 35cm away from you (which also happens to be a decent estimate for the average distance most people hold their phones away from their faces, by the way). We can calculate the angle required to subtend that line at that distance with the following:</p>
<p style="text-align: center;"><em>a<sub>rad</sub> = 2 * arctan( h / d*2 )</em></p>
<p>Where <em>a<sub>rad</sub></em> is the angle (in radians) that the text subtends, <em>h</em> is the height of that text, and <em>d</em> is the distance it is being viewed from. Plugging in the values we have from above, we get:</p>
<p style="text-align: center;"><em>a<sub>rad</sub> = 2 * arctan( 4.94 / 350*2 )</em></p>
<p style="text-align: center;"><em>a<sub>rad</sub> = .0141</em></p>
<p style="text-align: left;">If degrees are more familiar, we can convert radians to degrees with:</p>
<p style="text-align: center;"><em>a<sub>deg</sub> = a<sub>rad</sub> * ( 180.0 / 𝛑 )</em></p>
<p>By plugging in our numbers, we end up getting a value of <em>0.8086&deg;</em>. Which is pretty cool, right? With just a couple equations, we&rsquo;ve shown you how to identify the angle that text subtends (the distance your eye must travel to perceive the text top to bottom) &ndash; not just at one distance, but at any distance (just replace the <em>350</em> above, the distance in mm between viewer and object, with any other distance).</p>
<p>We&rsquo;ll wrap this section up by answering two more questions to show what you can do with the above information (and again, to just show how cool all this stuff is). First, what if instead of holding the menu 35cm away as in the example above, it was on a stand 100cm away from you. Specifically, how big should the text be to require the same angle to subtend?</p>
<p>The equation for this is pretty simple:</p>
<p style="text-align: center;"><em>h = tan(a<sub>rad</sub>) * d</em></p>
<p>Where <em>h</em> is the height, <em>a<sub>rad</sub></em> is the angle in radians (that we calculated above), and <em>d</em> is the distance that we want to calculate for. Plugging in our new numbers, we get (note that distance is in mm):</p>
<p style="text-align: center;"><em>h = tan(.0141) * 1000</em></p>
<p style="text-align: center;"><em>h = 14.11</em></p>
<p>Which means, if the text were 100cm away from you instead of 35cm, to maintain the same angular height that text would have to be 14.11mm tall. This is definitely something worth keeping in mind if you&rsquo;re designing a menu that may be read from multiple distances (or, you know, if you&rsquo;re designing products intended to be viewed on multiple devices)!</p>
<table style="border-collapse: collapse; width: 99.7301%;" border="1">
<tbody>
<tr>
<td style="width: 97.9999%;">
<p><strong>A shortcut</strong></p>
<p>If you don&rsquo;t need to calculate degrees or you&rsquo;re trying to avoid arctan in everyday life (no judgement here), you can also calculate mathematically equivalent heights at multiple distances with a simple ratio. As mentioned above with the post-it note example, if you double the distance an object is from you, you&rsquo;ll need to double the size of that object for it to be mathematically the same height &ndash; or, for the subtended angle required to observe the object to be the same.</p>
<p>How does that work? From the above, we already know that the text size at 35cm (or 350mm) is 4.94mm &ndash; our baseline. We can calculate what the size would be at another distance with the following:</p>
<p style="text-align: center;"><em>( 4.94 / 350 ) = ( size2 / distance2 )</em></p>
<p>If we wanted to see what the text size would need to be at 100cm (or 1000mm), we would solve for x in the following:</p>
<p style="text-align: center;"><em>( 4.94 / 350 ) = ( x / 1000 )</em></p>
<p>Cross-multiplying gets us <em>x = 4,940 / 350</em>, which again yields a height of 14.11. Same as above!</p>
</td>
</tr>
</tbody>
</table>
<p>And second, if the text size wasn&rsquo;t increased like above, what would the perceived height of that text be?</p>
<p>We can get this value with:</p>
<p style="text-align: center;"><em>h<sub>perceived</sub> = ( h / d ) * d<sub>base</sub></em></p>
<p>Where <em>h<sub>perceived</sub></em> is the perceived height, <em>h</em> is the actual height, <em>d</em> is the new distance, and <em>d<sub>base</sub></em> is the baseline distance &ndash; in our case, 35cm, or 350mm. Plugging in the values, we get:</p>
<p style="text-align: center;"><em>h<sub>perceived</sub> = ( 4.94 / 1000 ) * 350</em></p>
<p style="text-align: center;"><em>h<sub>perceived</sub> = 1.729mm</em></p>
<p>Which means, if the text were 100cm away from you instead of 35cm and the text size wasn&rsquo;t increased accordingly (i.e., holding the actual size constant rather than the angle), the perceived size of the text would be about 1.729mm. Which is noticeably smaller than the original 4.94mm text size!</p>
<p>We&rsquo;ll wrap up this section with a hopefully straightforward recommendation: when you&rsquo;re designing for multiple distances (or unknown distances), you&rsquo;d do well to consider the user experience at each of them. Hopefully, some of what I shared above will allow you to do that a little bit easier.</p>
<h2>Observation #3: Text size can be expressed as a measure of visual acuity</h2>
<p style="text-align: center;">&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p>If you&rsquo;ve managed to stick with me this far, well done! But before we wrap up I wanted to share one last observation that builds on the first two that may allow you to express or understand text sizes in a slightly new way. Specifically, by being sensitive to things like expected viewing distance (e.g., Observation 2) and how visual acuity is understood and calculated (e.g., Observation 1), <em>we can express text size as a measure of visual acuity.</em></p>
<p>To make this concrete, let&rsquo;s revisit the example from above &ndash; you are once again standing in line at your favorite bakery, holding the menu in front of you. For the sake of clarity and continuity, let&rsquo;s again say that the menu is about 35cm away from your eyes. But this time, instead of describing the text in terms of its size (i.e., 14pt Roboto, or about 4.94mm tall) we can describe it in terms of the visual acuity required to be able to reasonably distinguish the characteristics of that text.</p>
<p>Which means that instead of describing text as 14pt, or 4.94mm tall, we can state that this text, viewed from 35cm away, is about 20/190. Meaning that if any viewer has a visual acuity of 20/190 or better, they should technically be able to read that text at that distance. Again, recall that 20/190 is a Snellen fraction &ndash; similar to the familiar 20/20 that&rsquo;s typically considered &ldquo;perfect&rdquo; vision.</p>
<p>Note, though, that <em>technically</em> being legible is not the same as being readable &ndash; or even providing a good reading experience. We want to be clear: our goal is to give you a new way to think about text size that's more sensitive to the people who will be reading it. This includes being explicitly sensitive both to how close or far away your readers are from the text, as well as designing for readers who are low-vision or visually impaired. We are not suggesting that these are ideal minimum text sizes.</p>
<p>Before we move on and show you exactly how the Snellen fraction is calculated, consider a couple opportunities that expressing text size in this way opens up for us. First, it positions text size as a far more user-centric metric, where both expected viewing distance (e.g., context) as well as the viewer&rsquo;s visual acuity (e.g., user characteristics) must be taken into consideration from the very beginning. Second, it allows us to describe text size in a way that is potentially more familiar, or more intuitive, than through absolute measures. For instance, calling any text &ldquo;14pt Roboto&rdquo; is probably super clear to designers and those that love them, but to the average person what &ldquo;14pt Roboto&rdquo; looks like in practice may not be immediately apparent. On the other hand, however, if you describe text as &ldquo;20/80,&rdquo; meaning that anyone with 20/80 vision or greater (or corrected to 20/80 vision or greater with glasses/contacts) should be able to read that text.</p>
<p>Which is, again, super cool, right?! I mean, I do this for a living but I still think it&rsquo;s pretty neat.</p>
<p>With that out of the way, there&rsquo;s only one last thing to cover: given a text height and an expected or average viewing distance, how can we express that text size as a measure of visual acuity? We can do that with the following equation:</p>
<p style="text-align: center;"><em>s<sub>denominator</sub> = ( h / tan( radians( 5/60&deg; ) ) ) * ( 20 / d )</em></p>
<p>Where <em>s<sub>denominator</sub></em> is the denominator of the Snellen fraction (the numerator will always be 20). This one is a bit more complicated, so let&rsquo;s unpack it.</p>
<p>As mentioned above, the visual acuity in Snellen notation is given by the relation VA = D&rsquo;/D, where D&rsquo; is the viewing distance and D is the distance at which each the size of the text subtends 5 minutes of arc. The first part of the equation above &ndash; ( <em>h / tan( radians( 5/60&deg; ) )</em> ) &ndash; allows us to compute that distance (again, refer to [2] for more details on this). At this point, you have a Snellen equivalent, where the numerator is our actual distance and the denominator is the value you&rsquo;ve computed so far. To express this value in the more familiar Snellen notation (where the numerator is &ldquo;20&rdquo;) we just need to multiply the computed value by <em>20 / d</em>, where <em>d</em> is the expected viewing distance.</p>
<p>And that&rsquo;s it! Easy peasy, right?! To make sure this makes sense, let&rsquo;s walk through it one last time with a concrete example. If we return to our scenario above (we&rsquo;re still waiting in line at the bakery) and the menu text is 8pt Roboto (which is 2.82mm, rather than the 14pt size that we calculated above), how large is the text expressed as a measure of visual acuity, for an expected viewing distance of 35cm? We can solve that by plugging our values into the equation above:</p>
<p style="text-align: center;"><em>s<sub>denominator</sub> = ( 2.82 / tan( radians( 5/60&deg; ) ) ) * ( 20 / 350 )</em></p>
<p style="text-align: center;"><em>s<sub>denominator</sub> = ( 1938.89 ) * ( 20 / 350 )</em></p>
<p style="text-align: center;"><em>s<sub>denominator</sub> = 110.79</em></p>
<p>Which means, if we&rsquo;re looking at 8pt Roboto text at 35m away, we would need to have about 20/110 visual acuity or better (either normal or corrected to normal) to read that text. Which is a fair bit different from the 20/190 visual acuity that was required to read the 14pt Roboto as shown above.</p>
<p>Before we wrap up, let&rsquo;s answer one last question (we&rsquo;re almost done!). Let&rsquo;s say you're standing in line at the same bakery, but instead of holding the menu about 35cm away from your eyes, it&rsquo;s again on a physical stand on the counter. The question now is, how close would you need to be to read the menu if you had 20/40 visual acuity? And 20/40 was not chosen arbitrarily here &ndash; in the state of New York, 20/40 is what&rsquo;s required by the DMV to be able to apply for or renew a drivers&rsquo; license [3]. Let&rsquo;s say the text is again 14pt Roboto, 4.94mm tall &ndash; plugging in the values to the equation above, but instead solving for d rather than sdenominator, we get:</p>
<p style="text-align: center;"><em>40 = ( 4.94 / tan( radians( 5/60&deg; ) ) ) * ( 20 / d )</em></p>
<p style="text-align: center;"><em>40 = ( 3396.49 ) * ( 20 / d )</em></p>
<p style="text-align: center;"><em>40d = 67929.8</em></p>
<p style="text-align: center;"><em>d = 1698.25</em></p>
<p>&ldquo;Woah,&rdquo; you may be thinking, &ldquo;that seems like a long ways away!&rdquo; But remember our units are mm here, so how we can interpret this is: In order to read the menu at the bakery, where the text is 14pt Roboto, or 4.94mm tall, a person with 20/40 vision would need to be within 1698mm (or 169cm) of that sign. Which, for the Americans among us, is about 5.6 feet.</p>
<h2>Conclusion</h2>
<p>And that&rsquo;s it! Thank you for reading through all this. If you have any comments or corrections, I&rsquo;d love to hear them &ndash; feel free to reach out on Twitter by tagging <a href="https://twitter.com/materialdesign">@MaterialDesign</a>.</p>
<p>It&rsquo;s also worth noting that we&rsquo;ve identified some interesting cases where scaling text height by angular height alone may not be necessary &ndash; but that discussion is beyond the scope of this article. I&rsquo;ll write that up separately and share with you all later.</p>
<p>Until then, thanks again!</p>
<h2>Cited</h2>
<h5>[1] Sue, S. (2007). Test distance vision using a Snellen chart. In Community Eye Health, 20(63): 52. Retrieved from <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2040251/">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2040251/</a> 02/2020.</h5>
<h5>[2] Kalloniatis, M., Luu, C. (2007). Visual Acuity. In Webvision: The Organization of the Retina and Visual System. Retrieved from <a href="https://webvision.med.utah.edu/book/part-viii-psychophysics-of-vision/visual-acuity/">https://webvision.med.utah.edu/book/part-viii-psychophysics-of-vision/visual-acuity/ 02/2020</a>.</h5>
<h5>[3] Vision requirements &amp; restrictions. Retrieved from <a href="https://dmv.ny.gov/driver-license/vision-requirements-restrictions">https://dmv.ny.gov/driver-license/vision-requirements-restrictions 02/2020</a>.</h5>

Snellen chart

Figure 1: Snellen chart. 
Image source: https://commons.wikimedia.org/wiki/File:Snellen_chart.svg. This file is licensed under the Creative Commons Attribution-Share Alike 3.0 Unported license.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/40dbe9ec4584b17ecfb864ffd81ff818f9dd851821b2ab28ede46def74ff533a95630e401206e9f7df96e4696b1a2fd3166a3bb41dea950796eee112a8528081

https://lh3.googleusercontent.com/PEaL0VkabtclfgJfLmgDNVkBl6lC97HCGv8Pmt5U_Go01DkLKaBkkjtH0L0J0qAzc1mL4UAKTOnvNdG2U6R8R9LOZ6mElJtpMNMTF2y5SABQh_zoIkM

abstract illustration of colored orbs

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/4c53b78309f7e3a2bcf9b9a0248df5061871144e4a893cb87c039cf347b069b151bd45b2f3dc67cb2e650654b1b149d2bd60021520eb1b9f2d3a08530c684b42

https://lh3.googleusercontent.com/vUOhn7KPnv9d-RECVO2SAU_ZU_Bq8u_Xv1ivLZXbxvmKVQnTfNPPWCL20-UwW_uwlsWJbRJdxb0EwWw7iDMxoMY2xUs45A-9DRl7iaGn352-4DlEocg

Illustration showing angle and distance of viewing a bunch of bananas

Figure 2: Illustrating how the angle required to perceive this object changes as a function of distance. 
Image source for the bananas: http://www.freestockphotos.biz/stockphoto/15909. This image is licensed under Public Domain. Released to the Public Domain by its author.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/9c0bcfa2476d51d4310488f8ad09e45c7a0c6350c9c7b92ea5d14bc35c28574926a4304f27f8988c011fbd898d6bc5599183f55c4d38be3d7a03bb96adfebd9b

https://lh3.googleusercontent.com/Zq8nrMBYeHbsamMFWhUeOMVCyVOG33eSmaXff_qT5Td26UCkMFC6fLKBo9pIogLSdqrXjqIzfhw52lQtodKxhsZy9zlzV29d93sQh-lnO3WVu3wWpus

Illustration showing viewing distance for an arrangement of post-it notes

Figure 3: Illustrating how if you double the distance between you and an object, you need to double the actual height of that object to match the perceived height. Grab some post-it’s and give it a try!
Image source: The image above was created in Google Presentations by the author for use in this article

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/8308d5375b01aa4cd9ebfc7bdcef74f22f32a39d66325b6e7e12e3283b4e52b5f34da911796a7ead197c6ee34001022c22c038368988665a47faa31f9a3ace3c

https://lh3.googleusercontent.com/kYorLIW25QGPeqQHCBKhggDN5iHzWRszxpGb3eqzzQR0imbn87H2H4uD2rpfUC5DzCIjKV1ITQ5f0zN0smoFWtPNqHHp4cYD0qLOkBfNuj2nUaxLd8Q

Illustration demonstrating the Snellen fraction

Figure 4: Illustrating how we can arrive at a Snellen fraction (e.g., 20/20) given the ability to resolve detail (the features of the “E”) at a specific distance (subtending 5 minutes of arc, or 5/60ths of a degree).
Image source: This image is from a publicly accessible blog post, linked at [2]. License unknown.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/b7f676e581bf654c959cc7d0257d3c3b3268c1a937f86b5c34731c0b518f7061e131adde6d35f6ada95af1bbc410be97320e326d19311fa144507c49d5a3b68b

https://lh3.googleusercontent.com/sW0FLvro--78dKeXIp4yX9aDKF2ozbzxMISu0HbSl_ZROTxp_9HtoxT1BcfilfqyGu3Knzz_vY9QbWjtcZUBGuHhV4Je--EqEP9OBCviJRt0eESiPts

Abstract illustration of colored orbs, now arranged in a straight line through space

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/448b463c0a41d1b9e02e3db115a627884f0d2906067fc8999d8c5a3c558f00c3328215785c97f247b301688e65e6884fc9e43428a25a7ae0147ac7781551b256

https://lh3.googleusercontent.com/YGu41ttwa4JWpsftlsjM_-DTJoh9y-H_Uansbb9xHZU2v8cLjr8sauM54xH8jDPLazFFNAdumvm4tfbY39TDUGLLANLNtwE60hVT_YMqaMNto6_bNA

Abstract illustration of colored orbs with magnified letters behind them

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/b11fb00398c6a443dec98f99b1c07a830dad907fc487a0953b1d31fdd28917bfa97e3e1993d37c724727702b1dd388385dab8f5f77aea1b4039365a2138e9373

https://lh3.googleusercontent.com/G5Swupweu3VoBK5tKRvLePKBn1T-JiGAg_-2f0hT66od7aPL9ILj43zNzBUJTNRYZlOYxCeF3LgTsmbFTXi4Mvn0OYj6hkZXCaX6yvUJ8y09TFmajfQj

Abstract illustration of an eye and variously sized orbs floating in space

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/eab21bd88d97777314e77bb1b10b2b79e8ffb0b582c6ee8a4a88dc7d4ef75c39613840213d1abd35f1cbe1350710eea2101a1897f952e33cff0474b427ac62c7

https://lh3.googleusercontent.com/1lNY69iZ1beIzMdKwc5WOX7GpCR0PMsp93A1F_jF_kcEVJNqKy0YH-glyLtzr8uqrNbqhLjr63iCGWmg7VMiYRjMsqvXMc3hlubxgv1IGMVIGXCwcNU

Research Design Typography Patterns

 

{}

The science behind visual acuity, legibility, and text size

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/81b758a6b8d9080d1abda2ffc95439e2a689829df4bdd6b236daac6d04cca5e5a6d1d495839de3bc0987cb2bcd7f37b2de4ebcb5b9cac11bc6e1659c569c6d1c

https://lh3.googleusercontent.com/52BLWQi5ZM27HHd6BxF-bvDLfzr4S_M5XTh1Mkr0Cwl-uYWMf6v9-cW69ZdsXuEkOJQKf2n33vz7FmIvaRLnbN3Fd1GLQ8qN90mnHA

Designing Text for the People Who Read It

2021-03-11T13:00:00

designing-text-visual-acuity-research

The science behind visual acuity, legibility, and text size

Designing Text for the People Who Read It

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/7bbd8dbc40e9bb70ada1a87ec1d452185fa1bd23acf217dfa51f2b67d3e72a68eb03d290d7e9597fd4b2df021c1576b89b9fb505ec454d2b9c9392a50b683326

https://lh3.googleusercontent.com/1T6DD1rCMym64PMEPWDZkXntz8DRWfB7ac7RWS2k_nH1goLXbSZLkQbYBcj2zk3hXyUI9NLkuE-bINnvvb6-STbawnxnzVlsd4mx

/blog/design-material-theme-type

Material Blog

Designing a Material Theme: Typography

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/8edb584a4387b71d80b844b0ee09bc258045b78d9811489b51029623df94f3c1104c2499280d8914da26e195b6f87f1a6451b6e0dbf941848c054b142440a3cd

https://lh3.googleusercontent.com/wOXMyiYXehxIegai0fl2zhlwJVAOGy3tONR0Gs9QNwHI0mxsZY8Y956dEe8uOND0hufo5MskmAhkSaGp1xJVvYoDAB7tR_KophBC2Q

/blog/material-density-web

Material blog

Using Material Density on the Web

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/2fbf19ff8aea714d1c0eeb84f2f1152031b02b53ebe9dc21ac3caa3299e8284a2a0516f6f0a79955d1468eefe39bacba9d73b4ac4936ea8fb079acb581d05e6b

https://lh3.googleusercontent.com/-PHBkosgv2aQ-ieldkcVX6MqPD0l8yPEXvncrWGPIjbUcSwLa7yzoj-D65JI3mfoCc-9mV_BStrgyfuTsoX9pEuIP5EF9vdFwpxO

/blog/digital-wellbeing-design-systems

What “Digital Wellbeing” Means to Material Design

Digital Wellbeing

What “Digital Wellbeing” Means to Material Design

mio-example
