#!/usr/bin/env python3
"""Promote bold pseudo-headings to real MyST headings, using the PDF for titles.

The conversion emitted top-level section headings as ``**2.4 Quantifying Work
with a Closed**`` -- bold text rather than a heading, and truncated where the
title wrapped to a second line in the source.  Each chapter opens with its own
table of contents in the PDF, which carries the full titles; this reads them
from there and rewrites the headings, adding the ``(sec-N-M)=`` labels that the
sub-section headings already use.

Usage:  fix_headings.py [--write]
"""
from __future__ import annotations
import re, sys, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pdf_columns import PDF, page_streams, join_frags
import pymupdf

OUTLINE = json.load(open(ROOT / "outline.json"))

def toc_titles(start_page):
    """{'2.4': 'Quantifying Work with a Closed System'} from a chapter's TOC page.

    The chapter opener carries the contents on the page after the title page;
    section entries come through as ``**2.4** **Title** **37**``.
    """
    titles = {}
    page = start_page + 1
    with pymupdf.open(PDF) as doc:
        if page > doc.page_count:
            return titles
        st = page_streams(doc[page - 1], page - 1)
        # rendered (not raw) so the bold runs that mark section entries survive
        text = " ".join(join_frags(st[r]) for r in ("body", "other"))
    for num, title in re.findall(r"\*\*(\d+\.\d+)\*\*\s*\*\*(.+?)\*\*\s*\*\*\d+\*\*", text):
        titles[num] = title.strip()
    for num, title in re.findall(r"(?<![.\d])(\d+\.\d+\.\d+)\s+(.+?)\s+\d+(?=\s|$)", text):
        titles[num] = title.strip()
    return titles


def executive_summary(start_page):
    """The boxed 'Executive summary for chapter N' on the chapter opener."""
    page = start_page + 1
    with pymupdf.open(PDF) as doc:
        if page > doc.page_count:
            return None
        st = page_streams(doc[page - 1], page - 1)
        for role in ("caption", "other", "body"):
            text = join_frags(st[role], math=False)
            m = re.search(r"\*?Executive summary for chapter \d+\*?\s*(.+)", text, re.S)
            if m:
                return re.sub(r"\s+", " ", m.group(1)).strip()
    return None


def main():
    write = "--write" in sys.argv
    total = summaries = 0
    for ch in OUTLINE["chapters"]:
        path = ROOT / "chapters" / f"{ch['slug']}.md"
        text = original = path.read_text()
        titles = toc_titles(ch["start_page"])
        fixed = []

        def repl(m):
            num, shown, tail = m.group(1), m.group(2).strip(), m.group(3)
            full = titles.get(num, shown)
            out = f"(sec-{num.replace('.', '-')})=\n## {num} {full}"
            if tail.strip():
                out += "\n\n" + tail.strip()
            fixed.append(f"{num} {full}" + ("  [+body unwelded]" if tail.strip() else ""))
            return out

        # a heading line, sometimes with the whole section body welded onto it
        text = re.sub(r"^\*\*(\d+\.\d+)\s+([^*\n]+?)\*\*(.*)$", repl, text, flags=re.M)

        # the chapter's executive summary box, dropped by the conversion
        summary = executive_summary(ch["start_page"])
        if summary and "Executive summary" not in text:
            block = (":::{admonition} Executive summary\n:class: tip\n"
                     f"{summary}\n:::")
            # place it after the chapter's opening frontmatter + title
            m = re.search(r"^## Introduction\s*$", text, re.M)
            at = m.start() if m else len(text.split("\n\n")[0])
            text = text[:at] + block + "\n\n" + text[at:]
            summaries += 1

        total += len(fixed)
        print(f"{ch['slug']}: {len(fixed)} headings"
              + (", + executive summary" if summary and summary not in original else ""))
        for f in fixed:
            print(f"    {f}")
        if write and text != original:
            path.write_text(text)
    print(f"\ntotal: {total} headings, {summaries} summaries "
          f"({'WRITTEN' if write else 'dry run'})")


if __name__ == "__main__":
    main()
