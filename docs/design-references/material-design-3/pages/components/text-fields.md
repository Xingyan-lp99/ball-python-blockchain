# Text fields

Source: https://m3.material.io/components/text-fields
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/8741ef66-1a80-4b39-adb1-66bea5e6992f.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Make sure text fields look interactive</p></li><li><p>Two variants: <app-froala-tooltip-element description="Filled text fields have more visual emphasis than outlined text fields. They're often used in dialogs and short forms where their style draws more attention." link-label link-url should-open-link-in-new-tab="false">filled</app-froala-tooltip-element> and <app-froala-tooltip-element description="Outlined text fields have less visual emphasis than filled text fields. They're often used in long forms where their reduced emphasis helps simplify the layout." link-label link-url should-open-link-in-new-tab="false">outlined</app-froala-tooltip-element></p></li><li><p>The text field’s <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">state</app-froala-tooltip-element> (blank, with input, error, etc) should be visible at a glance</p></li><li><p>Keep labels and error messages brief and easy to act on</p></li><li><p>Text fields commonly appear in forms and <app-froala-tooltip-element description="Dialogs provide important prompts in a user flow." link-label="More on dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">dialogs</app-froala-tooltip-element></p></li></ul>

2 variants of text fields, filled and outlined.

<ol><li>Filled text field</li><li>Outlined text field</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx2u2h3p-1.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/1747ec3c98bda4e2

libraryModuleType: STATUS_TABLE

<h2>Differences from M2</h2>

<ul id="isPasted"><li>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></li></ul>

A filled and outlined text field with M3 color mappings.

<p>Text fields have new color mappings</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx2u3e4d-2.png?alt=media

## Specs

<h2>Tokens &amp; specs</h2><p>Browse the component elements, attributes, tokens, and their values. <a href="/m3/pages/design-tokens/overview" target="_self">Learn about design tokens</a></p>

resourceName: designSystems/20543ce18892f7d9/components/60990dd98dea0998

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Text field - Filled', 'Text field - Outlined'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2 id="isPasted">Filled text field</h2>

Diagram of a filled text field indicating the 10 parts of its anatomy.

<ol class="decimal"><li><p>Container</p></li><li><p>Leading icon (optional)</p></li><li><p>Label text in empty field</p></li><li><p>Label text in populated field</p></li><li><p>Trailing icon (optional)</p></li><li><p>Focused active Indicator</p></li><li><p>Caret</p></li><li><p>Input text</p></li><li><p>Supporting text (optional)</p></li><li><p>Enabled active indicator</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2j3wjd6-1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/X9POJ7yw_vGiALE8gBKfttJ_56zdy0ncjv5fYNyJVl1Y8SzdDbDA2VCVqWZDA0BYUfjgn3o1jfQ__CB1_3HLphvEi-u8Vex9Q1VZjqkR1HOG=s2048

<h3>Filled text field color</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" target="_self">Learn more about design tokens</a></p>

Diagram of a filled text field indicating its color mappings. 

<p>Filled text field color roles used for light and dark schemes:</p><ol class="decimal"><li><p>Surface container highest</p></li><li><p>On surface variant</p></li><li><p>On surface variant</p></li><li><p>Primary</p></li><li><p>On surface variant</p></li><li><p>Primary</p></li><li><p>Primary</p></li><li><p>On surface</p></li><li><p>On surface variant</p></li><li><p>On surface</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2j3x0d6-2-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/3QvK6g9HSsTheSVwbJnhS3xny_okcH05M7S-VzIzT8Y20T1azDNw3ab6oTjCFDJDqfz8rgA9If_Ra96-wTC9GoAVkjS1XvSfbPyAgiT3LHQcdw=s2048

<h3 id="isPasted">Filled text field states</h3><p>States are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states/overview" id="isPasted">Learn more about interaction states</a></p>

Side by side view of empty and populated filled text fields across different states, showing the differences between enabled, focused, hovered, and disabled. 

<ol><li>Enabled (empty)</li><li>Focused (empty)</li><li>Hovered (empty)</li><li>Disabled (empty)</li><li>Enabled (populated)</li><li>Focused (populated)</li><li>Hovered (populated)</li><li>Disabled (populated)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyqwy2pr-3.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/oKmfNMCJ_ViUQMDGqTLkxCQj9pqlu69kIuzt96fo0YC7mb_vceZF4LQUwYQViUk_oDf38-KSOFZVsM8Car1RCvjy6JPXVv92WCZIJzbEwNuJ_g=s2048

<h3>Filled text field error states</h3><p>Error <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">states</app-froala-tooltip-element> are visual representations used to communicate the status of a component or interactive element. An error message can display instructions on how to fix it. Error messages are displayed below the text field as supporting text until fixed.</p>

