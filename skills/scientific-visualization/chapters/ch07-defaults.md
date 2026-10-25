# 7. Mastering the defaults

Source: PDF pp. 109–118 (printed pp. 85–94). Use to create consistent figures without hiding figure-specific decisions in a global style.

## Separate three layers

1. **Library defaults:** inspect `mpl.rcParams` to understand implicit figure size, colors, line widths, margins, ticks, and fonts.
2. **Reusable visual policy:** use a small style or `mpl.rc_context({...})` for genuinely shared choices such as font size, spine visibility, and stroke weight.
3. **Figure semantics:** set data limits, units, meaningful tick locations, annotations, and reference values in the figure code.

Prefer a local context when a one-off figure should not alter later plots in the same process. Create artists inside the context so their properties are initialized from it. A style file can make a family of figures consistent, but cannot decide a meaningful tick scale for every dataset.

## Worked reconstruction

The source progressively refines sine and cosine: first implicit defaults, then their explicit equivalents, then a reusable style, then trigonometric ticks and moved spines. The lesson is to identify which layer owns the choice. For an engineering plot, apply a modest shared type/stroke style, then select explicit units, a meaningful range, and a small number of ticks in the plotting code.

When tick text is custom, pair labels with the intended positions using `ax.set_xticks(positions, labels=...)`, or use an appropriate locator and formatter. Do not change strings on arbitrary auto ticks and assume they will remain aligned after limits change.

## Fine tuning that earns its cost

- Remove top/right spines when they add no needed frame information.
- Move a spine to a data origin only when that origin helps interpretation and does not make labels collide.
- Use reference ticks, selective markers, and line styles to make comparisons clearer.
- Retain required axes, labels, or units even if a minimal style would look cleaner without them.

The source's individual snippets include typographic and axis-label errors, so preserve their design reasoning rather than copying them literally. Not every artist property belongs to rcParams; a style is not an API for arbitrary geometry. Stop polishing when further changes do not improve the figure's message or readability.

Connects to [anatomy](ch01-anatomy.md), [typography](ch04-typography.md), [layout](ch08-layout.md), and [ornaments](ch09-ornaments.md).
