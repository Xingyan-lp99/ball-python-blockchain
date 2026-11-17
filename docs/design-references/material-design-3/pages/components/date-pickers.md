# Date pickers

Source: https://m3.material.io/components/date-pickers
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/523144a0-9184-44bd-93f0-5b4c7355f421.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

## Overview

<ul><li><p>Date pickers can display past, present, or future dates</p></li><li><p>Three variants: <app-froala-tooltip-element description="Docked date pickers open from an onscreen input similar to a text field. They're often used within forms." link-label="More on docked date pickers" link-url="/google-material-3/pages/date-pickers/guidelines#8d78696c-a756-4a4d-b7dd-846d866ba985" should-open-link-in-new-tab="true">docked</app-froala-tooltip-element>, <app-froala-tooltip-element description="Modal date pickers extend full-screen. They're often used for selecting a date range." link-label="More on modal date pickers" link-url="/google-material-3/pages/date-pickers/guidelines#ced55f72-28b5-4f5d-a347-fa38214ef2d4" should-open-link-in-new-tab="true">modal</app-froala-tooltip-element>, <app-froala-tooltip-element description="Modal date inputs allow the manual entry of dates using the numbers on a keyboard. They're often used in compact layouts." link-label="More on modal date inputs" link-url="/google-material-3/pages/date-pickers/guidelines#d91ce7bc-dbc7-43e3-a802-152f2f9c892a" should-open-link-in-new-tab="true">modal input</app-froala-tooltip-element></p></li><li><p>Clearly indicate important dates, such as current and selected days</p></li><li><p>Follow common patterns, like a calendar view</p></li></ul>

3 variants of date pickers side-by-side. The docked date picker has an outlined text field above a calendar view. The modal date picker allows people to select a date from a calendar view. The modal date input lets someone type in a date.

<ol><li>Docked date picker</li><li>Modal date picker</li><li>Modal date input</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5mxu7o-01.png?alt=media

<h2>Availability &amp; resources</h2>

resourceName: designSystems/030656e0a1083ef1/components/13ab9956d1c04e88

libraryModuleType: STATUS_TABLE

<h2>Differences from M2</h2>

<ul><li><p>Typography and spacing: Titles and labels are larger and have increased spacing to accommodate 48dp target size</p></li><li><p>Color: New color mappings and compatibility with <app-froala-tooltip-element description="Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI." link-label="More on dynamic color" link-url="/m3/pages/dynamic/choosing-a-source" should-open-link-in-new-tab="true">dynamic color</app-froala-tooltip-element></p></li><li><p>Variants: The three variants of date pickers have been renamed to not be device-dependent. The former desktop date picker is now known as the <app-froala-tooltip-element description="Docked date pickers open from an onscreen input similar to a text field. They're often used within forms." link-label="More on docked date picker" link-url="https://m3.material.io/m3/pages/date-pickers/guidelines#8d78696c-a756-4a4d-b7dd-846d866ba985" should-open-link-in-new-tab="true">docked date picker</app-froala-tooltip-element>. The former mobile date picker and date input are now known as <app-froala-tooltip-element description="Modal date pickers extend full-screen. They're often used for selecting a date range." link-label="More on modal date picker" link-url="/m3/pages/date-pickers/overview" should-open-link-in-new-tab="true">modal date picker</app-froala-tooltip-element> and <app-froala-tooltip-element description="Modal date inputs allow the manual entry of dates using the numbers on a keyboard. They're often used in compact layouts." link-label="More on modal date input" link-url="/m3/pages/date-pickers/overview" should-open-link-in-new-tab="true">modal date input</app-froala-tooltip-element> to reinforce that the user must take an action.</p></li></ul>

Old version of a date picker with a white background and shadows.

<p>M2: Date pickers had a drop shadow and different color mappings</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fle4qmou9-1P-datepicker_whatsnew_1.png?alt=media

New version of date picker with a colorful background, rounded corners, and no shadows.

<p>M3: Date pickers have larger typography, no shadow, and new color mappings compatible with dynamic color</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmd5mtxw0-03.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/HWA4owUgCVU0oIuTW-9x1wyLuHIA6m_aaks97Ih_BEz-wvMRKQqmb8-FsElnU5Jxck9-Hi-br9L52IDZBwYY22tVVJyY8NtOKnsOlqxB8gJdpQ=s1004

## Specs

<h2>Tokens &amp; specs</h2><p>Select a component variant below to see its elements, attributes, <app-froala-tooltip-element description="Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code." link-label="More on tokens" link-url="/m3/pages/design-tokens/overview" should-open-link-in-new-tab="true">tokens</app-froala-tooltip-element>, and their values.</p>

resourceName: designSystems/20543ce18892f7d9/components/01c5310367774eb8

libraryModuleType: TOKEN_TABLE

moduleConfigurationOverrides: {'tokenSets': ['Date picker - Docked', 'Date picker - Modal', 'Date picker - Modal input'], 'contextTags': ['None', 'Medium contrast', 'Default', 'High contrast', 'Static', '3P', 'Android', 'Dark', 'Light'], 'tokenSetOrder': ['Date picker - Docked', 'Date picker - Modal', 'Date picker - Modal input'], 'hideSearchField': False, 'hideVersionName': True}

<h2>Docked date picker</h2>

Diagram indicating the 11 elements of a docked date picker.

