-- _metadata-pdf.lua
-- Filtro para inyectar metadatos del YAML al PDF automáticamente

function Meta(meta)
  -- Extraer valores del metadata del documento
  local title = pandoc.utils.stringify(meta.title or "")
  local abstract = pandoc.utils.stringify(meta.abstract or "")
  
  -- Convertir keywords de lista a string separado por comas
  local keywords = ""
  if meta.keywords then
    local kw_list = {}
    for _, kw in ipairs(meta.keywords) do
      table.insert(kw_list, pandoc.utils.stringify(kw))
    end
    keywords = table.concat(kw_list, ", ")
  end
  
  -- Si existe keywords-string, usarlo en su lugar
  if meta['keywords-string'] then
    keywords = pandoc.utils.stringify(meta['keywords-string'])
  end
  
  -- Crear bloque LaTeX con hypersetup
  local header = string.format([[
\usepackage{hyperref}
\hypersetup{
  pdftitle={%s},
  pdfauthor={Edison Achalma},
  pdfsubject={%s},
  pdfkeywords={%s},
  unicode=true,
  colorlinks=true,
  linkcolor=blue,
  citecolor=blue,
  urlcolor=blue,
  pdfcreator={Quarto},
  pdflang={es}
}
]], title, abstract, keywords)
  
  -- Agregar al header-includes
  if not meta['header-includes'] then
    meta['header-includes'] = pandoc.MetaList{}
  end
  table.insert(meta['header-includes'], pandoc.RawBlock('latex', header))
  
  return meta
end