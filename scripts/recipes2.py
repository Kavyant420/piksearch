# -*- coding: utf-8 -*-
"""Second extended recipe pass per CSS file (focus/hover/disabled/responsive/
print/prefers-color-scheme states). Consumed by gen_css.py alongside EXT."""

EXT2 = {}

def _states(prefix, variants):
    """Generate focus-visible/hover/active/disabled state rules for a base."""
    rows = []
    for v in variants:
        rows.append(("%s:focus-visible" % v, "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"))
        rows.append(("%s:hover" % v, "color: var(--og-white)"))
        rows.append(("%s[aria-disabled='true']" % v, "opacity: 0.4; pointer-events: none"))
    return rows

FOCUS_SETS = {
".og-btn": ["filled", "tinted", "gray", "bordered", "plain", "glass"],
}

EXT2["03-typography.css"] = [
 ("@media (prefers-reduced-motion: reduce)", ".og-link { transition: none }"),
 ("@media (forced-colors: active)", ".og-mark { background: Highlight; color: HighlightText }"),
 ("@media (forced-colors: active)", ".og-kbd { border: 1px solid CanvasText; background: Canvas }"),
 ("@media print", ".og-caption, .og-overline { color: #333 }"),
 ("@media print", ".og-quote { border-inline-start-color: #000 }"),
 (".og-display--tight", "letter-spacing: -0.05em; line-height: 1.0"),
 (".og-headline--loose", "line-height: 1.3; letter-spacing: 0"),
 (".og-title + .og-subtitle", "margin-block-start: var(--og-space-1)"),
 (".og-body--lead", "font-size: var(--og-text-lg); color: var(--og-text-secondary); max-inline-size: 60ch"),
 (".og-caption--upper", "text-transform: uppercase; letter-spacing: 0.08em"),
 (".og-num--big", "font-size: var(--og-text-3xl); font-weight: 700"),
 (".og-link--quiet", "text-decoration: none"),
 (".og-link--quiet:hover", "text-decoration: underline"),
 (".og-kbd-row", "display: flex; gap: var(--og-space-1); align-items: center"),
 (".og-flow-x > * + *", "margin-inline-start: var(--og-space-3)"),
 (".og-measure-widget", "max-inline-size: 34ch"),
 (".og-datetime", "font-variant-numeric: tabular-nums lining-nums; color: var(--og-text-muted)"),
 (".og-url-path", "font-family: var(--og-font-mono); font-size: var(--og-text-xs); word-break: break-all; color: var(--og-text-faint)"),
 (".og-phonetic", "font-family: var(--og-font-mono); color: var(--og-gray-4)"),
 (".og-thin", "font-weight: 200"),
 (".og-heavy", "font-weight: 900"),
]

EXT2["04-layout-grid.css"] = [
 ("@media (prefers-reduced-motion: reduce)", ".og-sidebar { position: static }"),
 (".og-container--fluid", "inline-size: 100%; padding-inline: var(--og-gutter)"),
 (".og-grid--sidebar-flip", "grid-template-columns: 320px minmax(0, 1fr)"),
 (".og-stack--tight", "gap: var(--og-space-2)"),
 (".og-stack--loose", "gap: var(--og-space-6)"),
 (".og-row--wrap", "flex-wrap: wrap"),
 (".og-row--end", "justify-content: end"),
 (".og-divider-block", "block-size: 1px; background: var(--og-hairline)"),
 (".og-region-wide", "grid-column: 1 / -1"),
 (".og-baseline-grid", "background-image: linear-gradient(var(--og-black-200) 1px, transparent 1px); background-size: 100% 2rem"),
 (".og-center-narrow", "display: grid; place-items: center; max-inline-size: 560px; margin-inline: auto"),
 (".og-grid-hero", "display: grid; grid-template-columns: repeat(6, 1fr); gap: var(--og-space-4)"),
 (".og-grid-hero > :first-child", "grid-column: span 4; grid-row: span 2"),
 (".og-inset-flush", "margin-inline: calc(var(--og-gutter) * -1)"),
 (".og-scroll-shadow", "mask-image: linear-gradient(#000 90%, transparent)"),
]

