"""Layout-aware reading of the thermodynamics source PDF.

The book is set in a single main column on A4 pages (595 × 842 pt).  There is
no tufte-style margin column; sidenotes are absent.  PyMuPDF's block
segmentation still breaks lines at equation numbers and scripts, so fragments
sharing a baseline are re-joined afterwards.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

import pymupdf

from mathtext import FLAT_FONTS, font_class

# --------------------------------------------------------------------------
# page geometry (points; page is 595.28 × 841.89)
# --------------------------------------------------------------------------

HEADER_Y = 55.0        # running heads live above this
FOOTER_Y = 820.0       # footer lines live below this
LEADING = 12.8         # body-text baseline separation
PARA_GAP = 15.6        # baseline separation that implies a new paragraph

# Single-column geometry (most body pages)
SINGLE_COLUMN = (56.0, 526.0, 526.0, 540.0)
# Two-column geometry (many problem pages: left + right body columns)
TWO_COLUMN = (56.0, 282.0, 300.0, 526.0)
COLUMNS = {0: SINGLE_COLUMN, 1: SINGLE_COLUMN}

# heading sizes, largest first
SIZE_PART = 24.0
SIZE_PART_LABEL = 18.6
SIZE_CHAPTER = 17.2     # section headings: 1.1, 1.2, …
SIZE_SECTION = 14.3     # subsection headings: 1.1.1, 1.1.2, …
SIZE_SUBSECTION = 12.0
SIZE_BODY = 10.0
SIZE_MARGIN = 7.8

# fill colours of shaded call-out rectangles
BOX_COLORS = {
    (0.95, 0.95, 0.95): "example",
    (0.83, 0.87, 0.95): "box",
    (0.99, 0.88, 0.93): "definition",
    (0.8, 1.0, 0.8): "explore",
    (0.71, 0.85, 0.96): "history",
}


def columns_for(page_index: int):
    return COLUMNS[page_index % 2]


# --------------------------------------------------------------------------
# data model
# --------------------------------------------------------------------------


@dataclass
class Char:
    c: str
    x: float
    y: float          # baseline origin
    size: float
    font: str
    color: int = 0
    w: float = 0.0    # advance width, used to spot missing inter-word spaces


@dataclass
class Frag:
    chars: list
    bbox: tuple
    column: str

    @property
    def baseline(self):
        """Baseline of the full-size text, ignoring scripts and delimiters."""
        vis = [c for c in self.chars if c.c.strip() and c.font not in FLAT_FONTS]
        if not vis:
            vis = [c for c in self.chars if c.c.strip()]
        if not vis:
            return round(self.chars[0].y, 1)
        top = max(c.size for c in vis)
        counts = {}
        for ch in vis:
            if ch.size >= top - 0.7:
                counts[round(ch.y, 1)] = counts.get(round(ch.y, 1), 0) + 1
        return max(counts.items(), key=lambda kv: kv[1])[0]

    @property
    def is_delimiter(self):
        return all(c.font in FLAT_FONTS for c in self.chars if c.c.strip())

    @property
    def size(self):
        vis = [round(c.size, 1) for c in self.chars if c.c.strip()]
        if not vis:
            return SIZE_BODY
        counts = {}
        for v in vis:
            counts[v] = counts.get(v, 0) + 1
        return max(counts.items(), key=lambda kv: (kv[1], v))[0]

    @property
    def maxsize(self):
        vis = [c.size for c in self.chars if c.c.strip()]
        return max(vis) if vis else SIZE_BODY

    @property
    def raw(self):
        return "".join(c.c for c in self.chars)

    @property
    def fonts(self):
        return {c.font for c in self.chars if c.c.strip()}


def _classify_column(x0, x1, geom, two_column=False):
    if x1 - x0 > 420:
        return "wide"
    if not two_column:
        return "main"
    m0, m1, g0, g1 = geom
    cx = 0.5 * (x0 + x1)
    mid = 0.5 * (m1 + g0)
    return "main" if cx < mid else "margin"


#: geometry of the back-matter pages, which run the full measure
WIDE_COLUMNS = (56.0, 525.0, 525.0, 540.0)


def page_frags(page, page_index, wide=False, two_column=False):
    geom = WIDE_COLUMNS if wide else (TWO_COLUMN if two_column else columns_for(page_index))
    out = []
    for block in page.get_text("rawdict")["blocks"]:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            chars = []
            for span in line["spans"]:
                for ch in span["chars"]:
                    if ch["c"] == "�":
                        continue
                    chars.append(Char(ch["c"], ch["origin"][0], ch["origin"][1],
                                      span["size"], span["font"], span.get("color", 0),
                                      ch["bbox"][2] - ch["bbox"][0]))
            if not chars:
                continue
            bbox = tuple(line["bbox"])
            if bbox[3] < HEADER_Y or bbox[1] > FOOTER_Y:
                continue
            chars.sort(key=lambda c: c.x)
            out.append(Frag(chars, bbox,
                            _classify_column(bbox[0], bbox[2], geom, two_column)))
    out.sort(key=lambda f: (f.bbox[1], f.bbox[0]))
    return out


# --------------------------------------------------------------------------
# shaded call-out rectangles
# --------------------------------------------------------------------------


def shaded_boxes(page):
    """Rectangles that mark Examples, History boxes, and other call-outs."""
    found = []
    for dr in page.get_drawings():
        fill = dr.get("fill")
        if fill is None:
            continue
        key = tuple(round(v, 2) for v in fill)
        kind = BOX_COLORS.get(key)
        if kind is None:
            continue
        r = dr["rect"]
        if r.width < 80 or r.height < 10:
            continue
        found.append((kind, (r.x0, r.y0, r.x1, r.y1)))
    merged = []
    for kind, rect in sorted(found, key=lambda kr: -(kr[1][3] - kr[1][1])):
        if any(k == kind and rect[0] >= m[0] - 2 and rect[2] <= m[2] + 2
               and rect[1] >= m[1] - 2 and rect[3] <= m[3] + 2 for k, m in merged):
            continue
        merged.append((kind, rect))
    return merged


# --------------------------------------------------------------------------
# figure artwork
# --------------------------------------------------------------------------

CAPTION_RE = re.compile(r"^(Figure|Table)\s+((?:[A-D]|\d+)\.\d+):")


def _inflate(r, d):
    return (r[0] - d, r[1] - d, r[2] + d, r[3] + d)


def _overlap(a, b):
    return not (a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1])


def _union(a, b):
    return (min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3]))


#: fills used by margin information/caution symbols (rare in this edition)
ICON_FILLS = {(0.93, 0.11, 0.14), (0.08, 0.46, 0.74), (0.34, 0.69, 0.89),
              (0.18, 0.19, 0.57), (0.73, 0.73, 1.0)}


def artwork_clusters(page, boxes, pad=9, frags=()):
    """Cluster the page's vector drawings and images into figure candidates."""
    box_rects = [r for _, r in boxes]
    text_rects = [f.bbox for f in frags
                  if any(font_class(c.font) == "text" for c in f.chars if c.c.strip())]
    rects = []
    for dr in page.get_drawings():
        r = dr["rect"]
        if r.is_empty or r.is_infinite:
            continue
        rect = (r.x0, r.y0, r.x1, r.y1)
        if rect[3] < HEADER_Y + 4 or rect[1] > FOOTER_Y:
            continue
        if rect[2] - rect[0] > 520 and rect[3] - rect[1] > 620:
            continue
        if any(rect[0] >= b[0] - 2 and rect[2] <= b[2] + 2
               and rect[1] >= b[1] - 2 and rect[3] <= b[3] + 2 for b in box_rects):
            continue
        stroke = dr.get("color")
        if stroke is not None and tuple(round(v, 2) for v in stroke) == (0.8, 0.76, 0.48):
            continue
        if rect[2] - rect[0] <= 17 and rect[3] - rect[1] <= 17:
            fill = dr.get("fill")
            if fill is not None and tuple(round(v, 2) for v in fill) in ICON_FILLS:
                continue
        if rect[3] - rect[1] <= 3.0 and any(
                rect[0] >= t[0] - 3 and rect[2] <= t[2] + 3
                and rect[1] >= t[1] - 3 and rect[3] <= t[3] + 4 for t in text_rects):
            continue
        rects.append(rect)
    for block in page.get_text("dict")["blocks"]:
        if block["type"] == 1:
            rects.append(tuple(block["bbox"]))
    clusters = []
    for rect in rects:
        hit = [c for c in clusters if _overlap(_inflate(rect, pad), _inflate(c, pad))]
        for c in hit:
            clusters.remove(c)
            rect = _union(rect, c)
        clusters.append(rect)
    changed = True
    while changed:
        changed = False
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                if _overlap(_inflate(clusters[i], pad), _inflate(clusters[j], pad)):
                    clusters[i] = _union(clusters[i], clusters[j])
                    del clusters[j]
                    changed = True
                    break
            if changed:
                break
    return clusters


def attach_figure_text(clusters, frags, pad=9):
    """Grow clusters over the text that belongs to the artwork."""
    out = list(clusters)
    changed = True
    while changed:
        changed = False
        for f in frags:
            if all(font_class(c.font) != "figure" for c in f.chars if c.c.strip()):
                continue
            for i, c in enumerate(out):
                if _overlap(_inflate(f.bbox, pad + 3), _inflate(c, pad + 3)):
                    new = _union(c, f.bbox)
                    if new != c:
                        out[i] = new
                        changed = True
                    break
            else:
                out.append(f.bbox)
                changed = True
    changed = True
    while changed:
        changed = False
        for i in range(len(out)):
            for j in range(i + 1, len(out)):
                if _overlap(_inflate(out[i], pad - 3), _inflate(out[j], pad - 3)):
                    out[i] = _union(out[i], out[j])
                    del out[j]
                    changed = True
                    break
            if changed:
                break
    return [c for c in out if (c[2] - c[0]) * (c[3] - c[1]) > 400]
