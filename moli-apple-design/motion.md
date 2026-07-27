# Motion Design Reference

## Philosophy

Apple-quality motion serves three masters simultaneously:

1. **Feedback** — every touch, every gesture, every state change must be acknowledged instantly. The response begins on pointer-down, not on release. Motion is the UI saying "I heard you."
2. **Spatial understanding** — motion must build and reinforce a consistent mental model of where things live, where they came from, and where they went. Elements that materialize should appear to grow from their trigger. Elements that dismiss should shrink to their origin. Panels slide from screen edges. Sheets rise from the bottom. This spatial consistency is the foundation of navigational trust.
3. **Deference** — motion assists comprehension, it does not compete for attention. Static content gets a tiny motion budget (hover lift, pulse indicators, segmented slide). Interactive layers get the full fluid treatment because the user is actively engaged. Never animate for animation's sake.

These three principles govern every decision below.

---

## Static Content Motion Budget

Content the user is passively reading or viewing gets deliberately restrained motion. The goal is subtle liveliness, not spectacle.

- **Hover lift**: `translateY(-1px or -2px)` with subtle shadow elevation. ~150ms `var(--ease-out-quart)`. Never more than 2px.
- **Pulse dot** (for live/active indicators): `scale` oscillation between 1 and ~1.15, duration ~2s, `var(--ease-out-quart)`. Loop with `animation-iteration-count: infinite`.
- **Segmented control slide**: the active highlight slides between segments. Use CSS `transition` on `translateX` and `width`, ~200ms `var(--ease-out-quart)`. Do NOT animate individual segment text color—transition the highlight behind it.
- **List item tap feedback**: quick opacity dip to ~0.6 on `pointer-down`, returning on `pointer-up`. ~100ms linear each direction. No transform shift unless the item supports drag-to-reorder.
- **Loading shimmer / skeleton**: `opacity` pulse on a gradient overlay, ~1.5s loop, `var(--ease-out-quart)`. Keep the shimmer subtle—moving highlight, not flashing.
- **Async content entrance**: do NOT use opacity-fade keyframes or staggered entrance animations on content that loads after the initial render. Content should simply appear in its position. If a gentle fade-in is desired for UX continuity, apply no more than a 150ms `opacity` transition, not keyframes. The UI should never feel like it's waiting for animations to finish so it can become usable.
- **Scroll-triggered reveals**: avoid unless the content benefits from sequential disclosure (e.g., a feed of cards). If used, use a single `opacity + translateY(8px)` enter, ~350ms `var(--ease-out-quart)`, staggered 50–80ms apart. Do NOT re-animate on re-scroll.

> **Rule of thumb**: if the content is readable and interactive without the animation, the animation is decoration, not function. Decoration is acceptable in tiny doses; abundance of decoration is noise.

---

## Interactive Layers: Full Fluid Treatment

Dialogs, sheets, popovers, drawers, tooltips, menus, and any layer summoned by a user action get the complete motion treatment:

### Core Requirements

