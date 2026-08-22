"""Assemble the extracted block stream into a MyST Markdown book.

Reads ``build/document.json`` (written by ``extract.py`` and annotated by
``render_figures.py``) and writes chapter/appendix/front/back Markdown from
``outline.json``.
"""

from __future__ import annotations

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import emit
from config import BUILD, OUTLINE, ROOT, load_outline
from textutil import build_vocabulary, fix_ocr, join_lines, slug

FRONT_MATTER = """---
title: "{title}"
short_title: "{short}"
label: {label}
---
"""

HISTORY_START = re.compile(r"^A Bit of History:", re.I)
PROBLEM_NUM = re.compile(r"^(\d+\.\d+)\s*$")
SECTION_HEAD = re.compile(r"^\*{0,2}\d+(?:\.\d+){1,2}\s+")


# --------------------------------------------------------------------------
# block grouping
# --------------------------------------------------------------------------


def chapter_blocks(pages, first, last):
    """All blocks of a page range, with paragraphs rejoined across breaks."""
    out = []
    for page in pages[first:last + 1]:
        page_main = [b for b in page["blocks"] if b["stream"] == "main"]
        for k, block in enumerate(page["blocks"]):
            block = dict(block)
            block["first_main"] = page_main and page_main[0] is page["blocks"][k]
            block["last_main"] = page_main and page_main[-1] is page["blocks"][k]
            out.append(block)
    return out


def merge_across_pages(blocks, right_edge=520.0):
    """Join a paragraph that runs off the bottom of one page onto the next."""
    merged = []
    for block in blocks:
        if merged:
            prev = merged[-1]
            if (prev["kind"] == "text" and block["kind"] == "text"
                    and prev["stream"] == "main" and block["stream"] == "main"
                    and prev["container"] == block["container"]
                    and block["page"] == prev["page"] + 1
                    and prev.get("last_main") and block.get("first_main")
                    and not prev.get("note") and not block.get("note")
                    and prev["bbox"][2] >= right_edge - 14
                    and not re.match(r"^\s*(\d{1,3}\.\s|\\?\[\d+\\?\]|[▶•])",
                                     block["lines"][0])):
                prev["lines"] = prev["lines"] + block["lines"]
                prev["bbox"] = block["bbox"]
                prev["page"] = block["page"]
                prev["last_main"] = block.get("last_main")
                continue
        merged.append(block)
    return merged


def _block_text(block):
    return clean_lines(block.get("lines") or [])


def clean_lines(lines):
    return " ".join(line.strip() for line in lines if line and line.strip())


def _is_chapter_toc(block):
    text = _block_text(block)
    if re.search(r"\.\s?\.\s?\.\s?\.", text):
        return True
    stripped = text.strip().strip("*")
    if re.match(r"^\d+(?:\.\d+)+\s+.+\s+\d{1,3}$", stripped):
        return True
    if re.match(r"^\d+\.\d+\s+.+\s+\d{1,3}$", stripped):
        return True
    return False


def _is_running_head(block):
    text = _block_text(block)
    if block["kind"] == "equation" and re.fullmatch(r"Chapter\s*\d+", text.replace(" ", "")):
        return True
    if block["kind"] != "text":
        return False
    return bool(re.match(r"^(\d{1,3}\s+)?Chapter \d+", text)
                or text.startswith("Engineering Thermodynamics")
                or text.startswith("https://"))


def _is_footer(block):
    text = _block_text(block)
    return "thermodynamicsbook.com" in text or "CC-by-sa" in text.lower()


