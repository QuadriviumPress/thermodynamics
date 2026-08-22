"""Markdown emission for :mod:`build_book`."""

from __future__ import annotations

import re

from textutil import fix_ocr, join_lines, link_references, slug

BULLET_TOKEN = "\u0001BULLET\u0001"
MONO_MARK = "\u0002"
NBSP = "\u00a0"

SECTION_RE = re.compile(r"^\*{0,2}(\d+(?:\.\d+){1,2})\s+(.*?)\*{0,2}$")
BOX_TITLE = re.compile(r"^\*\*Box\s+((?:[A-D]|\d+)\.\d+):\s*(.*?)\*\*\s*")
DEF_HEAD = re.compile(r"^\*\*Definition\s+((?:[A-D]|\d+)\.\d+\.\d+)\s*(.*?)\*\*\s*:?\s*")
EX_HEAD = re.compile(r"^\*\*Example\s+((?:[A-D]|\d+)\.\d+)\s*(.*?)\*\*\s*:?\s*")
EX_HEAD_PLAIN = re.compile(r"^Example\s+((?:[A-D]|\d+)\.\d+)\s*(.*?)\s*$")
HISTORY_HEAD = re.compile(r"^(A Bit of History:)\s*(.*?)\s*$")
CAP_PREFIX = re.compile(r"^\*\*(Figure|Table)\s+((?:[A-D]|\d+)\.\d+):\*\*\s*")
CAP_PREFIX_PLAIN = re.compile(r"^(Figure|Table)\s+((?:[A-D]|\d+)\.\d+):\s*")
MARGIN_NOTE = re.compile(r"^(\d{1,3}):\s*")
PROBLEM_NUM = re.compile(r"^(\d+\.\d+)\s*$")
PROBLEM_HEAD = re.compile(r"^(\d+\.\d+)\s+(.+)$")
PROBLEM_BOLD = re.compile(r"^\*\*(\d+\.\d+)\*\*")
PROBLEM_ITEM = re.compile(r"^(\d{1,3})\.\s+")


def _mono_run(text):
    """Collapse a typewriter run: URLs lose the spaces justification added."""
    lead = " " if text[:1].isspace() else ""
    trail = " " if text[-1:].isspace() else ""
    body = re.sub(r"\s+", "", text)
    if not body:
        return lead or trail
    if re.match(r"^https?://", body):
        inner = f"<{body}>"
    elif re.match(r"^10\.\d{4,}/", body):
        inner = f"[{body}](https://doi.org/{body})"
    else:
        inner = f"`{body}`"
    return lead + inner + trail


def clean(text):
    text = text.replace(NBSP, " ")
    text = re.sub(MONO_MARK + r"\s*" + MONO_MARK, "", text)
    text = re.sub(MONO_MARK + r"([^" + MONO_MARK + r"]*)" + MONO_MARK,
                  lambda m: _mono_run(m.group(1)), text)
    text = text.replace(MONO_MARK, "")
    text = text.replace("****", "")
    text = re.sub(r"(?<!\\)\$\$", "", text)
    text = re.sub(r"(?<!\\)\$ \$", " ", text)
    text = re.sub(r"(?<=\$)\s+(?=\$)", " ", text)
    text = re.sub(r"\*\*\s+\*\*", " ", text)
    text = re.sub(r"(?<!\*)\*\s+\*(?!\*)", " ", text)
    text = re.sub(r"\$\s+\$", " ", text)
    text = re.sub(r"\$\^\{\s*\}\$", "", text)
    text = re.sub(r"\$\_\{\s*\}\$", "", text)
    text = re.sub(r"\.\s\.\s\.(\s|$)", "\u2026\\1", text)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return fix_ocr(text.strip())


def container_head(container, head):
    """Split a call-out's opening line into (title, label, class, remainder)."""
    if container == "history":
        m = HISTORY_HEAD.match(head.strip("*").strip())
        if m:
            title = m.group(1) + " " + m.group(2).strip()
            num = re.search(r"hist-(\d+-\d+)", head)  # placeholder
            return (title.strip(), None, "note", head[len(m.group(0)):])
        return ("A Bit of History", None, "note", head)
    if container == "box":
        m = BOX_TITLE.match(head)
        if m:
            return (f"Box {m.group(1)}: {m.group(2)}", slug("box", m.group(1)),
                    "tip", head[m.end():])
        return ("Box", None, "tip", head)
    if container == "definition":
        m = DEF_HEAD.match(head)
        if m:
            title = f"Definition {m.group(1)}"
            term = m.group(2).strip().strip(":").strip()
            if term:
                title += f" — {term}"
            return (title, slug("def", m.group(1)), "important", head[m.end():])
        return ("Definition", None, "important", head)
    m = EX_HEAD.match(head) or EX_HEAD_PLAIN.match(head.strip("*").strip())
    if m:
        extra = m.group(2).strip().strip(":").strip()
        title = f"Example {m.group(1)}"
        if extra:
            title += f" — {extra}"
        rest = head[m.end():].lstrip(": ")
        return (title, slug("ex", m.group(1)), "example", rest)
    return ("Example", None, "example", head)


