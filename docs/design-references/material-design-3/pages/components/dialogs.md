# Dialogs

Source: https://m3.material.io/components/dialogs
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/79c01ab5-d09a-4f6c-9aca-f76d310583bc.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Use dialogs to make sure users act on information</p></li><li><p>Two variants: <app-froala-tooltip-element description="Basic dialogs interrupt users with urgent information, details, or actions. They're often used for alerts, quick selection, or confirmation." link-label="More on basic dialogs" link-url="/m3/pages/dialogs/guidelines#97ac3858-3932-4084-ae8e-73e42b7cb752" should-open-link-in-new-tab="true">basic</app-froala-tooltip-element> and <app-froala-tooltip-element description="Full-screen dialogs fill the entire screen, displaying actions that require a series of tasks to complete. They're often used for creating a calendar entry." link-label="More on full-screen dialogs" link-url="/m3/pages/dialogs/guidelines#007536b9-76b1-474a-a152-2f340caaff6f" should-open-link-in-new-tab="true">full-screen</app-froala-tooltip-element></p></li><li><p>Should be dedicated to completing a single task</p></li><li><p>Can also display information relevant to the task</p></li><li><p>Commonly used to confirm high-risk actions like deleting progress</p></li></ul>

Basic and full-screen dialog.

<ol><li>Basic dialog</li><li>Full-screen dialog</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fml9yk7iw-01.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/6kWyLPu-M7uuqJv2DLtnQd6MuRy2S5Pu5MzM-Q54y9MiOOFlX-2CLU9r1lATTgQLiUR7hUB2pBSVzT5qyoe9A3T1TWQ-3WOG9V50IM33Jkt3fg=s2048

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/160bdd9a0f6fe596

libraryModuleType: STATUS_TABLE

<h2>Differences from M2</h2>

<ul><li>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></li><li><app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/google-material-3/pages/understanding-layout/overview" should-open-link-in-new-tab="true">Layout</app-froala-tooltip-element>: Greater padding to account for the increased corner-radius and title size</li><li>Position: Option for custom <app-froala-tooltip-element description="Basic dialogs interrupt users with urgent information, details, or actions. They're often used for alerts, quick selection, or confirmation." link-label="More on basic dialogs" link-url="/m3/pages/dialogs/guidelines#97ac3858-3932-4084-ae8e-73e42b7cb752" should-open-link-in-new-tab="true">basic dialog </app-froala-tooltip-element>positioning</li><li>Shape: Increased corner-radius</li><li>Typography: Larger and darker headline</li></ul>

Basic dialog with rounded corner, larger headline.

<p>New updates to color, layout, position, shape, and typography</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fml9ykeuk-02.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/q8W8RpwCCScus4cQl-dtCeOGIWywtLjjCh3cFLmwYvEpaaKbny2HwDpi7qmX4qLlO9nOlnP5F0TYG8TozuGaZNbIis9Nu2zoaa806nkO-Wo=s1352

## Specs

<h2>Tokens &amp; specs</h2><p>Select a component variant below to see its elements, attributes, <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">tokens</app-froala-tooltip-element>, and their values.</p>

resourceName: designSystems/20543ce18892f7d9/components/0b1e39a67d5bafdc

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Dialog - Basic', 'Dialog - Full screen'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2 id="isPasted">Basic dialogs</h2>

Anatomy diagram numbering dialog elements.

<ol><li>Container</li><li>Icon (optional) </li><li>Headline (optional)</li><li>Supporting text </li><li>Divider (optional) </li><li>Button label text</li><li>Scrim</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmk29t71i-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/8zwGCq50u42Pisi3XIhquY9uN3sTnFAYcLYzdMcQ-7RGPou4Uyy5QzWjN3NWXlHALJhtxMM-lECAxX1_duYupPka9gdFn-THeTzCdggkOUit=s2048

<h3 id="isPasted">Basic dialog color</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview">Learn more about design tokens</a></p>

Color mapping diagram labeling 6 color roles across the dialog and scrim.

<p id="isPasted">Basic dialog color roles used for light and dark themes:</p><ol><li>Surface container high </li><li>Secondary </li><li>On surface </li><li>On surface variant</li><li>Primary </li><li>Scrim</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fml9yledn-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/OaqvzKCkUteypP4OIa5ABlelFupDNk5XXyc8cxl0SYBNXCJPqROSqNWKjvxWk1FJpSzOwqADZvwMhPgqsgj5tbMKKdvS8L1YWWmSvJ-sDi2K=s2048

<h3>Basic dialog measurements</h3>

Annotated diagram showing padding values.

<p>Basic dialog padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fml9ynrkv-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/0b11O-Tlquj7LEzCkk4IOw1EuhHgUI6KmNyMozEEr2aANs_Q3FshFNUhXzUkn2c3occn1_9y1XSndIceqhSPiMyAT4g5lr6xwcWZtqCvpNdnHw=s2048

<div class="table-wrapper"><table style="border:none;border-collapse:collapse;width:100%"><thead><tr><th style="text-align:center">Attribute</th><th style="text-align:center">Value</th></tr></thead><tbody><tr><th>Container shape<br /></th><td>28dp corner radius</td></tr><tr><th>Container height<br /></th><td>Dynamic</td></tr><tr><th>Container width<br /></th><td>Min 280dp; Max 560dp</td></tr><tr><th>Divider height<br /></th><td>1dp</td></tr><tr><th>Icon size<br /></th><td>24dp</td></tr><tr><th>Minimum width<br /></th><td>280dp </td></tr><tr><th>Maximum width<br /></th><td>560dp</td></tr><tr><th>Alignment with icon<br /></th><td>Center-aligned</td></tr><tr><th>Alignment without icon<br /></th><td>Start-aligned</td></tr><tr><th>Top/Left/right/bottom padding<br /></th><td>24dp</td></tr><tr><th>Padding between buttons<br /></th><td>8dp</td></tr><tr><th>Padding between title and body<br /></th><td>16dp</td></tr><tr><th>Padding between icon and title<br /></th><td>16dp</td></tr><tr><th>Padding between body and actions<br /></th><td>24dp</td></tr></tbody></table></div>

