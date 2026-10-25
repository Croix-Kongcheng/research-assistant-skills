# 2. Coordinate systems

Source: PDF pp. 43–56 (printed pp. 19–32). Use when an element moves or scales incorrectly after changing limits, size, or DPI.

## Choose coordinates by meaning

| Element's intended behavior | Coordinate system / transform |
|---|---|
| Follow an observation | Data: `ax.transData` |
| Stay at a relative panel location | Axes fraction: `ax.transAxes` |
| Stay at a relative whole-figure location | Figure fraction: `fig.transFigure` |
| Keep a physical offset or dimension | Inches via `fig.dpi_scale_trans`, or annotation offset points |
| Follow x data while spanning panel height | `ax.get_xaxis_transform()` |
| Follow y data while spanning panel width | `ax.get_yaxis_transform()` |

The book calls axes fractions normalized data coordinates; current Matplotlib usually calls them axes coordinates. They describe the axes box, not a normalization of raw data under arbitrary projections. Display units also depend on the backend: pixels for Agg, points for PDF/SVG.

## Reusable procedure

1. Write down which parts of a position are scientific coordinates and which are presentation spacing.
2. Let Matplotlib apply a transform to the artist whenever possible; avoid prematurely converting to display coordinates.
3. For conversion, use `transform.transform(points)` and `transform.inverted()`. Compose transforms in their application order: `A + B` applies A then B.
4. Recompute any cached display coordinates after layout, limits, figure size, or DPI changes. Draw the canvas first when final artist extents are needed.

An original minimal panel-label construction:

```python
from matplotlib.transforms import ScaledTranslation

offset = ScaledTranslation(5 / 72, -5 / 72, fig.dpi_scale_trans)
ax.text(0, 1, "A", transform=ax.transAxes + offset,
        va="top", ha="left", fontweight="bold")
```

This pins A to a corner while its five-point inset remains physical. For a label near a measured point, `annotate(..., xycoords="data", textcoords="offset points")` is often simpler.

## Advanced cases and failure modes

For rotating an image, compose an `Affine2D` rotation/translation with `ax.transData`; data limits and the artist's extent still need deliberate handling. The source's rotated principal-axis histogram reconstructs a floating axes from transformed corners, an enclosing figure-space rectangle, and an axisartist helper. Use that machinery only when the rotated coordinate frame itself is meaningful.

Blending x and y independently assumes separable transformations; do not assume a Cartesian blend works on polar coordinates. Markers usually retain physical shape and size under a projection. A true data-radius disk needs patch geometry in data coordinates plus an appropriate aspect, rather than interpreting scatter area as a data distance.

Disable clipping only for intentional out-of-panel content and verify the saved artifact includes it. The source contains `ScaleTranslation`/`ScaledTranslation` and bounding-box typos; use the public `ScaledTranslation` API and independently compute width and height.

Connects to [scales/projections](ch03-scales-projections.md), [layout](ch08-layout.md), and [ornaments](ch09-ornaments.md).
