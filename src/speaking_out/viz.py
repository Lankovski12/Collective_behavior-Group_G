"""Custom Solara/Mesa visualisation components."""
from __future__ import annotations

import numpy as np
import solara
from matplotlib.figure import Figure
from mesa.visualization.utils import update_counter

COLORS = {1: "#d62728", 2: "#1f77b4", 3: "#f9abda"}   # A, B, AB
LABELS = {1: "A", 2: "B", 3: "AB (knows both)"}


def draw_agents(model, ax, show_last_group=True):
    """Draw every agent as a dot coloured by its vocabulary."""
    agents = model._agents_list
    xy = model.layout
    vocab = np.array([a.vocab for a in agents])
    committed = np.array([a.committed for a in agents])
    size = float(np.clip(30000 / model.n, 4, 60))

    for v in (1, 2, 3):
        m = (vocab == v) & ~committed
        ax.scatter(xy[m, 0], xy[m, 1], s=size, c=COLORS[v], linewidths=0,
                   label=f"{LABELS[v]}  ({m.sum()})")
    if committed.any():
        ax.scatter(xy[committed, 0], xy[committed, 1], s=size * 2.2,
                   c=COLORS[1], edgecolors="black", linewidths=1.0, marker="D",
                   label=f"committed A  ({committed.sum()})")

    if show_last_group and model.last_group is not None:
        spk, hrs = model.last_group
        for h in hrs:
            ax.plot(*zip(xy[spk], xy[h]), color="black", lw=0.8, alpha=0.7, zorder=0)
        ax.scatter(*xy[spk], s=size * 5, facecolors="none", edgecolors="black",
                   linewidths=1.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 0.0), ncol=2,
              frameon=False, fontsize=8, markerscale=1.5)
    ax.set_title(f"Agents  (interaction {model.interactions:,})", fontsize=10)


@solara.component
def AgentPlot(model, show_last_group=True):
    update_counter.get()  # re-render whenever the model steps
    fig = Figure(figsize=(5, 5.6))
    draw_agents(model, fig.subplots(), show_last_group)
    solara.FigureMatplotlib(fig, format="png", bbox_inches="tight")


def make_agent_plot_component(show_last_group=True, page=0):
    def Make(model):
        return AgentPlot(model, show_last_group)
    return (Make, page)