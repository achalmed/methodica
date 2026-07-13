/* ============================================================================
   NAVBAR — estado de scroll
   ============================================================================
   Propósito      : Añadir/quitar .lab-scrolled en la navbar al hacer scroll
                    (transparencia → sólido; estilos en 03-layout/_navbar.scss).
   Cargado por    : assets/interactions.html (include-after-body, global).
   Dependencias   : Ninguna. Sin JS, la navbar queda translúcida: no se
                    oculta nada.
   Modificar si   : Cambia el umbral o el comportamiento de la barra.
   ============================================================================ */
(function () {
  "use strict";

  var nav = document.querySelector(".navbar");
  if (!nav) return;

  var onScroll = function () {
    nav.classList.toggle("lab-scrolled", window.scrollY > 20);
  };

  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
})();
