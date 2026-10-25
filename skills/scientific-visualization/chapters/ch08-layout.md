# 8. Size, aspect & layout

Source: PDF pp. 119–132 (printed pp. 95–108). Use when panels, aspect, labels, and colorbars compete for space.

## Solve the actual constraints

Figure aspect is height divided by width. Axes data aspect controls the display ratio of one y unit to one x unit. Axes box aspect controls the panel's physical height/width. These are distinct from data ranges. For equal geometric units use `set_aspect("equal")`; a square axes box alone does not ensure equal distances.

Decide what is essential: fixed final figure size, comparable panel size, equal data scaling, fixed data limits, or a particular arrangement. An overconstrained design may require changing one of these. Increasing padding indefinitely cannot solve incompatible constraints.

| Need | Useful starting method |
|---|---|
| Regular row/column panels | `plt.subplots` |
| Unequal widths, spans, aligned auxiliary axes | `fig.add_gridspec` and slices |
| A semantic arrangement with named panels | `plt.subplot_mosaic` or `fig.subplot_mosaic` |
| Intentional exact normalized placement | `fig.add_axes` with manual layout responsibility |
| Labels and colorbars accommodated automatically | Create with `layout="constrained"` |

The GridSpec emphasis comes from the source. Constrained layout is a modern starting choice; manually placed axes or unusual out-of-axes artists may still need explicit management. Do not call `tight_layout()` after enabling constrained layout because it turns constrained layout off.

## Layout procedure

Sketch the allocation of scientific panels, row/column labels, legend, title, and colorbar. Reserve slots for auxiliary elements rather than shrinking one scientific panel unexpectedly. Choose shared limits or norms where a comparison requires them. Use width/height ratios to encode the planned arrangement. Draw once, inspect artist extents, and adjust only the responsible constraint.

## Worked reconstructions

- **Image plus colorbar:** allocate a main axes and a narrow adjacent colorbar axes in one GridSpec row. Set the colorbar's `cax` explicitly when exact alignment matters. A chosen ratio such as 10:1 is an example, not a universal colorbar width.
- **Scatter plus marginal histograms:** reserve a large lower-left plot, a shallow top histogram, and a narrow right histogram. Share x with the top and y with the side. Preserve the main plot's geometry and avoid duplicate tick labels.
- **Many comparable panels:** reserve separate small rows for headings and columns for row labels when adding individual titles would make panel areas uneven.

## Modern correction and pitfalls

The source's `fig.add_mosaic("AB")` snippet should be replaced by current `subplot_mosaic`; the pyplot form returns `(fig, axes_dict)` and the Figure method returns a dictionary. Do not unpack axes dictionary iteration as though it returns the axes themselves.

Cropping with `bbox_inches="tight"` can help contain labels but changes the final physical canvas. Inspect that outcome if dimensions are contractual. Avoid using manual point offsets to compensate for a wrong GridSpec allocation.

Connects to [coordinates](ch02-coordinate-systems.md), [typography](ch04-typography.md), and [ornaments](ch09-ornaments.md).
