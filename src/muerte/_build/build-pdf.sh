#!/bin/bash
# Construye el PDF del Libro I, La muerte del software como lo conocemos (edición ES).
set -euo pipefail
bash "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/libro.sh" es
