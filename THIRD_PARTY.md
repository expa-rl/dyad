# Template and asset attribution

The Dyad page uses the layout and styling of [ExpA / EARL](https://expa-rl.github.io/), which uses [Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template), originally derived from [Nerfies](https://nerfies.github.io/).

- Template revision: `d38af1ccae1ce82c3404d2820c4c646afd409f81`.
- `static/css/bulma.min.css` was obtained from that repository at the revision above. Bulma's included copyright and MIT license notice are retained in the file.
- `static/css/expa.css` is the reference site's stylesheet, retrieved on 2026-10-15 and retained as the base theme.
- The page structure and the clipboard / scroll controls are adapted from the reference and template. Dyad-specific changes are in `index.html`, `static/css/dyad.css`, and `static/js/index.js`.
- The website-template adaptations follow [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Attribution is retained in the visible footer. This does not relicense the paper, its figures, or third-party dependencies.
- The three `dyad-*.png` figures are cropped from Figures 1, 2 and 3 of [the Dyad paper](https://arxiv.org/pdf/2609.36116). They are original paper figures, not new experimental visualizations. `static/pdfs/dyad.pdf` is the original paper downloaded from arXiv.
- Publication metadata, author affiliations and table values are transcribed from arXiv:2609.36116v1. Website descriptions are abbreviated paraphrases.
- `static/data/results.json` transcribes Tables 2, 3 and 4. The cross-environment heatmap is a new HTML presentation of all 48 paired differences from Table 3; it includes gains and regressions. `scripts/update_results.py` generates the static result tables.

The original upstream README is saved in `research/template-upstream-readme.md`. Retrieval details and file hashes are in `research/template-provenance.json`.
