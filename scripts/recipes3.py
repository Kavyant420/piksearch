# -*- coding: utf-8 -*-
"""Third extended recipe pass. Bridges the legacy markup classes that ship in
index.html (PikSearch) onto the open-glass-ui token system, then adds the
per-component state matrix (hover / focus-visible / active / disabled /
selected / reduced-motion / forced-colors / print).

Consumed by gen_css.py alongside EXT and EXT2. All values resolve through
--og-* custom properties so the palette contract (pure black & white except
icon glyphs) is enforced structurally, not per-rule.

Selectors beginning with @ are wrapper at-rules whose declaration string is a
nested rule (see gen_css.emit).
"""

EXT3 = {}

def _state_matrix(base, mods=None):
    """Standard interactive-state rows for one component base selector."""
    rows = []
    variants = [base] + ["%s--%s" % (base, m) for m in (mods or [])]
    for v in variants:
        rows.append(("%s:hover" % v,
                     "border-color: var(--og-hairline-strong); "
                     "box-shadow: var(--og-elev-1), var(--og-glass-inner-highlight)"))
        rows.append(("%s:focus-visible" % v,
                     "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"))
        rows.append(("%s:active" % v, "transform: scale(0.985)"))
        rows.append(("%s[aria-disabled='true']" % v,
                     "opacity: 0.4; pointer-events: none"))
    return rows


# ---------------------------------------------------------------- header/nav
EXT3["06-navigation.css"] = _state_matrix(".ps-nav-btn") + [
 (".header", "position: sticky; inset-block-start: 0; z-index: var(--og-z-sticky); "
             "padding-block: var(--og-space-3); "
             "background: linear-gradient(180deg, rgba(0,0,0,0.72), rgba(0,0,0,0.35)); "
             "-webkit-backdrop-filter: var(--og-glass-blur); backdrop-filter: var(--og-glass-blur); "
             "border-block-end: 1px solid var(--og-hairline)"),
 (".nav", "display: flex; align-items: center; justify-content: space-between; gap: var(--og-space-4); "
          "inline-size: min(100% - (var(--og-gutter) * 2), var(--og-container-wide)); margin-inline: auto"),
 (".logo-section", "display: flex; align-items: center; gap: var(--og-space-3)"),
 (".logo", "font-weight: 800; letter-spacing: -0.02em; color: var(--og-white); text-decoration: none; "
           "display: inline-flex; align-items: center; gap: var(--og-space-2); font-size: var(--og-text-lg)"),
 (".logo i", "color: var(--og-icon-accent)"),
 (".security-badge", "display: inline-flex; align-items: center; gap: var(--og-space-1); "
                     "padding: 2px var(--og-space-3); border-radius: var(--og-radius-pill); "
                     "border: 1px solid var(--og-hairline); font-size: var(--og-text-xs); "
                     "color: var(--og-text-muted); background: var(--og-surface)"),
 (".security-badge i", "color: var(--og-icon-accent)"),
 (".nav-controls", "display: flex; align-items: center; gap: var(--og-space-2)"),
 (".nav-btn", "inline-size: 40px; block-size: 40px; display: grid; place-items: center; "
              "border-radius: var(--og-radius-lg); border: 1px solid transparent; "
              "background: transparent; color: var(--og-text-secondary); cursor: pointer; "
              "transition: transform var(--og-dur-fast) var(--og-ease-standard), "
              "background var(--og-dur-fast) var(--og-ease-standard)"),
 (".nav-btn:hover", "background: var(--og-gray-1); color: var(--og-white)"),
 (".nav-btn:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"),
 (".nav-btn[aria-expanded='true']", "background: var(--og-gray-2); color: var(--og-white)"),
 (".breadcrumb", "display: flex; align-items: center; gap: var(--og-space-2); "
                 "font-size: var(--og-text-sm); color: var(--og-text-muted); margin-block-end: var(--og-space-4)"),
 (".breadcrumb-item", "color: var(--og-text-muted); text-decoration: none"),
 (".breadcrumb-item:hover", "color: var(--og-white); text-decoration: underline"),
 (".breadcrumb-separator i", "font-size: var(--og-text-xs); color: var(--og-gray-4)"),
 (".search-tabs", "position: sticky; inset-block-start: 64px; z-index: var(--og-z-sticky); "
                  "border-block-end: 1px solid var(--og-hairline); "
                  "background: linear-gradient(180deg, rgba(0,0,0,0.6), rgba(0,0,0,0.3)); "
                  "-webkit-backdrop-filter: var(--og-glass-blur-thin); backdrop-filter: var(--og-glass-blur-thin)"),
 (".tabs-container", "display: flex; gap: var(--og-space-1); overflow-x: auto; scrollbar-width: none; "
                     "inline-size: min(100% - (var(--og-gutter) * 2), var(--og-container-wide)); margin-inline: auto"),
 (".tabs-container::-webkit-scrollbar", "display: none"),
 (".tab", "flex-shrink: 0; display: inline-flex; align-items: center; gap: var(--og-space-2); "
          "padding: var(--og-space-3) var(--og-space-4); color: var(--og-text-muted); "
          "text-decoration: none; font-size: var(--og-text-sm); border-block-end: 2px solid transparent; "
          "white-space: nowrap; transition: color var(--og-dur-fast) var(--og-ease-standard)"),
 (".tab:hover", "color: var(--og-white)"),
 (".tab.active", "color: var(--og-white); border-block-end-color: var(--og-white)"),
 (".tab:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: -2px"),
 (".tab i", "color: var(--og-icon-accent)"),
 (".floating-action", "position: fixed; inset-block-end: var(--og-space-6); inset-inline-end: var(--og-space-6); "
                      "z-index: var(--og-z-fixed); inline-size: 48px; block-size: 48px; display: grid; "
                      "place-items: center; border-radius: var(--og-radius-pill); border: 1px solid var(--og-hairline); "
                      "background: var(--og-surface-raised); color: var(--og-white); cursor: pointer; "
                      "box-shadow: var(--og-elev-3); opacity: 0; visibility: hidden; "
                      "transform: translateY(var(--og-space-3)); "
                      "transition: opacity var(--og-dur-normal) var(--og-ease-standard), "
                      "transform var(--og-dur-normal) var(--og-ease-spring)"),
 (".floating-action.is-visible", "opacity: 1; visibility: visible; transform: none"),
 (".floating-action:hover", "transform: translateY(-2px)"),
 (".scroll-to-top", "position: fixed; inset-block-end: var(--og-space-6); inset-inline: 0; margin-inline: auto; "
                    "inline-size: 44px; block-size: 44px; z-index: var(--og-z-fixed)"),
]

