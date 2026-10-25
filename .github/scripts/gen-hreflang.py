#!/usr/bin/env python3
"""Pone hreflang (en · es · x-default → en) en cada página de los libros. Corre
sobre el sitio YA ENSAMBLADO, después de copiar los libros a sus rutas.

Cada edición se construye por separado (web-build.py, una corrida por idioma),
así que ninguna conoce las URLs de la otra; aquí ya están las dos. El par de una
página sale de su POSICIÓN en el índice del libro (la barra lateral, que lista
todas las páginas en orden): ES y EN se arman del mismo manifest y son espejo por
posición, y los slugs no lo son (cada uno sale de su título traducido).

Guardias (fallan el build): ES y EN con distinto número de páginas, o una página
del índice que no existe en el sitio — el par sería falso y Google lo descarta
entero si no es recíproco.

Las páginas del shell y el vocabulario ya traen su hreflang de origen.
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import casa

c = casa.cargar()
SITE, BASE = c['sitio'], c['base']
ROOT = sys.argv[1] if len(sys.argv) > 1 else '_site'

# (EN, ES) — las rutas del ensamblado (publish.yml), sin la base de la casa
LIBROS = [
    ('/real-time-enterprise', '/es/empresa-tiempo-real'),
    ('/aura', '/es/aura'),
    ('/agencydomains', '/es/agencydomains'),
]

CANON = re.compile(r'<link rel="canonical" href="[^"]+">\n')


def archivo(url):
    """URL de directorio con BASE → su index.html en el sitio ensamblado."""
    assert url.startswith(BASE + '/'), url
    return os.path.join(ROOT, url[len(BASE):].strip('/'), 'index.html')


def indice(ruta):
    """Las URLs de las páginas del libro, en orden, leídas de la barra lateral de su portada."""
    html = open(archivo(BASE + ruta + '/'), encoding='utf-8').read()
    nav = re.search(r'<nav class="book-nav".*?</nav>', html, re.S).group(0)
    return re.findall(r'<li(?: class="part")?><a class="[^"]*" href="([^"]+)">', nav)


def main():
    fallas, n = [], 0
    for en, es in LIBROS:
        p_en, p_es = indice(en), indice(es)
        if len(p_en) != len(p_es):
            fallas.append(f'{en} tiene {len(p_en)} páginas y {es} {len(p_es)}: no son espejo')
            continue
        for u_en, u_es in zip(p_en, p_es):
            links = (f'<link rel="alternate" hreflang="en" href="{SITE}{u_en}">\n'
                     f'<link rel="alternate" hreflang="es" href="{SITE}{u_es}">\n'
                     f'<link rel="alternate" hreflang="x-default" href="{SITE}{u_en}">\n')
            for u in (u_en, u_es):
                f = archivo(u)
                if not os.path.exists(f):
                    fallas.append(f'{u} está en el índice y no en el sitio'); continue
                html = open(f, encoding='utf-8').read()
                if 'hreflang=' in html:
                    fallas.append(f'{u} ya trae hreflang: no se duplica'); continue
                html, k = CANON.subn(lambda m: m.group(0) + links, html, count=1)
                if not k:
                    fallas.append(f'{u} no trae canonical'); continue
                open(f, 'w', encoding='utf-8').write(html)
                n += 1
    for x in fallas:
        print(f'::error::gen-hreflang: {x}')
    if fallas:
        sys.exit(1)
    print(f'  hreflang → {n} páginas de libro')


if __name__ == '__main__':
    main()
