# Time pickers

Source: https://m3.material.io/components/time-pickers
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/ec8e6da4-b726-403d-bab7-3fb660b6ef86.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul type="disc" style="list-style-type:disc"><li><p>Time pickers can be placed on a page, embedded directly within <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">lists</app-froala-tooltip-element> and sheets, or presented as modals</p></li><li><p>Use <strong>scroll pickers</strong> inline, <strong>dial pickers</strong> in a modal, and have an option to swap these to <strong>input pickers</strong> for text input</p></li><li><p>Can adapt to 12-hour and 24-hour time, horizontal or vertical orientations</p></li><li><p>Only use for selecting hours and minutes</p></li><li><p>Make sure time can easily be selected on a mobile device</p></li></ul>

A scroll time picker, with the ability to select day of the week, next to a 12-hour dial time picker.

<p>Time selection can be paired with day of the week and accessed through multiple inputs</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmugz32pr-01.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/5cae57e703105f6a

libraryModuleType: STATUS_TABLE

<h2>M3 Expressive update</h2>

<p>The expressive update added the scroll time picker variant, updated shapes, and updated color styling to all variants. <a href="https://m3.material.io/blog/building-with-m3-expressive" target="_blank">More on M3 Expressive</a></p>

<div class="fr-banner note"><div class="fr-banner-icon">star</div><div class="fr-banner-content note"><div class="fr-banner-label">Note:</div><div class="fr-banner-description">In Jetpack Compose, the Expressive styling is called "vibrant"</div></div></div>

<p><strong>Oct 2026</strong></p><p>Variants and naming</p><ul type="disc" style="list-style-type:disc"><li><p>Added <strong>scroll time picker</strong></p></li><li><p>Updated <strong>input time picker</strong> and <strong>dial time picker</strong> with expressive styles</p></li></ul><p>Expressive styles</p><ul type="disc" style="list-style-type:disc"><li><p>Higher contrast on hour and minute fields, and dial selector</p></li><li><p>Expressive button shape, color, and behavior for AM and PM buttons</p></li><li><p>Removed <strong>select time</strong> label</p></li></ul>

Expressive variants for time picker: scroll, input, and dial.

<p>The expressive update added <strong>scroll time pickers</strong>, and updated <strong>input</strong> and <strong>dial time pickers</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwbza46v-03-2x.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/rY2Q1QNrh2lRO5443KzA34v6gb0wOFboJYE-eW_8neAxzRxlQw1yqUTEexYS2W6V2jrVKC_1QgfdTsmGSrpFXNBbidKCxEgCsbM4B2xx4SUCYw=s2704

<h2>Differences from M2 to M3 baseline</h2>

<ul type="disc" style="list-style-type:disc"><li><p>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element><br /></p></li></ul>

Time picker’s old color mappings. The selected hour of 7 and AM text is purple, on a purple background.

<p>M2: Time pickers had different color mappings</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwacyuhf-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/NFgPP9w9yh9-ZxZ5gLA0Wh-SXsechSvgGQxRLjMkXeQ-XXhvNz4Tk5j5K8Swr0d7Bz8mCfP1HmqHFDnLPGruMHJ_MIitYq1Wnt8v_roUykJMVw=s1004

Time picker's new color mappings. The selected hour of 7 and AM text is black, with different background colors.

<p>M3: Time pickers have new color mappings compatible with dynamic color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwad1i2r-05.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/1wLfKTfayu3yrhYEQXGEPwB4uKnZmeMviMPOzNSCZJAC4u1JBq-DKFElfI5XXwtcp16tRp47M9mIKYv6y3OM3ocXqcsiUDwWZ-BDD_Qh8nxE=s1004

## Specs

<h2>Expressive variants</h2><p>Scroll time picker was added in the expressive update. Input and dial time pickers have updated visuals.</p>

Three expressive variants: scroll, input, and dial time pickers.

<ol type="1" style="list-style-type:decimal"><li><p>Scroll time picker</p></li><li><p>Input time picker</p></li><li><p>Dial time picker</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwadk1zg-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/5O5_jBMYyjbwAhqegI6YjI_BoZfv4fjK5zcB0RgJyASnE12T4HmAtoN2m1g6XRWS8ylN_TwTfcjcvEXiMMHunqNbmGkkieWPu-oAkdJNcX2a=s2048

<h2>Baseline variants</h2>

<p>Baseline variants for input time picker and dial time picker are no longer recommended. <a href="/m3/pages/time-pickers/specs#298a79d2-01ae-42ac-bbf0-ec89cecd7d6e" target="_self">Jump to baseline time picker specs</a></p>

Baseline versions of input and dial time picker.

<p>Baseline time pickers are no longer recommended:<br />1. Input time picker<br />2. Dial time picker</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwado8sn-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/jleceY4Qt4ejjOMlAJfK8paDociqr-5dQ-CTfzr0nNBNcu1cSRZuJnIb6YCBnzjn-Krh4e7QspZDvElBmYekhGV-jX4m-IhdnCpiuNgXc4kx=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><tbody><tr><th style="width:31.7476%;text-align:left"><p>Variant</p></th><th style="width:30.5898%;text-align:center"><p>M3</p></th><th style="width:37.5495%;text-align:center"><p>M3 Expressive</p></th></tr><tr><td><p>Scroll time picker</p></td><td><p>--</p></td><td><p>Available</p></td></tr><tr><td><p>Input time picker</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Dial time picker</p></td><td><p>Available</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Configurations</h2>

<h3>Behavior: Inline or modal</h3><p>Expressive scroll and input time pickers can be placed inline with page content. Baseline input time pickers are only available as modal.</p>

<h4>Scroll time picker</h4>

Inline and modal scroll time pickers. Modal has text buttons for OK and Cancel.

<ol type="1" style="list-style-type:decimal"><li><p>Inline</p></li><li><p>Modal</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwdrrp2g-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/WJMUtvDzRttZHlsSFhk85iQLuQWdrp_24I8g0DCi3RUSmqumdd9uuAXuWPGmbr7Iz9rTAr7pLq1CB-m_pqLchn1Wog43PlPIvcqsHmTJyEGX_w=s2048

<h4>Input time picker</h4>

