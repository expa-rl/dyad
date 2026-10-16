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
CAPABILITY_SOURCES = ("DIVE", "CodeGym")
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
    fig, ax = plt.subplots(figsize=(4, 4.5) if mobile else (9.6, 3.8))
    fig.subplots_adjust(left=.34 if mobile else .23, right=.72 if mobile else .80,
                        bottom=.19 if mobile else .20, top=.83)
    for key, color, offset, label in [
        ("baseline", GRAY, -.17, "GRPO"),
        ("dyad", BLUE, .17, "Dyad-GRPO"),
    ]:
        ys = [i + offset for i in range(4)]
        ax.barh(ys, row[key], height=.25, color=color, label=label, zorder=3)
        for i, (y, value) in enumerate(zip(ys, row[key])):
            text = f"{value:.2f}"
            if key == "dyad":
                text += f" ({signed(difference(value, row['baseline'][i]))})"
            ax.text(value + 1.0, y, text, va="center",
                    color=INK if key == "baseline" else BLUE,
                    fontsize=10.5 if mobile else 12)
    ax.set_yticks(range(4), ["ALFWorld", "WebShop", "τ²-bench", "SWE-bench\nVerified"],
                  fontsize=11.5 if mobile else 13)
    ax.invert_yaxis()
    ax.set_xlim(0, 85)
    ax.set_xticks([0, 40, 80] if mobile else [0, 20, 40, 60, 80])
    ax.set_xlabel("Score (%)", labelpad=12, fontsize=11 if mobile else 12)
    style_axis(ax)
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(.55, .99),
               ncol=2, frameon=False, fontsize=11 if mobile else 12,
               handlelength=1.1, columnspacing=1.4)
    save(fig, "codegym-transfer", mobile,
         "Figure 1. Generalization to unseen environments. Qwen3.5-9B trained on CodeGym: "
         "GRPO versus Dyad-GRPO scores on four other environments. Parentheses show "
         "percentage-point improvements. Three evaluation seeds, no further adaptation.")


def capabilities_chart(mobile):
    row = model_from(DATA["general_capabilities"]["models"])
    fig, axes = plt.subplots(2, 1, figsize=(4, 6.2)) if mobile else plt.subplots(1, 2, figsize=(9.6, 3.9))
    fig.subplots_adjust(left=.37 if mobile else .19, right=.94 if mobile else .97,
                        bottom=.16 if mobile else .24, top=.84 if mobile else .76,
                        hspace=.86, wspace=.85)
    for ax, training in zip(axes, CAPABILITY_SOURCES):
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
        ax.set_yticks(range(3), ["MMLU-Pro", "HMMT", "LiveCodeBench"], fontsize=11 if mobile else 12)
        ax.set_ylim(2.5, -.55)
        ax.set_xlim(-2.4, 7.1)
        ax.set_xticks([-2, 0, 2, 4, 6])
        ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:+.0f}" if x else "0"))
        ax.axvline(0, color="#64748b", linewidth=1, linestyle=(0, (4, 3)))
        ax.set_title(f"Trained on {training}", loc="left", fontsize=12 if mobile else 14, pad=20)
        ax.set_xlabel("Change vs. original LLM\n(percentage points)", fontsize=10 if mobile else 11, labelpad=11)
        style_axis(ax)
    fig.legend(handles=[
        Line2D([], [], marker="o", linestyle="none", markerfacecolor="white", markeredgecolor="#64748b", label="GRPO"),
        Line2D([], [], marker="o", linestyle="none", color=BLUE, label="Dyad-GRPO"),
    ], loc="upper center", bbox_to_anchor=(.56, .995), ncol=2, frameon=False,
       fontsize=11 if mobile else 12, columnspacing=1.5, handletextpad=.3)
    save(fig, "capabilities", mobile,
         "Figure 2. Retaining knowledge, reasoning and coding after agentic training. Qwen3.5-9B. Both GRPO and Dyad-GRPO are compared with the "
         "same original model on MMLU-Pro, HMMT February 2026 and LiveCodeBench v6. "
         "Connecting lines are paired comparisons, not uncertainty intervals. Three evaluation seeds.")


def frozen_table():
    row = model_from(DATA["frozen_adaptation"]["models"])
    output = [
        '<table id="table1" class="results-table">',
        '<caption id="frozen-caption"><strong>Table 1. Modular adaptation without updating the LLM.</strong> '
        'Scores (%) for <strong>Qwen3.5-9B</strong> before and after training the action encoder with GRPO '
        'on DIVE, while keeping the LLM and language head fixed. Evaluation uses three seeds in four '
        'other environments, without further training. Changes are in percentage points.</caption>',
        '<colgroup><col style="width:34%"><col style="width:22%"><col style="width:22%"><col style="width:22%"></colgroup>',
        '<thead><tr><th scope="col">Environment</th><th scope="col">Original LLM</th>'
        '<th scope="col">Frozen Dyad</th><th scope="col">Change (pp)</th></tr></thead><tbody>',
    ]
    for name, base, frozen in zip(ENVIRONMENTS, row["base"], row["frozen"]):
        output.append(
            f'<tr><th scope="row">{escape(name)}</th><td>{base:.2f}</td>'
            f'<td class="dyad-score"><strong>{frozen:.2f}</strong></td>'
            f'<td>{signed(difference(frozen, base))}</td></tr>'
        )
    return "\n".join(output + ['</tbody></table>'])


def main():
    page = ROOT / "index.html"
    markup = page.read_text()
    pattern = re.compile(r"(<!-- results:frozen:start -->).*?(<!-- results:frozen:end -->)", re.S)
    markup, count = pattern.subn(lambda m: f"{m[1]}\n{frozen_table()}\n{m[2]}", markup)
    if count != 1:
        raise ValueError(f"Expected one frozen results block, found {count}")
    for mobile in (False, True):
        transfer_chart(mobile)
        capabilities_chart(mobile)
    page.write_text(markup)
    print("Updated visible Table 1 and four desktop/mobile SVGs for Figures 1 and 2.")


if __name__ == "__main__":
    main()
