#!/usr/bin/env bash
# =============================================================================
# build-page-css.sh — compila assets/scss/05-pages/*.scss → assets/css/pages/
# =============================================================================
# Propósito : Los estilos por página se AUTORAN en SCSS (assets/scss/05-pages/)
#             y se sirven como CSS plano por página (assets/css/pages/). Este
#             script mantiene ambos sincronizados.
# Ejecución : Automática en cada render (hook project.pre-render en
#             _quarto.yml) o manual: ./scripts/build-page-css.sh
# Compilador: dart-sass embebido en Quarto (sin dependencias nuevas); si no
#             se encuentra, usa `sass` del PATH.
# Reglas    : Solo compila archivos SIN guion bajo inicial (los _stub.scss
#             quedan inactivos hasta renombrarlos).
# =============================================================================
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/assets/scss/05-pages"
OUT="$ROOT/assets/css/pages"

# ── Localizar dart-sass (el que trae Quarto) ────────────────────────────────
find_sass() {
  local qbin
  if command -v quarto >/dev/null 2>&1; then
    qbin="$(dirname "$(readlink -f "$(command -v quarto)")")"
    local candidate
    candidate="$(find "$qbin/tools" -type f -name sass 2>/dev/null | head -1 || true)"
    if [[ -n "${candidate:-}" && -x "$candidate" ]]; then
      echo "$candidate"; return 0
    fi
  fi
  if command -v sass >/dev/null 2>&1; then
    command -v sass; return 0
  fi
  return 1
}

SASS="$(find_sass)" || {
  echo "build-page-css: no se encontró dart-sass (ni en Quarto ni en PATH)" >&2
  exit 1
}

mkdir -p "$OUT"

for src in "$SRC"/[!_]*.scss; do
  [[ -e "$src" ]] || continue
  name="$(basename "$src" .scss)"
  tmp="$(mktemp)"
  "$SASS" --style=expanded --no-source-map --no-charset "$src" "$tmp"
  {
    printf '/* GENERADO desde assets/scss/05-pages/%s.scss — NO editar a mano.\n' "$name"
    printf '   Regenerar con: ./scripts/build-page-css.sh (corre solo en cada render) */\n'
    cat "$tmp"
  } > "$OUT/$name.css"
  rm -f "$tmp"
  echo "build-page-css: $name.scss → assets/css/pages/$name.css"
done
