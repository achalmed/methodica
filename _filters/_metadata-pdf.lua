-- _filters/_metadata-pdf.lua
-- Filtro minimalista para metadata PDF

function Meta(meta)
  local title = pandoc.utils.stringify(meta.title or "")
  local author = "Autor"

  if meta.author and type(meta.author) == "table" and #meta.author > 0 then
    local first = meta.author[1]
    if type(first) == "table" and first.name then
      author = pandoc.utils.stringify(first.name)
    end
  end

  -- Solo escapar tildes, nada más
  local function escape_tildes(str)
    local t = {
      ["á"] = "\\'{a}",
      ["é"] = "\\'{e}",
      ["í"] = "\\'{\\i}",
      ["ó"] = "\\'{o}",
      ["ú"] = "\\'{u}",
      ["ñ"] = "\\~{n}",
      ["Á"] = "\\'{A}",
      ["É"] = "\\'{E}",
      ["Í"] = "\\'{\\I}",
      ["Ó"] = "\\'{O}",
      ["Ú"] = "\\'{U}",
      ["Ñ"] = "\\~{N}",
    }
    for k, v in pairs(t) do
      str = str:gsub(k, v)
    end
    return str
  end

  local header = string.format([[
\hypersetup{
  pdftitle={%s},
  pdfauthor={%s}
}
]], escape_tildes(title), escape_tildes(author))

  if not meta['header-includes'] then
    meta['header-includes'] = pandoc.MetaList {}
  end
  table.insert(meta['header-includes'], pandoc.RawBlock('latex', header))

  return meta
end
