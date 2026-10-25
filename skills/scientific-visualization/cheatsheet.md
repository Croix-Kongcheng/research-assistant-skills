# Figure-design decisions

| If you see / need | Decide this way | Reason |
|---|---|---|
| A figure with no clear takeaway | State one supported message before styling | Design needs an audience and purpose |
| A slide adapted from a dense paper panel | Reduce detail, enlarge meaningful marks, redesign hierarchy | Viewing time and distance differ |
| Tiny type after insertion | Set final physical size first | High DPI does not fix undersized text |
| Exact raster dimensions | Inches = pixels / DPI; avoid tight cropping | Cropping changes the canvas |
| Physical geometry | Equal data aspect and units | Square panel shape alone is insufficient |
| Labels move during zoom | Use axes/figure fractions or point offsets | Presentation spacing is not data |
| A positive ratio spanning decades | Consider log; verify domain | Equal ratios then get equal distances |
| Signed multi-order data | Consider symlog; specify its linear region | Ordinary log excludes nonpositive values |
| Quantity varies from low to high | Sequential palette | Color should imply ordered magnitude |
| Departure around a meaningful center | Diverging + deliberate center norm | Automatic midpoint may map the reference incorrectly |
| Wrapping phase/angle | Cyclic palette | Avoid a false endpoint discontinuity |
| Too many category colors | Direct labels, styles, groups, or panels | Additional hues stop distinguishing reliably |
| Transparent bands overlap | Decide whether mixing or explicit color is preferable | Compositing depends on order/background |
| Dense scatter saturates | Aggregate and label the statistic | Darkness no longer resolves counts |
| Circle sizes encode value | Make area proportional to value | Radius proportionality exaggerates differences |
| Bars exaggerate a small difference | Recheck baseline and encoding | Length comparison implies a meaningful zero |
| Legend obscures evidence | Reposition, label directly, or split panels | Labels should reveal associations |
| Labels over heterogeneous image colors | Move first; then consider a thin outline | Contrast without concealing structure |
| Unequal panel sizes caused by colorbars | Reserve auxiliary axes / shared allocation | Preserve comparable scientific panel area |
| Layout needs endless offsets | Revisit fixed constraints | Size, aspect, ranges, and labels may conflict |
| Slow animation | Update artists; keep finite state | Rebuilding the figure adds overhead |
| Color changes meaning across frames | Share norm or disclose varying limits | Shape visibility and numeric comparison differ |
| Huge PDF from many points | Rasterize dense artist, retain other vector marks | Hybrid output reduces geometric payload |
| 3D obscures a comparison | Try aligned 2D views or slices | Perspective/occlusion complicate judgment |
| A style tweak adds no information | Remove it unless it improves reading | Message trumps beauty |

Use [chapter guides](SKILL.md) for mechanisms and [source notes](chapters/source-notes.md) for modern API corrections. Typical historical DPI examples are not universal publisher rules; verify the actual destination's requirements.
