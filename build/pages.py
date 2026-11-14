"""Registro de páginas, navegación y contenido del sitio ATES.

Todo el contenido técnico procede de ates.es (ver AUDITORIA.md). Ejecutar con: python3 build/build.py
"""
from components import (PAGES, NAV, OFFICIAL, img, icon, link, page_url, e, ext,
                        page_hero, section_head, specs, features, gallery, related,
                        contact_cta, actions_service, source_note, breadcrumbs)

# ======================================================================= REGISTRO
def reg(slug, **kw):
    PAGES[slug] = kw


reg("home", path="", title="ATES | Maquinaria, Construcción y Tecnologías",
    description="Descubre las soluciones de ATES en maquinaria, sistemas constructivos e innovación tecnológica para proyectos industriales y de construcción.",
    nav="Inicio", short="", area=None, area_label="", card="Construction-grua-ates.png", card_alt="", official=OFFICIAL)

# ---- Maquinaria
reg("maquinaria", path="maquinaria/", title="Maquinaria de elevación y maquinaria auxiliar | ATES",
    description="Grúas torre y automontantes, montacargas de obra y maquinaria auxiliar en alquiler y venta, con servicio técnico propio de ATES.",
    nav="Maquinaria", short="Elevación y maquinaria auxiliar para obra.", area="maquinaria", area_label="Maquinaria",
    card="Gruas-Torre-ATES-Construction.png", card_alt="Grúas torre ATES en obra frente al mar", card_pos="10% 50%",
    og="Gruas-Torre-ATES-Construction.png")
reg("gruas", path="maquinaria/gruas-torre-automontantes/", title="Grúas torre y grúas automontantes en alquiler y venta | ATES",
    description="Gran diversidad de modelos de grúas torre y grúas automontantes para la construcción, en alquiler y venta, con un servicio técnico de más de 40 años de experiencia.",
    nav="Grúas torre y automontantes", short="Modelos para obra, en alquiler y venta.", area="maquinaria", area_label="Maquinaria",
    card="Construction-grua-ates.png", card_alt="Grúa torre ATES amarilla", card_pos="58% 40%",
    official=OFFICIAL + "servicios/construccion/", og="Construction-grua-ates.png")
reg("montacargas", path="maquinaria/montacargas/", title="Montacargas y elevadores de obra de 500 a 2.000 kg | ATES",
    description="Montacargas de obra de 500 a 2.000 kg para palet europeo o pladur, con homologación para subir personas. Amplio parque en alquiler.",
    nav="Montacargas y elevadores", short="De 500 a 2.000 kg, homologados para personas.", area="maquinaria", area_label="Maquinaria",
    card="Montacargas-Ates-Construction.png", card_alt="Montacargas instalado en un edificio en altura", card_pos="42% 50%",
    official=OFFICIAL + "servicios/construccion/", og="Montacargas-Ates-Construction.png")
reg("auxiliar", path="maquinaria/maquinaria-auxiliar/", title="Maquinaria auxiliar de construcción: catálogo | ATES",
    description="Grupos electrógenos, compactación, dumpers, carretillas, compresores, plataformas de tijera, brazos articulados y más maquinaria auxiliar en venta y alquiler.",
    nav="Maquinaria auxiliar", short="Catálogo de 13 familias de equipos.", area="maquinaria", area_label="Maquinaria",
    card="Dumpers-maquinaria-auxiliar-construction-ATES.png", card_alt="Dumper de la flota ATES", card_pos="88% 50%",
    official=OFFICIAL + "servicios/construccion/maquinaria-auxiliar/", og="Dumpers-maquinaria-auxiliar-construction-ATES.png")

# ---- Construcción
reg("construccion", path="construccion/", title="Sistemas de construcción: andamios, encofrados y plataformas | ATES",
    description="Andamios, encofrados y apuntalamientos, cimbras, estabilizadores de fachada, escaleras de acceso y plataformas motorizadas en alquiler y venta.",
    nav="Construcción", short="Sistemas constructivos para obra nueva y rehabilitación.", area="construccion", area_label="Construcción",
    card="Plataformas-ATES-motorizadas-obra-nueva.png", card_alt="Plataformas motorizadas en fachada de obra nueva", card_pos="34% 50%",
    official=OFFICIAL + "servicios/construccion/", og="Plataformas-ATES-motorizadas-obra-nueva.png")
reg("andamios", path="construccion/andamios/", title="Andamios de marco y multidireccional europeo | ATES",
    description="Andamio de marco europeo y multidireccional en alquiler y venta, conforme a UNE-EN 12810 y UNE-EN 12811. Uno de los mayores parques de la Comunidad Valenciana.",
    nav="Andamios", short="Marco europeo y multidireccional, UNE-EN 12810/12811.", area="construccion", area_label="Construcción",
    card="Andamios-cara-sur-2-scaled.jpg", card_alt="Andamiaje ATES en el Castillo de los Funes", card_pos="66% 55%",
    official=OFFICIAL + "servicios/construccion/andamios/", og="Andamios-cara-sur-2-scaled.jpg")
reg("encofrados", path="construccion/encofrados-apuntalamientos/", title="Encofrados y apuntalamientos para muros, pilares y forjados | ATES",
    description="Encofrados de serie ligera (40 kN/m²) y pesada (60 kN/m²), pilares hasta 60 × 60 cm, encofrado de planta, cerchas y puntales de 1 a 6 metros.",
    nav="Encofrados y apuntalamientos", short="Muros, pilares, forjados, cerchas y puntales.", area="construccion", area_label="Construcción",
    card="Encofrados-apuntalamientos-ATES-Construction.png", card_alt="Puntales sosteniendo un forjado", card_pos="55% 50%",
    official=OFFICIAL + "servicios/construccion/", og="Encofrados-apuntalamientos-ATES-Construction.png")
reg("cimbras", path="construccion/cimbras-apeos/", title="Cimbras y apeos estructurales multidireccionales | ATES",
    description="Cimbras y apeos estructurales con unión multidireccional para apear encofrados, cimbras cuajadas y torres independientes, de montaje rápido.",
    nav="Cimbras y apeos", short="Sustentación de cargas y apeo de encofrados.", area="construccion", area_label="Construcción",
    card="Cimbras-y-apeos-estructurales-ATES-Construction.png", card_alt="Cimbra multidireccional bajo un encofrado de madera", card_pos="62% 50%",
    official=OFFICIAL + "servicios/construccion/andamios/", og="Cimbras-y-apeos-estructurales-ATES-Construction.png")
reg("plataformas", path="construccion/plataformas-motorizadas/", title="Plataformas motorizadas para obra nueva y rehabilitación | ATES",
    description="Plataformas motorizadas sobre mástil con cremallera, homologadas con marcado CE, para cerramientos de fachada, rehabilitación y trabajos en edificios altos.",
    nav="Plataformas motorizadas", short="Para fachadas de obra nueva y rehabilitación.", area="construccion", area_label="Construcción",
    card="Plataformas-ATES-Construction-motorizadas-rehabilitacion-fachadas.png", card_alt="Plataformas motorizadas ATES en una fachada", card_pos="72% 50%",
    official=OFFICIAL + "servicios/construccion/plataformas-motorizadas/", og="Plataformas-ATES-Construction-motorizadas-rehabilitacion-fachadas.png")
reg("estabilizadores", path="construccion/estabilizadores-fachadas/", title="Estabilizadores de fachadas | ATES",
    description="Sistema versátil y diáfano para la sustentación y estabilización de fachadas o estructuras frente a los esfuerzos del viento.",
    nav="Estabilizadores de fachadas", short="Sustentación de fachadas frente al viento.", area="construccion", area_label="Construcción",
    card="Estabilizadores-de-fachada-ATES-Construction.png", card_alt="Estabilizador de fachada en edificio histórico", card_pos="60% 50%",
    official=OFFICIAL + "servicios/construccion/andamios/", og="Estabilizadores-de-fachada-ATES-Construction.png")
reg("escaleras", path="construccion/escaleras-acceso/", title="Escaleras de acceso y servicio para obra | ATES",
    description="Escaleras de acceso y servicio que se adaptan a cualquier tipología, para acceso público o privativo, con desembarco seguro del usuario.",
    nav="Escaleras de acceso", short="Acceso público o privativo con desembarco seguro.", area="construccion", area_label="Construcción",
    card="Escaleras-de-acceso-ATES-Construction.png", card_alt="Torre de escalera de obra con cartel de Andamios ATES", card_pos="55% 50%",
    official=OFFICIAL + "servicios/construccion/andamios/", og="Escaleras-de-acceso-ATES-Construction.png")

# ---- Tecnologías
reg("tecnologias", path="tecnologias/", title="ATES Technologies: inspección inteligente de infraestructuras | ATES",
    description="Robótica, sensorización e inteligencia artificial para la inspección de infraestructuras civiles e industriales. Spin-off de ATES.",
    nav="Tecnologías", short="Robótica, sensorización e inteligencia artificial.", area="tecnologias", area_label="Tecnologías",
    card="Inspecciones-Inteligentes-ATES-Technologies.png", card_alt="Presa de hormigón vista desde el aire", card_pos="50% 55%",
    official=OFFICIAL + "servicios/tecnologias/", og="Inspecciones-Inteligentes-ATES-Technologies.png")
reg("inspeccion", path="tecnologias/inspeccion-infraestructuras/", title="Inspección de tuberías forzadas y canales con rover | ATES Technologies",
    description="Rover propio para inspeccionar tuberías forzadas, canales de carga y galerías de centrales hidráulicas, con inspección visual y modelizado 3D.",
    nav="Inspección de infraestructuras", short="Rover para tuberías forzadas, canales y galerías.", area="tecnologias", area_label="Tecnologías",
    card="Inspecciones-infraestructuras-hidraulicas-rover-proyectos-Ates.png", card_alt="Rover de inspección iluminando el interior de una tubería", card_pos="100% 50%",
    official="https://www.ates.es/ates-technologies-inteligencia-artificial-y-grandes-infraestructuras/", og="Inspecciones-infraestructuras-hidraulicas-rover-proyectos-Ates.png")
reg("shm", path="tecnologias/monitorizacion-estructural/", title="Monitorización estructural (SHM) con Big Data y Machine Learning | ATES Technologies",
    description="Structural Health Monitoring para presas, puentes, túneles y estructuras singulares: análisis de datos de sensores en tiempo real con Big Data, Data Mining y Machine Learning.",
    nav="Monitorización estructural (SHM)", short="Sensores, Big Data y Machine Learning.", area="tecnologias", area_label="Tecnologías",
    card="SHM-Ingenieria-artificial_Technologies_Ates_001.png", card_alt="Tableta mostrando los puntos de control de una presa", card_pos="100% 50%",
    official="https://www.ates.es/ates-technologies-inteligencia-artificial-y-grandes-infraestructuras/", og="SHM-Ingenieria-artificial_Technologies_Ates_001.png")
reg("ia", path="tecnologias/inteligencia-artificial/", title="Inteligencia artificial aplicada a infraestructuras | ATES Technologies",
    description="Proyectos de inteligencia artificial, Big Data, Deep Learning y Machine Learning: detección temprana de incendios en explotaciones mineras y análisis de infraestructuras.",
    nav="Inteligencia artificial", short="Big Data, Deep Learning, ML y Digital Twin.", area="tecnologias", area_label="Tecnologías",
    card="Proyectos-Inteligencia-Artificial-Big-Data-ATES-Technologies.png", card_alt="Tableta con la marca ATES Technologies sobre una mesa interactiva", card_pos="70% 50%",
    official="https://www.ates.es/ates-technologies-inteligencia-artificial-y-grandes-infraestructuras/", og="Proyectos-Inteligencia-Artificial-Big-Data-ATES-Technologies.png")

reg("contacto", path="contacto/", title="Contacto y asesoramiento técnico | ATES",
    description="Solicita asesoramiento a ATES para maquinaria, sistemas constructivos o tecnologías. Teléfono 902 171 517 y info@ates.es.",
    nav="Contacto", short="", area=None, area_label="", card="Construction-grua-ates.png", card_alt="", official=OFFICIAL + "contacto/")
reg("404", path="404.html", title="Página no encontrada | ATES", description="La página que buscas no existe en este prototipo.",
    nav="404", short="", area=None, area_label="", card="Construction-grua-ates.png", card_alt="")