<h2 id="isPasted">Full-screen dialogs</h2>

Diagram numbering 6 full-screen dialog elements.

<ol><li>Container </li><li>Header </li><li>Icon (close affordance) </li><li>Headline (optional) </li><li>Text button </li><li>Divider (optional)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm9h7yor0-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/DkDLF7N_cYRseSctPY0mcn5UU3s5M37UtbNZCMovSLfZacqNP1ZR-1ur4muZ0RXpZAxdcqi65q7Uc7GRZiLumQhf54hpWiUNMxgJbJNEIzc8RQ=s2048

<h3 dir="ltr" id="isPasted">Full-screen dialog color</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value.</p>

Color mapping diagram shows 5 callout markers across the dialog.

<p id="isPasted">Full-screen dialog color roles used for light and dark themes:</p><ol><li>Surface container high </li><li>On surface</li><li>On surface</li><li>Primary</li><li>On surface variant</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm9h7z23b-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/i7xYaPoPLi48zudMGabAj82oZQLxetMFg4YojUXfY9GlrVVdonnVQurEssQzX0LHqABfe9QcTts3lMtKa_-jYDektbV8HGkmAIKkiDuF573F8g=s2048

<h3 id="isPasted">Full-screen dialog measurements</h3>

Diagram noting layout measurements for padding values, title, height, and action regions.

<p>Full-screen dialog padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmafq2x4i-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/5vPLkkKzW-CnlkhE29h4YwG8QzCsM7QdxQpOS0hRO82Ox4D7VqBbZgPWKd2nHnj916gkB29tjl7k_fnuuffRyMGOmS9Xg_MJpMIsMWY-Meo=s2048

<div class="table-wrapper"><table style="border:none;border-collapse:collapse;width:100%"><thead><tr><th style="text-align:center">Attribute</th><th style="text-align:center">Value</th></tr></thead><tbody><tr><th>Container shape<br /></th><td>0dp corner radius</td></tr><tr><th>Container height<br /></th><td>Dynamic</td></tr><tr><th>Container width<br /></th><td>Container width; Max 560dp</td></tr><tr><th>Header height<br /></th><td>56dp</td></tr><tr><th>Header width<br /></th><td>Container width</td></tr><tr><th>Headline text alignment<br /></th><td>Start-aligned</td></tr><tr><th>Divider height<br /></th><td>1dp</td></tr><tr><th>Icon (close affordance) size<br /></th><td>24dp</td></tr><tr><th>Bottom action bar height<br /></th><td>56dp</td></tr><tr><th>Bottom action bar width<br /></th><td>Container width</td></tr><tr><th>Top/left/right padding<br /></th><td>24dp</td></tr><tr><th>Padding between elements<br /></th><td>8dp</td></tr></tbody></table></div>

## Guidelines

Basic dialog in isolation

<p>A basic dialog</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sf9qay-01.png?alt=media

<h2 id="isPasted">Usage</h2>

<p dir="ltr" id="isPasted">A dialog is a modal window that appears in front of app content to provide critical information or ask for a decision. Dialogs disable all app functionality when they appear, and remain on screen until confirmed, dismissed, or a required action has been taken.</p><p dir="ltr">Dialogs are purposefully interruptive, so they should be used sparingly. A less disruptive alternative is to use a dropdown <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element>, which provides options without interrupting a user’s experience.</p>

Diagram of basic and full-screen dialogs.

<p>There are two variants of dialogs:</p><ol class="decimal"><li><p>Basic dialog</p></li><li><p>Full-screen dialog</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfc7pz-02.png?alt=media

Dialog in front of app content.

<p>Use dialogs for prompts that block an app’s normal operation, and for critical information that requires a specific user task, decision, or acknowledgement</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfcqhr-03_do.png?alt=media

Low-priority dialog in front of app content.

<p>Don’t use dialogs for low- or medium-priority information. Instead use a snackbar, which can be dismissed or disappear automatically.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfdc9w-03_dont.png?alt=media

<h3 id="isPasted">Similar components</h3><p><app-froala-tooltip-element description="Snackbars show short updates about app processes at the bottom of the screen." link-label="More on snackbars" link-url="/m3/pages/snackbar/overview" should-open-link-in-new-tab="true">Snackbars</app-froala-tooltip-element> are also designed to show important messages.</p><p>Choose the right component based on the importance of the message. This component messaging strategy helps avoid overusing dialogs.</p>

Snackbar on a phone saying that new photos were synced to the device. No buttons exist.

<p>Snackbars can disappear automatically</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmk29xmfo-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/XLiUu7mOltTNoUojZheRl95_BXn_O9vc9-PwyzL2W_vZPBccPC1bntpTZ6KwgzKDMDt8UGih90E9GPDGd-uyGWZz0eqLMZOItywMT-yiDxS7=s1352

<div class="table-wrapper"><table class="borderGGrey300" style="width:100%"><thead><tr><th><div style="text-align:center"><strong id="isPasted">Component</strong></div></th><th><div style="text-align:center"><strong id="isPasted">Importance</strong></div></th><th><div style="text-align:center"><strong id="isPasted">Action needed</strong></div></th></tr></thead><tbody><tr><td>Snackbar</td><td>Low importance</td><td>Optional: Snackbars may not have a <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">button</app-froala-tooltip-element>, and can disappear automatically</td></tr><tr><td>Dialog</td><td>High importance</td><td>Required: Dialogs block the main content until an action is confirmed</td></tr></tbody></table></div>

