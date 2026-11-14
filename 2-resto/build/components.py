"""Componentes globales del sitio ATES (equivalentes a componentes React, renderizados a HTML).

Cada función devuelve una cadena HTML. `rel` es el prefijo relativo hasta la raíz del sitio
("", "../" o "../../"), para que el sitio funcione en cualquier subcarpeta (servidor local o GitHub Pages).
"""
import json
import os
import struct
from html import escape

ROOT = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(os.path.dirname(ROOT), "web")
IMG_DIR = os.path.join(WEB, "assets", "img", "ates")
IMAGES = json.load(open(os.path.join(ROOT, "images.json"), encoding="utf8"))
UPLOADS = "https://www.ates.es/wp-content/uploads/"
OFFICIAL = "https://www.ates.es/"
import time
VERSION = time.strftime("%Y%m%d%H%M")  # evita cachés antiguas de CSS/JS


# ---------------------------------------------------------------- utilidades
def e(text):
    return escape(text, quote=True)


def image_size(filename, folder=None):
    path = os.path.join(folder or IMG_DIR, filename)
    with open(path, "rb") as f:
        head = f.read(32)
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            return struct.unpack(">II", head[16:24])
        f.seek(2)
        while True:  # JPEG: recorre segmentos hasta SOF
            marker, = struct.unpack(">H", f.read(2))
            length, = struct.unpack(">H", f.read(2))
            if marker in (0xFFC0, 0xFFC1, 0xFFC2):
                f.read(1)
                h, w = struct.unpack(">HH", f.read(4))
                return w, h
            f.seek(length - 2, 1)


def img(rel, filename, alt, pos="50% 50%", lazy=True, cls="", priority=False):
    if filename not in IMAGES:
        raise KeyError("Imagen no registrada: " + filename)
    from crops import resolve, CROP_DIR  # import diferido: crops depende de este módulo
    cropped, pos = resolve(filename, pos)
    if cropped:
        # Recorte local de una foto oficial (díptico o pestaña lateral); se documenta la URL de origen
        w, h = image_size(cropped, CROP_DIR)
        source = [f'src="{rel}assets/img/ates/c/{cropped}"', f'data-source="{UPLOADS}{IMAGES[filename]}"']
    else:
        w, h = image_size(filename)
        source = [f'src="{UPLOADS}{IMAGES[filename]}"', f'data-fallback="{rel}assets/img/ates/{filename}"']
    attrs = source + [
        f'width="{w}" height="{h}"',
        f'alt="{e(alt)}"',
        'decoding="async"',
    ]
    if priority:
        attrs.append('fetchpriority="high"')
    elif lazy:
        attrs.append('loading="lazy"')
    if cls:
        attrs.append(f'class="{cls}"')
    if pos != "50% 50%":
        attrs.append(f'style="--pos: {pos}"')
    return "<img " + " ".join(attrs) + ">"


