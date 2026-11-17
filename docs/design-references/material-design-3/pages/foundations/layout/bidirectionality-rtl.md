# Bidirectionality &amp; RTL

Source: https://m3.material.io/foundations/layout/bidirectionality-rtl
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/35f8449d-9b29-4224-95ac-65a0708c8722.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Design products that adapt to languages that read right-to-left (RTL)

## Tab 1

<p><a href="https://www.w3.org/International/questions/qa-scripts.en.html" target="_blank">Over 2 billion people</a> read and write in right-to-left (RTL) languages like Arabic, Hebrew, Farsi, and Urdu. Layouts should support both left-to-right (LTR) and RTL languages through mirroring and other best practices to ensure content is easy for global audiences to understand and navigate. Consider the holistic experience including <a href="/m3/pages/global-writing/overview" target="_self">global writing</a>, localizing voice and <a href="/m3/pages/icons/designing-icons#5f0e344b-17f8-4b91-b0e4-45671b9900f4" target="_self">design principles for culturally appropriate icons</a>.</p><p>Material's components are built to support RTL, such as naming elements and tokens as "leading" and "trailing." However, extra configuration may be needed to achieve specific RTL situations.</p>

<h2>Mirroring</h2>

<p>When a layout is changed from LTR to RTL (or vice-versa), or flipped horizontally, it’s often called mirroring. UI elements and text that typically appear on the left in LTR aligns to the right. Reading flow starts from the top right corner, instead of the top left.</p><p>Not all elements mirror with RTL languages. For example, graphs and charts maintain a LTR directionality for Persian and Urdu. </p>

Layout in LTR and mirrored for RTL language.

<p>A mirrored layout in an RTL language reverses the alignment and ordering of elements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsftouf7-01.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/7bXPlBNYMf6eu5JeDb4znscEjXxoaiFtisaLzKCORSaxEZXYMj2NCoh96x0V6Wk-gFKp6SIYCEwmRBuWgKQldV24NNlKgP7d7gzBXJjiulk=s2704

<h2>Text rendering</h2>

<p>Correct text rendering is foundational for a great user experience, and it’s critical for readability and usability. Text rendering has two parts:</p><ol class="decimal"><li><p>Alignment: How the edges of the text box are placed alongside other elements</p></li><li><p>Directionality: How text and other elements flow within a text box, like left-to-right or right-to-left</p></li></ol><p>In RTL languages, text is usually right-aligned, and elements flow from right-to-left.</p><p>Common issues with RTL language rendering are text entry, cursor position, punctuation, phone numbers, and URLs.</p><p>Improperly rendering text in RTL languages can create cognitive overload and negatively impact user sentiment and trust.</p>

Text field incorrectly displaying the word order of an email address and cursor placement.

<p>Don't reverse the order of the email username and domain (@google.com). The domain should always be to the right of the username. Usernames can still be written RTL, with the cursor moving to the left.</p><p>Note: This example isn’t translated to illustrate a common issue with text rendering.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsftq4kx-02-dont.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/JVlDFjXgPxdC_zdlgXhCZp49ZeyjAiDRVsACglR2IUEhVHPkJA_PlIndveJatddV_T_zwlTWN_IN5nKkI1Hs3pz6VqtL-_9Ir2tid-1vOzc=s1312

Dialog window incorrectly displaying word order decreasing readability.

<p>Don’t apply LTR directionality to RTL content, because it may scramble word order. To ensure readability across all languages, the content should have both RTL alignment and directionality.</p><p>Note: This example isn’t translated to illustrate a common issue with text rendering.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsftrw89-03-dont.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/3-tex9271iuyBH7y1kYRePlY5qW2WEXDag00pyBIZR1qPfwVL_sOjVMK1XbF-5cuFVZxw8_Ubf7_1jF3gtB6HZKZH7Mjgj-XEU32nVYJfj9v=s1312

<h2>Icons &amp; symbols</h2>

<p>In RTL languages, directional UI icons, like back and forward, should be mirrored. However, in Hebrew, timelines and media controls on a page should retain left-to-right directionality.</p><p>The meaning of icons and symbols can vary significantly across cultures. For additional guidance, refer to <a href="/m3/pages/icons/designing-icons#5f0e344b-17f8-4b91-b0e4-45671b9900f4" target="_self">design principles for icons</a>.</p>

