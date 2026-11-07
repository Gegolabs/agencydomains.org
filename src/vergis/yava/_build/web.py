#!/usr/bin/env python3
"""La edición web de Yava: el Markdown que lee web-build.py (una página por capítulo) y el arreglo
de los enlaces entre páginas.

Uso:
  web.py md     <es|en> <yava.md> <salida.md> <version>   → el Markdown de la edición web
  web.py enlaces <dir_web> <base>                        → los enlaces #ref-… que apuntan a otra página
                                                            pasan a <base>/<capítulo>/#ref-…

El Markdown de la web:
  · la portada (el primer «# ») lleva el título, la ficha, cómo citar, los capítulos y las descargas;
  · cada capítulo (##) pasa a «# », y así a una página propia; sus secciones (###) pasan a «## » y
    forman el sub-índice de la página; el Anexo A y las fuentes son páginas al final;
  · las figuras llevan su pie como leyenda (figcaption);
  · las referencias cruzadas se enlazan al título que nombran (referencias.py).
"""
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from referencias import enlaza_referencias  # noqa: E402

T = {
    "es": {
        "subtitulo": "Arquitectura de lo determinista del AgencyDomain",
        "autores": "César Obach-Renner y Simón Alero",
        "serie": "Vergis · Tecnología Agentiva · A",
        "editor": "Editor",
        "cite": "Cómo citar",
        "cite_txt": "Obach-Renner, César y Simón Alero. *Yava: arquitectura de lo determinista del AgencyDomain*. Versión {v}. Gegolabs, 2026.",
        "ficha": "Ficha",
        "capitulos": "Capítulos",
        "descargas": "Descargas",
        "pdf": "PDF en español",
        "md": "Markdown en español",
        "otra": "English edition",
        "otra_url": "/vergis/yava/",
        "base": "/es/vergis/yava",
        "coleccion": "La colección de documentos de Vergis",
        "coleccion_url": "/es/vergis/documentos/",
    },
    "en": {
        "subtitulo": "Architecture of the deterministic part of the AgencyDomain",
        "autores": "César Obach-Renner and Simón Alero",
        "serie": "Vergis · Agentive Technology · A",
        "editor": "Publisher",
        "cite": "How to cite",
        "cite_txt": "Obach-Renner, César and Simón Alero. *Yava: Architecture of the deterministic part of the AgencyDomain*. Version {v}. Gegolabs, 2026.",
        "ficha": "Record",
        "capitulos": "Chapters",
        "descargas": "Downloads",
        "pdf": "PDF in English",
        "md": "Markdown in English",
        "otra": "Edición en español",
        "otra_url": "/es/vergis/yava/",
        "base": "/vergis/yava",
        "coleccion": "The Vergis document collection",
        "coleccion_url": "/vergis/documents/",
    },
}


def slugify(t):  # la misma de web-build.py: el enlace de la portada nace igual que la ruta de la página
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()


def web_md(L, src, out, version):
    t = T[L]
    v = version.lstrip("v")
    lines = open(src, encoding="utf-8").read().split("\n")
    first = next(i for i, l in enumerate(lines) if l.startswith("## "))
    head, body = lines[:first], lines[first:]

    # la ficha, con el editor después de los autores (como en el PDF)
    ficha = [l for l in head if l.startswith("|")]
    k = next(i for i, r in enumerate(ficha) if r.startswith("| **Aut"))
    ficha.insert(k + 1, f"| **{t['editor']}** | Gegolabs |")
    ficha[0] = "| | |"

    # el cuerpo: cada título sube un nivel (fuera de los bloques de código); sin separadores
    out_body, fence = [], False
    for l in body:
        if l.startswith("```"):
            fence = not fence
        if not fence and re.match(r"^#{2,6} ", l):
            l = l[1:]
        if not fence and l.strip() == "---":
            continue
        out_body.append(l)
    b = "\n".join(out_body)

    # figuras: la imagen con su pie como leyenda
    b, nfig = re.subn(r"!\[[^\]]*\]\((figuras/[^)]+)\)\n\n\*([^\n]+)\*", r"![\2](\1)", b)
    assert nfig == 9, nfig
    # las URL sueltas de las fuentes, como enlaces
    b = re.sub(r"(?<!\]\()(?<!<)(https?://[^\s)]+?)([.,;]?)(?=[\s)]|$)", r"<\1>\2", b)
    b, nref = enlaza_referencias(b, L, nivel_min=2)

    caps = [l[2:].strip() for l in b.split("\n") if l.startswith("# ")]
    lista = "\n".join(f"{i}. [{c}]({t['base']}/{slugify(c)}/)" for i, c in enumerate(caps[:8], 1))
    extra = "\n".join(f"- [{c}]({t['base']}/{slugify(c)}/)" for c in caps[8:])
    portada = f"""# Yava

*{t['subtitulo']}*

{t['autores']} · {t['serie']}

## {t['capitulos']}

{lista}

{extra}

## {t['descargas']}

- [{t['pdf']}]({t['base']}/Yava-{version}-{L}.pdf) · [{t['md']}]({t['base']}/Yava-{version}-{L}.md)
- [{t['otra']}]({t['otra_url']})
- [{t['coleccion']}]({t['coleccion_url']})

## {t['ficha']}

{chr(10).join(ficha)}

**{t['cite']}:** {t['cite_txt'].format(v=v)}

"""
    open(out, "w", encoding="utf-8").write(portada + b.rstrip() + "\n")
    print(f"  web {L}: {len(caps)} páginas de capítulo · {nfig} figuras · {nref} referencias enlazadas")


def enlaces(d, base):
    """Un #ref-… que no está en la página que lo cita apunta a la página que lo tiene."""
    paginas = {}
    for raiz, _, fs in os.walk(d):
        for f in fs:
            if f == "index.html":
                p = os.path.join(raiz, f)
                rel = os.path.relpath(raiz, d)
                url = f"{base}/" if rel == "." else f"{base}/{rel}/"
                paginas[p] = (url, open(p, encoding="utf-8").read())
    donde = {}
    for p, (url, html) in paginas.items():
        for i in re.findall(r'\bid="(ref-[^"]+)"', html):
            donde[i] = url
    n, rotos = 0, []
    for p, (url, html) in paginas.items():
        def sub(m):
            nonlocal n
            i = m.group(1)
            if i not in donde:
                rotos.append(i)
                return m.group(0)
            if donde[i] == url:
                return m.group(0)
            n += 1
            return f'href="{donde[i]}#{i}"'
        nuevo = re.sub(r'href="#(ref-[^"]+)"', sub, html)
        if nuevo != html:
            open(p, "w", encoding="utf-8").write(nuevo)
    if rotos:
        sys.exit("✗ enlaces a títulos que no están en ninguna página: " + " · ".join(sorted(set(rotos))))
    print(f"  enlaces entre páginas: {n} (y ningún #ref- sin destino)")


if __name__ == "__main__":
    if sys.argv[1] == "md":
        web_md(*sys.argv[2:6])
    elif sys.argv[1] == "enlaces":
        enlaces(*sys.argv[2:4])
    else:
        sys.exit(__doc__)