def icon(name, cls="icon"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'


def link(rel, path):
    """Ruta interna relativa. path='' es la home; admite anclas ('#x') y rutas de carpeta."""
    if path == "":
        return rel or "./"
    return rel + path


def ext(url, text, cls="link-arrow"):
    return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener">{text} {icon("arrow-up-right")}</a>'


# ---------------------------------------------------------------- sitio
PAGES = {}   # slug -> metadatos (se rellena desde site.py)
NAV = []     # estructura del mega menú


def page_url(rel, slug):
    return link(rel, PAGES[slug]["path"])


SPRITE = open(os.path.join(ROOT, "sprite.svg"), encoding="utf8").read()


def head(rel, page):
    og = page.get("og", "Construction-grua-ates.png")
    canonical = page.get("official")
    canon = f'\n  <link rel="canonical" href="{canonical}">' if canonical else ""
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{e(page['title'])}</title>
  <meta name="description" content="{e(page['description'])}">
  <!-- Prototipo conceptual privado: noindex hasta que ATES autorice su publicación. -->
  <meta name="robots" content="noindex, nofollow">
  <meta name="theme-color" content="#ECE8E2">{canon}
  <link rel="icon" href="{UPLOADS}2020/06/favicon.png">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_ES">
  <meta property="og:title" content="{e(page['title'])}">
  <meta property="og:description" content="{e(page['description'])}">
  <meta property="og:image" content="{UPLOADS}{IMAGES[og]}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preconnect" href="https://www.ates.es">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{rel}assets/css/styles.css?v={VERSION}">
  <script>document.documentElement.classList.add('js');</script>
</head>"""


def header(rel, area=None):
    items = []
    for group in NAV:
        gid = group["id"]
        current = ' aria-current="true"' if area == gid else ""
        entries = []
        for slug, anchor in group["items"]:
            p = PAGES[slug]
            href = page_url(rel, slug) + (anchor or "")
            label = p["nav"] if not anchor else group["anchors"][anchor]["label"]
            text = p["short"] if not anchor else group["anchors"][anchor]["short"]
            entries.append(
                f'<li><a href="{href}"><span class="mega__name">{e(label)}</span>'
                f'<span class="mega__desc">{e(text)}</span></a></li>'
            )
        feat = PAGES[group["landing"]]
        items.append(f"""
        <li class="nav-item" data-mega-item>
          <button class="nav-item__trigger" type="button" aria-expanded="false" aria-controls="mega-{gid}"{current} data-mega-trigger>
            {e(group['label'])} {icon('chevron-down', 'icon nav-item__chevron')}
          </button>
          <div class="mega" id="mega-{gid}" data-mega>
            <div class="mega__inner">
              <div class="mega__intro">
                <p class="eyebrow">{e(group['label'])}</p>
                <p class="mega__lead">{e(group['lead'])}</p>
                <a class="link-arrow" href="{page_url(rel, group['landing'])}">Ver todo {e(group['label'].lower())} {icon('arrow-right')}</a>
              </div>
              <ul class="mega__list">{''.join(entries)}</ul>
              <a class="mega__feature media" href="{page_url(rel, group['landing'])}" tabindex="-1" aria-hidden="true">
                {img(rel, group['image'], '', group.get('image_pos', '50% 50%'))}
                <span>{e(feat['nav'])}</span>
              </a>
            </div>
          </div>
        </li>""")
    return f"""
{SPRITE}
<a class="skip-link" href="#contenido">Saltar al contenido</a>
<header class="site-header" data-header>
  <div class="site-header__bar">
    <a class="site-header__logo" href="{link(rel, '')}" aria-label="ATES, ir al inicio">
      <img src="{UPLOADS}{IMAGES['Logotipo-ATES.png']}" data-fallback="{rel}assets/img/ates/Logotipo-ATES.png" width="200" height="80" alt="ATES">
    </a>
    <nav class="site-nav" aria-label="Navegación principal">
      <ul class="site-nav__list" id="menu-principal" data-menu>{''.join(items)}
        <li class="nav-item"><a class="nav-item__link" href="{link(rel, '#sobre-ates')}">Sobre ATES</a></li>
        <li class="site-nav__mobile-cta"><a class="btn btn--red" href="{page_url(rel, 'contacto')}">Solicitar asesoramiento {icon('arrow-right')}</a></li>
      </ul>
    </nav>
    <a class="btn btn--red site-header__cta" href="{page_url(rel, 'contacto')}">Solicitar asesoramiento</a>
    <button class="site-header__toggle" type="button" aria-controls="menu-principal" aria-expanded="false" aria-label="Abrir menú" data-menu-toggle>
      {icon('menu', 'icon icon--open')}{icon('x', 'icon icon--close')}
    </button>
  </div>
</header>"""


def footer(rel):
    cols = []
    for group in NAV:
        lis = "".join(
            f'<li><a href="{page_url(rel, slug)}{anchor or ""}">{e(PAGES[slug]["nav"] if not anchor else group["anchors"][anchor]["label"])}</a></li>'
            for slug, anchor in group["items"]
        )
        cols.append(f"""
      <nav class="footer__col" aria-labelledby="f-{group['id']}">
        <h2 id="f-{group['id']}"><a href="{page_url(rel, group['landing'])}">{e(group['label'])}</a></h2>
        <ul>{lis}</ul>
      </nav>""")
    return f"""
<footer class="footer">
  <div class="footer__lines" aria-hidden="true"></div>
  <div class="footer__inner wrap">
    <div class="footer__top footer__top--5">
      <div class="footer__brand">
        <img class="footer__logo" src="{UPLOADS}{IMAGES['Logotipo-ATES.png']}" data-fallback="{rel}assets/img/ates/Logotipo-ATES.png" width="200" height="80" alt="ATES" loading="lazy">
        <p>Empresa fundada en 1968, especializada en maquinaria, sistemas constructivos, elevación e innovación tecnológica, con una relación directa y personal con cada cliente.</p>
        <ul class="footer__social" aria-label="Redes sociales de ATES">
          <li><a href="https://es.linkedin.com/company/grupo-ates" target="_blank" rel="noopener" aria-label="LinkedIn">{icon('linkedin')}</a></li>
          <li><a href="https://www.youtube.com/user/GrupoAtes" target="_blank" rel="noopener" aria-label="YouTube">{icon('youtube')}</a></li>
          <li><a href="https://www.facebook.com/ATES-632923803402772/" target="_blank" rel="noopener" aria-label="Facebook">{icon('facebook')}</a></li>
          <li><a href="https://twitter.com/Grupo_Ates" target="_blank" rel="noopener" aria-label="X (Twitter)">{icon('twitter')}</a></li>
        </ul>
      </div>{''.join(cols)}
      <div class="footer__col footer__contact">
        <h2><a href="{page_url(rel, 'contacto')}">Contacto</a></h2>
        <ul>
          <li><a href="mailto:info@ates.es">{icon('mail')}<span>info@ates.es</span></a></li>
          <li><a href="tel:+34902171517">{icon('phone')}<span>(+34) 902 171 517<small>Oficinas, España</small></span></a></li>
          <li><a href="tel:+34648611411">{icon('phone')}<span>(+34) 648 611 411<small>Móvil, España</small></span></a></li>
          <li><a href="tel:+34962524400">{icon('wrench')}<span>962 524 400<small>Aviso de averías 24 horas</small></span></a></li>
          <li><a href="{OFFICIAL}" target="_blank" rel="noopener">{icon('globe')}<span>www.ates.es</span></a></li>
        </ul>
      </div>
    </div>
    <p class="footer__statement" aria-hidden="true">Maquinaria <span>·</span> Construcción <span>·</span> Tecnologías</p>
    <div class="footer__bottom">
      <ul class="footer__legal">
        <li><a href="{OFFICIAL}aviso-legal-es/" target="_blank" rel="noopener">Aviso legal</a></li>
        <li><a href="{OFFICIAL}politica-de-privacidad/" target="_blank" rel="noopener">Política de privacidad</a></li>
        <li><a href="{OFFICIAL}politica-de-cookies/" target="_blank" rel="noopener">Política de cookies</a></li>
        <li><a href="{OFFICIAL}clausula-clientes-lopd/" target="_blank" rel="noopener">Cláusula clientes LOPD</a></li>
        <li><a href="{OFFICIAL}certificados-de-calidad/" target="_blank" rel="noopener">Certificados de calidad</a></li>
      </ul>
      <p class="footer__note">Prototipo conceptual de rediseño, no oficial. Logotipo, textos y fotografías © ATES, utilizados con fines de presentación.</p>
    </div>
  </div>
</footer>
<script src="{rel}assets/js/main.js?v={VERSION}" defer></script>
</body>
</html>
"""


def document(rel, page, body, area=None, body_class=""):
    cls = f' class="{body_class}"' if body_class else ""
    return head(rel, page) + f"\n<body{cls}>" + header(rel, area) + f'\n<main id="contenido">{body}\n</main>' + footer(rel)


# ---------------------------------------------------------------- bloques de página
def breadcrumbs(rel, trail):
    """trail: lista de (texto, slug|None). El último es la página actual."""
    lis = []
    for i, (text, slug) in enumerate(trail):
        if i == len(trail) - 1:
            lis.append(f'<li><span aria-current="page">{e(text)}</span></li>')
        else:
            href = link(rel, "") if slug == "" else page_url(rel, slug)
            lis.append(f'<li><a href="{href}">{e(text)}</a></li>')
    return f'<nav class="crumbs" aria-label="Ruta de navegación"><ol>{"".join(lis)}</ol></nav>'


def page_hero(rel, *, variant, eyebrow, title, lead, image, alt, pos="50% 50%", trail, actions="", aside="", tag=""):
    """variant: 'frame' (foto a sangre en contenedor), 'split' (texto + foto) o 'dark' (tecnología)."""
    crumbs = breadcrumbs(rel, trail)
    tag_html = f'<figcaption class="media__tag">{e(tag)}</figcaption>' if tag else ""
    if variant in ("frame", "dark"):
        return f"""
  <section class="phero phero--{variant}" aria-labelledby="page-title">
    <div class="phero__frame">
      {img(rel, image, alt, pos, cls='phero__img', priority=True)}
      <div class="phero__shade" aria-hidden="true"></div>
      <div class="phero__top">{crumbs}</div>
      <div class="phero__content">
        <p class="eyebrow eyebrow--light" data-hero-item>{e(eyebrow)}</p>
        <h1 class="phero__title" id="page-title" data-hero-item>{title}</h1>
        <p class="phero__lead" data-hero-item>{lead}</p>
        <div class="hero__actions" data-hero-item>{actions}</div>
      </div>{aside}
    </div>
  </section>"""
    return f"""
  <section class="phero phero--split" aria-labelledby="page-title">
    <div class="phero__split">
      <div class="phero__text">
        {crumbs}
        <p class="eyebrow" data-hero-item>{e(eyebrow)}</p>
        <h1 class="phero__title phero__title--dark" id="page-title" data-hero-item>{title}</h1>
        <p class="lead" data-hero-item>{lead}</p>
        <div class="hero__actions" data-hero-item>{actions}</div>
      </div>
      <figure class="phero__media media" data-hero-item>
        {img(rel, image, alt, pos, priority=True)}{tag_html}
      </figure>
    </div>
  </section>"""


def actions_service(rel, subject):
    from urllib.parse import quote
    return (
        f'<a class="btn btn--red" href="{page_url(rel, "contacto")}?asunto={quote(subject)}#formulario">Solicitar información {icon("arrow-right")}</a>'
        f'<a class="btn btn--line" href="tel:+34902171517">{icon("phone")} 902 171 517</a>'
    )


def section_head(eyebrow, title, aside="", center=False, light=False, hid=""):
    cls = " section-head--center" if center else ""
    ey = " eyebrow--light" if light else ""
    h2 = " h2--light" if light else ""
    idattr = f' id="{hid}"' if hid else ""
    aside_html = f'<div class="section-head__aside">{aside}</div>' if aside else ""
    return f"""
      <header class="section-head{cls}" data-reveal>
        <div>
          <p class="eyebrow{ey}">{e(eyebrow)}</p>
          <h2 class="h2{h2}"{idattr}>{title}</h2>
        </div>{aside_html}
      </header>"""


def specs(rows, title="Datos técnicos publicados", note="Fuente: catálogo publicado en ates.es."):
    lis = "".join(f"<div><dt>{e(k)}</dt><dd>{v}</dd></div>" for k, v in rows)
    return f"""
        <div class="specs" data-reveal>
          <h3 class="specs__title">{icon('ruler')} {e(title)}</h3>
          <dl>{lis}</dl>
          <p class="specs__note">{e(note)}</p>
        </div>"""


def features(items, cols=3, light=False):
    lis = "".join(
        f'<li data-reveal>{icon(ic)}<div><h3>{e(t)}</h3><p>{d}</p></div></li>' for ic, t, d in items
    )
    cls = " features--light" if light else ""
    return f'<ul class="features features--{cols}{cls}" data-reveal-group>{lis}</ul>'


def gallery(rel, items, cls=""):
    figs = []
    for it in items:
        f, alt, cap_t, cap_s = it[0], it[1], it[2], it[3]
        pos = it[4] if len(it) > 4 else "50% 50%"
        size = it[5] if len(it) > 5 else ""
        figs.append(
            f'<figure class="gal__item media {size}" data-reveal>{img(rel, f, alt, pos)}'
            f'<figcaption><strong>{e(cap_t)}</strong>{e(cap_s)}</figcaption></figure>'
        )
    return f'<div class="gal {cls}" data-reveal-group>{"".join(figs)}</div>'


def related(rel, slugs, title="Soluciones relacionadas", eyebrow="Sigue explorando"):
    cards = []
    for s in slugs:
        p = PAGES[s]
        cards.append(f"""
          <a class="rel-card" href="{page_url(rel, s)}" data-reveal>
            <figure class="rel-card__media media">{img(rel, p['card'], p['card_alt'], p.get('card_pos', '50% 50%'))}</figure>
            <span class="rel-card__area">{e(p['area_label'])}</span>
            <span class="rel-card__title">{e(p['nav'])}</span>
            <span class="rel-card__desc">{e(p['short'])}</span>
            <span class="rel-card__arrow" aria-hidden="true">{icon('arrow-up-right')}</span>
          </a>""")
    return f"""
  <section class="section related" aria-labelledby="rel-title">
    <div class="wrap">
      {section_head(eyebrow, title, hid='rel-title')}
      <div class="rel-grid" data-reveal-group>{''.join(cards)}</div>
    </div>
  </section>"""


def contact_cta(rel, subject, title="¿Necesitas una solución para tu proyecto?",
                text="Cuéntanos qué necesitas y nuestro equipo técnico te ayudará a encontrar la alternativa más adecuada.",
                image="Encofrados-serie-pesada-ATES-Construction.png", pos="50% 60%"):
    from urllib.parse import quote
    return f"""
  <section class="cta" aria-labelledby="cta-title">
    <div class="cta__frame">
      {img(rel, image, '', pos, cls='cta__img')}
      <div class="cta__shade" aria-hidden="true"></div>
      <div class="cta__content" data-reveal>
        <p class="eyebrow eyebrow--light">Hablemos de tu proyecto</p>
        <h2 class="cta__title" id="cta-title">{e(title)}</h2>
        <p class="lead lead--light">{e(text)}</p>
        <div class="cta__actions">
          <a class="btn btn--red btn--lg" href="{page_url(rel, 'contacto')}?asunto={quote(subject)}#formulario">Solicitar información {icon('arrow-right')}</a>
          <a class="btn btn--glass btn--lg" href="{page_url(rel, 'contacto')}">Contactar con ATES</a>
        </div>
        <ul class="cta__direct">
          <li><a href="tel:+34902171517">{icon('phone')}(+34) 902 171 517</a></li>
          <li><a href="mailto:info@ates.es">{icon('mail')}info@ates.es</a></li>
        </ul>
      </div>
    </div>
  </section>"""


def source_note(url, text="Contenido basado en la página oficial"):
    return f'<p class="source-note">{icon("link")} {e(text)}: <a href="{url}" target="_blank" rel="noopener">{e(url.replace("https://www.", ""))}</a></p>'
