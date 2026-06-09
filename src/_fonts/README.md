# Fuentes del libro (vendorizadas)

Tipografías con las que se componen los PDFs, fijadas aquí para que el build sea
idéntico en cualquier máquina (CI o local). Todas bajo **SIL Open Font License 1.1**
(ver licencia en cada directorio), que permite esta redistribución.

| Familia | Rol | Origen |
|---|---|---|
| STIX Two Text | cuerpo | TeX Live `stix2-otf` (stipub/stixfonts) |
| STIX Two Math | matemática y fallbacks Unicode | ídem |
| Source Code Pro | monoespaciada (código) | adobe-fonts/source-code-pro |

Instalación (lo hace el workflow de publicación; para un build local, una vez):

```bash
# Linux:  cp src/_fonts/*/*.otf ~/.local/share/fonts/ && fc-cache -f
# macOS:  cp src/_fonts/*/*.otf ~/Library/Fonts/
```