<h2 id="isPasted">Anatomy</h2><h3>Basic dialog</h3>

Diagram of 7 elements of basic dialog.

<ol><li>Container</li><li>Icon (optional)</li><li>Headline (optional)</li><li>Supporting text</li><li>Divider (optional)</li><li>Buttons label text</li><li>Scrim</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfhos4-07.png?alt=media

<h3 id="isPasted">Full-screen dialog</h3>

6 elements of full-screen dialog.

<ol><li>Container</li><li>Header region</li><li>Icon (close affordance)</li><li>Headline (optional)</li><li>Button label text</li><li>Divider (optional)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfick9-08.png?alt=media

<h3 dir="ltr" id="isPasted">Container and scrim</h3><p dir="ltr">Dialog containers appear above other screen elements and hold the dialog’s headline, text, <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element> items.</p><p dir="ltr">To focus attention on the dialog, surfaces behind the container are scrimmed with a temporary overlay to make them less prominent.</p>

Basic dialog shown above a scrim overlay that reduces the prominence of the background elements.

<p>Basic dialogs appear over a background scrim</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfkf69-09.png?alt=media

<h3 dir="ltr" id="isPasted">Headline (optional)</h3><p dir="ltr">A dialog’s purpose should be communicated by its headline and buttons or actionable items.</p><p dir="ltr">Headlines should:</p><ul><li>Contain a brief, clear statement or question</li><li dir="ltr">Avoid apologies (“Sorry for the interruption”), alarm (“Warning!”), or ambiguity (“Are you sure?”)</li></ul>

Dialog title asking “Use location service?”

<p>This dialog title poses a specific question, concisely explains what’s involved in the request, and provides clear actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfl8j1-10_do.png?alt=media

Dialog title asking “Are you sure?”

<p>Don’t use dialog titles that pose an ambiguous question</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sflmm0-11_don't.png?alt=media

<p dir="ltr" id="isPasted">Headlines should always be succinct. They can wrap to a second line if necessary, and be truncated.</p><p dir="ltr">In full-screen dialogs, long headlines or headlines of variable lengths (such as translations), can be placed in the content area instead of the app bar.</p>

Example full-screen dialog with truncated long headline.

<p>Avoid placing long headlines in a full-screen dialog’s app bar (1), as the truncated text may lead to misunderstanding</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfm2yt-12_Caution.png?alt=media

Example full-screen dialog with short headline, and longer text in content area.

<p>Find ways to shorten app bar text, and place longer headlines into the content area (1) of a full-screen dialog</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfmezr-13_do.png?alt=media

<h3 dir="ltr" id="isPasted">Buttons </h3><p dir="ltr">Dialog actions are most often represented as <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element> and allow users to confirm, dismiss, or acknowledge something.</p><p dir="ltr">Buttons are aligned to the trailing edge of the dialog for easier interaction. The confirmation button is always closest to the edge. </p><p dir="ltr">Button alignment responds automatically for right-to-left languages, where the confirmation button is aligned to the left edge.</p>

Dialog with the confirmation button disabled because a required radio selection is missing.

<p>Disable confirming actions (1) until a choice is made. Dismissive actions are never disabled.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfmqqd-14_do.png?alt=media

Dialog with the dismissing action "Cancel" on the right of the 2 buttons.

<p>Don’t place dismissive actions (1) to the right of confirming actions. Instead, place them to the left of confirming actions.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfn276-15_don't.png?alt=media

Dialog with a single-action button: “OK”.

<p>A single action may be provided only if it’s an acknowledgement</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfq9tm-16_do.png?alt=media

Dialog with 2 button choices: “Cancel”, “Got it”.

<p>Avoid presenting people with unclear choices. <strong>Cancel</strong> doesn't make sense here because no clear action is proposed.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfqm2i-17_don't.png?alt=media

<p dir="ltr" id="isPasted">Dialogs should contain a maximum of two actions.</p><ul><li dir="ltr">If a single action is provided, it must be an acknowledgement action</li><li dir="ltr">If two actions are provided, one must be a confirming action, and the other a dismissing action</li></ul>

Dialog with 2 buttons side-by-side: “Disagree”, “Agree”.

<p>Display two text buttons next to one another</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfqzp1-18_do.png?alt=media

Dialog with 2 stacked buttons: “Turn on speed boost”, “No thanks”.

<p>Stacked buttons accommodate longer button text, but take up more room. Confirming actions appear above dismissive actions.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfre4i-19_caution.png?alt=media

<p dir="ltr" id="isPasted">Providing a third action, such as <strong>Learn more</strong>, is not recommended as it navigates the user away from the dialog, leaving the dialog task unfinished.</p><p dir="ltr">Rather than adding a third action, an inline expansion can display more information. If more extensive information is needed, provide it prior to entering the dialog.</p>

Dialog with 3 text buttons: Learn more, Disagree, Agree.

<p>The <strong>Learn more</strong> action (1) navigates away from this dialog, potentially leaving it in an indeterminate state</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfrskh-20.png?alt=media

<h2 id="isPasted">Basic dialog</h2><p>Basic dialogs interrupt users with urgent information, details, or actions. Common use cases for basic dialogs include alerts, quick <app-froala-tooltip-element description="Selection lets users choose specific items to act on." link-label="More on selection" link-url="/m3/pages/selection" should-open-link-in-new-tab="true">selection</app-froala-tooltip-element>, and confirmation. </p>

Example of basic dialog action request.

<p>Basic dialogs require a person to take action before it will close</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfumns-21.png?alt=media

Example of basic dialog confirmation.

<p>Basic dialogs can give people the ability to provide confirmation of a choice before committing to it</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfuxlx-22.png?alt=media

