#!/usr/bin/env bash
# render.sh — render reproducible de un sitio de la familia (hub o pub); tema compartido por hardlink (ola 6, 6d; fase 2, 2026-10-20)
# Fija SOURCE_DATE_EPOCH (y FORCE_SOURCE_DATE) a la fecha del último commit de fuentes del sitio, que LuaTeX y Pandoc usan como
# fecha interna de los PDF y DOCX; el pre-render (fechas-desde-git.py) fija la de cada página. Así dos renders del
# mismo commit dan el mismo _site/, byte a byte (comprobado en res-publica: tres renders, 0 diferencias).
# Solo HTML por defecto (fase 2): `--to html` tarda segundos donde el render con apaquarto tardaba minutos. Un render
# completo de Quarto vacía `_site/`, así que antes se apartan los PDF y DOCX ya compilados (cada `_site/<r>/<x>.pdf|docx`
# con fuente `<r>/<x>.qmd|md|ipynb|Rmd`) y después vuelven los de las páginas que siguen publicadas (las que tienen su
# `<x>.html`); los de un borrador o una página retirada no vuelven, como no habrían sobrevivido al render. Los enlaces
# «Otros formatos» de cada página no dependen de esto: Quarto los escribe con los formatos declarados.
# Uso: scripts/render.sh [argumentos de quarto render]   solo HTML y conserva los PDF y DOCX de _site/  (desde la raíz del sitio)
#      scripts/render.sh --documentos [--aplicar] [--forzar] [--solo RUTA] [--registrar] [--verificar]
#                        PDF y DOCX solo de las páginas cuya fuente cambió (scripts/documentos.py; simula sin --aplicar)
#      scripts/render.sh --completo [argumentos]           todos los formatos de cada página (el render de antes de la fase 2)
#      (con --to o -t explícito se respeta lo pedido y no se aparta nada)
# Salida: la de quarto render o documentos.py; 2 si la carpeta no es un repo git.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
# la fecha del último commit que toca fuentes: no la mueven _site/ ni los intermedios del render que se versionan
# (index.tex de keep-tex, index.html.md de keep-md), ni los punteros de _pubs/ en el hub, ni la caché de documentos.
# Límite: Quarto da a cada celda de código un id aleatorio (`<div id="…" class="cell">`): las páginas con celdas
# cambian ese atributo en cada render; el texto visible y los PDF sin celdas, no.
SOURCE_DATE_EPOCH="$(git log -1 --format=%ct -- . ':(exclude)_site' ':(exclude)_freeze' ':(exclude)_pubs' ':(exclude,glob)**/index.tex' ':(exclude,glob)**/index.html.md' ':(exclude)scripts' ':(exclude)netlify.toml' ':(exclude).gitignore' ':(exclude,glob)**/README.md' ':(exclude)CITATION.cff' ':(exclude)CLAUDE.md' ':(exclude)AGENTS.md' ':(exclude)LICENSE' ':(exclude)estado.md' ':(exclude)THEME_VERSION' ':(exclude)_documentos.tsv' 2>/dev/null)" || { echo "render.sh: $(pwd) no es un repo git" >&2; exit 2; }
export SOURCE_DATE_EPOCH FORCE_SOURCE_DATE=1
case "${1:-}" in
    --documentos) shift; exec nice -n 10 python3 scripts/documentos.py . "$@" ;;
    --completo)   shift; exec nice -n 10 quarto render "$@" ;;
esac
for a in "$@"; do
    case "$a" in --to|-t|--to=*|-t=*) exec nice -n 10 quarto render "$@" ;; esac
done

APARTADOS="$(mktemp -d .render-documentos.XXXXXX)"   # en el mismo disco: mover no copia y conserva el inodo
apartar() {
    local f rel ext
    while IFS= read -r -d '' f; do
        rel="${f#_site/}"
        for ext in qmd md ipynb Rmd rmd; do
            if [[ -f "${rel%.*}.$ext" ]]; then
                mkdir -p "$APARTADOS/$(dirname "$rel")"; mv "$f" "$APARTADOS/$rel"; break
            fi
        done
    done < <(find _site -type f \( -name '*.pdf' -o -name '*.docx' \) -print0 2>/dev/null)
}
devolver() {        # $1 = publicadas (solo las páginas con su .html) o todo (el render falló o se interrumpió)
    local g rel n=0 fuera=0
    [[ -d "$APARTADOS" ]] || return 0
    while IFS= read -r -d '' g; do
        rel="${g#"$APARTADOS"/}"
        if [[ "$1" == todo || -f "_site/${rel%.*}.html" ]] && [[ ! -e "_site/$rel" ]]; then
            mkdir -p "_site/$(dirname "$rel")"; mv "$g" "_site/$rel"; n=$((n + 1))
        else
            fuera=$((fuera + 1))
        fi
    done < <(find "$APARTADOS" -type f -print0)
    rm -rf "$APARTADOS"
    echo "render.sh: $n PDF/DOCX conservados en _site/$( ((fuera)) && echo "; $fuera de páginas no publicadas o ya rehechos, fuera")"
}
trap 'devolver todo; exit 130' INT TERM
apartar
estado=0
nice -n 10 quarto render --to html "$@" || estado=$?
if (( estado == 0 )); then devolver publicadas; else devolver todo; fi
exit "$estado"
