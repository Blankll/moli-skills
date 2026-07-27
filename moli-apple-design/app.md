# App / iOS screens — the mobile shell layer

The core skill is desktop-web scale (720/1080 containers, hover lift). An **App screen** is different: it lives inside a device, is touch-first, and needs iOS chrome the web system doesn't ship. This file adds that shell. **Everything else stays the same**: tokens, unified-panel-not-cards, glass-only-on-overlap, grayscale + one accent, tabular-nums, materialize motion.

> Read this when the task is "an app / iOS screen / mobile mockup / app 原型." Use the core files (`design-system.md`, `components.md`) for the *content*; use this file for the *shell around it*.

## Iron rule — never hand-roll the device frame

```
screen (points)      393 × 852
device corner radius 55        bezel (padding) 12
Dynamic Island       125 × 37  ·  top 11  ·  centered  ·  radius 999
safe-area top (status bar)   59      safe-area bottom 34
home indicator       139 × 5   ·  centered  ·  bottom 8
nav bar compact      44        large-title expanded area ~96 (44 + 52)
tab bar              49 content + 34 safe = 83
```

## 1. Device frame (bezel + island + status bar + home indicator)

```html
<div class="ios">
  <div class="ios-screen">
    <div class="ios-island"></div>
    <div class="ios-status">
      <span class="t">9:41</span>
      <span class="i"><!-- signal / wifi / battery --></span>
    </div>
    <!-- app content: nav + scroll + tab bar -->
    <div class="ios-home"></div>
  </div>
</div>
```
```css
.ios{ position:relative; width:393px; height:852px; background:#000;
  border-radius:55px; padding:12px; box-shadow:0 50px 100px rgba(0,0,0,.5); }
.ios-screen{ position:relative; width:100%; height:100%; background:var(--bg);
  border-radius:44px; overflow:hidden; display:flex; flex-direction:column; }
.ios-island{ position:absolute; top:11px; left:50%; transform:translateX(-50%);
  width:125px; height:37px; background:#000; border-radius:999px; z-index:60; }
.ios-status{ flex:none; height:59px; display:flex; align-items:center; justify-content:space-between;
  padding:0 32px; font-size:15px; font-weight:600; color:var(--text); }
.ios-home{ position:absolute; bottom:8px; left:50%; transform:translateX(-50%);
  width:139px; height:5px; border-radius:999px; background:rgba(0,0,0,.85); z-index:80; }
```

## 2. Large-title nav (collapses on scroll)

```html
<header class="nav-c" id="navc"><span class="nav-c-t">钱包</span></header>
<div class="scroll" id="scroll">
  <h1 class="lt">钱包</h1>
  <!-- content -->
</div>
```
```css
.nav-c{ position:absolute; top:59px; left:0; right:0; height:44px; z-index:50;
  display:flex; align-items:center; justify-content:center;
  background:rgba(245,245,247,.72); backdrop-filter:saturate(180%) blur(20px);
  border-bottom:1px solid transparent; opacity:0; transition:opacity .25s, border-color .25s; pointer-events:none; }
.nav-c.show{ opacity:1; border-bottom-color:var(--hairline); }
.nav-c-t{ font-size:16px; font-weight:600; letter-spacing:-0.01em; }
.lt{ padding:6px 20px 10px; font-size:34px; font-weight:700; letter-spacing:-0.02em; }
```
```js
const sc=document.getElementById('scroll'), nc=document.getElementById('navc');
sc.addEventListener('scroll',()=>nc.classList.toggle('show', sc.scrollTop>44),{passive:true});
```

## 3. Tab bar (glass, safe-area, one accent)

```html
<nav class="tabbar">
  <a class="tab on">
    <svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="18" height="13" rx="2.5"/><path d="M3 10.5h18"/><circle cx="17" cy="14.5" r="1.25"/></svg>钱包</a>
  <a class="tab">
    <svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19"/></svg>卡片</a>
  <a class="tab">
    <svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M5 12h14"/></svg>添加</a>
  <a class="tab">
    <svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 20a8 8 0 0 1 16 0"/></svg>我的</a>
</nav>
```
```css
.tabbar{ flex:none; height:83px; padding:8px 0 34px; display:flex; justify-content:space-around; align-items:flex-start;
  background:rgba(245,245,247,.82); backdrop-filter:saturate(180%) blur(20px);
  border-top:1px solid var(--hairline); }
.tab{ display:flex; flex-direction:column; align-items:center; gap:3px; width:64px;
  font-size:10px; font-weight:500; color:var(--text-3); text-decoration:none; }
.tab.on{ color:var(--accent); }
```

## 4. Bottom sheet (edge-anchored)

```css
.sheet{ position:absolute; left:0; right:0; bottom:0; z-index:71; background:var(--surface);
  border-radius:22px 22px 0 0; padding:10px 20px max(24px, env(safe-area-inset-bottom));
  box-shadow:0 -8px 40px rgba(0,0,0,.16);
  transform:translateY(100%); transition:transform .4s var(--ease-spring); }
.sheet.open{ transform:translateY(0); }
.sheet .grab{ width:38px; height:5px; border-radius:999px; background:var(--faint); margin:0 auto 16px; }
.scrim{ position:absolute; inset:0; z-index:70; background:rgba(0,0,0,.28);
  opacity:0; pointer-events:none; transition:opacity .25s ease; }
.scrim.open{ opacity:1; pointer-events:auto; }
```

## 5. Mobile-first rules
- Container = the screen, not 720/1080. Content padding 16px.
- Touch ≥ 44px hit area for every control.
- No `:hover` as the only affordance — use `:active` for feedback.
- Safe areas via `env(safe-area-inset-top/bottom)`.

## 6. Restraint still rules
- One colored moment max (a gradient hero card).
- Don't color list values by status (income green/expense red).
- Transactions/settings → unified panel + hairlines, never per-row cards.

## App self-check
- [ ] Device frame from exact spec (island centered, home above overlays).
- [ ] Large title collapses to compact glass bar on scroll.
- [ ] Tab bar: glass, safe-area bottom, exactly one accent tab, real icons.
- [ ] Bottom sheet: edge-anchored, grab handle, top-rounded; reduced-motion handled.
- [ ] Touch targets ≥44px; feedback on `:active`; safe-area insets used.
- [ ] Still grayscale + one accent — list values not colored by status.