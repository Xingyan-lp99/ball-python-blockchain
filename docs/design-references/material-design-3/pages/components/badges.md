# Badges

Source: https://m3.material.io/components/badges
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/e18a73ff-b00d-46e7-af20-ab9dd24bf579.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Can contain labels or numbers</p></li><li><p>Two variants: <app-froala-tooltip-element description="Small badges are a simple circle used to indicate an unread notification." link-label link-url should-open-link-in-new-tab="false">small</app-froala-tooltip-element> and <app-froala-tooltip-element description="Large badges contain label text communicating item count information." link-label link-url should-open-link-in-new-tab="false">large</app-froala-tooltip-element></p></li><li><p>Anchor badges inside the icon bounding box, at the upper trailing edge of the icon</p></li><li><p>Limit content to four characters, including a <strong>+</strong></p></li><li><p>Keep the default color mapping</p></li></ul>

3 icons with badges. 1 is a small dot. 2 is a larger circle with a 1 digit number. 3 is an oval with a 4 digit number.

<ol class="decimal"><li>Small badge on a navigation item</li><li>Large badge on a navigation item</li><li>Large badge with max characters on a navigation item</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme8hopxl-01.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/69586a0d0e3bfa32

libraryModuleType: STATUS_TABLE

<h2>Differences from M2</h2>

<ul><li><p>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element><br /></p></li></ul>

Navigation bar showing 4 icons with different badge variants in a bright red color.

<p>Badges have new color mappings</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme8hz0r2-02.png?alt=media

## Specs

5 aspects of badge anatomy on a navigation bar.

<p>Navigation bar</p><ol><li id="isPasted">Small badge</li><li>Large badge container</li><li>Large badge label</li><li>Large badge maximum character count container</li><li>Large badge maximum character count label</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmamlcpos-1-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/1c2wjkW2_C9l1HmNkRT8GpeQ7WqSDcJdMKdNym4xk_wPBfFSgVP3NhSXBwBV52vI3L-Z7CAmnY7c-1WM1I9xfyj4EfI_ucXRgOhWSRvfLy5E=s1004

5 aspects of badge anatomy on a navigation rail.

<p>Navigation rail</p><ol><li>Small badge</li><li>Large badge container</li><li>Large badge label</li><li>Large badge maximum character count container</li><li>Large badge maximum character count label</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmamlee0o-2-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/9yjKmecr7ZJh2Tm71DBDcwftLy2cMEpCW2yl73CCr7kUctUtmKaW78yFdO-0ZUSBXShJh9CDLZtQhcOyVt9CmdNhywVGvneguYneZMeui26j=s1004

<h2>Tokens &amp; specs</h2><p>Browse the component elements, attributes, tokens, and their values.</p>

resourceName: designSystems/20543ce18892f7d9/components/59a1b3a9a90ca8b3

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2 id="isPasted"><span style="white-space:pre-wrap">Color</span></h2>

<p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview" id="isPasted">Learn more about design tokens</a></p>

5 applications of badge color on light and dark theme navigation bars.

<p id="isPasted">Badge color roles used for light and dark schemes in navigation bar:</p><ol><li>Error</li><li>Error</li><li>On error</li><li>On error</li><li>Error</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmg0yc68n-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/GXqQAaWohBPLwvJAZUGaxFwy8CI_R4BLcAXPDq-e4P67CObmbEHL-GzwJbo6hBOmuqFuoV8QrPMXhmL2Zfca9_o5bTyMbxGhVxeM1Fwf7KU=s1004

5 applications of badge color on light and dark theme navigation rails.

<p id="isPasted">Badge color roles used for light and dark schemes in navigation rail:</p><ol><li>Error</li><li>On error</li><li>Error</li><li>On error</li><li>Error</li></ol><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flz9ep1tz-4.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/8-bcqHO-CggN9L5OTiWVxPDT-wPzcurO0xXI7dZeo5htfXRjDwMnoMl_Qco9Z8NGG9CE2_5qrO2QdLV-nmieRVopeqNZeeHavE0GJqJpLRA=s1004

<h2>Measurements</h2>

Annotation of badge sizes, padding, and measurements from the corner of the icon to the badge opposite corner.

