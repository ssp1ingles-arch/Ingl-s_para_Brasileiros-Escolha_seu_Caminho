"""Gera um painel de livro no template do S17/S18/S19 a partir de um arquivo de seções.

Uso: python tmp/pdfs/_mk.py config.json
O JSON traz: out, title, eyebrow, h1, lead, metrics [[valor,rotulo],...],
placeholder, back, footer, sections (caminho do arquivo com as <section>).
As métricas de "itens" usam id=m-total e são contadas pelo próprio JS da página.
"""
from __future__ import annotations

import io
import json
import re
import sys
from pathlib import Path

CSS = """:root{--bg:#0a0a0a;--surface:#141414;--surface2:#1b1b1b;--border:#242424;--text:#e5e5e5;--muted:#8a8a8a;--dim:#5a5a5a;--accent:#22C55E;}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{background:var(--bg);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;overflow-x:hidden;line-height:1.6;padding-top:58px;}
.bg-glow{position:fixed;inset:0;pointer-events:none;z-index:0;}
.bg-glow::before{content:'';position:absolute;top:-12%;left:8%;width:46%;height:55%;background:radial-gradient(ellipse,color-mix(in srgb,var(--accent) 8%,transparent),transparent 70%);border-radius:50%;}
.wrap{position:relative;z-index:1;max-width:1180px;margin:0 auto;padding:0 22px;}
.back{position:fixed;top:10px;left:12px;z-index:1000;display:inline-flex;align-items:center;gap:.4rem;min-height:44px;padding:0 18px;font-family:'Space Grotesk',sans-serif;font-size:.9rem;font-weight:600;color:var(--text);text-decoration:none;background:rgba(18,18,18,.88);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border:1px solid var(--border);border-radius:30px;box-shadow:0 4px 16px rgba(0,0,0,.45);transition:border-color .2s,color .2s;}
.back:hover{color:var(--accent);border-color:var(--accent);}
.eyebrow{font-family:'Space Grotesk',sans-serif;font-size:.72rem;font-weight:800;letter-spacing:.18em;color:var(--accent);text-transform:uppercase;margin-top:34px;}
h1.title{font-family:'Space Grotesk',sans-serif;font-size:clamp(1.9rem,4.6vw,2.9rem);font-weight:800;line-height:1.08;margin:12px 0;}
h1.title em{font-style:normal;color:var(--accent);}
.lead{color:var(--muted);max-width:760px;line-height:1.6;}
.lead a{color:var(--accent);}
.metrics{display:flex;gap:26px;flex-wrap:wrap;margin:22px 0 6px;}
.metric b{font-family:'Space Grotesk',sans-serif;font-size:1.6rem;display:block;color:var(--text);}
.metric span{font-size:.76rem;color:var(--dim);text-transform:uppercase;letter-spacing:.05em;}

/* BUSCA */
.searchbar{position:sticky;top:0;z-index:900;margin:26px 0 6px;padding:12px 0;background:linear-gradient(to bottom,var(--bg) 72%,transparent);}
.searchbox{display:flex;align-items:center;gap:10px;background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:11px 15px;transition:border-color .2s;}
.searchbox:focus-within{border-color:var(--accent);}
.searchbox svg{flex:none;width:17px;height:17px;stroke:var(--muted);fill:none;stroke-width:2;}
.searchbox input{flex:1;background:none;border:none;outline:none;color:var(--text);font-family:'Inter',sans-serif;font-size:.97rem;min-width:0;}
.searchbox input::placeholder{color:var(--dim);}
.searchbox button{flex:none;background:var(--surface2);border:1px solid var(--border);color:var(--muted);border-radius:7px;padding:4px 10px;font-family:'Space Grotesk',sans-serif;font-size:.74rem;font-weight:700;cursor:pointer;display:none;}
.searchbox button:hover{color:var(--accent);border-color:var(--accent);}
.searchbox.has-q button{display:block;}
.searchinfo{font-family:'Space Grotesk',sans-serif;font-size:.78rem;color:var(--dim);padding:8px 4px 0;min-height:20px;}
.searchinfo b{color:var(--accent);}
mark{background:color-mix(in srgb,var(--accent) 30%,transparent);color:var(--text);border-radius:3px;padding:0 2px;}

/* LAYOUT */
.layout{display:grid;grid-template-columns:250px 1fr;gap:38px;align-items:start;margin:14px 0 0;}
.toc{position:sticky;top:76px;max-height:calc(100vh - 96px);overflow-y:auto;padding-right:6px;}
.toc h3{font-family:'Space Grotesk',sans-serif;font-size:.7rem;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--dim);margin-bottom:12px;}
.toc a{display:block;color:var(--muted);text-decoration:none;font-size:.85rem;padding:5px 0 5px 11px;border-left:2px solid var(--border);line-height:1.35;transition:color .15s,border-color .15s;}
.toc a:hover,.toc a.on{color:var(--accent);border-left-color:var(--accent);}
.toc::-webkit-scrollbar{width:5px;}
.toc::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px;}

/* SECOES */
section{margin:0 0 46px;scroll-margin-top:86px;}
.snum{font-family:'Space Grotesk',sans-serif;font-size:.7rem;font-weight:800;letter-spacing:.15em;color:var(--accent);text-transform:uppercase;}
section h2{font-family:'Space Grotesk',sans-serif;font-size:1.42rem;font-weight:800;margin:5px 0 8px;line-height:1.2;}
.sdesc{color:var(--muted);font-size:.93rem;margin-bottom:16px;max-width:760px;}
.sdesc b{color:var(--text);font-weight:600;}
.sdesc code{background:var(--surface2);border:1px solid var(--border);border-radius:4px;padding:1px 6px;font-size:.86em;color:var(--accent);}

.items{display:flex;flex-direction:column;gap:9px;}
.i{background:var(--surface);border:1px solid var(--border);border-left:2px solid var(--border);border-radius:0 10px 10px 0;padding:13px 16px;transition:border-left-color .15s;}
.i:hover{border-left-color:var(--accent);}
.en{font-size:1rem;font-weight:500;line-height:1.5;}
.en i{color:var(--accent);font-style:normal;font-weight:600;}
.pt{color:var(--muted);font-size:.89rem;margin-top:4px;line-height:1.5;}
.def{color:var(--dim);font-size:.83rem;margin-top:3px;line-height:1.45;font-style:italic;}
.tag{display:inline-block;font-family:'Space Grotesk',sans-serif;font-size:.63rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--dim);background:var(--surface2);border:1px solid var(--border);border-radius:5px;padding:2px 7px;margin-bottom:6px;}

/* TABELAS */
.tablewrap{overflow-x:auto;border:1px solid var(--border);border-radius:10px;margin:4px 0 12px;}
table{width:100%;border-collapse:collapse;font-size:.9rem;min-width:400px;}
th{background:var(--surface2);text-align:left;font-family:'Space Grotesk',sans-serif;font-size:.72rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:var(--accent);padding:10px 13px;border-bottom:1px solid var(--border);white-space:nowrap;}
td{padding:9px 13px;border-bottom:1px solid var(--border);vertical-align:top;}
tr:last-child td{border-bottom:none;}
tbody tr:hover{background:rgba(255,255,255,.02);}
td.w{color:var(--muted);}
td b{font-weight:600;}
.x{color:#f87171;}
.ok{color:var(--accent);}

.empty{display:none;text-align:center;color:var(--muted);padding:44px 20px;border:1px dashed var(--border);border-radius:14px;}
.empty b{display:block;color:var(--text);font-family:'Space Grotesk',sans-serif;font-size:1.05rem;margin-bottom:6px;}
footer{position:relative;z-index:1;text-align:center;color:var(--dim);font-family:'Space Grotesk',sans-serif;font-size:.74rem;padding:44px 20px 40px;letter-spacing:.04em;}

@media(max-width:900px){
  .layout{grid-template-columns:1fr;gap:20px;}
  .toc{position:static;max-height:none;border-bottom:1px solid var(--border);padding-bottom:14px;}
  .toc-list{display:flex;flex-wrap:wrap;gap:5px;}
  .toc a{border-left:none;border:1px solid var(--border);border-radius:7px;padding:5px 10px;font-size:.79rem;}
  .toc a.on{border-color:var(--accent);}
}
@media(max-width:600px){
  html,body{overflow-x:hidden;max-width:100vw;}
  body{font-size:16px;}
  .wrap{padding-left:15px;padding-right:15px;}
  .metrics{gap:14px 18px;}
  table{font-size:.85rem;}
}"""

