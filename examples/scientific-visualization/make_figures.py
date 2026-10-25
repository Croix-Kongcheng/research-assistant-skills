"""Two original, reproducible scientific-visualization demonstrations.

SPDX-License-Identifier: BSD-2-Clause
Copyright (c) 2026 Croix-Kongcheng and contributors.
See LICENSE-CODE. Input data are invented mathematical examples, not experiments.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import heapq
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle, Rectangle
import numpy as np

INK = "#18334a"
MUTED = "#64778b"
BLUE = "#3768ad"
TEAL = "#00867d"
ORANGE = "#c77a32"
BG = "#f7fafc"


def style() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11,
        "text.color": INK, "axes.labelcolor": INK,
        "xtick.color": MUTED, "ytick.color": MUTED,
        "axes.edgecolor": "#bdcad6", "axes.spines.top": False,
        "axes.spines.right": False, "axes.titleweight": "bold",
        "figure.facecolor": "white", "savefig.facecolor": "white",
        "svg.fonttype": "none", "pdf.fonttype": 42,
        "axes.unicode_minus": True,
    })


def save(fig: plt.Figure, output: Path, stem: str) -> None:
    for extension in ("png", "svg", "pdf"):
        target = output / f"{stem}.{extension}"
        fig.savefig(target, dpi=200)
        if extension == "svg":
            # Matplotlib emits trailing spaces inside multiline path data.
            # Normalize formatting without changing the graphic or text.
            target.write_text("\n".join(line.rstrip() for line in target.read_text(encoding="utf-8").splitlines()) + "\n",
                              encoding="utf-8", newline="\n")
    plt.close(fig)


def write_csv(path: Path, header: list[str], rows) -> None:
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def grid_path(blocked, risk, start, goal, cell_km, risk_weight):
    """Eight-neighbour Dijkstra; forbid diagonal corner cutting."""
    distance = np.full(blocked.shape, np.inf)
    distance[start] = 0
    previous = {}
    heap = [(0.0, start)]
    while heap:
        cost, current = heapq.heappop(heap)
        if cost > distance[current]:
            continue
        if current == goal:
            break
        row, col = current
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1),
                       (-1, -1), (-1, 1), (1, -1), (1, 1)):
            nr, nc = row + dr, col + dc
            if not (0 <= nr < blocked.shape[0] and 0 <= nc < blocked.shape[1]):
                continue
            if blocked[nr, nc]:
                continue
            if dr and dc and (blocked[row, nc] or blocked[nr, col]):
                continue
            ds = cell_km * np.hypot(dr, dc)
            local_risk = (risk[row, col] + risk[nr, nc]) / 2
            candidate = cost + ds * (1 + risk_weight * local_risk)
            if candidate + 1e-12 < distance[nr, nc]:
                distance[nr, nc] = candidate
                previous[(nr, nc)] = current
                heapq.heappush(heap, (candidate, (nr, nc)))
    if not np.isfinite(distance[goal]):
        raise RuntimeError("Demonstration has no feasible route")
    route = [goal]
    while route[-1] != start:
        route.append(previous[route[-1]])
    return np.asarray(route[::-1])


def path_figure(output: Path) -> dict:
    cell = 0.05
    x = np.arange(0, 10 + cell / 2, cell)
    y = np.arange(0, 6 + cell / 2, cell)
    xx, yy = np.meshgrid(x, y)
    risk = np.exp(-(((xx - 5.3) / 1.45) ** 2 + ((yy - 4.05) / 0.9) ** 2) / 2)
    risk += 0.52 * np.exp(-(((xx - 7.9) / 0.9) ** 2 + ((yy - 2.0) / 0.7) ** 2) / 2)
    risk /= risk.max()
    # Rectangle and circle are expanded by half a grid diagonal. This conservative
    # mask keeps segment centre lines outside the original physical obstacles.
    margin = cell * np.sqrt(2) / 2
    blocked = (((xx >= 3.7 - margin) & (xx <= 5.4 + margin) &
                (yy >= 1.7 - margin) & (yy <= 3.5 + margin)) |
               ((xx - 6.7) ** 2 + (yy - 3.6) ** 2 <= (0.52 + margin) ** 2))
    start = (round(3 / cell), round(0.7 / cell))
    goal = (round(3 / cell), round(9.3 / cell))
    results = {}
    cmap = LinearSegmentedColormap.from_list("risk", ["#fafafa", "#fae6ce", "#d68d4c"])
    fig = plt.figure(figsize=(12, 8.2))
    ax = fig.add_axes((0.075, 0.22, 0.76, 0.64))
    cax = fig.add_axes((0.86, 0.28, 0.017, 0.49))
    im = ax.imshow(risk, origin="lower", extent=(-cell/2, 10+cell/2, -cell/2, 6+cell/2),
                   cmap=cmap, vmin=0, vmax=1, interpolation="nearest", rasterized=True)
    colorbar = fig.colorbar(im, cax=cax, ticks=[0, 0.25, 0.5, 0.75, 1])
    colorbar.set_label("Illustrative risk score (unitless)", labelpad=12)
    colorbar.outline.set_visible(False)
    ax.add_patch(Rectangle((3.7, 1.7), 1.7, 1.8, facecolor="#dce3e9", edgecolor="#718294",
                           linewidth=1, hatch="////", zorder=4))
    ax.add_patch(Circle((6.7, 3.6), 0.52, facecolor="#dce3e9", edgecolor="#718294",
                        linewidth=1, hatch="////", zorder=4))
    for key, weight, color, label in (("shortest", 0, BLUE, "Shortest feasible"),
                                      ("risk_weighted", 3, TEAL, "Risk-weighted")):
        route = grid_path(blocked, risk, start, goal, cell, weight)
        coords = np.column_stack((x[route[:, 1]], y[route[:, 0]]))
        ds = np.linalg.norm(np.diff(coords, axis=0), axis=1)
        route_risk = risk[route[:, 0], route[:, 1]]
        exposure = float(np.sum(ds * (route_risk[:-1] + route_risk[1:]) / 2))
        length = float(ds.sum())
        results[key] = {"length_km": length, "risk_exposure_score_km": exposure,
                        "risk_weight": weight, "weighted_cost_km": length + weight * exposure}
        ax.plot(coords[:, 0], coords[:, 1], color="white", linewidth=5.3, zorder=5)
        ax.plot(coords[:, 0], coords[:, 1], color=color, linewidth=2.7, zorder=6,
                label=label)
        write_csv(output / f"route_{key}.csv", ["x_km", "y_km", "risk_score"],
                  zip(coords[:, 0], coords[:, 1], route_risk))
    assert not blocked[start] and not blocked[goal]
    assert results["risk_weighted"]["risk_exposure_score_km"] < results["shortest"]["risk_exposure_score_km"]
    # Each endpoint is the same for both routes; neither strategy is a real study.
    ax.scatter([x[start[1]], x[goal[1]]], [y[start[0]], y[goal[0]]],
               s=74, color=INK, edgecolor="white", linewidth=1.4, zorder=7)
    ax.annotate("START", (x[start[1]], y[start[0]]), xytext=(0, 13),
                textcoords="offset points", ha="center", weight="bold", fontsize=10)
    ax.annotate("GOAL", (x[goal[1]], y[goal[0]]), xytext=(0, 13),
                textcoords="offset points", ha="center", weight="bold", fontsize=10)
    ax.annotate("High-risk region", (5.4, 4.6), xytext=(2.1, 5.45), color=ORANGE,
                arrowprops={"arrowstyle": "-", "color": ORANGE}, fontsize=11)
    ax.text(4.55, 2.45, "NO-FLY\nZONE", ha="center", va="center", fontsize=9.5,
            color="#536879", zorder=8, bbox={"fc": "#e6edf2", "ec": "none", "pad": 3})
    ax.set(xlim=(0, 10), ylim=(0, 6), xlabel="East (km)", ylabel="North (km)")
    ax.set_aspect("equal")
    ax.set_xticks(np.arange(0, 11, 2))
    ax.set_yticks(np.arange(0, 7, 1))
    ax.legend(loc="lower left", frameon=True, framealpha=0.96, facecolor="white",
              edgecolor="none", handlelength=2.7, borderpad=0.9)
    fig.text(0.075, 0.95, "01  /  UAV PATH PLANNING", color=TEAL, fontsize=10, weight="bold")
    fig.text(0.075, 0.90, "A shorter route can carry more exposure", fontsize=21, weight="bold")
    for xpos, key, color, name in ((0.09, "shortest", BLUE, "SHORTEST FEASIBLE"),
                                   (0.48, "risk_weighted", TEAL, "RISK-WEIGHTED")):
        value = results[key]
        fig.text(xpos, 0.15, name, color=color, fontsize=10, weight="bold")
        fig.text(xpos, 0.11, f"{value['length_km']:.2f} km   |   exposure {value['risk_exposure_score_km']:.2f} score-km",
                 fontsize=12, color=INK)
    fig.text(0.075, 0.047,
             "Synthetic mathematical example. Same 50 m grid, obstacles and endpoints; Dijkstra weights 1 or (1 + 3r).\n"
             "Risk is an invented scalar field. Distances and exposure are grid-path values, not aircraft performance.",
             fontsize=9, color=MUTED, linespacing=1.65)
    save(fig, output, "01_uav_route_tradeoff")
    # Full raw grid allows reuse without reverse-engineering the rendered image.
    write_csv(output / "risk_grid.csv", ["x_km", "y_km", "risk_score", "blocked"],
              zip(xx.ravel(), yy.ravel(), risk.ravel(), blocked.astype(int).ravel()))
    return {"grid_spacing_km": cell, "risk_definition": "two Gaussian fields normalized by maximum",
            "gaussians": [{"centre_km": [5.3, 4.05], "scales_km": [1.45, 0.9], "amplitude": 1},
                          {"centre_km": [7.9, 2], "scales_km": [0.9, 0.7], "amplitude": 0.52}],
            "rectangle_km": [3.7, 1.7, 1.7, 1.8], "circle_km": [6.7, 3.6, 0.52],
            "obstacle_mask_margin_km": margin, "start_km": [float(x[start[1]]), 3],
            "goal_km": [float(x[goal[1]]), 3], "routes": results}


def restoration_figure(output: Path) -> dict:
    time = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
    demand_mw = 10.0
    profiles = {
        "Late restoration": np.array([0.15, 0.15, 0.25, 0.25, 0.45, 0.60, 0.75, 0.90, 1.0]),
        "Even restoration": np.array([0.15, 0.25, 0.40, 0.55, 0.70, 0.80, 0.90, 1.00, 1.0]),
        "Early restoration": np.array([0.15, 0.45, 0.65, 0.80, 0.90, 1.00, 1.00, 1.00, 1.0]),
    }
    colors = {"Late restoration": "#929fae", "Even restoration": BLUE, "Early restoration": TEAL}
    shortfall = {key: float(np.sum(np.diff(time) * (1 - value[:-1]) * demand_mw))
                 for key, value in profiles.items()}
    fig = plt.figure(figsize=(12, 7.4))
    ax = fig.add_axes((0.085, 0.28, 0.54, 0.51))
    bx = fig.add_axes((0.735, 0.28, 0.20, 0.51))
    ax.axhline(100, color="#bdcad6", linewidth=1, linestyle=(0, (3, 4)), zorder=1)
    ax.fill_between(time, profiles["Early restoration"] * 100, 100, step="post",
                    color=TEAL, alpha=0.10, linewidth=0, zorder=1)
    for label, values in profiles.items():
        ax.step(time, values * 100, where="post", color=colors[label], linewidth=2.6,
                label=label, zorder=3)
        ax.scatter(time[:-1], values[:-1] * 100, s=21, color=colors[label],
                   edgecolor="white", linewidth=0.65, zorder=4)
    ax.set(xlim=(0, 8), ylim=(0, 108), xlabel="Time after interruption (h)",
           ylabel="Restored demand (%)")
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_xticks(np.arange(0, 9, 1))
    ax.grid(axis="y", color="#e7edf2", linewidth=0.8, zorder=0)
    ax.text(5.15, 103.5, "10 MW fully restored", fontsize=9.5, color=MUTED)
    ax.annotate("Shaded area = unmet demand\nfor the early schedule", xy=(1.45, 79),
                xytext=(0.4, 88), color=TEAL, fontsize=10, linespacing=1.4,
                arrowprops={"arrowstyle": "->", "color": TEAL,
                            "connectionstyle": "arc3,rad=0.22"})
    for index, (label, value) in enumerate(shortfall.items()):
        bx.barh(index, value, color=colors[label], height=0.48)
        bx.text(value + 0.7, index, f"{value:.1f}", va="center", color=INK,
                fontsize=12, weight="bold")
        bx.text(0, index - 0.36, label.replace(" restoration", " schedule"), color=colors[label],
                fontsize=10, weight="bold", va="bottom")
    bx.set(xlim=(0, 46), ylim=(2.7, -0.9), xlabel="Energy not served (MWh)")
    bx.set_xticks([0, 20, 40])
    bx.set_yticks([])
    bx.spines["left"].set_visible(False)
    fig.text(0.085, 0.94, "02  /  DISTRIBUTION RESTORATION", color=TEAL, fontsize=10, weight="bold")
    fig.text(0.085, 0.885, "The timing of recovery changes the energy shortfall", fontsize=20, weight="bold")
    fig.text(0.085, 0.825, "Three invented step schedules, all ending at 100% restoration", color=MUTED, fontsize=11)
    fig.text(0.085, 0.19, "AREA HAS A PHYSICAL MEANING", fontsize=10, weight="bold", color=TEAL)
    fig.text(0.085, 0.142,
             r"$E_{\mathrm{NS}} = D\,\sum_k (1-R_k)\,\Delta t_k$"
             "     |     D = 10 MW; horizon = 8 h; post-step values", fontsize=13)
    fig.text(0.085, 0.06,
             "Synthetic teaching data. No feeder topology, power-flow, routing, uncertainty or optimization is modelled.\n"
             "The graphic explains integration of unmet demand; it does not establish the benefit of any technology.",
             fontsize=9, color=MUTED, linespacing=1.65)
    save(fig, output, "02_restoration_energy")
    write_csv(output / "restoration_schedules.csv", ["time_h", *profiles],
              zip(time, *profiles.values()))
    return {"demand_mw": demand_mw, "horizon_h": 8, "step_convention": "post",
            "time_h": time.tolist(), "restoration_fraction": {k: v.tolist() for k, v in profiles.items()},
            "energy_not_served_mwh": shortfall}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent / "output")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    style()
    metadata = {
        "kind": "synthetic mathematical teaching examples; not experimental evidence",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "numpy_version": np.__version__, "matplotlib_version": matplotlib.__version__,
        "source": "Original scripts and invented inputs; no source-book images or code copied",
        "figure_license": "CC-BY-4.0", "code_license": "BSD-2-Clause",
        "uav_route_tradeoff": path_figure(args.output_dir),
        "restoration_energy": restoration_figure(args.output_dir),
    }
    (args.output_dir / "parameters-and-results.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output_dir": str(args.output_dir), "routes": metadata["uav_route_tradeoff"]["routes"],
                      "energy_not_served_mwh": metadata["restoration_energy"]["energy_not_served_mwh"]}, indent=2))


if __name__ == "__main__":
    main()