<ol><li>Outlined text field</li><li>Menu button: Month selection</li><li>Menu button: Year selection</li><li>Icon button</li><li>Weekdays label text</li><li>Unselected date</li><li>Today’s date</li><li>Outside month date</li><li>Text buttons</li><li>Selected date</li><li>Container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vnbm5-01-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/tETsEHo8OLEiIv-Aaw1wjb742B5Thac-7QZTp95nvITcOKMWXrSKJTl0gTnbAwyOiSl9EvWo8aMtz52MJtC8vm1VZx6EaOgPVWoP7AaDkvjs=s2048

Diagram indicating 8 elements of a docked date picker with an open dropdown menu showing the months May to November.

<ol><li>Outlined text field</li><li>Menu button: Month selection (pressed)</li><li>Menu button: Year selection (disabled)</li><li>Header</li><li>Menu</li><li>Selected list item</li><li>Unselected menu list item</li><li>Container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vo1av-02-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/MKNjpAopgtytl_kFpz85rnKyX4WdXng4gAvBAcQPMcDKWYzvwPrFzXEaKJoof31oj0KDhcCZLG0nBVwAlvpPlXrUf3UljRtKNCAjO4sC2K4w=s2048

<h3 id="isPasted"><span style="white-space:pre-wrap">Docked date picker color</span></h3><p>Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview/" id="isPasted" target="_self">Learn more about design tokens</a></p>

11 color roles of a docked date picker in light and dark themes.

<p>Docked date picker color roles used for light and dark themes:</p><ol class="decimal"><li id="isPasted">Primary</li><li id="isPasted">On surface variant</li><li id="isPasted">On surface variant</li><li id="isPasted">On surface</li><li id="isPasted">On surface</li><li id="isPasted">Primary</li><li id="isPasted">On surface variant</li><li id="isPasted">Primary</li><li id="isPasted">Surface container high</li><li id="isPasted">Primary</li><li id="isPasted">On primary</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vofa8-03-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/t5niu5LsIjOjw0wey4JXXcQ9J0PQuCxTW7cXasgVguRXLf1Sjuuv7VDs81XvQvD9GfrYj9CXwjPpij_rLi-ylLRJt6BIiv-Io_jGktOkZzY=s2048

7 color roles of a docked date picker menu in light and dark themes.

<p>Docked date picker menu color roles used for light and dark themes:</p><ol class="decimal"><li id="isPasted">Primary</li><li id="isPasted">On surface variant</li><li id="isPasted">On surface</li><li id="isPasted">Outline variant</li><li id="isPasted">Surface container high</li><li id="isPasted">Surface variant</li><li id="isPasted">On surface</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vovcl-04-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/8dm3XqLpo47xIT6RMfiGCFeylnMi_-bxLabwkeigMuXB6e17c35Pf_uhK7ykl7vKRDm5NzrY5V_rracq3Uz8KYoMRrNKA_GejWGHbtR0jRM=s2048

<h3 id="isPasted"><span style="white-space:pre-wrap">Docked date picker measurements</span></h3>

Diagram of padding, size, and layout measurements.

<p>Docked date picker padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmel11ou5-05-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/PTixdykCflNGubuMrHJpl5MMA4Gg3W9U8LDFn2SjrMoswSQ2F_uJAVkm8NtkjoxRvJbQsyUev55lyKIPDhTcgFQlGsMlruJKGYNfdOH9Lu0e1Q=s2048

Diagram of padding, size, and layout measurements.

<p>Docked date picker month menu padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmel12gcl-06-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/MTNVLCkRAS7bSuaXx8wcn3u_6dmltsszWRSC3Qo7cnc_G2Lk1K_QkeULzwaGWNidXlO12HIxRvKnYspR2Z5ae9WC-V87xrRK6I9JqpwjnZOd=s2048

<h3 id="isPasted"><span style="white-space:pre-wrap">Docked date picker configurations</span></h3>

3 configurations of docked date picker.

<ol><li>Day selection</li><li>Month selection</li><li>Year selection</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vrc28-07-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LpdT8F1acz-J6VISmCSL1-BMFHSFrOP0Ey9WkdUVp0xjdG_8xA4mWV3fz2aSuws2Sjq5YllidbsViN5M2T3XsG2mmOXzJAMlEwySnUG-GYY=s2048

<h2 id="isPasted"><span style="white-space:pre-wrap">Modal date picker</span></h2>

Diagram indicating the 13 elements of a modal date picker in the day selection view.

<ol><li>Headline</li><li>Supporting text</li><li>Header</li><li>Container</li><li>Icon button</li><li>Icon buttons</li><li>Weekdays</li><li>Today’s date</li><li>Unselected date</li><li>Text buttons</li><li>Selected date</li><li>Menu button</li><li>Divider</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vsstf-08-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/lTTHd1QoFOtnUn9kre2Ifx3m8tZlBEcNzwIbibxsbeIo3srW5t25mBOewAYkO5fFIFLzW4JA0uiDk-0srfUGaXKuUhnyTB29Xvx3prdUIZE=s2048

10 elements of a modal date picker menu.

<ol><li id="isPasted">Headline</li><li id="isPasted">Supporting text </li><li id="isPasted">Header</li><li id="isPasted">Container</li><li id="isPasted">Icon button</li><li id="isPasted">Unselected year</li><li id="isPasted">Selected year</li><li id="isPasted">Text buttons</li><li id="isPasted">Divider</li><li id="isPasted">Menu button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vtc2f-09-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/MEsCpopd1hOL195tikhDp1oekUbo_Dgjj3C8uO-1DuhPneuxpqu6Rntq6FMue_xJj6Bg0cvUFGBr3nSvdonOPiJ2nLFHghJ9rUc_uLz--W3p=s2048

