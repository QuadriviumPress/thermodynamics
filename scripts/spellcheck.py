"""Hunspell-backed spell checking for OCR cleanup and verification."""

from __future__ import annotations

import re
import subprocess

WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")
OCR_MARKERS = re.compile(
    r"cfi|fci|fgi|fni|defn[^i]|ecf[^i]|fol[^l]|ful[^l]|fxi|ifc|difef|signif[^i]|confg|"
    r"modif[^i]|quantif[^i]|identif[^i]|inefc|effci|sufcf|coefcf|ofcf|afef|itesimal|ecfii"
)

# Proper names, SI units, and thermodynamics jargon not in en_US.
ALLOW = {
    "boltzmann", "carnot", "celsius", "chaleur", "clausius", "cleynen", "exergy",
    "fahrenheit", "gigawatts", "iapws", "isentropic", "isochoric", "isothermal",
    "joule", "kelvin", "kilowatt", "lavoisier", "maxwell", "mollier", "napier",
    "nist", "olivier", "otto", "pambour", "rankine", "reynolds", "rudolf", "sadi",
    "stodola", "thomson", "turboshaft", "unitless", "wilson", "watt", "wee",
    "doi", "cc", "sa", "fig", "eq", "pdf", "html", "svg", "png", "github",
    "thermodynamicsbook", "quadriviumpress", "isbn",
}


def _batch_misspellings(words: set[str], lang: str = "en_US") -> set[str]:
    """Return the subset of *words* flagged by hunspell."""
    todo = {w.lower() for w in words if w.lower() not in ALLOW and len(w) >= 4}
    if not todo:
        return set()
    proc = subprocess.run(
        ["hunspell", "-l", "-d", lang],
        input="\n".join(sorted(todo)),
        text=True,
        capture_output=True,
        check=False,
    )
    return {w.strip().lower() for w in proc.stdout.splitlines() if w.strip()}


def _swap_pairs(word: str) -> set[str]:
    """Generate fi↔if and similar Libertinus transposition candidates."""
    out = {word.lower()}
    for w in list(out):
        out.add(w.replace("fi", "if"))
        out.add(w.replace("if", "fi"))
        out.add(w.replace("fc", "cf"))
        out.add(w.replace("cf", "fc"))
        out.add(w.replace("fe", "ef"))
        out.add(w.replace("ef", "fe"))
        for i in range(len(w) - 1):
            out.add(w[:i] + w[i + 1] + w[i] + w[i + 2:])
    out.discard(word.lower())
    return out


def _build_fix_map(words: set[str]) -> dict[str, str]:
    """Map lower-case misspellings to a unique hunspell-valid correction."""
    suspects = {w.lower() for w in words if OCR_MARKERS.search(w.lower())}
    if not suspects:
        return {}
    misspelled = _batch_misspellings(suspects)

    candidates: set[str] = set()
    options: dict[str, list[str]] = {}
    for word in misspelled:
        opts = sorted(w for w in _swap_pairs(word) if w not in ALLOW)
        if opts:
            options[word] = opts
            candidates.update(opts)

    if not candidates:
        return {}

    known = candidates - _batch_misspellings(candidates)

    fixes: dict[str, str] = {}
    for word, opts in options.items():
        good = [o for o in opts if o in known]
        if len(good) == 1:
            fixes[word] = good[0]
    return fixes


def fix_words(text: str) -> str:
    """Correct OCR typos using batched hunspell checks (suspect words only)."""
    words = {m.group(0) for m in WORD.finditer(text)}
    fixes = _build_fix_map(words)
    if not fixes:
        return text

    def repl(m: re.Match[str]) -> str:
        word = m.group(0)
        fix = fixes.get(word.lower())
        if not fix:
            return word
        if word[0].isupper():
            fix = fix[0].upper() + fix[1:]
        return fix

    return WORD.sub(repl, text)


def ocr_suspects(text: str) -> list[str]:
    """Words that fail hunspell and look like OCR transpositions."""
    words = {m.group(0).lower() for m in WORD.finditer(text)}
    bad = _batch_misspellings(words)
    return sorted(w for w in bad if OCR_MARKERS.search(w))
