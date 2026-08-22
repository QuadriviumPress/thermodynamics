#!/usr/bin/env python3
"""Repair body paragraphs that the original extraction wove margin notes into.

The book sets 8pt margin notes in the outer margin beside 11pt body text.  The
original pipeline read both as one column, so on those pages a margin note is
spliced through the middle of a body sentence and both become unreadable.

This tool rebuilds the affected passages from the PDF: it re-extracts each page
with font-size-based column separation (``pdf_columns``), aligns the damaged
Markdown against the clean body sentences, and swaps in the clean text.  The
margin note is re-emitted as a MyST ``{aside}`` so no content is dropped.

Usage:  repair_interleave.py [--write] [--quiet] [file ...]
"""
from __future__ import annotations
import re, sys, json, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pdf_columns import page_streams, join_frags, PDF
import pymupdf

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUTLINE = json.load(open(ROOT / "outline.json"))

# a margin note surfaces as a superscript holding a run of \mathrm-wrapped words
DEBRIS = re.compile(r"\^\{?[^{}]*(?:\\mathrm\{[^{}]*\}[\s,.]*){3,}|«|»")
MIN_CONTAIN = 0.45          # fraction of a clean sentence's words seen in the damage

def norm(s):
    s = s.replace("’", "'").replace("“", '"').replace("”", '"').replace("—", " ")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s.lower())).strip()

def md_words(block):
    """Every prose word in a damaged block, margin debris included."""
    s = re.sub(r"\\mathrm\{([^{}]*)\}", r"\1 ", block)
    s = re.sub(r"[\$\^_{}\\*`\[\]()#|]", " ", s)
    return set(norm(s).split())

def sentences(text):
    for part in re.split(r"(?<=[.:;!?])\s+", text):
        part = part.strip()
        if part:
            yield part

def page_range(path):
    for group in ("chapters", "appendices"):
        for it in OUTLINE.get(group, []):
            if it.get("slug") == path.stem:
                return it["start_page"], it["end_page"]
    front = OUTLINE.get("front", {})
    for it in front.values():
        if it.get("slug") == path.stem:
            return it["start_page"], it["end_page"]
    return None

def chapter_streams(first, last):
    """Ordered clean body sentences plus per-page margin notes."""
    sents, margins = [], {}
    with pymupdf.open(PDF) as doc:
        for pno in range(first, min(last, doc.page_count) + 1):
            st = page_streams(doc[pno - 1], pno - 1)
            for para in join_frags(st["body"]).split("\n\n"):
                for s in sentences(para):
                    sents.append((pno, s))
            note = join_frags(st["margin"]).strip()
            if note:
                margins[pno] = note
    return sents, margins

def runs_of_damage(blocks):
    """Index ranges of consecutive blocks carrying margin-note debris."""
    out, i = [], 0
    while i < len(blocks):
        if DEBRIS.search(blocks[i]):
            j = i
            while j + 1 < len(blocks) and (
                DEBRIS.search(blocks[j + 1])
                or (blocks[j + 1].strip() and not blocks[j + 1].lstrip().startswith((":", "#", "```")))
            ):
                # only absorb a clean neighbour if more damage follows it
                if not DEBRIS.search(blocks[j + 1]) and not any(
                    DEBRIS.search(b) for b in blocks[j + 2 : j + 3]
                ):
                    break
                j += 1
            out.append((i, j))
            i = j + 1
        else:
            i += 1
    return out

def link_citations(text):
    """Turn a bare [30, 35] bibliography reference into the file's link form."""
    def one(m):
        nums = re.findall(r"\d+", m.group(0))
        return "[" + ", ".join(f"[{n}](#ref-{n})" for n in nums) + "]"
    return re.sub(r"\[\d+(?:,\s*\d+)*\]", one, text)


def repair_file(path, write=False, quiet=False):
    text = path.read_text()
    rng = page_range(path)
    if not rng:
        return 0, 0
    sents, margins = chapter_streams(*rng)
    blocks = text.split("\n\n")
    repaired = asides = 0

    for lo, hi in reversed(runs_of_damage(blocks)):
        damage = "\n\n".join(blocks[lo : hi + 1])
        dw = md_words(damage)
        if len(dw) < 10:
            continue
        hits = []
        for k, (_, s) in enumerate(sents):
            sw = set(norm(s).split())
            # short sentences match almost anything; they cannot anchor a passage
            if len(sw) >= 6 and len(sw & dw) / len(sw) >= MIN_CONTAIN:
                hits.append(k)
        if len(hits) < 2:
            if not quiet:
                print(f"  skip (no alignment): {damage[:70]!r}")
            continue
        # the damage is one passage, so keep the densest run of hits and drop
        # stray matches elsewhere in the chapter
        clusters, cur = [], [hits[0]]
        for k in hits[1:]:
            if k - cur[-1] <= 3:
                cur.append(k)
            else:
                clusters.append(cur)
                cur = [k]
        clusters.append(cur)
        cluster = max(clusters, key=len)
        if len(cluster) < 2:
            if not quiet:
                print(f"  skip (scattered): {damage[:70]!r}")
            continue
        start, end = cluster[0], cluster[-1]

        # The damaged run garbles some sentences of this passage, but the
        # conversion often also emitted neighbouring sentences of the same page
        # intact in adjacent blocks.  Keep only what the file does not already
        # carry, so the repair fills the gap instead of duplicating prose.
        rest = "\n\n".join(blocks[:lo] + blocks[hi + 1:])
        rest_norm = norm(re.sub(r"\$[^$]*\$", " ", rest))
        keep = [s for _, s in sents[start:end + 1]
                if not (len(s.split()) >= 6 and norm(s)[:60] in rest_norm)]
        if not keep:
            if not quiet:
                print(f"  skip (all sentences already present): {damage[:60]!r}")
            continue
        span_words = sum(len(s.split()) for s in keep)
        damage_words = len(re.sub(r"[\$\^_{}\\*`\[\]()#|]", " ", damage).split())
        if span_words > damage_words * 1.6 + 15:
            if not quiet:
                print(f"  skip (span {span_words}w vs damage {damage_words}w): {damage[:60]!r}")
            continue

        pages = sorted({sents[k][0] for k in range(start, end + 1)})
        clean = " ".join(keep)
        parts = [clean]
        for pno in pages:
            if pno in margins:
                note = margins.pop(pno)
                note = re.sub(r"\s*[«»]\s*", "", note).strip()
                note = link_citations(note)
                parts.append(":::{aside}\n" + note + "\n:::")
                asides += 1
        blocks[lo : hi + 1] = ["\n\n".join(parts)]
        repaired += 1
        if not quiet:
            print(f"  p{pages[0]}-{pages[-1]}: {clean[:70]}...")

    if write and repaired:
        path.write_text("\n\n".join(blocks))
    return repaired, asides

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    write, quiet = "--write" in sys.argv, "--quiet" in sys.argv
    if write and "--i-reviewed-the-diff" not in sys.argv:
        sys.exit("refusing to --write: the automatic rewrite duplicates prose and "
                 "hoists tables into asides. Use this as a diagnostic and repair by "
                 "hand from pdf_columns.py.")
    files = [pathlib.Path(a) for a in args] or sorted((ROOT / "chapters").glob("*.md"))
    tr = ta = 0
    for f in files:
        print(f"{f}:")
        r, a = repair_file(f, write, quiet)
        tr += r; ta += a
        print(f"  -> {r} passages rebuilt, {a} asides restored")
    print(f"\ntotal: {tr} passages, {ta} asides  ({'WRITTEN' if write else 'dry run'})")

if __name__ == "__main__":
    main()
