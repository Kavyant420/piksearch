/* =============================================================
 * PikSearch · app.js — consolidated application logic
 *
 * Replaces the 30 generated boilerplate modules (js/01–js/30),
 * which registered empty namespaces but never wired a single
 * control. This file implements the real behaviour:
 *
 *   · search pipeline (deterministic demo corpus, XSS-safe DOM)
 *   · suggestions listbox with full keyboard support
 *   · tabs / filters / sort / time / region / advanced search
 *   · settings panel + persisted preferences (localStorage)
 *   · dark ("default") / light ("paper") theme switching
 *   · modal manager, toasts, live-region announcements
 *   · voice search (SpeechRecognition with graceful fallback)
 *   · export (JSON / CSV / print-to-PDF)
 *   · keyboard shortcuts, scroll-to-top, progress bar
 *   · monochrome particle field + pointer-tracked glass light
 *
 * Contracts honoured: CSP-safe (no eval/inline), no innerHTML with
 * dynamic data, prefers-reduced-motion / reduced-transparency.
 * License: MIT.
 * ============================================================= */
(function () {
  'use strict';

  /* ---------- tiny DOM helpers -------------------------------- */
  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = String(text);
    return node;
  }

  function icon(cls) {
    var i = el('i');
    i.className = cls;
    i.setAttribute('aria-hidden', 'true');
    return i;
  }

  function announce(text, assertive) {
    var region = $('#liveRegion');
    if (!region) return;
    region.textContent = '';
    /* re-set on next tick so screen readers re-announce repeats */
    window.setTimeout(function () {
      region.textContent = String(text).slice(0, 300);
      region.setAttribute('aria-live', assertive ? 'assertive' : 'polite');
    }, 30);
  }

  function debounce(fn, ms) {
    var t = 0;
    return function () {
      var args = arguments, self = this;
      window.clearTimeout(t);
      t = window.setTimeout(function () { fn.apply(self, args); }, ms);
    };
  }

  var store = {
    get: function (key, fallback) {
      try {
        var raw = window.localStorage.getItem(key);
        return raw == null ? fallback : JSON.parse(raw);
      } catch (_) { return fallback; }
    },
    set: function (key, value) {
      try { window.localStorage.setItem(key, JSON.stringify(value)); } catch (_) { /* private mode */ }
    }
  };

  /* ---------- deterministic PRNG (stable demo results) -------- */
  function hashString(str) {
    var h = 2166136261 >>> 0;
    for (var i = 0; i < str.length; i++) {
      h ^= str.charCodeAt(i);
      h = Math.imul(h, 16777619);
    }
    return h >>> 0;
  }

  function mulberry32(seed) {
    var a = seed >>> 0;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function pick(rand, arr) { return arr[Math.floor(rand() * arr.length)]; }

  /* ---------- element references ------------------------------- */
  var input = $('#searchInput');
  var searchBox = $('#searchBox');
  var searchBtn = $('#searchBtn');
  var clearBtn = $('#clearBtn');
  var voiceBtn = $('#voiceSearchBtn');
  var suggestionsEl = $('#searchSuggestions');
  var tabsBar = $('#searchTabs');
  var resultsSection = $('#resultsSection');
  var resultsList = $('#resultsList');
  var resultsCount = $('#resultsCount');
  var searchTimeEl = $('#searchTime');
  var progressBar = $('#progressBar');
  var pageTransition = $('#pageTransition');
  var settingsPanel = $('#settingsPanel');
  var settingsBtn = $('#settingsBtn');
  var closeSettingsBtn = $('#closeSettings');
  var modal = $('#modal');
  var modalBackdrop = $('#modalBackdrop');
  var modalTitle = $('#modalTitle');
  var modalContent = $('#modalContent');
  var closeModalBtn = $('#closeModal');
  var notification = $('#notification');
  var notificationText = $('#notificationText');
  var scrollTopBtn = $('#scrollToTop');
  var advancedBtn = $('#advancedSearchBtn');
  var advancedPanel = $('#advancedSearch');
  var operatorsPanel = $('#searchOperators');
  var contextBox = $('#searchContext');
  var contextContent = $('#contextContent');
  var perfResponse = $('#responseTime');
  var perfResults = $('#resultCount');
  var easterEgg = $('#easterEgg');

  var REDUCED_MOTION = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* ---------- state -------------------------------------------- */
  var SETTINGS_KEY = 'piksearch.settings.v1';
  var HISTORY_KEY = 'piksearch.history.v1';

  var settings = Object.assign({
    darkMode: true,
    safeSearch: true,
    autoSuggestions: true,
    searchHistory: true,
    resultsPerPage: 20,
    defaultSearch: 'web',
    language: 'en',
    defaultRegion: 'wt-wt'
  }, store.get(SETTINGS_KEY, {}));

  var history = store.get(HISTORY_KEY, []);
  if (!Array.isArray(history)) history = [];

  var state = {
    query: '',
    tab: 'all',
    filter: 'all',
    sort: 'relevance',
    time: 'any',
    region: 'all',
    results: [],
    suggestionIndex: -1,
    searching: false
  };

  /* ---------- toast --------------------------------------------- */
  var toastTimer = 0;
  function toast(text) {
    if (!notification) return;
    notificationText.textContent = String(text);
    notification.classList.add('is-visible');
    window.clearTimeout(toastTimer);
    toastTimer = window.setTimeout(function () {
      notification.classList.remove('is-visible');
    }, 3200);
  }

  /* ---------- modal manager -------------------------------------- */
  var lastFocused = null;

  function openModal(title, buildContent) {
    if (!modal) return;
    lastFocused = document.activeElement;
    modalTitle.textContent = '';
    modalTitle.appendChild(icon('fas fa-info-circle'));
    modalTitle.appendChild(document.createTextNode(' ' + title));
    modalContent.textContent = '';
    buildContent(modalContent);
    modal.classList.add('is-open');
    modalBackdrop.classList.add('is-open');
    document.body.classList.add('ps-modal-open');
    modal.setAttribute('aria-hidden', 'false');
    closeModalBtn.focus();
    announce(title + ' dialog opened.');
  }

  function closeModal() {
    if (!modal || !modal.classList.contains('is-open')) return;
    modal.classList.remove('is-open');
    modalBackdrop.classList.remove('is-open');
    document.body.classList.remove('ps-modal-open');
    modal.setAttribute('aria-hidden', 'true');
    if (lastFocused && lastFocused.focus) lastFocused.focus();
  }

  if (closeModalBtn) closeModalBtn.addEventListener('click', closeModal);
  if (modalBackdrop) modalBackdrop.addEventListener('click', closeModal);

  /* How-to: set as default engine (referenced by inline onclick) */
  window.setAsDefault = function setAsDefault() {
    openModal('Set PikSearch as default', function (root) {
      var p1 = el('p', null, 'PikSearch runs entirely in your browser, so your browser controls the default search engine setting:');
      var list = el('ol');
      [
        'Open your browser settings and find "Search engine".',
        'Choose "Manage search engines" and add a new engine.',
        'Name it PikSearch and paste this page\'s URL with %s where the query goes.',
        'Save, then select PikSearch as the default.'
      ].forEach(function (step) { list.appendChild(el('li', null, step)); });
      var note = el('p', null, 'Your searches never leave this page — the demo index is generated locally.');
      note.style.marginBlockStart = '12px';
      root.appendChild(p1);
      root.appendChild(list);
      root.appendChild(note);
    });
  };

  /* ---------- settings panel -------------------------------------- */
  function openSettings() {
    settingsPanel.classList.add('is-open');
    settingsPanel.setAttribute('aria-hidden', 'false');
    settingsPanel.focus();
    announce('Settings opened.');
  }

  function closeSettings() {
    if (!settingsPanel.classList.contains('is-open')) return;
    settingsPanel.classList.remove('is-open');
    settingsPanel.setAttribute('aria-hidden', 'true');
    settingsBtn.focus();
  }

  settingsBtn.addEventListener('click', function () {
    if (settingsPanel.classList.contains('is-open')) closeSettings();
    else openSettings();
  });
  closeSettingsBtn.addEventListener('click', closeSettings);
  document.addEventListener('pointerdown', function (e) {
    if (settingsPanel.classList.contains('is-open') &&
        !settingsPanel.contains(e.target) &&
        !settingsBtn.contains(e.target)) {
      closeSettings();
    }
  });

  function saveSettings() { store.set(SETTINGS_KEY, settings); }

  function applyTheme() {
    var root = document.documentElement;
    /* data-ps-theme is REQUIRED: without it, a prefers-color-scheme:light
       media query in styles/31 flips text tokens to dark-on-black. */
    if (settings.darkMode) {
      root.setAttribute('data-ps-theme', 'dark');
      root.removeAttribute('data-theme');
    } else {
      root.setAttribute('data-ps-theme', 'light');
      root.setAttribute('data-theme', 'paper');
    }
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', settings.darkMode ? '#000000' : '#ffffff');
  }

  /* wire the settings form */
  function bindSetting(id, key, isSelect) {
    var control = $('#' + id);
    if (!control) return;
    if (isSelect) {
      control.value = String(settings[key]);
      control.addEventListener('change', function () {
        settings[key] = id === 'resultsPerPage' ? parseInt(control.value, 10) : control.value;
        saveSettings();
        toast('Preference saved');
        if (state.query) renderResults();
      });
    } else {
      control.checked = !!settings[key];
      control.setAttribute('aria-checked', String(!!settings[key]));
      control.addEventListener('change', function () {
        settings[key] = control.checked;
        control.setAttribute('aria-checked', String(control.checked));
        saveSettings();
        if (key === 'darkMode') applyTheme();
        if (key === 'searchHistory' && !control.checked) { history = []; persistHistory(); renderHistory(); }
        if (key === 'safeSearch' && state.query) renderResults();
        toast('Preference saved');
      });
    }
  }

  bindSetting('darkModeToggle', 'darkMode');
  bindSetting('safeSearch', 'safeSearch');
  bindSetting('autoSuggestions', 'autoSuggestions');
  bindSetting('searchHistory', 'searchHistory');
  bindSetting('resultsPerPage', 'resultsPerPage', true);
  bindSetting('defaultSearch', 'defaultSearch', true);
  bindSetting('language', 'language', true);
  bindSetting('defaultRegion', 'defaultRegion', true);
  applyTheme();

  /* ---------- history --------------------------------------------- */
  function persistHistory() { store.set(HISTORY_KEY, history.slice(0, 12)); }

  function recordHistory(query) {
    if (!settings.searchHistory) return;
    history = [query].concat(history.filter(function (q) { return q.toLowerCase() !== query.toLowerCase(); }));
    persistHistory();
    renderHistory();
  }

  function renderHistory() {
    var wrap = $('.search-history');
    if (!wrap) return;
    $$('.history-item', wrap).forEach(function (n) { n.remove(); });
    var items = history.length ? history.slice(0, 6) : ['No searches yet'];
    items.forEach(function (q) {
      var row = el('div', 'history-item');
      var qEl = el('span', 'history-query', q);
      var tEl = el('span', 'history-time', history.length ? 'recent' : '');
      row.appendChild(qEl);
      row.appendChild(tEl);
      if (history.length) {
        row.style.cursor = 'pointer';
        row.addEventListener('click', function () {
          closeSettings();
          setQuery(q);
          performSearch();
        });
      }
      wrap.appendChild(row);
    });
  }

  /* ---------- demo corpus ------------------------------------------ */
  var SUGGESTION_SEED = [
    'javascript tutorials', 'python programming', 'web development', 'machine learning',
    'cybersecurity', 'privacy tools', 'open source projects', 'css glassmorphism',
    'rust programming', 'typescript handbook', 'react hooks', 'kubernetes basics',
    'docker tutorial', 'linux commands', 'git workflows', 'sql for beginners',
    'data structures', 'system design', 'web accessibility', 'three.js examples',
    'webgl shaders', 'progressive web apps', 'api design', 'graphql vs rest',
    'password managers', 'tor network', 'encryption explained', 'zero knowledge proofs',
    'self hosting', 'degoogle guide', 'privacy focused browsers', 'vpn comparison',
    'cloud computing', 'devops roadmap', 'ai ethics', 'neural networks',
    'compiler design', 'operating systems', 'network protocols', 'quantum computing'
  ];

  var DOMAINS = [
    'developer.mozilla.org', 'wikipedia.org', 'github.com', 'stackoverflow.com',
    'w3.org', 'css-tricks.com', 'freecodecamp.org', 'owasp.org',
    'eff.org', 'privacyguides.org', 'arxiv.org', 'medium.com',
    'dev.to', 'hackernews.com', 'reddit.com', 'youtube.com'
  ];

  var TITLE_TEMPLATES = {
    all:      ['{Q} — The Complete Guide', 'Understanding {Q}: Fundamentals', '{Q} Best Practices for 2026', 'How {Q} Actually Works', '{Q} Explained Simply', 'Advanced {Q} Techniques', '{Q}: Common Mistakes to Avoid', 'The State of {Q}', 'Getting Started with {Q}', '{Q} Tips from Experts'],
    images:   ['{Q} — HD Image Gallery', '{Q} Photos and Wallpapers', '{Q} Infographics Collection', '{Q} Diagrams Explained Visually', 'High Resolution {Q} Pictures'],
    news:     ['{Q}: Latest Developments', 'Breaking: New {Q} Updates', '{Q} Trends This Week', 'What\'s Next for {Q}', '{Q} Industry News Roundup'],
    videos:   ['{Q} — Video Tutorial Series', 'Learn {Q} in 20 Minutes', '{Q} Deep Dive (Full Course)', '{Q} Explained on Video', '{Q} Conference Talks'],
    shopping: ['{Q} — Best Deals Compared', 'Top Rated {Q} Products', '{Q} Buyer\'s Guide 2026', '{Q}: Price Comparison', 'Best Budget {Q} Options']
  };

  var SNIPPET_TEMPLATES = [
    'A practical walkthrough of {q}, covering the essentials, real-world examples and the pitfalls most guides skip.',
    'Everything you need to know about {q} — from first principles to production-ready techniques, updated for 2026.',
    'Community-curated resources for {q}. Includes documentation, interactive examples and expert commentary.',
    'Step-by-step {q} tutorial with privacy-friendly tooling. No tracking, no accounts, just the material.',
    'An in-depth analysis of {q}: benchmarks, comparisons and actionable recommendations.',
    'The definitive reference for {q}. Comprehensive coverage with searchable examples and clear explanations.',
    'Learn {q} the right way. Structured lessons, exercises and projects designed for lasting understanding.',
    '{q} demystified: a clear, honest breakdown of what matters, what doesn\'t, and where to go next.'
  ];

  function capitalize(s) { return s.charAt(0).toUpperCase() + s.slice(1); }

  function generateResults(query, tab) {
    var rand = mulberry32(hashString(query.toLowerCase() + '|' + tab));
    var templates = TITLE_TEMPLATES[tab] || TITLE_TEMPLATES.all;
    var count = 24 + Math.floor(rand() * 40);
    var results = [];
    for (var i = 0; i < count; i++) {
      var title = pick(rand, templates).replace(/\{Q\}/g, capitalize(query));
      var domain = pick(rand, DOMAINS);
      var path = '/' + query.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') +
                 (rand() > 0.5 ? '/' + Math.floor(rand() * 9000 + 1000) : '');
      var snippet = pick(rand, SNIPPET_TEMPLATES).replace(/\{q\}/g, query);
      results.push({
        title: title,
        displayUrl: domain + path,
        href: 'https://duckduckgo.com/?q=' + encodeURIComponent(query + ' ' + domain),
        snippet: snippet,
        daysAgo: Math.floor(rand() * 400),
        verified: rand() > 0.55,
        popularity: Math.floor(rand() * 98000) + 200,
        score: rand(),
        adult: rand() > 0.96
      });
    }
    return results;
  }

  /* ---------- filtering / sorting ---------------------------------- */
  var TIME_LIMITS = { any: Infinity, hour: 1, day: 1, week: 7, month: 30, year: 365 };

  function visibleResults() {
    var out = state.results.slice();
    if (settings.safeSearch) out = out.filter(function (r) { return !r.adult; });
    if (state.filter === 'recent') out = out.filter(function (r) { return r.daysAgo <= 7; });
    if (state.filter === 'verified') out = out.filter(function (r) { return r.verified; });
    if (state.time !== 'any') out = out.filter(function (r) { return r.daysAgo <= TIME_LIMITS[state.time]; });
    if (state.sort === 'date') out.sort(function (a, b) { return a.daysAgo - b.daysAgo; });
    else if (state.sort === 'popularity') out.sort(function (a, b) { return b.popularity - a.popularity; });
    else out.sort(function (a, b) { return b.score - a.score; });
    return out.slice(0, settings.resultsPerPage);
  }

  function formatDate(daysAgo) {
    if (daysAgo < 1) return 'Today';
    if (daysAgo === 1) return 'Yesterday';
    if (daysAgo < 30) return daysAgo + ' days ago';
    if (daysAgo < 365) return Math.floor(daysAgo / 30) + ' months ago';
    return Math.floor(daysAgo / 365) + ' years ago';
  }

  /* ---------- rendering --------------------------------------------- */
  function renderResults() {
    var items = visibleResults();
    resultsList.textContent = '';

    if (state.tab === 'tools') {
      operatorsPanel.style.display = 'block';
      resultsList.style.display = 'none';
    } else {
      operatorsPanel.style.display = 'none';
      resultsList.style.display = '';
    }

    if (!items.length && state.tab !== 'tools') {
      var empty = el('div', 'ps-empty-state');
      empty.appendChild(icon('fas fa-search'));
      empty.appendChild(el('p', null, 'No results match your filters. Try widening the time range or clearing filters.'));
      resultsList.appendChild(empty);
    }

    items.forEach(function (r) {
      var li = el('li', 'result-item');

      var head = el('div', 'result-head');
      head.appendChild(el('span', 'result-favicon', r.displayUrl.charAt(0).toUpperCase()));
      var url = el('span', 'result-url', r.displayUrl + ' · ' + formatDate(r.daysAgo));
      head.appendChild(url);
      li.appendChild(head);

      var link = el('a', 'result-link', r.title);
      link.href = r.href;
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      li.appendChild(link);

      li.appendChild(el('p', 'result-snippet', r.snippet));

      var badges = el('div', 'result-badges');
      if (r.verified) badges.appendChild(el('span', 'result-badge', 'Verified'));
      if (r.daysAgo <= 7) badges.appendChild(el('span', 'result-badge', 'Recent'));
      if (r.popularity > 80000) badges.appendChild(el('span', 'result-badge', 'Popular'));
      if (badges.childNodes.length) li.appendChild(badges);

      resultsList.appendChild(li);
    });

    var total = state.results.length;
    resultsCount.textContent = 'About ' + total.toLocaleString('en-US') + ' results';
    if (perfResults) perfResults.textContent = String(items.length);
    renderContext();
  }

  function renderContext() {
    var bits = [];
    if (state.filter !== 'all') bits.push('Filter: ' + state.filter);
    if (state.sort !== 'relevance') bits.push('Sorted by ' + state.sort);
    if (state.time !== 'any') bits.push('Time: ' + state.time);
    if (state.region !== 'all') bits.push('Region: ' + state.region.toUpperCase());
    var adv = advancedQueryParts();
    if (adv) bits.push('Advanced: ' + adv);
    if (bits.length) {
      contextBox.style.display = '';
      contextContent.textContent = bits.join(' · ');
    } else {
      contextBox.style.display = 'none';
      contextContent.textContent = '';
    }
  }

  function advancedQueryParts() {
    var parts = [];
    var exact = ($('#exactPhrase') || {}).value;
    var site = ($('#siteFilter') || {}).value;
    var none = ($('#noneWords') || {}).value;
    var file = ($('#fileType') || {}).value;
    if (exact && exact.trim()) parts.push('"' + exact.trim() + '"');
    if (none && none.trim()) parts.push(none.trim().split(/\s+/).map(function (w) { return '-' + w; }).join(' '));
    if (site && site.trim()) parts.push('site:' + site.trim());
    if (file) parts.push('filetype:' + file);
    return parts.join(' ');
  }

  /* ---------- progress bar ------------------------------------------ */
  function progress(frac) {
    if (!progressBar) return;
    progressBar.style.inlineSize = Math.round(frac * 100) + '%';
    if (frac >= 1) {
      window.setTimeout(function () { progressBar.style.inlineSize = '0'; }, 450);
    }
  }

  /* ---------- search pipeline ---------------------------------------- */
  function setQuery(q) {
    input.value = q;
    hideSuggestions();
  }

  function performSearch() {
    var raw = input.value.trim();
    if (!raw) {
      toast('Type something to search');
      input.focus();
      return;
    }
    if (state.searching) return;
    state.searching = true;
    state.query = raw;

    var advWords = ($('#allWords') || {}).value;
    var effectiveQuery = (advWords && advWords.trim()) ? advWords.trim() + ' ' + raw : raw;

    tabsBar.style.display = '';
    resultsSection.style.display = '';
    document.body.classList.add('has-results');
    pageTransition.classList.add('is-active');
    progress(0.25);

    /* skeletons while "fetching" */
    resultsList.textContent = '';
    resultsList.style.display = '';
    for (var i = 0; i < 3; i++) resultsList.appendChild(el('div', 'ps-skeleton'));

    var t0 = performance.now();
    var latency = REDUCED_MOTION.matches ? 120 : 260 + Math.random() * 320;

    window.setTimeout(function () {
      state.results = generateResults(effectiveQuery, state.tab);
      renderResults();
      progress(1);
      pageTransition.classList.remove('is-active');
      state.searching = false;

      var elapsed = (performance.now() - t0) / 1000;
      searchTimeEl.textContent = elapsed.toFixed(2) + ' seconds';
      if (perfResponse) perfResponse.textContent = Math.round(elapsed * 1000) + 'ms';

      recordHistory(raw);
      announce(state.results.length + ' results for ' + raw + ' in ' + elapsed.toFixed(2) + ' seconds.');

      if (!performSearch._revealed) {
        performSearch._revealed = true;
        toast('Demo index: results are generated locally, links open a private DuckDuckGo search');
      }
      resultsSection.scrollIntoView({ behavior: REDUCED_MOTION.matches ? 'auto' : 'smooth', block: 'start' });
    }, latency);
  }

  function backToHero() {
    tabsBar.style.display = 'none';
    resultsSection.style.display = 'none';
    document.body.classList.remove('has-results');
    state.query = '';
    state.results = [];
    setQuery('');
    input.focus();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  searchBtn.addEventListener('click', performSearch);
  clearBtn.addEventListener('click', function () {
    setQuery('');
    input.focus();
    announce('Search cleared.');
  });

  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      if (state.suggestionIndex >= 0) {
        var active = $$('.suggestion-item', suggestionsEl)[state.suggestionIndex];
        if (active) { setQuery(active.getAttribute('data-value')); }
      }
      performSearch();
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      moveSuggestion(1);
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      moveSuggestion(-1);
    } else if (e.key === 'Escape') {
      hideSuggestions();
    }
  });

  /* home breadcrumb + logo */
  $$('.breadcrumb-item').forEach(function (b) {
    b.addEventListener('click', function (e) { e.preventDefault(); backToHero(); });
  });
  var logo = $('.logo');
  if (logo) logo.addEventListener('click', function (e) { e.preventDefault(); backToHero(); });

  /* ---------- suggestions -------------------------------------------- */
  function buildSuggestions(q) {
    var lower = q.toLowerCase();
    var fromHistory = history.filter(function (h) { return h.toLowerCase().indexOf(lower) === 0 && h.toLowerCase() !== lower; });
    var fromSeed = SUGGESTION_SEED.filter(function (s) { return s.indexOf(lower) !== -1 && s !== lower; });
    return fromHistory.slice(0, 3).map(function (v) { return { value: v, kind: 'history' }; })
      .concat(fromSeed.slice(0, 7).map(function (v) { return { value: v, kind: 'seed' }; }))
      .slice(0, 8);
  }

  function renderSuggestions() {
    var q = input.value.trim();
    suggestionsEl.textContent = '';
    state.suggestionIndex = -1;
    input.removeAttribute('aria-activedescendant');
    if (!q || !settings.autoSuggestions) { hideSuggestions(); return; }
    var items = buildSuggestions(q);
    if (!items.length) { hideSuggestions(); return; }

    items.forEach(function (item, idx) {
      var li = el('li', 'suggestion-item');
      li.id = 'suggestion-' + idx;
      li.setAttribute('role', 'option');
      li.setAttribute('aria-selected', 'false');
      li.setAttribute('data-value', item.value);
      li.appendChild(icon(item.kind === 'history' ? 'fas fa-history suggestion-icon' : 'fas fa-search suggestion-icon'));

      var text = el('span');
      var lower = item.value.toLowerCase();
      var qLower = q.toLowerCase();
      var at = lower.indexOf(qLower);
      if (at >= 0) {
        text.appendChild(document.createTextNode(item.value.slice(0, at)));
        var mark = el('mark', null, item.value.slice(at, at + q.length));
        text.appendChild(mark);
        text.appendChild(document.createTextNode(item.value.slice(at + q.length)));
      } else {
        text.textContent = item.value;
      }
      li.appendChild(text);
      li.addEventListener('pointerdown', function (e) {
        e.preventDefault();
        setQuery(item.value);
        performSearch();
      });
      suggestionsEl.appendChild(li);
    });
    suggestionsEl.hidden = false;
  }

  function hideSuggestions() {
    suggestionsEl.hidden = true;
    suggestionsEl.textContent = '';
    state.suggestionIndex = -1;
    input.removeAttribute('aria-activedescendant');
  }

  function moveSuggestion(delta) {
    var items = $$('.suggestion-item', suggestionsEl);
    if (!items.length) return;
    var states = items.length + 1; /* -1 (input) .. items.length-1 */
    state.suggestionIndex = (((state.suggestionIndex + delta + 1) % states) + states) % states - 1;
    items.forEach(function (n, i) {
      var active = i === state.suggestionIndex;
      n.classList.toggle('is-active', active);
      n.setAttribute('aria-selected', String(active));
      if (active) input.setAttribute('aria-activedescendant', n.id);
    });
    if (state.suggestionIndex === -1) input.removeAttribute('aria-activedescendant');
  }

  input.addEventListener('input', debounce(renderSuggestions, 120));
  input.addEventListener('blur', function () {
    window.setTimeout(hideSuggestions, 150);
  });
  document.addEventListener('pointerdown', function (e) {
    if (!searchBox.contains(e.target)) hideSuggestions();
  });

  /* ---------- voice search -------------------------------------------- */
  voiceBtn.addEventListener('click', function () {
    var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) {
      toast('Voice search is not supported in this browser');
      return;
    }
    try {
      var rec = new SR();
      rec.lang = 'en-US';
      rec.interimResults = false;
      voiceBtn.style.color = '#fff';
      voiceBtn.setAttribute('aria-pressed', 'true');
      toast('Listening… speak now');
      rec.onresult = function (e) {
        var transcript = e.results[0][0].transcript;
        setQuery(transcript);
        performSearch();
      };
      rec.onerror = function () { toast('Voice search unavailable'); };
      rec.onend = function () {
        voiceBtn.style.color = '';
        voiceBtn.setAttribute('aria-pressed', 'false');
      };
      rec.start();
    } catch (_) {
      toast('Voice search unavailable');
    }
  });

  /* ---------- tabs ------------------------------------------------------ */
  $$('.tab', tabsBar).forEach(function (tab) {
    tab.addEventListener('click', function (e) {
      e.preventDefault();
      $$('.tab', tabsBar).forEach(function (t) { t.classList.remove('active'); });
      tab.classList.add('active');
      state.tab = tab.getAttribute('data-tab');
      if (state.query) {
        state.results = generateResults(state.query, state.tab);
        renderResults();
        announce('Switched to ' + state.tab + ' results.');
      }
    });
  });

  /* ---------- filter / sort / time / region ------------------------------ */
  $$('.filter-btn[data-filter]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      $$('.filter-btn[data-filter]').forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      state.filter = btn.getAttribute('data-filter');
      if (state.query) renderResults();
    });
  });

  /* generic dropdown wiring */
  function wireDropdown(buttonId, attr, onPick) {
    var btn = $('#' + buttonId);
    if (!btn) return;
    var wrap = btn.closest('.filter-dropdown');
    var menu = $('.filter-dropdown-content', wrap);
    btn.setAttribute('aria-haspopup', 'listbox');
    btn.setAttribute('aria-expanded', 'false');

    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = wrap.classList.contains('is-open');
      closeAllDropdowns();
      if (!open) {
        wrap.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });

    $$('.filter-option', menu).forEach(function (opt) {
      opt.setAttribute('role', 'option');
      opt.setAttribute('tabindex', '0');
      opt.addEventListener('click', function () {
        $$('.filter-option', menu).forEach(function (o) { o.setAttribute('aria-selected', 'false'); });
        opt.setAttribute('aria-selected', 'true');
        onPick(opt.getAttribute(attr), opt.textContent.trim());
        wrap.classList.remove('is-open');
        btn.setAttribute('aria-expanded', 'false');
      });
      opt.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); opt.click(); }
      });
    });
  }

  function closeAllDropdowns() {
    $$('.filter-dropdown.is-open').forEach(function (d) {
      d.classList.remove('is-open');
      var b = $('button', d);
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  }

  document.addEventListener('pointerdown', function (e) {
    if (!e.target.closest('.filter-dropdown')) closeAllDropdowns();
  });

  function setButtonLabel(btn, text) {
    var ic = btn.querySelector('i');
    btn.textContent = '';
    if (ic) btn.appendChild(ic);
    btn.appendChild(document.createTextNode(' ' + text));
  }

  wireDropdown('sortDropdown', 'data-sort', function (value, label) {
    state.sort = value;
    setButtonLabel($('#sortDropdown'), label);
    if (state.query) renderResults();
    toast('Sorted by ' + label);
  });

  wireDropdown('timeFilter', 'data-time', function (value, label) {
    state.time = value;
    setButtonLabel($('#timeFilter'), label);
    if (state.query) renderResults();
  });

  wireDropdown('regionFilter', 'data-region', function (value, label) {
    state.region = value;
    setButtonLabel($('#regionFilter'), label);
    if (state.query) renderResults();
    toast('Region: ' + label);
  });

  /* ---------- advanced search ------------------------------------------- */
  advancedBtn.addEventListener('click', function () {
    var open = advancedPanel.style.display !== 'none';
    advancedPanel.style.display = open ? 'none' : 'block';
    advancedBtn.setAttribute('aria-expanded', String(!open));
    if (!open) {
      var first = $('#allWords');
      if (first) first.focus();
    }
    renderContext();
  });

  ['allWords', 'exactPhrase', 'anyWords', 'noneWords', 'siteFilter', 'fileType'].forEach(function (id) {
    var c = $('#' + id);
    if (c) c.addEventListener('change', renderContext);
  });

  /* ---------- quick actions / trending / related ------------------------- */
  function bindQueryTrigger(selector, textSelector) {
    $$(selector).forEach(function (node) {
      node.style.cursor = 'pointer';
      node.addEventListener('click', function (e) {
        e.preventDefault();
        var q = node.getAttribute('data-query') ||
                (textSelector && $(textSelector, node) ? $(textSelector, node).textContent.trim() : node.textContent.trim());
        if (!q) return;
        setQuery(q);
        performSearch();
      });
    });
  }

  bindQueryTrigger('.quick-action');
  bindQueryTrigger('.trending-item', '.trending-query');
  bindQueryTrigger('.related-item', '.related-text');

  /* ---------- export ------------------------------------------------------ */
  function downloadFile(name, content, type) {
    var blob = new Blob([content], { type: type });
    var url = URL.createObjectURL(blob);
    var a = el('a');
    a.href = url;
    a.download = name;
    document.body.appendChild(a);
    a.click();
    a.remove();
    window.setTimeout(function () { URL.revokeObjectURL(url); }, 4000);
  }

  $$('.export-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var fmt = btn.getAttribute('data-format');
      if (!state.results.length) {
        toast('Run a search first, then export');
        return;
      }
      var items = visibleResults();
      var stamp = new Date().toISOString().slice(0, 10);
      if (fmt === 'json') {
        downloadFile('piksearch-' + stamp + '.json', JSON.stringify({ query: state.query, exported: stamp, results: items }, null, 2), 'application/json');
        toast('Exported ' + items.length + ' results as JSON');
      } else if (fmt === 'csv') {
        var rows = [['title', 'url', 'snippet', 'date']].concat(items.map(function (r) {
          return [r.title, r.displayUrl, r.snippet, formatDate(r.daysAgo)];
        }));
        var csv = rows.map(function (row) {
          return row.map(function (cell) { return '"' + String(cell).replace(/"/g, '""') + '"'; }).join(',');
        }).join('\r\n');
        downloadFile('piksearch-' + stamp + '.csv', csv, 'text/csv');
        toast('Exported ' + items.length + ' results as CSV');
      } else if (fmt === 'pdf') {
        toast('Opening print dialog — choose "Save as PDF"');
        window.print();
      }
      announce('Export complete: ' + fmt.toUpperCase());
    });
  });

  /* ---------- scroll to top ------------------------------------------------ */
  function onScroll() {
    if (!scrollTopBtn) return;
    scrollTopBtn.classList.toggle('is-visible', window.scrollY > 420);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  if (scrollTopBtn) {
    scrollTopBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: REDUCED_MOTION.matches ? 'auto' : 'smooth' });
      input.focus();
    });
  }

  /* ---------- keyboard shortcuts -------------------------------------------- */
  document.addEventListener('keydown', function (e) {
    var mod = e.ctrlKey || e.metaKey;
    if (mod && (e.key === 'k' || e.key === 'K')) {
      e.preventDefault();
      input.focus();
      input.select();
    } else if (mod && (e.key === 'l' || e.key === 'L')) {
      e.preventDefault();
      setQuery('');
      input.focus();
    } else if (mod && e.key === ',') {
      e.preventDefault();
      openSettings();
    } else if (e.key === 'Escape') {
      if (modal.classList.contains('is-open')) closeModal();
      else if (settingsPanel.classList.contains('is-open')) closeSettings();
      else closeAllDropdowns();
    } else if (e.key === '/' && document.activeElement !== input && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) {
      e.preventDefault();
      input.focus();
    }
  });

  /* simple focus containment for modal + settings */
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Tab') return;
    var container = modal.classList.contains('is-open') ? modal :
                    (settingsPanel.classList.contains('is-open') ? settingsPanel : null);
    if (!container) return;
    var focusables = $$('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])', container)
      .filter(function (n) { return !n.disabled && n.offsetParent !== null; });
    if (!focusables.length) return;
    var first = focusables[0];
    var last = focusables[focusables.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });

  /* ---------- shortcuts help button ------------------------------------------ */
  var shortcutsBtn = $('#shortcutsBtn');
  if (shortcutsBtn) {
    shortcutsBtn.addEventListener('click', function () {
      openModal('Keyboard shortcuts', function (root) {
        var wrap = el('div', 'keyboard-shortcuts');
        [
          ['Focus search', 'Ctrl + K  or  /'],
          ['Clear search', 'Ctrl + L'],
          ['Open settings', 'Ctrl + ,'],
          ['Close dialogs', 'Esc'],
          ['Navigate suggestions', '↑ / ↓'],
          ['Run search', 'Enter']
        ].forEach(function (pair) {
          var row = el('div', 'shortcut-item');
          row.appendChild(el('span', null, pair[0]));
          row.appendChild(el('span', 'shortcut-key', pair[1]));
          wrap.appendChild(row);
        });
        root.appendChild(wrap);
      });
    });
  }

  /* ---------- easter egg (Konami) --------------------------------------------- */
  (function konami() {
    var seq = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
    var pos = 0;
    document.addEventListener('keydown', function (e) {
      pos = (e.key === seq[pos]) ? pos + 1 : 0;
      if (pos === seq.length) {
        pos = 0;
        if (easterEgg) {
          easterEgg.style.transition = 'transform 1s cubic-bezier(0.2, 0.9, 0.25, 1.2), opacity 1s';
          easterEgg.style.transform = 'translateY(-70vh) rotate(720deg) scale(3)';
          easterEgg.style.opacity = '1';
          window.setTimeout(function () {
            easterEgg.style.transform = '';
            easterEgg.style.opacity = '';
          }, 1400);
        }
        toast('You found the easter egg. PikSearch salutes you.');
        announce('Easter egg activated.');
      }
    });
  })();

  /* ---------- monochrome particle field --------------------------------------- */
  (function particles() {
    var host = $('#particleBackground');
    if (!host || REDUCED_MOTION.matches) return;
    var canvas = el('canvas');
    canvas.setAttribute('aria-hidden', 'true');
    canvas.style.cssText = 'position:fixed;inset:0;z-index:-1;pointer-events:none;';
    host.appendChild(canvas);
    var ctx = canvas.getContext('2d');
    var dots = [];
    var W = 0, H = 0;

    function resize() {
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = window.innerWidth; H = window.innerHeight;
      canvas.width = W * dpr;
      canvas.height = H * dpr;
      canvas.style.width = W + 'px';
      canvas.style.height = H + 'px';
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var target = Math.min(90, Math.floor(W * H / 22000));
      dots = [];
      for (var i = 0; i < target; i++) {
        dots.push({
          x: Math.random() * W,
          y: Math.random() * H,
          r: 0.6 + Math.random() * 1.8,
          vx: (Math.random() - 0.5) * 0.18,
          vy: (Math.random() - 0.5) * 0.18,
          a: 0.08 + Math.random() * 0.3
        });
      }
    }

    var running = true;
    function frame() {
      if (!running) return;
      ctx.clearRect(0, 0, W, H);
      for (var i = 0; i < dots.length; i++) {
        var d = dots[i];
        d.x += d.vx; d.y += d.vy;
        if (d.x < -4) d.x = W + 4; if (d.x > W + 4) d.x = -4;
        if (d.y < -4) d.y = H + 4; if (d.y > H + 4) d.y = -4;
        ctx.globalAlpha = d.a;
        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.arc(d.x, d.y, d.r, 0, Math.PI * 2);
        ctx.fill();
      }
      window.requestAnimationFrame(frame);
    }

    document.addEventListener('visibilitychange', function () {
      var was = running;
      running = !document.hidden;
      if (running && !was) window.requestAnimationFrame(frame);
    });

    window.addEventListener('resize', debounce(resize, 200));
    resize();
    window.requestAnimationFrame(frame);
  })();

  /* ---------- pointer-tracked glass light -------------------------------------- */
  (function glassLight() {
    if (REDUCED_MOTION.matches || !window.matchMedia('(pointer: fine)').matches) return;
    var SELECTOR = '.search-box,.settings-panel,.modal-content,.search-suggestions,.filter-dropdown-content,.quick-action,.btn,.export-btn,.filter-btn,.result-item,.sidebar-section,.security-status,.search-context,.advanced-search,.search-operators';
    var ticking = false;
    document.addEventListener('pointermove', function (e) {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () {
        ticking = false;
        var t = e.target && e.target.closest ? e.target.closest(SELECTOR) : null;
        if (!t) return;
        var rect = t.getBoundingClientRect();
        if (!rect.width || !rect.height) return;
        t.style.setProperty('--mx', (((e.clientX - rect.left) / rect.width) * 100).toFixed(1) + '%');
        t.style.setProperty('--my', (((e.clientY - rect.top) / rect.height) * 100).toFixed(1) + '%');
      });
    }, { passive: true });
  })();

  /* ---------- misc wiring -------------------------------------------------------- */
  /* hero subtitle typing effect is CSS-driven; ensure title is readable for SRs */
  var title = $('.search-title');
  if (title) title.setAttribute('aria-label', title.textContent.trim());

  /* mark glass hosts */
  [searchBox, settingsPanel, modal].forEach(function (n) {
    if (n && !n.hasAttribute('data-glass')) n.setAttribute('data-glass', '');
  });

  /* initial render */
  renderHistory();
  announce('PikSearch ready. Type a query and press Enter.');
})();
