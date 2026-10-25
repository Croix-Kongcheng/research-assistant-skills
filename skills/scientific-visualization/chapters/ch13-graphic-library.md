# 13. Graphic library

Source: PDF pp. 183–195 (printed pp. 159–171). Use for composed scientific diagrams, paths, clipping, or lightweight graphical prototypes.

## Compose from primitives

Treat paths, patches, collections, text, and images as a small graphics vocabulary. Matplotlib can combine them into custom schematics and teaching illustrations. Decide whether reproducibility or repeated use justifies a procedural construction; for a single complex diagram, an editable vector drawing may be more efficient.

Clipping restricts where an artist is visible. It is not automatically a polygon Boolean operation that returns reusable geometry. For explicit intersections or clipped Voronoi cells, the source uses a geometry library; verify its public API and handle empty/invalid geometries before drawing.

## Source patterns worth transferring

- **Dyson hatching:** begin with a blue-noise point distribution, attach short parallel-line hatch motifs with varied orientations, and clip each motif to its cell to prevent unwanted overlap. Restrict motifs to the region where they explain boundaries. Bridson's Poisson-disk method enforces minimum point separation, unlike ordinary independent uniform sampling.
- **Tiny bot:** separate scene geometry, robot state, sensor calculations, and artists. Draw walls with a line collection, the body with a patch, heading with a line, and sensor rays with a collection. Update those artists during animation. This is a graphical prototype, not validated robot dynamics or sensing.
- **Density-defined biological schematic:** combine a reference image and paths, a point placement view, an aggregated activity image, and colored clipped cells. Each panel answers a different question and needs a caption explaining its representation.

## Worked engineering adaptation

For a toy UAV relay diagram, use feeder buses as points and feeder branches as one `LineCollection`, UAV positions as distinct markers, and communication links as dashed paths. Keep coordinates and units explicit if the geometry is metric. If it is a topology schematic, label it as schematic and do not imply real distances. A separate panel can show supplied telemetry, preserving the same relay identifiers and color semantics. The bundled executable illustrates this separation using synthetic values.

## Failure modes

Do not equate an attractive procedural texture with measurement or a physical simulation. The source's segment-intersection example is compact and purpose specific; production geometry needs careful handling of parallel, collinear, endpoint, and floating-point cases. Randomized placement needs a recorded seed and parameter choices when reproducibility matters. Avoid reconstructing an entire drawing toolkit when ordinary axes, an SVG asset, or the project's existing graphics system would handle the task clearly.

Connects to [coordinates](ch02-coordinate-systems.md), [animation](ch10-animation.md), [optimization](ch12-optimization.md), and [showcases](showcases.md).
