---
title: "A8. Errata & Change Log"
short_title: "Appendix A8"
label: app-a8-errata-change-log
---

# A8. Errata & Change Log

Appendix A8 321

## A8 Errata & Change Log

This document was generated on June 7, 2026. Since its initial release in June 2025, the following changes have been carried out, in addition to minor text and formatting fixes:

• The downloadable pdf file size has been reduced by re-working a handful of embedded photo files;

• Appendix A6 on Notation (p. 319) has been re-worked for clarity;

• Appendix A7: *Mental Health for the Engineering Student* has been added, page 320.

• The text in §1.3 is clarified. Thanks to Patrice Krakow.

The most recent version of this book, its full change log, and a contact form to report any remaining errors to the author can all be found on the book's website, https://thermodynamicsbook.com/. The author can also be reached by email at olivier@cleynen.fr.

## Web Rendering Differences

The web version of this textbook (built with MyST Markdown) differs from the original PDF in several ways due to the automated conversion process from PDF to structured markdown. Readers comparing the two versions should be aware of the following known differences:

### Body Text in Math Blocks

During the PDF-to-markdown conversion, some body text and explanatory passages incorrectly ended up enclosed in math blocks (`:::{math}` directives). These passages are semantically body text or problem descriptions, not mathematical equations. Examples include:

• Explanatory text preceding an equation (e.g., "We will denote power by placing a dot above the symbol...")
• Problem statement introductions (e.g., "What is the energy supplied to the spring...")
• Unit descriptions and labels (e.g., "joules per kilogram (J kg^{-1})")
• References and cross-references within equations

**Impact**: The affected text may render with different styling (monospace font or code-like appearance) in the web version compared to normal prose in the PDF. The content is still readable and intelligible, but the visual presentation differs.

**Frequency**: This occurs in approximately 10–15 instances across the ten chapters, most notably in chapters 1–5 where the conversion process was more challenging.

### Problem and Answer Pairing

In the PDF, exercises and their answers appear on facing pages or in close proximity due to the two-column layout. In the web version, each problem (marked with `{exercise}` directives) includes its answer in a collapsible dropdown section, which changes how readers discover and engage with solutions compared to paging through the PDF.

**Impact**: Readers expecting to find answers adjacent to problems on the same screen may need to click to expand the answer dropdown. This is intentional and improves interactivity on smaller screens, though it differs from the PDF's side-by-side presentation.

### Merged Heading and Body Text

A small number of page breaks in the original PDF caused section headings to merge with the opening lines of body text. During conversion, these were parsed as single text blocks and required manual cleanup. A few instances may remain where:

• A heading appears to have extra body text attached to it
• An opening sentence of a paragraph appears separated from the rest of the text

**Frequency**: Fewer than five instances, primarily in appendices and front matter.

### Minor Layout Differences

• Footnote positioning and styling may differ from the PDF
• Indentation and spacing around figures and code blocks may vary
• Table rendering is optimized for web display and may wrap differently than in the PDF's two-column format

### Conversion Defects: Found and Fixed (2026-08-23)

The issues described below were identified by a comprehensive audit of the PDF-to-Markdown conversion, and have now been **corrected by hand against the original source PDF**, equation by equation. They are kept here as a record of what was wrong and how it was resolved, not as an outstanding list.