Diagram indicating the 15 elements of a modal date picker when selecting a range of dates.

<ol><li>Headline</li><li>Supporting text</li><li>Icon button</li><li>Header</li><li>Text button</li><li>Icon button</li><li>Weekdays label text</li><li>Container</li><li>Today’s date </li><li>Unselected date</li><li>In-range active indicator</li><li>In-range date</li><li>Month subhead</li><li>Selected date</li><li>Divider</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vtxo6-10-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/VAgYqCiSgxR776ucqoudANiddYBjkUwzrtQPxdVWC3vLAjapPUH0OjC_aHhHU1gX-a7jAtlSdyfL6nZ8zZTRi9UggwYWdkEnMXOdZfA-5Fk=s2048

<h3 id="isPasted"><span style="white-space:pre-wrap">Modal date picker color</span></h3><p>Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview/" target="_self">Learn more about design tokens</a></p>

12 color roles of a modal date picker day selection view.

<p>Modal date picker color roles used for light and dark themes in a day selection menu:</p><ol class="decimal"><li id="isPasted">On surface</li><li id="isPasted">On surface variant</li><li id="isPasted">Surface container high</li><li id="isPasted">On surface variant</li><li id="isPasted">On surface variant</li><li id="isPasted">On surface</li><li id="isPasted">Primary</li><li id="isPasted">On surface</li><li id="isPasted">Primary</li><li id="isPasted">Primary</li><li id="isPasted">On surface variant</li><li id="isPasted">Outline variant</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vuima-11-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/KtGAhuY4gAAooTlzNro5r28R-JqaNn-GIuLF784YUnV4r9xuN73HBLIGoK2ngiHQTkEBH3-Pv5i_KhcGI86MpUTOFXtNXKl44_CULQTkD_Acjw=s2048

Diagram of 9 color roles of a modal date picker year selection view.

<p id="isPasted">Modal date picker color roles used for light and dark themes in a year selection menu:</p><ol class="decimal"><li>On surface</li><li>On surface variant</li><li>Surface container high</li><li>On surface variant</li><li>On surface variant</li><li>Primary</li><li>Primary</li><li>Outline variant</li><li>On surface variant</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vuwh7-12-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/z3NPv_bl1zhqrcVdxulXJmeLSWmbTfWTkIMYyQCoeXa4HbUQUuV3mm1rtgBDFRBxgZ__Q-YBLJ__9ffRDqk8d2anxULFonL4YcxS2u7fI12j=s2048

Diagram of 14 color roles of a modal date picker when selecting a range of dates.

<p><span style="white-space:pre-wrap">Modal date picker range selector color roles used for light and dark themes:<br /></span></p><ol class="decimal"><li id="isPasted"><span style="white-space:pre-wrap">On surface<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">On surface variant<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">On surface variant<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">Surface container high<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">Primary<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">On surface variant<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">On surface<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">Primary<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">On surface<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">Secondary container <br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">On secondary container <br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">Outline variant<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">On surface variant<br /></span></li><li id="isPasted"><span style="white-space:pre-wrap">Primary</span></li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vv9ft-13-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/KEpszqYIa1lMPVecD3eDqQDiYPTnl02lIWnD6vRP4EuLg1B1bCy9pvIWH567lYGjxPeOeC_Hdvm_CxRF8HXfi6WXlnrvKp3puWzqZxeq1g=s2048

<h3 id="isPasted"><span style="white-space:pre-wrap">Modal date picker measurements</span></h3>

Diagram of size and padding measurements in day selection view.

<p>Modal date picker padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmel16bx5-14-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Qe-iPyRhBKhCxHScEGB4S8BssYvRdETO_pEbYIPRrGLewt2ObrK4fEJXcRN7DnsWZeAWSlL0J1fXPjVuBSfxUt3ZgeFKXuRIojAVlEClcuw=s2048

Diagram of size and padding measurements in year selection view.

<p>Modal date picker year selector padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmel16puv-15-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/LkaUY6KA1A3o2AsE0U9A8Yka862hS-QLjbWWC7etGxAi8UU55KnFHwor3AeHy814pTq_IJgpND4k_UN-UPlc8cRhALLZIh6tP88xh6Lneb0s=s2048

Diagram of size and padding measurements when selecting a range of dates.

<p>Modal date picker date range selector padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmel175wp-16-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/-H_XlEpqZPu5-zavBZl448ZPXeg3RwDWwmtidrkSwPBcUKrXk0b_4uZrjvsdt-chOrMLLquYznzK0jWn8iZ_L4zJ3lR1zTkBIXwJrv3M283H=s2048

<h3 id="isPasted"><span style="white-space:pre-wrap">Modal date picker configurations</span></h3>

3 configurations of a modal date picker shown in dark mode.

<ol><li>Single date selection</li><li id="isPasted">Date range selection</li><li>Year selection</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vxg0z-17-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/X5qMWXDD7RFiXL6-gzkVulqL9pNGDfUX0efsHAsahVvpsZYW9bLkl-4UyWkXho6YWmAxoVSpz3dhhve7Rw_bFdsVFtCwp29xfoGlKrZlanIy=s2048

<h2 id="isPasted"><span style="white-space:pre-wrap">Modal date input</span></h2>

Diagram indicating the 8 elements of a modal date input.

