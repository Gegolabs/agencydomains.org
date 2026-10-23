#!/usr/bin/env python3
"""Deposita en Zenodo la edición de UN libro: un DOI-concepto por libro, un DOI por versión.

La integración GitHub→Zenodo de fábrica da un solo concepto por repositorio, y
este repo trae tres libros: el consultor que cita AURA no cita la trilogía. Por
eso el depósito va por la API REST, con los metadatos en src/<libro>/.zenodo.json
y la configuración (entorno, conceptos, archivos) en .github/zenodo/deposito.json.

Flujo, contra la documentación (verificada el 2026-10-23):
  · API de depósito ............ https://developers.zenodo.org/
      crear       POST /api/deposit/depositions
      listar      GET  /api/deposit/depositions?q=…&size=100&all_versions=true
      metadatos   PUT  /api/deposit/depositions/:id            {"metadata": …}
      archivos    PUT  <links.bucket>/<nombre>   ·   DELETE …/depositions/:id/files/:file_id
      versión     POST /api/deposit/depositions/:id/actions/newversion  (:id = la ÚLTIMA versión;
                  la respuesta es el original, el borrador nuevo está en links.latest_draft)
      publicar    POST /api/deposit/depositions/:id/actions/publish     (202)
      alcances    deposit:write + deposit:actions
  · última versión de un concepto  https://inveniordm.docs.cern.ch/reference/rest_api_drafts_records/#get-latest-version
      GET /api/records/:conceptrecid/versions/latest   (301 al registro vigente; medido en zenodo.org)
  · vocabularios .............. GET /api/vocabularies/licenses/gfdl-1.3-only · /api/vocabularies/languages/spa

Un concepto nace con la primera versión que se deposita; su conceptrecid se
registra a mano en deposito.json (el workflow lee el repo, no lo escribe). Para no
abrir un segundo concepto si se olvida, antes de crear uno se buscan los depósitos
propios con el mismo título y, si existe, se aborta.

Uso:
  zenodo-deposito.py --libro aura --version v1.1 --sitio _site [--entorno sandbox|zenodo]
                     [--en-seco] [--vocabularios] [--sin-publicar] [--sin-token-ok]
El token se lee de la variable de entorno que nombra deposito.json para el entorno
(ZENODO_SANDBOX_TOKEN o ZENODO_TOKEN); nunca se pasa por argumento ni se imprime.
"""
import argparse, datetime, json, os, re, sys, urllib.error, urllib.parse, urllib.request

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
CONFIG = os.path.join(RAIZ, '.github', 'zenodo', 'deposito.json')

# Lo obligatorio y los vocabularios cerrados, tal como los lista «Deposit metadata»
# en https://developers.zenodo.org/ — lo que no está aquí se valida en línea.
OBLIGATORIOS = ['upload_type', 'publication_type', 'title', 'creators', 'description',
                'access_right', 'license']
UPLOAD_TYPES = {'publication', 'poster', 'presentation', 'dataset', 'image', 'video',
                'software', 'lesson', 'physicalobject', 'other'}
PUBLICATION_TYPES = {'annotationcollection', 'book', 'section', 'conferencepaper',
                     'datamanagementplan', 'article', 'patent', 'preprint', 'deliverable',
                     'milestone', 'proposal', 'report', 'softwaredocumentation',
                     'taxonomictreatment', 'technicalnote', 'thesis', 'workingpaper', 'other'}
ACCESS_RIGHTS = {'open', 'embargoed', 'restricted', 'closed'}
RELACIONES = {'isCitedBy', 'cites', 'isSupplementTo', 'isSupplementedBy', 'isContinuedBy',
              'continues', 'isDescribedBy', 'describes', 'hasMetadata', 'isMetadataFor',
              'isNewVersionOf', 'isPreviousVersionOf', 'isPartOf', 'hasPart', 'isReferencedBy',
              'references', 'isDocumentedBy', 'documents', 'isCompiledBy', 'compiles',
              'isVariantFormOf', 'isOriginalFormof', 'isIdenticalTo', 'isAlternateIdentifier',
              'isReviewedBy', 'reviews', 'isDerivedFrom', 'isSourceOf', 'requires',
              'isRequiredBy', 'isObsoletedBy', 'obsoletes'}
# Campos que el script pone en cada versión: no se escriben en .zenodo.json.
DEL_SCRIPT = {'publication_date'}


def fallar(msg):
    print('::error::zenodo: ' + msg)
    sys.exit(1)


def resumen(linea):
    print(linea)
    ruta = os.environ.get('GITHUB_STEP_SUMMARY')
    if ruta:
        with open(ruta, 'a', encoding='utf-8') as f:
            f.write(linea + '\n')


