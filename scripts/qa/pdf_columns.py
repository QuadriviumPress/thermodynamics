#!/usr/bin/env python3
"""Column-aware re-extraction of the source PDF, for QA and repair.

The book sets 11pt body text in one wide column with 8pt margin notes in the
outer margin and 10pt figure captions.  Font size separates the three cleanly.
The original pipeline read some pages as a single stream, splicing margin notes
through the middle of body sentences; this module rebuilds those pages from the
same character data, reusing ``mathtext.render_line`` so the output carries the
project's usual LaTeX conventions rather than raw Unicode math glyphs.
"""
from __future__ import annotations
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import pymupdf
from layout import page_frags
from mathtext import render_line

PDF = ROOT / "thermodynamics-free-textbook.pdf"

SIZE = {"body": (10.5, 11.4), "margin": (7.4, 8.6), "caption": (9.7, 10.4)}
CHROME = 11.8            # running head and folio

def role_of(frag):
    s = frag.size
    if s >= CHROME:
        return "chrome"
    for role, (lo, hi) in SIZE.items():
        if lo <= s <= hi:
            return role
    return "other"

def page_streams(page, page_index):
    """Frags grouped by role, in reading order."""
    out = {k: [] for k in ("body", "margin", "caption", "chrome", "other")}
    for f in page_frags(page, page_index):
        out[role_of(f)].append(f)
    for role in out:
        out[role].sort(key=lambda f: (round(f.bbox[1], 1), f.bbox[0]))
    return out

def join_frags(frags, *, math=True):
    """Render frags into paragraphs, undoing hyphenation and column wrapping."""
    text, prev_bottom = "", None
    for f in frags:
        line = render_line(f.chars, sidenotes=False) if math else f.raw
        line = line.strip()
        if not line:
            continue
        if text and prev_bottom is not None and f.bbox[1] - prev_bottom > 9:
            text += "\n\n"                       # a vertical gap ends a paragraph
        elif text:
            if text.endswith("-"):
                text = text[:-1]                 # word hyphenated across lines
            else:
                text += " "
        text += line
        prev_bottom = f.bbox[3]
    return re.sub(r"[ \t]+", " ", text).strip()

def page_text(pno, role="body", math=True):
    """1-based PDF page number -> that role's text for the page."""
    with pymupdf.open(PDF) as doc:
        return join_frags(page_streams(doc[pno - 1], pno - 1)[role], math=math)

def dump(first, last):
    with pymupdf.open(PDF) as doc:
        for pno in range(first, last + 1):
            st = page_streams(doc[pno - 1], pno - 1)
            print(f"\n===== page {pno} =====")
            for role in ("body", "margin", "caption"):
                if st[role]:
                    print(f"--- {role} ---\n{join_frags(st[role])}")

if __name__ == "__main__":
    a = int(sys.argv[1]); dump(a, int(sys.argv[2]) if len(sys.argv) > 2 else a)
