#!/usr/bin/env python3
"""Genera la página de vocabulario canónico de la trilogía (ES + EN) desde los
glosarios de los libros. Corre sobre el sitio YA ENSAMBLADO, antes del sitemap.

La página NO define nada: es una vista derivada. Cada término tiene una sola
fuente de verdad —el glosario del libro que lo acuña— y aquí se lee tal cual,
con un ancla estable por término y el enlace de vuelta a su entrada de origen.
Escribirla a mano la desincronizaría a la primera edición nueva (es el defecto
por el que se descartó el «kit» suelto; ver NEXT.md del repo agencydomains-org).

Fuentes, por libro y por idioma (una función de parseo por sintaxis):
  · Libro I   — contenido/glosario.md · contenido-en/glosario.md
                entradas «**término** — definición *(dónde vive)*»
  · Libro II  — §9 del manifiesto para agentes (para-agentes.md · para-agents.md)
                lista «- **término** — definición». Es la única fuente canónica de
                vocabulario que AURA tiene hoy; cuando el libro incorpore su propio
                glosario, se cambia la fuente aquí y nada más.
  · Libro III — contenido/apendices/glosario.md · contenido-en/apendices/glosario.md
                entradas «### Término» + primer párrafo + «*Ver: …*»

Las anclas de origen salen del MISMO código que las produce en el libro-web
(web-build.py: ids de pandoc para «###», entry_anchors() para «**término** —»),
así que el enlace no puede apuntar a un ancla que no exista.

Guardias (fallan el build):
  · paridad ES/EN por libro: mismo número de entradas, o no se publica;
  · ninguna fuente vacía.

Salida: <root>/vocabulary/index.html · <root>/es/vocabulario/index.html, cada una
con su gemelo Markdown para agentes (vocabulary.md · vocabulario.md) y JSON-LD
(schema.org DefinedTermSet) inline.
"""
import html as H
import json
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else '_site'
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(REPO, 'src', 'agencydomains', '_build'))
import importlib
wb = importlib.import_module('web-build')          # slugify · pandoc · strip_tags · entry_anchors
SITE = wb.SITE


def ver(book):
    with open(os.path.join(REPO, 'src', book, 'CHANGELOG.md'), encoding='utf-8') as fh:
        m = re.search(r'^## (v\d+\.\d+(?:\.\d+)?)', fh.read(), re.M)
    return m.group(1)


# ---------------------------------------------------------------- fuentes ---
# Cada libro: título por idioma, base URL por idioma, y (archivo fuente, parser,
# cómo se enlaza la entrada de origen) por idioma.
BOOKS = [
    {
        'key': 'rte', 'num': 'I',
        'title': {'es': 'La Empresa en Tiempo Real', 'en': 'The Real-Time Enterprise'},
        'base':  {'es': '/es/empresa-tiempo-real', 'en': '/real-time-enterprise'},
        'src':   {'es': 'src/rte/contenido/glosario.md', 'en': 'src/rte/contenido-en/glosario.md'},
        'kind': 'entries',
        'src_label': {'es': 'Glosario', 'en': 'Glossary'},
    },
    {
        'key': 'aura', 'num': 'II',
        'title': {'es': 'AURA', 'en': 'AURA'},
        'base':  {'es': '/es/aura', 'en': '/aura'},
        'src':   {'es': 'src/aura/para-agentes.md', 'en': 'src/aura/para-agents.md'},
        'kind': 'manifest',
        'section': {'es': r'^## 9 · Glosario canónico', 'en': r'^## 9 · Canonical glossary'},
        'link': {'es': '/es/AURA-agents-es.md', 'en': '/AURA-agents-en.md'},
        'src_label': {'es': 'Manifiesto canónico §9', 'en': 'Canonical manifest §9'},
    },
    {
        'key': 'agencydomains', 'num': 'III',
        'title': {'es': 'AgencyDomains', 'en': 'AgencyDomains'},
        'base':  {'es': '/es/agencydomains', 'en': '/agencydomains'},
        'src':   {'es': 'src/agencydomains/contenido/apendices/glosario.md',
                  'en': 'src/agencydomains/contenido-en/apendices/glosario.md'},
        'kind': 'headings',
        'src_label': {'es': 'Apéndice A', 'en': 'Appendix A'},
    },
]

