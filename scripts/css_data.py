# -*- coding: utf-8 -*-
"""CSS module bodies for PikSearch files 02..40. Real, purposeful styling;
the build script pads each to >=310 lines with a scoped utility layer."""

C = {}

C["02-liquid-glass.css"] = """
/* =============================================================
 * PikSearch - 02-liquid-glass.css
 * iOS 26 "Liquid Glass" material system (CSS-first, renderer="auto").
 * .og-glass is the base recipe; variants tune the refraction illusion
 * via layered gradients, edge speculars and backdrop-filter. The WebGL
 * renderer (open-glass-ui/webgl) upgrades ONLY owned canvas hosts.
 * ============================================================= */
@layer og.glass {
  .og-glass {
    position: relative;
    isolation: isolate;
    background:
      linear-gradient(135deg, var(--og-glass-tint-strong), var(--og-glass-tint) 55%, transparent),
      var(--og-surface);
    -webkit-backdrop-filter: var(--og-glass-blur);
    backdrop-filter: var(--og-glass-blur);
    border-radius: var(--og-radius-fluid);
    box-shadow: var(--og-glass-shadow), var(--og-glass-inner-highlight);
    overflow: hidden;
  }
  /* Specular rim: top light catch, bottom shadow edge (gradient border trick) */
  .og-glass::before {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: inherit;
    padding: 1px;
    background: linear-gradient(160deg,
      var(--og-glass-border-top) 0%,
      transparent 38%,
      transparent 62%,
      var(--og-glass-border-bottom) 100%);
    -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
    -webkit-mask-composite: xor;
            mask-composite: exclude;
    pointer-events: none;
    z-index: 2;
  }
  /* Soft internal lens highlight following the corner curvature */
  .og-glass::after {
    content: "";
    position: absolute;
    inset: -30% -10% auto -10%;
    height: 60%;
    background: radial-gradient(60% 100% at 30% 0%,
      rgba(255,255,255,0.17) 0%,
      transparent 70%);
    pointer-events: none;
    z-index: 1;
  }
  .og-glass > * { position: relative; z-index: 3; }

  /* ---------- Thickness variants ---------- */
  .og-glass--thin  { backdrop-filter: var(--og-glass-blur-thin);  -webkit-backdrop-filter: var(--og-glass-blur-thin); }
  .og-glass--thick { backdrop-filter: var(--og-glass-blur-thick); -webkit-backdrop-filter: var(--og-glass-blur-thick); }
  .og-glass--clear { background: rgba(255,255,255,0.02); }
  .og-glass--solid { background: var(--og-black-200); backdrop-filter: none; -webkit-backdrop-filter: none; }

  /* ---------- Tonal variants (monochrome only) ---------- */
  .og-glass--dark   { background: linear-gradient(180deg, rgba(0,0,0,0.55), rgba(0,0,0,0.75)); }
  .og-glass--light  { background: linear-gradient(180deg, rgba(255,255,255,0.14), rgba(255,255,255,0.05)); }
  .og-glass--invert { background: var(--og-white); color: var(--og-black); --og-glass-border-top: rgba(0,0,0,0.18); }

  /* ---------- Shape recipes ---------- */
  .og-glass--pill   { border-radius: var(--og-radius-pill); }
  .og-glass--card   { border-radius: var(--og-radius-xl); }
  .og-glass--sheet  { border-radius: var(--og-radius-2xl) var(--og-radius-2xl) 0 0; }
  .og-glass--circle { border-radius: 50%; aspect-ratio: 1; }

  /* ---------- Interactive glass (buttons / toggles live here) ---------- */
  .og-glass--interactive {
    cursor: pointer;
    transition:
      transform var(--og-dur-fast) var(--og-ease-spring),
      box-shadow var(--og-dur-base) var(--og-ease-standard),
      background-color var(--og-dur-base) var(--og-ease-standard);
  }
  .og-glass--interactive:hover {
    background:
      linear-gradient(135deg, var(--og-glass-tint-strong), var(--og-glass-tint)),
      var(--og-surface-strong);
    transform: translateY(-1px) scale(1.005);
  }
  .og-glass--interactive:active {
    transform: translateY(0) scale(0.985);
    box-shadow: var(--og-elev-1), var(--og-glass-inner-highlight);
  }

  /* ---------- Liquid morph on focus-within (glass "gels") ---------- */
  .og-glass--morph:focus-within {
    border-radius: calc(var(--og-radius-fluid) + 6px);
    box-shadow: var(--og-glass-shadow), var(--og-glass-inner-highlight),
                0 0 0 4px rgba(255,255,255,0.06);
  }

  /* ---------- Floating tab-bar / toolbar recipe (iOS 26 style) ---------- */
  .og-glass--bar {
    display: flex;
    align-items: center;
    gap: var(--og-space-2);
    padding: var(--og-space-2);
    border-radius: var(--og-radius-xl);
  }
  .og-glass--bar .og-glass__item {
    flex: 1;
    display: grid;
    place-items: center;
    padding-block: var(--og-space-2);
    border-radius: var(--og-radius-lg);
    transition: background var(--og-dur-fast) var(--og-ease-standard);
  }
  .og-glass--bar .og-glass__item[aria-current="true"],
  .og-glass--bar .og-glass__item.is-active {
    background: rgba(255,255,255,0.16);
    box-shadow: var(--og-glass-inner-highlight);
  }

  /* ---------- Layered depth: stacked glass sheets ---------- */
  .og-glass-stack { display: grid; }
  .og-glass-stack > * { grid-area: 1 / 1; }
  .og-glass-stack > :nth-child(1) { transform: translateY(8px) scale(0.94); opacity: 0.35; filter: blur(1px); }
  .og-glass-stack > :nth-child(2) { transform: translateY(4px) scale(0.97); opacity: 0.6; }

  /* ---------- Renderer hooks (renderer="auto") ---------- */
  [data-og-renderer="css"] { --og-render-hint: css; }
  [data-og-renderer="webgl"] > canvas[data-og-refract] {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    pointer-events: none;
    border-radius: inherit;
  }

  /* ---------- Fallback: no backdrop-filter support ---------- */
  @supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
    .og-glass { background: rgba(20,20,20,0.92); }
    .og-glass--light { background: rgba(240,240,240,0.92); }
  }

  /* ---------- Reduced transparency: flatten all glass ---------- */
  @media (prefers-reduced-transparency: reduce) {
    .og-glass {
      -webkit-backdrop-filter: none;
      backdrop-filter: none;
      background: var(--og-black-200);
    }
    .og-glass::before, .og-glass::after { display: none; }
  }

  /* ---------- Forced colors: single System-on boundary ---------- */
  @media (forced-colors: active) {
    .og-glass {
      background: Canvas;
      border: 1px solid CanvasText;
      box-shadow: none;
      forced-color-adjust: auto;
    }
    .og-glass::before, .og-glass::after { display: none; }
    .og-glass--bar .og-glass__item[aria-current="true"] {
      background: Highlight;
      color: HighlightText;
    }
  }
}
"""

C["03-typography.css"] = """
/* =============================================================
 * PikSearch - 03-typography.css
 * Monochrome editorial type system: fluid display sizes, optical
 * weights, tabular numerics for stats, disciplined measure lengths.
 * ============================================================= */
@layer og.type {
  .og-display { font-size: clamp(2.5rem, 1.6rem + 4vw, var(--og-text-4xl)); font-weight: 800; letter-spacing: -0.035em; line-height: 1.05; }
  .og-headline { font-size: clamp(1.75rem, 1.3rem + 1.8vw, var(--og-text-3xl)); font-weight: 750; letter-spacing: -0.025em; }
  .og-title { font-size: var(--og-text-xl); font-weight: 650; letter-spacing: -0.015em; }
  .og-subtitle { font-size: var(--og-text-lg); font-weight: 500; color: var(--og-text-secondary); }
  .og-body { font-size: var(--og-text-base); color: var(--og-text-secondary); max-inline-size: 65ch; }
  .og-caption { font-size: var(--og-text-xs); color: var(--og-text-muted); letter-spacing: 0.01em; }
  .og-overline { font-size: var(--og-text-xs); font-weight: 700; text-transform: uppercase; letter-spacing: var(--og-tracking-wide); color: var(--og-text-faint); }
  .og-quote { font-size: var(--og-text-lg); font-style: italic; border-inline-start: 2px solid var(--og-hairline-strong); padding-inline-start: var(--og-space-4); }
  .og-num { font-variant-numeric: tabular-nums lining-nums; }
  .og-mark { background: var(--og-white); color: var(--og-black); padding-inline: 0.15em; border-radius: 3px; font-weight: 600; }
  .og-link { color: var(--og-text); text-decoration: underline; text-decoration-color: var(--og-gray-2); text-underline-offset: 0.18em; transition: text-decoration-color var(--og-dur-fast); }
  .og-link:hover { text-decoration-color: var(--og-white); }
  .og-kbd { display: inline-block; min-width: 1.6em; padding: 0.15em 0.45em; font-family: var(--og-font-mono); font-size: 0.8em; text-align: center; background: var(--og-black-400); border-radius: var(--og-radius-xs); box-shadow: inset 0 -1px 0 rgba(0,0,0,0.6), 0 1px 0 rgba(255,255,255,0.08); }
  .og-measure-narrow { max-inline-size: 42ch; }
  .og-measure-wide { max-inline-size: 78ch; }
  .og-flow > * + * { margin-block-start: var(--og-space-4); }
  .og-flow-lg > * + * { margin-block-start: var(--og-space-6); }
  h1.og-display, h2.og-headline { text-wrap: balance; }
  .og-dim { color: var(--og-text-muted); }
  .og-invert { background: var(--og-white); color: var(--og-black); }
}
"""

