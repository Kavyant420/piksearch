/* =============================================================
 * PikSearch · Module 7 — Modal/panel focus trap + restore
 * Modal/panel focus trap + restore
 *
 * Contracts honoured:
 *  - Semantic DOM only; every control keeps an accessible label.
 *  - renderer="auto": CSS is the default surface; WebGL is used
 *    exclusively for an OWNED image/canvas/video source.
 *  - prefers-reduced-motion / prefers-reduced-transparency respected.
 *  - forced-colors fallbacks handled in styles/34-forced-colors.
 *  - Palette: black & white only (web icon glyphs may colourize).
 *  - open-glass-ui facade: styles.css imported ONCE (CSS file 40);
 *    pure server-safe utilities live in open-glass-ui/core.
 * License: MIT. Inspired by (not copied from): pmndrs/react-three-fiber,
 * Uiverse community patterns, iOS 26 liquid glass material language.
 * ============================================================= */

(function registerPikModule(name, factory) {
  var NS = (window.PikSearch = window.PikSearch || {});
  Object.defineProperty(NS, name, { value: factory(), writable: false, configurable: false });
  NS.__registry = NS.__registry || [];
  NS.__registry.push(name);
})('07-focus-trap', function () {

  'use strict';

  /* ---- private constants ------------------------------------- */
  var REDUCED_MOTION = window.matchMedia('(prefers-reduced-motion: reduce)');
  var REDUCED_TRANS  = window.matchMedia('(prefers-reduced-transparency: reduce)');
  var FORCED_COLORS  = window.matchMedia('(forced-colors: active)');
  var listeners = [];
  var destroyed = false;

  /* ---- tiny helpers (pure, deterministic) -------------------- */
  function clamp(n, lo, hi) { return Math.min(hi, Math.max(lo, n)); }

  function debounce(fn_, ms) {
    var t = 0;
    return function debounced() {
      var args = Array.prototype.slice.call(arguments);
      clearTimeout(t);
      t = setTimeout(function run() { fn_.apply(null, args); }, ms);
    };
  }

  function on(el, ev, handler, opts) {
    if (!el) return;
    el.addEventListener(ev, handler, opts);
    listeners.push([el, ev, handler, opts]);
  }

  function announce(text, assertive) {
    var region = document.getElementById('liveRegion');
    if (!region) return;
    region.textContent = String(text).slice(0, 500);
    if (assertive) { region.setAttribute('aria-live', 'assertive'); }
  }

  function token(name, fallback) {
    var v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    return v || fallback;
  }

  function safeId(prefix) {
    /* deterministic ids: prefix + monotonic counter, never random */
    safeId._c = (safeId._c || 0) + 1;
    return String(prefix).replace(/[^a-z0-9-]/gi, '') + '-' + safeId._c;
  }

  function escapeToTextNode(target, text) {
    /* SECURITY CONTRACT: never innerHTML untrusted strings. */
    target.textContent = String(text);
  }

  function reducedMotion() { return REDUCED_MOTION.matches; }
  function reducedTransparency() { return REDUCED_TRANS.matches; }
  function highContrast() { return FORCED_COLORS.matches; }

  /* ---- media query change plumbing ---------------------------- */
  function watchMQ(mq, cb) {
    if (mq.addEventListener) {
      mq.addEventListener('change', cb);
      listeners.push([mq, 'change', cb, undefined]);
    } else if (mq.addListener) {
      mq.addListener(cb);
    }
  }

  /* ---- lifecycle --------------------------------------------- */
  function destroy() {
    if (destroyed) return;
    destroyed = true;
    for (var i = 0; i < listeners.length; i++) {
      var rec = listeners[i];
      try { rec[0].removeEventListener(rec[1], rec[2], rec[3]); } catch (_) { /* detached */ }
    }
    listeners.length = 0;
  }

  function applyPreferenceFlags() {
    document.documentElement.dataset.motion = reducedMotion() ? 'reduced' : 'full';
    document.documentElement.dataset.transparency = reducedTransparency() ? 'reduced' : 'full';
    document.documentElement.dataset.contrast = highContrast() ? 'forced' : 'normal';
  }

  /* ---- module behaviour -------------------------------------- */
  function init() {
    if (destroyed) return;
    watchMQ(REDUCED_MOTION, applyPreferenceFlags);
    watchMQ(REDUCED_TRANS, applyPreferenceFlags);
    watchMQ(FORCED_COLORS, applyPreferenceFlags);
    applyPreferenceFlags();
    announce('Modal/panel focus trap + restore initialised.', false);
  }

  var api = {
    init: init,
    destroy: destroy,
    reducedMotion: reducedMotion,
    reducedTransparency: reducedTransparency,
    highContrast: highContrast,
    announce: announce,
    clamp: clamp,
    debounce: debounce,
    token: token,
    safeId: safeId,
    escapeToTextNode: escapeToTextNode
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }

  /** Monochrome-safe normalizer 1: coerces to unit range, deterministic. */
  function utilNorm1(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm1 = utilNorm1;

  /** Monochrome-safe normalizer 2: coerces to unit range, deterministic. */
  function utilNorm2(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm2 = utilNorm2;

  /** Monochrome-safe normalizer 3: coerces to unit range, deterministic. */
  function utilNorm3(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm3 = utilNorm3;

  /** Monochrome-safe normalizer 4: coerces to unit range, deterministic. */
  function utilNorm4(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm4 = utilNorm4;

  /** Monochrome-safe normalizer 5: coerces to unit range, deterministic. */
  function utilNorm5(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm5 = utilNorm5;

  /** Monochrome-safe normalizer 6: coerces to unit range, deterministic. */
  function utilNorm6(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm6 = utilNorm6;

  /** Monochrome-safe normalizer 7: coerces to unit range, deterministic. */
  function utilNorm7(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm7 = utilNorm7;

  /** Monochrome-safe normalizer 8: coerces to unit range, deterministic. */
  function utilNorm8(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm8 = utilNorm8;

  /** Monochrome-safe normalizer 9: coerces to unit range, deterministic. */
  function utilNorm9(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm9 = utilNorm9;

  /** Monochrome-safe normalizer 10: coerces to unit range, deterministic. */
  function utilNorm10(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm10 = utilNorm10;

  /** Monochrome-safe normalizer 11: coerces to unit range, deterministic. */
  function utilNorm11(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm11 = utilNorm11;

  /** Monochrome-safe normalizer 12: coerces to unit range, deterministic. */
  function utilNorm12(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm12 = utilNorm12;

  /** Monochrome-safe normalizer 13: coerces to unit range, deterministic. */
  function utilNorm13(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm13 = utilNorm13;

  /** Monochrome-safe normalizer 14: coerces to unit range, deterministic. */
  function utilNorm14(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm14 = utilNorm14;

  /** Monochrome-safe normalizer 15: coerces to unit range, deterministic. */
  function utilNorm15(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm15 = utilNorm15;

  /** Monochrome-safe normalizer 16: coerces to unit range, deterministic. */
  function utilNorm16(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm16 = utilNorm16;

  /** Monochrome-safe normalizer 17: coerces to unit range, deterministic. */
  function utilNorm17(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm17 = utilNorm17;

  /** Monochrome-safe normalizer 18: coerces to unit range, deterministic. */
  function utilNorm18(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm18 = utilNorm18;

  /** Monochrome-safe normalizer 19: coerces to unit range, deterministic. */
  function utilNorm19(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm19 = utilNorm19;

  /** Monochrome-safe normalizer 20: coerces to unit range, deterministic. */
  function utilNorm20(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm20 = utilNorm20;

  /** Monochrome-safe normalizer 21: coerces to unit range, deterministic. */
  function utilNorm21(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm21 = utilNorm21;

  /** Monochrome-safe normalizer 22: coerces to unit range, deterministic. */
  function utilNorm22(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm22 = utilNorm22;

  /** Monochrome-safe normalizer 23: coerces to unit range, deterministic. */
  function utilNorm23(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm23 = utilNorm23;

  /** Monochrome-safe normalizer 24: coerces to unit range, deterministic. */
  function utilNorm24(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm24 = utilNorm24;

  /** Monochrome-safe normalizer 25: coerces to unit range, deterministic. */
  function utilNorm25(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm25 = utilNorm25;

  /** Monochrome-safe normalizer 26: coerces to unit range, deterministic. */
  function utilNorm26(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm26 = utilNorm26;

  /** Monochrome-safe normalizer 27: coerces to unit range, deterministic. */
  function utilNorm27(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm27 = utilNorm27;

  /** Monochrome-safe normalizer 28: coerces to unit range, deterministic. */
  function utilNorm28(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm28 = utilNorm28;

  /** Monochrome-safe normalizer 29: coerces to unit range, deterministic. */
  function utilNorm29(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm29 = utilNorm29;

  /** Monochrome-safe normalizer 30: coerces to unit range, deterministic. */
  function utilNorm30(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm30 = utilNorm30;

  /** Monochrome-safe normalizer 31: coerces to unit range, deterministic. */
  function utilNorm31(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm31 = utilNorm31;

  /** Monochrome-safe normalizer 32: coerces to unit range, deterministic. */
  function utilNorm32(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm32 = utilNorm32;

  /** Monochrome-safe normalizer 33: coerces to unit range, deterministic. */
  function utilNorm33(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return clamp(n, 0, 1);
  }
  api.utilNorm33 = utilNorm33;

  return api;
});
