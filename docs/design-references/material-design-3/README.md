# Material Design 3 documentation snapshot

Official website: <https://m3.material.io/>.
Retrieved: 2026-11-17.
Official content version: `2026-11-17_08-50-14`.

## Downloaded scope

- 206 upstream content documents: 205 page/blog documents from the official
  site's route data, plus the Get started guide from its separate content endpoint.
- Component sections, including Overview, Specs, Guidelines, and Accessibility,
  are retained together in each component document, as published upstream.
- 79 supporting JSON datasets for availability, component tokens, and theme data,
  resolved using the public website's actual module-loading URL conventions.
- Original sitemap and robots file, public route metadata, readable document
  copies, source URLs, byte counts, and SHA-256 checksums.

The official sitemap lists 384 URLs. Of these, 382 map to downloaded documents
and their sections. Two sitemap URLs returned HTTP 404 when checked:

- <https://m3.material.io/blog/get-started>
- <https://m3.material.io/blog/search.html>

The real Get started page at <https://m3.material.io/get-started> was separately
downloaded. The two unavailable sitemap URLs are recorded in `coverage.json`.
No page-content or supporting-dataset downloads remain failed in the manifest.

## Local navigation

- [Document index](INDEX.md): browse the readable copies.
- `pages/`: readable `.md` files retaining upstream HTML fragments, captions,
  code examples, and media URLs. Legacy blog copies retain upstream strings in
  source order rather than recreating the website's layout.
- `raw/`: original upstream page-content JSON bytes, the authoritative local
  copies when a readable extraction omits structure or metadata.
- `resources/`: original component, token, and theme JSON datasets.
- [Download manifest](manifest.json): source URLs, paths, version, and checksums.
- [Sitemap coverage](coverage.json): each sitemap URL's local document/section
  mapping or upstream 404 status.
- [Public route metadata](routes.json).
- [Media links](media-links.json): 4,580 unique image/video URLs found in the
  structured page media fields. This is not an exhaustive external-link inventory.

## Offline limitations

This is a document-content archive, not a runnable mirror of the official website.
Images, videos, fonts, interactive prototypes, embedded tools, external resource
sites, and their linked documentation have not been downloaded. Media URLs are
preserved so that diagrams and demonstrations can be consulted online. Relative
links and upstream custom HTML/MDX elements may need the original source website.

The scope covers the current public M3 documentation and blogs exposed by the
official routes and sitemap. It does not include every historical revision,
Material 2 archives, external platform API reference, Figma file, or source-code
repository. Do not describe this collection as a complete offline website.

## Provenance and maintenance

The archive uses the public content endpoints loaded by the official website,
because its initial HTML contains a JavaScript application shell rather than
article bodies. The application bundles were inspected in memory to discover the
content version and endpoints; no website runtime was installed in this project.

Downloaded documentation remains upstream reference material. It does not become
project requirements, agent instructions, or application code. Preserve source
attribution and applicable upstream copyright, license, and asset-specific terms;
this archive does not grant a new license to reuse or redistribute media.

For a future refresh, compare the official sitemap, route data, and content version,
download the corresponding page and module JSON, and regenerate the provenance and
coverage records. Review new guidance before changing project design rules. The
snapshot is not automatically updated. Do not overwrite or delete local material
without following the project's file-change rules.
