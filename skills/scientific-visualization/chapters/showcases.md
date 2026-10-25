# Showcase techniques: 12 short essays

Source: PDF text pp. 201–224 (printed pp. 177–200), with figure-only pages and the opening showcase spread around pp. 196–200. These are unnumbered showcase entries after chapter 13; they are grouped here because each explains a compact graphical technique.

Use these as conditional patterns, not a style prescription for every scientific plot. Some deliberately favor aesthetic effects over quantitative readability. The scientific question determines whether the technique belongs in the figure.

| Showcase / text pages | Technique to transfer | Decision and limitation |
|---|---|---|
| Filled contours with dropshadows, 201–202 | Render contour masks offscreen, blur their alpha for shadow images, then layer shadow and colored contour from back to front. | Shadows can distinguish raised/depressed regions but need a stated meaning; a conventional diverging map may communicate sign more directly. |
| Domain coloring, 203–204 | Encode a complex function's argument as color and magnitude with a separately explained modulation; contours expose structure. | Prefer a cyclic hue mapping when phase continuity matters. The source chooses Spectral for appearance and explicitly acknowledges discontinuities. |
| Escher like projections, 205–206 | Use a complex exponential map for spiral tiling; build thick lines as polygonal geometry if width itself must transform. | Ordinary constant display-width strokes do not behave like projected geometry. This is mainly an illustration/geometry technique. |
| Self-organizing maps, 207–208 | Color a polygon collection by the neuron represented by each cell. | Check antialias seams between abutting polygons. The visual is not an explanation or validation of the learning algorithm by itself. |
| Waterfall plots, 209–210 | Use layered 3D polygons; polygon intersections create horizontal color-gradient slices. | Staggering and occlusion can hide quantitative comparisons. Consider aligned 2D spectra or a heatmap when precision matters more than depth. |
| Streamlines, 211–212 | Split curves into segments, color them with a `LineCollection`, and animate a progression to suggest direction. | Explain what color/progression means; a static gradient alone may not identify direction unambiguously. The source's cap workaround is version specific; check current collection APIs. |
| Mandelbrot set, 213–214 | Use an image representation and smooth escape-time coloring. | State the computed quantity and handling of bounded/undefined values; visual smoothness does not create additional numerical precision. |
| Recursive Voronoi, 215–216 | Combine Poisson-disk placement, recursive polygon subdivision, clipping, and level-dependent styling. | Record random seeds and recursion parameters for repeatable results. The source's runtime is a historical example, not a bound. |
| 3D Heightmap, 217–218 | Triangulate/represent terrain and depth-sort faces for projection. | The source uses an experimental 3D axes. Prefer supported tools and verify visibility; angle and shading can exaggerate apparent terrain. |
| Voronoi mosaic, 219–220 | Sample an image using blue-noise centers, construct cells, and color each cell from a sampled image color. | A stylized lossy reconstruction, not an unmodified scientific image. Label transformations when used with research imagery. |
| Text shadow, 221–222 | Convert text to outlines, extend segments into sheared shadow geometry, and fade the result using an alpha-gradient image. | Useful for graphic titles; it usually adds no evidence to a data panel. |
| Text spiral, 223–224 | Warp TextPath vertices around an Archimedean spiral with constant radial spacing between turns. | Equal turn spacing does not mean constant linear speed along the spiral. Treat it as typographic art, with a readability cost. |

## Reuse procedure

Identify the single graphical mechanism needed: clipping, projection, varying stroke color, alpha masks, or path warping. Build a small original example that isolates that mechanism. Then test geometry, color meaning, output format, and readability before integrating it into the scientific figure. Avoid adopting unrelated decorative layers from the source image.

For path effects and silhouettes, preserve an unmodified representation or an explicit statement of what was transformed when that distinction matters. For simulations, distinguish model state from rendering effects and from measured data. See [graphic library](ch13-graphic-library.md), [3D](ch11-going-3d.md), [typography](ch04-typography.md), and [color](ch05-colors.md).
