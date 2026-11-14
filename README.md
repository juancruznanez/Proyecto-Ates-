# ATES · Maquinaria, Construcción y Tecnologías — prototipo de rediseño integral

Prototipo conceptual **privado** para una presentación profesional a Grupo ATES. No es la web oficial
y no debe presentarse como tal (todas las páginas llevan `noindex`).

## Ver la web

```bash
cd web && python3 -m http.server 5173
```

Abrir http://localhost:5173 — cada ruta es una carpeta con su `index.html`, así que funciona al entrar
directamente por URL y al recargar.

## Regenerar el sitio

El HTML se genera con un script de Python sin dependencias (Node no está instalado en este equipo):

```bash
python3 build/build.py
```

```
build/
├── components.py   Componentes globales: Header + MegaMenu, Footer, Breadcrumbs, PageHero, Specs,
│                   Features, Gallery, RelatedServices, ContactCTA (equivalentes a componentes React)
├── pages.py        Registro de rutas, navegación y contenido/composición de cada página
├── crops.py        Recortes de dípticos y pestañas laterales de las fotos oficiales (sips)
├── images.json     Archivo → ruta oficial en ates.es/wp-content/uploads
├── sprite.svg      Iconos Lucide
└── build.py        Genera /web
web/
├── assets/css/styles.css   Tokens (variables CSS) + estilos por componente + responsive
├── assets/js/main.js       Mega menú, menú móvil, filtros de catálogo, formulario, animaciones
└── assets/img/ates/        Copias locales de fotos oficiales (+ c/ recortes)
```

## Documentación

- [AUDITORIA.md](AUDITORIA.md) — auditoría de ates.es, inventario y arquitectura de rutas.
- [QA.md](QA.md) — matriz de control de calidad por página.
- [DIRECCION-DE-ARTE.md](DIRECCION-DE-ARTE.md) — paleta, tipografía y movimiento.
- [FOTOGRAFIA-IA.md](FOTOGRAFIA-IA.md) — tratamiento fotográfico y prompts de mejora con IA (no ejecutados).
