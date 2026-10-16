"""Regenerate the page's static results from paper-backed JSON. No dependencies."""

from decimal import Decimal
from html import escape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "static/data/results.json").read_text())
LABELS = [("ALF", "ALFWorld"), ("Web", "WebShop"), ("τ²", "τ²-bench"), ("SWE", "SWE-bench Verified")]


def score(value):
    return f"{value:.2f}"


def score_table(models, compact=False):
    heads = "".join(f'<th scope="col"><abbr title="{full}">{short}</abbr></th>' for short, full in LABELS)
    output = [f'<table class="results-table frozen-table"><caption>{"Qwen3.5-9B · " if compact else ""}GRPO on DIVE · 3 evaluation seeds</caption><thead><tr><th scope="col">Method</th>{heads}</tr></thead><tbody>']
    for model in models:
        if not compact:
            output.append(f'<tr class="model-row"><th colspan="5" scope="rowgroup">{escape(model["model"])}</th></tr>')
        for key, label in [("base", "Base model"), ("frozen", "+ Dyad · frozen LLM"), ("joint", "+ Dyad · joint training")]:
            row_class = ' class="dyad-result"' if key == "frozen" else ""
            cells = "".join(f'<td class="num" data-score="{score(v)}">{score(v)}</td>' for v in model[key])
            output.append(f'<tr{row_class}><th scope="row">{label}</th>{cells}</tr>')
    output.append("</tbody></table>")
    return "\n".join(output)


def in_domain():
    output = ['<table class="results-table in-domain-table"><caption>Qwen3.5-9B · 3 evaluation seeds</caption><thead><tr><th scope="col">Method</th><th scope="col">ALFWorld</th><th scope="col">WebShop</th></tr></thead><tbody>']
    for row in DATA["in_domain"]["rows"]:
        row_class = ' class="dyad-result"' if "Dyad" in row["method"] else ""
        cells = "".join(f'<td class="num" data-score="{score(v)}">{score(v)}</td>' for v in row["scores"])
        output.append(f'<tr{row_class}><th scope="row">{escape(row["method"])}</th>{cells}</tr>')
    output.append("</tbody></table>")
    return "\n".join(output)


def cross_environment():
    heads = "".join(f'<th scope="col"><abbr title="{full}">{short}</abbr></th>' for short, full in LABELS) * 2
    output = ['<table class="heatmap-table"><caption>Change from the corresponding RL baseline (percentage points)</caption><thead><tr><th scope="col" rowspan="2">Qwen3.5<br>+ Dyad</th><th scope="colgroup" colspan="4">Trained on DIVE</th><th scope="colgroup" colspan="4">Trained on CodeGym</th></tr>', f"<tr>{heads}</tr></thead><tbody>"]
    for row in DATA["cross_environment"]["rows"]:
        size = row["model"].removeprefix("Qwen3.5-")
        output.append(f'<tr><th scope="row">{size}<span>{row["algorithm"]}</span></th>')
        for training in ("DIVE", "CodeGym"):
            for i, (baseline, dyad) in enumerate(zip(row[training]["baseline"], row[training]["dyad"])):
                delta = Decimal(str(dyad)) - Decimal(str(baseline))
                signed = f"{delta:+.2f}"
                tone = "gain" if delta > 0 else "loss" if delta < 0 else "neutral"
                alpha = .08 + min(abs(float(delta)) / 6.16, 1) * .28
                label = f'{row["model"]}, {row["algorithm"]}, trained on {training}, evaluated on {LABELS[i][1]}: {score(baseline)} to {score(dyad)}, {signed} percentage points'
                output.append(f'<td class="{tone}" style="--cell-alpha:{alpha:.3f}" data-delta="{signed}" aria-label="{escape(label)}" title="{escape(label)}">{signed}</td>')
        output.append("</tr>")
    output.append("</tbody></table>")
    return "\n".join(output)


def main():
    page = ROOT / "index.html"
    markup = page.read_text()
    models = DATA["frozen_adaptation"]["models"]
    blocks = {
        "frozen-preview": score_table([next(m for m in models if m["model"] == "Qwen3.5-9B")], compact=True),
        "frozen-full": score_table(models),
        "in-domain": in_domain(),
        "cross-environment": cross_environment(),
    }
    for name, content in blocks.items():
        pattern = re.compile(rf"(<!-- results:{name}:start -->).*?(<!-- results:{name}:end -->)", re.S)
        markup, count = pattern.subn(lambda m: f"{m[1]}\n{content}\n{m[2]}", markup)
        if count != 1:
            raise ValueError(f"Expected one results block for {name}, found {count}")
    page.write_text(markup)
    print("Updated four static result tables from static/data/results.json")


if __name__ == "__main__":
    main()