Inline and modal input time pickers. Modal has text buttons for OK and Cancel.

<ol type="1" style="list-style-type:decimal"><li><p>Inline</p></li><li><p>Modal</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwdrs50m-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/STmWmsa55hBHGqvS6bchEfAQWuHWllT9UApDloKKZ6xU5K4_jDKYV13ZpZEyu3W2u8UQbp6Dn_mVFqQAVVZtV3su8jncqhXHWmOeeHZ4tbq9rA=s2048

<h4>Dial orientation: horizontal or vertical</h4>

Comparing vertical and horizontal dial time pickers.

<ol type="1" style="list-style-type:decimal"><li><p>Vertical layout (default on mobile)</p></li><li><p>Horizontal layout</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwdrsgtr-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/BpALszuJPzlM_TJzeYUJboIdjVDUL6IMOZgNpM1yoC791jkvVlt8toDLJcqKoLIoSPdN7HOQAG_Y3KMvocwhL3rIVFSelwVckNDlS8z0b3jP5Q=s2048

<h4>Time length: 12-hour or 24-hour</h4><p>24-hour time pickers don’t have the AM or PM buttons, so are have a smaller width when modal. Dial time pickers have an outer dial for 0 to 11, and an inner dial for 12 to 23.</p>

<h5>Scroll time picker</h5>

2 24-hour scroll time pickers with vertical and horizontal layouts.

<ol type="1" style="list-style-type:decimal"><li><p>Inline</p></li><li><p>Modal</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwaect5w-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/jToJFGNTxBNJQS2dJpv6dFsId5XhK4PG7H97HK9WWBndUy__rWgrLJzh3N8hGOk63H3xIoWjPuigVvUVybKmC-8uBQ1VjREO5rONaFK5G2tZ=s2048

<h5>Dial time picker</h5>

2 24-hour dial time pickers with vertical and horizontal layouts.

<ol type="1" style="list-style-type:decimal"><li><p>24h dial in vertical layout (default on mobile)</p></li><li><p>24h dial in horizontal layout</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwaedllu-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ssXWi08YaBOrEFHSLVGa6Nh0SfHwDjhH8BScMhkvpgY_5Srv1v3OBl-sSEstiipdrb1zd9SzP060js7miFm_avgZjS-00boEKa_sOZB5uHpr=s2048

<h5>Input time picker</h5>

12-hour and 24-hour input time pickers.

<ol type="1" style="list-style-type:decimal"><li><p>Inline</p></li><li><p>Modal</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwaehvr9-08-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/76uCVNZ-yvVdbni8G3jiBdCXvDEXU_CHyK8no2pUUgFp4tt24rpAVK3afPvLsPjAKQk5G1m60dYGBoag74cS3fpJ2BL8pHxVBuG4LjWEGsWN=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><tbody><tr><th><p>Category</p></th><th><p>Configuration</p></th><th style="text-align:center"><p>M3</p></th><th style="text-align:center"><p>M3 Expressive</p></th></tr><tr><td><p>Behavior</p></td><td><p>Inline</p></td><td><p>Available (input only)</p></td><td><p>Available (input &amp; scroll only)</p></td></tr><tr><td></td><td><p>Modal</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Time length</p></td><td><p>12-hour, 24-hour</p></td><td><p>Available</p></td><td><p>Available</p></td></tr><tr><td><p>Dial orientation</p></td><td><p>Horizontal, vertical</p></td><td><p>Available</p></td><td><p>Available</p></td></tr></tbody></table></div>

<h2>Tokens &amp; specs</h2><p>Select a component variant below to see its elements, attributes, tokens, and their values. <a href="/m3/pages/design-tokens" target="_blank">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/39f4b152dd9bd292

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Time pickers'], 'contextTags': ['High contrast', '3P', 'Medium contrast', 'Light', 'Bold', 'Default', 'Expressive', 'Static', 'Standard', 'Dark', 'None', 'Compose', 'Android', 'Web'], 'showInlineTokenShare': True}

<h2>Anatomy</h2>

<h3>Scroll time picker </h3>

Diagram identifying the 4 elements of a scroll time picker.

<ol type="1" style="list-style-type:decimal"><li><p>Scroll field</p></li><li><p>Separator</p></li><li><p>Period selector</p></li><li><p>Input mode toggle</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwag29x4-09-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/mGunN-W1R_HfwPEqnk1NXkcwny2sbZgy9--O8SlOhm3u1zbXUV6jreMuXJOPpg0INf14pJr5U-oDnb6OZLuvbVL_9igdkofUdZBj5WveGjpJ=s2048

<h3>Input &amp; dial time picker</h3>

Diagram identifying the 13 elements of a dial and input time picker.

<ol type="1" style="list-style-type:decimal"><li><p>Scroll field</p></li><li><p>Selected active value</p></li><li><p>Separator</p></li><li><p>Container</p></li><li><p>Toggle label button</p></li><li><p>Period selector label text</p></li><li><p>Clock dial selector center</p></li><li><p>Clock dial selector track</p></li><li><p>Text buttons</p></li><li><p>Icon button</p></li><li><p>Clock dial selector container</p></li><li><p>Clock dial label text</p></li><li><p>Clock dial container</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwag63s1-10-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/romTeX8K3RQ6Zv7xwRLhaMu8mIcXhI4doxw4IxK6V8GHGA_wcZWI90GwX9Vu8R7BUMVuGzUu2owpct5S6i34o8JEG-qrsNz2m33dkKg0SFGqKQ=s2048

<h2>Color</h2><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p>

<h3>Scroll time picker color</h3>

Side-by-side light and dark diagrams identifying the 9 different color elements of a scroll time picker.

<p>Scroll time picker color roles used for light and dark themes:</p><ol type="1" style="list-style-type:decimal"><li><p>Surface container lowest</p></li><li><p>On surface</p></li><li><p>On surface</p></li><li><p>Outline</p></li><li><p>Primary container</p></li><li><p>On primary container</p></li><li><p>Surface container lowest</p></li><li><p>On surface variant</p></li><li><p>On surface variant</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwagarlr-11-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/wXR4kHMp4cDTdgKS8bn0dDwlyfhJeoEruz5zF0FUiTW-gyXZwPS3MW7BKOaVyyb0mDiF73khC2ROudjGNihZKNAfDFH_Mm1NlOpoDeFOSgTh=s2048

