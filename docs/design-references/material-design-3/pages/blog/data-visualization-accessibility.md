# Top Tips for Data Accessibility

Source: https://m3.material.io/blog/data-visualization-accessibility
Content endpoint: https://m3.material.io/page-data/Posts/5048380078292992.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/595929b4f412105df8576d87fc5827ec60182fdffa58b92b5e1f7625a864bb4cd41553fcc5bf5d816f7369fcf8e886b116e20358a444e373a60cdc981f59c746

https://lh3.googleusercontent.com/LLq4cGS9mvVkZasBqxKNyqUbSXsUehhLbUgauTOi1_Qv7vougcvpEoFUYxSnlpWYVBJQzBL4ESM1DXDsb4nMCy1_lhvuaJ12gZ4W1HIScG-gVF0laLg

Kent Eisenhuth

Co-founder, Google Data Accessibility Working Group

mio-example

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/00df0ccf5cc436defb4818e87c15a42d4ab807ce704f58017c6e111ede978ed520311cb76d74893533a023ca3b6cd9ab7c602cfb246c0ed623f9112d9872e1be

https://lh3.googleusercontent.com/V5YnUX0degXjlzi3R8T6OXn275rlyjpmUVCDMq1CpITcKP93briy5dfGDwrIXJ6UZEdAdvdK2tROjeRa3PVSMK3ps9w0RjZ9QgrlymxK9oQOeNcjZh4i

Gerrit de Vries

Co-founder, Google Data Accessibility Working Group

mio-example

<p>Data visualizations like charts should work for everyone, regardless of their ability. But creating accessible data visualizations extends beyond simply meeting compliance requirements. Explore the six tips below to learn how to represent data in a way that is accessible, scalable, and helpful.</p>
<p>See the Material Design <a href="https://material.io/design/communication/data-visualization.html#principles" target="_blank" rel="noopener">data visualization principles</a> for general guidance on portraying information in graphical form.</p>
<h2>1.&nbsp;Facilitate comparisons</h2>
<p>Arrange or convey your data so that it&rsquo;s easy to compare data sets or data points across multisensory experiences including audio, haptic, and visual representations.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p><strong>In practice:</strong></p>
<ul>
<li>Reduce the amount of information that people need to process to understand how data sets differ or relate to each other. Keep comparable data sets on the same scales and measures where possible.</li>
<li>Provide inclusive controls like filtering&nbsp; to allow people to quickly locate outliers or other instances where the data deviates from the common trend.</li>
<li>Whenever possible, use a <a href="https://material.io/design/communication/data-visualization.html#types" target="_blank" rel="noopener">chart type</a> that makes it easier to differentiate between data sets. For example, line charts make it easy to spot small changes over time with continuous data.</li>
</ul>
<h2>2. Be a helpful guide</h2>
<p>Provide the right context at the right time. Build affordances that prioritize data comprehension, exploration, and navigation.</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p><strong>In practice:</strong></p>
<ul>
<li>If possible, provide a summary of what your chart is trying to convey. Refresh this based on interaction, such as if data was filtered. Try not to rely on verbally summarizing the chart&rsquo;s visual elements, which can distract from the main data points.</li>
<li>Orient people within the data by consistently highlighting where they are, where they came from, and where they can go. For example, supply information on data recency and data collection methods, and standardize patterns and components across different data visualization projects whenever possible.</li>
<li>Offer flexible ways to explore and prioritize data so that people using assistive technology can manipulate the data using familiar tools (for example, through sorting).</li>
<li>Provide an accessible method for linking to the underlying data set so people can explore the data on their own (for example, link to downloadable data in CSV format or in an accessible table).</li>
</ul>
<h2>3.&nbsp;Focus on what matters</h2>
<p>Always prioritize data accuracy, integrity, and simplicity. Every action, color, haptic, and audio element should support data insights, build understanding, and reduce cognitive load.</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p><strong>In practice:</strong></p>
<ul>
<li>Use common charts, such as area charts, bar charts, donut charts, line charts, and <a href="https://material.io/design/communication/data-visualization.html#types" target="_blank" rel="noopener">other charts</a> that most people already understand.</li>
<li>Use colors that achieve required&nbsp; contrast ratios with adjacent elements (for example, background, metrics, and interaction states) along with an additional element or encoding to draw focus and communicate consistent meaning.</li>
<li>Ensure the visual elements and encodings within your data visualization accurately represent the underlying data.</li>
</ul>
<h2>4. Provide structure</h2>
<p>Hierarchy and structure make it easy to understand what the chart is for and what its elements represent. Appropriate structure can help users navigate your visualization.</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p><strong>In practice:</strong></p>
<ul>
<li>Provide labels for legends, data points, axes, and marks so that chart elements can be unambiguously interpreted.</li>
<li>For interactive charts, use proper accessibility markup, like <a href="https://www.w3.org/TR/wai-aria-1.1/" target="_blank" rel="noopener">ARIA</a>, to describe the organization of the data and the elements of the visualization. This will help people relying on assistive technology to interpret the visualization.</li>
<li>Use elements that support keyboard navigation (or ensure it works on your custom elements), in a way that isn&rsquo;t taxing (for example, decreasing tab stops for people with limited motor skills). See the <a href="https://m3.material.io/foundations/accessible-design/overview" target="_blank" rel="noopener">Material accessibility principles</a> for more tips on keyboard navigation.</li>
</ul>
<h2>5. Embrace flexibility</h2>
<p>Respect different needs on data depth, complexity, and modality. Allow your data visualizations to extend and adapt over time.</p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p><strong>In practice:</strong></p>
<ul>
<li>Consider how chart elements (color palettes, axes, etc.) meet a variety of needs, abilities, screen sizes, and data types.</li>
<li>If appropriate, provide discoverable&nbsp; options that allow people to choose&nbsp; the visualization&rsquo;s theme, contrast, and density based on their needs.</li>
</ul>
<h2>6. Exceed expectations</h2>
<p>Embrace dynamic, smart, and clever experiences that overdeliver for your audience.</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p><strong>In practice:&nbsp;</strong></p>
<ul>
<li>Strive to create a multisensory experience that leverages a device's core capabilities, including audio, haptic, and visual representations.</li>
<li>Account for overall performance and compatibility with all platforms and assistive technology.</li>
<li>Factor in polish, surprise, and innovation as you design your data visualizations or data experiences.</li>
</ul>
<h2>Applying this guidance</h2>
<p>Creating accessible data experiences requires listening, humility, and a constant appetite for improvement. We should always embrace diversity on our teams and co-design our data accessibility solutions with people with varying abilities.</p>
<p><strong>These tips are just a starting point.</strong> How we practice them will change time and time again as we continue to work together to make data experiences that provide value and insights to everyone.</p>
<h4>Recommended reading</h4>
<ul>
<li><a href="https://m3.material.io/foundations/accessible-design/overview" target="_blank" rel="noopener">Alt text guidelines</a></li>
<li><a href="https://medium.com/google-design/redefining-data-visualization-at-google-9bdcf2e447c6" target="_blank" rel="noopener">Google&rsquo;s Six Principles for Designing Any Chart</a></li>
<li><a href="https://www.w3.org/WAI/fundamentals/accessibility-usability-inclusion/" target="_blank" rel="noopener">W3C Fundamentals of Accessibility and Inclusion</a></li>
<li><a href="https://www.w3.org/WAI/standards-guidelines/wcag/" target="_blank" rel="noopener">WCAG (Web Content Accessibility Guidelines)</a></li>
</ul>
<h4>Acknowledgements</h4>
<p>I&rsquo;m incredibly proud of the designers, researchers, engineers, writers, and subject matter experts who helped create these tips: Brandon Wilson, Gerrit de Vries, Ian Hill, Jialin Yun, Jennifer Reilly, Jessica Klos, Jennifer Yuchi, Jesse Kulp,&nbsp; Jesse Zackery, Kai Chang, Lorraine Kan, Nicholas Cottrell, Sierra Seeborn, Tyler Williamson, and Young Choi. This amazing group has played an essential role in creating accessible data experiences that meet people where they are.</p>

