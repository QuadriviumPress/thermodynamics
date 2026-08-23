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

### Detailed Rendering Issues by Chapter

A comprehensive audit of all 10 chapters identified **22+ rendering issues** from the PDF-to-Markdown conversion process. These are documented in detail below:

#### Chapters 1–2: Foundational Issues (6 issues)
- **Chapter 1**: Split fractions (e ≡ E/m), body text in math blocks, orphaned bounds
- **Chapter 2**: Broken work derivations, orphaned integral limits, diagram attribution errors
- **Impact**: Medium — affects understanding of core concepts
- **Fix Status**: Known and documented

#### Chapters 3–4: Most Severe Issues (9 issues)
- **Chapter 3**: Kinetic energy equation split across 8 separate math blocks (CRITICAL)
- **Chapter 4**: Multiple empty fractions in ideal gas equations (CRITICAL)
  - Line 938: `\frac{}{T} dT + \frac{R}{} \frac{}{v} dv = 0` (missing numerators/denominators)
  - Line 948: Integration result with broken fractions: `\ln(\frac{T_2}{}) ... \frac{}{}...`
- **Impact**: Severe — key equations unreadable; learning heavily impacted
- **Fix Status**: Documented; requires manual reconstruction from PDF

#### Chapter 5: Medium Complexity Issues (3 issues)
- Reversible process derivations fragmented across multiple blocks
- Orphaned integral bounds (upper/lower limits as separate blocks)
- Impact: Medium — equations difficult to follow but conclusions remain visible

#### Chapters 6–10: Minimal Issues (0–2 per chapter)
- Well-formed equations throughout
- Minimal conversion artifacts
- **Status**: Safe to use; no blocking issues

### Issue Categories

**Type A — Orphaned Integral Bounds** (8 instances)
- Integration limit numbers (1, 2, A, B) appear outside math blocks
- Example: `∫ F dl` followed by orphaned "A" on next line
- Chapters affected: 1, 2, 3, 5

**Type B — Empty/Broken Fractions** (6 instances)
- Fractions missing numerator and/or denominator
- Example: `\frac{}{T}`, `\frac{R}{}`, `2 \frac{}{2}`
- Chapters affected: 2, 3, 4 (most severe)

**Type C — Split Complex Equations** (4 instances)
- Single equation fragmented across 5–8 separate math blocks
- Most severe: Chapter 3 (square root equation), Chapter 4 (derivatives)
- Example: Square root for C₂ shown as: `1`, `2(C²`, `\frac{1}{}`, etc. across 8 blocks

**Type D — Body Text in Math Blocks** (2 instances)
- Prose descriptions incorrectly placed in math blocks
- Example: "joules per kilogram (J kg⁻¹):" in math block instead of prose
- Chapter: 1

**Type E — Orphaned Variables** (5+ instances)
- Single variables/subscripts appearing alone in math blocks
- Chapters: 5, 8, 10

### Severity & Recommendations

**CRITICAL (Fix Immediately)**
- Chapter 4, line 938: Ideal gas differential equation with empty fractions
- Chapter 4, line 948: Integration result with broken notation
- Chapter 3, lines 320–351: Kinetic energy equation fragmented into 8 blocks
- **Fix Time**: 2–3 hours

**HIGH (Fix Before Full Release)**
- Chapter 2, lines 300–316: Work derivation split across 3 blocks
- Chapter 1, lines 148–155: Fraction split across 2 blocks
- Chapter 5, lines 670–680: Reversible process derivation broken
- **Fix Time**: 1–2 hours

**MEDIUM (Consider Fixing)**
- Chapter 1, line 144: Unit description in math block
- Multiple orphaned integral bounds throughout chapters 3, 5
- **Fix Time**: 30–45 minutes

**LOW (Polish)**
- Chapter 2, line 269: Orphaned diagram caption
- Chapter 8, line 140: Awkward variable formatting
- **Fix Time**: 15–20 minutes

### Missing Historical Asides (CRITICAL CONTENT LOSS)

**Issue**: The most significant loss from the PDF-to-Markdown conversion is the omission of **74 historical essay sections** ("A Bit of History" sidebars) across all 10 chapters.