<h3>Dial &amp; input time picker  color</h3>

Side-by-side light and dark themed diagrams identifying the 13 different color elements of a dial and input time picker.

<p>Dial and input time picker color roles used for light and dark themes:</p><ol type="1" style="list-style-type:decimal"><li><p>Primary</p></li><li><p>Primary</p></li><li><p>On surface</p></li><li><p>Surface container lowest</p></li><li><p>Primary container</p></li><li><p>On primary container</p></li><li><p>Surface container lowest</p></li><li><p>On surface variant</p></li><li><p>Surface container lowest</p></li><li><p>On surface</p></li><li><p>Primary</p></li><li><p>On surface variant</p></li><li><p>Primary</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwagfk1v-12-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-iRjxk5GhJ_pQEz1IQZa9hCpYEx0n7LJw-nKhB38pqESNAfUWr1myTMiCogeEfXvOV-fnAgLvcWDGYqaH_Gze93Yi3_CTSKZF-eZe6fkMkar=s2048

<h2 id="isPasted">States</h2>

Digram showing the 4 interactive states of a time picker, in both light theme and dark theme.

<p>States for scroll (default), text input, and AM/PM buttons:</p><ol type="1" style="list-style-type:decimal"><li><p>Enabled</p></li><li><p>Hovered</p></li><li><p>Focused</p></li><li><p>Pressed</p></li><li><p>Disabled</p></li><li><p>Error</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwah3fls-13-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/V7IXWklQbXo4Jg8E4nUTbtTArjbwUtG-PU9g5cPM6b2VEz5EYe5atvi5EgEo-oXdfevqJy_JCsQgkVcJEFchzYQp2WlTLJUpp3Lb9G_r4kWU=s2048

Digram showing the 3 interactive states of a time picker’s clock dials, in both light and dark theme.

<p>States for clock dials:</p><ol type="1" style="list-style-type:decimal"><li><p>Enabled</p></li><li><p>Hovered</p></li><li><p>Focused</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwah4qb5-14-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/sqTMOvffpd1tTAz3KGmA7IeIA9wL1cGGKqCw-_6z_eceOe3F0UHL3laE1dAQMRrFwEJS_bj8jJE7Owd2KTGxfBGbEip0V8hGMIpN5ZMD1NJP=s2048

<h2>Measurements</h2>

<h3>Inline time picker (input &amp; scroll)</h3>

Diagram of scroll time picker measurements.

<p>Scroll time picker padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwahxsq8-15-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/vg3dkSOy9rvUAC_iJXjMhHe5_IhLFwbbTgDFPbUjaXl3l2NoFLKS7uV8EOa_deO3Cr-_xW3qswHKS6QbGw0vH5o4L81V5xkQWW0J9vYDvWM=s2048

<h3>Modal time picker (input &amp; scroll)</h3>

Diagram of input time picker measurements.

<p>Input time picker padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwai24qa-16-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/iwmHRH_xoTMazmYovn6eAyvCabFEaslEBOmeUxzyjQoy7ZG38U4puvDJ44lJinSaZMbu6WNM-iE3HaND7jzOx4xX0fnmXs1IDZMfKEBPiXyB=s2048

<h3>Dial time picker (vertical)</h3>

Diagram of vertical dial time picker measurements.

<p>Vertical dial time picker padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwaidlwl-17-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/9-qN0p20APU2HxNu1_xxG9JeIh6lSsAXNd8cTZzhrFeAvGG7aXaXftpBzZA10BB558xG173sl1iZF8Me7b-ZMNHpNpg35FFwvSBtHwzvlQYW=s2048

<h3>Dial time picker (horizontal)</h3>

Diagram of horizontal dial time picker measurements.

<p>Horizontal dial time picker padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwaieqex-18-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/loyIzSBx82pKgfc34MVqDHExnLo6KtgRT36pwjCoumk3wgDOp3oaXYtbBdgS5huMT2EHRLEqSwksMVAoG6GKHsZY7VYqJI_BPqKweklmfwo=s2048

<h2>Baseline</h2>

<h3>Tokens &amp; specs</h3>

<p>Select a token set to view in the table's menu. Baseline time picker token sets are organized into dial and input sets. <a href="/m3/pages/design-tokens" target="_blank">Learn more about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/39f4b152dd9bd292

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Time picker - Input', 'Time picker - Dial'], 'contextTags': ['High contrast', '3P', 'Medium contrast', 'Light', 'Bold', 'Default', 'Expressive', 'Static', 'Standard', 'Dark', 'None', 'Android'], 'showInlineTokenShare': True}

<h2 id="isPasted">Configurations</h2>

<p>Vertical and horizontal orientation for dial time picker is the same for expressive and baseline.</p>

<h4>24-hour dial time picker</h4>

2 24-hour baseline time picker dials with vertical and horizontal layouts.

<ol type="1" style="list-style-type:decimal"><li><p>24h dial in vertical layout (default on mobile)</p></li><li><p>24h dial in horizontal layout</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwaloe9n-27-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/QxMO9mq0HWSUN4lz5cLLKynPOOfMXLSZ-lFivXnf9VKP1p6_NbtDP_0eWwKroJz37FikHb3YRzjAJkFr45i-xi_Gm8mURfpzFfHONUir68hf=s2048

<h4>12-hour and 24-hour input time pickers</h4>

Compare 12-hour and 24-hour baseline time picker inputs.

<ol type="1" style="list-style-type:decimal"><li><p>12h input</p></li><li><p>24h input</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwalw0bp-28-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/O9BGM2tjMTG7Y3o0r2ygUgcLBu-bln0_cXa1dBn_90ea9l73cmURsfh-Je_h2X1rKbdNWRPoY_s5fuvxwDWIDLzuW2aCij2p7QEsz9DKyRrNjA=s2048

<h3>Anatomy</h3>

<h4>Input time picker</h4>

Diagram identifying the 10 elements of a baseline input time picker.

