# Cards

Source: https://m3.material.io/components/cards
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/1a23fbe7-0474-444c-abfb-717bb148d3a8.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Use cards to contain related elements</p></li><li><p>Three variants: <app-froala-tooltip-element description="Elevated cards have a drop shadow, providing more separation from the background than filled cards, but less than outlined cards" link-label link-url should-open-link-in-new-tab="false">elevated</app-froala-tooltip-element>, <app-froala-tooltip-element description="Filled cards provide subtle separation from the background. This has less emphasis than elevated or outlined cards." link-label link-url should-open-link-in-new-tab="false">filled</app-froala-tooltip-element>, <app-froala-tooltip-element description="Outlined cards have a visual boundary around their container. This can provide greater emphasis than the other types." link-label link-url should-open-link-in-new-tab="false">outlined</app-froala-tooltip-element></p></li><li><p>Contents can include anything from images to headlines, supporting text, <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">lists</app-froala-tooltip-element></p></li><li><p>Can also contain other components</p></li><li><p>Cards have flexible <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/understanding-layout/overview" should-open-link-in-new-tab="true">layouts</app-froala-tooltip-element> and dimensions based on their contents</p></li></ul>

3 variants of cards

<ol><li id="isPasted">Elevated card</li><li>Filled card</li><li>Outlined card</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuilyza-1.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/4611eb61fa32c0e5

libraryModuleType: STATUS_TABLE

moduleConfigurationOverrides: {'headings': ['Type', 'Resource', 'Status']}

<h2>Differences from M2</h2>

<ul><li><p>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic-color/overview" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></p></li><li><p>Elevation: Lower elevation and no shadow by default</p></li><li><p>Variants: Three official card variants – <app-froala-tooltip-element description="Elevated cards have a drop shadow, providing more separation from the background than filled cards, but less than outlined cards" link-label link-url should-open-link-in-new-tab="false">elevated</app-froala-tooltip-element>, <app-froala-tooltip-element description="Filled cards provide subtle separation from the background. This has less emphasis than elevated or outlined cards." link-label link-url should-open-link-in-new-tab="false">filled</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Outlined cards have a visual boundary around their container. This can provide greater emphasis than the other types." link-label link-url should-open-link-in-new-tab="false">outlined</app-froala-tooltip-element></p></li></ul>

M3-style card

<p>Cards have updated colors, elevation, and variants</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuimnd8-2.png?alt=media

## Specs

<h2>Tokens &amp; specs</h2><p>Select a component variant below to see its elements, attributes, tokens, and their values.</p>

resourceName: designSystems/20543ce18892f7d9/components/100ebfb4332adab1

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Card - Elevated', 'Card - Filled', 'Card - Outlined'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', '3P', 'Android', 'Dark', 'Light'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Elevated card</h2>

Diagram indicating elevated card container.

<ol><li>Container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flx8i6cjo-1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/E3Vi9qZnejfvkANGxN7TTmb5Utn3gzxXo8tbngvR9A83WXhpvV-mK_p9erAn4wBXMFmFRXpw2SmD7N-mIEq_5nOkXuKc8LOzoFXj6Oa8G1lv=s2048

<p dir="ltr" id="isPasted">Default values (enabled state)</p><div align="left" dir="ltr" style="margin-left:0pt"><div class="table-wrapper"><table><thead><tr><th>Element<br /></th><th style="width:22.7941%">Design attribute<br /></th><th style="width:22.6103%">Role<br /></th><th>Token<br /></th></tr></thead><tbody><tr><th rowspan="3">1. Container<br /></th><td>Color</td><td>Surface container low</td><td><a href="/m3/pages/using-color/tokens#7fd4440e-986d-443f-8b3a-4933bff16646">md.sys.color.surface-container-low</a></td></tr><tr><td>Shadow color</td><td>Shadow</td><td><a href="/m3/pages/using-color/tokens#7fd4440e-986d-443f-8b3a-4933bff16646" id="isPasted">md.sys.color.shadow</a></td></tr><tr><td>Elevation</td><td>Level 1</td><td><a href="/m3/pages/elevation/tokens">md.sys.elevation.level1</a></td></tr></tbody></table></div></div>

<h3>Elevated card color</h3><p>Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview/" id="isPasted">Learn more about design tokens</a></p>

Color diagram indicating elevated card surface color.

<p id="isPasted">Elevated card color roles used for light and dark themes:</p><ol><li>Surface container low</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flx8i798w-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/gOvzxWalOCyRSRq6I8AqYgS6Y-XJlhBZ7VW82pxtb3dFUccU5LHnNcaccQ4BVnHcQflh6KOXqswxajoIj-v_9S6huJlw4kvNscb4UZN6Zb0=s2048

