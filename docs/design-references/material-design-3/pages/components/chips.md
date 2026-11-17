# Chips

Source: https://m3.material.io/components/chips
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/592d28d0-0c82-4642-a203-556b1e0581b0.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Use chips to show options for a specific context</p></li><li><p>Four variants: <app-froala-tooltip-element description="Assist chips represent smart or automated actions that can span multiple apps, such as opening a calendar event from the home screen." link-label link-url should-open-link-in-new-tab="true">assist</app-froala-tooltip-element>, <app-froala-tooltip-element description="Filter chips use tags or descriptive words to filter content. They can be a good alternative to toggle buttons or checkboxes." link-label link-url should-open-link-in-new-tab="true">filter</app-froala-tooltip-element>, <app-froala-tooltip-element description="Input chips represent discrete pieces of information entered by a user, such as Gmail contacts or filter options within a search field." link-label link-url should-open-link-in-new-tab="true">input</app-froala-tooltip-element>, and <app-froala-tooltip-element description="Suggestion chips help narrow a user’s intent by presenting dynamically generated suggestions, such as suggested responses or search filters." link-label link-url should-open-link-in-new-tab="true">suggestion</app-froala-tooltip-element></p></li><li><p>Chip <app-froala-tooltip-element description="Elevation is the distance between two surfaces on the z-axis." link-label="More on elevation" link-url="/m3/pages/elevation/overview" should-open-link-in-new-tab="true">elevation</app-froala-tooltip-element> defaults to 0 but can be elevated if they need more visual separation</p></li></ul>

4 chip variants.

<ol><li>Assist chip</li><li>Filter chip</li><li>Input chip</li><li>Suggestion chip</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flzthj7vk-1.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/0c68159e11eed87a

libraryModuleType: STATUS_TABLE

<h2>Updates</h2>

<p><strong>Aug 2024</strong></p><p><span style="white-space:pre-wrap" id="isPasted">Updated stroke color from <strong>outline</strong> to <strong>outline variant</strong>.</span></p>

A chip with a clear outline is now a chip with a subtle outline.

<p>The stroke color was softened to improve visual hierarchy between chips and buttons</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sdpshu-02.png?alt=media

<h2>Differences from M2</h2>

<ul><li><p>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></p></li><li><p>Shape: Rounded rectangle </p></li><li><p>Variants: Action chips have been separated into <app-froala-tooltip-element description="Assist chips represent smart or automated actions that can span multiple apps, such as opening a calendar event from the home screen." link-label link-url should-open-link-in-new-tab="true">assist chips</app-froala-tooltip-element> and <app-froala-tooltip-element description="Suggestion chips help narrow a user’s intent by presenting dynamically generated suggestions, such as suggested responses or search filters." link-label link-url should-open-link-in-new-tab="true">suggestion chips</app-froala-tooltip-element>. Choice chips are now a subset of <app-froala-tooltip-element description="Filter chips use tags or descriptive words to filter content. They can be a good alternative to toggle buttons or checkboxes." link-label link-url should-open-link-in-new-tab="true">filter chips</app-froala-tooltip-element></p></li></ul>

M2 chip variants.

<p>M2: Variants of chips are input, choice, filter, and action chips</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8se5ler-05.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/2QvL9BG6dybkEq8-MxokwRvnU_5-Yxey0SZtSxa9o6KlczyP2t5hAtUxTyZRJbGF9i7m6oOrZCWKJT4CQikVZP3D0cxsKj0yYaMJT4QjnE5q=s1004

M3 chip variants.

<p>M3: Variants of chips updated to assist, filter, input, and suggestion chips</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8se6c0w-06.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/3W0HJhJSBgfi_3TWYvZlXCPDg42elT_0VwxJmTTK5l61ZFdC9l9mPQPqPcUOBXNIce2r3aDWGNECHLcoe41RXvv2rr1bjDL6BsCCvjkxUto=s1004

## Specs

<h2>Tokens &amp; specs</h2><p>Select a component variant below to see its elements, attributes, tokens, and values.</p>

resourceName: designSystems/20543ce18892f7d9/components/484a63be03b01a17

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Chip - Assist', 'Chip - Filter', 'Chip - Input', 'Chip - Suggestion'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['Chip - Assist', 'Chip - Filter', 'Chip - Input', 'Chip - Suggestion'], 'hideSearchField': False, 'hideVersionName': True}

<h2 id="isPasted">Assist chip</h2>

Assist chip diagram numbering 3 elements.

<ol><li>Container </li><li>Label text </li><li>Leading icon</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm01dv1nz-1.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/UipTazZY6lB09YYRrq_uydfwLG0Xj5EIIlJVA252BfyovfvZXXXPGP66wGx4ZT0jOXqI6eQ7OLB6zVCjzqJ8CCJEqPW8Gw34jd-gSSA7qHsdIQ=s2048

<h3 id="isPasted">Assist chip color</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview">Learn more about design tokens</a></p>

Assist chip diagram numbering 4 color elements.

<p>Assist chip color roles used for light and dark themes:</p><ol><li>Surface container low (optional)</li><li>On surface</li><li>Outline</li><li>Primary</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm01dv6ou-2.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/CgU4dUqBVfaebvIlmiYeW8i9Geq2Z3kASKWrVMHXl1kgDAx2tDJ40MrFVDf7tqkPEKuX4au-iLvzbSBoRQDxQokAEP5Y9-y3vwkFIyl6c0Hy=s2048

<h3 id="isPasted">Assist chip states</h3><p><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element> are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states/overview">Learn more about interaction states</a></p>

36 assist chips illustrating combinations of styles, selection and non-selection, and 6 interaction states.

<p>Selected and unselected assist chip states:</p><ol><li>Enabled </li><li>Disabled </li><li>Hovered </li><li>Focused </li><li>Pressed </li><li>Dragged</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8sg1d2r-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/s6LyjzP2TrQRGesL7fSbWcwEr94zeAaCTl8Zj7vDx6EsJ9Hn-9fNov0mtodXBs61mOtW6OnsmyPnirrfIzoRgYUxPDTIeH_4bXq-29iBOnxE=s2048

<h3>Assist chip measurements</h3>

3 assist chips with measurements shown for variants with and without a leading icon.

<p>Assist chip padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm01dvj22-4.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/tDL76BxJhx73568XEIJ3nbFUBxkn1ac2zO3Vqrf0CmFLPBi3yuLhjPYhZHmEFv6_cfjXMg-16mB2O5c11x-0yDMvb9L4QB7oHVHVLm29QvCH=s2048