Back and forward icons in LTR and RTL.

<p>Back and foward icons are mirrored in RTL</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsftt2b2-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/GvIIi9efFFifgSytQkM_LydZ9nagyoByO85kHfVyJHacgAAmCSEJfCUkJq69A4m4emhH0Icajp8dCaO61qfMg21QJC-VVjI8hdr1hD5OWpPu2Q=s1312

Send and question mark icons in LTR and RTL.

<p>Send buttons are mirrored in RTL. Help icons are mirrored in some RTL languages, like Urdu and Persian.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsftts4z-05.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/lV7W9uPzT_HnFVhfZXBOhEO-XmWh6ZyboXsV3lO2ieRQJOGrdI7rhGG_ukjK0iqnZ10P5DBGLwMniRh3faP4fiUj524hRHVdFRLurxr5oC8g=s1312

<h2>Time</h2>

<p>Linear representations of time are often mirrored in RTL language experiences. </p><p>Linear progress indicators should move from right to left for most RTL languages, except Hebrew where it should remain LTR.</p><p>Circular representations of time remain the same.</p>

RTL linear progress indicator filling from right to left and circular progress indicator filling clockwise.

<ol class="decimal"><li><p>RTL linear progress indicator starts to fill progress from the right </p></li><li><p>Circular progress indicators move clockwise</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsftutz2-06.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/g91ADNfx-kybwW9djnX_Bg0UgVl-GDlqK0oTZLyZx2K_TriXig4XZlZZMbo8eCE2gFNudXJg4N-WzHr--RBJoM-sBWZ-qbB9-nQuNX7X7T4=s1352

<h3>Media players</h3><p>Media controls for video or audio players are always LTR.</p>

Media player with control and progress in LTR and all other content is RTL.

<p>In Urdu, controls and progress for media and a podcast title are shown in LTR, while all other content is RTL</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfu1nlp-07.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/s6HIEi9IqqJ1FCd5-qqE4UXx8fyPymG4ac6GBJP--4aCUkk-1USxO5X5nojks0V99BBMsENc11m0-N6CzFWppLEeLF-Jk7I1QFNTN1n2QoU=s1352

<h3>Clocks</h3><p>For RTL languages, the directionality of time remains LTR, and clocks still turn clockwise. However, the AM/PM symbols for 12h clocks should be placed to the left. The 24-hour clock is often used in countries where the primary language isn’t English.</p><p>Clock icons, circular refresh icons, and progress indicators with arrows pointing clockwise shouldn’t be mirrored.</p>

24-hour clock in RTL.

<p>24-hour clocks in RTL move clockwise, but mirror elements such as buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfu311j-08.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Wq16Adx940iD1dbLpZPHmNzXEXT4qYJALgLTyECNIPsEjGJvmakDWq3d2TKe4ui1OGnX41Dx7wX-w2O1uWrn_6Tw5M-Gl_KZA5WRn9cCNJcsBw=s1312

12-hour clock in RTL.

<p>12-hour clocks in RTL move clockwise, but mirror UI elements such as AM/PM and buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfu4524-09.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/4UhQyg-neULcpAl8ueDg_qS_DmeIbWoMGfFrQFz-z6ePNZWCpGmLlfc0yFm_zJ2EXv84t2sMOBTWmc0oGl7wnjVVV6j6f_yRrktLGC8_TOXx=s1312

<h2>Canonical layout examples</h2>

<h3>List-detail</h3><p>The <a href="/m3/pages/canonical-examples/list-detail" target="_blank">list-detail layout</a>:</p><ul><li><p>Is a single-pane at compact <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element>, switching between list and detail views</p></li><li><p>Divides the window into two side-by-side panes on large screens</p></li><li><p>Is mirrored in RTL</p></li></ul>

RTL list layout on mobile.

