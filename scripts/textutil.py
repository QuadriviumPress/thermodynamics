"""Shared text helpers for assembling the MyST edition."""

from __future__ import annotations

import collections
import re

# --------------------------------------------------------------------------
# text tidying
# --------------------------------------------------------------------------

MATH_SPLIT = re.compile(r"(\$[^$]*\$)")


def outside_math(text, fn):
    """Apply ``fn`` to the prose of ``text``, leaving maths untouched."""
    return "".join(part if part.startswith("$") and part.endswith("$") else fn(part)
                   for part in MATH_SPLIT.split(text))


def build_vocabulary(pages):
    """Count every word that is not touched by a line break."""
    words = collections.Counter()
    for page in pages:
        for block in page["blocks"]:
            for line in block.get("lines", []):
                plain = outside_math(line, lambda s: s)
                plain = MATH_SPLIT.sub(" ", plain)
                tokens = re.findall(r"[A-Za-z][A-Za-z'’-]*", plain)
                for k, tok in enumerate(tokens):
                    if k == len(tokens) - 1 and plain.rstrip().endswith("-"):
                        continue
                    words[tok.lower()] += 1
    return words


def join_lines(lines, vocab):
    """Glue a paragraph's lines back together, undoing hyphenation."""
    out = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if not out:
            out = line
            continue
        m = re.search(r"([A-Za-z’']+)-(\*{1,3})?$", out)
        n = re.match(r"(\*{1,3})?([A-Za-z’']+)", line)
        if m and n:
            left, right = m.group(1), n.group(2)
            marks = len(m.group(2) or "")
            merged = (left + right).lower()
            kept = (left + "-" + right).lower()
            tail = len(n.group(1) or "")
            head = out[: len(out) - marks]
            rest = line[tail:]
            if vocab[kept] > 0 or (vocab[merged] == 0
                                   and vocab[left.lower()] > 2 and vocab[right.lower()] > 2):
                out = head + rest        # a genuine hyphenated compound
            else:
                out = head[:-1] + rest   # TeX broke the word across lines
            continue
        out += " " + line
    return out


# --------------------------------------------------------------------------
# OCR / extraction artifact repair (Libertinus PDF fi↔if transpositions)
# --------------------------------------------------------------------------

