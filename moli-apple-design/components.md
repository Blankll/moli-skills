# Components — copy-paste library

All snippets use the `tokens.css` custom properties (`var(--…)`). Paste, then swap content. Keep the **structure** and the **tokens**; don't re-introduce raw values or fragment the surfaces. See these rendered together in `reference.html`.

---

## 1. Sticky glass nav

The one place glass is mandatory (it overlaps scrolling content).

```html
<header class="glass-nav" style="position:sticky; top:0; z-index:50;">
  <div style="max-width:var(--max-grid); margin:0 auto; padding:0 var(--pad-x); height:54px;
              display:flex; align-items:center; justify-content:space-between; gap:16px;">
    <a href="/" style="display:flex; align-items:center; gap:9px; text-decoration:none; color:var(--text);">
      <img src="/icon.png" width="24" height="24" alt="">
      <span style="font-size:15px; font-weight:650; letter-spacing:-0.01em;">Brand</span>
    </a>
    <a href="/search" style="display:inline-flex; align-items:center; height:32px; padding:0 14px;
       border-radius:var(--r-pill); background:rgba(0,0,0,0.05); color:var(--text); font-size:13px;
       font-weight:550; text-decoration:none;">Ask AI</a>
  </div>
</header>
```

## 2. Page hero

```html
<section style="max-width:var(--max-read); margin:0 auto; padding:clamp(36px,6vw,64px) var(--pad-x) clamp(20px,4vw,32px);">
  <div style="display:flex; align-items:center; gap:9px; font-size:12px; font-weight:600;
              letter-spacing:0.14em; color:var(--text-3);">
    <span style="width:7px; height:7px; border-radius:50%; background:var(--live); animation:pulse-dot 2.2s infinite;"></span>
    EYEBROW · LIVE
  </div>
  <h1 style="margin-top:15px; font-size:clamp(32px,6vw,52px); font-weight:700; letter-spacing:-0.03em; line-height:1.06;">
    The headline
  </h1>
  <p style="margin-top:16px; font-size:clamp(15px,2.5vw,18px); color:var(--text-2); line-height:1.6; max-width:560px;">
    One restrained sub-line. No filler, no "in today's world".
  </p>
</section>
```

## 3. Unified panel list ⭐ (the anti-fragmentation pattern)

Sibling items go on **one** white panel, separated by hairlines — never as separate bordered cards.

```html
<div style="background:var(--surface); border-radius:var(--r-panel); box-shadow:var(--sh-panel); overflow:hidden;">
  <a class="row" href="#" style="display:block; padding:16px clamp(17px,3vw,24px); color:var(--text); text-decoration:none;">
    <h3 style="font-size:17px; font-weight:600; letter-spacing:-0.01em; line-height:1.45;">Row title</h3>
    <p style="margin-top:4px; font-size:13.5px; color:var(--text-2);">One line of supporting context.</p>
  </a>
  <a class="row" href="#" style="display:block; padding:16px clamp(17px,3vw,24px); color:var(--text); text-decoration:none;">
    <h3 style="font-size:17px; font-weight:600; letter-spacing:-0.01em; line-height:1.45;">Another row</h3>
    <p style="margin-top:4px; font-size:13.5px; color:var(--text-2);">Continuous surface, not islands.</p>
  </a>
</div>
```
```css
.row + .row { border-top: 1px solid var(--hairline); }
.row:hover  { background: var(--hover); transition: background .15s; }
```

## 4. Standard card + grid

```html
<div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(290px, 1fr)); gap:14px;">
  <a class="card" href="#" style="background:var(--surface); border-radius:var(--r-card); box-shadow:var(--sh-card);
     padding:18px; color:var(--text); text-decoration:none; display:block;">
    <h3 style="font-size:17px; font-weight:600; letter-spacing:-0.01em;">Card title</h3>
    <p style="margin-top:6px; font-size:13.5px; color:var(--text-2); line-height:1.5;">Summary…</p>
  </a>
</div>
```
```css
.card { transition: transform .2s, box-shadow .2s; }
.card:hover { transform: translateY(-3px); box-shadow: var(--sh-lift); }
```

