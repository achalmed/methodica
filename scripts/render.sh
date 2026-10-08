#!/usr/bin/env bash
# render.sh — render reproducible de un sitio de la familia (hub o pub); tema compartido por hardlink (ola 6, 6d)
# Fija SOURCE_DATE_EPOCH (y FORCE_SOURCE_DATE) a la fecha del último commit del sitio, que LuaTeX y Pandoc usan como
# fecha interna de los PDF y DOCX; el pre-render (fechas-desde-git.py) fija la de cada página. Así dos renders del
# mismo commit dan el mismo _site/, byte a byte (comprobado en pub_res-publica: tres renders, 0 diferencias).
# Uso: scripts/render.sh [argumentos de quarto render]      (desde la raíz del sitio)
# Salida: la de quarto render; 2 si la carpeta no es un repo git.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
SOURCE_DATE_EPOCH="$(git log -1 --format=%ct 2>/dev/null)" || { echo "render.sh: $(pwd) no es un repo git" >&2; exit 2; }
export SOURCE_DATE_EPOCH FORCE_SOURCE_DATE=1
exec nice -n 10 quarto render "$@"