<div class="table-wrapper"><table><thead><tr><th style="text-align:center">Attribute<br /></th><th style="text-align:center">Value<br /></th></tr></thead><tbody><tr><th>Height<br /></th><td>32dp</td></tr><tr><th>Shape<br /></th><td>8dp corner radius</td></tr><tr><th>Icon size<br /></th><td>18dp</td></tr><tr><th>Vertical label text alignment<br /></th><td>Center-aligned</td></tr><tr><th>Horizontal label text alignment<br /></th><td>Start-aligned</td></tr><tr><th>Left/right padding<br /></th><td>16dp</td></tr><tr><th>Left/right padding with icon<br /></th><td>8dp</td></tr><tr><th>Padding between elements<br /></th><td>8dp</td></tr></tbody></table></div>

<h2>Filter chip</h2>

Filter chip diagram numbering 4 elements.

<ol><li>Container </li><li>Label text </li><li>Leading icon</li><li>Trailing icon</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm01dvpzm-5.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/WczxPrTlNqVqk9HILdgclP7OR_TQ6sLWYPB9qIHvZ6QLGDS9Uo1Sjm30UFiVAJmo8DVAWcZPacF_gyj-dGZDZ1JROW93iccqf-sa_rjqQ-S7=s2048

<h3 dir="ltr" id="isPasted">Filter chip color</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview">Learn more about design tokens</a></p>

Filter chip diagram numbering 4 color elements.

<p>Filter chip color roles used for light and dark themes:</p><ol class="decimal"><li><p>On surface variant</p></li><li><p>On secondary container</p></li><li><p>Secondary container</p></li><li><p>Outline variant</p></li><li><p>Surface container low (optional)</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmmp8q5ab-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/2raflfeNVlaC3gjYDipGLH5aIA6hJB4NL7ruSwZGbqk7Ec8W1AHpbd2Eyhxbeo0g0rVWSvHwdbjU16hJSB8o4AfiMqPzGn3K9uK4NDJIY-gu=s2048

<h3 dir="ltr" id="isPasted">Filter chip states</h3><p dir="ltr"><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element> are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states/overview" id="isPasted">Learn more about interaction states</a></p>

24 filter chips showing combinations of elevated, non-elevated, selected, and non-selected styles, and 6 interaction states.

<p id="isPasted">Selected and unselected filter chip states:</p><ol><li>Enabled </li><li>Disabled </li><li>Hovered </li><li>Focused </li><li>Pressed </li><li>Dragged</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8sg2d2t-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/KftllQmRE7STKHvBYUhxG13rWSMWMWOj_Y3mqpHMyKpj4Exvl-J7B4cBwB1_Cexx8oaCnXYw7hdPnk16YmZS-zyVWB7vbokHFJjfkahSM0Eo=s2048

<h3 id="isPasted">Filter chip measurements</h3>

3 filter chips with measurements shown for types with and without a leading icon and trailing icon.

<p>Filter chip padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm01dwqif-8.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/22fmoqWkQTxchSh4qTgO2nrZ76sooCtX3ywKPLhqba5suVk8PW60_IA03iQ1yUdTipCKCFx0mRHhnWRs9Hm2oGdr2s9K9J8uaKukdPjGkNoA=s2048

<div class="table-wrapper"><table><thead><tr><th style="text-align:center">Attribute<br /></th><th style="text-align:center">Value<br /></th></tr></thead><tbody><tr><th>Container height<br /></th><td>32dp</td></tr><tr><th>Container shape<br /></th><td>8dp corner radius</td></tr><tr><th>Icon size<br /></th><td>18dp</td></tr><tr><th>Vertical label text alignment<br /></th><td>Center-aligned</td></tr><tr><th>Horizontal label text alignment<br /></th><td>Start-aligned</td></tr><tr><th>Left/right padding<br /></th><td>16dp</td></tr><tr><th>Left/right padding with icon<br /></th><td>8dp</td></tr><tr><th>Padding between elements<br /></th><td>8dp</td></tr></tbody></table></div>

<h2 id="isPasted">Input chip</h2>

Input chip diagram numbering 4 elements.

<ol><li>Container </li><li>Label text </li><li>Trailing icon </li><li>Leading icon</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm01dwxct-9.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/MFMFJhZqnlfNlT6wWDldzAYdPhLBn9OvPgeAyUmocIf1YooTBamJN4doylmVzztWcDYbjHmV2OSQEaOoefcOMS8Uu0hEuGTGbTJYCxLfXKSu=s2048

<h3 dir="ltr" id="isPasted">Input chip color</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview">Learn more about design tokens</a></p>

Input chip diagram numbering 5 color elements.

<p id="isPasted">Input chip color roles used for light and dark themes:</p><ol><li>On surface variant</li><li>Surface container low (optional)</li><li>On surface variant</li><li>On surface variant</li><li>Outline variant</li><li>Primary</li><li>Secondary container</li><li>On secondary container</li><li>On secondary container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm02q3wit-10-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/YmMzczrJL0g0MAMFwW2zs8up57xJzcAxNJraHceXpaVZVPAEN2ukdjQwHpuYnVjEKQrnC-KGaC09_KYKNpWgMXg5iqhm8xGleC3-wuG0E0XYwg=s2046

<h3 dir="ltr" id="isPasted">Input chip states</h3><p dir="ltr"><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element> are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states/overview" id="isPasted">Learn more about interaction states</a></p>

33 input chips illustrating combinations of styles, selection and non-selection, and 6 interaction states.

<p id="isPasted">Selected and unselected input chip states:</p><ol><li>Enabled </li><li>Disabled </li><li>Hovered </li><li>Focused </li><li>Pressed </li><li>Dragged</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8sg4m8e-11-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ganq0HIgyGsa-HH5bnqU95oJCYypADT4v0LOgsmwQ9ek5B45GtD6EgJCpd589BbA4-tDKOpNCksyDIkrq7krkMG8_nJ0eHSu30BIj7OCqFE=s2048

<h3 id="isPasted">Input chip measurements</h3>

2 input chips with measurements: 1 with a trailing icon only; 1 with an avatar as a leading icon and a trailing icon.

Input chip padding and size measurements

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm34ufke8-12-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LwwDa1dknxPJeGchp4qkldM7ofBH7mypUCmVb5VQRgeY0cICTc5_H0fHVUTbuY0TQ7VNaBlqfYrlPFwKL4FnRQL5N5chlOoz8EhVdkbmers=s2048

