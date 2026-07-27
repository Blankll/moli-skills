# Checklist — the gate before "done"

Run this on any page/component before claiming it's finished. Every box must be checked or consciously waived. Pair it with a visual compare against `reference.html`.

## Surface & layout
- [ ] Page ground is `#f5f5f7` (COOL — not warm cream/beige/off-white).
- [ ] Content sits on `#fff` surfaces; container centered (`max-width` 720 reading / 1080 grid), side padding 22px.
- [ ] Sibling same-kind items use **one panel + hairline dividers** (`rgba(0,0,0,0.07)`), not separate bordered/tinted cards.
- [ ] Layout is flex/grid + `gap` — not inline elements + margin.
- [ ] Sections separated by `clamp(34px,6vw,56px)`; panels sized to content, not all equal-padded.

## Glass
- [ ] `backdrop-filter` appears **only** on sticky nav / overlay / colored CTA.
- [ ] No glass on plain content cards, list rows, or between white blocks.
- [ ] Glass-on-color has blurred light orbs behind it.

## Type
- [ ] System font stack (SF / PingFang) — no Inter/Roboto/Arial as brand face.
- [ ] Big titles have **negative letter-spacing** (bigger → more negative).
- [ ] Long body line-height ≥ 1.85.
- [ ] Numbers use `tabular-nums`.
- [ ] CJK↔Latin have a half-width space between them.

## Color
- [ ] Body world is grayscale; color appears only as accent (one blue) / heat / brand / live.
- [ ] No tinted backgrounds, colored left-bars, or gradient washes on plain content.
- [ ] At most one accent color competing in a single view.

## Radius & shadow
- [ ] Radius taken from named tiers (pill 999 / thumb 12 / card 18 / panel 22 / hero 26).
- [ ] Shadows are two-layer (tight contact + soft spread); no single hard drop-shadow.

## Motion & accessibility
- [ ] Hover = gentle lift (`translateY(-2~-3px)`) or row tint, 0.15–0.25s.
- [ ] No opacity-fade entrance keyframes on async-rendered content.
- [ ] Touch targets ≥ 44px; mobile collapses to one column.
- [ ] `prefers-reduced-motion` / `prefers-reduced-transparency` / `prefers-contrast` all handled (see motion.md).

## Restraint
- [ ] Removed avoidable noise: extra icons, stat padding, decorative emoji.
- [ ] Every element carries meaning; nothing is there just to look "rich/techy/designed".

## Interaction foundations
- [ ] Every screen answers: where am I / where can I go / what's there / how out.
- [ ] Controls sit next to what they affect; labels are specific, not generic.
- [ ] Feedback on pointer-down (not just on release) for interactive elements.
- [ ] Sticky chrome uses scroll-edge (hairline only when content scrolls beneath).

## Final
- [ ] Side-by-side, it looks like it belongs on the same page as `reference.html`.