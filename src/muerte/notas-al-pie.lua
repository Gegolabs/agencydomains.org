-- Convierte cada nota de Pandoc en un span que WeasyPrint lleva al pie de su página (float: footnote).
function Note(el)
  local html = pandoc.write(pandoc.Pandoc(el.content), 'html')
  html = html:gsub('^%s*<p>', ''):gsub('</p>%s*$', ''):gsub('</p>%s*<p>', ' ')
  return pandoc.RawInline('html', '<span class="fn">' .. html .. '</span>')
end
