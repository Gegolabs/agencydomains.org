#!/usr/bin/env python3
"""Verifica que la pieza de las cuatro medidas (hoja + kit) no defina ni cite nada
por su cuenta. Corre en publish.yml sobre el sitio YA ENSAMBLADO, después del
vocabulario y antes de publicar: si la pieza deriva de sus fuentes, no se publica.

La pieza vive en site/four-measures/ (hoja: index.html · kit: agent-kit.md). Es un
derivado del Libro II, y un derivado sin verificador se desincroniza a la primera
edición nueva (el «kit» suelto se descartó por eso; ver NEXT.md del repo
agencydomains-org). Si este script falla, manda el libro: se corrige la pieza.

Uso:
  python3 verificar-cuatro-medidas.py --vocab <vocabulary.md> --libro <src/rte/contenido-en> \\
      --manifiesto <RealTimeEnterprise-vX.Y-agents-en.md> --version vX.Y \\
      [--sitio <_site>] <pieza> [<pieza> ...]

Fuentes (en publish.yml, las del mismo build que se va a publicar):
  --vocab       gemelo Markdown de /vocabulary/ (lo genera gen-vocabulario.py)
  --libro       fuente EN del Libro II (su Conclusión trae la tabla de las medidas)
  --manifiesto  manifiesto EN para agentes del Libro II, edición vigente
  --version     edición vigente del Libro II (primer «## vX.Y» de su CHANGELOG)
  --sitio       raíz del sitio ensamblado: activa la comprobación 7

Comprobaciones (cualquier falla → código de salida 1):
  1. Definiciones. Toda línea «**término** — definición» existe en la sección II
     del vocabulario con la definición idéntica, carácter por carácter.
  2. Anclas. Si la definición va seguida de un enlace a /vocabulary/#…, el ancla
     es la del término.
  3. Tabla de las medidas. La tabla del kit (§2) es idéntica, fila por fila y en el
     mismo orden, a la de la Conclusión del libro; en la hoja, cada cara lleva la
     medida que la Conclusión le asigna.
  4. Citas en bloque. Toda cita «> …» del kit está literal en el libro, salvo la
     agenda canónica, que se busca en el manifiesto (y el recuadro «What this is»,
     que es del kit). La cita de la agenda en la hoja, en el libro.
  5. Citas en línea. Todo texto entre comillas de tres palabras o más está literal
     en el libro o en el manifiesto (el punto o la coma final dentro de las comillas,
     a la inglesa, no cuenta), salvo las frases propias de la pieza (PROPIAS:
     las preguntas de la encuesta y el pedido hipotético), que se declaran abajo.
  6. Edición. Toda mención de edición del Libro II en la pieza («The Real-Time
     Enterprise … vX.Y», «edition II vX.Y», «RealTimeEnterprise-vX.Y-») es la vigente:
     una edición nueva obliga a revisar la pieza, no la deja citando la anterior.
  7. Enlaces internos (con --sitio). Todo https://agencydomains.org/<ruta> que la
     pieza enlaza existe en el sitio ensamblado (el enlace hoja → kit incluido).
  8. Ninguna pieza repite las dos cifras que el memo editorial 008 marcó como mal
     calculadas («five hundred times», «orders of magnitude»).
"""
import argparse
import html
import os
import re
import sys

# Frases entre comillas que son de la pieza, no del libro ni del manifiesto.
# Cambiar una de estas frases en la pieza obliga a cambiarla aquí: es a propósito.
PROPIAS = {
    'help us start measuring this.',
    'it would take weeks',
    'why did this move?',
    'Today, how many hours did you work without being interrupted?',
    'What time did your workday truly end today?',
    'The four measures — kit for agents',
    'The executive agenda',           # título de la sección del libro que se cita
}

SITE = 'https://agencydomains.org'


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()


def strip_md(s):
    return s.replace('**', '').replace('*', '')


def plain(s):
    return norm(strip_md(s))


def load_vocab(path):
    txt = open(path, encoding='utf-8').read()
    sec = re.search(r'^## II · .*?(?=^## )', txt, re.M | re.S).group(0)
    vocab = {}
    for m in re.finditer(r'^- \*\*(.+?)\*\* — (.+) · (https://\S+)$', sec, re.M):
        vocab[m.group(1)] = (m.group(2), m.group(3))
    if not vocab:
        sys.exit('verificar-cuatro-medidas: la sección II del vocabulario está vacía')
    return vocab