<h3>Elevated card states</h3><p>States are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states" id="isPasted">Learn more about interaction states</a></p>

Diagram of 5 elevated card states.

<p>Elevated card states: </p><ol><li>Hovered</li><li>Focused </li><li>Pressed </li><li>Dragged </li><li>Disabled</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8tathzk-3.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/8OD9zWeF6hOtcHP-XQEqSVrCYSmtOFcwnb19h4zkqIDtpszCMXho0opgebc5B_ukqbsOiK-Q_iMQoDf1Iz94KTS5kg3zH3qXyF8Ki9kZAo0_=s2048

<h2>Filled card</h2>

Diagram indicating filled card container.

<ol><li>Container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flx8i88xc-4.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/RbaHdHqyYyeHjx_eq4Kbjc4e3WWtYoHRrwqEg2mnQUhLVLjtwyp3KtjjaHrV6kdyFRPu5O26lbeXiQwSA3kQSGeiiggAit3rHjrWhadLuwCU=s2048

<h3 id="isPasted">Filled card color</h3><p>Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview/" id="isPasted">Learn more about design tokens</a></p>

Color diagram indicating filled card surface color.

<p id="isPasted">Filled card color roles used for light and dark themes:</p><ol><li>Surface container highest</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flx8i8kna-5.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/28sRV5HrMfndGdrvcX_VHMHcm9rf_kk7W_LC3Jom8_R9rtsrEJAMjjPVT552KXBmxiaMKszeZ5QenLT1ejk3anom5NgsKHr-02mDyG4VEuzl=s2048

<h3 id="isPasted">Filled card states</h3><p>States are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states" id="isPasted">Learn more about interaction states</a></p>

Diagram of 5 filled card states.

<p>Filled card states: </p><ol><li>Hovered</li><li>Focused </li><li>Pressed </li><li>Dragged </li><li>Disabled</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8taswqd-7.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/dyvw6FZH2BO4dAPsybP7VtJyu3dvPM_SK6YtHcXcFOSbUXx2KFiOganJcT29S4R85p3ZNem11PKaAFjRQLg4nGHjca0CLE2MF2N4t9vUn0E=s2048

<h2>Outlined card</h2>

Diagram indicating outlined card container and outline.

<ol><li>Container</li><li>Outline</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flx8ia1sc-8.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/mwuwAzgNXs1xArEeUNQ5ayKXGbsLGzverYdD2EPiqL9Nk2EoZb5LEVop_RyeltCreY-py6o6B5Ry1lndyG6bQ-7p8AvUYtNNmlu1D10dwqSU=s2048

<h3 id="isPasted">Outlined card color</h3><p>Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview/" id="isPasted">Learn more about design tokens</a></p>

Outlined card color roles in light and dark themes.

<p id="isPasted">Outlined card color roles used for light and dark themes:</p><ol><li>Surface</li><li>Outline variant</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flx8iah38-9.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/X8jbeHzsvv736FiatKGB2IOlsdiGVljvmrVCHUTgi0Au8RPx_aVvF1UMhbbjcAu--WnKD3LAWI4hLZiLmW9Q4oO0BkuSR4HpsAmpqleifMA=s2048

<h3 id="isPasted">Outlined card states</h3><p>States are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states" id="isPasted">Learn more about interaction states</a></p>

Diagram of 5 outlined card states.

<p>Outlined card states: </p><ol><li>Hovered </li><li>Focused </li><li>Pressed </li><li>Dragged </li><li>Disabled</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8taue2l-10.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/knnDmfc6SIH-85gkuLOhQRHJhvHpPRGu_OzMgaQMMtDnloC-fCR1jJl1PGG0AP72kt6sqmBKlZgIbQ80HKeubSnxa5_zUOYcA0-Ip1hiQV4=s2048

<h2>Measurements</h2>

Diagram with card layout measurements.

<p>Card padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Flx8ibavc-11.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/el_YhKWDFNMsVV51gm6oChPgPeNh4NiZU7_jdajUv38w5rT3nVlzDXfArepuPH38d1er7SCslFJyrf-KaBtIap102w7_CFnOj_BVu43S-ds=s2048

<div class="table-wrapper"><table><thead><tr><th style="text-align:center">Attribute<br /></th><th style="text-align:center">Value<br /></th></tr></thead><tbody><tr><th>Shape<br /></th><td>12dp corner radius</td></tr><tr><th>Left/right padding<br /></th><td>16dp</td></tr><tr><th>Padding between cards<br /></th><td>8dp max</td></tr><tr><th>Label text alignment<br /></th><td>Start-aligned</td></tr></tbody></table></div>

## Guidelines

3 variants of cards: elevated, filled, and outlined.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwujy207-1.png?alt=media