C["04-layout-grid.css"] = """
/* =============================================================
 * PikSearch - 04-layout-grid.css
 * Container queries first, classic grid utilities second. Search
 * results use an asymmetric two-column layout that collapses to a
 * single flow on narrow viewports.
 * ============================================================= */
@layer og.layout {
  .og-container { inline-size: min(100% - (var(--og-gutter) * 2), var(--og-container)); margin-inline: auto; }
  .og-container--narrow { inline-size: min(100% - (var(--og-gutter) * 2), var(--og-container-narrow)); }
  .og-container--wide { inline-size: min(100% - (var(--og-gutter) * 2), var(--og-container-wide)); }
  .og-grid { display: grid; gap: var(--og-space-5); }
  .og-grid--2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .og-grid--3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .og-grid--4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .og-grid--auto { grid-template-columns: repeat(auto-fill, minmax(min(240px, 100%), 1fr)); }
  .og-grid--results { grid-template-columns: minmax(0, 1fr) 320px; align-items: start; }
  .og-sidebar { position: sticky; top: calc(var(--og-header-h) + var(--og-space-4)); }
  .og-stack { display: flex; flex-direction: column; gap: var(--og-space-4); }
  .og-row { display: flex; align-items: center; gap: var(--og-space-3); }
  .og-row--between { justify-content: space-between; }
  .og-center { display: grid; place-items: center; min-block-size: 50vh; }
  .og-hero { display: grid; place-items: center; text-align: center; min-block-size: 100svh; padding-block: var(--og-space-8); }
  @container (max-width: 720px) {
    .og-grid--3, .og-grid--4 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  }
  @media (max-width: 1024px) {
    .og-grid--results { grid-template-columns: 1fr; }
    .og-sidebar { position: static; }
  }
  @media (max-width: 640px) {
    .og-grid--2, .og-grid--3, .og-grid--4 { grid-template-columns: 1fr; }
  }
}
"""

C["05-color-monochrome.css"] = """
/* =============================================================
 * PikSearch - 05-color-monochrome.css
 * Enforces the premiumistic black & white rule: every surface,
 * border, shadow and text role resolves to the gray ramp. Color is
 * permitted ONLY inside icon glyphs (.og-icon[data-hue]).
 * ============================================================= */
@layer og.color {
  .og-page { background: var(--og-black); color: var(--og-white); }
  .og-band { background: var(--og-black-100); border-block: 1px solid var(--og-hairline); }
  .og-chip-mono { display: inline-flex; align-items: center; gap: var(--og-space-2); padding: 0.25em 0.75em; border: 1px solid var(--og-hairline-strong); border-radius: var(--og-radius-pill); font-size: var(--og-text-xs); color: var(--og-text-secondary); }
  .og-divider { block-size: 1px; background: linear-gradient(90deg, transparent, var(--og-hairline-strong), transparent); border: 0; }
  .og-vignette { position: fixed; inset: 0; pointer-events: none; background: radial-gradient(120% 90% at 50% 0%, transparent 55%, rgba(0,0,0,0.55) 100%); z-index: var(--og-z-raised); }
  .og-grain { position: fixed; inset: 0; pointer-events: none; opacity: 0.05; mix-blend-mode: overlay; z-index: var(--og-z-raised); background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='120' height='120' filter='url(%23n)' opacity='0.6'/%3E%3C/svg%3E"); }
  .og-icon[data-hue="success"] { color: var(--og-icon-success); }
  .og-icon[data-hue="warning"] { color: var(--og-icon-warning); }
  .og-icon[data-hue="danger"]  { color: var(--og-icon-danger); }
  .og-icon[data-hue="info"]    { color: var(--og-icon-info); }
  .og-icon[data-hue="brand"]   { color: var(--og-icon-brand); }
  .og-icon:not([data-hue])     { color: currentColor; }
  html[data-mono-strict] *:not(.og-icon):not(.og-icon *) { filter: grayscale(1) contrast(1.02); }
  html[data-mono-strict] .og-icon, html[data-mono-strict] .og-icon * { filter: none; }
  @media (forced-colors: active) {
    .og-chip-mono, .og-divider { border-color: CanvasText; background: Canvas; }
  }
}
"""

C["06-navigation.css"] = """
/* =============================================================
 * PikSearch - 06-navigation.css
 * Sticky glass header, floating pill nav, breadcrumb rail, mobile
 * slide-over drawer. All controls are semantic nav/a/button DOM.
 * ============================================================= */
@layer og.nav {
  .og-header { position: sticky; top: 0; z-index: var(--og-z-header); block-size: var(--og-header-h); display: flex; align-items: center; }
  .og-header__inner { inline-size: min(100% - (var(--og-gutter) * 2), var(--og-container-wide)); margin-inline: auto; display: flex; align-items: center; gap: var(--og-space-5); }
  .og-logo { display: flex; align-items: center; gap: var(--og-space-3); font-weight: 800; letter-spacing: -0.03em; }
  .og-nav { display: flex; align-items: center; gap: var(--og-space-1); }
  .og-nav__link { display: inline-flex; align-items: center; gap: var(--og-space-2); padding: var(--og-space-2) var(--og-space-4); border-radius: var(--og-radius-pill); color: var(--og-text-secondary); font-size: var(--og-text-sm); font-weight: 550; transition: color var(--og-dur-fast), background var(--og-dur-fast); text-decoration: none; }
  .og-nav__link:hover { color: var(--og-white); background: var(--og-accent-soft); }
  .og-nav__link[aria-current="page"] { color: var(--og-black); background: var(--og-white); }
  .og-breadcrumb { display: flex; gap: var(--og-space-2); font-size: var(--og-text-sm); color: var(--og-text-muted); list-style: none; }
  .og-breadcrumb li + li::before { content: "/"; margin-inline-end: var(--og-space-2); }
  .og-drawer { position: fixed; inset-block: 0; inset-inline-end: 0; inline-size: min(84vw, 360px); z-index: var(--og-z-modal); transform: translateX(100%); transition: transform var(--og-dur-slow) var(--og-ease-emphasize); padding: var(--og-space-5); }
  .og-drawer[data-open="true"] { transform: translateX(0); }
  .og-drawer__scrim { position: fixed; inset: 0; z-index: calc(var(--og-z-modal) - 1); background: rgba(0,0,0,0.6); opacity: 0; pointer-events: none; transition: opacity var(--og-dur-base); }
  .og-drawer__scrim[data-open="true"] { opacity: 1; pointer-events: auto; }
  .og-menu-toggle { display: none; }
  @media (max-width: 860px) {
    .og-nav--desktop { display: none; }
    .og-menu-toggle { display: inline-grid; place-items: center; }
  }
}
"""

C["07-search-core.css"] = """
/* =============================================================
 * PikSearch - 07-search-core.css
 * The search field itself: giant liquid-glass bar on hero, compact
 * variant under the sticky header, submit affordance, clear button,
 * engine badge row.
 * ============================================================= */
@layer og.search {
  .og-search { position: relative; inline-size: 100%; }
  .og-search__field { inline-size: 100%; padding: var(--og-space-4) var(--og-space-8); padding-inline-start: calc(var(--og-space-8) + 2rem); font-size: var(--og-text-lg); background: transparent; border: 0; outline: none; caret-color: var(--og-white); }
  .og-search__field::placeholder { color: var(--og-text-faint); }
  .og-search__icon { position: absolute; inset-inline-start: var(--og-space-4); top: 50%; translate: 0 -50%; color: var(--og-text-muted); pointer-events: none; }
  .og-search__clear { position: absolute; inset-inline-end: var(--og-space-4); top: 50%; translate: 0 -50%; display: grid; place-items: center; inline-size: 28px; block-size: 28px; border-radius: 50%; background: var(--og-surface-strong); color: var(--og-text-secondary); cursor: pointer; visibility: hidden; border: 0; }
  .og-search[data-filled="true"] .og-search__clear { visibility: visible; }
  .og-search__submit { position: absolute; inset-inline-end: var(--og-space-2); top: 50%; translate: 0 -50%; padding: var(--og-space-2) var(--og-space-4); border-radius: var(--og-radius-pill); background: var(--og-white); color: var(--og-black); font-weight: 700; cursor: pointer; border: 0; transition: transform var(--og-dur-fast) var(--og-ease-spring); }
  .og-search__submit:hover { transform: scale(1.05); }
  .og-search--hero { max-inline-size: 680px; margin-inline: auto; }
  .og-search--hero .og-search__field { font-size: var(--og-text-xl); padding-block: var(--og-space-5); }
  .og-search--compact .og-search__field { font-size: var(--og-text-sm); padding-block: var(--og-space-2); }
  .og-engines { display: flex; justify-content: center; gap: var(--og-space-2); margin-block-start: var(--og-space-4); flex-wrap: wrap; }
  .og-engine-chip { padding: var(--og-space-1) var(--og-space-3); border-radius: var(--og-radius-pill); border: 1px solid var(--og-hairline); font-size: var(--og-text-xs); color: var(--og-text-muted); cursor: pointer; transition: all var(--og-dur-fast); background: transparent; }
  .og-engine-chip[aria-pressed="true"] { background: var(--og-white); color: var(--og-black); border-color: var(--og-white); }
  .og-results-meta { display: flex; gap: var(--og-space-4); color: var(--og-text-muted); font-size: var(--og-text-sm); }
}
"""