def parse_answers(blocks):
    """Split the Answers section into a dict keyed by problem number."""
    answers = {}
    current = None
    buf = []
    in_answers = False
    for block in blocks:
        text = clean_lines(block.get("lines") or [])
        stripped = text.strip().strip("*").strip()
        if stripped.lower() == "answers":
            in_answers = True
            continue
        if block["kind"] in ("section", "subsection"):
            title = stripped.lower()
            if title.startswith("answer"):
                in_answers = True
                continue
            if in_answers:
                break
        if not in_answers:
            continue
        if block["kind"] in ("caption", "artwork"):
            continue
        first = text.split("\n", 1)[0].strip().strip("*").strip()
        m = PROBLEM_NUM.match(first) or re.match(r"^\*\*(\d+\.\d+)\*\*", first)
        if m:
            if current and buf:
                answers[current] = "\n".join(buf).strip()
            current = m.group(1)
            rest = text[m.end():].strip() if PROBLEM_NUM.match(first) else text[len(m.group(0)):].strip()
            buf = [rest] if rest else []
        elif re.match(r"^\*\*(\d+\.\d+)\*\*", text.strip()):
            m = re.match(r"^\*\*(\d+\.\d+)\*\*", text.strip())
            if current and buf:
                answers[current] = "\n".join(buf).strip()
            current = m.group(1)
            rest = text[m.end():].strip()
            buf = [rest] if rest else []
        elif current:
            buf.append(text)
    if current and buf:
        answers[current] = fix_ocr("\n".join(buf).strip())
    return {k: fix_ocr(v) for k, v in answers.items()}


def strip_answers_section(blocks):
    """Remove the Answers section — answers are folded into exercises."""
    out = []
    in_answers = False
    for block in blocks:
        text = _block_text(block).strip().strip("*").strip()
        if text.lower() == "answers":
            in_answers = True
            continue
        if block["kind"] in ("section", "subsection"):
            title = text.lower()
            if title.startswith("answer"):
                in_answers = True
                continue
            if in_answers:
                in_answers = False
        if in_answers:
            continue
        out.append(block)
    return out


def group_containers(blocks):
    """Collect runs of blocks that share one shaded call-out box."""
    out = []
    i = 0
    while i < len(blocks):
        b = blocks[i]
        if b["stream"] == "main" and b["container"] in (
                "box", "example", "definition", "history"):
            group, j = [b], i + 1
            while j < len(blocks):
                nxt = blocks[j]
                same_box = (nxt["container"] == b["container"]
                            and (nxt["container_rect"] == group[-1]["container_rect"]
                                 or nxt["page"] != group[-1]["page"]))
                if same_box:
                    group.append(nxt)
                    j += 1
                    continue
                break
            out.append(("container", b["container"], group))
            i = j
        else:
            out.append(("block", b))
            i += 1
    return out


def group_history(blocks):
    """Group history sections that start with a title line, not a shaded box."""
    out = []
    i = 0
    while i < len(blocks):
        entry = blocks[i]
        if entry[0] != "block":
            out.append(entry)
            i += 1
            continue
        block = entry[1]
        head = _block_text(block)
        if not HISTORY_START.match(head.strip("*").strip()) or _is_toc_history_ref(block):
            out.append(entry)
            i += 1
            continue
        group = [block]
        j = i + 1
        while j < len(blocks):
            nxt = blocks[j]
            if nxt[0] != "block":
                break
            nb = nxt[1]
            if nb["kind"] in ("section", "subsection"):
                break
            if HISTORY_START.match(_block_text(nb).strip("*").strip()):
                break
            if nb["kind"] == "caption":
                out.append(("history", group))
                out.append(nxt)
                group = []
                j += 1
                continue
            group.append(nb)
            j += 1
        if group:
            out.append(("history", group))
        i = j
    return out


# --------------------------------------------------------------------------
# labels
# --------------------------------------------------------------------------


