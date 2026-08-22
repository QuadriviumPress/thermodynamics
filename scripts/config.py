"""Shared paths and book structure for the thermodynamics conversion."""

from __future__ import annotations

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "thermodynamics-free-textbook.pdf")
OUTLINE = os.path.join(ROOT, "outline.json")
BUILD = os.path.join(ROOT, "build")
WORK = os.path.join(ROOT, "work")
PAGES = os.path.join(WORK, "pages")
IMAGES = os.path.join(ROOT, "images")


def load_outline() -> dict:
    with open(OUTLINE) as fh:
        return json.load(fh)
