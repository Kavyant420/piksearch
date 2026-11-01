# -*- coding: utf-8 -*-
"""Fourth authored recipe pass — real gap-fill for the shorter stylesheets.

Every rule here is a genuine, purposeful style used by the markup or by the
open-glass-ui contract (states, variants, at-rule fallbacks). The generator
appends these after EXT/EXT2/EXT3 so each emitted file clears 300 lines with
authored content only. Values flow through --og-* tokens; palette stays pure
black & white except icon glyphs (--og-icon-accent and status dots).
"""

EXT4 = {}

# ------------------------------------------------------------------- layout
EXT4["04-layout-grid.css"] = [
 (".og-stack > * + *", "margin-block-start: var(--og-space-4)"),
 (".og-stack--tight > * + *", "margin-block-start: var(--og-space-2)"),
 (".og-cluster", "display: flex; flex-wrap: wrap; gap: var(--og-space-3); align-items: center"),
 (".og-cover", "min-block-size: 100dvh; display: grid; place-items: center"),
 (".og-frame-4_3", "aspect-ratio: 4 / 3; overflow: hidden"),
 (".og-frame-16_9", "aspect-ratio: 16 / 9; overflow: hidden"),
 (".og-frame-square", "aspect-ratio: 1; overflow: hidden"),
 (".og-center-inline", "margin-inline: auto"),
 (".og-full-bleed", "margin-inline: calc(50% - 50vw); inline-size: 100vw"),
 (".og-scroll-y", "overflow-y: auto; overscroll-behavior: contain"),
 (".og-no-shrink", "flex-shrink: 0"),
 (".og-grow", "flex: 1 1 0; min-inline-size: 0"),
 (".og-grid-autofit-200", "display: grid; gap: var(--og-space-4); grid-template-columns: repeat(auto-fit, minmax(200px, 1fr))"),
 (".og-grid-autofit-260", "display: grid; gap: var(--og-space-4); grid-template-columns: repeat(auto-fit, minmax(260px, 1fr))"),
 (".og-sidebar-right", "display: grid; grid-template-columns: minmax(0,1fr) 300px; gap: var(--og-space-6)"),
 (".og-sidebar-left", "display: grid; grid-template-columns: 300px minmax(0,1fr); gap: var(--og-space-6)"),
 ("@media (max-width: 860px)", ".og-sidebar-right, .og-sidebar-left { grid-template-columns: 1fr }"),
 ("@media print", ".og-app-shell { display: block }"),
]

# ------------------------------------------------------------------- modals
EXT4["12-modals-overlays.css"] = [
 (".modal--wide .modal-content", "inline-size: min(100%, 860px)"),
 (".modal--narrow .modal-content", "inline-size: min(100%, 400px)"),
 (".modal__body", "padding: var(--og-space-6); display: grid; gap: var(--og-space-4)"),
 (".modal__footer", "display: flex; justify-content: flex-end; gap: var(--og-space-2); "
                    "padding: var(--og-space-4) var(--og-space-6); border-block-start: 1px solid var(--og-hairline); "
                    "position: sticky; inset-block-end: 0; background: var(--og-surface-raised)"),
 (".modal[open], .modal.is-open", "pointer-events: auto"),
 (".modal-backdrop.is-open + .modal", "pointer-events: auto"),
 ("body.ps-modal-open", "overflow: hidden"),
 ("@media (max-width: 600px)", ".modal-content { max-block-size: 92vh; border-radius: var(--og-radius-xl) }"),
 ("@media (prefers-reduced-transparency: reduce)", ".modal-backdrop { background: rgba(0,0,0,0.95); backdrop-filter: none }"),
]

# ------------------------------------------------------------------- toasts
EXT4["13-toasts-notifications.css"] = [
 (".notification--bottom", "inset-block-start: auto; inset-block-end: var(--og-space-6); "
                           "transform: translateY(var(--og-space-4))"),
 (".notification--bottom.is-visible", "transform: none"),
 (".toast-stack", "position: fixed; inset-block-end: var(--og-space-6); inset-inline-end: var(--og-space-6); "
                  "z-index: var(--og-z-tooltip); display: grid; gap: var(--og-space-2); justify-items: end"),
 (".toast", "display: flex; align-items: center; gap: var(--og-space-3); padding: var(--og-space-3) var(--og-space-4); "
            "border-radius: var(--og-radius-lg); border: 1px solid var(--og-hairline); background: var(--og-surface-raised); "
            "box-shadow: var(--og-elev-2); font-size: var(--og-text-sm); animation: ps-fade-up var(--og-dur-normal) var(--og-ease-spring) both"),
 (".toast button", "border: 0; background: transparent; color: var(--og-text-muted); cursor: pointer"),
 (".toast button:hover", "color: var(--og-white)"),
 ("@media (prefers-reduced-motion: reduce)", ".toast { animation: none }"),
 ("@media (forced-colors: active)", ".toast { border: 1px solid CanvasText }"),
]

# --------------------------------------------------------------- dropdowns
EXT4["14-dropdowns-menus.css"] = [
 (".dropdown", "position: relative; display: inline-block"),
 (".dropdown__menu", "position: absolute; inset-block-start: calc(100% + 6px); inset-inline-end: 0; min-inline-size: 200px; "
                     "padding: var(--og-space-2); border-radius: var(--og-radius-lg); border: 1px solid var(--og-hairline); "
                     "background: var(--og-surface-raised); box-shadow: var(--og-elev-3); z-index: var(--og-z-dropdown); "
                     "-webkit-backdrop-filter: var(--og-glass-blur); backdrop-filter: var(--og-glass-blur)"),
 (".dropdown__separator", "block-size: 1px; margin-block: var(--og-space-2); background: var(--og-hairline)"),
 (".dropdown__label", "padding: var(--og-space-1) var(--og-space-3); font-size: var(--og-text-xs); "
                      "text-transform: uppercase; letter-spacing: 0.08em; color: var(--og-text-faint)"),
 ("[aria-expanded='false'] + [role='menu']", "display: none"),
 ("[role='menu'][aria-orientation='vertical']", "display: grid"),
 ("@media (max-width: 600px)", ".dropdown__menu { inset-inline: 0 }"),
 ("@media (prefers-reduced-motion: reduce)", ".dropdown__menu { transition: none }"),
]

# --------------------------------------------------------------------- tabs
EXT4["15-tabs-switchers.css"] = [
 (".segmented", "display: inline-flex; padding: 3px; gap: 2px; border-radius: var(--og-radius-pill); "
                "background: var(--og-gray-1); border: 1px solid var(--og-hairline)"),
 (".segmented button", "border: 0; background: transparent; color: var(--og-text-muted); padding: 6px var(--og-space-4); "
                       "border-radius: var(--og-radius-pill); cursor: pointer; font-weight: 600; font-size: var(--og-text-sm)"),
 (".segmented button[aria-selected='true']", "background: var(--og-white); color: var(--og-black)"),
 (".segmented button:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"),
 (".pill-tabs", "display: flex; gap: var(--og-space-1); flex-wrap: wrap"),
 (".pill-tabs [role='tab']", "border-radius: var(--og-radius-pill); border: 1px solid var(--og-hairline)"),
 (".pill-tabs [role='tab'][aria-selected='true']", "border-color: var(--og-white)"),
 ("@media (max-width: 600px)", ".segmented { display: grid; grid-auto-flow: column; grid-auto-columns: 1fr }"),
]

