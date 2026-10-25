# 11. Going 3D

Source: PDF pp. 159–172 (printed pp. 135–148). Use to reason about projection and visibility, including when 3D should be simplified.

## Model, view, projection

The source reconstructs a 3D mesh renderer using NumPy and a 2D polygon collection, rather than hiding the geometry inside an axes. Retain its conceptual decomposition:

1. **Model:** place and orient local mesh coordinates.
2. **View:** position the scene relative to the camera.
3. **Projection:** map the visible volume to the image.

For column-vector convention, the combined matrix is `P @ V @ M`. With NumPy vertices stored as rows, apply its transpose. Append a homogeneous coordinate of 1 for points, transform, then divide by the transformed w. Matrix order matters; translating before and after a rotation can produce different scenes.

## Projection and visibility decisions

- **Orthographic:** parallel sight lines preserve parallelism and remove distance-based apparent size. Useful when metric relationships matter.
- **Perspective:** apparent size decreases with camera distance. Field of view and camera distance jointly control appearance; wide fields exaggerate depth.
- **Viewing volume:** near/far and side planes determine what is visible. Keep geometry in a valid camera configuration and handle clipping and degenerate w deliberately.
- **Depth sorting:** painter-style rendering orders polygons from back to front. Sorting by mean face depth is an approximation that works best for small nonintersecting faces. It cannot correctly resolve every intersecting or cyclic overlap.

## Worked reconstruction

Take a triangular mesh as vertex and face arrays. Normalize its extent for a controlled example, rotate the model, translate it away from the camera, apply the chosen projection, and divide homogeneous coordinates. Gather projected vertices into face polygons, compute a depth key, sort the faces and their colors together, and add a `PolyCollection` to an equal-aspect 2D axes. The source's initially distorted bunny demonstrates that putting the camera inside the object is a scene setup problem, not a styling problem.

This renderer is educational. A model-specific minimal OBJ parser is not a robust loader for arbitrary files. Its depth-based face coloring is an appearance cue, not physical illumination or a measured scalar field. Do not reuse the source's matrix listings blindly; independently validate projection conventions and clipping when implementing a renderer.

## When to use another representation

For publication comparisons of values, start with aligned 2D views, contour maps, or slices. Use 3D when shape or spatial arrangement matters enough to justify occlusion and viewpoint dependence. Provide units, viewpoint, and a scale reference. Keep labels readable; physical projected lettering can become illegible when the camera rotates. Use a proper 3D renderer when accurate hidden-surface handling is required.

Connects to [scales/projections](ch03-scales-projections.md), [typography](ch04-typography.md), and [showcases](showcases.md).