Abstract example of how comparisons are facilitated through visual encodings and sonification.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/37d8671d65959c1b1f199b7ce8864e74073ebb0681eceb37a6cea83b0ba4d010ba5ed73dce01c229c9678f4bc0e8350f5102d0725790765ad361a88c8284f5f3

https://lh3.googleusercontent.com/xSf4_TQ6-6mmp3Lr39LA8h_ACxzmOI9reyXxaE9xgRUF0UORkjZDH5tCpY8M7WzdSpAkeBw9rSrPdl5XFdWEyeKbBgSZDl4pHe9J6ku5HNP-xIRCuA

An example of how text, data ink, and data set navigation can work together to guide the user to take necessary actions.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/274a549e72345c3f0ce63f921da47f449d57f0bc8496c72841334344f43e8fd7197b8404c5f78acf9660ecf14393c17a81bf4db4b6f4f4056b6e9cf06fd1e5c5

https://lh3.googleusercontent.com/6Lr_nGKyo1qB_Dm2C5w51eOcoUfHlAqIQWkSvsRTXJlbcWvcdC13c0SlXyN880i1tV6KSM4Nt4AxuHUSOfKtG2ygWPtUGakbXeeEpMrjMyRXEeiX1A

A categorical chart sketch that uses outlines and fills to draw focus.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/39c081c25a31e04b6347e82429195bca8b1de350c639e928c3cc3ba8d1a2db55da1d376cd45348913e6e50d2ba668f9a36d4b407199186a08d62cc05b4992df2

https://lh3.googleusercontent.com/n2L87evsGnVgnHWzJ5ZNZpSmzgrPOtpFUTP1lTUsxD3Uk0t_1gNU_kUq0k-tZRM0efdgFUvQznn5nSbM1kArJhLwSwSwnW0nKMZzO9O9ighnEZ-Cz2Y