UI = {
    'es': {
        'lang': 'es', 'path': '/es/vocabulario/', 'alt': '/vocabulary/', 'md': 'vocabulario.md',
        'eyebrow': 'El vocabulario · un término, una definición, un ancla',
        'h1': 'Vocabulario canónico del Mundo Agentivo',
        'deck': 'Los términos de la trilogía, en una línea cada uno, tal como los define el libro que los acuña.',
        'intro': ('Esta página no define nada: <strong>cada entrada se lee del glosario de su libro</strong> y '
                  'enlaza a él. Por eso se puede citar con confianza — la definición que ves aquí es la '
                  'misma que está en la obra, y el ancla de cada término (<code>#linea-nadella</code>) es '
                  'estable: sirve para enlazar desde cualquier parte.'),
        'cite': 'Para citar', 'cite_txt': 'copia el enlace del término; lleva a esta definición y, desde ella, a su capítulo.',
        'source': 'fuente', 'in_book': 'Libro', 'also': 'también en',
        'md_title': 'Vocabulario canónico del Mundo Agentivo',
        'md_intro': ('Un término por línea, con su definición tal como la da el libro que lo acuña y el enlace '
                     'a la entrada de origen. Generado desde los glosarios de la trilogía en cada publicación.'),
        'crumb_home': '← agencydomains.org', 'foot': 'César Obach-Renner · La Trilogía del Mundo Agentivo',
        'next': [('Para agentes ·', 'este vocabulario en Markdown →', '/es/vocabulario/vocabulario.md'),
                 ('La puerta para agentes ·', 'llms.txt →', '/es/llms.txt'),
                 ('La trilogía completa ·', 'agencydomains.org →', '/es/')],
        'editions': 'Ediciones',
    },
    'en': {
        'lang': 'en', 'path': '/vocabulary/', 'alt': '/es/vocabulario/', 'md': 'vocabulary.md',
        'eyebrow': 'The vocabulary · one term, one definition, one anchor',
        'h1': 'Canonical vocabulary of the Agentive World',
        'deck': 'The terms of the trilogy, one line each, exactly as defined by the book that coins them.',
        'intro': ('This page defines nothing: <strong>each entry is read from the glossary of its book</strong> '
                  'and links back to it. That is why it can be cited with confidence — the definition you see '
                  'here is the one in the work, and each term’s anchor (<code>#nadella-line</code>) is stable: '
                  'use it to link from anywhere.'),
        'cite': 'To cite', 'cite_txt': 'copy the term’s link; it leads to this definition and, from it, to its chapter.',
        'source': 'source', 'in_book': 'Book', 'also': 'also in',
        'md_title': 'Canonical vocabulary of the Agentive World',
        'md_intro': ('One term per line, with its definition exactly as given by the book that coins it and the '
                     'link to the source entry. Generated from the trilogy’s glossaries on every publication.'),
        'crumb_home': '← agencydomains.org', 'foot': 'César Obach-Renner · The Agentive World Trilogy',
        'next': [('For agents ·', 'this vocabulary as Markdown →', '/vocabulary/vocabulary.md'),
                 ('The door for agents ·', 'llms.txt →', '/llms.txt'),
                 ('The full trilogy ·', 'agencydomains.org →', '/')],
        'editions': 'Editions',
    },
}

FONTS = wb.FONTS


# ---------------------------------------------------------------- parseo ----
def _inline(s):
    """Deja solo el marcado inline inocuo (strong/em/code) — sin enlaces ni bloques."""
    s = re.sub(r'<a\b[^>]*>(.*?)</a>', r'\1', s, flags=re.S)
    s = re.sub(r'</?(?!strong\b|em\b|code\b)[a-zA-Z][^>]*>', '', s)
    return re.sub(r'\s+', ' ', s).strip()     # pandoc parte las líneas a 72 columnas


def parse_entries(html):
    """«**término** — definición *(dónde vive)*» ya con id (entry_anchors)."""
    out = []
    for m in re.finditer(r'<p id="([^"]+)" class="entry"><strong>(.+?)</strong>\s*(?:—|&#8212;)\s*(.*?)</p>', html, re.S):
        sid, term, rest = m.group(1), m.group(2), m.group(3)
        rest = re.sub(r'\s*<em>\((.*?)\)</em>\s*$', '', rest, flags=re.S)   # quita el *(ref)* final
        out.append({'id': sid, 'term': _inline(term), 'def': _inline(rest)})
    return out