class Writer:
    """Accumulates the Markdown for one output file."""

    def __init__(self, known, vocab):
        self.known = known
        self.vocab = vocab
        self.out = []
        self.footnotes = {}
        self.in_problems = False
        self.in_answers = False
        self.used = set()
        self.note_anchors = {}
        self.answers = {}
        self.history_count = 0
        self.chapter_num = None

    def text(self, lines):
        return clean(join_lines(lines, self.vocab))

    def emit(self, s=""):
        self.out.append(s)

    def label(self, name):
        if not name or name in self.used:
            return None
        self.used.add(name)
        return name

    def para(self, text, indent=""):
        text = link_references(text, self.known)
        chunks = [c.strip() for c in text.split(BULLET_TOKEN)]
        lead, items = chunks[0], [c for c in chunks[1:] if c]
        if lead:
            self.emit(indent + lead)
            self.emit()
        for item in items:
            wrapped = ("\n" + indent + "  ").join(item.split("\n"))
            self.emit(indent + "- " + wrapped)
        if items:
            self.emit()

    def heading(self, block, depth):
        raw = self.text(block["lines"]).strip("*").strip()
        m = SECTION_RE.match(raw)
        if m:
            number, title = m.group(1), m.group(2).strip("*").strip()
            name = self.label(slug("sec", number))
            if name:
                self.emit(f"({name})=")
            self.emit(f"{'#' * depth} {number} {title}")
            low = title.lower()
            self.in_problems = low.startswith("problem") and "answer" not in low
            self.in_answers = low.startswith("answer")
        else:
            self.emit(f"{'#' * depth} {raw}")
            low = raw.lower()
            self.in_problems = low.startswith("problem") and "answer" not in low
            self.in_answers = low.startswith("answer")
        self.emit()

    def equation(self, block, indent=""):
        body = " ".join(block["lines"]).strip()
        body = re.sub(r"^\$|\$$", "", body).strip()
        body = re.sub(r"\s+", " ", body.replace("$", " ")).strip()
        body = fix_ocr(body)
        name = self.label(slug("eq", block["eqnum"])) if block.get("eqnum") else None
        pad = indent
        self.emit(pad + ":::{math}")
        if name:
            self.emit(pad + f":label: {name}")
            self.emit(pad + f":enumerator: {block['eqnum']}")
        self.emit(pad + body)
        self.emit(pad + ":::")
        self.emit()

    def figure(self, block, indent=""):
        caption = self.text(block["lines"])
        m = CAP_PREFIX.match(caption) or CAP_PREFIX_PLAIN.match(caption)
        caption = caption[m.end():] if m else caption
        caption = link_references(caption, self.known)
        name = self.label(slug("fig", block["number"]))
        image = block.get("image")
        if not image:
            return
        self.emit(indent + f":::{{figure}} ../images/{image}")
        if name:
            self.emit(indent + f":label: {name}")
            self.emit(indent + f":enumerator: {block['number']}")
        self.emit(indent + f":alt: {_alt_text(caption)}")
        self.emit(indent)
        self.emit(indent + caption)
        self.emit(indent + ":::")
        self.emit()

    def artwork(self, block, indent=""):
        image = block.get("image")
        if not image:
            return
        self.emit(indent + f":::{{figure}} ../images/{image}")
        self.emit(indent + ":alt: Illustration from the original text")
        self.emit(indent + ":::")
        self.emit()

    def table(self, block, indent=""):
        rows = block.get("rows") or []
        if not block.get("number"):
            if rows and all(len(r.get("cells") or []) <= 1 for r in rows):
                for r in rows:
                    cell = " ".join(c for c in (r.get("cells") or []) if c).strip()
                    if cell:
                        self.para(link_references(clean(cell), self.known), indent=indent)
                return
            self._table_body(rows, indent)
            return
        caption = self.text(block["lines"])
        m = CAP_PREFIX.match(caption) or CAP_PREFIX_PLAIN.match(caption)
        caption = caption[m.end():] if m else caption
        caption = link_references(caption, self.known)
        name = self.label(slug("tab", block["number"]))
        self.emit(indent + ":::{table} " + caption)
        if name:
            self.emit(indent + f":label: {name}")
            self.emit(indent + f":enumerator: {block['number']}")
        self.emit(indent)
        self._table_body(rows, indent, fenced=False)
        self.emit(indent + ":::")
        self.emit()

    def _table_body(self, rows, indent="", fenced=True):
        if rows:
            width = max(len(r["cells"]) for r in rows)
            head = [r for r in rows if r["header"]]
            body = [r for r in rows if not r["header"]]
            if not head:
                head, body = rows[:1], rows[1:]
            merged = [""] * width
            for r in head:
                for k, cell in enumerate(r["cells"]):
                    if cell:
                        merged[k] = (merged[k] + " " + cell).strip()
            self.emit(indent + "| " + " | ".join(_cell(c) for c in merged) + " |")
            self.emit(indent + "|" + "|".join([" --- "] * width) + "|")
            for r in body:
                cells = r["cells"] + [""] * (width - len(r["cells"]))
                self.emit(indent + "| " + " | ".join(_cell(c) for c in cells) + " |")
        if fenced:
            self.emit()

    def container(self, kind, group, page_width_right):
        head = clean(" ".join(group[0]["lines"][:1]))
        title, name, cls, remainder = container_head(kind, head)
        if kind == "example":
            self._example_block(group, head, name)
            return
        if kind == "history":
            self.history_count += 1
            ch = self.chapter_num or 0
            name = self.label(slug("hist", f"{ch}-{self.history_count}"))
        self.emit(f"::::{{admonition}} {title}")
        self.emit(f":class: {cls}")
        name = self.label(name) if name else None
        if name:
            self.emit(f":label: {name}")
        self.emit()
        first = True
        for block in group:
            lines = block["lines"][:]
            if first:
                lines = [remainder] + lines[1:] if remainder else lines[1:]
                first = False
            if block["kind"] == "equation":
                self.equation(block)
                continue
            body = self.text(lines)
            if body:
                self.para(body)
        self.emit("::::")
        self.emit()

    def _example_block(self, group, head, name):
        m = EX_HEAD.match(head) or EX_HEAD_PLAIN.match(head.strip("*").strip())
        number = m.group(1) if m else None
        name = self.label(slug("ex", number)) if number else None
        self.emit("````{prf:example}")
        if name:
            self.emit(f":label: {name}")
        if number:
            self.emit(f":enumerator: {number}")
        self.emit()
        first = True
        for block in group:
            lines = block["lines"][:]
            if first:
                _, _, _, remainder = container_head("example", head)
                lines = [remainder] + lines[1:] if remainder else lines[1:]
                first = False
            if block["kind"] == "equation":
                self.equation(block)
                continue
            body = self.text(lines)
            if body:
                self.para(body)
        self.emit("````")
        self.emit()

    def margin(self, block):
        body = self.text(block["lines"])
        if not body:
            return
        self.emit(":::{margin}")
        self.para(body)
        self.emit(":::")
        self.emit()

    def problem(self, block):
        if self.in_answers:
            return
        body = self.text(block["lines"])
        first_line = body.split("\n", 1)[0].strip()
        m = PROBLEM_NUM.match(first_line) or PROBLEM_HEAD.match(first_line) \
            or PROBLEM_BOLD.match(first_line)
        if m:
            num = m.group(1)
            if PROBLEM_HEAD.match(first_line):
                title = m.group(2).strip()
                rest = body.split("\n", 1)[1].strip() if "\n" in body else ""
            elif PROBLEM_BOLD.match(first_line):
                title = ""
                rest = body[m.end():].strip()
            else:
                rest = body[m.end():].strip()
                lines = rest.split("\n", 1)
                title = lines[0].strip()
                rest = lines[1].strip() if len(lines) > 1 else ""
            label = self.label(slug("prob", num))
            self.emit("```{exercise}")
            if label:
                self.emit(f":label: {label}")
            self.emit(f":enumerator: {num}")
            self.emit()
            if title:
                self.emit(f"**{title}**")
                self.emit()
            if rest:
                self.para(link_references(rest, self.known))
            answer = self.answers.get(num)
            if answer:
                self.emit(":::{admonition} Answer")
                self.emit(":class: dropdown")
                self.emit()
                self.para(link_references(clean(answer), self.known))
                self.emit(":::")
            self.emit("```")
            self.emit()
            return
        m = PROBLEM_ITEM.match(body)
        if not m:
            self.para(body, indent="")
            return
        rest = link_references(body[m.end():], self.known)
        rest = rest.replace(BULLET_TOKEN, "\n- ")
        self.emit(f"{m.group(1)}. {rest}")
        self.emit()

    def history(self, group):
        """Emit a history box grouped by title detection."""
        group = [b for b in group if b.get("lines")]
        if not group:
            return
        self.history_count += 1
        ch = self.chapter_num or 0
        name = self.label(slug("hist", f"{ch}-{self.history_count}"))
        head = clean(" ".join(group[0]["lines"][:1]))
        m = HISTORY_HEAD.match(head.strip("*").strip())
        title = (m.group(1) + " " + m.group(2)).strip() if m else head
        self.emit(f"::::{{admonition}} {title}")
        self.emit(":class: note")
        if name:
            self.emit(f":label: {name}")
        self.emit()
        first = True
        for block in group:
            lines = block["lines"][:]
            if first:
                lines = lines[1:]
                first = False
            if block["kind"] == "equation":
                self.equation(block)
                continue
            body = self.text(lines)
            if body:
                self.para(body)
        self.emit("::::")
        self.emit()