# ------------------------------------------------------------- search core
EXT3["07-search-core.css"] = _state_matrix(".ps-quick-action") + [
 (".main-search", "display: grid; place-items: center; min-block-size: calc(100vh - 140px); "
                  "padding: var(--og-space-8) var(--og-gutter)"),
 (".search-container", "display: grid; justify-items: center; gap: var(--og-space-5); "
                       "inline-size: min(100%, var(--og-container-narrow))"),
 (".search-title", "font-size: clamp(2.5rem, 1.6rem + 4.4vw, 4.5rem); font-weight: 850; "
                   "letter-spacing: -0.045em; line-height: 1.02; color: var(--og-white); text-align: center"),
 (".search-subtitle", "font-size: var(--og-text-lg); color: var(--og-text-muted); text-align: center; "
                      "max-inline-size: 46ch"),
 (".search-box", "position: relative; inline-size: 100%; display: flex; flex-wrap: wrap; align-items: center; "
                 "gap: var(--og-space-2); padding: var(--og-space-3); border-radius: var(--og-radius-pill); "
                 "border: 1px solid var(--og-hairline); background: var(--og-surface-raised); "
                 "-webkit-backdrop-filter: var(--og-glass-blur); backdrop-filter: var(--og-glass-blur); "
                 "box-shadow: var(--og-elev-2), var(--og-glass-inner-highlight); "
                 "transition: box-shadow var(--og-dur-normal) var(--og-ease-standard), "
                 "border-color var(--og-dur-normal) var(--og-ease-standard)"),
 (".search-box:focus-within", "border-color: var(--og-hairline-strong); box-shadow: var(--og-elev-3), "
                              "0 0 0 4px rgba(255,255,255,0.06)"),
 (".search-input", "flex: 1 1 220px; min-inline-size: 0; border: 0; background: transparent; "
                   "color: var(--og-white); font-size: var(--og-text-lg); padding-inline: var(--og-space-3); "
                   "outline: none; font-family: inherit"),
 (".search-input::placeholder", "color: var(--og-text-faint)"),
 (".voice-search", "inline-size: 40px; block-size: 40px; border-radius: var(--og-radius-pill); border: 0; "
                   "background: transparent; color: var(--og-text-muted); cursor: pointer; display: grid; "
                   "place-items: center"),
 (".voice-search:hover", "color: var(--og-white); background: var(--og-gray-1)"),
 (".voice-search.is-listening", "color: var(--og-white); animation: ps-pulse 1.4s var(--og-ease-standard) infinite"),
 (".search-actions", "display: flex; gap: var(--og-space-2)"),
 (".search-suggestions", "position: absolute; inset-block-start: calc(100% + 8px); inset-inline: 0; z-index: var(--og-z-dropdown); "
                         "max-block-size: 320px; overflow-y: auto; border-radius: var(--og-radius-xl); "
                         "border: 1px solid var(--og-hairline); background: var(--og-surface-raised); "
                         "-webkit-backdrop-filter: var(--og-glass-blur); backdrop-filter: var(--og-glass-blur); "
                         "box-shadow: var(--og-elev-3); padding-block: var(--og-space-2); "
                         "list-style: none; margin: 0"),
 (".search-suggestions:empty", "display: none"),
 (".suggestion-item", "display: flex; align-items: center; gap: var(--og-space-3); "
                      "padding: var(--og-space-2) var(--og-space-4); cursor: pointer; color: var(--og-text-secondary)"),
 (".suggestion-item:hover, .suggestion-item.is-active", "background: var(--og-gray-1); color: var(--og-white)"),
 (".quick-actions", "display: flex; flex-wrap: wrap; gap: var(--og-space-2); justify-content: center"),
 (".quick-action", "display: inline-flex; align-items: center; gap: var(--og-space-2); padding: var(--og-space-2) var(--og-space-4); "
                   "border-radius: var(--og-radius-pill); border: 1px solid var(--og-hairline); "
                   "color: var(--og-text-secondary); text-decoration: none; font-size: var(--og-text-sm); "
                   "background: var(--og-surface); transition: all var(--og-dur-fast) var(--og-ease-standard)"),
 (".quick-action:hover", "color: var(--og-white); border-color: var(--og-hairline-strong); transform: translateY(-1px)"),
 (".quick-action i", "color: var(--og-icon-accent)"),
 (".advanced-search", "inline-size: min(100%, var(--og-container-mid)); margin-inline: auto; "
                      "padding: var(--og-space-6); border-radius: var(--og-radius-xl); "
                      "border: 1px solid var(--og-hairline); background: var(--og-surface)"),
 (".advanced-search-title", "font-size: var(--og-text-xl); font-weight: 700; margin-block-end: var(--og-space-4)"),
 (".advanced-form", "display: grid; gap: var(--og-space-4); grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))"),
 (".form-group", "display: grid; gap: var(--og-space-1)"),
 (".form-label", "font-size: var(--og-text-xs); text-transform: uppercase; letter-spacing: 0.08em; "
                 "color: var(--og-text-muted)"),
 (".form-input", "inline-size: 100%; padding: var(--og-space-2) var(--og-space-3); border-radius: var(--og-radius-md); "
                 "border: 1px solid var(--og-hairline); background: var(--og-gray-1); color: var(--og-white); "
                 "font: inherit; outline: none"),
 (".form-input:focus-visible", "border-color: var(--og-white); box-shadow: 0 0 0 3px rgba(255,255,255,0.12)"),
 (".operator-list", "display: grid; gap: var(--og-space-2)"),
 (".operator-item", "display: flex; gap: var(--og-space-3); align-items: baseline; padding: var(--og-space-2); "
                    "border-radius: var(--og-radius-md)"),
 (".operator-symbol", "font-family: var(--og-font-mono); color: var(--og-white); background: var(--og-gray-2); "
                      "padding: 1px 8px; border-radius: var(--og-radius-sm)"),
 (".search-operators", "display: grid; gap: var(--og-space-2)"),
 ("@media (prefers-reduced-motion: reduce)", ".voice-search.is-listening { animation: none }"),
 ("@media (forced-colors: active)", ".search-box { border: 1px solid CanvasText; -webkit-backdrop-filter: none; backdrop-filter: none }"),
]

