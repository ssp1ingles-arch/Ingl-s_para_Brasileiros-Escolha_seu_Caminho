#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mkpanel.py — gera, amplia e valida os paineis `livroNN.html` dos Sistemas
avancados (S20, S21 e S22), que seguem o REGRAS_AVANCADO.md.

Existe porque os paineis avancados tem um contrato que e facil de quebrar
na mao: acento dourado #F59E0B, um `<section>` por bloco de gramatica, um
`<div class="i">` por item, e um minimo de conteudo por painel. O script
trava a gravacao se o minimo nao for atingido — e melhor falhar aqui do
que publicar painel raso e so descobrir na auditoria.

MINIMOS (REGRAS_AVANCADO + regra da sessao de 2026-08-04):
    12 blocos e 150 itens por painel.

USO
    python mkpanel.py check  <painel.html>
        Conta blocos e itens do painel e sai com 1 se estiver abaixo do minimo.

    python mkpanel.py append <painel.html> <spec.json>
        Acrescenta as secoes do spec ao painel existente, logo antes de
        </main>, renumerando os ids (s01, s02, ...) na sequencia, e
        atualiza a metrica de blocos do cabecalho. Valida o minimo ANTES
        de gravar; se nao passar, nada e escrito.

    python mkpanel.py build  <painel.html> <spec.json>
        Gera um painel novo do zero a partir do spec (chaves extras:
        sistema, livro, titulo, subtitulo, lead, nivel, padrao, footer,
        placeholder, voltar).

FORMATO DO SPEC (JSON, UTF-8)
{
  "secoes": [
    {
      "snum": "Negativas",                  # rotulo curto (aparece no TOC)
      "h2":   "<i>Not</i> ou <i>no</i>?",   # titulo do bloco (HTML inline ok)
      "sdesc": "Explicacao do bloco.",      # HTML inline ok
      "itens": [
        {"tag": "o erro",                   # opcional
         "tagtipo": "err",                  # opcional: "" | "err" | "reg"
         "en": "Frase real em ingles.",     # obrigatorio
         "pt": "Traducao.",                 # obrigatorio
         "def": "Nota de uso/registro."}    # opcional
      ]
    }
  ]
}

Convencoes de marcacao dentro de "en" (herdadas do CSS do painel):
    <i>...</i>  = destaque dourado na estrutura estudada
    <s>...</s>  = forma ERRADA (riscada em vermelho)
    <u>...</u>  = sublinhado dourado
    ·           = separador entre exemplos dentro do mesmo item
    ×           = confronto entre duas estruturas