NAV.extend([
    {"id": "maquinaria", "label": "Maquinaria", "landing": "maquinaria",
     "lead": "Equipos de elevación y maquinaria auxiliar para obra, en alquiler y venta.",
     "image": "Gruas-Torre-ATES-Construction.png", "image_pos": "18% 50%",
     "items": [("gruas", "#gruas-torre"), ("gruas", "#automontantes"), ("montacargas", None), ("auxiliar", None)],
     "anchors": {"#gruas-torre": {"label": "Grúas torre", "short": "Gran diversidad de modelos para obra."},
                 "#automontantes": {"label": "Grúas automontantes", "short": "Varios modelos, alquiler y venta."}}},
    {"id": "construccion", "label": "Construcción", "landing": "construccion",
     "lead": "Sistemas constructivos para obra nueva, rehabilitación y cerramiento de fachadas.",
     "image": "Andamios-cara-sur-2-scaled.jpg", "image_pos": "66% 55%",
     "items": [("andamios", None), ("encofrados", None), ("cimbras", None), ("plataformas", None),
               ("estabilizadores", None), ("escaleras", None)], "anchors": {}},
    {"id": "tecnologias", "label": "Tecnologías", "landing": "tecnologias",
     "lead": "ATES Technologies: robótica, sensorización e inteligencia artificial aplicadas a infraestructuras.",
     "image": "Inspecciones-infraestructuras-hidraulicas-rover-proyectos-Ates.png", "image_pos": "100% 50%",
     "items": [("inspeccion", None), ("shm", None), ("ia", None)], "anchors": {}},
])


# ======================================================================= utilidades de contenido
def T(rel, slug):  # migas comunes
    p = PAGES[slug]
    area = p["area"]
    trail = [("Inicio", "")]
    if area and slug != area:
        trail.append((PAGES[area]["nav"], area))
    trail.append((p["nav"], None))
    return trail


def chips(items):
    return '<ul class="tags">' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def checklist(items, light=False):
    cls = " checklist--light" if light else ""
    return f'<ul class="checklist{cls}">' + "".join(f"<li>{icon('check')}<span>{i}</span></li>" for i in items) + "</ul>"


def family_cards(rel, slugs, big_first=True):
    out = []
    for i, s in enumerate(slugs):
        p = PAGES[s]
        big = " fam--big" if (big_first and i == 0) else ""
        out.append(f"""
        <a class="fam{big}" href="{page_url(rel, s)}" data-reveal>
          {img(rel, p['card'], p['card_alt'], p.get('card_pos', '50% 50%'))}
          <span class="fam__body">
            <span class="fam__num">{i + 1:02d}</span>
            <span class="fam__title">{e(p['nav'])}</span>
            <span class="fam__desc">{e(p['short'])}</span>
          </span>
          <span class="tile__arrow" aria-hidden="true">{icon('arrow-up-right')}</span>
        </a>""")
    return "".join(out)


# ======================================================================= HOME
def home(rel):
    P = lambda s: page_url(rel, s)
    return f"""
  <section class="hero" id="inicio" aria-labelledby="hero-title">
    <div class="hero__frame">
      {img(rel, 'Construction-grua-ates.png', 'Grúa torre con la marca ATES en la contrapluma, sobre cielo azul', cls='hero__img', priority=True)}
      <div class="hero__shade" aria-hidden="true"></div>
      <div class="hero__content">
        <p class="eyebrow eyebrow--light hero__eyebrow" data-hero-item>Maquinaria · Construcción · Tecnología</p>
        <h1 class="hero__title" id="hero-title" data-hero-item>Soluciones que impulsan cada proyecto.</h1>
        <p class="hero__lead" data-hero-item>Maquinaria, sistemas constructivos y tecnología para responder a los desafíos de la construcción y la industria.</p>
        <div class="hero__actions" data-hero-item>
          <a class="btn btn--white" href="#soluciones">Explorar soluciones {icon('arrow-right')}</a>
          <a class="btn btn--glass" href="{P('contacto')}">Contactar con ATES</a>
        </div>
      </div>
      <ul class="hero__chips" aria-label="Por qué ATES">
        <li data-hero-item>{icon('check')}Más de 50 años de experiencia</li>
        <li data-hero-item>{icon('check')}Alquiler y venta</li>
        <li data-hero-item>{icon('check')}Asesoramiento técnico</li>
      </ul>
    </div>
  </section>

  <section class="trust" aria-label="ATES en datos">
    <ul class="trust__list">
      <li class="trust__item" data-reveal><span class="trust__kicker">Desde</span><strong class="trust__figure">1968</strong><span class="trust__label">Fundada como empresa de maquinaria</span></li>
      <li class="trust__item" data-reveal><span class="trust__kicker">Más de</span><strong class="trust__figure">50<span>años</span></strong><span class="trust__label">de experiencia avalan nuestra calidad</span></li>
      <li class="trust__item" data-reveal><span class="trust__kicker">Soluciones de</span><strong class="trust__figure trust__figure--text">Alquiler<br>y venta</strong><span class="trust__label">de maquinaria y equipos para obra</span></li>
      <li class="trust__item" data-reveal><span class="trust__kicker">Atención y</span><strong class="trust__figure trust__figure--text">Asesoría<br>técnica</strong><span class="trust__label">departamento técnico propio para cada obra</span></li>
    </ul>
  </section>

  <section class="about section" id="sobre-ates" aria-labelledby="about-title">
    <div class="about__grid wrap">
      <div class="about__text" data-reveal>
        <p class="eyebrow">Sobre ATES</p>
        <h2 class="h2" id="about-title">Experiencia que transforma los desafíos en soluciones.</h2>
        <p class="lead">ATES ofrece soluciones especializadas en maquinaria, construcción, elevación e innovación tecnológica. Un equipo profesional que combina experiencia, capacidad técnica y compromiso con cada proyecto, desde su fundación en 1968.</p>
        <ul class="about__facts">
          <li>{icon('wrench')}<span><strong>Departamento técnico cualificado</strong> que estudia cada proyecto para proponer la solución más adecuada.</span></li>
          <li>{icon('layers')}<span><strong>Equipo experimentado de montadores</strong> y una amplia red técnico-comercial con asesoramiento personalizado.</span></li>
          <li>{icon('shield')}<span><strong>Certificados por SGS</strong> en ISO 9001, ISO 14001 e ISO 45001.</span></li>
        </ul>
        {ext(OFFICIAL + 'sobre-nosotros/', 'Conoce la historia de ATES', 'btn btn--dark')}
      </div>
      <figure class="about__media media" data-reveal>
        {img(rel, 'Plataformas-ATES-Construction-motorizadas-rehabilitacion-fachadas.png', 'Plataformas motorizadas ATES trabajando en la rehabilitación de una fachada', '72% 50%')}
        <figcaption class="media__tag">Plataformas motorizadas ATES en rehabilitación de fachadas</figcaption>
      </figure>
    </div>
  </section>

  <section class="services section" id="soluciones" aria-labelledby="services-title">
    <div class="wrap">
      {section_head('Áreas de negocio', 'Todo lo que necesitas para hacer avanzar tu proyecto.', '<p>Tres áreas especializadas que integran maquinaria, sistemas constructivos e innovación tecnológica.</p>', hid='services-title')}
      <article class="area area--img-left" data-reveal>
        <figure class="area__media media">{img(rel, 'Gruas-Torre-ATES-Construction.png', 'Grúas torre ATES en una obra frente al mar', '0% 50%')}<span class="area__index" aria-hidden="true">01</span></figure>
        <div class="area__body">
          <p class="eyebrow">Maquinaria</p>
          <h3 class="h3">Equipos de elevación y maquinaria para cada desafío.</h3>
          <p>Grúas torre y automontantes, montacargas de obra y un catálogo de maquinaria auxiliar en alquiler y venta.</p>
          <ul class="tags"><li><a href="{P('gruas')}#gruas-torre">Grúas torre</a></li><li><a href="{P('gruas')}#automontantes">Grúas automontantes</a></li><li><a href="{P('montacargas')}">Montacargas</a></li><li><a href="{P('auxiliar')}">Maquinaria auxiliar</a></li></ul>
          <a class="btn btn--dark" href="{P('maquinaria')}">Explorar maquinaria {icon('arrow-right')}</a>
        </div>
      </article>
      <article class="area area--img-right" data-reveal>
        <figure class="area__media media">{img(rel, 'Construction-andamios-estructuras-edificios.png', 'Montador con casco naranja trabajando entre plataformas de andamio')}<span class="area__index" aria-hidden="true">02</span></figure>
        <div class="area__body">
          <p class="eyebrow">Construcción</p>
          <h3 class="h3">Sistemas constructivos para obra nueva y rehabilitación.</h3>
          <p>Andamios, encofrados, cimbras y plataformas motorizadas, con estudio técnico de cada obra y equipo propio de montadores.</p>
          <ul class="tags"><li><a href="{P('andamios')}">Andamios</a></li><li><a href="{P('encofrados')}">Encofrados</a></li><li><a href="{P('cimbras')}">Cimbras y apeos</a></li><li><a href="{P('plataformas')}">Plataformas motorizadas</a></li><li><a href="{P('estabilizadores')}">Estabilizadores</a></li><li><a href="{P('escaleras')}">Escaleras de acceso</a></li></ul>
          <a class="btn btn--dark" href="{P('construccion')}">Explorar construcción {icon('arrow-right')}</a>
        </div>
      </article>
      <article class="area area--panoramic" data-reveal>
        <figure class="area__media media">{img(rel, 'Inspecciones-Inteligentes-ATES-Technologies.png', 'Vista aérea de una presa de hormigón, infraestructura objeto de inspección inteligente', '50% 55%')}<span class="area__index" aria-hidden="true">03</span></figure>
        <div class="area__body area__body--card">
          <p class="eyebrow">Tecnologías</p>
          <h3 class="h3">Innovación, robótica e inteligencia artificial aplicada a infraestructuras.</h3>
          <p>Inspección de infraestructuras civiles e industriales mediante sistemas autónomos sensorizados.</p>
          <ul class="tags"><li><a href="{P('inspeccion')}">Inspección con rover</a></li><li><a href="{P('shm')}">Monitorización SHM</a></li><li><a href="{P('ia')}">Inteligencia artificial</a></li></ul>
          <a class="btn btn--dark" href="{P('tecnologias')}">Descubrir tecnologías {icon('arrow-right')}</a>
        </div>
      </article>
    </div>
  </section>

  <section class="machinery section" aria-labelledby="featured-title">
    <div class="machinery__panel">
      <div class="wrap">
        {section_head('Soluciones destacadas', 'La capacidad de elevar grandes proyectos.', f'<p>Una selección de los equipos y sistemas más demandados, cada uno con su página técnica.</p><a class="btn btn--red" href="{P("maquinaria")}">Ver toda la maquinaria {icon("arrow-right")}</a>', hid='featured-title')}
        <div class="bento" data-reveal-group>
          <a class="tile tile--hero" href="{P('gruas')}" data-reveal>{img(rel, 'Gruas-Automontantes-ATES-Construction.png', 'Grúa automontante suspendida durante su montaje', '38% 50%')}
            <span class="tile__caption"><span class="tile__num">01</span><span class="tile__title">Grúas torre y automontantes</span><span class="tile__desc">Diversidad de modelos para obra, en alquiler y venta.</span></span>
            <span class="tile__arrow" aria-hidden="true">{icon('arrow-up-right')}</span></a>
          <a class="tile" href="{P('plataformas')}" data-reveal>{img(rel, 'Plataformas-ATES-motorizadas-obra-nueva.png', 'Plataformas motorizadas en una fachada de obra nueva', '34% 50%')}
            <span class="tile__caption"><span class="tile__num">02</span><span class="tile__title">Plataformas motorizadas</span></span><span class="tile__arrow" aria-hidden="true">{icon('arrow-up-right')}</span></a>
          <a class="tile" href="{P('montacargas')}" data-reveal>{img(rel, 'Montacargas-Ates-Construction.png', 'Montacargas de obra en la fachada de un edificio en altura', '42% 50%')}
            <span class="tile__caption"><span class="tile__num">03</span><span class="tile__title">Montacargas</span></span><span class="tile__arrow" aria-hidden="true">{icon('arrow-up-right')}</span></a>
          <a class="tile" href="{P('encofrados')}" data-reveal>{img(rel, 'Encofrados-apuntalamientos-ATES-Construction.png', 'Puntales amarillos sosteniendo un forjado', '55% 50%')}
            <span class="tile__caption"><span class="tile__num">04</span><span class="tile__title">Encofrados y apuntalamientos</span></span><span class="tile__arrow" aria-hidden="true">{icon('arrow-up-right')}</span></a>
          <a class="tile" href="{P('auxiliar')}" data-reveal>{img(rel, 'Compactacion-ATES-Construction.png', 'Equipos de compactación ATES', '45% 50%')}
            <span class="tile__caption"><span class="tile__num">05</span><span class="tile__title">Maquinaria auxiliar</span></span><span class="tile__arrow" aria-hidden="true">{icon('arrow-up-right')}</span></a>
        </div>
      </div>
    </div>
  </section>

  <section class="tech section" aria-labelledby="tech-title">
    <div class="tech__panel">
      <div class="tech__lines" aria-hidden="true"></div>
      <div class="tech__grid wrap">
        <div class="tech__text" data-reveal>
          <p class="eyebrow eyebrow--light">Innovación · ATES Technologies</p>
          <h2 class="h2 h2--light" id="tech-title">El futuro de la inspección de infraestructuras ya está aquí.</h2>
          <p class="lead lead--light">Combinamos experiencia industrial, robótica, sensorización e inteligencia artificial para desarrollar soluciones avanzadas de inspección y análisis de infraestructuras.</p>
          <ul class="tech__concepts">
            <li>{icon('bot')}<div><h3><a href="{P('inspeccion')}">Robótica</a></h3><p>Rover propio para inspeccionar grandes infraestructuras hidráulicas.</p></div></li>
            <li>{icon('activity')}<div><h3><a href="{P('shm')}">Monitorización SHM</a></h3><p>Seguimiento del comportamiento estructural mediante sensores.</p></div></li>
            <li>{icon('brain')}<div><h3><a href="{P('ia')}">Inteligencia artificial</a></h3><p>Big Data, Deep Learning y Machine Learning aplicados a cada activo.</p></div></li>
            <li>{icon('cube')}<div><h3><a href="{P('inspeccion')}">Modelizado 3D</a></h3><p>Inspección visual y modelo 3D del estado de la conducción.</p></div></li>
          </ul>
          <a class="btn btn--red" href="{P('tecnologias')}">Descubrir ATES Technologies {icon('arrow-right')}</a>
        </div>
        <div class="tech__visual" data-reveal>
          <figure class="tech__main media">{img(rel, 'Inspeccionar-infraestructuras-con-rober-ATES-Technologies.png', 'Rover de inspección rojo de ATES Technologies equipado con focos y sensores', '6% 50%')}<figcaption class="media__tag media__tag--dark">Rover de inspección ATES Technologies</figcaption></figure>
          <figure class="tech__inset media">{img(rel, 'tuberias-inspecciones-ATES-Technologies.png', 'Tuberías forzadas de una central hidráulica', '45% 50%')}<figcaption>Tuberías forzadas</figcaption></figure>
          <figure class="tech__inset tech__inset--b media">{img(rel, 'Infraestructuras-inspeccionadas-por-profesionales-ATES-Technologies.png', 'Técnico supervisando el rover durante una inspección vertical', '96% 50%')}<figcaption>Inspección en galería</figcaption></figure>
        </div>
      </div>
    </div>
  </section>

  <section class="projects section" id="proyectos" aria-labelledby="projects-title">
    <div class="wrap">
      {section_head('Proyectos y experiencia', 'Experiencia respaldada por proyectos reales.', '<p>Trabajos publicados por ATES: andamiaje de gran altura, patrimonio histórico e inspección tecnológica de infraestructuras.</p>', hid='projects-title')}
      <div class="cases" data-reveal-group>
        <a class="case case--feature" href="https://www.ates.es/instalacion-finalizada-del-andamiaje-ates-de-50-metros-para-el-parotet-de-valencia/" target="_blank" rel="noopener" data-reveal>
          <figure class="case__media media">{img(rel, 'Andamiaje_ATES_Gran_altura_esculturas_patrimonio.png', 'Andamio ATES de 50 metros envolviendo la escultura del Parotet en Valencia', '50% 40%')}</figure>
          <div class="case__body"><span class="case__cat">Andamiaje de gran altura · Patrimonio</span><h3 class="h3">Andamio de 50 metros para «El Parotet» de Valencia</h3><p>Andamiaje para la restauración integral de la escultura, permitiendo el acceso seguro a cada parte para su limpieza, saneado y pintado.</p><span class="link-arrow link-arrow--static">Leer el proyecto {icon('arrow-up-right')}</span></div>
        </a>
        <a class="case" href="https://www.ates.es/andamiaje-en-la-rehabilitacion-del-castillo-de-los-funes-de-villel-de-mesa-en-guadalajara/" target="_blank" rel="noopener" data-reveal>
          <figure class="case__media media">{img(rel, 'Andamios-cara-sur-2-scaled.jpg', 'Andamiaje en la cara sur del Castillo de los Funes, Villel de Mesa', '66% 55%')}</figure>
          <div class="case__body"><span class="case__cat">Patrimonio histórico</span><h3 class="h4">Rehabilitación del Castillo de los Funes</h3><p>Andamiaje para la conservación de este conjunto fortificado del siglo XII en Villel de Mesa (Guadalajara).</p><span class="link-arrow link-arrow--static">Leer el proyecto {icon('arrow-up-right')}</span></div>
        </a>
        <a class="case" href="https://www.ates.es/ates-technologies-inteligencia-artificial-y-grandes-infraestructuras/" target="_blank" rel="noopener" data-reveal>
          <figure class="case__media media">{img(rel, 'Salto_de_Moncabril_inspeccion_Zamora.png', 'Técnicos de ATES Technologies inspeccionando el canal de carga de Moncabril', '30% 50%')}</figure>
          <div class="case__body"><span class="case__cat">ATES Technologies</span><h3 class="h4">Inspección del canal de carga de Moncabril</h3><p>Inspección visual y modelizado 3D desde el rover en una central hidroeléctrica de Zamora.</p><span class="link-arrow link-arrow--static">Leer el proyecto {icon('arrow-up-right')}</span></div>
        </a>
      </div>
      <div class="gallery" data-reveal-group>
        <figure class="gallery__item gallery__item--wide media" data-reveal>{img(rel, 'Estabilizadores-de-fachada-ATES-Construction.png', 'Estabilizador de fachada multidireccional en un edificio histórico', '60% 50%')}<figcaption><strong>Estabilizadores de fachada</strong>Rehabilitación de edificio histórico</figcaption></figure>
        <figure class="gallery__item media" data-reveal>{img(rel, 'Encofrados-pilares-ATES-Construction.png', 'Encofrados metálicos de pilares en obra', '70% 50%')}<figcaption><strong>Encofrado de pilares</strong>Estructura en ejecución</figcaption></figure>
        <figure class="gallery__item media" data-reveal>{img(rel, 'Andamiaje-restauracion-chimeneas-industriales.png', 'Andamio ATES en la restauración de una chimenea industrial', '50% 50%')}<figcaption><strong>Chimeneas industriales</strong>Patrimonio industrial</figcaption></figure>
        <figure class="gallery__item media" data-reveal>{img(rel, 'Cimbras-y-apeos-estructurales-ATES-Construction.png', 'Cimbra multidireccional sosteniendo un encofrado de madera', '62% 50%')}<figcaption><strong>Cimbras y apeos</strong>Soporte de estructuras</figcaption></figure>
        <figure class="gallery__item gallery__item--wide media" data-reveal>{img(rel, 'Andamios-multidireccional-europero-ATES-Construction.png', 'Andamio multidireccional montado en el paramento de una presa', '60% 50%')}<figcaption><strong>Andamio multidireccional</strong>Infraestructura hidráulica</figcaption></figure>
      </div>
    </div>
  </section>
{contact_cta(rel, 'Asesoramiento técnico', title='Cada proyecto necesita una solución.', text='Cuéntanos qué necesitas y nuestro equipo te ayudará a encontrar la alternativa más adecuada.')}"""