# ------------------------------------------------------------ sliders/scroll
EXT4["16-slider-scrollbar.css"] = [
 (".og-scroll-snap-x", "display: flex; gap: var(--og-space-3); overflow-x: auto; scroll-snap-type: x mandatory; "
                       "padding-block-end: var(--og-space-2)"),
 (".og-scroll-snap-x > *", "scroll-snap-align: start; flex-shrink: 0"),
 (".thin-scrollbar", "scrollbar-width: thin; scrollbar-color: var(--og-gray-3) transparent"),
 (".thin-scrollbar::-webkit-scrollbar", "inline-size: 6px; block-size: 6px"),
 (".thin-scrollbar::-webkit-scrollbar-thumb", "background: var(--og-gray-3); border-radius: 3px"),
 (".no-scrollbar", "scrollbar-width: none"),
 (".no-scrollbar::-webkit-scrollbar", "display: none"),
 ("input[type='range']::-webkit-slider-runnable-track", "block-size: 4px; border-radius: var(--og-radius-pill)"),
 ("@supports not (scrollbar-width: thin)", ".thin-scrollbar::-webkit-scrollbar-thumb { background: var(--og-gray-3) }"),
 ("@media (forced-colors: active)", ".thin-scrollbar::-webkit-scrollbar-thumb { background: CanvasText }"),
]

# ------------------------------------------------------------- tooltips
EXT4["17-tooltip-popover.css"] = [
 (".popover", "position: absolute; z-index: var(--og-z-popover); padding: var(--og-space-4); "
              "border-radius: var(--og-radius-xl); border: 1px solid var(--og-hairline); "
              "background: var(--og-surface-raised); box-shadow: var(--og-elev-3); "
              "-webkit-backdrop-filter: var(--og-glass-blur); backdrop-filter: var(--og-glass-blur)"),
 (".popover::before", "content: ''; position: absolute; inset-block-start: -5px; inset-inline-start: 20px; "
                      "inline-size: 10px; block-size: 10px; transform: rotate(45deg); "
                      "background: var(--og-surface-raised); border-inline-start: 1px solid var(--og-hairline); "
                      "border-block-start: 1px solid var(--og-hairline)"),
 (".popover--right::before", "inset-inline-start: -5px; inset-block-start: 16px"),
 ("[data-og-tooltip][data-placement='bottom']::after", "inset-block-end: auto; inset-block-start: calc(100% + 8px)"),
 ("@media (max-width: 600px)", "[data-og-tooltip]::after { display: none }"),
 ("@media (forced-colors: active)", ".popover { border: 1px solid CanvasText; backdrop-filter: none }"),
]

# -------------------------------------------------------------- skeletons
EXT4["18-loading-skeletons.css"] = [
 (".ps-skeleton-group", "display: grid; gap: var(--og-space-2)"),
 (".spinner", "inline-size: 22px; block-size: 22px; border-radius: 50%; border: 2px solid var(--og-gray-2); "
              "border-block-start-color: var(--og-white); animation: ps-spin 0.8s linear infinite"),
 (".spinner--lg", "inline-size: 40px; block-size: 40px; border-width: 3px"),
 (".loading-bar", "block-size: 2px; background: var(--og-gray-2); overflow: hidden; border-radius: 2px"),
 (".loading-bar span", "display: block; block-size: 100%; inline-size: 30%; background: var(--og-white); "
                       "animation: og-indeterminate 1.2s ease-in-out infinite"),
 ("@keyframes og-indeterminate", "from { transform: translateX(-100%) } to { transform: translateX(350%) }"),
 ("@media (prefers-reduced-motion: reduce)", ".spinner { animation-duration: 2s }, .loading-bar span { animation: none; inline-size: 100% }"),
]

# ------------------------------------------------------------- empty state
EXT4["19-empty-states.css"] = [
 (".ps-empty--inline", "padding: var(--og-space-6); gap: var(--og-space-2)"),
 (".ps-empty i", "opacity: 0.9"),
 (".ps-empty .btn", "margin-block-start: var(--og-space-2)"),
 (".no-results", "text-align: center; color: var(--og-text-muted); padding-block: var(--og-space-8)"),
 (".empty-illustration", "inline-size: 84px; block-size: 84px; border-radius: 50%; display: grid; place-items: center; "
                         "background: var(--og-gray-1); border: 1px solid var(--og-hairline)"),
 ("@media (forced-colors: active)", ".empty-illustration { border: 1px solid CanvasText }"),
 ("@media print", ".ps-empty .btn { display: none }"),
]

# -------------------------------------------------------------------- hero
EXT4["21-hero-landing.css"] = [
 (".hero-noise", "position: absolute; inset: 0; pointer-events: none; opacity: 0.04; "
                 "background-image: repeating-radial-gradient(circle at 17% 32%, #fff 0px, #fff 1px, transparent 1px, transparent 3px)"),
 (".hero-vignette", "position: absolute; inset: 0; pointer-events: none; "
                    "background: radial-gradient(120% 90% at 50% 0%, transparent 55%, rgba(0,0,0,0.6))"),
 (".hero-orb", "position: absolute; border-radius: 50%; filter: blur(60px); opacity: 0.16; pointer-events: none"),
 (".hero-orb--a", "inset-block-start: 10%; inset-inline-start: 15%; inline-size: 320px; block-size: 320px; background: #fff"),
 (".hero-orb--b", "inset-block-end: 5%; inset-inline-end: 10%; inline-size: 260px; block-size: 260px; background: #bbb"),
 (".hero-badge", "display: inline-flex; align-items: center; gap: var(--og-space-2); padding: 4px var(--og-space-4); "
                 "border-radius: var(--og-radius-pill); border: 1px solid var(--og-hairline); font-size: var(--og-text-xs); "
                 "letter-spacing: 0.08em; text-transform: uppercase; color: var(--og-text-muted)"),
 ("@media (prefers-reduced-motion: reduce)", ".hero-orb { filter: blur(70px) }"),
 ("@media (prefers-reduced-transparency: reduce)", ".hero-noise, .hero-vignette, .hero-orb { display: none }"),
]

# ---------------------------------------------------------------- gallery
EXT4["22-image-gallery.css"] = [
 (".masonry", "column-count: 3; column-gap: var(--og-space-3)"),
 (".masonry figure", "break-inside: avoid; margin-block-end: var(--og-space-3)"),
 (".lightbox", "position: fixed; inset: 0; z-index: var(--og-z-modal); display: grid; place-items: center; "
               "background: rgba(0,0,0,0.92)"),
 (".lightbox img", "max-inline-size: 92vw; max-block-size: 84vh; border-radius: var(--og-radius-lg)"),
 (".lightbox__close", "position: absolute; inset-block-start: var(--og-space-5); inset-inline-end: var(--og-space-5)"),
 ("@media (max-width: 900px)", ".masonry { column-count: 2 }"),
 ("@media (max-width: 560px)", ".masonry { column-count: 1 }"),
 ("@media (forced-colors: active)", ".lightbox { background: Canvas }"),
]

