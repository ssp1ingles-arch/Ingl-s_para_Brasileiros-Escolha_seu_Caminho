# Resumo Técnico — Inglês para Brasileiros: Escolha seu Caminho

## Visão Geral
Projeto de ensino de inglês organizado em painéis HTML interativos, hospedado no GitHub Pages.
Cada Sistema é uma pasta com index.html (hub) + sub-painéis dedicados.

---

## Caminhos Importantes

| O quê | Caminho |
|-------|---------|
| Pasta raiz do projeto | `C:\Users\Samukk99\Documents\Claude Code Projetos\Inglês para Brasileiros - Escolha seu Caminho` |
| Pasta de entrada de novo conteúdo | `...\#Para distribuição` |
| Repositório GitHub | https://github.com/ssp1ingles-arch/Ingl-s_para_Brasileiros-Escolha_seu_Caminho |
| Site público (GitHub Pages) | https://ssp1ingles-arch.github.io/Ingl-s_para_Brasileiros-Escolha_seu_Caminho/ |
| Script de push | `auto_push.bat` na raiz do projeto |
| Raiz do git | `C:\Users\Samukk99\Documents\Claude Code Projetos\Inglês para Brasileiros - Escolha seu Caminho` |
| Branch | `main` |

---

## Estrutura de Sistemas (10 no total)

| # | Sistema | Conteúdo principal | Sub-painéis |
|---|---------|-------------------|-------------|
| 01 | Base. Fluência. Gramática | 25 módulos A1→C1 em 4 fases (cards+modal), Pronomes e Artigos | pronomes-e-artigos.html |
| 02 | Reduções do Inglês Real | 5 tipos de redução, frases crescentes, contextos progressivos | reducoes.html, entender-nativos.html |
| 03 | Motor de Verbos | Matriz 12 tempos, 170 verbos, modais/phrasal, 100 colocações | gramatica-viva.html, dicionario-de-verbos.html, modais-phrasal-verbs.html, colocacoes-verbais.html |
| 04 | Conectar Frases | 14 conversas question words, 100 colocações, expressões, 41 conectivos | conversas-question-words.html, colocacoes-naturais.html, expressoes-idiomaticas.html, conectivos-question-words.html |
| 05 | Situar a Frase | Preposições, teste 30 questões, went/gone, estruturas fixas, quantificadores | ingles-do-zero.html, teste-seu-nivel.html, went-ou-gone.html, estruturas-fixas.html, preposicoes-quantificadores.html |
| 06 | Baseado em Desenho Infantil | 7 níveis progressivos, 37 cenas de desenho animado, para adultos (linguagem simples) | Navegação por cenas via JS |
| 07 | Transcrições e Canais | 45 docx processados: 11.513 falas, 231 expressões, 1.259 frases de nativos | 16 sub-painéis (um por canal) |
| 08 | Baseado em Livros | 6 livros implementados, 3.513 itens de inglês real | livro01.html a livro06.html |
| 09 | Dúvidas Pontuais | 32 cards: 22 gramática + 10 vocabulário, 30 verbos irregulares, auxiliares | duvidas-gramatica.html, vocabulario-referencia.html |
| 10 | Prática Completa · 4 Pilares | Extraído do S02 — 4 pilares: Frases Crescentes, 1.000 Frases, Padrões, 150 Textos | pilar1 a pilar4.html |

---

## Sistema 08 — Livros Implementados

| Arquivo | Conteúdo | Itens | Status |
|---------|----------|-------|--------|
| LIVRO_01 | 1.006 dicas de inglês real | 1.006 | ✅ livro01.html |
| LIVRO_02 | Conversação para viagem (Michaelis) | 261 frases, 9 contextos | ✅ livro02.html |
| LIVRO_03 | 120 frases de conversação | 120 frases, 5 temas | ✅ livro03.html |
| LIVRO_04 | Música + 90 citações célebres | 1.286 itens | ✅ livro04.html |
| LIVRO_05 | Vocabulário essencial + números + datas | 404 itens | ✅ livro05.html |
| LIVRO_06 | Erros reais (remember/remind, lose/miss...) | 436 frases, 128 tópicos | ✅ livro06.html |

**Livros descartados:** LIVRO_04 antigo (Mairo Vergara — método), LIVRO_13 antigo (tratado acadêmico de 1927 — arquivo errado).

