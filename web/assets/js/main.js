/* ATES · interacciones del prototipo
   1. Respaldo local de imágenes   4. Revelado progresivo al hacer scroll
   2. Header sticky                 5. Sección activa en la navegación
   3. Menú móvil                    6. Entrada del hero
*/
(() => {
  const root = document.documentElement;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

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

  /* 3 · Menú hamburguesa */
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-menu]');
  const setMenu = (open) => {
    header.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  };
  toggle.addEventListener('click', () => setMenu(!header.classList.contains('is-open')));
  menu.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && header.classList.contains('is-open')) { setMenu(false); toggle.focus(); }
  });
  document.addEventListener('click', (e) => {
    if (header.classList.contains('is-open') && !header.contains(e.target)) setMenu(false);
  });
  window.matchMedia('(min-width: 1101px)').addEventListener('change', (e) => { if (e.matches) setMenu(false); });

  /* 4 · Revelado progresivo (una vez por elemento, con escalonado corto en grupos) */
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

  /* 5 · Marca en la navegación la sección visible */
  const links = [...document.querySelectorAll('.site-nav__list a[href^="#"]:not(.btn)')];
  const sections = [...document.querySelectorAll('main > section[id]')];
  if ('IntersectionObserver' in window && sections.length) {
    const navIO = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        links.forEach((a) => {
          if (a.getAttribute('href') === `#${entry.target.id}`) a.setAttribute('aria-current', 'true');
          else a.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach((s) => navIO.observe(s));
  }

  /* 6 · Entrada del hero, escalonada */
  document.querySelectorAll('[data-hero-item]').forEach((el, i) => {
    el.style.setProperty('--d', reduceMotion ? '0ms' : `${120 + i * 80}ms`);
  });
  requestAnimationFrame(() => requestAnimationFrame(() => document.body.classList.add('is-loaded')));
})();