<ol type="1" style="list-style-type:decimal"><li><p>Headline</p></li><li><p>Time input field separator</p></li><li><p>Container</p></li><li><p>Period selector container</p></li><li><p>Period selector label text</p></li><li><p>Text buttons</p></li><li><p>Icon button</p></li><li><p>Time input field supporting text</p></li><li><p>Time input field label text</p></li><li><p>Time input field container</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwam5qzc-19-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/RjYIGw6cRdDIJb6Mb40bqPM1QP88IeYtrW9cEHJEhhjg1wvMFRWMccQFGJ-UCmG6Agi7vcxa0foo7JY0TwYiqDYurGiTp4tlR1STwgwYc5xD=s2048

<h4>Dial time picker</h4>

Diagram identifying the 14 elements of a baseline dial time picker.

<ol type="1" style="list-style-type:decimal"><li><p>Headline</p></li><li><p>Time selector separator</p></li><li><p>Container</p></li><li><p>Period selector container</p></li><li><p>Period selector label text</p></li><li><p>Clock dial selector center</p></li><li><p>Clock dial selector track</p></li><li><p>Text buttons</p></li><li><p>Icon button</p></li><li><p>Clock dial selector container</p></li><li><p>Clock dial label text</p></li><li><p>Clock dial container</p></li><li><p>Time selector label text</p></li><li><p>Time selector container</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwam724l-20-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/zXTGkqWN_mEhaZLaPRRKvWOoGg66XNi3MCCGv8wha8q0cLz7XOkr5Arkr0nDcHGeEjlxNumHBlLtnwC0WFf6SP-w3glfxhcHgTtFv0H4Gno=s2048

<h3>Color</h3>

<p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_blank">Learn more about design tokens</a></p>

<h4>Input time picker color</h4>

Side-by-side light and dark diagrams indicating the 13 different color elements of a time picker input.

<p>Input time picker color roles used for light and dark themes:</p><ol type="1" style="list-style-type:decimal"><li><p>On surface variant</p></li><li><p>On surface</p></li><li><p>Surface container highest</p></li><li><p>On surface</p></li><li><p>Tertiary container</p></li><li><p>On tertiary container</p></li><li><p>Surface container high</p></li><li><p>Outline</p></li><li><p>On surface</p></li><li><p>Primary</p></li><li><p>On surface variant</p></li><li><p>On primary container</p></li><li><p>Primary container</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwam8wa5-22-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/UPw8Js0HoKe8mQgWKipCfJqg6XAuzOe_mvbr30vGpmyqt3mD108J1O50ZZnF7CzXanVt4T3uD09YN_dDVfoLsGd08G-fWqzF_EyNrf7WAGg=s2048

<h4>Dial time picker color</h4>

Side-by-side light and dark diagrams identifying the 17 different color elements of a baseline dial time picker.

<p>Dial time picker color roles used for light and dark themes:</p><ol type="1" style="list-style-type:decimal"><li><p>On surface variant</p></li><li><p>On surface</p></li><li><p>Surface container highest</p></li><li><p>On surface</p></li><li><p>Tertiary container</p></li><li><p>On tertiary container</p></li><li><p>Surface container high</p></li><li><p>Outline</p></li><li><p>On surface</p></li><li><p>Primary</p></li><li><p>On primary</p></li><li><p>Primary</p></li><li><p>On surface variant</p></li><li><p>On surface</p></li><li><p>Surface container highest</p></li><li><p>On primary container</p></li><li><p>Primary container</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwamacq4-21-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/dyKvb_HaJcV9UPA1_MMOR4YdtAAqXkz4F1A9yRt_QyE2g4IqHnmqHTeRvBBM_CMMUT8GyYVBNZvjdqz8loXrx7MkfhBHdWc1oO9cX0xqh6I=s2048

<h3>States</h3>

Digram showing the 4 interactive states of a time picker, in both light theme and dark theme.

<ol type="1" style="list-style-type:decimal"><li><p>Enabled</p></li><li><p>Hover</p></li><li><p>Focus</p></li><li><p>Pressed</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwamogug-23-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/i62EOAkNAgKofejbz6lkGcfbhUl6N_Huq5YfdV25H5Z8VMTT0wX4-C-7Xgxl-4Su05-TZGPv0EJnQ50bovPx_cMRIssZPhy3ZkewNVPad9Y=s2048

<p><a href="/m3/pages/time-pickers/specs#2ccd9809-9246-4667-85fa-7747f4ac7349" target="_self">States specs can be found in the token module above</a></p>

<h3>Measurements</h3>

<h4>Input time picker</h4>

Diagram of time picker input measurements.

<p>Time picker input padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwampvhe-26-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/kAbzSccQxzDU206rinW0mU_g75e-Zw1eTuFXbCZfOiU8r-OcgU5oMPybtF4BAsRc8_bKRK2LZfUxxsdonJGRVzqIS1GZBHr_FOt3hNIPeE21sg=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><tbody><tr><th style="text-align:center"><p>Element</p></th><th style="text-align:center"><p>Attribute</p></th><th style="text-align:center"><p>Value</p></th></tr><tr><th rowspan="5"><p>Container</p></th><td><p>Width</p></td><td><p>Dynamic</p></td></tr><tr><td><p>Height</p></td><td><p>Dynamic</p></td></tr><tr><td><p>Headline alignment</p></td><td><p>Left</p></td></tr><tr><td><p>Top/bottom padding</p></td><td><p>24dp</p></td></tr><tr><td><p>Left/right padding</p></td><td><p>24dp</p></td></tr><tr><th rowspan="2"><p>Time input field container</p></th><td><p>Width</p></td><td><p>96dp</p></td></tr><tr><td><p>Height</p></td><td><p>72dp</p></td></tr><tr><th rowspan="2"><p>Period selector container</p></th><td><p>Width</p></td><td><p>52dp</p></td></tr><tr><td><p>Height</p></td><td><p>72dp</p></td></tr></tbody></table></div>

<h4>Dial time picker (vertical)</h4>

Diagram of baseline vertical dial time picker measurements.

