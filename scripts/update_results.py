# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib==3.10.7"]
# ///
"""Generate a visible results table and named result SVGs. Run with uv."""

from decimal import Decimal
from html import escape
import json
from pathlib import Path
import re
import copy
import xml.etree.ElementTree as ET

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.text import Text
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "static/data/results.json").read_text())
MODEL = "Qwen3.5-9B"
ENVIRONMENTS = DATA["environments"]
CAPABILITY_SOURCES = ("CodeGym", "DIVE")
BLUE, GRAY, INK = "#2563eb", "#94a3b8", "#1e293b"
IMAGES = ROOT / "static/images"
plt.rcParams.update({
    "font.family": ["DejaVu Sans", "Arial", "sans-serif"], "font.size": 12, "text.color": INK,
    "axes.labelcolor": INK, "xtick.color": "#64748b", "ytick.color": INK,
    "axes.edgecolor": "#cbd5e1", "axes.spines.top": False,
    "axes.spines.right": False, "axes.spines.left": False,
    "svg.fonttype": "none", "svg.hashsalt": "dyad-project-page",
})


def difference(value, reference):
    return float(Decimal(str(value)) - Decimal(str(reference)))


def signed(value):
    return f"{value:+.2f}".replace("-", "−")


def model_from(records):
    return next(row for row in records if row["model"] == MODEL)


def style_axis(ax):
    ax.set_axisbelow(True)
    ax.grid(axis="x", color="#e2e8f0", linewidth=0.8)
    ax.tick_params(axis="y", length=0, pad=12)
    ax.tick_params(axis="x", length=0, pad=8)


def save(fig, name, mobile, description):
    fig.patch.set_alpha(0)
    for ax in fig.axes:
        ax.set_facecolor("none")
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    canvas = fig.bbox
    for label in fig.findobj(Text):
        if label.get_visible() and label.get_text():
            bounds = label.get_window_extent(renderer)
            if (bounds.x0 < -1 or bounds.y0 < -1 or
                    bounds.x1 > canvas.x1 + 1 or bounds.y1 > canvas.y1 + 1):
                raise ValueError(f"Clipped label in {name}, mobile={mobile}: {label.get_text()}")
    suffix = ".mobile" if mobile else ""
    output = IMAGES / f"results-{name}{suffix}.svg"
    fig.savefig(output, metadata={
        "Date": None, "Creator": "Dyad project page",
        "Title": f"{MODEL}: {name.replace('-', ' ')}",
        "Description": description,
        "Source": DATA["source"],
    })
    output.write_text("\n".join(line.rstrip() for line in output.read_text().splitlines()) + "\n")
    plt.close(fig)


def transfer_chart(mobile):
    row = next(r for r in DATA["cross_environment"]["rows"]
               if r["model"] == MODEL and r["algorithm"] == "GRPO")["CodeGym"]
    row = {**row, "original": model_from(DATA["cross_environment"]["original_models"])["scores"]}
    fig, ax = plt.subplots(figsize=(4.2, 5.8) if mobile else (9.6, 4.6))
    fig.subplots_adjust(left=.34 if mobile else .23, right=.87,
                        bottom=.15, top=.82 if mobile else .84)
    for key, color, offset, label in [
        ("original", "white", -.25, "Original LLM"),
        ("baseline", GRAY, 0, "GRPO"),
        ("dyad", BLUE, .25, "Dyad-GRPO"),
    ]:
        ys = [i + offset for i in range(4)]
        ax.barh(ys, row[key], height=.19, color=color, label=label, zorder=3,
                edgecolor="#94a3b8" if key == "original" else color,
                linewidth=.8 if key == "original" else 0,
                hatch="///" if key == "original" else None)
        for i, (y, value) in enumerate(zip(ys, row[key])):
            label = f"{value:.2f}"
            if key == "dyad":
                delta = signed(difference(value, row["original"][i]))
                if mobile:
                    ax.text(value + 1.2, y + .23, f"({delta}%)", va="center",
                            color=BLUE, fontsize=10)
                else:
                    label += f"  ({delta}%)"
            ax.text(value + 1.2, y, label, va="center",
                    color=BLUE if key == "dyad" else INK,
                    fontsize=11 if mobile else 12)
    ax.set_yticks(range(4), ["ALFWorld", "WebShop", "τ²-bench", "SWE-bench\nVerified"],
                  fontsize=11.5 if mobile else 13)
    ax.invert_yaxis()
    ax.set_xlim(0, 82)
    ax.set_xticks([0, 40, 80] if mobile else [0, 20, 40, 60, 80])
    ax.set_xlabel("Score (%)", labelpad=12, fontsize=11 if mobile else 12)
    style_axis(ax)
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(.51, .99),
               ncol=2 if mobile else 3, frameon=False, fontsize=11 if mobile else 12,
               handlelength=1.1, columnspacing=1.4)
    save(fig, "codegym-transfer", mobile,
         "Figure 1. Agent performance beyond the training environment. Qwen3.5-9B "
         "before training and after CodeGym training with GRPO or Dyad-GRPO. "
         "Scores (%) on four other environments without further training. "
         "Dyad-GRPO annotations show absolute gains (%) over the original LLM.")


