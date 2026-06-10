# Correcciones aplicadas — Auditoría del libro AURA v0.1

Resolución del inventario `auditoria-libro-aura-v0.1.md` (58 hallazgos). Fecha: 2026-06-09.

## Mecanismo adoptado para la duplicación spec↔libro (H-I06, H-I09, H-I13)

**Marcadores condicionales** resueltos por `_build/concat.sh` al ensamblar:
`<!-- standalone -->…<!-- /standalone -->` (vive solo en la spec autónoma) y
`<!-- libro … /libro -->` (vive solo en el libro — puentes de capítulo). Aplicado en
IRIS (4 bloques: tesis compartida, definición empresa en línea/tiempo real, dos
referencias a la Visión como documento externo) y MOTOR (2 bloques: nota de versión
AOMM, referencia a la Visión). Una sola fuente, dos lecturas correctas.

## Resueltos (52)

- **CRITICOS**: H-C01 (7 construcciones "del «…»" reescritas) · H-C02 (referencia
  corrupta eliminada) · H-C03 (9 refs a archivos del cluster eliminadas; sección
  "Documentos del cluster" reemplazada por nota única sin nombres) · H-C04
  (**anonimización**: Hijuelas/A.R.B.O.L. → "holding agroindustrial multinacional";
  cifras internas generalizadas) · H-C05 (figura a `specs/figuras/` + `build-pdf.sh`
  con `--resource-path`; embebida verificada) · H-C06 (composición de la SV #1
  corregida contra inventario, también en el ejemplo introductorio).
- **IMPORTANTES**: todos salvo los listados abajo — incluye prefacio sin numeración
  fantasma, bullets de Datos de contexto alineados (2027/causas/48%), CAGR ≈39%,
  etapa/nivel precisado (Nivel IV, etapas 7–8), Fuentes depuradas (−7 no citadas,
  +2 citadas, anclas con dominio), agéntica→agentiva en Data Canon, puente
  terminológico en Wingmap, apéndices del capítulo renombrados/eliminados,
  Wingworking ×8, fases de Wingmap (previa + cinco operativas, sin ordinales),
  regla de iteraciones reformulada, "el cliente"→"la organización" (~25),
  ProcessBench → estimación del autor, SV #2 y áreas corregidas, headers del anexo
  a MOTOR, nota introductoria del anexo ampliada (CU-NEW, escala, leyenda A–D),
  ROI del anexo (campo N/A eliminado; total calificado).
- **MENORES**: subtítulos H1→cursiva (×5), pies de spec eliminados (×2), sumas de
  mercado ajustadas, nomenclatura de niveles homologada (ES + EN como etiqueta),
  glosario +Marketplace de Agentes, assessment p3 corregida, "esta visión"→"este
  libro" (×5), emoji en code block, convergencia promovida, y el resto de pulidos
  léxicos/narrativos del inventario.
- **Extra**: fallback Unicode `★` agregado al header LaTeX compartido (beneficia a
  ambos libros).

## Aceptados como diseño (6)

| Hallazgo | Decisión |
|---|---|
| H-C07 prólogo placeholder | Pendiente declarado (prologuista invitado); bloqueante de publicación, no de borrador. |
| M-05 prefacio ↔ intros de parte | El eco es deliberado: mapa vs puerta de entrada. |
| M-06 "siempre debieron estar" | Licencia retórica de cierre, consciente. |
| M-17 autorreferencia "paper" | Los capítulos-paper conservan su voz (el frontmatter declara la heterogeneidad); revisitar en la homogeneización de v0.2. |
| P3 resúmenes de referencia rápida (IRIS/MOTOR) | Conservados como vistas de consulta; evaluar en v0.2. |
| M-15/M-16 parcialmente | Paráfrasis aplicada; la coletilla "anclada…" variada solo fuera de definiciones. |

---

• *Generado con [Wingworking](https://wingworking.org)*