<p>Vertical dial time picker padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwamriue-24-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/7RPhsaMgtMBeehu4YuzF7eUx2q-xldVsKiR3gWjQzKQALyLGACbutgDjTP3MymSldwHvAZ2kgtwbNgs5a-J2bR9G50GLe-V952kIIs7pdBT2fA=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><tbody><tr><th style="width:46.4625%;text-align:center"><p>Element</p></th><th style="width:36.9476%;text-align:center"><p>Attribute</p></th><th style="width:16.4995%;text-align:center"><p>Value</p></th></tr><tr><th rowspan="5" style="width:46.4625%"><p>Container</p></th><td><p>Width</p></td><td><p>Dynamic</p></td></tr><tr><td><p>Height</p></td><td><p>Dynamic</p></td></tr><tr><td><p>Headline alignment</p></td><td><p>Left</p></td></tr><tr><td><p>Top/bottom padding</p></td><td><p>24dp</p></td></tr><tr><td><p>Left/right padding</p></td><td><p>24dp</p></td></tr><tr><th rowspan="3" style="width:46.4625%"><p>Time selector container</p></th><td><p>Width</p></td><td><p>96dp</p></td></tr><tr><td><p>Width (24h vertical)</p></td><td><p>114dp</p></td></tr><tr><td><p>Height</p></td><td><p>80dp</p></td></tr><tr><th rowspan="4" style="width:46.4625%"><p>Period selector container</p></th><td><p>Width (vertical layout)</p></td><td><p>52dp</p></td></tr><tr><td><p>Height (vertical layout)</p></td><td><p>80dp</p></td></tr><tr><td><p>Width (horizontal layout)</p></td><td><p>216dp</p></td></tr><tr><td><p>Height (horizontal layout)</p></td><td><p>38dp</p></td></tr><tr><th style="width:46.4625%"><p>Clock dial container</p></th><td><p>Size</p></td><td><p>256dp</p></td></tr><tr><th style="width:46.4625%"><p>Clock dial selector handle</p></th><td><p>Size</p></td><td><p>48dp</p></td></tr><tr><th style="width:46.4625%"><p>Clock dial selector center</p></th><td><p>Size</p></td><td><p>8dp</p></td></tr><tr><th style="width:46.4625%"><p>Clock dial selector track</p></th><td><p>Width</p></td><td><p>2dp</p></td></tr></tbody></table></div>

<h4>Dial time picker (horizontal)</h4>

Diagram of baseline horizontal dial time picker measurements.

<p>Horizontal dial time picker padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmwamtacw-25-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/uzLUzr8NJrf-HvAgePPxCVpIDcsrAfcfvBwQ1pwjaXCsT5tj6yiTy_eZ2WH5YHNeCa0aWG8v2PtzBRz3CrWYOQzTbwuY27rGtfGjOdrRSX-H=s2048

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><tbody><tr><th style="text-align:center"><p>Element</p></th><th style="text-align:center"><p>Attribute</p></th><th style="text-align:center"><p>Value</p></th></tr><tr><th rowspan="5"><p>Container</p></th><td><p>Width</p></td><td><p>Dynamic</p></td></tr><tr><td><p>Height</p></td><td><p>Dynamic</p></td></tr><tr><td><p>Headline alignment</p></td><td><p>Left</p></td></tr><tr><td><p>Top/bottom padding</p></td><td><p>24dp</p></td></tr><tr><td><p>Left/right padding</p></td><td><p>24dp</p></td></tr><tr><th rowspan="3"><p>Time selector container</p></th><td><p>Width</p></td><td><p>96dp</p></td></tr><tr><td><p>Width (24h vertical)</p></td><td><p>114dp</p></td></tr><tr><td><p>Height</p></td><td><p>80dp</p></td></tr><tr><th rowspan="4"><p>Period selector container</p></th><td><p>Width (vertical layout)</p></td><td><p>52dp</p></td></tr><tr><td><p>Height (vertical layout)</p></td><td><p>80dp</p></td></tr><tr><td><p>Width (horizontal layout)</p></td><td><p>216dp</p></td></tr><tr><td><p>Height (horizontal layout)</p></td><td><p>38dp</p></td></tr><tr><th><p>Clock dial container</p></th><td><p>Size</p></td><td><p>256dp</p></td></tr><tr><th><p>Clock dial selector handle</p></th><td><p>Size</p></td><td><p>48dp</p></td></tr><tr><th><p>Clock dial selector center</p></th><td><p>Size</p></td><td><p>8dp</p></td></tr><tr><th><p>Clock dial selector track</p></th><td><p>Width</p></td><td><p>2dp</p></td></tr></tbody></table></div>

## Guidelines

Full-scale presentation of three time picker variants: scroll, input, and dial.

<p>Use the time picker that best complements the available space and existing interaction patterns:</p><ol type="1" style="list-style-type:decimal"><li><p>Scroll time picker</p></li><li><p>Input time picker</p></li><li><p>Dial input picker</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmurj5247-01.png?alt=media

<h2>Usage</h2>

<p>Time pickers are used to enter a specific time value, usually hours and minutes. They can be placed inline with other content, on surfaces like <app-froala-tooltip-element description="Bottom sheets show secondary content anchored to the bottom of the screen." link-label="More on bottom sheets" link-url="/m3/pages/bottom-sheets/overview" should-open-link-in-new-tab="true">bottom sheets</app-froala-tooltip-element>, <app-froala-tooltip-element description="Side sheets show secondary content anchored to the side of the screen." link-label="More on side sheets" link-url="/m3/pages/side-sheets/overview" should-open-link-in-new-tab="true">side sheets</app-froala-tooltip-element>, <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menus</app-froala-tooltip-element>, or in modal <app-froala-tooltip-element description="Dialogs provide important prompts in a user flow." link-label="More on dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">dialogs</app-froala-tooltip-element>. Whenever possible, place time pickers inline so surrounding content remains visible.</p><p>Time pickers can be used for a wide range of use cases, like:</p><ul type="disc" style="list-style-type:disc"><li><p>Setting an alarm</p></li><li><p>Scheduling a meeting</p></li><li><p>Choosing a time range</p></li></ul><p>There are three time pickers: <strong>scroll</strong>, <strong>input</strong>, and <strong>dial</strong>.</p>

Scroll time picker setting an alert with an option for recurring alert and additional fields for day of week and AM or PM.

<p>A scroll time picker can be used inline to set an alert</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukwm4vp-02.png?alt=media