EXT2["05-color-monochrome.css"] = [
 ("@media (prefers-color-scheme: light)", ".og-bg-deep { background: var(--og-white-50) }"),
 ("@media (forced-colors: active)", ".og-vignette, .og-grain { display: none }"),
 (".og-tone-strip i:nth-child(2)", "background: var(--og-gray-4)"),
 (".og-tone-strip i:nth-child(3)", "background: var(--og-gray-6)"),
 (".og-tone-strip i:nth-child(4)", "background: var(--og-gray-8)"),
 (".og-inverse-zone", "background: var(--og-white); color: var(--og-black)"),
 (".og-inverse-zone a", "color: var(--og-black)"),
 (".og-veil-strong:hover", "background: var(--og-surface-strong)"),
 (".og-edge-glow", "box-shadow: 0 0 0 1px rgba(255,255,255,0.06), 0 0 32px rgba(255,255,255,0.05)"),
 (".og-no-chroma", "filter: grayscale(1)"),
 (".og-paper-ink", "color: var(--og-black); background: var(--og-white)"),
 (".og-ghost-white", "color: rgba(255,255,255,0.06)"),
 (".og-ink-shade-1", "color: var(--og-gray-8)"),
 (".og-ink-shade-2", "color: var(--og-gray-5)"),
 (".og-ink-shade-3", "color: var(--og-gray-2)"),
]

EXT2["06-navigation.css"] = [
 ("@media (prefers-reduced-motion: reduce)", ".og-drawer { transition: none }"),
 ("@media (forced-colors: active)", ".og-nav__link[aria-current='page'] { background: Highlight; color: HighlightText }"),
 (".og-nav__link:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"),
 (".og-header[data-hidden='true']", "translate: 0 -100%; transition: translate var(--og-dur-base) var(--og-ease-emphasize)"),
 (".og-header", "transition: translate var(--og-dur-base) var(--og-ease-emphasize)"),
 (".og-logo:hover .og-brand-dot", "scale: 1.4; transition: scale var(--og-dur-fast) var(--og-ease-spring)"),
 (".og-drawer[data-open='false']", "visibility: hidden"),
 (".og-menu-toggle[aria-expanded='true'] svg", "rotate: 90deg"),
 (".og-menu-toggle svg", "transition: rotate var(--og-dur-base) var(--og-ease-spring)"),
 (".og-breadcrumb [aria-current='page']", "color: var(--og-white)"),
 (".og-nav__badge", "font-size: 9px; background: var(--og-white); color: var(--og-black); border-radius: 6px; padding: 0 4px; font-weight: 800"),
]

def chip_states(base):
    out = []
    out.append(("%s:focus-visible" % base, "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"))
    out.append(("%s[aria-disabled='true']" % base, "opacity: 0.4; pointer-events: none"))
    return out

for _fname, _bases in {
 "07-search-core.css": [".og-engine-chip", ".og-history-item"],
 "08-results-feed.css": [".og-page-btn", ".og-sitelink"],
 "10-buttons-actions.css": [".og-btn", ".og-iconbtn", ".og-linkbtn"],
 "11-forms-inputs.css": [".og-radio-row", ".og-stepper button"],
 "14-dropdowns-menus.css": [".og-menu__item"],
 "15-tabs-switchers.css": [".og-tab", ".og-segmented button"],
 "20-settings-premium.css": [".og-set-row"],
 "22-image-gallery.css": [".og-thumb"],
 "29-tables-data.css": [".og-table th"],
}.items():
    rows = []
    for b in _bases:
        rows += chip_states(b)
    EXT2[_fname] = EXT2.get(_fname, []) + rows

EXT2.setdefault("12-modals-overlays.css", []) + [
 ("@media (prefers-reduced-motion: reduce)", ".og-modal__panel { transition: none; transform: none; opacity: 1 }"),
 ("@media (forced-colors: active)", ".og-modal__scrim { background: Canvas; opacity: 0.8 }"),
 (".og-modal__panel:focus-visible", "outline: 2px solid var(--og-focus-ring)"),
]

EXT2.setdefault("13-toasts-notifications.css", []) + [
 ("@media (prefers-reduced-motion: reduce)", ".og-toast, .og-toast__progress i { animation: none }"),
 ("@media (forced-colors: active)", ".og-toast { border: 1px solid CanvasText }"),
 (".og-toast__close:focus-visible", "outline: 2px solid var(--og-focus-ring)"),
]