<div class="table-wrapper"><table><thead><tr><th style="text-align:center">Attribute<br /></th><th style="text-align:center">Value<br /></th></tr></thead><tbody><tr><th>Container height<br /></th><td>32dp</td></tr><tr><th>Container shape<br /></th><td>8dp corner radius</td></tr><tr><th>Icon size<br /></th><td>18dp</td></tr><tr><th>Avatar shape<br /></th><td>12dp corner radius</td></tr><tr><th>Avatar size<br /></th><td>24dp</td></tr><tr><th>Vertical label text alignment<br /></th><td>Center-aligned</td></tr><tr><th>Horizontal label text alignment<br /></th><td>Start-aligned</td></tr><tr><th>Left padding for avatar<br /></th><td>4dp</td></tr><tr><th>Right padding for avatar<br /></th><td>8dp</td></tr><tr><th>Left/right padding for icon<br /></th><td>8dp</td></tr><tr><th>Padding between elements<br /></th><td>8dp</td></tr><tr><th>Target size for close icon<br /></th><td>Min 48dp</td></tr></tbody></table></div>

<h2 id="isPasted">Suggestion chip</h2>

Suggestion chip diagram numbering 2 elements.

<ol><li>Container </li><li>Label text</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm01dxq8p-13.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ytfZyslYlVSL6feuGZznpeG6Wi6YP9sPrNyN7IDDr8cClF4pFIS2gdMGmX6GAG6oYN2ZAHE4hitoYzO2MSs88zdrks6vikOU8NHwkOGHeWU=s2048

<h3 dir="ltr" id="isPasted">Suggestion chip color</h3><p>Color values are implemented through <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">design tokens</app-froala-tooltip-element>. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview">Learn more about design tokens</a></p>

Suggestion chip diagram numbering 3 color elements.

<p id="isPasted">Suggestion chip color roles used for light and dark themes:</p><ol><li>Outline</li><li>Surface container low (optional)</li><li>On surface variant</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm01dxxwr-14.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/4Ni_EPMelCZDcAAcbhbIDdGj4ER5JGlUjPOtgO4Qx1IIooRh25eJo_y7LgMr7yD0tX-PcXu3vY6O7u-wlJRgFUK23JxG69NgKqYz6sSPywNx=s2048

<h3 dir="ltr" id="isPasted">Suggestion chip states</h3><p dir="ltr"><app-froala-tooltip-element description="States show the interaction status of a component or UI element." link-label="More on states" link-url="/m3/pages/interaction-states/overview" should-open-link-in-new-tab="true">States</app-froala-tooltip-element> are visual representations used to communicate the status of a component or interactive element. <a href="/m3/pages/interaction-states/overview" id="isPasted">Learn more about interaction states</a></p>

24 suggestion chips illustrating combinations of styles across 6 interaction states.

<p id="isPasted">Selected and unselected suggestion chip states:</p><ol><li>Enabled</li><li>Disabled</li><li>Hovered</li><li>Focused</li><li>Pressed</li><li>Dragged</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8sg5r6a-15-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/YYoIuUfDsUQqPR--eP-zfow9SJVnjSlY060t1WUqtVUdBkynNCTTe1IK16I4rpfBRRpHrZqDKEYftwwhLFa18FYaI3-aRJpqPTUpr1w5ekG0=s2048

<h3>Suggestion chip measurements</h3>

2 suggestion chips with measurements shown for variants with and without a leading icon.

<p>Suggestion chip padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm01dybi0-16.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ToyBZvY6HgToxkWV0wPdYIHq3FzSkIz4HUsgSzJD-Q30jS8TQTzRzN81nagH7Q1XDitG-Lgzav9wephSlFzWHaJn24mnANMqlm3KUNaeCRt6=s2048

<div class="table-wrapper"><table><thead><tr><th style="text-align:center">Attribute<br /></th><th style="text-align:center">Value<br /></th></tr></thead><tbody><tr><th>Container height<br /></th><td>32dp</td></tr><tr><th>Container shape<br /></th><td>8dp corner radius</td></tr><tr><th>Icon size<br /></th><td>18dp</td></tr><tr><th>Vertical label text alignment<br /></th><td>Center-aligned</td></tr><tr><th>Horizontal label text alignment<br /></th><td>Start-aligned</td></tr><tr><th>Left/right padding without icon<br /></th><td>16dp</td></tr><tr><th>Left/right padding with icon<br /></th><td>8dp</td></tr><tr><th>Padding between elements<br /></th><td>8dp</td></tr></tbody></table></div>

## Guidelines

4 chip variants: Assist, filter, input, and suggestion.

<p>There are four variants of chips: Assist, filter, input, and suggestion</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8smcq59-01.png?alt=media

<h2>Usage</h2>

<p>Chips help people enter information, make selections, filter content, or trigger actions. They're best used to help people accomplish their current task faster and easier.</p>

3 assist chips in restaurant review app.

<p>Chips appear as a group of interactive elements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8smdd4g-02.png?alt=media

<h3 dir="ltr" id="isPasted">Chips aren’t buttons</h3><p dir="ltr">Chips and <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap. " link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element> are similar. They both provide visual cues to prompt people to take actions and make selections. </p><p dir="ltr">While buttons appear consistently and with familiar calls to action, chips are dynamic to the situation, and appear as a group of interactive elements.</p><p dir="ltr">Use chips to enhance a person's current journey and encourage action. Use buttons to progress them through the product and for significant actions.</p>

Chips used for “Reserve a table” and “Order delivery” in a restaurant app.

<p>Use chips to present contextual, supplemental options</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztjonhj-3-do.png?alt=media

Chips used for Save and Cancel actions in a dialog.

<p>Avoid replacing major actions with chips. Actions that progress people to the next or previous step should always be displayed as buttons.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztjp9f8-4-dont.png?alt=media

<p>Chips should dynamically offer various actions depending on the current task, whereas a button should be a persistent fixture of a layout. </p><p>Chips represent forking paths for a current task, while buttons represent linear steps.</p>

Button labeled “Save task” in a task management app.

<p>Use buttons for the final step in a task</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztjqmoj-5-do.png?alt=media

Chip labeled “Save task” in a task management app.

<p>Avoid using chips to finish or progress a task</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztjqyzl-6-dont.png?alt=media

<p>Multiple chips should appear together in a set, whereas there should be no more than 3 buttons in a single arrangement.</p><p dir="ltr">Chip sets can be scrolled horizontally.</p>

Multiple chips in event reminder.

<p id="isPasted">Chips can be scrolled horizontally</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8smf6wp-07_do.png?alt=media

Single chip in event reminder.

<p>Don’t display a single chip by itself. Chips should appear in a set.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8smfmgg-08_don't.png?alt=media

<h3>Variants</h3><p>Choose the chip variant based on its purpose and author. </p><p>Does the chip represent an action (assist chip) or filter results (filter chip)? </p><p>Is its content generated by the product (suggestion chip), or by the person using the product (input chip)?</p>

4 chip variants.