JS = """(function(){
  const art=document.getElementById('art'), q=document.getElementById('q'), sbox=document.getElementById('sbox'),
        clr=document.getElementById('clr'), info=document.getElementById('info'), empty=document.getElementById('empty'),
        toclist=document.getElementById('toclist');
  const secs=[...art.querySelectorAll('section')];

  secs.forEach(s=>{
    const a=document.createElement('a');
    a.href='#'+s.id; a.textContent=s.querySelector('h2').textContent;
    toclist.appendChild(a);
  });
  const links=[...toclist.querySelectorAll('a')];

  const units=[];
  secs.forEach(s=>{
    s.querySelectorAll('.i, tbody tr').forEach(el=>{
      units.push({el, sec:s, txt:el.textContent.toLowerCase()});
    });
  });
  document.getElementById('m-total').textContent=units.length;

  const norm=s=>s.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');
  units.forEach(u=>u.norm=norm(u.txt));

  const wraps=[...art.querySelectorAll('.tablewrap')].map(w=>({
    el:w, rows:[...w.querySelectorAll('tbody tr')]
  }));

  function run(){
    const raw=q.value.trim();
    sbox.classList.toggle('has-q', raw.length>0);
    if(!raw){
      units.forEach(u=>u.el.style.display='');
      wraps.forEach(w=>w.el.style.display='');
      secs.forEach(s=>s.style.display='');
      empty.style.display='none';
      info.innerHTML='<b>'+units.length+'</b> itens em '+secs.length+' se\\u00e7\\u00f5es.';
      return;
    }
    const needle=norm(raw);
    let hits=0;
    const live=new Set();
    units.forEach(u=>{
      const on=u.norm.includes(needle);
      u.el.style.display=on?'':'none';
      if(on){hits++;live.add(u.sec);}
    });
    wraps.forEach(w=>{
      w.el.style.display=w.rows.some(r=>r.style.display!=='none')?'':'none';
    });
    secs.forEach(s=>{s.style.display=live.has(s)?'':'none';});
    empty.style.display=hits?'none':'block';
    info.innerHTML=hits
      ? '<b>'+hits+'</b> '+(hits===1?'item':'itens')+' em <b>'+live.size+'</b> '+(live.size===1?'se\\u00e7\\u00e3o':'se\\u00e7\\u00f5es')+' para &ldquo;'+raw.replace(/[<>&]/g,'')+'&rdquo;'
      : 'Nenhum resultado para &ldquo;'+raw.replace(/[<>&]/g,'')+'&rdquo;';
  }
  q.addEventListener('input',run);
  clr.addEventListener('click',()=>{q.value='';run();q.focus();});
  q.addEventListener('keydown',e=>{if(e.key==='Escape'){q.value='';run();}});
  run();

  const obs=new IntersectionObserver(es=>{
    es.forEach(e=>{
      if(e.isIntersecting){
        links.forEach(l=>l.classList.toggle('on', l.getAttribute('href')==='#'+e.target.id));
      }
    });
  },{rootMargin:'-80px 0px -70% 0px'});
  secs.forEach(s=>obs.observe(s));
})();"""


