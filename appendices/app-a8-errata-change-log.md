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

These rendering differences are purely presentational and do not affect the technical content or accuracy of the textbook. All equations, figures, data, and explanatory text remain faithful to the original source.