**Broken equations and derivations.** In chapters 1–5, 7, 8, 9, and 10, a number of equations were fragmented across multiple `:::{math}` blocks during conversion, sometimes with numerators, denominators, or integral bounds left empty or stranded in their own block (e.g. `\frac{}{T}`, an orphaned `A` or `B` next to an integral, a bare digit in its own block). These have been reconstructed as single, correctly-formed equations checked against the PDF, including:
- Chapter 1: the specific-energy relation $e \equiv E/m$ (1/3), and the exercise 1.8/1.9 problem statements and answers, which had been interleaved with each other by the column-based extraction.
- Chapter 2: the spring/pressure-volume work derivation (2/14), the heat-quantification section heading and equations 2/16–2/17 (which had been scrambled into a garbled heading "## System for a closed system."), a duplicated and broken copy of exercise 2.5's answer, and an unclosed `prf:example` fence that had silently swallowed the following worked example and several unrelated sections into one block.
- Chapter 3: the enthalpy equations (3/12–3/15, including a Stodola pull-quote that had absorbed two of the equation numbers), and the nozzle-exit-velocity worked example (ex-3-2).
- Chapter 4: the reversible-adiabatic derivation and relations 4/35–4/39, equations 4/8–4/9, and a worked example whose final velocity calculation was missing an exponent.
- Chapter 5: the constant-pressure and constant-volume process derivations (5/7–5/9, 5/11–5/14).
- Chapter 7: the refrigerator and heat-pump efficiency equations (6/7, 7/7, 6/9, 7/8), where the absolute-value bars `|...|` had been mis-extracted as literal `|||` characters.
- Chapter 8: the entropy definition and its ideal-gas consequences (8/1–8/13), a duplicated/garbled copy of that same derivation left over from conversion, and examples 8.2, 8.8, and 8.9, one of which had been split into two disconnected example blocks with a misplaced attribution line in between.
- Chapter 9: the efficiency prose in §9.2.1, where several sentences and equation 6/4 had been wrongly enclosed in `:::{math}` blocks (rendering as code instead of prose), and a stray, unmatched closing fence before the Problems section.
- Chapter 10: the compressor isentropic-efficiency relation (10/5–10/6), which had an empty `\frac{1}{}`.

**Misplaced diagram captions and figures.** A figure attribution line in chapter 2 (figure 2.5) was missing while an identical, unrelated line sat several paragraphs later; a figure caption in chapter 8 (figure 8.7) was truncated mid-sentence. Both have been restored to their correct locations, and a diagram belonging to chapter 2's example 2.5 (previously unreferenced in the book) has been placed correctly.

**Result**: all equations, worked examples, and problem/answer text identified as broken during the audit now match the original PDF.

### Missing End-of-Chapter Exercises: Found and Restored (2026-08-23)

Independently of the equation-level defects above, a structural check of every chapter's Problems section (comparing labeled exercises against the source PDF's numbering) turned up a real, separate class of content loss: **27 end-of-chapter exercises across 8 chapters were entirely absent from the web edition**, not merely mis-rendered — in most cases the problem statement, the worked answer, or both were missing outright, and in a few cases the statement survived as unlabeled, out-of-order floating text with no answer at all.