def collect_labels(files):
    known = set()
    for spec in files:
        known.add(spec["label"])
        for entry in spec["items"]:
            if entry[0] == "container":
                head = " ".join(entry[2][0]["lines"][:1])
                for pattern, prefix in (
                    (r"^\*\*Box\s+((?:[A-D]|\d+)\.\d+):", "box"),
                    (r"^\*\*Definition\s+((?:[A-D]|\d+)\.\d+\.\d+)", "def"),
                    (r"^\*\*Example\s+((?:[A-D]|\d+)\.\d+)", "ex"),
                    (r"^Example\s+((?:[A-D]|\d+)\.\d+)", "ex"),
                ):
                    m = re.match(pattern, head.strip("*").strip())
                    if m:
                        known.add(slug(prefix, m.group(1)))
                continue
            if entry[0] == "history":
                continue
            if entry[0] == "problem":
                head = _block_text(entry[1][0]).strip().strip("*")
                m = re.match(r"^(\d+\.\d+)", head)
                if m:
                    known.add(slug("prob", m.group(1)))
                continue
            block = entry[1]
            if block["kind"] == "caption" and block.get("number"):
                known.add(slug("fig" if block["captionkind"] == "figure" else "tab",
                               block["number"]))
            elif block["kind"] == "equation" and block.get("eqnum"):
                known.add(slug("eq", block["eqnum"]))
            elif block["kind"] in ("section", "subsection"):
                m = emit.SECTION_RE.match(" ".join(block["lines"]).strip())
                if m:
                    known.add(slug("sec", m.group(1)))
        ch = spec.get("number")
        if ch:
            known.add(f"ch-{ch}")
            for n in range(1, 30):
                known.add(slug("prob", f"{ch}.{n}"))
                known.add(slug("ex", f"{ch}.{n}"))
                known.add(slug("hist", f"{ch}-{n}"))
    return known


# --------------------------------------------------------------------------
# per-file writing
# --------------------------------------------------------------------------


def write_body(w, spec):
    for entry in spec["items"]:
        if entry[0] == "container":
            w.container(entry[1], entry[2], None)
            continue
        if entry[0] == "history":
            w.history(entry[1])
            continue
        if entry[0] == "problem":
            text_lines = []
            for b in entry[1]:
                if b.get("kind") == "caption":
                    continue
                text_lines.extend(b.get("lines", []))
            w.problem({"lines": text_lines, "kind": "text", "stream": "main"})
            for b in entry[1]:
                if b.get("kind") == "caption" and b.get("captionkind") == "figure":
                    w.figure(b, indent="   ")
            continue
        block = entry[1]
        kind = block["kind"]
        if kind == "caption" and block["captionkind"] == "figure":
            w.figure(block, indent="   " if w.in_problems else "")
        elif kind == "caption":
            w.table(block, indent="   " if w.in_problems else "")
        elif kind == "artwork":
            w.artwork(block, indent="   " if w.in_problems else "")
        elif block["stream"] == "margin":
            # Two-column problem pages use the margin stream for the right column.
            if w.in_problems and not w.in_answers:
                w.problem(block)
            else:
                w.para(w.text(block["lines"]))
        elif kind == "section":
            w.heading(block, 2)
        elif kind == "subsection":
            w.heading(block, 3)
        elif kind == "equation":
            w.equation(block, indent="   " if w.in_problems else "")
        elif kind in ("part-title", "part-label", "chapter-title"):
            continue
        elif kind == "text":
            raw = w.text(block["lines"]).strip()
            low = raw.lower()
            if low in ("problems", "answers"):
                w.emit(f"## {raw}")
                w.in_problems = low == "problems"
                w.in_answers = low == "answers"
                w.emit()
            elif w.in_problems and not w.in_answers:
                w.problem(block)
            else:
                w.para(w.text(block["lines"]))
        else:
            if w.in_problems and not w.in_answers:
                w.problem(block)
            else:
                w.para(w.text(block["lines"]))