# ------------------------------------------------------------ results feed
EXT3["08-results-feed.css"] = _state_matrix(".ps-result") + [
 (".results-section", "inline-size: min(100% - (var(--og-gutter) * 2), var(--og-container-wide)); "
                      "margin-inline: auto; display: grid; grid-template-columns: minmax(0, 1fr) 340px; "
                      "gap: var(--og-space-8); padding-block: var(--og-space-6); align-items: start"),
 (".results-main", "min-inline-size: 0"),
 (".results-meta", "display: flex; flex-wrap: wrap; gap: var(--og-space-4); align-items: center; "
                   "font-size: var(--og-text-sm); color: var(--og-text-muted); margin-block-end: var(--og-space-4)"),
 (".results-count", "font-variant-numeric: tabular-nums"),
 (".search-stats", "display: flex; gap: var(--og-space-4)"),
 (".search-time", "font-family: var(--og-font-mono); color: var(--og-text-faint)"),
 (".filter-controls", "display: flex; flex-wrap: wrap; gap: var(--og-space-2); margin-block-end: var(--og-space-5)"),
 (".filter-btn", "padding: 6px var(--og-space-4); border-radius: var(--og-radius-pill); "
                 "border: 1px solid var(--og-hairline); background: transparent; color: var(--og-text-muted); "
                 "font: inherit; font-size: var(--og-text-sm); cursor: pointer; "
                 "transition: all var(--og-dur-fast) var(--og-ease-standard)"),
 (".filter-btn:hover", "color: var(--og-white); border-color: var(--og-hairline-strong)"),
 (".filter-btn.active", "background: var(--og-white); color: var(--og-black); border-color: var(--og-white)"),
 (".filter-btn:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"),
 (".filter-dropdown", "position: relative"),
 (".filter-dropdown-content", "position: absolute; inset-block-start: calc(100% + 6px); inset-inline-start: 0; "
                              "min-inline-size: 180px; z-index: var(--og-z-dropdown); padding: var(--og-space-2); "
                              "border-radius: var(--og-radius-lg); border: 1px solid var(--og-hairline); "
                              "background: var(--og-surface-raised); box-shadow: var(--og-elev-3); "
                              "-webkit-backdrop-filter: var(--og-glass-blur); backdrop-filter: var(--og-glass-blur)"),
 (".filter-option", "padding: var(--og-space-2) var(--og-space-3); border-radius: var(--og-radius-sm); "
                    "cursor: pointer; font-size: var(--og-text-sm); color: var(--og-text-secondary)"),
 (".filter-option:hover", "background: var(--og-gray-1); color: var(--og-white)"),
 (".filter-option.selected", "color: var(--og-white); font-weight: 600"),
 (".results-list", "display: grid; gap: var(--og-space-6); list-style: none; margin: 0; padding: 0"),
 (".result-item", "display: grid; gap: var(--og-space-1)"),
 (".result-link", "color: var(--og-white); text-decoration: none; font-size: var(--og-text-xl); font-weight: 500"),
 (".result-link:hover", "text-decoration: underline; text-underline-offset: 3px"),
 (".result-url", "font-family: var(--og-font-mono); font-size: var(--og-text-xs); color: var(--og-text-faint)"),
 (".result-snippet", "color: var(--og-text-secondary); line-height: 1.6; max-inline-size: 65ch"),
 (".context-content", "color: var(--og-text-secondary); font-size: var(--og-text-sm)"),
 (".related-searches", "display: flex; flex-wrap: wrap; gap: var(--og-space-2); margin-block-start: var(--og-space-6)"),
 (".related-item", "display: inline-flex; align-items: center; gap: var(--og-space-2); padding: 6px var(--og-space-3); "
                   "border: 1px solid var(--og-hairline); border-radius: var(--og-radius-pill); "
                   "color: var(--og-text-secondary); text-decoration: none; font-size: var(--og-text-sm)"),
 (".related-item:hover", "color: var(--og-white); border-color: var(--og-hairline-strong)"),
 (".related-icon", "color: var(--og-icon-accent)"),
 (".related-text", "font-weight: 500"),
 ("@media (max-width: 1024px)", ".results-section { grid-template-columns: 1fr }"),
 ("@media (forced-colors: active)", ".filter-btn.active { background: Highlight; color: HighlightText }"),
]

# --------------------------------------------------------- widgets/sidebar
EXT3["09-widgets-cards.css"] = _state_matrix(".ps-widget") + [
 (".results-sidebar", "display: grid; gap: var(--og-space-5); position: sticky; inset-block-start: 120px"),
 (".sidebar-section", "padding: var(--og-space-5); border-radius: var(--og-radius-xl); "
                      "border: 1px solid var(--og-hairline); background: var(--og-surface); "
                      "box-shadow: var(--og-elev-1), var(--og-glass-inner-highlight)"),
 (".sidebar-title", "font-size: var(--og-text-sm); font-weight: 700; text-transform: uppercase; "
                    "letter-spacing: 0.08em; color: var(--og-text-muted); margin-block-end: var(--og-space-4); "
                    "display: flex; align-items: center; gap: var(--og-space-2)"),
 (".sidebar-title i", "color: var(--og-icon-accent)"),
 (".trending-searches", "display: grid; gap: var(--og-space-3)"),
 (".trending-item", "display: flex; align-items: center; gap: var(--og-space-3); cursor: pointer"),
 (".trending-item:hover .trending-query", "text-decoration: underline; text-underline-offset: 3px"),
 (".trending-rank", "font-size: var(--og-text-lg); font-weight: 800; color: var(--og-gray-4); "
                    "font-variant-numeric: tabular-nums; min-inline-size: 2ch"),
 (".trending-query", "font-size: var(--og-text-sm); color: var(--og-text-secondary)"),
 (".search-history", "display: grid; gap: var(--og-space-2)"),
 (".history-item", "display: flex; justify-content: space-between; align-items: baseline; gap: var(--og-space-3); "
                   "padding: var(--og-space-2); border-radius: var(--og-radius-md); cursor: pointer"),
 (".history-item:hover", "background: var(--og-gray-1)"),
 (".history-query", "font-size: var(--og-text-sm); color: var(--og-text-secondary)"),
 (".history-time", "font-size: var(--og-text-xs); color: var(--og-text-faint); white-space: nowrap"),
 (".search-tips", "display: grid; gap: var(--og-space-3)"),
 (".tip-item", "display: flex; gap: var(--og-space-3); align-items: flex-start"),
 (".tip-icon", "color: var(--og-icon-accent); margin-block-start: 2px"),
 (".tip-text", "font-size: var(--og-text-sm); color: var(--og-text-muted); line-height: 1.5"),
 (".search-location", "display: flex; align-items: center; gap: var(--og-space-2); font-size: var(--og-text-sm); "
                      "color: var(--og-text-muted)"),
 (".search-location i", "color: var(--og-icon-accent)"),
 ("@media (prefers-reduced-motion: reduce)", ".sidebar-section { transform: none !important }"),
]

# ---------------------------------------------------------------- buttons
EXT3["10-buttons-actions.css"] = _state_matrix(".btn", ["primary", "secondary", "ghost"]) + [
 (".btn", "display: inline-flex; align-items: center; justify-content: center; gap: var(--og-space-2); "
          "padding: var(--og-space-2) var(--og-space-5); border-radius: var(--og-radius-pill); "
          "border: 1px solid var(--og-hairline); background: var(--og-gray-1); color: var(--og-white); "
          "font: inherit; font-weight: 600; font-size: var(--og-text-sm); cursor: pointer; "
          "text-decoration: none; -webkit-tap-highlight-color: transparent; "
          "transition: transform var(--og-dur-fast) var(--og-ease-spring), "
          "background var(--og-dur-fast) var(--og-ease-standard), "
          "box-shadow var(--og-dur-fast) var(--og-ease-standard)"),
 (".btn:active", "transform: scale(0.97)"),
 (".btn-primary", "background: var(--og-white); color: var(--og-black); border-color: var(--og-white)"),
 (".btn-primary:hover", "background: var(--og-gray-3); box-shadow: var(--og-elev-2)"),
 (".btn-secondary", "background: transparent; color: var(--og-text-secondary)"),
 (".btn-secondary:hover", "color: var(--og-white); border-color: var(--og-hairline-strong)"),
 (".close-btn", "inline-size: 36px; block-size: 36px; display: grid; place-items: center; border: 0; "
                "background: transparent; color: var(--og-text-muted); cursor: pointer; "
                "border-radius: var(--og-radius-pill)"),
 (".close-btn:hover", "color: var(--og-white); background: var(--og-gray-1)"),
 (".close-btn:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"),
 (".export-btn", "display: inline-flex; align-items: center; gap: var(--og-space-2); padding: var(--og-space-2) var(--og-space-4); "
                 "border-radius: var(--og-radius-md); border: 1px solid var(--og-hairline); background: transparent; "
                 "color: var(--og-text-secondary); cursor: pointer; font: inherit; font-size: var(--og-text-sm)"),
 (".export-btn:hover", "color: var(--og-white); background: var(--og-gray-1)"),
 (".export-options", "display: flex; flex-wrap: wrap; gap: var(--og-space-2)"),
 ("@media (forced-colors: active)", ".btn-primary { background: ButtonText; color: ButtonFace }"),
]

