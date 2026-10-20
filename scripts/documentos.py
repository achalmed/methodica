#!/usr/bin/env python3
"""documentos.py — PDF y DOCX de las páginas, aparte del render HTML y solo para las fuentes que cambiaron (fase 2, 2026-10-20).

`scripts/render.sh` renderiza solo HTML; este script compila los demás formatos que declara cada página (hoy
`apaquarto-pdf` con LuaLaTeX y `apaquarto-docx`) con `quarto render <página> --to <formatos> --use-freezer`, y solo
cuando cambió su **clave**: el sha256 de todo lo que entra en el documento (la carpeta de la página sin sus
intermedios ni las páginas anidadas, sus `include`, su `bibliography` y `csl`, la cadena de `_metadata.yml`,
`_quarto.yml` sin `website` ni `format.html`, `_filters/`, `_extensions/`, la versión de Quarto), la fecha
`SOURCE_DATE_EPOCH` de la página y la de modificación de su fuente (el DOCX lleva `date-modified`). Esa fecha es la del último commit que tocó la página, no la del sitio: así un
documento cuya fuente no cambió sale idéntico byte a byte aunque se recompile (`--forzar`), y la fecha interna del
PDF y del DOCX es la de su fuente.

La caché es `_documentos.tsv` en la raíz del sitio, versionada junto al `_site/` que describe (GENERADO; no se
edita): una fila por página y formato con la salida, la clave y el sha256 de la salida. Un documento está al día si
su fila tiene la clave actual y su salida en `_site/` tiene ese sha256; si falta o alguien la pisó, se recompila.
Solo se consideran las páginas publicadas (con su HTML en `_site/`): un borrador o una página sin render no lleva
documentos. Las filas de páginas que ya no existen se descartan; sus salidas las quita el render HTML.

Uso:  python3 scripts/documentos.py [carpeta del sitio] [--aplicar] [--forzar] [--solo RUTA]… [--registrar] [--verificar]
      (o `scripts/render.sh --documentos …`, que fija la fecha del sitio como respaldo)
      sin opciones simula: dice qué compilaría y por qué
      --aplicar      compila lo que no está al día y actualiza _documentos.tsv tras cada página
      --forzar       compila aunque esté al día (con --solo, solo esas páginas)
      --solo RUTA    limita a las páginas bajo RUTA (relativa a la raíz del sitio; se repite)
      --registrar    adopta los documentos que ya están en _site/ sin compilarlos (primera vez en un sitio cuyo
                     _site/ salió de un render completo con las fuentes confirmadas); con --aplicar escribe
      --verificar    sale 1 si algún documento falta o no está al día (no escribe)
Salida: 0 bien · 1 documentos por compilar (--verificar) o alguna compilación falló · 2 uso o carpeta incorrectos.
"""
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ESTADO = "_documentos.tsv"
CABECERA = (
    "# _documentos.tsv — GENERADO por scripts/documentos.py; no editar\n"
    "# Caché del modo documentos (render.sh --documentos): una fila por página y formato; la clave es el sha256 de la\n"
    "# fuente y de la fecha de la página; sha256 es el de la salida en _site/. Ver web/docs/decisiones.md §4.5.\n"
    "fuente\tformato\tsalida\tclave\tsha256\n"
)
BASES_DOCUMENTO = {"pdf", "docx", "odt", "epub", "pptx", "typst", "beamer"}
EXTENSIONES = (".qmd", ".md", ".ipynb", ".rmd", ".Rmd")
INTERMEDIOS = (".tex", ".html.md", ".quarto_ipynb", ".log", ".aux", ".pdf", ".docx")
OMITIR = {".quarto", "__pycache__", ".git", ".Rhistory", ".directory"}
NINGUNO = "-"


