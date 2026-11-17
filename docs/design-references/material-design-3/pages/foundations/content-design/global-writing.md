# Global writing

Source: https://m3.material.io/foundations/content-design/global-writing
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/33c706d8-c9b9-4190-a403-d028a56da5cb.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Global writing is easier to read, understand, and translate. This guidance is for all American English that is localized.

## Overview

<h2>Overview</h2>

<h3>Global writing</h3><p id="isPasted">Global writing is the practice of writing inclusively for many cultures and optimizing for localization. This makes writing easier to read, understand, and translate. Writing for localization is necessary when a product will be translated, but can also be a helpful lens when writing for anyone.</p>

3 apps in different languages.

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuo0vnn-1.png?alt=media

## Word choice

<h2>Word choice</h2>

<h3>Use global examples &amp; explain local references</h3><p>References to local places, holidays, and companies won’t always make sense to global audiences.</p>

Empty wishlist screen that references the holidays

<p>Use generalized, global examples. Most countries and cultures have holidays.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuo362u-1_do.png?alt=media

Empty wishlist screen that references Christmas

<p>Don’t call out a specific country or culture’s holiday</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuo41ao-2_don't.png?alt=media

<p>If it doesn’t make sense to use a global example, explain the reference in the message description so the translator can substitute a locale-specific example. Some instances where local references should be called out include:</p><ul><li>Locations</li><li>Names (common first names and nicknames)</li><li>Currencies</li><li>Temperatures</li><li>Date formats</li><li>Providers (internet and cable)</li></ul>

Empty state that references New York with message description about replacing New York with a well-known city in other languages

<p>Help translators understand the context by adding message descriptions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuo4v88-3.png?alt=media

<h3>Use short, simple sentences</h3><p id="isPasted">Break text into shorter sentences. Use bullets or separate content into sections with headings. </p><p>Other languages average at 1.5 times longer than English, so text that’s short may be long when translated.</p>

2 screens side by side, in English and German

<p>Many languages, like German, are longer than English</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuo5uis-4.png?alt=media

<h3>Avoid abbreviations</h3><p id="isPasted">Abbreviations don’t translate well and can be confusing out of context. Spell things out whenever possible.</p><p>However, common abbreviations for time are acceptable.</p>

Dialog with options that aren’t abbreviated

<p>Use clear names to refer to things</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuo6t6b-5_do.png?alt=media

Dialog with options that are abbreviated

<p>Avoid abbreviations. If they're used, provide their meaning in message descriptions.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuo82rh-6.png?alt=media

<h3>Clarify pronouns</h3><p id="isPasted">Using pronouns, like “it,” can get tricky when translators are working with small, unconnected strings of text and when nouns have genders in many languages. Repeat the noun, or clarify the noun in a message description.</p>

Photo app with snackbar that reads “Couldn’t move photo”

<p>Using nouns instead of, or in addition to, pronouns can help clarify future and past user actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuo92qu-7_do.png?alt=media

Photo app with snackbar that reads “Couldn’t move it to ‘Travel’ folder because it’s unavailable”

<p>Avoid using pronouns when it’s unclear what nouns they’re referring to, especially when explaining user actions</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuoacju-8_don't.png?alt=media

<h3>Clarify “this” and “that”</h3><p id="isPasted">Don’t start a sentence with "this" or "that" unless it's immediately followed by the noun. When the noun is unclear, the sentence is more difficult to translate. </p>

Form with clear writing that doesn’t use “this” or “that”

<p>Make sure it’s clear who text is referring to</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuobsfb-9_do.png?alt=media

Form with a subhead that reads “This can be seen by your IT administrator.” It’s not clear what “this” refers to.

<p>Avoid using “this” and “that”</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuocbnw-10_don't.png?alt=media

<h3>Avoid idiomatic, colloquial, and polite expressions</h3><p id="isPasted">Idiomatic or colloquial phrases can be confusing if the meaning isn’t clear. If you use them, clarify the purpose and context of the phrase to help the translator choose an appropriate alternative.</p><p>Avoid polite expressions, such as “Please,” “Sorry,” and “Thank you,” especially in error messages. However, "please" may be used when asking the user to do something inconvenient.</p>

Empty state with illustration that reads “Let’s go”

<p>Clear, everyday language can be used in an expressive and whimsical way when paired with imagery</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm48wnsm6-11_do.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/fbOdPNZxbnWg8h1AtfrVzrHEfx87HqTbn1uV7XqiOCvs017tfdkalXYclDMLKuAlW2fhnxehv4sRAOflGxm7TFe7ckUfdhE57Pkwu57MUkZP=s656

Empty state with illustration that reads “Let’s get this party started”

<p>Idiomatic phrases can be difficult for everyone to understand and for translators to localize</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fm48wp6t5-12_don't.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/hIGnwFcZ-4N3wxDr7EvS9-3j_B_l5DbU24maq8wmMOyakUI4sgTD9O-Ab5Ck8oxjJx0samUsMnB-Vlg40cWx6Yx3S9SHTgoqj9uGcQk-yDPv=s656

<h3>Reduce technical jargon</h3><p id="isPasted">Technical terms don't always translate. Descriptions should be simple, and in some cases literal, to avoid confusion when translating.</p>

Dialog that prompts people to sign up to try new products

<p>Plain language is easier for everyone to understand</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuoeiu1-13_do.png?alt=media

Wordy and confusing dialog that prompts people to sign up for new communication preferences

<p>Confusing language makes it difficult for people to understand the actions they’re taking</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuoexnd-14_don't.png?alt=media

<h3>Clarify ambiguities</h3><p id="isPasted">Some words have multiple meanings. For example, “traffic,” “filter,” and “change” can be used as either nouns or verbs. Avoid using both meanings of the word in the same string or body of text. If a word has the potential to be confusing, provide as much context as possible in the message description so the translation will be accurate.</p>

Screen displaying devices and speakers at home, next to bottom app bar with “home” button

<p>Clarify words that have multiple meanings. “Home” could reference a homepage or where someone lives.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fgoogle-material-3%2Fimages%2Flvuoff5i-15.png?alt=media