<p>Badge padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flz9eqf8f-badge_layout-correct.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/_9tsQOYHX4YH6bQJJwi1ylkI-nu2RJBNb84ivjXE8ksTqqpuE4w-riSO17Sh2gclSOMxjzlDHS_B2zKmb7uBo3Y1ZBPiLWi6UoHlHOAK9Zw=s2048

<div class="table-wrapper"><table style="width:100%;margin-right:calc(0%)"><thead><tr><th style="text-align:center;width:50.045%"><p id="isPasted">Attribute</p></th><th style="text-align:center;width:49.8651%"><p id="isPasted">Value</p></th></tr></thead><tbody><tr><td><p id="isPasted">Small badge shape</p></td><td><p id="isPasted">3dp corner radius</p></td></tr><tr><td><p id="isPasted">Small badge size (HxW)</p></td><td><p id="isPasted">6dp</p></td></tr><tr><td><p id="isPasted">Large badge shape</p></td><td><p id="isPasted">8dp corner radius</p></td></tr><tr><td><p id="isPasted">Large badge one digit size (HxW)</p></td><td><p id="isPasted">16dp</p></td></tr><tr><td><p id="isPasted">Large badge max character count size (HxW)</p></td><td><p id="isPasted">16x34dp</p></td></tr><tr><td><p id="isPasted">Small badge: distance from top trailing icon corner to bottom leading badge corner (HxW)</p></td><td><p id="isPasted">6x6dp</p></td></tr><tr><td><p id="isPasted">Large badge: distance from top trailing icon corner to bottom leading badge corner (HxW)</p></td><td><p id="isPasted">14x12dp</p></td></tr><tr><td><p id="isPasted">Large badge padding between badge and text container</p></td><td><p id="isPasted">4dp</p></td></tr></tbody></table></div>

<h2 id="isPasted">Configuration</h2>

<p>Different badges are shown on navigation destinations in various <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">states.</app-froala-tooltip-element></p>

Diagram of 3 badge variations shown on navigation destinations in various states.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flz9eqsps-6.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/dmnjAmE1Ol38Ijd8REgLVSvLNv733cEX_WngU88yFKfiKjSdwanYmhHnCGueyMQAzJRxRMrvdgtC2KPaNzyG_B4Rn3ptMP-22440icqyFFKmFA=s2048

<ol><li id="isPasted"><span style="white-space:pre-wrap">Inactive with label - small badge</span></li><li><span style="white-space:pre-wrap">Inactive with label - large badge</span></li><li><span style="white-space:pre-wrap">Inactive with label - large badge max character count</span></li><li><span style="white-space:pre-wrap">Inactive - small badge</span></li><li><span style="white-space:pre-wrap">Inactive - large badge</span></li><li><span style="white-space:pre-wrap">Inactive - large badge max character count</span></li><li><span style="white-space:pre-wrap">Active with label - small badge</span></li><li><span style="white-space:pre-wrap">Active with label - large badge</span></li><li><span style="white-space:pre-wrap">Active with label - large badge max character count</span></li><li><span style="white-space:pre-wrap">Active nav bar no label - small badge</span></li><li><span style="white-space:pre-wrap">Active nav bar no label - large badge</span></li><li><span style="white-space:pre-wrap">Active nav bar no label - large badge max character count</span></li><li><span style="white-space:pre-wrap">Active nav rail no label - small badge</span></li><li><span style="white-space:pre-wrap">Active nav rail no label - large badge</span></li><li><span style="white-space:pre-wrap">Active nav rail no label - large badge max character count</span></li></ol>

## Guidelines

Diagram of 4 badges in different configurations on a navigation bar's destination icons.

<p>Large badges and a small badge in a navigation bar</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0wmkr4-01.png?alt=media

<h2>Usage</h2>

<p>Badges are used to indicate a notification, item count, or other information relating to a navigation destination. They are placed on the ending edge of icons, typically within other components.</p><p>There are two variants:</p><ol class="decimal"><li><p>Small badge</p></li><li><p>Large badge</p></li></ol>

Diagram of 4 badges in different configurations on a navigation bar's destination icons.