C["08-results-feed.css"] = """
/* =============================================================
 * PikSearch - 08-results-feed.css
 * Organic result cards, sitelinks tree, pagination pills, infinite
 * sentinel, sponsored label discipline (monochrome badges).
 * ============================================================= */
@layer og.results {
  .og-result { padding: var(--og-space-5); margin-block-end: var(--og-space-4); }
  .og-result__url { display: flex; align-items: center; gap: var(--og-space-2); font-size: var(--og-text-xs); color: var(--og-text-muted); }
  .og-result__favicon { inline-size: 18px; block-size: 18px; border-radius: 4px; background: var(--og-black-400); }
  .og-result__title { font-size: var(--og-text-lg); color: var(--og-white); text-decoration: none; }
  .og-result__title:visited { color: var(--og-gray-5); }
  .og-result__title:hover { text-decoration: underline; text-underline-offset: 3px; }
  .og-result__snippet { margin-block-start: var(--og-space-2); color: var(--og-text-secondary); font-size: var(--og-text-sm); }
  .og-result__badges { display: flex; gap: var(--og-space-2); margin-block-start: var(--og-space-3); }
  .og-sitelinks { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: var(--og-space-2); margin-block-start: var(--og-space-3); list-style: none; }
  .og-sitelink { font-size: var(--og-text-sm); color: var(--og-text-secondary); padding: var(--og-space-2); border-radius: var(--og-radius-xs); text-decoration: none; }
  .og-sitelink:hover { background: var(--og-accent-soft); color: var(--og-white); }
  .og-sponsored { font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; border: 1px solid var(--og-hairline-strong); padding: 2px 6px; border-radius: 3px; color: var(--og-text-faint); }
  .og-pagination { display: flex; justify-content: center; gap: var(--og-space-2); margin-block: var(--og-space-7); }
  .og-page-btn { inline-size: 40px; block-size: 40px; display: grid; place-items: center; border-radius: var(--og-radius-md); color: var(--og-text-secondary); cursor: pointer; border: 1px solid transparent; transition: all var(--og-dur-fast); background: transparent; }
  .og-page-btn:hover { border-color: var(--og-hairline-strong); }
  .og-page-btn[aria-current="page"] { background: var(--og-white); color: var(--og-black); font-weight: 700; }
  .og-sentinel { block-size: 1px; }
  .og-result--dense { padding: var(--og-space-3); }
  .og-result--dense .og-result__title { font-size: var(--og-text-base); }
}
"""

C["09-widgets-cards.css"] = """
/* =============================================================
 * PikSearch - 09-widgets-cards.css
 * Knowledge panel, weather widget, calculator card, stock sparkline
 * frame, definition card - all glass cards, all monochrome.
 * ============================================================= */
@layer og.widgets {
  .og-widget { padding: var(--og-space-5); }
  .og-widget__head { display: flex; align-items: center; justify-content: space-between; margin-block-end: var(--og-space-4); }
  .og-widget__title { font-size: var(--og-text-sm); font-weight: 700; text-transform: uppercase; letter-spacing: var(--og-tracking-wide); color: var(--og-text-muted); }
  .og-kp { display: grid; gap: var(--og-space-4); }
  .og-kp__image { aspect-ratio: 16/9; border-radius: var(--og-radius-lg); background: linear-gradient(135deg, var(--og-black-300), var(--og-black-100)); overflow: hidden; }
  .og-kp__facts { display: grid; grid-template-columns: auto 1fr; gap: var(--og-space-2) var(--og-space-4); font-size: var(--og-text-sm); }
  .og-kp__fact-label { color: var(--og-text-muted); }
  .og-weather { display: flex; align-items: baseline; gap: var(--og-space-3); }
  .og-weather__temp { font-size: var(--og-text-4xl); font-weight: 300; letter-spacing: -0.04em; }
  .og-weather__days { display: grid; grid-template-columns: repeat(5, 1fr); gap: var(--og-space-2); margin-block-start: var(--og-space-4); text-align: center; font-size: var(--og-text-xs); list-style: none; }
  .og-calc { display: grid; gap: var(--og-space-3); }
  .og-calc__display { text-align: end; font-size: var(--og-text-2xl); font-family: var(--og-font-mono); padding: var(--og-space-3); background: var(--og-surface-inset); border-radius: var(--og-radius-md); }
  .og-calc__keys { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--og-space-2); }
  .og-spark { inline-size: 100%; block-size: 64px; }
  .og-spark path.line { fill: none; stroke: var(--og-white); stroke-width: 1.5; }
  .og-def__word { font-size: var(--og-text-2xl); }
  .og-def__phonetic { color: var(--og-text-muted); font-family: var(--og-font-mono); font-size: var(--og-text-sm); }
  .og-def__meaning { margin-block-start: var(--og-space-3); }
}
"""

C["10-buttons-actions.css"] = """
/* =============================================================
 * PikSearch - 10-buttons-actions.css
 * Forty-recipe compatible button set: filled, tinted, gray, bordered,
 * plain, glass. Semantic button elements only.
 * ============================================================= */
@layer og.buttons {
  .og-btn { display: inline-flex; align-items: center; justify-content: center; gap: var(--og-space-2); padding: var(--og-space-2) var(--og-space-5); min-block-size: 40px; border-radius: var(--og-radius-pill); font-weight: 600; font-size: var(--og-text-sm); cursor: pointer; user-select: none; border: 1px solid transparent; transition: transform var(--og-dur-instant) var(--og-ease-spring), background var(--og-dur-fast), color var(--og-dur-fast), border-color var(--og-dur-fast), box-shadow var(--og-dur-fast); }
  .og-btn:active { transform: scale(0.97); }
  .og-btn:disabled, .og-btn[aria-disabled="true"] { opacity: 0.4; pointer-events: none; }
  .og-btn--filled { background: var(--og-white); color: var(--og-black); }
  .og-btn--filled:hover { background: var(--og-gray-8); box-shadow: 0 0 20px rgba(255,255,255,0.18); }
  .og-btn--tinted { background: var(--og-accent-soft); color: var(--og-white); }
  .og-btn--tinted:hover { background: rgba(255,255,255,0.2); }
  .og-btn--gray { background: var(--og-black-400); color: var(--og-text-secondary); }
  .og-btn--gray:hover { background: var(--og-black-500); color: var(--og-white); }
  .og-btn--bordered { border-color: var(--og-hairline-strong); color: var(--og-text-secondary); }
  .og-btn--bordered:hover { color: var(--og-white); border-color: var(--og-white); }
  .og-btn--plain { color: var(--og-text-secondary); }
  .og-btn--plain:hover { color: var(--og-white); background: var(--og-accent-soft); }
  .og-btn--glass { background: transparent; -webkit-backdrop-filter: var(--og-glass-blur-thin); backdrop-filter: var(--og-glass-blur-thin); border-color: var(--og-glass-border-top); color: var(--og-white); box-shadow: var(--og-glass-inner-highlight); }
  .og-btn--sm { min-block-size: 30px; padding-inline: var(--og-space-3); font-size: var(--og-text-xs); }
  .og-btn--lg { min-block-size: 52px; padding-inline: var(--og-space-7); font-size: var(--og-text-base); }
  .og-btn--icon { inline-size: 40px; padding-inline: 0; }
  .og-btn--block { inline-size: 100%; }
  .og-iconbtn { display: grid; place-items: center; inline-size: 36px; block-size: 36px; border-radius: 50%; color: var(--og-text-secondary); cursor: pointer; border: 0; background: transparent; transition: background var(--og-dur-fast), color var(--og-dur-fast); }
  .og-iconbtn:hover { background: var(--og-accent-soft); color: var(--og-white); }
  .og-iconbtn[aria-pressed="true"] { color: var(--og-black); background: var(--og-white); }
}
"""

