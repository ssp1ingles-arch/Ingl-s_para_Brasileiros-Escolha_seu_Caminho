# Mapeamento de Arquivos — o que ainda NÃO foi implementado nos painéis

> Scan de S01–S10 em 2026-07-21. Ordem: do mais valioso ao menos.

## 0. Atualização 2026-07-22 — leitura dos PDFs do S08 (LIVRO_03, 04, 13)

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
