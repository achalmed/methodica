---
documentmode: doc
copyrightnotice: 2026
copyrightext: All rights reserved
title: Configuración de `_metadata.yml` para documentos académicos
abstract: El archivo _metadata.yml constituye una herramienta fundamental en Quarto para establecer configuraciones compartidas y consistentes en documentos y sitios académicos. Esta guía exhaustiva explica su funcionamiento, jerarquía de precedencia, estructura recomendada y las principales opciones de configuración (autoría con taxonomía CRediT, formatos de salida HTML/PDF/DOCX con apaquarto, ejecución de código, referencias cruzadas, citas académicas y gestión de borradores). Se presentan casos de uso reales, comparación entre configuraciones antiguas y optimizadas, mejores prácticas, proceso de migración y resolución de problemas frecuentes. El objetivo es facilitar la creación de blogs académicos reproducibles, mantenibles y profesionalmente presentados, minimizando la repetición de código (principio DRY) y maximizando la consistencia en proyectos de mediana y gran escala.
keywords:
- Quarto
- _metadata.yml
- Metadatos compartidos
categories:
- Metodología de Investigación
tags:
- metodologia_investigacion
- quarto
- _metadata.yml
author-note:
  status-changes:
    affiliation-change: null
    deceased: null
  disclosures:
    study-registration: null
    data-sharing: null
    related-report: null
    conflict-of-interest: El autor no tiene conflictos de interés que revelar.
    financial-support: null
    gratitude: null
    authorship-agreements: null
description: _metadata.yml es un archivo especial de Quarto que establece opciones por defecto para todos los documentos dentro de un directorio (y sus subdirectorios).
eval: false
citation:
  type: article-journal
  author:
  - Edison Achalma
  pdf-url: https://methodica.netlify.app/posts/2025-04-23-tipos-de-elementos-en-zotero/index.pdf
date: 01/02/2026
draft: false
image: ../featured.jpg
---


# ¿Qué es `_metadata.yml`?

## Concepto

`_metadata.yml` es un archivo especial de Quarto que establece **opciones por defecto para todos los documentos** dentro de un directorio (y sus subdirectorios).

**Función principal:**

```
Define opciones compartidas → Aplica a todos los posts del blog
                            → Evita repetición en cada documento
                            → Hereda y combina con _quarto.yml
```

## ¿Por qué usarlo?

**CON `_metadata.yml`:**

```yaml
# En _metadata.yml (una sola vez)
author:
  - name: Edison Achalma
date-modified: "today"
draft: true
```

**SIN `_metadata.yml`:**

```yaml
# En CADA post individualmente (repetitivo)
---
title: "Post 1"
author:
  - name: Edison Achalma
date-modified: "today"
draft: true
---
```

## Ventajas