<h2 id="isPasted">Usage</h2>

<p id="isPasted">Use a card to display content and actions on a single topic.</p><p>Cards should be easy to scan for relevant and actionable information. </p><p>Elements like text and images should be placed on cards in a way that clearly indicates hierarchy.</p>

Example card containing an image, title, text, and button.

<p>Cards can display content and actions on a single topic</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwujyk5p-2.png?alt=media

<p>Cards can serve as entry points into deeper levels of detail or navigation, such as a music album or details on an upcoming vacation.</p>

Example world tour card.

<p>Card text and image show a clear hierarchy</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwujz8zw-3.png?alt=media

Card displaying connected details about a world tour.

<p>Use cards to display related information on a single subject</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwujzmmd-4.png?alt=media

<p>Cards can be displayed together in a grid, vertical list, or <app-froala-tooltip-element description="Carousels show a collection of items that can be scrolled on and off the screen." link-label="More on carousels" link-url="/m3/pages/carousel/overview" should-open-link-in-new-tab="true">carousel</app-froala-tooltip-element>.</p>

4 cards together in a grid layout.

<p>Cards can be shown together</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuk08jk-5.png?alt=media

5 albums in a vertical list of cards.  

<p>Don't force content into cards when spacing, headlines, or dividers would create a simpler visual hierarchy</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuk0pob-6.png?alt=media

<p>There are three card variants:</p><ul><li><p><app-froala-tooltip-element description="Elevated cards have a drop shadow, providing more separation from the background than filled cards, but less than outlined cards" link-label link-url should-open-link-in-new-tab="false">Elevated</app-froala-tooltip-element></p></li><li><p><app-froala-tooltip-element description="Filled cards provide subtle separation from the background. This has less emphasis than elevated or outlined cards." link-label link-url should-open-link-in-new-tab="false">Filled</app-froala-tooltip-element></p></li><li><p><app-froala-tooltip-element description="Outlined cards have a visual boundary around their container. This can provide greater emphasis than the other types." link-label link-url should-open-link-in-new-tab="false">Outlined</app-froala-tooltip-element></p></li></ul><p>Each provides the same legibility and functionality, so the variant you use depends on style alone.</p>

3 variants of cards.

<ol><li>Elevated card</li><li>Filled card </li><li>Outlined card</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuk16p3-7.png?alt=media

Example elevated card.

<p>Elevated cards have a drop shadow, providing more separation from the background than filled cards, but less than outlined cards</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuk25nc-8.png?alt=media

Example filled card.

<p>Filled cards provide subtle separation from the background. This has less emphasis than elevated or outlined cards.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuk2m44-9.png?alt=media

Example outlined card.

<p>Outlined cards have a visual boundary around the container. This can provide greater emphasis than the other variants.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuk337j-10.png?alt=media

<h2 id="isPasted">Anatomy</h2>

<p>The card container is the only required element in a card. Card layouts can vary to support the kinds of content they contain. Below is a common configuration of elements.</p>

Diagram labeling the 6 parts of card anatomy.

<ol class="decimal"><li><p>Container</p></li><li><p>Image</p></li><li><p>Button</p></li><li><p>Supporting text</p></li><li><p>Subhead</p></li><li><p>Headline</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmk6jnfqn-11.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-eiTnWJl-s5HUIjPs1tfHU9HJp4izquC1-CiHPmdGA3Eq1YAw82dWNDHWYoQN1aUiXKSQm1jkq8uHW8i2aR_xg8kUxVMmHW-tyV93R8gmc0=s2048

<h3 dir="ltr" id="isPasted">Container</h3><p dir="ltr">Card containers hold all card elements. Their size is determined by the space those elements occupy. Card elevation is expressed by the container.</p><p dir="ltr">The card container is the only required element of a card. All other elements are optional.</p>

3 card containers with various elements: 1 with all elements except a button. 1 with a container, headline, supporting text, button. 1 with a container, headline, supporting text, 2 buttons.

<p>Card size is determined by the elements it contains</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuk4ddn-12.png?alt=media

<h3>Content blocks</h3><p>Card contents are grouped into blocks. Content can have different levels of visual emphasis depending on importance.</p><p>Card layouts vary to support the kinds of content they contain.</p>

Diagram of card content blocks.

<p>Cards can contain a headline, subhead, supporting text, media, and actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuk4w24-13.png?alt=media

<h3 dir="ltr" id="isPasted">Dividers</h3><p dir="ltr"><a href="/m3/pages/divider/specs">Dividers</a> can separate regions in cards or indicate areas of a card that can expand.</p>

A divider running the entire width of the card.

<p>1. Use full-width dividers for content that can be expanded</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuk5dl8-14.png?alt=media

