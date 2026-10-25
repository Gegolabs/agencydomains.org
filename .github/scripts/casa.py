#!/usr/bin/env python3
"""La casa del sitio: dónde se sirve la trilogía, leído de casa.json (raíz del repo).

Es la ÚNICA fuente de la dirección. web-build.py, gen-vocabulario.py,
gen-sitemap.py, gen-hreflang.py, las guardias, el ensamblado del shell y el
despliegue la leen de aquí; ninguno cablea un dominio ni una ruta. Mudar el sitio
es cambiar casa.json, no el código (diseño de la casa en soveria.ai v0.2, F1a).

  sitio         origen canónico, sin barra final        https://agencydomains.org
  base          ruta del fondo bajo el sitio, "" o "/x"  (vacía: el sitio en la raíz)
  puerta        dominio viejo que redirige a la casa     (= sitio mientras no haya mudanza)
  bucket · distribucion · router · rol    a dónde publica el workflow
  patrocinio.nivel                        hoy solo «puerta» (sin mención de Soveria)

CASA=<ruta> sustituye casa.json (builds de prueba contra otra casa).

Uso como script:  casa.py <clave>   → imprime el valor
                  casa.py env       → CASA_<CLAVE>=valor, una por línea (para $GITHUB_ENV)
"""
import json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLAVES = ('sitio', 'base', 'puerta', 'bucket', 'distribucion', 'router', 'rol')
# Lo que el build sabe pintar. Subir de nivel exige implementarlo antes: un nivel
# que el build no conoce publicaría en silencio como si fuera «puerta».
NIVELES = ('puerta',)


def cargar(ruta=None):
    ruta = ruta or os.environ.get('CASA') or os.path.join(REPO, 'casa.json')
    with open(ruta, encoding='utf-8') as fh:
        c = json.load(fh)
    falta = [k for k in CLAVES if k not in c]
    if falta:
        sys.exit(f'casa: {ruta} no trae {", ".join(falta)}')
    for k in ('sitio', 'puerta'):
        if not re.fullmatch(r'https://[a-z0-9.-]+', c[k]):
            sys.exit(f'casa: «{k}» debe ser https://<host>, sin ruta ni barra final (es {c[k]!r})')
    if c['base'] and not re.fullmatch(r'(/[a-z0-9][a-z0-9-]*)+', c['base']):
        sys.exit(f'casa: «base» debe ser "" o /a/b, sin barra final (es {c["base"]!r})')
    nivel = (c.get('patrocinio') or {}).get('nivel', 'puerta')
    if nivel not in NIVELES:
        sys.exit(f'casa: el patrocinio «{nivel}» aún no está implementado en el build ({", ".join(NIVELES)})')
    return c


def host(url):
    return url.split('://', 1)[1]


if __name__ == '__main__':
    c = cargar()
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    if sys.argv[1] == 'env':
        for k in CLAVES:
            print(f'CASA_{k.upper()}={c[k]}')
    elif sys.argv[1] in CLAVES:
        print(c[sys.argv[1]])
    else:
        sys.exit(f'casa: clave desconocida {sys.argv[1]!r}')
