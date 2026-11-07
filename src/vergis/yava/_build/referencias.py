"""Referencias cruzadas de Yava, para el libro en PDF (prepara.py) y la edición web (web.py).

El texto cita sus secciones por el título entre comillas: «¿Qué es un Conector?» en español,
“What is a Connector?” en inglés. Cada título recibe un id estable (ref-<título en ASCII>) y cada
cita de un título se vuelve un enlace a ese id. Toda cita entrecomillada que termina en «?» tiene que
nombrar un título del documento, salvo las preguntas que el texto cita como preguntas y no como títulos
(NO_SON_TITULOS); si no, es una referencia rota y detiene el build.
"""
import re
import sys
import unicodedata

def ref_id(titulo):
    t = unicodedata.normalize("NFKD", titulo).encode("ascii", "ignore").decode()
    return "ref-" + re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()


COMILLAS = {"es": ("«", "»"), "en": ("\u201c", "\u201d")}

# Preguntas que el texto cita entre comillas sin que sean títulos: la lista blanca del detector.
NO_SON_TITULOS = {
    "es": {"¿puede este sujeto hacer esta operación sobre este Dominion?"},
    "en": {"may this subject perform this operation on this Dominion?"},
}


def enlaza_referencias(md, lang, nivel_min=2):
    """Da a cada título (de nivel_min a 5 almohadillas) un id estable y enlaza sus citas.
    Devuelve (md, n.º de enlaces)."""
    a, c = COMILLAS[lang]
    titulos = {}
    fence = False
    out = []
    for l in md.split("\n"):
        if l.startswith("```"):
            fence = not fence
        m = None if fence else re.match(r"^(#{%d,5}) (.+?)\s*$" % nivel_min, l)
        if m:
            titulos[m.group(2)] = ref_id(m.group(2))
            l = f"{m.group(1)} {m.group(2)} {{#{titulos[m.group(2)]}}}"
        out.append(l)
    md = "\n".join(out)
    rotas = []

    def sub(m):
        t = m.group(1)
        if t in titulos:
            return f"[{a}{t}{c}](#{titulos[t]})"
        if t.endswith("?") and t not in NO_SON_TITULOS[lang]:
            rotas.append(t)
        return m.group(0)

    lineas = md.split("\n")
    fence = False
    n = 0
    for i, l in enumerate(lineas):
        if l.startswith("```"):
            fence = not fence
            continue
        if fence or re.match(r"^#{1,6} ", l):
            continue
        nuevo = re.sub(re.escape(a) + r"([^" + re.escape(c) + r"]+)" + re.escape(c), sub, l)
        n += nuevo.count("](#ref-") - l.count("](#ref-")
        lineas[i] = nuevo
    if rotas:
        sys.exit("✗ referencias cruzadas que no nombran un título: " + " · ".join(sorted(set(rotas))))
    return "\n".join(lineas), n