def md_table_rows(text, header_first_cell):
    """Filas de la primera tabla Markdown cuya cabecera empieza por header_first_cell."""
    lines = text.split('\n')
    for i, line in enumerate(lines):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if line.lstrip().startswith('|') and cells[0] == header_first_cell:
            rows = [cells]
            for nxt in lines[i + 2:]:
                if not nxt.lstrip().startswith('|'):
                    break
                rows.append([c.strip() for c in nxt.strip().strip('|').split('|')])
            return rows
    return None


def piece_text(path, raw):
    if path.endswith('.html'):
        body = re.sub(r'<(style|script)\b.*?</\1>', '', raw, flags=re.S)
        body = re.sub(r'<br\s*/?>', '\n', body)
        body = re.sub(r'<strong>(.*?)</strong>', r'**\1**', body)
        body = re.sub(r'</(p|td|tr|li|h\d|div)>', '\n', body)
        body = re.sub(r'<[^>]+>', '', body)
        return html.unescape(body)
    return raw


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vocab', required=True)
    ap.add_argument('--libro', required=True)
    ap.add_argument('--manifiesto', required=True)
    ap.add_argument('--version', required=True)
    ap.add_argument('--sitio')
    ap.add_argument('piezas', nargs='+')
    a = ap.parse_args()

    vocab = load_vocab(a.vocab)
    files = sorted(f for f in os.listdir(a.libro) if f.endswith('.md'))
    book_raw = {f: open(os.path.join(a.libro, f), encoding='utf-8').read() for f in files}
    book = plain(' '.join(book_raw.values()))
    manifest = plain(open(a.manifiesto, encoding='utf-8').read())
    concl = [t for f, t in book_raw.items() if 'conclusion' in f]
    if len(concl) != 1:
        sys.exit('verificar-cuatro-medidas: no encuentro una sola Conclusión en %s' % a.libro)
    tabla = md_table_rows(concl[0], 'Face')
    if not tabla or len(tabla) != 5:
        sys.exit('verificar-cuatro-medidas: la Conclusión no trae la tabla de las cuatro caras '
                 '(cabecera «Face» + 4 filas) — si el libro la cambió de forma, ajusta este script')
    medida_de = {strip_md(r[0]): r[2] for r in tabla[1:]}

    fails, oks = [], 0

    def ok(msg):
        nonlocal oks
        oks += 1
        print('  ok  ' + msg)

    for p in a.piezas:
        raw = open(p, encoding='utf-8').read()
        text = piece_text(p, raw)
        lines = text.split('\n')
        name = os.path.relpath(p)

        # 1 + 2 · definiciones y anclas
        for i, line in enumerate(lines):
            m = re.match(r'^\s*\*\*(.+?)\*\* — (.+)$', line)
            if not m:
                continue
            term, d = m.group(1), m.group(2).strip()
            if term not in vocab:
                fails.append(f'{name}: «{term}» no es entrada del vocabulario (sección II)')
                continue
            vdef, vurl = vocab[term]
            if d != vdef:
                fails.append(f'{name}: «{term}» difiere del vocabulario\n    pieza: {d}\n    vocab: {vdef}')
                continue
            anchor = vurl.split('#')[-1]
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ''
            if 'vocabulary/#' in nxt and not nxt.strip('<>').endswith('#' + anchor):
                fails.append(f'{name}: «{term}» enlaza a {nxt}, debería ser #{anchor}')
                continue
            ok(f'{name}: definición «{term}»')

        # 3 · tabla de las medidas contra la Conclusión
        if p.endswith('.md'):
            t = md_table_rows(text, 'Face')
            if t is None:
                fails.append(f'{name}: no trae la tabla de las cuatro medidas (cabecera «Face»)')
            elif t != tabla:
                for k in range(max(len(t), len(tabla))):
                    pk = t[k] if k < len(t) else None
                    lk = tabla[k] if k < len(tabla) else None
                    if pk != lk:
                        fails.append(f'{name}: la tabla de las medidas difiere de la Conclusión, fila {k}\n'
                                     f'    pieza: {pk}\n    libro: {lk}')
            else:
                ok(f'{name}: tabla de las medidas idéntica a la Conclusión ({len(t) - 1} filas)')
        else:
            pares = re.findall(r'<td class="face">(.*?)</td>\s*<td class="measure">(.*?)</td>', raw, re.S)
            if len(pares) != 4:
                fails.append(f'{name}: la hoja no trae las cuatro caras con su medida ({len(pares)})')
            for cara, med in pares:
                cara, med = norm(html.unescape(cara)), norm(html.unescape(med))
                if medida_de.get(cara) != med:
                    fails.append(f'{name}: «{cara}» lleva «{med}»; la Conclusión dice «{medida_de.get(cara)}»')
                else:
                    ok(f'{name}: {cara} → «{med}»')

        # 4 · citas en bloque
        quotes = []   # (texto, fuente)
        if p.endswith('.md'):
            block = []
            for line in lines + ['']:
                if line.startswith('> ') or line == '>':
                    block.append(line[2:])
                elif block:
                    quotes.append(' '.join(block))
                    block = []
            quotes = [(q, 'manifiesto' if q.startswith('**Executive agenda') else 'libro')
                      for q in quotes if not q.startswith('**What this is')]
        else:
            m = re.search(r'executive agenda: “(.*?)”', text)
            if m:
                quotes.append((m.group(1), 'libro'))
        for q, fuente in quotes:
            q = re.sub(r'\s*\*\(Chapter \d+\.\)\*\s*$', '', q)
            q = re.sub(r'^1\. ', '', plain(q))
            hay = book if fuente == 'libro' else manifest
            if q in hay:
                ok(f'{name}: cita en bloque ({fuente}) «{q[:55]}…»')
            else:
                fails.append(f'{name}: cita en bloque no encontrada en el {fuente}: «{q[:90]}…»')

        # 5 · citas en línea
        cuerpo = re.sub(r'```.*?```', '', text, flags=re.S)
        cuerpo = cuerpo.replace('“', '"').replace('”', '"')
        for m in re.finditer(r'"([^"]+)"', cuerpo):
            q = plain(m.group(1))
            if len(q.split()) < 3:
                continue
            # puntuación a la inglesa: el punto o la coma final dentro de las comillas
            # no es parte de la cita
            q_sin = q[:-1] if q[-1] in '.,' else q
            if q in PROPIAS:
                ok(f'{name}: frase propia de la pieza «{q[:55]}»')
            elif q in book or q_sin in book:
                ok(f'{name}: cita en línea (libro) «{q[:55]}»')
            elif q in manifest or q_sin in manifest:
                ok(f'{name}: cita en línea (manifiesto) «{q[:55]}»')
            else:
                fails.append(f'{name}: cita en línea que no está ni en el libro ni en el manifiesto '
                             f'(si es frase propia, decláralo en PROPIAS): «{q[:90]}»')

        # 6 · edición vigente
        flat = norm(strip_md(text))
        menciones = re.findall(r'The Real-Time Enterprise[^.()]{0,45}?\b(v\d+\.\d+(?:\.\d+)?)', flat)
        menciones += re.findall(r'edition II (v\d+\.\d+(?:\.\d+)?)', flat)
        menciones += re.findall(r'RealTimeEnterprise-(v\d+\.\d+(?:\.\d+)?)-', raw)
        for v in menciones:
            if v != a.version:
                fails.append(f'{name}: cita la edición {v} del Libro II; la vigente es {a.version}')
        if menciones and all(v == a.version for v in menciones):
            ok(f'{name}: {len(menciones)} menciones de edición, todas {a.version}')

        # 7 · enlaces internos
        if a.sitio:
            rutas = {u.split('#')[0].split('?')[0].rstrip('.,;')
                     for u in re.findall(re.escape(SITE) + r'(/[^\s<>")\]]*)', raw)}
            for ruta in sorted(rutas):
                dest = os.path.join(a.sitio, ruta.lstrip('/'))
                if ruta.endswith('/') or ruta == '':
                    dest = os.path.join(dest, 'index.html')
                if os.path.isfile(dest):
                    ok(f'{name}: enlace {ruta}')
                else:
                    fails.append(f'{name}: enlaza {SITE}{ruta}, que no existe en el sitio ensamblado')

        # 8 · cifras retiradas
        for bad in ('five hundred times', 'orders of magnitude'):
            if bad in text.lower():
                fails.append(f'{name}: repite la cifra marcada por el memo 008: «{bad}»')

    print(f'\n{oks} comprobaciones correctas, {len(fails)} fallas')
    for f in fails:
        print('FALLA ' + f)
        if os.environ.get('GITHUB_ACTIONS'):
            print('::error::cuatro medidas — ' + f.split('\n')[0])
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