def _alt_text(caption):
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", caption)
    text = re.sub(r"\$[^$]*\$", "", text)
    text = re.sub(r"[*`_<>]", "", text).replace("\u2013", "-").replace("\u2014", "-")
    text = re.sub(r"\s+", " ", text).strip()
    return text[:140].rstrip(" ,;:")


def _cell(text):
    text = (text or "").replace("|", "\\|").strip()
    if text in ("$...$", "$\\ldots$", "..."):
        text = "\u22ee"
    return text or " "


# --------------------------------------------------------------------------
# back-matter styles
# --------------------------------------------------------------------------

BIB_ENTRY = re.compile(r"^\\?\[(\d+)\\?\]\s*")
CITED_ON = re.compile(r"\s*\(cited on pages?\s+[^)]*\)\.?")
PAGE_TAIL = re.compile(
    r"\s+\d{1,3}(?:[–-]\d{1,3})?(?:,\s*\d{1,3}(?:[–-]\d{1,3})?)*\.?\s*$")
URL = re.compile(r"(?<![<\(\[])(https?://[^\s,)\]<>]+[^\s,.)\];<>])")
DOI = re.compile(r"\bdoi:\s*(10\.\d{4,}/\S+?)(?=[\s,)]|$)")


def linkify(text):
    text = DOI.sub(lambda m: f"doi: [{m.group(1)}](https://doi.org/{m.group(1)})", text)
    return URL.sub(lambda m: f"<{m.group(1)}>", text)