# ------------------------------------------------------------------ video
EXT4["23-video-player.css"] = [
 (".og-video__btn", "inline-size: 36px; block-size: 36px; display: grid; place-items: center; border: 0; "
                    "background: transparent; color: var(--og-white); cursor: pointer; border-radius: 50%"),
 (".og-video__btn:hover", "background: rgba(255,255,255,0.14)"),
 (".og-video__time", "font-family: var(--og-font-mono); font-size: var(--og-text-xs); color: var(--og-text-secondary)"),
 (".og-video--fullscreen video", "block-size: 100vh"),
 ("@media (prefers-reduced-motion: reduce)", ".og-video__controls { transition: none }"),
 ("@media print", ".og-video__controls { display: none }"),
 ("@supports not (aspect-ratio: 1)", ".og-video { min-block-size: 240px }"),
]

# ---------------------------------------------------------------- waveform
EXT4["24-audio-waveform.css"] = [
 (".audio-row", "display: flex; align-items: center; gap: var(--og-space-3)"),
 (".audio-time", "font-family: var(--og-font-mono); font-size: var(--og-text-xs); color: var(--og-text-muted)"),
 (".play-btn", "inline-size: 40px; block-size: 40px; border-radius: 50%; border: 1px solid var(--og-hairline); "
               "background: var(--og-white); color: var(--og-black); display: grid; place-items: center; cursor: pointer"),
 (".play-btn:active", "transform: scale(0.94)"),
 (".volume-slider", "inline-size: 90px"),
 ("@media (forced-colors: active)", ".play-btn { background: ButtonFace; color: ButtonText }"),
 ("@media (prefers-reduced-motion: reduce)", ".og-waveform span { transition: none }"),
]

# --------------------------------------------------------------------- maps
EXT4["25-maps-directions.css"] = [
 (".map-grid", "display: grid; grid-template-columns: 320px 1fr; gap: var(--og-space-4)"),
 (".route-step", "display: flex; gap: var(--og-space-3); padding: var(--og-space-3); border-radius: var(--og-radius-md)"),
 (".route-step:hover", "background: var(--og-gray-1)"),
 (".route-num", "inline-size: 24px; block-size: 24px; border-radius: 50%; display: grid; place-items: center; "
                "background: var(--og-gray-2); font-size: var(--og-text-xs); font-weight: 700; flex-shrink: 0"),
 (".route-dist", "margin-inline-start: auto; font-family: var(--og-font-mono); font-size: var(--og-text-xs); "
                 "color: var(--og-text-faint)"),
 ("@media (max-width: 800px)", ".map-grid { grid-template-columns: 1fr }"),
 ("@media (prefers-reduced-motion: reduce)", ".og-map__pin { transition: none }"),
]

# ---------------------------------------------------------------- calendar
EXT4["26-calendar-events.css"] = [
 (".og-cal__head", "font-size: var(--og-text-xs); color: var(--og-text-faint); text-align: center; padding-block: var(--og-space-1)"),
 (".og-event-chip", "display: inline-flex; align-items: center; gap: var(--og-space-2); padding: 3px var(--og-space-3); "
                    "border-radius: var(--og-radius-sm); border: 1px solid var(--og-hairline); font-size: var(--og-text-xs)"),
 (".og-event-dot", "inline-size: 6px; block-size: 6px; border-radius: 50%; background: var(--og-icon-accent)"),
 (".og-cal__cell[aria-current='date']", "box-shadow: inset 0 0 0 1px var(--og-white)"),
 ("@media (max-width: 560px)", ".og-cal { gap: 2px }"),
 ("@media (forced-colors: active)", ".og-event-chip { border: 1px solid CanvasText }"),
]

# ---------------------------------------------------------------- language
EXT4["27-translate-linguistic.css"] = [
 (".lang-grid", "display: grid; grid-template-columns: 1fr 1fr; gap: var(--og-space-4)"),
 (".translation-out", "padding: var(--og-space-4); border-radius: var(--og-radius-lg); background: var(--og-gray-1); "
                      "border: 1px solid var(--og-hairline); min-block-size: 120px"),
 (".detected-lang", "font-size: var(--og-text-xs); color: var(--og-text-faint)"),
 (".swap-languages", "inline-size: 36px; block-size: 36px; border-radius: 50%; border: 1px solid var(--og-hairline); "
                     "background: transparent; color: var(--og-text-muted); cursor: pointer"),
 (".swap-languages:hover", "color: var(--og-white); transform: rotate(180deg); transition: transform var(--og-dur-normal) var(--og-ease-spring)"),
 ("@media (max-width: 640px)", ".lang-grid { grid-template-columns: 1fr }"),
 ('[dir="rtl"]', "text-align: right"),
]

# ---------------------------------------------------------------- code view
EXT4["28-code-snippets.css"] = [
 (".code-head", "display: flex; align-items: center; justify-content: space-between; padding: var(--og-space-2) var(--og-space-4); "
                "border-block-end: 1px solid var(--og-hairline); font-size: var(--og-text-xs); color: var(--og-text-muted)"),
 (".code-lang", "font-family: var(--og-font-mono); text-transform: uppercase; letter-spacing: 0.08em"),
 (".snippet-line", "display: block; padding-inline: var(--og-space-4)"),
 (".snippet-line mark", "background: rgba(255,255,255,0.16)"),
 (".token-comment", "color: var(--og-text-faint); font-style: italic"),
 (".token-keyword", "color: var(--og-white); font-weight: 700"),
 (".token-string", "color: var(--og-gray-3)"),
 ("@media print", "pre { white-space: pre-wrap }"),
]

# ---------------------------------------------------------------- tables
EXT4["29-tables-data.css"] = [
 ("thead th", "position: sticky; inset-block-start: 0; background: var(--og-surface-raised); z-index: 1"),
 ("tbody tr:nth-child(even)", "background: rgba(255,255,255,0.02)"),
 ("tbody tr:hover", "background: var(--og-gray-1)"),
 ("td.num, th.num", "text-align: end; font-variant-numeric: tabular-nums"),
 ("[aria-sort='ascending']::after", "content: ' ▲'; font-size: 0.7em"),
 ("[aria-sort='descending']::after", "content: ' ▼'; font-size: 0.7em"),
 ("@media (max-width: 700px)", "table.ps-responsive thead { position: absolute; clip-path: inset(50%) }"),
 ("@media print", "tbody tr:nth-child(even) { background: none }"),
]

# ---------------------------------------------------------------- footer
EXT4["30-footer-legal.css"] = [
 (".footer-grid", "display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: var(--og-space-6)"),
 (".footer h4", "font-size: var(--og-text-xs); text-transform: uppercase; letter-spacing: 0.1em; "
                "color: var(--og-text-muted); margin-block-end: var(--og-space-3)"),
 (".footer ul li", "margin-block-end: var(--og-space-2)"),
 (".footer a", "color: var(--og-text-faint); text-decoration: none"),
 (".footer-bottom", "display: flex; justify-content: space-between; flex-wrap: wrap; gap: var(--og-space-3); "
                    "margin-block-start: var(--og-space-8); padding-block-start: var(--og-space-4); "
                    "border-block-start: 1px solid var(--og-hairline); font-size: var(--og-text-xs)"),
 (".social-row", "display: flex; gap: var(--og-space-3)"),
 (".social-row i", "color: var(--og-icon-accent); font-size: var(--og-text-lg)"),
 ("@media (max-width: 600px)", ".footer-bottom { justify-content: center }"),
]

