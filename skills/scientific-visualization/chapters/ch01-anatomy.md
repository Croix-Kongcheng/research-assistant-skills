# 1. Anatomy of a figure

Source: PDF pp. 27–42 (printed pp. 3–18). Use when debugging ownership, rendering, size, and export.

## Decision model

Think of a figure as a hierarchy of artists. `Figure` is the outer container; `Axes` owns a plotting region; its `Axis` objects arrange ticks, tick labels, and axis labels. Spines mark the region's borders. Lines, patches, text, images, and collections produce the visible marks. Edit the artist that owns the property instead of hoping an unrelated plotting command changes it.

Use `fig, ax = plt.subplots(...)` for a simple explicit figure. Keep axes references in multi-panel code; `plt.plot` targets the current axes, which becomes fragile after new panels or colorbars are created. A plotted artist belongs to one axes; create a new artist when an equivalent mark is needed in another panel.

## Practical choices

- Specify `figsize` in inches from the intended placement. For an uncropped raster output, pixel width equals width in inches times the save DPI. Screen DPI and export DPI can differ.
- Set type and stroke sizes for the final physical figure, rather than making a large figure and shrinking it in the manuscript. Matplotlib points are 1/72 inch; TeX points are slightly different.
- Prefer PDF or SVG for lines and text when the destination accepts them. Images and explicitly rasterized artists remain resolution dependent even inside vector containers.
- Treat `zorder` as layer order. Explicitly layer overlapping objects when overlap is meaningful; merely reordering plotting calls can obscure the intended relationships.
- Separate the rendering backend from the output format. Agg supports headless rendering; PDF/SVG exports can still be requested from a figure created with Agg. GUI display needs an interactive backend and an event loop.

## Worked reconstruction

For a hypothetical 90 mm wide figure exported at 300 DPI, use a width of `90 / 25.4` inches. An uncropped raster width is about 1063 pixels after rounding. Pick the height to support the message and labels. Export with `fig.savefig(..., dpi=300)` and inspect the saved dimensions. A tight bounding box changes the final canvas extent, so avoid it when exact pixel geometry is required.

## Modern notes and pitfalls

The book's backend list reflects its publication date; select from the installed version. Its statement that saving always overrides the figure facecolor with white is historical: current `savefig` supports automatic facecolor. Specify background behavior deliberately when it matters.

Do not infer publication suitability from DPI alone. Fine text can still be unreadable at a technically high resolution. Do not set every artist to an extreme `zorder`; that makes layering difficult to reason about.

Connects to [coordinates](ch02-coordinate-systems.md), [typography](ch04-typography.md), [layout](ch08-layout.md), and [optimization](ch12-optimization.md). Current API links are in [source notes](source-notes.md).