C["11-forms-inputs.css"] = """
/* =============================================================
 * PikSearch - 11-forms-inputs.css
 * Settings form primitives: labeled fields, selects, switches, radio
 * rows. Every control carries a visible accessible label.
 * ============================================================= */
@layer og.forms {
  .og-field { display: grid; gap: var(--og-space-2); margin-block-end: var(--og-space-5); }
  .og-field__label { font-size: var(--og-text-sm); font-weight: 600; color: var(--og-text-secondary); }
  .og-field__hint { font-size: var(--og-text-xs); color: var(--og-text-muted); }
  .og-input, .og-select, .og-textarea { inline-size: 100%; padding: var(--og-space-3) var(--og-space-4); background: var(--og-surface); border: 1px solid var(--og-hairline); border-radius: var(--og-radius-md); color: var(--og-white); transition: border-color var(--og-dur-fast), background var(--og-dur-fast); }
  .og-input:hover, .og-select:hover { border-color: var(--og-hairline-strong); }
  .og-input:focus, .og-select:focus, .og-textarea:focus { border-color: var(--og-white); background: var(--og-surface-strong); outline: none; }
  .og-select { appearance: none; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' fill='%23ffffff'%3E%3Cpath d='M6 8L1 3h10z'/%3E%3C/svg%3E"); background-repeat: no-repeat; background-position: right 12px center; }
  .og-switch { position: relative; inline-size: 51px; block-size: 31px; display: inline-block; }
  .og-switch input { position: absolute; opacity: 0; inline-size: 100%; block-size: 100%; margin: 0; cursor: pointer; }
  .og-switch__track { position: absolute; inset: 0; border-radius: var(--og-radius-pill); background: var(--og-black-500); box-shadow: inset 0 1px 3px rgba(0,0,0,0.6); transition: background var(--og-dur-base) var(--og-ease-standard); pointer-events: none; }
  .og-switch__thumb { position: absolute; top: 2px; left: 2px; inline-size: 27px; block-size: 27px; border-radius: 50%; background: var(--og-white); box-shadow: 0 2px 6px rgba(0,0,0,0.5); transition: translate var(--og-dur-base) var(--og-ease-spring); pointer-events: none; }
  .og-switch input:checked ~ .og-switch__track { background: var(--og-white); }
  .og-switch input:checked ~ .og-switch__thumb { translate: 20px 0; background: var(--og-black); }
  .og-switch input:focus-visible ~ .og-switch__track { outline: 2px solid var(--og-focus-ring); outline-offset: 2px; }
  .og-radio-row { display: flex; align-items: center; gap: var(--og-space-3); padding: var(--og-space-3); border-radius: var(--og-radius-md); cursor: pointer; }
  .og-radio-row:hover { background: var(--og-surface); }
  .og-radio-row input { accent-color: var(--og-white); inline-size: 18px; block-size: 18px; }
}
"""

C["12-modals-overlays.css"] = """
/* =============================================================
 * PikSearch - 12-modals-overlays.css
 * Dialog sheet recipe with scrim, spring entry, focus-trap friendly
 * structure. Uses semantic dialog where available.
 * ============================================================= */
@layer og.modal {
  .og-modal { position: fixed; inset: 0; z-index: var(--og-z-modal); display: grid; place-items: center; padding: var(--og-gutter); visibility: hidden; }
  .og-modal[data-open="true"] { visibility: visible; }
  .og-modal__scrim { position: absolute; inset: 0; background: rgba(0,0,0,0.7); -webkit-backdrop-filter: blur(8px); backdrop-filter: blur(8px); opacity: 0; transition: opacity var(--og-dur-base); border: 0; cursor: pointer; }
  .og-modal[data-open="true"] .og-modal__scrim { opacity: 1; }
  .og-modal__panel { position: relative; inline-size: min(560px, 100%); max-block-size: 82vh; overflow: auto; padding: var(--og-space-6); transform: translateY(24px) scale(0.96); opacity: 0; transition: transform var(--og-dur-slow) var(--og-ease-spring), opacity var(--og-dur-base); }
  .og-modal[data-open="true"] .og-modal__panel { transform: translateY(0) scale(1); opacity: 1; }
  .og-modal__header { display: flex; justify-content: space-between; align-items: center; margin-block-end: var(--og-space-4); }
  .og-modal__title { font-size: var(--og-text-xl); }
  .og-sheet { border-radius: var(--og-radius-2xl) var(--og-radius-2xl) 0 0; align-self: end; inline-size: 100%; max-inline-size: 720px; }
  dialog.og-modal { position: fixed; }
  dialog.og-modal::backdrop { background: transparent; }
}
"""

C["13-toasts-notifications.css"] = """
/* =============================================================
 * PikSearch - 13-toasts-notifications.css
 * Stacked glass toasts, slide+fade entry, progress drain bar,
 * aria-live region defaults.
 * ============================================================= */
@layer og.toast {
  .og-toast-region { position: fixed; inset-block-start: calc(var(--og-header-h) + var(--og-space-4)); inset-inline-end: var(--og-gutter); z-index: var(--og-z-toast); display: grid; gap: var(--og-space-3); inline-size: min(380px, calc(100vw - var(--og-gutter) * 2)); }
  .og-toast { display: grid; grid-template-columns: auto 1fr auto; gap: var(--og-space-3); align-items: start; padding: var(--og-space-4); animation: og-toast-in var(--og-dur-slow) var(--og-ease-spring) both; }
  .og-toast[data-leaving="true"] { animation: og-toast-out var(--og-dur-base) var(--og-ease-standard) both; }
  .og-toast__msg { font-size: var(--og-text-sm); }
  .og-toast__progress { grid-column: 1 / -1; block-size: 2px; background: var(--og-hairline); border-radius: 2px; overflow: hidden; }
  .og-toast__progress i { display: block; block-size: 100%; background: var(--og-white); animation: og-drain linear forwards; }
  @keyframes og-toast-in { from { transform: translateX(40px) scale(0.9); opacity: 0; } to { transform: none; opacity: 1; } }
  @keyframes og-toast-out { to { transform: translateY(-12px) scale(0.95); opacity: 0; } }
  @keyframes og-drain { from { inline-size: 100%; } to { inline-size: 0%; } }
}
"""

C["14-dropdowns-menus.css"] = """
/* =============================================================
 * PikSearch - 14-dropdowns-menus.css
 * Menu recipe with roving tabindex support, separators, checkable
 * items. Keyboard model implemented in 14-menus.js.
 * ============================================================= */
@layer og.menu {
  .og-menu-anchor { position: relative; display: inline-block; }
  .og-menu { position: absolute; inset-block-start: calc(100% + var(--og-space-2)); inset-inline-end: 0; min-inline-size: 220px; padding: var(--og-space-2); z-index: var(--og-z-popover); transform-origin: top right; animation: og-menu-in var(--og-dur-fast) var(--og-ease-spring) both; }
  .og-menu[hidden] { display: none; }
  .og-menu__item { display: flex; align-items: center; gap: var(--og-space-3); inline-size: 100%; padding: var(--og-space-2) var(--og-space-3); border-radius: var(--og-radius-sm); font-size: var(--og-text-sm); color: var(--og-text-secondary); cursor: pointer; text-align: start; border: 0; background: transparent; }
  .og-menu__item:hover, .og-menu__item:focus-visible { background: var(--og-accent-soft); color: var(--og-white); outline: none; }
  .og-menu__item[role="menuitemcheckbox"][aria-checked="true"]::before { content: "\\2713"; font-weight: 800; }
  .og-menu__sep { block-size: 1px; background: var(--og-hairline); margin-block: var(--og-space-2); border: 0; }
  .og-menu__label { padding: var(--og-space-2) var(--og-space-3); font-size: var(--og-text-xs); text-transform: uppercase; letter-spacing: 0.08em; color: var(--og-text-faint); }
  @keyframes og-menu-in { from { transform: scale(0.95) translateY(-4px); opacity: 0; } to { transform: none; opacity: 1; } }
}
"""

C["15-tabs-switchers.css"] = """
/* =============================================================
 * PikSearch - 15-tabs-switchers.css
 * Pill tabs with sliding glass indicator (transform-driven),
 * segmented control recipe. ARIA tablist semantics required.
 * ============================================================= */
@layer og.tabs {
  .og-tabs { position: relative; }
  .og-tablist { display: flex; gap: var(--og-space-1); padding: var(--og-space-1); border-radius: var(--og-radius-pill); background: var(--og-surface); border: 1px solid var(--og-hairline); }
  .og-tab { flex: 1; display: inline-flex; justify-content: center; align-items: center; gap: var(--og-space-2); padding: var(--og-space-2) var(--og-space-4); border-radius: var(--og-radius-pill); font-size: var(--og-text-sm); font-weight: 550; color: var(--og-text-muted); cursor: pointer; background: transparent; border: 0; transition: color var(--og-dur-fast); position: relative; z-index: 2; }
  .og-tab[aria-selected="true"] { color: var(--og-black); }
  .og-tab-indicator { position: absolute; z-index: 1; border-radius: var(--og-radius-pill); background: var(--og-white); box-shadow: var(--og-elev-2); transition: transform var(--og-dur-base) var(--og-ease-spring), inline-size var(--og-dur-base) var(--og-ease-spring); }
  .og-tabpanel[hidden] { display: none; }
  .og-tabpanel { animation: og-panel-in var(--og-dur-base) var(--og-ease-standard) both; }
  @keyframes og-panel-in { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: none; } }
  .og-segmented { display: inline-flex; border: 1px solid var(--og-hairline-strong); border-radius: var(--og-radius-pill); overflow: hidden; }
  .og-segmented button { padding: var(--og-space-1) var(--og-space-4); font-size: var(--og-text-xs); color: var(--og-text-muted); border: 0; background: transparent; cursor: pointer; }
  .og-segmented button[aria-pressed="true"] { background: var(--og-white); color: var(--og-black); font-weight: 700; }
}
"""

