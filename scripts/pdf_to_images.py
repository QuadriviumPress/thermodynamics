#!/usr/bin/env python3
"""Render PDF pages to PNG for visual QA during conversion."""

import argparse
import json
import os

import pymupdf


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--dpi", type=int, default=120)
    ap.add_argument("--out", default="work/pages")
    ap.add_argument("--first", type=int, default=1)
    ap.add_argument("--last", type=int, default=0)
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    doc = pymupdf.open(args.pdf)
    last = args.last or doc.page_count
    pages = []
    zoom = args.dpi / 72.0
    mat = pymupdf.Matrix(zoom, zoom)
    for i in range(args.first - 1, min(last, doc.page_count)):
        pix = doc[i].get_pixmap(matrix=mat)
        path = os.path.abspath(os.path.join(args.out, f"page_{i + 1:03d}.png"))
        pix.save(path)
        pages.append({"page": i + 1, "path": path})
    print(json.dumps(pages))


if __name__ == "__main__":
    main()
