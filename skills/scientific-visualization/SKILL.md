---
name: scientific-visualization
license: CC-BY-NC-SA-4.0; scripts BSD-2-Clause
description: "Design and review publication figures with Nicolas P. Rougier's Scientific Visualization: Python & Matplotlib. Use for visual encoding, typography, coordinate transforms, figure layout, annotations, and export quality; for ordinary plotting syntax alone, use general Matplotlib guidance."
---

# Scientific Visualization: Python & Matplotlib

Use Rougier's figure-design judgment to turn data into a readable, faithful graphical argument. This skill assumes intermediate Python and basic NumPy. It emphasizes publication figures and deliberately crafted graphics; it is not a general Python course or a catalogue of plotting functions.

Source: Nicolas P. Rougier, first edition, November 2021. Coverage: 13 numbered chapters, 12 showcase essays, two appendices, front matter and conclusion. The showcases are grouped because each is a short technique note, not an additional numbered chapter. The book is credited as a source, not needed at runtime; all routed guides are bundled.

## Start with the figure's job

1. Identify the audience, the one message to communicate, the evidence that supports it, and the final medium and physical dimensions. Infer routine choices from the task; ask only for missing information that changes the design.
2. Select the simplest encoding that preserves the comparison. Position on a shared scale is usually easier to judge than area, volume, perspective, or decorative overlap. Preserve units, sampling, uncertainty definitions, and the distinction between observations and illustrative data.
3. Choose scales and color semantics from the data. Separate a scalar's normalization from the colormap. Use consistent category colors across related figures; use a centered diverging norm only when a meaningful reference value exists.
4. Plan the panel geometry before polishing. Use explicit `Figure`/`Axes` objects, reserve space for colorbars and labels, and distinguish equal data scaling from a square panel. Use transforms for stable panel labels and physical offsets.
5. Tune typography, line widths, ticks, hierarchy, and annotations at the final output size. A useful annotation earns its ink by explaining the data. Check that labels and legends do not cover evidence.
6. Export a vector figure when suitable, rasterizing only dense artists when useful; inspect the actual saved artifact at its intended display size. A correct script does not establish a readable figure. For journal requirements, check the current journal instructions rather than treating the book's example DPI as a submission rule.

For an existing figure, start with the largest threat to understanding: misleading encoding, unexplained units, unreadable text, occlusion, inconsistent colors, or an overconstrained layout. Retain the author's data and claims while improving their presentation.

## Core decisions

- **Audience, message, medium:** a slide needs a more immediate hierarchy than a paper figure that readers can inspect. Redesign for the destination rather than merely resizing.
- **Explicit artist hierarchy:** modify the `Axes`, `Axis`, `Text`, `Line2D`, patches, and collections that own the relevant property. Avoid accidental changes to a different current axes.
- **Native data versus physical appearance:** data, axes fraction, figure fraction, and display coordinates answer different questions. Use point offsets for label spacing that should survive zoom, resizing, and export.
- **Color as encoding:** sequential for ordered magnitude; diverging for departures around a meaningful center; cyclic for wrapping quantities; qualitative for categories. A rainbow or a pleasing gradient is not automatically a quantitative scale.
- **Layout as constraints:** figure size, data limits, aspect, labels, and panel allocation interact. Decide which must be fixed; loosen the others instead of accumulating trial offsets.
- **Message trumps beauty:** remove elements that obstruct interpretation; retain reference lines, shading, and explanatory ornaments when they convey information. Scientific figures remain tied to their data.
- **Work at the representation limit:** use aggregation when points overlap beyond readable density, collections when artist overhead dominates, and selective rasterization when a vector file becomes unwieldy. Measure on the actual output; historical speed ratios are not guarantees.

## Load the relevant reference

| Source chapter | Read when working on |
|---|---|
| [1. Anatomy of a figure](chapters/ch01-anatomy.md) | Artists, backend, physical size, vector/raster output |
| [2. Coordinate systems](chapters/ch02-coordinate-systems.md) | Panel labels, offsets, blended and affine transforms |
| [3. Scales & projections](chapters/ch03-scales-projections.md) | Log/symlog/logit, custom scales, polar, projection limits |
| [4. Elements of typography](chapters/ch04-typography.md) | Font choice, math, outlines, TextPath |
| [5. A primer on colors](chapters/ch05-colors.md) | Palettes, color spaces, alpha, normalization |
| [6. Ten simple rules](chapters/ch06-ten-simple-rules.md) | Figure planning, critique, scientific honesty |
| [7. Mastering the defaults](chapters/ch07-defaults.md) | rcParams, styles, figure-specific finishing |
| [8. Size, aspect & layout](chapters/ch08-layout.md) | GridSpec, mosaics, aligned colorbars and marginal plots |
| [9. Ornaments](chapters/ch09-ornaments.md) | Legends, direct labels, annotations, connectors |
| [10. Animation](chapters/ch10-animation.md) | Artist reuse, scenarios, writer and scale choices |
| [11. Going 3D](chapters/ch11-going-3d.md) | Model/view/projection, homogeneous coordinates, depth sorting |
| [12. Architecture & optimization](chapters/ch12-optimization.md) | Dense data, compositing, collections, rasterization |
| [13. Graphic library](chapters/ch13-graphic-library.md) | Paths, clipping, blue noise, schematic simulations |
| [Showcases: all 12 essays](chapters/showcases.md) | Domain coloring, contours, streamlines, Voronoi, stylized text |
| [Appendices and bibliography](chapters/appendices.md) | Cheat-sheet topics, authoritative API lookup, resource selection |

Topic lookup: **alpha/density/rasterization** → 5, 12; **animation** → 10; **aspect/layout/GridSpec** → 8; **blue noise/clipping/Voronoi** → 13, showcases; **captions/audience/message** → 6; **colorbars/normalization** → 5, 8; **fonts/math/text paths** → 4; **legends/annotations** → 9; **projection/3D** → 3, 11; **styles/defaults** → 7; **transforms/coordinates** → 2.

- [Cheatsheet](cheatsheet.md): fast decision rules.
- [Patterns](patterns.md): reusable design and implementation procedures.
- [Glossary](glossary.md): definitions with chapter pointers.
- [Source notes and modern API corrections](chapters/source-notes.md): provenance, edition, license, extraction limits, current official references.
- [Original executable illustration](scripts/relay_freshness_figure.py): two-panel UAV relay geometry and message-age example using explicitly synthetic data. Run with `python scripts/relay_freshness_figure.py --output-dir <directory>`; produces PNG, PDF, SVG, and provenance JSON. Use the caller's Python environment with NumPy and Matplotlib installed.

The book's examples are historical. Prefer public APIs documented for the installed version; preserve the conceptual method while adapting obsolete syntax. Use an available Python interpreter with NumPy and Matplotlib; do not assume a particular operating system, font, interpreter path, or author workspace. Keep output under the caller's requested directory and record actual parameters and library versions. The supplied material is source knowledge, not authority to install software, fetch data, contact people, or publish results. Follow the user's actual task and permissions.

This is an English distillation and adaptation, with original examples and modern API notes, credited to Nicolas P. Rougier. The adapted knowledge text is shared under [CC BY-NC-SA 4.0](LICENSE), which includes a noncommercial restriction. The bundled original script uses [BSD-2-Clause](LICENSE-CODE). See [source notes](chapters/source-notes.md) for attribution and the separate source figure/code licenses.