def capabilities_chart(mobile, training):
    row = model_from(DATA["general_capabilities"]["models"])
    fig, ax = plt.subplots(figsize=(4.2, 4.6) if mobile else (9.6, 3.5))
    fig.subplots_adjust(left=.37 if mobile else .23, right=.94, bottom=.25, top=.78)
    assert training in CAPABILITY_SOURCES
    baseline = [difference(v, b) for b, v in zip(row["original"], row[training]["GRPO"])]
    dyad = [difference(v, b) for b, v in zip(row["original"], row[training]["Dyad-GRPO"])]
    for i, (b, d) in enumerate(zip(baseline, dyad)):
        ax.plot([b, d], [i, i], color="#cbd5e1", linewidth=2.5, zorder=2)
        ax.scatter([b], [i], s=55, facecolor="white", edgecolor="#64748b", linewidth=1.4, zorder=4)
        ax.scatter([d], [i], s=45, color=BLUE, zorder=5)
        ax.annotate(signed(d), (d, i), xytext=(0, 10), textcoords="offset points",
                    ha="center", va="bottom", color=BLUE, fontsize=11)
        ax.annotate(signed(b), (b, i), xytext=(0, -10), textcoords="offset points",
                    ha="center", va="top", color="#64748b", fontsize=10.5 if mobile else 10)
    ax.set_yticks(range(3), ["Knowledge", "Mathematical\nReasoning", "Coding"], fontsize=11 if mobile else 12)
    ax.set_ylim(2.5, -.55)
    ax.set_xlim(-2.4, 7.1)
    ax.set_xticks([-2, 0, 2, 4, 6])
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:+.0f}" if x else "0"))
    ax.axvline(0, color="#64748b", linewidth=1, linestyle=(0, (4, 3)))
    ax.set_title(f"Trained on {training}", loc="left", fontsize=12 if mobile else 14, pad=22)
    ax.set_xlabel("Absolute change vs. original LLM\n(%)", fontsize=10 if mobile else 11, labelpad=11)
    style_axis(ax)
    fig.legend(handles=[
        Line2D([], [], marker="o", linestyle="none", markerfacecolor="white", markeredgecolor="#64748b", label="GRPO"),
        Line2D([], [], marker="o", linestyle="none", color=BLUE, label="Dyad-GRPO"),
    ], loc="upper center", bbox_to_anchor=(.56, .995), ncol=2, frameon=False,
       fontsize=11 if mobile else 12, columnspacing=1.5, handletextpad=.3)
    save(fig, f"capabilities-{training.lower()}", mobile,
         f"Figure 2. General capabilities after agentic training on {training}. Qwen3.5-9B. Both GRPO and Dyad-GRPO are compared with the "
         "same original model for Knowledge (MMLU-Pro), Mathematical Reasoning (HMMT February 2026), "
         "and Coding (LiveCodeBench v6). Values are absolute score changes (%).")


def frozen_table():
    row = model_from(DATA["frozen_adaptation"]["models"])
    output = [
        '<table id="table1" class="results-table">',
        '<caption id="frozen-caption"><strong>Table 1. Improving decisions with a frozen LLM.</strong> '
        '<strong>Qwen3.5-9B</strong> before and after action-encoder training on DIVE with GRPO. '
        'The LLM stays frozen. Scores (%).</caption>',
        '<colgroup><col style="width:34%"><col style="width:22%"><col style="width:22%"><col style="width:22%"></colgroup>',
        '<thead><tr><th scope="col">Environment</th><th scope="col">Original LLM</th>'
        '<th scope="col">Frozen Dyad</th><th scope="col">Gain (%)</th></tr></thead><tbody>',
    ]
    for name, base, frozen in zip(ENVIRONMENTS, row["base"], row["frozen"]):
        output.append(
            f'<tr><th scope="row">{escape(name)}</th><td>{base:.2f}</td>'
            f'<td class="dyad-score"><strong>{frozen:.2f}</strong></td>'
            f'<td>{signed(difference(frozen, base))}</td></tr>'
        )
    return "\n".join(output + ['</tbody></table>'])