# ------------------------------------------------------------------ modals
EXT3["12-modals-overlays.css"] = [
 (".modal-backdrop", "position: fixed; inset: 0; z-index: var(--og-z-modal-backdrop); background: rgba(0,0,0,0.72); "
                    "-webkit-backdrop-filter: blur(8px); backdrop-filter: blur(8px); opacity: 0; "
                    "visibility: hidden; transition: opacity var(--og-dur-normal) var(--og-ease-standard)"),
 (".modal-backdrop.is-open", "opacity: 1; visibility: visible"),
 (".modal", "position: fixed; inset: 0; z-index: var(--og-z-modal); display: grid; place-items: center; "
            "padding: var(--og-gutter); pointer-events: none"),
 (".modal-content", "inline-size: min(100%, 560px); max-block-size: 85vh; overflow-y: auto; pointer-events: auto; "
                    "border-radius: var(--og-radius-2xl); border: 1px solid var(--og-hairline); "
                    "background: var(--og-surface-raised); box-shadow: var(--og-elev-4), var(--og-glass-inner-highlight); "
                    "-webkit-backdrop-filter: var(--og-glass-blur); backdrop-filter: var(--og-glass-blur); "
                    "transform: translateY(var(--og-space-4)) scale(0.98); opacity: 0; "
                    "transition: transform var(--og-dur-normal) var(--og-ease-spring), "
                    "opacity var(--og-dur-normal) var(--og-ease-standard)"),
 (".modal.is-open .modal-content", "transform: none; opacity: 1"),
 (".modal-header", "display: flex; align-items: center; justify-content: space-between; gap: var(--og-space-3); "
                   "padding: var(--og-space-5) var(--og-space-6); border-block-end: 1px solid var(--og-hairline); "
                   "position: sticky; inset-block-start: 0; background: var(--og-surface-raised); z-index: 1"),
 (".modal-title", "font-size: var(--og-text-lg); font-weight: 700; margin: 0"),
 ("@media (prefers-reduced-motion: reduce)", ".modal-content, .modal-backdrop { transition: none }"),
 ("@media (forced-colors: active)", ".modal-content { border: 1px solid CanvasText; backdrop-filter: none }"),
]

# ---------------------------------------------------------------- toasts
EXT3["13-toasts-notifications.css"] = [
 (".notification", "position: fixed; inset-block-start: var(--og-space-6); inset-inline: 0; margin-inline: auto; "
                   "z-index: var(--og-z-tooltip); inline-size: min(92%, 420px); display: flex; align-items: center; "
                   "gap: var(--og-space-3); padding: var(--og-space-3) var(--og-space-5); "
                   "border-radius: var(--og-radius-pill); border: 1px solid var(--og-hairline); "
                   "background: var(--og-surface-raised); box-shadow: var(--og-elev-3); "
                   "-webkit-backdrop-filter: var(--og-glass-blur); backdrop-filter: var(--og-glass-blur); "
                   "opacity: 0; visibility: hidden; transform: translateY(calc(var(--og-space-4) * -1)); "
                   "transition: all var(--og-dur-normal) var(--og-ease-spring)"),
 (".notification.is-visible", "opacity: 1; visibility: visible; transform: none"),
 (".notification i", "color: var(--og-icon-accent)"),
 ("@media (prefers-reduced-transparency: reduce)", ".notification { background: var(--og-black); backdrop-filter: none }"),
 ("@media (prefers-reduced-motion: reduce)", ".notification { transition: opacity var(--og-dur-fast) linear }"),
]

# --------------------------------------------------------------- settings
EXT3["20-settings-premium.css"] = _state_matrix(".ps-setting") + [
 (".settings-panel", "position: fixed; inset-block: 0; inset-inline-end: 0; z-index: calc(var(--og-z-modal) + 1); "
                     "inline-size: min(420px, 100%); background: var(--og-surface-raised); "
                     "border-inline-start: 1px solid var(--og-hairline); box-shadow: var(--og-elev-4); "
                     "transform: translateX(100%); transition: transform var(--og-dur-slow) var(--og-ease-spring); "
                     "display: grid; grid-template-rows: auto 1fr; overflow-y: auto"),
 (".settings-panel.is-open", "transform: none"),
 (".settings-header", "display: flex; align-items: center; justify-content: space-between; "
                      "padding: var(--og-space-5) var(--og-space-6); border-block-end: 1px solid var(--og-hairline)"),
 (".settings-content", "padding: var(--og-space-6); display: grid; gap: var(--og-space-6)"),
 (".setting-group", "display: grid; gap: var(--og-space-3)"),
 (".setting-label", "font-size: var(--og-text-sm); font-weight: 600; color: var(--og-white)"),
 (".setting-control", "display: flex; align-items: center; justify-content: space-between; gap: var(--og-space-4)"),
 (".toggle-switch", "position: relative; inline-size: 48px; block-size: 28px; flex-shrink: 0; cursor: pointer"),
 (".toggle-switch input", "position: absolute; opacity: 0; inline-size: 100%; block-size: 100%; margin: 0; cursor: pointer"),
 (".toggle-slider", "position: absolute; inset: 0; border-radius: var(--og-radius-pill); background: var(--og-gray-2); "
                    "border: 1px solid var(--og-hairline); pointer-events: none; "
                    "transition: background var(--og-dur-fast) var(--og-ease-standard)"),
 (".toggle-slider::before", "content: ''; position: absolute; inset-block-start: 3px; inset-inline-start: 3px; "
                            "inline-size: 20px; block-size: 20px; border-radius: 50%; background: var(--og-white); "
                            "box-shadow: var(--og-elev-1); transition: transform var(--og-dur-normal) var(--og-ease-spring)"),
 (".toggle-switch input:checked + .toggle-slider", "background: var(--og-white)"),
 (".toggle-switch input:checked + .toggle-slider::before", "transform: translateX(20px); background: var(--og-black)"),
 (".toggle-switch input:focus-visible + .toggle-slider", "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"),
 ("@media (prefers-reduced-motion: reduce)", ".settings-panel, .toggle-slider::before { transition: none }"),
 ("@media (forced-colors: active)", ".toggle-slider { border: 1px solid CanvasText }"),
]

# ----------------------------------------------------------------- tokens
EXT3["31-dark-theme-tokens.css"] = [
 (":root[data-ps-theme='light']", "--og-black: #ffffff; --og-white: #0a0a0a; "
                                  "--og-text-primary: #0a0a0a; --og-text-secondary: #333333; "
                                  "--og-text-muted: #5c5c5c; --og-text-faint: #8a8a8a; "
                                  "--og-surface: rgba(0,0,0,0.04); --og-surface-raised: rgba(255,255,255,0.85); "
                                  "--og-hairline: rgba(0,0,0,0.12); --og-hairline-strong: rgba(0,0,0,0.28)"),
 (":root[data-ps-theme='light'] body", "background: linear-gradient(135deg, #ffffff, #f2f2f2 50%, #e8e8e8)"),
 (":root[data-ps-theme='light'] .header", "background: linear-gradient(180deg, rgba(255,255,255,0.8), rgba(255,255,255,0.4))"),
 (":root[data-ps-theme='light'] .btn-primary", "background: var(--og-black); color: var(--og-white)"),
 (":root[data-ps-theme='dark'] .og-glass", "--og-glass-tint: rgba(255,255,255,0.06)"),
 ("@media (prefers-color-scheme: light)", ":root:not([data-ps-theme]) { --og-surface: rgba(0,0,0,0.04) }"),
]

