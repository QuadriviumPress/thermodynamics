# Engineering Thermodynamics (MyST edition)

Web-native [MyST Markdown](https://mystmd.org/) edition of Olivier Cleynen's
*Engineering Thermodynamics*, converted from the free PDF at
[thermodynamicsbook.com](https://thermodynamicsbook.com).

## Status

Phases 0–6 complete: full book generated from the PDF, verified, building with
MyST, and deployed to GitHub Pages.

- **Live site**: [quadriviumpress.com/thermodynamics](https://quadriviumpress.com/thermodynamics/)
- **Pipeline**: PDF → `build/document.json` → 24 Markdown files (10 chapters,
  11 appendices, front/back matter); 321 figure images and selectable steam tables.
- **Conventions**: `{prf:example}`, `{exercise}` with collapsible `{dropdown}`
  answers, history admonitions, `(N/M)` equation labels; index omitted.
- **QA**: `npm run verify` checks structure against `outline.json` and flags OCR
  suspects with hunspell; `npm run build` produces static HTML.
- **CI/CD**: `.github/workflows/ci.yml` on pull requests;
  `.github/workflows/deploy.yml` publishes to GitHub Pages on pushes to `main`.

Known remaining polish (non-blocking): some body text still lands in `:::{math}`
blocks from PDF layout; problem/answer pairing on two-column pages is partial;
merged heading/body lines on a few pages.

## Source and license

© Olivier Cleynen (2015–2025), ISBN 9781446710067.
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Build

```bash
npm install
npm run start          # preview at :3000
npm run build          # static site in _build/html/
```

## Convert from PDF

Download the source PDF from [thermodynamicsbook.com](https://thermodynamicsbook.com)
into the repo root as `thermodynamics-free-textbook.pdf`, then:

```bash
python3 scripts/pdf_to_images.py thermodynamics-free-textbook.pdf --out work/pages
sh scripts/build.sh    # extract → figures → steam tables → markdown
npm run verify
```

Requires `PyMuPDF`, `Pillow`, `mutool` (`mupdf-tools`), `hunspell`, and Node ≥ 20.

## Layout

| Path | Role |
| --- | --- |
| `outline.json` | Page ranges and expected content counts |
| `myst.yml` | Project metadata and TOC |
| `scripts/` | PDF → MyST pipeline |
| `work/` | Scratch extracts and page renders (git-ignored) |

Conventions: problem answers as collapsible `{dropdown}` under each
`{exercise}`; index omitted; equation numbers like `2/16`.