Side by side view of empty and populated filled text fields across different error states, showing the differences between enabled, focused, hovered. 

<ol><li>Enabled (empty)</li><li>Focused (empty)</li><li>Hovered (empty)</li><li>Enabled (populated)</li><li>Focused (populated)</li><li>Hovered (populated)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyqx5pjx-4.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/nuNzqyBbqzPQww1YvytMccqt-cGwmw0Brm79oYB6w-Z1am626wYtqGd6pN2nx393wXxEIJRPia-Fb3WuFB61iDiuXmt4F5ERiaV8fcDWYDqs=s2048

<h3 id="isPasted">Filled text field measurements</h3>

Diagram showing layout values and paddings for filled text fields without icons. 

<p>Padding and size measurements without icons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyqxam89-5.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/2AoiwzxCOioxZi9xQyWBalI9wO_Q2Xvt-udVeaI-UDY00zFWxtWZHUvOZa5PFbRwRJrOOQDlMra63kpmnbLyU0GxAKCCL4d-ZlhN50HdtSPn=s2048

Diagram showing layout values and paddings for outlined text fields with leading and trailing icons. 

<p>Padding and size measurements with icons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyqxhgvg-6.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/hG_Z6Lx5Jfmhqu7Rnds8d_Ia4DGHtlVW1oCZbwwqD29FtoXf2_g24bzr81cvy3i7nQxSxDzTXYqKrZ4kKSRIB8yz4QSOK1wDfR1jy2psSypxyQ=s2048

A diagram showing layout values and paddings for supporting text, and supporting text in combination with a character count. 

<p>Padding and size measurements with supporting text and character count</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4adcnvc-7-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/QbiBv3lVHm9nL8hoQllo5jKgQ6AA37Ngmcd3R0DuB37MAANtap_k0woqbUvLxZJqDgPznP0tIBzy1o0GTKPCp9Omo-StlisHHInPTWMcl9vN=s2048

<div class="table-wrapper"><table style="border:none;border-collapse:collapse"><thead><tr><th style="text-align:center">Attribute</th><th style="text-align:center">Value</th></tr></thead><tbody><tr><th>Default container height<br /></th><td>56dp</td></tr><tr><th>Label alignment (unpopulated)<br /></th><td>Vertically centered</td></tr><tr><th>Top/bottom padding<br /></th><td>8dp</td></tr><tr><th>Left/right padding without icons<br /></th><td>16dp</td></tr><tr><th>Left/right padding with icons<br /></th><td>12dp</td></tr><tr><th>Icon alignment<br /></th><td>Vertically centered</td></tr><tr><th>Padding between icons and text<br /></th><td>16dp</td></tr><tr><th>Supporting text and character counter top padding<br /></th><td>4dp</td></tr><tr><th>Padding between supporting text and character counter<br /></th><td>16dp</td></tr><tr><th>Target size</th><td>56dp</td></tr></tbody></table></div>

<h3 id="isPasted">Filled text field configurations</h3>

Side by side view of filled text fields in different configurations.

<p>Empty and populated filled text fields with:</p><ol class="decimal"><li><p>Supporting text</p></li><li><p>Trailing icon</p></li><li><p>Leading icon</p></li><li><p>Leading and trailing icons</p></li><li><p>Prefix</p></li><li><p>Suffix</p></li><li><p>Multi-line text field</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm84goiff-8%20-%203P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/KpOprJPDbuBUSURPtov109LS7MrNCFY0Ek20qjx5tGAzycWbhUb1YSwjT7Bc7KEu3_7woFXY5msSf47VLtW_WDLOBO-g298eC7JmWKfvuXNOGQ=s2048

<h2 id="isPasted">Outlined text field</h2>

Diagram of an outlined text field indicating the 9 parts of its anatomy

<ol class="decimal"><li><p>Enabled container outline</p></li><li><p>Leading icon (optional)</p></li><li><p>Label text in empty field</p></li><li><p>Label text in populated field</p></li><li><p>Trailing icon (optional)</p></li><li><p>Focused container outline</p></li><li><p>Caret</p></li><li><p>Input text</p></li><li><p>Supporting text (optional)</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmhk4c6jn-09-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/juT_ZbiIpoR4u-rL6ab7C0pqjMMp9nEOCEx43GdSNJ0jPkt4RAwIeOy3k047QwD4VLaHhkG4Xc7ZW5tN_AjXfY75D7vByomGUGoz5Y9JfBxyTQ=s2048

<h3 id="isPasted">Outlined text field color</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview">Learn more about design tokens</a></p>

