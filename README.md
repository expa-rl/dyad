# Dyad project page

Project website for **Dyad: Extending Large Language Models with Native Typed
Decision-Making** ([paper](https://arxiv.org/abs/2609.36116)).

Adapted from [ExpA / EARL](https://expa-rl.github.io/) and its upstream
[Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template).
The website is plain HTML, CSS and JavaScript. It has no installation or build
step and is published at <https://expa-rl.github.io/dyad/>.

## Editorial research

[EARL page and paper analysis](docs/earl-project-page-analysis.md) records which
results the reference page presents, omits or explains through animation.
[EARL writing and caption analysis](docs/earl-writing-and-captions.md) records the
one-sentence TL;DR, paragraph structure, emphasis and independent evidence labels.
[Dyad restructuring plan](docs/dyad-project-page-plan.md) documents the resulting
content choices, exact source values and writing rules used in this revision.

## Local preview

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000/>.

## Content and layout

1. Paper title, authors, affiliations and resource links.
2. A one-sentence TL;DR followed by an explanatory paragraph.
3. **Modular Adaptation with a Frozen LLM**: visible Table 1 compares the original
   model and frozen-LLM adaptation in four environments.
4. **Stronger Agents with Preserved General Capabilities**: Figure 1 compares
   the original LLM, GRPO, and Dyad-GRPO beyond CodeGym, including Dyad gains
   relative to the original LLM. Figure 2 shows capability changes in a manual
   carousel, defaulting to CodeGym with DIVE available through either arrow.
5. **Approach**: Figure 3 explains Jev-style direct decisions, conventional LLM
   agents, and Dyad. Figure 4 plays the silent architecture walkthrough, with a
   static architecture fallback.
   Table 2 sits beside one analysis paragraph on desktop and above it on narrow
   screens. It compares Jev, the original LLM and Dyad on JevBench; LLM-based
   methods use reasoning, specified once in the caption. The analysis highlights
   overall and hard-case gains over the original LLM.
6. Copyable BibTeX, upstream-template credit and institution-logo sources.

EARL's 960px desktop container is reused for both text and evidence. Each numbered
section has one heading followed directly by paragraphs. Dense full-result panels,
duplicated category labels, and expandable experiment sections are removed.
Each result chart has a separate mobile SVG with all selected values labelled directly.
The concept figure stacks its three original vector panels on narrow screens.
Both tables are visible HTML. Every exhibit has its own page number, name and caption;
there are no hidden data tables or expandable results. The requested capability
carousel switches between two fully labelled charts; it has no autoplay, supports
keyboard arrows and shows both charts when JavaScript is unavailable or when printed.
The previous/next controls sit at the left and right edges of the chart, vertically
centered, with no duplicate toolbar above it. The figure names the selected
training environment; an accessible live status announces changes. Model specifications are
kept in concise captions, while prose explains the research problems and capability gains.
Captions omit seed counts and evaluation-procedure detail. Sections alternate white
and soft blue. Body paragraphs use general training-environment descriptions;
exact names remain in the evidence captions and chart controls. Dyad is bold in
prose, with selected key claims highlighted in dark blue at 110% of body size. The header displays six complete institutional identity images in
a compact two-row layout, without hand-typeset institution names.

## Approach video

Figure 4 uses the author-supplied screen recording, packaged as
`static/videos/dyad-approach.mp4`. It contains only H.264 video, with no audio
track. The video stream was copied without re-encoding; the MP4 is prepared for
progressive playback. Its first and last frames each hold for an additional
second, with the animation between them retaining its original timing. A frame
at 17 seconds supplies its poster image,
`static/images/dyad-approach-poster.jpg`.

Playback uses native controls, starts muted, supports inline mobile playback,
and does not autoplay. The player follows the recording's 2518 × 1166 aspect
ratio. A load error restores the static architecture fallback. See
`static/videos/README.md` for asset details and replacement instructions.

## Update result figures

`static/data/results.json` retains Tables 2, 3 and 4 and the general-capability
scores supplied in the paper's arXiv v1 source. It also records the original
pretrained-model scores from the cross-environment table and selected JevBench
accuracy values, with source-file hashes. Main agent / capability exhibits use
**Qwen3.5-9B with GRPO**; JevBench uses **Qwen3.5-4B** as in the paper.
Captions identify these settings. JevBench values are manuscript results, not
measurements copied from the current benchmark leaderboard.

To regenerate both visible tables, the adjacent JevBench analysis, the six desktop/mobile result SVGs,
and the stacked mobile concept figure:

```sh
uv run scripts/update_results.py
```

The JevBench analysis computes its percentage-point gains from the same selected
rows as the table. The script declares its Matplotlib dependency through PEP 723. This is an authoring
dependency only; serving the website requires no packages or build. Values come
from the paper and the author's manuscript-score backup, not raw seed logs. No
unreported uncertainty intervals are drawn.

## Files and sources

- `index.html`: page narrative, selected evidence and MP4 configuration.
- `static/css/expa.css`: unchanged EARL base stylesheet.
- `static/css/dyad.css`: responsive additions to the flat reference layout.
- `static/js/index.js`: video fallback, capability carousel, citation copy and back-to-top controls.
- `static/images/results-*.svg`: generated desktop and mobile versions of Figures 1 and 2.
- `static/images/dyad-concept*.svg`: original vector concept art and its stacked mobile layout.
- `static/pdfs/dyad-concept.pdf`: unaltered concept figure from the arXiv source.
  Its desktop SVG was rendered with Poppler `pdftocairo -svg`.
- `static/images/dyad-*.png`: original paper figures, including the video fallback.
- `static/pdfs/dyad.pdf`: the original arXiv paper.
- `research/template-provenance.json`: template versions, hashes and result provenance.
- `docs/`: EARL analysis and Dyad editorial decisions.

The public implementation repository is not linked until a verified URL is
supplied. This repository contains the project website.

## Validation

Scores and signed differences are checked against the paper and its source.
Validation covers flat headings, page-local Table/Figure numbering, a single-sentence TL;DR, visible results,
CodeGym-only transfer evidence, generated figures, assets, and mobile rendering. The video
fallback and citation controls remain available. Final MP4 playback must be
checked after the actual video is added.

## Attribution

The upstream template is pinned to
`d38af1ccae1ce82c3404d2820c4c646afd409f81` and derives from
[Nerfies](https://nerfies.github.io/). The visible footer preserves attribution.
See [THIRD_PARTY.md](THIRD_PARTY.md) for licenses and figure provenance.

Local exports, preview environments and raw reference captures are excluded from Git.
