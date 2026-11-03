#!/usr/bin/env python3
"""빌드된 site/의 HTML에 정리·정의 등 환경 번호를 미리 써 넣는다.

docs/javascripts/theorems.js가 방문자 브라우저에서 하던 일을 빌드 시점에 한 번만 한다.
  - 제목:  "Functor"            → "Definition 1.3 (Functor)"
  - 앵커:  본문 첫 문단/항목의 id → 박스(div/details)로 이동
  - 링크:  빈 링크 [](Section 1.md#id) → "Definition 1.1"  (같은 페이지/다른 페이지 모두)

번호 규칙 (theorems.js와 동일)
  - .../Chapter N/Section M/ 페이지는 접두어 N, 같은 챕터의 앞 섹션(챕터 index 포함)에서 이어서 셈
  - 그 밖의 페이지는 data-thm-prefix 표시나 h1의 "Chapter/Section/§ 1.2"에서 접두어를 얻고 1부터 셈

처리한 페이지의 .md-content에는 data-thm-static을 붙여, theorems.js가 다시 계산하지 않게 한다.
`zensical build` 다음에 실행:  python scripts/number_theorems.py [site]
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

from bs4 import BeautifulSoup

KINDS = {
    "definition": "Definition",
    "theorem": "Theorem",
    "lemma": "Lemma",
    "proposition": "Proposition",
    "corollary": "Corollary",
    "example": "Example",
    "remark": "Remark",
}
# True: 모든 환경이 번호 하나를 공유 / False: 환경마다 따로
SHARED_COUNTER = True

SELECTOR = ", ".join(f".admonition.{t}, details.{t}" for t in KINDS)
ANCHOR_SEL = ":scope > [id], :scope > :is(ul, ol) > li[id], :scope > :is(ul, ol) > li > p[id]"
TITLE_SEL = ":scope > .admonition-title, :scope > summary"
LOCATION = re.compile(r"^(.*/Chapter\s*(\d+))(?:/Section\s*(\d+))?/?(?:index\.html)?$", re.I)
H1_PREFIX = re.compile(r"^\s*(?:Chapter|Section|§)\s*(\d+(?:\.\d+)*)", re.I)


def type_of(box):
    return next(t for t in KINDS if t in box.get("class", []))


def key_of(t):
    return "_all" if SHARED_COUNTER else t


def parse_location(url_path):
    m = LOCATION.match(url_path)
    if not m:
        return None
    return {"base": m.group(1), "chapter": m.group(2), "section": int(m.group(3) or 0)}


def get_prefix(root, loc):
    marker = root.select_one("[data-thm-prefix]")
    if marker:
        return marker["data-thm-prefix"]
    if loc:
        return loc["chapter"]
    h1 = root.find("h1")
    m = h1 and H1_PREFIX.match(h1.get_text())
    return m.group(1) if m else ""


class Page:
    def __init__(self, site, path):
        self.path = path
        rel = path.relative_to(site).as_posix()
        # 사이트 루트 기준 URL 경로 (디렉터리형 URL: .../Section 2/)
        self.url = "/" + (rel[: -len("index.html")] if rel.endswith("index.html") else rel)
        self.soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        self.root = self.soup.select_one(".md-content") or self.soup.body
        self.loc = parse_location(self.url)
        self.boxes = self.root.select(SELECTOR) if self.root else []
        self.labels = {}

    def counts(self):
        c = {}
        for box in self.boxes:
            k = key_of(type_of(box))
            c[k] = c.get(k, 0) + 1
        return c


def main():
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "site").resolve()
    pages = [Page(site, p) for p in sorted(site.rglob("*.html"))]
    by_url = {p.url: p for p in pages}

    # 1) 번호 매기기
    for page in pages:
        if not page.boxes:
            continue
        counters = {}
        if page.loc:
            for other in pages:
                o = other.loc
                if o and o["base"] == page.loc["base"] and o["section"] < page.loc["section"]:
                    for k, v in other.counts().items():
                        counters[k] = counters.get(k, 0) + v
        prefix = get_prefix(page.root, page.loc)

        for box in page.boxes:
            t = type_of(box)
            k = key_of(t)
            counters[k] = counters.get(k, 0) + 1
            label = f"{KINDS[t]} {prefix + '.' if prefix else ''}{counters[k]}"

            title = box.select_one(TITLE_SEL)
            if title is not None:
                raw = title.get_text().strip()
                children = list(title.contents)
                title.clear()
                if raw and raw.lower() != t:
                    # 이름 안의 수식 등 HTML은 그대로 보존
                    title.append(f"{label} (")
                    for ch in children:
                        title.append(ch)
                    title.append(")")
                else:
                    title.append(label)

            if not box.get("id"):
                anchor = box.select_one(ANCHOR_SEL)
                if anchor is not None:
                    box["id"] = anchor["id"]
                    del anchor["id"]
            if box.get("id"):
                page.labels[box["id"]] = label

    # 2) 빈 링크 채우기
    missing = 0
    for page in pages:
        if not page.root:
            continue
        for a in page.root.select('a[href*="#"]'):
            if a.get_text().strip():
                continue
            parts = urlsplit(a["href"])
            if parts.scheme or parts.netloc:
                continue
            target_url = unquote(urlsplit(urljoin(page.url, a["href"])).path)
            target = by_url.get(target_url) or by_url.get(target_url.rstrip("/") + "/")
            frag = unquote(parts.fragment)
            label = target.labels.get(frag) if target else None
            if label:
                a.string = label
                a["data-thm-ref"] = "1"
            else:
                missing += 1
                print(f"::warning::{page.url}: 번호를 찾지 못한 빈 링크 {a['href']}")

    # 3) 저장
    changed = 0
    for page in pages:
        if page.root is not None and page.root.name != "body":
            page.root["data-thm-static"] = ""
        if page.boxes or page.root is not None:
            page.path.write_text(str(page.soup), encoding="utf-8")
            changed += 1
    numbered = sum(len(p.labels) for p in pages)
    print(f"theorem numbering: {numbered} labelled box(es), {changed} page(s), {missing} unresolved link(s)")


if __name__ == "__main__":
    main()
