# Matriz de control de calidad — 14-11-2026

## Comprobaciones automáticas (todas las páginas)

Script ejecutado en el navegador sobre las 18 rutas × 4 anchos (1440, 1280, 768 y 390 px) = 72 renders:

| Comprobación | Resultado |
|---|---|
| Desbordamiento horizontal | 0 casos |
| Un único `<h1>` por página | 18/18 |
| Imágenes rotas | 0 |
| Imágenes sin `alt` | 0 |
| `<title>` únicos | 18/18 |
| Enlaces internos (17 rutas distintas) | 17/17 responden 200 |
| Enlaces externos (24) | 23 responden 200; LinkedIn devuelve 403 a peticiones automáticas (URL oficial publicada en ates.es) |
| URL de fotos oficiales (46) | 46/46 responden 200 |
| Poppins cargada (400–800) | Sí (Google Fonts) |
| Logotipo | Archivo original `2019/03/Logotipo-ATES.png`, sin modificar |

## Matriz por página

Leyenda: ✔ revisado y correcto. "Visual" = revisión con captura en el navegador.

| Página | Ruta | Tipo | Diseño | Fotografía | Navegación | Responsive | QA visual |
|---|---|---|---|---|---|---|---|
| Home | `/` | Oficial rediseñada | ✔ | ✔ | ✔ mega menú, anclas | ✔ | ✔ escritorio y móvil |
| Maquinaria | `/maquinaria/` | Nueva (contenido oficial reorganizado) | ✔ | ✔ | ✔ | ✔ | ✔ escritorio |
| Grúas torre y automontantes | `/maquinaria/gruas-torre-automontantes/` | Reorganizada | ✔ | ✔ | ✔ anclas `#gruas-torre` `#automontantes` | ✔ | ✔ automática |
| Montacargas | `/maquinaria/montacargas/` | Reorganizada | ✔ | ✔ | ✔ | ✔ | ✔ automática |
| Maquinaria auxiliar | `/maquinaria/maquinaria-auxiliar/` | Oficial rediseñada | ✔ | ✔ | ✔ filtros + `#elevacion` | ✔ | ✔ escritorio |
| Construcción | `/construccion/` | Oficial rediseñada | ✔ | ✔ | ✔ | ✔ | ✔ automática |
| Andamios | `/construccion/andamios/` | Oficial rediseñada | ✔ | ✔ | ✔ | ✔ | ✔ escritorio |
| Encofrados y apuntalamientos | `/construccion/encofrados-apuntalamientos/` | Reorganizada | ✔ | ✔ | ✔ | ✔ | ✔ escritorio |
| Cimbras y apeos | `/construccion/cimbras-apeos/` | Reorganizada | ✔ | ✔ | ✔ | ✔ | ✔ automática |
| Plataformas motorizadas | `/construccion/plataformas-motorizadas/` | Oficial rediseñada | ✔ | ✔ | ✔ | ✔ | ✔ móvil |
| Estabilizadores de fachadas | `/construccion/estabilizadores-fachadas/` | Reorganizada (compacta) | ✔ | ✔ | ✔ | ✔ | ✔ automática |
| Escaleras de acceso | `/construccion/escaleras-acceso/` | Reorganizada (compacta) | ✔ | ✔ | ✔ | ✔ | ✔ automática |
| Tecnologías | `/tecnologias/` | Oficial rediseñada | ✔ | ✔ | ✔ | ✔ | ✔ escritorio |
| Inspección de infraestructuras | `/tecnologias/inspeccion-infraestructuras/` | Reorganizada | ✔ | ✔ | ✔ ancla `#caso` | ✔ | ✔ móvil |
| Monitorización estructural (SHM) | `/tecnologias/monitorizacion-estructural/` | Reorganizada | ✔ | ✔ | ✔ | ✔ | ✔ automática |
| Inteligencia artificial | `/tecnologias/inteligencia-artificial/` | Reorganizada | ✔ | ✔ | ✔ | ✔ | ✔ automática |
| Contacto | `/contacto/` | Oficial rediseñada | ✔ | — | ✔ asunto precargado | ✔ | ✔ validación probada |
| 404 | `/404.html` | Nueva | ✔ | — | ✔ | ✔ | ✔ automática |

## Funcionalidad verificada

- Mega menú: abre por clic y teclado; con ratón, al pasar con retardo de 120 ms; se cierra con Escape, al salir y al hacer clic fuera.
- Menú móvil: acordeones por área; se cierra al elegir un enlace.
- Catálogo: 5 filtros con contador; `#elevacion` aplica el filtro al entrar desde Montacargas.
- Formulario: valida nombre, email y mensaje; precarga la solución desde `?asunto=`; prepara un correo a info@ates.es (no envía datos a terceros).
- Todos los CTA llevan a contacto, teléfono, email o a la página oficial correspondiente; no hay botones sin acción.

## Contenido técnico

Todos los datos (capacidades, presiones, normas, modelos, proyectos) proceden de ates.es; cada página
interior enlaza su fuente oficial al pie. Dos descripciones de andamios y una lista de grúas se
reescribieron durante la revisión para ajustarlas al texto publicado.

## Pendiente / limitaciones conocidas

- Fotografías mejoradas con IA: no generadas (ver `FOTOGRAFIA-IA.md`).
- Las fotos oficiales tienen poca resolución (≈ 900 px de ancho, salvo el Castillo de los Funes a 2560 px); en heros de 1440 px se ven suaves.
- `404.html` solo actúa como página de error en un servidor que lo configure; el servidor de Python no lo usa.
