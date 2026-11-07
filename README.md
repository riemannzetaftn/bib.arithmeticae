# Bibliotheca Arithmeticae
 
[![Documentation](https://github.com/riemannzetaftn/bib.arithmeticae/actions/workflows/docs.yml/badge.svg)](https://github.com/riemannzetaftn/bib.arithmeticae/actions/workflows/docs.yml)
 
**A blog dedicated to number theory** — a record of my studies in mathematics, built with [Zensical](https://zensical.org) and published on GitHub Pages.
 
🔗 **https://riemannzetaftn.github.io/bib.arithmeticae/**
 
---
 
## About
 
I am an undergraduate student in the Department of Mathematics at KAIST, with a particular interest in analytic number theory. This site collects my notes on the background material needed to understand the deeper results of number theory. The aim is to reinterpret standard theories carefully and fill in the details often left out of the literature.
 
The notes are a work in progress, and new subjects are added over time. See the site for the current table of contents.
 
## Repository Structure
 
````
.
├── docs/                    # Site content (Markdown)
│   ├── index.md             # Home page
│   ├── <Area>/<Subject>/Chapter N/Section M.md
│   ├── javascripts/         # MathJax config & macros, theorem numbering, tikzcd
│   └── stylesheets/         # Theorem boxes, tikzcd diagrams
├── scripts/
│   ├── gen_nav.py           # Builds the nav in zensical.toml from front-matter `weight`
│   ├── cite.py              # Resolves [@key] citations against references.bib
│   ├── tikzcd_fence.py      # SuperFences custom fence: ```tikzcd → inline SVG
│   ├── render_tikzcd.py     # Renders tikzcd blocks to SVG (needs TeX + dvisvgm)
│   ├── tikzcd_preamble.tex  # LaTeX preamble used for diagrams
│   └── number_theorems.py   # Numbers definitions/theorems in the built HTML
├── tikzcd/                  # Cached SVGs of rendered diagrams (content-hashed)
├── references.bib           # Bibliography (BibTeX)
├── zensical.toml            # Site configuration
└── .github/workflows/docs.yml
````
 
## Writing Conventions
 
### Page order
 
Pages are ordered by a `weight` in the front matter (lower comes first; pages without a weight go last, by name). A folder takes the weight of its `index.md`.
 
````markdown
---
title: Category Theory
weight: 1
---
````
 
Files named `Chapter N` / `Section N` get short labels in the navigation automatically.
 
### Mathematics
 
Use `\( ... \)` for inline math and `\[ ... \]` for display math (`$...$` also works inline). Custom macros such as `\sfC`, `\Hom`, `\Ob` are defined in `docs/javascripts/mathjax.js`.
 
### Theorem environments
 
Use admonitions (or collapsible `???` blocks) with one of the types `definition`, `theorem`, `lemma`, `proposition`, `corollary`, `example`, `remark`. Give it an id so it can be referenced:
 
````markdown
!!! definition "Category"
 
    A *category* $\sfC$ consists of the following data.
    { #def-category }
````
 
All environments share one counter, numbered by chapter (e.g. *Definition 1.3*), continuing across sections of the same chapter.
 
### Cross-references
 
An empty link to an id is filled in with the environment's number:
 
````markdown
See [](#def-category).
See [](<Section 1.md#ex-category>).
````
 
### Citations
 
Add the entry to `references.bib`, then cite it by key. A numbered **References** section is appended to the page automatically.
 
````markdown
[@MacLane]
[@MacLane, Ch. IV]
[@MacLane; @Riehl, Thm. 2.3]
````
 
### Commutative diagrams
 
Write a `tikzcd` fenced block (it also works inside admonitions):
 
````markdown
```tikzcd
\begin{tikzcd}
  A \arrow[r, "f"] \arrow[d, "g"'] & B \arrow[d] \\
  C \arrow[r] & D
\end{tikzcd}
```
````
 
Diagrams are rendered to SVG once and cached in `tikzcd/` by a hash of their source. They follow the theme's text color, including dark mode.
 
## Building Locally
 
````bash
pip install zensical pybtex beautifulsoup4
 
python scripts/gen_nav.py              # update navigation
PYTHONPATH=scripts zensical serve      # preview at http://localhost:8000
````
 
To render new diagrams locally (optional; CI does this too), install TeX Live with `tikz-cd` and `dvisvgm`, then run:
 
````bash
python scripts/render_tikzcd.py        # render missing diagrams
python scripts/render_tikzcd.py --prune  # delete unused SVGs
````
 
> `cite.py` and the "last updated" step modify `docs/*.md` in place, so they are meant to run only in CI.
 
## Deployment
 
Every push to `main` triggers the GitHub Actions workflow, which:
 
1. Checks for unrendered `tikzcd` diagrams; if any, installs TeX, renders them, and commits the SVGs back (`[skip ci]`).
2. Resolves citations from `references.bib`.
3. Appends a *Last updated* date to each page from its git history.
4. Generates the navigation and builds the site with Zensical.
5. Numbers theorem environments in the built HTML.
6. Deploys to GitHub Pages.