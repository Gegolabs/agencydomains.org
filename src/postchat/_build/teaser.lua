-- Envuelve los divs ::: cajateaser ::: en el entorno LaTeX homónimo
-- (definido en header-fusion.tex), preservando el Markdown del contenido.
-- El atributo comentario="…" viaja como argumento del entorno y termina
-- montado sobre el borde inferior de la caja.
function Div(el)
  if el.classes:includes('cajateaser') then
    local com = el.attributes['comentario'] or ''
    local blocks = pandoc.List({
      pandoc.RawBlock('latex', '\\begin{cajateaser}{' .. com .. '}')
    })
    blocks:extend(el.content)
    blocks:insert(pandoc.RawBlock('latex', '\\end{cajateaser}'))
    return blocks
  end
end
