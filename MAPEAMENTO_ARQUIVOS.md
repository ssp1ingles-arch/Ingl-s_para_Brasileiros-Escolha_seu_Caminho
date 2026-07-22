# Mapeamento de Arquivos — o que ainda NÃO foi implementado nos painéis

> Scan de S01–S10 em 2026-07-21. Ordem: do mais valioso ao menos.

## 0b. Atualização 2026-07-22 (T3/T4) — pasta S08 renumerada + LIVRO_04 (Música) implementado

> **Atenção:** a pasta `Sistema 08` foi **renumerada** e hoje tem só **6 PDFs**. A numeração NÃO bate mais com o item 0 abaixo (scan antigo). Estado real da pasta:
>
> | Arquivo atual | O que é | Status |
> |---|---|---|
> | `LIVRO_01_1000 melhores dicas…` | 1.006 dicas/frases | ✅ Implementado (`livro01.html`) |
> | `LIVRO_02_…Conversação para viagem (Michaelis)` | 261 frases de viagem | ✅ Implementado (`livro02.html`) |
> | `LIVRO_03_120 frases para uma conversa…` | 60 expressões + 120 exemplos | ✅ Implementado (`livro03.html`) |
> | `LIVRO_04_Segredo da Fluência — aprender Inglês com Música (Leonardo de Mello, 2016)` | Compilação: música Queen + phrasebook conversacional | ✅ **Implementado** (`livro04.html`) |
> | `LIVRO_05_…Memorização para aprender idiomas (Marcos da Costa Gois)` | Método de memorização + núcleo de inglês real | ✅ **Implementado** (`livro05.html`) |
> | `LIVRO_06_Como não aprender Inglês (PDFDrive)` | Livro de método | ⏳ Pendente de leitura |
>
> **LIVRO_04 (Música) — 201 pág., lido integralmente (T4):** apesar do título "aprender com música", o miolo é uma **compilação-phrasebook conversacional** riquíssima. Extraído para `livro04.html` só o inglês real:
> - **We Are The Champions (Queen)** — letra completa + tradução + 16 cards de vocabulário/phrasal verbs (kicked in, come through, keep on, goes with, bed of roses, ain't, gonna…).
> - **210 frases por palavra-chave** (42 palavras: YOU, HE, WHAT, MAKE, KNOW, THINK…).
> - **~986 padrões de conversação** (Básico/Interm/Avançado): I'm gonna, I used to, I'd rather, would you mind, rumor has it that… → 172 categorias, **1.196 frases** no total.
> - **Descartado (REGRAS §4):** todo o método em português (input/output, subconsciente, SRS/Anki, "divirta-se"). *(Atualização: as 90 citações foram DEPOIS incluídas a pedido, como seção "Frases Célebres em Inglês" — ver T1.)*
>
> **LIVRO_05 (Memorização, Marcos da Costa Gois) — 128 pág., lido integralmente (T2):** livro de **técnica de memorização** (OCR de scan, baixa qualidade). Estimativa: **~85% método** em português (facilitadores/mnemônicos, método dos locais, respiração, classificação…) vs. **~15% inglês real**. Extraído para `livro05.html` só o inglês real:
> - **~300 palavras mais comuns do inglês** (Cap. 8) com tradução — grafia inglesa **reconstruída** (o OCR corrompeu muitas: "Giue"→Give, "Knout"→Know, "Aboue"→Above…). Os "facilitadores" (mnemônicos) foram descartados por serem técnica.
> - **Números** cardinais (0–1 bilhão) e ordinais (1st–1000th), + **7 expressões com números** com frase de exemplo (Cap. 11).
> - **Dias da semana, meses e formas de escrever/ler datas**, com frases de exemplo (Cap. 13).
> - Total: **404 itens** de inglês. **Descartado:** todo o miolo de método/técnica de memorização.

## 0. Atualização 2026-07-22 — leitura dos PDFs do S08 (LIVRO_03, 04, 13)

> ⚠️ Este bloco reflete a numeração ANTIGA da pasta (o "LIVRO_04 Mairo Vergara" e o "LIVRO_13 Wyld" abaixo já não estão mais na pasta com esses números). Ver bloco 0b acima para o estado atual.

- ✅ **LIVRO_03** — lido (61 pág.). É inglês real (60 expressões + 120 frases de exemplo + tradução). **Implementado** em `Sistema 08/livro03.html` + card no hub.
- ⚠️ **LIVRO_13 "Short Stories in English for Beginners"** — **arquivo mal rotulado.** O PDF (312 pág.) é na verdade *"A Short History of English"*, de **Henry Cecil Wyld (1927)** — tratado acadêmico de filologia (mudanças fonéticas do inglês antigo/médio, dialetos, flexões). **Não são short stories, não é para iniciantes, não é conversação.** Falha as REGRAS do S08 → **não implementado.** Se quiser contos de verdade, é preciso o arquivo correto.
- ❌ **LIVRO_04 "Como Aprender Inglês (Mairo Vergara)"** — lido (63 pág.). É um **guia de método** ("como aprender inglês"): ~**98,5%** texto de metodologia em português; só ~1,5% são frases-exemplo isoladas usadas para ilustrar técnicas de estudo (flashcards/Anki), não conversação real. Falha as REGRAS → **não implementado** (confirmado).

## 1. Conteúdo real de inglês — candidatos fortes a implementar

| Sistema | Arquivo | O que é | Observação |
|---|---|---|---|
| **S08** | `LIVRO_03_120 frases para uma conversa em inglês` | 120 frases prontas de conversação | ✅ **Implementado** (`livro03.html`). |
| ~~**S08**~~ | ~~`LIVRO_13_Short Stories…`~~ | Na verdade tratado acadêmico (Wyld, *A Short History of English*) | ⚠️ Mal rotulado — **não é short stories.** Não implementar. |
| **S06** | `Inglês em alguns minutos _ .docx` | 729 falas transcritas de desenho animado (níveis básicos) | **Parcialmente** implementado — o painel S06 já traz um subconjunto curado (Jenny, clima, fome). Há muitas cenas/falas ainda não extraídas (números, apresentações, escola…). |
| **S08** | `LIVRO_12_Segredo da Fluência — aprender Inglês com Música` | Método + possíveis letras/frases | Só extrair o inglês real (letras/frases); o miolo é método (fora das REGRAS). |

## 2. Livros de método/dicas no S08 — provavelmente SEM conteúdo sob as REGRAS

As REGRAS do S08 dizem: **só inglês real, nunca dicas/métodos/motivação.** Estes livros são "como aprender inglês" — metodologia. Sob a regra atual, geram pouco ou nenhum card:

- `LIVRO_04_COMO APRENDER INGLÊS (MAURO VERGARA)` — ✅ confirmado por leitura: ~98,5% método, descartado
- `LIVRO_05_Como aprender inglês de maneira natural`
- `LIVRO_06_Como aprender Inglês fácil — Sonia Sánchez`
- `LIVRO_07_Como não aprender Inglês`
- `LIVRO_08_Guia Prático Para Aprender Inglês`
- `LIVRO_09_Memorização para aprender idiomas`
- `LIVRO_10_O Guia definitivo para aprender inglês mais rápido`
- `LIVRO_11_O SEGREDO PARA APRENDER INGLÊS EM MENOS DE UM ANO`
- `LIVRO_14_Guia Definitivo para aprender inglês sozinho`

> Decisão sua: ignorar (recomendado, pela REGRA) ou garimpar exemplos soltos de inglês em uso.

## 3. Fontes já implementadas (staging — pode ignorar para trabalho de painel)

- **`sistemaN_conteudo.md`** espalhados em S01/S02/S03/S04/S05 — dumps de conteúdo já integrados. Ex.: `sistema2_conteudo.md` = os "4 Pilares" (agora no **S10**); `Sistema 02 … _v01.md` = fonte do painel do **S02**; `sistema7_conteudo.md` = colocações verbais (já no **S03**). São cópias de trabalho.
- **S07** — 45 `.docx` de transcrições em 16 canais (All Ears English, Luke's, Kendry, Derek Polyglot, English Coach Chad…): já integrados ao painel do S07.
- **S08** — `LIVRO_01` (1.006 dicas) e `LIVRO_02` (261 frases de viagem): implementados.

## 4. Arquivos administrativos / de processo — NÃO são conteúdo de inglês

Não pertencem a painel (metodologia, handoff, prompts, configs). Candidatos a limpeza — você decide:

- **S01:** pasta `_admin/`, `HANDOFF_*.md`, `PROMPT_REDESIGN_PAINEL.md`, `handoff_tecnico_ingles_brasileiros.md`, `jornada_completa.md`, `SanAmericano_Resumo_Tecnico_Completo.md`, `arquivos_processados.json`, `settings.local.json`, `Sala_001/`, e os `.docx` de prompt/metodologia ("PROMPT UNIVERSAL", "Prompt Universal v2.3", "Crie um resumo técnico…", "Explicação e aplicação", "O que é Words Conectivos", "#(Base).docx").
- **S09:** `RESUMO_SISTEMA09.md` (nota técnica/handoff).

## 5. `#Para distribuição`

Vazia — nada pendente de triagem no momento.
