# Icons — Lucide-based Line Icon Set

## Philosophy

Apple-quality icons are **minimal, purposeful, and system-integrated**. They use Lucide's line-icon set with:

- **Single-color** (accent color when active, grayscale when inactive)
- **Consistent stroke weight** (1.75px for most, 1.5px for small)
- **Fixed dimensions** (26×26px for main, 24×24px for secondary)
- **No fill** (pure outline)
- **No shadows** (maintains visual hierarchy)

## Icon Library

All icons are from **Lucide** (https://lucide.dev) — a free and open-source icon set with 1000+ icons optimized for UI.

### Integration

```html
<!-- Import Lucide -->
<script src="https://unpkg.com/lucide@latest"></script>

<!-- Use icon -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12 5v14"/>
  <path d="M5 12h14"/>
</svg>
```

### Icon Sizing & Weight

| Size | Dimensions | Stroke Width | Use Case |
|------|------------|--------------|----------|
| **Main** | 26×26px | 1.75px | Primary actions, tab bar, buttons |
| **Secondary** | 24×24px | 1.5px | Small actions, status, indicators |
| **Mini** | 20×20px | 1.25px | Inline text, compact spaces |

### Icon States

```css
/* Default (inactive) */
.ic { color: var(--text-3); }

/* Active (selected) */
.tab.on .ic { color: var(--accent); }

/* Hover */
.tab:hover .ic { color: var(--text); }

/* Disabled */
.tab.disabled .ic { opacity: 0.4; pointer-events: none; }
```

## Icon Set Categories

### 1. Navigation & Layout

```html
<!-- Wallet (active) -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="18" height="13" rx="2.5"/><path d="M3 10.5h18"/><circle cx="17" cy="14.5" r="1.25"/></svg>

<!-- Cards -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19"/></svg>

<!-- Add -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M5 12h14"/></svg>

<!-- Profile -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 20a8 8 0 0 1 16 0"/></svg>
```

### 2. Actions & Operations

```html
<!-- Search -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>

<!-- Filter -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><polygon points="22,3 2,3 10,12.46 10,19 14,21 14,12.46 22,3"/></svg>

<!-- Sort -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="m3 6 4 6v4a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-4l4-6"/><path d="M12 12v8"/><path d="M9 6v12"/><path d="15 6v12"/></svg>

<!-- Share -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><path d="m16 6-4-4-4 4"/><path d="M12 2v13"/></svg>

<!-- Download -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/></svg>

<!-- Upload -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/></svg>
```

### 3. Status & Indicators

```html
<!-- Success -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="m9 11 3 3L22 4"/></svg>

<!-- Error -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/></svg>

<!-- Warning -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17v.01"/></svg>

<!-- Info -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>

<!-- Loading -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v4"/><path d="m6.75 6.75 2.25 2.25"/><path d="M18 12h4"/><path d="m6.75 17.25 2.25-2.25"/><path d="M12 20v-4"/><path d="m6.75 17.25-2.25-2.25"/><path d="M2 12h4"/><path d="m17.25 6.75-2.25 2.25"/></svg>

<!-- Offline -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><line x1="2" y1="12" x2="22" y2="12"/><path d="M8.71 10.71a2 2 0 0 1 2.83-2.83L12 12.17l2.46-2.46a2 2 0 0 1 2.83 2.83L12 17.17"/></svg>

<!-- Bluetooth -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="m17.71 5.06a10 10 0 1 0 0 14.88"/><path d="M8 12.01l4 4L22 8"/></svg>
```

### 4. Device & System

```html
<!-- Battery -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" rx="2"/><path d="M16 3v4"/><path d="M8 3v4"/><path d="M2 11h20"/></svg>

<!-- WiFi -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20v-6"/><path d="M8.71 17.29a4 4 0 0 1 5.58 0"/><path d="M5.17 11a8 8 0 0 1 9.66 0"/><path d="M1.14 9a12 12 0 0 1 21.72 0"/></svg>

<!-- Signal -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M2 20h20"/><path d="M5 20v-16"/><path d="M10 20v-8"/><path d="M15 20v-4"/><path d="M19 20v-2"/></svg>

<!-- Moon -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>

<!-- Sun -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>
```

### 5. Data & Finance

```html
<!-- Wallet -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="18" height="13" rx="2.5"/><path d="M3 10.5h18"/><circle cx="17" cy="14.5" r="1.25"/></svg>

<!-- Credit Card -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19"/></svg>

<!-- Money -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 3"/></svg>

<!-- Trending Up -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 9 12 1 20"/><polyline points="17 6 23 6 23 12"/></svg>

<!-- Trending Down -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 18 13.5 8.5 9 12 1 4"/><polyline points="17 18 23 18 23 12"/></svg>

<!-- Pie Chart -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21.21 15a2 2 0 0 1-1.81 1.35H5.72a2 2 0 0 1-1.81-1.35"/><path d="M12 2a10 10 0 1 0 10 10"/><path d="M12 2a10 10 0 0 1 10 10"/><path d="M12 12a4 4 0 0 1-4-4"/></svg>
```

### 6. Communication & Social

```html
<!-- Message -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>

<!-- Mail -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>

<!-- Phone -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 12 12 0 0 1-8.62-8.62A2 2 0 0 1 8.31 9.4l1.51 1.51a2 2 0 0 1 2.85 0L15.5 9.36a2 2 0 0 1 2.64-.94 12 12 0 0 1 6.16 6.16 2 2 0 0 1-.94 2.64l-2.46 2.46a2 2 0 0 1-2.85 0L13.5 13.5"/><path d="M14.5 8A5.5 5.5 0 0 0 9 13.5"/></svg>

<!-- Camera -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 4h-5L7 9v11h10V9z"/><path d="M14.5 4a2 2 0 0 1 2 2h0a2 2 0 0 1 2-2"/><path d="M9.5 4a2 2 0 0 1-2 2h0a2 2 0 0 1-2-2"/></svg>

<!-- Camera Off -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><line x1="2" y1="2" x2="22" y2="22"/><path d="M17 17H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h9.76a2 2 0 0 1 1.59.91l3.64 3.64a2 2 0 0 1 .45 1.45"/></svg>

<!-- Video -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="m10 9 5 3-5 3V9z"/></svg>

<!-- Video Off -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><line x1="1" y1="1" x2="23" y2="23"/><rect x="2" y="7" width="20" height="14" rx="2"/></svg>
```

### 7. Files & Storage

```html
<!-- File -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M13 2v7h7"/></svg>

<!-- File Plus -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M12 12v6"/><path d="M9 15h6"/></svg>

<!-- File Minus -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M9 15h6"/></svg>

<!-- Folder -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>

<!-- Folder Plus -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/><path d="M12 11v6"/><path d="M9 14h6"/></svg>

<!-- Folder Minus -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/><path d="M9 14h6"/></svg>

<!-- Archive -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/><path d="M12 12v6"/></svg>

<!-- Trash -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>

<!-- Trash 2 -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M10 11v6"/><path d="M14 11v6"/></svg>

<!-- Copy -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"/><rect x="2" y="9" width="13" height="13" rx="2"/></svg>

<!-- Copy Plus -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"/><rect x="2" y="9" width="13" height="13" rx="2"/><path d="M12 18v-6"/><path d="M9 15h6"/></svg>

<!-- Copy Minus -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"/><rect x="2" y="9" width="13" height="13" rx="2"/><path d="M9 15h6"/></svg>
```

### 8. Time & Calendar

```html
<!-- Clock -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>

<!-- Calendar -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/></svg>

<!-- Calendar Plus -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/><path d="M12 16v-6"/><path d="M9 13h6"/></svg>

<!-- Calendar Minus -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/><path d="M9 13h6"/></svg>

<!-- Timer -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>

<!-- Alarm -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M2 6h20"/><path d="M12 10v4"/><path d="M12 14h.01"/></svg>
```

### 9. Settings & Tools

```html
<!-- Settings -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 1v6m0 6v6m4.22-13.22L19.78 5.98M4.22 18.22L5.98 19.78M1 12h6m6 0h6M5.98 5.98 4.22 18.22"/></svg>

<!-- Settings 2 -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M20 7h-9"/><path d="M14 17H5"/><circle cx="17" cy="17" r="3"/><circle cx="7" cy="7" r="3"/></svg>

<!-- Wrench -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 0-7.94 7.94l-3.02 3.02a6 6 0 0 0 7.94 7.94l3.02-3.02a6 6 0 0 0 0-8.47z"/></svg>

<!-- Tool -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 0-7.94 7.94l-3.02 3.02a6 6 0 0 0 7.94 7.94l3.02-3.02a6 6 0 0 0 0-8.47z"/><path d="M2 12h8"/><path d="M9 4v8"/></svg>

<!-- Layers -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z"/></svg>

<!-- Package -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z"/><path d="M9 12l2 2 4-4"/></svg>

<!-- Box -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M3.27 6.96a2 2 0 0 0 1.03 2.56l7.29 4.22a2 2 0 0 0 2.14 0l7.29-4.22a2 2 0 0 0 1.03-2.56M12 2v20"/></svg>
```

### 10. Shapes & Elements

```html
<!-- Square -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/></svg>

<!-- Circle -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/></svg>

<!-- Triangle -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z"/></svg>

<!-- Diamond -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z"/></svg>

<!-- Star -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26"/></svg>

<!-- Heart -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>

<!-- Heart Off -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><line x1="2" y1="2" x2="22" y2="22"/><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>

<!-- Hexagon -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z"/></svg>

<!-- Octagon -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z"/></svg>
```

### 11. Arrows & Direction

```html
<!-- Arrow Up -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5"/><path d="M5 12l7-7 7 7"/></svg>

<!-- Arrow Down -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M19 12l-7 7-7-7"/></svg>

<!-- Arrow Left -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M11 19L2 12l9-7v5h8v6h-8z"/></svg>

<!-- Arrow Right -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h20"/><path d="M13 5l7 7-7 7"/></svg>

<!-- Arrow Up Right -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7"/><path d="M7 7h10v10"/></svg>

<!-- Arrow Down Left -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M17 7L7 17"/><path d="M7 7h10v10"/></svg>

<!-- Arrow Up Left -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M17 17L7 7"/><path d="M7 17h10V7"/></svg>

<!-- Arrow Down Right -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7l10 10"/><path d="M7 7v10h10"/></svg>
```

### 12. Text & Typography

```html
<!-- Type -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7V4m16 0V4M4 20V7m16 13V20M4 14h16M4 20h16M4 10h16"/></svg>

<!-- Text -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7V4m16 0V4M4 20V7m16 13V20M4 14h16M4 20h16M4 10h16"/></svg>

<!-- Align Left -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16"/><path d="M4 12h10"/><path d="M4 18h16"/></svg>

<!-- Align Center -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16"/><path d="M8 12h8"/><path d="M4 18h16"/></svg>

<!-- Align Right -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16"/><path d="M12 12h10"/><path d="M4 18h16"/></svg>

<!-- Bold -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4h8a4 4 0 0 1 4 4 4 4 0 0 1-4 4H6z"/><path d="M6 20h8a4 4 0 0 1 4-4 4-4 0 0 1-4-4H6z"/></svg>

<!-- Italic -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M10 4v11m4-7v7"/></svg>

<!-- Underline -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h16"/><path d="M4 4v16"/></svg>

<!-- Strikethrough -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h16"/><path d="M16 4L8 20"/></svg>
```

### 13. Media & Entertainment

```html
<!-- Play -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M8 5v14l11-7z"/></svg>

<!-- Pause -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4h4v16H6z"/><path d="M14 4h4v16h-4z"/></svg>

<!-- Stop -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="6" width="12" height="12" rx="2"/></svg>

<!-- Skip Back -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M19 20L9 12l10-8z"/><path d="M5 19v-14"/></svg>

<!-- Skip Forward -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4l10 8-10 8z"/><path d="M19 5v14"/></svg>

<!-- Volume -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5l0 14"/><path d="M15 5l0 14"/><path d="M2 9l4 6 4-6 4 6 4-6"/></svg>

<!-- Volume Off -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><line x1="2" y1="2" x2="22" y2="22"/><path d="M11 5l0 14"/><path d="M15 5l0 14"/><path d="M2 9l4 6 4-6 4 6 4-6"/></svg>

<!-- Mic -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><path d="M12 22v-4"/></svg>

<!-- Mic Off -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><line x1="2" y1="2" x2="22" y2="22"/><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><path d="M12 22v-4"/></svg>

<!-- Camera -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 4h-5L7 9v11h10V9z"/><path d="M14.5 4a2 2 0 0 1 2 2h0a2 2 0 0 1 2-2"/><path d="M9.5 4a2 2 0 0 1-2 2h0a2 2 0 0 1-2-2"/></svg>

<!-- Image -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>

<!-- Image Off -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><line x1="2" y1="2" x2="22" y2="22"/><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
```

### 14. Maps & Location

```html
<!-- Map -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>

<!-- Map Pin -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/><path d="M12 7v7l3 3"/></svg>

<!-- Navigation -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z"/><path d="M12 22V12"/><path d="M5 12h14"/></svg>

<!-- Compass -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2v4"/><path d="M12 18v4"/><path d="m4.93 4.93 2.83 2.83"/><path d="m16.24 16.24 2.83 2.83"/><path d="M2 12h4"/><path d="M18 12h4"/><path d="m4.93 19.07 2.83-2.83"/><path d="m16.24 7.76 2.83-2.83"/></svg>

<!-- Route -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"/><path d="M3 12h18"/><path d="M3 18h18"/><path d="M8 6v12"/><path d="M12 6v12"/><path d="M16 6v12"/></svg>

<!-- Traffic -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M3 12h18"/><path d="M3 6h18"/><path d="M8 6v12"/><path d="M12 6v12"/><path d="M16 6v12"/></svg>
```

### 15. Security & Safety

```html
<!-- Shield -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>

<!-- Shield Off -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><line x1="2" y1="2" x2="22" y2="22"/><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>

<!-- Lock -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>

<!-- Lock Open -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/><path d="M9 11h6"/></svg>

<!-- Unlock -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/><path d="M9 16h6"/></svg>

<!-- Fingerprint -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"/><path d="M12 18v2"/><path d="M8 22v-2"/><path d="M16 22v-2"/><path d="M12 20a4 4 0 0 1-4-4"/><path d="M12 20a4 4 0 0 1 4-4"/><path d="M12 14a2 2 0 0 1-2-2"/><path d="M12 14a2 2 0 0 1 2-2"/></svg>

<!-- Scan -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7v4a1 1 0 0 0 1 1h4"/><path d="M17 7v4a1 1 0 0 1-1 1h-4"/><path d="M3 17v4a1 1 0 0 0 1 1h4"/><path d="M17 17v4a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-4a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1z"/></svg>

<!-- Eye -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a10 10 0 1 0 10 10"/><path d="M12 2a10 10 0 0 1 10 10"/><path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"/></svg>

<!-- Eye Off -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><line x1="2" y1="2" x2="22" y2="22"/><path d="M12 2a10 10 0 1 0 10 10"/><path d="M12 2a10 10 0 0 1 10 10"/><path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"/></svg>
```

### 16. Development & Tools

```html
<!-- Code -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M16 18l6-6-6-6"/><path d="M8 6l-6 6 6 6"/></svg>

<!-- Code 2 -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M18 1l-6 5 6 5z"/><path d="M6 1l-6 5 6 5z"/><path d="M12 1v10"/><path d="M12 11v10"/></svg>

<!-- Terminal -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><polyline points="4,7 4,4 20,4 20,7"/><polyline points="9,12 7,10 12,5 17,10 15,12 20,12"/><rect x="3" y="16" width="18" height="5" rx="2"/></svg>

<!-- Git Branch -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="3" x2="6" y2="15"/><circle cx="6" cy="3" r="3"/><path d="M9 12l-3-3 3-3"/><path d="M9 12l3 3 3-3"/><path d="M9 6h12"/></svg>

<!-- Git Commit -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 1v6m0 6v6m4.22-13.22L19.78 5.98M4.22 18.22L5.98 19.78M1 12h6m6 0h6M5.98 5.98 4.22 18.22"/></svg>

<!-- Git Merge -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="3"/><circle cx="18" cy="6" r="3"/><path d="M6 9v12"/><path d="M18 9v12"/><line x1="6" y1="15" x2="18" y2="15"/></svg>

<!-- Git Pull -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 1v6m0 6v6m4.22-13.22L19.78 5.98M4.22 18.22L5.98 19.78M1 12h6m6 0h6M5.98 5.98 4.22 18.22"/></svg>

<!-- Git Push -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 1v6m0 6v6m4.22-13.22L19.78 5.98M4.22 18.22L5.98 19.78M1 12h6m6 0h6M5.98 5.98 4.22 18.22"/></svg>

<!-- Package -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z"/><path d="M9 12l2 2 4-4"/></svg>

<!-- Layers -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z"/></svg>

<!-- Box -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M3.27 6.96a2 2 0 0 0 1.03 2.56l7.29 4.22a2 2 0 0 0 2.14 0l7.29-4.22a2 2 0 0 0 1.03-2.56M12 2v20"/></svg>
```

### 17. File System & Organization

```html
<!-- Hard Drive -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M2 7h20"/><path d="M6 11h12"/></svg>

<!-- Memory -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M2 7v10a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2z"/><path d="M2 11h20"/><path d="M6 11h12"/></svg>

<!-- Database -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="4"/><ellipse cx="12" cy="19" rx="9" ry="4"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>

<!-- Cloud -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h4"/><path d="M12 12v6"/><path d="M9 13l2 2 4-4"/></svg>

<!-- Cloud Off -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><line x1="2" y1="2" x2="22" y2="22"/><path d="M18 10h-1.26A8 8 0 1 0 9 20h4"/><path d="M12 12v6"/><path d="M9 13l2 2 4-4"/></svg>

<!-- Upload -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/></svg>

<!-- Download -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/></svg>

<!-- External Link -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><path d="M15 3h6v6"/><path d="M10 14L21 3"/></svg>

<!-- Link -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.72"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.72-1.72"/></svg>

<!-- Link 2 -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M15 7h3a5 5 0 1 1 0 10h-3"/><path d="M8 7V4a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1V7z"/></svg>
```

### 18. Actions & Operations

```html
<!-- Plus -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M5 12h14"/></svg>

<!-- Plus Circle -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 5v14"/><path d="M5 12h14"/></svg>

<!-- Plus Square -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 5v14"/><path d="M5 12h14"/></svg>

<!-- Minus -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/></svg>

<!-- Minus Circle -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M5 12h14"/></svg>

<!-- Minus Square -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M5 12h14"/></svg>

<!-- X -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6L6 18"/><path d="M6 6l12 12"/></svg>

<!-- X Circle -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M18 6L6 18"/><path d="M6 6l12 12"/></svg>

<!-- X Square -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M18 6L6 18"/><path d="M6 6l12 12"/></svg>

<!-- Check -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>

<!-- Check Circle -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M20 6L9 17l-5-5"/></svg>

<!-- Check Square -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M20 6L9 17l-5-5"/></svg>

<!-- Help -->
<svg class="ic" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a6 .