Diagram of an outlined text field indicating its color mappings 

<p id="isPasted">Outlined text field color roles used for light and dark schemes:</p><ol><li>Outline</li><li>On surface variant</li><li>On surface variant</li><li>Primary</li><li>On surface variant</li><li>Primary</li><li>Primary</li><li>On surface</li><li>On surface variant</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm2j3xtlg-10-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/QRrrzuYpe5zpPsCu6AbhllIu1DaJBehUTcv2cIVtd6O7bLdl-ZuUnukzJePt9Y4_-szZKPRj8u0vgwnRAsGDeXih4qprDvoIvyh1_ST_UQUM=s2048

<h3>Outlined text field states</h3><p>States are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states/overview" id="isPasted">Learn more about interaction states</a></p>

Side by side view of empty and populated outlined text fields across different states, showing the differences between enabled, focused, hovered, and disabled. 

<ol><li>Enabled (empty)</li><li>Focused (empty)</li><li>Hovered (empty)</li><li>Disabled (empty)</li><li>Enabled (populated)</li><li>Focused (populated)</li><li>Hovered (populated)</li><li>Disabled (populated)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyqy69rp-11.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/7ChV4X-ZSeY8_BCyeu3u3qdlGOmI9fGOOM00iO7V4hK0Ci3rwp_hy9EoMRpsX5t-SnO-nesLg-wBoom_2uX0Ix15ZtmzEQJZFf1ufQaSCWY=s2048

<h3 id="isPasted">Outlined text field error states</h3><p>Error <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">states</app-froala-tooltip-element> are visual representations used to communicate the status of a component or interactive element. An error message can display instructions on how to fix it. Error messages are displayed below the text field as supporting text until fixed.</p>

Side by side view of empty and populated filled text fields across different error states, showing the differences between enabled, focused, hovered. 

<ol><li>Enabled (empty)</li><li>Focused (empty)</li><li>Hovered (empty)</li><li>Enabled (populated)</li><li>Focused (populated)</li><li>Hovered (populated)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyqya4uw-12.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/JzpL2KJVz10gQRdqaY43CbT_rimzZySTQc-l3ZSUVIdVIYgAXeOvtbuBqIpR3MUIV7uGKVPnHPzTZ8N0SMaRGCeKf7dpiLc4AhE9kxWWdLYp=s2048

<h3 id="isPasted">Outlined text field measurements</h3>

A diagram showing layout values and paddings for outlined text fields without icons. 

<p>Padding and size measurements without icons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyqys303-13.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/fbPahcRVZOrZP4b6Iro8dbT09lSK22S5Fy_Pi_z0Kjiqd_11BD-7MOoRsO3qcXo5x--D8HprVru2ChlRr2BSl-OxHPE5TqKZaVVsMXXD7tJz=s2049

A diagram showing layout values and paddings for outlined text fields with leading and trailing icons. 

<p>Padding and size measurements with icons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyqyuu9g-14.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/IPC3bKvB5geLDysQJQQsC4IYzNggiZUaqGguykwiwZvUKkNbtAH4_QXRM2MRS3kK04txiDciUgwDAPqLOfunUBEFJBw3lyXuoJPln5nweeyo=s2049

A diagram showing layout values and paddings for supporting text, and supporting text in combination with a character count. 

<p>Padding and size measurements with supporting text and character count</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flyqywif5-15.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/_JjJwZsUzwXoqZBtCVcypOsMMq3BPaHVC11s604XWSrXVgPsm5_Jd2mFcMk0lbxVFr2XZSOrtwQeGZAytx0F6sDF42Dz15nNf0_vLAbNBLI=s2049

<div class="table-wrapper"><table><thead><tr><th style="text-align:center">Attribute</th><th style="text-align:center">Value</th></tr></thead><tbody><tr><th>Container height<br /></th><td>56dp</td></tr><tr><th>Left/right padding without icons<br /></th><td>16dp</td></tr><tr><th>Left/right padding with icons<br /></th><td>12dp</td></tr><tr><th>Padding between icons and text<br /></th><td>16dp</td></tr><tr><th>Icon alignment<br /></th><td>Vertically centered</td></tr><tr><th>Supporting text and character counter top padding<br /></th><td>4dp</td></tr><tr><th>Padding between supporting text and character counter<br /></th><td>16dp</td></tr><tr><th>Label alignment<br /></th><td>Vertically centered</td></tr><tr><th>Left/right padding populated label text<br /></th><td>4dp</td></tr><tr><th>Target size</th><td>56dp</td></tr></tbody></table></div>

<h3 id="isPasted">Outlined text field configurations</h3>

A side by side view of outlined text fields in different configurations.