def version_changelog(libro):
    with open(os.path.join(RAIZ, 'src', libro, 'CHANGELOG.md'), encoding='utf-8') as f:
        m = re.search(r'^## (v\d+\.\d+(?:\.\d+)?)', f.read(), re.M)
    return m.group(1) if m else None


def validar(md, libro, version):
    """Valida sin red. Devuelve la lista de errores."""
    err = []
    for k in OBLIGATORIOS:
        if not md.get(k):
            err.append('falta «%s»' % k)
    for k in DEL_SCRIPT & set(md):
        err.append('«%s» lo pone el script en cada versión: sácalo de .zenodo.json' % k)
    if md.get('upload_type') not in UPLOAD_TYPES:
        err.append('upload_type «%s» fuera del vocabulario' % md.get('upload_type'))
    if md.get('upload_type') == 'publication' and md.get('publication_type') not in PUBLICATION_TYPES:
        err.append('publication_type «%s» fuera del vocabulario' % md.get('publication_type'))
    if md.get('access_right') not in ACCESS_RIGHTS:
        err.append('access_right «%s» fuera del vocabulario' % md.get('access_right'))
    for c in md.get('creators') or []:
        if ', ' not in c.get('name', ''):
            err.append('creator «%s» no está en la forma «Apellido, Nombres»' % c.get('name'))
    lang = md.get('language', '')
    if lang and not re.fullmatch(r'[a-z]{3}', lang):
        err.append('language «%s» no es un código ISO 639-2/639-3' % lang)
    for r in md.get('related_identifiers') or []:
        if r.get('relation') not in RELACIONES:
            err.append('relation «%s» fuera del vocabulario' % r.get('relation'))
        if not r.get('identifier'):
            err.append('related_identifier sin identifier')
    # La misma guardia que el workflow aplica a frontmatter.tex: el número que sale
    # impreso en el depósito es el del CHANGELOG del libro, no uno escrito aparte.
    cl = version_changelog(libro)
    if md.get('version') != cl:
        err.append('.zenodo.json dice version «%s» y el CHANGELOG de %s dice «%s»'
                   % (md.get('version'), libro, cl))
    if version and version != cl:
        err.append('--version %s no coincide con el CHANGELOG de %s (%s)' % (version, libro, cl))
    return err


def http(metodo, url, token=None, datos=None, tipo='application/json', esperado=(200, 201, 202, 204)):
    cab = {'Accept': 'application/json'}
    if token:
        cab['Authorization'] = 'Bearer ' + token
    cuerpo = None
    if datos is not None:
        cuerpo = datos if isinstance(datos, bytes) else json.dumps(datos).encode('utf-8')
        cab['Content-Type'] = tipo
    req = urllib.request.Request(url, data=cuerpo, headers=cab, method=metodo)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            codigo, texto = r.status, r.read()
    except urllib.error.HTTPError as e:
        codigo, texto = e.code, e.read()
    if codigo not in esperado:
        fallar('%s %s → %s %s' % (metodo, url.split('?')[0], codigo, texto[:800].decode('utf-8', 'replace')))
    return json.loads(texto) if texto.strip() else {}