# ======================================================================= CATEGORÍAS
def maquinaria(rel):
    s = "maquinaria"
    hero = page_hero(rel, variant="frame", eyebrow="Maquinaria y elevación", title="La capacidad de elevar grandes proyectos.",
                     lead="Grúas torre y automontantes, montacargas de obra y maquinaria auxiliar, en alquiler y venta, con un servicio técnico que garantiza la disponibilidad del equipo en obra.",
                     image="Gruas-Torre-ATES-Construction.png", alt="Grúas torre ATES en una obra junto al mar", pos="12% 45%", trail=T(rel, s),
                     actions=f'<a class="btn btn--white" href="#familias">Ver familias de equipos {icon("arrow-right")}</a><a class="btn btn--glass" href="{page_url(rel, "contacto")}?asunto=Maquinaria#formulario">Consultar disponibilidad</a>')
    aux = PAGES["auxiliar"]
    return hero + f"""
  <section class="section intro" aria-labelledby="intro-title">
    <div class="wrap intro__grid">
      <div data-reveal>
        <p class="eyebrow">Parque de maquinaria</p>
        <h2 class="h2" id="intro-title">Equipos propios, mantenidos por un servicio técnico propio.</h2>
      </div>
      <div class="intro__text" data-reveal>
        <p class="lead">Disponemos de una gran diversidad de modelos de grúas torre y varios modelos de grúas automontantes para la construcción, tanto para alquiler como para venta.</p>
        <p>Nuestro servicio técnico, con más de 40 años de experiencia, garantiza la plena disponibilidad del equipo durante todo el tiempo de permanencia en la obra. Completamos el parque con montacargas y una amplia gama de maquinaria auxiliar para facilitar la ejecución rápida y económica de las obras.</p>
      </div>
    </div>
  </section>

  <section class="section section--tight" id="familias" aria-labelledby="fam-title">
    <div class="wrap">
      {section_head('Familias de equipos', 'Elige la familia que necesita tu obra.', hid='fam-title')}
      <div class="fam-grid" data-reveal-group>{family_cards(rel, ['gruas', 'montacargas', 'auxiliar'])}</div>
      <div class="aux-strip" data-reveal>
        <p class="aux-strip__label">{icon('box')} En el catálogo de maquinaria auxiliar</p>
        {chips(['Grupos electrógenos', 'Compactación', 'Dumpers', 'Carretillas elevadoras', 'Compresores', 'Plataformas de tijera', 'Brazos articulados', 'Hormigoneras', 'Martillos eléctricos', 'Elevadores eléctricos', 'Equipos de corte', 'Vibradores', 'Rodillos'])}
        <a class="link-arrow" href="{page_url(rel, 'auxiliar')}">Abrir el catálogo {icon('arrow-right')}</a>
      </div>
    </div>
  </section>

  <section class="section band" aria-labelledby="adv-title">
    <div class="band__panel">
      <div class="wrap">
        {section_head('Servicio', 'Lo que respalda a cada equipo.', light=True, hid='adv-title')}
        {features([
            ('wrench', 'Servicio técnico de más de 40 años', 'Garantiza la plena disponibilidad del equipo durante toda su permanencia en obra.'),
            ('key', 'Alquiler y venta', 'Grúas torre, automontantes y maquinaria auxiliar en las dos modalidades.'),
            ('users', 'Homologación para personas', 'Montacargas homologados también para subir personas, con ahorro de costes en obra.'),
          ], cols=3, light=True)}
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="gal-title">
    <div class="wrap">
      {section_head('Galería', 'Equipos ATES trabajando en obra.', hid='gal-title')}
      {gallery(rel, [
          ('Construction-grua-ates.png', 'Grúa torre ATES amarilla sobre cielo azul', 'Grúa torre', 'Marca ATES en la contrapluma', '62% 40%', 'gal__item--tall'),
          ('Gruas-Automontantes-ATES-Construction.png', 'Grúa automontante durante su montaje', 'Grúa automontante', 'Montaje del equipo', '38% 50%', 'gal__item--wide'),
          ('Brazos-articulados-maquinaria-auxiliar-ATES-Construction.png', 'Brazo articulado junto a un andamio', 'Brazo articulado', 'Maquinaria auxiliar', '42% 40%'),
          ('Dumpers-maquinaria-auxiliar-construction-ATES.png', 'Dumper con rotulación ATES', 'Dumper', 'Movimiento de tierras', '88% 50%'),
          ('tijeras-electricas-maquinaria-ATES.png', 'Plataformas de tijera eléctricas en nave', 'Plataformas de tijera', 'Elevación de personas', '30% 50%', 'gal__item--wide'),
        ])}
    </div>
  </section>
{related(rel, ['construccion', 'plataformas', 'tecnologias'], title='Otras áreas de ATES')}
{contact_cta(rel, 'Maquinaria', image='Construction-grua-ates.png', pos='60% 30%')}"""


