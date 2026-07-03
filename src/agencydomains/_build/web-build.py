#!/usr/bin/env python3
r"""Genera el libro-web multipágina (una página por capítulo) desde el Markdown único.
Barra lateral persistente con sub-índice del capítulo activo + navegación prev/next.
Las partes LaTeX (```{=latex}\part{X}```) se vuelven páginas-divisor con clase propia.
Salida: <out>/index.html (portada) y <out>/<slug>/index.html por capítulo."""
import argparse, os, re, shutil, subprocess, sys, unicodedata

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,340..620;'
 '1,9..144,340..560&family=Spectral:ital,wght@0,300;0,400;0,500;0,600;1,400;1,500&'
 'family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')

def slugify(t):
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    t = re.sub(r'[^a-zA-Z0-9]+', '-', t).strip('-').lower()
    return t

def pandoc(md):
    r = subprocess.run(['pandoc', '-f', 'markdown', '-t', 'html'],
                       input=md, capture_output=True, text=True)
    if r.returncode: sys.exit('pandoc falló:\n' + r.stderr)
    return r.stdout

def strip_tags(s): return re.sub(r'<[^>]+>', '', s).strip()

# Canales de feedback. El correo directo es el canal SIN paredes: cualquiera puede
# escribir sin cuenta. (Swappable: cambiar aquí si se crea un alias dedicado.)
CONTACT_EMAIL = 'cesar.obach@ultrabase.net'
REPO_URL = 'https://github.com/gegolabs/agencydomains.org'

# Strings de UI por idioma (el resto del HTML es agnóstico).
STRINGS = {
    'es': {'cover': 'Portada', 'prev': '← Anterior', 'next': 'Siguiente →',
           'nav_aria': 'Índice del libro', 'book': 'El libro',
           'zoom': 'Ampliar la figura', 'close': 'Cerrar (Esc)',
           'fb_q': '¿Comentarios, dudas o una corrección? Este libro se escribe en público y busca crítica.',
           'fb_mail_k': 'Sin cuenta ·', 'fb_mail': 'escríbeme directo',
           'fb_issue_k': 'En GitHub ·', 'fb_issue': 'abre un tema',
           'fb_pr_k': 'A fondo ·', 'fb_pr': 'cómo proponer un cambio (GFDL)'},
    'en': {'cover': 'Cover', 'prev': '← Previous', 'next': 'Next →',
           'nav_aria': 'Book contents', 'book': 'The book',
           'zoom': 'Enlarge figure', 'close': 'Close (Esc)',
           'fb_q': 'Comments, questions, or a correction? This book is written in public and invites critique.',
           'fb_mail_k': 'No account ·', 'fb_mail': 'email me directly',
           'fb_issue_k': 'On GitHub ·', 'fb_issue': 'open an issue',
           'fb_pr_k': 'Go deeper ·', 'fb_pr': 'how to propose a change (GFDL)'},
}

# Pie de feedback por página: correo sin login (para todos) + issue + cómo contribuir.
def feedback(ui, name, version):
    subj = f'Feedback — {name} {version}'.replace(' ', '%20').replace('—', '%E2%80%94')
    return (
        f'<footer class="book-foot">'
        f'<p class="ff-q">{ui["fb_q"]}</p>'
        f'<a href="mailto:{CONTACT_EMAIL}?subject={subj}"><span class="k">{ui["fb_mail_k"]}</span> {ui["fb_mail"]} →</a>'
        f'<a href="{REPO_URL}/issues/new"><span class="k">{ui["fb_issue_k"]}</span> {ui["fb_issue"]} →</a>'
        f'<a href="{REPO_URL}/blob/main/CONTRIBUTING.md"><span class="k">{ui["fb_pr_k"]}</span> {ui["fb_pr"]} →</a>'
        f'</footer>\n')