<ol><li>Headline</li><li>Supporting text</li><li>Header</li><li>Container</li><li>Icon button</li><li>Outlined text field</li><li>Text buttons</li><li>Divider</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vxz7r-18-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/y_Bb20CqP7MSVjr8eJmNwxui08VclLGtULHxuZijAxVbdPmwcdepZbOoM1dKSK0YSXbOaKhGQqangV1Ol662UAR5TsDqKH0zzYB2hoLmkktz=s2048

<h3 id="isPasted"><span style="white-space:pre-wrap">Modal date input color</span></h3><p>Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. <a href="/m3/pages/design-tokens/overview/" target="_self">Learn more about design tokens</a></p>

Diagram indicating the 7 color roles of a modal date input.

<p>Modal date input color roles used for light and dark themes:</p><ol class="decimal"><li id="isPasted">On surface</li><li id="isPasted">On surface variant</li><li id="isPasted">Surface container high</li><li id="isPasted">On surface variant</li><li id="isPasted">Primary</li><li id="isPasted">Primary</li><li id="isPasted">Outline variant</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vyfrl-19-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/iefNrcoiuJ0ugSFq7Sr-IDU2JcAbmJPJqObTZJRuoEd3MIKOdAZZuy2PBx-hnXJEYrmXuN-BwMsIVLtdS2gzzaZrN9L_kfy-PyUDrocRjsNoYw=s2048

<h3 id="isPasted"><span style="white-space:pre-wrap">Modal date input measurements</span></h3>

Diagram of the padding and size measurements of a modal date input.

<p>Modal date input padding and size measurements</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vyzk0-20-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/M_rfbkLJHuLrKAZGQQmuEVaZMyte_u_3ybmULmG8aiNvTnIcB9OmLtKv9dswOeVNC0NML5TtfQVSUop_Q9vz5pLqrwp9Xchth7vF4cumQCuN=s2048

<h3 id="isPasted"><span style="white-space:pre-wrap">Modal date input configurations</span></h3>

2 configurations of modal date input.

<ol><li>Single date input</li><li>Date range input</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6vzozd-21-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/dL3RrXAFk0yAelVnpdVtEswLMzDgTjbDjVW1Ws00MppaklNXca5Dwx0PDdWkU6pc7SYy9I0xUXQ1ttwm38Oh7d5XCSTr6Kbph0EqGtMMgKtWbA=s2036

<h2>Element states</h2>

Diagram of 5 various states for date and year elements within date pickers.

<p>States for date and year selection: </p><ol class="decimal"><li>Default (enabled) </li><li>Disabled </li><li>Hovered </li><li>Focused </li><li>Pressed (ripple)</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fme6w02sb-22b-3P.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/6XspP-OQE7aCNEQ93nEte0mKmgkyvY2j9jfFYbQHtiUK-tfwKvK1ncuufXe5RMFHSrGkqZSvzbPTExmW-sakoDgzKxiN0ebx-ZlcVaS_afDe=s2048

## Guidelines

A date picker opens in a form UI.

<p>Docked date picker on desktop</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5o0x3j-01.png?alt=media

<h2>Usage</h2>

<p>Date pickers let people select a date or range of dates. They should be suitable for the context in which they appear.</p><p>Date pickers can be embedded into:</p><ol type="1" style="list-style-type:decimal"><li><p><app-froala-tooltip-element description="Dialogs provide important prompts in a user flow." link-label="More on dialogs" link-url="/m3/pages/dialogs/overview" should-open-link-in-new-tab="true">Dialogs</app-froala-tooltip-element> on compact <a href="/m3/pages/breakpoints" target="_blank">breakpoints</a> like mobile</p></li><li><p><app-froala-tooltip-element description="Text fields let users enter text into a UI." link-label="More on text fields" link-url="/m3/pages/text-fields/overview" should-open-link-in-new-tab="true">Text field</app-froala-tooltip-element> drop-downs on medium and <app-froala-tooltip-element description="Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop." link-label="More on expanded breakpoints" link-url="/m3/pages/breakpoints/expanded" should-open-link-in-new-tab="true">expanded breakpoints</app-froala-tooltip-element> like tablet and desktop</p></li></ol>

2 date picker variations: a dialog on mobile and a dropdown within a text field on desktop.

<ol><li>Date picker dialog on mobile
</li><li>Date picker text field dropdown on desktop</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5sha07-02.png?alt=media

<p>There are three variants of date pickers:</p><ol type="1" style="list-style-type:decimal"><li><p>Docked date picker</p></li><li><p>Modal date picker</p></li><li><p>Modal date input</p></li></ol>

A docked date picker component.

1. Docked date picker

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5si8zx-03.png?alt=media

A modal date picker component.

2. Modal date picker

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5sj3v5-04.png?alt=media

A modal date input component.

3. Modal date input

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fme1yy2eb-05.png?alt=media

<h2>Anatomy</h2>

<h3><span style="white-space:pre-wrap">Docked date picker</span></h3>

7 elements of a docked date picker.

<ol><li>Text field</li><li>Menu button</li><li>Icon button</li><li>Label text</li><li>Menu</li><li>Text buttons</li><li>Container</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5skthv-06.png?alt=media

3 elements of a docked date picker.

<p>1. Text field <br />2. Menu button <br />3. Menu </p><p><br /></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5slanf-07.png?alt=media

<h3><span style="white-space:pre-wrap">Modal date picker</span></h3>

12 elements of a modal date picker.