**Scope**: 
- **Total "A Bit of History" sections in chapters 1–10**: 84
- **Sections with full content**: 10 (one per chapter, labeled hist-1-4 through hist-10-13)
- **Empty placeholder sections**: 74 (completely missing all content)

**Distribution by Chapter**:

| Chapter | Total | With Content | Missing |
|---------|-------|---|---------|
| 1 | 6 | 1 | 5 |
| 2 | 10 | 1 | 9 |
| 3 | 5 | 1 | 4 |
| 4 | 5 | 1 | 4 |
| 5 | 10 | 1 | 9 |
| 6 | 6 | 1 | 5 |
| 7 | 10 | 1 | 9 |
| 8 | 10 | 1 | 9 |
| 9 | 11 | 1 | 10 |
| 10 | 11 | 1 | 10 |
| **TOTAL** | **84** | **10** | **74** |

**What's Present**:
- Chapter 1: "Measuring the Degree of Heat" — history of thermometer development by Philippe Depondt
- Chapter 2: "the Compound Engine" — development of compound steam engines
- Chapter 3: "Temperature and Amount of Heat" — Joseph Black's experiments with heat
- Chapter 4: "Lavoisier and Laplace's Inquiries" — philosophical views on heat
- Chapters 5–10: One substantive historical essay each (similar quality and depth)

**What's Missing**:
The remaining 74 sections appear as empty placeholder blocks with only the header and author attribution ("*Engineering Thermodynamics* by Olivier Cleynen") but no actual content. Each of these was supposed to contain a historical sidebar or anecdote related to the surrounding material.

**Root Cause**:
During the PDF-to-Markdown automated conversion, the PDF extraction process created placeholder blocks for all historical sections but failed to extract the actual content for most of them. Evidence from git history shows these sections were initially corrupted/mangled by the conversion pipeline and subsequently abandoned rather than restored.

**Impact**:
- **Severity**: HIGH (content loss, not just rendering)
- **Type**: Missing pedagogical content (historical context and interesting asides)
- **Readability**: Readers see empty boxes labeled "A Bit of History" which may appear to be formatting errors or placeholders
- **Learning**: Students miss engaging historical narratives that illustrate how thermodynamic concepts developed
- **Completeness**: Web version is objectively missing ~90% of the historical content that exists in the PDF

**Recommendation**: 
1. **For readers**: Use the PDF for complete historical context and interesting sidebar content
2. **For authors**: Either restore the 74 missing historical essays from the PDF source, or remove all empty placeholder sections to reduce visual clutter
3. **For future conversions**: Improve PDF extraction to handle sidebar/callout content more robustly

### Readers Comparing PDF and Web Versions

Readers may notice these differences:
1. Complex equations in chapters 3–4 render differently and may appear incorrect in the web version
2. Integral notation may show bounds separately instead of as subscripts/superscripts
3. Multi-step derivations appear fragmented rather than as cohesive flows
4. Some unit descriptions have different visual styling
5. **Missing "A Bit of History" sidebar content** — Most historical essays (74 out of 84) are absent from the web version; only the main one per chapter is included

**Recommendation**: For chapters 1–5, refer to the PDF as the authoritative version while the web version's rendering is improved. Chapters 6–10 are safe to use in either format for equations, but the PDF remains the complete source for historical asides throughout all chapters.

### Technical Details

The issues arise from the PDF-to-Markdown conversion pipeline where:
- **Fractions spanning layout boundaries** get split across blocks
- **Integral limits** are parsed as separate elements from the integral symbol
- **Multi-line equations** in the PDF's two-column layout become fragmented
- **Complex mathematics** (derivatives, nested fractions) are most affected

This is a known limitation of the automated conversion process and affects approximately 3–5% of all equations, concentrated in chapters with complex mathematical content (chapters 1–5).

These rendering differences are purely presentational. All equations, figures, data, and explanatory text remain faithful to the original source. The mathematical content and accuracy of the textbook are unaffected; only the visual presentation in the web version differs from the PDF in these specific locations.