<p>Navigation bar with four badges</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0wmphl-02.png?alt=media

<p>A <strong>small badge</strong> is a simple circle, used to indicate an unread notification.  </p><p>A <strong>large badge</strong> contains label text communicating item count information.</p>

A small badge is a circle with no characters.

<p>Small badge</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi46ui92-03.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Xnibw8kAnTzaV0TmLVU5oOfL5xZTO6E8gxqFFo843YlClRZ3TI3eTR7cGtDL76c7_3oQ6xVKU3l7NV0PxnLeYgRw3ATNSz91ytruFjCWBNSIhw=s656

A large badge holds 4 characters and expands its container's width but not height.

<p>Large badge</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmi46uzu8-04.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/UiES3FVbu4QTgh3y8L-WfQz6q2u2ao86ZpjIGDu6CxAIgDLxmu7zM-RC33uLQPuDaUJtgI1qqck8tM_bdeOfiZYNPg-PBiIsJD-7QV6gyc3a=s656

<h3>With other components</h3><p>Badges are most commonly used within other components, such as <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element>, <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element>, <app-froala-tooltip-element description="App bars display navigation, actions, and text at the top of a screen." link-label="More on app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">app bars</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Tabs organize content across different screens and views." link-label="More on tabs" link-url="/m3/pages/tabs/overview" should-open-link-in-new-tab="true">tabs</app-froala-tooltip-element>.</p>

Navigation bar with 3 icon buttons. 2 icons buttons have badges and 1 doesn't.


<p>In navigation bars, hide the badge once the destination has been selected</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvm8dp3k-5.png?alt=media

<h2 id="isPasted">Anatomy</h2>

Small and large badges on 2 icon buttons.

<ol><li>Small badge</li><li>Large badge container</li><li>Large badge label</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvm8fkil-7.png?alt=media

<h2>Container</h2>

<p>There are two container options for the badge: </p><ul><li><p><app-froala-tooltip-element description="Small badges are a simple circle used to indicate an unread notification." link-label link-url should-open-link-in-new-tab="true">Small badge</app-froala-tooltip-element> with no text</p></li><li><p><app-froala-tooltip-element description="Large badges contain label text communicating item count information." link-label link-url should-open-link-in-new-tab="true">Large badge</app-froala-tooltip-element> with text</p></li></ul>

A small badge on a navigation item.


<p>A small badge uses only shape to indicate a status change or new notification</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0womos-07.png?alt=media

Number 10 displayed within large badge on a navigation item.

<p>A large badge displays a number within a container to indicate a quantifiable status change related to a destination</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme8jybps-08.png?alt=media

<p id="isPasted">Badge containers are anchored inside the icon bounding box. As the number count increases for <app-froala-tooltip-element description="Large badges contain label text communicating item count information." link-label link-url should-open-link-in-new-tab="true">large badges</app-froala-tooltip-element>, their width expands, but keeps the same placement.</p><p>Badges use a color intended to stand out against labels, icons, and navigation elements. Use the default color mapping to avoid color conflict issues. </p>

Small and large badges on the left side of 2 navigation items in a right-to-left language.

<p>Change the position of the badge for right-to-left languages</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme8k2962-9-do.png?alt=media

Small and large badges at random positions on 3 icon buttons on a navigation rail.

<p>Badges have fixed positions. Don’t change the position of the badge arbitrarily or place the badge over the icon.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme8k2vet-10-dont.png?alt=media

Small and large badges in default red color on 3 navigation items.

<p>Use the default badge color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0wr0gz-11_do.png?alt=media

Small and large badges in custom colors on 3 navigation items.

<p>Avoid using custom color roles for the badge container and label text. If custom roles are necessary, make sure they have contrast of at least 3:1.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0wr4mw-12_dont.png?alt=media

<h3>Label text</h3><p>Label <app-froala-tooltip-element description="Large badges contain label text communicating item count information." link-label link-url should-open-link-in-new-tab="true">large badges</app-froala-tooltip-element> with counts or a status. The maximum number of characters within large badge label text is four, including a + to indicate more.</p>

4 icons with increasing number badges. The badges represent quantities, using a "+" symbol for quantities over 999.