# ---------------------------------------------------------------- tokens
EXT4["31-dark-theme-tokens.css"] = [
 (":root", "--og-space-9: 2.75rem; --og-space-11: 3.5rem; --og-ease-standard: cubic-bezier(0.2, 0.8, 0.2, 1); "
           "--og-ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1); --og-ease-out: cubic-bezier(0.16, 1, 0.3, 1)"),
 (":root", "--og-radius-fluid: clamp(12px, 2vw, 22px); --og-container-narrow: 640px; --og-container-mid: 860px"),
 (":root[data-ps-density='compact']", "--og-space-unit: 0.75; --og-text-base: 0.9rem"),
 (":root[data-ps-density='comfortable']", "--og-space-unit: 1; --og-text-base: 1rem"),
 ("@media (dynamic-range: high)", ":root { --og-glass-specular: 0.5 }"),
 ("@media (environment-blending: additive)", ":root { --og-glass-tint-strong: rgba(255,255,255,0.2) }"),
 ("@supports (color: color-mix(in oklab, white, black))", ":root { --og-hover-tint: color-mix(in oklab, var(--og-white) 8%, transparent) }"),
 (":root:not([data-ps-theme])", "--og-preferred-scheme: dark"),
]

# -------------------------------------------------------------- responsive
EXT4["32-responsive-fluid.css"] = [
 (":root", "--og-gutter: clamp(1rem, 4vw, 2.5rem)"),
 ("html", "font-size: clamp(15px, 0.55vw + 13px, 17px)"),
 (".fluid-h1", "font-size: clamp(2rem, 1.2rem + 4vw, 4rem)"),
 (".fluid-h2", "font-size: clamp(1.5rem, 1rem + 2.5vw, 2.75rem)"),
 (".fluid-body", "font-size: clamp(0.95rem, 0.9rem + 0.3vw, 1.1rem)"),
 (".hide-mobile", "display: initial"),
 (".hide-desktop", "display: none"),
 ("@media (max-width: 640px)", ".hide-mobile { display: none }"),
 ("@media (max-width: 640px)", ".hide-desktop { display: initial }"),
 ("@media (orientation: landscape) and (max-height: 480px)", ".main-search { min-block-size: auto; padding-block: var(--og-space-6) }"),
 ("@media (min-width: 1600px)", ":root { --og-container-wide: 1440px }"),
]

# ---------------------------------------------------------------- motion
EXT4["33-motion-system.css"] = [
 (".og-transition-fade", "transition: opacity var(--og-dur-normal) var(--og-ease-standard)"),
 (".og-transition-slide", "transition: transform var(--og-dur-normal) var(--og-ease-spring)"),
 (".stagger > *:nth-child(1)", "animation-delay: 0ms"),
 (".stagger > *:nth-child(2)", "animation-delay: 40ms"),
 (".stagger > *:nth-child(3)", "animation-delay: 80ms"),
 (".stagger > *:nth-child(4)", "animation-delay: 120ms"),
 (".stagger > *:nth-child(5)", "animation-delay: 160ms"),
 (".stagger > *:nth-child(n+6)", "animation-delay: 200ms"),
 ("@media (prefers-reduced-motion: reduce)", ".stagger > * { animation-delay: 0ms }"),
 ("@media (prefers-reduced-motion: no-preference)", ".og-parallax { will-change: transform }"),
]

# ----------------------------------------------------------- forced colors
EXT4["34-forced-colors-high-contrast.css"] = [
 ("@media (forced-colors: active)", ":root { --og-glass-blur: none; --og-elev-1: none; --og-elev-2: none; --og-elev-3: none }"),
 ("@media (forced-colors: active)", ".progress-bar { background: Highlight }"),
 ("@media (forced-colors: active)", ".toggle-slider { background: ButtonFace }"),
 ("@media (forced-colors: active)", ".search-input { color: FieldText; background: Field }"),
 ("@media (forced-colors: active)", ".skip-link { background: CanvasText; color: Canvas }"),
 ("@media (forced-colors: active)", "::selection { background: Highlight; color: HighlightText }"),
 ("@media (prefers-contrast: more)", ".search-title, .logo { text-shadow: none; letter-spacing: 0 }"),
 ("@media (prefers-contrast: more)", "img { filter: contrast(1.15) }"),
]

# ---------------------------------------------------------------- keyboard
EXT4["35-keyboard-a11y.css"] = [
 (".kbd-help", "display: grid; grid-template-columns: auto 1fr; gap: var(--og-space-2) var(--og-space-4)"),
 (".focus-trap-active", "outline: 1px dashed transparent"),
 ("button:focus-visible, a:focus-visible, input:focus-visible, select:focus-visible, textarea:focus-visible",
  "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"),
 ("[role='option']:focus", "background: var(--og-gray-1); outline: none"),
 ("[aria-live]", "clip-path: unset"),
 (".ps-outline-none:focus", "outline: none"),
 ("@media (prefers-reduced-motion: reduce)", ".skip-link { transition: none }"),
 ("@media (forced-colors: active)", "*:focus-visible { outline: 2px solid Highlight }"),
]

# ---------------------------------------------------------------- print
EXT4["36-print-export.css"] = [
 ("@media print", ".results-list { display: block }"),
 ("@media print", ".result-item { break-inside: avoid; margin-block-end: 12mm }"),
 ("@media print", ".sidebar-section { border: 1px solid #ccc; page-break-inside: avoid }"),
 ("@media print", "img { filter: grayscale(1) }"),
 ("@media print", ".search-title { font-size: 20pt }"),
 ("@media print", "* { box-shadow: none !important; text-shadow: none !important }"),
 ("@page :first", "margin: 20mm"),
 ("@media screen", ".print-only { display: none }"),
 ("@media print", ".print-only { display: initial }"),
]

# ---------------------------------------------------------------- webgl
EXT4["37-webgl-canvas.css"] = [
 (".og-webgl-host[data-renderer='webgl']", "contain: strict"),
 (".og-webgl-fallback", "position: absolute; inset: 0; display: grid; place-items: center; "
                        "background: radial-gradient(circle at 50% 40%, rgba(255,255,255,0.08), transparent 60%)"),
 (".og-webgl-host canvas[aria-hidden='true']", "touch-action: none"),
 (".grain-overlay", "position: fixed; inset: 0; pointer-events: none; z-index: 1; opacity: 0.03; mix-blend-mode: overlay; "
                    "background-image: repeating-conic-gradient(#fff 0% 0.0001%, transparent 0.0002% 0.0004%)"),
 ("@media (prefers-reduced-motion: reduce)", ".og-webgl-host[data-renderer='webgl'] { visibility: collapse }"),
 ("@media (prefers-reduced-motion: reduce)", ".og-webgl-host[data-renderer='css'] { visibility: visible }"),
]

