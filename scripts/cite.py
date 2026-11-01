#!/usr/bin/env python3
"""docs/ 안의 [@key] 인용을 번호 링크로 바꾸고, 페이지 끝에 References를 붙인다.

  [@maclane1998]                       → [1]
  [@maclane1998, Ch. IV]               → [1, Ch. IV]
  [@maclane1998; @riehl2016, Thm. 2.3] → [1; 2, Thm. 2.3]

- 문헌 정보: 저장소 루트의 references.bib (BibTeX)
- 번호: 페이지마다 처음 인용된 순서
- 코드 블록(``` / ~~~, tikzcd 포함), 인라인 코드, front matter는 건드리지 않음
- docs/*.md를 직접 고치므로 CI에서만 실행 (last-updated 단계와 같은 방식)
"""
import re
import unicodedata
from pathlib import Path

from pybtex.database import parse_file

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
BIB = ROOT / "references.bib"

HEADING = "## References { #references }"

KEY = r"[\w:.+/-]+"
# \[ (디스플레이 수식), [@x](url) / [@x][y] / [@x]: (링크 정의)는 제외
CITE = re.compile(r"(?<!\\)\[(@[^\[\]\n]+)\](?![(\[:])")
ITEM = re.compile(rf"^\s*@({KEY})\s*(?:,\s*(.*?))?\s*$")
FENCE_OPEN = re.compile(r"^[ \t]*(`{3,}|~{3,})")
INLINE_CODE = re.compile(r"(`+).+?\1")


def anchor(key: str) -> str:
    return "ref-" + re.sub(r"[^A-Za-z0-9_-]+", "-", key)


# ---------- BibTeX 필드의 LaTeX → 텍스트 ($...$ 수식은 그대로 두어 MathJax가 처리) ----------

ACCENTS = {
    "'": "\u0301", "`": "\u0300", "^": "\u0302", '"': "\u0308", "~": "\u0303",
    "=": "\u0304", ".": "\u0307", "u": "\u0306", "v": "\u030C", "H": "\u030B",
    "c": "\u0327", "k": "\u0328", "r": "\u030A", "d": "\u0323", "b": "\u0331",
}
SYMBOLS = {
    "ss": "ß", "ae": "æ", "AE": "Æ", "oe": "œ", "OE": "Œ", "aa": "å", "AA": "Å",
    "o": "ø", "O": "Ø", "l": "ł", "L": "Ł", "i": "ı", "j": "ȷ",
}
ACCENT_SYM = re.compile(r"""\\([`'^"~=.])\s*(?:\{\s*\\?([A-Za-z])\s*\}|\\?([A-Za-z]))""")
ACCENT_LET = re.compile(r"\\([uvHckrdb])(?:\s*\{\s*\\?([A-Za-z])\s*\}|\s+\\?([A-Za-z]))")
SYMBOL = re.compile(r"\\(ss|ae|AE|oe|OE|aa|AA|o|O|l|L|i|j)(?![A-Za-z])\s?")
MATH = re.compile(r"(\$[^$]*\$)")


def _plain(s: str) -> str:
    accent = lambda m: (m.group(2) or m.group(3)) + ACCENTS[m.group(1)]
    s = ACCENT_SYM.sub(accent, s)
    s = ACCENT_LET.sub(accent, s)
    s = SYMBOL.sub(lambda m: SYMBOLS[m.group(1)], s)
    s = re.sub(r"\\(?:emph|textit)\s*\{([^{}]*)\}", r"*\1*", s)
    s = re.sub(r"\\textbf\s*\{([^{}]*)\}", r"**\1**", s)
    for a, b in (("\\&", "&"), ("\\%", "%"), ("\\_", "_"),
                 ("---", "—"), ("--", "–"), ("~", "\u00a0")):
        s = s.replace(a, b)
    s = re.sub(r"[{}]", "", s)
    return unicodedata.normalize("NFC", s)


def tex(s: str) -> str:
    segs = MATH.split(s or "")
    return "".join(seg if i % 2 else _plain(seg) for i, seg in enumerate(segs)).strip()


# ---------- 문헌 항목 서식 ----------

THESIS = {"phdthesis": "PhD thesis", "mastersthesis": "Master's thesis"}


def names(persons) -> str:
    out = []
    for p in persons:
        if p.last_names == ["others"]:
            out.append("et al.")
            continue
        n = " ".join(p.first_names + p.middle_names + p.prelast_names + p.last_names)
        if p.lineage_names:
            n += ", " + " ".join(p.lineage_names)
        out.append(tex(n))
    if out and out[-1] == "et al.":
        return ", ".join(out[:-1]) + " et al."
    if len(out) <= 2:
        return " and ".join(out)
    return ", ".join(out[:-1]) + ", and " + out[-1]


