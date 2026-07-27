# Lote processado — 2026-07-26

**188 imagens** (`IMG_6520.PNG` … `IMG_6714.PNG`, com falhas de numeração na origem:
6584-6585, 6620, 6645, 6652, 6675, 6686). Capturas de tela de posts de Instagram
(`english__with_ravi`, `ingles.doimigrante` / `uptallk`, `inglesdocotidianobr`).

## Status: conteúdo 100% implementado

O conteúdo deste lote foi garimpado e virou **6 painéis novos — 938 itens de inglês**:

| Sistema | Painel | Seções | Itens |
|---|---|---|---|
| S01 · Base. Fluência. Gramática | `gramatica-em-tabelas.html` | 9 | 192 |
| S02 · Dúvidas Pontuais | `falar-melhor.html` | 8 | 168 |
| S03 · Reduções do Inglês Real | `livro-x-rua.html` | 6 | 118 |
| S04 · Motor de Verbos | `familias-de-verbos.html` | 12 | 211 |
| S05 · Conectar Frases | `even-so-conectores.html` | 4 | 76 |
| S06 · Situar a Frase | `preposicoes-mapas.html` | 9 | 173 |
| | | | **938** |

Painéis criados no commit `f9877c5`; o card do hub do S01, que ficou faltando,
entrou no commit seguinte.

## Por que o lote ficou junto, e não dividido por Sistema

As imagens são um rolo de posts salvos, **não** blocos contíguos por tema — imagens
vizinhas alimentam Sistemas diferentes (ex.: 6592→S02, 6604→S05, 6616→S06,
6628→S02, 6640→S04, 6653→S04, 6677→S04). O mapeamento imagem→Sistema não foi
registrado quando os painéis foram feitos, e várias imagens alimentaram mais de um
painel. Arquivar o lote inteiro preserva a proveniência sem o risco de mandar
arquivo para o `_fontes/` do Sistema errado.

Para rastrear a origem de um item específico: busque a frase em inglês no painel
correspondente e depois neste lote.
