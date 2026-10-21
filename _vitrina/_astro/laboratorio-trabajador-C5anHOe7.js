(function(){let e=null;async function t({pyodide:t,base:n,archivos:r,disciplina:i,modulo:a}){let o=performance.now();self.postMessage({tipo:`avance`,fase:`pyodide`}),importScripts(`${t}pyodide.js`);let s=()=>{},c=await self.loadPyodide({indexURL:t,stdout:s,stderr:s});self.postMessage({tipo:`avance`,fase:`numpy`}),await c.loadPackage(`numpy`,{messageCallback:s,errorCallback:s}),self.postMessage({tipo:`avance`,fase:`modelo`});let l=await Promise.all(r.map(async e=>{let t=await fetch(new URL(e,n));if(!t.ok)throw Error(`no se pudo leer ${e} (${t.status})`);return[e,await t.text()]}));for(let[e,t]of l){let n=`/lab/${e}`;c.FS.mkdirTree(n.slice(0,n.lastIndexOf(`/`))),c.FS.writeFile(n,t)}c.globals.set(`_disciplina`,i),c.globals.set(`_modulo`,a),c.runPython(`
import importlib, sys
sys.path[:0] = ['/lab/' + _disciplina, '/lab']
import navegador
navegador.preparar()
_MODELO = importlib.import_module(_modulo).MODELO
_calcular = lambda s: navegador.calcular_json(_MODELO, s)
`),e=c.globals.get(`_calcular`),self.postMessage({tipo:`listo`,ms:Math.round(performance.now()-o)})}self.onmessage=async n=>{let r=n.data;try{if(r.tipo===`iniciar`)await t(r);else if(r.tipo===`calcular`&&e){let t=performance.now(),n=JSON.parse(e(JSON.stringify(r.valores??{})));self.postMessage({tipo:`resultado`,id:r.id,datos:n,ms:Math.round(performance.now()-t)})}}catch(e){self.postMessage({tipo:`error`,mensaje:String(e?.message??e).split(`
`).slice(-3).join(` `)})}}})();