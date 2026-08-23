#!/usr/bin/env python3
"""Quality checks on the ported MyST files, independent of the conversion pipeline.

Flags the failure modes that PDF->Markdown extraction introduces: two-column
margin notes woven into body paragraphs, body prose captured as math, ligature
scrambles, headings demoted to bold, and paragraphs split mid-sentence.
"""
import re, sys, json, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parents[2]
FILES = sorted(
    [p for d in ("front", "chapters", "appendices", "back") for p in (ROOT / d).glob("*.md")]
)

# words the PDF's fi/fl ligatures get scrambled into by the extractor
LIGATURE = re.compile(r"\b\w*(?:fni|fi\s+(?:ally|eld|rst|nd|ne)\b|feid|eifd|unifeid|defni|fni\s)\w*", re.I)
BAD_LIG = re.compile(r"(fni|feid|eifd|fl\s+ow\b|de.?ne\s+e\b|de.?ne\s+ite\b)", re.I)

CHECKS = collections.OrderedDict()

def check(name):
    def deco(fn):
        CHECKS[name] = fn
        return fn
    return deco

def paragraphs(text):
    """Yield (line_no, paragraph) for body paragraphs outside fenced/directive blocks."""
    lines = text.split("\n")
    buf, start = [], 0
    for i, line in enumerate(lines, 1):
        if line.strip():
            if not buf:
                start = i
            buf.append(line)
        else:
            if buf:
                yield start, "\n".join(buf)
            buf = []
    if buf:
        yield start, "\n".join(buf)

@check("margin-note-interleave")
def c_margin(text):
    """Margin-note text woven into a body paragraph as \\mathrm superscripts.

    A restored ``{aside}`` legitimately carries the book's guillemet quotation
    marks, so only unrestored body paragraphs count.
    """
    for ln, p in paragraphs(text):
        if p.lstrip().startswith((":::{aside}", "::::{aside}")):
            continue
        if re.search(r"\$\^?\{?\\mathrm\{\w+\}\s*\\mathrm\{", p) or "«" in p or "»" in p:
            yield ln, p[:120]


@check("unbalanced-quote")
def c_quote(text):
    """A guillemet quotation opened or closed but not both -- a truncated pull-quote."""
    for ln, p in paragraphs(text):
        if p.count("«") != p.count("»"):
            yield ln, p.replace("\n", " ")[:100]

@check("prose-as-math")
def c_prose_math(text):
    """Inline math that is really italic prose: $joule$, $joules (J)$ etc."""
    for ln, p in paragraphs(text):
        # walk $-delimited spans in order so we never match across two of them
        for i, span in enumerate(p.split("$")):
            if i % 2 == 0 or "\\" in span or len(span) > 60:
                continue
            words = re.findall(r"[A-Za-z]{4,}", span)
            if words and all(w.islower() for w in words):
                yield ln, "$" + span + "$"

@check("math-block-prose")
def c_math_block(text):
    """:::{math} blocks whose content is mostly running prose."""
    for m in re.finditer(r":::\{math\}(.*?):::", text, re.S):
        body = m.group(1)
        # strip LaTeX commands and their braced arguments before looking for prose
        body = re.sub(r"\\(?:mathrm|text|mathbf|mathit|operatorname)\s*\{[^{}]*\}", " ", body)
        body = re.sub(r"\\[a-zA-Z]+", " ", body)
        alpha = re.findall(r"\b[a-z]{4,}\b", body)
        if len(alpha) >= 6:
            ln = text[: m.start()].count("\n") + 1
            yield ln, " ".join(alpha[:10])

@check("ligature-scramble")
def c_lig(text):
    for ln, p in paragraphs(text):
        for m in BAD_LIG.finditer(p):
            s = max(0, m.start() - 25)
            yield ln, p[s : m.end() + 25].replace("\n", " ")

@check("bold-pseudo-heading")
def c_heading(text):
    """Section headings that came out as **1.1 Title** instead of ## 1.1 Title."""
    for ln, p in paragraphs(text):
        if re.fullmatch(r"\*\*\d+(\.\d+)*\s+[^*]+\*\*", p.strip()):
            yield ln, p.strip()

@check("heading-blob")
def c_blob(text):
    """A section heading with the section's entire body welded onto the same line."""
    for ln, p in paragraphs(text):
        m = re.match(r"\*\*\d+(\.\d+)*\s[^*]+\*\*(.+)", p.strip(), re.S)
        if m and len(m.group(2).split()) > 40:
            yield ln, p.strip()[:70] + f"  (+{len(m.group(2).split())} words)"


@check("inline-display-eq")
def c_inline_eq(text):
    """A numbered display equation left inline in a prose paragraph."""
    for ln, p in paragraphs(text):
        if p.lstrip().startswith((":", "#", "|")):
            continue
        for m in re.finditer(r"\$[^$]*\([0-9]+/[0-9]+\)[^$]*\$", p):
            yield ln, m.group(0)[:70]