<ol><li id="isPasted">Headline </li><li id="isPasted">Supporting text</li><li id="isPasted">Container</li><li id="isPasted">Icon button</li><li id="isPasted">Previous/next month buttons</li><li id="isPasted">Day of week labels</li><li id="isPasted">Today’s date </li><li id="isPasted">Unselected date </li><li id="isPasted">Text buttons</li><li id="isPasted">Selected date </li><li id="isPasted">Menu button</li><li id="isPasted">Divider</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5sma00-08.png?alt=media

9 elements of a modal date picker.

<ol><li id="isPasted">Headline</li><li id="isPasted">Supporting text</li><li id="isPasted">Container</li><li id="isPasted">Icon button</li><li id="isPasted">Unselected year </li><li id="isPasted">Selected year </li><li id="isPasted">Text buttons</li><li id="isPasted">Divider</li><li id="isPasted">Menu button</li></ol>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5smpl6-09.png?alt=media

<h3><span style="white-space:pre-wrap">Modal date input</span></h3>

7 elements of a modal date input.

<p>1. Headline <br />2. Supporting text<br />3. Container<br />4. Icon button<br />5. Date input<br />6. Text buttons<br />7. Divider</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5sng56-10.png?alt=media

<h3><span style="white-space:pre-wrap">Full-screen date picker</span></h3>

14 elements of a full-screen date picker.

<p>1. Headline<br />2. Supporting text<br />3. Icon button<br />4. Container<br />5. Text button<br />6. Icon button<br />7. Divider<br />8. Day of week labels<br />9. Today’s date <br />10. Selected date range <br />11. Unselected date <br />12. Text buttons<br />13. Selected date range start date <br />14. Month label</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5srxxg-11.png?alt=media

<h2>Docked date picker</h2>

<h3 id="isPasted"><span style="white-space:pre-wrap">Usage</span></h3><p>Docked date pickers allow the <app-froala-tooltip-element description="Selection lets users choose specific items to act on." link-label="More on selection" link-url="/google-material-3/pages/selection" should-open-link-in-new-tab="true">selection</app-froala-tooltip-element> of a specific date and year. The docked date picker displays a date <app-froala-tooltip-element description="Inputs are devices that provide interactive control of an app. Common inputs are a mouse, keyboard, and touchpad." link-label link-url should-open-link-in-new-tab="false">input</app-froala-tooltip-element> field by default, and a dropdown calendar appears when the user taps on the input field. Either form of date entry can be interacted with.<br /><br />Docked date pickers are ideal for navigating dates in both the near future or past and the distant future or past, as they provide multiple ways to select dates.</p>

Docked date picker on a desktop screen.

<p>Docked date picker on desktop</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhhvs4s-12.png?alt=media

<h3><span style="white-space:pre-wrap">Behavior</span></h3><p><span style="white-space:pre-wrap">Dates can be added by using a keyboard or by navigating the calendar UI; both options are immediately available when the docked date picker is accessed.</span></p>

Docked date picker with a text field and the UI picker showing the selected date. 

Docked date picker

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5swv36-13.png?alt=media

Animation of a docked date picker adjusting its size to the selected month.

<p>Docked date pickers adjust size dynamically</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhi1ze1-GM3-Components-DatePickers-Guidelines-1-v01.mp4?alt=media

Animation of a docked date picker changing from calendar view to year selection menu view.

<p>The year selection menu replaces the calendar view</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhi7618-GM3-Components-DatePickers-Guidelines-1-2-v01.mp4?alt=media

<h3>Month selection</h3><p>Month <app-froala-tooltip-element description="Selection lets users choose specific items to act on." link-label="More on selection" link-url="/m3/pages/selection" should-open-link-in-new-tab="true">selection</app-froala-tooltip-element> can be navigated with the corresponding back and next arrows or by tapping the dropdown menu.</p>

Docked date picker with a list of months May through September. August is selected.

<p>Docked date picker month selection</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5sxs60-16.png?alt=media

<h3 id="isPasted">Year selection</h3><p><span style="white-space:pre-wrap">Year selection can be navigated with the corresponding back and next arrows or by tapping the dropdown menu.</span></p>

Docked date picker with a list of years 2025 to 2029. 2025 is selected.

Docked date picker year selection

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5t0t93-17.png?alt=media

<h2 id="isPasted">Modal date picker</h2>

<h3 id="isPasted">Behavior</h3><p><span style="white-space:pre-wrap">Modal date pickers navigate across dates in several ways:</span></p><ul><li><span style="white-space:pre-wrap">To navigate across months, swipe horizontally</span></li><li><span style="white-space:pre-wrap">To navigate across years, scroll vertically</span></li><li><span style="white-space:pre-wrap">To access the year picker, tap the year</span></li></ul><p><span style="white-space:pre-wrap">Don’t use a modal date picker to prompt for dates in the distant past or future, such as a date of birth. In these cases, use a modal input picker or a docked date picker instead.</span></p>

Animation of a docked date picker being swiped horizontally to navigate across months. 

<p>To navigate across months, swipe horizontally</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhkhvz2-GM3-Components-DatePickers-Guidelines-2-v01.mp4?alt=media

Animation of a year picker in a docked date picker being tapped and scrolled vertically to navigate across years.

<p>To navigate across years, tap the year picker and scroll vertically </p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhkizck-GM3-Components-DatePickers-Guidelines-2-1-v01.mp4?alt=media

