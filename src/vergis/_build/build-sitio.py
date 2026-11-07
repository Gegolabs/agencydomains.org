#!/usr/bin/env python3
"""Las páginas de Vergis en el sitio, en español y en inglés:

  /vergis/            /es/vergis/              qué es Vergis, en simple (sitio/vergis.<l>.html)
  /vergis/documents/  /es/vergis/documentos/   la colección de documentos (sitio/documentos.json)
  /vergis/library/    /es/vergis/biblioteca/   la biblioteca de referencias (sitio/biblioteca.json)

Uso: build-sitio.py <dir_vergis> <dist>
  Lee la colección y la biblioteca de <dir_vergis>/sitio/, y la edición web ya construida de cada
  documento de <dir_vergis>/<id>/_dist/web-<l>/ (de ahí salen los enlaces de cada cita y de cada
  capítulo, que se comprueban: una cita a un título que no está detiene el build). Escribe
  <dist>/web-en/ (servida en /vergis/) y <dist>/web-es/ (servida en /es/vergis/), con cada documento
  en su subcarpeta.
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from urllib.parse import urlparse

SITE = "https://agencydomains.org"
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,340..620;1,9..144,340..560&family=Spectral:'
         'ital,wght@0,300;0,400;0,500;0,600;1,400;1,500&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')

RUTA = {  # la ruta de cada página, por lengua
    "es": {"home": "/es/vergis/", "docs": "/es/vergis/documentos/", "lib": "/es/vergis/biblioteca/", "raiz": "/es/", "base": "/es/vergis"},
    "en": {"home": "/vergis/", "docs": "/vergis/documents/", "lib": "/vergis/library/", "raiz": "/", "base": "/vergis"},
}
UI = {
    "es": {
        "home_title": "Vergis · Tecnología Agentiva",
        "home_desc": "Vergis, la implementación de referencia de AgencyDomains, en simple: qué es, dónde encaja en el Mundo Agentivo, su código abierto, sus documentos y su biblioteca de referencias.",
        "docs_title": "Documentos de Vergis",
        "docs_eyebrow": "Vergis · Tecnología Agentiva",
        "docs_deck": "Cómo está hecho Vergis, documento por documento.",
        "docs_intro": "Cada documento se lee en la web, un capítulo por página, o se descarga en PDF, en español y en inglés. Toda la documentación va bajo GNU FDL v1.3.",
        "docs_desc": "La colección de documentos técnicos de Vergis: se leen en la web por capítulos o se descargan en PDF, en español y en inglés.",
        "doc_n": "Documento {n}",
        "version": "versión",
        "leer": "Leer en la web",
        "pdf": "PDF",
        "pdf_otra": "PDF in English",
        "pags": "{n} págs.",
        "pags_otra": "{n} pp.",
        "md": "Markdown",
        "capitulos": "Capítulos",
        "lib_title": "Biblioteca de referencias de Vergis",
        "lib_h1": "Biblioteca de referencias",
        "lib_deck": "Las fuentes que consultan los documentos de Vergis, por tema.",
        "lib_intro": "Cada fuente lleva una línea con lo que aporta y el lugar del documento que la usa. Junto a cada afirmación, el documento dice con qué grado de certeza la sostiene: medido, verificado, reportado o conjetura.",
        "lib_desc": "Las fuentes que consultan los documentos de Vergis, ordenadas por tema, con lo que aporta cada una y dónde la usa cada documento.",
        "en_doc": "En {doc}:",
        "tambien": "también",
        "volver": "← Vergis",
        "raiz": "← agencydomains.org",
        "otra_lengua": "EN",
        "esta_lengua": "ES",
        "siguen": "La colección crece con cada documento que se publica.",
        "a_lib": "Las fuentes de los documentos, por tema: la biblioteca de referencias →",
        "a_docs": "Los documentos que las citan: la colección →",
        "a_repo": "El código: gegolabs/vergis →",
    },
    "en": {
        "home_title": "Vergis · Agentive Technology",
        "home_desc": "Vergis, the reference implementation of AgencyDomains, in plain words: what it is, where it fits in the Agentive World, its open-source code, its documents and its reference library.",
        "docs_title": "Vergis documents",
        "docs_eyebrow": "Vergis · Agentive Technology",
        "docs_deck": "How Vergis is built, one document at a time.",
        "docs_intro": "Each document can be read on the web, one chapter per page, or downloaded as PDF, in English and in Spanish. All documentation is under the GNU FDL v1.3.",
        "docs_desc": "The collection of Vergis technical documents: read them on the web chapter by chapter or download them as PDF, in English and Spanish.",
        "doc_n": "Document {n}",
        "version": "version",
        "leer": "Read on the web",
        "pdf": "PDF",
        "pdf_otra": "PDF en español",
        "pags": "{n} pp.",
        "pags_otra": "{n} págs.",
        "md": "Markdown",
        "capitulos": "Chapters",
        "lib_title": "Vergis reference library",
        "lib_h1": "Reference library",
        "lib_deck": "The sources Vergis's documents consult, by theme.",
        "lib_intro": "Each source carries a line on what it contributes and the place in the document that uses it. Next to every claim, the document states how certain it is: measured, verified, reported or conjecture.",
        "lib_desc": "The sources Vergis's documents consult, ordered by theme, with what each contributes and where each document uses it.",
        "en_doc": "In {doc}:",
        "tambien": "also",
        "volver": "← Vergis",
        "raiz": "← agencydomains.org",
        "otra_lengua": "ES",
        "esta_lengua": "EN",
        "siguen": "The collection grows with each document that is published.",
        "a_lib": "The documents' sources, by theme: the reference library →",
        "a_docs": "The documents that cite them: the collection →",
        "a_repo": "The code: gegolabs/vergis →",
    },
}
OTRA = {"es": "en", "en": "es"}


def slugify(t):  # la de web-build.py: la ruta de cada capítulo
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()


def ref_id(titulo):  # la de yava/_build/referencias.py: el id de cada título
    t = unicodedata.normalize("NFKD", titulo).encode("ascii", "ignore").decode()
    return "ref-" + re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()


def corto(url):
    """El texto de un enlace secundario: el sitio y el último tramo de la ruta."""
    p = urlparse(url)
    ultimo = p.path.rstrip("/").split("/")[-1]
    return p.netloc.removeprefix("www.") + (f"/…/{ultimo}" if ultimo else "")


def inline(md):
    """El Markdown en línea de un título (*cursiva*, `código`) a HTML."""
    s = html.escape(md, quote=False)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", s)


def pagina(L, clave, titulo, desc, cuerpo, crumb_home):
    r, ro = RUTA[L], RUTA[OTRA[L]]
    u = UI[L]
    href_l = {L: r[clave], OTRA[L]: ro[clave]}
    alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{href_l[l]}">\n' for l in ("en", "es"))
    volver = (f'<a href="{r["raiz"]}">{u["raiz"]}</a>' if crumb_home else f'<a href="{r["home"]}">{u["volver"]}</a>')
    return (f'<!DOCTYPE html>\n<html lang="{L}">\n<head>\n<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{titulo}</title>\n<meta name="description" content="{html.escape(desc)}">\n'
            f'<meta property="og:title" content="{titulo}">\n<meta property="og:description" content="{html.escape(desc)}">\n'
            f'<meta property="og:type" content="website">\n<link rel="canonical" href="{SITE}{r[clave]}">\n{alt}{FONTS}\n'
            '<link rel="stylesheet" href="/assets/agencydomains.css">\n<link rel="stylesheet" href="/assets/page.css">\n</head>\n<body>\n'
            f'<main class="page vg">\n  <nav class="crumb">{volver}<span><a href="{ro[clave]}">{u["otra_lengua"]}</a> · '
            f'<span class="on">{u["esta_lengua"]}</span></span></nav>\n{cuerpo}\n</main>\n</body>\n</html>\n')


def paginas_pdf(p):
    out = subprocess.run(["pdfinfo", p], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"^Pages:\s+(\d+)", out, re.M).group(1))


def documento(vdir, d, L):
    """Lo que la colección muestra de un documento, leído de su fuente y de su build."""
    src = open(os.path.join(vdir, d["fuente"][L]), encoding="utf-8").read().split("\n")
    ver = next(re.search(r"\| ([0-9.]+) \|", l).group(1) for l in src if re.match(r"^\| \*\*(Versión|Version)\*\*", l))
    caps, fence = [], False
    for l in src:
        if l.startswith("```"):
            fence = not fence
        if not fence and l.startswith("## "):
            caps.append(l[3:].strip())
    dist = os.path.join(vdir, d["id"], "_dist")
    web = os.path.join(dist, f"web-{L}")
    for c in caps:  # cada capítulo tiene su página en la edición web
        if not os.path.exists(os.path.join(web, slugify(c), "index.html")):
            sys.exit(f"✗ {d['id']} ({L}): el capítulo «{c}» no tiene página en {web}")
    pdf = {l: os.path.join(dist, f"{d['titulo']}-v{ver}-{l}.pdf") for l in ("es", "en")}
    for p in pdf.values():
        if not os.path.exists(p):
            sys.exit(f"✗ falta {p}: corre el build del documento")
    return {"ver": ver, "caps": caps, "web": web, "pags": {l: paginas_pdf(p) for l, p in pdf.items()}}


def cita_url(doc_web, base_doc, titulo):
    """La página y el ancla de la sección que una cita nombra, buscadas en la edición web construida."""
    i = ref_id(titulo)
    for raiz, _, fs in os.walk(doc_web):
        if "index.html" in fs and f'id="{i}"' in open(os.path.join(raiz, "index.html"), encoding="utf-8").read():
            rel = os.path.relpath(raiz, doc_web)
            return f"{base_doc}/" + ("" if rel == "." else f"{rel}/") + f"#{i}"
    sys.exit(f"✗ la cita «{titulo}» no nombra ninguna sección de {doc_web}")


def main(vdir, dist):
    docs = json.load(open(os.path.join(vdir, "sitio", "documentos.json"), encoding="utf-8"))["documentos"]
    lib = json.load(open(os.path.join(vdir, "sitio", "biblioteca.json"), encoding="utf-8"))["temas"]
    for L in ("es", "en"):
        u, r = UI[L], RUTA[L]
        out = os.path.join(dist, f"web-{L}")
        shutil.rmtree(out, ignore_errors=True)
        os.makedirs(out)
        info = {d["id"]: documento(vdir, d, L) for d in docs}

        # 1. Qué es Vergis
        frag = open(os.path.join(vdir, "sitio", f"vergis.{L}.html"), encoding="utf-8").read()
        open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(
            pagina(L, "home", u["home_title"], u["home_desc"], frag, crumb_home=True))

        # 2. La colección
        bloques = []
        for n, d in enumerate(docs, 1):
            i, t = info[d["id"]], d[L]
            base_doc = f"{r['base']}/{d['id']}"
            caps = "".join(f'<li><a href="{base_doc}/{slugify(c)}/">{inline(c)}</a></li>' for c in i["caps"])
            otra = OTRA[L]
            base_otra = f"{RUTA[otra]['base']}/{d['id']}"
            bloques.append(
                f'<article class="vg-doc">\n<p class="vg-n">{u["doc_n"].format(n=n)}</p>\n'
                f'<h2><a href="{base_doc}/">{d["titulo"]}</a></h2>\n<p class="vg-sub">{t["subtitulo"]}</p>\n'
                f'<p class="vg-meta">{t["autores"]} · {u["version"]} {i["ver"]} · GNU FDL v1.3</p>\n'
                f'<p>{t["resumen"]}</p>\n'
                f'<p class="vg-acc"><a class="vg-leer" href="{base_doc}/">{u["leer"]} →</a>'
                f'<a href="{base_doc}/{d["titulo"]}-v{i["ver"]}-{L}.pdf">{u["pdf"]} · {u["pags"].format(n=i["pags"][L])}</a>'
                f'<a href="{base_otra}/{d["titulo"]}-v{i["ver"]}-{otra}.pdf">{u["pdf_otra"]} · {u["pags_otra"].format(n=i["pags"][otra])}</a>'
                f'<a href="{base_doc}/{d["titulo"]}-v{i["ver"]}-{L}.md">{u["md"]}</a></p>\n'
                f'<details class="vg-caps" open><summary>{u["capitulos"]}</summary><ol>{caps}</ol></details>\n</article>')
            shutil.copytree(i["web"], os.path.join(out, d["id"]))
        cuerpo = (f'<p class="eyebrow">{u["docs_eyebrow"]}</p>\n<h1>{u["docs_title"]}</h1>\n<p class="deck">{u["docs_deck"]}</p>\n'
                  f'<p class="promise">{u["docs_intro"]}</p>\n' + "\n".join(bloques) +
                  f'\n<p class="vg-siguen">{u["siguen"]}</p>\n'
                  f'<div class="next"><a href="{r["lib"]}">{u["a_lib"]}</a><a href="https://github.com/gegolabs/vergis">{u["a_repo"]}</a></div>')
        dest = os.path.join(out, r["docs"][len(r["base"]) + 1:], "index.html")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(pagina(L, "docs", f'{u["docs_title"]} · AgencyDomains', u["docs_desc"], cuerpo, False))

        # 3. La biblioteca
        nombre = {d["id"]: d["titulo"] for d in docs}
        secciones, total = [], 0
        for tema in lib:
            items = []
            for f in tema["fuentes"]:
                t = f[L]
                links = f["enlaces"][L] if isinstance(f["enlaces"], dict) else f["enlaces"]
                tit = f'<a href="{links[0]}">{inline(t["titulo"])}</a>' if links else inline(t["titulo"])
                mas = ""
                if len(links) > 1:
                    mas = (f' <span class="vg-mas">· {u["tambien"]}: ' +
                           " · ".join(f'<a href="{x}">{corto(x)}</a>' for x in links[1:]) + "</span>")
                nota = f'<p class="vg-nota">{html.escape(f["nota"][L])}</p>' if "nota" in f else ""
                por_doc = {}
                for doc, sec in f["citas"][L]:
                    por_doc.setdefault(doc, []).append(
                        f'<a href="{cita_url(info[doc]["web"], r["base"] + "/" + doc, sec)}">{inline(sec)}</a>')
                citas = " ".join(f'<p class="vg-cita">{u["en_doc"].format(doc=nombre[doc])} {" · ".join(v)}</p>' for doc, v in por_doc.items())
                items.append(f'<li><p class="vg-t">{tit}{mas}</p><p class="vg-por">{t["por"]}</p>{nota}{citas}</li>')
                total += 1
            secciones.append(f'<h2 id="{tema["id"]}">{tema[L]}</h2>\n<ul class="vg-refs">{"".join(items)}</ul>')
        cuerpo = (f'<p class="eyebrow">{u["docs_eyebrow"]}</p>\n<h1>{u["lib_h1"]}</h1>\n<p class="deck">{u["lib_deck"]}</p>\n'
                  f'<p class="promise">{u["lib_intro"]}</p>\n'
                  f'<nav class="vg-temas">' + " · ".join(f'<a href="#{t["id"]}">{t[L]}</a>' for t in lib) + '</nav>\n' +
                  "\n".join(secciones) +
                  f'\n<div class="next"><a href="{r["docs"]}">{u["a_docs"]}</a><a href="https://github.com/gegolabs/vergis">{u["a_repo"]}</a></div>')
        dest = os.path.join(out, r["lib"][len(r["base"]) + 1:], "index.html")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(pagina(L, "lib", f'{u["lib_title"]} · AgencyDomains', u["lib_desc"], cuerpo, False))
        print(f"  ✓ Vergis ({L}) → {out}: portada · colección ({len(docs)} documento(s)) · biblioteca ({len(lib)} temas, {total} fuentes)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:3])