# Lightbox: las figuras se renderizan reducidas al ancho de la columna; un clic
# las abre a tamaño real sobre un velo oscuro (clic en cualquier lugar o Esc cierra).
def lightbox(ui):
    return (
        f'<div class="lightbox" id="lightbox" hidden role="dialog" aria-modal="true" aria-label="{ui["zoom"]}">'
        f'<button class="lightbox-close" type="button" aria-label="{ui["close"]}">&times;</button>'
        f'<img alt=""></div>\n'
        '<script>(function(){'
        'var lb=document.getElementById("lightbox"),im=lb.querySelector("img");'
        'function open(s,a){im.src=s;im.alt=a||"";lb.hidden=false;document.body.classList.add("lb-open");}'
        'function close(){lb.hidden=true;im.removeAttribute("src");document.body.classList.remove("lb-open");}'
        'document.querySelectorAll("article.book img").forEach(function(g){'
        'g.addEventListener("click",function(){open(g.currentSrc||g.src,g.alt);});});'
        'lb.addEventListener("click",close);'
        'document.addEventListener("keydown",function(e){if(e.key==="Escape"&&!lb.hidden)close();});'
        '})();</script>\n')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--md', required=True); ap.add_argument('--figuras', required=True)
    ap.add_argument('--out', required=True); ap.add_argument('--pdf'); ap.add_argument('--agents')
    ap.add_argument('--base', default='/agencydomains')   # ruta absoluta de servido
    ap.add_argument('--name', default='AgencyDomains')    # marca corta del libro (nombra los distribuibles)
    ap.add_argument('--title', default=None)               # título visible (default: --name)
    ap.add_argument('--lang', default='es', choices=('es', 'en'))
    ap.add_argument('--version', required=True)           # vX.Y — nombra los distribuibles
    a = ap.parse_args()
    a.title = a.title or a.name
    UI = STRINGS[a.lang]

    md = open(a.md, encoding='utf-8').read()
    # Partes LaTeX → páginas-divisor (heading sintético con marcador).
    # Un bloque {=latex} que contenga \part{X} se reemplaza completo (p. ej.
    # \appendix + \part{Anexos}); los demás bloques latex quedan intactos.
    def _latex_block(m):
        pm = re.search(r'\\part\{([^}]+)\}', m.group(1))
        return f'# {pm.group(1)} <!--part-->' if pm else m.group(0)
    md = re.sub(r'(?ms)^```\{=latex\}\n(.*?)\n```[ \t]*$', _latex_block, md)
    chunks = [c for c in re.split(r'(?m)(?=^# )', md) if c.strip()]
    pages = []
    for c in chunks:
        first = c.splitlines()[0]
        part = '<!--part-->' in first
        if part:
            c = c.replace(' <!--part-->', '', 1)
        title = strip_tags(c.splitlines()[0].lstrip('# ').strip())
        pages.append({'title': title, 'md': c, 'part': part})
    # portada = primer chunk (AgencyDomains); resto = capítulos
    pages[0]['slug'] = ''; pages[0]['cover'] = True; pages[0]['label'] = UI['cover']
    for p in pages[1:]:
        p['slug'] = slugify(p['title']); p['cover'] = False; p['label'] = p['title']

    def url(p): return f"{a.base}/" if p['cover'] else f"{a.base}/{p['slug']}/"

    # render cuerpo + sub-toc por página
    for p in pages:
        body = pandoc(p['md']).replace('src="figuras/', f'src="{a.base}/figuras/')
        p['body'] = body
        p['sub'] = [(m.group(1), strip_tags(m.group(2)))
                    for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body, re.S)]

    os.makedirs(a.out, exist_ok=True)
    for i, p in enumerate(pages):
        # barra lateral (mismos capítulos en todas; sub-índice bajo el activo)
        nav = []
        for j, q in enumerate(pages):
            active = ' active' if j == i else ''
            sub = ''
            if j == i and q['sub']:
                items = ''.join(f'<li><a href="#{sid}">{txt}</a></li>' for sid, txt in q['sub'])
                sub = f'<ul class="subtoc">{items}</ul>'
            licls = ' class="part"' if q.get('part') else ''
            nav.append(f'<li{licls}><a class="{active.strip()}" href="{url(q)}">{q["label"]}</a>{sub}</li>')
        nav_html = ''.join(nav)
        # prev / next
        pn = []
        if i > 0:
            pp = pages[i-1]
            pn.append(f'<a href="{url(pp)}"><span class="dir">{UI["prev"]}</span>{pp["label"]}</a>')
        if i < len(pages)-1:
            nx = pages[i+1]
            pn.append(f'<a class="nx" href="{url(nx)}"><span class="dir">{UI["next"]}</span>{nx["label"]}</a>')
        prevnext = ''.join(pn) if pn else ''
        co, cc = ('<section class="book-cover">', '</section>') if p['cover'] else \
                 (('<section class="book-part">', '</section>') if p.get('part') else ('', ''))
        crumb = UI['cover'] if p['cover'] else p['title']
        html = (f'<!DOCTYPE html>\n<html lang="{a.lang}">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{p["title"] if p["title"] == a.title else p["title"] + " · " + a.title}</title>\n{FONTS}\n'
            f'<link rel="stylesheet" href="/assets/agencydomains.css">\n</head>\n<body>\n'
            f'<div class="book-topbar"><a class="home" href="/">← AgencyDomains.org</a>'
            f'<span class="crumb">{crumb}</span></div>\n'
            f'<div class="book-shell">\n'
            f'<nav class="book-nav" aria-label="{UI["nav_aria"]}"><p class="nav-label">{UI["book"]} · {a.version}</p>'
            f'<ol>{nav_html}</ol></nav>\n'
            f'<main class="book-main"><article class="book">{co}\n{p["body"]}\n{cc}'
            f'<nav class="prevnext">{prevnext}</nav>{feedback(UI, a.title, a.version)}</article></main>\n'
            f'</div>\n{lightbox(UI)}</body>\n</html>\n')
        dest = os.path.join(a.out, 'index.html') if p['cover'] else os.path.join(a.out, p['slug'], 'index.html')
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, 'w', encoding='utf-8').write(html)

    # assets del libro
    figdst = os.path.join(a.out, 'figuras'); shutil.rmtree(figdst, ignore_errors=True)
    shutil.copytree(a.figuras, figdst)
    if a.agents:
        shutil.copy(a.agents, os.path.join(a.out, f'{a.name}-{a.version}-agents-{a.lang}.md'))
        shutil.copy(a.agents, os.path.join(a.out, f'{a.name}-{a.version}-agents-{a.lang}.txt'))
    if a.pdf and os.path.exists(a.pdf):
        shutil.copy(a.pdf, os.path.join(a.out, f'{a.name}-{a.version}-{a.lang}.pdf'))
    print(f"  ✓ {len(pages)} páginas → {a.out}")
    print("    " + " · ".join((p['slug'] or 'index') for p in pages))

if __name__ == '__main__': main()
