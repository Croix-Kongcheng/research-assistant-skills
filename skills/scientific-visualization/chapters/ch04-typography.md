# 4. Elements of typography

Source: PDF pp. 69–78 (printed pp. 45–54). Use when text hierarchy, math, contrast, or font consistency affects comprehension.

## Treat type as figure structure

Choose a coherent family for labels, ticks, and annotations, with weights and sizes that communicate hierarchy. Match the surrounding document where appropriate and verify actual font resolution; requesting a font name does not prove that it was found. Font family, face, weight, glyph, em, kerning, and line spacing describe different properties.

Physical point size is separate from figure dimensions. Creating a large canvas does not automatically enlarge labels. Shrinking a figure after export shrinks all its type. Judge legibility at the figure's final placement, including the smallest tick label and superscript.

## Decisions and techniques

- Start with available fonts that cover the required symbols. Use `findfont(FontProperties(...), fallback_to_default=False)` to detect an unavailable intended face rather than accepting a silent replacement.
- Use MathText for supported mathematics without a TeX installation; select a math font family compatible with body type. Use real TeX only when its typography or notation is needed and the toolchain is available.
- For labels over varying image backgrounds, compare moving the label, a light/dark outline, and a small background patch. A thin contrasting outline often improves readability while obscuring less of the image than an opaque box.
- Use regular `Text` for titles, labels, and annotations. Use `TextPath` only when glyph outlines must be warped, clipped, or projected as geometry. Distorted glyphs can become illegible and no longer behave like ordinary searchable text.

## Worked reconstruction

A contour label placed over both bright and dark image regions may disappear if it is simply black or white. Keep its location and data association, then add a narrow contrasting stroke using `matplotlib.patheffects.withStroke`. Inspect the exported image: an excessively heavy halo can erase nearby structure. If there is no unobstructed placement, use a side label and connector rather than more effects.

The source's curved contour labels warp TextPath vertices along a contour. This fits smooth, sufficiently long paths; sharp bends and short contours make letter geometry collide. Its 3D text example shows why camera-facing default labels often remain more readable than physically projected lettering when the camera rotates.

## Modern correction

The book's `font_manager._rebuild()` is a private historical mechanism. For an explicitly supplied local font file, use public `font_manager.fontManager.addfont(path)` and register it for each process that needs it, or use `FontProperties(fname=path)` directly. Do not install fonts or change system configuration merely because an example uses a different family.

Connects to [physical sizing](ch01-anatomy.md), [defaults](ch07-defaults.md), [ornaments](ch09-ornaments.md), and the [text showcases](showcases.md).
