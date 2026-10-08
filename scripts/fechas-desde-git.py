#!/usr/bin/env python3
"""fechas-desde-git.py — fija la fecha de modificación de cada página fuente a la de su último commit (ola 6, 6d).

Quarto ordena los listados por la fecha de modificación del archivo (`data-listing-file-modified-sort`) y la escribe
en el `<lastmod>` del `sitemap.xml`. Esa fecha cambia con cada `git checkout` o clon, así que dos renders del mismo
commit daban `_site/` distintos. Con este paso, previo al render (`pre-render` de `_quarto.yml`), la fecha sale de
git y el render es reproducible.

Toca solo páginas fuente (`.qmd`, `.md`, `.ipynb`, `.Rmd`) rastreadas, sin cambios sin confirmar y **sin hardlinks**:
un hardlink del tema es un solo inodo con una sola fecha, y cada sitio le pondría la suya. `_site/` y `_freeze/`
nunca. Simula por defecto; `--aplicar` escribe. Sale 0 bien, 2 si la carpeta no es un repo git.

Uso:  python3 scripts/fechas-desde-git.py [carpeta] [--aplicar]
      (en el pre-render, Quarto pasa la carpeta del proyecto en QUARTO_PROJECT_DIR)
"""
import os
import subprocess
import sys

EXTENSIONES = (".qmd", ".md", ".ipynb", ".rmd")
FUERA = ("_site/", "_freeze/", ".quarto/", "_pubs/")


def git(raiz, *args):
    return subprocess.run(["git", "-C", raiz, *args], capture_output=True, text=True, check=True).stdout


def main(argv):
    aplicar = "--aplicar" in argv
    resto = [a for a in argv if not a.startswith("--")]
    raiz = os.path.abspath(resto[0] if resto else os.environ.get("QUARTO_PROJECT_DIR", "."))
    try:
        rastreados = set(git(raiz, "ls-files", "-z").split("\0"))
        sucios = {l[3:] for l in git(raiz, "status", "--porcelain").splitlines()}
        historia = git(raiz, "log", "--format=@%ct", "--name-only", "--no-renames", "HEAD")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"fechas-desde-git: {raiz} no es un repo git", file=sys.stderr)
        return 2
    fecha = {}
    actual = None
    for linea in historia.splitlines():          # del más nuevo al más viejo: la primera aparición manda
        if linea.startswith("@"):
            actual = int(linea[1:])
        elif linea and linea not in fecha:
            fecha[linea] = actual
    cambiadas = saltadas = 0
    for rel in sorted(rastreados):
        if not rel.lower().endswith(EXTENSIONES) or rel.startswith(FUERA) or rel in sucios or rel not in fecha:
            continue
        ruta = os.path.join(raiz, rel)
        try:
            st = os.stat(ruta)
        except OSError:
            continue
        if st.st_nlink > 1:
            saltadas += 1
            continue
        if int(st.st_mtime) != fecha[rel]:
            cambiadas += 1
            if aplicar:
                os.utime(ruta, (st.st_atime, fecha[rel]))
    modo = "fijadas" if aplicar else "se fijarían (simulación; --aplicar escribe)"
    print(f"fechas-desde-git: {cambiadas} páginas {modo}; {saltadas} con hardlinks, sin tocar")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