<p>Empty and populated outlined text fields with:</p><ol class="decimal"><li><p>Supporting text</p></li><li><p>Trailing icon</p></li><li><p>Leading icon</p></li><li><p>Leading and trailing icons</p></li><li><p>Prefix</p></li><li><p>Suffix</p></li><li><p>Multi-line text field</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm84gq17k-16%20-%203P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-FpsbRTgumDQyTLpD4LAvrmPPGOU5CXnJFFxPPHNWfN6Fml9KUbuwsV-Uzz7EWlfTKXjfUnGqwv0l1HqTXO7EcMtHgY2BEkZ-XLYOYew_7Nn=s2048

## Guidelines

A side by side view of a filled and a outlined text field.

<p>Filled and outlined text fields</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flyqb5o7k-1%20(1).png?alt=media

<h2>Usage</h2>

<p>Use a text field when someone needs to enter text into a UI, such as filling in contact or payment information.</p>

Mobile UI of contact form with several text fields. 

<p>Contact form using outlined text fields</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx31ssyn-1.png?alt=media

<p>There are two variants of text fields:</p><ol class="decimal"><li><p>Filled text fields</p></li><li><p>Outlined text fields</p></li></ol><p>Both variants of text fields use a container to provide a visual cue for interaction and provide the same functionality.</p>

Side by side view of a populated and unpopulated filled text field. 

<p>Filled text field</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx31t4yp-2.png?alt=media

Side by side view of a populated and unpopulated outlined text field. 

<p>Outlined text field</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx31tc9a-3.png?alt=media

<h3>Outlined text fields</h3><p>Outlined text fields have less visual emphasis than <app-froala-tooltip-element description="Filled text fields have more visual emphasis than outlined text fields. They're often used in dialogs and short forms where their style draws more attention." link-label link-url should-open-link-in-new-tab="false">filled text fields</app-froala-tooltip-element>. When they appear in places like forms (where many text fields are placed together), their reduced emphasis helps simplify the <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/understanding-layout/overview" should-open-link-in-new-tab="true">layout</app-froala-tooltip-element>.</p>

App screen with 1 focused and 1 unfocused outlined text field.

<p>Login screen with outlined text fields</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx31u7r0-4.png?alt=media

<h2>Choosing text fields</h2>

<h3>Choosing text fields</h3><p>Both variants of text field provide the same functionality. The variant of text field used can depend on style alone.</p><p>Choose the variant that:</p><ul><li><p>Works best with an app’s visual style</p></li><li><p>Best accommodates the UI's goals</p></li><li><p>Is most distinct from other components (like <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element>) and surrounding content</p></li></ul>

Mobile UI of a contact form with several filled text fields. 

<p>Mobile form using filled text fields</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx31v0nn-5.png?alt=media

Mobile UI of a contact form with several outlined text fields. 

<p>The same mobile form using outlined text fields</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx31vds5-6.png?alt=media

<h3>Using both text field variants on the same screen</h3><p>If both variants of text field are used in a UI, they should be used consistently within different sections, and not intermixed within the same region. </p><p>For example, use <app-froala-tooltip-element description="Outlined text fields have less visual emphasis than filled text fields. They're often used in long forms where their reduced emphasis helps simplify the layout." link-label link-url should-open-link-in-new-tab="false">outlined text fields</app-froala-tooltip-element> in one section and <app-froala-tooltip-element description="Filled text fields have more visual emphasis than outlined text fields. They're often used in dialogs and short forms where their style draws more attention." link-label link-url should-open-link-in-new-tab="false">filled text fields</app-froala-tooltip-element> in another.</p>

Mobile UI of a contact form with several filled text fields, and an open dialog on top using an outlined text field. 

<p>When using both variants of text fields in a UI, separate them by region</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx31vnye-7_do.png?alt=media

Mobile UI of a contact form with a mix of outlined and filled text fields.

<p>When using both variants of text fields, don't use both next to each other or within the same form</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx31vw2z-8_dont.png?alt=media

<h2 id="isPasted">Anatomy</h2>

<h3 id="isPasted">Filled text field</h3>

Diagram of filled text field indicating the 10 parts of its anatomy.

<ol class="decimal"><li><p>Container</p></li><li><p>Leading icon (optional)</p></li><li><p>Label text in empty field</p></li><li><p>Label text in populated field</p></li><li><p>Trailing icon (optional)</p></li><li><p>Focused active Indicator</p></li><li><p>Caret</p></li><li><p>Input text</p></li><li><p>Supporting text (optional)</p></li><li><p>Enabled active Indicator</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2j3kn4a-9.png?alt=media

<h3 id="isPasted">Outlined text field</h3>