- **DRY (Don't Repeat Yourself):** Define una vez, aplica a todo
- **Consistencia:** Todos los posts tienen la misma configuración base
- **Mantenimiento:** Cambiar una opción actualiza todos los posts
- **Limpieza:** Los posts individuales solo tienen lo específico
- **Jerarquía:** Se combina inteligentemente con `_quarto.yml`

# Ubicación y Jerarquía

## Estructura Típica de un Blog

```bash
epsilon-y-beta/                      # Raíz del proyecto
├── _quarto.yml                      # Config global del sitio
├── index.qmd                        # Página principal
├── 01-fundamentos-econometria/      # Categoría de posts
│   ├── _metadata.yml                # ← Opciones para ESTA categoría
│   ├── 2021-03-01-post1/
│   │   └── index.qmd                # Post individual
│   ├── 2021-03-08-post2/
│   │   └── index.qmd
│   └── featured.jpg
├── 02-macroeconometria/             # Otra categoría
│   ├── _metadata.yml                # ← Opciones para ESTA categoría
│   ├── 2021-09-20-post1/
│   │   └── index.qmd
│   └── featured.jpg
└── estadistica/
    ├── _metadata.yml
    └── ...
```

## Jerarquía de Configuración (Orden de Prioridad)

```
1. index.qmd (front-matter)         ← Mayor prioridad (sobrescribe todo)
   ↓
2. _metadata.yml (directorio post)  ← Opciones del post
   ↓
3. _metadata.yml (categoría)        ← Opciones de la categoría
   ↓
4. _quarto.yml (proyecto)           ← Opciones globales
   ↓
5. Valores por defecto de Quarto    ← Menor prioridad
```

**Ejemplo práctico:**

```yaml
# _quarto.yml (global)
format:
  html:
    toc: true
    toc-depth: 2

# 01-fundamentos-econometria/_metadata.yml
format:
  html:
    toc-depth: 3        # ← Sobrescribe toc-depth para esta categoría
    
# 01-fundamentos-econometria/2021-03-01-post1/index.qmd
---
format:
  html:
    toc: false          # ← Sobrescribe toc solo para ESTE post
---
```

**Resultado final para `index.qmd`:**

- `toc: false` (del post)
- `toc-depth: 3` (de la categoría, no se usa porque toc está desactivado)

# Estructura Básica

## Template Mínimo

```yaml
# ========================================================================
# METADATA COMPARTIDO PARA TODOS LOS POSTS DE ESTA CATEGORÍA
# ========================================================================
# Archivo: _metadata.yml
# Ubicación: [Nombre de la categoría]/_metadata.yml
# Ejemplo: 01-fundamentos-econometria/_metadata.yml

# ------------------------------------------------------------------------
# INFORMACIÓN DEL AUTOR (común a todos los posts)
# ------------------------------------------------------------------------
author:
  - name: Edison Achalma
    orcid: 0000-0001-6996-3364
    email: elmer.achalma.09@unsch.edu.pe

# ------------------------------------------------------------------------
# METADATOS GENERALES
# ------------------------------------------------------------------------
date-modified: "today"
lang: es
license: "CC BY-SA"

# ------------------------------------------------------------------------
# VISIBILIDAD
# ------------------------------------------------------------------------
draft: true          # Todos los posts inician como borradores

# ------------------------------------------------------------------------
# EJECUCIÓN DE CÓDIGO
# ------------------------------------------------------------------------
execute:
  freeze: true       # No re-ejecutar código en cada render
```

## Template Completo (Con Todas las Opciones)

```yaml
# ========================================================================
# CONFIGURACIÓN COMPLETA DE _metadata.yml
# ========================================================================
# Este archivo define opciones compartidas para todos los documentos
# en este directorio y subdirectorios

# ========================================================================
# SECCIÓN 1: INFORMACIÓN DEL AUTOR
# ========================================================================
author:
  - name: Edison Achalma
    url: https://achalmaedison.netlify.app
    affiliation:
      - id: unsch
        name: Universidad Nacional de San Cristóbal de Huamanga
        department: Escuela Profesional de Economía
        city: Ayacucho
        region: AYA
        country: Perú
    affiliation-url: https://www.gob.pe/unsch
    orcid: 0000-0001-6996-3364
    email: elmer.achalma.09@unsch.edu.pe
    attributes:
      corresponding: true
      equal-contributor: true
      deceased: false
    roles:
      - conceptualización
      - redacción

# Nota del Autor (si aplica)
author-note:
  disclosures:
    conflict-of-interest: Los autores no tienen conflictos de intereses \ 
    que revelar.

# ========================================================================
# SECCIÓN 2: METADATOS GENERALES DEL DOCUMENTO
# ========================================================================
date-modified: "today"
license: "CC BY-SA"
lang: es
search: true
lightbox: true

# Bloque de Título
title-block-banner: true
is-particlejs-enabled: false

# ========================================================================
# SECCIÓN 3: CONFIGURACIÓN DE TABLA DE CONTENIDOS
# ========================================================================
toc: true
toc-title: " "
toc-location: left

# ========================================================================
# SECCIÓN 4: REFERENCIAS Y CITAS
# ========================================================================
floatsintext: true
citation: true
google-scholar: true
link-citations: true
appendix-cite-as: display
citation-last-author-separator: "y"
citation-masked-author: "Cita Enmascarada"
citation-masked-title: "Título Enmascarado"
citation-masked-date: "n.f."

# Títulos de Bloques
title-block-author-note: "Nota de Autores"
title-block-correspondence-note: "La correspondencia relativa a este  \ 
artículo debe dirigirse a"
title-block-role-introduction: "Los roles de autor se clasificaron    \ 
utilizando la taxonomía de roles de colaborador (CRediT;              \ 
https://credit.niso.org/) de la siguiente manera:"
references-meta-analysis: "Las referencias marcadas con un asterisco  \ 
indican estudios incluidos en el metanálisis."

# ========================================================================
# SECCIÓN 5: REFERENCIAS CRUZADAS
# ========================================================================
language:
  crossref-fig-title: Figura
  crossref-tbl-title: Tabla
  crossref-lst-title: "Listing"
  crossref-thm-title: "Teorema"
  crossref-lem-title: "Lema"
  crossref-cor-title: "Corolario"
  crossref-prp-title: "Proposición"
  crossref-cnj-title: "Conjetura"
  crossref-def-title: "Definición"
  crossref-exm-title: "Ejemplo"
  crossref-exr-title: "Ejercicio"
  crossref-ch-prefix: "Capítulo"
  crossref-apx-prefix: Anexo
  crossref-sec-prefix: "Sección"
  crossref-eq-prefix: Ecuación
  crossref-lof-title: "Lista de Figuras"
  crossref-lot-title: "Lista de Tablas"
  crossref-lol-title: "Lista de Listings"

# ========================================================================
# SECCIÓN 6: VISIBILIDAD Y BORRADOR
# ========================================================================
mask: false
draft: true
draftfirst: false
draftall: false

# ========================================================================
# SECCIÓN 7: FORMATOS DE SALIDA
# ========================================================================
format:
  # ----------------------------------------------------------------------
  # Formato HTML
  # ----------------------------------------------------------------------
  html:
    toc-depth: 1
    toc-expand: 3
    smooth-scroll: true
    link-external-newwindow: true
    citations-hover: true
    footnotes-hover: true
    highlight-style: github
    code-copy: true
    code-fold: true
    code-summary: "Mostrar el código"
    code-overflow: scroll
    code-line-numbers: true
    code-tools:
      source: repo
      toggle: false
      caption: none
    mermaid:
      theme: neutral
    citation-location: document
    self-contained: false
    template-partials:
      - ../_partials/title-block-link-buttons/title-block.html
    theme: litera
    format-links: true
    
  # ----------------------------------------------------------------------
  # Formato PDF (APA Quarto)
  # ----------------------------------------------------------------------
  apaquarto-pdf:
    documentmode: jou
    copyrightnotice: 2026
    copyrightext: Todos los derechos reservados
    toc: true
    list-of-figures: true
    list-of-tables: true
    keep-tex: true
    fontsize: 12pt
    a4paper: true
    numbered-lines: false
    number-sections: true
    colorlinks: true
    pdf-engine: xelatex
    keep-md: false
    
  # ----------------------------------------------------------------------
  # Formato DOCX (APA Quarto)
  # ----------------------------------------------------------------------
  apaquarto-docx:
    toc: true
    fontsize: 12pt
    a4paper: true
    numbered-lines: false
    number-sections: true
    keep-md: false

# ========================================================================
# SECCIÓN 8: CONFIGURACIÓN DEL ENTORNO DE EJECUCIÓN
# ========================================================================
jupyter: python3

# Editor
editor:
  mode: source
  markdown:
    canonical: true
    wrap: 72
    references:
      location: section
    auto-wrapping: true
    sentence-spacing: true

# ========================================================================
# SECCIÓN 9: CONFIGURACIÓN DE COMENTARIOS
# ========================================================================
comments:
  utterances:
    repo: achalmed/website-achalma
    issue-term: title
    theme: boxy-light
    label: "comments :crystal_ball:"

# ========================================================================
# SECCIÓN 10: CONFIGURACIÓN DE EJECUCIÓN DE CÓDIGO
# ========================================================================
execute:
  freeze: true
  keep-md: true
  keep-ipynb: true
  echo: true
  output: true
  warning: false
  error: false
  enabled: false
  cache: true
```

# Configuración Completa Sección por Sección

## Sección 1: Información del Autor

Esta sección define la información del autor que se mostrará en todos los posts de la categoría.

### Opciones Básicas

```yaml
author:
  - name: Edison Achalma                     # Nombre completo del autor
    orcid: 0000-0001-6996-3364               # ID ORCID
    email: elmer.achalma.09@unsch.edu.pe     # Email de contacto
```

### Opciones Completas

```yaml
author:
  - name: Edison Achalma
    url: https://achalmaedison.netlify.app   # Sitio web personal
    
    # Afiliación institucional
    affiliation:
      - id: unsch                             # ID único para referenciar
        name: Universidad Nacional de San Cristóbal de Huamanga
        department: Escuela Profesional de Economía
        address: Portal Independencia N° 57
        city: Ayacucho
        region: AYA
        postal-code: 05001
        country: Perú
    
    affiliation-url: https://www.gob.pe/unsch
    orcid: 0000-0001-6996-3364
    email: elmer.achalma.09@unsch.edu.pe
    
    # Atributos del autor
    attributes:
      corresponding: true      # Es el autor de correspondencia
      equal-contributor: false # Contribuyó equitativamente con otros autores
      deceased: false          # Está fallecido 
    # Roles del autor (taxonomía CRediT)
    roles:
      - conceptualización
      - metodología
      - análisis formal
      - investigación
      - recursos
      - curación de datos
      - redacción
      - visualización
      - supervisión
      - administración del proyecto
```

### Múltiples Autores

```yaml
author:
  - name: Edison Achalma
    corresponding: true
    orcid: 0000-0001-6996-3364
    email: elmer.achalma.09@unsch.edu.pe
    affiliation:
      - ref: unsch
    roles:
      - conceptualización
      - redacción
      
  - name: Colaborador Dos
    orcid: 0000-0000-0000-0002
    affiliation:
      - ref: unsch
    roles:
      - análisis formal
      - visualización
      
  - name: Colaborador Tres
    affiliation:
      - name: Universidad Nacional Mayor de San Marcos
        department: Facultad de Ciencias Económicas
        city: Lima
        country: Perú
    roles:
      - revisión

# Definir afiliaciones compartidas
affiliations:
  - id: unsch
    name: Universidad Nacional de San Cristóbal de Huamanga
    department: Escuela Profesional de Economía
    city: Ayacucho
    region: AYA
    country: Perú
```

### Nota del Autor

```yaml
author-note:
  disclosures:
    conflict-of-interest: Los autores no tienen conflictos de intereses  \
    que revelar.
    study-registration: Este estudio fue registrado en el Registro       \ 
    Nacional de Investigaciones (código XYZ123).
    data-sharing: Los datos están disponibles en                         \ 
    https://github.com/achalmed/data
    financial-support: Esta investigación fue financiada por CONCYTEC    \ 
    mediante el proyecto N° 2024-01.
    gratitude: Los autores agradecen a los revisores anónimos por sus    \ 
    valiosos comentarios.
```


## Sección 2: Metadatos Generales

### Fechas

```yaml
date-modified: "today"                    # Se actualiza cada render
# O fecha específica:
# date-modified: "2025-01-02"
```

**Opciones de fecha:**

- `"today"`: Fecha actual al renderizar
- `"last-modified"`: Fecha de última modificación del archivo
- `"2025-01-02"`: Fecha específica en formato YYYY-MM-DD

### Idioma y Licencia

```yaml
lang: es                     # Idioma del contenido (es, en, fr, de, etc.)
license: "CC BY-SA"          # Licencia Creative Commons

# Otras licencias comunes:
# license: "CC BY"           # Atribución
# license: "CC BY-NC"        # Atribución-No Comercial
# license: "CC BY-NC-SA"     # Atribución-No Comercial-Compartir Igual
# license: "CC0"             # Dominio Público
```

### Búsqueda y Características

```yaml
search: true                 # Habilitar búsqueda en el documento
lightbox: true               # Habilitar lightbox para zoom de imágenes
```

### Bloque de Título

```yaml
title-block-banner: true     # Banner colorido en el título
# O imagen personalizada:
# title-block-banner: images/banner.jpg

is-particlejs-enabled: false #Efecto de partículas en el fondo
```


## Sección 3: Tabla de Contenidos

```yaml
toc: true                    # Mostrar tabla de contenidos
toc-title: " "               # Título (vacío para solo mostrar el ícono)
# toc-title: "Contenidos"    # O con título explícito

toc-location: left           # Ubicación: left, right, body
toc-depth: 3                 # Profundidad de niveles (1-6)
toc-expand: 2                # Nivel inicial expandido

# Solo HTML:
toc-float: true              # TOC flotante, visible al hacer scroll
```

**Ejemplos según tipo de post:**

```yaml
# Blog post corto
toc: false

# Artículo técnico medio
toc: true
toc-depth: 2
toc-expand: 2

# Tutorial largo y detallado
toc: true
toc-depth: 4
toc-expand: 1
toc-location: left
```


## Sección 4: Referencias y Citas

### Configuración de Citas

```yaml
citation: true          # Habilitar generación de citas
google-scholar: true    # Habilitar metadatos para Google Scholar
link-citations: true    # Enlaces clicables en citas
floatsintext: true      # Figuras y tablas en el texto (no al final)

# Personalización de citas
citation-last-author-separator: "y"      # "y" español, "and" inglés)
citation-masked-author: "Cita Enmascarada"
citation-masked-title: "Título Enmascarado"
citation-masked-date: "n.f."              # "n.f." = no fecha

# Ubicación de citas (solo HTML)
citation-location: document               # Opciones: document, margin
# footnote-location: margin               # Ubicación de notas al pie
```

### Estilo de Citas

```yaml
# Estilo CSL (Citation Style Language)
csl: apa-6th-edition.csl                 # Archivo .csl en el proyecto
# O URL:
# csl: https://www.zotero.org/styles/apa-6th-edition

# Método de citación
cite-method: citeproc                     # citeproc, biblatex, natbib
```

### Archivo de Bibliografía

```yaml
# Una sola bibliografía
bibliography: references.bib

# Múltiples archivos
bibliography:
  - references.bib
  - additional-refs.bib
  - papers.bib
```

### Textos Personalizados

```yaml
title-block-author-note: "Nota de Autores"
title-block-correspondence-note: "La correspondencia relativa a este \ 
artículo debe dirigirse a"
title-block-role-introduction: "Los roles de autor se clasificaron   \ 
utilizando la taxonomía de roles de colaborador (CRediT;             \ 
https://credit.niso.org/) de la siguiente manera:"
references-meta-analysis: "Las referencias marcadas con un asterisco \ 
indican estudios incluidos en el metanálisis."
```


## Sección 5: Referencias Cruzadas

Las referencias cruzadas permiten referenciar figuras, tablas, ecuaciones, etc. de forma automática.

```yaml
language:
  # Figuras
  crossref-fig-title: Figura
  crossref-fig-prefix: Figura
  
  # Tablas
  crossref-tbl-title: Tabla
  crossref-tbl-prefix: Tabla
  
  # Ecuaciones
  crossref-eq-prefix: Ecuación
  
  # Secciones
  crossref-sec-prefix: "Sección"
  crossref-ch-prefix: "Capítulo"
  crossref-apx-prefix: Anexo
  
  # Otros elementos
  crossref-lst-title: "Listado"         # Code listings
  crossref-thm-title: "Teorema"
  crossref-lem-title: "Lema"
  crossref-cor-title: "Corolario"
  crossref-prp-title: "Proposición"
  crossref-cnj-title: "Conjetura"
  crossref-def-title: "Definición"
  crossref-exm-title: "Ejemplo"
  crossref-exr-title: "Ejercicio"
  
  # Listas
  crossref-lof-title: "Lista de Figuras"
  crossref-lot-title: "Lista de Tablas"
  crossref-lol-title: "Lista de Listados"
```

**Uso en el documento:**

```markdown
Ver @fig-grafico para más detalles.

![Gráfico importante](grafico.png){#fig-grafico}

Como se muestra en @tbl-resultados...

| A | B |
|---|---|
| 1 | 2 |

: Resultados principales {#tbl-resultados}
```


## Sección 6: Visibilidad y Borrador

```yaml
# Modo borrador (no se publica)
draft: true                  # true = borrador, false = publicado

# Enmascarar información (para peer review)
mask: false                  # Oculta nombres de autores y afiliaciones

# Opciones avanzadas de borrador
draftfirst: false            # Solo primera página como borrador (PDF)
draftall: false              # Todas las páginas como borrador (PDF)
```

**Workflow típico:**

```yaml
# Durante escritura
draft: true

# Cuando está listo para revisar
draft: false
mask: true                   # Para peer review anónimo

# Después de aceptación
draft: false
mask: false
```


## Sección 7: Formatos de Salida

Esta es la sección más extensa y permite configurar cómo se genera cada formato de salida.

### Formato HTML

```yaml
format:
  html:
    # --- TABLA DE CONTENIDOS ---
    toc: true
    toc-depth: 3
    toc-expand: 2
    toc-title: "Contenidos"
    toc-location: left            # left, right, body
    
    # --- NAVEGACIÓN ---
    smooth-scroll: true           # Scroll suave al navegar
    link-external-newwindow: true # Enlaces externos en nueva pestaña
    
    # --- CITAS Y NOTAS ---
    citations-hover: true         # Popup con cita al pasar el mouse
    footnotes-hover: true         # Popup con nota al pie al pasar el mouse
    citation-location: document   # document, margin
    
    # --- CÓDIGO ---
    highlight-style: github       # Estilo: github, monokai, etc.
    code-copy: true               # Botón para copiar código
    code-fold: true               # Código plegable
    code-summary: "Mostrar el código"     # Texto del botón
    code-overflow: scroll         # scroll, wrap
    code-line-numbers: true       # Números de línea
    code-tools:
      source: repo                # Mostrar enlace al código fuente
      toggle: false               # Botón para mostrar/ocultar código
      caption: none
    
    # --- DIAGRAMAS ---
    mermaid:
      theme: neutral              # Tema para diagramas mermaid
    
    # --- TEMA ---
    theme: litera                 # Tema Bootstrap
    # Temas disponibles: default, cerulean, cosmo, cyborg, darkly, flatly,
    # journal, litera, lumen, lux, materia, minty, morph, pulse, quartz,
    # sandstone, simplex, sketchy, slate, solar, spacelab, superhero,
    # united, vapor, yeti, zephyr
    
    # O tema personalizado:
    # theme: 
    #   - litera
    #   - custom.scss
    
    # --- OTRAS OPCIONES ---
    self-contained: false         # HTML independiente (incluye CSS/JS)
    page-layout: article          # article, full, custom
    format-links: true            # Enlaces a otros formatos
    
    # Plantillas personalizadas
    template-partials:
      - ../_partials/title-block-link-buttons/title-block.html
    
    # Configuración de grid (ancho de columnas)
    grid:
      sidebar-width: 400px
      body-width: 1000px
      margin-width: 200px
      gutter-width: 1.5rem
```

### Formato PDF (con apaquarto)

```yaml
format:
  apaquarto-pdf:
    # --- MODO DE DOCUMENTO ---
    documentmode: jou  # jou (journal), man (manuscript), stu (student), doc (document)
    
    # --- METADATOS ---
    copyrightnotice: 2025
    copyrightext: Todos los derechos reservados
    
    # Solo para modo journal:
    journal: "Revista de Economía"
    volume: "2025, Vol. 1, No. 1, 1--30"
    
    # Solo para modo estudiante:
    # course: "Econometría Avanzada"
    # professor: "Dr. Edison Achalma"
    # duedate: "2025-12-31"
    
    # --- ESTRUCTURA ---
    toc: true
    list-of-figures: true
    list-of-tables: true
    number-sections: true
    
    # --- FORMATO ---
    fontsize: 12pt                        # 10pt, 11pt, 12pt
    a4paper: true                         # true para A4, false para Letter
    numbered-lines: false                 # Numerar líneas
    colorlinks: true                      # Enlaces con color
    
    # --- OPCIONES DE COMPILACIÓN ---
    pdf-engine: xelatex                   # xelatex, pdflatex, lualatex
    keep-tex: true                        # Mantener archivos .tex
    keep-md: false                        # Mantener archivos .md
    
    # --- SUPRESIÓN SELECTIVA ---
    # suppress-title-page: false
    # donotrepeattitle: false
    # draftfirst: false
    # draftall: false
```

### Formato DOCX (con apaquarto)

```yaml
format:
  apaquarto-docx:
    toc: true
    fontsize: 12pt
    a4paper: true
    numbered-lines: false
    number-sections: true
    keep-md: false
    
    # Opciones adicionales
    # blank-lines-above-title: 2
    # blank-lines-above-author-note: 2
```

### Formato Typst (con apaquarto)

```yaml
format:
  apaquarto-typst:
    toc: true
    keep-typ: true                # Mantener archivo .typ
```


## Sección 8: Entorno de Ejecución

```yaml
# Kernel de Jupyter
jupyter: python3                  # python3, ir (R), julia

# Configuración del editor
editor:
  mode: source                    # source (código) o visual (WYSIWYG)
  
  markdown:
    canonical: true               # Formato Markdown consistente
    wrap: 72                      # Ancho de línea (caracteres)
    references:
      location: section           # Ubicación de referencias: document, section, block
    auto-wrapping: true           # Ajuste automático de línea
    sentence-spacing: true        # Doble espacio después de punto
```


## Sección 9: Comentarios

Integración con sistemas de comentarios.

```yaml
comments:
  utterances:                         # GitHub Utterances
    repo: achalmed/website-achalma    # Repositorio de GitHub
    issue-term: title                 # Cómo asociar comentarios: title, pathname, url, og:title
    theme: boxy-light                 # Tema: github-light, github-dark, boxy-light, etc.
    label: "comments :crystal_ball:"  # Etiqueta en los issues
```

**Otras opciones de comentarios:**

```yaml
# Hypothes.is
comments:
  hypothesis: true

# Giscus (alternativa a Utterances)
comments:
  giscus:
    repo: achalmed/website-achalma
    repo-id: "R_xxxx"
    category: "Announcements"
    category-id: "DIC_xxxx"
    mapping: pathname
    reactions-enabled: true
    theme: light
```


## Sección 10: Ejecución de Código

Esta sección controla cómo se ejecuta el código en los documentos.

```yaml
execute:
  # --- CONTROL DE EJECUCIÓN ---
  freeze: true                    # No re-ejecutar código al renderizar
  # Opciones de freeze:
  # - true: Nunca re-ejecutar (usa resultados guardados)
  # - false: Siempre re-ejecutar
  # - auto: Re-ejecutar solo si el código cambió
  
  enabled: false                  # Deshabilitar ejecución por defecto
  # Para ejecutar: quarto render --execute
  
  # --- SALIDA ---
  echo: true                      # Mostrar código fuente
  output: true                    # Mostrar resultados
  warning: false                  # Ocultar advertencias
  error: false                    # Ocultar errores
  message: false                  # Ocultar mensajes
  
  # --- ARCHIVOS GENERADOS ---
  keep-md: true                   # Mantener archivo .md intermedio
  keep-ipynb: true                # Mantener notebook .ipynb
  
  # --- CACHÉ ---
  cache: true                     # Usar caché para resultados
  # Para limpiar caché: quarto render --cache-refresh
```

**Estrategias de `freeze` según tipo de blog:**

```yaml
# Blog académico con análisis largos
execute:
  freeze: true          # Ejecutar una vez, guardar resultados
  cache: true

# Blog de tutoriales (código siempre debe funcionar)
execute:
  freeze: auto          # Re-ejecutar si cambia el código
  cache: false

# Blog personal sin código
execute:
  enabled: false        # No ejecutar nada
```


# Casos de Uso Prácticos

Aquí cubrimos **10 escenarios reales** con configuraciones completas para cada uno.


## Caso 1: Blog Académico de Econometría

**Escenario:** Blog con múltiples categorías de posts académicos sobre econometría, con código R/Python, figuras, tablas, y citas bibliográficas.

**Estructura:**

```bash
epsilon-y-beta/
├── _quarto.yml
├── 01-fundamentos-econometria/
│   ├── _metadata.yml          # ← Este archivo
│   ├── 2021-03-01-post1/
│   └── 2021-03-08-post2/
├── 02-macroeconometria/
│   ├── _metadata.yml
│   └── ...
└── estadistica/
    ├── _metadata.yml
    └── ...
```

**`01-fundamentos-econometria/_metadata.yml` (Completo):**

```yaml
# ========================================================================
# METADATA PARA CATEGORÍA: FUNDAMENTOS DE ECONOMETRÍA
# ========================================================================

# ------------------------------------------------------------------------
# AUTOR
# ------------------------------------------------------------------------
author:
  - name: Edison Achalma
    url: https://achalmaedison.netlify.app
    affiliation:
      - id: unsch
        name: Universidad Nacional de San Cristóbal de Huamanga
        department: Escuela Profesional de Economía
        city: Ayacucho
        region: AYA
        country: Perú
    affiliation-url: https://www.gob.pe/unsch
    orcid: 0000-0001-6996-3364
    email: elmer.achalma.09@unsch.edu.pe
    attributes:
      corresponding: true
    roles:
      - conceptualización
      - análisis formal
      - redacción
      - visualización

author-note:
  disclosures:
    conflict-of-interest: El autor no tiene conflictos de intereses que \
    revelar.
    data-sharing: El código y los datos están disponibles en \
    https://github.com/achalmed

# ------------------------------------------------------------------------
# METADATOS GENERALES
# ------------------------------------------------------------------------
date-modified: "today"
license: "CC BY-SA"
lang: es
search: true
lightbox: true
title-block-banner: true

# ------------------------------------------------------------------------
# TABLA DE CONTENIDOS
# ------------------------------------------------------------------------
toc: true
toc-title: " "
toc-location: left
toc-depth: 3
toc-expand: 2

# ------------------------------------------------------------------------
# REFERENCIAS Y CITAS
# ------------------------------------------------------------------------
floatsintext: true
citation: true
google-scholar: true
link-citations: true
citation-last-author-separator: "y"
bibliography: references.bib
csl: apa-6th-edition.csl

# ------------------------------------------------------------------------
# REFERENCIAS CRUZADAS
# ------------------------------------------------------------------------
language:
  crossref-fig-title: Figura
  crossref-tbl-title: Tabla
  crossref-eq-prefix: Ecuación
  crossref-sec-prefix: "Sección"

# ------------------------------------------------------------------------
# VISIBILIDAD
# ------------------------------------------------------------------------
draft: true            # Cambiar a false cuando esté listo

# ------------------------------------------------------------------------
# FORMATOS DE SALIDA
# ------------------------------------------------------------------------
format:
  html:
    toc-depth: 3
    toc-expand: 2
    smooth-scroll: true
    link-external-newwindow: true
    citations-hover: true
    footnotes-hover: true
    highlight-style: github
    code-copy: true
    code-fold: true
    code-summary: "Mostrar el código"
    code-overflow: scroll
    code-line-numbers: true
    mermaid:
      theme: neutral
    theme: litera
    template-partials:
      - ../_partials/title-block-link-buttons/title-block.html
    
  apaquarto-pdf:
    documentmode: jou
    copyrightnotice: 2025
    copyrightext: Todos los derechos reservados
    toc: true
    list-of-figures: true
    list-of-tables: true
    keep-tex: true
    fontsize: 12pt
    a4paper: true
    number-sections: true
    colorlinks: true
    pdf-engine: xelatex
    
  apaquarto-docx:
    toc: true
    fontsize: 12pt
    number-sections: true

# ------------------------------------------------------------------------
# EJECUCIÓN DE CÓDIGO
# ------------------------------------------------------------------------
jupyter: python3

execute:
  freeze: true # No re-ejecutar en cada render (para análisis largos)
  keep-md: true
  keep-ipynb: true
  echo: true
  output: true
  warning: false
  error: false
  cache: true

# ------------------------------------------------------------------------
# EDITOR
# ------------------------------------------------------------------------
editor:
  mode: source
  markdown:
    canonical: true
    wrap: 72
    references:
      location: section

# ------------------------------------------------------------------------
# COMENTARIOS
# ------------------------------------------------------------------------
comments:
  utterances:
    repo: achalmed/website-achalma
    issue-term: title
    theme: boxy-light
    label: "comments :crystal_ball:"
```

**Uso en un post individual (`2021-03-01-post1/index.qmd`):**

```yaml
---
title: "Modelo Clásico de Regresión Lineal"
subtitle: "Fundamentos teóricos y aplicaciones"
description: "Introducción al modelo de regresión lineal clásico"
date: "2021-03-01"
categories:
  - regresión lineal
  - teoría econométrica
  - R
image: featured.jpg

# Solo necesitas especificar lo que difiere de _metadata.yml
# Por ejemplo, si este post en particular NO debe ser borrador:
draft: false

# O si quieres un formato diferente solo para este post:
# format:
#   html:
#     code-fold: false    # Mostrar código por defecto en este post
---

# Introducción

Este post introduce el modelo clásico de regresión lineal...

[El resto del contenido]
```

**Ventajas de esta configuración:**

- Consistencia: Todos los posts tienen el mismo formato
- Eficiencia: No repites autor, afiliación, etc. en cada post
- Mantenimiento: Cambiar email solo requiere editar `_metadata.yml`
- Flexibilidad: Cada post puede sobrescribir opciones si es necesario


## Caso 2: Blog Personal de Tutoriales (Sin Afiliación)

**Escenario:** Blog de tutoriales de programación, sin afiliación académica, código que debe ejecutarse siempre para verificar que funciona.

**`tutoriales/_metadata.yml`:**

```yaml
# ========================================================================
# METADATA PARA TUTORIALES
# ========================================================================

# ------------------------------------------------------------------------
# AUTOR (Sin afiliación académica)
# ------------------------------------------------------------------------
author:
  - name: Edison Achalma
    url: https://achalmaedison.netlify.app
    email: achalmaedison@gmail.com
    orcid: 0000-0001-6996-3364

# ------------------------------------------------------------------------
# METADATOS
# ------------------------------------------------------------------------
date-modified: "today"
license: "CC BY"            # Licencia permisiva para tutoriales
lang: es
search: true
lightbox: true

# ------------------------------------------------------------------------
# TABLA DE CONTENIDOS
# ------------------------------------------------------------------------
toc: true
toc-location: left
toc-depth: 2                # Menos profundidad para tutoriales

# ------------------------------------------------------------------------
# VISIBILIDAD
# ------------------------------------------------------------------------
draft: false                # Tutoriales se publican inmediatamente

# ------------------------------------------------------------------------
# FORMATO HTML (solo)
# ------------------------------------------------------------------------
format:
  html:
    theme: flatly           # Tema limpio y moderno
    code-fold: false        # Código siempre visible en tutoriales
    code-copy: true
    code-line-numbers: true
    highlight-style: monokai
    smooth-scroll: true

# ------------------------------------------------------------------------
# EJECUCIÓN (Código DEBE funcionar)
# ------------------------------------------------------------------------
execute:
  freeze: auto              # Re-ejecutar si el código cambió
  cache: false              # No usar caché (verificar que funciona)
  echo: true
  warning: true             # Mostrar warnings (importantes en tutoriales)
  error: true               # Mostrar errores (para debugging)
```


## Caso 3: Posts de Investigación con Peer Review

**Escenario:** Papers académicos que pasan por peer review anónimo.

**`papers/_metadata.yml`:**

```yaml
# ========================================================================
# METADATA PARA PAPERS DE INVESTIGACIÓN
# ========================================================================

# ------------------------------------------------------------------------
# AUTOR (completo)
# ------------------------------------------------------------------------
author:
  - name: Edison Achalma
    url: https://achalmaedison.netlify.app
    affiliation:
      - id: unsch
        name: Universidad Nacional de San Cristóbal de Huamanga
        department: Escuela Profesional de Economía
        city: Ayacucho
        country: Perú
    affiliation-url: https://www.gob.pe/unsch
    orcid: 0000-0001-6996-3364
    email: elmer.achalma.09@unsch.edu.pe
    corresponding: true
    roles:
      - conceptualización
      - análisis formal
      - redacción

author-note:
  disclosures:
    conflict-of-interest: Los autores no tienen conflictos de intereses \ 
    que revelar.
    financial-support: Esta investigación fue financiada por [Fuente].
    data-sharing: Los datos y materiales están disponibles bajo petición.

# ------------------------------------------------------------------------
# METADATOS
# ------------------------------------------------------------------------
date-modified: "today"
license: "CC BY-NC-SA"      # No comercial para papers
lang: es

# ------------------------------------------------------------------------
# ENMASCARAMIENTO (para peer review)
# ------------------------------------------------------------------------
mask: false                 # Cambiar a true para envío anónimo

# Si mask: true, también necesitas:
# masked-citations:
#   - achalma2023
#   - achalma2024

# ------------------------------------------------------------------------
# CITAS Y REFERENCIAS
# ------------------------------------------------------------------------
citation: true
google-scholar: true
link-citations: true
bibliography: paper-refs.bib
csl: apa-7th-edition.csl    # APA 7 para papers formales

# ------------------------------------------------------------------------
# FORMATO PDF (prioritario para papers)
# ------------------------------------------------------------------------
format:
  apaquarto-pdf:
    documentmode: man       # Manuscript (doble espacio)
    toc: false              # Sin TOC en papers formales
    number-sections: true
    numbered-lines: true    # Líneas numeradas para revisión
    fontsize: 12pt
    a4paper: true
    keep-tex: true
    
  apaquarto-docx:
    toc: false
    fontsize: 12pt
    numbered-lines: true

# ------------------------------------------------------------------------
# EJECUCIÓN
# ------------------------------------------------------------------------
execute:
  freeze: true              # Congelar resultados (importante)
  echo: false               # No mostrar código en paper final
  warning: false
  error: false
  cache: true
```

**Workflow de peer review:**

```yaml
# 1. Borrador inicial
draft: true
mask: false

# 2. Envío para peer review
draft: false
mask: true                  # Oculta info de autores

# 3. Después de aceptación
draft: false
mask: false
```


## Caso 4: Blog Multilingüe (Español/Inglés)

**Escenario:** Posts que se publican en español e inglés.

**Estructura:**

```bash
blog/
├── es/                     # Posts en español
│   ├── _metadata.yml
│   └── posts/
└── en/                     # Posts en inglés
    ├── _metadata.yml
    └── posts/
```

**`es/_metadata.yml`:**

```yaml
# ========================================================================
# METADATA PARA POSTS EN ESPAÑOL
# ========================================================================

# ------------------------------------------------------------------------
# AUTOR
# ------------------------------------------------------------------------
author:
  - name: Edison Achalma
    orcid: 0000-0001-6996-3364
    email: elmer.achalma.09@unsch.edu.pe

# ------------------------------------------------------------------------
# IDIOMA Y LOCALIZACIÓN
# ------------------------------------------------------------------------
lang: es

# Textos en español
language:
  crossref-fig-title: Figura
  crossref-tbl-title: Tabla
  crossref-eq-prefix: Ecuación

citation-last-author-separator: "y"
title-block-author-note: "Nota de Autores"

# ------------------------------------------------------------------------
# FORMATO
# ------------------------------------------------------------------------
format:
  html:
    theme: cosmo
    
execute:
  freeze: true
```

**`en/_metadata.yml`:**

```yaml
# ========================================================================
# METADATA FOR ENGLISH POSTS
# ========================================================================

# ------------------------------------------------------------------------
# AUTHOR
# ------------------------------------------------------------------------
author:
  - name: Edison Achalma
    orcid: 0000-0001-6996-3364
    email: elmer.achalma.09@unsch.edu.pe

# ------------------------------------------------------------------------
# LANGUAGE AND LOCALIZATION
# ------------------------------------------------------------------------
lang: en

# English texts
language:
  crossref-fig-title: Figure
  crossref-tbl-title: Table
  crossref-eq-prefix: Equation

citation-last-author-separator: "and"
title-block-author-note: "Author Note"

# ------------------------------------------------------------------------
# FORMAT
# ------------------------------------------------------------------------
format:
  html:
    theme: cosmo
    
execute:
  freeze: true
```


## Caso 5: Blog de Análisis de Datos con Python/R

**Escenario:** Análisis reproducibles con datos, código visible, y notebooks interactivos.

**`analisis/_metadata.yml`:**

```yaml
# ========================================================================
# METADATA PARA ANÁLISIS DE DATOS
# ========================================================================

# ------------------------------------------------------------------------
# AUTOR
# ------------------------------------------------------------------------
author:
  - name: Edison Achalma
    url: https://achalmaedison.netlify.app
    orcid: 0000-0001-6996-3364

# ------------------------------------------------------------------------
# METADATOS
# ------------------------------------------------------------------------
date-modified: "today"
license: "CC BY"
lang: es

# ------------------------------------------------------------------------
# FORMATO HTML (solo)
# ------------------------------------------------------------------------
format:
  html:
    theme: darkly           # Tema oscuro (popular en data science)
    code-fold: show         # Código visible pero plegable
    code-copy: true
    code-line-numbers: true
    code-tools:
      source: repo          # Link al repo de GitHub
    highlight-style: monokai
    
    # Grid para notebooks anchos
    grid:
      body-width: 1200px
      margin-width: 300px

# ------------------------------------------------------------------------
# EJECUCIÓN (IMPORTANTE para reproducibilidad)
# ------------------------------------------------------------------------
jupyter: python3            # O 'ir' para R

execute:
  freeze: auto              # Re-ejecutar si el código cambió
  keep-ipynb: true          # ← IMPORTANTE: Mantener notebook
  echo: true                # Mostrar código
  warning: true             # Mostrar warnings
  error: false              # No mostrar errores (para mantener limpio)
  cache: true               # Usar caché para análisis largos

# ------------------------------------------------------------------------
# HERRAMIENTAS DE DATOS
# ------------------------------------------------------------------------
# Metadatos para datasets
# data-files:
#   - data/raw/
#   - data/processed/
```

**Generar notebook descargable:**

Quarto automáticamente generará un archivo `.ipynb` descargable si `keep-ipynb: true`.


## Caso 6: Blog de Estudiante (Trabajos de Clase)

**Escenario:** Tareas y proyectos de un estudiante.

**`tareas/_metadata.yml`:**

```yaml
# ========================================================================
# METADATA PARA TAREAS DE CLASE
# ========================================================================

# ------------------------------------------------------------------------
# ESTUDIANTE
# ------------------------------------------------------------------------
author:
  - name: Edison Achalma
    affiliation:
      - name: Universidad Nacional de San Cristóbal de Huamanga
        department: Escuela Profesional de Economía
        city: Ayacucho
        country: Perú
    email: elmer.achalma.09@unsch.edu.pe

# ------------------------------------------------------------------------
# METADATOS
# ------------------------------------------------------------------------
lang: es
date-modified: "today"

# ------------------------------------------------------------------------
# FORMATO PDF (modo estudiante)
# ------------------------------------------------------------------------
format:
  apaquarto-pdf:
    documentmode: stu       # ← Modo estudiante
    course: "Econometría Avanzada (ECON 401)"
    professor: "Dr. Juan Pérez"
    duedate: "2025-12-31"
    toc: true
    number-sections: true
    fontsize: 12pt
    
  html:
    theme: united
    toc: true

# ------------------------------------------------------------------------
# EJECUCIÓN
# ------------------------------------------------------------------------
execute:
  freeze: false             # Siempre re-ejecutar (para verificar)
  echo: true
  warning: true
```


## Caso 7: Blog de Empresa/Organización

**Escenario:** Blog corporativo con múltiples autores.

**`blog-empresa/_metadata.yml`:**

```yaml
# ========================================================================
# METADATA PARA BLOG CORPORATIVO
# ========================================================================

# ------------------------------------------------------------------------
# AUTORES (plantilla, se sobrescribe en cada post)
# ------------------------------------------------------------------------
# Los autores se especifican por post individual

# ------------------------------------------------------------------------
# ORGANIZACIÓN
# ------------------------------------------------------------------------
affiliations:
  - id: empresa
    name: Consultora Económica S.A.
    city: Lima
    country: Perú

# ------------------------------------------------------------------------
# METADATOS
# ------------------------------------------------------------------------
date-modified: "today"
license: "Todos los derechos reservados"  # Copyright corporativo
lang: es

# ------------------------------------------------------------------------
# BRANDING
# ------------------------------------------------------------------------
title-block-banner: images/banner-empresa.jpg

# ------------------------------------------------------------------------
# FORMATO
# ------------------------------------------------------------------------
format:
  html:
    theme:
      - flatly
      - custom-empresa.scss  # Colores corporativos
    logo: images/logo.png
    
execute:
  freeze: true
  echo: false               # No mostrar código en blog público
```


## Caso 8: Documentación Técnica

**Escenario:** Documentación de software/paquete.

**`docs/_metadata.yml`:**

```yaml
# ========================================================================
# METADATA PARA DOCUMENTACIÓN TÉCNICA
# ========================================================================

# ------------------------------------------------------------------------
# AUTOR
# ------------------------------------------------------------------------
author:
  - name: Edison Achalma
    url: https://achalmaedison.netlify.app
    email: dev@example.com

# ------------------------------------------------------------------------
# METADATOS
# ------------------------------------------------------------------------
lang: es
license: "MIT"              # Licencia de software

# ------------------------------------------------------------------------
# TABLA DE CONTENIDOS (detallada)
# ------------------------------------------------------------------------
toc: true
toc-depth: 4                # Mucha profundidad para docs técnicas
toc-expand: true

# ------------------------------------------------------------------------
# FORMATO HTML
# ------------------------------------------------------------------------
format:
  html:
    theme: cosmo
    code-fold: false        # Código siempre visible
    code-copy: true
    code-line-numbers: true
    highlight-style: github
    
    # Navegación
    page-navigation: true   # Siguiente/Anterior
    
execute:
  freeze: auto
  echo: true
  warning: true
  error: true               # Mostrar errores (importante en docs)
```


## Caso 9: Blog de Noticias/Actualidad

**Escenario:** Posts cortos, sin código, publicación rápida.

**`noticias/_metadata.yml`:**

```yaml
# ========================================================================
# METADATA PARA NOTICIAS
# ========================================================================

# ------------------------------------------------------------------------
# AUTOR
# ------------------------------------------------------------------------
author:
  - name: Edison Achalma
    url: https://achalmaedison.netlify.app

# ------------------------------------------------------------------------
# METADATOS
# ------------------------------------------------------------------------
date-modified: "today"
lang: es

# ------------------------------------------------------------------------
# SIN TABLA DE CONTENIDOS (posts cortos)
# ------------------------------------------------------------------------
toc: false

# ------------------------------------------------------------------------
# FORMATO SIMPLE
# ------------------------------------------------------------------------
format:
  html:
    theme: journal          # Tema periodístico
    page-layout: article
    
# ------------------------------------------------------------------------
# SIN CÓDIGO
# ------------------------------------------------------------------------
execute:
  enabled: false            # No ejecutar nada
```


## Caso 10: Blog Mínimo (Lo Esencial)

**Escenario:** Configuración más simple posible.

**`blog-minimo/_metadata.yml`:**

```yaml
# ========================================================================
# CONFIGURACIÓN MÍNIMA
# ========================================================================

author:
  - name: Edison Achalma
    email: elmer.achalma.09@unsch.edu.pe

lang: es
draft: true

execute:
  freeze: true
```

**Eso es todo.** Quarto usará valores por defecto para el resto.


# Mi Configuración Actual vs Optimizada

## Mi Configuración Antigua (Comentada)

```yaml
#  PROBLEMAS:
#title-block-banner: "#EDF3F9"  
# - Comentado, no hace nada

#title-block-banner: images/philosophy2.jpg 
# - Comentado, no hace nada

#title-block-banner-color: body  
# - Comentado, no hace nada

# OK: Layout de figuras y tablas
fig-cap-location: top  
tbl-cap-location: top  

# OK: Información del autor
author:
  - name: Edison Achalma
    url: https://achalmaedison.netlify.app  
    affiliation: 
        - name: Universidad Nacional de San Cristóbal de Huamanga
          departament: Economía          #  Typo: "department"
          address: Portla Independencia N 57  #  Typo: "Portal"
          city: Huamanga
          region: Ayacucho
    affiliation-url: https://www.gob.pe/unsch
    orcid: 0000-0001-6996-3364  
    email: achalmed.18@gmail.com         #  Email antiguo
    attributes:
      corresponding: true
      equal-contributor: true
      deceased: false

# OK pero podría simplificarse
date-modified: "today"  
search: true  

#  PROBLEMA: Referencias no configuradas correctamente
citation: true  
google-scholar: true  
csl: apa-6th-edition.csl  #  Archivo no existe en proyecto
cite-method: biblatex     #  Método incompatible con HTML

# OK: Referencias cruzadas
crossref:
  fig-title: Figura  
  fig-prefix: Figura  
  tbl-title: Tabla  
  tbl-prefix: Tabla  
  ref-hyperlink: true  

# OK
draft: true  
image-path: "index_files/figure-html/"  #  Innecesario

#  PROBLEMA: Highlight debe estar bajo format:html
highlight-style: github   #  Ubicación incorrecta

# OK: Formato HTML (bien configurado)
format:
  html:
    page-layout: article  
    toc: true  
    toc-depth: 3  
    toc-expand: 2  
    toc-title: Contenidos  
    toc-location: left  
    # css: index.css       #  Comentado
    # number-sections: true #  Comentado
    # number-depth: 3      #  Comentado
    smooth-scroll: true  
    # link-external-icon: true  #  Comentado
    link-external-newwindow: true  
    citations-hover: true  
    footnotes-hover: true  
    code-copy: true  
    code-fold: true  
    code-summary: "Mostrar el código"  
    code-overflow: scroll  
    code-tools:
      source: repo  
      toggle: false  
      caption: none  
    mermaid: 
      theme: neutral
    grid: 
      sidebar-width: 400px 
      body-width: 1000px 
      margin-width: 200px 
      gutter-width: 1.5rem
      
  # OK: Formato PDF
  pdf:
    documentclass: article  
    papersize: a4  
    geometry: 
      - top=2.54cm  
      - right=2.54cm  
      - bottom=2.54cm  
      - left=2.54cm  
    language: es  
    pdf-engine: pdflatex    
    #  PROBLEMA: Fonts comentadas (no se usan)
    # fontfamily: anttor
    # sansfont: "Open Sans" 
    # mainfont: "Merriweather"
    # monofont: "Consolas"
    # mathfont: "TeX-Gyre-Termes-Math"
    # CJKmainfont: "Noto Sans CJK SC"
    fig-width: 7
    fig-height: 5
    # toc: true  #  Comentado
    # toc-depth: 3  #  Comentado
    # toc-title: Contenidos  #  Comentado
    # number-sections: true  #  Comentado
    # number-depth: 3  #  Comentado
    highlight-style: github  
    code-overflow: wrap  
    colorlinks: true  
    cite-method: biblatex  
    link-citation: true  
    link-bibliography: true  
    keep-tex: true  
    output-file: index.pdf
    #  PROBLEMA: Include no existe
    include-in-header: 
      - file: packages.tex  #  Archivo no existe

format-links:   #  Ubicación incorrecta, debe estar bajo format:html
  - pdf
  - ipynb
  
jupyter: python3
editor: visual    #  Modo visual, probablemente querías source
```

## Mi Configuración Actual (Con apaquarto)

```yaml
# MUY MEJORADA: Bien organizada y documentada

# ========================================================================
# CONFIGURACIÓN GENERAL DEL DOCUMENTO
# ========================================================================
date-modified: "today"
license: "CC BY-SA"
lang: es
search: true
lightbox: true

title-block-banner: true
is-particlejs-enabled: true  #  Requiere extensión instalada

# ========================================================================
# INFORMACIÓN DEL AUTOR
# ========================================================================
author:
  - name: Edison Achalma
    url: https://achalmaedison.netlify.app
    affiliation:
      - id: unsch
        name: Universidad Nacional de San Cristóbal de Huamanga
        department: Escuela Profesional de Economía  # Corregido
        city: Ayacucho
        region: AYA
        country: Perú
    affiliation-url: https://www.gob.pe/unsch
    orcid: 0000-0001-6996-3364
    email: elmer.achalma.09@unsch.edu.pe  # Email actualizado
    attributes:
      corresponding: true
      equal-contributor: true
      deceased: false
    roles:
      - conceptualización
      - redacción

author-note:
  disclosures:
    conflict-of-interest: Los autores no tienen conflictos de intereses \
    que revelar.

# ========================================================================
# CONFIGURACIÓN DE TABLA DE CONTENIDOS
# ========================================================================
toc: true
toc-title: " "
toc-location: left

# ========================================================================
# CONFIGURACIÓN DE REFERENCIAS Y CITAS
# ========================================================================
floatsintext: true
citation: true
google-scholar: true
link-citations: true
appendix-cite-as: display
citation-last-author-separator: "y"
citation-masked-author: "Cita Enmascarada"
citation-masked-title: "Título Enmascarado"
citation-masked-date: "n.f."

title-block-author-note: "Nota de Autores"
title-block-correspondence-note: "La correspondencia relativa a este  \ 
artículo debe dirigirse a"
title-block-role-introduction: "Los roles de autor se clasificaron    \ 
utilizando la taxonomía de roles de colaborador (CRediT;  \ 
https://credit.niso.org/) de la siguiente manera:"
references-meta-analysis: "Las referencias marcadas con un asterisco  \ 
indican estudios incluidos en el metanálisis."

# ========================================================================
# CONFIGURACIÓN DE REFERENCIAS CRUZADAS
# ========================================================================
language:
  crossref-fig-title: Figura
  crossref-tbl-title: Tabla
  crossref-lst-title: "Listing"
  crossref-thm-title: "Teorema"
  crossref-lem-title: "Lema"
  crossref-cor-title: "Corolario"
  crossref-prp-title: "Proposición"
  crossref-cnj-title: "Conjetura"
  crossref-def-title: "Definición"
  crossref-exm-title: "Ejemplo"
  crossref-exr-title: "Ejercicio"
  crossref-ch-prefix: "Capítulo"
  crossref-apx-prefix: Anexo
  crossref-sec-prefix: "Sección"
  crossref-eq-prefix: Ecuación
  crossref-lof-title: "Lista de Figuras"
  crossref-lot-title: "Lista de Tablas"
  crossref-lol-title: "Lista de Listings"

# ========================================================================
# CONFIGURACIÓN DE VISIBILIDAD Y BORRADOR
# ========================================================================
mask: false
draft: true
draftfirst: false
draftall: false

# ========================================================================
# FORMATOS DE SALIDA
# ========================================================================
format:
  html:
    toc-depth: 1
    toc-expand: 3
    smooth-scroll: true
    link-external-newwindow: true
    citations-hover: true
    footnotes-hover: true
    highlight-style: github
    code-copy: true
    code-fold: true
    code-summary: "Mostrar el código"
    code-overflow: scroll
    code-line-numbers: true
    code-tools:
      source: repo
      toggle: false
      caption: none
    mermaid:
      theme: neutral
    citation-location: document
    self-contained: true  #  Crea archivos grandes, considera false
    template-partials:
      - ../_partials/title-block-link-buttons/title-block.html
    theme: litera
    other-links:
      - text: Gravatar
        href: https://gravatar.com/achalmaedison
    format-links: true
    
  apaquarto-pdf:
    documentmode: jou
    copyrightnotice: 2025
    copyrightext: Todos los derechos reservados
    toc: true
    list-of-figures: true
    list-of-tables: true
    keep-tex: true
    fontsize: 12pt
    a4paper: true
    numbered-lines: false
    number-sections: true
    colorlinks: true
    pdf-engine: xelatex
    keep-md: false
    
  apaquarto-docx:
    toc: true
    fontsize: 12pt
    a4paper: true
    numbered-lines: false
    number-sections: true
    keep-md: false

# ========================================================================
# CONFIGURACIÓN DEL ENTORNO DE EJECUCIÓN
# ========================================================================
jupyter: python3

editor:
  mode: source
  markdown:
    canonical: true
    wrap: 72
    references:
      location: section
    auto-wrapping: true
    sentence-spacing: true

# ========================================================================
# CONFIGURACIÓN DE COMENTARIOS
# ========================================================================
comments:
  utterances:
    repo: achalmed/website-achalma
    issue-term: title
    theme: boxy-light
    label: "comments :crystal_ball:"

# ========================================================================
# CONFIGURACIÓN DE EJECUCIÓN
# ========================================================================
execute:
  freeze: true
  keep-md: true
  keep-ipynb: true
  echo: true
  output: true
  warning: false
  error: false
  enabled: false
  cache: true
```

## Configuración Optimizada (Recomendada)

```yaml
# ========================================================================
# METADATA.YML OPTIMIZADO PARA BLOG ACADÉMICO DE ECONOMETRÍA
# ========================================================================
# Versión: 2.0
# Autor: Edison Achalma
# Última actualización: 2025-01-02

# ========================================================================
# SECCIÓN 1: INFORMACIÓN DEL AUTOR
# ========================================================================
author:
  - name: Edison Achalma
    url: https://achalmaedison.netlify.app
    affiliation:
      - id: unsch
        name: Universidad Nacional de San Cristóbal de Huamanga
        department: Escuela Profesional de Economía
        address: Portal Independencia N° 57
        city: Ayacucho
        region: AYA
        postal-code: 05001
        country: Perú
    affiliation-url: https://www.gob.pe/unsch
    orcid: 0000-0001-6996-3364
    email: elmer.achalma.09@unsch.edu.pe
    attributes:
      corresponding: true
    roles:
      - conceptualización
      - análisis formal
      - redacción
      - visualización

author-note:
  disclosures:
    conflict-of-interest: El autor no tiene conflictos de intereses  \
    que revelar.
    data-sharing: El código y los datos están disponibles en  \
    https://github.com/achalmed

# ========================================================================
# SECCIÓN 2: METADATOS GENERALES
# ========================================================================
date-modified: "today"
license: "CC BY-SA"
lang: es
search: true
lightbox: true

# Bloque de título
title-block-banner: true
# title-block-banner: images/banner.jpg  # O imagen personalizada

# ========================================================================
# SECCIÓN 3: TABLA DE CONTENIDOS
# ========================================================================
toc: true
toc-title: " "                            # Vacío = solo ícono
toc-location: left
toc-depth: 3                              # Ajustar según complejidad
toc-expand: 2

# ========================================================================
# SECCIÓN 4: REFERENCIAS Y CITAS
# ========================================================================
floatsintext: true
citation: true
google-scholar: true
link-citations: true
citation-last-author-separator: "y"

# Bibliografía (especificar si tienes archivo común)
# bibliography: ../references.bib
# csl: ../apa-6th-edition.csl

# Textos personalizados
title-block-author-note: "Nota de Autores"
title-block-correspondence-note: "La correspondencia relativa a este  \
artículo debe dirigirse a"
title-block-role-introduction: "Los roles de autor se clasificaron    \
utilizando la taxonomía de roles de colaborador                       \ 
(CRediT; https://credit.niso.org/) de la siguiente manera:"

# ========================================================================
# SECCIÓN 5: REFERENCIAS CRUZADAS
# ========================================================================
language:
  crossref-fig-title: Figura
  crossref-tbl-title: Tabla
  crossref-eq-prefix: Ecuación
  crossref-sec-prefix: "Sección"
  crossref-apx-prefix: Anexo

# ========================================================================
# SECCIÓN 6: VISIBILIDAD
# ========================================================================
draft: true                            # Cambiar a false cuando esté listo
mask: false                            # true para peer review anónimo

# ========================================================================
# SECCIÓN 7: FORMATOS DE SALIDA
# ========================================================================
format:
  # ----------------------------------------------------------------------
  # HTML (Prioritario para blog)
  # ----------------------------------------------------------------------
  html:
    # Tabla de contenidos
    toc-depth: 3
    toc-expand: 2
    
    # Navegación
    smooth-scroll: true
    link-external-newwindow: true
    page-navigation: true                 # Botones Siguiente/Anterior
    
    # Citas y referencias
    citations-hover: true
    footnotes-hover: true
    citation-location: document
    
    # Código
    highlight-style: github
    code-copy: true
    code-fold: true
    code-summary: "Mostrar el código"
    code-overflow: scroll
    code-line-numbers: true
    code-tools:
      source: repo
      toggle: false
    
    # Diagramas
    mermaid:
      theme: neutral
    
    # Tema y apariencia
    theme: litera
    template-partials:
      - ../_partials/title-block-link-buttons/title-block.html
    
    # Archivos
    self-contained: false            # false = más rápido
    format-links: true               # Enlaces a PDF/DOCX
    
    # Enlaces personalizados (opcional)
    other-links:
      - text: Gravatar
        href: https://gravatar.com/achalmaedison
      - text: GitHub
        href: https://github.com/achalmed
    
  # ----------------------------------------------------------------------
  # PDF (Formato académico)
  # ----------------------------------------------------------------------
  apaquarto-pdf:
    documentmode: jou                # jou (journal) o man (manuscript)
    
    # Copyright
    copyrightnotice: 2025
    copyrightext: Todos los derechos reservados
    
    # Estructura
    toc: true
    list-of-figures: true
    list-of-tables: true
    number-sections: true
    
    # Formato
    fontsize: 12pt
    a4paper: true
    numbered-lines: false
    colorlinks: true
    
    # Motor
    pdf-engine: xelatex
    
    # Archivos
    keep-tex: true
    keep-md: false
    
  # ----------------------------------------------------------------------
  # DOCX (Opcional)
  # ----------------------------------------------------------------------
  apaquarto-docx:
    toc: true
    fontsize: 12pt
    number-sections: true
    keep-md: false

# ========================================================================
# SECCIÓN 8: ENTORNO DE EJECUCIÓN
# ========================================================================
jupyter: python3

# Editor
editor:
  mode: source
  markdown:
    canonical: true
    wrap: 72
    references:
      location: section
    auto-wrapping: true

# ========================================================================
# SECCIÓN 9: COMENTARIOS
# ========================================================================
comments:
  utterances:
    repo: achalmed/website-achalma
    issue-term: title
    theme: boxy-light
    label: "comments :crystal_ball:"

# ========================================================================
# SECCIÓN 10: EJECUCIÓN DE CÓDIGO
# ========================================================================
execute:
  freeze: true                            # No re-ejecutar en cada render
  keep-md: true                           # Mantener Markdown intermedio
  keep-ipynb: true                        # Mantener notebooks
  echo: true                              # Mostrar código
  output: true                            # Mostrar resultados
  warning: false                          # Ocultar warnings
  error: false                            # Ocultar errores
  enabled: false                          # Deshabilitado por defecto
  cache: true                             # Usar caché

# ========================================================================
# FIN DE CONFIGURACIÓN
# ========================================================================
```

**Cambios principales en la versión optimizada:**

1. **Organización más clara** con comentarios descriptivos
2. **self-contained: false** para archivos más pequeños
3. **page-navigation: true** para mejor UX
4. **Comentarios sobre opciones opcionales** (bibliografía, imagen)
5. **Documentación de versión** en el header
6. **Valores más sensatos** para toc-depth y toc-expand


# Migración de Configuraciones Antiguas

## Paso 1: Identificar Configuraciones Obsoletas

```yaml
#  OBSOLETAS (ya no se usan):
image-path: "..."                        # Automático
cite-method: biblatex                    # Incompatible con HTML

#  UBICACIÓN INCORRECTA:
highlight-style: github                  # Debe estar bajo format:html
format-links: [pdf, ipynb]               # Debe estar bajo format:html
```

## Paso 2: Mover Opciones a Ubicación Correcta

**Antes:**

```yaml
highlight-style: github       #  Top-level

format:
  html:
    toc: true
```

**Después:**

```yaml
format:
  html:
    toc: true
    highlight-style: github   # Dentro de html
```

## Paso 3: Actualizar Opciones de Referencias Cruzadas

**Antes (formato antiguo):**

```yaml
crossref:
  fig-title: Figura
  fig-prefix: Figura
  tbl-title: Tabla
```

**Después (formato nuevo):**

```yaml
language:
  crossref-fig-title: Figura
  crossref-tbl-title: Tabla
```

## Paso 4: Convertir a apaquarto (Si Aplica)

**Antes (PDF básico):**

```yaml
format:
  pdf:
    documentclass: article
    papersize: a4
    toc: true
```

**Después (apaquarto):**

```yaml
format:
  apaquarto-pdf:
    documentmode: jou
    a4paper: true
    toc: true
```

**Instalar apaquarto:**

```bash
cd ~/Documents/publicaciones/epsilon-y-beta
quarto add wjschne/apaquarto
```

## Paso 5: Limpiar Opciones Comentadas

```yaml
#  Eliminar o descomentar:
# css: index.css
# number-sections: true

# Decidir: usar o eliminar
css: index.css                # Descomentar si existe el archivo
number-sections: true         # Descomentar si quieres numeración
```


# Best Practices

## 1. Organización del Archivo

```yaml
# BUENO: Organizado por secciones con comentarios
# ========================================================================
# SECCIÓN 1: AUTOR
# ========================================================================
author:
  - name: ...

# ========================================================================
# SECCIÓN 2: METADATOS
# ========================================================================
lang: es
```

```yaml
#  MALO: Todo mezclado sin estructura
author:
  - name: ...
lang: es
toc: true
draft: true
```

## 2. Comentarios Útiles

```yaml
# BUENO: Explica el por qué
execute:
  freeze: true    # No re-ejecutar: análisis tarda 30 minutos

#  MALO: Repite lo obvio
execute:
  freeze: true    # Freeze es true
```

## 3. Valores Por Defecto

```yaml
# BUENO: Solo especifica lo diferente del defecto
toc: true         # Default es false, así que especificamos

#  MALO: Especifica valores que ya son el defecto
search: true      # Ya es true por defecto, innecesario
```

## 4. DRY (Don't Repeat Yourself)

```yaml
# BUENO: En _metadata.yml (una vez)
author:
  - name: Edison Achalma

#  MALO: En cada post individual
# Repites autor en 50 posts = 50 lugares para actualizar
```

## 5. Jerarquía Clara

```
_quarto.yml           ← Config global (todo el sitio)
   ↓
categoría/_metadata.yml  ← Config de categoría
   ↓
post/index.qmd        ← Config específica del post
```

## 6. Documentación de Cambios

```yaml
# ========================================================================
# METADATA.YML
# ========================================================================
# Versión: 2.0
# Última actualización: 2025-01-02
# Cambios:
#   - Migrado a apaquarto
#   - Actualizado email de autor
#   - Añadido soporte para múltiples formatos
```

## 7. Uso de Anclas YAML (DRY avanzado)

```yaml
# Definir afiliación una vez
affiliations:
  - id: unsch
    name: Universidad Nacional de San Cristóbal de Huamanga
    # ...

# Referenciarla en múltiples autores
author:
  - name: Autor 1
    affiliation:
      - ref: unsch
  - name: Autor 2
    affiliation:
      - ref: unsch
```

## 8. Versionado con Git

```bash
# Commit cada cambio significativo
git add 01-fundamentos-econometria/_metadata.yml
git commit -m "feat(metadata): Añadir apaquarto PDF support"
```

## 9. Testing de Configuración

```bash
# Siempre probar después de cambios
quarto render 01-fundamentos-econometria/ --to html
quarto render 01-fundamentos-econometria/ --to apaquarto-pdf

# Verificar que no hay errores
```

## 10. Backup Antes de Cambios Grandes

```bash
# Crear backup
cp 01-fundamentos-econometria/_metadata.yml \
   01-fundamentos-econometria/_metadata.yml.backup

# Hacer cambios
# ...

# Si algo sale mal:
mv 01-fundamentos-econometria/_metadata.yml.backup \
   01-fundamentos-econometria/_metadata.yml
```


# Troubleshooting

## Problema 1: Opciones No Se Aplican

**Síntoma:** Cambias `_metadata.yml` pero no se ve el cambio.

**Causas y soluciones:**

```bash
# Causa 1: Caché de Quarto
# Solución:
rm -rf .quarto
quarto render

# Causa 2: Freeze activado (código no se re-ejecuta)
# Solución:
quarto render --execute

# Causa 3: Opción sobrescrita en post individual
# Revisar el front-matter del post

# Causa 4: Sintaxis YAML incorrecta
# Validar YAML online: https://www.yamllint.com/
```

## Problema 2: Error de YAML

**Síntoma:**

```
Error: YAML parse error at line 15
```

**Causas comunes:**

```yaml
#  MALO: Indentación incorrecta
author:
  - name: Edison Achalma
  affiliation:           # ← Debe tener espacios adicionales
    - name: UNSCH

# BUENO:
author:
  - name: Edison Achalma
    affiliation:         # ← Correctamente indentado
      - name: UNSCH
```

```yaml
#  MALO: Falta quote en string con caracteres especiales
title: My Title: With Colon

# BUENO:
title: "My Title: With Colon"
```

```yaml
#  MALO: Mezcla tabs y espacios (usa solo espacios)

# BUENO: Solo espacios (2 o 4, consistente)
```

**Verificar sintaxis:**

```bash
# Usar yamllint
yamllint _metadata.yml

# O validar online
# https://www.yamllint.com/
```

## Problema 3: apaquarto No Funciona

**Síntoma:**

```
Error: Unknown format 'apaquarto-pdf'
```

**Solución:**

```bash
# Verificar si está instalado
ls _extensions/wjschne/apaquarto

# Si no existe, instalar:
quarto add wjschne/apaquarto

# Actualizar si está desactualizado:
quarto update wjschne/apaquarto
```

## Problema 4: Bibliografía No Aparece

**Síntoma:** No se muestran referencias.

**Checklist:**

```yaml
# 1. ¿Archivo .bib existe y tiene contenido?
ls references.bib

# 2. ¿Ruta correcta en _metadata.yml?
bibliography: references.bib      # Relativo a _metadata.yml
# O:
bibliography: ../references.bib   # Si está en directorio padre

# 3. ¿Tienes citas en el documento?
# Necesitas al menos una cita para que aparezca la bibliografía
# Ejemplo: [@achalma2024]

# 4. ¿CSL existe?
csl: apa-6th-edition.csl
# Verificar:
ls apa-6th-edition.csl
```

## Problema 5: Código No Se Ejecuta

**Síntoma:** Código en posts no se ejecuta.

**Causas:**

```yaml
# Causa 1: freeze: true (diseño intencional)
execute:
  freeze: true        # ← No re-ejecuta

# Solución: Render con --execute
quarto render --execute

# O cambiar a:
execute:
  freeze: auto        # Re-ejecuta si código cambió
```

```yaml
# Causa 2: enabled: false
execute:
  enabled: false      # ← Ejecución deshabilitada

# Solución: Cambiar a true
execute:
  enabled: true
```

```yaml
# Causa 3: Kernel incorrecto
jupyter: python3      # ¿Tienes Python instalado?
# O
jupyter: ir          # ¿Tienes R + IRkernel?

# Verificar:
jupyter kernelspec list
```

## Problema 6: PDF No Se Genera

**Síntoma:**

```
Error: LaTeX failed to compile
```

**Soluciones:**

```bash
# 1. Verificar que tienes LaTeX instalado
xelatex --version

# Si no:
# Linux:
sudo apt install texlive-xetex

# macOS:
brew install --cask mactex

# O usar TinyTeX (recomendado):
quarto install tinytex

# 2. Ver log detallado
quarto render --verbose

# 3. Verificar paquetes LaTeX necesarios
# En el .tex generado busca:
\usepackage{...}
# E instalarlos si faltan
```

## Problema 7: Conflictos entre _quarto.yml y _metadata.yml

**Síntoma:** Comportamiento inesperado o inconsistente.

**Entender jerarquía:**

```yaml
# _quarto.yml (global)
format:
  html:
    toc: true
    toc-depth: 2

# _metadata.yml (categoría)
format:
  html:
    toc-depth: 3      # ← Sobrescribe toc-depth
    # toc: true heredado de _quarto.yml

# index.qmd (post)
---
format:
  html:
    toc: false        # ← Sobrescribe toc
---
```

**Regla:** Más específico gana.

**Debug:**

```bash
# Ver configuración efectiva
quarto inspect post/index.qmd
```

## Problema 8: Imágenes No Aparecen

**Síntoma:** Imágenes rotas en HTML.

**Soluciones:**

```markdown
#  MALO: Ruta absoluta desde sistema
![](~/Documents/blog/images/fig1.png)

# BUENO: Ruta relativa al documento
![](images/fig1.png)

# BUENO: Ruta relativa al proyecto
![](/posts/2021-03-01/images/fig1.png)
```

```yaml
# Configurar lightbox si no funcionan las imágenes
lightbox: true
```

# Conclusión

## ¿Qué va en `_metadata.yml`?

```yaml
SÍ incluir:
- Información del autor (común a todos los posts)
- Afiliación institucional
- Opciones de formato compartidas
- Configuración de ejecución de código
- Idioma y localización
- Opciones de draft/visibilidad

 NO incluir:
- Título del post (va en index.qmd)
- Fecha del post (va en index.qmd)
- Categorías del post (va en index.qmd)
- Contenido específico del post
- Opciones únicas de un solo post
```

## Template Rápido (Copiar/Pegar)

```yaml
# ========================================================================
# TEMPLATE RÁPIDO _metadata.yml
# ========================================================================

author:
  - name: TU NOMBRE
    orcid: 0000-0000-0000-0000
    email: tu@email.com
    affiliation:
      - name: Tu Universidad
        department: Tu Departamento
        city: Tu Ciudad
        country: Tu País

date-modified: "today"
lang: es
license: "CC BY-SA"
draft: true

toc: true
toc-location: left

format:
  html:
    theme: litera
    code-fold: true
    code-copy: true

execute:
  freeze: true
  echo: true
  warning: false
```

## Comandos Útiles

```bash
# Renderizar categoría completa
quarto render 01-fundamentos-econometria/

# Renderizar con ejecución de código
quarto render --execute

# Renderizar formato específico
quarto render --to html
quarto render --to apaquarto-pdf

# Limpiar caché
rm -rf .quarto
rm -rf _site

# Refrescar caché
quarto render --cache-refresh

# Ver configuración efectiva
quarto inspect post/index.qmd

# Preview local
quarto preview
```


# Publicaciones Similares

Si te interesó este artículo, te recomendamos que explores otros blogs y recursos relacionados que pueden ampliar tus conocimientos. Aquí te dejo algunas sugerencias:


1. [{{< fa regular file-pdf >}}](https://methodica.netlify.app/posts/2023-06-03-ideas-de-investigacion-para-economia/index.pdf) [Ideas De Investigacion Para Economia](https://methodica.netlify.app/posts/2023-06-03-ideas-de-investigacion-para-economia)
2. [{{< fa regular file-pdf >}}](https://methodica.netlify.app/posts/2023-06-03-pautas-de-presentacion-del-informe-de-investigacion/index.pdf) [Pautas De Presentacion Del Informe De Investigacion](https://methodica.netlify.app/posts/2023-06-03-pautas-de-presentacion-del-informe-de-investigacion)
3. [{{< fa regular file-pdf >}}](https://methodica.netlify.app/posts/2025-01-12-recursos-de-bibliografia-y-documentacion/index.pdf) [Recursos De Bibliografia Y Documentacion](https://methodica.netlify.app/posts/2025-01-12-recursos-de-bibliografia-y-documentacion)
4. [{{< fa regular file-pdf >}}](https://methodica.netlify.app/posts/2025-02-09-recursos-para-traducción-y-correccion/index.pdf) [Recursos Para Traducción Y Correccion](https://methodica.netlify.app/posts/2025-02-09-recursos-para-traducción-y-correccion)
5. [{{< fa regular file-pdf >}}](https://methodica.netlify.app/posts/2025-04-23-tipos-de-elementos-en-zotero/index.pdf) [Tipos De Elementos En Zotero](https://methodica.netlify.app/posts/2025-04-23-tipos-de-elementos-en-zotero)


Esperamos que encuentres estas publicaciones igualmente interesantes y útiles. ¡Disfruta de la lectura!