<p>Basic dialogs most often appear as alerts or <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">lists</app-froala-tooltip-element>, but can have a variety of <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/understanding-layout/overview" should-open-link-in-new-tab="true">layouts</app-froala-tooltip-element> and component combinations, including lists, <app-froala-tooltip-element description="Date pickers let people select a date, or a range of dates." link-label="More on date pickers" link-url="/m3/pages/date-pickers/overview" should-open-link-in-new-tab="true">date pickers</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Time pickers help users select and set a specific time." link-label="More on time pickers" link-url="/m3/pages/time-pickers/overview" should-open-link-in-new-tab="true">time pickers</app-froala-tooltip-element>.</p>

Date picker dialog.

<p>Date picker dialogs allow people to tap a date, then confirm it by tapping <strong>OK</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfzk1g-23.png?alt=media

Time picker dialog.

<p>Time picker dialogs allow people to move the clock hand and then confirm by tapping <strong>OK</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sfxxnd-24.png?alt=media

<h2 id="isPasted">Full-screen dialog</h2>

<p dir="ltr" id="isPasted">Full-screen dialogs fill the entire screen, containing actions that require a series of tasks to complete. One example is creating a calendar entry with the event title, date, location, and time.</p><p dir="ltr">Because they take up the entire screen, full-screen dialogs are the only dialogs over which other dialogs can appear.</p><p dir="ltr">Use a <a href="/m3/pages/motion-transitions/transition-patterns#b67cba74-6240-4663-a423-d537b6d21187">container transform</a> pattern to transition a <app-froala-tooltip-element description="Floating action buttons (FABs) help people take primary actions." link-label="More on FABs" link-url="/m3/pages/fab/overview" should-open-link-in-new-tab="true">FAB</app-froala-tooltip-element> into a full-screen dialog.</p>

A FAB transitioning into a full-screen dialog.

<p>Full-screen dialogs contain actions that require a series of tasks to complete</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmbh08c2v-GM3_Dialogs_Guidelines_25_IA_v02.mp4?alt=media

<p dir="ltr" id="isPasted">When a full-screen dialog is closed without being saved, a basic dialog appears in front of it to confirm <app-froala-tooltip-element description="Selection lets users choose specific items to act on." link-label="More on selection" link-url="/m3/pages/selection" should-open-link-in-new-tab="true">selections</app-froala-tooltip-element> should be discarded without saving changes.</p>

Closing a full-screen dialog triggers a basic dialog asking to discard the changes.

<p>A basic modal dialog appears when a full-screen dialog is closed without being saved</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmbh098mh-GM3_Dialogs_Guidelines_26_IA_v01.mp4?alt=media

<p>Full-screen dialogs may be used for content or tasks that meet any of these criteria:</p><ul type="disc" style="list-style-type:disc"><li><p>Dialogs that include components which require keyboard <app-froala-tooltip-element description="Inputs are devices that provide interactive control of an app. Common inputs are a mouse, keyboard, and touchpad." link-label link-url should-open-link-in-new-tab="false">input</app-froala-tooltip-element>, such as form fields</p></li><li><p>When changes aren’t saved instantly</p></li><li><p>When components within the dialog open additional dialogs</p></li></ul><p>Full-screen dialogs are for <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoints</app-froala-tooltip-element> only, like mobile devices. For medium and <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints</app-froala-tooltip-element>, use a basic dialog.</p>

<h3><span style="white-space:pre-wrap" id="isPasted">Saving selections</span></h3>

<p><span style="white-space:pre-wrap" id="isPasted">To save a selection in a full-screen dialog, use <strong>Save</strong>.  The close icon or dismissive action, such as <strong>Cancel</strong> or <strong>Back</strong>, should close the dialog.</span></p>

<h3><span style="white-space:pre-wrap" id="isPasted">Confirmation</span></h3>

<p>The confirmation action should be clear about what happens next, like <strong>Send</strong> or <strong>Create</strong>. Avoid using vague terms like <strong>Done</strong>, <strong>OK</strong>, or <strong>Close</strong>. Only trigger an additional basic dialog if the action fails. Don’t <app-froala-tooltip-element description="A disabled state communicates an inoperable component or element." link-label="More on disabled state" link-url="/m3/pages/interaction-states/applying-states#4aff9c51-d20f-4580-a510-862d2e25e931" should-open-link-in-new-tab="true">disable</app-froala-tooltip-element> the confirmation button.</p>

Full-screen dialog with create button as confirmation action.

<p><span style="white-space:pre-wrap">A <strong>Create</strong> button is clear that the event will be created</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sg5wkr-27_do.png?alt=media

Full-screen dialog with an additional basic dialog asking if you want to create this event.

<p><span style="white-space:pre-wrap">Don’t trigger a basic dialog when the confirming action is selected</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sg67kv-28_don't.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Dismissing</span></h3>

<p><span style="white-space:pre-wrap" id="isPasted">When someone dismisses a full-screen dialog, a basic dialog should appear to confirm that they want to discard the unsaved changes.</span></p>

A basic dialog with options to either keep editing or discard unsaved changes.

<p><span style="white-space:pre-wrap">Use a basic dialog to confirm that the user wants to discard unsaved changes</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sg91cq-29_do.png?alt=media

A full-screen dialog with a Close button as the confirming action.

<p><span style="white-space:pre-wrap">Don’t use the confirming action to dismiss the full-screen dialog</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sg9bz5-30_don't.png?alt=media

<h3><span style="white-space:pre-wrap" id="isPasted">Error messages</span></h3>