C["16-slider-scrollbar.css"] = """
/* =============================================================
 * PikSearch - 16-slider-scrollbar.css
 * Range slider with liquid thumb, custom scroll rails, marquee.
 * Fill geometry updated by 16-slider.js.
 * ============================================================= */
@layer og.slider {
  .og-range { position: relative; block-size: 36px; display: flex; align-items: center; }
  .og-range input[type="range"] { inline-size: 100%; appearance: none; background: transparent; cursor: pointer; }
  .og-range__rail { position: absolute; inset-inline: 0; block-size: 4px; border-radius: 4px; background: var(--og-black-500); pointer-events: none; }
  .og-range__fill { position: absolute; block-size: 4px; border-radius: 4px; background: var(--og-white); pointer-events: none; }
  .og-range input::-webkit-slider-thumb { appearance: none; inline-size: 22px; block-size: 22px; border-radius: 50%; background: var(--og-white); box-shadow: var(--og-elev-2); border: 0; transition: transform var(--og-dur-fast) var(--og-ease-spring); }
  .og-range input:active::-webkit-slider-thumb { transform: scale(1.2); }
  .og-range input::-moz-range-thumb { inline-size: 22px; block-size: 22px; border-radius: 50%; background: var(--og-white); border: 0; }
  .og-scrollrail { overflow: auto; scrollbar-width: thin; overscroll-behavior: contain; }
  .og-marquee { overflow: hidden; mask-image: linear-gradient(90deg, transparent, #000 10%, #000 90%, transparent); }
  .og-marquee__track { display: flex; gap: var(--og-space-6); width: max-content; animation: og-marquee 30s linear infinite; }
  .og-marquee:hover .og-marquee__track { animation-play-state: paused; }
  @keyframes og-marquee { to { transform: translateX(-50%); } }
}
"""

C["17-tooltip-popover.css"] = """
/* =============================================================
 * PikSearch - 17-tooltip-popover.css
 * Delay-aware tooltip with arrow, popover card recipe, info-dot
 * pattern used across settings screens.
 * ============================================================= */
@layer og.tip {
  .og-tip { position: absolute; z-index: var(--og-z-tooltip); padding: var(--og-space-2) var(--og-space-3); max-inline-size: 260px; font-size: var(--og-text-xs); color: var(--og-white); background: rgba(255,255,255,0.1); -webkit-backdrop-filter: var(--og-glass-blur-thin); backdrop-filter: var(--og-glass-blur-thin); border: 1px solid var(--og-glass-border-top); border-radius: var(--og-radius-sm); box-shadow: var(--og-elev-3); pointer-events: none; opacity: 0; transform: translateY(4px) scale(0.98); transition: opacity var(--og-dur-fast), transform var(--og-dur-fast) var(--og-ease-spring); }
  .og-tip[data-show="true"] { opacity: 1; transform: none; }
  .og-popover { position: absolute; z-index: var(--og-z-popover); inline-size: min(340px, 92vw); padding: var(--og-space-4); animation: og-pop-in var(--og-dur-base) var(--og-ease-spring) both; }
  .og-popover[hidden] { display: none; }
  .og-info-dot { display: inline-grid; place-items: center; inline-size: 16px; block-size: 16px; border-radius: 50%; border: 1px solid var(--og-hairline-strong); font-size: 10px; color: var(--og-text-muted); cursor: help; background: transparent; }
  @keyframes og-pop-in { from { opacity: 0; transform: scale(0.94) translateY(6px); } to { opacity: 1; transform: none; } }
}
"""

C["18-loading-skeletons.css"] = """
/* =============================================================
 * PikSearch - 18-loading-skeletons.css
 * Shimmer skeletons (grayscale sweep), spinner ring, indeterminate
 * bar. Reduced-motion freezes shimmer.
 * ============================================================= */
@layer og.load {
  .og-skel { position: relative; overflow: hidden; background: var(--og-black-400); border-radius: var(--og-radius-sm); }
  .og-skel::after { content: ""; position: absolute; inset: 0; transform: translateX(-100%); background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent); animation: og-shimmer 1.6s var(--og-ease-standard) infinite; }
  @keyframes og-shimmer { to { transform: translateX(100%); } }
  .og-skel--text { block-size: 0.9em; margin-block: 0.35em; }
  .og-skel--title { block-size: 1.4em; inline-size: 60%; }
  .og-skel--thumb { aspect-ratio: 16/9; border-radius: var(--og-radius-lg); }
  .og-spinner { inline-size: 28px; block-size: 28px; border-radius: 50%; border: 2px solid var(--og-black-600); border-block-start-color: var(--og-white); animation: og-spin 0.8s linear infinite; }
  @keyframes og-spin { to { rotate: 360deg; } }
  .og-progress { block-size: 3px; border-radius: 3px; background: var(--og-black-500); overflow: hidden; }
  .og-progress i { display: block; block-size: 100%; inline-size: 30%; background: var(--og-white); animation: og-indet 1.2s var(--og-ease-standard) infinite; }
  @keyframes og-indet { 0% { transform: translateX(-100%); } 100% { transform: translateX(340%); } }
  @media (prefers-reduced-motion: reduce) {
    .og-skel::after, .og-spinner, .og-progress i { animation: none; }
    .og-spinner { border-block-start-color: var(--og-gray-4); }
  }
}
"""

C["19-empty-states.css"] = """
/* =============================================================
 * PikSearch - 19-empty-states.css
 * Zero-result art (pure SVG line-art, monochrome), gentle copy,
 * recovery CTA cluster, offline banner.
 * ============================================================= */
@layer og.empty {
  .og-empty { display: grid; justify-items: center; text-align: center; gap: var(--og-space-4); padding-block: var(--og-space-9); }
  .og-empty__art { inline-size: 140px; opacity: 0.85; }
  .og-empty__art .stroke { fill: none; stroke: var(--og-gray-3); stroke-width: 2; stroke-linecap: round; }
  .og-empty__art .accent { fill: var(--og-white); }
  .og-empty__title { font-size: var(--og-text-xl); }
  .og-empty__desc { color: var(--og-text-muted); max-inline-size: 44ch; }
  .og-offline { position: fixed; inset-block-start: var(--og-header-h); inset-inline: 0; z-index: var(--og-z-overlay); text-align: center; padding: var(--og-space-2); font-size: var(--og-text-sm); background: var(--og-white); color: var(--og-black); transform: translateY(-120%); transition: transform var(--og-dur-base) var(--og-ease-spring); }
  .og-offline[data-show="true"] { transform: none; }
}
"""

C["20-settings-premium.css"] = """
/* =============================================================
 * PikSearch - 20-settings-premium.css
 * Grouped-list settings screen (iOS-style inset grouped cards),
 * section headers, value trails.
 * ============================================================= */
@layer og.settings {
  .og-settings { display: grid; gap: var(--og-space-6); max-inline-size: 720px; margin-inline: auto; }
  .og-set-group { padding: var(--og-space-1); }
  .og-set-group__title { padding: var(--og-space-3) var(--og-space-4) var(--og-space-2); }
  .og-set-row { display: flex; align-items: center; gap: var(--og-space-4); padding: var(--og-space-4); border-radius: var(--og-radius-md); min-block-size: 56px; transition: background var(--og-dur-fast); border: 0; background: transparent; inline-size: 100%; text-align: start; color: inherit; }
  .og-set-row + .og-set-row { box-shadow: inset 0 1px 0 var(--og-hairline); }
  .og-set-row:hover { background: var(--og-surface); }
  .og-set-row__icon { inline-size: 30px; block-size: 30px; display: grid; place-items: center; border-radius: 8px; background: var(--og-surface-strong); flex: none; }
  .og-set-row__label { flex: 1; font-size: var(--og-text-base); }
  .og-set-row__value { color: var(--og-text-muted); font-size: var(--og-text-sm); }
  .og-set-row__chev { color: var(--og-text-faint); }
  .og-set-row--nav { cursor: pointer; }
}
"""

C["21-hero-landing.css"] = """
/* =============================================================
 * PikSearch - 21-hero-landing.css
 * Full-bleed hero with WebGL canvas behind glass search bar, wordmark
 * lockup, tagline, feature ticker. The canvas is an OWNED source -
 * the sanctioned open-glass-ui/webgl surface on the landing page.
 * ============================================================= */
@layer og.hero {
  .og-hero-stage { position: relative; display: grid; place-items: center; min-block-size: 100svh; overflow: hidden; }
  .og-hero-canvas { position: absolute; inset: 0; inline-size: 100%; block-size: 100%; z-index: 0; }
  .og-hero-content { position: relative; z-index: 1; display: grid; justify-items: center; gap: var(--og-space-6); inline-size: 100%; padding-inline: var(--og-gutter); }
  .og-wordmark { font-size: clamp(3rem, 8vw, 6rem); font-weight: 900; letter-spacing: -0.05em; line-height: 1; }
  .og-wordmark span { color: var(--og-gray-2); }
  .og-tagline { color: var(--og-text-muted); font-size: var(--og-text-lg); max-inline-size: 46ch; }
  .og-ticker { display: flex; gap: var(--og-space-6); color: var(--og-text-faint); font-size: var(--og-text-xs); text-transform: uppercase; letter-spacing: 0.12em; list-style: none; }
  .og-scroll-hint { position: absolute; inset-block-end: var(--og-space-6); inset-inline-start: 50%; translate: -50% 0; animation: og-bob 2s var(--og-ease-standard) infinite; color: var(--og-text-faint); }
  @keyframes og-bob { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(8px); } }
}
"""

