# 6. Ten simple rules

Source: PDF pp. 95–108 (printed pp. 71–84). This chapter reproduces Rougier, Droettboom, and Bourne's 2014 article. Use these named rules as a practical critique framework.

| Rule | Apply it by checking |
|---|---|
| 1. Know Your Audience | What prior knowledge and reading time can the design assume? |
| 2. Identify Your Message | What should a reader be able to conclude from the actual evidence? |
| 3. Adapt the Figure to the Support Medium | Are complexity, label size, line widths, and contrast appropriate to paper, poster, or projection? |
| 4. Captions Are Not Optional | Can the reader understand symbols, variables, units, conditions, and uncertainty without guessing? |
| 5. Do Not Trust the Defaults | Are automatic ranges, ticks, styles, fonts, and colors appropriate here? |
| 6. Use Color Effectively | Does each color distinguish, order, or highlight something meaningful? |
| 7. Do Not Mislead the Reader | Do scale, area, perspective, cropping, and omission preserve the quantitative comparison? |
| 8. Avoid Chartjunk | Does each visible element help explain or read the data? |
| 9. Message Trumps Beauty | Does the visual remain accurate and readable when decorative choices are removed? |
| 10. Get the Right Tool | Is the chosen tool suitable for the required figure and output? |

## Turn the rules into an editing procedure

State the message in one sentence. Trace it to the displayed evidence. Identify the most consequential source of ambiguity or distortion and fix that first. Recheck the entire figure at its final size; a local improvement can introduce global collisions or change the visual hierarchy.

Use zero baselines for bars when length is the quantitative encoding. If a restricted range is justified for a different encoding, make the scale and context explicit. When circular area represents quantity, area should be proportional to the value; encoding value directly as radius exaggerates differences. Matplotlib scatter's `s` is in squared points, while a circle patch's radius is a length.

Captions should explain how to read the figure and identify what the marks represent. Put exact numerical values elsewhere when the claim depends on precision that the graphic cannot provide. Do not infer significance, confidence intervals, or sample size from visual decoration.

## Worked reconstruction: too many traces

If seven equally important traces obscure one another, arbitrary colors and an overlapping legend may worsen the problem. Reconstruct the source's approach with seven aligned panels: emphasize one trace per panel and show the others lightly for context. Direct labels eliminate legend lookup. Use shared scales and mark the reference range clearly in the caption. Keep ticks only where they support comparison. The point is to preserve equal access to all seven traces, not to remove axes universally.

The source's sketch-style hypothetical curve communicates a conceptual hypothesis. Apply that choice only to explicitly illustrative content. Sketch styling does not excuse invented or concealed measurements.

Connects to [color](ch05-colors.md), [layout](ch08-layout.md), and [ornaments](ch09-ornaments.md). The original article is linked in [source notes](source-notes.md).