<p>There are four chip variants: </p><ol class="decimal"><li><p>Assist </p></li><li><p>Filter </p></li><li><p>Input </p></li><li><p>Suggestion</p></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8smgjsw-09.png?alt=media

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:19.2933%"><p>Purpose</p></th><th style="width:12.0274%"><p>Chip variant</p></th><th style="width:44.5097%"><p>Rationale</p></th><th><p>Example</p></th></tr></thead><tbody><tr><th style="width:19.2933%"><p>Action</p></th><td><p><a href="/m3/pages/chips/guidelines#5dd1928c-1476-4029-bdc5-fde66fc0dcb1" target="_self">Assist chip</a></p></td><td><p>Assist chips represent smart or automated actions that can span multiple apps</p></td><td><p><strong>Add to calendar</strong> action</p></td></tr><tr><th style="width:19.2933%"><p>Filter</p></th><td><p><a href="/m3/pages/chips/guidelines#8d453d50-8d8e-43aa-9ae3-87ed134d2e64" target="_self">Filter chip</a></p></td><td><p>Filter chips represent filters for a collection</p></td><td><p>Platform selector on material.io/components</p></td></tr><tr><th style="width:19.2933%"><p>Information, user-authored</p></th><td><p><a href="/m3/pages/chips/guidelines#4d2d5ef5-3fcd-46e9-99f2-067747b2393f" target="_self">Input chip</a></p></td><td><p>Input chips represent discrete pieces of information entered by a person</p></td><td><p>Gmail contact in the <strong>To</strong> field</p></td></tr><tr><th style="width:19.2933%"><p>Information, product-authored</p></th><td><p><a href="/m3/pages/chips/guidelines#36d7bb16-a9bf-4cf6-a73d-8e05510d66a7" target="_self">Suggestion chip</a></p></td><td><p>Suggestion chips help narrow a person’s intent by presenting dynamically-generated suggestions</p></td><td><p>Suggested chat response</p></td></tr></tbody></table></div>

<h2 id="isPasted">Anatomy</h2>

Diagram of 4 elements of a chip.

<ol><li>Container</li><li>Label text</li><li>Leading icon or image (optional)</li><li>Trailing icon (required for input chips, optional for filter chips)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztjtuyd-10.png?alt=media

<h3 dir="ltr" id="isPasted">Container</h3><p dir="ltr">All chips are slightly rounded with an 8dp corner.</p>

Diagram of rounded corner of chip container.

<p><span style="white-space:pre-wrap">Chips have rounded corners</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8wn25i4-12_do.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/vQmC7jK0blnznQXHhWp0CdSBv5rz2kM_HaE4_6bNjPYJZ7m8esMLk2mjsq3d_YYoNHL1DVWS0mNeggD2YPKFRWq7LmdauD2q4_QeqAhbh7ZFng=s1352

<p><strong>Shadows &amp; elevation</strong></p><p>Chip containers can be elevated if placed on top of an image or dynamic background.</p>

3 elevated assist chips above image of restaurant photograph.

<p>When on complicated backgrounds, chip containers can be elevated</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm99ytacz-13.png?alt=media

3 variants of chips in an outlined style.

<p>Use an outline to define the edge of the chip's container on regular backgrounds</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8smkogw-14_do.png?alt=media

3 variants of chips in an elevated style above restaurant photograph.

<p>Chips may use elevation when placed on an image</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sml3zk-15_do.png?alt=media

4 elevated chips above blank background.

<p>Chips shouldn't be elevated when placed directly on the page</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8smnajs-16_don't.png?alt=media

Elevated chip in pressed state.

<p>Avoid using elevation to indicate a chip's pressed state. Instead, use the visual ripple effect.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm9a01xre-17_don't.png?alt=media

<h3 dir="ltr" id="isPasted">Label text</h3><p dir="ltr">Chip label text should be 20 characters or fewer, and have the same typography style as <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element>.</p><p dir="ltr">Chip labels should remain brief for the limited space available. Skip conventional grammar rules, such as articles (take "a" walk), to save space.</p>

Filter chip in maps app labeled “Walking.”

<p>Keep chip labels short</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztjz5d8-17-do.png?alt=media

Filter chip in maps app labeled “Walking navigation session."

<p>Avoid chip labels longer than 20 characters</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztjzmjd-18-dont.png?alt=media

<h3 dir="ltr" id="isPasted">Leading icon or image (optional)</h3><p dir="ltr">Chips can contain a leading icon, logo, or circular image. Use a system icon to help identify a chip's category.</p>

2 input chips, 1 with a leading circular avatar and the other with a leading icon.

<p>Chips can contain a logo, icon, or circular image</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8zizvw6-21.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/54paAbiWax0rtT9FkGkAokFuFZqCr77ChCZATiYDeSdKuytmj1yIEIO62QDdSfxj4J7O3l5DX-BNOXTkj8b7RTpJRIxe6Wvioy0UPzXRudFQ=s1352

<p>The leading icon color for unselected chips can be customized through theming. While the default <app-froala-tooltip-element description="Color roles are assigned to UI elements based on emphasis, container type, and relationship with other elements. This ensures proper contrast and usage in any color scheme." link-label="More on color roles" link-url="/m3/pages/color-roles" should-open-link-in-new-tab="true">color role</app-froala-tooltip-element> is <strong>primary</strong>, the <strong>on surface variant</strong> color role is a good alternative when the icon style requires less emphasis.</p>

2 screens of a restaurant page with chips labeled "Add photos" and "Add dishes." The leading icons are purple in 1, grey in the other.

<p><strong>Primary</strong> color (left) and <strong>on surface variant</strong> color (right)</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztk48sd-20.png?alt=media

<p dir="ltr" id="isPasted">Leading circular images are sized larger than leading icons to provide more space for detail. Icons are designed to <span style="font-size:1rem;background-color:initial;color:inherit">be legible at small sizes.</span></p><p dir="ltr">See the <a href="/m3/pages/chips/specs/">Specs tab</a> for precise measurement values.</p>

2 input chips, 1 with a 24dp leading avatar and the other with an 18dp leading icon.

<p>Leading images, such as avatars, are sized larger than leading icons or logos</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8zj3zjt-24.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/iY2D7FmINqLpS43Y2mhnr_dlNru2sEZCNSyKFwJS_NVseYGAGlY-nRl_qYY4hn_zu4NTZV40NTysX2qaS3NPnh_J6StQbI4mlzvSQkQm3RU=s1352

<h3 dir="ltr" id="isPasted">Trailing icon (optional, input and filter chips only)</h3><p dir="ltr">The trailing icon is present for input and <app-froala-tooltip-element description="Filter chips use tags or descriptive words to filter content. They can be a good alternative to toggle buttons or checkboxes." link-label link-url should-open-link-in-new-tab="false">filter chips</app-froala-tooltip-element>.</p><p dir="ltr">On input chips, it's required and must be used to remove the chip. On filter chips, it's optional, and can be used to open a menu or remove the chip. </p><p dir="ltr">Secondary actions (such as a trailing icon button for <strong>Remove</strong>) must have a 48x48dp interaction target that doesn’t interfere with the chip's primary action (such as <strong>Edit</strong> or <strong>Drag</strong>). To achieve this, apply a minimum width of 88dp to the chip, or 42dp to the label text.</p>

