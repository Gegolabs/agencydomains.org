#!/bin/zsh
# Renderiza todos los HTML de figuras a PNG via Chrome headless.
# Uso: ./render.sh [nombre-fig-sin-extension]   (omitir = renderiza todos)

set -e
cd "$(dirname "$0")"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HTML_DIR="$(pwd)"
OUT_DIR="$(pwd)/../figuras"
SIZE="1600,1000"

render_one() {
  local name="$1"
  local html="$HTML_DIR/${name}.html"
  local png="$OUT_DIR/${name}.png"
  [ ! -f "$html" ] && { echo "skip: $html no existe"; return; }
  echo "→ $name"
  "$CHROME" \
    --headless=new \
    --disable-gpu \
    --hide-scrollbars \
    --window-size=$SIZE \
    --default-background-color=00000000 \
    --screenshot="$png" \
    "file://$html" 2>/dev/null
}

if [ -n "$1" ]; then
  render_one "$1"
else
  for f in "$HTML_DIR"/f*.html; do
    name="$(basename "$f" .html)"
    render_one "$name"
  done
fi

echo "OK · imágenes en $OUT_DIR"
