#!/bin/sh
# Regenerate the MyST edition from thermodynamics-free-textbook.pdf.
# Phase 2 will retarget build_book.py to outline.json; extract/render are
# adapted from energyAndHumanAmbitions.
set -e
cd "$(dirname "$0")"
python3 extract.py
python3 render_figures.py
python3 render_steam_tables.py
python3 build_book.py
