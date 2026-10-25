# 3. Scales & projections

Source: PDF pp. 57–68 (printed pp. 33–44). Use to change representation without silently changing the underlying observations.

## Scale selection

Scales act independently on one dimension. Projections can couple dimensions. Changing axis scale preserves original values and allows appropriate ticks and inverse coordinate mapping; manually transforming an array transfers that bookkeeping to the author.

| Data / comparison | Starting choice | What to disclose or check |
|---|---|---|
| Equal additive changes | Linear | Units and range |
| Positive ratios across orders of magnitude | Log | No zero/negative observations; handling of invalid values |
| Signed values across orders of magnitude | Symlog | Linear region around zero and its transition |
| Probabilities strictly between 0 and 1 | Logit | Endpoint treatment and transformed interpretation |
| Domain-specific monotone mapping | Function scale | Valid domain, forward/inverse pair, ticks |
| Angle and radius | Polar | Angular convention, radial origin/range, wrapping |

The source's enumeration of four built-in scales is historical; current versions provide others. Never add arbitrary positive offsets solely to make a log plot run. Explain a scientifically justified transformation or choose another representation.

## Projection reasoning

For polar data, supply angle/radius and let the axes project them. The forward map is `(r*cos(theta), r*sin(theta))`; the inverse supports interaction and coordinate recovery. Label orientation, radial origins, and angular/radial limits determine how the reader interprets the image.

Projection changes positions and path geometry; ordinary text, line widths, and markers are largely designed to remain readable in display space. If text must follow a nonlinear curve, convert it to geometry deliberately using TextPath, accepting the readability trade-off.

For geographic work, choose the projection and coordinate reference system from the geography. A polar plot is not a cartographic projection. The book lists Cartopy and other extensions as examples; check their present documentation and the project's actual dependencies before using them.

## Worked decision

For message ages ranging from milliseconds to seconds, a positive log axis can expose ratios. If age can be exactly zero, first determine whether zero is a real reset or an instrument floor. A linear panel, justified symlog scale, or clearly identified floor treatment may be more faithful. A logarithm of zero is not a valid plotted value.

Use a 3D projection only when the third dimension communicates needed structure. Its painter-style drawing can misorder overlapping objects; apparent depth is not proof of accurate visibility. See [going 3D](ch11-going-3d.md). Typography and color still need deliberate design under any projection.