def write_file(spec, known, vocab):
    w = emit.Writer(known, vocab)
    w.chapter_num = spec.get("number")
    w.answers = spec.get("answers") or {}
    w.emit(FRONT_MATTER.format(title=spec["title"].replace('"', "'"),
                               short=spec["short"].replace('"', "'"),
                               label=spec["label"]))
    if spec.get("hero"):
        w.emit(f":::{{figure}} ../images/{spec['hero']}")
        w.emit(":alt: Chapter opening illustration")
        w.emit(":::")
        w.emit()
    w.emit(f"# {spec['heading']}")
    w.emit()
    if spec.get("number"):
        w.emit(f"(ch-{spec['number']})=")
        w.emit()
    style = spec.get("style", "default")
    if style == "steam_tables":
        w.steam_tables(spec)
    elif style == "bibliography":
        w.bibliography(spec["items"])
    elif style == "symbols":
        w.symbols(spec["items"])
    else:
        write_body(w, spec)
    body = "\n".join(w.out)
    body = re.sub(r"\n{3,}", "\n\n", body)
    try:
        from spellcheck import fix_words
        body = fix_words(body)
    except OSError:
        pass
    path = os.path.join(ROOT, spec["path"])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        fh.write(body.rstrip() + "\n")
    return w


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------


def hero_image(blocks):
    for block in blocks:
        if block["kind"] == "artwork" and block.get("image") and block["bbox"][1] < 100:
            return block
    return None


def group_problems(items):
    """Merge a problem header through its body, including the opposite column."""
    out = []
    i = 0
    while i < len(items):
        entry = items[i]
        if entry[0] != "block":
            out.append(entry)
            i += 1
            continue
        block = entry[1]
        text = _block_text(block).strip().strip("*")
        m = re.match(r"^(\d+\.\d+)(?:\s|$)", text)
        if not m:
            out.append(entry)
            i += 1
            continue
        num = m.group(1)
        group = [block]
        j = i + 1
        while j < len(items):
            nxt = items[j]
            if nxt[0] in ("container", "history", "problem"):
                break
            if nxt[0] != "block":
                j += 1
                continue
            nb = nxt[1]
            ntext = _block_text(nb).strip().strip("*")
            nm = re.match(r"^(\d+\.\d+)(?:\s|$)", ntext)
            if nm and nm.group(1) != num:
                break
            if nb["kind"] in ("section", "subsection"):
                break
            if ntext.lower() in ("problems", "answers"):
                break
            group.append(nb)
            j += 1
        out.append(("problem", group))
        i = j
    return out


def _is_pipe_artifact(block):
    lines = block.get("lines") or []
    if lines and lines[0].strip().startswith("|"):
        return True
    if any(ln.strip().startswith("|") for ln in lines):
        return True
    text = _block_text(block)
    return block["kind"] == "text" and text.count("|") >= 2 and len(text) < 500


def _is_toc_history_ref(block):
    text = _block_text(block).strip().strip("*")
    if "A Bit of History" not in text:
        return False
    return bool(re.search(r"\d{1,3}\s*$", text)) or "Measuring the Degree" in text and len(text) < 80


def _is_opener_junk(block, opener_page):
    if block.get("page") != opener_page:
        return False
    text = _block_text(block).strip().strip("*")
    if text in ("*or*", "or"):
        return True
    if text.lower().startswith("chapter ") and "–" in text:
        return True
    if text in ("Fundamental Concepts",) or text.startswith("*or*"):
        return True
    return "Playset" in text or "Thermodynamicist" in text


def _is_attribution_history(block, opener_page=None):
    if block.get("container") != "history":
        return False
    if opener_page is not None and block.get("page") not in (opener_page, opener_page + 1):
        return False
    plain = _block_text(block).strip().strip("*").strip()
    return (plain.startswith("Engineering Thermodynamics")
            and "Olivier Cleynen" in plain and len(plain) < 120)


