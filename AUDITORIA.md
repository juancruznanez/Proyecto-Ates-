# Auditoría de ates.es e inventario de páginas

Fuente: `https://www.ates.es/sitemap_index.xml` (Yoast) → `page-sitemap.xml` (21 páginas) y
`post-sitemap.xml` (11 noticias), más la navegación de header/footer y los enlaces internos de cada
página. Auditoría realizada el 14-11-2026.

## 1. Páginas oficiales dentro del alcance

La web oficial **no tiene** páginas independientes para grúas, encofrados, cimbras, estabilizadores,
escaleras ni montacargas: viven como pestañas dentro de `/servicios/construccion/` y
`/servicios/construccion/andamios/`. Tecnologías es una sola página y una noticia amplía su contenido.

| Página original | Servicio | URL original | Contenido disponible | Acción | Nueva ruta (prototipo) |
|---|---|---|---|---|---|
| Home | Corporativo | `/` | 50 años, cinco áreas, certificados, contacto | Rediseñar | `/` |
| Página general | Construcción | `/servicios/construccion/` | Andamios, grúas, encofrados, plataformas, maquinaria auxiliar, montacargas | Rediseñar y **dividir** en Maquinaria + Construcción | `/maquinaria/` · `/construccion/` |
| Página de servicio | Andamios | `/servicios/construccion/andamios/` | Marco europeo, multidireccional, normas UNE-EN 12810/12811, cimbras, estabilizadores, escaleras | Rediseñar | `/construccion/andamios/` |
| Página de servicio | Plataformas motorizadas | `/servicios/construccion/plataformas-motorizadas/` | Sistema, directiva 89/392/CEE, seguridad, aplicaciones | Rediseñar | `/construccion/plataformas-motorizadas/` |
| Página de servicio | Maquinaria auxiliar | `/servicios/construccion/maquinaria-auxiliar/` | 13 familias con potencias, pesos y modelos | Rediseñar como catálogo con filtros | `/maquinaria/maquinaria-auxiliar/` |
| Página general | Tecnologías | `/servicios/tecnologias/` | Inspección, robótica, IA, Big Data, Digital Twin | Rediseñar | `/tecnologias/` |
| Noticia | ATES Technologies | `/ates-technologies-inteligencia-artificial-y-grandes-infraestructuras/` | Rover, Moncabril, IA en minería, SHM | Contenido reorganizado en 3 páginas | `/tecnologias/…` |
| Contacto | Corporativo | `/contacto/` | Emails, teléfonos | Rediseñar | `/contacto/` |

Fuera de alcance (otras áreas de negocio): Ascensores, Soluciones energéticas, Industrial,
Medioambiente, PCI, placas solares, encuesta, empleo y páginas legales (se enlazan a la web oficial).

## 2. Contenido reorganizado (pestañas oficiales → páginas propias del prototipo)

| Contenido oficial | Dónde está hoy | Nueva ruta propuesta | Justificación |
|---|---|---|---|
| Grúas torre y automontantes | Pestaña en `/servicios/construccion/` | `/maquinaria/gruas-torre-automontantes/` | ATES las presenta juntas en un mismo bloque; una sola página con dos secciones evita duplicar contenido |
| Montacargas y elevadores de obra | Pestaña en `/servicios/construccion/` | `/maquinaria/montacargas/` | Datos propios: 500–2.000 kg, palet europeo, plataforma de 3,30 m, homologación para personas |
| Encofrados y apuntalamientos | Pestaña en `/servicios/construccion/` | `/construccion/encofrados-apuntalamientos/` | Seis sistemas con datos técnicos publicados |
| Cimbras y apeos estructurales | Pestaña en `/andamios/` | `/construccion/cimbras-apeos/` | Texto técnico amplio sobre unión multidireccional |
| Estabilizadores de fachadas | Pestaña en `/andamios/` | `/construccion/estabilizadores-fachadas/` | Contenido breve: página compacta, sin rellenar con datos no publicados |
| Escaleras de acceso y servicio | Pestaña en `/andamios/` | `/construccion/escaleras-acceso/` | Contenido breve: página compacta |
| Inspección de infraestructuras (rover, Moncabril) | Noticia + `/servicios/tecnologias/` | `/tecnologias/inspeccion-infraestructuras/` | Caso real publicado con detalle |
| SHM – Structural Health Monitoring | Noticia | `/tecnologias/monitorizacion-estructural/` | Servicio descrito en la noticia oficial |
| IA, Big Data, Machine Learning, Digital Twin | `/servicios/tecnologias/` + noticia | `/tecnologias/inteligencia-artificial/` | Proyecto de detección temprana de incendios + análisis de datos |