<h3>Scroll time picker</h3><p>The scroll time picker is a compact way to select time. It’s best placed inline with other content, but can also be used on surfaces like a sheet, menu, or modal dialog.</p><p>Use <strong>scroll</strong> time pickers instead of <strong>dial</strong> pickers when you want people to see surrounding content.</p><p><strong>Scroll</strong> time pickers can toggle to <strong>input</strong> time pickers.</p>

Scroll time picker for a 12-hour clock, with AM/PM selector visible.

<p>A scroll time picker for a 12-hour clock, with AM/PM selector visible</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukwr3dh-03-VQA.png?alt=media

<h3>Input time picker</h3><p>The input time picker uses keyboard entry to input time. Similar to scroll time picker, it can be used inline or modal, on any kind of surface.</p><p>Both the <strong>dial</strong> and <strong>scroll</strong> time pickers are built to toggle to <strong>input</strong> time pickers to ensure accessible time entry.</p>

Input time picker for a 12-hour clock with the hour field active and highlighted and AM/PM selector visible.

<p>Input selector for a 12-hour clock, with AM/PM selector</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukwux7f-04.png?alt=media

<h3>Dial time picker</h3><p>Dial time pickers are the most engaging way to select time, but they take up the most space, and are only available in modal dialogs, not inline.</p><p>Avoid using dial time pickers for granular time selection, such as milliseconds for a stopwatch application.</p><p><strong>Dial</strong> time pickers can toggle to <strong>input</strong> time pickers.</p>

Dial time picker for a 12-hour clock with hour 7 selected.

<p>When using a 12-hour clock for dial select, numbers only appear in the outer ring</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukx1dy5-05.png?alt=media

<h3>Toggling to input selector</h3><p>The input selector can be toggled from either the dial or scroll selector using the keyboard icon button.</p><p>Toggle back to dial picker with a clock icon. Toggle back to scroll picker with a swipe icon.</p>

Dial time picker with keyboard icon button for toggling to input.

<p>Selecting the keyboard icon switches to direct input. Selecting the dial icon switches back to dial input.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukx8qrj-Gm3%20-%20Time%20Pickers%20-%20Guidelines%2006%20-IA%20-v01.mp4?alt=media

<h3>24-hour time selection</h3>

<p>The time picker should auto-adjust to 24-hour time settings, removing the AM and PM buttons, and adding the inner dial. For dial picker, time moves from 0-11 on the outer dial, switches to 12-23 on the inner dial, and returns to 00 on the outer dial for the 24th hour.</p>

Time picker with scroll input, with the hour field set to 18 and the minute field set to 30.

<p>24-hour scroll and input time pickers have no AM and PM buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukxgdhf-07.png?alt=media

Time picker with dial input selecting hour 20. Hours 0–11 use an outer dial, while hours 13–24 use an inner dial.

<p>24-hour dial time picker has no AM and PM buttons, and has an inner dial</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukxhknr-08.png?alt=media

<h3>Alternate time selection components</h3>

<p>Only use time pickers when any time can be chosen, down to the minute. If people only need to choose from preset times or intervals, consider using a simpler, smaller component like a <app-froala-tooltip-element description="Button groups organize buttons and add interactions between them." link-label="More on button groups" link-url="/m3/pages/button-groups/overview" should-open-link-in-new-tab="true">button group</app-froala-tooltip-element>, <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element>, or <app-froala-tooltip-element description="Combo boxes combine a text field and a menu to quickly enter text and make a selection." link-label link-url should-open-link-in-new-tab="false">combo box</app-froala-tooltip-element>.</p>

Button groups listing multiple reservation times, with some missing.

<p>Use button groups when certain time options are unavailable</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukxojjq-09-do.png?alt=media

A calendar app showing multiple times for a meeting, in 15-minute increments.

<p>Use menus or combo boxes when time options are limited and part of a range </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukxqalv-10-do.png?alt=media

<h2>Customization</h2>

<h3>Text &amp; containers</h3><p>Typography can be customized for more expressive time selection experiences, such as stretching, narrowing, and rounding the text.</p><p>When using narrower and larger typography, use taller scroll field heights so the surrounding options are at least half-visible.</p>

Scroll time picker with large, bold, and narrow numerals.

<p>Adjust scroll field container height when increasing size of typography</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukxv7vt-11.png?alt=media

<h3>Color</h3><p>When customizing color, make sure both active and inactive values maintain the required <app-froala-tooltip-element description="Contrast ratios represent how different one color is from another color, commonly written as 1:1 or 21:1. The greater the difference is between the two numbers in the ratio, the greater the difference in relative luminance between the colors." link-label="More on contrast ratios" link-url="/m3/pages/designing/color-contrast#ccf80af1-c775-4fac-8d26-0e10766c074d" should-open-link-in-new-tab="true">contrast ratio</app-froala-tooltip-element> with the scroll field background.</p>

Scroll time picker with custom colors applied.

<p>When customizing color, maintain proper contrast between the numerals and scroll field</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukxzmuq-12.png?alt=media

<h3>Container (modal)</h3><p>When in a modal <app-froala-tooltip-element description="Dialogs provide important prompts in a user flow." link-label="More on dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">dialog</app-froala-tooltip-element>, the time picker container should always be visible, appearing above other screen elements in front of a scrim.</p><p>The container usually isn’t needed when inline with other content.</p>

2 input time pickers, with and without containers.

<ol type="1" style="list-style-type:decimal"><li><p>Input time picker modal (with a container)</p></li><li><p>Input time picker inline (without a container)</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmuky2avc-13.png?alt=media

<h3>Input toggle button</h3><p>An <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon button</app-froala-tooltip-element> must be present to toggle from a dial or scroll time picker to an input time picker.</p><p>If not using the built-in toggle, make sure a toggle is placed nearby.</p>

Cropped portion of dial selector without keyboard icon, removing path to input selector.

<p>Don’t remove the built-in toggle button from dial or scroll time pickers without providing another way to toggle</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmuky4v6z-14-dont.png?alt=media

<h2>Placement</h2>

<h3>Inline</h3><p>Whenever possible, place time pickers inline with content, rather than as a modal dialog. This makes it much easier for people to reference other content on the page when making their decision.</p>