EXT2.setdefault("16-slider-scrollbar.css", []) + [
 ("@media (prefers-reduced-motion: reduce)", ".og-marquee__track { animation: none }"),
 ("@media (forced-colors: active)", ".og-rail-knob { background: CanvasText }"),
 (".og-range input:focus-visible", "outline: none"),
]

EXT2.setdefault("17-tooltip-popover.css", []) + [
 ("@media (prefers-reduced-motion: reduce)", ".og-tip, .og-popover { transition: none; animation: none }"),
 ("@media (forced-colors: active)", ".og-tip { background: Canvas; border: 1px solid CanvasText; color: CanvasText }"),
]

EXT2.setdefault("18-loading-skeletons.css", []) + [
 ("@media (forced-colors: active)", ".og-boot-screen { background: Canvas }"),
 (".og-spinner--lg", "inline-size: 44px; block-size: 44px; border-width: 3px"),
]

EXT2.setdefault("19-empty-states.css", []) + [
 ("@media (prefers-reduced-motion: reduce)", ".og-offline { transition: none }"),
 ("@media (forced-colors: active)", ".og-offline { background: Canvas; color: CanvasText; border-block-end: 1px solid CanvasText }"),
]

EXT2.setdefault("21-hero-landing.css", []) + [
 ("@media (prefers-reduced-motion: reduce)", ".og-scroll-hint { animation: none }"),
 ("@media (orientation: landscape) and (max-height: 520px)", ".og-hero-stage { min-block-size: auto; padding-block: var(--og-space-7) }"),
]

EXT2.setdefault("23-video-player.css", []) + [
 ("@media (prefers-reduced-motion: reduce)", ".og-video:not(:hover) .og-video__controls { opacity: 1; transform: none }"),
 (".og-video__controls button:focus-visible", "outline: 2px solid var(--og-focus-ring)"),
]

EXT2.setdefault("24-audio-waveform.css", []) + [
 ("@media (prefers-reduced-motion: reduce)", ".og-audio.is-playing .og-wave i { animation: none }"),
 (".og-audio__play:focus-visible", "outline: 2px solid var(--og-focus-ring)"),
]

EXT2.setdefault("25-maps-directions.css", []) + [
 ("@media (prefers-reduced-motion: reduce)", ".og-pin { transition: none }"),
 (".og-place-row:hover", "background: var(--og-surface)"),
 (".og-map-zoom-btn:focus-visible", "outline: 2px solid var(--og-focus-ring)"),
]

EXT2.setdefault("26-calendar-events.css", []) + [
 (".og-cal-grid button:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: -2px"),
 ("@media (max-width: 480px)", ".og-countdown { gap: var(--og-space-2) }"),
]

EXT2.setdefault("27-translate-linguistic.css", []) + [
 ("@media (prefers-reduced-motion: reduce)", ".og-swap:hover svg { rotate: none }"),
 (".og-trans-pane textarea:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: -2px"),
]

EXT2.setdefault("28-code-snippets.css", []) + [
 (".og-copy-btn:focus-visible", "outline: 2px solid var(--og-focus-ring)"),
 ("@media (prefers-reduced-motion: reduce)", ".og-cursor-blink { animation: none }"),
]

EXT2.setdefault("30-footer-legal.css", []) + [
 ("@media (max-width: 640px)", ".og-footer__cols { grid-template-columns: 1fr 1fr }"),
 (".og-footer a:focus-visible", "outline: 2px solid var(--og-focus-ring)"),
]

EXT2.setdefault("31-dark-theme-tokens.css", []) + [
 ("@media (prefers-color-scheme: light)", "html[data-theme='auto'] body { background: var(--og-white) }"),
 ("@media (prefers-color-scheme: light)", "html[data-theme='auto'] ::selection { background: var(--og-black); color: var(--og-white) }"),
]

EXT2.setdefault("32-responsive-fluid.css", []) + [
 ("@media (max-width: 480px)", ".og-pillnav { font-size: var(--og-text-xs) }"),
 ("@media (min-width: 769px)", ".og-mobile-only { display: none !important }"),
 ("@media (max-width: 768px)", ".og-desktop-only { display: none !important }"),
]

