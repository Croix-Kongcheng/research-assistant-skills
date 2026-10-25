# Appendices, front matter, conclusion, and bibliography

The front matter establishes intermediate Python/basic NumPy as prerequisites, historical dependency versions, an open-source production workflow, and separate text/figure/code licenses. The introduction's library landscape is dated: choose tools by target medium, needed 3D capability, output quality, data scale, documentation, and maintained support. It is a decision checklist, not a current package ranking.

The conclusion (PDF p. 227) describes the first edition's incomplete feature coverage. This skill likewise does not claim to cover every Matplotlib feature or to replace its API documentation.

## A. External resources — PDF pp. 231–234

Use official documentation for parameter semantics and the Matplotlib gallery to find the nearest working pattern. Galleries and comparable scientific papers can help choose an encoding, but judge their design against the audience and message. Historical mailing-list counts, social links, and package descriptions are not evidence of current project status.

The source cites Butterick for typography, Hunter's Matplotlib paper, Rougier's NumPy book, the ten-rules article, VanderPlas's data-science handbook, and Wilke's visualization text. Use these as pointers rather than implying their full contents are included here. Current official API links are collected in [source notes](source-notes.md).

## B. Quick References — PDF pp. 235–244

The appendix contains panoramic cheat sheets plus beginner, intermediate, and tips/tricks handouts. Its useful topic coverage maps to the guides below; dense catalogs are not duplicated.

| Handout topic | Read |
|---|---|
| Anatomy, initialization, save formats | [Chapter 1](ch01-anatomy.md) |
| Plot primitives, lines, markers | [Chapter 13](ch13-graphic-library.md), then current API docs |
| Scales and projections | [Chapter 3](ch03-scales-projections.md) |
| Tick locators/formatters, styling | [Chapter 7](ch07-defaults.md) |
| Image extent/origin and layout | [Chapters 2](ch02-coordinate-systems.md), [8](ch08-layout.md) |
| Color families and norms | [Chapter 5](ch05-colors.md) |
| Text alignment, outlines, fonts | [Chapter 4](ch04-typography.md) |
| Legend anchoring, annotation connectors/arrows | [Chapter 9](ch09-ornaments.md) |
| Animation, artist reuse | [Chapter 10](ch10-animation.md) |
| Rasterization, performance | [Chapter 12](ch12-optimization.md) |
| Figure critique | [Chapter 6](ch06-ten-simple-rules.md) |

The handouts target Matplotlib 3.4.2 and their multi-column extraction sometimes interleaves unrelated commands. Do not execute the extracted snippets literally. Examples such as tuple-shaped `plt.subplots((2, 1))`, `ax.colorbar`, `ax.tight_layout`, and tick-rotation shortcuts need correction or context: use `plt.subplots(2, 1)`, `fig.colorbar(...)`, a figure layout method, and `tick_params(labelrotation=...)` respectively. Preserve API intent rather than extraction errors.

Bibliography: PDF pp. 245–248, including blank/decorative end pages. Titles are research pointers, not additional converted source books.
