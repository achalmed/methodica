---
tipo: readme
estado: activo
---
# methodica/ — Investigación y metodología: blog satélite del hub `04 index` (repo methodica, methodica.netlify.app)

<!-- GENERADO por `04 index/scripts/pubs.py readme --aplicar` desde `04 index/_pubs/pubs.yml` (2026-10-10); no editar aquí: se regenera desde el hub -->

## Qué es

Métodos cualitativos y cuantitativos, APA y redacción académica. Es uno de los 11 blogs satélite de la familia Quarto de Edison Achalma: un sitio Quarto
con repositorio y sitio Netlify propios, incluido como submódulo git en el hub `04 index` (repo
`website-achalma`) bajo `04 index/_pubs/methodica/`. El mismo blog tiene tres nombres: carpeta `methodica`, repo
GitHub `achalmed/methodica` y dominio `methodica.netlify.app`; el registro de los tres es `04 index/_pubs/pubs.yml`.

El tema visual (SCSS, JS, extensiones, filtros, `scripts/build-page-css.sh`) **no se edita aquí**: vive en el hub y
llega por `04 index/scripts/sync-theme-pubs.sh`. Lo propio de este blog es `_quarto.yml`, `index.qmd`, `_contenido-*.qmd`,
`assets/img/` y las entradas; los índices `_contenido_<sección>.qmd` los genera `scripts-quarto`
(`script_generador_publicacion_similar`) y no se editan a mano.

## Uso

```bash
quarto preview                              # vista previa local
quarto render                               # regenera _site/ (freeze: true: el código no se re-ejecuta)
git add -- <carpeta del post> _contenido_*.qmd _site && git commit -m "post: …"   # confirmar AQUÍ primero…
../../scripts/puerta-r6.sh .                # puerta R6: _site/index.html al día antes del push (también es el hook pre-push)
git push                                    # …al remoto propio (ssh git@github.com:achalmed/methodica.git)
cd ../.. && git add _pubs/methodica && git commit -m "pubs: methodica al último commit"   # y mover el puntero en el hub
```

## Estructura

| carpeta | qué es | entradas |
|---|---|--:|
| `posts/` | entradas sin sección temática | 7 |
| `_quarto.yml`, `index.qmd`, `404.qmd`, `_contenido-inicio.qmd`, `_contenido-final.qmd` | configuración y portada propias del blog | |
| `assets/scss/`, `assets/js/`, `assets/css/global.css`, `assets/css/components/`, `_extensions/`, `_filters/apa-floats-html.lua`, `scripts/build-page-css.sh` | tema propagado desde el hub por `sync-theme-pubs.sh`: no se edita aquí | |
| `assets/img/`, `assets/fonts/`, `assets/gtm-*.html`, `assets/interactions.html`, `assets/scss/05-pages/`, `assets/css/pages/`, `_filters/_metadata-pdf.lua`, `_partials/` | propios del blog (no los escribe la sincronización) | |
| `_site/` | sitio generado por `quarto render`; versionado a propósito: su push es el despliegue (`04 index/docs/decisiones.md` §4.1) | |
| `THEME_VERSION` | sello del tema: commit del hub y sha256 del conjunto; lo escribe `sync-theme-pubs.sh --aplicar` (GENERADO) | |
| `_freeze/` | caché de ejecución de Quarto (`freeze: true`); se versiona cuando existe (normativa 5.16 y 7.6) | |
| `netlify.toml` | configuración de Netlify: publica `_site/` sin comando de build | |

7 entradas. Cada entrada es `<sección>/AAAA-MM-DD-slug/index.qmd` con frontmatter apaquarto y fecha ISO;
sus metadatos se editan en masa desde `scripts-quarto` (`metadata_manager`).

## Documentación

Toda la familia se documenta una vez, en el hub: `04 index/README.md` (qué es la familia y cómo se opera),
`04 index/docs/pubs-submodulos.md` (submódulos y flujo de commit), `04 index/docs/publicar-un-post.md` (de
principio a fin), `04 index/docs/despliegue-netlify.md` (cómo publica cada sitio) y `assets/scss/README.md` (el tema).

## Límite honesto

- Este README es el único documento propio del blog y se regenera desde el hub: lo escrito aquí a mano se pierde.
- `_site/` sigue en git: Netlify publica el _site/ empujado, sin build (decisiones §4.1 del hub); `netlify.toml` lo declara (`publish = "_site"`, sin comando de build), y el hook pre-push de la puerta R6 no viaja con el repo: lo instala `04 index/scripts/puerta-r6.sh --instalar`.
- Licencia: código MPL-2.0 (`LICENSE`), contenido CC-BY-SA-4.0 según `license.qmd` del hub; unificarlas en los 12 sitios es la decisión D9.