<p>List-detail mirrored for RTL, where text and other elements are aligned to the right and flow from right to left</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfu5hg5-10.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/HKDWDsXNp_CJb84ZQEHNwuu-0oxpPLppPnaJ3o--ObAB4yVeU2kgQWlDryzjDuSgN9aOEaJD_NHPbwA_8bOpkC5oaK_stNeM3ZVLowOFeqGt=s1352

<h3>Feed</h3><p>Use a <a href="/m3/pages/canonical-examples/feed" target="_blank">feed layout</a> to arrange content elements like cards in a configurable grid for quick, convenient viewing of a large amount of content. The feed layout is mirrored in RTL.</p>

RTL feed layout.

<p>Feed layout mirrored for RTL, where the order of text, grid, and other elements align to the right and flow from right to left</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfu84eb-11.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/JhU530pRqL1O4OoAUKD8KzfKbTWTZ0ppUOZj3oKpLcg2kuBaZUjR9mu465H24RkNMdV11EITG38Q_OJc7vS9HkYGlgh20wMmZLzRjV8imQCp=s1352

<h3>Supporting pane</h3><p>Use the <a href="/m3/pages/canonical-examples/supporting-pane" target="_blank">supporting pane layout</a> to organize content into primary and secondary display areas. The supporting pane layout is mirrored in RTL.</p>

RTL supporting pane in an RTL language.

<p>Supporting pane to the left of the primary content. Text and other elements within the pane are aligned to the right and flow from right to left.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfu93jo-12.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/NhwHSdtr5w_V2xLINEl8iHRTubLt8Y07M7LPH-I6FMVLPYpJAhWHJcUqv6svxL1sxdFjcj4Uu7q5l-qFBg9bafWTETDibDawcayYJnhRkZI=s1352

<h2>Component examples</h2>

<h3>Badges</h3><p>Change the position and alignment of <a href="/m3/pages/badges/overview" target="_self">badges</a> for RTL languages.</p>

Small badge on the top left of a folder icon.

<p>Small badge appears on the top left of the icon</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfuadi8-13.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/tLzukatL9UErk2NIb17_gZki0BAQ-Zuopc4FaP9-rWXW2EMerWK-zxDClC9eQzQEq5BGsFjRkUU1aqQwb7tkHlTL3YUjEHcYpRdrWC1XBuo=s656

Large badge on the top left of an image icon.

<p>Large badge appears on the top left of the icon</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfub9sg-14.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/N8FZIDMnkJ3weBDFn0JAV59SMdEjVb2CarDw0rvc-1HcelsLX67gFgp84kK3CfoVJuVrofnOUAPTcOHjh6sdO9KYSRaS-hod0IbgDwF49WZ2=s656

<h3>Toolbars</h3><p><a href="/m3/pages/toolbars/overview" target="_self">Toolbars</a> provide actions related to the current page. For RTL languages, mirror the order of the tools.</p>

RTL floating toolbar. 

<p>Mirrored floating toolbar, where the FAB appears on the left </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfucmb1-15.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/uUGwZbEfNTrxp-8LV3l6MoSn0mUU_zOoFFHZQTIMgOlcTJiaW4Kh9MVk_0dgRy1CQWJDVHncwlYRPfVHUlKccJmsf_GIS1Hj2baYBV9iwX41=s1352

<h3>App bars</h3><p><a href="/m3/pages/app-bars/overview" target="_self">App bars</a> are placed at the top of the screen to help people navigate through a product:</p><ul><li><p>Mirror an app bar’s layout in RTL</p></li><li><p>Flip appropriate icons, such as arrows</p></li></ul>

4 app bars in RTL.

<ol class="decimal"><li><p>RTL center-aligned, small app bars </p></li><li><p>RTL medium, flexible app bar </p></li><li><p>RTL large, flexible app bar</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfue0zv-16.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/mpn0hTVDPqfH-Bp9h3FZB4UuqaSuWelq_XMeIUfdhVztf7JYwTektgf-TAlKdl7LZlRm_lP7ZmbFf_4iE1MaXFqguYKi-bNXrbXtVMl_TwgZsA=s1352

<h3>Navigation rail</h3><p>The <a href="/m3/pages/navigation-rail/overview" target="_self">navigation rail</a> is placed on the leading edge of the screen, on the left side for LTR, and on the right for RTL.</p>

