/* El abreboca (2 minutos) como overlay-lámina: la página /2-minutes/ es el
   canon; esto asoma su esencia —título, Línea Nadella, figura g52, escalera—
   sin scroll. El fetch va a la ruta real, así que la visita queda registrada.
   En pantallas chicas cae a la pieza completa (con scroll); sin JS o si algo
   falla → navegación normal. */
(function () {
  var link = document.querySelector('a[data-peek]');
  if (!link || !window.fetch || !window.HTMLDialogElement) return;

  var es = document.documentElement.lang === 'es';
  var dlg = null, loaded = false;

  function build() {
    dlg = document.createElement('dialog');
    dlg.className = 'peek';
    dlg.innerHTML = '<button class="peek-close" aria-label="' + (es ? 'Cerrar' : 'Close') + '">×</button><div class="peek-body"></div>';
    document.body.appendChild(dlg);
    dlg.querySelector('.peek-close').addEventListener('click', function () { dlg.close(); });
    dlg.addEventListener('click', function (ev) { if (ev.target === dlg) dlg.close(); });
  }

  function lamina(page) {
    var box = document.createElement('div');
    box.className = 'lamina';

    var head = document.createElement('header');
    ['.eyebrow', 'h1', '.deck'].forEach(function (sel) {
      var el = page.querySelector(sel);
      if (el) head.appendChild(el.cloneNode(true));
    });
    box.appendChild(head);

    var ps = page.querySelectorAll('main.page > p, p');
    var q = null, nad = null;
    for (var i = 0; i < ps.length; i++) {
      if (!q && ps[i].querySelector('em') && /\?/.test(ps[i].textContent)) q = ps[i];
      if (!nad && /Nadella/.test(ps[i].textContent)) nad = ps[i];
      if (q && nad) break;
    }
    if (q) { q = q.cloneNode(true); q.className = 'q'; box.appendChild(q); }
    if (nad) box.appendChild(nad.cloneNode(true));

    var fig = page.querySelector('figure');
    if (fig) box.appendChild(fig.cloneNode(true));

    var next = page.querySelector('.next');
    if (next) {
      next = next.cloneNode(true);
      Array.prototype.forEach.call(next.querySelectorAll('a'), function (a) {
        var h = a.getAttribute('href');
        if (h === '/' || h === '/es/') a.remove();
      });
      var full = document.createElement('a');
      full.href = link.getAttribute('href');
      full.innerHTML = '<span class="k">' + (es ? 'La pieza completa ·' : 'The full piece ·') + '</span> ' +
        (es ? 'El Mundo Agentivo en 2 minutos →' : 'The Agentive World in 2 minutes →');
      next.insertBefore(full, next.firstChild);
      box.appendChild(next);
    }
    return box;
  }

  function open() {
    if (!dlg) build();
    if (loaded) { dlg.showModal(); return; }
    fetch(link.getAttribute('href'))
      .then(function (r) { if (!r.ok) throw 0; return r.text(); })
      .then(function (html) {
        var doc = new DOMParser().parseFromString(html, 'text/html');
        var page = doc.querySelector('main.page');
        if (!page) throw 0;
        var body = dlg.querySelector('.peek-body');
        if (window.innerHeight >= 620 && window.innerWidth >= 760) {
          dlg.classList.add('peek-lamina');
          body.className = 'peek-body';
          body.innerHTML = '';
          body.appendChild(lamina(page));
        } else {
          body.className = 'peek-body page';
          body.innerHTML = page.innerHTML;
        }
        loaded = true;
        dlg.showModal();
      })
      .catch(function () { location.href = link.href; });
  }

  link.addEventListener('click', function (e) { e.preventDefault(); open(); });
  if (location.hash === '#2min') open();
})();