**Regra S08:** extrair APENAS inglês real (diálogos, frases, vocabulário em uso). NUNCA dicas de estudo, métodos, motivação, "como aprender".

---

## Arquivos de Controle (raiz do projeto)

| Arquivo | Função |
|---------|--------|
| `sistemas.json` | Lista dos 10 sistemas — o painel principal lê este arquivo para gerar os cards dinamicamente |
| `REGRAS_GERAIS.md` | Regras globais do projeto |
| `MAPEAMENTO_ARQUIVOS.md` | Status de todos os arquivos/livros |
| `auto_push.bat` | Faz git add + commit + push para origin/main |
| `index.html` | Painel principal (lê sistemas.json, gera 10 cards) |

Cada pasta de Sistema tem também seu próprio `REGRAS.md`.

---

## Regras Fundamentais do Projeto

1. **#Para distribuição** — TODO conteúdo novo entra primeiro nesta pasta. Claude analisa, decide o Sistema correto, move e implementa no painel.
2. **Nunca alterar conteúdo** — reorganizações são só de estrutura/layout/navegação.
3. **Visual padrão** — fundo `#0a0a0a`, fontes Space Grotesk/Inter, tema dark em todos os painéis.
4. **Botão Voltar fixo** — `position:fixed` no topo, sempre visível ao rolar, altura mínima 44px (mobile).
5. **Hub → Sub-painel** — cada Sistema é uma página-hub com cards clicáveis para sub-painéis. Sem scroll infinito.
6. **Livros PDF (S08)** — ler com critério, extrair só inglês real. Um livro por vez, direcionado pelo usuário.
7. **Transcrições (S07)** — extrair diálogos reais, expressões em contexto, frases prontas de nativos. Sem links externos.
8. **Conteúdo de maior para menor** — organizar sempre do mais fácil ao mais avançado.
9. **Não inventar conteúdo** — usar apenas o que está nos arquivos.
10. **Commit por tarefa** + `git push origin main` ao final de cada lote.

---

## Pastas de Origem (já organizadas, NÃO excluídas ainda)

- `C:\Users\Samukk99\Documents\Claude Code Projetos\Americano_01` — fonte original dos sistemaX_conteudo.md
- `C:\Users\Samukk99\Documents\Claude Code Projetos\Sala_001` — PDFs distribuídos nos Sistemas

---

## Sistema 07 — Canais das Transcrições

All Ears English, English Coach Chad (7 ep.), English Evolution Step 1 (9 ep.), English Speaking TV (5 ep.) + outros canais menores. Total: 45 episódios, 16 sub-painéis.

---

## Fluxo para Adicionar Conteúdo Novo

```
Usuário coloca arquivo em #Para distribuição
        ↓
Claude lê + analisa o conteúdo
        ↓
Decide o Sistema correto (consultando REGRAS.md de cada um)
        ↓
Move o arquivo para a pasta do Sistema (_fontes/)
        ↓
Implementa no sub-painel correto (nunca inventa, usa só o arquivo)
        ↓
git add + commit + push
```

---

## Fluxo para Adicionar Novo Livro ao S08

```
Usuário indica qual livro quer implementar
        ↓
Claude lê REGRAS.md do S08
        ↓
Lê o PDF completo com critério
        ↓
Extrai APENAS inglês real (frases, diálogos, vocabulário em uso)
        ↓
Cria livroXX.html + adiciona card no hub (index.html do S08)
        ↓
Atualiza MAPEAMENTO_ARQUIVOS.md
        ↓
Commit + push
```

---

## Pontos Pendentes / Próximos Passos

- [ ] LIVRO_13 correto (Short Stories for Beginners) — arquivo estava errado, aguarda o PDF correto
- [ ] Sistema 06 — ainda há cenas do docx não extraídas (729 falas, parcialmente implementado)
- [ ] Novos livros para S08 — usuário direciona um por vez
- [ ] Novos conteúdos — entram pela pasta `#Para distribuição`
- [ ] Sistema 04 (Conectar Frases) — nasceu sem arquivo sistemaX dedicado; conteúdo veio de sistema6/7/15

---

## Como Fazer Push Manual

```bash
cd "C:\Users\Samukk99\Documents\Claude Code Projetos\Inglês para Brasileiros - Escolha seu Caminho"
git add .
git commit -m "Descrição do que foi feito"
git push origin main
```
Ou simplesmente rodar o `auto_push.bat` na raiz do projeto.
