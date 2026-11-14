"""Recortes de las fotografías oficiales de ATES.

Muchas imágenes de ates.es son dípticos/trípticos (varias fotos con separador blanco) o llevan una
pestaña decorativa blanca de ~25 px en un lateral. Detectado por análisis de píxeles (columnas >90 %
blancas). Aquí se extrae cada fotografía individual, sin escalar ni alterar su contenido, con `sips`.

SPEC: original -> {clave: (x, y, ancho, alto)} en píxeles del original.
"""
import os
import subprocess

from components import IMG_DIR

CROP_DIR = os.path.join(IMG_DIR, "c")

H4, H3 = 400, 322
SPEC = {
    # --- fotografía única con pestaña blanca a la derecha (900-925)
    **{f: {"main": (0, 0, 900, H4)} for f in [
        "Gruas-Torre-ATES-Construction.png", "Gruas-Automontantes-ATES-Construction.png",
        "Montacargas-Ates-Construction.png", "Plataformas-ATES-motorizadas-obra-nueva.png",
        "Plataformas-ATES-Construction-motorizadas-rehabilitacion-fachadas.png",
        "Proyectos-Inteligencia-Artificial-Big-Data-ATES-Technologies.png",
        "Elevadores-electricos-maquinaria-auxiliar-Construction-ATES.png",
        "Escaleras-de-acceso-ATES-Andamios.png", "Cimbras-y-apeos-estructurales-ATES-Andamios.png",
        "tijeras-electricas-maquinaria-ATES.png", "Hormigoner-construction-maquinaria-auxiliar-ATES.png",
        "Vibradores-de-hormigon-maquinaria-auxiliar-Construction-ATES.png"]},
    # --- fotografía única con pestaña blanca a la izquierda (0-25)
    **{f: {"main": (26, 0, 900, H4)} for f in [
        "Andamios-marco-europero-ATES-Construction.png", "Andamios-multidireccional-europero-ATES-Construction.png",
        "Encofrados-apuntalamientos-ATES-Construction.png", "Encofrados-pilares-ATES-Construction.png",
        "Encofrados-serie-ligera-ATES-Construction.png", "Encofrados-serie-pesada-ATES-Construction.png",
        "Escaleras-de-acceso-ATES-Construction.png", "Estabilizadores-de-fachada-ATES-Construction.png",
        "Cimbras-y-apeos-estructurales-ATES-Construction.png",
        "Compactacion-ATES-Construction.png", "Cortadora-asfaltica-sima-maquinaria-auxiliar-construction-ATES.png",
        "Martillos-electricos-maquinaria-auxiliar-construction-ATES.png",
        "compresores-kaeser-maquinaria-auxiliar-construction-ATES.png",
        "grupo-electrogeno-100kvas-maquinaria-auxiliar-construction-ATES.png",
        "rodillos-dinapacc-maquinaria-auxiliar-ATES-construction.png"]},
    "Brazos-articulados-maquinaria-auxiliar-ATES-Construction.png": {"main": (24, 0, 897, H4)},
    # --- dípticos
    "Carretillas-maquinaria-auxiliar-ATES.png": {"L": (0, 0, 483, H4), "R": (508, 0, 394, H4)},
    "Dumpers-maquinaria-auxiliar-construction-ATES.png": {"L": (24, 0, 468, H4), "R": (517, 0, 409, H4)},
    "Inspeccionar-infraestructuras-con-rober-ATES-Technologies.png": {"L": (26, 0, 411, H4), "R": (464, 0, 462, H4)},
    "Infraestructuras-inspeccionadas-por-profesionales-ATES-Technologies.png": {"L": (26, 0, 411, H4), "R": (464, 0, 462, H4)},
    "Inspeccions-de-infraestructuras-civiles-ATES.png": {"L": (26, 0, 411, H4), "R": (464, 0, 462, H4)},
    "Inspecciones-infraestructuras-hidraulicas-rover-proyectos-Ates.png": {"L": (0, 0, 366, H3), "R": (377, 0, 549, H3)},
    "SHM-Ingenieria-artificial_Technologies_Ates_001.png": {"L": (30, 0, 374, H3), "R": (437, 0, 489, H3)},
    "Inspecciones-infraestructuras-complejidad-innovacion-ATES.png": {"L": (0, 0, 475, H3)},
    # --- trípticos y cuádruples
    "Salto_de_Moncabril_inspeccion_Zamora.png": {"q1": (14, 19, 230, 288), "q2": (248, 19, 196, 288),
                                                 "q3": (446, 19, 230, 288), "q4": (679, 19, 235, 288)},
    "Salto_de_Moncabril_zamora_inspeccion.png": {"p1": (11, 21, 284, 286), "p2": (305, 21, 270, 286),
                                                 "p3": (575, 0, 351, H3)},
}


def crop_name(src, key):
    return os.path.splitext(src)[0] + "--" + key + ".jpg"


def generate():
    os.makedirs(CROP_DIR, exist_ok=True)
    made = 0
    for src, crops in SPEC.items():
        path = os.path.join(IMG_DIR, src)
        for key, (x, y, w, h) in crops.items():
            out = os.path.join(CROP_DIR, crop_name(src, key))
            if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(path):
                continue
            subprocess.run(["sips", "-c", str(h), str(w), "--cropOffset", str(y), str(x),
                            "-s", "format", "jpeg", "-s", "formatOptions", "86", path, "--out", out],
                           check=True, stdout=subprocess.DEVNULL)
            made += 1
    return made


def _x(pos):
    try:
        return float(pos.split()[0].rstrip("%"))
    except (ValueError, IndexError):
        return 50.0


def resolve(src, pos):
    """Devuelve (archivo_recortado | None, posición). La parte de un díptico se elige por la x de `pos`."""
    crops = SPEC.get(src)
    if not crops:
        return None, pos
    if "main" in crops:
        return crop_name(src, "main"), pos
    x = _x(pos)
    keys = list(crops)
    if keys == ["L"]:
        key = "L"
    elif keys[0] == "L":
        key = "L" if x < 50 else "R"
    else:  # varias fotos en fila: elige por tramo
        key = keys[min(int(x / (100 / len(keys) + 0.001)), len(keys) - 1)]
    y = pos.split()[1] if len(pos.split()) > 1 else "50%"
    return crop_name(src, key), f"50% {y}"