A UI displaying a scroll time picker for the specific time of an event, surrounded by fields for date and setting time zone.

<p>Inline time pickers can be shown and hidden to preserve space when not in use</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukygx94-Gm3%20-%20Time%20Pickers%20-%20Guidelines%2016%20-IA%20-v02.mp4?alt=media

<h3>Menus</h3><p>On touch devices, when time pickers can't be placed inline, consider using a scroll time picker in a menu.</p>

Scroll time picker displayed in a menu.

<p>If inline layout is not possible, use a menu to fully display the time picker</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukyl4kd-GM3%20-%20Time%20Pickers%20-%20Guidelines%2017%20-%20IA%20-%20v01.mp4?alt=media

<h3>Modals</h3><p>Time pickers can be in modal dialogs above a scrim. However, modals should be used rarely, when the UI is too cluttered for more components.</p><p>Dial time pickers are only available in modals.</p>

A modal showing input time picker above a UI filled with fields for event details.

<p>Modals block all other actions when active, though can save space in a busy UI</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukyo1bf-17.png?alt=media

<h2>Adaptive design</h2>

<p>Scroll and input time pickers can resize to fit the container they’re placed in. Each field should resize evenly.</p>

A calendar app using inline scroll time picker that expands when moving from compact to larger breakpoints.

<p>Scroll fields should expand in larger panes to allow for larger tap targets</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukyuab1-GM3%20-%20Time%20Picker%20-%20Guidelines%2018%20-%20IA%20-%20v02.mp4?alt=media

<p>Dial time pickers should swap orientation or variant depending on the <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoint</app-froala-tooltip-element> and available vertical space. Avoid adding scrolling to dial time pickers.</p><p>For example:</p><ul type="disc" style="list-style-type:disc"><li><p>At larger breakpoints with more space, swap from the vertical to horizontal dial time picker</p></li><li><p>When vertical space is reduced, like rotating a phone, swap to the landscape dial picker to avoid scrolling or cutting off the dial</p></li><li><p>When vertical space is very limited, or the interface is zoomed in, swap from dial to a scroll or input time picker</p></li></ul>

A dial time picker in vertical configuration, which is too tall for mobile in landscape mode.

<p>Don’t cut off the dial time picker. Instead, swap to horizontal orientation, or to another time picker.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmukyxufn-19_dont.png?alt=media

<h2>Behavior</h2>

<h3>Scroll time pickers</h3><p>Swipe the scroll fields to select a time value. Values snap into place when released.</p><p>Tap the inactive value above or below to navigate to it.</p><p>The keyboard icon swaps the component to an input time picker.</p>

Scroll time picker with options to swipe and tap, or select the keyboard icon for direct input.

<p>The scroll time picker supports both scrolling and direct input</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmul1fz56-GM3%20-%20Time%20Picker%20-%20Guidelines%2019%20-%20IA%20-%20v01.mp4?alt=media

<h3>Dial time pickers</h3><p>When the dial time picker is opened, the hour field is selected by default. Once hour is selected by dial, the minutes field will activate to then select minutes by dial.</p><p>Selecting either field will reactivate the corresponding dial to select another option.</p><p>The keyboard icon swaps the component to an input time picker.</p>

Dial time picker with hour field selected, and keyboard icon to access direct input.

<p>The dial time picker supports both direct and dial input</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmul1ikkm-GMe-%20Time%20Pickers%20-%20Guidelines%2021%20-%20IA%20-v02.mp4?alt=media

<h3>Input time picker</h3><p>Select a text field to activate the keyboard entry and input a time value.</p><p>Errors should appear below the time picker, and highlight the invalid field with an error color scheme.</p>

Input time picker with swiping icon to access scroll selector.

<p>The swipe icon allows the input selector to switch to scroll selector</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmul1msdq-22-VQA.png?alt=media

<h3>Modals &amp; motion</h3><p>When appearing in a modal, time pickers use <a href="/m3/pages/dialogs/guidelines#71058dbd-d228-4cd5-95e6-eb39761f4c29" target="_blank">appearing and disappearing transitions</a> similar to dialogs.</p><p>The <strong>OK</strong> button confirms the selection and closes the modal. The <strong>Cancel</strong> button, and interacting on the scrim, dismisses the changes and closes the modal.</p>

Time picker enter and exit transitions based on dialogs.

<p><strong>OK</strong> or <strong>Cancel</strong> closes the modal</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmul1scnh-GM3-%20Time%20Pickers%20-%20Guidelines%2023%20-%20IA-%20v02.mp4?alt=media

## Accessibility

<h2>Use cases</h2>

<p>People should be able to use assistive technology to: </p><ul type="disc" style="list-style-type:disc"><li><p>Select or enter hours, minutes, seconds, or milliseconds</p></li><li><p>Choose between 12-hour or 24-hour clock format</p></li><li><p>Enter time selection directly using input fields</p></li></ul>

<h2>Interaction &amp; style</h2>

<p>Material requires time pickers to allow direct time entry through text input in addition to the scroll and dial selector. This toggle is built into the component by default.</p><p>Allowing text input makes it easier for those using keyboard <app-froala-tooltip-element description="Device inputs provide interactive control of an app. Common inputs include a mouse, keyboard, and touchpad." link-label="More on inputs" link-url="/m3/pages/inputs" should-open-link-in-new-tab="true">inputs</app-froala-tooltip-element> rather than touch screens.</p>

Time picker with active manual text input for hours.

<p>Text input is available for both dial and scroll time pickers</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmul2bxcw-01.png?alt=media

<h3>Targets</h3><p>Targets for a scroll field’s inactive values need to be at least 48dp high.</p><p>The tap targets for the AM/PM button and input toggle need to be at least 48x48dp.</p>

Diagram showing scroll fields' target sizes.

<p>Scroll fields, whether active or inactive, must be at least 48dp high</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmul2f323-02.png?alt=media

<p>Targets for each dial item need to be at least 48x48dp. </p>

Dial time picker selector specs, selecting hour 7.

<p>Dial targets should be a minimum of 48x48dp</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmul2ijk3-03.png?alt=media