An inset divider indented from the edge of card.

<p>1. Use inset dividers, which don’t run the full width of a card, to separate related content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuk5r9g-15.png?alt=media

<h3 dir="ltr" id="isPasted">Media</h3><p class="normal" dir="ltr"><strong>Thumbnail</strong><br />Cards can include thumbnails for an avatar or logo.</p><p class="normal" dir="ltr"><strong>Image</strong><br />Cards can include photos, illustrations, and other graphics, such as weather icons.</p><p class="normal" dir="ltr"><strong>Video</strong><br />Cards can include video.</p>

A mobile chat app with: 5 cards with images, 1 card with a thumbnail avatar, and 1 card with a video. 

<p>Cards can contain thumbnails, images, and video</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuk7ixf-16.png?alt=media

<h3 dir="ltr" id="isPasted">Text</h3><p class="normal" dir="ltr"><strong>Headline</strong><br />Headline text often communicates the subject of the card, such as the name of a photo album or article.</p><p class="normal" dir="ltr"><strong>Subhead</strong><br />Subheads are smaller text elements, such as an article byline or a tagged location.</p><p class="normal"><strong>Supporting text</strong><br />Supporting text includes body content, such as an article summary or a restaurant description.</p>

card container with several elementsA tablet email app with an email summary card with multiple text elements.

<p>Headline, subhead, and supporting text in a card</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukrum6-17.png?alt=media

<h4 dir="ltr" id="isPasted">Layering text, icons, and images</h4><p dir="ltr">It isn’t recommended to place text or icons on images. If it’s necessary, ensure the background image provides sufficient contrast for the text to meet <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/cards/accessibility" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> standards.</p><p dir="ltr">Add a translucent scrim or bounding shape beneath the text or icon to help ensure proper contrast.</p>

Layered text contrasts with the background image.

<p>Ensure that text on images meets accessible contrast standards</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuke2rr-18.png?alt=media

Icon within a bounding shape, placed on an image.

<p>When placing text or icons on images, consider using a bounding shape to ensure proper contrast</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukejwa-19.png?alt=media

<h3 dir="ltr" id="isPasted">Actions</h3><h4 dir="ltr"><strong>Primary action area</strong></h4><p dir="ltr">Cards can be one large touch target triggering an expanded detail screen.</p>

The action area of a card contains rich media and supporting text.

<p>Cards can include a primary action area that expands into a full-screen view</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukf67i-20.png?alt=media

<p dir="ltr" id="isPasted"><strong>Buttons</strong><br />Cards can include <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element> for actions such as <strong>Learn more</strong> or <strong>Add to cart</strong>.</p><p dir="ltr"><strong>Icon buttons</strong><br />Cards can include <app-froala-tooltip-element description="Icon buttons help people take minor actions with one tap." link-label="More on icon buttons" link-url="/m3/pages/icon-buttons/overview" should-open-link-in-new-tab="true">icon buttons</app-froala-tooltip-element> for actions such as <strong>Save</strong>, <strong>Heart</strong>, or <strong>Leave a 4-star review</strong>.</p><p dir="ltr"><strong>Selection controls</strong><br />Cards can also include <app-froala-tooltip-element description="Chips help people enter information, make selections, filter content, or trigger actions." link-label="More on chips" link-url="/m3/pages/chips/overview" should-open-link-in-new-tab="true">chips</app-froala-tooltip-element>, <app-froala-tooltip-element description="Sliders let users make selections from a range of values." link-label="More on sliders" link-url="/m3/pages/sliders/overview" should-open-link-in-new-tab="true">sliders</app-froala-tooltip-element>, <app-froala-tooltip-element description="Checkboxes let users select one or more items from a list, or turn an item on or off." link-label="More on checkboxes" link-url="/m3/pages/checkbox/overview" should-open-link-in-new-tab="true">checkboxes</app-froala-tooltip-element>, and other selection controls.</p><p dir="ltr"><strong>Linked text</strong><br />There can be a link in the supporting text on a card.</p>

Supplemental text and actions at the top and bottom of the card.

<p>Cards can include multiple action areas containing buttons, links, and other controls</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukfjtw-21.png?alt=media

Album card with an option to give a star rating.

<p>Cards can contain icon buttons like stars to rate content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukg62l-22.png?alt=media

Card to purchase tickets with choice chips for 3 event times.

<p>Cards can contain choice chips in the action area</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukgix5-23.png?alt=media

Card with slider to control a song’s volume.

<p>Cards can contain a slider control in the action area</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukgu3i-24.png?alt=media

<p><strong id="isPasted">Overflow menu</strong><br />Overflow menus contain related actions. They are typically placed in the upper-right or lower-right corner of a card.</p>

