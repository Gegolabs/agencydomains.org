#!/usr/bin/env python3
"""Posproceso del .tex de Yava: las tablas que caben en una página no se rompen.

pandoc escribe cada tabla como longtable, que repite la cabecera (\\endhead) cuando se corta.
Para las que caben en una página, se cambia cada fin de fila del cuerpo por \\\\* (longtable no corta
la página en un \\\\*): la tabla entera pasa a la página siguiente si no cabe donde cae. Las largas
(más de ~38 líneas estimadas) se dejan cortar, con su cabecera repetida.
Uso: posproceso.py yava.tex
"""
import math
import re
import sys

LINEAS_MAX = 38          # líneas de texto \small que caben con holgura en la caja de una página
CHARS_POR_ANCHO = 330    # caracteres \small en el ancho completo de la caja (16,6 cm)

p = sys.argv[1]
t = open(p, encoding="utf-8").read()


def plano(s):
    s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", "", s)
    return re.sub(r"[{}\\]", "", s).strip()


def procesa(m):
    env = m.group(0)
    shares = [float(x) for x in re.findall(r"\\real\{([0-9.]+)\}", env)]
    if "\\endlastfoot" not in env:
        return env
    head, body = env.split("\\endlastfoot", 1)
    body_main, end = body.rsplit("\\end{longtable}", 1)
    rows = [r for r in re.split(r"\\\\(?:\s*\\noalign\{\})?", body_main) if plano(r)]
    total = 0
    for r in rows:
        cells = r.split("&")
        n = 1
        for j, c in enumerate(cells):
            share = shares[j] if j < len(shares) else 1 / max(len(cells), 1)
            n = max(n, math.ceil(len(plano(c)) / max(share * CHARS_POR_ANCHO, 8)))
        total += n + 0.3
    hdr = head.split("\\endfirsthead")[0]
    total += 2
    if total <= LINEAS_MAX:
        body_main = re.sub(r"\\\\(?!\*)", r"\\\\*", body_main)
        procesa.cortas += 1
    else:
        procesa.largas.append(round(total))
    return head + "\\endlastfoot" + body_main + "\\end{longtable}" + end


def corta_codigo(m):
    s = m.group(1)
    if len(s) < 30:
        return m.group(0)
    return "\\texttt{" + re.sub(r"([.|>])", r"\1\\allowbreak{}", s) + "}"


t = re.sub(r"\\texttt\{((?:[^{}]|\{[^{}]*\})*)\}", corta_codigo, t)

procesa.cortas = 0
procesa.largas = []
t = re.sub(r"\\begin\{longtable\}.*?\\end\{longtable\}", procesa, t, flags=re.S)
open(p, "w", encoding="utf-8").write(t)
print(f"posproceso: {procesa.cortas} tablas que no se rompen · {len(procesa.largas)} largas que se cortan con cabecera repetida (líneas estimadas: {procesa.largas})")
