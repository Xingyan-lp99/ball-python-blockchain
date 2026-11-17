# Adjusting Grade for Mode

Source: https://m3.material.io/blog/readability-research
Content endpoint: https://m3.material.io/page-data/Posts/5915993901367296.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/5d60e753f0001fb83ad9d525e057a56f1bddb114a16ddc6e6c6e8a514eced94c2aae3c01fdfa05967760a77857a452a00b0c259e085842f56de155b00e6b5786

https://lh3.googleusercontent.com/-cVJ6qd7QoOFzT-KbBKJBEyvC4ODnzy2-oCK1rO3BH6vKea3i0F5Qudiy0dKSs61DEg0FsXTOhOLeSY80skXBZwV9OGTm-tjweMmmA

Michael Gilbert

Staff UX Researcher, Material Design

mio-example

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/73bfd8781cd9f1d75338c8ca19f6a358360865c6edbcc442b3d863fdf9e2be7462ff5e4d4122d9b0f47915f946ba68b8f45afe25a1b2c72beeaa9a47efbd0e42

https://lh3.googleusercontent.com/S_cFY1shz9XVw7G0N_CRcWV84TMij9npZJSUs_orMJDaEp2q2dDULWfWGox_9PB5huMB40flftvnKbF6tHj_gcNHL6sJ46gAGyJ2Ojaw1OaZ8TTJElDQ

Julia Feldman

Senior UX Researcher, Material Design

mio-example

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/d0c35cc07a1a84b3da6989484e42f9db5387e162afcf660a7cadcefdcd70a47100aa9f377e47d6ea042e08316e33bdfd7beb5ee523be9bb59e18e63a3991a855

https://lh3.googleusercontent.com/a99u00GMHFCsxvQqCC-dDhCem9te5huIDPiQv66j6GL5Ynop-e0nVrJiewnfDmjOVq2khQPdTsSAFKFr6HX4PFQlK8YU_M3NhnITmgDxRYBwrWE_K4s

Brenton Simpson

Senior UX Engineer, Material Design

mio-example

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/525dd6aafde9ce95e6b512dfd9ecb2c5f3da763c34fecc6839125d91faa0cc975f90b297b983556caee0c8402211063054bcae7312da78b5a0f724c496886f0d

https://lh3.googleusercontent.com/IvUgJJOnlQYDXqC5h4iWwc7miYCbTrbdUcOHZghR_Hn6z5uX1_T9Y0bdMc1WDG6TaCyu2Nr-BWoHRS8aoUPNeiQxla6UmGtepDYGWmtK4FJTiJWMiY8

Sedeeq Al-khazraji

UX Research Associate, Material Design

mio-example