<p>Large badges with one to four characters</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme8ks60f-13.png?alt=media

<p>Use the recommended maximum character count to ensure labels don’t extend beyond the badge container.</p>

4-digit numbers condensed to a 3-digit badge with "+" to fit the badge container's width.

<p>Truncate badge labels as needed</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0wrqi2-14_do.png?alt=media

4-digit and 5-digit number badges on navigation items exceed the badge container's width and get cut off at the edge.

<p>Don’t let the badge get cut off or collide with another element</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0wru4w-15_dont.png?alt=media

<h2 id="isPasted">Placement</h2>

Large badge to the right of a navigation rail item.

<p>Use a large badge to show count information when visual collisions aren’t an issue, such as in a navigation rail</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0wsl1o-16_do.png?alt=media

Small badge on an icon button in an app bar.

<p>Use a small badge when spaces are tightly constrained, such as app bars. Small badges won’t run into the edge of the screen.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme8kxkle-17_caution.png?alt=media

Large badge placed at the end of a tab.

<p>When an icon with a badge is followed by text or another element, place a large badge at the trailing edge</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme8kyp7i-18_do.png?alt=media

Large badge overlapping the icon and text in a tab.

<p>Avoid using a large badge when it might overlap with a trailing element. Either place it at the trailing edge or use a small badge instead.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme8kzbcm-19_dont.png?alt=media

## Accessibility

<h2>Use cases</h2>

<p>People should be able to use assistive technology to<span style="white-space:pre-wrap">:</span></p><ul><li><span style="white-space:pre-wrap">Understand the dynamic information conveyed in badges, such as counts or labels</span></li><li><span style="white-space:pre-wrap">Address badge announcements by selecting corresponding navigation destinations</span></li></ul>

<h2>Interaction &amp; style</h2>

<p>Badges are most commonly used within other components, such as <app-froala-tooltip-element description="Navigation bars let people switch between UI views on smaller devices." link-label="More on navigation bars" link-url="/m3/pages/navigation-bar/overview" should-open-link-in-new-tab="true">navigation bar</app-froala-tooltip-element>, <app-froala-tooltip-element description="Navigation rails let people switch between UI views on mid-sized devices." link-label="More on navigation rails" link-url="/m3/pages/navigation-rail/overview" should-open-link-in-new-tab="true">navigation rail</app-froala-tooltip-element>, <app-froala-tooltip-element description="App bars display navigation, actions, and text at the top of a screen." link-label="More on app bars" link-url="/m3/pages/app-bars/overview" should-open-link-in-new-tab="true">app bars</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Tabs organize content across different screens and views." link-label="More on tabs" link-url="/m3/pages/tabs/overview" should-open-link-in-new-tab="true">tabs</app-froala-tooltip-element>.<br id="isPasted" /><br />When a badge is used to indicate an unread notification, the badge gets hidden once it's selected.</p>

An animation of a badge disappearing once it's tapped.

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvp03lg1-GM3-Components-Badges-Accessibility-1-v01.mp4?alt=media

<h2>Visual indicators</h2>

<p>Badges use a color intended to stand out against labels, icons, and navigation elements. Use the default color mapping to avoid color conflict issues.</p>

Diagram of large and small badges showing that they need to pass 3 to 1 contrast.

<p id="isPasted">Badges must use default color with at least 3:1 contrast</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0x2h51-02_do.png?alt=media

Diagram of large and small badges not passing 3 to 1 contrast.

<p>Avoid using custom color roles for the badge container and label text. If custom roles are necessary, make sure they have contrast of at least 3:1.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmg0x2kti-03_dont.png?alt=media

<h2 id="isPasted">Labeling elements</h2>

<p>The <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview/principles" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> label for a badge item will be read after its navigation destination. Any numerical badges will have their number read, while non-counting badges will simply announce <strong>New notification</strong>.</p>

Navigation bar highlighting numerical badge.

<p>Numerical badges will have their number read</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme8l8lhl-04.png?alt=media

Navigation bar highlighting non-counting badge.

<p>Non-counting badges will simply announce <strong>New notification</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme8l9na6-05.png?alt=media
