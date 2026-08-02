"""Troca um card 'Em breve' do index de um Sistema por um card ativo.

Uso: python tmp/pdfs/_card.py <index.html> <num> <arquivo.html> <titulo> <descricao> <meta1;meta2;meta3>
Atualiza também os contadores 'disponível/disponíveis' e o total de frases, se passados.
"""
from __future__ import annotations

import io
import re
import sys


def main() -> int:
    index, num, href, titulo, desc, metas = sys.argv[1:7]
    s = io.open(index, encoding="utf-8").read()
    pat = re.compile(
        r'  <div class="hub-card hub-soon">\n'
        r'    <div class="hc-top"><span class="hc-num">Livro ' + re.escape(num) + r'</span>'
        r'<span class="hc-icon">(?P<icon>[^<]*)</span></div>\n'
        r'    <h2 class="hc-title">[^<]*</h2>\n'
        r"    <p class=\"hc-desc\">.*?</p>\n"
        r'    <div class="hc-meta">.*?</div>\n'
        r"  </div>",
        re.S,
    )
    m = pat.search(s)
    if not m:
        print(f"card do Livro {num} não encontrado (ou já ativo)")
        return 1
    meta_html = "".join(f"<span>{x}</span>" for x in metas.split(";"))
    novo = (
        f'  <a class="hub-card" href="{href}">\n'
        f'    <div class="hc-top"><span class="hc-num">Livro {num}</span>'
        f'<span class="hc-icon">{m.group("icon")}</span></div>\n'
        f'    <h2 class="hc-title">{titulo}</h2>\n'
        f'    <p class="hc-desc">{desc}</p>\n'
        f'    <div class="hc-meta">{meta_html}</div>\n'
        f'    <span class="hc-cta">Abrir livro &#8594;</span>\n'
        f"  </a>"
    )
    s = s[: m.start()] + novo + s[m.end() :]
    io.open(index, "w", encoding="utf-8", newline="\n").write(s)
    print(f"card do Livro {num} ativado em {index}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