def _bib_writer(self, items):
    self.emit("References are numbered in order of first appearance in the book.")
    self.emit()
    pending = []
    started = False

    def flush():
        if not pending:
            return
        body = clean(join_lines(pending, self.vocab))
        m = BIB_ENTRY.match(body)
        if not m:
            self.emit(linkify(body))
            self.emit()
            pending.clear()
            return
        number = m.group(1)
        rest = CITED_ON.sub("", body[m.end():]).strip()
        self.emit(f"({slug('ref', number)})=")
        self.emit(f"**[{number}]**  " + linkify(rest))
        self.emit()
        pending.clear()

    for entry in items:
        if entry[0] != "block":
            continue
        block = entry[1]
        if block["kind"] in ("caption", "artwork"):
            continue
        lines = block.get("lines") or []
        if not lines:
            continue
        if BIB_ENTRY.match(lines[0].strip()):
            flush()
            started = True
        if not started:
            continue
        pending.extend(lines)
    flush()


def _symbols_writer(self, items):
    self.emit("Symbols used throughout the book, as defined in the original edition.")
    self.emit()
    for entry in items:
        if entry[0] != "block":
            continue
        block = entry[1]
        if block["kind"] in ("caption", "artwork") or not block.get("lines"):
            continue
        body = clean(join_lines(block["lines"], self.vocab))
        if body:
            self.para(link_references(body, self.known))


Writer.bibliography = _bib_writer
Writer.symbols = _symbols_writer


def _steam_tables_writer(self, spec):
    self.emit(
        "The thermodynamic properties of water across a wide range of pressures and "
        "temperatures, from the NIST IAPWS-1995 model. The tables below are page "
        "images from the original PDF for numerical fidelity."
    )
    self.emit()
    for pno in spec.get("steam_pages") or []:
        name = f"steam-table-p{pno + 1:03d}.png"
        self.emit(f":::{{figure}} ../images/{name}")
        self.emit(f":alt: Steam tables page {pno + 1}")
        self.emit(":::")
        self.emit()


Writer.steam_tables = _steam_tables_writer