Diagram of an outlined text field indicating the 9 parts of its anatomy.

<ol class="decimal"><li><p>Enabled container outline</p></li><li><p>Label text in empty field</p></li><li><p>Leading icon (optional)</p></li><li><p>Label text in populated field</p></li><li><p>Trailing icon (optional)</p></li><li><p>Focused container outline</p></li><li><p>Caret</p></li><li><p>Input text</p></li><li><p>Supporting text (optional)</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm2j3kqed-10.png?alt=media

<h3>Containers</h3><p id="isPasted">Containers improve the discoverability of text fields by creating contrast between the text field and surrounding content.</p><p><strong>Fill and stroke</strong><br />A text field container has a fill and a stroke either around the entire container, or just the bottom edge. The color and thickness of a stroke can change to indicate when the text field is active. </p><p><strong>Rounded corners</strong><br />The container of an outlined text field has rounded corners, while the container of a filled text field has rounded top corners and square bottom corners.</p>

Side by side view of the containers of a filled and outlined text field.

<p>Text field containers</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx31y44j-11.png?alt=media

<h3>Label text</h3><p id="isPasted">Label text tells people what information is requested. Every text field should have a label.</p><p>Label text should be aligned with the input text, and always visible. It can be placed in the middle of a text field, or rest near the top of the container.</p><p>Label text shouldn't be truncated or take up multiple lines. Keep it short, clear, and fully visible.</p>

Animation of 2 text field’s label text changing position when empty and populated.

Label text should always be visible. When the field is selected, the label text moves from the middle of the text field to the top.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32tcjs-GM3-Components-TextFields-Guidelines-1-v01.mp4?alt=media

Text field with very long label text, too long to display fully display inside the text field container.

Don’t truncate label text. Keep it short, clear, and fully visible.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx31ykco-13_dont.png?alt=media

Text field with very long label text split into 2 lines. 

<p>Label text shouldn’t take up multiple lines</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx320mke-14_dont.png?alt=media

<h3>Adjacent label</h3><p id="isPasted">A text field doesn't require a label if the field's purpose is indicated by a separate, adjacent label. </p><p>Adjacent labels should be aligned to the leading edge of the text field container.</p>

Mobile UI of a contact form with label texts placed outside and on top of the text fields. 

<p>Text fields with adjacent labels</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32132w-15.png?alt=media

<h3>Required text indicator</h3><p id="isPasted"><span style="white-space:pre-wrap" id="isPasted">To show a field is required, display an asterisk (*) next to the label text, and explain that asterisks indicate required fields in one of two ways:</span></p><ul><li><span style="white-space:pre-wrap">Supporting text<br /></span></li><li><span style="white-space:pre-wrap">A single note at the beginning of the form</span></li></ul><p><span style="white-space:pre-wrap">Additional best practices include:<br /></span></p><ul><li><span style="white-space:pre-wrap">Indicate all required fields<br /></span></li><li><span style="white-space:pre-wrap">If required text has a particular color, use the same color for the asterisk</span></li></ul>

Mobile UI of a contact form showing supporting text below the text field, indicating an input is required. 

<p><span style="white-space:pre-wrap">Asterisk with required supporting text</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx322ilp-16.png?alt=media

<h3>Input text</h3><p id="isPasted">Input text is text a person has entered into a text field.</p><p>Text fields can display input text in the following ways:</p><ul><li><strong>Single line</strong> text fields display only one line of text</li><li><strong>Multi-line</strong> text fields grow to accommodate multiple lines of text</li><li><strong>Text areas</strong> are fixed-height fields</li></ul>

Text field with populated input text. 

<p>Input text in a filled text field</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx322ww5-17.png?alt=media

Text field with very long input text that scrolls sideways. 

<p>In <strong>single-line</strong> fields, as the cursor reaches the right field edge, text longer than the input line automatically scrolls left. Single-line fields are not suitable for collecting long responses; use a multi-line text field or text area instead.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32tu4z-GM3-Components-TextFields-Guidelines-2-1-v01.mp4?alt=media

Text field with very long input text that wraps into a second line, expanding the text field container. 

<p>In <strong>multi-line</strong> fields, overflow text causes the text field to expand, shifting screen elements downward and text wraps onto a new line. These fields initially appear as single-line fields, which is useful for compact layouts that need to accommodate large amounts of text.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32uir5-GM3-Components-TextFields-Guidelines-2-2-v01.mp4?alt=media

Text area with enough space to allow a very long input text to wrap into a second line without the need to expand the container.

