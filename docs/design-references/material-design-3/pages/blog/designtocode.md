# Design to Code: Turning Handoffs Into High-fives

Source: https://m3.material.io/blog/designtocode
Content endpoint: https://m3.material.io/page-data/Posts/5125582148599808.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/d641a152617b85842da26b6f0e4c18b28e133419ae5a7203879df73846332a26ffeacdfc506a64c4f1d4dcb5178c6772a6c192aee4b85a0be2191617e1d228b9

https://lh3.googleusercontent.com/VDfVYxWYmwj4dm8DTWMXW8Z_IWWFSvtT5t6BfNtlxLEYFnOsnMxPR1thxPIhdSBX8qhWbDSS_KgovtWnsCQJKoVwWjCmLR78LsLj7dwiBAmNHTORFo4

Damon Seeley

Senior Staff Designer, Material Design

mio-example

<p>Design systems like Material have profoundly changed the way teams build digital products. What was once a wild landscape of team-specific design practices is now a well understood set of guidelines and shared components. Material creates both a baseline for product excellence and an expressive vocabulary to realize exciting new experiences, while design tools like Figma help translate that vocabulary into compelling UI.</p>
<h2>The handoff problem</h2>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<p>Despite those improvements, design systems have yet to address one major friction point in product design: The messy handoff of UI between designers and developers. Even with great design systems our teams are still subject to lossy, ad-hoc practices for translating our ideas into working code. What typeface is this? Which component should I use? How does this thing stretch? We&rsquo;re still copying values from emails, chat and bug tickets, and it doesn&rsquo;t feel productive. Most of our time is spent improving process artifacts rather than the product itself.</p>
<h2>Design to code with Figma and Android Studio</h2>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>This year at Android Developer Summit <a href="https://www.youtube.com/watch?v=CMC8X1qVPEw" target="_blank" rel="noopener">our team shared a glimpse of how we&rsquo;re addressing this problem</a> with a new design to code workflow. The workflow is built with both designers and developers in mind, and introduces some new ideas for how to describe, exchange and iterate UI.</p>
<p>To achieve this, Material Design is teaming up with Figma, the leading UI design tool. Figma is all in on design to code workflows, and we&rsquo;re working together to ensure the right mental models and connections exist across the tools we use.</p>
<p>Our design to code workflow allows teams to create UI components in Figma and export them in a portable container we call a UI Package. These Packages can be directly used in Jetpack Compose projects for Android applications, can be edited in Figma, and can be directly updated in code with good developer ergonomics for component reuse and change management. Our current work is focused on high-fidelity translation of layout, appearance, dynamic data bindings and interaction design intent, with plans to extend the UI Package model in the future.</p>
<h2>Get a glimpse of the future</h2>
<div style="text-align: center; position: relative; padding-bottom: 56.25%; max-width: 100%; height: 0;"><iframe style="border-radius: 16px; position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://www.youtube.com/embed/CMC8X1qVPEw" frameborder="0" allowfullscreen=""></iframe></div>
<p>We hope you&rsquo;ll check out our lightning talk from Android Developer Summit to learn more. Over the next few months, we&rsquo;d like to work with a small group of teams to help shape this new workflow, so if you&rsquo;re interested in joining our early access program <a href="https://services.google.com/fb/forms/designtocode/" target="_blank" rel="noopener">please sign up using this form</a> and we&rsquo;ll be in touch!</p>

UI handoff remains one of the biggest pain points for teams building digital products

UI handoff remains one of the biggest pain points for teams building digital products

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/4de0c13d1ca1c585e2e7f3379b1e48bbb53d5416086869bd3ea5354cf44777727e60d56a9a897b1aa97271fa42df32d0177652caf70e0819d689868458553968

https://lh3.googleusercontent.com/i6AGtN52tZIPNjmWc8k-VU_EVfS7-0Nc7jZS4qnKT12SRpn1CprTmu7Ml3LX8xqpUt8z4Ehw_AwHa3e39YWubsIHJqj7U_M5pnc3rjgC3V801Qcg5NoE