<p>Consider this scenario: you&rsquo;re designing a product that has both a light mode and dark mode. You&rsquo;ve heard that text in dark mode might be easier to read if it&rsquo;s more <strong>bold</strong>. You&rsquo;d like to make sure your users can have an equally delightful (and highly readable!) experience across both light mode and dark mode. How do you find exactly how bold the text should be to be similarly readable across both modes?</p>
<p>If that&rsquo;s a scenario you&rsquo;ve found yourself in&hellip; well, you and I are in the same boat. As researchers on the Material Design team, we were recently asked this very question.</p>
<p>This blog post will describe, first, how we answered that question; second, what we found; and third, how might you use the method we describe here to use Variable Fonts to improve readability for your products, and your users.</p>
<p>Let&rsquo;s dive in!</p>
<h2>First: How we answered the question, what font grade is equally readable in light mode versus dark mode?</h2>
<p>Before we get started, let&rsquo;s make sure we all understand what variable fonts are. The best way to describe variable fonts may be in comparison to traditional fonts. Traditional fonts, for instance, need a different font file for every available style, like thin, normal, or bold (see the image below for an example). Historically, letters were cast in metal and foundries would create a new letter set for each style, and traditional digital fonts still follow this pattern.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>Variable fonts, however, provide the ability to use <em><strong>type as software</strong></em> and benefit from the flexibility that digital media can provide. Rather than requiring a new font file for every style, variable fonts provide the ability to modify the design of your text along a continuous scale for a number of visual characteristics. So, rather than requiring three font files to display thin, normal, or bold fonts, you can use the same variable font to display every weight on a continuous scale, from the very thinnest possible style to the very boldest.</p>
<p>Similar to the weight variable font characteristic, you can also modify text grade. Grade can be thought of like weight in most ways, but grade maintains text width, so you can increase grade from the minimum to the maximum values while minimizing the impact on the overall design of text blocks or causing line reflows. An example of text cycling through the minimum to maximum grade values for a Variable Font is shown below.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>Now that we&rsquo;re on the same page with variable fonts and grade, how might we approach the question: What font grade is equally readable in light mode versus dark mode? To answer this question, along with oh-so-many other questions we&rsquo;ve been asked, we designed an experiment.</p>
<p>Our experiment was pretty simple: we designed a prototype that would show study participants a two word phrase. We asked participants to read the phrase, remember it, and then hit the enter key. Once they hit the enter key the phrase would disappear, and we asked participants to type the same two word phrase into a text box. We measured, first, the time it took participants to read the phrase; second, the time it took to type their response; and third, the accuracy of their response, allowing &ldquo;correct&rdquo; responses to include minor misspellings.</p>
<p>And that&rsquo;s pretty much it! This is one of those instances where a straightforward question really does benefit from a straightforward experiment.</p>
<table style="border-collapse: collapse; width: 99.7611%;" border="1">
<tbody>
<tr>
<td style="width: 98.2279%;">
<p>If you&rsquo;re still curious about the details of our study design, here&rsquo;s a brief rundown that will hopefully help you tackle readability questions in a similar way.</p>
<ul>
<li><strong>Participant count</strong>: We launched the experiment with 184 users. This number was arrived at after completing a&nbsp;<a href="https://en.wikipedia.org/wiki/Power_of_a_test" target="_blank" rel="noopener">power analysis</a>&nbsp;to decide on the minimum number of people needed to detect a significant result if there is one. We included extra participants to account for drop out rates and took into account corrections given the number of analyses we ran.</li>
<li><strong>Word selection</strong>: All words used for this study were selected from the&nbsp;<a href="https://www.readabilityformulas.com/articles/dale-chall-readability-word-list.php" target="_blank" rel="noopener">Dale-Chall word list</a>. This list identifies words that the average 4th grade student should know (specifically, once 80% of 4th graders know the word it can be added to their ~3000 word list). We intentionally opted for a word list that was based on familiarity rather than difficulty since we wanted to minimize the confound of an individual's reading ability impacting response times (i.e., a word's difficulty is a characteristic of the word; it's familiarity is a characteristic of the broader population, statistically speaking). By identifying a list of words that aim to be familiar to a broad set of the population, we hoped to minimize the impact that individual familiarity may have on overall readability</li>
<li><strong>Word order</strong>: Each of the phrases included a two syllable and three syllable word. The order of the words was randomized in each trial, again, with the aim of minimizing any potential impact of word complexity on response times.</li>
<li><strong>Dependent variables</strong>: We measured (1) the time to read a phrase, (2) the time to repeat that phrase, and (3) the accuracy of the repeated message. Phrase accuracy was measured by calculating the&nbsp;<a href="https://en.wikipedia.org/wiki/Levenshtein_distance" target="_blank" rel="noopener">Levenshtein distance</a>&nbsp;between the typed and displayed phrase.</li>
<li><strong>Analysis</strong>: Data were analyzed with a two-way repeated measures Analysis of Variance (ANOVA). We ran post hoc tests with bonferroni corrections.</li>
</ul>
And that&rsquo;s it! If you&rsquo;d like to do a similar study the setup is pretty simple, all things considered. By doing the above, you can determine the impact of grade on readability like we did. But you could also determine the impact width, optical size, or any other variable font characteristics has on text readability!</td>
</tr>
</tbody>
</table>
<h2><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">Second: What we found</span></h2>
<p>This part is easy because we can describe all our results in a single graph:</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>From a quick glance at this graph we can see a couple things right away. First, readability in dark mode (the blue line, on top) appears to be consistently higher than readability in light mode (the orange line, below). And second, while readability in dark mode appears to be relatively stable across values of grade, readability in light mode appears to improve as grade values increase (that is, the time to read a phrase decreases as the value for grade increases, shown by the orange line going down and to the right). But are these apparent differences <em>significant</em>, in the <a href="https://en.wikipedia.org/wiki/Statistical_significance" target="_blank" rel="noopener">statistical sense</a>? We had three main findings, described below using the same graph.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p><em><strong>First</strong></em>, we didn&rsquo;t find any impact of grade on readability for dark mode. What does this mean, you might be asking? Are you free to run wild and use any value of grade in dark mode wherever you want, willy nilly, without fear of repercussion or rebuke?</p>
<p>Not <em>quite</em>. While we didn&rsquo;t find a significant impact of grade on readability in dark mode, it&rsquo;s possible that in other contexts&mdash;for instance, reading long paragraphs instead of short phrases&mdash;the difference might be significant. But for the contexts we tested, we&rsquo;d suggest that design can select a value of grade they feel is most appealing, without that grade value negatively impacting readability.</p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p><em><strong>Second</strong></em>, we <em>did</em> find a significant difference between the lowest and highest values of grade in light mode. As the graph above shows, readability appears to gradually increase (i.e., reading time decreases) as the <em>grade</em> value increases. You can see the greatest difference between the reading time grade at 150 versus grade at -112.5 is about a tenth of a second (1.92 to 2.02 seconds). This may not sound like a lot, but remember that this is the average difference in time it takes to read two short words&mdash;that difference can add up!</p>
<p>So what does this mean? Basically, in light mode, higher values of grade result in text that is more readable. This difference doesn&rsquo;t appear to exist when the grade value is 0 (the default), so increasing grade arbitrarily from the default won&rsquo;t improve readability significantly. But if you&rsquo;re considering adopting the <em>minimum</em> value of grade (i.e., -200 in the graph above), you should be sensitive to the fact that this may have an adverse impact on the readability of your text. Which is not to say that you should never use these values, but consider using them in a context where that impact is balanced by the aesthetic or brand goals you&rsquo;re trying to achieve.</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p>And <em><strong>third</strong></em>, we did find a significant difference between the highest values of grade in light mode, and most values of grade in dark mode above around -115. This is where it gets interesting (I mean, I think the whole thing above was <em>interesting</em> too, but this is where we get to answer the question we set out to answer, around finding equivalent readability between dark and light modes). This graph allows us to draw two final conclusions.</p>
<p>First, if we&rsquo;re looking to identify grade values that result in equivalent readability between light and dark mode, when you&rsquo;re using the highest values of grade in light mode, you&rsquo;ll need to approach the lowest values of grade in dark mode before you&rsquo;ll start to see equivalent readability (i.e., before you&rsquo;ll start to see reading times that <em>aren&rsquo;t</em> significantly different between light and dark modes).</p>
<p>However, the visual difference between minimum and maximum grade values is a dramatic change! If you&rsquo;re using the maximum grade value in light mode and are creating an equivalent dark mode, consider the balance between equivalent readability and equivalent visual design&mdash;you may be able to approach equivalent readability by minimizing grade in dark mode, but you should be sensitive to the impact this may have on how people perceive the two modes of your product as complimentary.</p>
<p>And last, revisiting the question we set out to answer at the top: <em><strong>what font grade is equally readable in light mode versus dark mode?</strong></em> We can now answer: if you&rsquo;re using the default value of grade (0), our results suggest there is <em>not</em> a significant difference in readability between light and dark mode. So, in the context we tested, there is no need to modify grade between light and dark modes to achieve equivalent readability.</p>
<p>And <em>that</em>, is how I met your mother. Jk, but that&rsquo;s pretty much how we tackled this research question, and how you might be able to tackle similar questions for your own products, in your own contexts.</p>
<h2>Third: Where you can go from here</h2>
<p>I hope the above shows you a bit more clearly how you might <em>collect</em> and <em>interpret</em> data that allows you to more effectively measure text readability. A reasonable next question might be: where do we go from here? How might we use this information to build better experiences?</p>
<p>Most immediately, I&rsquo;d suggest that the above should provide a more clear path towards understanding and improving readability for a <em>specific audience</em> in a <em>known context</em>. If you know who is using your products and how those products are being used, you should be able to adopt the above approach to fine tune text design for those specific contexts of use.</p>
<p>More broadly, though, I think there&rsquo;s a <em><strong>huge</strong></em> opportunity to use approaches like the one described above to not only iteratively improve existing product experiences, but to envision new ways of making interactions more <em>usable</em> and more <em>accessible</em> in any situation.</p>
<p>Consider for example designing a product that can be used both when you&rsquo;re right next to it or when you&rsquo;re across the room.</p>
<p style="text-align: center;">&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p>Using the approach we&rsquo;ve described above, you can start to optimize for readability <em>no matter how the product is used</em>. With this type of approach, we can start to move from readability and accessibility as a static and stable factor in design, to a future where accessibility can be sensitive to <em>any situation</em>, and even to <em>any individual person</em>.</p>
<p>This is a pretty neat future, I think. And I&rsquo;m excited to continue doing the work that helps us get there.</p>
<p></p>