def construccion(rel):
    s = "construccion"
    hero = page_hero(rel, variant="frame", eyebrow="Sistemas constructivos", title="Sistemas que dan forma a cada obra.",
                     lead="Amplia gama de productos para la construcción en alquiler y venta: andamios, encofrados, cimbras y plataformas para obra nueva, rehabilitación y cerramiento de fachadas.",
                     image="Plataformas-ATES-motorizadas-obra-nueva.png", alt="Plataformas motorizadas en la fachada de un edificio de obra nueva", pos="40% 50%", trail=T(rel, s),
                     actions=f'<a class="btn btn--white" href="#sistemas">Ver sistemas {icon("arrow-right")}</a><a class="btn btn--glass" href="{page_url(rel, "contacto")}?asunto=Construcción#formulario">Estudiar mi proyecto</a>')
    systems = [("andamios", "Marco europeo y multidireccional"), ("encofrados", "Ligera, pesada, pilares, planta"), ("cimbras", "Apeo de encofrados"),
               ("plataformas", "Obra nueva y rehabilitación"), ("estabilizadores", "Frente a esfuerzos del viento"), ("escaleras", "Acceso público y privativo")]
    rows = "".join(f"""
        <a class="sys" href="{page_url(rel, k)}" data-reveal>
          <figure class="sys__media media">{img(rel, PAGES[k]['card'], PAGES[k]['card_alt'], PAGES[k].get('card_pos', '50% 50%'))}</figure>
          <span class="sys__num">{i + 1:02d}</span>
          <span class="sys__title">{e(PAGES[k]['nav'])}</span>
          <span class="sys__meta">{e(meta)}</span>
          <span class="sys__arrow" aria-hidden="true">{icon('arrow-right')}</span>
        </a>""" for i, (k, meta) in enumerate(systems))
    return hero + f"""
  <section class="section intro" aria-labelledby="intro-title">
    <div class="wrap intro__grid">
      <div data-reveal>
        <p class="eyebrow">Capacidad técnica</p>
        <h2 class="h2" id="intro-title">Estudiamos tu proyecto antes de proponer un sistema.</h2>
      </div>
      <div class="intro__text" data-reveal>
        <p class="lead">Nuestro departamento técnico, altamente cualificado en el sector de la construcción, estudia cada proyecto para proporcionar la solución más adecuada.</p>
        <p>Un equipo experimentado de montadores ejecuta las especificaciones que determina el departamento técnico, y una amplia red técnico-comercial ofrece asesoramiento personalizado para cada obra.</p>
        <div class="intro__stats">
          <div><strong>UNE-EN 12810 · 12811</strong><span>Normas que cumplen nuestros andamios</span></div>
          <div><strong>Marcado CE</strong><span>Plataformas motorizadas homologadas</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight" id="sistemas" aria-labelledby="sys-title">
    <div class="wrap">
      {section_head('Catálogo de sistemas', 'Seis sistemas, una misma exigencia de seguridad.', hid='sys-title')}
      <div class="sys-list" data-reveal-group>{rows}</div>
    </div>
  </section>

  <section class="section split-uses" aria-labelledby="uses-title">
    <div class="wrap">
      {section_head('Aplicaciones', 'Obra nueva y rehabilitación.', center=True, hid='uses-title')}
      <div class="uses">
        <article class="use" data-reveal>
          <figure class="use__media media">{img(rel, 'Plataformas-ATES-motorizadas-obra-nueva.png', 'Plataformas motorizadas en fachada de obra nueva', '30% 50%')}</figure>
          <div class="use__body">
            <h3 class="h3">Obra nueva</h3>
            {checklist(['Encofrados para muros, cimentaciones, pilares y forjados', 'Cimbras y apuntalamientos para sostener estructuras', 'Plataformas motorizadas para cerramientos de fachada', 'Escaleras de acceso y servicio en obra'])}
          </div>
        </article>
        <article class="use" data-reveal>
          <figure class="use__media media">{img(rel, 'Estabilizadores-de-fachada-ATES-Construction.png', 'Estabilizador de fachada en un edificio histórico', '60% 50%')}</figure>
          <div class="use__body">
            <h3 class="h3">Rehabilitación</h3>
            {checklist(['Andamios para rehabilitación y cerramiento de fachadas', 'Estabilizadores de fachada frente a los esfuerzos del viento', 'Plataformas motorizadas para rehabilitación de edificios', 'Andamiaje en patrimonio histórico e industrial'])}
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="gal-title">
    <div class="wrap">
      {section_head('En obra', 'Sistemas ATES en proyectos reales.', hid='gal-title')}
      {gallery(rel, [
          ('Andamios-cara-sur-2-scaled.jpg', 'Andamiaje en el Castillo de los Funes', 'Castillo de los Funes', 'Andamiaje en patrimonio', '66% 55%', 'gal__item--wide gal__item--tall'),
          ('Encofrados-serie-pesada-ATES-Construction.png', 'Obra con encofrados de serie pesada', 'Encofrados', 'Serie pesada', '50% 50%'),
          ('Andamios-marco-europero-ATES-Construction.png', 'Andamio de marco europeo en fachada', 'Andamio de marco europeo', 'Rehabilitación de fachada', '45% 70%'),
          ('Construction-andamios-estructuras-edificios.png', 'Montador trabajando en un andamio', 'Montaje', 'Equipo propio de montadores', '50% 50%', 'gal__item--wide'),
        ])}
    </div>
  </section>
{related(rel, ['auxiliar', 'gruas', 'montacargas'], title='Maquinaria para completar la obra', eyebrow='Servicios relacionados')}
{contact_cta(rel, 'Construcción', image='Encofrados-serie-pesada-ATES-Construction.png')}"""


def tecnologias(rel):
    s = "tecnologias"
    hero = page_hero(rel, variant="dark", eyebrow="ATES Technologies", title="Inspección inteligente de infraestructuras.",
                     lead="Expertos en robótica, sensorización e inteligencia artificial para conocer el estado real de infraestructuras civiles e industriales.",
                     image="Inspecciones-infraestructuras-hidraulicas-rover-proyectos-Ates.png", alt="Rover de ATES Technologies iluminando el interior de una tubería forzada", pos="100% 50%", trail=T(rel, s),
                     actions=f'<a class="btn btn--white" href="#servicios">Ver servicios {icon("arrow-right")}</a><a class="btn btn--glass" href="{page_url(rel, "contacto")}?asunto=ATES Technologies#formulario">Hablar con el equipo</a>')
    cards = "".join(f"""
        <a class="svc" href="{page_url(rel, k)}" data-reveal>
          <figure class="svc__media media">{img(rel, PAGES[k]['card'], PAGES[k]['card_alt'], PAGES[k].get('card_pos', '50% 50%'))}</figure>
          <span class="svc__icon">{icon(ic)}</span>
          <h3 class="svc__title">{e(PAGES[k]['nav'])}</h3>
          <p class="svc__desc">{d}</p>
          <span class="link-arrow link-arrow--static">Ver servicio {icon('arrow-right')}</span>
        </a>""" for k, ic, d in [
        ("inspeccion", "bot", "Rover propio para tuberías forzadas, canales de carga y galerías de centrales hidráulicas."),
        ("shm", "activity", "Seguimiento del comportamiento estructural con sensores y análisis de datos."),
        ("ia", "brain", "Big Data, Deep Learning y Machine Learning aplicados a problemas industriales reales.")])
    return hero + f"""
  <section class="section intro" aria-labelledby="intro-title">
    <div class="wrap intro__grid">
      <div data-reveal>
        <p class="eyebrow">Quiénes somos</p>
        <h2 class="h2" id="intro-title">Una spin-off de ATES con base industrial y equipo investigador.</h2>
      </div>
      <div class="intro__text" data-reveal>
        <p class="lead">ATES Technologies se dedica a la inspección de infraestructuras civiles e industriales, obteniendo información real de su estado mediante sistemas autónomos convenientemente sensorizados.</p>
        <p>A la experiencia de ATES en construcción y mantenimiento de infraestructuras se une un equipo de investigadores de la Universidad Carlos III de Madrid, tecnólogos en robótica, sensorización e inteligencia artificial.</p>
      </div>
    </div>
  </section>

  <section class="section tech-svcs" id="servicios" aria-labelledby="svc-title">
    <div class="tech__panel">
      <div class="tech__lines" aria-hidden="true"></div>
      <div class="wrap">
        {section_head('Servicios', 'Tecnología aplicada a problemas reales.', light=True, hid='svc-title')}
        <div class="svc-grid" data-reveal-group>{cards}</div>
        <div class="disciplines" data-reveal>
          <p>Especialidades</p>
          {chips(['Robótica', 'Sensorización', 'Inteligencia artificial', 'Big Data', 'Deep Learning', 'Machine Learning', 'Digital Twin'])}
        </div>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="case-title">
    <div class="wrap">
      <article class="feature-case" data-reveal>
        <figure class="feature-case__media media">{img(rel, 'Salto_de_Moncabril_inspeccion_Zamora.png', 'Equipo de ATES Technologies trabajando dentro del canal de carga de Moncabril', '8% 50%')}</figure>
        <div class="feature-case__body">
          <p class="eyebrow">Caso publicado</p>
          <h2 class="h3" id="case-title">Salto de Moncabril (Zamora)</h2>
          <p>Inspección de una canal de carga de hormigón con más de 60 años en una central hidroeléctrica. El rover permitió una inspección visual y un modelizado 3D, base del análisis estructural que confirmó el buen estado de la conducción.</p>
          <div class="feature-case__actions">
            <a class="btn btn--dark" href="{page_url(rel, 'inspeccion')}#caso">Ver el caso {icon('arrow-right')}</a>
            {ext('https://www.ates.es/ates-technologies-inteligencia-artificial-y-grandes-infraestructuras/', 'Noticia en ates.es')}
          </div>
        </div>
      </article>
    </div>
  </section>
{contact_cta(rel, 'ATES Technologies', title='¿Necesitas conocer el estado real de tu infraestructura?', image='Inspecciones-Inteligentes-ATES-Technologies.png', pos='50% 50%')}"""


# ======================================================================= MAQUINARIA · interiores
def gruas(rel):
    s = "gruas"
    hero = page_hero(rel, variant="frame", eyebrow="Maquinaria · Elevación", title="Grúas torre y automontantes.",
                     lead="Gran diversidad de modelos de grúas torre y varios modelos de grúas automontantes para la construcción, en alquiler y venta.",
                     image="Construction-grua-ates.png", alt="Grúa torre ATES amarilla con la marca en la contrapluma", pos="62% 30%", trail=T(rel, s),
                     actions=actions_service(rel, "Grúas torre y automontantes"))
    return hero + f"""
  <section class="section" aria-labelledby="models-title">
    <div class="wrap">
      {section_head('Tipologías', 'Dos formatos de grúa para cada tipo de obra.', '<p>ATES presenta ambas familias de forma conjunta: comparten servicio técnico, modalidades de alquiler y venta, y asesoramiento.</p>', hid='models-title')}
      <div class="duo">
        <article class="duo__item" id="gruas-torre" data-reveal>
          <figure class="duo__media media">{img(rel, 'Gruas-Torre-ATES-Construction.png', 'Dos grúas torre ATES en una obra frente al mar', '4% 50%')}</figure>
          <div class="duo__body">
            <span class="duo__num">01</span>
            <h3 class="h3">Grúas torre</h3>
            <p>Disponemos de una gran diversidad de modelos de grúas torre para la construcción, tanto para alquiler como para venta.</p>
            {chips(['Alquiler', 'Venta', 'Gran diversidad de modelos'])}
          </div>
        </article>
        <article class="duo__item" id="automontantes" data-reveal>
          <figure class="duo__media media">{img(rel, 'Gruas-Automontantes-ATES-Construction.png', 'Grúa automontante suspendida durante su montaje', '36% 50%')}</figure>
          <div class="duo__body">
            <span class="duo__num">02</span>
            <h3 class="h3">Grúas automontantes</h3>
            <p>Contamos con varios modelos de grúas automontantes para la construcción, igualmente disponibles en alquiler y en venta.</p>
            {chips(['Alquiler', 'Venta', 'Varios modelos'])}
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="section statband" aria-labelledby="st-title">
    <div class="statband__panel">
      <div class="wrap statband__grid">
        <div class="statband__figure" data-reveal><span>Más de</span><strong>40</strong><span>años de servicio técnico</span></div>
        <div data-reveal>
          <p class="eyebrow eyebrow--light">Servicio técnico</p>
          <h2 class="h2 h2--light" id="st-title">La grúa disponible durante toda la obra.</h2>
          <p class="lead lead--light">Nuestro servicio técnico, con más de 40 años de experiencia, garantiza la plena disponibilidad del equipo durante todo el tiempo de permanencia en la obra.</p>
          {checklist(['Asesoramiento técnico personalizado para cada obra', 'Modalidades de alquiler y venta', 'Aviso de averías 24 horas: 962 524 400'], light=True)}
        </div>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="gal-title">
    <div class="wrap">
      {section_head('Galería', 'Grúas ATES en obra.', hid='gal-title')}
      {gallery(rel, [
          ('Construction-grua-ates.png', 'Pluma y contrapluma de una grúa torre ATES', 'Grúa torre ATES', 'Pluma, mástil y contrapluma', '30% 50%', 'gal__item--wide'),
          ('Gruas-Torre-ATES-Construction.png', 'Mástiles de dos grúas torre ATES', 'Grúas torre', 'Obra residencial en costa', '22% 50%', 'gal__item--tall'),
          ('Gruas-Automontantes-ATES-Construction.png', 'Grúa automontante izada por una grúa auxiliar', 'Automontante', 'Maniobra de montaje', '60% 50%'),
          ('Encofrados-pilares-ATES-Construction.png', 'Obra con pilares encofrados', 'En obra', 'Elevación de encofrados', '70% 50%'),
        ])}
      {source_note(OFFICIAL + 'servicios/construccion/')}
    </div>
  </section>
{related(rel, ['montacargas', 'auxiliar', 'encofrados'])}
{contact_cta(rel, 'Grúas torre y automontantes', image='Gruas-Torre-ATES-Construction.png', pos='10% 50%')}"""