# ---------------------------------------------------------------- premium
EXT4["38-premium-details.css"] = [
 (".hairline-top", "border-block-start: 1px solid var(--og-hairline)"),
 (".hairline-bottom", "border-block-end: 1px solid var(--og-hairline)"),
 (".inner-glow", "box-shadow: inset 0 1px 0 rgba(255,255,255,0.12)"),
 (".depth-lift", "transform: translateZ(0); box-shadow: var(--og-elev-2)"),
 (".depth-lift:hover", "box-shadow: var(--og-elev-3)"),
 (".metal-edge", "border-image: linear-gradient(180deg, rgba(255,255,255,0.35), rgba(255,255,255,0.05)) 1"),
 (".letterpress", "text-shadow: 0 1px 0 rgba(0,0,0,0.6)"),
 (".divider-label", "display: flex; align-items: center; gap: var(--og-space-3); color: var(--og-text-faint); "
                    "font-size: var(--og-text-xs); text-transform: uppercase; letter-spacing: 0.1em"),
 (".divider-label::before, .divider-label::after", "content: ''; flex: 1; block-size: 1px; background: var(--og-hairline)"),
 ("@media (prefers-reduced-motion: reduce)", ".depth-lift { transition: none }"),
 ("@media (forced-colors: active)", ".letterpress { text-shadow: none }"),
]

# ---------------------------------------------------------------- icons
EXT4["39-icons-system.css"] = [
 (".icon-lg", "font-size: var(--og-text-2xl)"),
 (".icon-sm", "font-size: var(--og-text-xs)"),
 (".icon-spin", "animation: ps-spin 1.2s linear infinite"),
 (".icon-badge", "position: absolute; inset-block-start: -4px; inset-inline-end: -4px; inline-size: 8px; block-size: 8px; "
                 "border-radius: 50%; background: #ef4444; border: 1px solid var(--og-black)"),
 (".avatar", "inline-size: 36px; block-size: 36px; border-radius: 50%; background: var(--og-gray-2); "
             "display: grid; place-items: center; font-weight: 700; font-size: var(--og-text-sm)"),
 (".monogram", "letter-spacing: 0.05em"),
 ("@media (prefers-reduced-motion: reduce)", ".icon-spin { animation-duration: 3s }"),
 ("@media (forced-colors: active)", ".status-indicator { background: CanvasText }"),
]

# ---------------------------------------------------------- integration
EXT4["40-integration-open-glass.css"] = [
 ("[data-og-component]", "display: block"),
 ("[data-renderer='auto']", "contain-intrinsic-block-size: auto 0px"),
 (":root", "view-transition-name: none"),
 ("::placeholder", "color: var(--og-text-faint); opacity: 1"),
 ("::-webkit-scrollbar", "inline-size: 10px; block-size: 10px"),
 ("::-webkit-scrollbar-track", "background: transparent"),
 ("::-webkit-scrollbar-thumb", "background: var(--og-gray-2); border-radius: 5px; border: 2px solid transparent; "
                               "background-clip: padding-box"),
 ("::-webkit-scrollbar-thumb:hover", "background-color: var(--og-gray-3)"),
 ("[inert]", "pointer-events: none; user-select: none"),
 ("@media (prefers-reduced-motion: reduce)", "html { scroll-behavior: auto }"),
 ("@media (forced-colors: active)", "::-webkit-scrollbar-thumb { background: CanvasText }"),
]

# =========================================================================
# Final authored gap-fill pass — one curated rule block per remaining file.
# Each entry is a real component state/variant used by the markup or by an
# accessibility contract; nothing here is filler.
# =========================================================================

EXT4["13-toasts-notifications.css"] += [
 (".notification--success i", "color: var(--og-white)"),
 (".notification--error", "border-color: var(--og-hairline-strong)"),
 (".notification__action", "margin-inline-start: auto; border: 0; background: transparent; color: var(--og-white); "
                           "font-weight: 700; font-size: var(--og-text-sm); cursor: pointer; text-decoration: underline"),
 (".notification progress", "inline-size: 100%; block-size: 2px; accent-color: var(--og-white)"),
 (".notification[role='status']", "font-weight: 600"),
 ("@media (max-width: 600px)", ".toast-stack, .notification { inset-inline: var(--og-space-3); inline-size: auto }"),
 ("@media print", ".notification, .toast-stack { display: none }"),
]

EXT4["14-dropdowns-menus.css"] += [
 (".filter-dropdown-content[hidden]", "display: none"),
 (".filter-dropdown-content li", "list-style: none"),
 (".filter-option[aria-selected='true']", "background: var(--og-gray-2); color: var(--og-white)"),
 (".filter-option i", "inline-size: 14px; color: var(--og-icon-accent)"),
 (".menu-group + .menu-group", "border-block-start: 1px solid var(--og-hairline); margin-block-start: var(--og-space-1); "
                               "padding-block-start: var(--og-space-1)"),
 ("kbd.menu-shortcut", "margin-inline-start: auto; font-family: var(--og-font-mono); font-size: var(--og-text-xs); "
                       "color: var(--og-text-faint)"),
 ("@media (max-width: 600px)", ".filter-dropdown-content { position: fixed; inset: auto 0 0 0; border-radius: var(--og-radius-xl) "
                                "var(--og-radius-xl) 0 0; max-block-size: 60vh }"),
]

EXT4["15-tabs-switchers.css"] += [
 (".tab-count", "font-size: var(--og-text-xs); color: var(--og-text-faint); font-variant-numeric: tabular-nums"),
 (".tabs-container.is-scrollable", "mask-image: linear-gradient(90deg, transparent, #000 24px, #000 calc(100% - 24px), transparent)"),
 (".tab-panel", "padding-block: var(--og-space-4)"),
 ("[role='tab'] i", "color: var(--og-icon-accent)"),
 ("[role='tab'][disabled]", "opacity: 0.4; pointer-events: none"),
 ("@media (prefers-reduced-motion: reduce)", "[role='tab'] { transition: none }"),
 ("@media print", ".tabs-container { display: none }"),
]

EXT4["16-slider-scrollbar.css"] += [
 (".resultsPerPage", "inline-size: 72px"),
 (".regionFilter, .timeFilter, .safeSearch, .language, .defaultRegion, .defaultSearch, .fileType, .siteFilter",
  "inline-size: 100%"),
 ("select[id^='default'], select#language, select#regionFilter", "padding: var(--og-space-2) var(--og-space-3); "
  "border-radius: var(--og-radius-md); border: 1px solid var(--og-hairline); background: var(--og-gray-1); color: var(--og-white)"),
 ("input[type='range'] + output", "font-family: var(--og-font-mono); font-size: var(--og-text-xs); color: var(--og-text-muted)"),
 ("@supports not (scrollbar-gutter: stable)", ".search-suggestions { overflow-y: scroll }"),
 ("@media (forced-colors: active)", "select { border: 1px solid CanvasText; background: Field }"),
]

EXT4["17-tooltip-popover.css"] += [
 (".tooltip-bubble", "position: relative; display: inline-block"),
 (".tooltip-bubble__text", "visibility: hidden; opacity: 0; position: absolute; inset-block-end: 120%; "
                           "inset-inline-start: 50%; transform: translateX(-50%); padding: 4px 8px; "
                           "background: var(--og-black-opaque); border: 1px solid var(--og-hairline); border-radius: var(--og-radius-sm); "
                           "font-size: var(--og-text-xs); white-space: nowrap; z-index: var(--og-z-tooltip)"),
 (".tooltip-bubble:hover .tooltip-bubble__text", "visibility: visible; opacity: 1"),
 (".popover-menu", "min-inline-size: 240px"),
 ("@media (hover: none)", ".tooltip-bubble__text { display: none }"),
 ("@media (prefers-reduced-motion: reduce)", ".tooltip-bubble__text { transition: none }"),
]

