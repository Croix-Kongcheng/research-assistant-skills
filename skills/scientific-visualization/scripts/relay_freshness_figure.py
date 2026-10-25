"""Original synthetic UAV relay illustration; not an experiment or performance claim.

Copyright (c) 2026, the authors of this demonstration. All rights reserved.
SPDX-License-Identifier: BSD-2-Clause

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.transforms import ScaledTranslation
import numpy as np


def make_figure(output_dir: Path) -> dict:
    """Write an original figure from fixed illustrative arrays; return provenance."""
    output_dir.mkdir(parents=True, exist_ok=True)
    time = np.arange(0.0, 9.0)
    age_a = np.array([0.2, 1.2, 0.1, 1.1, 2.1, 0.2, 1.2, 0.1, 1.1])
    age_b = np.array([0.6, 0.1, 1.1, 2.1, 0.2, 1.2, 0.1, 1.1, 2.1])
    limit = 2.0
    buses = np.array([[0.0, 0.0], [0.7, 0.3], [1.4, 0.0], [2.1, 0.5]])
    branch_indices = np.array([[0, 1], [1, 2], [2, 3]])
    relays = np.array([[0.7, 1.2], [1.7, 1.3]])
    colors = {"Relay A": "#0072B2", "Relay B": "#D55E00"}
    style = {
        "font.family": "DejaVu Sans",
        "font.size": 8,
        "axes.labelsize": 8,
        "axes.titlesize": 9,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "lines.linewidth": 1.3,
        "savefig.facecolor": "white",
    }
    with matplotlib.rc_context(style):
        fig = plt.figure(figsize=(6.6, 2.8), layout="constrained")
        gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.4])
        map_ax = fig.add_subplot(gs[0, 0])
        age_ax = fig.add_subplot(gs[0, 1])
        map_ax.add_collection(LineCollection(buses[branch_indices], colors="0.4", linewidths=1.2))
        map_ax.plot(buses[:, 0], buses[:, 1], "o", color="0.2", markersize=3.5)
        for i, (position, name) in enumerate(zip(relays, colors)):
            color = colors[name]
            map_ax.plot(*position, marker="^", color=color, markersize=6)
            ground_bus = buses[1 + i]
            map_ax.plot([position[0], ground_bus[0]], [position[1], ground_bus[1]],
                        linestyle="--", color=color, linewidth=1)
            map_ax.annotate(name, position, xytext=(0, 7), textcoords="offset points",
                            ha="center", color=color)
        map_ax.text(0.8, -0.22, "Feeder buses", ha="center", color="0.25")
        map_ax.set(xlim=(-0.2, 2.35), ylim=(-0.35, 1.75),
                   xlabel="East (km)", ylabel="North (km)", title="Illustrative relay geometry")
        map_ax.set_aspect("equal", adjustable="box")
        for age, name, marker in [(age_a, "Relay A", "o"), (age_b, "Relay B", "s")]:
            age_ax.plot(time, age, label=name, color=colors[name], marker=marker,
                        markersize=3, linestyle="-" if name == "Relay A" else "--")
        age_ax.axhline(limit, color="0.35", linestyle=":", linewidth=1)
        age_ax.annotate("Illustrative limit", (0.15, limit), xytext=(0, 4),
                        textcoords="offset points", va="bottom", color="0.3")
        age_ax.set(xlabel="Time (min)", ylabel="Message age (min)",
                   title="Synthetic age samples", xlim=(-0.2, 8.3), ylim=(0, 2.65))
        age_ax.set_xticks([0, 2, 4, 6, 8])
        age_ax.set_yticks([0, 1, 2])
        age_ax.legend(loc="upper right", frameon=False, fontsize=7)
        for ax, label in [(map_ax, "A"), (age_ax, "B")]:
            offset = ScaledTranslation(3 / 72, -3 / 72, fig.dpi_scale_trans)
            ax.text(0, 1, label, transform=ax.transAxes + offset,
                    fontweight="bold", va="top", ha="left")
        fig.suptitle("Synthetic illustration — no restoration performance results", fontsize=9)
        fig.canvas.draw()
        canvas_size = list(fig.canvas.get_width_height())
        for extension in ("png", "pdf", "svg"):
            fig.savefig(output_dir / f"relay-freshness.{extension}", dpi=180)
        plt.close(fig)
    provenance = {
        "purpose": "Original synthetic design illustration, not experimental evidence",
        "data_kind": "fixed illustrative arrays; no measurements or restoration simulation",
        "units": {"position": "km", "time": "min", "message_age": "min"},
        "time": time.tolist(),
        "relay_a_age": age_a.tolist(),
        "relay_b_age": age_b.tolist(),
        "illustrative_limit": limit,
        "feeder_bus_positions": buses.tolist(),
        "relay_positions": relays.tolist(),
        "figure_inches": [6.6, 2.8],
        "canvas_pixels_at_screen_dpi": canvas_size,
        "export_dpi": 180,
        "numpy_version": np.__version__,
        "matplotlib_version": matplotlib.__version__,
    }
    (output_dir / "relay-freshness.provenance.json").write_text(
        json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    return provenance


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(make_figure(args.output_dir), indent=2))


if __name__ == "__main__":
    main()
