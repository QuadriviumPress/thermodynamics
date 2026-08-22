#!/usr/bin/env python3
"""Replace truncated figure ``:alt:`` text with the figure's full caption.

The conversion wrote ``:alt:`` as a fixed-length prefix of the caption, so most
figures announce themselves to a screen reader with a sentence that stops
mid-word.  The full caption is already in the directive body, so use it.

Usage:  fix_alt.py [--write]
"""
from __future__ import annotations
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
FILES = [p for d in ("front", "chapters", "appendices", "back") for p in sorted((ROOT / d).glob("*.md"))]

FIGURE = re.compile(r"(^:::+\{figure\}[^\n]*\n)((?::[^\n]*\n)*?)(:alt: )([^\n]*)\n((?::[^\n]*\n)*)\n?(.*?)(?=^:::+\s*$)",
                    re.M | re.S)

def main():
    write = "--write" in sys.argv
    total = 0
    for path in FILES:
        text = path.read_text()
        changed = 0

        def repl(m):
            nonlocal changed
            head, pre, tag, alt, post, body = m.groups()
            caption = " ".join(body.split()).strip()
            if not caption or len(caption) < len(alt):
                return m.group(0)
            # only rewrite where the alt really is a truncated prefix of the caption
            if not caption.startswith(alt[:40]):
                return m.group(0)
            if caption == alt:
                return m.group(0)
            clean = re.sub(r"\s*\*(Photo|Diagram|Figure)\b.*$", "", caption).strip()
            changed += 1
            return f"{head}{pre}{tag}{clean or caption}\n{post}\n{body}"

        text2 = FIGURE.sub(repl, text)
        if changed:
            total += changed
            print(f"{path.relative_to(ROOT)}: {changed}")
        if write and text2 != text:
            path.write_text(text2)
    print(f"\ntotal: {total} ({'WRITTEN' if write else 'dry run'})")

if __name__ == "__main__":
    main()