<p>Errors about the dialog fields should always appear inline where they occur. Some components like <app-froala-tooltip-element description="Text fields let users enter text into a UI." link-label="More on text fields" link-url="/m3/pages/text-fields/overview" should-open-link-in-new-tab="true">text fields</app-froala-tooltip-element> have built-in error messaging, while others like <app-froala-tooltip-element description="Checkboxes let users select one or more items from a list, or turn an item on or off." link-label="More on checkboxes" link-url="/m3/pages/checkbox/overview" should-open-link-in-new-tab="true">checkboxes</app-froala-tooltip-element> and <app-froala-tooltip-element description="Radio buttons let people select one option from a set of options." link-label="More on radio buttons" link-url="/m3/pages/radio-button/overview" should-open-link-in-new-tab="true">radio buttons</app-froala-tooltip-element> need error messages to be added next to the fields.<span style="white-space:pre-wrap"><br /><br />General errors such as network issues preventing saving or submitting should appear in a basic dialog when the confirming action fails.<br /><br />Error messages should clearly but briefly explain the source of the error and how to fix it. Show all errors on the page at once so people can fix everything before trying again.</span></p>

A full-screen dialog with inline error messages for text fields.

<p><span style="white-space:pre-wrap">Error messages related to the fields should be displayed inline</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sg9nzm-31_do.png?alt=media

A basic dialog mentioning that entries were not saved due to a connection issue.

<p><span style="white-space:pre-wrap">Errors unrelated to the fields can be displayed in a basic dialog</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sg9xoh-32_caution.png?alt=media

<h3 dir="ltr" id="isPasted">Dialog windows</h3><p dir="ltr">Launching a full-screen dialog temporarily resets the app’s perceived elevation, allowing simple <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menus</app-froala-tooltip-element> or dialogs to appear above the full-screen dialog. They cover the screen and don’t appear as a floating modal window.</p><h3 dir="ltr">Navigation</h3><p dir="ltr">Because full-screen dialogs can only be completed, dismissed, or closed, the close “X” icon button should be the only navigation option in the <app-froala-tooltip-element description="App bars display information and actions at the top of a screen." link-label="More on app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">app bar</app-froala-tooltip-element>.</p>

<h2 id="isPasted">Adaptive design</h2>

<p>Dialogs can swap variants as the <app-froala-tooltip-element description="Breakpoints are opinionated window sizes where a layout changes to match available space, device conventions, and ergonomics (previously window size classes)." link-label="More on breakpoints" link-url="/m3/pages/breakpoints" should-open-link-in-new-tab="true">breakpoint</app-froala-tooltip-element> changes. For example, a <app-froala-tooltip-element description="Full-screen dialogs fill the entire screen, displaying actions that require a series of tasks to complete. They're often used for creating a calendar entry." link-label="More on full-screen dialogs" link-url="/m3/pages/dialogs/guidelines#007536b9-76b1-474a-a152-2f340caaff6f" should-open-link-in-new-tab="true">full-screen dialog</app-froala-tooltip-element> can change into a <app-froala-tooltip-element description="Basic dialogs interrupt users with urgent information, details, or actions. They're often used for alerts, quick selection, or confirmation. " link-label="More on basic dialogs" link-url="/m3/pages/dialogs/guidelines#97ac3858-3932-4084-ae8e-73e42b7cb752" should-open-link-in-new-tab="true">basic dialog</app-froala-tooltip-element> at larger breakpoints.</p>

Example of full-screen dialog on left, simple dialog on right

<ol><li>Full-screen dialog on mobile</li><li>Dialog on a tablet</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sgbmj3-33.png?alt=media

<h3>Medium breakpoint</h3><p>Basic dialogs appear in a center position by default.<br /><br />Their position can be overridden to provide a more ergonomic experience.</p>

Basic dialog on tablet photos app.

Dialog custom positioned on the right side of the screen

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sgc676-34.png?alt=media

<h3>Expanded breakpoint</h3><p>Dialogs on <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints</app-froala-tooltip-element>, like desktop, are modal windows above a scrim. This puts the dialog at the forefront of a person's view, calling attention to the action prompted in the dialog.</p>

Example of desktop dialog.

<p>Desktop dialogs call attention to the required action</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sgj2r1-35.png?alt=media

<p dir="ltr" id="isPasted"><span>Basic dialogs can be custom-positioned anywhere on larger screens, respecting <app-froala-tooltip-element description="Margins are the spaces between the edge of a nested element and its parent element, such as the space between a button's label text and the edge of its container." link-label="More on margins" link-url="/m3/pages/understanding-layout/spacing#38a538d7-991f-4c39-8449-195d32caf397" should-open-link-in-new-tab="true">margins</app-froala-tooltip-element> to prevent edge collision.</span></p>

Basic dialog position diagram.

<p>Custom placement area for basic dialogs that respects a 56dp margin from the edges of the screen</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sgjir4-36.png?alt=media

<h2>Behavior</h2>

<h3 dir="ltr" id="isPasted">Appearing</h3><p dir="ltr">Dialogs appear without warning, requiring users to stop their current task. They should be used sparingly, as not every choice or setting warrants interruption.</p><p dir="ltr">Dialogs use an <a href="/m3/pages/motion-transitions/transition-patterns#e1c2a650-d7a4-4a6d-9025-e6b7845291ed" id="isPasted" rel="noopener noreferrer" target="_blank">enter and exit</a> transition pattern to appear on screen.</p>

Dialog entering and exiting screen using fade transition.

<p>A dialog appears with an enter and exit transition</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmbh0yk3u-GM3_Dialogs_Guidelines_37_IA_v01.mp4?alt=media

<h3 dir="ltr" id="isPasted">Position</h3><p dir="ltr">Dialogs retain focus until dismissed or an action has been taken, such as choosing a setting. They shouldn’t be obscured by other elements or appear partially on screen, with the exception of full-screen dialogs.</p>

A basic dialog covering a full-screen dialog.

<p>Dialogs shouldn’t be obscured by other elements except for full-screen dialogs</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sgqe15-38.png?alt=media

