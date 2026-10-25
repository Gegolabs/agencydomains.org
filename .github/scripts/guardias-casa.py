#!/usr/bin/env python3
"""Guardias de la casa sobre el sitio YA ENSAMBLADO (fallan el build).

  1 · raíz    todo enlace absoluto a la raíz (href="/…", src="/…") y toda URL del
              propio sitio empiezan por la base de la casa. Con la casa en una ruta,
              un "/x" pelado apuntaría a la raíz de otro sitio.
  2 · puerta  la dirección de la puerta (agencydomains.org, en minúsculas) no
              aparece en lo publicado salvo como el repositorio
              (github.com/gegolabs/agencydomains.org), que no cambia de nombre. Solo
              rige cuando la casa no es la puerta.
  3 · hreflang  cada página HTML (salvo 404) lleva su canonical a sí misma y
              hreflang en · es · x-default (= en); cada uno apunta a una página que
              existe en el sitio, la página se nombra a sí misma con su <html lang>,
              y el par es recíproco.

Una guardia que no aplica a la casa dada lo dice («no rige»), no pasa en silencio.
Sale con 0 si todo calza y 1 si algo falla.
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import casa

c = casa.cargar()
SITE, BASE = c['sitio'], c['base']
ROOT = sys.argv[1] if len(sys.argv) > 1 else '_site'
TEXTO = ('.html', '.md', '.txt', '.xml')
REPO = 'github.com/gegolabs/agencydomains.org'

fallas = []


def falla(guardia, msg):
    fallas.append(f'{guardia}: {msg}')


def archivos(exts):
    for d, dirs, fs in os.walk(ROOT):
        dirs[:] = [x for x in dirs if not x.startswith('.')]
        for f in sorted(fs):
            if f.endswith(exts):
                p = os.path.join(d, f)
                yield '/' + os.path.relpath(p, ROOT).replace(os.sep, '/'), p


def leer(p):
    return open(p, encoding='utf-8').read()


# 1 · raíz ------------------------------------------------------------------
def raiz():
    pre = BASE + '/'
    n = 0
    for rel, p in archivos(('.html',)):
        for m in re.finditer(r'\b(?:href|src|action|content)="(/[^"]*)"', leer(p)):
            n += 1
            if not m.group(1).startswith(pre):
                falla('raíz', f'{rel} enlaza {m.group(1)} fuera de {pre}')
    for rel, p in archivos(TEXTO):
        for m in re.finditer(re.escape(SITE) + r'(/[^\s"\'<>)\]]*)?', leer(p)):
            n += 1
            if not (m.group(1) or '/').startswith(pre):
                falla('raíz', f'{rel} enlaza {m.group(0)} fuera de {SITE}{pre}')
    nota = ' (base vacía: todo enlace raíz calza; rige con la casa en una ruta)' if not BASE else ''
    print(f'  guardia raíz: {n} enlaces revisados{nota}')


# 2 · puerta ----------------------------------------------------------------
def puerta():
    viejo = casa.host(c['puerta'])
    if viejo == casa.host(SITE):
        print(f'  guardia puerta: no rige (la casa es la puerta, {viejo})')
        return
    # La dirección se escribe en minúsculas (con o sin esquema y www.). «AgencyDomains.org»
    # con mayúsculas es otra cosa: el nombre propio del catálogo público en el Libro III,
    # que no es un enlace y no se muda con la casa.
    pat = re.compile(r'(?<![\w-])' + re.escape(viejo))
    n = 0
    for rel, p in archivos(TEXTO):
        for ln, linea in enumerate(leer(p).splitlines(), 1):
            for m in pat.finditer(linea):
                if linea[max(0, m.start() - len(REPO) + len(viejo)):m.end()] == REPO:
                    continue
                n += 1
                falla('puerta', f'{rel}:{ln} nombra {viejo}: {linea.strip()[:120]}')
    print(f'  guardia puerta: {n} menciones de {viejo} fuera de {REPO}')


# 3 · hreflang --------------------------------------------------------------
LINK = re.compile(r'<link rel="(canonical|alternate)"(?: hreflang="([a-z-]+)")? href="([^"]+)">')


def url_de(rel):
    """/es/aura/index.html → https://sitio/base/es/aura/"""
    return SITE + BASE + rel[:-len('index.html')]


def hreflang():
    paginas = {}
    for rel, p in archivos(('.html',)):
        if rel == '/404.html':
            continue
        h = leer(p)
        links = LINK.findall(h)
        lang = re.search(r'<html lang="([a-z]+)"', h)
        paginas[url_de(rel)] = {
            'rel': rel,
            'lang': lang.group(1) if lang else None,
            'canon': [u for k, _, u in links if k == 'canonical'],
            'alt': {hl: u for k, hl, u in links if k == 'alternate' and hl},
        }
    for url, pg in paginas.items():
        rel, alt = pg['rel'], pg['alt']
        if pg['canon'] != [url]:
            falla('hreflang', f'{rel}: canonical {pg["canon"]} en vez de [{url}]')
        falta = [k for k in ('en', 'es', 'x-default') if k not in alt]
        if falta:
            falla('hreflang', f'{rel}: le falta hreflang {", ".join(falta)}'); continue
        for k, u in alt.items():
            if u not in paginas:
                falla('hreflang', f'{rel}: hreflang {k} → {u}, que no es una página del sitio')
        if alt['x-default'] != alt['en']:
            falla('hreflang', f'{rel}: x-default ({alt["x-default"]}) no es la edición en')
        if alt.get(pg['lang']) != url:
            falla('hreflang', f'{rel}: su hreflang {pg["lang"]} no la nombra a ella')
        for k in ('en', 'es'):
            otra = paginas.get(alt[k])
            if otra and otra['alt'].get(pg['lang']) != url:
                falla('hreflang', f'{rel}: {alt[k]} no le devuelve el par ({pg["lang"]})')
    print(f'  guardia hreflang: {len(paginas)} páginas revisadas')


if __name__ == '__main__':
    if not os.path.isdir(ROOT):
        sys.exit(f'guardias-casa: no existe {ROOT}')
    raiz(); puerta(); hreflang()
    for x in fallas:
        print(f'::error::{x}')
    if fallas:
        print(f'guardias-casa: {len(fallas)} fallas')
        sys.exit(1)
    print('guardias-casa: todo calza')