def build(cfg: dict) -> str:
    body = io.open(cfg["sections"], encoding="utf-8").read().strip()
    metrics = "\n".join(
        f'  <div class="metric"><b{" id=\'m-total\'" if v == "@" else ""}>{"&mdash;" if v == "@" else v}</b><span>{label}</span></div>'
        for v, label in cfg["metrics"]
    )
    toc_label = cfg.get("toc_label", "Seções")
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{cfg["title"]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
<div class="bg-glow"></div>
<a href="./index.html" class="back">&#8592; {cfg["back"]}</a>
<div class="wrap">

<div class="eyebrow">{cfg["eyebrow"]}</div>
<h1 class="title">{cfg["h1"]}</h1>
<p class="lead">{cfg["lead"]}</p>

<div class="metrics">
{metrics}
</div>

<div class="searchbar">
  <div class="searchbox" id="sbox">
    <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
    <input type="search" id="q" placeholder="{cfg["placeholder"]}" autocomplete="off" spellcheck="false">
    <button type="button" id="clr">limpar</button>
  </div>
  <div class="searchinfo" id="info"></div>
</div>

<div class="layout">
  <nav class="toc"><h3>{toc_label}</h3><div class="toc-list" id="toclist"></div></nav>
  <main class="article" id="art">

{body}

  </main>
</div>

<div class="empty" id="empty"><b>Nada encontrado</b>Tente outro termo &mdash; a busca cobre o inglês e o português de todos os itens e tabelas.</div>
</div>

<footer>{cfg["footer"]}</footer>

<script>
{JS}
</script>
</body>
</html>
"""


def main() -> int:
    cfg = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    html = build(cfg)
    out = Path(cfg["out"])
    out.write_text(html, encoding="utf-8", newline="\n")
    secs = len(re.findall(r"<section id=", html))
    items = len(re.findall(r'<div class="i">', html))
    rows = len(re.findall(r"<tr><td", html))
    print(f"{out}: {secs} seções, {items} itens, {rows} linhas de tabela, {len(html.encode('utf-8'))} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