<h3>Scrolling</h3><p>Most dialog content should avoid scrolling. Even when scrolling is required, the dialog title is pinned at the top, with <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element> pinned at the bottom. This ensures selected content remains visible alongside the title and buttons, even upon scroll.</p><p>Dialogs don’t scroll with elements outside of the dialog, such as the background.</p>

Example of fixed dialog title and buttons.

<p>When viewing a scrollable list of options, the dialog title and buttons remain fixed</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmbh0z34p-GM3_Dialogs_Guidelines_39_IA_v01.mp4?alt=media

<h3 dir="ltr" id="isPasted">Dismissing</h3><p dir="ltr">To close a dialog used as an alert, one of its actions must be selected.</p><p dir="ltr">Other dialogs may be dismissed by:</p><ul><li>Tapping a <strong>Cancel</strong> button, if one is shown</li><li>Selecting an actionable list item</li><li>Pressing the keyboard <strong>Esc</strong> key</li><li>Tapping the scrim (Android, iOS)</li><li>Tapping the Android system <strong>Back</strong> button</li><li>Using another standard cancel or escape action, such as iOS VoiceOver escape gesture</li></ul><p dir="ltr">If the user’s ability to dismiss a dialog is disabled, the user must choose a dialog action to proceed.</p>

Example of dialog alert

<p>Dismissing a dialog alert involves selecting an action</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fktug7t17-3_Mid.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/B7aiYo5IM932EzqTfX7bkS08Ebciat0LGJWQg8PM6ZD1tl7iIqXm2lmUyfQ56VoXLoaTaNmMuVgsSg5QLBA6q67v88RUwONUL0LfX01m5LU9=s676

<p dir="ltr" id="isPasted">When a dialog box is dismissed, the following transitions occur:</p><ul><li dir="ltr">The dialog box fades out</li><li dir="ltr">The background scrim fades out</li></ul>

Example of dialog box fading out

<p>When dismissed, a dialog box fades out along with the background scrim</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fktug7t17-3_Mid.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/B7aiYo5IM932EzqTfX7bkS08Ebciat0LGJWQg8PM6ZD1tl7iIqXm2lmUyfQ56VoXLoaTaNmMuVgsSg5QLBA6q67v88RUwONUL0LfX01m5LU9=s676

## XR

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">This is a rapidly changing space. Guidelines are primarily intended for designers at this time. Find what’s implemented in code in the <a href="https://www.figma.com/community/file/1035203688168086460" target="_blank" rel="noopener noreferrer">design kit</a>.</div></div></div>

<p>Extended reality (XR) introduces spatial capabilities, such as using depth to make dialogs stand out from the background. Currently, spatial dialogs are only available in <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components. " link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element>. For <app-froala-tooltip-element description="Home space is compatible with mobile and large screen apps, but doesn’t support spatial components." link-label="More on home space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">home space</app-froala-tooltip-element>, follow Material’s general <a href="/m3/pages/dialogs/guidelines#b33988d3-88e6-432c-acb1-4461a84171c9" target="_blank" rel="noopener noreferrer">dialog guidance</a>.</p>

<h2>Color &amp; elevation</h2>

<p>XR uses <a href="/m3/pages/color-roles/tab-1#89f972b1-e372-494c-aabc-69aea34ed591" target="_blank" rel="noopener noreferrer">color roles</a> to communicate the elevation of UI elements. Dialogs can use two color options: <strong>surface container high</strong> or <strong>surface container highest</strong>.  </p>

<div class="fr-banner note"><div class="fr-banner-icon" contenteditable="false">star</div><div class="fr-banner-content note"><div class="fr-banner-label" contenteditable="false">Note:</div><div class="fr-banner-description">Color and elevation for spatial dialogs can be customized by makers and are not available in Jetpack Compose yet.</div></div></div>

2 spatially elevated dialogs with surface-container-high and surface-container-highest color roles.

<ol class="decimal"><li>Surface container high</li><li>Surface container highest</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadfali7-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/U8ru72wkyiSvzWy1y-npuQelcvHDdGcI1Vl7Xgqc_aWt4IUs9oV4OWehS7OmyV02GUXJtr4AecKrDRvQouwJ5IU5uZCLsn0JZ3hLdN-Gc50=s2048

<p>For effective visual hierarchy, a dialog should be the most prominent element. <br /><br />Add a scrim behind a dialog to improve its visibility. Scrims prevent other content from being selected until the dialog action is complete.</p>

Dialog with surface-container-highest color and a scrim.

<p><span style="white-space:pre-wrap">Make sure a spatial dialog’s color is higher than all other UI elements, and use a scrim</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmalezhon-02-do.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/UbfenXJcmu7EicBwP5t7vLK-_9MtCoLkTyK5F8ymjYpGivp0AC72Od_07R3T5LAJoNbfKJEjekcjCEwcpkD6f0dpZNNe2-clKr4EqMr_WN2G=s1506

<p>The dialog should have the highest elevation in the product.</p><p>For example, if a dialog is <strong>surface container high</strong>, don’t use <strong>surface container highest</strong> for any other elements.</p>

Dialog with surface-container-high color and no scrim. An orbiter is at a higher elevation than the dialog.

<p>If a dialog’s color is <strong>surface container high</strong>, don’t use <strong>surface container highest</strong> for any other element</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmalezlwb-03-dont.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/uJQx6_YXe-_Z0MiBZZ2qGdoidQ8CCUrsVGhmD1ta9wRV0HESD-TgVPnxz_LHTFI2aOElt4PxTd8Am9oUBQTWt4TAlIeuy7SLbxkzkY3Jw1z3=s1506

<h2><span style="white-space:pre-wrap" id="isPasted">Usage</span></h2>

