# 12. Architecture & optimization

Source: PDF pp. 173–182 (printed pp. 149–158). Use when density, artist count, compositing, or export size limits the figure.

## Diagnose the bottleneck first

Separate data preparation, artist construction, drawing, file writing, and viewer responsiveness. Time the stage that matters at the intended output dimensions. The book's approximate speedups and file sizes describe its examples and software stack; they are not portable performance promises.

| Problem | Candidate remedy | Scientific/visual check |
|---|---|---|
| Points saturate into an opaque blob | `hist2d`, `hexbin`, or an explicit density estimate | Show count/density units, bin size, and norm |
| Many identical markers | A single marker-only `plot` call | Confirm all marker properties really are shared |
| Many segments or polygons | `LineCollection` / `PolyCollection` | Preserve per-element color, order, and geometry |
| Disconnected same-style lines | One path separated by NaN/None | Check compositing and joins remain equivalent |
| Dense vector file | Rasterize the dense artist | Keep text/axes vector; inspect raster resolution |
| Repeated frames recreate artists | Update artist data | Keep limits/norms scientifically consistent |

## Rendering is part of the encoding

Transparency reveals overlap only while the renderer and output can distinguish it. The source's approximate alpha floor of 0.002 is an observation about its rendering path, not a universal mathematical lower limit. Quantitative density should not be inferred from darkness after saturation.

A continuous line and a collection of independently composited segments can look different at self-overlap. The source demonstrates this with a high-frequency modulated sine wave: unified paths avoid some overpainting that independent segments accumulate. An optimization that changes blending can change the message, so compare rendered outputs rather than assuming identical vertices imply identical appearance.

For a signal above the display's resolvable frequency, merely drawing more samples can create aliasing or misleading density. Consider aggregation or a representation that conveys the envelope and unresolved variation, and document the transformation. The source's multisampling example is one rendering strategy, not permission to smooth away meaningful events.

## Worked reconstruction: hybrid export

Render a very dense scatter with `rasterized=True`, then save the overall figure as PDF at an appropriate raster DPI. Axes labels and ordinary lines can remain vector while the dense point layer becomes an image. Compare readability and file size at the actual target scale. Pure vector output may still be preferable for a sparse figure or a large format that will be enlarged substantially.

## Parallel rendering correction

The source calls its tiled example multithreading, but the shown implementation uses `multiprocessing.Pool`. Matplotlib is not thread-safe. Prefer separate processes for independent batch figures; use a noninteractive backend and a Windows `if __name__ == "__main__":` entry guard. For tiled reconstruction, include overlap sufficient to cover marker extent and avoid seams. Match extents, origin, transforms, and resolution across tiles; do not assume arbitrary scientific panels can be tiled independently.

Connects to [color](ch05-colors.md), [animation](ch10-animation.md), and [graphic library](ch13-graphic-library.md).
