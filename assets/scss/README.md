# Design System — "Quiet Laboratory"

Arquitectura SCSS del sitio, adaptación de ITCSS al sistema de temas de Quarto.
Dos entradas (`theme-light.scss`, `theme-dark.scss`) definen el **mismo
contrato de tokens semánticos `$lab-*`** con valores distintos e importan un
**único conjunto de módulos compartidos**. Así, cada regla se escribe una sola
vez y los temas solo declaran colores.

## Cómo compila Quarto estos archivos

- `_quarto.yml → format.html.theme` apunta a las dos entradas (tras `cosmo`).
- Quarto compila **dos bundles CSS independientes** (claro y oscuro) y los
  intercambia con el toggle. No hay cascada entre temas: cada bundle contiene
  Bootstrap + nuestras reglas ya coloreadas.
- Cada entrada tiene dos secciones obligatorias:
  - `/*-- scss:defaults --*/` — variables Sass (se inyectan ANTES de
    Bootstrap: aquí se configura cosmo).
  - `/*-- scss:rules --*/` — reglas CSS (se emiten DESPUÉS de Bootstrap:
    aquí se sobreescribe).
    Un partial solo puede importarse desde la sección que le corresponde.

## Capas

| Capa               | Contenido                                                                                                  | Emite CSS  |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | ---------- |
| `00-settings/`     | Paletas crudas (`$spc-*`), tokens semánticos (`$lab-*`), tipografía, layout y mapeo a Bootstrap            | No         |
| `01-tools/`        | Mixins y funciones Sass                                                                                    | No         |
| `02-base/`         | @font-face, custom properties `--lab-*`, documento, tipografía aplicada                                    | Sí         |
| `03-layout/`       | Navbar, footer, TOC, responsive transversal                                                                | Sí         |
| `04-components/`   | Title block, listados, código, tablas, matemáticas, citas, callouts, botones, paginación, social, búsqueda | Sí         |
| `05-interactions/` | Microinteracciones (.lab-reveal, glow) y reduced-motion                                                    | Sí         |
| `05-pages/`        | Estilos por página, compilados APARTE del tema (ver abajo)                                                 | CSS propio |
| `06-themes/`       | Reglas exclusivas de un tema (hoy: ajustes nocturnos)                                                      | Sí         |

## Flujo de tokens

```
_palette-{light,dark}.scss   $spc-*     colores crudos, sin significado
        │
_tokens-{light,dark}.scss    $lab-*     roles: fondo, tinta, acento, borde…
        │
        ├── _bootstrap.scss             $primary, $body-bg… (configura cosmo)
        ├── módulos 02–06               consumen SOLO $lab-*
        └── 02-base/_root.scss          publica --lab-* para assets/css/*.css
```

**Regla de oro:** los módulos compartidos nunca usan `$spc-*` ni hex directos;
solo tokens `$lab-*`. Un color nuevo entra por la paleta, recibe rol en los
dos archivos de tokens y recién entonces se usa.

## Asimetrías entre temas

Diferencias heredadas del diseño original, hechas explícitas (candidatas a
revisión en Fase 2):

- `$lab-quirk-mono-subtitle` — solo light pone `.subtitle` en monospace.
- `$lab-quirk-copy-chrome` — solo light define radio/transición del botón copiar.
- `$lab-dim-media` — solo dark atenúa imágenes hasta el hover.
- Tokens anulables (`null` = el tema no emite la regla): `$lab-callout-bg`,
  `$lab-cell-output-color`, `$lab-table-color`, `$lab-btn-primary-hover-color`,
  `$lab-pagination-active-color`.
- `06-themes/_dark-adjustments.scss` — scrollbar oscuro, dimming global de
  imágenes y paginación deshabilitada (solo lo importa `theme-dark.scss`).

## Estilos por página: `05-pages/` → `assets/css/pages/`

Los estilos de página NO forman parte del tema global (los selectores de
`listing` afectarían a todo el sitio si fueran globales). Se **autoran en
SCSS** en `05-pages/` y `scripts/build-page-css.sh` (hook `project.pre-render`
de `_quarto.yml`, usa el dart-sass embebido en Quarto) los compila a CSS plano
en `assets/css/pages/` en cada render. Consumen `var(--lab-*)`, por lo que se
adaptan a ambos temas sin duplicarse.

```
assets/scss/05-pages/            assets/css/  (GENERADO: no editar a mano)
├── home.scss          ──build──▶ pages/home.css      # portada (index.qmd)
├── about.scss         ──build──▶ pages/about.css     # about/index.qmd
├── contact.scss       ──build──▶ pages/contact.css   # contact.qmd
├── listing.scss       ──build──▶ pages/listing.css   # blog/, talk/, teching/
├── _blog.scss, _post.scss, _publications.scss,       # stubs inactivos:
│   _projects.scss, _courses.scss                     #   quitar "_" + enlazar
│
│  (escritos a mano, fuera del pipeline:)
├──                    assets/css/global.css           # todo el sitio (_quarto.yml)
└──                    assets/css/components/bibbase.css # BibBase (_quarto.yml)
```

Cada página carga su CSS vía `header-includes` + `resources` en su YAML.
Los archivos con guion bajo son stubs documentados: para activarlos, quitar
el guion bajo (entran al build) y enlazar el CSS resultante en la página.

## JavaScript (`assets/js/`)

Las microinteracciones viven en módulos independientes (`navbar.js`,
`cursor.js`, `hero.js`, `scroll-effects.js`) cargados globalmente por
`assets/interactions.html` (include-after-body). Ver `assets/js/README.md`.

## Checklist para cambios

1. ¿Es un color/medida nuevo? → paleta + ambos archivos de tokens.
2. ¿Es un componente global? → `04-components/` + `@import` en **ambas** entradas.
3. ¿Es de una sola página? → `05-pages/` (el build genera `assets/css/pages/`).
4. ¿Solo afecta a un tema? → flag/token anulable, o `06-themes/`.
5. Documenta el encabezado del archivo (propósito, responsabilidad,
   dependencias, cuándo modificarlo).
6. `quarto render index.qmd` para compilar rápido los temas y revisar.
