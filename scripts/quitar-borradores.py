#!/usr/bin/env python3
"""quitar-borradores.py — los borradores no se publican: quita del `_site/` la salida de cada página con `draft: true`.

Quarto, con el modo de borradores por omisión, sigue escribiendo en `_site/` una página vacía de cada borrador y su
PDF y DOCX con la portada (título, autor, resumen). El autor decidió (2026-10-08) que un borrador no se publica: este
paso, en el `post-render` de `_quarto.yml`, borra esa salida. Para `<dir>/index.qmd` quita la carpeta `_site/<dir>/`
entera; para `<dir>/x.qmd`, `_site/<dir>/x.{html,pdf,docx}`. Ningún índice del sitio (sitemap, búsqueda, listados)
enlaza un borrador; si una página publicada lo enlaza, se avisa.

Simula por defecto; `--aplicar` borra. Sale 0 bien (los enlaces a borradores se avisan), 1 con `--estricto` si una
página publicada enlaza un borrador, 2 si no hay `_site/`.
Uso:  python3 scripts/quitar-borradores.py [carpeta del sitio] [--aplicar]   (en el post-render: QUARTO_PROJECT_DIR)
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

BORRADOR = re.compile(r"^draft:\s*true\s*(#.*)?$", re.M)


def frontmatter(texto):
    if not texto.startswith("---"):
        return ""
    fin = texto.find("\n---", 3)
    return texto[3:fin] if fin > 0 else ""


def main(argv):
    aplicar = "--aplicar" in argv
    resto = [a for a in argv if not a.startswith("--")]
    raiz = Path(resto[0] if resto else os.environ.get("QUARTO_PROJECT_DIR", ".")).resolve()
    site = raiz / "_site"
    if not site.is_dir():
        print(f"quitar-borradores: no hay {site}", file=sys.stderr)
        return 2
    fuentes = subprocess.run(["git", "-C", str(raiz), "ls-files", "-z", "*.qmd"], capture_output=True, text=True).stdout.split("\0")
    salidas = []
    for rel in filter(None, fuentes):
        if rel.startswith(("_site/", "_pubs/")) or Path(rel).name.startswith("_"):
            continue
        try:
            fm = frontmatter((raiz / rel).read_text(encoding="utf-8"))
        except OSError:
            continue
        if not BORRADOR.search(fm):
            continue
        p = Path(rel)
        if p.name == "index.qmd" and p.parent != Path("."):
            salidas.append(site / p.parent)
        else:
            salidas += [site / p.with_suffix(s) for s in (".html", ".pdf", ".docx")]
    existentes = [s for s in salidas if s.exists()]
    rutas = {"/" + s.relative_to(site).as_posix() for s in existentes}
    enlazan = []
    if rutas:
        patron = re.compile("|".join(re.escape(r.lstrip("/")) for r in sorted(rutas)))
        for html in site.rglob("*.html"):
            if any(html == s or s in html.parents for s in existentes):
                continue
            if patron.search(html.read_text(encoding="utf-8", errors="ignore")):
                enlazan.append(html.relative_to(site).as_posix())
    for s in existentes:
        if aplicar:
            shutil.rmtree(s) if s.is_dir() else s.unlink()
    modo = "quitadas" if aplicar else "se quitarían (simulación; --aplicar borra)"
    print(f"quitar-borradores: {len(existentes)} salidas de borradores {modo}")
    for h in enlazan[:10]:
        print(f"  aviso: {h} enlaza un borrador", file=sys.stderr)
    return 1 if enlazan and "--estricto" in argv else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