# ------------------------------------------------------------- responsive
EXT3["32-responsive-fluid.css"] = [
 ("@media (max-width: 1200px)", ".results-sidebar { display: none }"),
 ("@media (max-width: 900px)", ".results-section { grid-template-columns: 1fr; gap: var(--og-space-6) }"),
 ("@media (max-width: 768px)", ".search-actions { width: 100% }"),
 ("@media (max-width: 768px)", ".btn { flex: 1 }"),
 ("@media (max-width: 600px)", ".nav { padding-inline: var(--og-space-3) }"),
 ("@media (max-width: 600px)", ".search-title { font-size: clamp(2rem, 9vw, 3rem) }"),
 ("@media (max-width: 480px)", ".quick-actions { justify-content: flex-start; overflow-x: auto; flex-wrap: nowrap; "
                               "padding-block-end: var(--og-space-2); scrollbar-width: none }"),
 ("@media (hover: none) and (pointer: coarse)", ".nav-btn, .btn, .filter-btn { min-inline-size: 44px; min-block-size: 44px }"),
 ("@media (hover: none) and (pointer: coarse)", ".quick-action { scroll-snap-align: start }"),
 ("@supports not (backdrop-filter: blur(1px))", ".og-glass, .search-box, .header { background: var(--og-black-opaque) }"),
 ("@container (max-width: 400px)", ".sidebar-section { padding: var(--og-space-4) }"),
]

# ---------------------------------------------------------------- motion
EXT3["33-motion-system.css"] = [
 ("@keyframes ps-pulse", "0% { box-shadow: 0 0 0 0 rgba(255,255,255,0.35) } "
                        "70% { box-shadow: 0 0 0 12px rgba(255,255,255,0) } "
                        "100% { box-shadow: 0 0 0 0 rgba(255,255,255,0) }"),
 ("@keyframes ps-fade-up", "from { opacity: 0; transform: translateY(12px) } to { opacity: 1; transform: none }"),
 ("@keyframes ps-shimmer", "from { background-position: -200% 0 } to { background-position: 200% 0 }"),
 (".ps-enter", "animation: ps-fade-up var(--og-dur-slow) var(--og-ease-spring) both"),
 (".ps-enter-delay-1", "animation-delay: 60ms"),
 (".ps-enter-delay-2", "animation-delay: 120ms"),
 (".ps-enter-delay-3", "animation-delay: 180ms"),
 (".progress-bar", "position: fixed; inset-block-start: 0; inset-inline-start: 0; block-size: 2px; inline-size: 0; "
                   "z-index: calc(var(--og-z-tooltip) + 1); background: var(--og-white); "
                   "box-shadow: 0 0 12px rgba(255,255,255,0.6); transition: inline-size var(--og-dur-normal) var(--og-ease-standard)"),
 (".page-transition", "position: fixed; inset: 0; z-index: calc(var(--og-z-modal) + 10); display: grid; place-items: center; "
                      "background: var(--og-black-opaque); opacity: 0; visibility: hidden; pointer-events: none; "
                      "transition: opacity var(--og-dur-normal) var(--og-ease-standard)"),
 (".page-transition.is-active", "opacity: 1; visibility: visible; pointer-events: all"),
 (".loader", "inline-size: 44px; block-size: 44px; border-radius: 50%; border: 2px solid var(--og-gray-2); "
             "border-block-start-color: var(--og-white); animation: ps-spin 0.9s linear infinite"),
 ("@keyframes ps-spin", "to { transform: rotate(360deg) }"),
 ("@media (prefers-reduced-motion: reduce)", ".ps-enter, .loader { animation-duration: 1ms; animation-iteration-count: 1 }"),
 ("@media (prefers-reduced-motion: reduce)", "* { transition-duration: 1ms !important }"),
]

# ------------------------------------------------------------ keyboard/a11y
EXT3["35-keyboard-a11y.css"] = [
 (".keyboard-shortcuts", "display: grid; gap: var(--og-space-2)"),
 (".shortcut-item", "display: flex; justify-content: space-between; align-items: center; gap: var(--og-space-4); "
                    "padding: var(--og-space-2) 0; border-block-end: 1px dashed var(--og-hairline)"),
 (".shortcut-key", "font-family: var(--og-font-mono); font-size: var(--og-text-xs); padding: 2px 8px; "
                   "border: 1px solid var(--og-hairline-strong); border-radius: var(--og-radius-sm); "
                   "background: var(--og-gray-1); box-shadow: 0 1px 0 var(--og-hairline-strong)"),
 (".sr-only", "position: absolute; inline-size: 1px; block-size: 1px; margin: -1px; padding: 0; "
              "overflow: hidden; clip-path: inset(50%); white-space: nowrap; border: 0"),
 (".skip-link", "position: fixed; inset-block-start: -100px; inset-inline-start: var(--og-space-4); z-index: 9999; "
                "padding: var(--og-space-3) var(--og-space-5); background: var(--og-white); color: var(--og-black); "
                "border-radius: var(--og-radius-md); font-weight: 700; text-decoration: none; "
                "transition: inset-block-start var(--og-dur-fast) var(--og-ease-standard)"),
 (".skip-link:focus", "inset-block-start: var(--og-space-4)"),
 ("[tabindex='-1']:focus-visible", "outline: none"),
 ("@media (forced-colors: active)", ".shortcut-key { border: 1px solid CanvasText }"),
]

# ---------------------------------------------------------------- webgl
EXT3["37-webgl-canvas.css"] = [
 (".particle-background", "position: fixed; inset: 0; z-index: -1; pointer-events: none; opacity: 0.55"),
 (".particle-background canvas", "inline-size: 100%; block-size: 100%; display: block"),
 (".og-webgl-host", "position: relative; isolation: isolate; overflow: hidden; border-radius: inherit"),
 (".og-webgl-host > canvas", "position: absolute; inset: 0; inline-size: 100%; block-size: 100%"),
 (".og-webgl-host[data-renderer='css']", "background: var(--og-surface)"),
 ("@media (prefers-reduced-motion: reduce)", ".particle-background { display: none }"),
 ("@media (prefers-reduced-transparency: reduce)", ".og-webgl-host > canvas { opacity: 0.2 }"),
 ("@media (forced-colors: active)", ".particle-background { display: none }"),
]