<p><a href="/m3/pages/dialogs/guidelines#97ac3858-3932-4084-ae8e-73e42b7cb752" target="_blank" rel="noopener noreferrer">Basic dialogs</a> are recommended when designing for XR’s expanded window sizes. This keeps the required action in the person’s <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place" target="_blank" rel="noopener noreferrer">field of view</a>. Limit use of <a href="/m3/pages/dialogs/guidelines#007536b9-76b1-474a-a152-2f340caaff6f" target="_blank" rel="noopener noreferrer">full-screen dialogs</a> to compact window sizes, like mobile devices.</p>

Basic dialog in XR.

<p>A basic dialog elevated above an app in home space </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadfk9dk-04.png?alt=media

Full-screen dialog in XR.

<p>Avoid using full-screen dialogs in XR. Required actions could appear beyond a person’s field of view.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadfn41n-05.png?alt=media

<h2>Spatial dialogs</h2>

<p>In <app-froala-tooltip-element description="Full space is Android XR’s immersive mode and supports spatial components. " link-label="More on full space" link-url="https://developer.android.com/design/ui/xr/guides/foundations#modes" should-open-link-in-new-tab="true">full space</app-froala-tooltip-element>, dialogs can be <app-froala-tooltip-element description="Spatial elevation displays a component above an app on the Z-axis." link-label="More on spatial elevation" link-url="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation " should-open-link-in-new-tab="true">elevated spatially</app-froala-tooltip-element> via <a href="https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design#use-enablexrcomponentoverrides" target="_blank" rel="noopener noreferrer">overrides</a>. This helps dialogs stand out from their background in XR.</p>

Side view of basic dialog showcasing spatial elevation.

<p><span style="white-space:pre-wrap">Side view of a basic dialog with spatial elevation in full space</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadfqce4-06.png?alt=media

<h2><span style="white-space:pre-wrap" id="isPasted">Behavior</span></h2>

<h3 id="isPasted">Effect</h3><p>The spatial dialog should scale uniformly. It also fades in when appearing, and fades out when disappearing. <br /><br />The dialog's scrim only fades in and out.</p>

A direct view of a spatial dialog appearing and disappearing.

<p>Front view of a spatial dialog in motion in full space</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadfydkq-XR_Dialog_Behavior_01_IA_v02%20.mp4?alt=media

<h3 id="isPasted">Movement</h3><p>When activated, the spatial dialog rises from the app to the highest resting level on the Z-axis. </p><p><span style="white-space:pre-wrap" id="isPasted">When the action is complete, it returns to a normal resting level.</span></p><p>The dialog's scrim stays at the app content level at all times. <br /><br />To prevent motion sickness, use <a href="/m3/pages/motion-easing-and-duration/tokens-specs#601d5552-a6e6-4d74-9886-ff8f24b9ec35" target="_blank" rel="noopener noreferrer">standard easing</a> and <a href="/m3/pages/motion-easing-and-duration/tokens-specs#48bf653e-46f9-48f5-87e0-eaf8ea3fe716" target="_blank" rel="noopener noreferrer">long duration</a> motion tokens.</p>

A spatial dialog elevating on the Z-axis, as seen from a side angle.

<p>Side view of a spatial dialog in motion in full space</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadg0a4h-XR_Dialog_Behavior_02_IA_v02%20.mp4?alt=media

<h2><span style="white-space:pre-wrap" id="isPasted">Placement</span></h2>

<p>Consider factors like field of view, viewing distance, and possible interactions when deciding where to place dialogs in XR.</p>

<h3 id="isPasted">Elevation: highest resting level</h3><p>Display spatial dialogs at the highest resting level. When setting the depth value of the highest resting level, make sure the elevated dialog is at a comfortable viewing distance from the person. <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation" target="_blank" rel="noopener noreferrer">More on spatial elevation</a></p>

An animated side view of a dialog moving from the lowest to the highest resting level.

<p>A spatial dialog moves to the highest resting level in full space</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadg3ndl-GM3_XR_Dialogs_Motion_Placement_01_IA_v03.mp4?alt=media

<h3 id="isPasted">Center spatial dialogs in field of view</h3><p>Spatial dialogs should be centered in a person’s <a href="https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place" target="_blank" rel="noopener noreferrer">field of view</a>. If the dialog <strong>can't</strong> track head movements, position it in the center of the app’s content. </p><p>If the dialog <strong>can</strong> track head movements, configure it with a lazy follow behavior. This keeps the dialog anchored to the center of a person’s field of view until an action is taken.</p>

A dialog follows a person’s head movements, remaining centered in their field of view.

<p>A dialog in full space stays centered in a person’s field of view</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmadg6ja9-GM3_XR_Dialogs_Motion_Placement_02_IA_v05.mp4?alt=media

<h2>Accessibility considerations</h2>

<p><a href="https://developer.android.com/design/ui/xr/guides/get-started#make-app" target="_blank" rel="noopener noreferrer">XR accessibility</a> guidelines are still evolving. Spatial dialogs should follow applicable Material <a href="/m3/pages/dialogs/accessibility" target="_blank" rel="noopener noreferrer">dialog accessibility standards</a>.</p>

## Accessibility

<h2>Use cases</h2>

<p>People should be able to use assistive technology to:</p><ul><li>Open and close a dialog</li><li>Provide and submit other inputs if the dialog is interactive, such as a <app-froala-tooltip-element description="Text fields let users enter text into a UI." link-label="More on text fields" link-url="/google-material-3/pages/text-fields/overview" should-open-link-in-new-tab="true">text field</app-froala-tooltip-element> or selectable <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/google-material-3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element></li><li>Scroll the dialog to access all of its contents if that content extends beyond the container of the dialog</li></ul>

<h2><span style="white-space:pre-wrap">Interaction &amp; style</span></h2>