def montacargas(rel):
    s = "montacargas"
    hero = page_hero(rel, variant="split", eyebrow="Maquinaria · Elevación", title="Montacargas y elevadores de obra.",
                     lead="Un amplio parque de montacargas en alquiler, de 500 a 2.000 kg de carga, con homologación para subir personas.",
                     image="Montacargas-Ates-Construction.png", alt="Montacargas de obra instalado en la fachada de un edificio en altura", pos="42% 50%", trail=T(rel, s),
                     actions=actions_service(rel, "Montacargas"), tag="Montacargas en edificio en altura")
    return hero + f"""
  <section class="section" aria-labelledby="cap-title">
    <div class="wrap">
      {section_head('Capacidad', 'De 500 a 2.000 kg por viaje.', hid='cap-title')}
      <div class="scale" data-reveal>
        <div class="scale__bar"><span class="scale__fill"></span></div>
        <div class="scale__ends"><div><strong>500 kg</strong><span>Carga mínima de la gama</span></div><div><strong>2.000 kg</strong><span>Carga máxima de la gama</span></div></div>
      </div>
      {features([
          ('box', 'Palet europeo', 'Montacargas preparados para subir palets europeos a cada planta.'),
          ('ruler', 'Plataforma de hasta 3,30 m', 'Plataforma de carga de hasta 3,30 m de largo, pensada para placas de pladur.'),
          ('users', 'Homologados para personas', 'También disponemos de la homologación para subir personas.'),
          ('gauge', 'Ahorro y rendimiento', 'Un aspecto cada vez más apreciado que ahorra costes y mejora el rendimiento de la obra y del personal.'),
        ], cols=4)}
    </div>
  </section>

  <section class="section section--tight" aria-labelledby="aux-title">
    <div class="wrap">
      <article class="feature-case feature-case--reverse" data-reveal>
        <figure class="feature-case__media media">{img(rel, 'Elevadores-electricos-maquinaria-auxiliar-Construction-ATES.png', 'Elevador eléctrico de obra', '30% 50%')}</figure>
        <div class="feature-case__body">
          <p class="eyebrow">Para cargas ligeras</p>
          <h2 class="h3" id="aux-title">Elevadores eléctricos de 300 kg</h2>
          <p>Para cargas menores, el catálogo de maquinaria auxiliar incluye elevadores eléctricos con capacidad de carga de 300 kg.</p>
          <a class="btn btn--dark" href="{page_url(rel, 'auxiliar')}#elevacion">Ver en el catálogo {icon('arrow-right')}</a>
        </div>
      </article>
      {source_note(OFFICIAL + 'servicios/construccion/')}
    </div>
  </section>
{related(rel, ['gruas', 'plataformas', 'auxiliar'])}
{contact_cta(rel, 'Montacargas', image='Montacargas-Ates-Construction.png', pos='50% 60%')}"""


AUX = [  # (id, filtro, nombre, imagen, pos, descripción, [especificaciones])
    ("electrogenos", "energia", "Grupos electrógenos", "grupo-electrogeno-100kvas-maquinaria-auxiliar-construction-ATES.png", "30% 50%",
     "Grupos con potencias comprendidas entre 4,5 kVA y 150 kVA para suministro de luz 220 V – 380 V, 50 Hz.",
     ["Gasolina Preme: 4, 5, 6 y 8 kVA, monofásicos y trifásicos", "10 y 60 kVA A.E.M.", "100 kVA Gesan · 150 kVA A.E.M."]),
    ("compresores", "energia", "Compresores", "compresores-kaeser-maquinaria-auxiliar-construction-ATES.png", "30% 50%",
     "Compresores Kaeser para obra.", ["Modelos M-38, M-43 y M-58"]),
    ("compactacion", "tierras", "Compactación", "Compactacion-ATES-Construction.png", "45% 50%",
     "Bandejas compactadoras y pisones para la compactación de terrenos.", ["Bandejas de 75, 125 y 220 kg"]),
    ("dumpers", "tierras", "Dumpers", "Dumpers-maquinaria-auxiliar-construction-ATES.png", "88% 50%",
     "Dumpers para movimientos de tierras y dumpers de descarga en altura.", ["Movimiento de tierras: 750 a 3.000 kg", "Descarga en altura: 1.500 a 2.500 kg"]),
    ("rodillos", "tierras", "Rodillos", "rodillos-dinapacc-maquinaria-auxiliar-ATES-construction.png", "30% 50%",
     "Rodillos compactadores Dinapacc.", ["De 750 a 3.000 kg"]),
    ("vibradores", "hormigon", "Vibradores", "Vibradores-de-hormigon-maquinaria-auxiliar-Construction-ATES.png", "30% 50%",
     "Vibradores de hormigón y pisón vibrosaltador Dinapacc.", ["Pisón vibrosaltador Dinapacc"]),
    ("carretillas", "elevacion", "Carretillas elevadoras", "Carretillas-maquinaria-auxiliar-ATES.png", "25% 50%",
     "Carretillas telescópicas Agria.", ["Modelos TH30-25 y 30-21"]),
    ("tijera", "elevacion", "Plataformas de tijera", "tijeras-electricas-maquinaria-ATES.png", "30% 50%",
     "Plataformas de tijera eléctricas JLG.", ["6 metros de altura de trabajo"]),
    ("brazos", "elevacion", "Brazos articulados", "Brazos-articulados-maquinaria-auxiliar-ATES-Construction.png", "42% 40%",
     "Plataforma elevadora de brazo articulado Haulotte.", ["18 metros"]),
    ("elevadores", "elevacion", "Elevadores eléctricos", "Elevadores-electricos-maquinaria-auxiliar-Construction-ATES.png", "30% 50%",
     "Elevadores eléctricos para cargas ligeras.", ["Capacidad de carga de 300 kg"]),
    ("hormigoneras", "hormigon", "Hormigoneras", "Hormigoner-construction-maquinaria-auxiliar-ATES.png", "28% 50%",
     "Hormigonera con desmultiplicación de par en volante.", ["Capacidad de 250 kg"]),
    ("martillos", "hormigon", "Martillos eléctricos", "Martillos-electricos-maquinaria-auxiliar-construction-ATES.png", "30% 50%",
     "Martillos eléctricos para demolición y picado.", ["De 3 kg hasta 15 kg"]),
    ("corte", "hormigon", "Sección de corte", "Cortadora-asfaltica-sima-maquinaria-auxiliar-construction-ATES.png", "30% 50%",
     "Cortadora asfáltica, tronzadora de agua y tronzadora de madera.", ["Cortadora asfáltica SIMA", "Cortadora de agua SIMA", "Cortadora de madera"]),
]
FILTERS = [("todos", "Todos"), ("energia", "Energía y aire"), ("tierras", "Tierras y compactación"),
           ("elevacion", "Elevación y manipulación"), ("hormigon", "Hormigón, demolición y corte")]


def auxiliar(rel):
    s = "auxiliar"
    hero = page_hero(rel, variant="split", eyebrow="Maquinaria · Catálogo", title="Maquinaria auxiliar para construcción.",
                     lead="Una diversa gama de maquinaria auxiliar en venta y alquiler, para facilitar la ejecución rápida y económica de las obras de nuestros clientes.",
                     image="Dumpers-maquinaria-auxiliar-construction-ATES.png", alt="Dumpers de la flota de maquinaria auxiliar ATES", pos="100% 50%", trail=T(rel, s),
                     actions=f'<a class="btn btn--red" href="#catalogo">Ver catálogo {icon("arrow-right")}</a><a class="btn btn--line" href="tel:+34902171517">{icon("phone")} 902 171 517</a>',
                     tag="Dumper con rotulación ATES")
    from urllib.parse import quote
    filt = "".join(f'<button type="button" class="filter{" is-active" if k == "todos" else ""}" data-filter="{k}" aria-pressed="{"true" if k == "todos" else "false"}">{e(t)}</button>' for k, t in FILTERS)
    cards = "".join(f"""
        <article class="product" id="{pid}" data-cat="{cat}" data-reveal>
          <figure class="product__media media">{img(rel, f, name + ' de la flota de maquinaria auxiliar ATES', pos)}</figure>
          <div class="product__body">
            <span class="product__cat">{e(dict(FILTERS)[cat])}</span>
            <h3 class="h4">{e(name)}</h3>
            <p>{e(desc)}</p>
            <ul class="product__specs">{''.join(f'<li>{icon("check")}{e(x)}</li>' for x in spec)}</ul>
            <a class="link-arrow" href="{page_url(rel, 'contacto')}?asunto={quote('Maquinaria auxiliar: ' + name)}#formulario">Consultar disponibilidad {icon('arrow-right')}</a>
          </div>
        </article>""" for pid, cat, name, f, pos, desc, spec in AUX)
    return hero + f"""
  <section class="section catalog" id="catalogo" aria-labelledby="cat-title">
    <div class="wrap">
      {section_head('Catálogo', '13 familias de equipos, en venta y alquiler.', '<p>Modelos y capacidades tal como figuran en el catálogo publicado por ATES.</p>', hid='cat-title')}
      <div class="filters" role="group" aria-label="Filtrar por categoría" data-filters>{filt}<span class="filters__count" aria-live="polite" data-count>{len(AUX)} equipos</span></div>
      <div class="products" data-products>{cards}</div>
      {source_note(OFFICIAL + 'servicios/construccion/maquinaria-auxiliar/')}
    </div>
  </section>
  <span id="elevacion" class="anchor-alias" data-filter-alias="elevacion"></span>
{related(rel, ['montacargas', 'gruas', 'construccion'])}
{contact_cta(rel, 'Maquinaria auxiliar', image='Compactacion-ATES-Construction.png', pos='45% 50%')}"""


# ======================================================================= CONSTRUCCIÓN · interiores
def andamios(rel):
    s = "andamios"
    hero = page_hero(rel, variant="frame", eyebrow="Construcción · Andamios", title="Andamios de marco y multidireccional europeo.",
                     lead="Uno de los mayores parques de la Comunidad Valenciana, con una amplia gama de productos para construcción, rehabilitación y cerramiento de fachadas, en alquiler y venta.",
                     image="Andamios-cara-sur-2-scaled.jpg", alt="Andamiaje ATES en la rehabilitación del Castillo de los Funes, Villel de Mesa", pos="68% 52%", trail=T(rel, s),
                     actions=actions_service(rel, "Andamios").replace("btn--line", "btn--glass"))
    return hero + f"""
  <section class="section intro" aria-labelledby="intro-title">
    <div class="wrap intro__grid">
      <div data-reveal>
        <p class="eyebrow">Andamios</p>
        <h2 class="h2" id="intro-title">Trabajo seguro en lugares de difícil acceso.</h2>
      </div>
      <div class="intro__text" data-reveal>
        <p class="lead">Los andamios facilitan la ejecución de trabajos en lugares de difícil acceso y cumplen con las especificaciones de las normas europeas adoptadas por el Comité Europeo de Normalización (CEN).</p>
        <div class="norms">
          <div class="norm"><span>Norma</span><strong>UNE-EN 12810</strong></div>
          <div class="norm"><span>Norma</span><strong>UNE-EN 12811</strong></div>
          <div class="norm norm--soft"><span>Adoptadas por</span><strong>CEN</strong></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight" aria-labelledby="types-title">
    <div class="wrap">
      {section_head('Tipologías', 'Dos sistemas de andamio europeo.', hid='types-title')}
      <div class="stack">
        <article class="stack__item" data-reveal>
          <figure class="stack__media media">{img(rel, 'Andamios-marco-europero-ATES-Construction.png', 'Andamio de marco europeo cubriendo la fachada de un edificio urbano', '45% 72%')}</figure>
          <div class="stack__body">
            <span class="duo__num">01</span>
            <h3 class="h3">Andamio de marco europeo</h3>
            <p>Para trabajos de construcción, rehabilitación y cerramiento de fachadas, disponible en alquiler y venta.</p>
            {chips(['Construcción', 'Rehabilitación', 'Cerramiento de fachadas'])}
          </div>
        </article>
        <article class="stack__item stack__item--reverse" data-reveal>
          <figure class="stack__media media">{img(rel, 'Andamios-multidireccional-europero-ATES-Construction.png', 'Andamio multidireccional montado en el paramento de una presa', '62% 50%')}</figure>
          <div class="stack__body">
            <span class="duo__num">02</span>
            <h3 class="h3">Andamio multidireccional europeo</h3>
            <p>La técnica de unión multidireccional ahorra tiempo en el montaje y aporta gran estabilidad y múltiples posibilidades formales.</p>
            {chips(['Unión multidireccional', 'Montaje rápido', 'Gran estabilidad'])}
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--tight" aria-labelledby="comp-title">
    <div class="wrap">
      {section_head('Sistemas complementarios', 'Del andamio a la estructura completa.', hid='comp-title')}
      <div class="mini-grid" data-reveal-group>
        {''.join(f'<a class="mini" href="{page_url(rel, k)}" data-reveal><figure class="mini__media media">{img(rel, PAGES[k]["card"], PAGES[k]["card_alt"], PAGES[k].get("card_pos", "50% 50%"))}</figure><span class="mini__title">{e(PAGES[k]["nav"])}</span><span class="mini__desc">{e(PAGES[k]["short"])}</span></a>' for k in ['cimbras', 'estabilizadores', 'escaleras'])}
      </div>
    </div>
  </section>

  <section class="section band" aria-labelledby="team-title">
    <div class="band__panel">
      <div class="wrap">
        {section_head('Capacidad técnica', 'Del estudio al montaje, con equipo propio.', light=True, hid='team-title')}
        {features([
            ('file', 'Departamento técnico', 'Estudia cada proyecto para proporcionar la solución de andamiaje más adecuada.'),
            ('hard-hat', 'Montadores experimentados', 'Ejecutan las especificaciones que determina el departamento técnico.'),
            ('users', 'Red técnico-comercial', 'Asesoramiento personalizado para cada una de tus obras.'),
          ], cols=3, light=True)}
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="proj-title">
    <div class="wrap">
      {section_head('Proyectos publicados', 'Andamiaje en patrimonio y gran altura.', hid='proj-title')}
      <div class="proj-row" data-reveal-group>
        {''.join(f'<a class="proj" href="{u}" target="_blank" rel="noopener" data-reveal><figure class="proj__media media">{img(rel, f, a, p)}</figure><span class="case__cat">{e(c)}</span><span class="proj__title">{e(t)}</span><span class="link-arrow link-arrow--static">Leer en ates.es {icon("arrow-up-right")}</span></a>' for u, f, a, p, c, t in [
            ('https://www.ates.es/andamiaje-en-la-rehabilitacion-del-castillo-de-los-funes-de-villel-de-mesa-en-guadalajara/', 'Andamios-cara-sur-2-scaled.jpg', 'Andamiaje en el Castillo de los Funes', '66% 55%', 'Guadalajara · Siglo XII', 'Castillo de los Funes de Villel de Mesa'),
            ('https://www.ates.es/instalacion-finalizada-del-andamiaje-ates-de-50-metros-para-el-parotet-de-valencia/', 'Andamiaje_ATES_Gran_altura_esculturas_patrimonio.png', 'Andamio de 50 metros en El Parotet', '50% 40%', 'Valencia · 50 metros', 'Andamiaje para «El Parotet»'),
            ('https://www.ates.es/andamios-de-ates-en-la-restauracion-de-chimeneas-industriales/', 'Andamiaje-restauracion-chimeneas-industriales.png', 'Andamio en chimenea industrial', '50% 50%', 'Patrimonio industrial', 'Chimeneas de Aielo de Malferit y l’Alcúdia de Crespins'),
        ])}
      </div>
      {source_note(OFFICIAL + 'servicios/construccion/andamios/')}
    </div>
  </section>
{related(rel, ['cimbras', 'plataformas', 'estabilizadores'])}
{contact_cta(rel, 'Andamios', image='Andamios-marco-europero-ATES-Construction.png', pos='45% 75%')}"""


