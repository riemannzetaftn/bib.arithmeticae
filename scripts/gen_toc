#!/usr/bin/env python3
"""subject / chapter 소개글(index.md)에 본문 목차(Contents)를 넣는다.

  subject 페이지 (Chapter N 폴더를 가진 폴더의 index.md)
    - Chapter 1. 제목          → Chapter 1/index.md
        - Section 1.1. 제목    → Chapter 1/Section 1.md
        - Section 1.2. 제목
    - Chapter 2. 제목
        ...
  chapter 페이지 (Chapter M/index.md)
    - Section M.1. 제목
    - Section M.2. 제목

- 제목은 각 파일의 첫 번째 '# ' 제목에서 읽는다.
  '# Section 1. Categories' → 'Section M.1. Categories' (M = chapter 번호)
- 번호는 파일/폴더 이름(Chapter M, Section N)에서 가져오고, 숫자 순으로 정렬한다.
- index.md 안에 <!-- contents --> 줄이 있으면 그 자리에, 없으면 글 끝에 넣는다.
- docs/*.md를 직접 고치므로 CI에서만 실행 (cite.py, last-updated 단계와 같은 방식)
"""
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

HEADING = "## Contents { #contents }"
MARKER = re.compile(r"^[ \t]*<!--\s*contents\s*-->[ \t]*$", re.M | re.I)

CHAPTER_DIR = re.compile(r"^chapter\s+(\d+)$", re.I)
SECTION_FILE = re.compile(r"^section\s+(\d+)$", re.I)

FRONT_MATTER = re.compile(r"\A---[ \t]*\n.*?\n---[ \t]*(?:\n|\Z)", re.S)
H1 = re.compile(r"^#[ \t]+(.+?)[ \t]*#*[ \t]*$", re.M)
ATTRS = re.compile(r"\s*\{[^{}]*\}\s*$")  # 제목 끝의 { #id } 제거
FENCE = re.compile(r"^[ \t]*(`{3,}|~{3,}).*?^[ \t]*\1[ \t]*$", re.M | re.S)
# 'Chapter 1.' / 'Section 1:' / 'Section 1 -' 같은 접두어
PREFIX = re.compile(r"^(?:chapter|section)\s+\d+(?:\.\d+)*\s*[.:\-–—]?\s*", re.I)


def title_of(md: Path) -> str:
    """첫 '# ' 제목에서 'Chapter N.' / 'Section N.' 접두어를 뗀 나머지."""
    text = md.read_text(encoding="utf-8-sig")
    text = FRONT_MATTER.sub("", text, count=1)
    text = FENCE.sub("", text)
    m = H1.search(text)
    if not m:
        return ""
    return PREFIX.sub("", ATTRS.sub("", m.group(1))).strip()


def label(kind: str, number: str, title: str) -> str:
    return f"{kind} {number}. {title}" if title else f"{kind} {number}"


def link(target: Path, base: Path) -> str:
    """base 폴더 기준 상대 경로 (공백 등은 %인코딩)."""
    rel = target.relative_to(base).as_posix()
    return quote(rel)


def chapters_in(subject: Path):
    out = []
    for d in subject.iterdir():
        m = CHAPTER_DIR.match(d.name)
        if d.is_dir() and m:
            out.append((int(m.group(1)), d))
    return sorted(out)


def sections_in(chapter: Path):
    out = []
    for f in chapter.glob("*.md"):
        m = SECTION_FILE.match(f.stem)
        if m:
            out.append((int(m.group(1)), f))
    return sorted(out)


def section_lines(m: int, chapter: Path, base: Path, indent: str):
    lines = []
    for n, f in sections_in(chapter):
        text = label("Section", f"{m}.{n}", title_of(f))
        lines.append(f"{indent}- [{text}]({link(f, base)})")
    return lines


def subject_toc(subject: Path):
    lines = []
    for m, chapter in chapters_in(subject):
        index = chapter / "index.md"
        text = label("Chapter", str(m), title_of(index) if index.exists() else "")
        target = index if index.exists() else None
        lines.append(f"- [{text}]({link(target, subject)})" if target else f"- {text}")
        lines.extend(section_lines(m, chapter, subject, "    "))
    return lines


def chapter_toc(chapter: Path):
    m = int(CHAPTER_DIR.match(chapter.name).group(1))
    return section_lines(m, chapter, chapter, "")


def insert(index: Path, lines):
    if not lines:
        return False
    block = "\n".join([HEADING, "", *lines])
    text = index.read_text(encoding="utf-8-sig")
    if MARKER.search(text):
        new = MARKER.sub(lambda _: block, text, count=1)
    else:
        new = text.rstrip() + "\n\n" + block + "\n"
    index.write_text(new, encoding="utf-8")
    return True


def main():
    for index in sorted(DOCS.rglob("index.md")):
        folder = index.parent
        if any(p.startswith((".", "_")) for p in folder.relative_to(DOCS).parts):
            continue
        if CHAPTER_DIR.match(folder.name):
            lines = chapter_toc(folder)
        elif chapters_in(folder):
            lines = subject_toc(folder)
        else:
            continue
        if insert(index, lines):
            print(f"contents → {index.relative_to(DOCS)}")


if __name__ == "__main__":
    main()