# Using the Gemini app with Material Design 3

Source: https://m3.material.io/blog/how-to-gemini-app-compose-material-design-3
Content endpoint: https://m3.material.io/page-data/Posts/5572176225107968.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/614fdc1c4f82aa57d9c9aaa01c44509258620870563e9046d7929870ecb5a4bb971f72a19acc7daff9f406d54bd41d6a73cd82ffab7ea9581b440b0b953e8b7e

https://lh3.googleusercontent.com/TvSMcJ9qApbYSwdbs_wvzuF-JljmgZgxpCVIBwjliVoSlSdp3UnT-7qpDMUHI_4eABPsfvC8XgJv5qv0TrtzX79ZMY-f9w6mhDmjcw

Abla Hamilton

Senior UX Researcher, Material Design

mio-example

<p>As a UX researcher on the Material Design team, I run lots of research studies with designers and developers. More and more, I see Android developers try to use Large Language Models (LLM) tools as they learn about and use Material Design 3 components on Compose. When I see developers struggle to get helpful results from these powerful tools, I want to help.</p>
<p>How can I help? My first thought was that I wanted to change the information in the model itself, however, that is not really possible. So, I decided to take a look at general AI prompts that are used to get informational output from the model and how to expand the prompts specifically related to learning and using Material Design. These example prompts can be used by designers and developers!</p>
<p>I&rsquo;d recommend taking a look at the <a href="https://ai.google.dev/gemini-api/docs/prompting-strategies" target="_blank" rel="noopener">Prompt Best Practices</a>. I reviewed the prompt recommendations and considered use cases specific to using Material Design and user interface design and development process.</p>
<p>So, let&rsquo;s go over a few basic AI prompt writing best practices and show some Material Design specific examples.</p>
<p><em>Just a heads up: These prompts are suggestions for use with <a href="https://gemini.google.com/" target="_blank" rel="noopener">the Gemini app</a>. Your results may vary.</em></p>
<h2>1. Prompting with text and an image</h2>
<p><strong>Why It Matters</strong></p>
<p>Working on the user interface for an app or website, designers create a mockup to handoff to developers to reference during the coding and implementation phase.&nbsp; There are several different user experience (UX) aspects that designers and developers need to take into consideration such as:&nbsp; Portrait vs landscape orientation, light and dark mode, and any accessibility concerns, just for a start. You can use an image to determine which specific Material Design component aligns with patterns shown in the mockup.</p>
<p><strong>Example 1: Identify UX aspects based on a mockup</strong></p>
<p><strong>Prompt 1:</strong></p>
<p>Review this mockup showing a Tablet UI and show me all of the Material design 3 components I should use based on the mockup. Include portrait and landscape view considerations, include light and dark mode and any accessibility needs for the app. Then, show me Compose Kotlin code for this screen based on the descriptions generated.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p><strong>Gemini app output:</strong></p>
<p>Sure, I can review the mockup and discuss Material Design 3 components, portrait and landscape considerations, light and dark mode, and accessibility needs for the app. However, I can't generate the Compose Kotlin code for this specific screen since it requires knowledge of the app's functionalities and data structures which are not available from the image.</p>
<p><strong>Material Design 3 components in the mockup:</strong></p>
<ul>
<li><strong>Top app bar: </strong>The mockup uses a top app bar with the app name "Your Family Tree" centered. Material Design 3 recommends using large titles centered in the toolbar for tablet apps Material 3 design tokens.</li>
<li><strong>Navigation rail: </strong>The mockup uses a navigation rail on the left hand side of the screen with five destinations: "Home", "Tree View", "Map view", "Story view", and "History view". Material Design 3 recommends using navigation rails for applications with more than three destinations Material 3 navigation: <a href="https://material.io/components/navigation-rail/" target="_blank" rel="noopener">https://material.io/components/navigation-rail/</a>.</li>
<li><strong>Cards: </strong>The mockup uses cards to display information about the user's family tree. Material Design 3 uses cards to group and present information. Cards can be used with other UI components to create a variety of layouts Material 3 cards: <a href="https://material.io/components/cards" target="_blank" rel="noopener">https://material.io/components/cards</a><strong>.</strong></li>
<li><strong>Buttons: </strong>The mockup uses multiple buttons including an elevated button with the text "Add Person" and a text button with the text "Close". Material Design 3 offers different button types including text buttons and elevated buttons Material 3 buttons:<strong> </strong><a href="https://material.io/components/buttons" target="_blank" rel="noopener">https://material.io/components/buttons</a>.</li>
<li><strong>Text fields: </strong>The mockup shows a text field where the user can input their name. Material Design 3 offers a variety of text field styles including outlined text fields Material 3 text fields: <a href="https://material.io/components/text-fields" target="_blank" rel="noopener">https://material.io/components/text-fields</a>.</li>
</ul>
<p><strong>Portrait and Landscape view considerations:</strong></p>
<ul>
<li>In portrait view, the navigation rail can be displayed on the left side of the screen, taking advantage of the additional screen real estate of tablets.</li>
<li>In landscape view, you may consider using a bottom navigation bar instead of a navigation rail, as it may be more convenient for users to reach with their thumbs.</li>
</ul>
<p><strong>Light and dark mode:</strong></p>
<ul>
<li>Material Design 3 supports both light and dark themes. When switching between light and dark mode, you should ensure that there is sufficient color contrast between text and background colors to meet WCAG accessibility guidelines WCAG contrast checker:</li>
</ul>
<p><strong>Accessibility needs:</strong></p>
<ul>
<li>The app should use sufficient color contrast between text and background colors.</li>
<li>The app should use clear and concise language in the UI.</li>
<li>The app should be compatible with screen readers.</li>
</ul>
<p>I hope this helps! Let me know if you have any other questions.</p>
<p style="text-align: center;">✧</p>
<p><strong>Comments about the output:</strong></p>
<p>1. There is a tool that Android developers can use called the <a href="https://play.google.com/store/apps/details?id=com.google.android.apps.accessibility.auditor" target="_blank" rel="noopener">Accessibility Scanner app</a> that developers can use to check screens and will alert contrast issues.</p>
<p>2. Accessibility needs section is missing information on touch targets.</p>
<h2>2. Break down complex requests into multiple smaller prompts</h2>
<p><strong>Why It Matters</strong></p>
<p>Using easier-to-understand chunks or tasks will result in better output from the LLM. This allows you to iterate and focus on specific aspects of the model's output. It&rsquo;s almost like having a conversation.</p>
<p>After Example 1, I wanted to break down the one complex prompt into smaller chunks to compare the Gemini app output.</p>
<p><strong>Revised Prompt 1:</strong></p>
<p>Review this mockup showing a Tablet UI and show me all of the Material design 3 components I should use based on the mockup. Include portrait and landscape orientation considerations.</p>
<p><strong>Gemini app output:</strong></p>
<p>Based on the mockup you sent, here are the Material Design 3 components you can use:</p>
<p><strong>Top App Bar</strong></p>
<ul>
<li>A top app bar&nbsp; is used at the top of the screen and&nbsp; contains the app title&nbsp; and&nbsp; other actions, such as a search bar or&nbsp; avatar.&nbsp; In the portrait view, you can use the app title and a&nbsp; close button. In landscape orientation, you can include additional actions such as&nbsp; Search&nbsp; and&nbsp; Contact Us.</li>
<li>Material Design 3 recommends using a large font for the title on tablets&nbsp; <a href="https://m3.material.io/components/top-app-bar" target="_blank" rel="noopener">https://m3.material.io/components/top-app-bar</a>.</li>
</ul>
<p><strong>Navigation</strong></p>
<ul>
<li><strong>Navigation drawer</strong>:&nbsp; A navigation drawer&nbsp; is a panel that slides in from the left or right side of the screen.&nbsp; This is a good option for portrait&nbsp; as it&nbsp; efficiently uses screen space. Material Design 3 recommends using a top app bar&nbsp; alongside a navigation drawer in tablet apps <a href="https://m3.material.io/components/navigation-drawer/specs" target="_blank" rel="noopener">https://m3.material.io/components/navigation-drawer/specs</a>.</li>
<li><strong>Tabs</strong>:&nbsp; You can use tabs&nbsp; in landscape mode to organize content across different screens and views. Tabs are a good way to&nbsp; improve the&nbsp; discoverability of&nbsp; different functions&nbsp; within the app <a href="https://m3.material.io/components/tabs/guidelines" target="_blank" rel="noopener">https://m3.material.io/components/tabs/guidelines</a>.</li>
</ul>
<p><strong>Content</strong></p>
<ul>
<li><strong>Cards</strong>: You can use cards to display&nbsp; information&nbsp; like&nbsp; "John Scott" and "History view". Cards&nbsp; elevate content priority and&nbsp; bring focus to specific elements of your app <a href="https://m3.material.io/components/cards/" target="_blank" rel="noopener">https://m3.material.io/components/cards/</a>.</li>
<li><strong>Buttons</strong>:&nbsp; Different&nbsp; types of buttons&nbsp; can be used throughout the app&nbsp; depending on their function.&nbsp; In the mockup, you have a text button that says "Close" and&nbsp; a floating action button (FAB)&nbsp; with a plus sign (+) which&nbsp; could be used to create a new family member entry. Material Design 3&nbsp; offers various button options including&nbsp; text buttons, outlined buttons,&nbsp; and&nbsp; contained buttons <a href="https://m3.material.io/components/buttons/" target="_blank" rel="noopener">https://m3.material.io/components/buttons/</a>.</li>
<li><strong>Typography</strong>: Material Design 3 emphasizes&nbsp; using a strong typographical hierarchy&nbsp; to&nbsp; improve the readability of&nbsp; your app. Use a combination of&nbsp; headings, subheadings and body text&nbsp; to&nbsp; structure&nbsp; your content <a href="https://m3.material.io/styles/typography" target="_blank" rel="noopener">https://m3.material.io/styles/typography</a>.</li>
</ul>
<p><strong>Responsive Design Considerations</strong></p>
<ul>
<li>Material Design 3 promotes responsive design which means your app layout should adapt to different screen sizes and orientations. In this mockup, the content can be stacked on top of each other in portrait mode and laid out side by side in landscape mode.</li>
</ul>
<p>I hope this helps!</p>
<p style="text-align: center;">✧</p>
<p><strong>Revised Prompt 2:</strong></p>
<p>What are any accessibility needs for this screen, including light and dark mode?</p>
<p><strong>Gemini app output:</strong></p>
<p>Here are some accessibility needs for the tablet UI screen you're designing, considering both light and dark mode:</p>
<p><strong>Color Contrast</strong>:</p>
<ul>
<li>Ensure a <strong>high color contrast ratio</strong> between text and background elements in both light and dark mode. This is crucial for users with visual impairments.&nbsp; Use a contrast checker tool to verify your choices meet WCAG (Web Content Accessibility Guidelines) standards</li>
<li><strong>Avoid relying solely on color</strong> to differentiate information. Use <strong>text labels</strong> in addition to color-coded elements.</li>
</ul>
<p><strong>Text Size and Readability</strong>:</p>
<ul>
<li>Use a <strong>large enough font size</strong> for body text and headings, especially on tablets.</li>
<li>Choose a <strong>clear and easy-to-read font</strong> that works well in different sizes.</li>
</ul>
<p><strong>Light and Dark Mode Consistency</strong>:</p>
<ul>
<li>Make sure the <strong>information hierarchy</strong> and <strong>visual elements</strong> remain consistent across both light and dark modes. Users shouldn't be confused by drastic changes in layout or functionality when switching modes.</li>
<li>Use <strong>appropriate color adjustments</strong> for icons and other visual elements to maintain clarity in both light and dark themes.</li>
</ul>
<p><strong>Additional Considerations</strong>:</p>
<ul>
<li><strong>Focus indicators</strong>: Clearly indicate which element has focus when using the keyboard to navigate the app. This helps users with motor impairments or those who rely on screen readers.</li>
<li><strong>Alternative text (alt text)</strong>: Provide alt text descriptions for images to convey their meaning to screen reader users.</li>
<li><strong>Touch targets</strong>: Make sure buttons and other interactive elements have a large enough touch target size for users with motor impairments.</li>
</ul>
<p>By considering these accessibility needs, you can create a tablet UI that's usable and comfortable for everyone, regardless of their visual abilities or how they choose to interact with the app.</p>
<p style="text-align: center;">✧</p>
<p><strong>Comments about the output:</strong></p>
<p>Comparing the outputs from the two revised prompts in Example 2, the model did provide a bit more detail about accessibility. This is something to consider when writing your prompts is adding the right level of context without trying to add all questions at one time.</p>
<h2>3. Provide contextual information</h2>
<p>Providing context helps the model understand in more detail what you're asking for. Here are some suggestions of contextual information specific to Compose Material 3 to include in your prompts.</p>
<ul>
<li>m3.material.io</li>
<li>Material Design 3</li>
<li>Compose Material</li>
<li>Jetpack Compose</li>
<li>Kotlin</li>
<li>New to Compose Material</li>
</ul>
<p><strong>Why It Matters</strong></p>
<p>While using the name &ldquo;Material Design&rdquo;&nbsp; aligns with&nbsp; our design guidance and code samples, we are now on our third version. Using just that &ldquo;Material Design&rdquo; name may not be enough for the prompt. Design guidance is agnostic and&nbsp; we do have code examples for different programming languages, such as Java-Views, Kotlin, Flutter and Compose. Vague prompts might lead to incorrect information or code for your project.</p>
<p>Plus, by including your knowledge level, such as &ldquo;new to Material Compose,&rdquo; you ensure more learning-focused content.</p>
<p>Example prompts with contextual information in bold:</p>
<ol>
<li>What is the migration effort for a <strong>Compose app</strong> from <strong>Material Design 2</strong> to <strong>Material Design 3</strong>?</li>
<li>Using <strong>m3.material.io</strong>, show me <strong>Kotlin</strong> code for a <strong>Jetpack Compose</strong> app where the theme has the primary color = #1e555c and the secondary color = #f4d8cd. font = roboto. I am <strong>new to Compose Material 3</strong>.</li>
</ol>
<p>Another suggestion is that you use any generated code as a starting point. Any code generated may need adjustments.</p>
<p><a href="https://gemini.google.com/corp/faq#coding" target="_blank" rel="noopener">FAQ: Can Gemini help with coding?</a></p>
<p>Yes, Gemini can help with coding and topics about coding, but you are responsible for</p>
<p>your use of code or coding explanations. So you should use discretion and carefully test and review all code for errors, bugs, and vulnerabilities before relying on it.&rdquo;&nbsp; Source: <a href="https://gemini.google.com/faq#coding" target="_blank" rel="noopener">https://gemini.google.com/faq#coding</a></p>
<p style="text-align: center;">✧</p>
<p>These LLM tools are still evolving and for our example use cases, I expect to see improvements in the future.</p>
<p>Over on Material Design, we&rsquo;re incredibly excited to see how we can use Gemini in different ways&nbsp; to help designers and developers learn and implement our system for their Android apps.</p>
<p>Thanks to Shalom Gibly, Nikita Singh, Mark McDonald, Liam Spradlin, Barbara Eldredge,&nbsp; Lorie Napolitano and Frank Bentley for their contributions to this article!</p>