<p><strong>Text areas</strong> are taller than text fields and wrap overflow text onto a new line. They are a fixed height and scroll vertically when the cursor reaches the bottom of the field. The large initial size indicates that longer responses are possible and encouraged. These should be used instead of multi-line fields on the web. Ensure the height of a text area fits within mobile screen sizes.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32usx4-GM3-Components-TextFields-Guidelines-2-3-v01.mp4?alt=media

<h3>Prefix text</h3><p>Text fields can contain prefix text such as currency symbol.</p>

Text field with a currency prefix before the input text. 

<p>A text field with a currency symbol text prefix</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx323bkz-21.png?alt=media

<h3>Suffix text</h3><p>Text fields can contain suffix text such as unit of measurement or email domain.</p>

Text field with a suffix after the input text indicating a maximum input of 100. 

<p>A text field with a grading scale as suffix</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx323jpq-22.png?alt=media

Text field with a suffix after the input text indicating an email address. 

<p>A text field with an email domain suffix</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx3246iw-23.png?alt=media

<h3>Supporting text &amp; character counter</h3><p id="isPasted">Supporting text conveys additional information about the input field, such as how it will be used. It should ideally be one line, though may wrap to multiple lines if required. It can be either persistently visible or visible only on focus.</p><p>If there is a character or word limit, include a character or word counter. They display the ratio of characters used and the total character limit.</p>

A side by side view of a text field with supporting text aligned with the trailing side, and a character counter aligned with the trailing side. 

<ol><li>Supporting text</li><li>Character counter</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx324ofo-24.png?alt=media

<h3>Error text</h3><p id="isPasted">For text fields that validate their content such as passwords, replace supporting text with error text. Swapping supporting text with error text prevents new lines of text from bumping content and changing the layout.</p><ul><li>If only one error is possible, error text should describe how to avoid the error</li><li>If multiple errors are possible, error text should describe how to avoid the most likely error</li></ul>

Mobile UI of a sign up form indicating a invalid entry, and a hint on how to resolve as supporting text below the container. 

<p>Swap supporting text with error text</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32v93h-GM3-Components-TextFields-Guidelines-3-1-v01.mp4?alt=media

Mobile UI of a sign up form with an invalid text field entry. The regular supporting text remains above the error message. 

<p>Don't add error text in addition to supporting text, as their appearance will shift content</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32vmu8-GM3-Components-TextFields-Guidelines-3-2-v01.mp4?alt=media

Mobile UI of a sign up form with an invalid text field entry. The error message wraps to 2 lines. 

<p>Long errors can wrap to multiple lines if there isn't enough space to clearly describe the error. In this case, ensure padding between text fields is sufficient to prevent multi-lined errors from bumping layout content.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx325xha-27_caution.png?alt=media

<h3>Error icon</h3><p id="isPasted">It’s strongly recommended to show an error icon when the text field is in the error state. </p><p>This highlights the error for people with visual impairments, and provides an additional sensory indicator.</p>

2 text fields with error messages. The active text field has a thicker border. Both text fields have a trailing error icon.

<p>The error icon is an important second visual indicator that a text field has an error</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm5vj8xje-28.png?alt=media

<h3>Icons &amp; images</h3><p id="isPasted">Icons in text fields are optional. Text field icons can: </p><ul><li>Describe valid <app-froala-tooltip-element description="Inputs are devices that provide interactive control of an app. Common inputs are a mouse, keyboard, and touchpad." link-label link-url should-open-link-in-new-tab="false">input</app-froala-tooltip-element> methods such as a microphone icon</li><li>Provide affordances to access additional functionality such as clearing the content of a field</li><li>Express an error</li></ul><p>Leading and trailing icons change their position based on LTR or RTL contexts.</p><p>Images that are 24dp in height can be placed inside of text fields. This image height allows for optimal top and bottom padding within the field and is consistent with icon size recommendations.</p>

<ol><li dir="ltr" id="isPasted"><strong>Icon signifier <br /></strong>Icon signifiers can describe the type of input a text field requires, and be touch targets for nested components. For example, a calendar icon may be tapped to reveal a <app-froala-tooltip-element description="Date pickers let people select a date, or a range of dates." link-label="More on date pickers" link-url="/m3/pages/date-pickers/overview" should-open-link-in-new-tab="true">date picker</app-froala-tooltip-element>.</li><li dir="ltr"><strong>Valid or error icon<br /></strong>Iconography can indicate both valid and invalid inputs, making error states clear for colorblind users. </li><li dir="ltr"><strong>Clear icon<br /></strong>Clear icons let a person clear an entire input field. They appear only when input text is present.</li><li dir="ltr"><strong>Voice input icon<br /></strong>A microphone icon signifies that people can input characters using voice. </li><li dir="ltr"><strong>Dropdown icon<br /></strong>A dropdown arrow indicates that a text field has a nested <app-froala-tooltip-element description="Selection lets users choose specific items to act on." link-label="More on selection" link-url="/m3/pages/selection" should-open-link-in-new-tab="true">selection</app-froala-tooltip-element> component.</li><li dir="ltr"><strong>Image<br /></strong>An image can help contextualize the required input text such as a credit card number.</li></ol>

