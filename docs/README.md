# Edison Achalma — Sitio Web Personal

> Investigador y educador que aplica la ciencia de datos priorizando la equidad social.

[![Quarto](https://img.shields.io/badge/Quarto-1.6.42-blue?logo=quarto&logoColor=white)](https://quarto.org) [![Netlify](https://img.shields.io/badge/Netlify-deployed-00C7B7?logo=netlify&logoColor=white)](https://achalmaedison.netlify.app) ![License](https://img.shields.io/badge/Licencia-CC%20BY--SA-lightgrey) ![Estado](https://img.shields.io/badge/Estado-Activo-brightgreen) ![Idioma](https://img.shields.io/badge/Idioma-Espa%C3%B1ol-red)

**🌐 Sitio en producción:** [https://achalmaedison.netlify.app](https://achalmaedison.netlify.app)
**📦 Repositorio:** [https://github.com/achalmed/website-achalma](https://github.com/achalmed/website-achalma)

---

## Tabla de Contenidos

- [Descripción](#descripci%C3%B3n)
- [Red de Sitios Especializados](#red-de-sitios-especializados)
- [Secciones del Sitio Principal](#secciones-del-sitio-principal)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Tecnologías Utilizadas](#tecnolog%C3%ADas-utilizadas)
- [Configuración del Proyecto](#configuraci%C3%B3n-del-proyecto)
- [Cómo Renderizar el Sitio](#c%C3%B3mo-renderizar-el-sitio)
- [Numeración de Publicaciones](#numeraci%C3%B3n-de-publicaciones)
- [Cómo Contribuir](#c%C3%B3mo-contribuir)
- [Licencia](#licencia)
- [Autor](#autor)

---

## Descripción

Este repositorio contiene el código fuente de mi sitio web personal, construido con [Quarto](https://quarto.org) y desplegado en [Netlify](https://netlify.com). El sitio integra publicaciones académicas, material docente, entradas de blog y presentaciones sobre economía, ciencia de datos, matemáticas, programación y metodología de investigación.

El sitio principal actúa como **hub central** de una red de blogs especializados, cada uno alojado en su propio dominio y repositorio, pero con una identidad visual y configuración Quarto coherente.

Los artículos y entradas de blog siguen el estilo APA 7 mediante la extensión [`apaquarto`](https://github.com/wjschne/apaquarto), y los documentos se publican en formatos HTML, PDF y DOCX desde un mismo archivo fuente `.qmd`.

---

## Red de Sitios Especializados

Este sitio principal enlaza y da origen a los siguientes blogs temáticos. Todos comparten la misma configuración base:

| Área temática                | URL                                                                          | Descripción                                                             |
| ---------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Econometría                  | [epsilon-y-beta.netlify.app](https://epsilon-y-beta.netlify.app)             | Modelos econométricos, series de tiempo y análisis estadístico aplicado |
| Filosofía y política         | [dialectica-y-mercado.netlify.app](https://dialectica-y-mercado.netlify.app) | Filosofía política, ética económica y teoría social                     |
| Finanzas                     | [pecunia-fluxus.netlify.app](https://pecunia-fluxus.netlify.app)             | Finanzas personales, corporativas e internacionales                     |
| Gestión empresarial          | [actus-mercator.netlify.app](https://actus-mercator.netlify.app)             | Administración, estrategia y gestión organizacional                     |
| Gestión pública              | [res-publica.netlify.app](https://res-publica.netlify.app)                   | Políticas públicas, administración del Estado y descentralización       |
| Metodología de investigación | [methodica.netlify.app](https://methodica.netlify.app)                       | Métodos cualitativos y cuantitativos, APA, redacción académica          |
| Macroeconomía                | [aequilibria.netlify.app](https://aequilibria.netlify.app)                   | Política monetaria, fiscal, crecimiento económico y ciclos              |
| Matemáticas                  | [axiomata.netlify.app](https://axiomata.netlify.app)                         | Cálculo, álgebra lineal, estadística y matemáticas aplicadas            |
| Microeconomía                | [optimums.netlify.app](https://optimums.netlify.app)                         | Teoría del consumidor, productor, mercados y equilibrio general         |
| Programación y software      | [numerus-scriptum.netlify.app](https://numerus-scriptum.netlify.app)         | R, Python, Quarto, Linux y herramientas para ciencia de datos           |
| Seguridad informática        | [chaska-x.netlify.app](https://chaska-x.netlify.app)                         | Ciberseguridad, privacidad digital y tecnología                         |

---

## Secciones del Sitio Principal

### Blog (`/blog`)

Entradas sobre economía, tecnología, ciencia de datos y temas interdisciplinarios. Cada entrada se publica en HTML, PDF y DOCX con metadatos académicos completos (abstract, keywords, cita APA, ORCID).

Ejemplos de publicaciones:

- _Economía Agraria y Rural en el Perú_ (2022)
- _Impacto del cambio climático en la economía peruana_ (2022)
- _La economía peruana entre 1970–1990_ (2023)
- _Economía Regional y Desarrollo Local_ (2023)

### Talks (`/talk`)

Material de sesiones docentes sobre metodología de investigación y escritura académica (APA 7, estilo Vancouver, técnicas de paráfrasis, tablas y figuras). Las sesiones incluyen presentaciones en PDF y materiales de práctica en ODT/DOCX.

Sesiones disponibles (ciclo 2025):

- Sesión 01: Monografía e informe académico
- Sesión 02: Estructura en Word (portada, títulos)
- Sesión 03: Citas y referencias APA
- Sesión 04: Práctica APA
- Sesión 05: Técnicas de parafraseo y bases de datos académicas
- Sesión 06: Formato APA 7
- Sesión 07: Estilo Vancouver
- Sesión 08: Tablas, figuras y notas
- Sesión 09: Práctica integradora

### Teaching (`/teching`)

Material del curso _Economía Preuniversitaria_ (ciclo 2014), con 14 unidades que cubren desde conceptos básicos hasta macroeconomía y comercio internacional. Disponible en HTML, PDF y DOCX.

Temas incluidos: conceptos básicos de economía · necesidades y bienes · teoría de la producción · costos · oferta y demanda · mercados · empresas · sistema financiero · macroeconomía · inflación · sector público · indicadores económicos · desempleo · comercio internacional.

### Publications (`/publication`)

Publicaciones formales, documentos técnicos y contribuciones externas. Incluye el informe ENIS 2022–2023 con acceso al PDF.

### About, Contact, Appointment

Páginas informativas del autor con formulario de contacto y opción de agendar una cita.

### Carpeta `README/`

Contiene plantillas de referencia para documentos académicos en formato `apaquarto`, organizadas por modo de salida:

| Archivo                           | Modo apaquarto | Uso recomendado                             |
| --------------------------------- | -------------- | ------------------------------------------- |
| `index_doc.qmd`                   | `doc`          | Ensayos, reportes y working papers          |
| `index_jou.qmd`                   | `jou`          | Artículos en formato revista (dos columnas) |
| `index_man.qmd`                   | `man`          | Manuscritos para envío a revistas           |
| `index_stu.qmd`                   | `stu`          | Trabajos académicos estudiantiles           |
| `_metadata_guia.yml`              | —              | Guía completa de metadatos disponibles      |
| `_metadata_guia_simplificada.yml` | —              | Versión simplificada para uso cotidiano     |
| `_quarto_guia.yml`                | —              | Referencia de opciones de `_quarto.yml`     |

---

## Estructura del Repositorio

```
website-achalma/
├── _quarto.yml              # Configuración global del sitio (navbar, footer, tema)
├── index.qmd                # Página de inicio
├── _metadata-pdf.lua        # Filtro Lua para metadatos PDF
├── _partials/               # Parciales HTML personalizados (title-block)
├── assets/                  # Estilos, fuentes, imágenes e íconos
│   ├── img/                 # Logotipos, favicon, imágenes de perfil
│   ├── *.scss               # Temas light/dark (Flatly + personalización)
│   └── styles.css           # CSS global adicional
├── blog/                    # Entradas del blog (subcarpetas por fecha-slug)
│   └── posts/
├── talk/                    # Material de sesiones docentes
├── teching/                 # Cursos y clases (economía preuniversitaria)
├── publication/             # Publicaciones formales
├── about/, contact.qmd      # Páginas informativas
├── README/                  # Plantillas apaquarto y guías de metadatos
├── _extensions/             # Extensiones Quarto instaladas
│   ├── wjschne/apaquarto/   # Formato APA 7 (PDF, DOCX, HTML, Typst)
│   └── quarto-ext/          # FontAwesome, Lightbox
├── _freeze/                 # Resultados cacheados de ejecución de código
├── _site/                   # Sitio compilado (generado, no editar)
├── resources/               # CV en PDF y otros recursos estáticos
├── requirements.txt         # Dependencias Python
└── LICENSE                  # Licencia del proyecto
```

---

## Tecnologías Utilizadas

| Tecnología                                        | Versión            | Rol                                                 |
| ------------------------------------------------- | ------------------ | --------------------------------------------------- |
| [Quarto](https://quarto.org)                      | 1.6.42             | Motor de publicación (`.qmd` → HTML/PDF/DOCX)       |
| [apaquarto](https://github.com/wjschne/apaquarto) | última             | Formato APA 7 para documentos académicos            |
| R                                                 | 4.x                | Análisis estadístico y generación de figuras/tablas |
| Python 3                                          | 3.x                | Análisis de datos y notebooks Jupyter               |
| Bootstrap / Cosmo                                 | 5.x                | Tema visual base del sitio HTML                     |
| SCSS personalizado                                | —                  | Temas light/dark, tipografía y colores del sitio    |
| [Netlify](https://netlify.com)                    | —                  | Hosting y despliegue continuo                       |
| [Utterances](https://utteranc.es)                 | —                  | Sistema de comentarios vía GitHub Issues            |
| FontAwesome 6                                     | 0.1.0              | Íconos en el pie de página y contenido              |
| Lightbox (glightbox)                              | —                  | Visualización ampliada de imágenes                  |
| TinyTeX / XeLaTeX                                 | —                  | Compilación de documentos PDF                       |
| Pandoc                                            | embebido en Quarto | Conversión de formatos de documentos                |

---

## Configuración del Proyecto

### Requisitos previos

- [Quarto CLI](https://quarto.org/docs/get-started/) ≥ 1.6
- R ≥ 4.0 con los paquetes especificados en los `.qmd` individuales
- Python 3 con dependencias en `requirements.txt`
- TinyTeX para compilación PDF: `quarto install tinytex`
- Chromium para capturas (opcional): `quarto install chromium`

### Instalación de extensiones

Las extensiones ya están versionadas en `_extensions/`. Para actualizarlas:

```bash
quarto update wjschne/apaquarto
```

Para reinstalarlas desde cero:

```bash
quarto add wjschne/apaquarto
quarto add quarto-ext/fontawesome
quarto add quarto-ext/lightbox
```

---

## Cómo Renderizar el Sitio

### Renderizado completo

```bash
quarto render
```

### Vista previa en desarrollo

```bash
quarto preview
```

### Renderizar solo un post o sección

```bash
quarto render blog/posts/2023-05-16-economia-regional/index.qmd
quarto render talk/
```

### Limpiar caché y artefactos generados

```bash
# Eliminar el sitio compilado y el caché de Quarto
rm -rf _site .quarto

# Eliminar archivos staged del feed (si hay conflictos)
find . -name "*.feed-full-staged" -exec rm {} \;

# Forzar re-ejecución del caché de cálculos
quarto render --cache-refresh
```

### Comportamiento de `freeze` y `cache`

El proyecto usa `freeze: true` en `_quarto.yml`, lo que significa:

- En un **renderizado global** (`quarto render`), el código R/Python **no se re-ejecuta**; se reutilizan los resultados guardados en `_freeze/`.
- En un **renderizado incremental** (`quarto render archivo.qmd`), el código **siempre se ejecuta**.
- Para forzar la re-ejecución global, eliminar `_freeze/` antes de renderizar.
- `cache: true` guarda resultados de chunks individuales pesados; limpiar con `--cache-refresh`.

---

## Numeración de Publicaciones

Las publicaciones del sitio siguen un esquema trimestral bajo el nombre de publicación _Actus Mercator_:

- **Volumen**: corresponde al año de publicación (ej. Vol. 2025).
- **Número / Issue**: indica el trimestre del año:
  - No. 1 → enero – marzo
  - No. 2 → abril – junio
  - No. 3 → julio – septiembre
  - No. 4 → octubre – diciembre

**Formato de citación recomendado:**

```
Achalma, E. (2025). Título del artículo. Actus Mercator, 2025(2), 45–60.
```

Este esquema facilita la indexación en bases de datos académicas como SciELO, Redalyc, Latindex y RENATI.

---

## Cómo Contribuir

Las contribuciones son bienvenidas. Puedes colaborar de las siguientes formas:

- **Reportar errores o sugerir mejoras** abriendo un [issue](https://github.com/achalmed/website-achalma/issues).
- **Proponer cambios** mediante un pull request: haz fork del repositorio, crea una rama con tu mejora y abre el PR con una descripción clara.
- **Comentar en el sitio** usando el sistema Utterances disponible al pie de cada artículo (requiere cuenta GitHub).
- **Compartir** el sitio o algún artículo en tus redes sociales.

Para cambios estructurales importantes (reorganización de secciones, cambio de tema visual, nuevas extensiones), abre primero un issue para discutirlo antes de enviar el PR.

---

## Licencia

Este proyecto está bajo la licencia **Creative Commons Atribución-CompartirIgual (CC BY-SA)**. Consulta el archivo `license.qmd` para los términos completos.

En resumen: puedes usar, adaptar y redistribuir el contenido siempre que acredites al autor original y mantengas la misma licencia en tus derivados.

---

## 👤 Autor

**Edison Achalma**

[LinkedIn](https://linkedin.com/in/achalmaedison) • [GitHub](https://github.com/achalmed) • [Blog](https://achalmaedison.netlify.app) • [Buy Me a Coffee](https://buymeacoffee.com/achalmaedison)

![Screenshot](../assets/img/achalma-social.png)

<div align="center">

**Hecho con ❤️ desde Ayacucho, Perú**

_"El conocimiento compartido es el conocimiento multiplicado."_

</div>
