# REGRAS — Sistema 19 · Baseado em Livros V10 · Gramática Básica

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
Botão fixo **"← Voltar ao Sistema 19"** → `./index.html`. O hub (`index.html`) volta para `../index.html`.
Busca própria EN/PT em cada painel de livro.

## 5. Regras específicas
- Cor de acento: **verde `#22C55E`**.
- Público: quem está **montando a base**. Quem já tem base sólida vai para os Sistemas 20, 21 e 22.
- Ordem dentro de cada livro: da estrutura mais simples à mais avançada.

## 6. Livros deste Sistema
| # | Livro | Status |
|---|---|---|
| 01 | Basic English Grammar Workbook For Dummies | ✅ `livro01.html` — 43 estruturas, 1.130 itens, 41 tabelas |
| 02 | Everything You Need to Ace English Language Arts (Big Fat Notebook) | ⏳ aguardando |
| 03 | English Grammar For Dummies | ⏳ aguardando |
| 04 | English Grammar — A Resource Book for Students | ⏳ aguardando |
| 05 | Grammar For Young Learners | ⏳ aguardando |
| 06 | Grammar And Usage For Better Writing | ⏳ aguardando |
| 07 | The Infographic Guide to Grammar | ⏳ aguardando |

## 7. Commits
Um commit por livro: `feat(S19): <nome do livro> — livroNN`.
