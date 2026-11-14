# ATES · Maquinaria, Construcción y Tecnologías
## Dirección de arte — prototipo conceptual (uso privado, presentación profesional)

### Idea
**"Ingeniería editorial."** Una web que se lee como un dossier industrial bien maquetado: grandes
fotografías reales de ATES enmarcadas en contenedores redondeados sobre un fondo gris cálido,
titulares Poppins compactos y un único color de acción — el rojo corporativo de ATES.

### Cómo se combinan las referencias
| Referencia | Qué se toma | Dónde aparece |
| --- | --- | --- |
| 01 · Hero minimalista | Fondo gris cálido, contenedor con márgenes, hero fotográfico redondeado, navegación flotante, titulares blancos en mayúsculas, chips de confianza a la derecha | Estructura general, header, hero |
| 02 · Industrial corporativa | Contraste blanco/negro/acento, líneas finas, footer oscuro de gran formato, iconografía lineal | Franja de confianza, ATES Technologies, footer |
| 03 · Maquinaria | Hero panorámico con la máquina a la derecha y texto a la izquierda, capa de contraste, franja inferior de experiencia, tarjetas beige, bloques de servicio fotográficos | Hero, franja, secciones de servicios y maquinaria |

### Color
El logotipo oficial es rojo (`#D7282F`, extraído del CSS de ates.es). Las referencias usan naranja, pero
introducir un naranja junto al rojo de marca diluiría la identidad: **el papel del "naranja de acción"
de las referencias lo asume el rojo ATES**. El resto de la paleta es neutra y cálida.

| Token | Valor | Uso |
| --- | --- | --- |
| `--c-bg` | `#ECE8E2` | Fondo general (gris cálido) |
| `--c-surface` | `#FAF8F5` | Paneles blanco roto |
| `--c-sand` | `#F1EBE2` | Tarjetas beige suaves |
| `--c-ink` | `#141518` | Texto principal |
| `--c-ink-soft` | `#55575E` | Texto secundario |
| `--c-anthracite` | `#18191C` | Bloques de contraste y footer |
| `--c-red` | `#D7282F` | Acción, detalles, marca |

### Tipografía
Poppins exclusivamente (Google Fonts, 400–800). Hero en 800 mayúsculas con interlineado 0.95 y
tracking negativo; H2 en 700; etiquetas en 500 con tracking amplio.

### Fotografía
Solo imágenes publicadas en ates.es, enlazadas desde su URL oficial (con copia local de respaldo
para presentar sin conexión). Tratamiento cinematográfico ligero: saturación −10 %, contraste +5 %,
degradados oscuros únicamente donde hay texto. Muchas fotos oficiales son dípticos o llevan una
pestaña blanca decorativa en un lateral: se recortan con `object-fit: cover` + `object-position`, sin
deformarlas.

### Movimiento
Aparición progresiva al hacer scroll (opacidad + 16 px, 700 ms, curva `cubic-bezier(.23,1,.32,1)`),
zoom fotográfico de 1.04 en hover (solo dispositivos con puntero fino), botones con `scale(.97)` al
pulsar, header que se compacta al hacer scroll. `prefers-reduced-motion` desactiva desplazamientos.

### Composición propia por página (versión multipágina)

Todas comparten header con mega menú, migas, CTA y footer, pero cada página tiene un bloque protagonista distinto:

| Página | Hero | Bloque protagonista |
| --- | --- | --- |
| Maquinaria | Foto a sangre (grúas frente al mar) | Mosaico de familias + franja del catálogo auxiliar |
| Grúas torre y automontantes | Foto a sangre (grúa ATES) | Díptico de tipologías + cifra "40 años de servicio técnico" |
| Montacargas | Partido texto/foto | Barra de capacidad 500 → 2.000 kg |
| Maquinaria auxiliar | Partido texto/foto | Catálogo filtrable de 13 familias con datos técnicos |
| Construcción | Foto a sangre (plataformas) | Índice editorial de sistemas + obra nueva / rehabilitación |
| Andamios | Foto a sangre (Castillo de los Funes, 2560 px) | Sellos de normas UNE-EN + proyectos publicados |
| Encofrados | Foto a sangre (puntales) | Comparativa de presión 40/60 kN/m² + fichas técnicas |
| Cimbras y apeos | Partido texto/foto | Secuencia de montaje en 4 pasos |
| Plataformas motorizadas | Foto a sangre | Anatomía del sistema + panel de seguridad CE |
| Estabilizadores / Escaleras | Partido texto/foto | Página compacta (el contenido oficial es breve) |
| Tecnologías (4 páginas) | Hero oscuro | Paneles oscuros con retícula, caso Moncabril, cadena Big Data → ML |
