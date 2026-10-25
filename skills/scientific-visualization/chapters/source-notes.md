# Source notes, attribution, and modern API boundary

## Provenance and coverage

- Author: Nicolas P. Rougier.
- Title: *Scientific Visualization: Python & Matplotlib* (the supplied cover also uses the spelling *Visualisation*), Scientific Python, Volume II.
- First edition: November 2021; supplied PDF creation date: June 21, 2022. ISBN 978-2-9579901-0-8.
- Source edition used for this distillation: 248 PDF pages, 98,175,187 bytes. No book PDF is bundled or required to use this skill.
- SHA-256: `18c87f0ef0974d3837f7fe5253e8454ab323fe25835985fa01e8669d2c3bd45b`.
- [Author's source repository](https://github.com/rougier/scientific-visualization-book); the PDF itself gives the historical repository name `rougier/python-scientific-visualisation`.
- Distilled October 17, 2026 into English decision guides, original worked reconstructions, and a new executable illustration. Long source passages, source code listings, and raw extracted text are not bundled.

The table of contents and bookmarks establish 13 numbered substantive chapters. Twelve unnumbered showcase essays are grouped in one guide. Two appendices and the bibliography have their own routing guide. Front matter, introduction, and conclusion inform scope and provenance. Per-chapter source page ranges are in each guide.

Substantive prose was read in bounded section batches. Numeric/glyph-only chart-label noise was excluded from those read views. The appendix contains wide multi-column handouts whose text can interleave; selected page renders were inspected to confirm their layout and topic coverage. Selected figures were visually inspected; not every source illustration or source code file was independently reconstructed. Original extraction artifacts are not included; neither they nor a private source folder are a runtime dependency. Public packaging on October 25, 2026 removed machine-specific archive paths, added explicit license files, and clarified portable runtime choices.

## Attribution and license

This knowledge text is a distillation and adaptation of Nicolas P. Rougier's book, with modern API notes and new engineering examples added. Credit the author and source and indicate this adaptation when redistributing it. The adapted book-derived knowledge text is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/). It is not licensed for commercial use under those terms.

The PDF separately states that, unless otherwise marked, its figures use [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and its code uses the BSD 2-clause license. The chapter-six article has its own CC0 notice. No source images or code files are bundled in this skill. The newly authored demonstration script declares its own BSD-2-Clause license in its header; it is not a copy of a book script. The author's [license notice](https://github.com/rougier/scientific-visualization-book/blob/master/LICENSE.txt) was checked October 25, 2026 and confirms the book's CC BY-NC-SA 4.0 and code's BSD terms. This directory's book-derived knowledge text is an adaptation, including new summaries, examples and API commentary; it is not the original book or an endorsement by its author.

## Historical source versus current implementation

The preface records Python 3.7.4, NumPy 1.16.4, SciPy 1.3.0, and Matplotlib 3.1.0; later pages mention Matplotlib 3.4/3.4.2. Preserve concepts, not assumptions that these versions describe the user's current environment.

| Source-era issue | Modern handling / primary reference |
|---|---|
| Figure/axes coordinate names and pixel assumptions | Follow the [transform tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html); display units depend on backend; blends assume separability. |
| `font_manager._rebuild()` | Use public [font management](https://matplotlib.org/stable/api/font_manager_api.html), including `fontManager.addfont` per process or `FontProperties(fname=...)`. |
| `fig.add_mosaic` and ambiguous unpacking | Use [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html); its axes are returned by label in a dictionary. |
| Repeated layout adjustments | Consider [constrained layout](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html) from creation; calling `tight_layout` disables it. |
| Incomplete scale catalogue | Check current [axis scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html), domains, and inverses. |
| Diverging map with asymmetric limits | Use [`TwoSlopeNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html) only for a meaningful center. |
| Saving always overrides the background to white | Current [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html) supports automatic facecolor; choose deliberate background/cropping behavior. |
| Marker size ambiguity | [`Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html) uses squared points for `s`; marker edges also influence apparent size. |
| Artist batching and geometric scaling | Use current [collection APIs](https://matplotlib.org/stable/api/collections_api.html) and [`Axes.set_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html); distinguish data scaling from panel shape. |
| Large vector output | [Selective rasterization](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html) leaves other artists as vector; output DPI controls raster detail. |
| Animation lifetime, finite frames, blitting | Follow [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html); retain the object and return modified artists when blitting. |
| Multithread terminology | The source actually demonstrates processes. Matplotlib's [threading FAQ](https://matplotlib.org/stable/users/faq.html#work-with-threads) explains its lack of thread safety. |
| Global random calls in examples | For new stochastic illustrations use NumPy's [`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html), record seed and library version; a fixed seed is not a cross-version guarantee. |

Official pages above were checked October 17, 2026 against Matplotlib 3.11.2 documentation and NumPy 2.5 documentation. Runtime validation used Matplotlib 3.11.2 and NumPy 2.5.4. Only the bundled original script and targeted API/invariant checks were executed; the source's whole code repository and optional toolkits were not tested.

Other explicit corrections: alpha saturation floors, speed factors, and file-size reductions are historical observations, not guarantees. Do not infer chronological event playback from the earthquake example, which discards event time. Per-frame color rescaling changes color meaning. An Archimedean spiral has constant radial turn spacing, not constant linear speed at constant angular velocity. Painter-style 3D depth sorting cannot solve all visibility cases.

The ten-rules chapter derives from Rougier, Droettboom, and Bourne, [Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833) (2014). Its coauthors and separate source notice are preserved here.