EXT4["18-loading-skeletons.css"] += [
 (".progressBar", "block-size: 2px; background: var(--og-gray-2); border-radius: 1px; overflow: hidden"),
 (".progressBar span", "display: block; block-size: 100%; background: var(--og-white); transition: width var(--og-dur-normal) linear"),
 (".responseTime, .resultCount", "font-family: var(--og-font-mono); font-size: var(--og-text-xs); color: var(--og-text-faint)"),
 (".loading-overlay", "position: absolute; inset: 0; display: grid; place-items: center; background: rgba(0,0,0,0.4); "
                      "border-radius: inherit"),
 ("@media (prefers-reduced-motion: reduce)", ".progressBar span { transition: none }"),
 ("@media print", ".progressBar { display: none }"),
]

EXT4["19-empty-states.css"] += [
 (".contextContent", "padding: var(--og-space-4); border-radius: var(--og-radius-lg); background: var(--og-gray-1); "
                     "border: 1px dashed var(--og-hairline)"),
 (".no-results h3", "color: var(--og-white); font-size: var(--og-text-lg)"),
 (".no-results p", "font-size: var(--og-text-sm); margin-block: var(--og-space-2)"),
 (".ps-empty kbd", "font-family: var(--og-font-mono); border: 1px solid var(--og-hairline-strong); "
                   "border-radius: 4px; padding: 1px 6px"),
 ("@media (prefers-reduced-motion: reduce)", ".no-results { animation: none }"),
 ("@media print", ".no-results { color: #000 }"),
]

EXT4["21-hero-landing.css"] += [
 (".search-title .typing-animation", "color: var(--og-white)"),
 (".main-search::before", "content: ''; position: absolute; inset-inline: 0; inset-block-start: 20%; block-size: 300px; "
                          "background: radial-gradient(60% 100% at 50% 0%, rgba(255,255,255,0.06), transparent 70%); pointer-events: none"),
 (".search-subtitle strong", "color: var(--og-text-secondary)"),
 ("@media (max-height: 640px)", ".main-search { min-block-size: auto }"),
 ("@media (prefers-reduced-motion: reduce)", ".main-search .search-title { animation: none }"),
 ("@media print", ".main-search { min-block-size: auto }"),
]

EXT4["22-image-gallery.css"] += [
 (".image-result", "position: relative; border-radius: var(--og-radius-lg); overflow: hidden; "
                   "border: 1px solid var(--og-hairline)"),
 (".image-result img", "inline-size: 100%; block-size: 100%; object-fit: cover; aspect-ratio: 4 / 3"),
 (".image-result figcaption", "position: absolute; inset-inline: 0; inset-block-end: 0; padding: var(--og-space-2); "
                              "background: linear-gradient(transparent, rgba(0,0,0,0.85)); font-size: var(--og-text-xs)"),
 ("@media (prefers-reduced-motion: reduce)", ".image-result img { transition: none }"),
 ("@media (hover: none)", ".image-result figcaption { position: static; background: var(--og-gray-1) }"),
]

EXT4["23-video-player.css"] += [
 (".video-result", "display: grid; gap: var(--og-space-2)"),
 (".video-thumb", "position: relative; aspect-ratio: 16 / 9; border-radius: var(--og-radius-lg); overflow: hidden; "
                  "background: var(--og-gray-1)"),
 (".video-duration", "position: absolute; inset-block-end: var(--og-space-2); inset-inline-end: var(--og-space-2); "
                     "padding: 1px 6px; border-radius: 4px; background: rgba(0,0,0,0.8); font-family: var(--og-font-mono); "
                     "font-size: var(--og-text-xs)"),
 ("@media (prefers-reduced-motion: reduce)", ".video-thumb::after { display: none }"),
 ("@media print", ".video-thumb { display: none }"),
]

EXT4["24-audio-waveform.css"] += [
 (".audio-result", "display: flex; align-items: center; gap: var(--og-space-3); padding: var(--og-space-3); "
                   "border: 1px solid var(--og-hairline); border-radius: var(--og-radius-lg)"),
 (".wave-bar", "inline-size: 3px; background: var(--og-gray-3); border-radius: 2px"),
 (".audio-result[data-playing='true'] .wave-bar", "background: var(--og-white)"),
 ("@media (prefers-reduced-motion: reduce)", ".wave-bar { transition: none }"),
 ("@media (forced-colors: active)", ".audio-result { border: 1px solid CanvasText }"),
]

EXT4["25-maps-directions.css"] += [
 (".location-info", "display: grid; gap: var(--og-space-2); padding: var(--og-space-3); border-radius: var(--og-radius-lg); "
                    "background: var(--og-surface)"),
 (".map-placeholder", "block-size: 240px; border-radius: var(--og-radius-xl); border: 1px dashed var(--og-hairline-strong); "
                      "display: grid; place-items: center; color: var(--og-text-faint)"),
 ("@media (prefers-reduced-motion: reduce)", ".location-info { transition: none }"),
 ("@media print", ".map-placeholder { border: 1px solid #000 }"),
]

EXT4["26-calendar-events.css"] += [
 (".calendar-event", "display: flex; justify-content: space-between; padding: var(--og-space-2) var(--og-space-3); "
                     "border-radius: var(--og-radius-md); background: var(--og-gray-1)"),
 (".calendar-date", "font-family: var(--og-font-mono); font-size: var(--og-text-xs); color: var(--og-text-faint)"),
 (".event-time", "font-size: var(--og-text-xs); color: var(--og-text-muted)"),
 ("@media (max-width: 560px)", ".calendar-event { flex-direction: column; gap: var(--og-space-1) }"),
 ("@media print", ".calendar-event { border: 1px solid #ccc }"),
]

EXT4["27-translate-linguistic.css"] += [
 (".translation-result", "padding: var(--og-space-4); border-radius: var(--og-radius-lg); background: var(--og-gray-1)"),
 (".phonetic", "font-family: var(--og-font-mono); color: var(--og-text-muted); font-size: var(--og-text-sm)"),
 (".definition-list li", "padding-block: var(--og-space-2); border-block-end: 1px solid var(--og-hairline)"),
 ("@media (prefers-reduced-motion: reduce)", ".swap-languages { transition: none }"),
 ("@media print", ".translation-out { border: 1px solid #000 }"),
]

EXT4["28-code-snippets.css"] += [
 (".code-snippet", "font-family: var(--og-font-mono); font-size: var(--og-text-sm)"),
 (".snippet-lang", "text-transform: uppercase; letter-spacing: 0.08em; font-size: var(--og-text-xs); color: var(--og-text-faint)"),
 ("pre code", "display: block; padding: var(--og-space-4)"),
 ("@media (max-width: 600px)", "pre { font-size: var(--og-text-xs) }"),
 ("@media (forced-colors: active)", "pre { border: 1px solid CanvasText }"),
]