Image showing the text “thin, normal, bold, black” in Roboto font, demonstrating the range of font weights between thin to black

Roboto font showing thin, normal, bold, and black weights.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/c7d70278432b626092acb0fb5b2f6122a666311685ac2c20a4625a953b821ea59126df64c0c7d8ea11340eb09bd0b12c7449c5cea3a5c09d464e35854216ea50

https://lh3.googleusercontent.com/UNg4f2lBdyWLA9GgmFSSfmHCB3NS2jqKAB4a3a-z8xK7Jz9TTOQM5-B48wNjwndohoCKQaFlcyB1E4JQA2bi7bMV8ucgFalss0oZ_7LTdddGA989zQ

An animation showing the Roboto Flex Variable Font displaying the text “maine lobster,” cycling from the minimum to the maximum value for the grade Variable Font characteristic.

Roboto Flex Variable Font, demonstrating the continuous range between the minimum and maximum values for grade.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/39b8ca3f3fe9c6ea443727797dbd19da952d1a4a6e4f50dec3be43327c4a9f8f59020f46cc28e19a3fee6dcce90369074dcdf6b8940e672ba524e608d6f8def5

https://lh3.googleusercontent.com/QtIYUc2KV4oek2V3PocYGzc8MlTMcgbCgvAmgHdRC2evRpffuGJnLKVANE07iEM-UVbzEGIDbM8qTBGkUPSlBEdINL45jW14S1To1raY96OBoYjyszo