def git(raiz, *args):
    r = subprocess.run(["git", "-C", str(raiz), *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


_SUMAS = {}


def sha_archivo(p):
    p = Path(p)
    if p not in _SUMAS:
        h = hashlib.sha256()
        with open(p, "rb") as f:
            for bloque in iter(lambda: f.read(1 << 20), b""):
                h.update(bloque)
        _SUMAS[p] = h.hexdigest()
    return _SUMAS[p]


def archivos_bajo(d):
    for raiz, dirs, nombres in os.walk(d):
        dirs[:] = sorted(x for x in dirs if x not in OMITIR)
        for n in sorted(nombres):
            if n not in OMITIR:
                yield Path(raiz) / n


def inspeccionar(raiz, ruta="."):
    r = subprocess.run(["quarto", "inspect", ruta], cwd=raiz, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"quarto inspect {ruta}: {r.stderr.strip()[-300:]}")
    return json.loads(r.stdout)


def frontmatter(texto):
    if not texto.startswith("---"):
        return {}
    fin = texto.find("\n---", 3)
    try:
        import yaml
        datos = yaml.safe_load(texto[3:fin]) if fin > 0 else None
    except Exception:
        return {}
    return datos if isinstance(datos, dict) else {}


def quarto_yml_documental(raiz):
    """_quarto.yml sin lo que no entra en un PDF ni en un DOCX (navegación del sitio y formato HTML)."""
    texto = (raiz / "_quarto.yml").read_text(encoding="utf-8")
    try:
        import yaml
        datos = yaml.safe_load(texto) or {}
        datos.pop("website", None)
        if isinstance(datos.get("format"), dict):
            datos["format"].pop("html", None)
        return json.dumps(datos, sort_keys=True, ensure_ascii=False, default=str)
    except Exception:          # sin PyYAML, el archivo entero (más recompilaciones, nunca menos)
        return texto


class Sitio:
    def __init__(self, raiz):
        self.raiz = raiz
        self.site = raiz / "_site"
        self.quarto = subprocess.run(["quarto", "--version"], capture_output=True, text=True).stdout.strip()
        proyecto = inspeccionar(raiz)
        self.entradas = sorted(Path(p).resolve().relative_to(raiz).as_posix() for p in proyecto["files"]["input"])
        self.info = proyecto.get("fileInformation", {})
        comun = [("quarto", self.quarto), ("_quarto.yml", hashlib.sha256(quarto_yml_documental(raiz).encode()).hexdigest())]
        for d in ("_filters", "_extensions"):
            comun += [(p.relative_to(raiz).as_posix(), sha_archivo(p)) for p in archivos_bajo(raiz / d)] if (raiz / d).is_dir() else []
        self.comun = comun
        self.epoch_sitio = os.environ.get("SOURCE_DATE_EPOCH") or git(raiz, "log", "-1", "--format=%ct") or str(int(time.time()))
        self.paginas_dirs = {Path(e).parent for e in self.entradas if Path(e).stem == "index"}

    def publicada(self, fuente):
        return (self.site / Path(fuente).with_suffix(".html")).is_file()

    def epoch(self, fuente):
        p = Path(fuente)
        objetivo = p.parent.as_posix() if p.stem == "index" and p.parent != Path(".") else fuente
        t = git(self.raiz, "log", "-1", "--format=%ct", "--", objetivo,
                ":(exclude,glob)**/*.tex", ":(exclude,glob)**/*.html.md", ":(exclude,glob)**/*.ipynb")
        return t or self.epoch_sitio

    def fecha_archivo(self, fuente):
        """La fecha de modificación que Quarto leerá (`date-modified: last-modified`, que el DOCX lleva): la del último
        commit del archivo si está limpio, como la fija fechas-desde-git.py en el pre-render; si no, la del disco."""
        if not git(self.raiz, "-c", "core.quotePath=false", "status", "--porcelain", "--", fuente):
            t = git(self.raiz, "log", "-1", "--format=%ct", "--", fuente)
            if t:
                return t
        return str(int((self.raiz / fuente).stat().st_mtime))

    def entradas_de(self, fuente):
        """Archivos que entran en los documentos de la página, como (ruta relativa, sha256)."""
        raiz, p = self.raiz, Path(fuente)
        archivos = set()
        if p.stem == "index" and p.parent != Path("."):
            base = raiz / p.parent
            for a in archivos_bajo(base):
                rel = a.relative_to(raiz)
                if any(d in self.paginas_dirs for d in rel.parents if p.parent in d.parents):   # una página anidada no es de esta
                    continue
                if a.name.endswith(INTERMEDIOS) and a.name.startswith(p.stem + "."):
                    continue
                if a.suffix == ".ipynb" and a.stem == p.stem and p.suffix != ".ipynb":     # keep-ipynb
                    continue
                if any(part.endswith("_files") for part in rel.parts[:-1]):
                    continue
                archivos.add(a)
        else:
            archivos.add(raiz / p)
        for inc in self.info.get(fuente, {}).get("includeMap", []):
            origen = Path(inc.get("source", raiz / p)).parent
            archivos.add((origen / inc["target"]).resolve())
        fm = frontmatter((raiz / p).read_text(encoding="utf-8", errors="ignore"))
        for clave in ("bibliography", "csl"):
            valores = fm.get(clave) or []
            for v in [valores] if isinstance(valores, str) else valores:
                if isinstance(v, str):
                    archivos.add(((raiz / p).parent / v).resolve())
        d = p.parent
        while True:                                   # la cadena de _metadata.yml hasta la raíz
            archivos.add(raiz / d / "_metadata.yml")
            if d == Path("."):
                break
            d = d.parent
        filas = []
        for a in sorted(archivos):
            if a.is_file():
                try:
                    rel = a.resolve().relative_to(raiz).as_posix()
                except ValueError:
                    rel = a.as_posix()
                filas.append((rel, sha_archivo(a)))
        return filas

    def clave(self, fuente, epoch):
        h = hashlib.sha256()
        for nombre, valor in self.comun + [("epoch", epoch), ("mtime", self.fecha_archivo(fuente))] + self.entradas_de(fuente):
            h.update(f"{nombre}\t{valor}\n".encode())
        return h.hexdigest()

    def formatos(self, fuente):
        """Formatos de documento de la página y su archivo de salida en _site/, según `quarto inspect`."""
        d = inspeccionar(self.raiz, fuente)
        res = []
        for nombre, f in d.get("formats", {}).items():
            base = f.get("identifier", {}).get("base-format", nombre.split("+")[0])
            salida = f.get("pandoc", {}).get("output-file")
            if base in BASES_DOCUMENTO and salida:
                res.append((nombre, (Path(fuente).parent / salida).as_posix()))
        return res


def leer_estado(raiz):
    filas = {}
    p = raiz / ESTADO
    if p.is_file():
        for linea in p.read_text(encoding="utf-8").splitlines():
            if not linea or linea.startswith("#") or linea.startswith("fuente\t"):
                continue
            c = linea.split("\t")
            if len(c) == 5:
                filas.setdefault(c[0], []).append(dict(zip(("fuente", "formato", "salida", "clave", "sha256"), c)))
    return filas


def escribir_estado(raiz, filas):
    lineas = [CABECERA]
    for fuente in sorted(filas):
        for f in sorted(filas[fuente], key=lambda x: x["formato"]):
            lineas.append("\t".join(f[k] for k in ("fuente", "formato", "salida", "clave", "sha256")) + "\n")
    tmp = raiz / (ESTADO + ".tmp")
    tmp.write_text("".join(lineas), encoding="utf-8")
    tmp.replace(raiz / ESTADO)


def al_dia(sitio, filas, clave):
    if not filas or any(f["clave"] != clave for f in filas):
        return "clave nueva" if filas else "sin registro"
    for f in filas:
        if f["formato"] == NINGUNO:
            continue
        s = sitio.site / f["salida"]
        if not s.is_file():
            return f"falta {f['salida']}"
        if sha_archivo(s) != f["sha256"]:
            return f"{f['salida']} distinto del registrado"
    return ""


def main(argv):
    opciones = {"--aplicar", "--forzar", "--registrar", "--verificar"}
    solo, resto, i = [], [], 0
    while i < len(argv):
        a = argv[i]
        if a == "--solo":
            if i + 1 >= len(argv):
                print("documentos: --solo pide una ruta", file=sys.stderr)
                return 2
            solo.append(argv[i + 1].strip("/")); i += 2; continue
        if a in ("-h", "--help"):
            print(__doc__); return 0
        if a.startswith("--") and a not in opciones:
            print(f"documentos: opción desconocida {a}", file=sys.stderr); return 2
        resto.append(a); i += 1
    aplicar, forzar = "--aplicar" in resto, "--forzar" in resto
    registrar, verificar = "--registrar" in resto, "--verificar" in resto
    carpetas = [a for a in resto if not a.startswith("--")]
    raiz = Path(carpetas[0] if carpetas else ".").resolve()
    if not (raiz / "_quarto.yml").is_file() or not (raiz / "_site").is_dir():
        print(f"documentos: {raiz} no es un sitio Quarto con _site/ (renderiza antes el HTML: scripts/render.sh)", file=sys.stderr)
        return 2
    sitio = Sitio(raiz)
    estado = leer_estado(raiz)
    nuevas = {}
    pendientes = []
    for fuente in sitio.entradas:
        if not sitio.publicada(fuente):
            continue
        dentro = not solo or any(fuente == s or fuente.startswith(s + "/") for s in solo)
        epoch = sitio.epoch(fuente)
        clave = sitio.clave(fuente, epoch)
        motivo = al_dia(sitio, estado.get(fuente, []), clave)
        if forzar and dentro and not motivo:
            motivo = "forzado"
        if motivo and dentro:
            pendientes.append((fuente, epoch, clave, motivo))
        if fuente in estado:
            nuevas[fuente] = estado[fuente]
    descartadas = sorted(set(estado) - {f for f in sitio.entradas if sitio.publicada(f)})

    if verificar:
        for fuente, _, _, motivo in pendientes:
            print(f"✖ {fuente}: {motivo}")
        print(f"documentos: {len(pendientes)} página(s) sin sus documentos al día")
        return 1 if pendientes else 0

    if registrar:
        adoptadas = 0
        for fuente, epoch, clave, motivo in pendientes:
            formatos = sitio.formatos(fuente)
            filas = [{"fuente": fuente, "formato": NINGUNO, "salida": NINGUNO, "clave": clave, "sha256": NINGUNO}] if not formatos else []
            for nombre, salida in formatos:
                s = sitio.site / salida
                if not s.is_file():
                    print(f"  {fuente}: falta {salida}; no se registra (--aplicar lo compila)")
                    filas = []
                    break
                filas.append({"fuente": fuente, "formato": nombre, "salida": salida, "clave": clave, "sha256": sha_archivo(s)})
            if filas:
                nuevas[fuente] = filas
                adoptadas += 1
        if aplicar:
            escribir_estado(raiz, nuevas)
        modo = "registradas" if aplicar else "se registrarían (simulación; --aplicar escribe)"
        print(f"documentos: {adoptadas} página(s) {modo} sin compilar; {len(descartadas)} fila(s) de páginas retiradas fuera")
        return 0

    for fuente, epoch, _, motivo in pendientes:
        print(f"{'→' if not aplicar else '·'} {fuente}: {motivo}")
    if not aplicar:
        print(f"documentos: compilaría {len(pendientes)} página(s) (simulación; --aplicar compila); "
              f"{len(descartadas)} fila(s) de páginas retiradas saldrían de {ESTADO}")
        return 0

    fallos = 0
    inicio = time.monotonic()
    for fuente, epoch, clave, _ in pendientes:
        t0 = time.monotonic()
        formatos = sitio.formatos(fuente)
        if not formatos:
            nuevas[fuente] = [{"fuente": fuente, "formato": NINGUNO, "salida": NINGUNO, "clave": clave, "sha256": NINGUNO}]
            escribir_estado(raiz, nuevas)
            print(f"  {fuente}: sin formatos de documento")
            continue
        entorno = dict(os.environ, SOURCE_DATE_EPOCH=epoch, FORCE_SOURCE_DATE="1")
        orden = ["quarto", "render", fuente, "--to", ",".join(n for n, _ in formatos), "--use-freezer"]
        r = subprocess.run(orden, cwd=raiz, env=entorno, capture_output=True, text=True)
        salidas = [(n, sitio.site / s, s) for n, s in formatos]
        if r.returncode != 0 or not all(p.is_file() for _, p, _ in salidas):
            fallos += 1
            print(f"✖ {fuente}: falló ({r.returncode}); últimas líneas:\n" + "\n".join(r.stderr.strip().splitlines()[-8:]), file=sys.stderr)
            continue
        for _, p, _ in salidas:                      # las salidas acaban de cambiar
            _SUMAS.pop(p, None)
        nuevas[fuente] = [{"fuente": fuente, "formato": n, "salida": s, "clave": clave, "sha256": sha_archivo(p)} for n, p, s in salidas]
        escribir_estado(raiz, nuevas)
        print(f"✔ {fuente}: {', '.join(n for n, _ in formatos)} en {time.monotonic() - t0:.0f} s")
    escribir_estado(raiz, nuevas)
    print(f"documentos: {len(pendientes) - fallos} página(s) compiladas, {fallos} fallo(s), "
          f"{len(descartadas)} fila(s) retiradas, {time.monotonic() - inicio:.0f} s")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