def encofrados(rel):
    s = "encofrados"
    hero = page_hero(rel, variant="frame", eyebrow="Construcción · Estructuras", title="Encofrados y apuntalamientos.",
                     lead="Sistemas para muros, cimentaciones, pilares y forjados, con cerchas para muros a una cara y puntales de 1 a 6 metros.",
                     image="Encofrados-apuntalamientos-ATES-Construction.png", alt="Bosque de puntales amarillos sosteniendo un forjado en obra", pos="50% 50%", trail=T(rel, s),
                     actions=actions_service(rel, "Encofrados y apuntalamientos").replace("btn--line", "btn--glass"))
    systems = [
        ("Encofrados-serie-ligera-ATES-Construction.png", "55% 50%", "Encofrado de serie ligera", "Para muros, cimentaciones y zapatas. No necesitan grúa en el montaje.", [("Presión admisible del hormigón", "40 kN/m²"), ("Montaje", "Sin grúa")]),
        ("Encofrados-serie-pesada-ATES-Construction.png", "50% 50%", "Encofrado de serie pesada", "Para muros, pilares, estribos y zapatas. Soporta grandes presiones de hormigón con excelentes acabados.", [("Presión admisible del hormigón", "60 kN/m²")]),
        ("Encofrados-pilares-ATES-Construction.png", "70% 50%", "Encofrado de pilares", "Paneles metálicos reforzados en los cantos e interiormente mediante nervios; forman pilares cuadrados o rectangulares.", [("Sección máxima", "60 × 60 cm"), ("Altura", "Variable")]),
        ("Encofrados-apuntalamientos-ATES-Construction.png", "55% 50%", "Encofrado de planta y puntales", "Sistema de encofrado horizontal para forjados de diferentes tipologías estructurales. Los puntales, últimos en colocarse, sostienen el forjado.", [("Puntales", "Entre 1 y 6 m")]),
    ]
    sys_html = "".join(f"""
        <article class="formwork" data-reveal>
          <figure class="formwork__media media">{img(rel, f, t + ' en obra', p)}</figure>
          <div class="formwork__body">
            <span class="duo__num">{i + 1:02d}</span>
            <h3 class="h4">{e(t)}</h3>
            <p>{e(d)}</p>
            <dl class="formwork__data">{''.join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in data)}</dl>
          </div>
        </article>""" for i, (f, p, t, d, data) in enumerate(systems))
    return hero + f"""
  <section class="section" aria-labelledby="pres-title">
    <div class="wrap">
      {section_head('Comparativa', 'Presión admisible del hormigón.', '<p>Los dos sistemas de muro se diferencian por la presión de hormigón que admiten.</p>', hid='pres-title')}
      <div class="pressure" data-reveal>
        <div class="pressure__row"><span class="pressure__name">Serie ligera</span><span class="pressure__bar" style="--w: 66.6%"><span>40 kN/m²</span></span></div>
        <div class="pressure__row"><span class="pressure__name">Serie pesada</span><span class="pressure__bar pressure__bar--strong" style="--w: 100%"><span>60 kN/m²</span></span></div>
      </div>
    </div>
  </section>

  <section class="section section--tight" aria-labelledby="sys-title">
    <div class="wrap">
      {section_head('Sistemas', 'Un sistema para cada elemento estructural.', hid='sys-title')}
      <div class="formwork-grid" data-reveal-group>{sys_html}</div>
    </div>
  </section>

  <section class="section statband" aria-labelledby="cer-title">
    <div class="statband__panel">
      <div class="wrap statband__grid">
        <div class="statband__figure" data-reveal><span>Cerchas de</span><strong>3–9<small>m</small></strong><span>de altura · hasta 6 m de ancho</span></div>
        <div data-reveal>
          <p class="eyebrow eyebrow--light">Muros a una cara</p>
          <h2 class="h2 h2--light" id="cer-title">Cerchas para bataches y muros perimetrales.</h2>
          <p class="lead lead--light">Estructuras metálicas de gran resistencia que se superponen entre sí y aportan gran seguridad en muros a una cara y en el encofrado por bataches de muros perimetrales.</p>
          {checklist(['Desde 3 hasta 9 metros de altura en cada hormigonado', 'Hasta 6 metros de ancho', 'Módulos superponibles'], light=True)}
        </div>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="gal-title">
    <div class="wrap">
      {section_head('Galería', 'Encofrados ATES en obra.', hid='gal-title')}
      {gallery(rel, [
          ('Encofrados-serie-pesada-ATES-Construction.png', 'Vista general de una obra con encofrados de muro y pilares', 'Obra en fase estructural', 'Muros y pilares', '50% 50%', 'gal__item--wide gal__item--tall'),
          ('Encofrados-pilares-ATES-Construction.png', 'Encofrados de pilares rojos', 'Pilares', 'Paneles metálicos', '85% 50%'),
          ('Encofrados-serie-ligera-ATES-Construction.png', 'Encofrado de serie ligera en zapata corrida', 'Serie ligera', 'Cimentación', '50% 50%'),
          ('Encofrados-apuntalamientos-ATES-Construction.png', 'Puntales bajo forjado', 'Apuntalamiento', 'Forjado', '30% 50%', 'gal__item--wide'),
        ])}
      {source_note(OFFICIAL + 'servicios/construccion/')}
    </div>
  </section>
{related(rel, ['cimbras', 'gruas', 'auxiliar'])}
{contact_cta(rel, 'Encofrados y apuntalamientos', image='Encofrados-serie-pesada-ATES-Construction.png')}"""


