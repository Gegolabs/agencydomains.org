#!/usr/bin/env python3
"""Prepara el Markdown de Yava para el libro (pandoc + xelatex).

Uso: prepara.py <es|en> <yava.md> <dir_salida> <version>
Escribe en <dir_salida>:
  ficha-<L>.md   la ficha del documento (la tabla de cabecera) + cómo citar + contacto → página de créditos
  cuerpo-<L>.md  el cuerpo y el Anexo A, listo para pandoc:
                 · sin el título (va en la portada y la portadilla) ni la ficha;
                 · secciones (##) numeradas; el Anexo A y las fuentes, sin número y al índice;
                 · figuras: las de columna en su ancho, la 2 y la 5 como láminas apaisadas a página completa;
                 · tablas: anchos de columna según su contenido (pandoc los lee de los guiones de la separación).
  Yava-<version>-<L>.md  lo que se publica: la ficha, cómo citar y el cuerpo, en Markdown limpio (lo que se coteja).
"""
import re
import sys

L, SRC, OUT, VER = sys.argv[1:5]
VER_N = VER.lstrip("v")  # la cita lleva el número, sin la «v» del nombre del archivo
T = {
    "es": {
        "cite": "Cómo citar",
        "cite_txt": f"Obach-Renner, César y Simón Alero. *Yava: arquitectura de lo determinista del AgencyDomain*. Versión {VER_N}. Gegolabs, 2026.",
        "contacto": "Información de contacto",
        "contacto_txt": "Sitio web: agencydomains.org · Repositorio: github.com/gegolabs/agencydomains.org · Errata y comentarios: github.com/gegolabs/agencydomains.org/issues",
        "editor": "Editor",
        "annex": "Anexo A",
        "fuentes": "¿Qué fuentes se consultaron?",
        "fuentes_corto": "Fuentes",
    },
    "en": {
        "cite": "How to cite",
        "cite_txt": f"Obach-Renner, César and Simón Alero. *Yava: Architecture of the deterministic part of the AgencyDomain*. Version {VER_N}. Gegolabs, 2026.",
        "contacto": "Contact information",
        "contacto_txt": "Website: agencydomains.org · Repository: github.com/gegolabs/agencydomains.org · Errata and comments: github.com/gegolabs/agencydomains.org/issues",
        "editor": "Publisher",
        "annex": "Annex A",
        "fuentes": "What sources were consulted?",
        "fuentes_corto": "Sources",
    },
}[L]

src = open(SRC, encoding="utf-8").read()
lines = src.split("\n")

# 1. Título y ficha: todo lo anterior a la primera sección (##)
first = next(i for i, l in enumerate(lines) if l.startswith("## "))
head, body = lines[:first], lines[first:]
ficha = [l for l in head if l.startswith("|")]
ficha_md = "\n".join(ficha) + "\n"
# la ficha lleva al editor como una fila más, después de los autores
fila_editor = f"| **{T['editor']}** | Gegolabs |"
ficha_rows = ficha_md.strip().split("\n")
ficha_rows[1] = "|" + "-" * 22 + "|" + "-" * 78 + "|"  # etiquetas angostas, valores anchos
idx = next(i for i, r in enumerate(ficha_rows) if r.startswith("| **Aut"))
ficha_rows.insert(idx + 1, fila_editor)
ficha_md = "\n".join(ficha_rows) + "\n"
ficha_md += f"\n**{T['cite']}:** {T['cite_txt']}\n\n**{T['contacto']}:** {T['contacto_txt']}\n"
open(f"{OUT}/ficha-{L}.md", "w", encoding="utf-8").write(ficha_md)

body_md = "\n".join(body)

# 2. Lo publicado, en Markdown limpio: ficha + citar + cuerpo (sin los separadores de sección)
titulo = head[0]
publicado = titulo + "\n\n" + ficha_md + "\n" + re.sub(r"\n---\n", "\n", body_md)
open(f"{OUT}/Yava-{VER}-{L}.md", "w", encoding="utf-8").write(publicado.rstrip() + "\n")

# 3. Cuerpo para pandoc
b = body_md
b = re.sub(r"\n---\n", "\n", b)  # los separadores: la sección ya separa


def tex_escape_plain(s):
    return (s.replace("\\", r"\textbackslash{}").replace("&", r"\&").replace("%", r"\%")
            .replace("#", r"\#").replace("_", r"\_").replace("{", r"\{").replace("}", r"\}"))


