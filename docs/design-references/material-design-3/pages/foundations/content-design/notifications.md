# Notifications

Source: https://m3.material.io/foundations/content-design/notifications
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/844999f2-e85f-4f25-bca4-6fb422a3853d.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Notifications help people see information they need or want at the right time

## Tab 1

<p><span style="white-space:pre-wrap" id="isPasted">Notifications should:</span></p><ul><li><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Be about the user, not the product</span></span></li><li><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Be precise, timely, actionable, contextual, and relevant</span></span></span></li><li><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted"><span style="white-space:pre-wrap" id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Give users easy controls to opt out</span></span></span></span></li><li><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted"><span style="white-space:pre-wrap" id="isPasted"><span style="white-space:pre-wrap" id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Not be used to send unsolicited ads</span></span></span></span></span></li></ul>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53k6lt-1.png?alt=media

<h3 id="isPasted"><span style="white-space:pre-wrap">Put important information at the top</span></h3><p><span style="white-space:pre-wrap" id="isPasted">Put the most important info at the beginning and make it easy to understand. People skim rather than read, often in an F shape. When it makes sense, try to move the most critical information to the front of sentences, rather than the end, where it may get overlooked or truncated.</span></p>

Three notifications from Google apps that include the point of the notification in the header.

<p><span style="white-space:pre-wrap">Prioritize the most important information</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53kfhk-2.png?alt=media

Three notifications from Google apps that include app names repeated in the header, instead of important information.

<p><span style="white-space:pre-wrap">Don't waste characters on app names, niceties, or unimportant information</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53kk0k-3.png?alt=media

<h3 id="isPasted"><span style="white-space:pre-wrap">Tell users what they can do</span></h3><p><span style="white-space:pre-wrap" id="isPasted">If you’re prompting someone to take action, make that clear. CTAs should be concise, specific, and actionable. If you know what motivates people to take action, add it. <br /></span></p>

Two notifications from Google maps that include actionable information in the header.

<p id="isPasted"><span style="white-space:pre-wrap">Clearly guide the user to their next action</span></p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53kq5j-4.png?alt=media

Two notifications from Google apps with non-actionable headers.

<p><span style="white-space:pre-wrap">Don't bury next steps</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53kvqx-5.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Make it relevant and personal</span></h3><p><span style="white-space:pre-wrap" id="isPasted">A notification shouldn’t be sent to everyone. The more you broaden the audience and the message for a notification, the more you risk being irrelevant. Consider user segments, in-app behavior, and personalized information to make sure notifications go to people who will benefit most from them.</span></p>

A Google maps notification in Memphis, TN that’s personalized to the user’s location downtown.

<p><span style="white-space:pre-wrap">Be specific to capture user attention</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53l2ot-6.png?alt=media

A Google maps notification in Memphis, TN that’s generic to the city, rather than the area.

<p><span style="white-space:pre-wrap">Don’t be so generic as to lose value</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53l86v-7.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Avoid dynamic text</span></h3><p><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Dynamic text are words that are implemented by engineering to change based on the user or context, like adding a user’s campaign name to headline or “good afternoon” when users log in at certain times.<br /><br />Try not to use dynamic text in notifications. It often breaks character limits, especially in headlines when translated. Text that gets truncated in the headline will not expand, even in expandable notifications. If you must use dynamic text in the headline, try to pair it with no more than one additional word. Create a backup notification that fits the character count when your primary notification won’t. </span></span></p>

Two notifications, one with dynamic text in the body, and the other with dynamic text in the header that’s formatted to always be short.

<p><span style="white-space:pre-wrap">Place dynamic text in the notification body, where there is more space. If you place dynamic text in the title, keep it very short.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53lep9-8.png?alt=media

Two notifications with dynamic text in the header that’s too long and truncates.

<p><span style="white-space:pre-wrap">Don’t place dynamic text in a long notification title</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53lk9g-9.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Mind your characters</span></h3><p><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Stay within these suggested character counts so text doesn’t get cut off:</span></span></p><ul><li><span><span style="white-space:pre-wrap">Title: &lt;29 chars</span></span></li><li><span><span style="white-space:pre-wrap">Collapsed body: &lt;40 chars</span></span></li><li><span><span style="white-space:pre-wrap">Expanded  body: &lt;80 chars; start with collapsed body and add to it</span></span></li><li><span><span style="white-space:pre-wrap">Button: 1-2 buttons (1-2 words each)</span></span></li></ul><p><span><span style="white-space:pre-wrap"><br />There’s more room for text on later versions of Android, but these limits are still recommended to prevent truncation on smaller devices.</span></span></p>

A short, relevant, and informative notification.

