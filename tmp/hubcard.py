#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hubcard.py — sincroniza o card do hub (`index.html` do Sistema) com o
painel `livroNN.html` que ele aponta.

Existe por um motivo especifico: o card do hub e o painel sao dois arquivos
diferentes, e o numero de blocos/itens vive nos dois. Toda vez que isso foi
escrito na mao, um dos dois desencontrou. Aqui o card NUNCA e uma promessa —
os numeros sao lidos do proprio painel, contando `<section id="sNN">` e
`<div class="i">`.

USO
    python hubcard.py sync   <hub/index.html> <painel.html> [mais paineis...]
        Le cada painel, atualiza o `.hc-meta` do card cujo href bate com o
        nome do arquivo. Preserva o terceiro span (nivel).

    python hubcard.py status <hub/index.html>
        Compara card x painel para todos os cards do hub e aponta os que
        estao desencontrados. Sai com 1 se houver divergencia.

    python hubcard.py metric <hub/index.html>
        Recalcula a metrica "N/M paineis prontos" do topo do hub: M = numero
        de cards, N = numero de cards que apontam para um painel existente.
"""

import re
import sys
from pathlib import Path

RE_SECTION = re.compile(r'<section id="s\d+">')
RE_ITEM = re.compile(r'<div class="i">')
RE_CARD_META = re.compile(
    r'(<a class="hub-card" href="(?P<href>[^"]+)".*?<div class="hc-meta">)'
    r'(?P<meta>.*?)'
    r'(</div>)',
    re.S,
)
RE_PRONTOS = re.compile(
    r'(<div class="metric"><b>)\d+/\d+(</b><span>pain[eé]is prontos</span></div>)'
)


def contar(painel):
    html = Path(painel).read_text(encoding="utf-8")
    return len(RE_SECTION.findall(html)), len(RE_ITEM.findall(html))


def _meta_spans(meta):
    return re.findall(r"<span>(.*?)</span>", meta, re.S)


def sync(hub_path, paineis):
    hub = Path(hub_path)
    html = hub.read_text(encoding="utf-8")
    dados = {}
    for p in paineis:
        p = Path(p)
        dados[p.name] = contar(p)

    tocados = []

    def repl(m):
        href = m.group("href")
        if href not in dados:
            return m.group(0)
        blocos, itens = dados[href]
        spans = _meta_spans(m.group("meta"))
        # o terceiro span e o nivel (C1–C2, B2–C1, ...) e nao se toca nele
        cauda = spans[2:] if len(spans) > 2 else []
        novo = f"<span>{blocos} blocos</span><span>{itens} itens</span>" + "".join(
            f"<span>{s}</span>" for s in cauda
        )
        tocados.append((href, blocos, itens))
        return m.group(1) + novo + m.group(4)

    html = RE_CARD_META.sub(repl, html)
    hub.write_text(html, encoding="utf-8")

    faltando = sorted(set(dados) - {t[0] for t in tocados})
    for href, blocos, itens in tocados:
        print(f"card {href}: {blocos} blocos / {itens} itens")
    for href in faltando:
        print(f"AVISO: nenhum card do hub aponta para {href}")
    return tocados


def status(hub_path):
    hub = Path(hub_path)
    html = hub.read_text(encoding="utf-8")
    base = hub.parent
    ruim = 0
    for m in RE_CARD_META.finditer(html):
        href = m.group("href")
        painel = base / href
        spans = _meta_spans(m.group("meta"))
        if not painel.exists():
            print(f"{href}: card existe, painel NAO existe")
            ruim += 1
            continue
        blocos, itens = contar(painel)
        card = f"{spans[0] if spans else ''} / {spans[1] if len(spans) > 1 else ''}"
        real = f"{blocos} blocos / {itens} itens"
        if spans[:2] != [f"{blocos} blocos", f"{itens} itens"]:
            print(f"{href}: card diz [{card}] mas o painel tem [{real}]  <-- DESENCONTRADO")
            ruim += 1
        else:
            print(f"{href}: {real}  ok")
    return 1 if ruim else 0


def metric(hub_path):
    hub = Path(hub_path)
    html = hub.read_text(encoding="utf-8")
    base = hub.parent
    hrefs = [m.group("href") for m in RE_CARD_META.finditer(html)]
    total = len(hrefs)
    prontos = sum(1 for h in hrefs if (base / h).exists())
    novo, n = RE_PRONTOS.subn(rf"\g<1>{prontos}/{total}\g<2>", html, count=1)
    if n:
        hub.write_text(novo, encoding="utf-8")
        print(f"metrica: {prontos}/{total} paineis prontos")
    else:
        print("metrica 'paineis prontos' nao encontrada no hub — nada alterado")
    return 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd = argv[1]
    if cmd == "sync":
        if len(argv) < 4:
            print(__doc__)
            return 2
        sync(argv[2], argv[3:])
        return 0
    if cmd == "status":
        return status(argv[2])
    if cmd == "metric":
        return metric(argv[2])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