<h3><span style="white-space:pre-wrap">Date range selection</span></h3><p id="isPasted"><span style="white-space:pre-wrap">Date range selection provides a start and end date. </span><span style="white-space:pre-wrap">Common use cases include:</span></p><ul><li><span style="white-space:pre-wrap">Booking a flight</span></li><li><span style="white-space:pre-wrap">Reserving a hotel</span></li></ul><p><span style="white-space:pre-wrap">Modal date pickers navigate across date ranges in several ways:</span></p><ul><li><span style="white-space:pre-wrap"><span style="white-space:pre-wrap">To select a range of dates, tap the start and end dates on the calendar</span></span></li><li><span style="white-space:pre-wrap">T<span style="white-space:pre-wrap">o navigate across months, scroll vertically</span></span></li></ul>

Animation of a date range being selected on a modal date range picker.

<p>Modal date range picker</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhklm21-GM3-Components-DatePickers-Guidelines-3-1-v01.mp4?alt=media

Animation of a modal date range picker being scrolled vertically to navigate across months.

<p>Modal date range picker with vertical scroll</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhkmci9-GM3-Components-DatePickers-Guidelines-3-2-v01.mp4?alt=media

<h2><span style="white-space:pre-wrap">Modal date input</span></h2>

<h3 id="isPasted">Usage</h3><p><span style="white-space:pre-wrap">Modal date inputs allow the manual entry of dates using the numbers on a keyboard. People can input a date or a range of dates in a dialog.</span></p>

A modal date input component.

<p><span style="white-space:pre-wrap">Modal date with manual input</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5t2vbx-22.png?alt=media

A modal date input component showing a day in 1979, which would be difficult to choose using UI.

<p>For dates that don’t require a calendar view, the modal date input can be the default view</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5t44vn-23-do.png?alt=media

A modal date input with hint text for entering the date.

<p>Alternatively, a text field with appropriate hint text can prompt for dates, such as in a form</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5t675k-24-do.png?alt=media

<h3>Behavior</h3>

<p>You can swap between the <app-froala-tooltip-element description="Modal date pickers extend full-screen. They're often used for selecting a date range." link-label="More on modal date pickers" link-url="/m3/pages/date-pickers/overview" should-open-link-in-new-tab="true">modal date picker</app-froala-tooltip-element> and <app-froala-tooltip-element description="Modal date inputs allow the manual entry of dates using the numbers on a keyboard. They're often used in compact layouts." link-label="More on modal date inputs" link-url="/m3/pages/date-pickers/overview" should-open-link-in-new-tab="true">modal date input</app-froala-tooltip-element> using the edit or calendar icon.</p>

Animation of a modal date picker switching to a modal date input when the range selection icon is tapped.

<p>Switching from a modal date picker to a mobile date input for selecting ranges</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhkrz7i-GM3-Components-DatePickers-Guidelines-4-1-v01.mp4?alt=media

Animation of a modal date picker switching to a modal date input when the edit icon is tapped.

<p>Switching from a modal date picker to a modal date input for selecting a single date</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhksla9-GM3-Components-DatePickers-Guidelines-4-2-v01.mp4?alt=media

<h3>Compact breakpoint</h3><p>On compact <a href="/m3/pages/breakpoints/overview" target="_self">breakpoints</a>, such as mobile, a full-screen <app-froala-tooltip-element description="Modal date pickers extend full-screen. They're often used for selecting a date range." link-label="More on modal date picker" link-url="/m3/pages/date-pickers/overview" should-open-link-in-new-tab="true">modal date picker</app-froala-tooltip-element> is recommended to increase readability and touch target size. It can cover the entire screen.</p>

A full-screen view of modal date picker on a mobile device.

<p>A full-screen modal date picker on mobile</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5t84q0-27.png?alt=media

<h3>Medium and expanded breakpoints</h3><p>The docked date picker works best for medium and expanded breakpoints. It displays a date input field by default, and a dropdown calendar appears when a person taps on the input field. A person can interact with either form of date entry.<br /><br />Docked date pickers are ideal for navigating dates in both the near future or past, and in the distant future or past, as they provide multiple ways to select dates.</p>

A docked date picker displaying a full calendar view on a large screen device.

<p>A docked date picker with a full calendar view is best used on larger devices</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5t9e1o-28.png?alt=media

<h3 id="isPasted"><span style="white-space:pre-wrap">Selection</span></h3><p><span style="white-space:pre-wrap">Selection is indicated through color, drawing visual attention. In date ranges, start and end dates are selected, while dates in-between appear connected with a subtle highlight.</span></p>

Animation of a modal date range picker showing visual differences between selecting a date range and today's date. 

<p>Differences between selected the selected date range (August 17–23) and today's date (August 5) are shown through color and fill</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhkykpc-GM3-Components-DatePickers-Guidelines-5-v01.mp4?alt=media

<h3>Appearing and disappearing</h3><p>Like other kinds of dialogs, modal date pickers use an enter and exit transition pattern to appear on the screen.<br /><br />To exit a date picker, the input can either be confirmed (<strong>OK</strong>) or dismissed (<strong>Cancel</strong>). Interacting outside of the dialog will also dismiss the <app-froala-tooltip-element description="Time pickers help users select and set a specific time." link-label link-url="/google-material-3/pages/time-pickers/overview" should-open-link-in-new-tab="true">time picker</app-froala-tooltip-element>. Unless one of these actions is taken, a time picker will continue to retain focus. Mobile full-screen pickers also have an additional close affordance (x) icon button and <strong>Save</strong> confirmation.<br /><br />Docked date pickers appear just below the input field.</p>

