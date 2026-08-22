#!/usr/bin/env python3
"""Repair fi/fl ligature transpositions in the generated Markdown.

Root cause (fixed in ``layout.py``): PyMuPDF reports the second character of an
``fi``/``fl`` ligature with an x-origin a thousandth of a point *past* the
character that follows it, so sorting a line's characters by x transposes them —
"first" became "frist", "definite" became "defni ite".  The already-generated
Markdown still carries the damage, so repair it in place using the PDF itself as
the authority: every candidate is confirmed against the corrected extraction
before it is rewritten.

Usage:  fix_ligatures.py [--write]
"""
from __future__ import annotations
import re, sys, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pdf_columns import PDF, page_streams, join_frags
import pymupdf

FILES = [p for d in ("front", "chapters", "appendices", "back") for p in sorted((ROOT / d).glob("*.md"))]

def pdf_vocabulary():
    """Every word the corrected extraction produces, with its frequency."""
    vocab = collections.Counter()
    with pymupdf.open(PDF) as doc:
        for i in range(doc.page_count):
            st = page_streams(doc[i], i)
            for role in ("body", "margin", "caption"):
                text = join_frags(st[role], math=False)
                vocab.update(re.findall(r"[A-Za-z]+", text))
    return vocab

def candidates(word):
    """Undo a transposed ligature: 'frist' -> 'first', 'defni ite' -> 'definite'."""
    out = set()
    for lig, (a, b) in (("fi", ("f", "i")), ("fl", ("f", "l")), ("ff", ("f", "f"))):
        # the ligature's second letter slipped one place to the right
        for m in re.finditer(re.escape(a), word):
            k = m.start()
            if k + 2 <= len(word) and word[k + 2 : k + 3] == b:
                out.add(word[:k + 1] + b + word[k + 1] + word[k + 3:])
    return out - {word}

def main():
    write = "--write" in sys.argv
    vocab = pdf_vocabulary()
    total = 0
    for path in FILES:
        text = path.read_text()
        original = text
        fixes = collections.Counter()

        # 1. a ligature that swallowed the following letter, splitting the word
        def rejoin(m):
            merged = m.group(1) + m.group(2)
            for cand in candidates(merged) | {merged}:
                if vocab[cand] >= 2 and vocab[merged] == 0:
                    fixes[f"{m.group(0)!r} -> {cand!r}"] += 1
                    return cand
            return m.group(0)

        text = re.sub(r"\b(\w*f[nl]i|\w*f[il]\w*)\s+(\w{2,})\b", rejoin, text)

        # 2. a straight transposition inside one word
        def untranspose(m):
            w = m.group(0)
            if vocab[w] >= 2:
                return w                       # the PDF really does spell it this way
            best = [c for c in candidates(w) if vocab[c] >= 2]
            if len(best) == 1:
                fixes[f"{w!r} -> {best[0]!r}"] += 1
                return best[0]
            return w

        text = re.sub(r"\b[A-Za-z]{4,}\b", untranspose, text)

        if fixes:
            n = sum(fixes.values())
            total += n
            print(f"{path.relative_to(ROOT)}: {n} fixes")
            for bad, count in fixes.most_common(40):
                print(f"    {bad} x{count}")
        if write and text != original:
            path.write_text(text)
    print(f"\ntotal: {total} ({'WRITTEN' if write else 'dry run'})")

if __name__ == "__main__":
    main()