_OCR_REPLACEMENTS = [
    (r"\bdifcfiult\b", "difficult"),
    (r"\bfgi ures\b", "figures"),
    (r"\bFgi ures\b", "Figures"),
    (r"\bfgi ure\b", "figure"),
    (r"\bFgi ure\b", "Figure"),
    (r"\bconfgi ured\b", "configured"),
    (r"\bmodifciations\b", "modifications"),
    (r"\bsignifciant\b", "significant"),
    (r"\bfni d\b", "find"),
    (r"\bspecifcially\b", "specifically"),
    (r"\binefcfiient\b", "inefficient"),
    (r"\bquantifeid\b", "quantified"),
    (r"\bdifcfiulty\b", "difficulty"),
    (r"\bdifcfiulties\b", "difficulties"),
    (r"\bconfgi ure\b", "configure"),
    (r"\bconfgi ured\b", "configured"),
    (r"\bconfgi gured\b", "configured"),
    (r"\bmodifciation\b", "modification"),
    (r"\bdifcfiulties\b", "difficulties"),
    (r"\bconstructive difcfiulties\b", "constructive difficulties"),
    (r"\$29 a nd \$", "$29 and $"),
    (r"\bPowerdecreases\b", "Power decreases"),
    (r"\batmo-\s*sphere\b", "atmosphere"),
    (r"\bspecifci\b", "specific"),
    (r"\bSpecifci\b", "Specific"),
    (r"\bfrist\b", "first"),
    (r"\bFrist\b", "First"),
    (r"\becfiiency\b", "efficiency"),
    (r"\becfiiencies\b", "efficiencies"),
    (r"\bfni al\b", "final"),
    (r"\bful id\b", "fluid"),
    (r"\bful ids\b", "fluids"),
    (r"\bfol w\b", "flow"),
    (r"\bFol w\b", "Flow"),
    (r"\bscientifci\b", "scientific"),
    (r"\bstifnf ess\b", "stiffness"),
    (r"\bsimplifeid\b", "simplified"),
    (r"\bdifefrence\b", "difference"),
    (r"\bdifefrent\b", "different"),
    (r"\bfxied\b", "fixed"),
    (r"\bidentifaible\b", "identifiable"),
    (r"\bidentifaiability\b", "identifiability"),
    (r"\bquantifaiability\b", "quantifiability"),
    (r"\bTechnol-\s*ogy\b", "Technology"),
    (r"\bfol-\s*lowed\b", "followed"),
    (r"\bfol-\s*lowing\b", "following"),
    (r"\bcon-\s*denser\b", "condenser"),
    (r"\bdis-\s*si-\s*pates\b", "dissipates"),
    (r"\bdis-\s*si-\s*pated\b", "dissipated"),
    (r"\bman-\s*ufacturing\b", "manufacturing"),
    (r"\bexper-\s*imenter\b", "experimenter"),
    (r"\bexper-\s*iment\b", "experiment"),
    (r"\bchar-\s*acteristics\b", "characteristics"),
    (r"\bther-\s*mometer\b", "thermometer"),
    (r"\bvisu-\s*al\b", "visual"),
    (r"\bvisu-\s*alization\b", "visualization"),
    (r"\bcent-\s*ury\b", "century"),
    (r"\bcent-\s*uries\b", "centuries"),
    (r"\bmeas-\s*ure\b", "measure"),
    (r"\bmeas-\s*urement\b", "measurement"),
    (r"\bmeas-\s*urements\b", "measurements"),
    (r"\btem-\s*perature\b", "temperature"),
    (r"\btem-\s*peratures\b", "temperatures"),
    (r"\brep-\s*resent\b", "represent"),
    (r"\brep-\s*resented\b", "represented"),
    (r"\brep-\s*resents\b", "represents"),
    (r"\brep-\s*resentation\b", "representation"),
    (r"\bcom-\s*pressor\b", "compressor"),
    (r"\bcom-\s*pressed\b", "compressed"),
    (r"\bcom-\s*pression\b", "compression"),
    (r"\bexpan-\s*sion\b", "expansion"),
    (r"\bexpan-\s*ded\b", "expanded"),
    (r"\bthermo-\s*dynamic\b", "thermodynamic"),
    (r"\bthermo-\s*dynamics\b", "thermodynamics"),
    (r"\bmass-specifci\b", "mass-specific"),
    (r"\bmass specifci\b", "mass specific"),
    (r"\bspecif-\s*ic\b", "specific"),
    (r"\bSI\s+unit\b", "SI unit"),
    (r"\bsi unit\b", "SI unit"),
    (r"\bjoule per second\b", "joule per second"),
    (r"\$joule per second\$\b", "joule per second"),
    # split-word Libertinus transpositions (space inserted mid-word)
    (r"\bdefni\s+e\b", "define"),
    (r"\bdefni\s+ed\b", "defined"),
    (r"\bdefni\s+ite\b", "definite"),
    (r"\*\*defni\s+e\*\*", "**define**"),
    (r"\*defni\s+e\*", "*define*"),
    (r"\beffecfollows\b", "follows"),
    (r"\bexpansignifciant\b", "expansion significant"),
    (r"\bfolw\b", "flow"),
    (r"\bFolw\b", "Flow"),
    (r"\bEfcfiiency\b", "Efficiency"),
    (r"\becfiiencies\b", "efficiencies"),
    (r"\bdefni\s+ition\b", "definition"),
    (r"\bDefni\s+ition\b", "Definition"),
    (r"\bdefni\s+itions\b", "definitions"),
    (r"\bDefni\s+itions\b", "Definitions"),
    (r"\bdefni\s+ing\b", "defining"),
    (r"\bdefni\s+es\b", "defines"),
    (r"\binfni\s+itesimal\b", "infinitesimal"),
    (r"\binfni\s+itesimals\b", "infinitesimals"),
    (r"\binfni\s+ity\b", "infinity"),
    (r"\binfni\s+ite\b", "infinite"),
    (r"\binfni\s+itely\b", "infinitely"),
    (r"\becfiiency\b", "efficiency"),
    (r"\becfiiencies\b", "efficiencies"),
    (r"\beffciency\b", "efficiency"),
    (r"\beffciiency\b", "efficiency"),
    (r"\befciency\b", "efficiency"),
    (r"\befciencies\b", "efficiencies"),
    (r"\befcfiiency\b", "efficiency"),
    (r"\befcfiiencies\b", "efficiencies"),
    (r"\befcfiient\b", "efficient"),
    (r"\befcfiiently\b", "efficiently"),
    (r"\bsignifciantly\b", "significantly"),
    (r"\bconfgi\s+uration\b", "configuration"),
    (r"\bconfgi\s+urations\b", "configurations"),
    (r"\bconfgi\b", "config"),
    (r"\bquantifciation\b", "quantification"),
    (r"\bquantifciations\b", "quantifications"),
    (r"\bquantifeis\b", "quantifies"),
    (r"\bdifefrently\b", "differently"),
    (r"\bdifefrential\b", "differential"),
    (r"\bdifefrences\b", "differences"),
    (r"\bdifefrentiate\b", "differentiate"),
    (r"\bdifefring\b", "differing"),
    (r"\bdifefrs\b", "differs"),
    (r"\bdifefr\b", "differ"),
    (r"\bdifefrence\b", "difference"),
    (r"\bsufcfiient\b", "sufficient"),
    (r"\binsufcfiient\b", "insufficient"),
    (r"\bmodifeid\b", "modified"),
    (r"\bfol\s+or\b", "floor"),
    (r"\bfol\s+ws\b", "flows"),
    (r"\bInfol\s+ws\b", "Inflows"),
    (r"\boutfol\s+ws\b", "outflows"),
    (r"\bafefcted\b", "affected"),
    (r"\bafefct\b", "affect"),
    (r"\bcoefcfiient\b", "coefficient"),
    (r"\bofcfiial\b", "official"),
    (r"\bofcfiially\b", "officially"),
    (r"\bredefni\b", "redefine"),
    (r"\bindefni\b", "indefinite"),
]


