# 10. Animation

Source: PDF pp. 145–158 (printed pp. 121–134). Use when temporal development itself is the message.

## Reuse artists, update state

Create the figure, axes, limits, labels, and artists once. The frame callback updates existing line data, scatter offsets/sizes/colors, image arrays, or text. Clearing the axes and rebuilding every object adds work and can change layout or scales unexpectedly.

Use `FuncAnimation` with an explicit finite frame sequence for reproducible export. Keep a reference to the animation for its lifetime. If blitting is enabled, both initialization and update callbacks return the artists that need redrawing; verify that the backend and changing elements support blitting. A frame interval controls intended interactive delay, while a writer's FPS sets exported playback timing.

## Reconstruct the source's examples

- **Progressive sine/cosine:** create two lines, then reveal increasingly long slices with `set_data`. The source uses a marker at the final data point to expose the moving endpoint.
- **Rain rings:** maintain a fixed pool of markers. Each frame increases size, decreases opacity, and recycles an expired marker at a new position. A bounded pool avoids unbounded artist creation.
- **Earthquake map:** update geographic point positions under a declared map transform. If event time is ignored, the animation cannot be interpreted as a chronology of earthquakes; the source example explicitly omits event times.
- **Scenario-driven fluid display:** keep a separate frame-to-event schedule; the renderer applies the scenario to model state. Distinguish the simulation algorithm from how its fields are visualized.

## Scientific scale decisions

The fluid showcase changes image color limits each frame. That can reveal instantaneous structure, but it also changes the numeric meaning of a color. For comparison over time, fix a common norm or visibly disclose changing limits. Do not present per-frame rescaling as a universal cure for flicker. Likewise, keep spatial axes fixed when changing ranges could suggest motion or growth that is only an autoscaling artifact.

## Export and review

Select an installed writer and supported destination format; FFmpeg requires its executable, while other writers have different dependencies and memory costs. Do not install or download a tool simply because the source assumes it. For long exports, use progress callbacks rather than interpreting an unresponsive window as failure.

Inspect representative early, middle, and late frames plus the actual saved playback when available. Verify timing, legends, normalization, missing data, and the scientific interpretation of frame order. Animation is not a substitute for a static comparison when the reader needs precise side-by-side judgment.

Connects to [optimization](ch12-optimization.md), [color](ch05-colors.md), and [graphic library](ch13-graphic-library.md).
