# Reusable patterns

## Message-first figure revision

**When to use:** An existing figure feels busy or does not make its result clear.

**How:** State the supported message, audience, and medium. Check encoding honesty before style. Remove or relocate the main source of ambiguity. Re-evaluate at the final physical size and write a caption explaining symbols, units, conditions, and uncertainty.

**Trade-offs:** A paper can carry detail that a projected slide cannot; separate versions may be warranted (6).

## Physical panel labels

**When to use:** Letters drift after limits, aspect, or DPI change.

**How:** Anchor to `ax.transAxes`, then add `ScaledTranslation(dx/72, dy/72, fig.dpi_scale_trans)` for point offsets. Choose alignment relative to the anchor. Check the saved export after final layout.

**Trade-offs:** Off-panel labels need reserved space and clipping/export review (2).

## Centered diverging field

**When to use:** A scalar has a meaningful center and asymmetric observed limits.

**How:** Choose a diverging map and explicit `TwoSlopeNorm(vcenter=reference, vmin=low, vmax=high)`. Share the norm across comparable panels. Create the colorbar from the actual mappable and state the reference and units.

**Trade-offs:** Equal palette distances on opposite sides can represent unequal numeric changes (5).

## Small multiples with background context

**When to use:** Equally important traces overlap beyond readable comparison.

**How:** Allocate aligned panels. Highlight one trace in each and show other traces lightly if context helps. Use shared limits, direct labels, and a clearly stated reference scale. Simplify redundant ticks.

**Trade-offs:** Consumes panel area but reduces legend lookup and occlusion; faint context still needs enough contrast (6, 8).

## Reserved auxiliary axes

**When to use:** Colorbars, marginal plots, row labels, or headings disrupt equal panel sizes.

**How:** Allocate GridSpec slots for scientific and auxiliary content. Use ratios and spans; share data axes where appropriate. Add the colorbar with `cax` when its geometry must be explicit. Inspect final labels and panel extents.

**Trade-offs:** More layout planning, less arbitrary manual nudging; aspect constraints can still require compromise (8).

## Side annotations with ordered connectors

**When to use:** Direct labels hide a dense set of selected points.

**How:** Reserve a side region; order target points by a sensible coordinate; assign matching label positions; set target and text coordinate systems explicitly. Inspect connector crossings and endpoints after data/layout changes.

**Trade-offs:** Manual placement is data dependent; it is not a generic collision solver (9).

## Bounded animated state

**When to use:** A temporal illustration repeatedly creates artists or clears the axes.

**How:** Allocate a fixed set of artists, update their arrays/properties per frame, and separate the event schedule from rendering. Retain the animation, specify finite export frames, and use fixed scientific limits/norms when comparing time points.

**Trade-offs:** More explicit state; avoids unbounded artist growth. Blitting needs returned artists and backend support (10).

## Aggregation at visual saturation

**When to use:** A scatter becomes an opaque central blob despite lower opacity.

**How:** Choose bins or another defined density estimate; label count/density and bin meaning; select a suitable norm; preserve outliers or subgroup structure needed by the question. Compare with the raw-point view at a readable scale.

**Trade-offs:** Aggregation changes what is encoded and can hide within-bin structure; alpha darkness is not a calibrated substitute (12).

## Batched primitives and hybrid export

**When to use:** Artist overhead or a huge vector file limits usability.

**How:** Batch compatible marks into collections; benchmark construction/drawing/export separately. Rasterize dense layers while retaining labels and sparse reference marks as vector. Inspect both appearance and artifact size.

**Trade-offs:** Unified paths and independent segments can composite differently; output raster resolution still matters (12).

## Composed reproducible schematic

**When to use:** A repeated scientific diagram combines geometry, labels, fields, and paths.

**How:** Separate geometry/state from artists. Use paths and collections for boundaries, images for scalar rasters, and text for explanations. Record randomness and source data. Explicitly label schematic or synthetic components.

**Trade-offs:** Automation pays off with reuse; a one-off procedural drawing can cost more than editing a vector asset (13).
