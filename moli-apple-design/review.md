# Review mode — audit an existing UI against the system

Use when the user has existing CSS / a page / a component and asks "is this Apple enough / what can be improved / make it consistent".

## First: find the real visual surface
A content generator (markdown, JSON, API) usually has no design of its own — the look lives in the **rendering layer**. Point at the CSS/template it feeds.

## Process
1. **Inventory.** Read the target file(s) in full. Note every color, font, radius, shadow, border, spacing decision.
2. **Score against `design-system.md`** on each axis.
3. **Run `checklist.md` + the anti-slop list.** Flag each violation with `file:line`.
4. **Prioritize:**
   - **P0** — breaks the aesthetic outright (wrong accent, warm ground, fragmented colored cards, generic font)
   - **P1** — inconsistency / drift (ad-hoc radius, wrong grey, hard divider instead of hairline)
   - **P2** — polish (slightly-off radius, spare emoji, minor spacing)
5. **Map each fix to a token** (`tokens.css`) and a component/pattern.
6. **Implement toward `reference.html`**, re-render and compare.

## Output format
| Pri | Finding (`file:line`) | Now | → Apple |
|---|---|---|---|
| P0 | accent everywhere | warm orange | Apple blue; grayscale body |
| P1 | text `#333` | generic grey | `#1d1d1f` / `#6e6e73` |

End with the single highest-leverage change.