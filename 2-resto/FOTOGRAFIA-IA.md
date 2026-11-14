# Dirección fotográfica y prompts de mejora con IA

## Estado

- **No se han generado ni editado imágenes con IA.** Este entorno no dispone de un modelo de
  generación/edición de imágenes, y las dos fotografías "adjuntas por el usuario" que cita el brief
  (obra en fase estructural y grúa torre ATES amarilla) no están en la carpeta del proyecto.
- Todas las fotos del prototipo son originales de ates.es (46 URL verificadas con respuesta 200),
  con copia local en `web/assets/img/ates/` como respaldo.
- La homogeneidad se resuelve con un **etalonaje CSS común**: `saturate(.85–.9) contrast(1.04–1.06)`,
  degradados oscuros solo donde hay texto, y `object-fit: cover` con un punto de corte definido por foto
  (`--pos`). Muchas imágenes oficiales son dípticos o trípticos (926 × 400 / 926 × 322): se recorta una
  sola fotografía de cada composición, sin deformarla.

## Estilo objetivo: Premium Industrial Corporate Photography

Luz natural equilibrada · alto rango dinámico · colores neutros y cálidos · cielos limpios sin saturar ·
negros profundos sin empastar · nitidez de detalle en estructuras metálicas · sin efectos ni filtros visibles.

## Reglas de fidelidad para cualquier edición

1. Mantener la geometría exacta de grúas, andamios, encofrados y plataformas.
2. No añadir, quitar ni mover piezas mecánicas, nudos, mástiles o puntales.
3. Conservar la marca ATES; si la IA la altera, restaurar el logotipo original en postproducción.
4. No cambiar el sistema constructivo representado ni añadir maquinaria.
5. Comparar siempre original y resultado a 100 % antes de publicar.

## Prompts por imagen (listos para un modelo de edición imagen-a-imagen)

| Imagen original | Uso en el prototipo | Formato | Prompt |
|---|---|---|---|
| `Construction-grua-ates.png` (900 × 400) | Hero Home, Grúas | 2,5:1 | Upscale ×3 and enhance this exact photograph of a yellow tower crane with the red "ATES" sign on the counter-jib. Keep every lattice member, cable, the ATES lettering and the crane geometry identical. Natural late-afternoon light, slightly warmer sky, high dynamic range, crisp metal detail, no added objects. |
| `Gruas-Torre-ATES-Construction.png` (926 × 400) | Hero Maquinaria, Grúas | 2,5:1 | Upscale ×3 this exact photo of two orange tower cranes over a coastal town. Remove the white decorative tab on the right edge by extending the sky and hillside naturally. Keep the cranes, the ATES plate and buildings unchanged. Balanced natural light, realistic sea colour. |
| `Encofrados-serie-pesada-ATES-Construction.png` (926 × 400) | Encofrados, CTA | 16:9 | Enhance this construction site in the structural phase: yellow and orange wall formwork, concrete columns with rebar. Keep all formwork panels and columns exactly in place. Reduce video compression artefacts, recover shadow detail, neutral daylight, editorial architectural photography. |
| `Encofrados-apuntalamientos-ATES-Construction.png` | Hero Encofrados | 16:9 | Upscale and sharpen this photo of yellow shoring props under a slab. Preserve the exact number and position of props. Remove the white tab on the left edge by extending the scene. Even daylight, true yellow tone. |
| `Plataformas-ATES-Construction-motorizadas-rehabilitacion-fachadas.png` | Hero Plataformas, Home | 4:3 | Upscale this photo of ATES mast-climbing work platforms on a residential façade. Keep the red ATES signs, masts and blue mesh exactly as they are. Correct converging verticals slightly, natural daylight, higher detail. |
| `Andamios-cara-sur-2-scaled.jpg` (2560 × 1920) | Hero Andamios, Construcción | 2,5:1 | Light grade only: recover sky highlights and shadow detail of this castle wrapped in scaffolding. Do not alter the scaffold, banners or buildings. |
| `Inspecciones-infraestructuras-hidraulicas-rover-proyectos-Ates.png` (diptych) | Hero Tecnologías | 2,5:1 | Take the right-hand photo only (rover inside a penstock). Upscale ×3, reduce noise, keep the rover's lights and frame exactly. Preserve the cool industrial tones; do not add sci-fi effects. |

## Paso a producción

Una vez aprobadas, exportar en WebP/AVIF (calidad 80) en dos tamaños (1600 px y 900 px), sustituir el
`src` por las versiones locales con `srcset`, y mantener la URL oficial original documentada en
`build/images.json`.