2 cards: 1 with an overflow menu in the upper-right corner, the other with it in the lower right.

<p>Overflow menus are usually located in the upper-right or lower-right corner of a card</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukh83p-25.png?alt=media

<h2>Cards in a collection</h2>

<p>Multiple cards can be grouped together into collections displayed in a grid, <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">list</app-froala-tooltip-element>, or <app-froala-tooltip-element description="Carousels show a collection of items that can be scrolled on and off the screen." link-label="More on carousels" link-url="/m3/pages/carousel/overview" should-open-link-in-new-tab="true">carousel</app-froala-tooltip-element>. </p><p>By default, cards in a collection are coplanar. They share the same resting elevation unless they're picked up or <app-froala-tooltip-element description="A dragged state communicates when a user presses and moves an element." link-label="More on dragged state" link-url="/m3/pages/interaction-states/applying-states#198c29c7-771e-4264-91e9-70c32b8902ec" should-open-link-in-new-tab="true">dragged</app-froala-tooltip-element>.</p>

9 cards in a grid layout.

<p>Multiple cards can be grouped into collections with a shared resting elevation</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukhv18-26.png?alt=media

<h4 dir="ltr" id="isPasted">Filtering and sorting</h4><p dir="ltr">Card collections can be filtered in a variety of ways, including by date or alphabetical order. If a collection can be filtered, the filter must apply to each card in the collection. </p><p>Filter or sorting options should be placed outside of the card collection.</p>

A sort-by-date option placed above a card collection.

<p>Card collections can be filtered in a variety of ways, including by date:<br />1. A sort-by-date option is placed outside of the card collection </p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukig38-27.png?alt=media

<p>Organize card collections so that they'e easy to use. Their <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/understanding-layout/overview" should-open-link-in-new-tab="true">layout</app-froala-tooltip-element> affects how they are perceived.</p>

A template for an 8-card collection layout.

<p>Place cards in a collection in a straightforward, easy-to-use manner</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukiwuu-28.png?alt=media

<h3 dir="ltr" id="isPasted">Grid</h3><p dir="ltr">Cards can be displayed together in a grid.</p>

A set of 4 cards in a grid.

<p>Cards displayed in a grid</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwumleea-GM3-Components-Cards-Guidelines-1-v01.mp4?alt=media

<p>The default grid can be customized in code to show cards in staggered or mosaic grids.</p>

5 menu item cards in a mosaic grid.

<p>Custom mosaic grid</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukjfiq-30.png?alt=media

4 menu item cards in a staggered grid.

<p>Custom staggered grid</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukk75c-31.png?alt=media

<h3 dir="ltr" id="isPasted">Vertical list</h3><p dir="ltr">Cards can be displayed together in a vertical list.</p>

3 cards in vertical list.

<p>Cards can be shown in a vertical list</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwummhcq-GM3-Components-Cards-Guidelines-2-v01.mp4?alt=media

<h3 dir="ltr" id="isPasted">Carousel</h3><p dir="ltr">Cards can be displayed together in a horizontal row or <app-froala-tooltip-element description="Carousels show a collection of items that can be scrolled on and off the screen." link-label="More on carousels" link-url="/m3/pages/carousel/overview" should-open-link-in-new-tab="true">carousel</app-froala-tooltip-element>.</p>

3 event reservation cards in a horizontal row.

<p>Cards displayed together in a horizontal row or carousel</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwumodmh-GM3-Components-Cards-Guidelines-3-v01.mp4?alt=media

<h2>Adaptive design</h2>

<p>As cards scale to adapt to different <a href="/m3/pages/breakpoints" target="_self">breakpoints</a>, their position and alignment can also change.</p><p>Cards and their elements can align left, right, or center as the layout scales.</p>

2 cards on a mobile screen row expand to 4 cards on a tablet screen row. 

<p>Card position and alignment changes as the screen size changes</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukkvy8-34.png?alt=media

<h3>Ergonomics</h3><p>Adjust the <app-froala-tooltip-element description="Layout is the visual arrangement of elements on the screen." link-label="More on layout" link-url="/m3/pages/understanding-layout/overview" should-open-link-in-new-tab="true">layout</app-froala-tooltip-element> of cards to meet the ergonomic needs of large screens. <br /><br />For example, a horizontally-oriented card in a <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoint</app-froala-tooltip-element> may become a larger, vertically-oriented card in an <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoint</app-froala-tooltip-element>, with more space for images and text on the larger screen.</p>

Card sizes change from mobile to tablet, with larger images in the tablet layout.

<p>Adjust the card layout so content remains the main focus on large screens</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuklb57-35.png?alt=media

