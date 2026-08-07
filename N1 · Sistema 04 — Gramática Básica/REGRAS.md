# REGRAS — Sistema 04 · Gramática Básica

> Leia também o `REGRAS_GERAIS.md` na raiz.
>
> ⚠️ **Este Sistema NÃO segue o `REGRAS_AVANCADO.md`.** O dourado e a permissão de explicação teórica valem só para S20, S21 e S22. Aqui vale a regra dura de livro: **só inglês real**.

## 1. Nome e propósito
**Gramática Básica V10.** Sete livros de gramática de nível inicial (A1–A2) — a linha *For Dummies*, guias visuais e livros de gramática para jovens aprendizes — transformados em painéis de **frase-modelo em uso**. A fonte explica; o painel mostra a frase.

## 2. O que PERTENCE aqui
- **Frases-modelo completas** de cada estrutura gramatical (`She doesn't work on Saturdays.`).
- **Exemplos contextualizados** — a estrutura dentro de uma situação real, não solta.
- **Diálogos e mini-textos** presentes no livro.
- **Tabelas de estrutura com exemplos** (conjugação, formas afirmativa/negativa/interrogativa, comparativos, plurais irregulares).

## 3. O que NÃO pertence aqui — REGRA DURA
- **NUNCA** enunciado de exercício (`Complete the sentences with…`, `Circle the correct answer`).
- **NUNCA** lacuna / frase incompleta (`She ___ to school every day.`). Se a frase do exercício é inglês real, ela entra **completa e resolvida**.
- **NUNCA** gabarito isolado (`1-b, 2-c, 3-a`).
- **NUNCA** explicação teórica sem exemplo de uso — a regra sozinha não entra.
- **NUNCA** dica pedagógica, método do autor, motivação, "como estudar gramática".

## 4. Formato padrão do painel
Painel dark, um arquivo por livro (`livroNN.html`). Dentro do livro, organizar **por estrutura gramatical, do mais simples ao mais avançado** — ordem pedagógica, não a ordem de página do PDF. Cada item: inglês + tradução. Conteúdo tabular vira **tabela HTML** dentro de `.tablewrap`.
Botão fixo **"← Voltar ao Sistema 04"** → `./index.html`. O hub (`index.html`) volta para `../index.html`.
Busca própria EN/PT em cada painel de livro.

## 5. Regras específicas
- Cor de acento: **verde `#22C55E`**.
- Público: quem está **montando a base**. Quem já tem base sólida vai para os Sistemas 22, 23 e 24.
- Ordem dentro de cada livro: da estrutura mais simples à mais avançada.

## 6. Livros deste Sistema
| # | Livro | Status |
|---|---|---|
| 01 | Basic English Grammar Workbook For Dummies | ✅ `livro01.html` — 43 estruturas, 1.130 itens, 41 tabelas |
| 02 | Everything You Need to Ace English Language Arts (Big Fat Notebook) | ✅ `livro02.html` — 18 estruturas, 18 tabelas |
| 03 | English Grammar For Dummies | ✅ `livro03.html` — 19 estruturas, 23 tabelas |
| 04 | English Grammar — A Resource Book for Students | ✅ `livro04.html` — 19 estruturas, 26 tabelas |
| 05 | Grammar For Young Learners | ✅ `livro05.html` — 19 estruturas, 17 tabelas |
| 06 | Grammar And Usage For Better Writing | ✅ `livro06.html` — 21 estruturas, 31 tabelas |
| 07 | The Infographic Guide to Grammar | ✅ `livro07.html` — 19 estruturas, 29 tabelas |

**Sistema completo:** 7 de 7 livros implementados, 158 estruturas gramaticais.

### Recortes de fonte adotados

Cada livro traz coisas que não são inglês real. Estes foram os cortes:

- **02 (Big Fat Notebook):** só as Unidades 1 e 2 (gramática e vocabulário). As Unidades 3–5 são análise literária e redação — bastidor, não conteúdo.
- **04 (Resource Book):** só a Parte A. As Partes B–D são discussão teórica e leituras acadêmicas.
- **05 (Young Learners):** é livro de atividades para professor. Entraram as frases-modelo, canções, chants, moldes de pergunta e os três anexos (verbos no passado, advérbios/adjetivos, Classroom language chart). Ficaram fora procedimento de atividade e dica pedagógica.
- **07 (Infographic Guide):** o capítulo 4 (Writing Style) é sobre método de escrita, não sobre inglês — entrou só a parte de voz ativa/passiva.

## 7. Commits
Um commit por livro: `feat(S04): <nome do livro> — livroNN`.
