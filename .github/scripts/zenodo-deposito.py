#!/usr/bin/env python3
"""Deposita en Zenodo la edición de UN libro: un DOI-concepto por libro, un DOI por versión.

La integración GitHub→Zenodo de fábrica da un solo concepto por repositorio, y
este repo trae tres libros: el consultor que cita AURA no cita la trilogía. Por
eso el depósito va por la API REST, con los metadatos en src/<libro>/.zenodo.json
y la configuración (entorno, conceptos, archivos) en .github/zenodo/deposito.json.

Flujo, contra la documentación (verificada el 2026-10-23):
  · API de depósito ............ https://developers.zenodo.org/
      crear       POST /api/deposit/depositions
      listar      GET  /api/deposit/depositions?size=100&page=N&all_versions=true  (sin q)
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
abrir un segundo concepto si se olvida, antes de crear uno se listan TODOS los
depósitos propios y, si hay uno publicado con el mismo título, se aborta. Una
versión ya depositada en cualquier punto del concepto no se vuelve a depositar.

Uso:
  zenodo-deposito.py --libro aura --version v1.1 --sitio _site [--entorno sandbox|zenodo]
                     [--en-seco] [--vocabularios] [--sin-publicar] [--sin-token-ok]
                     [--version-de-prueba vX.Y-prueba-N]   (solo sandbox)
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
    except OSError as e:
        # Caída de red, DNS o timeout: el log dice qué llamada falló, no un traceback.
        fallar('%s %s → sin respuesta (%s)' % (metodo, url.split('?')[0], e))
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
        except OSError as e:
            err.append('%s «%s»: %s sin respuesta (%s)' % (voc, valor, api, e))
    return err


def propios(api, token):
    """Todos los depósitos de la cuenta, con todas sus versiones, página a página.

    Sin `q`: la búsqueda del índice puede no devolver un depósito recién creado, y
    una guardia que dependa de ella falla abierta. Los depósitos de esta cuenta son
    pocos (tres libros), así que se traen todos y se filtra en el cliente.
    """
    todos, pagina = [], 1
    while True:
        q = urllib.parse.urlencode({'size': 100, 'page': pagina, 'all_versions': 'true'})
        lote = http('GET', '%s/deposit/depositions?%s' % (api, q), token)
        todos += lote
        if len(lote) < 100:
            return todos
        pagina += 1


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
    ap.add_argument('--version-de-prueba', help='solo sandbox: deposita con este número de versión '
                    '(p. ej. v1.0-prueba-2) para ejercitar newversion sin subir el CHANGELOG')
    a = ap.parse_args()

    with open(CONFIG, encoding='utf-8') as f:
        cfg = json.load(f)
    entorno = a.entorno or cfg['entorno']
    if a.version_de_prueba and entorno != 'sandbox':
        fallar('--version-de-prueba solo vale en el sandbox')
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

    # Los archivos se buscan con la versión del libro; el número que se deposita
    # puede ser uno de prueba (solo sandbox).
    version = a.version_de_prueba or version
    if a.version_de_prueba:
        print('  versión de prueba: se deposita como %s' % version)

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
        # Idempotencia contra TODAS las versiones publicadas del concepto, no solo la
        # última: re-ejecutar el job de un tag viejo cuando su libro ya tiene una
        # versión más nueva no debe acuñar un DOI duplicado.
        versiones = [d for d in propios(api, token)
                     if str(d.get('conceptrecid')) == str(concepto) and d.get('submitted')]
        if not versiones:
            fallar('el concepto %s de %s no aparece entre los depósitos publicados de esta cuenta: '
                   'no puedo comprobar que %s no esté ya depositada (¿token de otra cuenta, o '
                   'conceptrecid mal registrado?)' % (concepto, a.libro, version))
        ya = [d for d in versiones if d.get('metadata', {}).get('version') == version]
        if ya:
            resumen('zenodo: %s %s ya está depositada en el concepto %s (%s) — nada que hacer'
                    % (a.libro, version, concepto, ya[0].get('doi')))
            return
        ultimo = http('GET', '%s/records/%s/versions/latest' % (api, concepto), token)
        # Se asume, sin medir todavía, que el id del registro es el id del depósito
        # (en Zenodo coinciden en los ejemplos de la documentación); la primera
        # versión nueva en el sandbox (--version-de-prueba) lo refuta o lo corrobora.
        # Si ya hay un borrador de versión nueva, la documentación dice que
        # newversion «will have no effect» y latest_draft apunta a ese borrador.
        r = http('POST', '%s/deposit/depositions/%s/actions/newversion' % (api, ultimo['id']), token)
        borrador = http('GET', r['links']['latest_draft'], token)
    else:
        iguales = [d for d in propios(api, token) if d.get('title') == md['title']]
        publicados = [d for d in iguales if d.get('submitted')]
        if publicados:
            fallar('ya hay un depósito publicado con el título «%s» (conceptrecid %s): regístralo en '
                   'deposito.json en vez de abrir un segundo concepto'
                   % (md['title'], publicados[0].get('conceptrecid')))
        if iguales:
            # Un primer depósito que quedó a medias (corrida sin publicar, o caída
            # tras crearlo) se retoma: crear otro abriría un segundo concepto.
            borrador = http('GET', '%s/deposit/depositions/%s' % (api, iguales[0]['id']), token)
            print('  retomo el borrador %s, sin publicar' % borrador['id'])
        else:
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