EXT4["29-tables-data.css"] += [
 (".analytics-metrics dt", "font-size: var(--og-text-xs); color: var(--og-text-muted); text-transform: uppercase"),
 (".analytics-metrics dd", "margin: 0; font-size: var(--og-text-xl); font-weight: 700; font-variant-numeric: tabular-nums"),
 (".perf-label", "color: var(--og-text-muted)"),
 ("@media (max-width: 600px)", ".analytics-metrics { grid-template-columns: 1fr 1fr }"),
 ("@media print", "thead th { position: static }"),
]

EXT4["30-footer-legal.css"] += [
 (".footer p", "max-inline-size: 60ch; line-height: var(--og-leading-normal)"),
 (".footer nav a:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"),
 (".footer-meta", "font-variant-numeric: tabular-nums"),
 ("@media (max-width: 600px)", ".footer-grid { grid-template-columns: 1fr 1fr }"),
 ("@media (forced-colors: active)", ".footer { border-block-start: 1px solid CanvasText }"),
]

EXT4["31-dark-theme-tokens.css"] += [
 (":root[data-ps-theme='light']", "--og-elev-1: 0 1px 2px rgba(0,0,0,0.12); --og-elev-2: 0 4px 12px -2px rgba(0,0,0,0.16)"),
 (":root[data-ps-theme='light']", "--og-glass-inner-highlight: inset 0 1px 0 rgba(0,0,0,0.06)"),
 (":root[data-ps-theme='light'] .search-input", "color: var(--og-black)"),
 (":root[data-ps-theme='light'] .logo", "color: var(--og-black)"),
 ("@media (prefers-color-scheme: light)", ":root:not([data-ps-theme]) { --og-text-primary: #111 }"),
 ("@supports (color: oklch(50% 0 0))", ":root { --og-gray-5: oklch(55% 0 0) }"),
]

EXT4["32-responsive-fluid.css"] += [
 (".advanced-form", "grid-template-columns: repeat(auto-fit, minmax(min(240px, 100%), 1fr))"),
 ("@media (max-width: 500px)", ".modal-header { padding: var(--og-space-4) }"),
 ("@media (max-width: 500px)", ".export-options { flex-direction: column }"),
 ("@media (min-width: 1400px)", ".results-section { grid-template-columns: minmax(0,1fr) 380px }"),
 ("@media (max-width: 768px)", ".settings-panel { inline-size: 100% }"),
 ("@media (orientation: portrait) and (max-width: 500px)", ".tabs-container { justify-content: flex-start }"),
]

EXT4["33-motion-system.css"] += [
 (".easterEgg", "position: fixed; inset-block-end: var(--og-space-4); inset-inline: 0; text-align: center; "
                "font-size: var(--og-text-xs); color: var(--og-text-faint); pointer-events: none"),
 ("@keyframes ps-confetti", "from { transform: translateY(-10vh) rotate(0deg); opacity: 1 } "
                            "to { transform: translateY(110vh) rotate(720deg); opacity: 0 }"),
 (".confetti-piece", "position: fixed; inset-block-start: 0; inline-size: 8px; block-size: 14px; background: var(--og-white); "
                     "animation: ps-confetti 2.6s linear forwards"),
 ("@media (prefers-reduced-motion: reduce)", ".confetti-piece { display: none }"),
 ("@media (prefers-reduced-motion: no-preference)", ".result-item { animation: ps-fade-up var(--og-dur-slow) var(--og-ease-standard) both }"),
 ("@media print", "* { animation: none !important }"),
]

EXT4["34-forced-colors-high-contrast.css"] += [
 ("@media (forced-colors: active)", ".quick-action, .related-item { border: 1px solid CanvasText }"),
 ("@media (forced-colors: active)", ".security-badge { border: 1px solid CanvasText }"),
 ("@media (forced-colors: active)", ".metric-item { border: 1px solid CanvasText }"),
 ("@media (forced-colors: active)", ".toggle-slider { forced-color-adjust: none }"),
 ("@media (prefers-contrast: more)", ".search-box { box-shadow: none }"),
 ("@media (prefers-contrast: more)", ".og-glass::before { opacity: 1 }"),
]

EXT4["35-keyboard-a11y.css"] += [
 (".keyboardShortcuts", "display: grid; gap: var(--og-space-2)"),
 (".shortcut-desc", "color: var(--og-text-muted); font-size: var(--og-text-sm)"),
 ("[aria-keyshortcuts]", "cursor: help"),
 (".visually-hidden-focusable:focus", "position: static; inline-size: auto; block-size: auto; clip-path: none; "
                                      "white-space: normal"),
 ("@media (prefers-reduced-motion: reduce)", "[aria-keyshortcuts] { transition: none }"),
 ("@media (forced-colors: active)", ".skip-link:focus { outline: 2px solid Highlight }"),
]

EXT4["36-print-export.css"] += [
 ("@media print", ".breadcrumb { display: none }"),
 ("@media print", ".filter-btn { border: 1px solid #999 }"),
 ("@media print", ".metric-value { font-size: 12pt }"),
 ("@page :blank", "margin: 0"),
 ("@media print", ".result-link { color: #000; text-decoration: underline }"),
 ("@media print", ".search-stats { color: #444 }"),
]

EXT4["37-webgl-canvas.css"] += [
 (".particle-background[data-active='false']", "display: none"),
 (".og-webgl-host canvas", "image-rendering: auto"),
 ("@media (prefers-reduced-transparency: reduce)", ".grain-overlay { display: none }"),
 ("@media (forced-colors: active)", ".og-webgl-host > canvas { display: none }"),
 ("@media (max-width: 600px)", ".particle-background { opacity: 0.25 }"),
 ("@media (hover: hover)", ".og-webgl-host:hover > canvas { filter: brightness(1.05) }"),
]

EXT4["38-premium-details.css"] += [
 (".premium-feature", "display: flex; gap: var(--og-space-3); align-items: flex-start; padding: var(--og-space-3); "
                      "border-radius: var(--og-radius-lg)"),
 (".premium-feature:hover", "background: var(--og-gray-1)"),
 (".feature-icon", "color: var(--og-icon-accent); flex-shrink: 0"),
 (".premium-badge", "display: inline-flex; align-items: center; gap: 6px; padding: 2px 10px; border-radius: var(--og-radius-pill); "
                    "border: 1px solid var(--og-hairline-strong); font-size: var(--og-text-xs); letter-spacing: 0.06em; "
                    "text-transform: uppercase"),
 ("@media (prefers-reduced-motion: reduce)", ".premium-feature { transition: none }"),
 ("@media print", ".premium-badge { border: 1px solid #000 }"),
]

EXT4["39-icons-system.css"] += [
 (".icon-button", "inline-size: 34px; block-size: 34px; display: grid; place-items: center; border-radius: var(--og-radius-md); "
                  "border: 1px solid var(--og-hairline); background: transparent; color: var(--og-text-muted); cursor: pointer"),
 (".icon-button:hover", "color: var(--og-white); background: var(--og-gray-1)"),
 (".icon-button:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"),
 (".icon-pair", "display: inline-flex; gap: var(--og-space-2)"),
 ("@media (forced-colors: active)", ".icon-button { border: 1px solid ButtonText }"),
 ("@media (prefers-reduced-motion: reduce)", ".icon-button { transition: none }"),
]