<h3 dir="ltr" id="isPasted">Visual presentation</h3><p dir="ltr">To adjust the presentation of content-focused components, begin with spacing. </p><p dir="ltr">Allow components like <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">lists</app-froala-tooltip-element>, cards, and images to optimize space while filling the region of a screen that suits a device breakpoint’s ergonomic needs.</p>

2 cards with optimized space: 1 narrow rectangle, 1 wide square.

<p>Spacing adjusts for components such as cards, lists, and images</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukluzj-36.png?alt=media

2 examples of the same card: 1 vertical with an image at the top, 1 horizontal with an image on the left.

<p>Example of the same card with two different orientations and element positioning</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukmfqz-37.png?alt=media

<h3>Column-based layouts</h3><p>In mobile layouts, components such as <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">lists</app-froala-tooltip-element> or cards are stretched to fit the full width of the screen without compromising visual quality or user experience. When designing for large screens with an <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoint</app-froala-tooltip-element>, use multiple columns to display content.</p><p>Avoid extending UI elements across the screen when possible. On larger screens, rearrange groups of related cards into horizontal rows or <app-froala-tooltip-element description="Carousels show a collection of items that can be scrolled on and off the screen." link-label="More on carousels" link-url="/m3/pages/carousel/overview" should-open-link-in-new-tab="true">carousels</app-froala-tooltip-element>, to allow for better content organization.</p>

3 related cards in a carousel.

<p>When designing for large screens, use multiple columns to display content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwukn6ma-38.png?alt=media

<h3>Small screens</h3><p>On smaller screens with the <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact breakpoint</app-froala-tooltip-element>, consider swapping cards for <app-froala-tooltip-element description="Lists are continuous, vertical indexes of text and images." link-label="More on lists" link-url="/m3/pages/lists/overview" should-open-link-in-new-tab="true">lists</app-froala-tooltip-element>, which can display images and text in a more compact form. </p><p>Make sure that controls, actions, and other component-specific elements are maintained.</p>

Cards on a large screen adapt to a list on a small mobile screen.

<p>Certain devices or user contexts require different components to meet platform expectations</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwumrs3a-GM3-Components-Cards-Guidelines-4-v01.mp4?alt=media

<h2>Behavior</h2>

<h3 dir="ltr" id="isPasted">Expanding</h3><p dir="ltr">Cards can use a <a href="/m3/pages/motion-transitions/transition-patterns#b67cba74-6240-4663-a423-d537b6d21187" rel="noopener noreferrer" target="_blank">container transform</a> transition pattern to reveal additional content. Reserve this pattern for hero moments that are meant to be expressive.</p>

An album card expands to fill the screen and shows additional related content.

<p>A card expands to fill the full screen using a parent-child transition</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwunn86t-GM3-Components-Cards-Guidelines-6-v01.mp4?alt=media

A card expands, showing all content at once.

<p>Expand a card to reveal information</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwumvwvk-GM3-Components-Cards-Guidelines-7-1-v01.mp4?alt=media

A card expands, internally scrolling to only show some information.

<p>Don’t scroll within a card to reveal information</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwumwjkp-GM3-Components-Cards-Guidelines-7-2-v01.mp4?alt=media

<h3 dir="ltr" id="isPasted">Navigation</h3><p dir="ltr">Cards can use a <a href="/m3/pages/motion-transitions/transition-patterns#df9c7d76-1454-47f3-ad1c-268a31f58bad" rel="noopener noreferrer" target="_blank">forward and backward</a> transition pattern to navigate between screens at consecutive levels of hierarchy. This pattern has a simpler motion style compared to container transform, which makes it suitable for common navigation transitions.</p>

Card interaction transitioning to full screen.

<p>Cards can use a forward and backward transition pattern to navigate between screens</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwumxklj-GM3-Components-Cards-Guidelines-8-v01.mp4?alt=media

<h3>Gestures</h3>

<h4 dir="ltr" id="isPasted">Swipe</h4><p dir="ltr">A swipe <app-froala-tooltip-element description="Gestures are all the ways people interact with UI elements using touch." link-label="More on gestures" link-url="/m3/pages/gestures" should-open-link-in-new-tab="true">gesture</app-froala-tooltip-element> can be performed on a single card at a time, anywhere on that card.</p><p dir="ltr">It can be used to:</p><ul><li>Dismiss a card</li><li dir="ltr">Change the <app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">state</app-froala-tooltip-element> of a card, such as flagging or archiving it</li></ul>

A card with 1 assigned swipe: to heart the entire card.

<p>A card should only have one swipe action assigned to it</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwumypwh-GM3-Components-Cards-Guidelines-9-1-v01.mp4?alt=media

A card with an image carousel and a swipe motion to heart only the bottom text on the card.

