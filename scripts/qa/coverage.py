#!/usr/bin/env python3
"""Sentence-level coverage of the PDF's prose in the ported Markdown.

Independent of the conversion pipeline: re-extracts the PDF with pdftotext,
normalises both sides, and reports which source sentences have no match in the
generated Markdown.  Catches dropped problems, dropped paragraphs and dropped
boxes that structural counts miss.
"""
import json, re, subprocess, sys, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parents[2]
PDF = ROOT / "thermodynamics-free-textbook.pdf"

def norm(s):
    s = s.replace("­", "").replace("’", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()

def sentences(text):
    # de-hyphenate across line breaks, then join lines within a paragraph
    text = re.sub(r"(\w)-\n\s*(\w)", r"\1\2", text)
    text = re.sub(r"\n(?!\s*\n)", " ", text)
    for raw in re.split(r"(?<=[.:;!?])\s+", text):
        s = norm(raw)
        w = s.split()
        if len(w) < 8:                   # short fragments are noise
            continue
        # skip running headers/footers, the per-chapter TOC, and equation debris
        if "engineering thermodynamics by olivier cleynen" in s: continue
        if "thermodynamicsbook com cc by sa" in s: continue
        digits = sum(c.isdigit() for c in s)
        if digits / max(len(s), 1) > 0.25: continue
        if sum(len(x) <= 2 for x in w) / len(w) > 0.4: continue
        yield s

def shingles(s, k=6):
    w = s.split()
    return {" ".join(w[i:i+k]) for i in range(max(1, len(w) - k + 1))}

def main():
    pages = subprocess.run(["pdftotext", "-layout", str(PDF), "-"],
                           capture_output=True, text=True).stdout.split("\f")
    outline = json.load(open(ROOT / "outline.json"))

    md_all = "\n".join(p.read_text() for d in ("front", "chapters", "appendices", "back")
                       for p in (ROOT / d).glob("*.md"))
    md_all = re.sub(r"\$[^$]*\$", " ", md_all)          # drop maths
    md_norm = norm(md_all)
    md_shingles = set()
    words = md_norm.split()
    for i in range(len(words) - 5):
        md_shingles.add(" ".join(words[i:i+6]))

    sections = [(str(c["number"]), c["start_page"], c["end_page"]) for c in outline["chapters"]]
    sections += [(a["slug"].replace("app-", ""), a["start_page"], a["end_page"])
                 for a in outline.get("appendices", []) if a["slug"] != "app-a1-steam-tables"]
    sections += [(b["slug"][:12], b["start_page"], b["end_page"]) for b in outline.get("back", [])]

    rows, missed_all = [], []
    for name, first, last in sections:
        seg = "\n".join(pages[first - 1: last])
        total = missing = 0
        missed = []
        for s in sentences(seg):
            total += 1
            sh = shingles(s)
            hit = len(sh & md_shingles) / max(len(sh), 1)
            if hit < 0.34:                              # essentially absent
                missing += 1
                missed.append(s)
        rows.append((name, total, missing))
        missed_all.append((name, missed))

    print(f"{'section':>14} {'sentences':>10} {'missing':>8} {'coverage':>9}")
    gt = gm = 0
    for n, total, missing in rows:
        gt += total; gm += missing
        print(f"{n:>14} {total:>10} {missing:>8} {100*(1-missing/max(total,1)):>8.1f}%")
    print(f"{'ALL':>14} {gt:>10} {gm:>8} {100*(1-gm/max(gt,1)):>8.1f}%")

    if len(sys.argv) > 1:
        want = sys.argv[1]
        for n, missed in missed_all:
            if n == want:
                print(f"\n-- chapter {n}: {len(missed)} sentences with no match --")
                for s in missed[:60]:
                    print("  ", s[:150])

if __name__ == "__main__":
    main()
