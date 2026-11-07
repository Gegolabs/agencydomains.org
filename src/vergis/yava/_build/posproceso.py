#!/usr/bin/env python3
"""Posproceso del .tex de Yava: las tablas cortas no se rompen; las otras se cortan con cabecera repetida.

pandoc escribe cada tabla como longtable, que repite la cabecera (\\endhead) cuando se corta.
Las cortas (hasta ~20 líneas estimadas) no se cortan: cada fin de fila del cuerpo pasa a \\\\* (longtable
no corta la página en un \\\\*) y la tabla entera va a la página siguiente si no cabe donde cae. Las
medianas y largas sí se cortan, con su cabecera repetida, pero nunca dejan solas menos de 3 filas al
empezar ni menos de 2 al terminar: así una tabla alta no deja en blanco el resto de una página (el
tercio bajo la figura 8) y tampoco deja una fila huérfana.
Uso: posproceso.py yava.tex
"""
import math
import re
import sys

LINEAS_MAX = 16          # hasta aquí una tabla no se corta; más alta, se corta con cabecera repetida
FILAS_INICIO, FILAS_FIN = 2, 2  # filas mínimas juntas al empezar y al terminar una tabla que se corta
CHARS_POR_ANCHO = 110    # caracteres \small (STIX Two, 10 pt) en el ancho completo de la caja (16,6 cm); medido en la pág. 38: ~45 en una columna de 0,31

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
    alto = []
    for r in rows:
        cells = r.split("&")
        n = 1
        for j, c in enumerate(cells):
            share = shares[j] if j < len(shares) else 1 / max(len(cells), 1)
            n = max(n, math.ceil(len(plano(c)) / max(share * CHARS_POR_ANCHO, 8)))
        total += n + 0.3
        alto.append(n + 0.3)
    hdr = head.split("\\endfirsthead")[0]
    total += 2
    if total <= LINEAS_MAX:
        body_main = re.sub(r"\\\\(?!\*)", r"\\\\*", body_main)
        procesa.cortas += 1
        # entera o en la página siguiente: así longtable no empieza una tabla que no puede cortar
        return f"\\needspace{{{math.ceil(total * 1.1)}\\baselineskip}}\n" + head + "\\endlastfoot" + body_main + "\\end{longtable}" + end
    else:
        # sin corte antes de FILAS_INICIO filas ni dejando menos de FILAS_FIN al final: se protegen
        # los fines de fila 0 … FILAS_INICIO-2 y n-FILAS_FIN … n-1 (el corte cae después del fin k)
        fines = [m for m in re.finditer(r"\\\\(?!\*)", body_main)]
        n = len(fines)
        prot = set(range(min(FILAS_INICIO - 1, n))) | set(range(max(n - FILAS_FIN, 0), n))
        for k in sorted(prot, reverse=True):
            m = fines[k]
            body_main = body_main[:m.start()] + "\\\\*" + body_main[m.end():]
        procesa.largas.append(round(total))
        # que empiece solo si caben la cabecera y sus primeras filas: si no, empieza en la página siguiente
        # (si longtable corta justo después de la cabecera, la repite dos veces en la página nueva)
        minimo = math.ceil(3 + sum(alto[:FILAS_INICIO]))
        return f"\\needspace{{{minimo}\\baselineskip}}\n" + head + "\\endlastfoot" + body_main + "\\end{longtable}" + end
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
print(f"posproceso: {procesa.cortas} tablas que no se cortan · {len(procesa.largas)} que se cortan con cabecera repetida (líneas estimadas: {procesa.largas})")
