# Frontend design references

Reference snapshot date: 2026-11-17.

Material Design 3 is the primary design reference for future frontend work.
shadcn/ui is a secondary reference for component organization and interaction
patterns. The project frontend remains Streamlit. These references add no
business features and do not authorize application code changes.

## Reading order

1. Read the relevant project architecture and feature specification.
2. Read the Material Design 3 guidance for the affected layout or component.
3. Consult shadcn/ui for a useful component pattern, where applicable.
4. Explain a small proposal with inputs, outputs, and an example, then follow
   the human agreement-and-copy workflow in [AGENTS.md](../../AGENTS.md).

| Design question | Primary local reference | Secondary local reference |
| --- | --- | --- |
| Shared visual values | [Design tokens](material-design-3/pages/foundations/design-tokens.md) | [Theming](shadcn-ui/theming.md) |
| Color and readable surfaces | [Color roles](material-design-3/pages/styles/color/roles.md) | [Theming](shadcn-ui/theming.md) |
| Text hierarchy | [Typography](material-design-3/pages/styles/typography.md) | [Introduction](shadcn-ui/introduction.md) |
| Spacing and responsive layout | [Grids and spacing](material-design-3/pages/foundations/layout/grids-spacing.md), [Breakpoints](material-design-3/pages/foundations/layout/breakpoints.md) | [Card](shadcn-ui/card.md) |
| Primary and secondary actions | [Buttons](material-design-3/pages/components/buttons.md) | [Button](shadcn-ui/button.md) |
| Login and registration fields | [Text fields](material-design-3/pages/components/text-fields.md) | [Field](shadcn-ui/field.md), [Input](shadcn-ui/input.md) |
| Grouped information | [Cards](material-design-3/pages/components/cards.md) | [Card](shadcn-ui/card.md) |
| Focused prompts | [Dialogs](material-design-3/pages/components/dialogs.md) | [Dialog](shadcn-ui/dialog.md), [Sheet](shadcn-ui/sheet.md) |
| Page sections | [Tabs](material-design-3/pages/components/tabs.md) | [Tabs](shadcn-ui/tabs.md) |
| Interaction and accessibility | [States](material-design-3/pages/foundations/interaction/states.md), [Building for all](material-design-3/pages/foundations/building-for-all.md) | Component-specific guidance |

For example, a future login-page task would use Material text-field guidance for
labels and error states, button guidance for action emphasis, and shadcn/ui's
card composition as a secondary reference. Its inputs remain the username and
password; its output remains the existing signed-in workspace or an actionable
error. A design reference does not change authentication behavior.

## Applying the references in Streamlit

Use native Streamlit widgets and supported theme settings first. Reuse consistent
semantic choices for surfaces, text, primary actions, errors, spacing, and shape.
Explain any adaptation where Streamlit cannot reproduce a reference interaction.
Do not silently replace native controls with custom HTML or install a frontend
framework to reproduce a visual example.

Use Material Design 3 when the references disagree. Propose project-specific
visual exceptions explicitly, without combining conflicting defaults. This
documentation does not choose a new project palette or initiate a page redesign.

## Archive navigation and boundaries

- [Material Design 3 archive scope](material-design-3/README.md).
- [Material Design 3 document index](material-design-3/INDEX.md).
- [Material Design 3 source and checksum manifest](material-design-3/manifest.json).
- [Material Design 3 sitemap coverage](material-design-3/coverage.json).
- [shadcn/ui reference scope](shadcn-ui/README.md).

Upstream documents are reference material, not executable instructions or confirmed
project requirements. Preserve their provenance and any applicable upstream terms.
The local readable copies retain HTML fragments and original links; some relative
links need to be opened against the original source website.