A representation of keyboard navigation patterns and ARIA roles and landmarks for charts.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/18c0d486dbdaf8d8135b1d1eab2b309eef4ef5d77397abd012078d696462b17a3e8b6dbe592316a98b2e19671bf96f337d5fe132d06da80c6947c11a7cecc50d

https://lh3.googleusercontent.com/tBesw7PNqbmp6fMlwDI8pTAmqTb69Et1VOiI2tzK0FhFriTrmgMeWUQYLdd2r4_j_iacWNwKi1ZMDIDAzRSQhJERDhAq2b0y831FO-aNyRiuGZbnmg

Sketch showing how a chart can be displayed on multiple devices and surfaces.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/ca48e84e23c19a5d294b6867799b47fa74130f336182fd808ddad73058ec33b1c2af6f575a37de13f260ae90ec6305bfed3b8c08912020060d48ad46843ffbc4

https://lh3.googleusercontent.com/7YMcseoC0F5r14hOYRhxx5REP9efZb8urY_juQ6M0NvQnUV-IMWpqyjCgHz71d-mhMR4_Mfi9NhU_N24t4h5z3Iq4XtaSPnPplIGJtOBmyJv0hFg4Q

Example of how data trends can be represented by combining text, audio, and haptic feedback.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/ebdf24068089e51e8ae0ac3b907d8f261dafbe67d562817ec541fef39f18ae8813466021b08dac8cbf6e611759d2dd79a50376d72ff450592b1725f2f34c8f39

https://lh3.googleusercontent.com/yBmnmPX96Chf-7bBAMqIHibgC1F_Ts19CB6jg5_JT6sh0aN38RDQj29tHH01BftEFRNcsiglLAqNRv5dj56HfFqUbzfABjWNxLvu2vEfUxC_sUg2hFY

Abstract illustration of various charts

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/49dc21425f0e2939798317d8705b51581963084f1f7b538168887289cc0b689799ad1baccd42656b658543a7762717beb01ecd2c51538df3c46bcde7a0f82eaf

https://lh3.googleusercontent.com/mtoOMJ1gebE6i4qXKxXgi4Cyn-Qt8FinbBZGk_Jhha-NhJGvd9AX71JUmgGLIzXc1NkxLSbEjNqx4QvcIbtO5CZG5-H_yxHwDUIeBIwBF6baeFpY8so

how-to design accessibility

{}

Material Design data visualization principles. Learn about six strategies for making your data visualization accessible, scalable, and helpful.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d62464a6d2cf6c51d58c0c384ad32afb1ea7abc58a7cbf3581bf81c92914cb521d9098fb394c603be4fcbfea2479f943ea6ddd67aec291e92c16f66cb818b996

https://lh3.googleusercontent.com/CWMuWUsQzhzyvond4vNyl091yAfb7ZxGEiKo-5Dq0MznFPslci8JrHS3c9spAGK9qdCX5mBV01W8zRT-BmkRhX151SQzMmQNn50-PjK4uHvW3Qltk7E

Top Tips for Data Visualization & Accessibility

2022-11-08T13:00:00

data-visualization-accessibility

Six strategies for making your data visualization accessible, scalable, and helpful

Top Tips for Data Accessibility

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/6e1b33b4459260f611ad53abc79882c8b07c29ea5666480695b7ae7c7ced4753630b1200e7fee3d037144e614f520a48e5fde71da2ff40e4ee2a2403e9a7b29a

https://lh3.googleusercontent.com/yx1oQ8Lrfl4f07SbKimuQJheMhMxMrENYR9qX-Fc4FuCR1fdjT2WrF3ODg0DZQoWw2JMUTBhAxXXqACfwBzlf12BQnHbS2FhlQQhn_XubJY4neLNsIo

/blog/m3-a11y

Design for everyone

Material Blog

Design for everyone

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/f5dfcbc0e58d329536f35f550d3045ce74693de1248f1bba61be0cb8f36524ae6d740a457562f2ec442c56cfedde81db7e1829385e5e04bc65ad33b5fac985cc

https://lh3.googleusercontent.com/Bi7oDPu4sAThijGH18IKGlSfRWvrjOfBoTVTNGTf0w_wSbzVvwTyzAcmOgSZpObYxxXYgtC1yhT5G2NTu7GMyZqzUSS1BIgxyF0b8R9miM0Z3uxfUMY

/blog/asset-people-1

Replacing “Users” with People

Material Blog

Replacing “Users” with People

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/163967e90866e2bd46fbeb9fb23e0abe8b3159ad71ba5b6e6c8c1af8b96a1b01b67bc7ef9f7075806e2a1b8c4eb924f93447ab1db80933a574f17db4dd8e38c1

https://lh3.googleusercontent.com/pNM_PU6JBTYHPnVSuHa3g58e3wnVZujp87QQZlrmRfybmAGwdpqD6eiFB-vxNxbvsvQ6u_6Xo1pnIBrPIO2IoHKbk16jQ-npQtFzol-QLpDtUcBPcsU

/blog/5-steps-large-screen-apps

5 Exercises to Prepare Your App for Large Screens

Material Blog

5 Exercises to Prepare Your App for Large Screens

mio-example