Graph showing readability results across multiple values of grade, between both light mode and dark mode

Graph showing readability results across multiple values of grade, between both light mode and dark mode

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/db8effbf19c9effb6152f98abbfa37461e4f9cc86c493dea73c3e62671736cfea9c10cd55227abb176c19fba56950f41cc6ff79903d82a5420eb266e82e0ef5a

https://lh3.googleusercontent.com/Fs0jmhIGONaK5azzaPi1hcpbixcrLCoBhCmCzI7fTz2XU3dvq8WnBXHCkq4rjRJHSAoU_vWlh4iBJjZ8qFXM-V21e4VJg16aQ66sQ35oPW3Gpv9oiA

Showing readability across light mode vs dark mode, here calling out no significant difference in readability for all values of grade for dark mode

Showing readability across light mode vs dark mode, here calling out no significant difference in readability for all values of grade for dark mode

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/35dd02d2482fe10052bc44d247f12d398577e986a0d60a48a228de676d29a32d2c0c97f09d279592348494a67659ed44507c42b37772c72b0e69bdb92c5813c9

https://lh3.googleusercontent.com/L1yLlLcewN03yJZHNNg6gCDcxdad47bJ0hIEvcNlmLIIg5GyrvspcD3kSaInASs3r3vgmxaU-xCWqHAR5Sis4amEid8ct5ZikbeYom0veerCc4G6CT8

Showing readability across light mode vs dark mode, here calling out a significant difference in readability between the lowest and highest grade values for dark mode

Showing readability across light mode vs dark mode, here calling out a significant difference in readability between the lowest and highest grade values for dark mode

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/808e73ea73b47425755ab5b95d193e68d8ca1791b14f2ae5167467fdc54b8026c014ffb4e7ada2fd4d03b30c3b65fb6989ce4f260df002242d95cd560c0864c1

https://lh3.googleusercontent.com/TV7TozFl8Zk-ANMLlc91yL2DiCx9YdVvVetGL3Y58886VWezw8k8-IMf6-xbxgvYPDf6McQhZbuF9begLY54993QZxjePxx_vnGRKaaf55yefrRJgXM

Showing readability across light mode vs dark mode, here calling out a significant difference in readability between the highest grade value in light mode and grade values in dark mode above around -115

Showing readability across light mode vs dark mode, here calling out a significant difference in readability between the highest grade value in light mode and grade values in dark mode above around -115

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/520a81deffa848b2ce6faab10017ef9dfe0e861cd28d1187f25ebd4c829fd5597a2451f3ffe3001543b031ba8fd71623707f721085d93729c34d4f1f9721b495