A chip with 88dp min width has 2 touch targets of 48x48dp.

<p>Interaction targets for actions like <strong>Edit</strong> or <strong>Close</strong> have a size of 48x48. This can be achieved by setting the minimum container width to 88dp.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8wnoowx-25.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/FF2wTImHI_AYyfSWhT1XCU8XZj6mbCYc84FMCxjtZZ_lLum6wzABXhazLjGsceEqE9PWB44gmD3DO-j7lbjTrqCa507LWu-t7hdlSLxXt-M=s1352

<h2 id="isPasted">Assist chips</h2>

<p id="isPasted">Assist chips represent smart or automated actions that can span multiple apps, such as opening a calendar event from the home screen. Assist chips function as though the person asked an assistant to complete the action. They should appear dynamically and contextually in a UI.</p><p>An alternative to assist chips are <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">buttons</app-froala-tooltip-element>, which should appear persistently and consistently.</p>

2 assist chips labeled “Add to my itinerary” and “12 mins from hotel” on map screen about Los Cantantes.

<p>The text in most assist chips begins with a short verb, like <strong>Get </strong>or <strong>Add</strong></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8zjf1m3-24.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/uNDidhMjsDIxQhluaJHdkbRj_xJDpjTTfZN_YLW9tgVUwfShHRsuZgBfzSHWqjR4XJaPR-Hd1AqajUFnrPbtW1LW0c6NrrNYgNb5efdO7pbr=s1352

2 assist chips labeled “Event location” and “Chat” on phone lock screen.

<p>An assist chip can surface supplemental information like a calendar event, as well as provide contextual actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8smwopa-25.png?alt=media

Assist chip transformed into time picker with radio buttons.

<p>During an interaction, assist chips can transform into modals, transition into full-screen views of new content, or readjust to display more results inline</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8smx4qo-26.png?alt=media

<p>Assist chips can trigger an action or show progress and confirmation.</p><p>Write assist chips like buttons: start with a verb. Adjust text dynamically if the state changes, like <strong>Save</strong> to <strong>Saved</strong>.</p>

3 assist chips labeled “Mail,” ”Messenger”, and “Video Chat” on a travel article.

<p>Tapping an assist chip triggers a contextual action</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm6bar2g2-GM3-Components-Chips-Guidelines-1.1-3P-v01.mp4?alt=media

Assist chip showing confirmation upon selection.

<p>Assist chips can show progress and confirmation feedback</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm6af1abe-GM3-Components-Chips-Guidelines-1.2-v01.mp4?alt=media

<p>Assist chips are displayed after primary content, such as below a <app-froala-tooltip-element description="Cards display content and actions about a single subject." link-label="More on cards" link-url="/m3/pages/cards/overview" should-open-link-in-new-tab="true">card</app-froala-tooltip-element> or persistently at the bottom of a screen.</p>

3 assist chips labeled “Turn on lights”, “Set alarm”, and "Close Blinds" on Welcome Home screen.

<p>Assist chips should be shown underneath primary content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8wo1u2m-30.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/uqMzoI8CijB6iWV4gF5J6aL2rQ4W7JhsIrcJN98krkKJzpyDj1q9Oij6s5VAl7NVQ_LKzVyXwPf3B12ssVbtX8qsCHB7JUmPYjP8nXwY2pWNpw=s1352

<h2 id="isPasted">Filter chips</h2>

<p dir="ltr" id="isPasted">Filter chips use tags or descriptive words to filter content. They can be a good alternative to <app-froala-tooltip-element description="Segmented buttons help people select options, switch views, or sort elements." link-label="More on segmented buttons" link-url="/m3/pages/segmented-buttons/overview" should-open-link-in-new-tab="true">segmented buttons</app-froala-tooltip-element> or <app-froala-tooltip-element description="Checkboxes let users select one or more items from a list, or turn an item on or off." link-label="More on checkboxes" link-url="/m3/pages/checkbox/overview" should-open-link-in-new-tab="true">checkboxes</app-froala-tooltip-element> when viewing a list or search results.</p><p dir="ltr">Tapping on a filter chip activates it and appends a leading checkmark icon to the starting edge of the chip label.</p><p dir="ltr">Write filter chips with nouns that describe the category to <strong>include</strong> in the results. Avoid negative phrases like <strong>Exclude images</strong>.</p>

4 filter chips labeled “Docs” “Slides” “Sheets” and “Images” with “Slides” and “Sheets” selected

<p>Filter chips rely on tags or descriptive words to filter content</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmd8wjrh5-31.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/_FpN2Q4Pn2ev44ZnzH3j7EUtUJdwZ7AqRLNVQjhY8btJIKk135AcrsJAjufT287fOoUU5QbPvcm586-RL9RJTPDGJSBQAW7WZ1QIQabJ5P1Naw=s1352

5 filter chips representing popular electronics categories in a shopping app. The chip “Game consoles” is selected. 

<p>Filter chips in a shopping app</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sn3s8s-32.png?alt=media

6 filter chips representing apartment amenities in a real estate app. 2 of the chips are selected.

<p>Filter chips in a real estate app</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sn4ehq-33.png?alt=media

<p>Tap a chip to select it. Multiple chips can be selected or unselected.</p>

6 filter chips representing apartment amenities in a real estate app. 3 selected chips include checkmarks while 3 don’t.

<p>An icon can be added to indicate when a filter chip is selected</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm9a0g8g2-34.png?alt=media

3 amenities chips are selected, and 2 neighborhoods. 

<p>Filter chip suggestions can dynamically change as a person starts to select filters</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm9a0gd06-35.png?alt=media

<p>Alternatively, a single chip can be selected. This offers an alternative to <app-froala-tooltip-element description="Segmented buttons help people select options, switch views, or sort elements." link-label="More on segmented buttons" link-url="/m3/pages/segmented-buttons/overview" should-open-link-in-new-tab="true">segmented buttons</app-froala-tooltip-element>, <app-froala-tooltip-element description="Radio buttons let people select one option from a set of options." link-label="More on radio buttons" link-url="/m3/pages/radio-button/overview" should-open-link-in-new-tab="true">radio buttons</app-froala-tooltip-element>, or single select <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menus</app-froala-tooltip-element>.</p><p>However, avoid mixing chip set behaviors. All chip sets on a page should be either single-select or multi-select.</p>

 filter chips labeled “Extra soft”, “Soft”, “Medium”, and “Hard” First, the “Extra soft” chip is selected, then it unselects as the “Medium” chip is selected.