Android mockup

Uploaded mockup

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/81a478447d6399e34f877a48a7851d7eec9574ccfa3308f59136bcf580fae68b636f3c2f736428a421a0bcb50faa737fdccdb9b2bcb7b61b7f427cdd09e39956

https://lh3.googleusercontent.com/HSSMuL9CDG3tJeHLhaClmW-SgTVZtAdPTtSIsqlfujD2HqU2wb-e3sQKpskYrAtAbORmlUiZ9i1jsb-AcPEa5GBYHb8Nl6SbhcxVHyMbDowO617w9RsL

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/791217e0cf735da1955f4f146994a4e0850cc57f2bbbccb99f1571dbb53b50dbad7e5b85822d51f9a50b8f4a8e81e5689a0ab6c44261245dc751db619c9ef48b

https://lh3.googleusercontent.com/_GAV0tea_Vg-fwl92xjOoBHoZDyxl01gNGKMZJdDgPBkEIfJfkjvDGgLRmIQhDXkRyh3vfhhkznA7Zx74IFqADVf1nQoSAa59JWy3o3LyTUGs0gGLO4

gemini ai code compose material how-to

{}

Learn how to create a stunning Gemini app using compose and Material Design 3.  Example prompts for designers and developers.

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/4e0d4469a0e844b6129569301bd426a967b9611875cb8ce81fca075c94d8f0fbf5d5ff7cb7e3a796f3f210e05e1970c593e4b5efb0eca24692bde37745d52a78

