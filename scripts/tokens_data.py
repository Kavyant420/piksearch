# -*- coding: utf-8 -*-
"""File 01 — design tokens. Single source of truth for the whole system.

Every other stylesheet consumes these custom properties; the palette contract
(pure black & white everywhere except icon glyphs) lives here as data, so it
can be audited mechanically. --og-icon-accent is the ONLY chromatic token and
is referenced exclusively by icon/status rules (39-icons-system.css).
"""

C = {}

C["01-design-tokens.css"] = """
/* =============================================================
 * PikSearch - 01-design-tokens.css
 * Design-token foundation: color, spacing scale, type ramp,
 * radii, elevation, motion curves, z-index ladder. All values
 * are resolution-independent; components never hard-code raw
 * colors outside this file (except icon glyph accents).
 * ============================================================= */
@layer og.tokens {
  :root {
    color-scheme: dark;
    /* Monochrome ramp — pure black to pure white, no hue */
    --og-black: #000000;
    --og-black-opaque: #050505;
    --og-gray-0: #0a0a0a;
    --og-gray-1: #141414;
    --og-gray-2: #1f1f1f;
    --og-gray-3: #2e2e2e;
    --og-gray-4: #4a4a4a;
    --og-gray-5: #6e6e6e;
    --og-gray-6: #9a9a9a;
    --og-gray-7: #c4c4c4;
    --og-gray-8: #e6e6e6;
    --og-white: #ffffff;
    /* Semantic surfaces */
    --og-surface: rgba(255, 255, 255, 0.045);
    --og-surface-raised: rgba(20, 20, 20, 0.82);
    --og-hairline: rgba(255, 255, 255, 0.1);
    --og-hairline-strong: rgba(255, 255, 255, 0.24);
    /* Text */
    --og-text-primary: #f5f5f5;
    --og-text-secondary: #cfcfcf;
    --og-text-muted: #9a9a9a;
    --og-text-faint: #6e6e6e;
    /* The single sanctioned chromatic value: icon glyphs only */
    --og-icon-accent: #3b82f6;
    /* Focus + selection */
    --og-focus-ring: rgba(255, 255, 255, 0.85);
    /* Spacing scale (4px base grid) */
    --og-space-unit: 1;
    --og-space-0: 0px;
    --og-space-1: calc(0.25rem * var(--og-space-unit));
    --og-space-2: calc(0.5rem * var(--og-space-unit));
    --og-space-3: calc(0.75rem * var(--og-space-unit));
    --og-space-4: calc(1rem * var(--og-space-unit));
    --og-space-5: calc(1.25rem * var(--og-space-unit));
    --og-space-6: calc(1.5rem * var(--og-space-unit));
    --og-space-8: calc(2rem * var(--og-space-unit));
    --og-space-10: calc(2.5rem * var(--og-space-unit));
    --og-space-12: calc(3rem * var(--og-space-unit));
    --og-space-16: calc(4rem * var(--og-space-unit));
    --og-space-20: calc(5rem * var(--og-space-unit));
    /* Type ramp */
    --og-font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    --og-font-mono: ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace;
    --og-text-xs: 0.75rem;
    --og-text-sm: 0.875rem;
    --og-text-base: 1rem;
    --og-text-lg: 1.125rem;
    --og-text-xl: 1.375rem;
    --og-text-2xl: 1.75rem;
    --og-text-3xl: 2.25rem;
    --og-leading-tight: 1.15;
    --og-leading-snug: 1.4;
    --og-leading-normal: 1.6;
    /* Radii */
    --og-radius-sm: 6px;
    --og-radius-md: 10px;
    --og-radius-lg: 14px;
    --og-radius-xl: 18px;
    --og-radius-2xl: 26px;
    --og-radius-pill: 999px;
    /* Elevation ladder (monochrome shadows only) */
    --og-elev-1: 0 1px 2px rgba(0, 0, 0, 0.5);
    --og-elev-2: 0 4px 12px -2px rgba(0, 0, 0, 0.6);
    --og-elev-3: 0 12px 28px -8px rgba(0, 0, 0, 0.75);
    --og-elev-4: 0 24px 60px -12px rgba(0, 0, 0, 0.9);
    --og-glass-inner-highlight: inset 0 1px 0 rgba(255, 255, 255, 0.12), inset 0 -1px 0 rgba(0, 0, 0, 0.45);
    /* Liquid glass material */
    --og-glass-blur: blur(18px) saturate(118%);
    --og-glass-blur-thin: blur(10px) saturate(110%);
    --og-glass-tint: rgba(255, 255, 255, 0.07);
    --og-glass-tint-strong: rgba(255, 255, 255, 0.16);
    --og-glass-border-top: rgba(255, 255, 255, 0.28);
    --og-glass-shadow: 0 18px 48px -18px rgba(0, 0, 0, 0.85);
    --og-glass-specular: 0.32;
    /* Motion */
    --og-dur-fast: 120ms;
    --og-dur-normal: 240ms;
    --og-dur-slow: 420ms;
    /* Layout */
    --og-gutter: clamp(1rem, 4vw, 2.5rem);
    --og-container-narrow: 640px;
    --og-container-mid: 860px;
    --og-container-wide: 1240px;
    /* Z-index ladder */
    --og-z-base: 0;
    --og-z-dropdown: 1000;
    --og-z-sticky: 1020;
    --og-z-fixed: 1030;
    --og-z-modal-backdrop: 1040;
    --og-z-modal: 1050;
    --og-z-popover: 1060;
    --og-z-tooltip: 1070;
  }
}

/* Token aliases kept for the legacy inline-variable migration path.
   They resolve THROUGH the tokens above — never restate a literal. */
@layer og.tokens.aliases {
  :root {
    --primary-red: var(--og-white);
    --primary-red-hover: var(--og-gray-8);
    --primary-red-light: var(--og-white);
    --primary-red-dark: var(--og-gray-7);
    --secondary-red: var(--og-gray-6);
    --accent-red: var(--og-gray-2);
    --pure-black: var(--og-black);
    --dark-black: var(--og-gray-0);
    --medium-black: var(--og-gray-1);
    --light-black: var(--og-gray-2);
    --border-black: var(--og-gray-3);
    --text-white: var(--og-white);
    --text-gray: var(--og-text-secondary);
    --text-muted: var(--og-text-muted);
    --text-dark: var(--og-text-faint);
    --glass-black: var(--og-surface-raised);
    --glass-red: var(--og-glass-tint);
    --shadow-sm: var(--og-elev-1);
    --shadow-md: var(--og-elev-2);
    --shadow-lg: var(--og-elev-3);
    --shadow-xl: var(--og-elev-4);
    --shadow-red: var(--og-elev-2);
    --border-radius-sm: var(--og-radius-sm);
    --border-radius-md: var(--og-radius-md);
    --border-radius-lg: var(--og-radius-lg);
    --border-radius-xl: var(--og-radius-xl);
    --border-radius-2xl: var(--og-radius-2xl);
    --transition-fast: var(--og-dur-fast) linear;
    --transition-normal: var(--og-dur-normal) linear;
    --transition-slow: var(--og-dur-slow) linear;
    --font-size-xs: var(--og-text-xs);
    --font-size-sm: var(--og-text-sm);
    --font-size-base: var(--og-text-base);
    --font-size-lg: var(--og-text-lg);
    --font-size-xl: var(--og-text-xl);
    --font-size-2xl: var(--og-text-2xl);
    --font-size-3xl: var(--og-text-3xl);
    --spacing-1: var(--og-space-1);
    --spacing-2: var(--og-space-2);
    --spacing-3: var(--og-space-3);
    --spacing-4: var(--og-space-4);
    --spacing-5: var(--og-space-5);
    --spacing-6: var(--og-space-6);
    --spacing-8: var(--og-space-8);
    --spacing-10: var(--og-space-10);
    --spacing-12: var(--og-space-12);
    --spacing-16: var(--og-space-16);
    --spacing-20: var(--og-space-20);
    --spacing-24: var(--og-space-20);
    --z-index-dropdown: var(--og-z-dropdown);
    --z-index-sticky: var(--og-z-sticky);
    --z-index-fixed: var(--og-z-fixed);
    --z-index-modal-backdrop: var(--og-z-modal-backdrop);
    --z-index-modal: var(--og-z-modal);
    --z-index-popover: var(--og-z-popover);
    --z-index-tooltip: var(--og-z-tooltip);
  }
}

/* Token documentation surface — used by the settings preview panel so
   designers can eyeball the ramp without opening devtools. */
@layer og.tokens.preview {
  .token-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(88px, 1fr)); gap: var(--og-space-2) }
  .token-chip { border-radius: var(--og-radius-md); border: 1px solid var(--og-hairline); padding-block: var(--og-space-4); text-align: center; font-size: var(--og-text-xs); color: var(--og-text-faint) }
  .token-chip--g0 { background: var(--og-gray-0) }
  .token-chip--g1 { background: var(--og-gray-1) }
  .token-chip--g2 { background: var(--og-gray-2) }
  .token-chip--g3 { background: var(--og-gray-3) }
  .token-chip--g4 { background: var(--og-gray-4) }
  .token-chip--g5 { background: var(--og-gray-5) }
  .token-chip--g6 { background: var(--og-gray-6) }
  .token-chip--g7 { background: var(--og-gray-7); color: var(--og-black) }
  .token-chip--g8 { background: var(--og-gray-8); color: var(--og-black) }
  .token-chip--white { background: var(--og-white); color: var(--og-black) }
  @media (forced-colors: active) { .token-chip { background: Canvas; color: CanvasText; border: 1px solid CanvasText } }
}
"""