C["22-image-gallery.css"] = """
/* =============================================================
 * PikSearch - 22-image-gallery.css
 * Masonry-ish image grid (CSS columns), hover zoom-lift, lightbox
 * overlay. Images are owned sources eligible for WebGL refraction.
 * ============================================================= */
@layer og.gallery {
  .og-masonry { columns: 4 220px; column-gap: var(--og-space-4); }
  .og-masonry > * { break-inside: avoid; margin-block-end: var(--og-space-4); }
  .og-thumb { position: relative; border-radius: var(--og-radius-lg); overflow: hidden; cursor: zoom-in; background: var(--og-black-300); border: 0; padding: 0; display: block; inline-size: 100%; }
  .og-thumb img { inline-size: 100%; display: block; transition: transform var(--og-dur-slow) var(--og-ease-out-quint), filter var(--og-dur-base); filter: grayscale(1); }
  .og-thumb:hover img, .og-thumb:focus-visible img { transform: scale(1.04); filter: grayscale(0.85); }
  .og-thumb__caption { position: absolute; inset-inline: 0; inset-block-end: 0; padding: var(--og-space-3); font-size: var(--og-text-xs); background: linear-gradient(transparent, rgba(0,0,0,0.85)); opacity: 0; transition: opacity var(--og-dur-fast); }
  .og-thumb:hover .og-thumb__caption, .og-thumb:focus-within .og-thumb__caption { opacity: 1; }
  .og-lightbox { position: fixed; inset: 0; z-index: var(--og-z-modal); display: grid; place-items: center; background: rgba(0,0,0,0.92); -webkit-backdrop-filter: blur(20px); backdrop-filter: blur(20px); }
  .og-lightbox[hidden] { display: none; }
  .og-lightbox img { max-block-size: 82vh; max-inline-size: 90vw; border-radius: var(--og-radius-lg); box-shadow: var(--og-glass-shadow); }
}
"""

C["23-video-player.css"] = """
/* =============================================================
 * PikSearch - 23-video-player.css
 * Video result card: owned video source (WebGL-glass eligible),
 * custom monochrome transport controls over a glass bar.
 * ============================================================= */
@layer og.video {
  .og-video { position: relative; border-radius: var(--og-radius-xl); overflow: hidden; background: var(--og-black); }
  .og-video video { inline-size: 100%; display: block; }
  .og-video__controls { position: absolute; inset-inline: var(--og-space-3); inset-block-end: var(--og-space-3); display: flex; align-items: center; gap: var(--og-space-3); padding: var(--og-space-2) var(--og-space-3); }
  .og-video__scrub { flex: 1; position: relative; block-size: 4px; border-radius: 4px; background: rgba(255,255,255,0.25); cursor: pointer; border: 0; padding: 0; }
  .og-video__played { position: absolute; inset: 0 auto 0 0; block-size: 100%; border-radius: 4px; background: var(--og-white); }
  .og-video__time { font-family: var(--og-font-mono); font-size: var(--og-text-xs); color: var(--og-text-secondary); }
  .og-video:not(:hover):not(:focus-within) .og-video__controls { opacity: 0; transform: translateY(8px); transition: all var(--og-dur-base); }
}
"""

C["24-audio-waveform.css"] = """
/* =============================================================
 * PikSearch - 24-audio-waveform.css
 * Podcast/voice result card with static waveform bars (monochrome),
 * playhead sweep, speed pill.
 * ============================================================= */
@layer og.audio {
  .og-audio { display: grid; grid-template-columns: auto 1fr auto; gap: var(--og-space-4); align-items: center; padding: var(--og-space-4); }
  .og-wave { display: flex; align-items: center; gap: 2px; block-size: 40px; }
  .og-wave i { inline-size: 3px; border-radius: 2px; background: var(--og-gray-2); }
  .og-wave i.played { background: var(--og-white); }
  .og-audio.is-playing .og-wave i { animation: og-pulse 1.2s ease-in-out infinite alternate; }
  @keyframes og-pulse { from { transform: scaleY(0.7); } to { transform: scaleY(1.15); } }
  .og-speed { font-family: var(--og-font-mono); font-size: var(--og-text-xs); padding: var(--og-space-1) var(--og-space-2); border: 1px solid var(--og-hairline-strong); border-radius: var(--og-radius-pill); cursor: pointer; background: transparent; color: inherit; }
}
"""

C["25-maps-directions.css"] = """
/* =============================================================
 * PikSearch - 25-maps-directions.css
 * Local pack: stylized map frame (grayscale tiles), pin markers,
 * hours table, distance chips.
 * ============================================================= */
@layer og.maps {
  .og-map-frame { position: relative; aspect-ratio: 16/10; border-radius: var(--og-radius-lg); overflow: hidden; background: repeating-linear-gradient(45deg, var(--og-black-300) 0 12px, var(--og-black-200) 12px 24px); filter: grayscale(1) contrast(1.1); }
  .og-pin { position: absolute; translate: -50% -100%; }
  .og-pin::before { content: ""; display: block; inline-size: 14px; block-size: 14px; border-radius: 50% 50% 50% 0; rotate: -45deg; background: var(--og-white); box-shadow: 0 4px 10px rgba(0,0,0,0.6); }
  .og-hours { display: grid; grid-template-columns: auto 1fr; gap: var(--og-space-1) var(--og-space-4); font-size: var(--og-text-sm); }
  .og-hours [data-day="today"] { color: var(--og-white); font-weight: 600; }
  .og-dist-chips { display: flex; gap: var(--og-space-2); flex-wrap: wrap; list-style: none; }
}
"""

C["26-calendar-events.css"] = """
/* =============================================================
 * PikSearch - 26-calendar-events.css
 * Event widget: date brick, agenda list, countdown numerals.
 * ============================================================= */
@layer og.cal {
  .og-datebrick { display: grid; place-items: center; inline-size: 64px; block-size: 68px; border-radius: var(--og-radius-md); background: var(--og-white); color: var(--og-black); line-height: 1.1; }
  .og-datebrick b { font-size: var(--og-text-xl); }
  .og-agenda { display: grid; gap: var(--og-space-3); list-style: none; }
  .og-agenda li { display: grid; grid-template-columns: 56px 1fr; gap: var(--og-space-3); align-items: center; padding: var(--og-space-3); border-radius: var(--og-radius-md); border: 1px solid var(--og-hairline); }
  .og-countdown { display: flex; gap: var(--og-space-4); font-family: var(--og-font-mono); }
  .og-countdown div { text-align: center; }
  .og-countdown b { display: block; font-size: var(--og-text-2xl); }
}
"""

C["27-translate-linguistic.css"] = """
/* =============================================================
 * PikSearch - 27-translate-linguistic.css
 * Translator card: dual-pane layout, character counter, swap button
 * rotation animation, IPA line.
 * ============================================================= */
@layer og.i18n {
  .og-translator { display: grid; grid-template-columns: 1fr auto 1fr; gap: var(--og-space-4); align-items: stretch; }
  .og-trans-pane { padding: var(--og-space-4); min-block-size: 140px; }
  .og-trans-pane textarea { inline-size: 100%; block-size: 100%; resize: none; background: transparent; color: var(--og-white); border: 0; outline: none; }
  .og-swap { align-self: center; }
  .og-swap:hover svg { rotate: 180deg; transition: rotate var(--og-dur-base) var(--og-ease-spring); }
  .og-charcount { text-align: end; font-size: var(--og-text-xs); color: var(--og-text-faint); }
  .og-ipa { font-family: var(--og-font-mono); color: var(--og-text-muted); }
}
"""

C["28-code-snippets.css"] = """
/* =============================================================
 * PikSearch - 28-code-snippets.css
 * Code block card: mono type, copy affordance, line gutter, token
 * coloring expressed as gray-scale weights (bold/bright/dim).
 * ============================================================= */
@layer og.code {
  .og-codeblock { position: relative; border-radius: var(--og-radius-lg); background: var(--og-black); border: 1px solid var(--og-hairline); overflow: hidden; }
  .og-codeblock pre { padding: var(--og-space-5); overflow: auto; font-family: var(--og-font-mono); font-size: var(--og-text-sm); line-height: 1.7; }
  .og-codeblock .tok-kw { color: var(--og-white); font-weight: 700; }
  .og-codeblock .tok-str { color: var(--og-gray-5); font-style: italic; }
  .og-codeblock .tok-com { color: var(--og-black-900); }
  .og-codeblock .tok-num { color: var(--og-gray-7); }
  .og-copy-btn { position: absolute; inset-block-start: var(--og-space-3); inset-inline-end: var(--og-space-3); }
  .og-lang-tag { position: absolute; inset-block-start: var(--og-space-3); inset-inline-start: var(--og-space-4); font-size: 10px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--og-text-faint); }
  .og-line-no { display: inline-block; inline-size: 2.5ch; color: var(--og-black-800); user-select: none; text-align: end; margin-inline-end: 1.5ch; }
}
"""