Side by side view of text fields with different icons and images as trailing elements within the container. 

<ol><li>Icon signifier</li><li>Valid or error icon </li><li>Clear icon </li><li>Voice input icon</li><li>Dropdown icon</li><li>Image</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx3270td-28.png?alt=media

<h3>Read-only fields</h3><p><span style="white-space:pre-wrap">Read-only text fields display pre-filled text that people cannot edit. </span></p><p><span style="white-space:pre-wrap">A read-only text field is styled the same as a regular text field and is clearly labeled as read-only.</span></p>

Read only filled text field. 

<p>A filled read-only text field</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32b33u-29.png?alt=media

Read only outlined text field. 

<p>An outlined read-only text field</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32b91b-30.png?alt=media

<h2>Adaptive design</h2><p>As layouts adapt to larger screens and different <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoints</app-froala-tooltip-element>, apply flexible container dimensions to text fields. Set minimum and maximum values for <app-froala-tooltip-element description="Margins are the spaces between the edge of a nested element and its parent element, such as the space between a button's label text and the edge of its container." link-label="More on margins" link-url="/m3/pages/understanding-layout/spacing#38a538d7-991f-4c39-8449-195d32caf397" should-open-link-in-new-tab="true">margins</app-froala-tooltip-element>, padding, and container dimensions as layouts scale so that typography adjusts for better reading experiences.</p>

UI for creating a new album in a side by side view on mobile and tablet. 

<p>For compact breakpoints, text fields can span the full width of the display. For medium and expanded breakpoints, text fields should be bound by flexible margins or other containers.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32c2h0-Full%20to%20max%20-%201P.png?alt=media

<p id="isPasted">As text fields expand in fluid layouts, avoid maintaining fixed margins and typography properties. This can lead to extra long text fields. </p><p>For example, text fields should not span the full width of a large screen.</p>

Tablet UI with text fields spanning the complete width of the screen. 

<p>Don’t use fixed text field margins on large devices. Text fields shouldn’t span the full width of a large screen.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32d5ny-responsive-layout-dont.png?alt=media

<h3>Density</h3><p><span style="white-space:pre-wrap">Dense text fields enable people to scan and take action on large amounts of information.</span></p>

Tablet UI with desne text field as part of event creation form. 

<p>A form with dense text fields</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32dfqc-31.png?alt=media

<h4 id="isPasted"><strong>Avoid applying density by default</strong></h4><p>Don't apply density to text fields by default. This lowers their targets below the recommended 48x48 CSS pixels. Instead, give people a way to choose a higher density, like selecting a denser layout or changing the theme.</p><p>To ensure this density setting can be easily reverted when it's active, keep all the targets to change it at a minimum of 48x48 CSS pixels each.</p>

## Accessibility

<h2 id="isPasted"><span style="white-space:pre-wrap">Use cases</span></h2>

<p><span style="white-space:pre-wrap">User should be able to:</span></p><ul><li><span style="white-space:pre-wrap">Navigate to and activate a text field with assistive technology</span></li><li><span style="white-space:pre-wrap">Input information into the text field</span></li><li><span style="white-space:pre-wrap">Receive and understand supporting text and error messages</span></li><li><span style="white-space:pre-wrap">Navigate to and select interactive icons</span></li></ul>

<h2><span style="white-space:pre-wrap">Interaction &amp; style</span></h2>

<p>The containers for both <app-froala-tooltip-element description="Filled text fields have more visual emphasis than outlined text fields. They're often used in dialogs and short forms where their style draws more attention." link-label link-url should-open-link-in-new-tab="false">filled</app-froala-tooltip-element> and <app-froala-tooltip-element description="Outlined text fields have less visual emphasis than filled text fields. They're often used in long forms where their reduced emphasis helps simplify the layout." link-label link-url should-open-link-in-new-tab="false">outlined text fields</app-froala-tooltip-element> provide the same functionality. Changes to color and thickness of stroke help provide clear visual cues for interaction.</p>

2 filled text fields in enabled empty state and in focused populated state have visual cues to identify their state.

<p>Filled text fields</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmtsdrr40-01.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ueFOTTaBZqSJw0sLrnS0-JLzMtDWg-4J7Ot0sn6SkEiXvbCZ7l3OFYNhv1NlzBfKYVD7RzDXuo_ySEsBH7IEiBF_TnqAr16URqNt5-uWfmU=s656