def format_entry(e) -> str:
    typ = e.type.lower()
    f = lambda k: tex(e.fields.get(k, ""))
    raw = lambda k: re.sub(r"[{}\s]", "", e.fields.get(k, ""))
    authors = names(e.persons.get("author", []))
    eds = e.persons.get("editor", [])
    editors = names(eds)
    ed_label = "eds." if len(eds) > 1 else "ed."
    in_book = typ in ("incollection", "inproceedings", "inbook")

    parts = []
    if authors:
        parts.append(authors)
    elif editors and not in_book:
        parts.append(f"{editors} ({ed_label})")
    if f("title"):
        parts.append(f"*{f('title')}*")

    if typ == "article":
        j = f("journal")
        if f("volume"):
            j += f" **{f('volume')}**"
        if f("year"):
            j += f" ({f('year')})"
        if f("number"):
            j += f", no. {f('number')}"
        parts.append(j.strip())
        parts.append(f("pages"))
    else:
        if in_book and f("booktitle"):
            s = f"in: *{f('booktitle')}*"
            if editors:
                s += f" ({editors}, {ed_label})"
            parts.append(s)
        if f("edition"):
            parts.append(f"{f('edition')} ed.")
        if f("series"):
            parts.append(f"{f('series')} {f('volume')}".strip())
        elif f("volume"):
            parts.append(f"vol. {f('volume')}")
        parts.append(THESIS.get(typ, ""))
        for k in ("publisher", "organization", "institution", "school", "address", "howpublished"):
            parts.append(f(k))
        parts.append(f("year"))
        if f("pages"):
            parts.append(f"pp. {f('pages')}")
    parts.append(f("note"))
    text = ", ".join(p for p in parts if p) + "."

    links = []
    if raw("doi"):
        links.append(f"[doi:{raw('doi')}](https://doi.org/{raw('doi')})")
    if raw("eprint") and (raw("archiveprefix") or raw("eprinttype")).lower() == "arxiv":
        links.append(f"[arXiv:{raw('eprint')}](https://arxiv.org/abs/{raw('eprint')})")
    elif raw("url"):
        links.append(f"<{raw('url')}>")
    return " ".join([text, *links])


# ---------- 페이지 처리 ----------

def outside_code(line: str, fn) -> str:
    out, pos = [], 0
    for m in INLINE_CODE.finditer(line):
        out.append(CITE.sub(fn, line[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(CITE.sub(fn, line[pos:]))
    return "".join(out)


def process(text: str, bib):
    order, missing = {}, []

    def cite(m):
        items = [ITEM.match(s) for s in m.group(1).split(";")]
        if not all(items):
            return m.group(0)  # 인용 형식이 아니면 그대로
        out = []
        for im in items:
            key, loc = im.group(1), im.group(2)
            if key not in bib:
                missing.append(key)
                out.append(f"**?{key}**")
                continue
            n = order.setdefault(key, len(order) + 1)
            label = f"{n}, {loc}" if loc else f"{n}"
            out.append(f"[{label}](#{anchor(key)}){{ .citation }}")
        return "\\[" + "; ".join(out) + "\\]"

    lines = text.split("\n")
    start = 0
    if lines and lines[0].strip() == "---":  # front matter 건너뛰기
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                start = i + 1
                break

    fence = None
    for i in range(start, len(lines)):
        line = lines[i]
        if fence:
            if re.fullmatch(rf"[ \t]*{re.escape(fence[0])}{{{len(fence)},}}[ \t]*", line):
                fence = None
            continue
        m = FENCE_OPEN.match(line)
        if m:
            fence = m.group(1)
            continue
        lines[i] = outside_code(line, cite)

    body = "\n".join(lines)
    if not order:
        return body, missing
    refs = [f"\\[{n}\\] {format_entry(bib[key])}\n{{ #{anchor(key)} .reference }}"
            for key, n in order.items()]
    return body.rstrip() + "\n\n" + HEADING + "\n\n" + "\n\n".join(refs) + "\n", missing


def main():
    bib = parse_file(str(BIB), bib_format="bibtex").entries if BIB.exists() else {}
    changed = 0
    for md in sorted(DOCS.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        new, missing = process(text, bib)
        for key in dict.fromkeys(missing):
            print(f"::warning file={md.relative_to(ROOT)}::Unknown citation key: {key}")
        if new != text:
            md.write_text(new, encoding="utf-8")
            changed += 1
    print(f"{len(bib)} bib entries, citations resolved in {changed} page(s)")


if __name__ == "__main__":
    main()