"""

import json
import re
import sys
from pathlib import Path

MIN_BLOCOS = 12
MIN_ITENS = 150

ACCENT = "#F59E0B"

RE_SECTION = re.compile(r'<section id="s\d+">')
RE_ITEM = re.compile(r'<div class="i">')
RE_METRIC_BLOCOS = re.compile(r'(<div class="metric"><b>)\d+(</b><span>blocos</span></div>)')


# ---------------------------------------------------------------- contagem

def contar(html):
    """Retorna (blocos, itens) de um painel ja renderizado."""
    return len(RE_SECTION.findall(html)), len(RE_ITEM.findall(html))


def validar(blocos, itens, alvo):
    """Trava se o painel ficar abaixo do minimo. Nada e gravado sem passar aqui."""
    assert blocos >= MIN_BLOCOS, (
        f"{alvo}: {blocos} blocos — minimo e {MIN_BLOCOS}. "
        f"Volte ao .md e recorte mais {MIN_BLOCOS - blocos} bloco(s)."
    )
    assert itens >= MIN_ITENS, (
        f"{alvo}: {itens} itens — minimo e {MIN_ITENS}. "
        f"Faltam {MIN_ITENS - itens}. Painel raso nao entra."
    )


# ---------------------------------------------------------------- render

def render_item(it):
    if "en" not in it or "pt" not in it:
        raise ValueError(f"item sem 'en' ou 'pt': {it!r}")
    partes = ['<div class="i">']
    if it.get("tag"):
        tipo = it.get("tagtipo", "")
        cls = f"tag {tipo}".strip()
        partes.append(f'<span class="{cls}">{it["tag"]}</span>')
    partes.append(f'<div class="en">{it["en"]}</div>')
    partes.append(f'<div class="pt">{it["pt"]}</div>')
    if it.get("def"):
        partes.append(f'<div class="def">{it["def"]}</div>')
    partes.append("</div>")
    return "".join(partes)


def render_secao(sec, idx):
    if not sec.get("itens"):
        raise ValueError(f"secao '{sec.get('h2', '?')}' sem itens")
    linhas = [
        f'<section id="s{idx:02d}">',
        f'<div class="snum">{sec["snum"]}</div>',
        f'<h2>{sec["h2"]}</h2>',
        f'<p class="sdesc">{sec["sdesc"]}</p>',
        '<div class="items">',
    ]
    linhas += [render_item(i) for i in sec["itens"]]
    linhas += ["</div>", "</section>", ""]
    return "\n".join(linhas)


def render_secoes(secoes, inicio=1):
    return "\n".join(render_secao(s, inicio + n) for n, s in enumerate(secoes))


# ---------------------------------------------------------------- append

def append(caminho, spec_path):
    alvo = Path(caminho)
    html = alvo.read_text(encoding="utf-8")
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    secoes = spec["secoes"]

    ja = len(RE_SECTION.findall(html))
    if ja == 0:
        raise SystemExit(f"{alvo}: nenhum <section id=\"sNN\"> encontrado — use 'build'.")
    if "</main>" not in html:
        raise SystemExit(f"{alvo}: sem </main> — estrutura inesperada.")

    novo = render_secoes(secoes, inicio=ja + 1)
    html = html.replace("  </main>", novo + "\n  </main>", 1)

    blocos, itens = contar(html)
    html = RE_METRIC_BLOCOS.sub(rf"\g<1>{blocos}\g<2>", html, count=1)

    validar(blocos, itens, alvo.name)
    alvo.write_text(html, encoding="utf-8")
    print(f"{alvo.name}: +{len(secoes)} blocos  ->  {blocos} blocos / {itens} itens")
    return blocos, itens


# ---------------------------------------------------------------- build

CSS = """:root{--bg:#0a0a0a;--surface:#141414;--surface2:#1b1b1b;--border:#242424;--text:#e5e5e5;--muted:#8a8a8a;--dim:#5a5a5a;--accent:%s;}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{background:var(--bg);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;overflow-x:hidden;line-height:1.6;padding-top:58px;}
.bg-glow{position:fixed;inset:0;pointer-events:none;z-index:0;}
.bg-glow::before{content:'';position:absolute;top:-12%%;left:8%%;width:46%%;height:55%%;background:radial-gradient(ellipse,color-mix(in srgb,var(--accent) 8%%,transparent),transparent 70%%);border-radius:50%%;}
.wrap{position:relative;z-index:1;max-width:1180px;margin:0 auto;padding:0 22px;}
.back{position:fixed;top:10px;left:12px;z-index:1000;display:inline-flex;align-items:center;gap:.4rem;min-height:44px;padding:0 18px;font-family:'Space Grotesk',sans-serif;font-size:.9rem;font-weight:600;color:var(--text);text-decoration:none;background:rgba(18,18,18,.88);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border:1px solid var(--border);border-radius:30px;box-shadow:0 4px 16px rgba(0,0,0,.45);transition:border-color .2s,color .2s;}
.back:hover{color:var(--accent);border-color:var(--accent);}
.eyebrow{font-family:'Space Grotesk',sans-serif;font-size:.72rem;font-weight:800;letter-spacing:.18em;color:var(--accent);text-transform:uppercase;margin-top:34px;}
h1.title{font-family:'Space Grotesk',sans-serif;font-size:clamp(1.9rem,4.6vw,2.9rem);font-weight:800;line-height:1.08;margin:12px 0;}
h1.title em{font-style:normal;color:var(--accent);}
.lead{color:var(--muted);max-width:760px;line-height:1.6;}
.lead b{color:var(--text);font-weight:600;}
.lead i{color:var(--accent);font-style:normal;}
.metrics{display:flex;gap:26px;flex-wrap:wrap;margin:22px 0 6px;}
.metric b{font-family:'Space Grotesk',sans-serif;font-size:1.6rem;display:block;color:var(--text);}
.metric span{font-size:.76rem;color:var(--dim);text-transform:uppercase;letter-spacing:.05em;}

/* BUSCA */
.searchbar{position:sticky;top:0;z-index:900;margin:26px 0 6px;padding:12px 0;background:linear-gradient(to bottom,var(--bg) 72%%,transparent);}
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
.sdesc i{color:var(--accent);font-style:normal;}

.items{display:flex;flex-direction:column;gap:9px;}
.i{background:var(--surface);border:1px solid var(--border);border-left:2px solid var(--border);border-radius:0 10px 10px 0;padding:13px 16px;transition:border-left-color .15s;}
.i:hover{border-left-color:var(--accent);}
.en{font-size:1rem;font-weight:500;line-height:1.5;}
.en i{color:var(--accent);font-style:normal;font-weight:600;}
.en s{color:var(--dim);text-decoration-color:#f87171;}
.en u{text-decoration:none;border-bottom:2px solid var(--accent);}
.pt{color:var(--muted);font-size:.89rem;margin-top:4px;line-height:1.5;}
.def{color:var(--dim);font-size:.83rem;margin-top:3px;line-height:1.45;font-style:italic;}
.def b{color:var(--muted);font-weight:600;font-style:normal;}
.tag{display:inline-block;font-family:'Space Grotesk',sans-serif;font-size:.63rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--dim);background:var(--surface2);border:1px solid var(--border);border-radius:5px;padding:2px 7px;margin-bottom:6px;}
.tag.reg{color:#fcd34d;border-color:#5f4a1e;}
.tag.err{color:#fca5a5;border-color:#5f1e1e;}

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
}""" % ACCENT

JS = r"""(function(){
  const art=document.getElementById('art'), q=document.getElementById('q'), sbox=document.getElementById('sbox'),
        clr=document.getElementById('clr'), info=document.getElementById('info'), empty=document.getElementById('empty'),
        toclist=document.getElementById('toclist');
  const secs=[...art.querySelectorAll('section')];

  secs.forEach(s=>{
    const a=document.createElement('a');
    a.href='#'+s.id;
    a.textContent=s.querySelector('.snum').textContent+' — '+s.querySelector('h2').textContent;
    toclist.appendChild(a);
  });
  const links=[...toclist.querySelectorAll('a')];

  const units=[];
  secs.forEach(s=>{
    s.querySelectorAll('.i').forEach(el=>{
      units.push({el, sec:s, txt:el.textContent.toLowerCase()});
    });
  });
  document.getElementById('m-total').textContent=units.length;

  const norm=s=>s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');
  units.forEach(u=>u.norm=norm(u.txt));

  function run(){
    const raw=q.value.trim();
    sbox.classList.toggle('has-q', raw.length>0);
    if(!raw){
      units.forEach(u=>u.el.style.display='');
      secs.forEach(s=>s.style.display='');
      empty.style.display='none';
      info.innerHTML='<b>'+units.length+'</b> itens em '+secs.length+' blocos.';
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
    secs.forEach(s=>{s.style.display=live.has(s)?'':'none';});
    empty.style.display=hits?'none':'block';
    info.innerHTML=hits
      ? '<b>'+hits+'</b> '+(hits===1?'item':'itens')+' em <b>'+live.size+'</b> '+(live.size===1?'bloco':'blocos')+' para &ldquo;'+raw.replace(/[<>&]/g,'')+'&rdquo;'
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


def build(caminho, spec_path):
    alvo = Path(caminho)
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    corpo = render_secoes(spec["secoes"], inicio=1)
    blocos = len(spec["secoes"])
    itens = sum(len(s["itens"]) for s in spec["secoes"])
    validar(blocos, itens, alvo.name)

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{spec["titulo"]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
<div class="bg-glow"></div>
<a href="./index.html" class="back">&#8592; {spec.get("voltar", "Voltar")}</a>
<div class="wrap">

<div class="eyebrow">{spec["eyebrow"]}</div>
<h1 class="title">{spec["h1"]}</h1>
<p class="lead">{spec["lead"]}</p>

<div class="metrics">
  <div class="metric"><b>{blocos}</b><span>blocos</span></div>
  <div class="metric"><b id='m-total'>&mdash;</b><span>itens</span></div>
  <div class="metric"><b>{spec.get("nivel", "C1–C2")}</b><span>nível</span></div>
  <div class="metric"><b>{spec.get("padrao", "GB")}</b><span>padrão</span></div>
</div>

<div class="searchbar">
  <div class="searchbox" id="sbox">
    <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
    <input type="search" id="q" placeholder="{spec.get("placeholder", "Buscar em inglês ou português…")}" autocomplete="off" spellcheck="false">
    <button type="button" id="clr">limpar</button>
  </div>
  <div class="searchinfo" id="info"></div>
</div>

<div class="layout">
  <nav class="toc"><h3>Blocos</h3><div class="toc-list" id="toclist"></div></nav>
  <main class="article" id="art">

{corpo}
  </main>
</div>

<div class="empty" id="empty"><b>Nada encontrado</b>Tente outro termo &mdash; a busca cobre o inglês, o português e as notas de todos os itens.</div>
</div>

<footer>{spec["footer"]}</footer>

<script>
{JS}
</script>
</body>
</html>
"""
    alvo.write_text(html, encoding="utf-8")
    print(f"{alvo.name}: {blocos} blocos / {itens} itens")
    return blocos, itens


# ---------------------------------------------------------------- cli

def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd = argv[1]
    if cmd == "check":
        html = Path(argv[2]).read_text(encoding="utf-8")
        blocos, itens = contar(html)
        print(f"{Path(argv[2]).name}: {blocos} blocos / {itens} itens "
              f"(minimo {MIN_BLOCOS}/{MIN_ITENS})")
        if blocos < MIN_BLOCOS or itens < MIN_ITENS:
            print("ABAIXO DO MINIMO")
            return 1
        print("ok")
        return 0
    if cmd == "append":
        append(argv[2], argv[3])
        return 0
    if cmd == "build":
        build(argv[2], argv[3])
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