https://lh3.googleusercontent.com/cU5iH38YKVhTCyZF7LPn6NwqhFUep51LDSPnzT2_4OYlCI4O6l88lhcUFuzdboxXaammWlgg_BvrnZyv6FQfp11mC33DvuLNfoduud-sGnZBXGg9UA

Using the Gemini app with Material Design 3

2024-05-07T13:00:00

how-to-gemini-app-compose-material-design-3

Example prompts for designers and developers

Using the Gemini app with Material Design 3

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/7abbcfa5ee839d89879701fe8793fabcad6eee0d7b68804464e58dac78821eb2ecb9bdbb8a82972a40f056b867e966897618f36d6d63631b200146b59b8a1d56

https://lh3.googleusercontent.com/khMx4Ahoh9hQi-mXDDhKmK_kRoE0qpYj5dBATOTBKjsCRVJD3cz8UQ4bkTaAZxHuGvjlrGs0WssQzu_icP75PIlmwLuqgxVrBrXkZw7JysAOpZ9D_2a1

/blog/material-3-compose-1-1

Material Blog

Material Design 3 for Compose gets new components and features

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/92b74c588c798a7dc073ec8a25c9d4b57d893d91ed8284b17156e8a66bd0dcf8029eb73d3a028cb39c7dd9a4841562129e26cc9f1ff3aca5f1a4d02d5158acd4

https://lh3.googleusercontent.com/x_K1JvFXtoygMlLkLipXY-ByXw2JNmH2Jy3RHJsAoZ1am7lG9da_69cLGg_VcRYQUYgWqyjG3sGPDLEvsMS5d1yXrVLeK6L4yOXce-gb6OACQd_u2EmM

/blog/how-to-make-text-more-accessible

How to make your text more accessible

Material Blog

How to make your text more accessible

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/bce055b0ea8ebae5049b0f2ebd5489ea36bf2ce4133c7d1c4d7e93c033b71dc716ab99ba8cf4f4ed8136841f1eaf75c7d757d299a20af2c82a69a4f1362ccb0e

https://lh3.googleusercontent.com/RbHShPvohW9p32Ep0kbI_56p-2tXwOP39xcwIGHjjatuYPO0h5t_kmbK0uIcGNTBb6QLBmJUhJbALaQhZ3u5AtVv9r9E6bP2KS6APUfjUKm_33n3SZI

/blog/material-theme-builder-2-color-match

Material Blog

An updated theming experience with Material Theme Builder 2.0

mio-example
