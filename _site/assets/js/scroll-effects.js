/* ============================================================================
   SCROLL EFFECTS — aparición escalonada al hacer scroll
   ============================================================================
   Propósito      : Aplicar .lab-reveal/.lab-in a filas de listado, tarjetas
                    y secciones narrativas (.lab-section) mediante
                    IntersectionObserver, con retardo escalonado por columna.
   Cargado por    : assets/interactions.html (include-after-body, global).
   Dependencias   : Estilos en 05-interactions/_microinteractions.scss.
                    Sin JS o con prefers-reduced-motion TODO queda visible:
                    nada se oculta por defecto.
   Modificar si   : Cambian los elementos revelados o el ritmo del efecto.
   ============================================================================ */
(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce || !("IntersectionObserver" in window)) return;

  var items = document.querySelectorAll(
    ".quarto-listing .quarto-post, .quarto-listing .card, .quarto-grid-item, .lab-section"
  );
  if (!items.length) return;

  var io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("lab-in");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.06, rootMargin: "0px 0px -5% 0px" }
  );

  items.forEach(function (el, i) {
    el.classList.add("lab-reveal");
    el.style.transitionDelay = (i % 4) * 60 + "ms";
    io.observe(el);
  });
})();