def cimbras(rel):
    s = "cimbras"
    hero = page_hero(rel, variant="split", eyebrow="Construcción · Estructuras auxiliares", title="Cimbras y apeos estructurales.",
                     lead="Estructuras versátiles, realizadas a veces con los mismos elementos de un andamio de trabajo, cuya función es sustentar cargas en lugar de habilitar una zona de trabajo en altura.",
                     image="Cimbras-y-apeos-estructurales-ATES-Andamios.png", alt="Cimbra multidireccional sosteniendo un encofrado de forjado", pos="55% 50%", trail=T(rel, s),
                     actions=actions_service(rel, "Cimbras y apeos"), tag="Cimbra multidireccional")
    steps = [("hammer", "Un golpe de martillo", "Ajusta las cuñas de unión y permite alinear verticales, horizontales o diagonales al ángulo requerido."),
             ("layers", "Montaje en suelo o en vertical", "Las cimbras pueden montarse tumbadas en el suelo o directamente en su posición definitiva."),
             ("truck", "Traslado sin desmontar", "Se transportan de una estructura a otra sin necesidad de desmontarlas."),
             ("shield", "Estabilidad", "La unión multidireccional ahorra tiempo de montaje y aporta gran estabilidad y múltiples posibilidades formales.")]
    steps_html = "".join(f'<li class="step" data-reveal><span class="step__n">{i + 1:02d}</span>{icon(ic)}<h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (ic, t, d) in enumerate(steps))
    return hero + f"""
  <section class="section intro" aria-labelledby="intro-title">
    <div class="wrap intro__grid">
      <div data-reveal>
        <p class="eyebrow">Qué son</p>
        <h2 class="h2" id="intro-title">Sistemas de apeo de encofrados.</h2>
      </div>
      <div class="intro__text" data-reveal>
        <p class="lead">Las cimbras se componen de elementos verticales de apoyo y sistemas de conexión multidireccional entre sí. Así se logra versatilidad de uso y un montaje fácil.</p>
        <p>Permiten apear tanto cimbras cuajadas como torres independientes.</p>
        {chips(['Cimbras cuajadas', 'Torres independientes', 'Apeo de encofrados'])}
      </div>
    </div>
  </section>

  <section class="section section--tight" aria-labelledby="how-title">
    <div class="wrap">
      {section_head('Unión multidireccional', 'Cómo se monta una cimbra ATES.', hid='how-title')}
      <ol class="steps" data-reveal-group>{steps_html}</ol>
    </div>
  </section>

  <section class="section" aria-labelledby="gal-title">
    <div class="wrap">
      {section_head('Galería', 'Cimbras y estructuras multidireccionales.', hid='gal-title')}
      {gallery(rel, [
          ('Cimbras-y-apeos-estructurales-ATES-Construction.png', 'Cimbra bajo un encofrado de madera', 'Cimbra', 'Apeo de forjado', '62% 50%', 'gal__item--wide'),
          ('Andamios-multidireccional-europero-ATES-Construction.png', 'Estructura multidireccional en una presa', 'Sistema multidireccional', 'Infraestructura hidráulica', '62% 50%'),
          ('Cimbras-y-apeos-estructurales-ATES-Andamios.png', 'Detalle de nudos multidireccionales', 'Uniones', 'Nudos de cuña', '40% 50%'),
        ], cls='gal--3')}
      {source_note(OFFICIAL + 'servicios/construccion/andamios/')}
    </div>
  </section>
{related(rel, ['encofrados', 'andamios', 'estabilizadores'])}
{contact_cta(rel, 'Cimbras y apeos', image='Cimbras-y-apeos-estructurales-ATES-Construction.png', pos='60% 50%')}"""


def plataformas(rel):
    s = "plataformas"
    hero = page_hero(rel, variant="frame", eyebrow="Construcción · Trabajos en fachada", title="Plataformas motorizadas.",
                     lead="Plataformas para rehabilitación y obra nueva que se desplazan sobre mástiles con cremallera, con un plano de trabajo fijo, estable y seguro.",
                     image="Plataformas-ATES-Construction-motorizadas-rehabilitacion-fachadas.png", alt="Plataformas motorizadas ATES instaladas en la fachada de un edificio en rehabilitación", pos="70% 50%", trail=T(rel, s),
                     actions=actions_service(rel, "Plataformas motorizadas").replace("btn--line", "btn--glass"))
    parts = [("Motor reductor con piñones", "Impulsa la plataforma a lo largo del mástil."),
             ("Plataforma de trabajo", "Plano fijo y estable; sus extensibles se adaptan a la geometría de la fachada."),
             ("Mástiles con cremallera", "Guían el desplazamiento vertical del equipo.")]
    safety = ["Finales de carrera", "Dispositivos de nivelación", "Freno paracaídas", "Protecciones eléctricas",
              "Señalización acústica de movimiento", "Descenso manual de emergencia"]
    return hero + f"""
  <section class="section" aria-labelledby="sys-title">
    <div class="wrap anatomy">
      <div class="anatomy__text" data-reveal>
        <p class="eyebrow">El sistema</p>
        <h2 class="h2" id="sys-title">Tres componentes, un plano de trabajo estable.</h2>
        <ol class="anatomy__list">{''.join(f'<li><span>{i + 1:02d}</span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>' for i, (t, d) in enumerate(parts))}</ol>
      </div>
      <figure class="anatomy__media media" data-reveal>{img(rel, 'Plataformas-ATES-motorizadas-obra-nueva.png', 'Plataformas motorizadas desplazándose por sus mástiles en una fachada de obra nueva', '30% 50%')}<figcaption class="media__tag">Obra nueva</figcaption></figure>
    </div>
  </section>

  <section class="section band" aria-labelledby="safe-title">
    <div class="band__panel">
      <div class="wrap">
        {section_head('Seguridad', 'Equipos homologados con marcado CE.', '<p>Cumplen la directiva de la Comunidad Europea 89/392/CEE y están dotados de los siguientes elementos de seguridad.</p>', light=True, hid='safe-title')}
        <ul class="safety" data-reveal-group>{''.join(f'<li data-reveal>{icon("shield")}<span>{e(x)}</span></li>' for x in safety)}</ul>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="app-title">
    <div class="wrap intro__grid">
      <div data-reveal>
        <p class="eyebrow">Aplicaciones</p>
        <h2 class="h2" id="app-title">De lo más simple a lo más complejo.</h2>
        <p class="lead">A través de nuestro servicio técnico planificamos y diseñamos contigo cada proyecto para obtener el montaje más idóneo y seguro.</p>
      </div>
      <div data-reveal>
        {checklist(['Cerramientos de fachadas', 'Rehabilitación de edificios', 'Trabajos diversos en edificios altos', 'Soluciones especiales'])}
        <blockquote class="pull">Gracias a la seguridad y rapidez en los trabajos de fachada, el andamio motorizado está sustituyendo al andamio colgante por las ventajas de un plano fijo y estable de trabajo.</blockquote>
      </div>
    </div>
  </section>

  <section class="section section--tight" aria-labelledby="gal-title">
    <div class="wrap">
      {section_head('Rehabilitación y obra nueva', 'Plataformas ATES en fachada.', hid='gal-title')}
      {gallery(rel, [
          ('Plataformas-ATES-Construction-motorizadas-rehabilitacion-fachadas.png', 'Plataformas motorizadas ATES en rehabilitación', 'Rehabilitación', 'Plataforma con extensibles', '70% 50%', 'gal__item--wide gal__item--tall'),
          ('Plataformas-ATES-motorizadas-obra-nueva.png', 'Plataformas en fachada curva de obra nueva', 'Obra nueva', 'Fachada curva', '20% 50%'),
          ('Plataformas-ATES-motorizadas-obra-nueva.png', 'Mástiles de plataformas motorizadas en esquina de edificio', 'Mástiles', 'Desplazamiento vertical', '78% 50%'),
        ])}
      {source_note(OFFICIAL + 'servicios/construccion/plataformas-motorizadas/')}
    </div>
  </section>
{related(rel, ['andamios', 'montacargas', 'estabilizadores'])}
{contact_cta(rel, 'Plataformas motorizadas', image='Plataformas-ATES-motorizadas-obra-nueva.png', pos='40% 50%')}"""


def estabilizadores(rel):
    s = "estabilizadores"
    hero = page_hero(rel, variant="split", eyebrow="Construcción · Rehabilitación", title="Estabilizadores de fachadas.",
                     lead="Sistema versátil y diáfano que permite la sustentación y estabilización de fachadas o estructuras frente a los esfuerzos del viento.",
                     image="Estabilizadores-de-fachada-ATES-Construction.png", alt="Estabilizador de fachada multidireccional en un edificio histórico", pos="62% 50%", trail=T(rel, s),
                     actions=actions_service(rel, "Estabilizadores de fachadas"), tag="Edificio histórico en rehabilitación")
    return hero + f"""
  <section class="section" aria-labelledby="fn-title">
    <div class="wrap">
      {section_head('Función', 'Mantener la fachada en pie mientras se interviene.', hid='fn-title')}
      {features([
          ('building', 'Sustentación', 'Sostiene fachadas o estructuras durante la intervención.'),
          ('wind', 'Frente al viento', 'Estabiliza el conjunto frente a los esfuerzos del viento.'),
          ('grid', 'Versátil y diáfano', 'Un sistema que se adapta a cada fachada y deja libre el espacio de trabajo.'),
        ], cols=3)}
    </div>
  </section>

  <section class="section section--tight" aria-labelledby="ctx-title">
    <div class="wrap">
      <article class="feature-case" data-reveal>
        <figure class="feature-case__media media">{img(rel, 'Estabilizadores-de-fachada-ATES-Construction.png', 'Estructura multidireccional apuntalando la fachada de un edificio antiguo', '40% 50%')}</figure>
        <div class="feature-case__body">
          <p class="eyebrow">Parte del sistema de andamios</p>
          <h2 class="h3" id="ctx-title">Integrado con el andamio multidireccional</h2>
          <p>ATES presenta los estabilizadores dentro de su gama de andamios, junto al andamio de marco y multidireccional europeo, las cimbras y las escaleras de acceso.</p>
          <a class="btn btn--dark" href="{page_url(rel, 'andamios')}">Ver andamios {icon('arrow-right')}</a>
        </div>
      </article>
      {source_note(OFFICIAL + 'servicios/construccion/andamios/')}
    </div>
  </section>
{related(rel, ['andamios', 'cimbras', 'plataformas'])}
{contact_cta(rel, 'Estabilizadores de fachadas', image='Estabilizadores-de-fachada-ATES-Construction.png', pos='60% 50%')}"""


def escaleras(rel):
    s = "escaleras"
    hero = page_hero(rel, variant="split", eyebrow="Construcción · Accesos", title="Escaleras de acceso y servicio.",
                     lead="Se adaptan a cualquier tipología, permitiendo el acceso tanto público como privativo. Nuestros modelos permiten el desembarco del usuario de la forma más segura.",
                     image="Escaleras-de-acceso-ATES-Construction.png", alt="Torre de escalera de obra adosada a un edificio, con cartel de Andamios ATES", pos="55% 50%", trail=T(rel, s),
                     actions=actions_service(rel, "Escaleras de acceso"), tag="Escalera de acceso ATES")
    return hero + f"""
  <section class="section" aria-labelledby="fn-title">
    <div class="wrap">
      {section_head('Características', 'Acceso seguro a cualquier nivel de la obra.', hid='fn-title')}
      {features([
          ('layers', 'Cualquier tipología', 'Las escaleras se adaptan a la configuración de cada obra o edificio.'),
          ('users', 'Público o privativo', 'Para el acceso del personal de obra o del público, según el proyecto.'),
          ('shield', 'Desembarco seguro', 'Modelos que permiten al usuario desembarcar de la forma más segura.'),
        ], cols=3)}
    </div>
  </section>

  <section class="section section--tight" aria-labelledby="gal-title">
    <div class="wrap">
      {section_head('Galería', 'Escaleras ATES en obra.', hid='gal-title')}
      {gallery(rel, [
          ('Escaleras-de-acceso-ATES-Construction.png', 'Escalera de obra de varios tramos adosada a una nave', 'Torre de escalera', 'Varios tramos con descansillos', '55% 50%', 'gal__item--wide'),
          ('Escaleras-de-acceso-ATES-Andamios.png', 'Escalera de acceso y servicio en obra', 'Escalera de servicio', 'Acceso a plataformas', '50% 50%', 'gal__item--wide'),
        ], cls='gal--2')}
      {source_note(OFFICIAL + 'servicios/construccion/andamios/')}
    </div>
  </section>
{related(rel, ['andamios', 'plataformas', 'montacargas'])}
{contact_cta(rel, 'Escaleras de acceso', image='Escaleras-de-acceso-ATES-Construction.png', pos='55% 50%')}"""


# ======================================================================= TECNOLOGÍAS · interiores
def inspeccion(rel):
    s = "inspeccion"
    hero = page_hero(rel, variant="dark", eyebrow="ATES Technologies · Robótica", title="Inspección de infraestructuras hidráulicas.",
                     lead="Un rover propio para inspeccionar tuberías forzadas, canales de carga y galerías de centrales hidráulicas, sin depender de trabajos verticales o andamios.",
                     image="Inspecciones-infraestructuras-hidraulicas-rover-proyectos-Ates.png", alt="Rover de inspección iluminando el interior de una tubería forzada", pos="100% 50%", trail=T(rel, s),
                     actions=actions_service(rel, "Inspección de infraestructuras").replace("btn--line", "btn--glass"))
    return hero + f"""
  <section class="section intro" aria-labelledby="intro-title">
    <div class="wrap intro__grid">
      <div data-reveal>
        <p class="eyebrow">El reto</p>
        <h2 class="h2" id="intro-title">Infraestructuras con más de 60 años de media.</h2>
      </div>
      <div class="intro__text" data-reveal>
        <p class="lead">La edad media de estas infraestructuras en España supera los 60 años. Conocer su estado real permite optimizar los periodos de mantenimiento y su alcance.</p>
        <p>Las infraestructuras enterradas se han inspeccionado tradicionalmente mediante trabajos verticales o andamios. Si la inspección puede repetirse de forma recurrente, permite ver la evolución del estado e incluso analizar la ampliación de la vida útil de la instalación.</p>
      </div>
    </div>
  </section>

  <section class="section tech-svcs" aria-labelledby="rover-title">
    <div class="tech__panel">
      <div class="tech__lines" aria-hidden="true"></div>
      <div class="wrap rover">
        <figure class="rover__media media" data-reveal>{img(rel, 'Inspecciones-infraestructuras-hidraulicas-rover-proyectos-Ates.png', 'Técnico preparando el rover sobre su bastidor antes de introducirlo en la tubería', '0% 50%')}</figure>
        <div class="rover__text" data-reveal>
          <p class="eyebrow eyebrow--light">El rover</p>
          <h2 class="h2 h2--light" id="rover-title">Diseñado para tuberías forzadas y canales de carga.</h2>
          <p class="lead lead--light">El primer proyecto desarrollado por ATES Technologies: un rover para inspeccionar grandes infraestructuras hidráulicas de forma autónoma y sensorizada.</p>
          {checklist(['Tuberías forzadas', 'Canales de carga de centrales hidroeléctricas', 'Galerías de centrales hidráulicas', 'Inspección visual y modelizado 3D'], light=True)}
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="caso" aria-labelledby="case-title">
    <div class="wrap">
      {section_head('Caso publicado', 'Salto de Moncabril (Zamora).', '<p>Inspección de una canal de carga de hormigón con más de 60 años de antigüedad en una central hidroeléctrica propiedad de ENDESA/ENEL.</p>', hid='case-title')}
      <div class="timeline" data-reveal-group>
        <div class="tl" data-reveal><span class="tl__n">01</span><h3>Objetivo</h3><p>Los técnicos del propietario querían conocer a fondo el estado de la conducción para analizar su nivel de degradación.</p></div>
        <div class="tl" data-reveal><span class="tl__n">02</span><h3>Inspección</h3><p>Con la introducción del rover se realizó una inspección visual y un modelizado 3D de la canal.</p></div>
        <div class="tl" data-reveal><span class="tl__n">03</span><h3>Resultado</h3><p>El análisis estructural confirmó el buen estado de la conducción y permite optimizar sus periodos de mantenimiento.</p></div>
      </div>
      {gallery(rel, [
          ('Salto_de_Moncabril_inspeccion_Zamora.png', 'Equipo técnico dentro del canal de carga con el rover', 'Equipo en canal', 'Preparación de la inspección', '6% 50%'),
          ('Salto_de_Moncabril_inspeccion_Zamora.png', 'Rover suspendido durante el descenso a la galería', 'Descenso del rover', 'Inspección vertical', '68% 50%'),
          ('Salto_de_Moncabril_inspeccion_Zamora.png', 'Interior de la tubería iluminado por el rover', 'Interior de la conducción', 'Inspección visual', '100% 50%'),
          ('Inspecciones-infraestructuras-complejidad-innovacion-ATES.png', 'Modelo 3D de la sección de una tubería con desviaciones por colores', 'Modelizado 3D', 'Análisis de la sección', '0% 50%', 'gal__item--wide'),
          ('Salto_de_Moncabril_zamora_inspeccion.png', 'Modelo 3D de una conducción con mapa de desviaciones', 'Modelo de la conducción', 'Mapa de desviaciones', '100% 50%', 'gal__item--wide'),
        ], cls='gal--case')}
      {source_note('https://www.ates.es/ates-technologies-inteligencia-artificial-y-grandes-infraestructuras/', 'Fuente')}
    </div>
  </section>
{related(rel, ['shm', 'ia', 'andamios'], title='Otras soluciones tecnológicas')}
{contact_cta(rel, 'Inspección de infraestructuras', title='¿Necesitas inspeccionar una conducción?', image='tuberias-inspecciones-ATES-Technologies.png', pos='45% 50%')}"""


def shm(rel):
    s = "shm"
    hero = page_hero(rel, variant="dark", eyebrow="ATES Technologies · Sensorización", title="Monitorización estructural (SHM).",
                     lead="Structural Health Monitoring: seguimiento del estado y del comportamiento estructural de grandes infraestructuras mediante sensores y análisis de datos.",
                     image="Inspecciones-Inteligentes-ATES-Technologies.png", alt="Presa de hormigón en arco vista desde el aire", pos="50% 50%", trail=T(rel, s),
                     actions=actions_service(rel, "Monitorización estructural SHM").replace("btn--line", "btn--glass"))
    infra = ["Puentes y viaductos", "Túneles", "Presas", "Edificios singulares", "Estructuras offshore"]
    pipe = [("database", "Big Data", "Tratar el conjunto de datos generados a lo largo de los años."),
            ("scan", "Data Mining", "Localizar patrones repetitivos de las situaciones desfavorables."),
            ("brain", "Machine Learning", "Que el sistema aprenda a localizar situaciones de alerta o de fallo, y a predecir el comportamiento de la infraestructura.")]
    return hero + f"""
  <section class="section intro" aria-labelledby="intro-title">
    <div class="wrap intro__grid">
      <div data-reveal>
        <p class="eyebrow">Qué infraestructuras</p>
        <h2 class="h2" id="intro-title">Obras civiles que necesitan inspección periódica.</h2>
        {chips(infra)}
      </div>
      <div class="intro__text" data-reveal>
        <p class="lead">Además de la imprescindible inspección visual por técnicos que conocen la infraestructura, se disponen sensores para seguir su estado y su comportamiento estructural.</p>
        <p>Los sensores informan con frecuencia horaria, diaria, semanal, mensual o anual, y sus datos se completan con campañas topográficas o inspecciones visuales con dron. La cantidad de información resultante es muy elevada. Hoy, en infraestructuras como las presas, el seguimiento suele hacerse con sistemas SCADA que emiten una alerta cuando un sensor supera un umbral.</p>
      </div>
    </div>
  </section>

  <section class="section tech-svcs" aria-labelledby="pipe-title">
    <div class="tech__panel">
      <div class="tech__lines" aria-hidden="true"></div>
      <div class="wrap">
        {section_head('Del dato a la predicción', 'Tres capas de análisis.', light=True, hid='pipe-title')}
        <ol class="pipeline" data-reveal-group>{''.join(f'<li data-reveal><span class="pipeline__n">{i + 1:02d}</span>{icon(ic)}<h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (ic, t, d) in enumerate(pipe))}</ol>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="ben-title">
    <div class="wrap">
      <article class="feature-case" data-reveal>
        <figure class="feature-case__media media">{img(rel, 'SHM-Ingenieria-artificial_Technologies_Ates_001.png', 'Tableta mostrando los puntos de control sobre la imagen de una presa', '100% 50%')}</figure>
        <div class="feature-case__body">
          <p class="eyebrow">Beneficios</p>
          <h2 class="h3" id="ben-title">Análisis de datos en tiempo real.</h2>
          {checklist(['Descarte inmediato de datos erróneos', 'Mayor capacidad de detección de anomalías de comportamiento', 'Detección más temprana, con tiempo para el análisis y la acción', 'Valoración de la capacidad de operación de la infraestructura'])}
        </div>
      </article>
      {gallery(rel, [
          ('Structual-health-monitoring-SHM.png', 'Puesto de control con varios monitores de supervisión', 'Centro de control', 'Supervisión de datos', '50% 50%', 'gal__item--wide'),
          ('SHM-Ingenieria-artificial_Technologies_Ates_001.png', 'Interfaz de supervisión de una presa', 'Interfaz SCADA', 'Esquema de la presa', '0% 50%', 'gal__item--wide'),
        ], cls='gal--2')}
      {source_note('https://www.ates.es/ates-technologies-inteligencia-artificial-y-grandes-infraestructuras/', 'Fuente')}
    </div>
  </section>
{related(rel, ['ia', 'inspeccion', 'tecnologias'], title='Otras soluciones tecnológicas')}
{contact_cta(rel, 'Monitorización estructural SHM', title='¿Quieres anticiparte a una anomalía?', image='Inspecciones-Inteligentes-ATES-Technologies.png', pos='50% 70%')}"""


def ia(rel):
    s = "ia"
    hero = page_hero(rel, variant="dark", eyebrow="ATES Technologies · Datos", title="Inteligencia artificial aplicada.",
                     lead="Especialistas en Big Data, Deep Learning y Machine Learning, y en Digital Twin, aplicados a la operación y el mantenimiento de infraestructuras.",
                     image="Proyectos-Inteligencia-Artificial-Big-Data-ATES-Technologies.png", alt="Mano sujetando una tableta con la marca ATES Technologies sobre una mesa interactiva", pos="70% 50%", trail=T(rel, s),
                     actions=actions_service(rel, "Inteligencia artificial").replace("btn--line", "btn--glass"))
    disc = [("database", "Big Data", "Tratamiento de grandes volúmenes de datos de sensores e inspecciones."),
            ("brain", "Deep Learning", "Modelos de aprendizaje profundo para interpretar información compleja."),
            ("activity", "Machine Learning", "Sistemas que aprenden a detectar situaciones de alerta o fallo."),
            ("cube", "Digital Twin", "Réplicas digitales de la infraestructura como soporte del análisis.")]
    return hero + f"""
  <section class="section" aria-labelledby="disc-title">
    <div class="wrap">
      {section_head('Especialidades', 'Cuatro disciplinas, un objetivo: decidir con datos.', hid='disc-title')}
      {features(disc, cols=4)}
    </div>
  </section>

  <section class="section tech-svcs" aria-labelledby="fire-title">
    <div class="tech__panel">
      <div class="tech__lines" aria-hidden="true"></div>
      <div class="wrap rover">
        <div class="rover__text" data-reveal>
          <p class="eyebrow eyebrow--light">Proyecto en desarrollo</p>
          <h2 class="h2 h2--light" id="fire-title">Detección temprana de incendios en la extracción minera.</h2>
          <p class="lead lead--light">Una explotación minera ocupa decenas de km², con múltiples zonas de riesgo de incendio. ATES Technologies desarrolla un sistema centralizado que procesa datos de distintos sistemas de detección.</p>
          {checklist(['Un único centro de control para localizar el incendio y determinar su tipo', 'Drones y rovers para la observación y la extinción', 'Dimensionamiento de brigadas y vehículos según el incendio', 'Red de comunicaciones diseñada ad hoc, con ciberseguridad propia', 'Alimentación parcial con energías renovables'], light=True)}
          <p class="tech-note">Tecnologías previstas: FireTir, Flir y Siemens.</p>
        </div>
        <figure class="rover__media media" data-reveal>{img(rel, 'Proyectos-Inteligencia-Artificial-Big-Data-ATES-Technologies.png', 'Tableta de ATES Technologies sobre una mesa con datos', '70% 50%')}</figure>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="apply-title">
    <div class="wrap">
      <article class="feature-case feature-case--reverse" data-reveal>
        <figure class="feature-case__media media">{img(rel, 'Inspecciones-infraestructuras-complejidad-innovacion-ATES.png', 'Modelo 3D de una conducción coloreado según desviaciones', '100% 50%')}</figure>
        <div class="feature-case__body">
          <p class="eyebrow">Aplicación</p>
          <h2 class="h3" id="apply-title">De la inspección al modelo de comportamiento.</h2>
          <p>La IA se aplica también a la monitorización estructural: con Big Data, Data Mining y Machine Learning, el sistema aprende a predecir el comportamiento de la infraestructura bajo condiciones hipotéticas.</p>
          <a class="btn btn--dark" href="{page_url(rel, 'shm')}">Ver monitorización SHM {icon('arrow-right')}</a>
        </div>
      </article>
      {source_note('https://www.ates.es/ates-technologies-inteligencia-artificial-y-grandes-infraestructuras/', 'Fuente')}
    </div>
  </section>
{related(rel, ['shm', 'inspeccion', 'tecnologias'], title='Otras soluciones tecnológicas')}
{contact_cta(rel, 'Inteligencia artificial', title='¿Tienes datos que aún no hablan?', image='Structual-health-monitoring-SHM.png', pos='60% 50%')}"""


# ======================================================================= CONTACTO / 404
def contacto(rel):
    s = "contacto"
    opts = ["Asesoramiento técnico", "Maquinaria", "Grúas torre y automontantes", "Montacargas", "Maquinaria auxiliar",
            "Construcción", "Andamios", "Encofrados y apuntalamientos", "Cimbras y apeos", "Plataformas motorizadas",
            "Estabilizadores de fachadas", "Escaleras de acceso", "ATES Technologies", "Inspección de infraestructuras",
            "Monitorización estructural SHM", "Inteligencia artificial"]
    options = "".join(f'<option>{e(o)}</option>' for o in opts)
    return f"""
  <section class="contact-hero" aria-labelledby="page-title">
    <div class="wrap">
      {breadcrumbs(rel, [('Inicio', ''), ('Contacto', None)])}
      <p class="eyebrow">Contacto</p>
      <h1 class="phero__title phero__title--dark" id="page-title">Hablemos de tu proyecto.</h1>
      <p class="lead">Cuéntanos qué necesitas y nuestro equipo te ayudará a encontrar la alternativa más adecuada.</p>
    </div>
  </section>
  <section class="section section--tight contact" aria-label="Formulario y datos de contacto">
    <div class="wrap contact__grid">
      <form class="form" id="formulario" data-contact-form novalidate>
        <h2 class="h3">Solicitar información</h2>
        <p class="form__hint">Al enviar se abrirá tu correo con la solicitud preparada para info@ates.es.</p>
        <div class="form__row">
          <label class="field"><span>Nombre*</span><input name="nombre" autocomplete="name" required></label>
          <label class="field"><span>Empresa</span><input name="empresa" autocomplete="organization"></label>
        </div>
        <div class="form__row">
          <label class="field"><span>Email*</span><input type="email" name="email" autocomplete="email" required></label>
          <label class="field"><span>Teléfono</span><input type="tel" name="telefono" autocomplete="tel"></label>
        </div>
        <label class="field"><span>Solución</span><select name="asunto" data-subject>{options}</select></label>
        <label class="field"><span>Mensaje*</span><textarea name="mensaje" rows="5" required placeholder="Tipo de obra, ubicación, plazos…"></textarea></label>
        <p class="form__error" role="alert" data-form-error hidden>Completa nombre, un email válido y el mensaje.</p>
        <button class="btn btn--red btn--lg" type="submit">Preparar solicitud {icon('mail')}</button>
      </form>
      <aside class="contact__aside">
        <div class="contact-card">
          <h2 class="h4">Oficinas en España</h2>
          <ul>
            <li><a href="tel:+34902171517">{icon('phone')}<span>(+34) 902 171 517<small>Oficinas</small></span></a></li>
            <li><a href="tel:+34648611411">{icon('phone')}<span>(+34) 648 611 411<small>Móvil</small></span></a></li>
            <li><a href="mailto:info@ates.es">{icon('mail')}<span>info@ates.es<small>Correo general</small></span></a></li>
          </ul>
        </div>
        <div class="contact-card contact-card--dark">
          <h2 class="h4">Aviso de averías 24 horas</h2>
          <a class="contact-card__big" href="tel:+34962524400">962 524 400</a>
        </div>
        <div class="contact-card">
          <h2 class="h4">Chile</h2>
          <ul>
            <li><a href="tel:+56992018943">{icon('phone')}<span>+56 9 9201 8943<small>Oficinas centrales</small></span></a></li>
            <li><a href="mailto:info@ates.cl">{icon('mail')}<span>info@ates.cl</span></a></li>
          </ul>
        </div>
        {ext(OFFICIAL + 'donde-estamos/', 'Ver delegaciones en ates.es')}
      </aside>
    </div>
  </section>"""


def notfound(rel):
    return f"""
  <section class="contact-hero notfound" aria-labelledby="page-title">
    <div class="wrap">
      <p class="eyebrow">Error 404</p>
      <h1 class="phero__title phero__title--dark" id="page-title">Esta página no existe.</h1>
      <p class="lead">Puede que la dirección haya cambiado. Estas son las áreas principales de ATES:</p>
      <div class="hero__actions">
        <a class="btn btn--red" href="{page_url(rel, 'maquinaria')}">Maquinaria</a>
        <a class="btn btn--dark" href="{page_url(rel, 'construccion')}">Construcción</a>
        <a class="btn btn--dark" href="{page_url(rel, 'tecnologias')}">Tecnologías</a>
        <a class="btn btn--line" href="{link(rel, '')}">Volver al inicio</a>
      </div>
    </div>
  </section>"""


RENDER = {
    "home": home, "maquinaria": maquinaria, "construccion": construccion, "tecnologias": tecnologias,
    "gruas": gruas, "montacargas": montacargas, "auxiliar": auxiliar,
    "andamios": andamios, "encofrados": encofrados, "cimbras": cimbras, "plataformas": plataformas,
    "estabilizadores": estabilizadores, "escaleras": escaleras,
    "inspeccion": inspeccion, "shm": shm, "ia": ia, "contacto": contacto, "404": notfound,
}
DARK = {"tecnologias", "inspeccion", "shm", "ia"}