Restored, with problem statement and answer checked against the PDF:
- Chapter 1: exercise 1.5 (*Preparing a Bath*).
- Chapter 2: exercises 2.1 and 2.2 (*Simple Processes*, *Arbitrary Processes of a Gas in the Laboratory*).
- Chapter 3: exercise 3.7 (*Steam Turbine*).
- Chapter 4: exercises 4.1, 4.3, 4.6, 4.7, and 4.8, plus the chapter's Problems-section preamble (air properties and equations 4/36–4/38, 4/29), which was missing entirely.
- Chapter 5: exercises 5.3 and 5.4 (*Simple Recap Exercise*, *High-Pressure Steam Generation*).
- Chapter 6: exercises 6.1, 6.2, 6.3, 6.5, and 6.6, plus the missing Problems-section preamble.
- Chapter 7: exercises 7.1, 7.2, 7.4, and 7.6, plus the missing Problems-section preamble (including equations 7/6–7/8, which chapter 7's own worked examples already depended on).
- Chapter 8: exercises 8.3, 8.4, 8.5, 8.6, 8.8, 8.9, and 8.10, plus the missing Problems-section preamble, and the second half of exercise 8.7's statement, which had been left stranded as orphaned text after its own answer and figure.

Several exercises that were present but garbled have also been repaired in the same pass, including scrambled or duplicated answer text for exercises 2.5, 4.5, 6.4, 7.3, 7.5, and 7.7.

A `scripts/verify_book.py` structural check (comparing labeled exercise numbers per chapter against the PDF-derived `outline.json` counts) now passes for all ten chapters; it did not before this fix.

### Historical Asides: Correction of a Previous Errata Entry

A previous revision of this document (dated 2026-08-23, earlier the same day) claimed that 74 of 84 "A Bit of History" sidebar sections were missing their content, calling it "critical content loss." **That claim was incorrect and has been retracted.**

On inspection of the source PDF directly, the book contains exactly **ten** "A Bit of History" essays — one per chapter — and all ten were already present, in full, in the web edition (labeled `hist-1-4` through `hist-10-13`). What the previous audit mistook for "74 missing essays" were 73 empty `admonition` placeholder blocks scattered through the chapters, each containing only the heading and the boilerplate attribution line "*Engineering Thermodynamics* by Olivier Cleynen," with no title, author, or body text. These placeholders did not correspond to any content in the PDF at any point — they were spurious blocks produced by the conversion pipeline (most likely a false-positive match against the shaded-box fill color also used for an unrelated footer decoration that repeats on every page), not evidence of lost text.

These 73 spurious placeholders have now been removed from all ten chapters. Each chapter retains exactly the one genuine "A Bit of History" essay that exists in the source book.

### Technical Notes on the Conversion Pipeline

For future PDF re-conversions, the defects found in this audit point to a few recurring failure modes in `scripts/extract.py` / `scripts/mathtext.py`:
- Fractions and integral bounds spanning a layout boundary (e.g. a page or column break) were sometimes split into separate blocks instead of being re-joined.
- Absolute-value bars (`|...|`) were occasionally tripled (`|||...|||`) by the glyph-extraction step.
- The shaded-box color used to detect "A Bit of History" sidebars is also used by a decorative footer bar repeated on every page, which appears to have caused the pipeline to emit an empty history placeholder far more often than the source actually contains one.
- Two-column problem/answer pages occasionally had adjacent exercises' text interleaved during column reconstruction.

These are noted for anyone improving the pipeline; they do not affect the current, hand-corrected text.

### Chapters 1–2: Line-by-Line Audit Against the PDF (2026-08-23)

A full page-by-page comparison of chapters 1 and 2 against the source PDF (using `scripts/qa/pdf_columns.py`, which separates each page's body/margin/caption text by font size) was carried out, covering both correctness and a specific structural defect: pull-quotes from historical figures that belong in the margin column of the PDF, and should therefore be set apart from body prose as `:::{aside}` blocks in the Markdown, exactly as the book already does elsewhere.

**Nested aside block.** In chapter 1, §1.4.2 ("Heat"), a James Joule quote (1845) and a Rudolf Clausius quote (1850) — two separate margin items on PDF page 20 — had been merged during conversion into one nested `:::{aside}` block, with the Clausius quote's aside opening before the Joule quote's aside had closed. This rendered as one quote box containing a smaller box, instead of two sequential boxes. Split into two sibling `:::{aside}` blocks. Every other margin quote in chapters 1 and 2 (Feynman, Thomson, Clausius, Clapeyron, Pambour ×2) was checked against the PDF and found already correctly wrapped, with matching text.

**Missing exercise content.** Chapter 2, exercise 2.5 ("Cycle of a Gasoline Engine"), had its problem statement truncated mid-sentence, right after the description of the C→D expansion step; the D→A cooling step and all 8 numbered questions (present on PDF p.54) were missing entirely from the web edition. Restored from the PDF.

**Orphaned extraction artifacts.** Two single-character lines (`A`, `B` — leftover axis labels from margin figures) had been stranded in chapter 2's body prose, immediately before unrelated equations (§2.4.1, §2.4.2). A stray `.7**` fragment (debris from the `**2.7**` exercise-enumerator label) sat as its own line at the top of exercise 2.7's answer block. All removed.

A new document, `scripts/qa/admonition-audit-notes.md`, records the detection method (cross-referencing `pdf_columns.py`'s margin-column output against each chapter's `:::{aside}` blocks) and the specific defect classes found, so the same audit can be repeated for chapters 3–10.

### Chapters 3–4: Line-by-Line Audit Against the PDF (2026-08-23)

The same page-by-page audit (chapter 3 against PDF pp.59–80, chapter 4 against PDF pp.81–112, using `scripts/qa/pdf_columns.py`) was carried out for chapters 3 and 4.

**Margin pull-quotes.** All margin-column epigraphs in both chapters were checked against the PDF and found already correctly wrapped in standalone `:::{aside}` blocks, with matching text and no nested-aside merging: chapter 3 (Aurel Stodola ×2, §3.2.1 p.61 and §3.3.3 p.65) and chapter 4 (Sadi Carnot ×3, Émile Clapeyron, Richard Feynman, Louis Joseph Gay-Lussac, James Prescott Joule, Rudolf Diesel — §4.1.2 p.83 ×2, §4.1.4 p.85, §4.3.2 p.90, §4.3.3 p.91, §4.4.4 p.98, §4.4.5 p.99). No changes needed.

**Split exercise statements (problem text stranded after its own answer).** Two exercises in chapter 3 had their problem statement broken across the point where the PDF places a figure mid-problem: the conversion pipeline kept only the first half of the statement inside the `{exercise}` fence (immediately followed by the answer and the figure), while the second half of the statement — additional data and the final numbered sub-questions — was left as orphaned body prose *after* the figure and *after* the exercise had already closed, making it look like ordinary paragraph text rather than part of the question:
- Chapter 3, exercise 3.4 (*Turbine Engine Nozzle*, PDF p.76): the outlet-condition data (internal energy, temperature, specific volume) and both numbered questions, which follow figure 3.13 in the PDF, were stranded as body prose after the exercise's answer/closing fence. Merged back into the problem statement, ahead of the answer; the figure now again follows the complete exercise block, matching the pattern used by every other exercise in the chapter.
- Chapter 3, exercise 3.9 (*Compressor and Turbine of a Turboprop Engine*, PDF p.78): the entire second half of the problem — the turbine's inlet/outlet properties and questions 4–5 — sat as orphaned prose after figure 3.17, disconnected from the exercise that already contained their answers (items 4 and 5 were present in the answer key, but the questions themselves were not part of any `{exercise}` block). Merged back into the problem statement.

**Missing exercise continuation (chapter 4, exercise 4.9).** Exercise 4.9 (*Elementary Processes: Vocabulary*, PDF p.107) ends its problem statement with "...undergoes the following processes:"; the second half of the question ("Among the processes above, which ones are: 1. at constant temperature...? 2. at constant volume...?") had been left as a floating, unlabeled paragraph between exercise 4.9's answer and exercise 4.10, rather than inside exercise 4.9's own problem statement, ahead of its answer. Moved back into place.

**Stray enumerator-label fragments.** As in chapters 1–2, several answer blocks had a leftover fragment of the bold `**N.M**` exercise-number label sitting as its own line at the top of the answer, debris from the label being split across the extraction boundary: chapter 3 exercises 3.2 (`.2**`) and 3.8 (`.8**`); chapter 4 exercises 4.10 (`10**`), 4.11 (`11**`), and 4.12 (`12**`). All removed.

**Stray footer boilerplate inside an answer.** Chapter 3, exercise 3.9's answer ended with a stray `*Engineering Thermodynamics* by Olivier Cleynen` line and a doubled closing `$$` — both leftover page-footer/glyph artifacts of the kind already documented above (see "Historical Asides" and "Technical Notes" sections). Removed, and the unmatched `$$` corrected to a single closing `$`.

**Orphaned equation subscript (chapter 4, exercise 4.12 answer).** The answer to exercise 4.12 item 3 had lost the `B` subscript on $v^{-1.5}$ (rendering as bare `kv^{-1.5}`), with the subscript instead stranded as an orphaned single-letter line before the next value; the answer's introductory word had also been garbled to `Wth`. Restored to $kv_{\mathrm{B}}^{-1.5}$ and removed the stray line break.

**Swapped equation numerator/denominator.** Chapter 4, exercise 4.13 restates the reversible-adiabatic relation 4/36 as a starting point; its `v_1/v_2` had been swapped relative to the PDF and relative to the same equation's correct form given earlier in the chapter's Problems preamble (4/36: $(T_1/T_2)=(v_2/v_1)^{\gamma-1}$). Corrected to `v_2/v_1`.

No other content-loss, garbling, or orphaned-artifact defects were found in chapters 3–4; `scripts/verify_book.py`'s structural exercise-count check continues to pass for both chapters after these fixes.