<p><span style="white-space:pre-wrap">Keep notifications short and information-dense</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53ls3l-10.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">SMS messages</span></h3><p><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">SMS helps users get messages when they might not have access to their Google Account. It’s used for important or urgent communication only. <br /><br />SMS breaks into multiple messages after a certain number of characters, resulting in increased costs. To avoid this, stick to the following character limits:</span></span></p><ul><li><span><span style="white-space:pre-wrap">Latin languages:  &lt;160 characters</span></span></li><li><span><span style="white-space:pre-wrap">Non-latin languages: &lt;134 characters</span></span></li></ul><p><span><span style="white-space:pre-wrap"><br />If translation is needed, let translators know about the character limits in the message description. </span></span></p>

An SMS notification that’s brief and truncates sensitive information.

<p><span style="white-space:pre-wrap">SMS messages should be brief and important</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53lzfr-11.png?alt=media

An SMS notification that’s too long with too many links.

<p><span style="white-space:pre-wrap">Don’t use full emails or website links for text length</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53m528-12.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Emoji with caution</span></h3><p><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Use emoji sparingly. Many don’t translate and aren’t universally understood across cultures. </span></span><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Experiments</span></span><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted"> show that face and hand gesture emoji perform better than generic emoji because they tell a better story. Emoji should enhance content, not replace it.<br /><br />Since it’s not clear to users whether emoji mean we’re sympathizing with them or attempting to project our feelings onto them, don’t use emoji to accentuate bad news. In experiments, there was a strong negative reaction to negative emoji, such as frowning face, anguished face, and weary face.<br /><br />Gen Z adds another cultural nuance to emoji by </span></span><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted"><a href="https://www.textnow.com/blog/the-next-generation-of-emojis-gen-z-explained/" target="_blank" rel="noopener noreferrer">inventing new meanings</a></span></span><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted"> that go beyond the official or literal </span></span><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted"><a href="https://emojipedia.org/" target="_blank" rel="noopener noreferrer">definitions</a></span></span><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">.</span></span></p>

A notification about coffee with a coffee emoji at the end of the header.

<p><span style="white-space:pre-wrap">Use emoji only to enhance a message</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53mcby-13.png?alt=media

A notification about high traffic volume on a route to work that uses upset emoji. A notification about coffee that substitutes a coffee emoji for the word “coffee.”

<p><span style="white-space:pre-wrap">Don’t add negative emotions to a message. Don’t replace words with emoji.</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53mhmr-14.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Don’t overdo delight</span></h3><p><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">What seems funny or cute may not come across that way. When vying for limited user attention, be useful. Don’t focus on delight: delicately added and tested polish can better support Google’s brand.</span></span></p>

A notification that’s short and effective

<p id="isPasted"><span style="white-space:pre-wrap">Prioritize straightforward and useful messages</span></p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53mqhm-15.png?alt=media

A notification that’s meant to be funny, but comes across as creepy where the application calls the user “human.”

<p><span style="white-space:pre-wrap">Jokes aren’t appropriate for notifications</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53mx58-16.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Be day-specific</span></h3><p><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Use the days of the week. Don’t use “today,” “tomorrow,” “tonight,” or similar words. About 20% of users don’t see notifications on the day they’re sent, so “tomorrow” might be read when it’s “today” for the user.<br /><br />An exception is when a notification auto-dismisses at a specific timestamp.</span></span></p>

<p><span style="white-space:pre-wrap">Specify the day of the week so that it makes sense if someone reads it the following day</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53n553-17.png?alt=media

<p><span style="white-space:pre-wrap">Don’t use relative terms like “today” or “tomorrow”</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53nb80-18.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Don’t interrupt the flow</span></h3><p><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">If you have notifications or emails related to the onboarding process, make sure they don’t trigger during onboarding.</span></span></p>

<p><span style="white-space:pre-wrap">Don't prompt the user with a notification or email that might interrupt an important moment</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53nkf2-19.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Don’t name the product (again)</span></h3><p><span style="white-space:pre-wrap">An app’s name or logo is already included in a notification’s design. Use the limited space for other information.</span></p>

<p><span style="white-space:pre-wrap">Use the available space for useful information</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53ntem-20.png?alt=media

<p><span style="white-space:pre-wrap">Don’t waste space repeating information that is already included by the OS</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53nz6w-21.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Opting in and out</span></h3><p><span id="isPasted"><span style="white-space:pre-wrap" id="isPasted">Give users a way to opt-out of notifications in context. If you don’t, they’ll have to dig into settings and may get frustrated. If you do offer opt-outs or opt-ins, make it clear what benefit the user is getting or losing.</span></span></p>

<p><span style="white-space:pre-wrap">Make it easy for users to start or stop receiving notifications</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flw53o6jr-22.png?alt=media
