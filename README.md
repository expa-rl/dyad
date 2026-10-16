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
3. **Modular Adaptation with a Frozen LLM**: visible Table 1 compares the
   original model and frozen-LLM adaptation in four environments.
4. **Cross-environment Generalization**: Figure 1 shows the CodeGym-trained
   agent in four other environments, including scores and paired improvements.
5. **Preserving General Capabilities**: Figure 2 shows six comparisons, retaining both
   DIVE and CodeGym and all three capability benchmarks.
6. **Approach**: Figure 3 reserves the MP4 location, with architecture fallback
   and paragraphs describing inference and training.
7. Copyable BibTeX and template attribution.

EARL's 960px desktop container is reused for both text and evidence. Each numbered
section has one heading followed directly by paragraphs. Dense full-result panels,
duplicated category labels, and expandable experiment sections are removed.
Each chart has a separate mobile SVG with all selected values labelled directly.
Table 1 is visible HTML. Every exhibit has its own page number, name and caption;
there are no hidden data tables or expandable results. Model specifications are
kept in captions, while prose explains the research problems and capability gains.

## Add the Approach MP4

The final video has not been supplied. Until configured, this section shows
the architecture figure with a "Video walkthrough coming soon" label.

1. Save the video as `static/videos/dyad-approach.mp4`.
2. In `index.html`, set `data-video-src` on `#approach-video`:

   ```html
   data-video-src="static/videos/dyad-approach.mp4"
   ```

A hosted MP4 URL also works. Playback uses native controls, supports inline
mobile playback and does not autoplay. A load error restores the architecture
fallback. See `static/videos/README.md` for captions setup.

## Update result figures

`static/data/results.json` retains Tables 2, 3 and 4 and the general-capability
scores supplied in the paper's arXiv v1 source. Its metadata records the source
file and hash. The page consistently selects **Qwen3.5-9B with GRPO** as its main
example; captions state the training source and evaluation scope of each exhibit.

To regenerate visible Table 1 and the four desktop/mobile SVG assets:

```sh
uv run scripts/update_results.py
```

The script declares its Matplotlib dependency through PEP 723. This is an authoring
dependency only; serving the website requires no packages or build. Values come
from the paper and the author's manuscript-score backup, not raw seed logs. No
unreported uncertainty intervals are drawn.

## Files and sources

- `index.html`: page narrative, selected evidence and MP4 configuration.
- `static/css/expa.css`: unchanged EARL base stylesheet.
- `static/css/dyad.css`: responsive additions to the flat reference layout.
- `static/js/index.js`: video fallback, citation copy and back-to-top controls.
- `static/images/results-*.svg`: generated desktop and mobile versions of Figures 1 and 2.
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