## 5. Segmented pill control (apple.com style)

```html
<div class="seg" style="display:inline-flex; background:rgba(0,0,0,0.05); border-radius:var(--r-pill); padding:3px; gap:2px;">
  <button data-seg="a">Unified</button>
  <button data-seg="b">Grid</button>
  <button data-seg="c">Focus</button>
</div>
```
```css
.seg button {
  border:none; cursor:pointer; font-size:13px; font-weight:500; padding:7px 15px;
  border-radius:var(--r-pill); background:transparent; color:var(--text-2); transition:all .25s cubic-bezier(.25,.1,.25,1);
}
.seg button.active {
  background:var(--surface); color:var(--text); font-weight:600; box-shadow:0 1px 3px rgba(0,0,0,0.12);
}
.seg button.active--black {
  background:var(--text); color:#fff; box-shadow:0 1px 2px rgba(0,0,0,0.22), inset 0 1px 0 rgba(255,255,255,0.16);
}
```

## 6. Tags / chips

```html
<span style="font-family:var(--mono); font-size:10.5px; font-weight:700; color:#fff; background:var(--x-blue); padding:2px 7px; border-radius:var(--r-chip);">X</span>
<span style="font-size:11.5px; color:var(--text-2); background:rgba(0,0,0,0.05); padding:3px 10px; border-radius:var(--r-pill);">plain tag</span>
<span style="font-size:11.5px; color:var(--accent-link); background:rgba(0,113,227,0.08); padding:3px 10px; border-radius:var(--r-pill); font-weight:550;">accent tag</span>
<span style="font-size:11.5px; font-weight:650; color:var(--heat); background:var(--heat-bg); padding:3px 10px; border-radius:var(--r-pill);">🔥 hottest</span>
```

## 7. Buttons

```html
<!-- primary -->
<a style="display:inline-flex; align-items:center; height:44px; padding:0 22px; border-radius:var(--r-pill);
   background:var(--accent); color:#fff; font-size:15px; font-weight:600; text-decoration:none;">Primary →</a>
<!-- secondary / light glass -->
<a style="display:inline-flex; align-items:center; height:44px; padding:0 19px; border-radius:var(--r-pill);
   background:rgba(255,255,255,0.8); border:1px solid rgba(0,0,0,0.08); box-shadow:0 1px 2px rgba(0,0,0,0.05);
   color:var(--text); font-size:14px; font-weight:550; text-decoration:none;">Secondary</a>
```
Touch target ≥ 44px high.

## 8. Colored CTA with liquid-glass ⭐

```html
<section style="position:relative; overflow:hidden; border-radius:var(--r-hero); padding:clamp(26px,4vw,40px);
                background:var(--grad-cta); box-shadow:var(--sh-cta);">
  <div style="position:absolute; width:260px; height:260px; border-radius:50%; background:rgba(255,255,255,0.18); filter:blur(46px); top:-80px; right:-40px;"></div>
  <div style="position:absolute; width:200px; height:200px; border-radius:50%; background:rgba(120,80,255,0.5); filter:blur(50px); bottom:-90px; left:12%;"></div>
  <div style="position:relative;">
    <h2 style="font-size:clamp(18px,3vw,24px); font-weight:700; color:#fff; letter-spacing:-0.02em;">CTA headline</h2>
    <p style="margin-top:10px; font-size:14px; color:rgba(255,255,255,0.82); line-height:1.6; max-width:460px;">Supporting line.</p>
    <div style="display:flex; gap:10px; margin-top:20px; flex-wrap:wrap;">
      <a class="glass-chip" style="display:inline-flex; align-items:center; height:42px; padding:0 18px; border-radius:var(--r-pill); color:#fff; font-size:13.5px; font-weight:550; text-decoration:none;">Glass button</a>
    </div>
  </div>
</section>
```

## 9. Responsive notes
- All sizes via `clamp()`; one design auto-adapts PC↔mobile.
- Breakpoint ~`680px`: two-column → one (`.ds-2col { grid-template-columns:1fr; }`), hide secondary info (`.hide-sm`).
- Section spacing `clamp(34px,6vw,56px)`; panels sized to content.
