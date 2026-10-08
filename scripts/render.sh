#!/usr/bin/env bash
# render.sh — render reproducible de un sitio de la familia (hub o pub); tema compartido por hardlink (ola 6, 6d)
# Fija SOURCE_DATE_EPOCH (y FORCE_SOURCE_DATE) a la fecha del último commit de fuentes del sitio, que LuaTeX y Pandoc usan como
# fecha interna de los PDF y DOCX; el pre-render (fechas-desde-git.py) fija la de cada página. Así dos renders del
# mismo commit dan el mismo _site/, byte a byte (comprobado en pub_res-publica: tres renders, 0 diferencias).
# Uso: scripts/render.sh [argumentos de quarto render]      (desde la raíz del sitio)
# Salida: la de quarto render; 2 si la carpeta no es un repo git.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
# la fecha del último commit que toca fuentes: no la mueven _site/ ni los intermedios del render que se versionan
# (index.tex de keep-tex, index.html.md de keep-md), ni los punteros de _pubs/ en el hub.
# Límite: Quarto da a cada celda de código un id aleatorio (`<div id="…" class="cell">`): las páginas con celdas
# cambian ese atributo en cada render; el texto visible y los PDF sin celdas, no.
SOURCE_DATE_EPOCH="$(git log -1 --format=%ct -- . ':(exclude)_site' ':(exclude)_freeze' ':(exclude)_pubs' ':(exclude,glob)**/index.tex' ':(exclude,glob)**/index.html.md' 2>/dev/null)" || { echo "render.sh: $(pwd) no es un repo git" >&2; exit 2; }
export SOURCE_DATE_EPOCH FORCE_SOURCE_DATE=1
exec nice -n 10 quarto render "$@"
