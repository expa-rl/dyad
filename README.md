# Dyad project page

Project website for **Dyad: Extending Large Language Models with Native Typed
Decision-Making** ([paper](https://arxiv.org/abs/2609.36116)).

Adapted from [ExpA / EARL](https://expa-rl.github.io/) and its upstream
[Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template).
The page is plain HTML, CSS and JavaScript, with no installation or build step.

## Local preview

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000/>.

## Content and layout

1. Paper title, authors, affiliations and resource links.
2. TL;DR and the paper's conceptual comparison.
3. Frozen-LLM adaptation, with a compact Qwen3.5-9B comparison and expandable results for all four models.
4. Joint optimization: in-domain scores and all 48 cross-environment comparisons.
5. General knowledge, mathematical reasoning and coding results.
6. Approach video, the two training settings and expandable further analysis.
7. Copyable BibTeX and template attribution.

The reading column is 740px wide and figures can use 1040px. Desktop layouts
place frozen-adaptation text beside its table and the two joint-training results
beside each other. At smaller widths, these sections stack; wide tables scroll
inside their own containers.

## Add the Approach MP4

The final video has not been supplied. Until configured, this section shows
the architecture figure with a "Video walkthrough coming soon" label.

1. Save the video as `static/videos/dyad-approach.mp4`.
2. In `index.html`, set the `data-video-src` attribute on `#approach-video`:

   ```html
   data-video-src="static/videos/dyad-approach.mp4"
   ```

A hosted MP4 URL also works. Playback uses native controls, supports inline
mobile playback and does not autoplay. A load error restores the architecture
fallback. See `static/videos/README.md` for the poster and captions setup.

## Update results

`static/data/results.json` contains the scores transcribed from Tables 2, 3 and 4
of arXiv:2609.36116v1. To regenerate the four static HTML tables after updating it:

```sh
python3 scripts/update_results.py
```

The cross-environment heatmap shows **percentage-point changes from the paired
RL baseline**, including all seven regressions. Each cell also identifies the
underlying baseline and Dyad scores. Site visitors do not need JavaScript to
read these tables.

## Files and sources

- `index.html`: page content and the MP4 configuration.
- `static/css/expa.css`: unchanged EARL base stylesheet.
- `static/css/dyad.css`: layout, typography and responsive adaptations.
- `static/js/index.js`: video fallback, citation copy and back-to-top controls.
- `static/images/`: original paper figures and the favicon.
- `static/pdfs/dyad.pdf`: the arXiv paper.
- `research/template-provenance.json`: template versions, source hashes and figure locations.

Paper information and experimental values come from the original PDF. The
public implementation repository is not linked until a verified URL is supplied.
This repository contains the project website.

## Validation

The results JSON was checked against the original PDF, including the 48 signed
cross-environment differences. HTML structure, local resources, JavaScript syntax
and the unchanged EARL stylesheet hash were checked. Desktop and mobile layouts,
the expanded results and citation feedback were inspected in the browser.
Final MP4 playback remains to be checked after the actual video is added.

## Attribution

The upstream template is pinned to
`d38af1ccae1ce82c3404d2820c4c646afd409f81` and derives from
[Nerfies](https://nerfies.github.io/). The visible footer preserves attribution.
See [THIRD_PARTY.md](THIRD_PARTY.md) for licenses and figure provenance.

Local presentation exports, intermediate build files and raw reference-page
captures are excluded from Git. Template provenance remains included.
