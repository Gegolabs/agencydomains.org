#!/usr/bin/env python3
"""Genera sitemap.xml recorriendo el sitio YA ENSAMBLADO.

Se deriva del artefacto, no de una lista mantenida a mano: lo que se publica es
exactamente lo que se lista, y añadir un capítulo o un idioma no exige acordarse
de nada. Por eso corre después del ensamblado de _site y antes del sync.

Qué entra: cada index.html como URL de directorio, y los PDF.
Qué no: los manifiestos para agentes (.md/.txt) — su índice canónico es
/llms.txt, que es la puerta declarada para agentes; listarlos aquí duplicaría
cada uno en dos o tres URLs (versionada, alias y .txt).
"""
import os, sys, datetime, xml.sax.saxutils as sx

SITE = 'https://agencydomains.org'
root = sys.argv[1] if len(sys.argv) > 1 else '_site'
hoy = datetime.date.today().isoformat()

urls = []
for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if not d.startswith('.')]
    rel = os.path.relpath(dirpath, root)
    base = '/' if rel == '.' else '/' + rel.replace(os.sep, '/') + '/'
    for f in sorted(filenames):
        if f == 'index.html':
            urls.append(base)
        elif f == '404.html':
            continue
        elif f.lower().endswith('.pdf'):
            urls.append(base + f)

urls = sorted(set(urls))
if not urls:
    sys.exit('gen-sitemap: no encontré ninguna página en %s' % root)

out = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
]
for u in urls:
    out.append('  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>'
               % (SITE, sx.escape(u), hoy))
out.append('</urlset>')

dest = os.path.join(root, 'sitemap.xml')
with open(dest, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out) + '\n')
print('  sitemap.xml → %d URLs' % len(urls))