def parse_headings(html):
    """«### Término» + primer párrafo. Los «## A» (letras) no son entradas."""
    out = []
    for m in re.finditer(r'<h3 id="([^"]+)">(.*?)</h3>\s*(?:<p>(.*?)</p>)?', html, re.S):
        sid, term, para = m.group(1), m.group(2), m.group(3) or ''
        out.append({'id': sid, 'term': _inline(term), 'def': _inline(para)})
    return out


def parse_manifest(md, section_re):
    """Lista «- **término** — definición» bajo el heading indicado, hasta el próximo «## »."""
    m = re.search(section_re + r'.*?$(.*?)(?=^## |\Z)', md, re.S | re.M)
    if not m:
        sys.exit('gen-vocabulario: no encontré la sección %r' % section_re)
    html = wb.pandoc(m.group(1))
    out = []
    for li in re.finditer(r'<li>(.*?)</li>', html, re.S):
        mm = re.match(r'\s*<strong>(.+?)</strong>\s*(?:—|&#8212;)\s*(.*)$', li.group(1), re.S)
        if mm:
            out.append({'id': None, 'term': _inline(mm.group(1)), 'def': _inline(mm.group(2))})
    return out


def load(book, lang):
    path = os.path.join(REPO, book['src'][lang])
    md = open(path, encoding='utf-8').read()
    if book['kind'] == 'manifest':
        entries = parse_manifest(md, book['section'][lang])
        href = book['link'][lang]
        for e in entries:
            e['src'] = href
    else:
        html = wb.entry_anchors(wb.pandoc(md))
        entries = parse_entries(html) if book['kind'] == 'entries' else parse_headings(html)
        h1 = re.search(r'^# (.+)$', md, re.M).group(1)
        page = f"{book['base'][lang]}/{wb.slugify(wb.strip_tags(h1))}/"   # misma regla que web-build.py
        for e in entries:
            e['src'] = f"{page}#{e['id']}"
    if not entries:
        sys.exit('gen-vocabulario: %s no aportó ninguna entrada' % path)
    return entries


# ---------------------------------------------------------------- render ----
def assign_anchors(books_entries):
    """El primer libro que acuña un término se lleva el ancla pelada; una repetición
    posterior (p. ej. «Línea Nadella» en I y en II) lleva sufijo de libro."""
    taken = {}
    for book, entries in books_entries:
        for e in entries:
            base = wb.slugify(H.unescape(wb.strip_tags(e['term']))) or 'term'
            if base in taken:
                e['anchor'] = f"{base}--{book['key']}"
                e['also'] = taken[base]
            else:
                e['anchor'] = base
                taken[base] = book['num']
            e['also'] = e.get('also')


