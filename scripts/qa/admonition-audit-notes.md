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