<p>Filter chips can be set so that selecting a single chip automatically deselects all other chips in the set</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8zkgr9j-GM3_Chips_Guideline_36_IA_v01.mp4?alt=media

<p>In <app-froala-tooltip-element description="Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation." link-label="More on medium breakpoints" link-url="/m3/pages/breakpoints/medium" should-open-link-in-new-tab="true">medium</app-froala-tooltip-element> and <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints</app-froala-tooltip-element>, filter chips may contain a trailing icon to directly remove the chip or open a menu of options.</p><p>In <app-froala-tooltip-element description="Window widths smaller than 600dp, such as a phone in portrait orientation." link-label="More on compact breakpoints" link-url="/m3/pages/breakpoints/compact" should-open-link-in-new-tab="true">compact windows</app-froala-tooltip-element>, the trailing icon's target area is too small to be accessible on its own. However, if the whole chip can be selected to accomplish the action, the chip is likely still accessible.</p>

Filter chip with trailing remove icon.

<p>The remove icon helps users remove the filter</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8wocw84-37.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/AuxLEZb_nITl-CQputrqxzcMPXUeBkAvV1sFuT342wVPxav9dFEaTYNz201yWxHk9c6yEh-UInDpcA3h2-7znxXB9F3PCNiJIl5mzaTD3l0DFQ=s656

Filter chip with trailing menu icon.

<p>Filter chips can open a menu for more filtering options</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8wodig6-38.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/fi0lCD-KiEpAYuO3SZr2jI2I3WWk6us7PlDgn7VIJ2Q7BBCY9fy0LFaLaq3HFIm3JUbnOp8ULGZ5_QEXYFT27T6cbUGSVpuC8mDcsbWcjwiqzg=s656

<p dir="ltr" id="isPasted">When combined with a <app-froala-tooltip-element description="Menus display a list of choices on a temporary surface." link-label="More on menus" link-url="/m3/pages/menus/overview" should-open-link-in-new-tab="true">menu</app-froala-tooltip-element>, the filter chip opens a list of selectable options.</p>

In a trail selector mobile app, a person selects the whole chip to change the menu selection from Walking to Cycling. 

<p>In compact windows, make sure the whole chip opens the menu. Otherwise, the target area is likely too small to be accessible.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8zkn8ku-GM3_Chips_Guideline_39_IA_v01.mp4?alt=media

<p>Filter chips can be used with other components, such as <app-froala-tooltip-element description="Search lets people enter a keyword or phrase to get relevant information." link-label="More on search" link-url="/m3/pages/search/overview" should-open-link-in-new-tab="true">search</app-froala-tooltip-element> fields and <app-froala-tooltip-element description="Side sheets show secondary content anchored to the side of the screen." link-label="More on side sheets" link-url="/m3/pages/side-sheets/overview" should-open-link-in-new-tab="true">sheets</app-froala-tooltip-element>.</p>

4 filter chips below search field

<p>Filter chips can be shown underneath a search field</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8woi0j8-40.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/gVJ_TV4PsMN0Mhs-oAUEG47Gu9cYDp-T3LPvFLnsFv6yImHWTuuocs9l9en82TB_OrYoW31ffefMMp-rM8UQLo9RnXM5KCNjnbaC2cHrJNim=s1352

Filter chips used as tags in a side sheet on a file application.

<p>Use a side sheet to organize many filter chips</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8sni3vn-41.png?alt=media

6 filter chips wrapping to 2 rows

<p>Filter chips can wrap to a new row. If there are more than two rows, consider using horizontal scrolling to access them all.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztl3mne-41.png?alt=media

4 filter chips with right-most chip partly offscreen, indicating the chips are horizontally scrollable

<p>Filter chips can scroll horizontally to show many options</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztl40h2-42.png?alt=media

Single filter chip option beneath the header “Category”

<p>Filter chips should not present only a single option</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztl535g-43-dont.png?alt=media

<h2 id="isPasted">Input chips</h2>

<p id="isPasted">Input chips represent discrete pieces of information entered by a person, such as Gmail contacts or filter options within a <app-froala-tooltip-element description="Search lets people enter a keyword or phrase to get relevant information." link-label="More on search" link-url="/m3/pages/search/overview" should-open-link-in-new-tab="true">search</app-froala-tooltip-element> field.</p><p>They enable user input and verify that input by converting text into chips.</p>

Contacts transformed into 2 input chips in a draft event invite

<p>Input chips transform text based on a person's input</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8zjw6tr-46.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/UDjFkP1FOVQtew8xhKWpOI1bUKi2OeWXXgjETDRqn-1ZKzXFw0YNX3UYDJgk_b5s0rKIdh4CJEsU9LARx6SyEmwlGQ8CeeNVyhDxNu1EcQze=s1352

<p>Input chips can support editing to change their contents, such as correcting an email address. In edit mode, the chip reverts back to a text string. Editing can be triggered by interacting with the chip, either by selecting it or by a second interaction after selection.</p>

Contact transformed into input chip in the “To” filed of an email draft.

<p>Input chips converted from email addresses are editable</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm6baqmrn-GM3-Components-Chips-Guidelines-4-3P-v01.mp4?alt=media

Animation showing selection of chip with backspace key.

<p>Using the backspace key with the cursor before a chip selects the entire chip. The chip can then be deleted when the user taps the backspace key again.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8spbow8-GM3_Chips_Guideline_49_IA_v01.mp4?alt=media

<p>A single field can contain multiple <app-froala-tooltip-element description="Input chips represent discrete pieces of information entered by a user, such as Gmail contacts or filter options within a search field." link-label link-url should-open-link-in-new-tab="true">input chips</app-froala-tooltip-element>. These chips can be reordered or moved into other fields.</p>

2 input chips in the “To” field of an email draft

<p>Multiple input chips in one field</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8wovhxb-52.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/RgxqbsfzegYgXFAqY6gFgnc_m2Y36fjQfW7cr4h2J7Ar-4eMA8m0sHuYBD9omPg3Fkq4HkU7pIYsAccWpS-kWnkS97zPCTRG7B6rcY7hQfE=s656

1 input chip moved from the “To” field to the “CC” field of an email draft

<p>Input chips being moved from one field to another</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm01e2s34-48-3p.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/ei0DgkxK6YByXQJYx-ZgaGig9oudQEyPHJ8RwkOQ5txRR4sS9ZrlCXyd0Q0Z2N7lQohHqVgD7hvMnuz21gYIfDzTZN3FrsZnHyvM0aPTsQNE=s656

<p>Input chips can expand to show more information or options. A container transform transition pattern is used to reveal additional content.</p>

Contact input chip expands to show multiple email addresses for that contact