# ---------------------------------------------------------- premium polish
EXT3["38-premium-details.css"] = [
 (".glow-effect", "position: relative"),
 (".glow-effect::after", "content: ''; position: absolute; inset: -1px; border-radius: inherit; pointer-events: none; "
                         "background: linear-gradient(120deg, transparent 30%, rgba(255,255,255,0.14) 50%, transparent 70%); "
                         "background-size: 200% 100%; animation: ps-shimmer 6s linear infinite; opacity: 0.6"),
 (".typing-animation", "display: inline-block; overflow: hidden; white-space: nowrap; "
                       "border-inline-end: 2px solid var(--og-white); "
                       "animation: ps-typing 2.4s steps(24) 1 both, ps-blink 1s step-end infinite"),
 ("@keyframes ps-typing", "from { inline-size: 0 } to { inline-size: 100% }"),
 ("@keyframes ps-blink", "50% { border-color: transparent }"),
 (".custom-scrollbar", "scrollbar-width: thin; scrollbar-color: var(--og-gray-3) transparent"),
 (".custom-scrollbar::-webkit-scrollbar", "inline-size: 8px"),
 (".custom-scrollbar::-webkit-scrollbar-thumb", "background: var(--og-gray-3); border-radius: var(--og-radius-pill)"),
 (".custom-scrollbar::-webkit-scrollbar-track", "background: transparent"),
 (".easter-egg", "position: fixed; inset-block-end: var(--og-space-4); inset-inline-start: var(--og-space-4); "
                 "font-size: var(--og-text-xs); color: var(--og-text-faint); opacity: 0.5; user-select: none"),
 ("@media (prefers-reduced-motion: reduce)", ".glow-effect::after, .typing-animation { animation: none; border: 0 }"),
]

# ---------------------------------------------------------------- icons
EXT3["39-icons-system.css"] = [
 (":root", "--og-icon-accent: #3b82f6"),
 ("i.fas, i.fab, i.far", "display: inline-flex; align-items: center; justify-content: center; "
                         "font-style: normal; line-height: 1"),
 ("i.fas[aria-hidden='true'], i.fab[aria-hidden='true']", "pointer-events: none"),
 (".status-indicator", "inline-size: 8px; block-size: 8px; border-radius: 50%; background: var(--og-gray-4); "
                       "display: inline-block; margin-inline-end: var(--og-space-2)"),
 (".status-indicator.online", "background: #10b981; box-shadow: 0 0 8px rgba(16,185,129,0.6)"),
 (".status-indicator.warn", "background: #f59e0b"),
 (".metric-value i, .perf-value i", "color: var(--og-icon-accent)"),
 ("@media (forced-colors: active)", "i.fas, i.fab { color: CanvasText }"),
]

# -------------------------------------------------------------- analytics
EXT3["29-tables-data.css"] = _state_matrix(".ps-metric") + [
 (".analytics-metrics", "display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: var(--og-space-3)"),
 (".metric-item", "padding: var(--og-space-3); border-radius: var(--og-radius-lg); border: 1px solid var(--og-hairline); "
                  "background: var(--og-surface)"),
 (".metric-label", "font-size: var(--og-text-xs); text-transform: uppercase; letter-spacing: 0.06em; color: var(--og-text-muted)"),
 (".metric-value", "font-size: var(--og-text-xl); font-weight: 700; font-variant-numeric: tabular-nums; color: var(--og-white)"),
 (".analytics-chart", "block-size: 160px; display: flex; align-items: flex-end; gap: 4px; margin-block-start: var(--og-space-4)"),
 (".analytics-chart span", "flex: 1; background: linear-gradient(180deg, var(--og-white), var(--og-gray-3)); "
                           "border-radius: var(--og-radius-sm) var(--og-radius-sm) 0 0; min-block-size: 4px; "
                           "transition: height var(--og-dur-slow) var(--og-ease-spring)"),
 (".search-performance", "display: grid; gap: var(--og-space-2)"),
 (".perf-item", "display: flex; justify-content: space-between; font-size: var(--og-text-sm); color: var(--og-text-muted)"),
 (".perf-value", "font-family: var(--og-font-mono); color: var(--og-white)"),
 (".search-export", "display: grid; gap: var(--og-space-3)"),
 (".search-analytics", "display: grid; gap: var(--og-space-4)"),
 (".security-status", "display: grid; gap: var(--og-space-2)"),
 (".status-item", "display: flex; justify-content: space-between; align-items: center; font-size: var(--og-text-sm)"),
 (".status-label", "color: var(--og-text-muted); display: flex; align-items: center; gap: var(--og-space-2)"),
 (".status-label i", "color: var(--og-icon-accent)"),
 ("@media (prefers-reduced-motion: reduce)", ".analytics-chart span { transition: none }"),
]

# ------------------------------------------------------- integration layer
EXT3["40-integration-open-glass.css"] = [
 ("html", "color-scheme: dark light"),
 ("body", "background: radial-gradient(1200px 600px at 50% -10%, rgba(255,255,255,0.05), transparent 60%), "
          "linear-gradient(160deg, #000 0%, #0a0a0a 40%, #000 100%); color: var(--og-text-primary); "
          "font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; "
          "min-block-size: 100vh; -webkit-font-smoothing: antialiased"),
 ("::selection", "background: var(--og-white); color: var(--og-black)"),
 ("a", "color: inherit"),
 ("button", "font-family: inherit"),
 ("img, video, canvas", "max-inline-size: 100%; block-size: auto"),
 ("svg", "fill: currentColor"),
 ("[hidden]", "display: none !important"),
 ("template", "display: none"),
 (":focus:not(:focus-visible)", "outline: none"),
 ("@supports (selector(:has(*)))", ".search-box:has(.search-input:focus) { border-color: var(--og-hairline-strong) }"),
 ("@media print", "body { background: #fff; color: #000 }"),
]

# ----------------------------------------------------- page-level bridges
EXT3["05-color-monochrome.css"] = [
 ("* , *::before, *::after", "box-sizing: border-box"),
 ("*", "transition-property: color, background-color, border-color, box-shadow, opacity, transform"),
 ("html", "scroll-behavior: smooth; -webkit-text-size-adjust: 100%"),
 ("h1, h2, h3, h4", "color: var(--og-white); margin: 0"),
 ("p", "margin: 0"),
 ("ul[class], ol[class]", "list-style: none; margin: 0; padding: 0"),
 ("input, button, textarea, select", "font: inherit; color: inherit"),
 ("img", "display: block"),
 ("body > div#app", "display: grid"),
 ("hr", "border: 0; block-size: 1px; background: var(--og-hairline); margin-block: var(--og-space-5)"),
 ("table", "border-collapse: collapse; inline-size: 100%"),
 ("th", "text-align: start; font-weight: 600; color: var(--og-text-muted)"),
 ("td, th", "padding: var(--og-space-2) var(--og-space-3); border-block-end: 1px solid var(--og-hairline)"),
 ("code, pre, kbd, samp", "font-family: var(--og-font-mono)"),
 ("pre", "overflow-x: auto; padding: var(--og-space-4); background: var(--og-gray-1); "
         "border-radius: var(--og-radius-lg); border: 1px solid var(--og-hairline)"),
 ("mark", "background: rgba(255,255,255,0.18); color: var(--og-white); padding: 0 2px; border-radius: 2px"),
 ("small", "font-size: var(--og-text-xs)"),
 ("strong, b", "font-weight: 700; color: var(--og-white)"),
 ("dialog::backdrop", "background: rgba(0,0,0,0.7); -webkit-backdrop-filter: blur(6px); backdrop-filter: blur(6px)"),
]