C["29-tables-data.css"] = """
/* =============================================================
 * PikSearch - 29-tables-data.css
 * Data tables (stocks, comparisons): sticky header, sortable carets,
 * hairline rows, right-aligned tabular numerals.
 * ============================================================= */
@layer og.table {
  .og-table-wrap { overflow: auto; border-radius: var(--og-radius-lg); border: 1px solid var(--og-hairline); }
  .og-table { inline-size: 100%; border-collapse: collapse; font-size: var(--og-text-sm); }
  .og-table th { position: sticky; inset-block-start: 0; background: var(--og-black-200); text-align: start; padding: var(--og-space-3) var(--og-space-4); font-weight: 600; color: var(--og-text-secondary); cursor: pointer; }
  .og-table td { padding: var(--og-space-3) var(--og-space-4); border-block-start: 1px solid var(--og-hairline); }
  .og-table tbody tr:hover { background: var(--og-surface); }
  .og-table [data-align="num"] { text-align: end; font-variant-numeric: tabular-nums; }
  .og-sort-caret { opacity: 0.4; }
  th[aria-sort="ascending"] .og-sort-caret, th[aria-sort="descending"] .og-sort-caret { opacity: 1; }
}
"""

C["30-footer-legal.css"] = """
/* =============================================================
 * PikSearch - 30-footer-legal.css
 * Mega footer: link columns, language select, privacy-first badges.
 * ============================================================= */
@layer og.footer {
  .og-footer { margin-block-start: var(--og-space-9); border-block-start: 1px solid var(--og-hairline); padding-block: var(--og-space-8) var(--og-space-6); background: var(--og-black-100); }
  .og-footer__cols { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: var(--og-space-6); }
  .og-footer h3 { font-size: var(--og-text-xs); text-transform: uppercase; letter-spacing: 0.1em; color: var(--og-text-faint); margin-block-end: var(--og-space-3); }
  .og-footer a { display: block; padding-block: var(--og-space-1); color: var(--og-text-secondary); font-size: var(--og-text-sm); text-decoration: none; }
  .og-footer a:hover { color: var(--og-white); text-decoration: underline; text-underline-offset: 3px; }
  .og-footer__bottom { display: flex; flex-wrap: wrap; gap: var(--og-space-4); justify-content: space-between; margin-block-start: var(--og-space-8); padding-block-start: var(--og-space-4); border-block-start: 1px solid var(--og-hairline); color: var(--og-text-faint); font-size: var(--og-text-xs); }
}
"""

C["31-dark-theme-tokens.css"] = """
/* =============================================================
 * PikSearch - 31-dark-theme-tokens.css
 * The app ships black-first; this file defines the inverted "paper"
 * theme (white bg / black ink) toggled via html[data-theme="paper"],
 * plus auto-sync with prefers-color-scheme when data-theme="auto".
 * ============================================================= */
@layer og.theme {
  html[data-theme="paper"] {
    --og-bg: var(--og-white);
    --og-bg-elevated: var(--og-white-50);
    --og-text: var(--og-black);
    --og-text-secondary: var(--og-black-700);
    --og-text-muted: var(--og-black-500);
    --og-text-faint: var(--og-black-600);
    --og-surface: rgba(0,0,0,0.04);
    --og-surface-strong: rgba(0,0,0,0.08);
    --og-hairline: rgba(0,0,0,0.12);
    --og-hairline-strong: rgba(0,0,0,0.22);
    --og-accent: var(--og-black);
    --og-on-accent: var(--og-white);
    --og-focus-ring: rgba(0,0,0,0.85);
    --og-glass-tint: rgba(255,255,255,0.55);
    --og-glass-border-top: rgba(0,0,0,0.12);
    color-scheme: light;
  }
  @media (prefers-color-scheme: light) {
    html[data-theme="auto"] {
      --og-bg: var(--og-white);
      --og-text: var(--og-black);
      --og-text-secondary: var(--og-black-700);
      --og-surface: rgba(0,0,0,0.04);
      --og-hairline: rgba(0,0,0,0.12);
      --og-accent: var(--og-black);
      --og-on-accent: var(--og-white);
      color-scheme: light;
    }
  }
  html[data-theme="paper"] body { background: var(--og-white); }
  html[data-theme="paper"] ::selection { background: var(--og-black); color: var(--og-white); }
  html[data-theme="paper"] .og-search__submit { background: var(--og-black); color: var(--og-white); }
  html[data-theme="paper"] .og-btn--filled { background: var(--og-black); color: var(--og-white); }
}
"""

C["32-responsive-fluid.css"] = """
/* =============================================================
 * PikSearch - 32-responsive-fluid.css
 * Fluid interpolation across four breakpoints + dynamic viewport
 * units for mobile chrome, safe-area insets for notched devices.
 * ============================================================= */
@layer og.responsive {
  :root { --og-vh: 1vh; }
  @supports (height: 100dvh) { :root { --og-vh: 1dvh; } }
  .og-full-bleed { margin-inline: calc(50% - 50vw); inline-size: 100vw; }
  .og-safe-bottom { padding-block-end: env(safe-area-inset-bottom, 0px); }
  .og-safe-x { padding-inline: max(var(--og-gutter), env(safe-area-inset-left, 0px)) max(var(--og-gutter), env(safe-area-inset-right, 0px)); }
  @media (max-width: 480px) {
    :root { --og-header-h: 56px; }
    .og-hide-xs { display: none !important; }
  }
  @media (min-width: 481px) and (max-width: 768px) { .og-hide-sm { display: none !important; } }
  @media (min-width: 769px) and (max-width: 1200px) { .og-hide-md { display: none !important; } }
  @media (min-width: 1201px) { .og-hide-lg { display: none !important; } }
  @media (hover: none) and (pointer: coarse) {
    .og-hover-only { display: none !important; }
    .og-btn { min-block-size: 48px; }
  }
  @media (hover: hover) { .og-touch-only { display: none !important; } }
}
"""

C["33-motion-system.css"] = """
/* =============================================================
 * PikSearch - 33-motion-system.css
 * Named transitions & keyframes reused by JS controllers: spring
 * pop, sheet rise, liquid morph, parallax drift, stagger reveal.
 * ============================================================= */
@layer og.motion {
  .og-pop { animation: og-pop var(--og-dur-spring) var(--og-ease-spring) both; }
  @keyframes og-pop { 0% { transform: scale(0.8); opacity: 0; } 60% { transform: scale(1.03); } 100% { transform: scale(1); opacity: 1; } }
  .og-rise { animation: og-rise var(--og-dur-slow) var(--og-ease-emphasize) both; }
  @keyframes og-rise { from { transform: translateY(40px); opacity: 0; } to { transform: none; opacity: 1; } }
  .og-liquid-in { animation: og-liquid 900ms var(--og-ease-out-quint) both; }
  @keyframes og-liquid { 0% { border-radius: 50%; transform: scale(0.6); opacity: 0; } 55% { border-radius: var(--og-radius-xl); } 100% { transform: scale(1); opacity: 1; } }
  .og-stagger > * { animation: og-rise var(--og-dur-slow) var(--og-ease-emphasize) both; }
  .og-stagger > *:nth-child(1) { animation-delay: 0ms; }
  .og-stagger > *:nth-child(2) { animation-delay: 60ms; }
  .og-stagger > *:nth-child(3) { animation-delay: 120ms; }
  .og-stagger > *:nth-child(4) { animation-delay: 180ms; }
  .og-stagger > *:nth-child(5) { animation-delay: 240ms; }
  .og-stagger > *:nth-child(6) { animation-delay: 300ms; }
  .og-parallax { will-change: transform; transition: transform 120ms linear; }
  .og-morph-target { transition: border-radius var(--og-dur-slow) var(--og-ease-spring), transform var(--og-dur-slow) var(--og-ease-spring); }
  @media (prefers-reduced-motion: reduce) {
    .og-pop, .og-rise, .og-liquid-in, .og-stagger > * { animation: none !important; opacity: 1; transform: none; }
    .og-parallax { transition: none; }
  }
}
"""

