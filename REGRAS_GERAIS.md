# REGRAS GERAIS — Inglês para Brasileiros · Escolha seu Caminho

Regras que valem para **todos** os Sistemas. Cada Sistema tem, além destas, o seu próprio `REGRAS.md` com regras específicas. **Leia o `REGRAS.md` do Sistema antes de criar qualquer conteúdo nele.**

---

## 1. Fluxo de conteúdo novo — pasta `#Para distribuição`

- Todo conteúdo novo (PDF, transcrição, docx, imagem, etc.) chega **primeiro** na pasta `#Para distribuição` na raiz.
- A partir dali ele é **garimpado, classificado e distribuído** para o Sistema mais adequado.
- Nada é implementado em painel direto da fonte sem passar por essa triagem.
- Depois de distribuído e implementado no painel, o arquivo-fonte pode permanecer na pasta do Sistema como referência.

## 2. Padrão visual (dark) — obrigatório em todos os painéis

- Fundo: `--bg:#0a0a0a` · superfícies `#141414` / `#1b1b1b` · bordas `#242424`.
- Texto: `--text:#e5e5e5` · muted `#8a8a8a` · dim `#5a5a5a`.
- Tipografia: títulos em **Space Grotesk** (400–800), corpo em **Inter** (400–600).
- Cada Sistema tem **uma cor de acento** própria (ver `sistemas.json`). Use `--accent` para títulos, links ativos, bordas de destaque e o brilho de fundo (`.bg-glow`).
- Estrutura recorrente: `.bg-glow` → `.wrap` → botão `.back` → `.eyebrow` + `h1.title` + `.lead` + `.metrics` → `.layout` (TOC lateral `sticky` + `.article.md`) → `footer`.
- Responsivo: TOC vira estático abaixo de 820px; tabelas dentro de `.tablewrap` com scroll horizontal próprio.

## 3. Regra dos botões "← Voltar"

- O botão **"← Voltar ao início"** no topo do painel de um Sistema **sempre** aponta para `../index.html` (o painel principal).
- **Sub-painéis / seções com navegação própria** dentro de um Sistema: o botão "Voltar" desses sub-painéis deve retornar ao `index.html` **do próprio Sistema**, **não** ao painel principal.
- Navegação por âncora (TOC → `#id`) não é sub-painel e não precisa de botão "Voltar" próprio.

## 4. Painéis objetivos — sem ruído

- O painel mostra **conteúdo de inglês real**: diálogos, frases, vocabulário, tabelas, exemplos em uso.
- **Não** transformamos em aba/seção do painel: dicas de estudo, regras pedagógicas, conselhos, motivação, "como usar este material", metodologia. Isso é bastidor, não conteúdo.

## 5. Critério para livros PDF (Sistema 08)

- Extrair **apenas inglês real**: diálogos, frases de conversação, vocabulário em uso, expressões em contexto.
- **NUNCA** incluir: dicas de estudo, métodos, motivação, introduções, conselhos do autor.
- Foco: o inglês que a pessoa realmente fala/usa na situação — não teoria sobre aprender inglês.

## 6. Critério para transcrições e canais (Sistema 07)

- Extrair **diálogos reais**, **expressões em contexto** e **frases prontas de nativos**.
- Manter a fala como ela acontece (inclusive reduções e informalidade).
- **NUNCA** incluir: comentário pedagógico, dicas de estudo, resumo motivacional do episódio.

## 7. Commits

- Um commit por tarefa/entrega, com mensagem descritiva do que mudou e por quê.
- `git push origin main` ao final do lote de tarefas.