https://lh3.googleusercontent.com/OrVr4xEo02eAO3aPb1zGsQF1y9fOsssjWzLYxV1hx1K2L4qQVfqSyTvY37EFPb45D5Wem5ImUXf8sLwpUyblwPUM_DiO9Lp-LSarzklZceTGvtnl4Kc

Animation of a small screen in tablet orientation showing the text, “Your order is 7 mins away.” As the viewer backs away from the screen the text size and grade increases, as the text changes to “7 mins away,” showing that the text is always readable at multiple distances

An example of how the approach to readability research described above could be used to refine the experiences of future interactions

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/0ca7dde5bf3b49332565df29959f6ae04a6a2bd96a571d61a5aa965a11d4c5512e4f21f2e8f67b6512bb9711666daaafa5abf7f19935e866ad2fdc07ea11ed92

https://lh3.googleusercontent.com/u0Y_JNSbFzBdT-phyhew_8DsEcbdzkQgkIltSXKdU-mVchOFQZ0ZYeVep4apZt1jZSNHaRKLNhinzpRYadel2dSbkgaYtfEr3rVJIilT8Zr8H7GTKS8

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/98936c7573b123e188d8b56d3d7fbef42cb9782f6736a38847b0fbf5fe227262efcae4f56ee965f2f01e85f39f4c0968aa02124fe5c314b3319013dcf86aa41d

https://lh3.googleusercontent.com/Kj5Hi7eTnTTkho_DbsWuvoTo1LmyQpVJXGnmCD9u0eYZ6EErSX71gzh4zsi2MpyS4N5WoAqRsX5eapGrkPTd-GmhveRMckuMvScAoAGOh1cp8r3SokH2

 

{}

Measuring the impact font grade has on text readability

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d384de48fcd5bbed2528a08ab33f57fc1db1ab573081a55f1ad9ce0578edbbc204058421ebbe0a2d54f4ea3cfd1179223d21589d5c395c8dfaf57f8d35e0d0ed

https://lh3.googleusercontent.com/X6VTR-xJ7zSUs_GewWzw5S8scznVW9i7T6PPXAW76FwXrt-VOK9Wgd20RcJZVw3Lmy1Qsy_5jT8sfSJZOrIZ3QA7W7jkRYOMfV_6uzRhFHFK6ZS7gdc

Adjusting Grade for Mode

2022-05-11T09:00:00

readability-research

Measuring the impact font grade has on text readability

Adjusting Grade for Mode

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/4dcefa2b4c771ff73024bb9a7f93b45aedd11268b405d94eafbe32ff1fa2d53e8312eb6d4a85f0c223aae3d5d66efec1c3e41533c898052851c5acc2ac197a5e

https://lh3.googleusercontent.com/8bAEmxfET_BswMp5wmWuelccbR30wJ2ijNWmPXlBgvP-zKBk6PyFDOkwltb23P3JlaQ5DKAMEUy_mKnt7pudUrMkk8E2JWXEHBpwpyYspVJnFaz0aRA

https://m3.material.io/styles/typography/overview

M3 Typography

Material Design 3

Typography guidelines

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/10670050668c02a15305405869d10261ae9184c4b9943da19db1f77dfec09cbadff181927e3ee1b025e024736848d2c53950c779e44a033489d2f68c57607b44

https://lh3.googleusercontent.com/-WjjawJvR9AIODJEhrs_slzoG32Y_Ip0a0c_qe04DMIR2zS0UGQxrmY7DU0LH8--_G45NFBmIFEmAdGxbVC31KCl4Zw6h3Yz-L3pff45FVFM8rINVFw

Designing Text for the People Who Read It

/blog/designing-text-visual-acuity-research

Material Blog

Designing Text for the People Who Read It

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/6e7eec708fb5c1794eda7db3f0982e30c908fba4773e693836bd8a78e2c7a9d55b4905ed8963d701ad731a190f0169ff8ddb3f415e98b2ba57d6ba9732e73b41

https://lh3.googleusercontent.com/zvHQAODkXrk7n5wVwZXxjt8hIf0yCPm9wBgEtG6ZjANrYCAsLGRHSlNolT1fLQG0QweUaOnclPrBbKzf8ItZ3XpDubtUH6N0fPZUhZea34N8a0NxxIE

Say hello to Roboto Serif

/blog/roboto-serif

Say hello to Roboto Serif

Material Blog

Say hello to Roboto Serif

mio-example