Our design to code workflow preview allows teams to package UI components in Figma for Jetpack Compose Android projects

Our design to code workflow preview allows teams to package UI components in Figma for Jetpack Compose Android projects

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/2a73488647c2018b417939e2f4c9170ed79a1f32994fce81ac156e8f9db469488bf9b69aac03172db3bcc61a091740013c2cd3b16021eca60b28fb605aba197f

https://lh3.googleusercontent.com/Gli8S2kChMQ1mGgVDqs7fTlT6j9Rm1vZY5C7se6_ZjaKjIEldtnMdhNlZa_Rmrz0Sv2OOQv0hcvN1L5VTlqCGeSyPo0L84j7MxtNzo8fVpR-iDlaoIUN

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/05595770105fb1206a81032a9558593f38fe096e0ecf56d6803ca236ca18842b4126dcde80edbb5b0899859066d0144b7ea4c55a5bc375773ac752aa085b0ccf

https://lh3.googleusercontent.com/qpnv-ci_KsPIo_qayXp3E8Tv4xKUIYA-JAgJdiOdmjLD_UuGP7875Lg65YqmBysrvbMBmTP0rM7jknOXrWd2ZZ1BVN-sY-B2avEOdsV4xeqcPSewItI

 

{}

Teaming up with Figma to bring great UI from design to code

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/192c27dae8d74655a361896dee9ad2c1fdf8000590936c16e3384f99bde41c449477a577544e1e55f7c1965bf64d99ac2e4f832c38e351c62c5347ba63196d8d

https://lh3.googleusercontent.com/KsNEpFZNI-ffIcamwG8R8-sHyGimJ6sqBjZPnUpMvbu0OTEyhEpE7tlSYkct40tEUbZdVIRLDuqke_Q6Lj7TFBHjppmfaDhZrqBFeIea_D19-eN9OJQ

Design to Code: Turning Handoffs Into High-fives

2021-10-27T09:05:00

designtocode

Teaming up with Figma to bring great UI from design to code

Design to Code: Turning Handoffs Into High-fives

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/362302fcebd869d647a92554dbe8a7b1e06b1eeb8ce46a6e67bfc5403441aea79237facc6dfe929599f4fb4bc8e6e836d2efbccab8abed1fca121d67d244aac4

https://lh3.googleusercontent.com/rME0woOrBvWQqpvpmd_QteVRux9dw9pT7HhbEVneGV5yyo1WzljxXgwf4wynieJPHPs--tPySUe7uoMiJwuYj-oNzXC8PwwXE1wK7Dyv9_UDhyce5A

Start building with Material You

/blog/start-building-with-material-you

Start building with Material You

Material Blog

Start building with Material You

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/2a9f578ce95c17ec93b1fe68e0aaf09a31485c930856cc9bff4b9078729d5176ecfde464df9b48b7acee1142130575f7109d74630b886fbc58ce5b7292099699

https://lh3.googleusercontent.com/o60K_0LJTxbo1c-5SP-ZRrDTOU1lUyzujbsE63jDyFgN52AsTK0eEsdPsciQkjO8nJ6iTG9K8U5nZbJtgbYSpHGMsVBzBiWDAcoKK0u9AtdraOSCHWs

Migrating to Material Design 3

/blog/migrating-material-3

Migrating to Material Design 3

Material Blog

Migrating to Material Design 3

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/b14f83531e0ded0b48ab6c6e03d8645b76f3a34d7abe4a849ea689a09b0ab4dbd5b52ffda0e00d05c9cc3d0aafa490251c132c68911265a6b25b3b74cf67876a

https://lh3.googleusercontent.com/Aj_PgNvXar9dTxMmBoCjGE5OG1jhEZyjoXUI3mOJMdhY68LvL1LYuI5aL0r8e3lESTZWL6mqhRPY30qYd9VDIPx6lXdomuw4orxQ6T_mlAGJvggS6Bc

Introducing Material Theme Builder

/blog/material-theme-builder

Introducing Material Theme Builder

Material Blog

Introducing Material Theme Builder

mio-example