<p>Cards shouldn’t contain content that can be swiped, such as an image carousel or pagination. Also, swipe gestures shouldn’t cause portions of cards to detach upon swiping.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwumzbld-GM3-Components-Cards-Guidelines-9-2-v01.mp4?alt=media

<h4 dir="ltr" id="isPasted">Pick up &amp; move</h4><p dir="ltr">The pick-up-and-move <app-froala-tooltip-element description="Gestures are all the ways people interact with UI elements using touch." link-label="More on gestures" link-url="/m3/pages/gestures" should-open-link-in-new-tab="true">gesture</app-froala-tooltip-element> allows users to move and reorder cards in a collection.</p>

A card is elevated above all other cards when moved.

<p>When moving a card, increase its elevation</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwun0601-GM3-Components-Cards-Guidelines-10-1-v01.mp4?alt=media

A moved card bumps other cards around, and isn’t elevated above them.

<p>Don’t let cards bump other elements out of the way. When a card is picked up, it appears in front of all elements, except app bars and navigation.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwun0v03-GM3-Components-Cards-Guidelines-10-2-v01.mp4?alt=media

<h4 dir="ltr" id="isPasted">Scrolling</h4><p dir="ltr">Card content that’s taller than the maximum card height is truncated and doesn’t scroll, but can be displayed by expanding the height of a card.  <br /><br />A card can expand beyond the maximum height of the screen, in which case the card scrolls within the screen.</p>

Scrolling a page with an expanded card.

On a mobile device, cards can expand to reveal more content, scrolling within the screen. Content within cards doesn’t scroll.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fkvmo6wo3-cards-scrolling_do_03.png?alt=media

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwun21j4-GM3-Components-Cards-Guidelines-11-1-v01.mp4?alt=media

Expanded card on mobile with internal scrolling.

<p>On a mobile device, cards can't internally scroll, as it could cause two scroll bars to be displayed</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fkvmo7754-cards-scrolling_dont_03-1.png?alt=media

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwun2kqe-GM3-Components-Cards-Guidelines-11-2-v01.mp4?alt=media

<h4 dir="ltr" id="isPasted">Scrolling on desktop</h4><p dir="ltr">On a desktop device, card content can expand and scroll within a card.</p>

Expanded card on desktop with internal scrolling.

<p>On a desktop, content can expand and scroll within a card</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fkvmo6437-cards-desktop_scroll_01%20(2).png?alt=media

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwun3hn1-GM3-Components-Cards-Guidelines-12-v01.mp4?alt=media

## Accessibility

<h2>Use cases</h2>

<p id="isPasted">People should be able to do the following using assistive technology:</p><ul><li>Navigate to a card and the elements within a card </li><li>Get appropriate feedback based on input type documented under <a href="/m3/pages/cards/accessibility#ce764d54-6b59-42db-807f-b3cb370eecdb">Interaction &amp; style</a></li></ul>

<h2><span style="white-space:pre-wrap">Interaction &amp; style</span></h2>

<p>A card can be a non-actionable container that holds actions like <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element> and links, or it can be directly actionable without any buttons or links. This is to avoid stacking actionable elements. An action shouldn’t be placed on an actionable surface.</p>

2 possible card interaction behaviors.

<ol><li id="isPasted">Non-actionable card with buttons</li><li>Directly actionable card with no buttons</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuobzmz-1.png?alt=media

<h3>Touch</h3><p id="isPasted">When a user taps on a directly actionable card, a touch ripple appears across the card, indicating feedback. </p><p>Non-actionable cards don’t ripple.</p>

Ripple effect created when tapping on a card.

<p><span style="white-space:pre-wrap">Touch: Tap</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuonrmp-GM3-Components-Cards-Accessibility-1-v01%203.21.14%E2%80%AFPM.mp4?alt=media

<h3>Dragging and dismissing</h3><p><span style="white-space:pre-wrap" id="isPasted">To meet Material's accessibility standards, any dragging and swiping interactions need a single-pointer alternative, like selecting the same actions from a menu.<br /><br />For example, tapping a card, or pressing and holding, should open a menu to change its position in a list. That menu could also contain an action to delete the card.</span></p>

A list of cards has its order reshuffled using a single-pointer option.

<p><span style="white-space:pre-wrap">Use containers like bottom sheets or menus to show single-pointer options</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm6gok77f-Components-Cards-Accessibility-1-v01%20(1).mp4?alt=media

<p><span style="white-space:pre-wrap" id="isPasted">It isn’t recommended to place menus on top of the card on the draggable state. If doing so is necessary, ensure that the interaction can be completed.</span></p>

A menu over a card that doesn't totally obscure the card.

