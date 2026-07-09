/* ============================================================================
   CURSOR — iluminación que sigue el puntero
   ============================================================================
   Propósito      : Actualizar --lab-mx / --lab-my y activar .lab-glow-on para
                    el gradiente radial de body::before (estilos en
                    05-interactions/_microinteractions.scss).
   Cargado por    : assets/interactions.html (include-after-body, global).
   Dependencias   : Solo se activa con puntero fino (ratón) y sin
                    prefers-reduced-motion. Throttle vía requestAnimationFrame.
   Modificar si   : Cambia el efecto de luz o sus condiciones de activación.
   ============================================================================ */
(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce || !window.matchMedia("(pointer: fine)").matches) return;

  var pending = false;

  document.addEventListener(
    "mousemove",
    function (e) {
      if (pending) return;
      pending = true;
      var x = e.clientX, y = e.clientY;
      requestAnimationFrame(function () {
        document.body.style.setProperty("--lab-mx", x + "px");
        document.body.style.setProperty("--lab-my", y + "px");
        document.body.classList.add("lab-glow-on");
        pending = false;
      });
    },
    { passive: true }
  );

  document.documentElement.addEventListener("mouseleave", function () {
    document.body.classList.remove("lab-glow-on");
  });
})();