<h3>Use sparingly</h3><p id="isPasted">Dialogs are purposefully interruptive. This means they appear in front of app content and disrupt the flow of content for people who may, for example, be using a screen reader to navigate the page.</p><p>As such, dialogs should be used sparingly and only to provide critical information. Less critical information should be presented in a non-blocking way within the flow of app content.</p>

An inline tooltip doesn’t block a photo app’s content on a mobile screen.
A modal dialog blocks the content of a photo app on a mobile screen.

Present non-critical information using other UI within the flow of app content

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sgve0z-01_do.png?alt=media

A modal dialog blocks the content of a photo app on a mobile screen.
A modal dialog blocks the content of a photo app on a mobile screen.

Avoid putting non-critical information in a dialog

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sgvt7t-02_don't.png?alt=media

<h3>200% text size</h3><p>Avoid excessive text wrapping or truncation by choosing concise strings. </p><p>On Android, headlines should be kept concise enough to fit within <strong>four</strong> lines after the text size is increased to 200%. If a headline exceeds this limit and gets truncated, provide an alternative way to access the full content in a single tap.</p>

A dialog with 200% text wraps multiple times in the header and description. It covers most of the mobile screen.

<p>Avoid excessive text wrapping or truncation by choosing concise strings</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sh8mb2-03_caution.png?alt=media

<h3 id="isPasted"><span style="white-space:pre-wrap">Elements within dialogs</span></h3><p>Because dialogs can contain various elements within them, refer to the relevant <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview/principles" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> guidelines for each element. <br /><br />Some common examples include:</p><ol><li><app-froala-tooltip-element description="Text fields let users enter text into a UI." link-label="More on text fields" link-url="/m3/pages/text-fields/overview" should-open-link-in-new-tab="true">Text fields</app-froala-tooltip-element></li><li><app-froala-tooltip-element description="Material's typography follows a type scale with accessibility considerations baked in." link-label="More on typography" link-url="/m3/pages/text-fields/accessibility" should-open-link-in-new-tab="true">Typography</app-froala-tooltip-element></li><li><app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/google-material-3/pages/common-buttons/overview" should-open-link-in-new-tab="true">Buttons</app-froala-tooltip-element></li></ol>

3 elements of a full-screen dialog.

<p>Full-screen dialogs can contain various elements such as (1) text fields, (2) typography, and (3) buttons, which each may have their own accessibility guidelines</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8x3m4cu-04.png?alt=media

<h2><span style="white-space:pre-wrap">Initial focus</span></h2>

<p><span style="white-space:pre-wrap">When a dialog appears, focus should automatically land on the first interactive element within the dialog.</span></p>

A modal dialog titled “Permanently delete?” whose second interactive element is focused by selecting the Tab key.

Initial focus lands on the first interactive element within a dialog. The tab key moves focus through the next interactive elements in a cycle.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8wqpp2r-05.png?alt=media

A modal dialog titled “Permanently delete?” whose previous interactive element is focused on by selecting both the Shift and Tab keys.

The shift and tab keys together move focus in the opposite direction. The space or enter key triggers or commits the action of the focused element.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8wqq56l-06.png?alt=media

<h2><span style="white-space:pre-wrap">Keyboard navigation</span></h2>

<div class="table-wrapper"><table style="width:100%" class="fr-table-selection-hover"><thead><tr><th style="width:20.2899%">Keys</th><th style="width:79.5893%">Actions</th></tr></thead><tbody><tr><th>Tab</th><td>Focus lands on the next interactive element contained in the dialog, or the first element if focus is currently on the last element</td></tr><tr><th>Shift + Tab<br /></th><td>Focus lands on the previous interactive element contained in the dialog, or the last element if focus is currently on the first element</td></tr><tr><th>Space or Enter<br /></th><td>Triggers or commits the action of the <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/google-material-3/pages/interaction-states/applying-states#bfc1624f-6bcc-4306-b0c1-425e2d8a1bf9" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element> element</td></tr><tr><th>Escape<br /></th><td>Closes the dialog</td></tr></tbody></table></div>

<h2><span style="white-space:pre-wrap">Labeling elements</span></h2>

<p>The <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview/principles" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> label for a dialog is typically the same as the dialog’s title or headline.</p><p><span style="white-space:pre-wrap">On web, basic dialogs should have the <strong>alert dialog</strong> role.</span></p>

An alert dialog with a title “Set up traffic updates?”  Its label is “Set up traffic updates?” and its role as “Alert Dialog.”

<p>Basic dialogs are known as alert dialogs on web</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmk2a1j0z-07.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/lBX7M9XMiL98P1lM9cobZ7GLCzqaLJANo3iKDKkfG_RQRKbKZepzwsjLHXEDveGR3zjduX9QaCz-UIsW7qyHc2TqlHp_B-4RSR1BrYnZAPh-iw=s1352

<p><span style="white-space:pre-wrap">Components contained within the dialog, such as buttons, should be labeled according to the guidelines specific to those components.<br /></span></p><p id="isPasted">For common examples, see:</p><ul><li><app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/specs" should-open-link-in-new-tab="true">Buttons</app-froala-tooltip-element></li><li><app-froala-tooltip-element description="Text fields let users enter text into a UI." link-label="More on text fields" link-url="/m3/pages/text-fields/overview" should-open-link-in-new-tab="true">Text fields</app-froala-tooltip-element></li></ul>

A full-screen dialog titled “New event” containing a “Save” button and a text field, both with their own accessibility labels.

<p>Elements within a dialog should be labeled according to their guidelines</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmk2a20m5-08.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/XhxNfz1cPdhx_FBTjgzNKRYc047mN_rLn5N3jQsdL7OCeMe61us_nf42-JVISOD0ZDkjPuXfKLMkPbfxfxPVEBmDdG_L2P1TvSx72RXXkGUV=s1352
