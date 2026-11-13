# Formal certificate input

For the V2 stage, supply `BP-S001_Certificate_V2.pdf` and
`BP-S001_Certificate_V2_MODIFIED.pdf` here. Neither was found during implementation.
Inspect the same series CERT-LAB001-BP-S001, BP-S001 subject and laboratory name
before use. Upload only the original as formal V2; MODIFIED is external verification
input only. Generated TEST ONLY V2 originals/derived modifications are kept in
ignored `.local/`, under a separate test series so formal V2 stays unoccupied.

Place the supplied original here as `BP-S001_Certificate_V1.pdf`. It was absent during
implementation; no replacement formal certificate was invented.

Before formal acceptance, inspect its actual certificate ID, laboratory name and snake
identifier. Reconcile the lab name with the explicitly configured LAB001 mapping rather
than silently mislabelling a laboratory. Create BP-S001's database profile and register
it on the current SnakeRegistry first. Upload unchanged original bytes using the actual
certificate ID. Derive modified test content from this exact V1 and keep the original;
do not use a pre-existing V2_MODIFIED document for comparison.

Generated TEST ONLY PDFs live under ignored `.local/`; see
`../../level-3/certificate-v1-development.md` for the retained test example.
