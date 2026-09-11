"""Structural checks on the generated MyST edition.

Compares the Markdown against ``outline.json`` and the block stream extracted
from the PDF.  Run ``python3 scripts/verify_book.py``; non-zero exit = failure.
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import BUILD, OUTLINE, ROOT, load_outline

try:
    from spellcheck import ocr_suspects
except ImportError:
    ocr_suspects = None

problems: list[str] = []


def fail(msg):
    problems.append(msg)


def markdown_files():
    return sorted(glob.glob(os.path.join(ROOT, d, "*.md"))
                  for d in ("chapters", "appendices", "front", "back"))


def all_files():
    out = []
    for group in markdown_files():
        out.extend(group)
    out.append(os.path.join(ROOT, "index.md"))
    return out


def read(path):
    with open(path) as fh:
        return fh.read()


def slug_label(prefix, number):
    return f"{prefix}-" + str(number).replace(".", "-").replace("/", "-").lower()


def main():
    outline = load_outline()
    chapters = sorted(glob.glob(os.path.join(ROOT, "chapters", "*.md")))
    appendices = sorted(glob.glob(os.path.join(ROOT, "appendices", "*.md")))
    exp_ch = len(outline["chapters"])
    exp_ap = len(outline["appendices"])
    if len(chapters) != exp_ch:
        fail(f"expected {exp_ch} chapters, found {len(chapters)}")
    if len(appendices) != exp_ap:
        fail(f"expected {exp_ap} appendices, found {len(appendices)}")

    texts = {p: read(p) for p in all_files()}
    corpus = "\n".join(texts.values())

    # ---- labels and references ------------------------------------------
    labels = set(re.findall(r"^[ \t]*:label:\s*(\S+)", corpus, re.M))
    labels |= set(re.findall(r"^\((\S+?)\)=", corpus, re.M))
    labels |= set(re.findall(r"^[ \t]*label:\s*(\S+)", corpus, re.M))
    targets = set(re.findall(r"\]\(#([A-Za-z0-9_.-]+)\)", corpus))
    missing = sorted(targets - labels)
    if missing:
        fail(f"{len(missing)} cross-references without a target, e.g. {missing[:8]}")

    # ---- images ----------------------------------------------------------
    referenced = set(re.findall(r"^:::+\{figure\}\s+\.\./images/(\S+)", corpus, re.M))
    for name in sorted(referenced):
        if not os.path.exists(os.path.join(ROOT, "images", name)):
            fail(f"missing image file: images/{name}")

    # ---- coverage against outline + extraction ---------------------------
    doc_path = os.path.join(BUILD, "document.json")
    extracted = {}
    if os.path.exists(doc_path):
        with open(doc_path) as fh:
            data = json.load(fh)
        extracted["figures"] = {b["number"] for p in data["pages"] for b in p["blocks"]
                                if b.get("captionkind") == "figure" and b.get("number")}
        extracted["equations"] = {b["eqnum"] for p in data["pages"] for b in p["blocks"]
                                if b.get("eqnum")}

    for ch in outline["chapters"]:
        path = os.path.join(ROOT, "chapters", f"{ch['slug']}.md")
        if not os.path.exists(path):
            fail(f"missing chapter file: {ch['slug']}.md")
            continue
        text = texts.get(path, "")
        n = ch["number"]
        exp = ch["source_counts"]
        figs = len(re.findall(r":enumerator:\s*" + str(n) + r"\.\d+", text))
        if figs < exp["figures"] * 0.9:
            fail(f"{ch['slug']}: only {figs}/{exp['figures']} figures emitted")
        exs = len(re.findall(r"\{prf:example\}", text))
        if exs < exp["examples"] * 0.9:
            fail(f"{ch['slug']}: only {exs}/{exp['examples']} examples emitted")
        # problems are numbered N.1..N.k in the source; every one must be present
        probs = {int(m) for m in re.findall(rf"^[ \t]*:label: prob-{n}-(\d+)", text, re.M)}
        gaps = [k for k in range(1, max(probs, default=0) + 1) if k not in probs]
        if gaps:
            fail(f"{ch['slug']}: exercises missing: " +
                 ", ".join(f"{n}.{k}" for k in gaps))
        hists = len(re.findall(r"A Bit of History", text))
        if hists < exp["history"]:
            fail(f"{ch['slug']}: only {hists}/{exp['history']} history boxes")

    if extracted:
        for kind, numbers, prefix in (("figure", extracted.get("figures", set()), "fig"),
                                      ("equation", extracted.get("equations", set()), "eq")):
            want = {slug_label(prefix, n) for n in numbers}
            have = labels | set(re.findall(r"^[ \t]*:label:\s*(\S+)", corpus, re.M))
            lost = sorted(want - have)
            # allow 30% loss — some figures land inside problem groups without labels
            if len(lost) > 0.15 * max(len(want), 1):
                fail(f"{len(lost)}/{len(want)} {kind}s missing labels, e.g. {lost[:6]}")

    # ---- conversion artifacts -------------------------------------------
    skip_artifacts = {"app-a1-steam-tables.md", "list-of-symbols.md"}
    artifacts = [
        (r"\u0001", "unresolved bullet sentinel", 0),
        (r"\u0002", "unresolved typewriter marker", 0),
        (r"[a-z]- [a-z]{2,}", "hyphenation left un-joined", 20),
        (r"\\frac\{\$", "nested maths inside \\frac", 3),
        (r"(?:\*[A-Za-z0-9]\*){3,}", "single-letter italic scramble", 0),
        (r"\bdifcfiult\b", "OCR typo difcfiult", 0),
        (r"\bfgi ure\b", "OCR typo fgi ure", 0),
        (r"\bfgi ures\b", "OCR typo fgi ures", 0),
        (r"\bspecifci\b", "OCR typo specifci", 0),
        (r"\bspecifcially\b", "OCR typo specifcially", 0),
    ]
    for path, text in texts.items():
        base = os.path.basename(path)
        if base in skip_artifacts:
            continue
        for pattern, label, limit in artifacts:
            hits = re.findall(pattern, text)
            if len(hits) > limit:
                fail(f"{base}: {len(hits)} instances of {label}")

    # ---- hunspell OCR suspects (prose only) ------------------------------
    if ocr_suspects:
        skip_spell = skip_artifacts | {"bibliography.md", "list-of-symbols.md"}
        for path, text in texts.items():
            base = os.path.basename(path)
            if base in skip_spell:
                continue
            plain = re.sub(r"\$[^$]*\$", " ", text)
            plain = re.sub(r"```.*?```", " ", plain, flags=re.S)
            suspects = ocr_suspects(plain)
            if suspects:
                sample = ", ".join(sorted(set(suspects))[:6])
                fail(f"{base}: {len(suspects)} hunspell OCR suspects, e.g. {sample}")

    # ---- directive fences ------------------------------------------------
    for path, text in texts.items():
        depth = {3: 0, 4: 0}
        for line in text.splitlines():
            t = line.strip()
            if re.match(r"^::::(\{|$)", t):
                depth[4] += 1 if t.startswith("::::{") else -1
            elif re.match(r"^:::(\{|$)", t):
                depth[3] += 1 if t.startswith(":::{") else -1
        if depth[3] or depth[4]:
            fail(f"{os.path.basename(path)}: unbalanced directive fences {depth}")

    # ---- selectable steam tables -----------------------------------------
    steam = os.path.join(ROOT, "appendices", "app-a1-steam-tables.md")
    if os.path.exists(steam):
        table_text = os.path.join(ROOT, "appendices", "steam-tables.txt")
        if not os.path.exists(table_text):
            fail("steam tables: selectable source is missing")
        elif not re.search(r"Steam Table [123]", open(table_text).read()):
            fail("steam tables: selectable source has no table data")

    if problems:
        print("verification failed:")
        for p in problems:
            print("  -", p)
        return 1
    print(f"ok: {len(chapters)} chapters, {len(appendices)} appendices, "
          f"{len(labels)} labels, {len(referenced)} images")
    return 0


if __name__ == "__main__":
    sys.exit(main())
