# Auditoría de entregable · AgencyDomains v1.2 — «Captura», cuarta familia de manifestación

**Tipo:** Auditoría pre-publicación (skill `auditoria-entregables`, delta v1.1 → v1.2)
**Fecha:** 2026-09-05 (noche)
**Auditor:** juez Fable 5.1 (subagente sin el contexto de la edición), orquestado por Simón Alero
**Objeto:** el cambio sin commitear en `src/agencydomains/` (13 archivos + ADR nuevo), contra el brief de edición de la v1.2
**Veredicto:** **PUBLICAR CON CORRECCIONES** — una corrección textual que se propagaba a los derivados, más dos menores. **Las tres se aplicaron antes del commit y los cinco builds se rehicieron.**

---

## Hallazgos y su cierre

| ID | Dimensión | Hallazgo | Corrección | Estado |
|---|---|---|---|---|
| H-I01 | Consistencia inter-documento / derivados | La tabla de contenidos del Cap 9 en `contenido/00-frontmatter.md:33` y `contenido-en/00-frontmatter.md:33` seguía diciendo «esquema Vergis · Botler · Mira» cuando el título de la sección pasó a «… · Daftar»; el residuo ya estaba en `_dist/web-*/index.html` y en los PDF | ES «esquema Vergis · Botler · Mira · Daftar»; EN «the Vergis · Botler · Mira · Daftar scheme»; rebuild de los cinco artefactos. Verificación A-01: `grep -c "Mira · Daftar" _dist/web-es/index.html _dist/web-en/index.html` → 1 y 1 | ✅ aplicado |
| H-M01 | Factual (etiqueta) | Cap 5 §2, glosario y manifiestos decían «modo práctica y modo medición»; en el artefacto el segundo modo se llama `exam` (`packages/daftar/src/instrumentos.ts:140`) | «práctica y examen (la medición)» en los seis lugares ES/EN | ✅ aplicado |
| H-M02 | Registros | El CHANGELOG v1.2 no mencionaba el frontmatter (v1.1→v1.2) ni las cabeceras de la trilogía (v1.0→v1.2, rancias desde la v1.1) | Bullet agregado a la entrada v1.2 | ✅ aplicado |
| H-M03 | Brief vs convención | El brief pedía glosario EN «en orden alfabético inglés»; el ejecutor espejó la posición ES, que es la convención verificada del archivo | Sin acción; se anota para que nadie lo «corrija» después | ℹ registrado |

## Verificado sin hallazgo

1. **Paridad ES/EN del delta**: los seis pares (Cap 5, Cap 9, glosario, frontmatter, manifiestos, trilogía) con los mismos bloques en el mismo lugar y la terminología fijada (capture / action / information / decision · Information Product (PI) · record). «Daftar» 13/13 en contenido, 7/7 en manifiestos.
2. **Consistencia inter-documento**: cero menciones a «tres familias / three families» en todo el corpus; ninguna sede clasifica la ingestión como actuación; ninguna llama a Mira «el único» proto-Botlet; `vergis.md` («al menos un proto-Botlet platafórmico… MUST») sigue válido con dos.
3. **Glosarios**: entradas nuevas presentes en ES y EN en posición espejo; «Ver:» cruzados coherentes y todos los títulos citados existen.
4. **Derivados**: `_dist/AgencyDomains-v1.2-{humanos,agentes,en}.{md,pdf}`, `web-es/`, `web-en/` y los dos manifiestos unificados de la trilogía dicen «AgencyDomains v1.2»; sin `v1.1` fuera de las menciones históricas.
5. **Versionado y registro**: frontmatter ES/EN en v1.2 en sus tres apariciones; sin rastros evolutivos en el cuerpo; no existe tag `agencydomains-v1.1` (la v1.2 acumula la v1.1); el ADR nuevo calca el formato del existente y registra el origen en un artefacto real (Daftar, Vergis 0.27.0).
6. **Factual contra Vergis**: lo que el libro afirma de Daftar calca `vergis/CHANGELOG.md` 0.27.0 (segunda familia junto a Mira; Let evaluador por instancia; misma interfaz del runtime) e `instrumentos.ts:127` (instrumento publicado inmutable).

## Decisiones de figura, registradas

El caption de g49 («Vergis · Botler · Mira — tipo vs nombre propio») **no** es hallazgo: la regla append-only de figuras y el ADR de la v1.2 dejan el esquema en tres mientras la tabla lleva cuatro filas. Una g5x con Daftar es candidata para una revisión Z futura.

• *Generado con Wingworking*