EXT3["11-forms-inputs.css"] = _state_matrix(".form-input") + [
 ("select.form-input", "appearance: none; background-image: linear-gradient(45deg, transparent 50%, var(--og-text-muted) 50%), "
                       "linear-gradient(135deg, var(--og-text-muted) 50%, transparent 50%); "
                       "background-position: calc(100% - 18px) 55%, calc(100% - 13px) 55%; "
                       "background-size: 5px 5px; background-repeat: no-repeat; padding-inline-end: var(--og-space-8)"),
 ("textarea.form-input", "min-block-size: 90px; resize: vertical"),
 ("input[type='search']::-webkit-search-cancel-button", "appearance: none"),
 ("input:-webkit-autofill", "box-shadow: 0 0 0 1000px var(--og-gray-1) inset; -webkit-text-fill-color: var(--og-white)"),
 ("label[for]", "cursor: pointer"),
 (".form-group:has(input:required):not(:has(input:optional)) .form-label::after", "content: ' *'; color: var(--og-white)"),
 ("@media (forced-colors: active)", ".form-input { border: 1px solid CanvasText }"),
]

EXT3["14-dropdowns-menus.css"] = _state_matrix(".filter-dropdown") + [
 ("[role='menu']", "min-inline-size: 200px"),
 ("[role='menuitem']", "display: flex; align-items: center; gap: var(--og-space-2); "
                       "padding: var(--og-space-2) var(--og-space-3); border-radius: var(--og-radius-sm); cursor: pointer"),
 ("[role='menuitem']:hover, [role='menuitem']:focus", "background: var(--og-gray-1); outline: none"),
 ("[aria-haspopup='true'][aria-expanded='true']", "background: var(--og-gray-2)"),
 ("@media (prefers-reduced-motion: reduce)", "[role='menu'] { transition: none }"),
]

EXT3["15-tabs-switchers.css"] = [
 ("[role='tablist']", "display: flex; gap: var(--og-space-1)"),
 ("[role='tab']", "padding: var(--og-space-2) var(--og-space-4); border-radius: var(--og-radius-md) "
                  "var(--og-radius-md) 0 0; color: var(--og-text-muted); cursor: pointer; border: 0; background: transparent"),
 ("[role='tab'][aria-selected='true']", "color: var(--og-white); background: var(--og-gray-1)"),
 ("[role='tab']:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: 2px"),
 ("[role='tabpanel']:focus", "outline: none"),
 ("[hidden][role='tabpanel']", "display: none"),
]

EXT3["16-slider-scrollbar.css"] = [
 ("input[type='range']", "appearance: none; inline-size: 100%; block-size: 4px; border-radius: var(--og-radius-pill); "
                         "background: var(--og-gray-2); outline: none"),
 ("input[type='range']::-webkit-slider-thumb", "appearance: none; inline-size: 18px; block-size: 18px; border-radius: 50%; "
                                               "background: var(--og-white); box-shadow: var(--og-elev-1); cursor: grab"),
 ("input[type='range']::-moz-range-thumb", "inline-size: 18px; block-size: 18px; border: 0; border-radius: 50%; "
                                           "background: var(--og-white)"),
 ("input[type='range']:focus-visible", "outline: 2px solid var(--og-focus-ring); outline-offset: 4px"),
 ("@media (forced-colors: active)", "input[type='range']::-webkit-slider-thumb { background: CanvasText }"),
]

EXT3["17-tooltip-popover.css"] = [
 ("[data-og-tooltip]", "position: relative"),
 ("[data-og-tooltip]::after", "content: attr(data-og-tooltip); position: absolute; inset-block-end: calc(100% + 8px); "
                              "inset-inline-start: 50%; transform: translateX(-50%) translateY(4px); "
                              "padding: 4px 10px; border-radius: var(--og-radius-sm); background: var(--og-black-opaque); "
                              "border: 1px solid var(--og-hairline); color: var(--og-white); font-size: var(--og-text-xs); "
                              "white-space: nowrap; opacity: 0; pointer-events: none; "
                              "transition: opacity var(--og-dur-fast) var(--og-ease-standard), "
                              "transform var(--og-dur-fast) var(--og-ease-spring); z-index: var(--og-z-tooltip)"),
 ("[data-og-tooltip]:hover::after, [data-og-tooltip]:focus-visible::after", "opacity: 1; transform: translateX(-50%)"),
 ("@media (prefers-reduced-motion: reduce)", "[data-og-tooltip]::after { transition: opacity var(--og-dur-fast) linear }"),
]

EXT3["18-loading-skeletons.css"] = [
 (".ps-skeleton", "position: relative; overflow: hidden; background: var(--og-gray-1); border-radius: var(--og-radius-md); "
                  "block-size: 14px"),
 (".ps-skeleton::after", "content: ''; position: absolute; inset: 0; "
                         "background: linear-gradient(90deg, transparent, rgba(255,255,255,0.07), transparent); "
                         "background-size: 200% 100%; animation: ps-shimmer 1.6s linear infinite"),
 (".ps-skeleton--title", "block-size: 22px; inline-size: 60%"),
 (".ps-skeleton--line", "block-size: 12px; inline-size: 100%"),
 (".ps-skeleton--thumb", "block-size: 84px; inline-size: 84px; border-radius: var(--og-radius-lg)"),
 ("@media (prefers-reduced-motion: reduce)", ".ps-skeleton::after { animation: none }"),
 ("@media (forced-colors: active)", ".ps-skeleton { border: 1px solid CanvasText }"),
]

EXT3["19-empty-states.css"] = [
 (".ps-empty", "display: grid; justify-items: center; gap: var(--og-space-3); padding: var(--og-space-10) var(--og-gutter); "
               "text-align: center; color: var(--og-text-muted)"),
 (".ps-empty i", "font-size: 2.5rem; color: var(--og-icon-accent); opacity: 0.8"),
 (".ps-empty h3", "font-size: var(--og-text-lg); color: var(--og-white)"),
 (".ps-empty p", "max-inline-size: 44ch; font-size: var(--og-text-sm)"),
 ("@media (forced-colors: active)", ".ps-empty i { color: CanvasText }"),
]

EXT3["21-hero-landing.css"] = [
 (".hero-shell", "display: grid; place-items: center; gap: var(--og-space-6); padding-block: var(--og-space-16)"),
 (".hero-title", "font-size: clamp(3rem, 2rem + 6vw, 6rem); font-weight: 900; letter-spacing: -0.05em; "
                 "line-height: 0.95; text-align: center; "
                 "background: linear-gradient(180deg, #fff 30%, rgba(255,255,255,0.55)); "
                 "-webkit-background-clip: text; background-clip: text; color: transparent"),
 (".hero-sub", "text-align: center; color: var(--og-text-muted); font-size: var(--og-text-lg)"),
 (".hero-cta-row", "display: flex; gap: var(--og-space-3); flex-wrap: wrap; justify-content: center"),
 ("@supports not (background-clip: text)", ".hero-title { color: var(--og-white); background: none }"),
 ("@media (forced-colors: active)", ".hero-title { color: CanvasText; background: none }"),
]

