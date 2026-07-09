-- ============================================================================
-- apa-floats-html.lua — Formato APA para figuras y tablas en la salida HTML
-- ============================================================================
-- Propósito : Replicar en el formato `html` del sitio el comportamiento que
--             apaquarto aplica en PDF/DOCX/HTML propio, sin tocar _extensions/:
--               Figura N        (etiqueta)
--               Título          (cursiva)
--               (imagen/tabla)
--               Nota. ...       (nota al pie del float, desde apa-note="...")
-- Etapa     : post-render (se declara con `at: post-render` en el YAML del
--             documento). En esta etapa Quarto ya resolvió los crossrefs: el
--             float llega como Div#fig-…/#tbl-… > Figure, cuyo caption es
--             "Figura 1: Título" / "Tabla 1: Título".
-- Uso       : en el front matter del post:
--               format:
--                 html:
--                   filters:
--                     - at: post-render
--                       path: ../../../_filters/apa-floats-html.lua
-- Estilos   : assets/scss/04-components/_floats.scss (.apa-float-label,
--             .apa-float-title, .apa-float-note).
-- Referencia: _extensions/wjschne/apaquarto/{apacaption,apanote}.lua
-- ============================================================================

if FORMAT ~= "html" and FORMAT ~= "html5" then
  return {}
end

-- Palabras según el idioma del sitio (es: Figura/Tabla/Nota). En la etapa
-- post-render Quarto ya consumió `meta.language`, así que se derivan de
-- `lang`, con `language.*` como override si aún estuviera presente.
local figureword = "Figure"
local tableword  = "Table"
local noteword   = "Note"

local function getwords(m)
  local lang = m.lang and pandoc.utils.stringify(m.lang) or ""
  if lang:sub(1, 2) == "es" then
    figureword = "Figura"
    tableword  = "Tabla"
    noteword   = "Nota"
  end
  if m.language then
    if m.language["crossref-fig-title"] then
      figureword = pandoc.utils.stringify(m.language["crossref-fig-title"])
    end
    if m.language["crossref-tbl-title"] then
      tableword = pandoc.utils.stringify(m.language["crossref-tbl-title"])
    end
    if m.language["figure-table-note"] then
      noteword = pandoc.utils.stringify(m.language["figure-table-note"])
    end
  end
end

-- ¿La cadena empieza con "Figura 1:" / "Tabla 1:" (espacio normal o nbsp)?
local function starts_as_caption(s, word)
  local esc = word:gsub("%W", "%%%0")
  -- \194\160 son los bytes UTF-8 del no-break space que inserta Quarto
  return s:find("^" .. esc .. "[%s\194\160]*%d+%a?:") ~= nil
end

-- ¿Los inlines forman "Figura 1: Título" / "Tabla 1: Título"?
-- Devuelve (label_inlines, title_inlines) o nil. Tolera que el prefijo llegue
-- como un solo Str ("Tabla\u{a0}1:") o repartido en varios inlines.
local function split_caption_inlines(inls)
  if not inls or #inls == 0 then return nil end
  local s = pandoc.utils.stringify(inls)
  if not (starts_as_caption(s, figureword) or starts_as_caption(s, tableword)) then
    return nil
  end
  -- localizar el primer Str que contenga ":" (el separador etiqueta/título)
  for i, el in ipairs(inls) do
    if el.t == "Str" then
      local pos = string.find(el.text, ":", 1, true)
      if pos then
        local before = el.text:sub(1, pos - 1)
        local after  = el.text:sub(pos + 1)

        local label = pandoc.Inlines({})
        for j = 1, i - 1 do label:insert(inls[j]) end
        if before ~= "" then label:insert(pandoc.Str(before)) end

        local title = pandoc.Inlines({})
        if after ~= "" then title:insert(pandoc.Str(after)) end
        for j = i + 1, #inls do title:insert(inls[j]) end
        while #title > 0 and (title[1].t == "Space" or title[1].t == "SoftBreak") do
          title:remove(1)
        end

        if #label == 0 or #title == 0 then return nil end
        return label, title
      end
    end
  end
  return nil
end

-- Reemplaza, en cualquier nivel del float, el caption "Palabra N: Título"
-- por los bloques APA (etiqueta + título en cursiva). El caption vive como
-- Plain dentro de los divs .quarto-scaffold que forman el <figcaption>.
-- Devuelve los bloques transformados y true si hubo cambio.
local function apply_caption(blocks)
  local changed = false
  local walked = blocks:walk {
    Plain = function(p)
      if changed then return nil end
      local label, title = split_caption_inlines(p.content)
      if label then
        changed = true
        local labeldiv = pandoc.Div(pandoc.Plain(label))
        labeldiv.classes:insert("apa-float-label")
        local titlediv = pandoc.Div(pandoc.Plain({ pandoc.Emph(title) }))
        titlediv.classes:insert("apa-float-title")
        return { labeldiv, titlediv }
      end
      return nil
    end
  }
  return walked, changed
end

-- Crea el bloque "Nota. …" a partir del texto de apa-note (admite markdown).
local function make_note(notetext)
  local inls = quarto.utils.string_to_inlines(notetext)
  local content = pandoc.Inlines({ pandoc.Emph(pandoc.Str(noteword .. ".")), pandoc.Space() })
  content:extend(inls)
  local notediv = pandoc.Div(pandoc.Para(content))
  notediv.classes:insert("apa-float-note")
  return notediv
end

-- El Div exterior (#fig-… / #tbl-…) contiene el caption (anidado en los
-- scaffolds) y lleva el atributo apa-note; la nota se añade al final del
-- float, después de la imagen o tabla.
local function div(el)
  local id = el.identifier or ""
  if not (string.find(id, "^tbl%-") or string.find(id, "^fig%-")) then
    return nil
  end

  local walked, changed = apply_caption(el.content)
  if changed then el.content = walked end

  -- apa-note puede llegar en el Div exterior o en la imagen/tabla interior
  local note = el.attributes["apa-note"]
  if not note then
    el.content:walk {
      Image = function(img)
        if img.attributes["apa-note"] then note = img.attributes["apa-note"] end
        return img
      end,
      Table = function(tbl)
        if tbl.attr and tbl.attr.attributes["apa-note"] then
          note = tbl.attr.attributes["apa-note"]
        end
        return tbl
      end
    }
  end

  if note then
    el.content:insert(make_note(note))
    el.attributes["apa-note"] = nil
    el.content = el.content:walk {
      Image = function(img)
        img.attributes["apa-note"] = nil
        return img
      end,
      Table = function(tbl)
        if tbl.attr then tbl.attr.attributes["apa-note"] = nil end
        return tbl
      end
    }
    changed = true
  end

  if changed then return el end
end

return {
  { Meta = getwords },
  { Div = div }
}