def fix_ocr(text: str) -> str:
    """Repair common Libertinus PDF extraction transpositions."""
    for pattern, repl in _OCR_REPLACEMENTS:
        text = re.sub(pattern, repl, text)
    return text


# --------------------------------------------------------------------------
# cross references
# --------------------------------------------------------------------------

REFS = [
    (re.compile(r"\b(Figures?|Figs?\.)\s+((?:[A-D]|\d+)\.\d+)"), "fig"),
    (re.compile(r"\b(Tables?)\s+((?:[A-D]|\d+)\.\d+)"), "tab"),
    (re.compile(r"\b(Eqs?\.|Equations?)\s+((?:[A-D]|\d+)(?:\.\d+|/\d+)+)"), "eq"),
    (re.compile(r"\b(Boxe?s?)\s+((?:[A-D]|\d+)\.\d+)"), "box"),
    (re.compile(r"\b(Definitions?)\s+((?:[A-D]|\d+)\.\d+\.\d+)"), "def"),
    (re.compile(r"\b(Examples?)\s+((?:[A-D]|\d+)\.\d+\.\d+)"), "ex"),
    (re.compile(r"\b(Sections?|Secs?\.)\s+((?:[A-D]|\d+)\.\d+(?:\.\d+)?)"), "sec"),
    (re.compile(r"\b(Chapters?)\s+(\d+)"), "ch"),
    (re.compile(r"\b(Appendix)\s+([A-D])\b"), "app"),
]

def slug(prefix, number):
    return f"{prefix}-" + str(number).replace(".", "-").replace("/", "-").lower()


def link_references(text, known):
    def rewrite(chunk):
        for pattern, prefix in REFS:
            def sub(m):
                label = slug(prefix, m.group(2))
                if label not in known:
                    return m.group(0)
                return f"[{m.group(0)}](#{label})"
            chunk = pattern.sub(sub, chunk)
        # bibliography tags
        chunk = re.sub(r"(?<!\^)\[(\d+(?:[,;]\s*\d+)*)\]",
                       lambda m: "[" + ", ".join(
                           f"[{n.strip()}](#ref-{n.strip()})" if f"ref-{n.strip()}" in known
                           else n.strip() for n in re.split(r"[,;]", m.group(1))) + "]",
                       chunk)
        return chunk
    return outside_math(text, rewrite)


