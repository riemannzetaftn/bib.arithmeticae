#!/usr/bin/env python3
"""docs/ 아래 Markdown 파일의 front matter `weight`로 zensical.toml의 nav를 생성한다.

정렬 규칙
- 같은 폴더 안에서 weight 오름차순, 같으면 파일/폴더 이름순
- weight가 없는 항목은 맨 뒤 (이름순)
- 폴더의 weight는 그 폴더 index.md의 weight
- index.md / README.md는 항상 해당 섹션의 맨 앞 (navigation.indexes용)
- 이름이 '.' 또는 '_'로 시작하는 파일/폴더, .md가 없는 폴더는 제외
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CONFIG = ROOT / "zensical.toml"

BEGIN = "# >>> auto-generated nav (scripts/gen_nav.py) >>>"
END = "# <<< auto-generated nav <<<"
NO_WEIGHT = float("inf")

FRONT_MATTER = re.compile(r"\A---[ \t]*\n(.*?)\n---[ \t]*(?:\n|\Z)", re.S)
WEIGHT = re.compile(r"^weight\s*:\s*['\"]?(-?\d+(?:\.\d+)?)['\"]?\s*$", re.M)


def read_weight(md: Path) -> float:
    text = md.read_text(encoding="utf-8-sig")
    fm = FRONT_MATTER.match(text)
    if fm:
        m = WEIGHT.search(fm.group(1))
        if m:
            return float(m.group(1))
    return NO_WEIGHT

LABEL = re.compile(r"^(chapter|section)[\s-]+(\d+(?:\.\d+)*)$", re.I)
TITLE = re.compile(r"^title\s*:\s*['\"]?(.+?)['\"]?\s*$", re.M)


def display_name(directory: Path) -> str:
    """사이드바에 보일 폴더 이름: 'Chapter 1' 형태 > index.md의 title > 하이픈을 공백으로."""
    m = LABEL.match(directory.name)
    if m:
        return f"{m.group(1).capitalize()} {m.group(2)}"
    index = directory / "index.md"
    if index.exists():
        fm = FRONT_MATTER.match(index.read_text(encoding="utf-8-sig"))
        t = fm and TITLE.search(fm.group(1))
        if t:
            return t.group(1)
    return directory.name.replace("-", " ")

def nav_entry(md: Path, rel: str):
    """Chapter n / Section n 이름이면 {라벨: 경로}, 아니면 경로 그대로."""
    name = md.parent.name if is_index(md) else md.stem
    m = LABEL.match(name)
    return {f"{m.group(1).capitalize()} {m.group(2)}": rel} if m else rel

def is_index(path: Path) -> bool:
    return path.name.lower() in ("index.md", "readme.md")


def collect(directory: Path):
    """(nav 항목 리스트, 이 폴더의 weight)를 반환한다."""
    index_rel, index_weight = None, NO_WEIGHT
    items = []

    for child in directory.iterdir():
        if child.name.startswith((".", "_")):
            continue
        if child.is_dir():
            entries, weight = collect(child)
            if entries:
                items.append((weight, child.name.lower(), {display_name(child): entries}))
        elif child.suffix.lower() == ".md":
            rel = child.relative_to(DOCS).as_posix()
            if is_index(child):
                #index_rel, index_weight = rel, read_weight(child)
                index_rel, index_weight = nav_entry(child, rel), read_weight(child)
            else:
                items.append((read_weight(child), child.name.lower(), nav_entry(child, rel)))

    items.sort(key=lambda t: (t[0], t[1]))
    entries = [entry for _, _, entry in items]
    if index_rel:
        entries.insert(0, index_rel)
    return entries, index_weight


def q(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)  # TOML basic string과 호환


def render(entries, depth=1):
    pad = "  " * depth
    lines = []
    for entry in entries:
        if isinstance(entry, str):
            lines.append(f"{pad}{q(entry)},")
        else:
            (name, sub), = entry.items()
            if isinstance(sub, str):
                lines.append(f"{pad}{{ {q(name)} = {q(sub)} }},")
                continue
            lines.append(f"{pad}{{ {q(name)} = [")
            lines.extend(render(sub, depth + 1))
            lines.append(f"{pad}] }},")
    return lines


def main():
    entries, _ = collect(DOCS)
    block = "\n".join([BEGIN, "nav = [", *render(entries), "]", END])

    config = CONFIG.read_text(encoding="utf-8")
    marked = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)

    if marked.search(config):
        new = marked.sub(lambda _: block, config)
    else:
        new, n = re.subn(r"^\[project\][ \t]*$",
                         lambda m: m.group(0) + "\n" + block,
                         config, count=1, flags=re.M)
        if n == 0:
            sys.exit("zensical.toml에서 [project] 테이블을 찾지 못했습니다.")

    if new != config:
        CONFIG.write_text(new, encoding="utf-8")
    print(block)


if __name__ == "__main__":
    main()