EXT3["22-image-gallery.css"] = [
 (".og-gallery", "display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: var(--og-space-3)"),
 (".og-gallery figure", "margin: 0; border-radius: var(--og-radius-lg); overflow: hidden; "
                        "border: 1px solid var(--og-hairline); background: var(--og-gray-1)"),
 (".og-gallery img", "inline-size: 100%; block-size: 100%; object-fit: cover; aspect-ratio: 4 / 3; "
                     "transition: transform var(--og-dur-slow) var(--og-ease-spring)"),
 (".og-gallery figure:hover img", "transform: scale(1.04)"),
 (".og-gallery figcaption", "padding: var(--og-space-2) var(--og-space-3); font-size: var(--og-text-xs); "
                            "color: var(--og-text-muted)"),
 ("@media (prefers-reduced-motion: reduce)", ".og-gallery img { transition: none }"),
]

EXT3["23-video-player.css"] = [
 (".og-video", "position: relative; border-radius: var(--og-radius-xl); overflow: hidden; background: var(--og-black-opaque)"),
 (".og-video video", "inline-size: 100%; display: block"),
 (".og-video__controls", "position: absolute; inset-inline: 0; inset-block-end: 0; display: flex; gap: var(--og-space-2); "
                         "align-items: center; padding: var(--og-space-3); "
                         "background: linear-gradient(transparent, rgba(0,0,0,0.8))"),
 (".og-video__progress", "flex: 1; block-size: 3px; border-radius: var(--og-radius-pill); background: rgba(255,255,255,0.25)"),
 (".og-video__progress span", "display: block; block-size: 100%; background: var(--og-white); border-radius: inherit"),
 ("@media (forced-colors: active)", ".og-video__controls { background: Canvas }"),
]

EXT3["24-audio-waveform.css"] = [
 (".og-waveform", "display: flex; align-items: center; gap: 2px; block-size: 48px"),
 (".og-waveform span", "inline-size: 3px; block-size: 20%; background: var(--og-gray-3); border-radius: 2px; "
                       "transition: height var(--og-dur-fast) linear"),
 (".og-waveform.is-playing span", "background: var(--og-white)"),
 (".og-wave__bar", "animation: og-wave-bounce 1.1s ease-in-out infinite alternate"),
 ("@keyframes og-wave-bounce", "from { block-size: 15% } to { block-size: 90% }"),
 ("@media (prefers-reduced-motion: reduce)", ".og-wave__bar { animation: none; block-size: 40% }"),
]

EXT3["25-maps-directions.css"] = [
 (".og-map", "position: relative; border-radius: var(--og-radius-xl); overflow: hidden; block-size: 320px; "
             "border: 1px solid var(--og-hairline); background: var(--og-gray-1)"),
 (".og-map__pin", "position: absolute; transform: translate(-50%, -100%); color: var(--og-icon-accent)"),
 (".og-map__overlay", "position: absolute; inset-inline: var(--og-space-3); inset-block-end: var(--og-space-3); "
                      "padding: var(--og-space-3); border-radius: var(--og-radius-lg); background: var(--og-surface-raised); "
                      "-webkit-backdrop-filter: var(--og-glass-blur); backdrop-filter: var(--og-glass-blur)"),
 ("@media (forced-colors: active)", ".og-map__overlay { background: Canvas }"),
]

EXT3["26-calendar-events.css"] = [
 (".og-cal", "display: grid; grid-template-columns: repeat(7, 1fr); gap: 4px"),
 (".og-cal__cell", "aspect-ratio: 1; display: grid; place-items: center; border-radius: var(--og-radius-md); "
                   "font-size: var(--og-text-sm); color: var(--og-text-secondary)"),
 (".og-cal__cell[aria-selected='true']", "background: var(--og-white); color: var(--og-black); font-weight: 700"),
 (".og-cal__cell[data-has-event]::after", "content: ''; inline-size: 4px; block-size: 4px; border-radius: 50%; "
                                          "background: var(--og-icon-accent); position: absolute; margin-block-start: 18px"),
 ("@media (forced-colors: active)", ".og-cal__cell[aria-selected='true'] { background: Highlight; color: HighlightText }"),
]

EXT3["27-translate-linguistic.css"] = [
 (".og-lang-row", "display: grid; grid-template-columns: 1fr auto 1fr; gap: var(--og-space-3); align-items: center"),
 (".og-lang-chip", "padding: var(--og-space-2) var(--og-space-4); border-radius: var(--og-radius-pill); "
                   "border: 1px solid var(--og-hairline); font-size: var(--og-text-sm)"),
 (".og-script", "unicode-bidi: isolate"),
 ("[lang]", "font-variant-ligatures: contextual"),
]

EXT3["28-code-snippets.css"] = [
 (".og-code", "position: relative"),
 (".og-code__copy", "position: absolute; inset-block-start: var(--og-space-2); inset-inline-end: var(--og-space-2); "
                    "padding: 4px 10px; border-radius: var(--og-radius-sm); border: 1px solid var(--og-hairline); "
                    "background: var(--og-surface-raised); color: var(--og-text-muted); cursor: pointer; "
                    "font-size: var(--og-text-xs)"),
 (".og-code__copy:hover", "color: var(--og-white)"),
 ("@media print", ".og-code__copy { display: none }"),
]

EXT3["30-footer-legal.css"] = [
 (".footer, .og-footer", "border-block-start: 1px solid var(--og-hairline); padding: var(--og-space-8) var(--og-gutter); "
                         "margin-block-start: var(--og-space-10); color: var(--og-text-faint); font-size: var(--og-text-sm)"),
 (".og-footer__links", "display: flex; flex-wrap: wrap; gap: var(--og-space-4); justify-content: center"),
 (".og-footer__links a:hover", "color: var(--og-white); text-decoration: underline"),
 ("@media print", ".footer { display: none }"),
]

EXT3["34-forced-colors-high-contrast.css"] = [
 ("@media (forced-colors: active)", ".og-glass, .search-box, .header, .modal-content, .notification, .sidebar-section {"
                                    "background: Canvas; color: CanvasText; border: 1px solid CanvasText; "
                                    "-webkit-backdrop-filter: none; backdrop-filter: none; box-shadow: none}"),
 ("@media (forced-colors: active)", ".btn, .filter-btn, .nav-btn { border: 1px solid ButtonText; background: ButtonFace; color: ButtonText }"),
 ("@media (forced-colors: active)", ".toggle-slider::before { background: CanvasText }"),
 ("@media (forced-colors: active)", ".og-glass::before, .og-glass::after, .glow-effect::after { display: none }"),
 ("@media (prefers-contrast: more)", ":root { --og-hairline: rgba(255,255,255,0.4); --og-text-muted: #d4d4d4 }"),
 ("@media (prefers-contrast: less)", ":root { --og-hairline: rgba(255,255,255,0.06) }"),
]

EXT3["36-print-export.css"] = [
 ("@page", "margin: 16mm"),
 ("@media print", "body { background: #fff !important; color: #000 !important }"),
 ("@media print", ".header, .search-box, .filter-controls, .particle-background, .progress-bar, .floating-action, "
                  ".settings-panel, .notification { display: none !important }"),
 ("@media print", ".results-section { display: block }"),
 ("@media print", "a[href^='http']::after { content: ' (' attr(href) ')'; font-size: 9pt; color: #444 }"),
]