2 outlined text fields in enabled empty state and in focused populated state have visual cues to identify their state.

<p>Outlined text fields</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmtsdstko-02.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/0s1xBLUmS9DAStbieTHQwGKQq42pyoUiZdSTjlczK97CYRbrKPV58n7m02pcCtSY4XlgiRyv3WRHfZuF7_cSq9SF8pX2uoUNW3zTzU-nQkFp=s656

<p><span style="white-space:pre-wrap">Containers improve the discoverability of text fields by creating contrast between the text field and surrounding content. <br /><br />In some contexts, outlined text fields can improve the perception of the fields with a 3:1 or greater contrast ratio between the container outline and the background.<br /></span></p>

An outlined text field with label text that passes the minimum contrast of 3:1.

<p id="isPasted">Make sure the container outline has a minimum contrast of 3:1 to the background<br /></p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32k7wf-3.png?alt=media

An outlined text field with label text fails the minimum 3:1 contrast.

<p>Don't choose colors that won't pass Material's minimum contrast of 3:1</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32kef6-4.png?alt=media

<h2><span style="white-space:pre-wrap">Keyboard navigation</span></h2>

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="width:24.1156%"><div style="text-align:center">Keys</div></th><th style="width:75.8844%"><div style="text-align:center">Actions</div></th></tr></thead><tbody><tr><th style="width:24.1156%;text-align:left">Tab</th><td><span style="white-space:pre-wrap">Focus lands on (non-disabled) text field</span></td></tr></tbody></table></div>

<h2><span style="white-space:pre-wrap">Labeling elements</span></h2>

<p>If the UI text is correctly linked, assistive tech (such as a screenreader) will read the UI text followed by the component’s role.<br /><br />The <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> label for a text field is the same as the text field label.</p>

The text field  and accessibility label both read “Email.” The role is “textbox.”

<p><span style="white-space:pre-wrap">A text field’s label should include its UI text</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32ks8b-5.png?alt=media

<p><span style="white-space:pre-wrap">For text fields with interactive trailing icons, the accessibility label clarifies its function.</span></p><p><span style="white-space:pre-wrap">For example, when a password is hidden, the label for the view icon is "Show password," and when the password is visible, the label is "Hide password."<br /><br />When an icon has no actionable role, like an error icon, the label is "Error."</span></p>

The trailing icon’s accessibility label “Show Password.” The role is “Button.”

<p><span style="white-space:pre-wrap">When a trailing icon in the field acts as a button, the label should clarify function, while the role explains the component type</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32l5y8-6.png?alt=media

<p>The prefix and suffix of a text field provides symbols and abbreviations to help users enter the correct values. <br /> <br />The <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> label for prefix and suffix needs to have a unique id attribute, for example, the currency name for a currency symbol prefix.</p>

Text field accessibility labels “UI text” are “Euro” for a currency prefix and “At gmail dot com” for the email address suffix.

<p><span style="white-space:pre-wrap">A form containing fields with both a prefix for currency, and a suffix for email address</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32leg0-7.png?alt=media

<p><span style="white-space:pre-wrap">When there is an error, "alert" is applied to the role and the error message to the text label.</span></p><p><span style="white-space:pre-wrap">If a text field displays both supporting text and error text, the label should include the supporting text first, followed by the error text.</span></p>

The text field accessibility labels is: UI text “Not a valid ZIP code.” The role is “Alert.”

<p><span style="white-space:pre-wrap">Text field error messages should be given an “alert” role in accessibility labels</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32lojq-8.png?alt=media

<p><span style="white-space:pre-wrap">The accessibility label for the character counter clarifies the number of characters that can be entered into the text field. </span></p>

A character counter's accessibility label  reads: UI text (“Character count, 5/20”)

<p><span style="white-space:pre-wrap">The remaining character counter should be called “character count” within the label</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32m4pa-9.png?alt=media

<p><span style="white-space:pre-wrap">The text displayed in the supporting text is also used for its accessibility label.</span></p>

The accessibility label uses the supporting text. It reads: UI text (“Please use the company email address”). Role [No role].

<p><span style="white-space:pre-wrap">Text field supporting text should have its own accessibility label</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32meu7-10.png?alt=media

<p><span style="white-space:pre-wrap">If a text field requires input, indicate so with an asterisk at the end of the text field label. The accessibility label must include the asterisk.</span></p>

Accessibility label reads: UI text (“Username*”).  The role is “Textbox.”

<p><span style="white-space:pre-wrap">A required text field’s accessibility label should include any supporting text</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flx32mlzg-11.png?alt=media