def jevbench_table():
    output = [
        '<table id="table2" class="results-table jevbench-table">',
        '<caption id="jevbench-caption"><strong>Table 2. Direct decisions on JevBench.</strong> '
        'Accuracy (%) on the public subset. The original LLM and Dyad use '
        '<strong>Qwen3.5-4B</strong> with reasoning; Dyad is trained on CodeGym with GRPO.</caption>',
        '<colgroup><col style="width:50%"><col style="width:25%"><col style="width:25%"></colgroup>',
        '<thead><tr><th scope="col">Method</th>'
        '<th scope="col">Overall</th><th scope="col">Hard</th></tr></thead><tbody>',
    ]
    rows = [row for row in DATA["jevbench"]["rows"] if row["reasoning"] != "Off"]
    best = {key: max(row[key] for row in rows) for key in ("overall", "hard")}
    for row in rows:
        cells = []
        for key in ("overall", "hard"):
            text = f'{row[key]:.2f}'
            if row[key] == best[key]:
                text = f'<strong>{text}</strong>'
            css = ' class="dyad-score"' if row["method"] == "Dyad" else ''
            cells.append(f'<td{css}>{text}</td>')
        output.append(f'<tr><th scope="row">{escape(row["method"])}</th>{"".join(cells)}</tr>')
    return "\n".join(output + ['</tbody></table>'])


def jevbench_analysis():
    rows = {row["method"]: row for row in DATA["jevbench"]["rows"]
            if row["reasoning"] == "On"}
    overall = difference(rows["Dyad"]["overall"], rows["Original LLM"]["overall"])
    hard = difference(rows["Dyad"]["hard"], rows["Original LLM"]["hard"])
    return (
        '<p class="section-copy"><a href="https://github.com/fstandhartinger/jevbench" '
        'target="_blank" rel="noopener noreferrer">JevBench</a> evaluates standalone '
        'decisions through classification, yes/no judgments, and ratings. Here, we compare '
        'the jointly trained agent with a dedicated System 1 model, complementing '
        'the multi-step evaluations above.</p>\n'
        '<p class="section-copy"><strong class="dyad-name">Dyad</strong> achieves absolute gains of '
        f'<strong class="key-emphasis">{overall:.2f}% overall</strong> and '
        f'<strong class="key-emphasis">{hard:.2f}% on hard cases</strong> over the original LLM. '
        'It also slightly exceeds Jev on both metrics '
        '(<a href="#table2" class="ref-link">Table 2</a>).</p>'
    )


def concept_mobile():
    """Stack the three original vector panels for a readable narrow-screen figure."""
    namespace = "http://www.w3.org/2000/svg"
    xlink = "http://www.w3.org/1999/xlink"
    ET.register_namespace("", namespace)
    ET.register_namespace("xlink", xlink)
    tag = lambda name: f"{{{namespace}}}{name}"
    original = ET.parse(IMAGES / "dyad-concept.svg").getroot()
    _, _, width, height = map(float, original.get("viewBox").split())
    panel_width, gap = width / 3, 16
    total_height = height * 3 + gap * 2
    result = ET.Element(tag("svg"), {
        "width": f"{panel_width:g}pt", "height": f"{total_height:g}pt",
        "viewBox": f"0 0 {panel_width:g} {total_height:g}",
    })
    ET.SubElement(result, tag("title")).text = "System 1, System 2, and Dyad"
    defs = ET.SubElement(result, tag("defs"))
    artwork = ET.SubElement(defs, tag("g"), {"id": "concept-source"})
    for child in original:
        artwork.append(copy.deepcopy(child))
    for i in range(3):
        panel = ET.SubElement(result, tag("svg"), {
            "x": "0", "y": f"{i * (height + gap):g}",
            "width": f"{panel_width:g}", "height": f"{height:g}",
            "viewBox": f"{i * panel_width:g} 0 {panel_width:g} {height:g}",
        })
        ET.SubElement(panel, tag("use"), {f"{{{xlink}}}href": "#concept-source"})
    ET.indent(result)
    ET.ElementTree(result).write(IMAGES / "dyad-concept.mobile.svg", encoding="unicode")
    with (IMAGES / "dyad-concept.mobile.svg").open("a") as stream:
        stream.write("\n")


def main():
    page = ROOT / "index.html"
    markup = page.read_text()
    for name, render in [("jevbench", jevbench_table), ("jevbench-analysis", jevbench_analysis),
                         ("frozen", frozen_table)]:
        pattern = re.compile(rf"(<!-- results:{name}:start -->).*?(<!-- results:{name}:end -->)", re.S)
        markup, count = pattern.subn(lambda m: f"{m[1]}\n{render()}\n{m[2]}", markup)
        if count != 1:
            raise ValueError(f"Expected one {name} results block, found {count}")
    for mobile in (False, True):
        transfer_chart(mobile)
        for training in CAPABILITY_SOURCES:
            capabilities_chart(mobile, training)
    concept_mobile()
    page.write_text(markup)
    print("Updated Tables 1–2, JevBench analysis and desktop/mobile result SVGs for Figures 1–2.")


if __name__ == "__main__":
    main()