## 3. Decisiones de arquitectura

- **No se crean** `/tecnologias/digital-twin/` ni `/tecnologias/robotica-sensorizacion/`: la web oficial solo
  nombra "Digital Twin" y la robótica se concreta en el rover. Se integran en las páginas de inspección,
  SHM e IA para no inventar contenido.
- **Grúas automontantes** no tiene ruta propia: ATES solo publica "varios modelos de grúas automontantes".
  Tiene sección anclada `#automontantes` dentro de la página de grúas, enlazada desde el mega menú.
- **Maquinaria auxiliar** pasa de Construcción a Maquinaria (es una familia de equipos), y se enlaza
  también desde Construcción. Una única URL.
- Las noticias de proyectos (Parotet, chimeneas, Castillo de los Funes, Moncabril) se citan con su
  enlace oficial; no se crean páginas de proyecto.
- Páginas nuevas sin equivalente oficial: ninguna con contenido inventado. `/contacto/` y `404` son
  páginas de servicio del prototipo.

## 4. Inventario final de rutas del prototipo

```
/
├── maquinaria/
│   ├── gruas-torre-automontantes/      (reorganizada · #gruas-torre · #automontantes)
│   ├── montacargas/                    (reorganizada)
│   └── maquinaria-auxiliar/            (oficial rediseñada)
├── construccion/
│   ├── andamios/                       (oficial rediseñada)
│   ├── encofrados-apuntalamientos/     (reorganizada)
│   ├── cimbras-apeos/                  (reorganizada)
│   ├── plataformas-motorizadas/        (oficial rediseñada)
│   ├── estabilizadores-fachadas/       (reorganizada)
│   └── escaleras-acceso/               (reorganizada)
├── tecnologias/
│   ├── inspeccion-infraestructuras/    (reorganizada)
│   ├── monitorizacion-estructural/     (reorganizada)
│   └── inteligencia-artificial/        (reorganizada)
├── contacto/                           (oficial rediseñada)
└── 404.html
```

## 5. Datos y textos utilizados (todos publicados por ATES)

- Fundada en 1968; más de 50 años de experiencia; certificados SGS ISO 9001, 14001 y 45001.
- Andamios: uno de los mayores parques de la Comunidad Valenciana; alquiler y venta; UNE-EN 12810 y 12811 (CEN).
- Grúas: gran diversidad de modelos de grúas torre, varios de automontantes; alquiler y venta; servicio técnico con más de 40 años de experiencia.
- Encofrados: serie ligera 40 kN/m², serie pesada 60 kN/m², pilares hasta 60 × 60 cm, cerchas de 3 a 9 m de alto y hasta 6 m de ancho, puntales de 1 a 6 m.
- Plataformas: directiva 89/392/CEE, marcado CE, elementos de seguridad enumerados.
- Montacargas: de 500 a 2.000 kg, palet europeo, plataforma de hasta 3,30 m, homologación para personas.
- Maquinaria auxiliar: modelos y rangos tal como figuran en el catálogo oficial.
- Tecnologías: spin-off con investigadores de la Universidad Carlos III; rover para tuberías forzadas y canales de carga; Moncabril (Zamora); SHM con Big Data, Data Mining y Machine Learning; proyecto de IA para detección temprana de incendios en minería (en desarrollo).

## 6. Limitaciones

- **Skill Kowalsky**: no existe en el entorno. Se aplica la skill de diseño de interfaces de Emil Kowalski.
- **Mejora de fotografías con IA**: el entorno no dispone de un modelo de generación o edición de imágenes,
  y las dos fotografías "adjuntas por el usuario" que menciona el brief no están en la carpeta del proyecto.
  No se han generado imágenes. Se homogeneiza el tratamiento con un mismo etalonaje CSS (saturación,
  contraste y capas de contraste comunes). Ver sección de prompts en `FOTOGRAFIA-IA.md`.
- **React/Vite**: Node no está instalado. El sitio se genera con un script de Python sin dependencias
  (`build/build.py`) que produce HTML estático por ruta: cada URL existe como `ruta/index.html`, funciona
  al acceder directamente y al recargar.