<p>Input chips can expand</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm6baqa1g-GM3-Components-Chips-Guidelines-6-3P-v01.mp4?alt=media

<h3 dir="ltr" id="isPasted">Placement</h3><p dir="ltr">Input chips can be integrated with other components.</p><p dir="ltr">They can appear:</p><ul><li>Inline with the cursor in a text field</li><li>In a stacked list</li><li dir="ltr">In a list that can be horizontally scrolled</li></ul>

4 input chips wrapping to 2 rows.

<p>Input chips can wrap to a new row if all chips need to be visible</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm6bamolo-50.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/6ESM4iq-ENjgdXPRgFeaoVpZE2mUv1aL6soIeRHZgDxwAUJTQ2HYdWnCUQSYjaWVl5l7kvSbi9Rtn7NICABYNrE_6230Wv7OxhfoXLs6uN5kSg=s656

3 input chips horizontally scrolling.

<p>Input chips can scroll horizontally</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm8zkwi4x-GM3_Chips_Guideline_58%20-%203P%20-_IA_v01.mp4?alt=media

<h3 dir="ltr" id="isPasted">Icons &amp; images</h3><p dir="ltr">The leading icon of input chips can be an icon, logo, or circular image.</p>

2 input chips, 1 with leading thumbnail, 1 with leading icon.

<p>Input chips can contain an icon, logo, or circular image</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8snzt8q-60.png?alt=media

<p dir="ltr" id="isPasted">The trailing icon is always aligned to the end side of the container. It’s placed:</p><ul><li dir="ltr">On the right for left-to-right (LTR) languages, such as English</li><li dir="ltr">On the left for right-to-left (RTL) languages, such as Farsi</li></ul>

2 input chips with trailing icons following the label text.

<p>Input chips can be a more flexible way to filter search results, compared to filter chips</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztl8hee-55.png?alt=media

3 input chips with trailing icons following the label text.

<p>Input chips make it easier to add and remove contacts</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm01e408l-56.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/OW0kvrMWhnBCzG4I54KY3xyHktBmFAy75DO82QINdcwZjOKXf4O1cd8TH6sxo2ptCx7Y7wkGkxDnPLfuaI-CLAcLAx-BbkdleTuyJDLH5fBw=s656

Animation of overflowed chips in a text field.

<p><span style="white-space:pre-wrap">Overflowed chips in a text field should follow the same behavior as regular text. An unfocused text field with overflowed content should display the beginning of the input. Tapping the field snaps the user to the end of the input with the cursor and keyboard active.</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm8so4v60-GM3_Chips_Guideline_64_IA_v01.mp4?alt=media

<h2 id="isPasted">Suggestion chips</h2>

<p>Suggestion chips help narrow a user’s intent by presenting dynamically generated suggestions, such as possible responses or search filters.</p><p>Write suggestion chips as nouns or short phrases, depending on context. Avoid exceeding 20 characters when possible.</p>

3 suggestion chips offering ID options in a photo-recognition app.

<p>The text labels within suggestion chips are most often nouns or short phrases</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm99yzvnz-65.png?alt=media

3 suggestion chips with automated reply options in a chat app.

<p>Suggestion chips can offer quick-reply options in a chat or email app</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztlb0cw-60.png?alt=media

2 suggestion chips with search options “What song is this?” and “What are the lyrics?”

<p>A suggestion chip can help the user start a search</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztlbx06-61.png?alt=media

<h3>Placement</h3>

<p id="isPasted">When displaying multiple chips together, place them inline as a row of options, not listed vertically. Overflowing chips should break to the next line. </p><p>If the field is only one row high, chip sets can scroll horizontally instead.</p><p>Keep an 8dp minimum space between chips. Chips must also have a minimum 48dp target size, regardless of placement or density. If required, the target can extend beyond the visible container of the chip.</p><p>Text labels for chips should be concise. Chip labels will truncate when in a wrapped layout, and when they are wider than the full width of the window.</p>

Diagram of margins between a set of chips.

<ol><li id="isPasted">Margins between chips </li><li>Margin between each line</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flztlcsh2-62.png?alt=media

## Accessibility

<h2>Use cases</h2>

<p id="isPasted">People should be able to do the following with assistive technology:</p><ul><li>Use a chip to perform an action</li><li>Navigate to a chip </li><li>Activate a chip </li></ul>

<h2>Interaction &amp; style</h2>

<p>The chip label needs at least 3:1 contrast with the background.</p><p>A chip that performs an action should present the same semantics as a <app-froala-tooltip-element description="Buttons let people take action and make choices with one tap." link-label="More on buttons" link-url="/m3/pages/common-buttons/overview" should-open-link-in-new-tab="true">button</app-froala-tooltip-element> to a platform's accessibility API.</p>

The chip label needs to pass 3:1 contrast.

<p>High contrast helps differentiate chips clustered together</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm99z66s4-01.png?alt=media

<h3 id="isPasted"><span style="white-space:pre-wrap">Horizontal overflow</span></h3><p><span style="white-space:pre-wrap" id="isPasted">When there are too many chips to fit on one row, provide a way to display them all at once and avoid scrolling. </span></p><p><strong>Reflow method: </strong>Use a filter chip as a leading element to reflow the horizontal list. This should shift down the content below and make room for all chips to show. </p>

Selecting a leading button pushes chips previously reachable only by scroll below, making them all visible.

<p><span style="white-space:pre-wrap">The <strong>Show all </strong>filter chip is used to reflow the list, displaying all chips at once and pushing down the content below</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm9a4c1yw-GM3_Chips_Guidelines_07_IA_v01.mp4?alt=media

<p><span style="white-space:pre-wrap" id="isPasted"><strong>Menu method: </strong>Create a leading button to display all chip options in a menu. Use this option to avoid shifting the position of the content below.</span></p><p><span id="isPasted">Don’t use the menu method on chips with a second action, like a remove icon.</span></p>

Selecting a filter button produces a menu with all previously hidden chips visible.

<p><span style="white-space:pre-wrap">The <strong>Show all</strong> leading button shows a menu of chip options, keeping the place of content below</span></p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fm9a4cs1u-GM3_Chips_Guidelines_08_IA_v01.mp4?alt=media

<h3 id="isPasted">Avoid applying density by default</h3><p>Don't apply density to chips by default — this lowers their targets below our best practice of 48x48 CSS pixels. Instead, give people a way to choose a higher density, like selecting a denser layout or changing the theme.</p><p>To ensure that this density setting can be easily reverted when it's active, keep all the targets to change it at minimum 48x48 CSS pixels each.</p>