<p><span style="white-space:pre-wrap">Ensure that the menu doesn't cover the card</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm4ivybyo-3-a.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/UtnmXzj_hGKzI5R_xHaZroWQFz8QVFP84FZQS0iNVQIeJqE0-5q6CQGAszShyOylV59mHPIT3kyfXHFxAmJ34OD3CcE0yO1anFh0UoEwXXo=s1352

<h3>Cursor</h3><p id="isPasted">When a directly actionable card is hovered, the <app-froala-tooltip-element description="A hover state communicates when a user has placed a cursor above an interactive element." link-label="More on hover state" link-url="/m3/pages/interaction-states/applying-states#bf01ead3-12e0-4077-98d1-05927d284c35" should-open-link-in-new-tab="true">hover state</app-froala-tooltip-element> provides a visual cue to the person that the element is interactive. Non-actionable cards don’t have a hover state.</p><p>When a directly actionable card is clicked, a ripple appears, providing feedback.</p>

Hover state and touch ripple effect of a card.

<p><span style="white-space:pre-wrap">Cursor: Hover, Click</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuoolew-GM3-Components-Cards-Accessibility-2-v01%203.24.03%E2%80%AFPM.mp4?alt=media

<h3>Keyboard</h3><p>A focus indicator appears around actionable elements when tabbing through cards. This provides a visual cue to a person that the destination is now <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bfc1624f-6bcc-4306-b0c1-425e2d8a1bf9" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element> and an action can be taken.</p><p>A person can <strong>Tab</strong> to navigate between actionable elements of the cards. If the cards are non-actionable, <strong>Tab</strong> navigates directly to the actionable <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element> or links within the cards.</p><p>When engaging with a focused actionable card or element using the <strong>Space</strong> or <strong>Enter</strong> key, an action is performed or a secondary action is available, such as a <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element>.</p><p>Within the menu, a person is able to <strong>Arrow</strong> through the menu items, <strong>Space</strong> or <strong>Enter</strong> to select an item, or <strong>Tab</strong> to exit.</p>

Navigating cards with a keyboard.

<p><span style="white-space:pre-wrap">Keyboard: Tab, Arrows</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuop9fg-GM3-Components-Cards-Accessibility-3-v01.mp4?alt=media

<h2>Focus</h2>

<p id="isPasted">All interactive elements of cards need a tab stop so they can be <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bfc1624f-6bcc-4306-b0c1-425e2d8a1bf9" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element>. Directly actionable cards are tab stops.</p><p>For non-actionable cards, the card itself is not a tab stop. However, every actionable element in the card is a tab stop so they’re all visited before focus navigates to the next card.</p>

The focus areas of a card with interactive elements.

<p>Use <strong>T</strong><strong>ab</strong> to navigate through all buttons in a card</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuodgu3-5.png?alt=media

<p><br /></p><p><br /></p>

Cards forming a list on mobile and cards forming a gallery on tablet.

<p><span style="white-space:pre-wrap">Card layouts can change on different devices</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwuoeob6-6.png?alt=media

<h2>Keyboard navigation</h2>

<div class="table-wrapper"><table id="isPasted" style="width:100%"><thead><tr><th style="width:18.1023%">Keys</th><th style="width:81.7798%">Actions</th></tr></thead><tbody><tr><th style="width:18.1023%"><strong>Tab</strong></th><td><p id="isPasted">Move to the next actionable element</p><p><br /></p><p><strong>Directly actionable cards:</strong> Move to next card container</p><p><strong>Non-actionable cards with actionable elements:</strong> Move to next actionable element</p></td></tr><tr><th style="width:18.1023%"><strong>Space</strong> or <strong>Enter</strong></th><td>Confirm action</td></tr></tbody></table></div><p><br /></p>

<h2>Labeling elements</h2>

<p id="isPasted">The informative contents of a card are verbalized when navigating to them using a screen reader. If an image in a card is purely decorative, hide it from screen readers. All actionable elements must receive both screen reader and keyboard focus.</p><p>Directly actionable cards can have the <strong>button</strong> or <strong>link</strong> role, depending on how they’re used. </p><p>Non-actionable cards are purely containers, so they don’t need a role.</p><p><br /></p>

Card elements annotated in the order that a screen reader tabs through them.

<p id="isPasted">Non-actionable card elements are navigable, focused in order, and verbalized when in focus. In this example, the order is:</p><ol><li>Heading</li><li>Image</li><li>Body text</li><li>Primary button</li><li>Secondary button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmk6jw3io-09.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/kRZc33v7W2dec-MuK-hHKuYiBNxg2bd94Nl5lLgVpvf6JgZqUcU41USNzujmZqRUy3FjNddyFflMj37GqpyDMartw2BuUumFsfwjSxepog_T=s1352

<h2>Resources</h2>