Animation of a modal date picker's enter and exit transition.

<p>Modal date pickers can be dismissed through interacting with content outside the dialog, or with the action buttons in the lower right</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhl1ir9-GM3-Components-DatePickers-Guidelines-6-1-v01.mp4?alt=media

Animation of a docked date picker's calendar icon being clicked making the calendar view appear for date selection.

<p>Interacting with the input for a docked date picker makes the calendar view appear below</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhl2xgp-GM3-Components-DatePickers-Guidelines-6-2-v01.mp4?alt=media

<h3>Responsive layout</h3><p>The sizing of the docked and modal date picker components don’t scale responsively to different breakpoints.</p>

Docked date picker enlarged on a large screen responsively.

<p><span style="white-space:pre-wrap">Don’t scale the date picker responsively to a larger size</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5tb2d5-32.png?alt=media

## Accessibility

<h2 id="isPasted"><span style="white-space:pre-wrap">Use cases</span></h2>

<p>People should be able to:</p><ul><li>Enter dates manually by inputting text, without using the picker</li><li>Use multiple input methods, making it accessible to those using assistive technology</li></ul><p>On the <app-froala-tooltip-element description="Docked date pickers open from an onscreen input similar to a text field. They're often used within forms." link-label="More on docked date picker" link-url="/m3/pages/date-pickers/guidelines#523a5a5a-6e35-4fdf-86e5-18d1a23887c4" should-open-link-in-new-tab="true">docked date picker</app-froala-tooltip-element>, the text field can be used for input.<br />On the <app-froala-tooltip-element description="Modal date pickers extend full-screen. They're often used for selecting a date range." link-label="More on modal date picker" link-url="/m3/pages/date-pickers/guidelines#c5c0471f-aa8a-4205-ab4b-1ab8cb893c5c" should-open-link-in-new-tab="true">modal date picker</app-froala-tooltip-element>, the date input option should be available using the edit icon.</p>

<h2><span style="white-space:pre-wrap">Interaction &amp; style</span></h2>

<p>The edit icon indicates the ability to switch to the <app-froala-tooltip-element description="Modal date inputs allow the manual entry of dates using the numbers on a keyboard. They're often used in compact layouts." link-label="More on modal date inputs" link-url="/m3/pages/date-pickers/guidelines#c5c0471f-aa8a-4205-ab4b-1ab8cb893c5c" should-open-link-in-new-tab="true">modal date input</app-froala-tooltip-element>.<br /><br />Interactive targets for all elements meet Material's 48x48dp minimum touch target requirement. Increasing density would negatively impact <app-froala-tooltip-element description="Accessible design makes products usable for people with all kinds of abilities." link-label="More on accessibility" link-url="/m3/pages/overview/principles" should-open-link-in-new-tab="true">accessibility</app-froala-tooltip-element> by limiting tappable/clickable targets.</p>

Date picker with the edit icon focused.

<p><span style="white-space:pre-wrap">The edit icon indicates the ability to switch to the modal date input</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5tcq2g-01.png?alt=media

Touch target used to select September 17 to 23 on a date picker.

<p><span style="white-space:pre-wrap">Touch targets are 48x48dp</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5tdrn3-02.png?alt=media

<h2><span style="white-space:pre-wrap">Date entry methods</span></h2>

<p><span style="white-space:pre-wrap">The date entry component offers two ways to enter a date:</span></p><ul><li><span style="white-space:pre-wrap">Direct text entry into a text field</span></li><li><span style="white-space:pre-wrap">Through the date picker</span></li></ul><p><span style="white-space:pre-wrap">The calendar icon is the exclusive entry point for the date picker.<br /><br />This improves efficiency for a screen reader and other keyboard users, as it makes interaction with the date picker optional and reduces the amount of key presses required to input a date.<br /><br />Each input is a separate tab stop, which improves discoverability of the control.</span></p>

Text input field next to a date picker icon provides a choice of how to enter the date.

<p><span style="white-space:pre-wrap">Entering a date either through direct text entry or the date picker</span></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flwhl9jct-3.png?alt=media

<h2><span style="white-space:pre-wrap">Accessible date input</span></h2>

<p id="isPasted">Automatically format the date after the user hits “Enter“ or navigates out of the text field. Don't automatically format the date by adding slashes or other special characters while the user is typing (also known as input masks). This can cause confusion for people using screen readers because it changes what they typed.  </p><p>To reduce errors, accept a range of formats including dashes, spaces, slashes, dots, and 0 to the left of a single digit month/day. This is especially helpful for assistive technology users who might be more prone to errors when interacting with complex inputs.</p>

Numeric entry 08172323 automatically formatted to 08/17/2023.

<p>The text field's logic can adapt to the user's actual input format, applying the correct formatting after the user has completed their text entry</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5tjcxl-04.png?alt=media

<h2><span style="white-space:pre-wrap">Optional <strong>Clear</strong> button</span></h2>

<p><span style="white-space:pre-wrap">If it's not needed for your use case, remove the <strong>Clear</strong> button from the screen to reduce the number of tab stops for keyboard users.</span></p>

Optional clear button on lower left corner of a date picker.

<p>Remove non-critical actions to reduce the number of tab stops for keyboard users</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5tl1kf-05.png?alt=media

<h2><span style="white-space:pre-wrap">Affordance for keyboard shortcuts</span></h2>