EXT2.setdefault("33-motion-system.css", []) + [
 ("@media (prefers-reduced-transparency: reduce)", ".og-parallax { transform: none !important }"),
 ("@media (dynamic-range: high)", ".og-glow-pulse { animation-name: og-glow-hdr }"),
 ("@keyframes og-glow-hdr", "from { box-shadow: 0 0 0 rgba(255,255,255,0) } to { box-shadow: 0 0 40px rgba(255,255,255,0.2) }"),
]

EXT2.setdefault("34-forced-colors-high-contrast.css", []) + [
 ("@media (forced-colors: active)", ".og-priv-badge { border-color: CanvasText; color: CanvasText }"),
 ("@media (forced-colors: active)", ".og-query-token { border-color: CanvasText }"),
 ("@media (forced-colors: active)", ".og-shortcut-row { border-block-end-color: CanvasText }"),
 ("@media (forced-colors: active)", ".og-storage-bar { border: 1px solid CanvasText }"),
 ("@media (forced-colors: active)", ".og-confidence-bar { border: 1px solid CanvasText }"),
]

EXT2.setdefault("35-keyboard-a11y.css", []) + [
 (".og-shortcut-row kbd", "font-family: var(--og-font-mono)"),
 (".og-landmark-outline:focus-within", "outline-color: var(--og-focus-ring)"),
 ("@media (forced-colors: active)", ".og-required::after { color: CanvasText }"),
]

EXT2.setdefault("36-print-export.css", []) + [
 ("@media print", ".og-metal-text { -webkit-background-clip: unset; background-clip: unset; color: #000 }"),
 ("@media print", ".og-offline { display: none !important }"),
 ("@media print", "a[target='_blank']::after { content: ' ↗' }"),
]

EXT2.setdefault("37-webgl-canvas.css", []) + [
 ("@media (prefers-reduced-motion: reduce)", ".og-gl-host > canvas.og-gl { display: none }"),
 ("@media (forced-colors: active)", ".og-gl-host > canvas.og-gl { display: none }"),
 (".og-gl-host--dpr-cap", "--og-gl-max-dpr: 1.5"),
]

EXT2.setdefault("38-premium-details.css", []) + [
 ("@media (prefers-reduced-transparency: reduce)", ".og-spotlight, .og-edge-light::before { display: none }"),
 ("@media (forced-colors: active)", ".og-metal-text { color: CanvasText; background: none }"),
 (".og-notch-frame:focus-within", "box-shadow: 0 0 0 2px var(--og-focus-ring), 0 30px 60px -20px rgba(0,0,0,0.9)"),
]

EXT2.setdefault("39-icons-system.css", []) + [
 ("@media (forced-colors: active)", ".og-icon { stroke: CanvasText }"),
 ("@media (prefers-reduced-motion: reduce)", ".og-icon-spin { animation-duration: 4s }"),
 (".og-icon--status", "inline-size: 0.9em; block-size: 0.9em; vertical-align: 0.05em"),
]

EXT2.setdefault("40-integration-open-glass.css", []) + [
 ("@media (forced-colors: active)", ".ogui-btn { background: ButtonFace; color: ButtonText; border-color: ButtonText }"),
 (".ogui-btn:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"),
 (".ogui-toggle:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"),
 (".ogui-input:focus", "border-color: var(--og-white); outline: none"),
]

EXT2.setdefault("02-liquid-glass.css", []) + [
 ("@media (dynamic-range: high)", ".og-glass--chrome { box-shadow: var(--og-glass-shadow), inset 0 1px 0 rgba(255,255,255,0.5) }"),
 (".og-glass--interactive:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"),
 ("@supports not (inset: 0)", ".og-glass::before { top: 0; right: 0; bottom: 0; left: 0 }"),
]

EXT2.setdefault("09-widgets-cards.css", []) + [
 (".og-widget__head button:focus-visible", "outline: 2px solid var(--og-focus-ring)"),
 ("@media (max-width: 480px)", ".og-weather__days { grid-template-columns: repeat(3, 1fr) }"),
]