def prepare_blocks(blocks, opener_page=None):
    blocks = [b for b in blocks
              if not _is_chapter_toc(b) and not _is_running_head(b) and not _is_footer(b)
              and not _is_pipe_artifact(b)
              and not _is_toc_history_ref(b)
              and not _is_attribution_history(b, opener_page)
              and not (opener_page is not None and _is_opener_junk(b, opener_page))
              and not (b["kind"] == "text"
                       and re.match(r"^Chapter \d+ [–-] ", _block_text(b)))]
    answers = parse_answers(blocks)
    blocks = strip_answers_section(blocks)
    blocks = group_containers(blocks)
    flat = []
    for entry in blocks:
        flat.append(entry)
    blocks = group_history(flat)
    blocks = group_problems(blocks)
    return blocks, answers


def build_specs(pages, outline, only_slug=None):
    specs = []
    intro = outline["front"]["introduction"]
    specs.append({
        "path": intro["file"],
        "title": intro["title"],
        "short": intro["title"],
        "label": intro["slug"],
        "heading": intro["title"],
        "first": intro["start_page"] - 1,
        "last": intro["end_page"] - 1,
        "style": "default",
    })
    for ch in outline["chapters"]:
        if only_slug and ch["slug"] != only_slug:
            continue
        specs.append({
            "path": f"chapters/{ch['slug']}.md",
            "title": f"{ch['number']}. {ch['title']}",
            "short": f"Chapter {ch['number']}",
            "label": ch["slug"],
            "heading": f"{ch['number']}. {ch['title']}",
            "number": ch["number"],
            "first": ch["start_page"] - 1,
            "last": ch["end_page"] - 1,
            "style": "default",
        })
    if not only_slug:
        for ap in outline["appendices"]:
            aid = ap["id"].lower()
            style = "steam_tables" if ap["id"] == "A1" else "default"
            specs.append({
                "path": f"appendices/{ap['slug']}.md",
                "title": f"{ap['id']}. {ap['title']}",
                "short": f"Appendix {ap['id']}",
                "label": ap["slug"],
                "heading": f"{ap['id']}. {ap['title']}",
                "first": ap["start_page"] - 1,
                "last": ap["end_page"] - 1,
                "style": style,
            })
        for back in outline["back"]:
            style = "bibliography" if back["slug"] == "bibliography" else \
                "symbols" if back["slug"] == "list-of-symbols" else "default"
            specs.append({
                "path": f"back/{back['slug']}.md",
                "title": back["title"],
                "short": back["title"],
                "label": back["slug"],
                "heading": back["title"],
                "first": back["start_page"] - 1,
                "last": back["end_page"] - 1,
                "style": style,
            })
    for spec in specs:
        blocks = chapter_blocks(pages, spec["first"], spec["last"])
        blocks = merge_across_pages(blocks)
        hero = hero_image(blocks)
        if hero:
            spec["hero"] = hero["image"]
            blocks = [b for b in blocks if b is not hero]
            # drop subtitle/type lines on the chapter opener page
            opener = spec["first"]
            blocks = [b for b in blocks
                      if not (b["page"] == opener and b["kind"] in ("text", "equation")
                              and b.get("bbox", [0, 999])[1] < 220)]
        blocks, answers = prepare_blocks(blocks, opener_page=spec.get("first"))
        spec["answers"] = answers
        spec["items"] = blocks
        if spec.get("style") == "steam_tables":
            spec["steam_pages"] = list(range(spec["first"], spec["last"] + 1))
    return specs


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapter", help="Only build this chapter slug (pilot QA)")
    args = parser.parse_args()

    outline = load_outline()
    data = json.load(open(os.path.join(BUILD, "document.json")))
    pages = data["pages"]
    vocab = build_vocabulary(pages)
    specs = build_specs(pages, outline, only_slug=args.chapter)
    known = collect_labels(specs)
    known |= {f"ref-{n}" for n in range(1, 400)}
    stats = []
    for spec in specs:
        w = write_file(spec, known, vocab)
        stats.append((spec["path"], len(w.out), len(w.answers)))
    for path, n, ans in stats:
        print(f"  {path:52s} {n:5d} lines  {ans:3d} answers")
    print(f"wrote {len(specs)} files")


if __name__ == "__main__":
    main()
