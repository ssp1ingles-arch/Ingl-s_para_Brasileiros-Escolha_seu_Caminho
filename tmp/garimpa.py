# -*- coding: utf-8 -*-
"""Garimpa frases aproveitaveis de um dump OCR de livro.
Nao conserta nada: so separa o que vale olhar do que e irrecuperavel,
e ordena por sanidade tipografica para a curadoria ser rapida."""
import re, sys, io

COMUNS = set("""a about after again all also always am an and another any are as ask at
back be because been before being best better between big both but buy by call came can
cannot cant come could country day did didnt do does doesnt doing dont down each early
eat else even ever every example eyes face fact family far feel few find first for found
friend from get give go going good got great had hand has have he head hear help her here
high him his hold home hope house how i idea if in into is it its just keep kind knew know
land large last late learn leave left let letter life like little live long look love made
make man many may me mean men might mind more morning most move much must my name near
need never new next night no not nothing now number of off often oh old on once one only
open or other our out over own part people place play please point put read really right
room said same saw say says school see seem send set she should show side since sister
small so some something soon sound speak start still story such take talk tell than thank
thanks that the their them then there these they thing think this those thought three
through time to today together told tomorrow too took turn two under until up upon us use
used very want was watch water way we week well went were what when where which while who
whole why will wish with without woman word words work world would write year years yes
yet you young your telephone brother mistake afraid course boat maybe holiday sorry
excuse minute o'clock please thanks welcome""".split())

# lixo de scanner: barras invertidas, simbolos soltos, clusters impossiveis
RUIM = re.compile(r"[\\|@#$%^*_~{}\[\]<>]"
                  r"|\b[bcdfghjklmnpqrstvwxz]{4,}\b"
                  r"|[a-z][A-Z]{2}"
                  r"|\.{4,}")
PULA = re.compile(r"^#+\s|^-{2,}$|^\s*$|Página|^\d+$|^[ivxlIVXL]+$")

def limpa(l):
    l = re.sub(r"^[-–—•*\d\s.)]+", "", l.strip())
    return re.sub(r"\s{2,}", " ", l).strip()

def sanidade(l):
    pal = re.findall(r"[A-Za-z']+", l.lower())
    if len(pal) < 3: return 0.0
    conhecidas = sum(1 for w in pal if w.strip("'") in COMUNS)
    plausiveis = sum(1 for w in pal if 1 <= len(w) <= 12)
    return 0.5 * (conhecidas / len(pal)) + 0.5 * (plausiveis / len(pal))

def colagem(l):
    return sum(1 for w in re.findall(r"[A-Za-z]+", l) if len(w) > 13)

def garimpa(caminho, minlen=14, maxlen=115, corte=0.55):
    s = io.open(caminho, encoding="utf-8").read()
    vis, out = set(), []
    for bruto in s.split("\n"):
        if PULA.search(bruto): continue
        l = limpa(bruto)
        if not (minlen <= len(l) <= maxlen): continue
        if RUIM.search(l) or colagem(l): continue
        sc = sanidade(l)
        if sc < corte: continue
        k = re.sub(r"[^a-z]", "", l.lower())
        if not k or k in vis: continue
        vis.add(k); out.append((round(sc, 2), l))
    out.sort(key=lambda x: -x[0])
    return out

if __name__ == "__main__":
    corte = float(sys.argv[2]) if len(sys.argv) > 2 else 0.55
    r = garimpa(sys.argv[1], corte=corte)
    print(f"CANDIDATOS: {len(r)}")
    lim = int(sys.argv[3]) if len(sys.argv) > 3 else 60
    for sc, x in r[:lim]: print(f"  {sc} {x}")