@check("split-sentence")
def c_split(text):
    """Paragraph ends without terminal punctuation and the next begins lowercase."""
    paras = [(ln, p) for ln, p in paragraphs(text)]
    for (ln, p), (_, q) in zip(paras, paras[1:]):
        p_s, q_s = p.strip(), q.strip()
        if not p_s or not q_s:
            continue
        if p_s.startswith((":", "#", "-", "*", "|", "(", "!")) or q_s.startswith(
            (":", "#", "-", "*", "|", "(", "!", "$")
        ):
            continue
        # a wrapped two-column glossary entry is not a broken paragraph
        if "$" in p_s and len(p_s) < 90:
            continue
        if p_s[-1].isalpha() and re.match(r"[a-z]", q_s):
            yield ln, (p_s[-45:] + "  ||  " + q_s[:45]).replace("\n", " ")

@check("truncated-alt")
def c_alt(text):
    """figure :alt: cut off mid-word (extractor truncation)."""
    for m in re.finditer(r"^:alt: (.+)$", text, re.M):
        alt = m.group(1).strip()
        if len(alt) > 60 and alt[-1].isalpha() and not alt.endswith((".", "!", "?")):
            ln = text[: m.start()].count("\n") + 1
            yield ln, "..." + alt[-45:]

@check("inline-footnote")
def c_fn(text):
    """Footnote bodies left inline as $^{1}\\mathrm{A}$ ... instead of MyST footnotes."""
    for ln, p in paragraphs(text):
        if re.match(r"\$\^\{\d\}", p.strip()):
            yield ln, p.strip()[:90]

@check("dangling-start")
def c_dangling(text):
    """A paragraph that begins mid-sentence — a stitched-together fragment.

    A textbook legitimately repeats phrasing, so duplicate detection is noisy
    here; what is always wrong is a body paragraph whose first word continues a
    sentence that ended somewhere else.
    """
    prev = ""
    for ln, p in paragraphs(text):
        head, before = p.lstrip(), prev
        prev = p
        if head.startswith((":", "#", "|", "`", "-", "*", "$", "(", "!", "[", ">", "\u2022")):
            continue
        # The book sets each variable definition after a display equation on its
        # own line -- "where e is the specific energy (J/kg)," / "and m is the
        # mass ... (kg)." -- so these are house style, not stitched fragments.
        if re.match(r"(where|with|and|in which|is)\b", head) and re.search(r"\$.+\$\s+is\s+(the|a|an)\b", head):
            continue
        if before.rstrip().endswith(":::") and re.match(r"(where|with|and|in which)\b", head):
            continue
        # Equation glosses and glossary/table cross-refs are house style, not fragments.
        if re.match(r"(for a|for an|for any|for the|tab\.|fig\.|eq\.|p\.|see |cf\.)", head):
            continue
        # list-of-symbols abbreviation rows start lowercase by design
        if re.match(r"[a-z]{2,4}\s+[A-Z]", head) and len(head) < 120:
            continue
        # figure/photo credits and short cross-refs
        if re.match(r"(drawing|engraving|photo|image|diagram|selected by)\b", head, re.I):
            continue
        if re.match(r"tab\.\s*\d", head):
            continue
        first = re.match(r"([a-z][a-z'\u2019-]{2,})\b", head)
        if first and first.group(1) not in ("de", "von", "van", "der", "et", "al"):
            yield ln, head[:70]


@check("missing-image")
def c_img(text):
    for m in re.finditer(r"^:::\{figure\}\s+(\S+)", text, re.M):
        rel = m.group(1)
        if not (ROOT / "chapters" / rel).resolve().exists() and not (ROOT / rel.lstrip("./")).exists():
            ln = text[: m.start()].count("\n") + 1
            yield ln, rel

def main():
    want = sys.argv[1] if len(sys.argv) > 1 else None
    totals = collections.Counter()
    per_file = collections.defaultdict(collections.Counter)
    samples = collections.defaultdict(list)
    for f in FILES:
        text = f.read_text()
        for name, fn in CHECKS.items():
            if want and want not in (name, "all"):
                continue
            for ln, detail in fn(text):
                totals[name] += 1
                per_file[f.relative_to(ROOT).as_posix()][name] += 1
                samples[name].append(f"{f.relative_to(ROOT).as_posix()}:{ln}: {detail}")

    print(f"{'check':<24} {'count':>6}  files")
    print("-" * 60)
    for name in CHECKS:
        if want and want not in (name, "all"):
            continue
        nfiles = sum(1 for c in per_file.values() if c[name])
        print(f"{name:<24} {totals[name]:>6}  {nfiles}")
    print()
    if want:
        for s in samples[want if want != "all" else next(iter(CHECKS))]:
            print(s)
    return 0

if __name__ == "__main__":
    sys.exit(main())
