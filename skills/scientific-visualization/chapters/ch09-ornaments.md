# 9. Ornaments

Source: PDF pp. 133–142 (printed pp. 109–118). Use for legends, direct labels, titles, annotations, colorbars, and connectors that improve interpretation.

## Choose how the reader finds a mark

Use a legend when it maps a manageable number of styles to unambiguous labels without covering data. Automatic placement is a starting point; inspect the result. Use direct labels when the association is visually clearer and there is room. Use small multiples when no labeling scheme can make crowded traces legible.

Titles and axis labels establish context and units. Moving them for balance is useful only if it preserves their association and avoids tick collisions. Enlarged poster headings can use separate layout slots; a journal panel usually needs less visual emphasis.

## Annotation procedure

1. Identify the actual point, interval, region, or object to explain.
2. Express that target in its natural coordinates, usually data coordinates.
3. Express text placement separately: a physical offset for nearby labels, or an axes/figure fraction for a side explanation.
4. Add a connector only if the label's association would otherwise be unclear.
5. Check clipping, arrow endpoints, crossing connectors, collisions, and evidence covered by the label.

Use `annotate` with explicit `xycoords` and `textcoords`; annotation combines coordinate systems and point-sized text, which explains its many parameters. A thin halo can help text on heterogeneous backgrounds; it does not solve excessive labeling.

## Worked reconstruction

For five selected observations in a dense scatter, first attempt short direct labels at restrained offsets. If those labels obscure points, move labels into a reserved side area. Sort selected observations by vertical location before assigning side positions so connectors are less likely to cross. The source's side-label layout is manually designed, not an automatic collision solver. Recheck it if the data change.

For a zoom panel, use a rectangle to show the source region and `ConnectionPatch` or inset helpers to connect it to the detail view. Indicate the scale and limits of the zoom; do not allow a magnified detail to imply a larger effect in the overall plot.

## Useful limits

An ornament must explain, distinguish, locate, or supply context. Remove it if it only makes the image busier. Marginal distribution marks, threshold lines, and reference shading can be useful despite being non-primary marks; describe their meanings. A colorbar must come from the actual mappable and norm rather than an independently recreated approximate gradient.

Connects to [coordinates](ch02-coordinate-systems.md), [typography](ch04-typography.md), [color](ch05-colors.md), and [layout](ch08-layout.md).