def render_html(lang, books_entries, versions):
    ui = UI[lang]
    alt = 'en' if lang == 'es' else 'es'
    parts = []
    terms_ld = []
    for book, entries in books_entries:
        parts.append(f'<h2 id="book-{book["key"]}">{book["num"]} · {book["title"][lang]}'
                     f' <span class="ed">{versions[book["key"]]}</span></h2>')
        parts.append('<dl class="vocab">')
        for e in entries:
            also = (f' <span class="also">{ui["also"]} {ui["in_book"]} {e["also"]}</span>' if e['also'] else '')
            parts.append(
                f'<dt id="{e["anchor"]}"><a class="t" href="#{e["anchor"]}">{e["term"]}</a>{also}'
                f' <a class="src" href="{e["src"]}" title="{ui["source"]}">{ui["in_book"]} {book["num"]} · {book["src_label"][lang]} ↗</a></dt>'
                f'<dd>{e["def"]}</dd>')
            terms_ld.append({'@type': 'DefinedTerm', 'name': H.unescape(wb.strip_tags(e['term'])),
                             'description': H.unescape(wb.strip_tags(e['def'])),
                             'url': f'{SITE}{ui["path"]}#{e["anchor"]}',
                             'inDefinedTermSet': f'{SITE}{ui["path"]}'})
        parts.append('</dl>')
    ld = {'@context': 'https://schema.org', '@type': 'DefinedTermSet', 'name': ui['h1'],
          'url': f'{SITE}{ui["path"]}', 'inLanguage': lang, 'license': 'https://www.gnu.org/licenses/fdl-1.3.html',
          'hasDefinedTerm': terms_ld}
    eds = ' · '.join(f'{b["num"]} {versions[b["key"]]}' for b in BOOKS)
    toggle = (f'<span><span class="on">ES</span> · <a href="{ui["alt"]}">EN</a></span>' if lang == 'es'
              else f'<span><span class="on">EN</span> · <a href="{ui["alt"]}">ES</a></span>')
    nxt = ''.join(f'<a href="{h}"><span class="k">{k}</span> {t}</a>' for k, t, h in ui['next'])
    return (f'<!DOCTYPE html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{ui["h1"]} · AgencyDomains</title>\n'
            f'<meta name="description" content="{H.escape(wb.strip_tags(ui["deck"]))}">\n'
            f'<link rel="canonical" href="{SITE}{ui["path"]}">\n'
            f'<link rel="alternate" hreflang="{lang}" href="{SITE}{ui["path"]}">\n'
            f'<link rel="alternate" hreflang="{alt}" href="{SITE}{ui["alt"]}">\n'
            f'<link rel="alternate" type="text/markdown" href="{SITE}{ui["path"]}{ui["md"]}">\n'
            f'{FONTS}\n<link rel="stylesheet" href="/assets/agencydomains.css">\n'
            f'<link rel="stylesheet" href="/assets/page.css">\n'
            f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
            f'</head>\n<body>\n<main class="page">\n'
            f'  <nav class="crumb"><a href="{"/es/" if lang == "es" else "/"}">{ui["crumb_home"]}</a>{toggle}</nav>\n'
            f'  <p class="eyebrow">{ui["eyebrow"]}</p>\n  <h1>{ui["h1"]}</h1>\n'
            f'  <p class="deck">{ui["deck"]}</p>\n'
            f'  <p class="promise">{ui["editions"]}: {eds}</p>\n'
            f'  <p>{ui["intro"]}</p>\n'
            f'  <p class="callout"><span class="k">{ui["cite"]}</span> · {ui["cite_txt"]}</p>\n'
            + '\n'.join(parts) +
            f'\n  <div class="next">{nxt}</div>\n'
            f'  <p class="promise" style="border-bottom:0">{ui["foot"]}</p>\n</main>\n</body>\n</html>\n')


def render_md(lang, books_entries, versions):
    ui = UI[lang]
    out = [f'# {ui["md_title"]}', '', f'> {ui["md_intro"]}', '',
           f'> {ui["editions"]}: ' + ' · '.join(f'{b["num"]} {versions[b["key"]]}' for b in BOOKS), '']
    for book, entries in books_entries:
        out += [f'## {book["num"]} · {book["title"][lang]} ({versions[book["key"]]})', '']
        for e in entries:
            t = H.unescape(wb.strip_tags(e['term'])); d = H.unescape(wb.strip_tags(e['def']))
            out.append(f'- **{t}** — {d} · {SITE}{e["src"]}')
        out.append('')
    return '\n'.join(out)


def main():
    versions = {b['key']: ver(b['key']) for b in BOOKS}
    fail = False
    per_lang = {}
    for lang in ('es', 'en'):
        be = []
        for b in BOOKS:
            be.append((b, load(b, lang)))
        assign_anchors(be)
        per_lang[lang] = be
    for i, b in enumerate(BOOKS):
        n_es, n_en = len(per_lang['es'][i][1]), len(per_lang['en'][i][1])
        if n_es != n_en:
            print(f'::error::gen-vocabulario: {b["key"]} tiene {n_es} entradas en ES y {n_en} en EN — '
                  f'los glosarios no son espejo.'); fail = True
    if fail:
        sys.exit(1)
    for lang in ('es', 'en'):
        ui = UI[lang]
        dest = os.path.join(ROOT, ui['path'].strip('/'))
        os.makedirs(dest, exist_ok=True)
        with open(os.path.join(dest, 'index.html'), 'w', encoding='utf-8') as fh:
            fh.write(render_html(lang, per_lang[lang], versions))
        with open(os.path.join(dest, ui['md']), 'w', encoding='utf-8') as fh:
            fh.write(render_md(lang, per_lang[lang], versions))
        total = sum(len(e) for _, e in per_lang[lang])
        print(f'  {ui["path"]} → {total} términos (' +
              ' · '.join(f'{b["num"]} {len(e)}' for b, e in per_lang[lang]) + ')')


if __name__ == '__main__':
    main()
