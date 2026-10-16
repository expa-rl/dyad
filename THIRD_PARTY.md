# Template and asset attribution

The Dyad page uses the layout and styling of [ExpA / EARL](https://expa-rl.github.io/), which uses [Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template), originally derived from [Nerfies](https://nerfies.github.io/).

- Template revision: `d38af1ccae1ce82c3404d2820c4c646afd409f81`.
- `static/css/bulma.min.css` was obtained from that repository at the revision above. Bulma's included copyright and MIT license notice are retained in the file.
- `static/css/expa.css` is the reference site's stylesheet, retrieved on 2026-10-15 and retained as the base theme.
- The page structure and the clipboard / scroll controls are adapted from the reference and template. Dyad-specific changes are in `index.html`, `static/css/dyad.css`, and `static/js/index.js`.
- The website-template adaptations follow [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Attribution is retained in the visible footer. This does not relicense the paper, its figures, or third-party dependencies.
- The three `dyad-*.png` figures are cropped from Figures 1, 2 and 3 of [the Dyad paper](https://arxiv.org/pdf/2609.36116). They are original paper figures, not new experimental visualizations. `static/pdfs/dyad.pdf` is the original paper downloaded from arXiv.
- Publication metadata, author affiliations and table values are transcribed from arXiv:2609.36116v1. Website descriptions are abbreviated paraphrases.
- `static/data/results.json` transcribes Tables 2, 3, 4 and 5 (including the original pretrained-model baselines and JevBench accuracy) and the exact general-capability scores backed up in `resources/figures/figure_general_capabilities.tex` in the [arXiv v1 source archive](https://arxiv.org/src/2609.36116v1). These are author-provided manuscript scores, not raw run logs.
- `static/images/results-*.svg` are new Matplotlib presentations of selected Qwen3.5-9B/GRPO results: CodeGym-trained agent scores alongside the original LLM (page Figure 2), and paired general-capability changes (page Figure 3). `scripts/update_results.py` generates desktop/mobile SVGs and the directly visible JevBench and frozen-adaptation tables (page Tables 1–2). Page Figure 4 uses the original architecture overview while awaiting the MP4. The result SVGs are not cropped paper figures.

The original upstream README is saved in `research/template-upstream-readme.md`. Retrieval details and file hashes are in `research/template-provenance.json`.

Institution marks used in the author-affiliation area are documented in [affiliation asset sources and credits](docs/affiliation-assets.md), including the Wikimedia Commons Microsoft Research wordmark attribution (V-gthom; blue edition by LsnIg334, CC BY-SA 3.0). Official marks retain their respective ownership; the template license does not apply to them.

Page Figure 1 uses the unaltered conceptual artwork from `resources/figures/dyad_comparison_no_caption.pdf` in the arXiv source, retained as `static/pdfs/dyad-concept.pdf`. Its desktop SVG is a Poppler rendering. The mobile SVG stacks the same three vector panels without redrawing them. JevBench scores on this page are the paper’s public-subset measurements, not the benchmark maintainer’s current leaderboard.