Nav rail on the right side for an RTL language, and left side for LTR.

<p>Based on the language, a navigation rail is set on a screen’s leading edge:</p><ul><li><p>Right side for RTL languages</p></li><li><p>Left side for LTR languages</p></li></ul>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfufptj-18.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/1U-nHFdJxzu17VrF15b_140InoPHof7BeklNesALpU-DvyXkM8f7bP-t0gNVhC_NykZAGJhX315jpc8sS3dhiaFlnPegKYa2OKgOQCgqlMQ=s1352

<h3>Expanded navigation rail</h3><p>Expanded navigation rails that open from the side are always placed on the leading edge of the screen, on the left for LTR languages, and on the right for RTL.</p>

RTL expanded navigation rail, including mirrored icons.

<p>RTL expanded navigation rails open from the leading edge and should include mirrored icons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfugr2m-17.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/OcbxhQe0dc56YbktUpDHooMEAagt7sqqVp4e58ShtGfStoesFg0yUvuOJzMLoNAXe0Pt51oapqytgAqZzere5V559HKL02hyotzh7qN2BDg=s1352

<h3>Text fields</h3><p>Icons in <a href="/m3/pages/text-fields/guidelines#5c8a5f07-b1a5-455f-bf76-7ff0d724f6b0" target="_self">text fields</a> are optional. Leading and trailing icons change their position based on LTR or RTL contexts.</p>

Text fields in RTL with leading and trailing icons.

<p>Icons, symbols, and label text for RTL: </p><ol class="decimal"><li><p>Icon signifier </p></li><li><p>Valid or error icon </p></li><li><p>Clear icon </p></li><li><p>Voice input icon </p></li><li><p>Dropdown icon </p></li><li><p>Image</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfuhyps-19.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ZpQXQ588tQws77tpIHt4DazARMZVa-25ZbMGhT39qqfrD_LSARVYeC5QNZPWbE2M9K2O7OX2eDigXF-x1VtIDTs4a0fGtEZShUa6Cz3ROMwH=s1352

<h3>Chips</h3><p>The leading icon of input chips can be an icon, logo, or circular image.</p><p>The trailing icon is always aligned to the end side of the container. It’s placed on the right for LTR and on the left for RTL.</p>

Filter chips with checkmark icons in RTL layout.

<p>Filter chips shown in an RTL layout. Note: This example is not translated to help illustrate mirroring.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfuiwrg-20.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Mu7Bv9--8PIV0Ipxqn8cVeyO1Jb0SjSGgRw96abLHus4DhJ1bY56xeaT_P32YRxa12piY8d7EaAtKSvw4HjHlkwoWd2a-bXF_p5ZkBiTGWjt=s1352

<h2>Swipe gestures</h2>

<p>Gestures are the ways people interact with UI elements using touch or body motion.</p><p>People can navigate horizontally between peer views like tabs and to complete actions. </p><p>RTL swiping and gestures should mirror their counterparts in LTR. If a product includes a delete icon revealed when swiped from the right for LTR languages, the same should be possible on the left for RTL languages. </p>

RTL list layout with swipe gesture revealing additional actions.

<p>Swiping reveals additional action in RTL list layout</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmsfumeds-21.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Cj3dR33eshqEQLZi7uUpXo6GIWl5Gqyjy1jXiuN4gba27J7z7Y9BF99mwyqnDjzmYsk2vuDrF1gunUgtN4VW8kYL7bB5466Itb2kbgVNINk=s1352

<p>On Android, <a href="https://github.com/material-components/material-components-android/blob/master/docs/foundations/PredictiveBack.md" target="_blank">predictive back</a> allows people to swipe left or right on the screen to go back or dismiss modal components.</p><p>RTL predictive back features should mirror those found in a LTR context.</p>

Back swipe for RTL languages. The back swipe on a bottom sheet takes person back to previous screen of a photo feed.

<p>The predictive back gesture should adjust for RTL languages</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmp3l3v9p-GM3_Bidirectionality_Interaction%20Gestures_6_IA_v02.mp4?alt=media
