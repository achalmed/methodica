/* ============================================================================
   HERO — ajuste exacto al alto visible (portada)
   ============================================================================
   Propósito      : Dimensionar el hero de la portada (.quarto-about-solana)
                    para que llene la primera pantalla sin scroll inicial,
                    midiendo header y footer reales (doble pasada que
                    compensa márgenes del grid).
   Cargado por    : assets/interactions.html (include-after-body, global;
                    sale inmediatamente si la página no tiene hero).
   Dependencias   : Fallback CSS en assets/scss/05-pages/home.scss
                    (min-height aproximado si JS no corre).
   Modificar si   : Cambia la composición de la portada.
   ============================================================================ */
(function () {
  "use strict";

  var hero = document.querySelector(".quarto-about-solana");
  if (!hero) return;

  var footer = document.querySelector(".nav-footer");

  var fitHero = function () {
    hero.style.minHeight = "";
    var top = hero.getBoundingClientRect().top + window.scrollY;
    var free = window.innerHeight - top - (footer ? footer.offsetHeight : 0);
    hero.style.minHeight = Math.max(free, 420) + "px";
    /* segunda pasada: compensa márgenes y gaps del grid que quedan
       entre el hero y el footer, midiendo el desbordamiento real */
    var overflow = document.documentElement.scrollHeight - window.innerHeight;
    if (overflow > 0) {
      hero.style.minHeight = Math.max(free - overflow, 420) + "px";
    }
  };

  fitHero();
  /* re-ajustar cuando cargan las imágenes (cambian la altura del hero) */
  window.addEventListener("load", fitHero);
  window.addEventListener("resize", fitHero, { passive: true });
})();