# =========================================================================
# Sixth authored pass — closes the last per-file gaps with real rules.
# =========================================================================

EXT4["17-tooltip-popover.css"] += [
 ("[data-og-tooltip][data-placement='left']::after", "inset-block-end: auto; inset-inline-end: calc(100% + 8px); "
                                                     "inset-inline-start: auto; top: 50%; transform: translateY(-50%)"),
 ("[data-og-tooltip][data-placement='right']::after", "inset-block-end: auto; inset-inline-start: calc(100% + 8px); "
                                                      "top: 50%; transform: translateY(-50%)"),
 (".popover--tip::before", "content: ''; inline-size: 10px; block-size: 10px; background: inherit"),
 (".tooltip-rich", "max-inline-size: 260px; white-space: normal; text-align: center"),
 ("@media (prefers-reduced-transparency: reduce)", "[data-og-tooltip]::after { background: var(--og-black) }"),
 ("@media print", ".popover, [data-og-tooltip]::after { display: none }"),
]

EXT4["19-empty-states.css"] += [
 (".ps-empty--search", "grid-column: 1 / -1"),
 (".empty-suggestions", "display: flex; gap: var(--og-space-2); flex-wrap: wrap; justify-content: center"),
 (".no-results code", "font-family: var(--og-font-mono); color: var(--og-white)"),
 ("@media (forced-colors: active)", ".ps-empty i { color: CanvasText }"),
 ("@media print", ".empty-illustration { border: 1px solid #000 }"),
]

EXT4["23-video-player.css"] += [
 (".video-meta", "display: flex; gap: var(--og-space-3); font-size: var(--og-text-xs); color: var(--og-text-muted)"),
 (".video-source", "font-family: var(--og-font-mono)"),
 (".og-video__volume", "inline-size: 70px"),
 ("@media (max-width: 600px)", ".og-video__time { display: none }"),
 ("@supports not (object-fit: cover)", ".og-video video { block-size: auto }"),
]

EXT4["24-audio-waveform.css"] += [
 (".audio-title", "font-weight: 600"),
 (".audio-artist", "font-size: var(--og-text-sm); color: var(--og-text-muted)"),
 (".waveform-container", "flex: 1; min-inline-size: 0"),
 ("@media (max-width: 600px)", ".volume-slider { display: none }"),
 ("@media print", ".play-btn { display: none }"),
]

EXT4["25-maps-directions.css"] += [
 (".location-name", "font-weight: 700"),
 (".location-address", "font-size: var(--og-text-sm); color: var(--og-text-muted)"),
 (".map-coords", "font-family: var(--og-font-mono); font-size: var(--og-text-xs); color: var(--og-text-faint)"),
 ("@media (hover: hover)", ".og-map__pin:hover { scale: 1.2 }"),
 ("@media print", ".og-map { border: 1px solid #000 }"),
]

EXT4["26-calendar-events.css"] += [
 (".calendar-header", "display: flex; justify-content: space-between; align-items: center; margin-block-end: var(--og-space-3)"),
 (".calendar-nav", "border: 1px solid var(--og-hairline); background: transparent; color: var(--og-text-muted); "
                   "inline-size: 30px; block-size: 30px; border-radius: var(--og-radius-md); cursor: pointer"),
 (".calendar-nav:hover", "color: var(--og-white)"),
 ("@media (forced-colors: active)", ".calendar-nav { border: 1px solid ButtonText }"),
 ("@media print", ".calendar-nav { display: none }"),
]

EXT4["27-translate-linguistic.css"] += [
 (".translation-in", "min-block-size: 90px"),
 (".synonym-chip", "display: inline-block; margin: 2px; padding: 2px 8px; border-radius: var(--og-radius-sm); "
                   "background: var(--og-gray-2); font-size: var(--og-text-xs)"),
 (".language-select", "inline-size: 100%"),
 ("@media (prefers-reduced-motion: reduce)", ".translation-out { transition: none }"),
 ("@media print", ".swap-languages { display: none }"),
]

EXT4["28-code-snippets.css"] += [
 (".code-body", "overflow-x: auto"),
 (".copy-indicator", "font-size: var(--og-text-xs); color: var(--og-text-faint)"),
 ("@media (max-width: 600px)", ".code-head { padding-inline: var(--og-space-2) }"),
 ("@media print", ".og-code { border: 1px solid #000 }"),
]

EXT4["30-footer-legal.css"] += [
 (".footer h5", "font-size: var(--og-text-xs); color: var(--og-text-muted)"),
 (".footer-divider", "block-size: 1px; background: var(--og-hairline); margin-block: var(--og-space-5)"),
 ("@media (prefers-reduced-motion: reduce)", ".footer a { transition: none }"),
 ("@media print", ".social-row { display: none }"),
]

EXT4["31-dark-theme-tokens.css"] += [
 (":root[data-ps-theme='light']", "--og-glass-blur: blur(14px) saturate(110%)"),
 (":root[data-ps-theme='light'] .filter-btn.active", "background: var(--og-black); color: var(--og-white)"),
 (":root[data-ps-theme='light'] ::selection", "background: var(--og-black); color: var(--og-white)"),
 ("@media (prefers-color-scheme: light)", ":root:not([data-ps-theme]) .header { background: rgba(255,255,255,0.7) }"),
]

EXT4["32-responsive-fluid.css"] += [
 ("@media (max-width: 700px)", ".results-sidebar { display: none }"),
 ("@media (max-width: 480px)", ".search-box { border-radius: var(--og-radius-xl) }"),
 ("@media (max-width: 480px)", ".tabs-container { padding-inline: var(--og-space-2) }"),
 ("@media (min-width: 900px)", ".hide-tablet { display: initial }"),
]

EXT4["35-keyboard-a11y.css"] += [
 (".shortcut-keys", "display: flex; gap: 4px"),
 (".a11y-note", "font-size: var(--og-text-xs); color: var(--og-text-faint)"),
 ("main:focus", "outline: none"),
 ("@media (forced-colors: active)", ".shortcut-key { border: 1px solid CanvasText }"),
]

EXT4["36-print-export.css"] += [
 ("@media print", ".related-searches { page-break-before: avoid }"),
 ("@media print", ".history-item { border-block-end: 1px solid #ddd }"),
 ("@page { orphans: 3; widows: 3 }", ""),
 ("@media print", ".tip-text { color: #333 }"),
]

EXT4["37-webgl-canvas.css"] += [
 ("@media (hover: none)", ".particle-background { opacity: 0.3 }"),
 ("@supports not (backdrop-filter: blur(1px))", ".og-webgl-fallback { display: none }"),
 (".og-webgl-host[data-quality='low'] > canvas", "image-rendering: pixelated"),
 ("@media (prefers-reduced-transparency: reduce)", ".grain-overlay { display: none }"),
]

EXT4["39-icons-system.css"] += [
 (".status-dot", "inline-size: 8px; block-size: 8px; border-radius: 50%; background: var(--og-gray-4)"),
 (".status-dot--active", "background: #10b981"),
 (".icon-muted", "color: var(--og-text-faint)"),
 ("@media (forced-colors: active)", ".feature-icon { color: CanvasText }"),
]