def vocabularios_en_linea(api, md):
    """GET públicos (sin token) a los vocabularios de Zenodo: licencia e idioma existen."""
    err = []
    for voc, valor in (('licenses', md.get('license')), ('languages', md.get('language'))):
        if not valor:
            continue
        url = '%s/vocabularies/%s/%s' % (api, voc, urllib.parse.quote(valor))
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'Accept': 'application/json'}), timeout=60) as r:
                titulo = json.load(r).get('title', {}).get('en')
                print('  vocabulario %s/%s → 200 «%s»' % (voc, valor, titulo))
        except urllib.error.HTTPError as e:
            err.append('%s «%s» no existe en %s (%s)' % (voc, valor, api, e.code))
    return err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--libro', required=True, choices=['rte', 'aura', 'agencydomains'])
    ap.add_argument('--version', help='la del tag (vX.Y); se exige igual al CHANGELOG')
    ap.add_argument('--sitio', default='_site', help='el sitio ya ensamblado')
    ap.add_argument('--entorno', choices=['sandbox', 'zenodo'], help='por defecto, el de deposito.json')
    ap.add_argument('--en-seco', action='store_true', help='valida y dice qué haría; no escribe en Zenodo')
    ap.add_argument('--vocabularios', action='store_true', help='coteja licencia e idioma contra la API pública')
    ap.add_argument('--sin-publicar', action='store_true', help='deja el borrador sin publicar')
    ap.add_argument('--sin-token-ok', action='store_true', help='sin token: aviso y salida 0 (uso en el workflow)')
    a = ap.parse_args()

    with open(CONFIG, encoding='utf-8') as f:
        cfg = json.load(f)
    entorno = a.entorno or cfg['entorno']
    api = cfg['entornos'][entorno]['api']
    secreto = cfg['entornos'][entorno]['secreto']
    with open(os.path.join(RAIZ, 'src', a.libro, '.zenodo.json'), encoding='utf-8') as f:
        md = json.load(f)
    version = a.version or md.get('version')

    print('zenodo · libro %s · versión %s · entorno %s (%s)' % (a.libro, version, entorno, api))
    err = validar(md, a.libro, a.version)
    if a.vocabularios:
        err += vocabularios_en_linea(api, md)
    if err:
        fallar('metadatos de %s: ' % a.libro + ' · '.join(err))
    print('  metadatos: válidos (%d campos)' % len(md))

    archivos = [os.path.join(a.sitio, p.replace('{V}', version)) for p in cfg['archivos'][a.libro]]
    faltan = [p for p in archivos if not os.path.isfile(p) or os.path.getsize(p) == 0]
    for p in archivos:
        print('  archivo %s %s' % ('FALTA' if p in faltan else 'ok   ', p))
    concepto = cfg['conceptos'][entorno][a.libro]
    print('  concepto: %s' % (concepto or 'ninguno aún → la primera versión crea el concepto'))

    if a.en_seco:
        if faltan:
            print('  en seco: %d archivo(s) ausentes en %s — no pude medir el depósito de archivos'
                  % (len(faltan), a.sitio))
        print('  en seco: no se escribió nada en Zenodo')
        return
    if faltan:
        fallar('faltan archivos del depósito: ' + ', '.join(faltan))

    token = os.environ.get(secreto)
    if not token:
        if a.sin_token_ok:
            print('::warning::zenodo: no hay %s; la edición %s de %s no se depositó' % (secreto, version, a.libro))
            return
        fallar('falta la variable de entorno %s' % secreto)

    if concepto:
        ultimo = http('GET', '%s/records/%s/versions/latest' % (api, concepto), token)
        if ultimo.get('metadata', {}).get('version') == version:
            resumen('zenodo: %s %s ya está depositada en el concepto %s (%s) — nada que hacer'
                    % (a.libro, version, concepto, ultimo.get('doi')))
            return
        # Se asume, sin medir todavía, que el id del registro es el id del depósito
        # (en Zenodo coinciden en los ejemplos de la documentación); la primera
        # versión nueva en el sandbox lo refuta o lo corrobora.
        r = http('POST', '%s/deposit/depositions/%s/actions/newversion' % (api, ultimo['id']), token)
        borrador = http('GET', r['links']['latest_draft'], token)
    else:
        q = urllib.parse.urlencode({'q': 'title:"%s"' % md['title'], 'size': 100, 'all_versions': 'true'})
        propios = http('GET', '%s/deposit/depositions?%s' % (api, q), token)
        iguales = [d for d in propios if d.get('title') == md['title']]
        if iguales:
            fallar('ya hay un depósito con el título «%s» (conceptrecid %s): regístralo en deposito.json '
                   'en vez de abrir un segundo concepto' % (md['title'], iguales[0].get('conceptrecid')))
        borrador = http('POST', '%s/deposit/depositions' % api, token, {})
    did = borrador['id']

    # Un borrador de versión nueva hereda los archivos de la anterior: se vacían.
    for f in borrador.get('files') or []:
        http('DELETE', '%s/deposit/depositions/%s/files/%s' % (api, did, f['id']), token)

    md_version = dict(md, version=version, publication_date=datetime.date.today().isoformat())
    http('PUT', '%s/deposit/depositions/%s' % (api, did), token, {'metadata': md_version})

    bucket = borrador['links']['bucket']
    for p in archivos:
        with open(p, 'rb') as f:
            http('PUT', '%s/%s' % (bucket, urllib.parse.quote(os.path.basename(p))), token,
                 f.read(), tipo='application/octet-stream')
        print('  subido %s' % os.path.basename(p))

    if a.sin_publicar:
        resumen('zenodo: borrador %s de %s %s listo, sin publicar: %s'
                % (did, a.libro, version, borrador['links'].get('html')))
        return
    pub = http('POST', '%s/deposit/depositions/%s/actions/publish' % (api, did), token, esperado=(202,))
    resumen('zenodo (%s): %s %s · DOI %s · DOI-concepto %s · %s'
            % (entorno, a.libro, version, pub.get('doi'), pub.get('conceptdoi'), pub.get('record_url') or pub['links'].get('html')))
    if not concepto:
        resumen('zenodo: concepto NUEVO de %s → registra "%s" en .github/zenodo/deposito.json '
                '(conceptos.%s.%s) antes del próximo tag de este libro'
                % (a.libro, pub.get('conceptrecid'), entorno, a.libro))


if __name__ == '__main__':
    main()
