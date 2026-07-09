# JS — módulos de interacción "Quiet Laboratory"

Cada módulo es un IIFE independiente, sin dependencias externas y con un solo
propósito. Se cargan en todas las páginas mediante `assets/interactions.html`
(`include-after-body` en `_quarto.yml`) con rutas absolutas `/assets/js/...`.

**Principio de degradación**: sin JavaScript el sitio queda íntegro — ningún
módulo oculta contenido por defecto, solo lo realza. Los módulos que animan
respetan `prefers-reduced-motion`.

| Módulo              | Responsabilidad                                                                                        | Estilos asociados                         |
| ------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| `navbar.js`         | `.lab-scrolled` en la navbar al hacer scroll                                                           | `03-layout/_navbar.scss`                  |
| `cursor.js`         | Glow que sigue el puntero (`--lab-mx/--lab-my`, `.lab-glow-on`); solo pointer fino, sin reduced-motion | `05-interactions/_microinteractions.scss` |
| `hero.js`           | Ajusta el hero de portada al alto visible (sale si no hay hero)                                        | `05-pages/home.scss` (fallback CSS)       |
| `scroll-effects.js` | Revelado escalonado con IntersectionObserver (`.lab-reveal/.lab-in`)                                   | `05-interactions/_microinteractions.scss` |

## Módulos futuros (no crear hasta que hagan falta)

- `theme-toggle.js` — el toggle claro/oscuro es **nativo de Quarto** (no hay
  código propio); crear solo si se necesita comportamiento extra al cambiar
  de tema (p. ej. re-renderizar un gráfico).
- `animations.js` — reservado para animaciones no ligadas al scroll.

## Para añadir un módulo

1. Crear `assets/js/<nombre>.js` (IIFE, `"use strict"`, encabezado con
   propósito/dependencias, salida temprana si la página no aplica).
2. Añadir `<script src="/assets/js/<nombre>.js"></script>` en
   `assets/interactions.html`.
3. Respetar `prefers-reduced-motion` si anima algo.