# Anexo A y fuentes: sin número, al índice, con su marca de cabecera; sus subsecciones sin número
def heading_unnumbered(m):
    text = m.group(2)
    return f"{m.group(1)} {text} {{.unnumbered}}"


parts = re.split(r"(?m)^(?=## )", b)
out = []
in_annex = False
for p in parts:
    if not p.strip():
        continue
    h = p.split("\n", 1)[0]
    if h.startswith("## Anexo A") or h.startswith("## Annex A"):
        in_annex = True
        title = h[3:].strip()
        rest = p.split("\n", 1)[1]
        rest = re.sub(r"(?m)^(###+) (.+)$", heading_unnumbered, rest)
        out.append("```{=latex}\n\\clearpage\n\\phantomsection\n"
                   f"\\section*{{{tex_escape_plain(title)}}}\n"
                   f"\\addcontentsline{{toc}}{{section}}{{{tex_escape_plain(title)}}}\n"
                   f"\\markright{{{T['annex']}}}\n```\n" + rest)
        continue
    if h.startswith("## " + T["fuentes"]):
        rest = p.split("\n", 1)[1]
        out.append("```{=latex}\n\\phantomsection\n"
                   f"\\section*{{{tex_escape_plain(T['fuentes'])}}}\n"
                   f"\\addcontentsline{{toc}}{{section}}{{{tex_escape_plain(T['fuentes'])}}}\n"
                   f"\\markright{{{T['fuentes_corto']}}}\n```\n" + rest)
        continue
    out.append(p)
b = "".join(out)

# Figuras: imagen + párrafo de pie en cursiva → bloque LaTeX
FIG = re.compile(r"!\[([^\]]*)\]\((figuras/[^)]+)\)\n\n\*([^\n]+)\*")


def figura(m):
    path, cap = m.group(2), m.group(3)
    if "-2x" in path:  # lámina apaisada a página completa
        return ("```{=latex}\n\\begin{sidewaysfigure}\n\\centering\n"
                f"\\makebox[\\linewidth]{{\\includegraphics[width=\\linewidth,height=17cm,keepaspectratio]{{{path}}}}}\n"
                "\\par\\vspace{6pt}\\begin{minipage}{0.92\\linewidth}\\small\\itshape\\raggedright\n```\n\n"
                f"{cap}\n\n"
                "```{=latex}\n\\end{minipage}\n\\end{sidewaysfigure}\n```")
    return ("```{=latex}\n\\begin{figure}[htbp]\n\\centering\n"
            f"\\includegraphics[width=15cm,height=0.78\\textheight,keepaspectratio]{{{path}}}\n"
            "\\par\\vspace{6pt}\\begin{minipage}{15cm}\\small\\itshape\\raggedright\n```\n\n"
            f"{cap}\n\n"
            "```{=latex}\n\\end{minipage}\n\\end{figure}\n```")


b, nfig = FIG.subn(figura, b)
assert nfig == 9, nfig


# Tablas de tubos: anchos según el contenido (pandoc respeta la proporción de los guiones)
def anchos(block):
    rows = block.strip("\n").split("\n")
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    sep = 1
    ncol = len(cells[0])
    if any(len(c) != ncol for c in cells):
        return block  # una tabla con barras dentro de celdas: se deja como está
    w = []
    for j in range(ncol):
        lens = [len(re.sub(r"[*`]", "", c[j])) for k, c in enumerate(cells) if k != sep]
        avg = sum(lens) / len(lens)
        mx = max(lens)
        w.append(max(avg * 0.7 + mx * 0.3, 6))
    tot = sum(w)
    # ninguna columna más angosta que su palabra más larga (en negrita, \\small): ~5,6 pt por carácter sobre ~400 pt útiles
    palabra = [max((len(x) for k, c in enumerate(cells) if k != sep for x in re.sub(r"[*`]", "", c[j]).split()), default=4)
               for j in range(ncol)]
    share = [max(x / tot, 0.13 if ncol > 2 else 0.2, (palabra[j] * 5.6 + 10) / (400 - 12 * ncol)) for j, x in enumerate(w)]
    s2 = sum(share)
    dashes = [max(3, round(100 * x / s2)) for x in share]
    rows[sep] = "|" + "|".join("-" * d for d in dashes) + "|"
    return "\n".join(rows) + "\n"


b = re.sub(r"(?m)(^\|.*\|\n)+", lambda m: anchos(m.group(0)), b)

open(f"{OUT}/cuerpo-{L}.md", "w", encoding="utf-8").write(b)
print(f"prepara {L}: {nfig} figuras · cuerpo {len(b.split())} palabras")
