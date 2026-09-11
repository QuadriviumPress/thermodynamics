"""Extract the steam-table appendix as selectable, fixed-width text."""

from __future__ import annotations

import subprocess
from pathlib import Path

from config import PDF, ROOT, load_outline

OUTPUT = Path(ROOT) / "appendices" / "steam-tables.txt"


def main():
    outline = load_outline()
    ap = next(a for a in outline["appendices"] if a["id"] == "A1")
    first, last = ap["start_page"], ap["end_page"]
    result = subprocess.run(
        ["pdftotext", "-layout", "-f", str(first), "-l", str(last), PDF, "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    OUTPUT.write_text(result.stdout.replace("\f", "\n\n"))
    print(f"wrote selectable steam tables to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