<h2>Keyboard navigation</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:24.491%"><p><strong>Keys</strong></p></th><th style="width:75.3959%"><p><strong>Actions</strong></p></th></tr></thead><tbody><tr><th style="width:24.491%"><p><strong>Tab</strong></p></th><td><p>Focus lands on (non-disabled) time slot, and moves to the next element</p></td></tr><tr><th style="width:24.491%"><p><strong>Shift</strong> + <strong>Tab</strong></p></th><td><p>Focus moves to the previous element</p></td></tr><tr><th style="width:24.491%"><p><strong>Arrow keys</strong></p></th><td><p>Focus moves between hours or minutes, once hour or minute field is selected. </p><p>When AM/PM radio group is focused, selection moves  between AM and PM.</p><p>Up / down moves to previous / next option in scroll field.</p></td></tr><tr><th style="width:24.491%"><p><strong>Space</strong> or <strong>Enter</strong><br /></p></th><td><p>Activates the (non-disabled) time slot or button.</p><p>Allows direct entry of numbers in input.</p><p>Confirms hour and minute for dial, input, and scroll.</p></td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<p>The hour and minute fields have different roles depending on the type of time picker. </p>

Accessibility tag on a dial time picker's hour field lists “Toggle” for the element.

<p>On dial time pickers, the fields are toggles, not directly editable text fields</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmwds4viy-04.png?alt=media

Accessibility tag on an input time picker's hour field lists “Text input” for role.

<p>On input time pickers, the fields are text inputs</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmwds50lv-05.png?alt=media

Accessibility tag on a scroll time picker's hour  field lists “Rotor” for element. 

<p>On scroll time pickers, the fields are rotors</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmwds55qr-06.png?alt=media

<p>The AM/PM buttons use a <strong>radio group</strong> role, as only one can be selected at a time.</p>

Accessibility tag on the AM button lists “Label: AM, Role: Button.”

<p>The AM/PM buttons are <strong>radio group</strong>. Selecting one unselects the other.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmwds2ksd-07.png?alt=media

<p>Each hour on the dial input is listed out of 12 for a 12-hour dial. Minutes are listed out of 60. Examples:</p><ul type="disc" style="list-style-type:disc"><li><p>“Hour 7 of 12”</p></li><li><p>“Hour 23”</p></li><li><p>“Minute 24 of 60”</p></li></ul>

Accessibility tag on the time picker's dial selector lists "Hour 7 of 12.”

<p>The label on a dial time picker shows the hour out of 12, on a 12-hour dial</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmul346rr-08.png?alt=media

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><tbody><tr><th style="width:22.4114%"><p><strong>Element</strong></p></th><th style="width:26.665%"><p><strong>Accessibility label</strong></p></th><th style="width:30.6932%;text-align:center"><p><strong>Role (Wiz and Jetpack Compose)</strong></p></th><th style="width:20.1172%;text-align:center"><p><strong>Role (Android Views)</strong></p></th></tr><tr><th style="width:22.4114%"><p>Hour input</p></th><td><p>Hour</p></td><td><p>Text input</p></td><td><p>Text input</p></td></tr><tr><th style="width:22.4114%"><p>Hour scroll</p></th><td><p>Hour</p></td><td><p>Rotor (element)</p></td><td><p>Rotor (element)</p></td></tr><tr><th style="width:22.4114%"><p>Hour dial</p></th><td><p>Hour</p></td><td><p>Toggle (element)</p></td><td><p>Toggle (element)</p></td></tr><tr><th style="width:22.4114%"><p>Minute input</p></th><td><p>Minute</p></td><td><p>Text input</p></td><td><p>Text input</p></td></tr><tr><th style="width:22.4114%"><p>Minute dial</p></th><td><p>Minute</p></td><td><p>Rotor (element)</p></td><td><p>Rotor (element)</p></td></tr><tr><th style="width:22.4114%"><p>Minute toggle</p></th><td><p>Minute</p></td><td><p>Toggle (element)</p></td><td><p>Toggle (element)</p></td></tr><tr><th style="width:22.4114%"><p>AM/PM selection</p></th><td><p>AM</p><p> PM</p></td><td><p>Radio group</p></td><td><p>Radio group</p></td></tr><tr><th style="width:22.4114%"><p>Picker toggle button</p></th><td><p>Toggle input picker</p><p>Toggle dial picker</p><p>Toggle scroll picker</p></td><td><p>Button</p></td><td><p>Button</p></td></tr><tr><th style="width:22.4114%"><p>Cancel button</p></th><td><p>Cancel</p></td><td><p>Button</p></td><td><p>Button</p></td></tr><tr><th style="width:22.4114%"><p>OK button</p></th><td><p>OK</p></td><td><p>Button</p></td><td><p>Button</p></td></tr><tr><th style="width:22.4114%"><p>Clock dial time selection</p></th><td><p>12-hour: Hour {Value} of 12</p><p>24-hour: Hour {Value}</p><p>Minutes: Minute {Value} of 60</p></td><td><p>Button</p></td><td><p>Button</p></td></tr></tbody></table></div>

<h2>Navigation</h2>

<h3>Initial focus</h3><p>Initial focus lands on the hour field.</p>

Dial time picker with hour in focus.

<p>The hour field is focused first</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmwds3l1s-09.png?alt=media

<h3>Dial navigation</h3><p><strong>Tab</strong> to move through the hour, minute, and AM/PM options. Use arrow keys to toggle between AM and PM, and <strong>Enter</strong> to select.</p><p><strong>Enter</strong> on the hour or minute field will allow selection of specific numbers. Once focus moves to the dial, it begins on minute 0 or hour 12. <strong>Right</strong> or <strong>Down</strong> will move through hours or minutes clockwise. <strong>Left</strong> or <strong>Up</strong> will move counter-clockwise.</p><p>Selecting <strong>Enter</strong> will confirm hour or minute.</p>

A dial time picker with Tab and Left key moving the dial selector clockwise.

<p><strong>Right</strong> or <strong>Down</strong> moves the dial clockwise. <strong>Left</strong> or <strong>Up</strong> moves the dial counter-clockwise.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmul49fpq-GMe-%20Time%20Pickers%20-%20Accessibility%2010%20-%20IA%20-%20V01.mp4?alt=media
