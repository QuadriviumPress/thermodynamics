# Port QA tooling

Checks and repairs for the PDF → MyST port, independent of `scripts/` (the
conversion pipeline). Everything re-reads `thermodynamics-free-textbook.pdf`
directly, so the PDF is the authority.

| Script | Purpose |
| --- | --- |
| `pdf_columns.py N [M]` | Print a page's **body / margin / caption** text, separated by font size. This is the ground truth for repairs. |
| `check_port.py [check]` | Count the known defect classes; pass a check name to list every instance with `file:line`. |
| `coverage.py [ch]` | Fraction of the PDF's prose that survives in the Markdown; pass a chapter number to list missing sentences. |
| `fix_ligatures.py --write` | Undo `fi`/`fl` ligature transpositions ("frist" → "first"). |
| `fix_headings.py --write` | Promote `**1.1 Title**` to `## 1.1 Title`, restore full titles and executive summaries from the PDF. |
| `fix_alt.py --write` | Replace truncated figure `:alt:` text with the full caption. |
| `repair_interleave.py` | **Diagnostic only — do NOT run with `--write`.** It locates the damaged passages and shows which PDF page each belongs to; its automatic rewrite duplicates prose and hoists tables into asides. Repair by hand from `pdf_columns.py`. |

## Root cause found

`layout.py` sorted a line's characters by x-origin. PyMuPDF gives the second
character of an `fi`/`fl` ligature an x-origin ~0.001pt *past* the character
that follows it, so the sort transposed them book-wide. Fixed by rounding the
sort key to 0.1pt, which preserves reading order on ties.

## Conventions when repairing by hand

- Body prose: plain paragraphs. Margin notes: `:::{aside}` … `:::`.
- Figures: `:label: fig-N-M`, `:enumerator: N.M`, `:alt:` = the full caption.
- Display equations: `:::{math}` with `:label: eq-N-M`; the source's `(N/M)`
  number belongs in the label, never inside the maths body.
- Problems: ```{exercise}``` with `:label: prob-N-M`, answers in a `{dropdown}`.
- Bibliography references: `[[30](#ref-30)]`.