<p>Ensure keyboard shortcuts are readily available for keyboard and screen reader users by providing the shortcut key in the <app-froala-tooltip-element description="Tooltips display brief labels or messages." link-label="More on tooltips" link-url="/m3/pages/tooltips/overview" should-open-link-in-new-tab="true">tooltip</app-froala-tooltip-element>. It should be included in the hint description to be read out by the screen reader.<br /><br />As shown here, the previous year button is interactive and can therefore be focused via the keyboard. Upon <app-froala-tooltip-element description="A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice." link-label="More on focused state" link-url="/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f" should-open-link-in-new-tab="true">focus</app-froala-tooltip-element>, the tooltip explains the behavior of the button and shows the shortcut key.</p>

Shift + Page up is the keyboard shortcut to go to the previous year on a date picker.

<p>Keyboard tooltip example for date picker</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5tmhkf-06.png?alt=media

<h2><span style="white-space:pre-wrap">Truncated labels &amp; tooltips</span></h2>

<p>Truncating labels isn't ideal, but tooltips allow the full text to be shown on <app-froala-tooltip-element description="A hover state communicates when a user has placed a cursor above an interactive element." link-label="More on hover state" link-url="/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844" should-open-link-in-new-tab="true">hover</app-froala-tooltip-element> or keyboard focus.<br /><br />Days of the week are not interactive and are therefore not focusable via keyboard, yet the tooltip is available on hover. The date picker relies on the conventionality of these abbreviations for some assistive technology users.</p>

A pointer hover over the “T” day on a date picker produces the tooltip “Tuesday.”

<p>Days of the week are not navigable via keyboard, so the tooltip is shown only on pointer hover</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5tnt2t-07.png?alt=media

<h2><span style="white-space:pre-wrap">Color contrast between dates</span></h2>

<p><span style="white-space:pre-wrap">Dates should have contrast of at least 4.5:1 between the link text colors and the background.<br /><br /></span></p>

A date picker’s label text passes the color contrast minimum of 4.5:1.

<p>Dates pass the 4.5:1 contrast minimum</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5tp1fs-08.png?alt=media

<h2><span style="white-space:pre-wrap">Keyboard navigation</span></h2>

<div class="table-wrapper"><table style="width:100%"><thead><tr><th style="width:24.6016%"><div style="text-align:center"><strong>Keys</strong></div></th><th style="width:75.2984%"><div style="text-align:center"><strong>Actions</strong></div></th></tr></thead><tbody><tr><td><span style="white-space:pre-wrap">Enter/return</span></td><td><span style="white-space:pre-wrap">Enter/return</span></td></tr><tr><td><span style="white-space:pre-wrap">Enter/return</span></td><td><span style="white-space:pre-wrap">Closes the calendar and saves the selected date</span></td></tr><tr><td><span style="white-space:pre-wrap">Page up/down</span></td><td><span style="white-space:pre-wrap">Move to the same date on next/previous month</span></td></tr><tr><td><span style="white-space:pre-wrap">Home/End    </span></td><td><span style="white-space:pre-wrap">Move to the first day of the month</span></td></tr><tr><td><span style="white-space:pre-wrap">Shift + Page up/down</span></td><td><span style="white-space:pre-wrap">Moves to the same date in the next/previous year</span></td></tr><tr><td><span style="white-space:pre-wrap">Shift + M</span></td><td><span style="white-space:pre-wrap">Moves to the month list dropdown</span></td></tr><tr><td><span style="white-space:pre-wrap">Shift + Y</span></td><td><span style="white-space:pre-wrap">Moves to the year list dropdown</span></td></tr></tbody></table></div>

<h2>Labeling elements</h2>

<p><span style="white-space:pre-wrap">The text field's accessibility label should clearly state the purpose of the input (for example, event date or reservation date) and should match the placeholder text when the field is empty.<br /><br />The helper text (below the text field) should specify the date format (for example, MM/DD/YYYY or YYYY/MM/DD) and act as a description for the text field. The default helper text is "MM/DD/YYYY," but this can be customized.  </span></p>

Text field accessibility labels.

<p>The accessibility label clearly states the kind of input as an event date</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5tqs6i-09.png?alt=media

<div class="table-wrapper"><table style="width:100%"><thead><tr><th><div style="text-align:center"><strong>Element</strong></div></th><th><div style="text-align:center"><strong>A11y label</strong></div></th><th><div style="text-align:center"><strong>Role</strong></div></th></tr></thead><tbody><tr><td><span style="white-space:pre-wrap">Previous / next month and year</span></td><td><span style="white-space:pre-wrap">“{label}”</span></td><td><span style="white-space:pre-wrap">Button</span></td></tr><tr><td><span style="white-space:pre-wrap">Month and year dropdowns</span></td><td><span style="white-space:pre-wrap">“{label}”</span></td><td><span style="white-space:pre-wrap">Button</span></td></tr><tr><td><span style="white-space:pre-wrap">Days of the week</span></td><td><span style="white-space:pre-wrap">Column header</span></td><td></td></tr><tr><td><span style="white-space:pre-wrap">Month grid</span></td><td>Grid</td><td></td></tr></tbody></table></div>

<h2><span style="white-space:pre-wrap">Screen reader verbalizations</span></h2>

<p><span style="white-space:pre-wrap">To support screen reader users, labels are used to enumerate the complete date. This allows screen reader users to hear the full context of "Monday, August 17” instead of just part of the date.</span></p>

Current date label providing day, month, and year for screen reader accessibility.

<p>Screen readers will state the full day, month, date, and year instead of just the number 17</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Fmd5tw17z-10.png?alt=media
