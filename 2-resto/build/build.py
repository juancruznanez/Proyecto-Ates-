"""Genera el sitio estático en /web. Uso: python3 build/build.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from components import WEB, PAGES, document  # noqa: E402
import pages as _pages  # noqa: E402,F401  (registra páginas y navegación)
from pages import RENDER, DARK  # noqa: E402


def main():
    import crops
    print(f"{crops.generate()} recortes nuevos")
    written = []
    for slug, render in RENDER.items():
        page = PAGES[slug]
        path = page["path"]
        depth = path.count("/")
        rel = "../" * depth
        html = document(rel, page, render(rel), area=page.get("area"),
                        body_class="theme-tech" if slug in DARK else "")
        out = os.path.join(WEB, path, "index.html") if not path.endswith(".html") else os.path.join(WEB, path)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf8") as f:
            f.write(html)
        written.append(os.path.relpath(out, WEB))
    print(f"{len(written)} páginas generadas:")
    for w in written:
        print("  web/" + w)


if __name__ == "__main__":
    main()
