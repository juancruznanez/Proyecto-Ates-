/* ATES · interacciones del prototipo
   1. Respaldo local de imágenes     5. Revelado progresivo al hacer scroll
   2. Header sticky                   6. Sección activa (home)
   3. Mega menú                       7. Catálogo con filtros
   4. Menú móvil                      8. Formulario de contacto
   9. Entrada del hero
*/
(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const desktop = window.matchMedia('(min-width: 1101px)');
  const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');

  /* 1 · Las fotos se sirven desde ates.es; si alguna falla, se usa la copia local */
  document.querySelectorAll('img[data-fallback]').forEach((img) => {
    const useFallback = () => {
      if (img.dataset.fellBack) return;
      img.dataset.fellBack = 'true';
      img.src = img.dataset.fallback;
    };
    img.addEventListener('error', useFallback);
    if (img.complete && img.naturalWidth === 0 && img.currentSrc) useFallback();
  });

  /* 2 · Header: sombra al hacer scroll */
  const header = document.querySelector('[data-header]');
  const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 24);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* 3 · Mega menú: clic o teclado en cualquier dispositivo; hover con retardo solo con ratón */
  const megaItems = [...document.querySelectorAll('[data-mega-item]')];
  let hoverTimer;
  const setMega = (item, open) => {
    item.classList.toggle('is-open', open);
    item.querySelector('[data-mega-trigger]').setAttribute('aria-expanded', String(open));
  };
  const closeAllMega = (except) => megaItems.forEach((it) => { if (it !== except) setMega(it, false); });
  megaItems.forEach((item) => {
    const trigger = item.querySelector('[data-mega-trigger]');
    trigger.addEventListener('click', () => {
      const open = !item.classList.contains('is-open');
      closeAllMega(item);
      setMega(item, open);
    });
    item.addEventListener('pointerenter', (e) => {
      if (!desktop.matches || !finePointer.matches || e.pointerType !== 'mouse') return;
      clearTimeout(hoverTimer);
      const anyOpen = megaItems.some((it) => it.classList.contains('is-open'));
      // Primera apertura con pequeño retardo; si ya hay uno abierto, cambio instantáneo
      hoverTimer = setTimeout(() => { closeAllMega(item); setMega(item, true); }, anyOpen ? 0 : 120);
    });
    item.addEventListener('pointerleave', (e) => {
      if (!desktop.matches || e.pointerType !== 'mouse') return;
      clearTimeout(hoverTimer);
      hoverTimer = setTimeout(() => setMega(item, false), 220);
    });
    item.addEventListener('focusout', (e) => {
      if (desktop.matches && !item.contains(e.relatedTarget)) setMega(item, false);
    });
  });

  /* 4 · Menú hamburguesa */
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-menu]');
  const setMenu = (open) => {
    header.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    if (!open) closeAllMega();
  };
  toggle.addEventListener('click', () => setMenu(!header.classList.contains('is-open')));
  menu.addEventListener('click', (e) => {
    if (e.target.closest('a')) { setMenu(false); closeAllMega(); }
  });
  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape') return;
    const openItem = megaItems.find((it) => it.classList.contains('is-open'));
    if (openItem && desktop.matches) { setMega(openItem, false); openItem.querySelector('[data-mega-trigger]').focus(); return; }
    if (header.classList.contains('is-open')) { setMenu(false); toggle.focus(); }
  });
  document.addEventListener('click', (e) => {
    if (header.contains(e.target)) return;
    closeAllMega();
    if (header.classList.contains('is-open')) setMenu(false);
  });
  desktop.addEventListener('change', () => { setMenu(false); closeAllMega(); });

  /* 5 · Revelado progresivo */
  document.querySelectorAll('[data-reveal-group]').forEach((group) => {
    group.querySelectorAll('[data-reveal]').forEach((el, i) => {
      el.style.setProperty('--d', `${Math.min(i * 70, 280)}ms`);
    });
  });
  const revealables = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealables.forEach((el) => io.observe(el));
  } else {
    revealables.forEach((el) => el.classList.add('is-visible'));
  }

  /* 6 · Home: marca "Sobre ATES" cuando la sección está a la vista */
  const homeLinks = [...document.querySelectorAll('.site-nav__list a[href^="#"]:not(.btn)')];
  if ('IntersectionObserver' in window && homeLinks.length) {
    const sections = [...document.querySelectorAll('main > section[id]')];
    const navIO = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        homeLinks.forEach((a) => {
          if (a.getAttribute('href') === `#${entry.target.id}`) a.setAttribute('aria-current', 'true');
          else a.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach((s) => navIO.observe(s));
  }

  /* 7 · Catálogo de maquinaria auxiliar */
  const filters = document.querySelector('[data-filters]');
  if (filters) {
    const products = [...document.querySelectorAll('[data-products] [data-cat]')];
    const count = filters.querySelector('[data-count]');
    const apply = (cat) => {
      let n = 0;
      products.forEach((p) => {
        const show = cat === 'todos' || p.dataset.cat === cat;
        p.hidden = !show;
        if (show) { n += 1; p.classList.add('is-visible'); }
      });
      filters.querySelectorAll('[data-filter]').forEach((b) => {
        const active = b.dataset.filter === cat;
        b.classList.toggle('is-active', active);
        b.setAttribute('aria-pressed', String(active));
      });
      if (count) count.textContent = `${n} ${n === 1 ? 'equipo' : 'equipos'}`;
    };
    filters.addEventListener('click', (e) => {
      const btn = e.target.closest('[data-filter]');
      if (btn) apply(btn.dataset.filter);
    });
    const alias = document.querySelector(`[data-filter-alias][id="${location.hash.slice(1)}"]`);
    if (alias) {
      apply(alias.dataset.filterAlias);
      requestAnimationFrame(() => document.getElementById('catalogo').scrollIntoView());
    }
  }

  /* 8 · Formulario de contacto: prepara un correo a info@ates.es (no envía datos a terceros) */
  const form = document.querySelector('[data-contact-form]');
  if (form) {
    const subject = form.querySelector('[data-subject]');
    const wanted = new URLSearchParams(location.search).get('asunto');
    if (wanted) {
      let opt = [...subject.options].find((o) => o.value === wanted);
      if (!opt) { opt = new Option(wanted, wanted); subject.add(opt, 0); }
      subject.value = wanted;
    }
    const error = form.querySelector('[data-form-error]');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const fields = { nombre: form.nombre, email: form.email, mensaje: form.mensaje };
      let valid = true;
      Object.values(fields).forEach((f) => {
        const ok = f.value.trim() !== '' && (f.type !== 'email' || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.value.trim()));
        f.setAttribute('aria-invalid', String(!ok));
        if (!ok) valid = false;
      });
      error.hidden = valid;
      if (!valid) { form.querySelector('[aria-invalid="true"]').focus(); return; }
      const lines = [
        `Nombre: ${data.get('nombre')}`,
        data.get('empresa') ? `Empresa: ${data.get('empresa')}` : '',
        `Email: ${data.get('email')}`,
        data.get('telefono') ? `Teléfono: ${data.get('telefono')}` : '',
        '',
        data.get('mensaje'),
      ].filter((l, i) => l !== '' || i === 4);
      const href = `mailto:info@ates.es?subject=${encodeURIComponent(`Solicitud de información: ${data.get('asunto')}`)}&body=${encodeURIComponent(lines.join('\n'))}`;
      window.location.href = href;
    });
  }

  /* 9 · Entrada del hero, escalonada */
  document.querySelectorAll('[data-hero-item]').forEach((el, i) => {
    el.style.setProperty('--d', reduceMotion ? '0ms' : `${120 + i * 80}ms`);
  });
  requestAnimationFrame(() => requestAnimationFrame(() => document.body.classList.add('is-loaded')));
})();
