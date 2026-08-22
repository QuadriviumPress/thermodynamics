"""Render steam-table appendix pages as PNG for faithful reproduction."""

from __future__ import annotations

import os

import pymupdf

from config import IMAGES, PDF, load_outline

DPI = 160


def main():
    outline = load_outline()
    ap = next(a for a in outline["appendices"] if a["id"] == "A1")
    first, last = ap["start_page"] - 1, ap["end_page"] - 1
    doc = pymupdf.open(PDF)
    os.makedirs(IMAGES, exist_ok=True)
    names = []
    for pno in range(first, last + 1):
        name = f"steam-table-p{pno + 1:03d}.png"
        path = os.path.join(IMAGES, name)
        doc[pno].get_pixmap(dpi=DPI).save(path)
        names.append(name)
        print(f"  {name}")
    doc.close()
    print(f"wrote {len(names)} steam table pages to images/")


if __name__ == "__main__":
    main()