| Principle | Implementation |
|---|---|
| **Feedback on pointer-down** | Visual response begins the instant the finger/mouse touches the trigger. `:active` styles or `pointerdown` handlers, not `pointerup`. |
| **Enter timing** | ~400ms using `var(--ease-spring)` cubic-bezier |
| **Exit timing** | ~250–300ms, same easing curve (not mirrored) |
| **Enter/exit path symmetry** | Exit retraces the exact enter path in reverse. Same transform-origin, same axis, same curve. |
| **transform-origin** | Anchored to the trigger element's center. `calc()` from trigger bounding rect to layer center. |
| **Glass materialize** | `backdrop-filter: blur()` radius + `scale` + `opacity` animate together on enter. See [Materialize deep-dive](#materialize) below. |
| **CSS transitions** | Use CSS `transition` properties, NOT `@keyframes`, so that if the user re-triggers mid-flight the animation reverses smoothly from the current visual state. |
| **Interruptible exit** | If the user triggers close while the enter animation is still running, the exit picks up from the current interpolated position. CSS transitions handle this natively. |

### Spring Parameters

| Use Case | Easing | Duration | Notes |
|---|---|---|---|
| Dialog / sheet / drawer enter | `var(--ease-spring)` | ~400ms | Slight overshoot at the end gives a "settling" feel. Amplitude < 5%. |
| Dialog / sheet / drawer exit | `var(--ease-spring)` | ~250ms | Faster exit. Same curve, no overshoot on reverse. |
| Popover / tooltip enter | `var(--ease-spring)` | ~300ms | Smaller distance, quicker settle. |
| Popover / tooltip exit | `var(--ease-spring)` | ~200ms | Tools should dismiss snappily. |
| Menu expand (vertical) | `var(--ease-spring)` | ~350ms | Height + opacity. |
| Drag-to-dismiss sheet | Spring (physics) | dynamic | Driven by gesture, see [Gesture design](#gesture-design). |
| Segmented control slide | `var(--ease-out-quart)` | ~200ms | No overshoot. Precision required. |

#### Spring Physics Equivalents

When implementing in code with a spring physics library (Motion / Framer Motion / React Spring):

| CSS Easing | Motion `spring` params | Framer Motion `transition` |
|---|---|---|
| `var(--ease-spring)` | `{ damping: 1.0, response: 0.4 }` (critically damped) | `{ type: "spring", damping: 20, stiffness: 300, mass: 1 }` |
| `var(--ease-out-quart)` (0.25, 1, 0.5, 1) | N/A — use CSS transition | `{ type: "tween", ease: [0.25, 1, 0.5, 1], duration: 0.2 }` |

> **Note**: CSS `cubic-bezier(0.32, 0.72, 0, 1)` (`--ease-spring`) and a critically-damped spring with `damping: 1.0` + `response: 0.4` produce nearly identical motion curves. The CSS approach is lighter and interruptible by the browser's compositor. The spring approach gives you velocity handoff for gesture-driven interactions. Choose based on whether the animation is trigger-fixed (CSS) or gesture-driven (spring).

---

## Deep Dives

### Interruptibility

**The single most important principle in production motion.**

Every animation must be interruptible. The user should never feel trapped waiting for an animation to finish before they can act again.

#### Rules

1. **Animate from the current presentation value, never from the target value.** When an animation is interrupted, read `getComputedStyle()` or the current interpolated value—do NOT snap to the original starting value and replay from there.
2. **Avoid CSS transitions / `@keyframes` for gesture-driven motion.** CSS transitions snap to the computed end value when interrupted, then replay from the snapped value. This creates the "brick wall" problem where a rapidly-swiped sheet jerks back to its start position before following the finger. For gesture-driven motion, use spring physics with imperative control.
3. **Decompose 2D motion into independent X/Y springs.** A diagonal drag should not couple axes into a single transform. Let X and Y resolve independently with the same spring parameters. This prevents diagonal paths from feeling "magnetic" to one axis.
4. **Carry velocity through re-targeting.** If the user releases a sheet at 800px/s and immediately taps a button to dismiss it, the exit animation should inherit that 800px/s as initial velocity. Do NOT reset velocity to 0 on re-target. This is the difference between "brick wall" and buttery.
5. **CSS transitions (non-gesture) are automatically interruptible** when applied as `transition` properties rather than `@keyframes`. The browser interpolates from the current value to the new target. This is correct for trigger-based layers (dialog open/close).

#### Implementation pattern (gesture-driven)

```
pointerdown → capture pointer → start tracking delta
  → apply delta as transform (translateX, translateY)
  → on each frame, check if a transition/animation is running
  → if interrupted, cancel running animation, set start value to current render value
  → start new animation from current value with new target + carried velocity
```

### Velocity Handoff

When a gesture ends (pointerup), the user's finger was moving at a certain velocity. That velocity must be passed as the **initial velocity** of the spring animation that settles the element into its final position.

#### Why

Without velocity handoff, a flicked sheet decelerates from zero—it starts slow, builds up, and feels like it hit molasses. With velocity handoff, the sheet glides from the user's flick speed to rest, conserving the sense of momentum.

#### Implementation

```javascript
// On pointerup:
const velocity = {
  x: calculateVelocity(lastPositions, timestamp),
  y: calculateVelocity(lastPositions, timestamp),
};

// Pass as spring initial velocity
spring.start({
  from: { x: currentDeltaX, y: currentDeltaY },
  to: { x: snapTargetX, y: snapTargetY },
  velocity, // ← this is the key
  damping: 1.0,
  response: 0.35,
});
```

Velocity is typically calculated from the last 3–5 pointermove events using linear regression or weighted delta over time.

### Momentum Projection

Given a release velocity and a deceleration rate, predict where the element would stop under friction alone. Used to decide snap targets and rubber-band thresholds.

```javascript
function project(velocity, decelerationRate = 0.998) {
  // decelerationRate: 1.0 = no friction, 0.99 = heavy friction
  // Apple uses ~0.998 for UIScrollView
  const d = decelerationRate;
  return (velocity / 1000) * d / (1 - d);
}
```

**Use case**: when the user flicks a horizontally-scrolling card carousel, project the distance, round to the nearest snap point, and animate to that snap point with a spring carrying the release velocity.

**Threshold gates**: if the projected distance is below a threshold (e.g., 20px), snap back to the current item. This prevents accidental micro-swipes from changing selection.

### Rubber-banding

When a user drags an element past its boundary (e.g., pulling a sheet down past its open position), apply progressive resistance instead of a hard stop.

#### Formula

```javascript
function rubberBand(distance, boundary, tension = 0.55) {
  // distance: how far past the boundary (positive)
  // boundary: the limit value
  // tension: 0 = locked, 1 = linear (no resistance)
  const abs = Math.abs(distance);
  const sign = distance > 0 ? 1 : -1;
  const resisted = boundary * (1 - Math.pow(1 - abs / boundary, tension));
  return sign * resisted;
}
```

**Common values**: `tension: 0.55` for sheets and scroll views. Higher = stiffer resistance.

**Application**: when dragging a bottom sheet past its fully-open position, the sheet should resist but yield slightly to show the user they've hit the limit. On release, spring back to the boundary.

#### Overflow/dismiss distinction

- **Slight overflow** (< 30% past boundary): rubber-band and snap back.
- **Strong overflow** (> 30% past boundary or sufficient velocity): treat as dismiss gesture.

### Materialize

Glass surfaces (backdrop-filter blur) should not pop in. The blur radius, scale, and opacity should animate together on enter and reverse on exit.

#### Enter

```css
.glass-layer {
  opacity: 0;
  scale: 0.95;
  backdrop-filter: blur(0px);
  transition:
    opacity 400ms var(--ease-spring),
    scale 400ms var(--ease-spring),
    backdrop-filter 400ms var(--ease-spring);
}

.glass-layer.open {
  opacity: 1;
  scale: 1;
  backdrop-filter: blur(20px); /* or design token */
}
```

- Start: `opacity: 0`, `scale: 0.95`, `blur(0px)`
- End: `opacity: 1`, `scale: 1`, `blur(20px)` (adjust to design token)
- Same timing curve for all three properties so they arrive together

#### Exit

Reverse on all three properties simultaneously. Duration ~250ms. Same easing curve.

```
opacity: 1 → 0
scale: 1 → 0.95
blur(20px) → blur(0px)
```

#### Why this works

The blur masks the slight low-resolution appearance of the content at 0.95 scale. As the blur fades out, the scale resolves to 1.0, so the eye never sees a "soft then sharp" step—the transition is seamlessly masked.

---

## CSS Easing Tokens

```css
:root {
  /* Spring-like ease for interactive layers */
  --ease-spring: cubic-bezier(0.32, 0.72, 0, 1);

  /* Standard deceleration for static content */
  --ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);

  /* Convenience aliases */
  --ease-in-out-quint: cubic-bezier(0.83, 0, 0.17, 1);
}
```

### Token Reference

| Token | Curve | Character | Use |
|---|---|---|---|
| `--ease-spring` | (0.32, 0.72, 0, 1) | Fast start, gentle end, tiny overshoot | Interactive layers enter/exit |
| `--ease-out-quart` | (0.25, 1, 0.5, 1) | Smooth deceleration, no overshoot | Static content, UI chrome, seg slides |
| `--ease-in-out-quint` | (0.83, 0, 0.17, 1) | Symmetric ease | System-wide transitions (rare) |

### Spring Library Equivalents

When translating to code:

| CSS Token | Motion One | Framer Motion | React Spring |
|---|---|---|---|
| `--ease-spring` | `{ easing: spring({ damping: 1, stiffness: 200 }) }` | `{ type: "spring", damping: 20, stiffness: 300, mass: 1 }` | `{ config: { tension: 280, friction: 40, mass: 1 } }` |
| `--ease-out-quart` | `{ easing: cubicBezier(0.25, 1, 0.5, 1), duration: 200 }` | `{ type: "tween", ease: [0.25, 1, 0.5, 1], duration: 0.2 }` | `{ config: { duration: 200, easing: ... } }` |

---

## Gesture Design

### Press Feedback

Every interactive element must respond **on `pointerdown`**, not `pointerup`.

```css
.button {
  transition:
    transform 100ms var(--ease-out-quart),
    opacity 100ms var(--ease-out-quart);
}

.button:active {
  transform: scale(0.97);
  opacity: 0.7;
}
```

- Respond within 100ms of pointer-down. This is the threshold beneath which delay feels like "the UI is ignoring me."
- Restore on pointer-up (or pointer-cancel if the gesture leaves the element).

### Drag / Swipe

- **1:1 tracking**: the element's `translateX`/`translateY` equals the pointer delta from the initial down position. No dead zones.
- **`setPointerCapture`**: call `element.setPointerCapture(event.pointerId)` on pointerdown to ensure the element receives all subsequent pointer events even if the pointer leaves the element bounds. This prevents the "slip off" problem where swiping fast loses tracking.
- **Respect grab offset**: if the user grabs a sheet by its handle (say 60px from the top), the initial `pointerdown` establishes an origin. Delta is calculated as `pointerPosition - originPosition`, not `pointerPosition - layerDefaultPosition`. This prevents a snap on first frame.
- **Release behavior**: snap-to-target with spring + velocity handoff. See [Velocity Handoff](#velocity-handoff).

### Tap

A tap is distinguished from a drag by total displacement. Hysteresis:

```javascript
const TAP_HYSTERESIS = 10; // px

function isTap(pointerDownPos, currentPos) {
  const dx = currentPos.x - pointerDownPos.x;
  const dy = currentPos.y - pointerDownPos.y;
  return Math.sqrt(dx * dx + dy * dy) < TAP_HYSTERESIS;
}
```

- If displacement stays under ~10px between pointerdown and pointerup, treat as a tap. Fire `click`.
- If displacement exceeds threshold, treat as a drag. Do NOT fire `click`.
- **Timing threshold** (optional): if the finger stays down > 500ms without moving, treat as long-press. Provide clear visual feedback at ~300ms (scale/highlight change).

### Parallel Gesture Detection

A sheet might need to distinguish between:
- Vertical drag (to dismiss the sheet)
- Horizontal swipe (to page through content inside the sheet)
- Scroll (within a scrollable region inside the sheet)

**Strategy**: track the initial axis of movement. If the first N pixels of movement are primarily horizontal, lock to horizontal panning. If primarily vertical, lock to vertical. Use a 7–10px lock-in threshold.

```javascript
const AXIS_LOCK_THRESHOLD = 8;
let axisLock = null; // 'x', 'y', or null

function onPointerMove(event) {
  const dx = event.clientX - downPos.x;
  const dy = event.clientY - downPos.y;

  if (!axisLock && (Math.abs(dx) > AXIS_LOCK_THRESHOLD || Math.abs(dy) > AXIS_LOCK_THRESHOLD)) {
    axisLock = Math.abs(dx) > Math.abs(dy) ? 'x' : 'y';
  }

  if (axisLock === 'x') handleHorizontalPan(dx);
  else if (axisLock === 'y') handleVerticalPan(dy);
}
```

---

## Reduced Motion & Accessibility

Three mandatory media queries. Every interactive layer must implement all three.

### 1. `prefers-reduced-motion`

Replace slide/scale animations with cross-fade opacity transitions. Sheet still enters/exits, but via `opacity` only (no transform).

```css
@media (prefers-reduced-motion: reduce) {
  .layer-enter {
    transition: opacity 200ms ease !important;
    transform: none !important;
    scale: none !important;
  }

  .layer-exit {
    transition: opacity 150ms ease !important;
    transform: none !important;
    scale: none !important;
  }

  /* No spring, no overshoot */
  --ease-spring: ease;
  --ease-out-quart: ease;
}
```

### 2. `prefers-reduced-transparency`

Solidify glass surfaces. Replace `backdrop-filter: blur()` and semi-transparent backgrounds with near-opaque backgrounds.

```css
@media (prefers-reduced-transparency: reduce) {
  .glass-layer {
    backdrop-filter: none !important;
    background: var(--surface-elevated) !important; /* solid color */
    /* Keep opacity animation for enter/exit, but only on the solid background */
  }
}
```

### 3. `prefers-contrast`

When the user requests increased contrast, use near-solid backgrounds on layers and ensure text meets WCAG AAA contrast against the layer background.

```css
@media (prefers-contrast: more) {
  .glass-layer {
    backdrop-filter: none !important;
    background: var(--surface-elevated) !important;
    border: 1px solid var(--border-contrast);
  }

  .layer-content {
    color: var(--text-contrast);
  }
}
```

### Implementation Rule

All three queries must be tested in the same file/modal component. Do not ship an interactive overlay without all three.

---

## Frame-Level Smoothness

Every animation must run at 60fps (120fps on ProMotion displays). No dropped frames, no jank.

### Compositor-Only Properties

**Animate only:**

- `transform` (translate, scale, rotate)
- `opacity`

These properties are handled by the GPU compositor thread and do not trigger layout or paint.

**Avoid animating:**

- `width`, `height` (triggers layout)
- `top`, `left`, `right`, `bottom` (triggers layout)
- `margin`, `padding` (triggers layout)
- `box-shadow` (triggers paint, expensive)
- `border-radius` (triggers paint)
- `color`, `background-color` (triggers paint)
- `filter` (triggers paint, expensive—use `backdrop-filter` sparingly)
- `backdrop-filter` (GPU-accelerated on modern browsers, but keep blur radius changes to enter/exit only, not per-frame during gestures)

### Performance Checklist

- [ ] All animated properties are `transform` and/or `opacity` only
- [ ] No layout-triggering properties in transition lists
- [ ] Use `will-change: transform, opacity` on elements that animate, but remove after animation completes to free GPU memory
- [ ] For gesture-driven animations, use `requestAnimationFrame` loops, not `setInterval` or `css transition`
- [ ] For CSS transitions, prefer `transition` shorthand on a dedicated class rather than inline styles (avoids style recalculation)
- [ ] Test on low-powered devices (iPhone SE, iPad base model) — if it runs smoothly there, it runs smoothly everywhere

### requestAnimationFrame Pattern

```javascript
function startGestureAnimation(updateFn) {
  let rafId;

  function tick() {
    updateFn();
    rafId = requestAnimationFrame(tick);
  }

  rafId = requestAnimationFrame(tick);

  return () => cancelAnimationFrame(rafId); // cleanup
}
```

Do NOT use `setInterval` for animation frames. `requestAnimationFrame` pauses when the tab is backgrounded, saving battery and preventing hidden jank.

---

## Motion Self-Check

Before shipping any motion work, run this checklist:

### Static Content

- [ ] Are hover lifts below 3px?
- [ ] Do pulse indicators use `scale`, not `opacity` fading the entire element?
- [ ] Is the segmented control slide using `translateX` + `width` transition (not per-segment color animation)?
- [ ] Does async content appear without keyframed entrance animations?
- [ ] Are scroll-triggered reveals limited to one `opacity + translateY` pass?

### Interactive Layers

- [ ] Does the visual response begin on `pointerdown` (not `pointerup`)?
- [ ] Is enter timing ~400ms and exit timing ~250–300ms?
- [ ] Does exit retrace the exact enter path in reverse (same transform-origin, same curve)?
- [ ] Is `transform-origin` anchored to the trigger element's center?
- [ ] Is the glass materialization animating blur + scale + opacity together?
- [ ] Are CSS `transition` properties used instead of `@keyframes` for layer enter/exit?
- [ ] Can the animation be interrupted mid-flight and reversed without snapping?

### Springs & Gestures

- [ ] Is `setPointerCapture` called on `pointerdown` for draggable elements?
- [ ] Is the grab offset respected (no snap on first frame)?
- [ ] Does the element carry release velocity into the settle spring?
- [ ] Are 2D motions decomposed into independent X/Y springs?
- [ ] Is rubber-banding applied at boundaries with a tension value?
- [ ] Is there a hysteresis threshold (~10px) to distinguish tap from drag?
- [ ] Is axis lock applied (~8px threshold) for parallel gesture detection?

### Performance

- [ ] Are all animated properties `transform` and/or `opacity` only?
- [ ] Is `requestAnimationFrame` used instead of `setInterval` for gesture-driven animations?
- [ ] Are `will-change` values cleaned up after animation completes?
- [ ] Has the animation been tested on a low-powered device?

### Reduced Motion

- [ ] Does `prefers-reduced-motion` replace slide/scale with cross-fade opacity?
- [ ] Does `prefers-reduced-transparency` solidify glass surfaces with solid backgrounds?
- [ ] Does `prefers-contrast` use near-solid backgrounds and ensure AAA contrast?
- [ ] Are all three queries implemented in the same component?

### General

- [ ] Does every animation serve a purpose (feedback, spatial understanding, or deference)?
- [ ] Would removing the animation make the UI harder to understand? (If yes, keep it. If no, consider removing it.)
- [ ] Is there any animation that runs longer than 400ms for a non-essential effect? (If yes, reduce it.)
