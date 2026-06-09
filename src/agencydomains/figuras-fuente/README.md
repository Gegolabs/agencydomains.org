# Fuentes de las figuras

Cada figura del libro es un **HTML autocontenido** (+ `_base.css` compartido) que se
renderiza a PNG con Chrome headless:

```bash
./render.sh                      # renderiza las 51 figuras → ../figuras/
./render.sh g10-cuatro-capas     # renderiza una sola
```

La salida va directo a `../figuras/` (los PNG que embebe el libro). Para corregir una
figura: editar su `.html`, renderizar, y committear ambos (fuente y PNG).

**Pendiente:** versiones en inglés de las 51 figuras (hoy el texto interno está en español).
