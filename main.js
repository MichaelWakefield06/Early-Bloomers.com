(function () {
  'use strict';

  // ---- Copyright year ----
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  // ---- Mobile menu ----
  var burger = document.getElementById('burger'),
      nav    = document.getElementById('nav');

  if (burger && nav) {
    var setMenu = function (open) {
      nav.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    };
    burger.addEventListener('click', function () {
      setMenu(!nav.classList.contains('open'));
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') setMenu(false);
    });
    // Escape closes the menu and returns focus to the toggle
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        setMenu(false);
        burger.focus();
      }
    });
  }

  // ---- Sticky header shadow ----
  var hdr = document.getElementById('hdr');
  if (hdr) {
    var onScroll = function () { hdr.classList.toggle('is-stuck', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // ---- Milestone tabs (WAI-ARIA tabs pattern) ----
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.ms__tab'));
  if (tabs.length) {
    var select = function (tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(t.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
    };
    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { select(tab); });
      tab.addEventListener('keydown', function (e) {
        var n = null;
        if (e.key === 'ArrowRight') n = tabs[(i + 1) % tabs.length];
        if (e.key === 'ArrowLeft')  n = tabs[(i - 1 + tabs.length) % tabs.length];
        if (e.key === 'Home')       n = tabs[0];
        if (e.key === 'End')        n = tabs[tabs.length - 1];
        if (n) { e.preventDefault(); select(n); n.focus(); }
      });
    });
  }

  // ---- Contact form: AJAX submit, keeps the visitor on the site ----
  // Falls back to a normal POST if JS is unavailable.
  var form = document.getElementById('contact-form');
  if (form) {
    var status = document.getElementById('form-status');
    var btn    = document.getElementById('form-submit');

    var say = function (msg, ok) {
      status.textContent = msg;
      status.className = 'form__status ' + (ok ? 'form__status--ok' : 'form__status--err');
    };

    form.addEventListener('submit', function (e) {
      if (!window.fetch) return; // let the browser POST normally
      e.preventDefault();

      if (!form.checkValidity()) { form.reportValidity(); return; }

      btn.disabled = true;
      var original = btn.textContent;
      btn.textContent = 'Sending\u2026';
      say('Sending your message\u2026', true);

      fetch('https://formsubmit.co/ajax/' + form.dataset.to, {
        method: 'POST',
        headers: { 'Accept': 'application/json' },
        body: new FormData(form)
      })
      .then(function (r) { return r.json().then(function (d) { return { ok: r.ok, d: d }; }); })
      .then(function (res) {
        if (res.ok) {
          form.reset();
          say('Thank you. Your message is on its way and Michelle will be in touch soon. If it is urgent, please call 704-676-2661.', true);
        } else {
          throw new Error('bad response');
        }
      })
      .catch(function () {
        say('Something went wrong sending that. Please email EarlyBloomersllc@gmail.com or call 704-676-2661 instead.', false);
      })
      .then(function () {
        btn.disabled = false;
        btn.textContent = original;
      });
    });
  }

  // ---- Reveal on scroll ----
  var rv = document.querySelectorAll('.rv');
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    rv.forEach(function (el) { io.observe(el); });
  } else {
    rv.forEach(function (el) { el.classList.add('in'); });
  }
})();