<h2>Keyboard navigation</h2>

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="width:17.15%">Keys</th><th style="width:82.85%">Actions</th></tr></thead><tbody><tr><td><strong>Tab</strong></td><td>Moves focus to <app-froala-tooltip-element description="An enabled state communicates an interactive component or element." link-label="More on enabled state" link-url="/google-material-3/pages/interaction-states/applying-states#79d4c7b3-bd64-49ba-90f1-3eeb62f1b328" should-open-link-in-new-tab="true">enabled</app-froala-tooltip-element> chip or chip group</td></tr><tr><td><strong>Space</strong> or <strong>Enter</strong></td><td>Activates, selects, or deselects the focused chip</td></tr><tr><td><strong>Backspace</strong> or <strong>Delete</strong></td><td>Removes currently <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/google-material-3/pages/interaction-states/applying-states#bfc1624f-6bcc-4306-b0c1-425e2d8a1bf9" should-open-link-in-new-tab="true">focused</app-froala-tooltip-element> input chip</td></tr><tr><td><strong>Arrows</strong></td><td>Moves focus between chips</td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><thead><tr><th style="width:20%"><p>Element</p></th><th style="width:20%"><p>A11y label</p></th><th style="width:20%"><p>Role (Web)</p></th><th style="width:20%"><p>Role (Android Views (MDC-Android))</p></th><th style="width:20%"><p>Role (Jetpack Compose)</p></th></tr></thead><tbody><tr><th style="width:20%"><p>Image / Icon within chip</p></th><td><p>Hide image</p></td><td><p>-</p></td><td><p>-</p></td><td><p>-</p></td></tr><tr><th style="width:20%"><p>Basic chip (one action)</p></th><td><p>“{chip content}”</p></td><td><p>gridcell</p></td><td><p>button</p></td><td><p>button</p></td></tr><tr><th style="width:20%"><p>Selectable chip</p></th><td><p>“{chip content}”</p></td><td><p>gridcell</p></td><td><p>radio button</p></td><td><p>checkbox</p></td></tr><tr><th style="width:20%"><p>Remove icon (no other action)</p></th><td><p>“Remove {chip content}”</p></td><td><p>-</p></td><td><p>-</p></td><td><p>-</p></td></tr><tr><th style="width:20%"><p>Two actions (e.g., select + remove)</p></th><td><p>“{chip content}.” Then</p><p>“Remove {chip content}”.</p></td><td><p>button or checkbox</p></td><td><p>button or checkbox</p></td><td><p>button or checkbox</p></td></tr></tbody></table></div>

<p>The accessibility label for a chip is the chip's label text. Additional actions, like remove, are labeled separately.</p>

Accessibility tags for a chip.

<p>Accessibility tags should include both the label and role</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmderzcwe-02.png?alt=media

<h3>Multi-select</h3><p><span style="white-space:pre-wrap">For multi-select chip sets, <strong>Space</strong> or <strong>Enter</strong> will select the <span style="white-space:pre-wrap" id="isPasted">focused</span> chip and allow you to select all of the chips. <strong>Space</strong> or <strong>Enter</strong> will also deselect a focused selected chip. </span></p>

Accessibility tags for a multi-select chip.

<p>While multiple chips can be selected, only one can be in focus</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmderoau5-25.png?alt=media

<h3 id="isPasted">Drop-down list</h3><p id="isPasted">The accessibility label should align with each list item’s text label. </p><p>For list items with text and an icon, the accessibility label should be marked as decorative to avoid redundant verbalizations.</p>

Accessibility tags for a drop-down list chip.

<p>The accessibility label should be the text label</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd78nzr3-04.png?alt=media

<h3 id="isPasted">Input chip remove action</h3><p id="isPasted">Display the remove icon whenever a chip can be removed. On mobile, if remove is the only chip action, the remove icon isn't necessary. Instead the chip can be removed by selecting it and pressing the <strong>Delete</strong> key on the keyboard.</p><p>Each chip is a focusable element. </p><ul><li>If a chip only has a remove icon, the entire chip and icon are one focusable element. </li><li>If a chip has a second action, like select, then the chip content and remove icon are two separate focusable elements.</li></ul>

A focused remove action within a chip.

<p><span style="white-space:pre-wrap">The remove action is focused when the chip can also be selected</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmdfzbasm-06.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/6ogPU6jU6ecd-bIOHVBsztMIVbrMh9QFdEYLITFw2dbd9atxkbPCtGrNHZfykUnYCCmQUR4-XY9KTUDAeDG3GCh60nDvFFCG41_E8r2o88yq=s1352

<h3>Showing chip interactivity</h3><p>Material requires that chips use a secondary indicator to show that they are interactive in context, allowing users with low vision and cognitive disabilities to see them. <br /><br />Use one of the following methods: <br /></p><ul><li><p>Add a label before the chip group suggesting interaction, such as <strong>Select type</strong></p></li></ul>

Label saying “Select type” above a series of chips, with “Extra soft” selected.

<p>Labels introducing a chip group can indicate that they are selectable</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn7orxd0-09.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/gkYkp2thJm8NuXg0WkQDTthTjMCckk44U7U8HKxA322oYbQbIfE60aLw8mRpl4zG3yP9iM7xRKvISOEvSe0IzALT4v90lUxmkhX8Gk7tgYVg=s1352

<ul><li><p>Provide interactive page context, such as <strong>Filter results</strong>, indicating chips can be selected to narrow results</p></li></ul>

Page context saying “Filter results” above chips listing different categories.

<p>Page context can indicate how search results will be narrowed by selecting chips</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn7p0i6r-10.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/jEO4v0siZwhGUJRWwN3qHEggxZU7YO42T-yV1X2_7zuBm9bW_mHSE1cJ1U2YAh6fDxdvjv10zK9Jzn9tbNH7qdhR7ftNlEZUoNmMlN4oCjcPQg=s1352

<ul><li><p>Use the <strong>outline</strong> color role, instead of <strong>outline variant</strong>, to ensure a minimum 3:1 contrast</p></li><li><p>Include an interactive chip label, such as <strong>Turn on lights</strong>, or leading icon</p></li></ul>

A selectable chip with more pronounced outline stroke.

<p>Chips can show they are interactive with a darker outline color stroke</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn7ot1xs-11.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/3mkdqveEbxIinncg25_qmQvewzApIKUm8jK3Nml2ratbJLBLBhBUCNYcrGFsb-7nevBxFssZdACgsezFIgK8Rh_1MrIi8kmE2fxWpLg1iDSQ=s656

A chip labeled “Turn on lights” with a leading icon related to lights.

<p>Chips can also use a leading icon or label to show interactivity</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn7p0649-11%20(1).png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-PJSF2Rl5Xam0GLsqoqkWXhm3VNqDgZh7B3Ck1pLkVFTuPzwhSR9H-DXgfQOVggcz-CaZrqh4kh8DAR0LsSUZuwOBKeyMN75JYf5L_e2rKigVQ=s656
