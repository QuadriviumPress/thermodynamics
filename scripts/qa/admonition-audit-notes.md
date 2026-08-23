# Admonition audit notes

Notes from auditing chapters 1–2 for a specific defect class: pull-quotes by
named historical figures that should be visually separated from the body
prose they're not part of, but aren't. Written up here so the same pass can
be repeated mechanically on chapters 3–10.

**Scope note**: this is not about adding new pedagogical content (no new
"tip"/"warning" boxes). It is about correctly separating existing content —
a quote is either already set apart in the PDF's margin column, or it is a
genuine part of the surrounding paragraph. Only the former belongs in
`:::{aside}`.

## The rule

A margin-column pull-quote (an epigraph attributed to a scientist/engineer,
set beside the body text in the PDF's two-column layout) must be wrapped in
`:::{aside} ... :::` in the Markdown, never left as plain body prose and
never merged into the paragraph before/after it. This is the book's own
existing convention (used ~30 times already across the ten chapters); the
audit's job is just to find the places conversion missed or mangled it.

Format to match exactly (see chapters/ch-01-fundamental-concepts.md:61-67
for a clean reference instance):

```
:::{aside}
« quoted text, including internal *emphasis* markup »

Attributor Name, year

*Italicized source title* [[N](#ref-N)]
:::
```

## How to detect candidates

1. Run `python3 scripts/qa/pdf_columns.py N` for every page of the chapter.
   The `--- margin ---` section is the tell: anything in there bracketed by
   `«` … `»` is a pull-quote that was set in the margin column, i.e. it must
   become an `:::{aside}` block, not body prose.
2. `grep -c '«' chapters/ch-0X-*.md` vs. the count of margin quotes found via
   step 1 — a mismatch means one is unwrapped or missing.
3. For each margin quote found, grep the chapter markdown for a fragment of
   its text and confirm it's already inside a `:::{aside}` fence. If it's
   sitting in plain paragraph text instead, wrap it (do not alter the quote
   text itself beyond fixing conversion garbage already covered by Task 1's
   correctness pass).
4. Don't confuse a margin *figure caption/attribution* (e.g. `*Diagram* CC-0
   *Olivier Cleynen*`) with a quote — only wrap the `«...»` epigraphs.

## Named defect: nested aside blocks

One recurring conversion bug: two adjacent margin quotes on the same PDF
page (by two different people, e.g. two quotes both illustrating the same
section) get merged into a single Markdown block where the second
`:::{aside}` opens *before* the first one closes, producing a nested aside
with a double closing fence. This renders as one box containing a smaller
box instead of two sibling boxes, and doesn't match the PDF (where each
quote is its own separate margin item).

Detect it with:

```
grep -n "^:::{aside}" chapters/ch-0X-*.md
```

and check whether two `:::{aside}` opens appear with no `:::` close between
them. Fix by finding the true boundary between the two quotes (their
attribution lines differ — different name/year) and giving each its own
`:::{aside} ... :::` pair, in sequence, not nested.

## Instances found and fixed (chapters 1–2, 2026-08-23)

- `chapters/ch-01-fundamental-concepts.md:463-475` (§1.4.2 Heat) — the James
  Joule (1845) and Rudolf Clausius (1850) quotes were merged into one nested
  `:::{aside}` (Clausius's aside opened inside Joule's, before Joule's
  closed). PDF page 20's margin column confirms these are two separate
  quote boxes. Split into two sibling `:::{aside}` blocks.
- All other margin quotes checked in chapters 1–2 (Feynman/§1.1.2 p.12,
  Thomson/§1.5 p.23, Clausius/§2.3 p.35, Clapeyron/§2.4.1 p.40, Pambour ×2/
  §2.4.2–2.4.3 pp.41,45, Feynman/§2.4.4 p.49) were already correctly wrapped
  in standalone `:::{aside}` blocks with matching text — no changes needed.

## Related correctness fixes made in the same pass

Not admonition issues, but found via the same page-by-page PDF walk (see
`appendices/app-a8-errata-change-log.md` for the dated changelog entry):

- `chapters/ch-02-closed-systems.md:185` and `:396` — orphaned single-letter
  lines (`A`, `B`) left over from margin figure-axis labels during
  extraction, sitting in the body flow right before unrelated equations.
  Removed.
- `chapters/ch-02-closed-systems.md` exercise 2.5 (*Cycle of a Gasoline
  Engine*) — problem statement was truncated mid-sentence after the "C to D"
  process step; the "D to A" step and all 8 numbered questions (present on
  PDF p.54) were missing from the Markdown. Restored.
- `chapters/ch-02-closed-systems.md` exercise 2.7 answer — a stray `.7**`
  fragment (leftover from the `**2.7**` enumerator during column
  reconstruction) sat as its own line before the first answer item. Removed.

## Instances found and fixed (chapters 3–4, 2026-08-23)

All margin quotes already correctly wrapped, no changes needed. Checked
against `scripts/qa/pdf_columns.py` output for PDF pp.59–80 (chapter 3) and
pp.81–112 (chapter 4):

- Chapter 3: Aurel Stodola ×2 (§3.2.1 p.61, §3.3.3 p.65).
- Chapter 4: Sadi Carnot ×3, Émile Clapeyron, Richard Feynman, Louis Joseph
  Gay-Lussac, James Prescott Joule, Rudolf Diesel (§4.1.2 p.83 — two adjacent
  quotes, correctly two sibling `:::{aside}` blocks, not nested — §4.1.4
  p.85, §4.3.2 p.90, §4.3.3 p.91, §4.4.4 p.98, §4.4.5 p.99).

No nested-aside bug (the chapters 1–2 defect class) was found in either
chapter: every `:::{aside}` open/close pair in chapters 3–4 is already
correctly sequential and non-nested.

### Related correctness fixes made in the same pass

Not admonition issues, but found via the same page-by-page PDF walk (see
`appendices/app-a8-errata-change-log.md` for the dated changelog entry):

- `chapters/ch-03-open-systems.md`, exercise 3.4 (*Turbine Engine Nozzle*) —
  the second half of the problem statement (outlet conditions and both
  numbered questions), which follows a mid-problem figure in the PDF, had
  been left as orphaned body prose after the exercise's answer and closing
  fence instead of being part of the problem statement. Merged back in,
  ahead of the answer.
- `chapters/ch-03-open-systems.md`, exercise 3.9 (*Compressor and Turbine of
  a Turboprop Engine*) — same defect: the turbine sub-problem (properties
  and questions 4–5, whose numeric answers were already present in the
  answer key) sat as orphaned prose after the exercise's figure, disconnected
  from any `{exercise}` block. Merged back into the problem statement.
- `chapters/ch-04-the-ideal-gas.md`, exercise 4.9 (*Elementary Processes:
  Vocabulary*) — the second half of the question ("Among the processes
  above, which ones are: ...") had been left as a floating, unlabeled
  paragraph between the exercise's answer and the next exercise. Moved back
  into the problem statement, ahead of the answer.
- `chapters/ch-03-open-systems.md` exercises 3.2 and 3.8, and
  `chapters/ch-04-the-ideal-gas.md` exercises 4.10, 4.11, and 4.12 — stray
  `.2**`, `.8**`, `10**`, `11**`, `12**` fragments (leftover from
  `**N.M**` exercise-enumerator labels split during column reconstruction)
  sitting as their own line at the top of the answer block. Removed.
- `chapters/ch-03-open-systems.md`, exercise 3.9 answer — a stray
  `*Engineering Thermodynamics* by Olivier Cleynen` footer-boilerplate line
  and a doubled closing `$$` at the end of the answer. Removed / corrected
  to a single `$`.
- `chapters/ch-04-the-ideal-gas.md`, exercise 4.12 answer, item 3 — the `B`
  subscript on $v^{-1.5}$ had been stranded as an orphaned single-letter
  line, leaving the formula as a bare `kv^{-1.5}`. Restored to
  $kv_{\mathrm{B}}^{-1.5}$.
- `chapters/ch-04-the-ideal-gas.md`, exercise 4.13 — equation 4/36 as
  restated in the exercise had `v_1/v_2` swapped relative to the PDF and to
  the same equation given correctly earlier in the chapter's Problems
  preamble. Corrected to `v_2/v_1`.

## Instances found and fixed (chapters 5–6, 2026-08-23)

All margin quotes already correctly wrapped, no changes needed. Checked
against `scripts/qa/pdf_columns.py` output for PDF pp.113–148 (chapter 5)
and pp.149–174 (chapter 6):

- Chapter 5: Sadi Carnot, Rudolf Clausius ×2, François-Marie Guyonneau de
  Pambour ×4 (§5.1.2 p.115, §5.1.4 p.118, §5.2.1 p.119 and p.120, §5.2.3
  p.124, §5.4.2 p.131, §5.5.3 p.138).
- Chapter 6: Sadi Carnot (§6.2.4 p.162).

No nested-aside bug (the chapters 1–2 defect class) was found in either
chapter: every `:::{aside}` open/close pair in chapters 5–6 is already
correctly sequential and non-nested (verified with a `:::`-fence balance
check, not just the aside-count grep).

### Related correctness fixes made in the same pass

Not admonition issues, but found via the same page-by-page PDF walk (see
`appendices/app-a8-errata-change-log.md` for the dated changelog entry):

- `chapters/ch-05-liquids-and-vapors.md` exercises 5.10 and 5.11, and
  `chapters/ch-06-thermodynamic-cycles.md` exercises 6.8 and 6.9 — stray
  `10**`, `11**`, `.8**`, `.9**` fragments (leftover from `**N.M**`
  exercise-enumerator labels split during column reconstruction) sitting as
  their own line at the top of the answer block. Removed.
- `chapters/ch-06-thermodynamic-cycles.md`, exercise 6.10 (*Industrial
  Refrigeration*) — the exercise's final question ("What would be the
  annual financial savings generated by changing the refrigerator model?")
  had been left as a floating, unlabeled paragraph between the exercise's
  answer and exercise 6.11. Moved back into the problem statement, ahead of
  the answer.
- `chapters/ch-05-liquids-and-vapors.md`, Example 5.5's solution and
  exercise 5.13's answer, and `chapters/ch-06-thermodynamic-cycles.md`,
  exercise 6.7's answer — three more stray `*Engineering Thermodynamics* by
  Olivier Cleynen` footer-boilerplate lines spliced into running text (the
  same defect class already found once in chapter 3). In the chapter 6
  instance the footer text had also split the hyphenated word
  "refrig-erator" across a line break. All removed; the chapter 6 word
  rejoined as "refrigerator".

## Instances found and fixed (chapters 7–8, 2026-08-23)

All margin quotes already correctly wrapped, no changes needed. Checked
against `scripts/qa/pdf_columns.py` output for PDF pp.176–207 (chapter 7)
and pp.208–239 (chapter 8):

- Chapter 7: Sadi Carnot ×3, Rudolf Clausius, Émile Clapeyron, William
  Thomson ×2, Rudolf Diesel (§7.2.1 p.179, §7.3.1 p.182, §7.3.2 p.183,
  §7.3.3 p.184, §7.4.4 p.192 and p.194, §7.5.1 p.195 ×2).
- Chapter 8: Rudolf Clausius ×4, Sadi Carnot, Richard Feynman, William
  Thomson (§8.2.2 p.212, §8.3.2 p.217, §8.4.1 p.224, §8.4.1 p.225, §8.4.3
  p.226, §8.5.3 p.230 ×2, §8.5.4 p.232).

No nested-aside bug (the chapters 1–2 defect class) was found in either
chapter: every `:::{aside}` open/close pair in chapters 7–8 is already
correctly sequential and non-nested (verified with a `:::`-fence balance
check, not just the aside-count grep).

### Related correctness fixes made in the same pass

Not admonition issues, but found via the same page-by-page PDF walk (see
`appendices/app-a8-errata-change-log.md` for the dated changelog entry):

- `chapters/ch-08-entropy.md`, §8.2.2 — the integral bounds `A` and `B`
  (from $\int_{\mathrm{A}}^{\mathrm{B}}$) had been stranded as bare
  single-letter lines around three consecutive entropy-change equations
  (the unlabeled equation before 8/2, and equations 8/7 and 8/8), leaving
  each equation missing its bounds. Restored the `\int _{\mathrm{A}}^{\mathrm{B}}`
  bounds inside each equation and removed the orphaned `B` / `A B` / `A`
  lines.
- `chapters/ch-07-the-second-law.md` exercises 7.8 and 7.10, and
  `chapters/ch-08-entropy.md` exercises 8.11 and 8.13 — stray `.8**`,
  `10**`, `11**`, `13**` fragments (leftover from `**N.M**`
  exercise-enumerator labels split during column reconstruction) sitting as
  their own line at the top of the answer block. Removed.
- `chapters/ch-07-the-second-law.md`, exercise 7.10's answer, and
  `chapters/ch-08-entropy.md`, between example 8.2's solution and example
  8.3's problem statement, and exercise 8.14's answer — three more stray
  `*Engineering Thermodynamics* by Olivier Cleynen` footer-boilerplate
  lines spliced into running text (the same defect class already found in
  chapters 3, 5, and 6). None split a word across a line break this time.
  All removed.
- `chapters/ch-08-entropy.md`, figure 8.15's `:alt:` text — truncated
  mid-sentence ("...ensures the temperatures calcula") while the figure's
  own caption carried the complete sentence. Restored the alt text to
  match the full caption.

## Instances found and fixed (chapters 9–10, 2026-08-23)

All margin quotes already correctly wrapped, no changes needed. Checked
against `scripts/qa/pdf_columns.py` output for PDF pp.239–266 (chapter 9)
and pp.267–302 (chapter 10):

- Chapter 9: Sadi Carnot, François-Marie Guyonneau de Pambour, and a
  first-person narrative aside by Jacques Darolles (§9.1 p.241, §9.3.1
  p.243, §9.5 p.263 — the Darolles aside is not a historical-figure pull
  quote but is already wrapped the same way as the others).
- Chapter 10: Rudolf Diesel, Sadi Carnot, Louis Joseph Gay-Lussac, Aurel
  Stodola (§10.3.3 p.274, §10.4.1 p.278, §10.4.4 p.282, §10.5.2 p.285).

No nested-aside bug (the chapters 1–2 defect class) was found in either
chapter: every `:::{aside}` open/close pair in chapters 9–10 is already
correctly sequential and non-nested (verified with a `:::`-fence balance
check, not just the aside-count grep).

### Related correctness fixes made in the same pass

Not admonition issues, but found via the same page-by-page PDF walk (see
`appendices/app-a8-errata-change-log.md` for the dated changelog entry):

- `chapters/ch-09-steam-power-cycles.md`, §9.3.1 — the integral bounds `A`
  and `B` (from $\int_{\mathrm{A}}^{\mathrm{B}}$) had been stranded as bare
  single-letter lines around two equations (the restatement of 3/22 and
  equation 9/4), leaving both missing their bounds. Restored the
  `\int _{\mathrm{A}}^{\mathrm{B}}` bounds inside each equation and removed
  the orphaned `B` / `A` lines.
- `chapters/ch-10-air-based-power-cycles.md`, equation 10/3 — split across
  two separate `{math}` blocks (numerator only, then bare denominator)
  instead of one fraction. Merged into
  $\varepsilon \equiv \frac{v_{\mathrm{A}}}{v_{\mathrm{B}}}$.
- `chapters/ch-10-air-based-power-cycles.md`, equation 10/4 — missing
  fraction bar, rendering as $\eta_{\mathrm{Otto}} = 1 -
  \varepsilon^{\gamma-1}1$. Corrected to $\eta_{\mathrm{Otto}} = 1 -
  \frac{1}{\varepsilon^{\gamma-1}}$.
- `chapters/ch-10-air-based-power-cycles.md` exercises 10.3, 10.5, and
  10.6 — stray `.3**`, `.5**`, `.6**` fragments (leftover from `**N.M**`
  exercise-enumerator labels split during column reconstruction) sitting
  as their own line at the top of the answer block. Removed.
- `chapters/ch-09-steam-power-cycles.md`, exercise 9.3's answer, and
  `chapters/ch-10-air-based-power-cycles.md`, after equation 10/10 and in
  exercise 10.6's answer — stray `*Engineering Thermodynamics* by Olivier
  Cleynen` footer-boilerplate lines spliced into running text (the same
  defect class already found in chapters 3, 5, 6, and 7–8). The exercise
  10.6 instance was the worst found in this pass: the footer line, two
  stray page numbers ("303", "304"), and the entire Appendix A1–A11
  front-matter table of contents (real content from PDF p.303, but
  belonging to the next section, not to chapter 10) had all been spliced
  onto the end of the answer. All removed.
- Ligature/OCR-style word garbling in running prose (not captions), of the
  same kind `scripts/qa/fix_ligatures.py` targets but in forms its regexes
  didn't match (an inserted space or swapped letter rather than a
  same-word transposition): "fin ally" → "finally", "ef-fi ciency" →
  "efficiency" (chapter 9); "fin ite" → "finite", "ffity" → "fifty", "fti
  tightly" → "fit tightly", "briefly )" → "briefly)", "inful ence" →
  "influence" ×2, ```orifcie``` → "orifice" (chapter 10). Each confirmed
  against the source PDF's raw `get_text()` output before correcting.
  Pre-existing PDF-native typos ("the the painful reality", "air a as a
  working fluid", "to the the fact") were confirmed present in the raw PDF
  itself and left untouched.
