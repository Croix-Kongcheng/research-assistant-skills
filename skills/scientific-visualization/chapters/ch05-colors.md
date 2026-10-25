# 5. A primer on colors

Source: PDF pp. 79–91 (printed pp. 55–67). Use when colors carry scientific meaning or overlap changes their appearance.

## Separate representation from meaning

A color model describes coordinates such as RGB or HSV; a color space specifies the colors and interpretation of those coordinates. Matplotlib's ordinary RGB/hex values are normally interpreted in sRGB. Arithmetic interpolation of sRGB components is not the same as interpolation in linear light or in a perceptually designed space.

Use a designed colormap when possible. If a custom gradient is essential, specify the interpolation space and inspect its luminance and perceptual progression. Linear-light mixing and perceptually uniform interpolation solve different problems; neither makes an arbitrary gradient automatically suitable for the data.

## Colormap decision tree

| Quantity | Color family | Required reasoning |
|---|---|---|
| Unordered categories | Qualitative | Distinguish members without implying rank |
| Ordered low-to-high values | Sequential | A consistent perceptual progression |
| Signed departure or deviation around a reference | Diverging | A meaningful center mapped to the neutral midpoint |
| Angle, phase, repeating time | Cyclic | End colors meet without a false discontinuity |

Then choose the normalization. For an asymmetric range around a meaningful center, `TwoSlopeNorm(vmin=..., vcenter=..., vmax=...)` maps the center to 0.5. The two slopes allocate equal portions of the palette to unequal numeric spans; explain this if the visual distance could imply equal numeric increments. Shared comparisons usually need a shared norm and an accurately labeled colorbar.

## Category and overlap decisions

Use color to highlight the message or encode a real variable. If many categories require ever more similar colors, consider direct labels, line styles, grouping, or small multiples. Retain the same semantics across panels and related figures. A palette's category separation does not guarantee accessibility; check contrast and distinguish lines by more than hue where needed.

For uncertainty bands, state whether the band is SD, SE, a confidence interval, a range, or something else. Alpha blends show overlaps but produce composite colors dependent on background, layer order, and rendering. Opaque bands make colors explicit but can hide other bands. Choose from the needed comparison and verify the result.

## Worked decision

For feeder voltage deviation from a reference, a centered diverging map may be appropriate. For nonnegative message age, use a sequential map unless a threshold-based encoding is explicitly intended. For UAV headings, use a cyclic map rather than a sequential ramp with an abrupt wrap. These are design examples, not claims about a dataset.

A dark region in a transparent scatter can suggest high overlap but is not a calibrated density estimate. When quantitative density matters, use bins or another defined estimate. Multicolored line segments need a collection rather than one `Line2D` with a single color; see [optimization](ch12-optimization.md). The book's showcase use of Spectral for phase is explicitly aesthetic and introduces discontinuities; do not inherit that compromise by default.