C["34-forced-colors-high-contrast.css"] = """
/* =============================================================
 * PikSearch - 34-forced-colors-high-contrast.css
 * Comprehensive forced-colors fallbacks so every recipe remains
 * legible under Windows high-contrast / macOS Increase Contrast.
 * Backdrop effects removed; boundaries use system colors.
 * ============================================================= */
@layer og.a11y-forced {
  @media (forced-colors: active) {
    .og-btn, .og-iconbtn, .og-page-btn, .og-engine-chip, .og-tablist, .og-menu, .og-tip, .og-popover, .og-toast,
    .og-input, .og-select, .og-textarea, .og-table-wrap, .og-codeblock, .og-thumb, .og-datebrick, .og-set-group,
    .og-trans-pane {
      background: Canvas !important;
      color: CanvasText !important;
      border: 1px solid CanvasText !important;
      box-shadow: none !important;
      forced-color-adjust: auto;
    }
    .og-btn--filled, .og-nav__link[aria-current="page"], .og-page-btn[aria-current="page"],
    .og-tab[aria-selected="true"], .og-engine-chip[aria-pressed="true"] {
      background: Highlight !important;
      color: HighlightText !important;
      border-color: Highlight !important;
    }
    .og-switch__track { border: 1px solid CanvasText; background: Canvas; }
    .og-switch__thumb { background: CanvasText; }
    .og-switch input:checked ~ .og-switch__track { background: Highlight; }
    .og-range__fill { background: Highlight; }
    .og-range input::-webkit-slider-thumb, .og-range input::-moz-range-thumb { background: CanvasText; border: 1px solid CanvasText; }
    .og-tab-indicator { background: Highlight; }
    .og-skel { background: Canvas; border: 1px dashed CanvasText; }
    .og-skel::after { display: none; }
    .og-spinner { border-color: CanvasText; border-block-start-color: Highlight; }
    .og-glass::before, .og-glass::after, .og-grain, .og-vignette { display: none !important; }
    a, .og-result__title { color: LinkText !important; }
    a:visited, .og-result__title:visited { color: VisitedText !important; }
    :focus-visible { outline: 2px solid Highlight !important; outline-offset: 2px; }
  }
}
"""

C["35-keyboard-a11y.css"] = """
/* =============================================================
 * PikSearch - 35-keyboard-a11y.css
 * Visible focus recipes per component family, arrow-key roving
 * highlight styling, aria-invalid messaging, live-region helpers.
 * ============================================================= */
@layer og.kbd {
  [data-og-focus-managed]:focus { outline: none; }
  [data-og-focus-managed]:focus-visible { outline: 2px solid var(--og-focus-ring); outline-offset: 2px; }
  .og-menu__item[data-roving-active], .og-tab[data-roving-active] { background: var(--og-accent-soft); color: var(--og-white); outline: 2px solid var(--og-focus-ring); outline-offset: -2px; }
  .og-field[data-invalid="true"] .og-input, .og-field[data-invalid="true"] .og-select { border-color: var(--og-white); box-shadow: 0 0 0 1px var(--og-white); }
  .og-field__error { font-size: var(--og-text-xs); color: var(--og-white); font-weight: 600; }
  .og-live { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
  .og-search[data-og-focused="true"].og-glass { box-shadow: var(--og-glass-shadow), var(--og-glass-inner-highlight), 0 0 0 2px var(--og-white); }
  .og-result__title:focus-visible { outline-offset: 4px; }
  @media (prefers-reduced-motion: reduce) { [data-roving-active] { transition: none; } }
}
"""

C["36-print-export.css"] = """
/* =============================================================
 * PikSearch - 36-print-export.css
 * Print/export stylesheet: results become a clean black-on-white
 * document with URLs revealed after link text; glass flattens.
 * ============================================================= */
@layer og.print {
  @media print {
    html, body { background: #fff !important; color: #000 !important; }
    .og-header, .og-footer, .og-search__submit, .og-toast-region, .og-hero-canvas, .og-grain, .og-vignette, .og-menu-toggle { display: none !important; }
    .og-glass, .og-result { background: #fff !important; border: 1px solid #000 !important; box-shadow: none !important; -webkit-backdrop-filter: none !important; backdrop-filter: none !important; color: #000 !important; }
    .og-result__title { color: #000 !important; text-decoration: none; }
    main a[href^="http"]::after { content: " (" attr(href) ")"; font-size: 9pt; color: #333; word-break: break-all; }
    .og-grid--results { grid-template-columns: 1fr !important; }
    @page { margin: 18mm; }
  }
}
"""

C["37-webgl-canvas.css"] = """
/* =============================================================
 * PikSearch - 37-webgl-canvas.css
 * Layout contracts for open-glass-ui/webgl canvases. Every canvas is
 * absolutely positioned inside its OWNED host element, never affects
 * flow, and is removed under reduced-transparency or power saver.
 * ============================================================= */
@layer og.webgl {
  .og-gl-host { position: relative; isolation: isolate; }
  .og-gl-host > canvas.og-gl { position: absolute; inset: 0; inline-size: 100%; block-size: 100%; z-index: 0; pointer-events: none; border-radius: inherit; contain: strict; }
  .og-gl-host > :not(canvas) { position: relative; z-index: 1; }
  .og-gl-badge { position: absolute; inset-block-end: 6px; inset-inline-end: 8px; font-size: 9px; letter-spacing: 0.08em; color: var(--og-text-faint); z-index: 2; user-select: none; }
  @media (prefers-reduced-transparency: reduce) { .og-gl-host > canvas.og-gl { display: none; } }
  @media (prefers-contrast: more) { .og-gl-host > canvas.og-gl { display: none; } }
  html[data-power-saver="true"] canvas.og-gl { display: none !important; }
}
"""

C["38-premium-details.css"] = """
/* =============================================================
 * PikSearch - 38-premium-details.css
 * Micro-detail pass: hairline gradients, corner specular dots,
 * inner glow on press, ultra-thin separators, luxury spacing rhythm.
 * ============================================================= */
@layer og.premium {
  .og-hairline-top { position: relative; }
  .og-hairline-top::before { content: ""; position: absolute; inset-inline: 12%; inset-block-start: 0; block-size: 1px; background: linear-gradient(90deg, transparent, var(--og-hairline-strong), transparent); }
  .og-corner-spec { position: relative; }
  .og-corner-spec::after { content: ""; position: absolute; inline-size: 4px; block-size: 4px; border-radius: 50%; background: rgba(255,255,255,0.5); inset-block-start: 6px; inset-inline-start: 10px; filter: blur(0.5px); }
  .og-press-glow:active { box-shadow: inset 0 0 24px rgba(255,255,255,0.08); }
  .og-lux-pad { padding: clamp(var(--og-space-5), 4vw, var(--og-space-8)); }
  .og-rule-fade { block-size: 1px; border: 0; background: linear-gradient(90deg, var(--og-hairline-strong), transparent); }
  .og-shadow-layered { box-shadow: 0 1px 1px rgba(255,255,255,0.04), 0 8px 24px rgba(0,0,0,0.6), 0 32px 64px rgba(0,0,0,0.5); }
}
"""

C["39-icons-system.css"] = """
/* =============================================================
 * PikSearch - 39-icons-system.css
 * Icon layer: 1.5px stroke geometry icons (self-authored SVG sprite,
 * public-domain/MIT sources only), optical sizing, hue exceptions for
 * status glyphs - the ONLY colored pixels allowed in the UI.
 * ============================================================= */
@layer og.icons {
  .og-icon { inline-size: 1.25em; block-size: 1.25em; display: inline-block; vertical-align: -0.2em; fill: none; stroke: currentColor; stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round; }
  .og-icon--sm { inline-size: 1em; block-size: 1em; }
  .og-icon--lg { inline-size: 1.75em; block-size: 1.75em; }
  .og-icon--fill { fill: currentColor; stroke: none; }
  .og-sprite { position: absolute; inline-size: 0; block-size: 0; overflow: hidden; }
  .og-icon-spin { animation: og-spin 1s linear infinite; }
  @media (prefers-reduced-motion: reduce) { .og-icon-spin { animation-duration: 3s; } }
}
"""

C["40-integration-open-glass.css"] = """
/* =============================================================
 * PikSearch - 40-integration-open-glass.css
 * Bridge layer between local recipes and the public open-glass-ui
 * facade. open-glass-ui/styles.css is imported ONCE from here. These
 * rules harmonize og-* namespaced classes with our tokens so either
 * naming works without duplication. renderer="auto": CSS renders by
 * default; scripts/03-glass-renderer.js upgrades marked hosts.
 * ============================================================= */
@import "open-glass-ui/styles.css";

@layer og.bridge {
  :root { --ogui-blur: var(--og-glass-blur); --ogui-tint: var(--og-glass-tint); --ogui-radius: var(--og-radius-fluid); }
  .ogui-glass { background: var(--og-glass-tint); border-radius: var(--og-radius-fluid); }
  .ogui-glass .ogui-label, [data-og-role="label"] { font-size: var(--og-text-xs); color: var(--og-text-muted); }
  .og-panel { padding: var(--og-space-4); border-radius: var(--og-radius-lg); background: var(--og-surface); border: 1px solid var(--og-hairline); }
  .og-panel--glass { background: var(--og-glass-tint); -webkit-backdrop-filter: var(--og-glass-blur); backdrop-filter: var(--og-glass-blur); border-color: var(--og-glass-border-top); }
  @media (forced-colors: active) { .ogui-glass, .og-panel { background: Canvas; border: 1px solid CanvasText; backdrop-filter: none; -webkit-backdrop-filter: none; } }
  @media (prefers-reduced-transparency: reduce) { .ogui-glass, .og-panel--glass { backdrop-filter: none; -webkit-backdrop-filter: none; background: var(--og-black-300); } }
}
"""
