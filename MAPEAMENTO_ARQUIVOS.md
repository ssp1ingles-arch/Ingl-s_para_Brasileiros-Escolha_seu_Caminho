# Mapeamento de Arquivos — o que ainda NÃO foi implementado nos painéis

> Scan de S01–S10 em 2026-07-21. Ordem: do mais valioso ao menos.
> **Atualização mais recente: 2026-08-05 (T5) — ver bloco 0w (REORGANIZAÇÃO GERAL: 25 Sistemas renumerados por nível A1→C2). ATENÇÃO: todos os números de Sistema nos blocos 0v e anteriores usam o esquema ANTIGO — a chave de conversão está no bloco 0w.**
> Anteriores: 0v (S24 abandonado), 0u (Sistema 25 com 2 de 3 painéis), 0t (Sistema 26 completo), 0s (Sistema 08 reformatado), 0r (S20 l03, l04 e l07), 0q (S21 l01 e S20 l06), 0p (Sistemas 21 e 22), 0o (Sistema 20), 0n (Sistema 11), 0m (Sistema 14), 0l (Sistema 16), 0k (Sistema 15), 0i (Sistema 13) e 0h (Sistema 12).

## 0w. Atualização 2026-08-05 (T5) — **reorganização geral por nível A1→C2**

Os 25 Sistemas foram renumerados e reordenados por dificuldade pedagógica. **Todos
os números de Sistema citados nos blocos anteriores deste arquivo (0v e abaixo)
referem-se ao esquema ANTIGO** — a tabela abaixo é a chave de leitura.

| Antes | Agora | Título novo |
|---|---|---|
| 23 | **01** | Crianças · Kids Box |
| 07 | **02** | Crianças · Desenho Animado |
| 01 | **03** | Inglês do Zero · Base Completa |
| 19 | **04** | Gramática Básica |
| 04 | **05** | Motor de Verbos |
| 06 | **06** | Situar a Frase *(não mudou)* |
| 05 | **07** | Conectar Frases |
| 10 | **08** | Conversação & Frases |
| 13 | **09** | English for Everyone |
| 03 | **10** | Reduções e Pronúncia |
| 12 | **11** | American English File |
| 15 | **12** | Exercícios e Vocabulário |
| 11 | **13** | Gramática em Uso |
| 16 | **14** | In Use Series |
| 02 | **15** | Dúvidas Pontuais |
| 09 | **16** | Prática Completa · 4 Pilares |
| 08 | **17** | Transcrições e Canais |
| 17 | **18** | Accent Training |
| 14 | **19** | Business & Avançado |
| 18 | **20** | B2 First |
| 25 | **21** | Pronúncia & Conversação |
| 20 | **22** | Gramática Avançada · Proficiency |
| 21 | **23** | Gramática Avançada · Oxford |
| 22 | **24** | Gramática Avançada · Cambridge |
| 26 | **25** | Vocabulário & Oratória |

**Duas correções feitas durante a execução**, ambas necessárias para o mapa fechar:

1. O mapa recebido dizia que a origem do novo S21 era a pasta
   `Sistema 25 — Pronúncia & Conversação`. Essa pasta **não existia** — o disco
   tinha `Sistema 25 — Baseado em Livros V15` (só o *título* no `sistemas.json`
   havia sido mudado, a pasta nunca). Corrigido antes de renomear; sem isso o
   rename teria pulado o sistema em silêncio e o S21 não existiria.
2. A pasta vazia `Sistema 24 — Baseado em Livros V14` (o S24 abandonado, bloco 0v)
   estava fora do mapa e teria sobrevivido, criando **dois "Sistema 24"** e
   **dois "Sistema 25"** no estado final. Removida antes do rename.

**Defeito legado encontrado:** os cabeçalhos dos `REGRAS.md` já estavam com
numeração defasada *antes* desta reorganização — o do Motor de Verbos dizia
"Sistema 03", o de Situar a Frase dizia "05", o de Dúvidas Pontuais dizia "09".
Como as referências cruzadas internas seguiam esse esquema velho, remapeá-las por
número teria produzido lixo; foram corrigidas **por rótulo semântico** ("Verbos por
sentido → S05", "Reduções da fala → S10", "Preposições → S06").

---

## 0v. Atualização 2026-08-05 (T4) — **Sistema 24 ABANDONADO** por fonte inadequada

O Sistema 24 (Baseado em Livros V14 — pronúncia) foi **abandonado**. Os três PDFs
e os três `.md` foram removidos; a pasta ficou vazia. O S24 **nunca chegou a entrar
no `sistemas.json`** e continua fora — a raiz segue com 25 entradas.

### Motivo: não há IPA recuperável em nenhuma das fontes

Diagnóstico feito com PyMuPDF sobre os PDFs originais, contando apenas codepoints
que não existem no alfabeto latino:

| Fonte | Camada de texto | IPA real no PDF | Natureza | Resolução |
|---|---|---|---|---|
| Ship or Sheep | 300.301 chars | **0** | scan com camada OCR corrompida | — |
| Tree or Three | **0 chars** | **0** | imagem pura (1 JPEG/página) | ~145 DPI |
| Clear Speech | **0 chars** | **0** | imagem pura (1 JPEG/página) | **~400 DPI** |
| *(S25)* Pronunciation in Use | **0 chars** | **0** | imagem pura (1 JPEG/página) | ~108 DPI |

**Ship or Sheep** tem camada de texto, mas ela já *é* o OCR corrompido: `rrlektrrk`
(para `electric`, que deveria ser `/ɪˈlektrɪk/`) aparece tanto no PDF quanto no
`.md`, e os dois têm 84% de similaridade. Reextrair devolveria o mesmo lixo — a
destruição do IPA aconteceu antes deste PDF existir. Outros exemplos da mesma
corrupção: `electricity` → `/l,lekrtrrseti/`, `/æ/ man` → `lllnl man`,
`/e/ and /æ/` → `lel and la'l`.

**Tree or Three e Clear Speech** não têm texto nenhum — `get_text()` devolve string
vazia nas 138 e 194 páginas. São digitalizações puras.

> **Correção de um detalhe da decisão:** a justificativa original dizia que Tree or
> Three *e Clear Speech* estavam abaixo de 300 DPI. Isso vale para o Tree or Three
> (~145 DPI), mas **Clear Speech está a ~400 DPI** — acima do limiar. O abandono
> dele se sustenta por outro motivo: zero texto extraível e nenhuma engine de OCR
> com suporte a IPA disponível no ambiente. Se um dia houver OCR com modelo
> fonético, **Clear Speech é o único dos três que não precisa ser redigitalizado.**

### Caminho de OCR também bloqueado

`pytesseract` ausente e binário `tesseract` fora do PATH. Além disso, o Tesseract
padrão não reconhece símbolos IPA — precisa de modelo treinado para fonética. E a
145/108 DPI o diacrítico de IPA, que é traço pequeno, não sobrevive ao
reconhecimento.

### S25 livro02 — PDF apagado, MD mantido

`English Pronunciation in Use Intermediate` (Cambridge): o PDF foi removido pelo
mesmo motivo (imagem pura, ~108 DPI, zero IPA), mas o **`.md` foi mantido** — tem
312 KB de texto que pode servir para conteúdo não-fonético no futuro. O
**placeholder no hub do S25 permanece** (`<div class="hub-card soon">`, sem href,
com o selo "Em breve — aguardando reconversão do OCR").

### O que destravaria

Só uma fonte melhor, não uma conversão melhor: **PDF digital original com texto
embutido** dessas obras. Com texto real, a extração PyMuPDF entrega o IPA intacto.
Sem isso, o conteúdo de pronúncia é inutilizável e o S24 não volta.

---

## 0u. Atualização 2026-08-05 (T3) — Sistema 25 (Pronúncia & Conversação) · **2 de 3 livros**

| Painel | Livro | Blocos | Itens |
|---|---|---|---|
| `livro01.html` | Speak English: 30 Days to Better English | 12 | **156** |
| `livro02.html` | English Pronunciation in Use Intermediate | — | **pendente** |
| `livro03.html` | Everyday Dialogues | 12 | **156** |
| | | **24** | **312** |

Hub criado com três cards: dois ativos e o `livro02` como **placeholder sem
`href`** (um `<div class="hub-card soon">`, não um `<a>`, para não gerar link
morto), com o selo "Em breve — aguardando reconversão do OCR". S25 entra no
`sistemas.json` — a raiz vai de 24 para **25 entradas**.

**Livro 01 — a chave foram as páginas de resposta.** O livro é organizado em 30
dias temáticos, e os exercícios são de lacuna. As páginas `Progress check -
Answers` trazem a frase **completa**, com a lacuna já preenchida: são 488 frases
inteiras. Agrupei os 30 dias em 12 blocos (apresentar-se, família e descrever
pessoas, rotina, onde você mora, pedir ajuda na rua, pedir algo, compras,
comparar, descrever, casa, montar a pergunta, notas de uso). Mesmo recurso já
usado nos Sistemas avançados — ver bloco 0r.

**Livro 03 — diálogos íntegros.** A fonte tem 30 diálogos numerados
(`Dialogue 1-1` … `3-11`) com falante identificado, e o OCR preservou a estrutura.
Extraí os 29 que têm três ou mais falas e montei 12 blocos por situação.

**Normalização aplicada nas duas fontes:** ligaduras tipográficas do dump
(`Oﬃcial` → Official, `ﬂat` → flat) via `unicodedata.normalize('NFKC')` antes de
qualquer extração. Sem isso as palavras entram no painel com glifo quebrado.

**Descartado (REGRAS_GERAIS §4):** "como usar este livro", método e motivação, os
enunciados sem inglês, os gabaritos de alternativa (`1-a, 2-c`) e, no livro 03, os
fragmentos de fala sem contexto e as `LANGUAGE NOTES` que são comentário
pedagógico.

`tmp/garimpa.py` versionado nesta leva — é a ferramenta de medição de candidatos
usada antes de extrair, ao lado de `mkpanel.py` e `hubcard.py`.

### ⚠️ S25 livro02 — pendente de reconversão do OCR

`English Pronunciation in Use Intermediate` (Cambridge) tem transcrição fonética
em praticamente todo item, e **o IPA não sobreviveu à conversão**. O painel não sai
sem isso: um livro de pronúncia sem símbolo fonético vira lista de palavras solta,
que as REGRAS mandam descartar. Mesma causa dos três livros do S24.

**Ordem sugerida quando a reconversão sair:** S24 l03 (Clear Speech, 82,5% limpo),
depois S25 l02, e por fim S24 l02 e l01 — que são os piores OCRs do acervo.

---

## 0t. Atualização 2026-08-05 (T2) — Sistema 26 (Vocabulário & Oratória) · **completo**

Os três livros do S26 viraram painel, a partir dos `.md` (os PDFs seguem só como
arquivamento, e continuam fora do git pelo `.gitignore`).

| Painel | Livro | Blocos | Itens |
|---|---|---|---|
| `livro01.html` | Vocabulary Builder (Norman Lewis) | 12 | **157** |
| `livro02.html` | Talk Like TED (Carmine Gallo) | 12 | **156** |
| `livro03.html` | The Art of Public Speaking (Carnegie & Esenwein, 1915) | 12 | **156** |
| | | **36** | **469** |

Hub criado do zero (não existia) e S26 adicionado ao `sistemas.json` — a raiz
passa de 23 para **24 entradas**.

**Recorte de cada livro.** O `livro01` é organizado por família de raiz, como o
próprio Lewis ensina: `ego/alter`, `verto`, `dexter/sinister`, `misein`,
`monos-bi-polys`, `-logy`, `-iatreia/paidos`, `derma`, prefixos, sufixos, o método
do autor e os pares que o brasileiro troca. O `livro02` segue os nove segredos do
Gallo, mas sempre pelas falas reais dos palestrantes (Jobs, Gates, Robinson,
Cuddy, Bryan Stevenson, Jill Bolte Taylor), mais dois blocos práticos de frases de
abertura e vocabulário de oratória. O `livro03` vai por técnica — medo de palco,
domínio da plateia, monotonia, ênfase por contraste, tom, ritmo, pausa,
sinceridade — com as máximas e os trechos que o livro manda ler em voz alta.

**Descartado (REGRAS_GERAIS §4).** No Lewis, os exercícios de pareamento, os
quizzes YES/NO, as lacunas, as **302 linhas de `KEY:`** (gabarito isolado) e as
listas de palavras sem frase de uso — que são a maior parte do volume bruto. No
Gallo, o "como usar este livro", os resumos de capítulo sem inglês e o comentário
metodológico. No Carnegie, os enunciados de exercício vazios.

### A quebra de linha hifenizada — o detalhe que mudou o diagnóstico

Numa primeira leitura o Vocabulary Builder parecia render só ~68 linhas
aproveitáveis, e foi reportado como abaixo do mínimo. O erro era de método: o dump
quebra palavra no fim da linha (`the pro-
noun ego`), e sem remontar isso a prosa
do livro se fragmenta e some no filtro. Com as quebras remontadas, o mesmo arquivo
rende **2.322 frases de prosa aproveitáveis**. Vale para qualquer `.md` desta
leva — **remontar antes de medir.**

### Qualidade de OCR das nove fontes (medida)

Percentual de linhas que passam no filtro de sanidade tipográfica:

| Livro | % limpo | Coladas | Lixo |
|---|---|---|---|
| S26 l03 · Art of Public Speaking | 88,5% | 0,16% | 1,5% |
| S26 l02 · Talk Like TED | 88,4% | 0,25% | 2,3% |
| S24 l03 · Clear Speech | 82,5% | 0,16% | 0,7% |
| S25 l01 · Speak English 30 Days | 78,4% | 0,04% | 9,0% |
| S25 l03 · Everyday Dialogues | 71,9% | 0,13% | 2,5% |
| S26 l01 · Vocabulary Builder | 68,1% | 0,55% | 6,1% |
| S25 l02 · Pronunciation in Use | 66,1% | 0,77% | 0,4% |
| S24 l02 · Tree or Three | 64,7% | 1,45% | 0,1% |
| S24 l01 · Ship or Sheep | 56,5% | 1,51% | 8,3% |

### ⚠️ S24 e S25 — aguardando reconversão do OCR

Os três piores OCRs do acervo são os livros de pronúncia do S24, e o motivo é
estrutural: são páginas densas com transcrição fonética, e **o IPA foi destruído
na conversão** — `electric` virou `/rrlektrrk/`, `electricity` virou
`/l,lekrtrrseti/`. A corrupção não para no IPA: palavras se fundem
(`Didyou see the men?`, `That'sabadcut.`) e há lixo de scanner no meio da frase
(`rvVhy don't you come down?`, `\Mhat a beautiful curl!`).

O núcleo do Ship or Sheep são **173 frases de par mínimo** rotuladas `a -`/`b -`,
recuperáveis mas exigindo conserto item a item. **Decisão pendente do usuário:**
reconverter os PDFs de S24/S25 antes de implementar.

---

## 0s. Atualização 2026-08-05 — Sistema 08 (Transcrições e Canais) · **reformatado, 45 episódios**

> Não confundir com o "Sistema 08" citado nos blocos 0b e 0 abaixo: aqueles são da
> **numeração antiga** (pasta de PDFs/livros, hoje renumerada). Este bloco é sobre o
> **Sistema 08 — Transcrições e Canais** atual.

Os 45 episódios dos 16 canais foram reprocessados a partir dos `.docx` de origem e
passaram a ter três blocos por episódio, com o rótulo do primeiro bloco escolhido
pela **natureza real da fala** do vídeo:

| Rótulo | Quando | Episódios |
|---|---|---|
| 🎙️ Diálogo — troca real entre falantes (`A:`/`B:`) | dois falantes identificáveis | 11 |
| 🎙️ Diálogo — trechos de conversa (sem rótulo de falante) | coletânea roteirizada sem pontuação na fonte | 5 |
| 🎙️ Fala contínua | um apresentador só | 12 |
| 🔁 Treino de repetição | drill / lista | 16 |
| 💬 Expressões · 📌 Frases que você pode usar amanhã | conforme o episódio | 18 · 43 |

**O que estava errado e foi corrigido:**

- **13 episódios em `<p>` único** (até 271 KB de texto corrido dentro de uma caixa
  com `max-height:52vh`). Reprocessados da fonte. O achatamento tinha acontecido na
  geração do HTML, não no `.docx`: as fontes tinham de 1.641 a 4.014 linhas.
- **Expressões de lista fixa.** As 231 "expressões em contexto" vinham de um
  *lookup* de 52 chunks aplicado a todos os episódios — `want to` (21×), `you know`
  (19×), `kind of` (15×) apareciam como expressão idiomática, inclusive em lições de
  preposição. Agora são **137**, extraídas do texto de cada episódio; quem não tem
  expressão ensinada ficou **sem o bloco** em vez de receber preenchimento genérico.
- **Frases prontas por corte cego.** Eram sempre exatamente 40, as primeiras do
  episódio, com lixo de timestamp (`7 segundos I'm protecting myself.`). Agora são
  **663** selecionadas.
- **Timestamps incrustados na fala** (`N segundos`, `3:02:56`) — na fonte são
  parágrafos separados e tinham sido fundidos ao texto. Removidos na extração.
- **Comentário pedagógico tratado como diálogo real** (Chad, Kayla), que violava o
  `REGRAS.md` §5. Passou a 🎙️ Fala contínua.
- **`REGRAS.md` com numeração defasada em 1** nos dois Sistemas: o do S08 se
  identificava como "Sistema 07" e o do S07 como "Sistema 06". Corrigidos, junto das
  referências cruzadas internas.
- **Cards do index genéricos** — os 16 repetiam a mesma frase. Individualizados
  conforme a natureza do canal.

### ⚠️ Pendência de fonte — Luke's English Podcast, episódio 959

Os dois `.docx` do canal têm **praticamente o mesmo conteúdo**:

| Arquivo | Texto extraído |
|---|---|
| `Luke_s English Podcast _ (x) 872. The Birthday Party (Learn English with a Short Story).docx` | 40.237 chars |
| `Luke_s English Podcast _ How to Learn English with my podcast 🎧 [959].docx` | 40.178 chars |

O `.docx` do **959** carrega a transcrição do **872** (o conto "The Birthday
Party"), não o conteúdo do próprio episódio 959. Por isso os dois painéis do canal
exibem o mesmo texto e quase as mesmas expressões.

**A duplicação está na fonte, não na geração** — nenhum reprocessamento resolve.
Para corrigir é preciso substituir o `.docx` do 959 pela transcrição correta e
rodar de novo o build do canal. Enquanto isso, o canal conta como 2 episódios mas
entrega 1 conteúdo distinto.

---

## 0r. Atualização 2026-08-04 (T3) — S20 livros 03, 04 e 07 · **os três Sistemas avançados fechados**

> Fecha as três pendências abertas no bloco 0q. Com isto, **os 15 painéis dos
> Sistemas 20, 21 e 22 estão todos acima do mínimo de 12 blocos / 150 itens**,
> verificado por `tmp/mkpanel.py check`.

| Painel | Antes | Depois | Ganho |
|---|---|---|---|
| S20 · `livro03.html` — Grammar and Vocabulary for Advanced | 10 blocos / **106** itens | 28 blocos / **251** itens | +18 blocos, +145 itens |
| S20 · `livro04.html` — Advanced Language Practice (Vince) | 9 blocos / **81** itens | 29 blocos / **248** itens | +20 blocos, +167 itens |
| S20 · `livro07.html` — English Pronunciation in Use Advanced | 6 blocos / **43** itens | 26 blocos / **200** itens | +20 blocos, +157 itens |

**S20 livro03 — a seção de vocabulário inteira.** A primeira passada tinha ficado
só na seção de *gramática* (Units 1–25), que já é coberta pelos livros 01, 02 e 05
do Sistema. A segunda passada pegou a **seção de vocabulário (Units 26–45)**, que
nenhum outro painel do S20 toca — nem o livro06, que é do mesmo editor mas de
outra obra. Recorte: a língua do segredo, os pares que se confundem, os adjetivos
de crítica que elogiam × os que destroem, migração, `take` × `make`, linguagem
neutra de gênero, gradável × extremo, phrasal verbs com `get` e a manchete
econômica. *Um bloco escrito foi descartado antes do commit por duplicar o `s07`
(sufixos `-free`/`-friendly`/`-mad`), que já existia.*

**S20 livro04 — proof-reading, phrasal 2/3 e as Words and phrases.** Três seções
que faltavam. A **Grammar 28** traz ortografia, parônimos, homófonos e
**pontuação** — território que nenhum outro livro dos três Sistemas cobre, e cujas
regras não são as do português. Mais as listas **2 e 3 de phrasal verbs** (o painel
só tinha a 1) e as dez seções **Words and phrases** que fecham o livro. As frases
de exercício foram remontadas **completas** a partir da chave de respostas do
próprio livro, conforme `REGRAS_AVANCADO.md` §3.

### S20 livro07 — a limitação do OCR, verificada e contornada

A advertência sobre o IPA se confirmou, e por script: o `.md` tem **zero**
caracteres IPA restantes. O que sobrou dentro das barras é lixo — `/a:sbr.../`,
`/n?1l/`, `/0ae?/` — e em vários casos dois fonemas distintos colapsaram no mesmo
dígrafo ASCII, o que torna a reconstrução impossível mesmo por inferência.
**Nenhum símbolo foi reconstruído**; confirmado por script que os 20 blocos novos
não contêm transcrição fonética.

O que **sobreviveu intacto** foi a metade *prosódica* do livro, porque ela é feita
de prosa e de MAIÚSCULAS, não de símbolo:

- a marcação de proeminência — `He's got a HOUSE in LIVerpool`;
- as marcas de acento `'` e `,` — `,contro'versial`, `'news,paper`;
- as unidades de fala marcadas com `//`.

Sobre isso foram montados os 20 blocos: britânico × americano, acento em composto
(por tipo e em compostos de três partes), phrasal verbs de um e de dois acentos
— onde o acento chega a mudar o sentido (`'live on` × `,live 'on`) —, ligação
entre palavras, contrações que só existem na fala, o `t` que cai ou vira oclusiva
glotal, unidades de fala e como o corte muda o sentido, proeminência, a palavra
final «vazia», expressões vagas, tom descendente × ascendente como marca de
*notícia × não notícia*, *tails*, question tags nos dois tons, contraste, a
exclamação que vira sarcasmo só pelo tom, os sinais de escuta ativa, os incisos da
fala preparada e o *step-up* do palestrante. Onde a fonte só tinha IPA, o som vai
**descrito em palavras**.

**A meta de 150 itens foi atingida sem inventar nada** — o material legível era
mais abundante do que a estimativa inicial sugeria. O que ficou de fora, e ficará:
os exercícios de transcrição fonética e a Section E1 (prática do alfabeto
fonêmico), que dependem inteiramente dos símbolos perdidos. Recuperá-los exigiria
um **novo OCR do PDF** com suporte a Unicode fonético.

### Estado final dos três Sistemas avançados

| Sistema | Painéis | Faixa de itens |
|---|---|---|
| **S20** · V11 | 7 de 7 | 157 – 291 |
| **S21** · V12 | 5 de 5 | 162 – 276 |
| **S22** · V13 | 3 de 3 | 150 – 174 |

Nenhum painel abaixo do mínimo. `tmp/hubcard.py status` não aponta nenhum card
desencontrado do respectivo painel em nenhum dos três hubs.

---

## 0q. Atualização 2026-08-04 (T2) — segunda passada nos dois painéis rasos

> As duas pendências registradas no bloco 0p foram fechadas. Os dois painéis
> passaram do mínimo de **12 blocos / 150 itens** por larga margem.

| Painel | Antes | Depois | Ganho |
|---|---|---|---|
| S21 · `livro01.html` — Oxford English Grammar Course Advanced | 14 blocos / **91** itens / 46 KB | 36 blocos / **276** itens / 143 KB | +22 blocos, +185 itens |
| S20 · `livro06.html` — English Vocabulary in Use Advanced 3rd | 8 blocos / **88** itens / 36 KB | 30 blocos / **291** itens / 146 KB | +22 blocos, +203 itens |

**S21 livro01 — o que a segunda passada acrescentou.** A primeira passada
(2026-08-03) tinha lido só as Seções 2–5 do Swan. Esta leu o resto das 17 Seções
da Parte 1 e a **Parte 2 inteira** (*grammar beyond the sentence*): negativas
(`not` × `no`, `I don't think`), pergunta negativa, imperativo e exclamação,
modais perfeitos (com o par `needn't have` × `didn't need to`), `had better` e
`be supposed to`, as razões reais para usar passiva e a passiva de relato do
noticiário, infinitivo × `-ing` em dois blocos, verbo + preposição, causativas,
as exceções de artigo, seis pares de preposição confundida, *fronting* e
inversão, as duas *cleft sentences*, discourse markers de argumento e de
atitude, elipse, gramática da conversa e estilos abreviados.

**S20 livro06 — sobreposição verificada antes de escrever.** Como o S21 livro02
é a edição em 100 unidades do mesmo livro, foi conferido o recorte de lá antes
de escolher o daqui. O S21 ficou com as unidades **temáticas** (trabalho,
carreira, dinheiro, caráter, relações, aparência, prefixos, idioms, phrasal
verbs) — nada disso entrou aqui. O recorte novo é o que o S21 não toca:
palavras que se confundem e polissemia, sufixos, raízes clássicas e *blends*,
siglas, as cinco metáforas mortas do inglês corrente, a escala da vagueza
numérica, o jeito de dizer, a manchete, a língua da burocracia, escrita
acadêmica em dois blocos, e o vocabulário funcional (permitir, reclamar,
desculpar-se, elogiar, concordar, recordar, causa e efeito, comparar,
modalidade). **Zero repetição de bloco entre os dois painéis.**

### Utilitários agora versionados

`scratchpad/mkpanel.py` e `scratchpad/hubcard.py` viviam no scratchpad da sessão
e se perderam de novo. Foram reescritos e **versionados em `tmp/`**:

- **`tmp/mkpanel.py`** — `check` conta blocos/itens e sai com erro abaixo do
  mínimo; `append` acrescenta blocos de um spec JSON a um painel existente,
  renumerando os ids e atualizando a métrica de blocos; `build` gera painel novo.
  A gravação trava com `assert` se ficar abaixo de **12 blocos / 150 itens**.
- **`tmp/hubcard.py`** — `sync` atualiza o `.hc-meta` do card lendo os números
  **do próprio painel**; `status` aponta card desencontrado do conteúdo;
  `metric` recalcula o "N/M painéis prontos" do topo do hub.

### Pendência nova que o `hubcard.py status` revelou

Rodar `hubcard.py status` no hub do S20 mostrou que **outros três painéis do S20
estão abaixo do mínimo de 150 itens** — não estavam mapeados até agora:

| Painel | Estado | Fonte disponível |
|---|---|---|
| S20 · `livro03.html` — Grammar and Vocabulary for Advanced | 10 blocos / **106** itens | `.md` na pasta |
| S20 · `livro04.html` — Advanced Language Practice (Michael Vince) | 9 blocos / **81** itens | `.md` na pasta |
| S20 · `livro07.html` — English Pronunciation in Use Advanced | 6 blocos / **43** itens | `.md` na pasta |

Os demais painéis dos três Sistemas avançados estão todos acima do mínimo.

---

## 0p. Atualização 2026-08-04 — Sistemas 21 e 22 (Gramática Avançada) · **fechados**

> Segue o `REGRAS_AVANCADO.md`. Acento dourado `#F59E0B`; a explicação **é** conteúdo;
> entram comparação entre estruturas, nota de registro e erro comum com o porquê.
> Mínimo aplicado nesta sessão: **12 blocos e 150 itens por painel** (verificado por script).

### S21 — Baseado em Livros V12 · agora 5 de 5 painéis

| Livro | Arquivo `.md` | Painel | Blocos | Itens | Tamanho | Status |
|---|---|---|---|---|---|---|
| S21 · Livro 01 | `01_Oxford English Grammar Course Advanced…` | `livro01.html` | 14 | 91 | 45 KB | ✅ 2026-08-03 |
| S21 · Livro 02 | `02_English Vocabulary in Use Advanced 100 units…` | `livro02.html` | 18 | 214 | 64 KB | ✅ **2026-08-04** |
| S21 · Livro 03 | `03_English Vocabulary in Use Upper-intermediate…` | `livro03.html` | 18 | 219 | 60 KB | ✅ **2026-08-04** |
| S21 · Livro 04 | `04_Grammar and Vocabulary for Cambridge Advanced and Proficiency` | `livro04.html` | 16 | 162 | 55 KB | ✅ **2026-08-04** |
| S21 · Livro 05 | `05_New English File - Advanced Level…` | `livro05.html` | 21 | 164 | 59 KB | ✅ **2026-08-04** |

### S22 — Baseado em Livros V13 · agora 3 de 3 painéis (era 0)

| Livro | Arquivo `.md` | Painel | Blocos | Itens | Tamanho | Status |
|---|---|---|---|---|---|---|
| S22 · Livro 01 | `01_Advancing Vocabulary Skills - By Sherrie L. Nist` | `livro01.html` | 15 | 150 | 57 KB | ✅ **2026-08-04** |
| S22 · Livro 02 | `02_English Advancing A Bridge to Success` | `livro02.html` | 20 | 174 | 55 KB | ✅ **2026-08-04** |
| S22 · Livro 03 | `03_New Cambridge Advanced English Student's book` | `livro03.html` | 16 | 155 | 58 KB | ✅ **2026-08-04** |

**Total da sessão: 7 painéis novos, 1.238 itens.**

### Sobreposição verificada — S21 livro02/03 × S20 livro06

Antes de implementar, foi conferido se `02_English Vocabulary in Use Advanced`
e `03_… Upper-intermediate` são edições distintas do S20 livro06. Resultado:

- **S21 livro02 e S20 livro06 são o MESMO livro** (McCarthy & O'Dell, Cambridge)
  em edições diferentes: o S20 tem a **3ª edição (2017)**; o S21 tem a edição em
  **100 unidades (2002)**. Comparando os sumários, ~25 unidades batem com título
  idêntico (`Travel and accommodation`, `Cramming for success`, `Weather and climate`,
  `At work: colleagues and routines`, `Advertising`, `Talking about books`,
  `Divided by a common language`, `Abbreviations and acronyms`…), e a sobreposição
  real é maior — o OCR degradado impede casar o resto automaticamente.
- **Mas o painel do S20 livro06 é raso** (7 blocos, 37 KB) e pegou só o
  **meta-vocabulário**: colocação, conotação, registro, idioms gerais, fórmulas de
  polidez, britânico × americano. As ~90 unidades **temáticas** ficaram de fora.
- **Decisão:** o S21 livro02 foi construído sobre o que o S20 deixou de fora —
  trabalho e rotina de escritório, carreira, negócios, dinheiro pessoal, adjetivos
  de caráter e sociabilidade, desejo e aversão, aparência, prefixos, idioms de
  situação e phrasal verbs. Zero repetição de bloco entre os dois painéis.
- **S21 livro03 (Upper-intermediate) é livro diferente**, de outro nível (B2–C1).
  Sem conflito. Recorte próprio: formação de palavra, som (onomatopeia, homógrafos,
  homófonos), incontáveis, coletivos e expressões fixas (similes, binomials, idioms).

### Recorte de cada painel novo

- **S21 l02** — unidades temáticas do *Vocabulary in Use Advanced* (complementar ao S20 l06).
- **S21 l03** — como a palavra inglesa **se monta e como soa**: compostos, substantivos
  nascidos de phrasal verb, origens (nomes de gente e de cidade), a lógica sonora do
  `gr-`/`cl-`/`sp-`, homógrafos e homófonos, incontáveis, coletivos, similes e binomials.
- **S21 l04** — o que o **CAE/CPE Paper 3** cobra: subjuntivo presente e passado, Unreal
  Past, condicionais improváveis, inversão após advérbio negativo (com a regra de quando
  **não** inverter), cleft com `it`/`what`/`all`, metáfora lexical, prefixos e sufixos,
  paráfrase estrutural.
- **S21 l05** — a gramática **dentro da conversa**: discourse markers (resultado, razão,
  contraste, digressão), *distancing* com `seem`/`appear` e passiva de relato, a escala da
  especulação com modais, `have` em todas as funções (inclusive o causativo), cleft da fala,
  sons e voz humana.
- **S22 l01** — **único livro americano** dos três Sistemas avançados (`padrão US`). Método
  próprio: nenhuma palavra é definida antes de ser usada. Reorganizado **por campo semântico**,
  não por capítulo, como manda o `REGRAS_AVANCADO.md` §3.
- **S22 l02** — **linguagem funcional**: pedir (com a armadilha do `would you mind`), oferecer,
  aceitar/recusar, opinar em dois registros, criticar, pedir esclarecimento, `wish`/`if only`,
  condicionais mistas, discurso indireto, perguntas indiretas, subjuntivo de recomendação.
- **S22 l03** — as duas seções fixas do Leo Jones: **Grammar review** e **Word study**. Juntar
  frases do falado para o escrito, o sistema do passado + expressões de tempo, modais em pares
  que se confundem, escalas de força entre sinônimos, artigos, contável × incontável, prefixos.

### Também atualizados

- Hubs `index.html` do S21 e do S22: todos os cards "Em breve" viraram cards ativos, com
  blocos/itens reais; métrica passou a **5/5** e **3/3 painéis prontos**.
- A nota do hub do S21 sobre "PDFs sem prefixo numérico" foi corrigida — **todos já estão
  prefixados**; a nota agora aponta a relação complementar entre S21 l02 e S20 l06.

### Pendências conhecidas

- **S21 livro01 está abaixo do mínimo desta sessão**: 14 blocos / **91 itens** (mínimo 150).
  Foi implementado na sessão de 2026-08-03, antes da regra valer. Fica registrado para
  ampliação futura — não foi mexido aqui por estar fora da ordem pedida.
- **S20 livro06 continua raso** (7 blocos / 37 KB) e agora é o painel mais fino dos três
  Sistemas avançados. Como o S21 l02 cobre o complemento temático, a ampliação do l06
  deixou de ser urgente, mas segue em aberto.
- Os utilitários `scratchpad/mkpanel.py` e `scratchpad/hubcard.py` **não existiam** no
  repositório nem no histórico do git. Foram reescritos do zero nesta sessão, a partir do
  `livro01.html` do S21 como molde, e vivem no scratchpad da sessão (não versionados).
  `mkpanel.py` trava a gravação com `assert` se o painel ficar abaixo de 12 blocos ou 150
  itens; `hubcard.py` lê blocos/itens **do próprio painel**, para o card nunca desencontrar
  do conteúdo.

---

## 0o. Atualização 2026-08-03 — Sistema 20 (Baseado em Livros V11 · Gramática Avançada) · livro 01

> **Este Sistema segue o `REGRAS_AVANCADO.md`, não as regras de livro dos demais.** Acento dourado `#F59E0B`; a explicação **é** conteúdo; entram comparação entre estruturas, nota de registro e erro comum com o porquê.

| Livro | Arquivo `.md` | Painel | Blocos | Itens | Tamanho | Status |
|---|---|---|---|---|---|---|
| S20 · Livro 01 | `01_Objective Proficiency Student's Book with Answers…` | `livro01.html` | 20 | 232 | 91 KB | ✅ **2026-08-03** |

**É o primeiro painel do Sistema 20** — até aqui a pasta só tinha o `index.html`.

**Fonte dentro do livro:** o **Grammar folder** (páginas 178–188 do impresso,
`Página 180`–`190` no `.md`), que é onde o Objective Proficiency concentra a
explicação de gramática das 20 unidades. É exatamente o material que o
`REGRAS_AVANCADO.md` §4 pede: estrutura → explicação → exemplo → comparação →
registro. O corpo das unidades (textos de listening, tarefas de speaking,
exercícios de Use of English) ficou fora.

**Ordem:** pedagógica, não a do livro, como manda o `REGRAS_AVANCADO.md` §3 —
substantivos e artigos primeiro, depois tempos verbais, modais, condicionais,
gerúndio/infinitivo, passiva, discurso indireto e só então oração participial,
inversão, gradação, comparação e ordem dos advérbios.

**OCR:** o `.md` do Grammar folder vem com as **duas colunas intercaladas**
(uma linha de cada coluna, alternando). Todos os 20 blocos foram remontados a
partir do sentido; nenhuma frase de exemplo foi inventada.

**Descartado:** enunciados de exercício, gabaritos, mapas de conteúdo,
referências cruzadas de página e o material de exame que não é linguagem
(instruções de prova, tempos de gravação).

**Também atualizados:** o hub do S20 (card do livro 01 saiu de "Em breve" para
ativo; métrica "em preparação" → "1 disponível"), a tabela do
`REGRAS.md` da pasta e a entrada 20 do `sistemas.json`.

**Situação do S20 em 2026-08-03 (fim da sessão):** 6 dos 7 painéis prontos.

| Livro | Painel | Blocos | Itens | Recorte |
|---|---|---|---|---|
| 01 · Objective Proficiency | `livro01.html` | 20 | 232 | Grammar folder inteiro, ordem pedagógica |
| 02 · Advanced Grammar in Use | `livro02.html` | 20 | 221 | 20 das 100 unidades, as que não repetem o 01 |
| 03 · Grammar and Vocabulary for Advanced | `livro03.html` | 10 | 106 | padrões de complemento e orações |
| 04 · Advanced Language Practice | `livro04.html` | 9 | 81 | colocação: organizadores, preposições, phrasal |
| 05 · Complete Advanced | — | — | — | ⏳ **pendente** |
| 06 · English Vocabulary in Use Advanced | `livro06.html` | 8 | 88 | as unidades do "inglês sobre o inglês" |
| 07 · English Pronunciation in Use Advanced | `livro07.html` | 6 | 43 | acento e proeminência (IPA do OCR inutilizável) |

**Os painéis não têm todos o mesmo tamanho, e isso é deliberado em parte e
circunstancial em parte.** Deliberado: cada livro entrou só com o que os
anteriores do Sistema não cobriam, e quanto mais painéis o Sistema ganha, menor
fica a área que sobra para o seguinte — o 01 e o 02 pegaram a gramática inteira,
os demais pegaram o que restou. Circunstancial: o livro 07 é pequeno porque o
OCR destruiu os símbolos fonéticos, e recompor IPA por adivinhação teria
produzido um painel de pronúncia com erros.

**Pendentes:** S20 livro05 (*Complete Advanced*), os 5 livros do **S21** e os 3
do **S22** — 9 painéis.

## 0n. Atualização 2026-08-03 — Sistema 11 (Baseado em Livros V02) · CONCLUÍDO (livros 03, 05 e 06)

> Fonte: **exclusivamente o arquivo `.md`**. Template visual novo (o mesmo do S14/S15/S16/S18), não o antigo `example-list` dos livros 01, 02 e 04 deste Sistema.

| Livro | Arquivo `.md` | Painel | Blocos | Itens | Tamanho | Status |
|---|---|---|---|---|---|---|
| S11 · Livro 03 | `03_Oxford-Guide-to-English-Grammar.md` | `livro03.html` | 23 | 370 | 107 KB | ✅ **2026-08-03** |

**Critério de recorte — este é o ponto importante.** O Oxford Guide tem 453
páginas e 40 capítulos de gramática de referência; despejar tudo produziria um
painel redundante, porque os livros 01 (*English Grammar in Use*), 02 (*Grammar
Practice*) e 04 (*Essential Grammar in Use*) deste mesmo Sistema já cobrem
tempos verbais, modais, condicionais, artigos, preposições e relativas **com
exercício**. O painel foi montado só sobre o que o Eastwood tem e eles não têm:

- **Cap. 5 — elipse e substituição** (parar no auxiliar, o `to` solto, `So do I`,
  `do so/do it/do that`, `I think so / I'm afraid not`, one/ones, estilos que
  cortam tudo: placa, manchete, instrução, cartão-postal, anotação).
- **Cap. 6 — ordem da informação e ênfase** (velho antes / novo depois, front
  position, inversão, `there + be`, `it` vazio, `do` enfático, clivadas com
  *it* e com *what*).
- **Cap. 7 — inglês falado × escrito** (transcrição de conversa real, *well*,
  *you know*, *sort of*, *or something*, entonação que sobe e desce, formas
  fracas e curtas, pontuação — incluindo o erro de ligar duas orações só com
  vírgula, que é transferência direta do português).
- **Cap. 40 — British × American English**, o apêndice inteiro: verbos,
  substantivos, adjetivos, preposições, conjunções e grafia.

**Descartado:** os capítulos 1–4 e 8–39, por sobreposição com os outros livros do
Sistema; os quadros de resumo e os índices remissivos.

**Também atualizados:** o hub do S11 (card do livro 03 saiu de "Em breve" para
ativo; métricas 3 → 4 disponíveis, 3.900+ → 4.270+ exemplos) e a entrada 11 do
`sistemas.json`.

### Livro 05 — English Pronunciation Made Simple · ✅ 2026-08-03

| Livro | Arquivo `.md` | Painel | Blocos | Itens | Tamanho | Status |
|---|---|---|---|---|---|---|
| S11 · Livro 05 | `05_English Pronunciation Made Simple.md` | `livro05.html` | 22 | 239 | 77 KB | ✅ **2026-08-03** |

**Critério de recorte.** Pronúncia já aparece em três outros pontos do projeto
(S03 livro01 · Rachel's English; S14 livro05 · Susan Cameron; S16 livro03 ·
*Pronunciation in Use Elementary*). O que o Dale & Poms tem de próprio é o
**mapa das confusões**: em cada uma das 42 lições ele diz qual som o aluno vai
pôr no lugar e **que palavra vai sair** (*sheep → ship*, *very → berry*,
*thank → sank*, *state → estate*). O painel foi montado sobre isso: por bloco,
o erro nomeado, o par mínimo, a frase de contraste em que o erro muda o
sentido e a instrução física da boca. Inclui as três lições de Parte 2 —
acento da palavra, acento da frase (*content* × *function words*), ritmo
(contração, *blending*, redução: `ham'n cheese`, `pieceapie`, `Whatimeisit?`)
e entonação.

**OCR:** os símbolos fonéticos vieram corrompidos no `.md` (`[il`, `[erl`,
`[0]`, `Ifl`…). Todos foram restaurados em IPA a partir do título de cada lição
e dos exemplos.

**Descartado:** enunciados de exercício, gabaritos do Apêndice II, instruções
de faixa de CD e os poemas de leitura em voz alta.

### Livro 06 — Reactivate Your Grammar &amp; Vocabulary C1/C2 · ✅ 2026-08-03

| Livro | Arquivo `.md` | Painel | Blocos | Itens | Tamanho | Status |
|---|---|---|---|---|---|---|
| S11 · Livro 06 | `06_Reactivate Your Grammar And Vocabulary C1C2 - Exams.md` | `livro06.html` | 21 | 253 | 88 KB | ✅ **2026-08-03** |

**Com este painel o Sistema 11 fecha (6/6).** É o livro de nível mais alto do
Sistema, e o recorte pegou justamente o que os outros cinco não alcançam:
`wish`/`if only` nos cinco padrões, `would rather/sooner/prefer`,
`it's high time`, `as if/as though`, o discurso indireto completo (tabela de
mudanças, os casos em que **não** muda, perguntas relatadas e o padrão
sintático de cada verbo de relato), o subjuntivo, a passiva nas formas
difíceis (gerúndio, infinitivo perfeito, `get`-passive, dois objetos,
`let/help/make`, `by` × `with`), as estruturas impessoal e pessoal
(`It is said that…` × `He is said to…`), o causativo, a inversão, as clivadas,
o *fronting* e os conectores de causa, propósito e contraste.

**Descartado:** os enunciados de exercício, as lacunas, os gabaritos e os
textos de simulado (Cambridge Part 1/Part 2), as unidades 1–9 e 11 por
sobreposição com os livros 01, 02 e 04 do Sistema.

**Idioms:** entraram as 28 expressões cujo par idiom + significado sobreviveu
ao OCR. Duas do conjunto 5 se perderam (a lista da legenda das figuras veio
truncada) e **não foram inventadas**.

**Também atualizados:** o hub do S11 (card do livro 06 ativo; métricas 5 → 6
disponíveis, 4.500+ → 4.750+ exemplos) e a entrada 11 do `sistemas.json`.

## 0m. Atualização 2026-08-03 — Sistema 14 (Baseado em Livros V05) · CONCLUÍDO

> Fonte: **exclusivamente o arquivo `.md`**. Mesmo template visual do S15/S16/S17/S18.

| Livro | Arquivo `.md` | Painel | Blocos | Itens | Tamanho | Status |
|---|---|---|---|---|---|---|
| S14 · Livro 01 | `01_EfE Business English 1` | `livro01.html` | 34 | 601 | 135 KB | ✅ já existia |
| S14 · Livro 02 | `02_EfE Business English 2` | `livro02.html` | 32 | 443 | 122 KB | ✅ já existia |
| S14 · Livro 03 | `03_EfE Course Book Level 3` | `livro03.html` | 28 | 687 | 150 KB | ✅ já existia |
| S14 · Livro 04 | `04_EfE Practice Book Level 4` | `livro04.html` | 30 | 356 | 101 KB | ✅ já existia |
| S14 · Livro 05 | `05_Perfecting your english pronunciation` | `livro05.html` | 18 | 297 | 89 KB | ✅ já existia |
| S14 · Livro 06 | `06_4000 Essential English Words  Book 6.md` | `livro06.html` | 30 unidades | 600 | 205 KB | ✅ **2026-08-03** |

**O livro 06 é o último painel que faltava no Sistema 14.** As 600 palavras
(30 unidades × 20) entraram uma a uma com a **definição do próprio livro**
traduzida, a **frase de exemplo** original com a palavra-alvo destacada e a
tradução da frase. O `.md` é OCR e vinha com as frases sem espaço entre as
palavras (`Thecatbecamefranticwhen…`) — todas foram recompostas.

**Numeração das unidades:** os cabeçalhos `Word List` de 4 unidades se perderam
no OCR (a da unidade 13 saiu como `Ward List`); as quatro foram recuperadas pela
paginação. Cada unidade recebeu como título a **leitura que a fecha** no livro
(`The North Star`, `The Avalanche`, `The End of Smallpox`…), que é o contexto em
que aquelas 20 palavras aparecem juntas — a série não agrupa por tema.

**Descartado:** enunciados de exercício, gabaritos, as perguntas de *Reading
Comprehension*, a introdução metodológica de Paul Nation e o índice.

**Também atualizados:** o hub do S14 (card do livro 06 saiu de "Em breve" para
ativo; métricas do topo agora somam 6 livros, 2.984 itens, 172 blocos) e a
entrada 14 do `sistemas.json` (descrição e tag "Em breve" → "2.984 itens").

## 0l. Atualização 2026-08-03 — Sistema 16 (Baseado em Livros V07) · CONCLUÍDO

> Fonte: **exclusivamente os arquivos `.md`**. Mesmo template visual do S15/S17/S18/S19.

| Livro | Arquivo `.md` | Painel | Blocos | Itens | Tamanho | Status |
|---|---|---|---|---|---|---|
| S16 · Livro 01 | `02_English Vocabulary in Use. Elementary. 3rd Edition.md` | `livro01.html` | 58 unidades | 431 | 147 KB | ✅ já existia |
| S16 · Livro 02 | `01_Practice Makes Perfect Complete English All-in-One …` | `livro02.html` | 16 | 289 | 84 KB | ✅ **2026-08-02** |
| S16 · Livro 03 | `03_English Pronunciation in Use Elementary.md` | `livro03.html` | 15 | 173 | 56 KB | ✅ **2026-08-02** |
| S16 · Livro 04 | `04_Grammar - Grammar in Use Intermediate Student's.md` | `livro04.html` | 13 | 226 | 68 KB | ✅ **2026-08-02** |
| S16 · Livro 05 | `05_Practice Makes Perfect English Vocabulary for Beginning ESL …` | `livro05.html` | 19 | 407 | 143 KB | ✅ **2026-08-03** |
| S16 · Livro 06 | `06_Practise Makes Perfect_ English Verbs 3rd Edition.md` | `livro06.html` | 20 | 235 | 81 KB | ✅ **2026-08-03** |

**A numeração do painel não segue a numeração do `.md`:** o `livro01.html` (que já
existia) é o `02_English Vocabulary in Use Elementary`; o `livro02.html` é o
`01_PMP Complete English All-in-One`. Os demais coincidem.

**Descartado nos seis:** enunciados de exercício, gabaritos ("Answer Key"),
apêndices de verbos irregulares, prefácios e as caixas de método. No livro 05
(vocabulário) as listas de palavras entraram agrupadas por tema com tradução; no
livro 06 (verbos) entraram as frases-modelo de cada tempo-aspecto com o **motivo**
de escolher aquela forma, que é o diferencial do livro.

**Variante:** livros 01, 03 e 04 são Cambridge (in Use); livros 02, 05 e 06 são
McGraw-Hill (Practice Makes Perfect) — inglês **americano**.

## 0k. Atualização 2026-08-02 — Sistema 15 (Baseado em Livros V06) · CONCLUÍDO

> Fonte: **exclusivamente os arquivos `.md`**. Mesmo template visual do S17/S18/S19.

| Livro | Arquivo `.md` | Painel | Blocos | Itens | Tamanho | Status |
|---|---|---|---|---|---|---|
| S15 · Livro 01 | `01_English Grammar in Use Supplementary Exercises …` | `livro01.html` | 16 | 123 | 49 KB | ✅ já existia |
| S15 · Livro 02 | `02_Grammar - Grammar -Basic Grammar in Use …` | `livro02.html` | 23 | 490 | 119 KB | ✅ **2026-08-02** |
| S15 · Livro 03 | `03_English Collocations in Use Intermediate Book.md` | `livro03.html` | 18 | 425 | 114 KB | ✅ **2026-08-02** |
| S15 · Livro 04 | `04_Basic Grammar in Use Student's Book.md` | `livro04.html` | 16 | 338 | 86 KB | ✅ **2026-08-02** |
| S15 · Livro 05 | `05_English Phrasal Verbs in Use Intermediate …` | `livro05.html` | 16 | 266 | 74 KB | ✅ **2026-08-02** |
| S15 · Livro 06 | `06_Practice Makes Perfect English Conversation …` | `livro06.html` | 14 | 224 | 73 KB | ✅ **2026-08-02** |

**Nomes de arquivo enganosos — o painel segue o CONTEÚDO, não o nome:**

- `02_… Basic Grammar in Use … with Answers.md` → o conteúdo é **Essential Grammar in Use** (Murphy, Cambridge, 3ª ed., elementar).
- `04_Basic Grammar in Use Student's Book.md` → o conteúdo é **English Idioms in Use Intermediate** (McCarthy &amp; O'Dell, Cambridge, 2ª ed.).

**Descartado em todos os seis:** enunciados de exercício sem conteúdo, gabaritos
numerados (as seções "Answer key" no fim de cada livro), apêndices de ortografia,
rodapés de gráfica, e as caixas de método ("Over to you", "make a page in your
vocabulary notebook"). Nos dumps das séries *in Use* também foram recompostas as
ligaduras quebradas do OCR (`suff er` → `suffer`, `fi tness` → `fitness`).

**Variante:** livros 01–05 são inglês **britânico** (Cambridge); o livro 06 é
**americano** (McGraw-Hill) — a única fonte informal/coloquial do Sistema.

## 0i. Atualização 2026-08-02 — Sistema 13 (Baseado em Livros V04) · CONCLUÍDO

> Fonte: **exclusivamente os arquivos `.md`**. Mesmo template visual do S17/S18/S19.

| Livro | Arquivo `.md` | Painel | Blocos | Itens | Tamanho | Status |
|---|---|---|---|---|---|---|
| S13 · Livro 01 | *(anterior)* | `livro01.html` | 36 | 191 | 72 KB | ✅ já existia |
| S13 · Livro 02 | `02_English for Everyone English Vocabulary Builder …` | `livro02.html` | 14 | 150 | 58 KB | ✅ **2026-08-02** |
| S13 · Livro 03 | `03_English for Everyone Junior Beginner's Course.md` | `livro03.html` | 18 | 160 | 39 KB | ✅ **2026-08-02** |
| S13 · Livro 04 | `04_… Practice Book Level 1 Beginner …` | `livro04.html` | 12 | 166 | 38 KB | ✅ **2026-08-02** |
| S13 · Livro 05 | `05_… Practice Book Level 2 Beginner …` | `livro05.html` | 12 | 147 | 37 KB | ✅ **2026-08-02** |
| S13 · Livro 06 | `06_Pronouncing American English.md` | `livro06.html` | 7 | 90 | 33 KB | ✅ **2026-08-02** |

**O que foi extraído, por livro.** O *Vocabulary Builder* é um dicionário visual, mas traz em
14 unidades blocos de **Useful Expressions** com expressão + frase de exemplo + definição —
foi isso, e só isso, que virou painel (140 expressões, de aluguel a tecnologia). O *Junior*
rendeu as frases-modelo dos blocos `Listen and read`, as **12 canções** do curso e o
**Grammar guide** inteiro (cinco tabelas de conjugação, nove palavras interrogativas com
pergunta e resposta, plurais irregulares, pronomes, preposições). Nos dois *Practice Books*,
que são livros de exercício, o inglês real estava no **gabarito** e nos exemplos resolvidos —
frases completas e corretas; o nível 2 ainda traz tabelas `Review` em que os próprios autores
escolhem a frase-modelo de cada estrutura, e essas viraram a espinha dorsal do painel.
O *Pronouncing American English* rendeu os **pares mínimos em frase inteira**, as frases de
treino com os dois sons contrastantes, os pares substantivo × verbo em que só a tônica muda
o sentido, e 43 verbetes do apêndice de **100 homófonos**, cada um com a frase que o define.

**O que foi descartado.** Enunciado sem conteúdo (`Fill in the gaps`, `Number the pictures`,
`Mark the correct word`), respostas de marcar caixinha (`True / False`, letras soltas),
listas de vocabulário ilustrado sem frase (animais, roupas, cores, mobília), guia de
caligrafia, diagramas de boca e de escada de entonação (só imagem), instruções de manuseio
de fita e CD, texto de "como o curso funciona" e o lixo tipográfico do OCR.

**Sobreposição tratada.** O `livro01.html` (Grammar Guide) já cobria a gramática ilustrada
A1–B2 em 191 frases; por isso o livro 02 ficou só com expressões idiomáticas e colocações,
e os livros 04 e 05 priorizaram as estruturas que o Grammar Guide não detalha (negativas
contrastadas, perguntas de sujeito × objeto, pronomes indefinidos, as três formas de futuro).
O livro 03, por ser infantil, não repete nenhum: ele é o único do sistema que parte
literalmente do zero. O livro 06 não tem sobreposição com nenhum — é o único de pronúncia.

## 0h. Atualização 2026-08-02 — Sistema 12 (Baseado em Livros V03) · CONCLUÍDO

> Fonte: **exclusivamente os arquivos `.md`**, conforme a regra fixada em 2026-07-29.
> Nenhum PDF foi aberto. Template visual do S17/S18/S19 (fundo `#0a0a0a`, Space Grotesk /
> Inter, acento verde `#22C55E`, botão Voltar fixo, TOC lateral sticky, busca EN/PT com
> contador de itens).

| Livro | Arquivo `.md` | Painel | Seções | Itens | Tamanho | Status |
|---|---|---|---|---|---|---|
| S12 · Livro 01 | *(anterior)* | `livro01.html` | 16 | 174 | 51 KB | ✅ já existia |
| S12 · Livro 02 | `02_American English File 2 …` | `livro02.html` | 29 | 402 | 80 KB | ✅ **2026-08-02** |
| S12 · Livro 03 | `03_American English File 3 …` | `livro03.html` | 23 | 418 | 86 KB | ✅ **2026-08-02** |
| S12 · Livro 04 | `04_American English File 4 …` | `livro04.html` | 19 | 374 | 79 KB | ✅ **2026-08-02** |
| S12 · Livro 05 | `05_Close-up - 2nd - C1 Workbook.md` | `livro05.html` | 20 | 319 | 63 KB | ✅ **2026-08-02** |
| S12 · Livro 06 | `06_Close-up - 1st - C2 Workbook.md` | `livro06.html` | 22 | 342 | 70 KB | ✅ **2026-08-02** |

**O que foi extraído.** Nos três volumes do *American English File*, a fonte principal foi o
**Grammar Bank** (páginas de referência ao fim do livro): a frase-modelo de cada estrutura,
os pares que o próprio livro contrasta (`present perfect` × `simple past`, `used to` ×
`be used to`, first × second conditional) e as tabelas de formas. Somaram-se os diálogos
completos dos episódios de **Practical English** (hotel, restaurante, reagir a notícias,
pedir permissão) e as **Social English phrases**. Nos dois *Close-up*, a fonte foi a
**Grammar Reference** (estruturas C1/C2: inversão, cleft sentences, orações participiais,
condicionais invertidos, modais perfeitos, passiva impessoal), os apêndices de
**Collocations & Expressions** (90 no C1, 140 no C2) e de **Phrasal Verbs** (55 e 50, cada um
com a definição do próprio livro), mais a linguagem funcional da **Speaking Reference** (C1)
e da **Writing Reference** (C2).

**O que foi descartado.** Enunciado de exercício sem conteúdo (`Complete the sentences…`,
`Circle the correct form`), gabarito isolado, marcador de áudio (`1.30`, `Track 4.2`),
rodapé de gráfica e a URL comercial que o dump repete em quase toda página
(`www.avasshop.ir`), listas de vocabulário solto sem frase (nomes de peixes, legumes e
cores do *Vocabulary Bank*), seções de método (`Go online to review the grammar`),
e o lixo tipográfico do OCR — parênteses órfãos, colunas trocadas e caracteres quebrados
(`ü`, `ä` no lugar de vogais simples, `TU` por `I'll`).

**Sobreposição tratada.** O `livro01.html` (AEF 1) já cobria o básico A1–A2 com foco em
diálogos de situação; por isso os livros 02 a 04 priorizaram **estrutura gramatical** e os
diálogos de Practical English que o livro 01 não tem. Entre os dois *Close-up*, o C2 evitou
repetir o que o C1 já traz (inversão simples, cleft, modais perfeitos genéricos) e ficou
com o que só existe no C2: condicionais invertidos, `but for`, `would rather` com passado
irreal, `it's time we paid`, adjetivos graduáveis × não graduáveis, os dois sentidos de
`quite` e os adjetivos que mudam de significado conforme a posição.

## 0g. Atualização 2026-07-29 — Sistema 17 (Baseado em Livros V08)

> **Regra fixada para todo o projeto a partir desta data:** a extração de livros usa
> **exclusivamente o arquivo `.md`** como fonte. Os PDFs ficam na pasta apenas para
> arquivamento e **nunca** são abertos. Os `.md` **são** commitados no GitHub (são leves
> e servem como fonte oficial).

| Livro | Arquivo | Painel | Status | Data |
|---|---|---|---|---|
| S17 · Livro 01 | `01_American Accent Training.md` | `livro01.html` | ✅ **implementado** | 2026-07-29 |
| S17 · Livro 02 | `02_Mastering the American Accent (Lisa Mojsin) (z-lib.org).md` | `livro02.html` | 🔄 em andamento | — |
| S17 · Livro 03 | `03_English Vocabulary in Use Upper-Intermediate.md` | `livro03.html` | 🔄 em andamento | — |

### `livro01.html` — American Accent Training (Ann Cook, Barron's 2ª ed.)

**16 seções, ~1.400 itens de inglês real, 243 KB.** Fonte: MD de 208 páginas (dump OCR).

| Seção | Conteúdo |
|---|---|
| 1 · Entonação | substantivo × pronome (49 frases), 4 razões de tônica, inflexão (7 sentidos), "pretty", siglas, sílabas engolidas, parágrafo-modelo em 3 versões |
| 2 · Sílabas | padrões 1a–4f completos (~230 itens), teste de contagem |
| 3 · Duas palavras | descritiva × frase fixa (37 pares), quadro-resumo da tônica, nacionalidades, 90 compostos, 52 frases de teste, 5 histórias |
| 4 · Tempos verbais | *Dogs eat bones* × 25 tempos + *They eat them* × 25 + *floods erode* × 25, can/can't, subst.×verbo (33 pares), ~ate (17 pares) |
| 5 · Sons reduzidos | to, at, it, for, from, in, an, and, or, are, your, one, the, a, of, can, had, would, was, what, some — ~200 frases com a forma falada; "that"; tag endings (38 + 23 pronúncias) |
| 6 · Ligações | as 4 regras, TH composto, glides, T/D/S/Z+Y (~45), reduções coloquiais (36) |
| 7 · Cat/Caught/Cut | grade æ/ä/ə/ou/ei/ɛ (29×6), 6 leituras |
| 8 · T americano | as 5 regras com ~90 frases, combinações de Karina (18×3), vogal simples×dobrada |
| 9 · O L | L×T/D/N, L final com schwa, L mudo, grade de L final (11×8), Little Lola, Thirty Little Turtles |
| 10 · O R | os 7 R problemáticos, lista épsilon (42), grade de combinações (21×6), Mirror Store, método em 7 passos |
| 11 · TH | Throng of Thermometers, quadro sonora/surda, 3 trava-línguas |
| 12 · Vogais tensas/laxas | u×ʊ (20 pares), bit/bid/beat/bead, 26 frases de contraste, grades tensa (29×8) e laxa (31×5), lista do "I do meio" (~145), 5 leituras |
| 13 · V, S/Z, nasais, guturais | P/B/F/V/W, Vile VIP, S→Z, 2 leituras, "used to", nasais, letra X, 4 leituras |
| 14 · Emoção | 8 emoções, Really?/Maybe!, Who did it?, entonação não-verbal (14) |
| 15 · 3 e 4 palavras | descritiva/fixa modificada, 3-palavras, Three Little Pigs, Ignorance on Parade em 3 camadas |
| 16 · Textos longos | Caterpillar/UAW (3 versões), Russian Rebellion, US/Japan, debate presidencial, Texas millionaires (25), guia por idioma + seção Spanish adaptada ao falante de português |

**Descartado:** rodapés correntes (`American Accent Training` / `Chapter N`), números de página, marcadores `CD N Track NN` (~200), telefone e URL de tutoria comercial (800-457-4255, americanaccent.com — repetido 5×), instruções de manuseio do CD ("Pause the CD", "Back up the CD"), exercícios de linha em branco para o aluno preencher (1-12, 1-14, 1-40, 1-45, 11-8, 11-9), método/motivação ("Overdo It", "We All Do It", "A Child Can Learn Any Language"), desenhos de escada e diagramas de boca (só imagem), lixo tipográfico do OCR.

**⚠️ Ressalva de qualidade da fonte:** o MD do livro 01 é **OCR**, não extração de camada de texto.
A notação fonética própria da autora (colchetes com `ā`, `ä`, `ə`, `ĭ`) foi **corrompida** em vários
pontos (`[1e.1em]`, `[eq3.1]`, `[epeuem]`, `Z00` por *zoo*, `186` por *get*, `peda!` por *pedal*).
**Decisão:** a coluna "como soa" foi incluída **apenas** onde a transcrição sobreviveu legível;
onde virou lixo, foi **omitida** em vez de reconstruída por adivinhação — reconstruir daria
orientação de pronúncia errada num livro de sotaque. Cerca de 15% das transcrições fonéticas
do original ficaram de fora por esse motivo. O **inglês real** (frases, listas, histórias) está íntegro.

## 0e. Atualização 2026-07-24 — Sistema 03 fechado

> **Decisão sobre os PDFs-fonte do S03 e o segundo painel do Rachel's English.**
>
> ### Exclusões registradas (não geram painel)
>
> | Arquivo | Decisão | Motivo |
> |---|---|---|
> | `01_Forms of Reduced English.pdf` | ❌ **EXCLUÍDO** | Ensaio acadêmico de linguística sobre inglês *simplificado* (Basic English/Globish), não sobre redução da fala. Sem uso para o S03. Detalhe completo no bloco 0d. |
> | `02_Contractions.pdf` | ❌ **EXCLUÍDO** | Handout de 3 páginas (SJSU). Todo o seu conteúdo — a lista de contrações com a forma plena — já está coberto, e com muito mais profundidade, pelas seções 4–8 do `livro01.html` (contrações N'T, TO BE/TO HAVE, 'LL, 'D, modais). Redundante. |
>
> ### `03_American English Pronunciation` — agora com DOIS painéis (mesmo PDF, metades complementares)
>
> O livro tem 290 páginas em duas metades bem distintas. Cada uma virou um painel:
>
> | Painel | Metade do livro | Foco |
> |---|---|---|
> | `livro01.html` (feito antes) | cap. 5-T/D, 8–13 | **Fala ligada:** reduções, contrações, gonna/wanna/gotta, os 4 T, linking, diálogos |
> | `livro02.html` (**novo, 2026-07-24**) | cap. 3, 4, 5, 6, 7 | **Sistema de sons:** vogais, ditongos, consoantes, encontros, regras de plural/-ed, tônica em palavras longas |
>
> **Zero duplicação:** livro01 é *como as palavras se ligam e encolhem*; livro02 é *o inventário de sons e a tônica da palavra*. O único ponto de contato — as 4 pronúncias do T/D — fica no livro01; o livro02 só cita T/D como consoantes-plosivas e remete ao livro01. Ver bloco 0f.

## 0f. Atualização 2026-07-24 — `livro02.html` do S03 (Sistema de Sons)

> **`03_American English Pronunciation` (Rachel's English) — 2ª metade, capítulos 3–7.** Implementado em `livro02.html`: **6 seções, 183 itens de inglês**, mesma moldura visual do livro01 (dark, âmbar, busca própria, TOC, IPA do livro já normalizada).
>
> | Seção | Conteúdo | Itens |
> |---|---|---|
> | As 11 vogais | símbolo, nome, articulação, exemplos tônico/átono, grafias + 6 blocos de pares mínimos | 17 |
> | Os 6 ditongos | idem + 3 blocos de pares mínimos | 9 |
> | As 24 consoantes | por par voz/sem-voz, articulação, exemplos início/meio/fim, grafias + 4 notas ("derrubam o brasileiro") + 4 pares mínimos | 24 |
> | Encontros consonantais | 25 iniciais (2 sons) + 5 iniciais (3 sons) + 26 de meio/fim | 56 |
> | Plural -s/-es e passado -ed | regras [s]/[z]/[ɪz] e [t]/[d]/[ɪd] com exemplos | 6 |
> | Tônica das palavras longas | 3-sílabas (3 padrões), subst.×verbo, 7 heterônimos, regras de sufixo (3 grupos, 31 sufixos), compostos, siglas | 71 |
>
> **O que é NOVO (vs livro01):** todo o inventário de sons — vogais, ditongos, o quadro completo de consoantes, os encontros consonantais, as regras de plural/-ed e de tônica de palavra. Nada disso estava no livro01.
> **O que já estava coberto (e por isso ficou de fora daqui):** as 4 pronúncias do T, o Flap T no linking, e a diferença tônica/átona da *frase* — tudo no livro01, apenas referenciado por link. O destaque para o falante de português (encontros com S no início; o R que precisa ser segurado) foi mantido porque é a dor específica do público.

## 0d. Atualização 2026-07-24 — os 3 PDFs do S03 lidos · `01_Forms of Reduced English` DESCARTADO

> ### ❌ `01_Forms of Reduced English.pdf` — **arquivo mal rotulado para o S03. Não implementar.**
>
> **166 páginas, texto extraído integralmente e varrido.** Apesar do título, **não** é um livro sobre reduções do inglês falado. É um **ensaio acadêmico de linguística** — Massimo Laganà, *Forms of Reduced English*, Cambridge Scholars Publishing, 2023 — sobre **línguas construídas de inglês simplificado**: Basic English (Ogden), Globish (Nerrière), Basic Global English (Grzega), Plain English, Nuclear English, Special English.
>
> "Reduced" aqui significa **léxico e gramática reduzidos** (inglês controlado para comunicação internacional), **não** redução fonética da fala. Conteúdo: teoria semiótica, história da glotopolítica, o triângulo semiótico de Ogden, listas de vocabulário controlado, com longas citações em francês de Nerrière.
>
> **Contagem de termos no texto completo — a prova objetiva:**
>
> | Termo | Ocorrências |
> |---|---|
> | `gonna`, `wanna`, `gotta`, `kinda` | **0** |
> | `elision` | **0** |
> | contrações reais (`don't`, `isn't`…) | **0** |
> | `weak form` | 1 |
> | `connected speech` | 1 |
> | `contraction` | 3 |
>
> As duas únicas ocorrências que importariam **dizem o contrário do que o S03 ensina.** Na p. 137–138, ao descrever a fonologia do Basic Global English, o livro lista como *desejáveis*: "*the **absence of weak forms** (strong forms rather support intelligibility)*" e "*the **absence of assimilations in connected speech**.*" Ou seja: o livro defende **eliminar** exatamente aquilo que o Sistema 03 existe para ensinar a reconhecer.
>
> As 3 ocorrências de "contraction" são etimológicas/semânticas ("*till is a contraction of 'to the time that'*"; "de-contraction" como teoria do significado em Ogden) — nenhuma é contração da fala.
>
> **Veredito:** falha as REGRAS do S03 (§2 — os 5 tipos de redução) e o `REGRAS_GERAIS.md` §4 (é metateoria, não inglês em uso). Não gera painel. Mesmo caso do ~~*Short Stories in English for Beginners*~~ que era o tratado de Wyld (ver bloco 0).
>
> ### ✅ `03_American English Pronunciation (Rachel's English).pdf` — **IMPLEMENTADO** como `livro01.html`
>
> **290 páginas, lido integralmente.** É o livro que o `01_` prometia ser: Rachel Smith (Rachel's English, 2015). Contagem no texto completo: `stress` 695 · `contraction` 150 · `gonna` 73 · `flap` 72 · `linking` 71 · `gotta` 71 · `schwa` 67 · `wanna` 56.
>
> **Implementado em `livro01.html` (2026-07-24): 15 seções, 208 itens de inglês**, com a fonética (IPA) do próprio livro e busca própria (forma escrita + forma falada + fonética + exemplo). Extraído dos capítulos 5 (T e D), 8 (Linking), 9 (Stressed Words), 10 (Unstressed Words and Words that Reduce), 11 (Contractions), 12 (Gonna/Wanna/Gotta) e 13 (Putting it all Together):
>
> | Seção | Itens |
> |---|---|
> | Formas fracas (are, or, for, your, at, that, can, to, you, do, does, a, an, and, the, as, was, because, should, would, could) | 21 |
> | Sons que caem — H, THEM, OF | 9 |
> | Contrações N'T (+ can × can't) | 15 |
> | Contrações TO BE / TO HAVE | 34 |
> | Contrações 'LL (will) | 16 |
> | Contrações 'D (would/had/did) | 17 |
> | Modais + LET'S | 6 |
> | Gonna · Wanna · Gotta | 23 |
> | As 4 pronúncias do T (regras + pares Stop T + exceções) | 18 |
> | Linking (vogal→vogal, consoante→vogal, consoante→consoante) | 26 |
> | Reduções empilhadas | 7 |
> | Frases destrinchadas (Ben Franklin Exercises) | 11 |
> | Diálogos completos | 5 |
>
> **Exceção de regra aplicada:** neste Sistema as explicações de **como e quando** a redução ocorre são conteúdo, não bastidor — são o núcleo do aprendizado do S03. Fora ficaram os exercícios de áudio/vídeo (`engl.io/...`), os gabaritos e o método de estudo do capítulo 14.
>
> **Nota técnica:** o PDF tem um artefato de fonte que duplica o schwa (U+0259 seguido de U+04D9 cirílico) em todas as 747 ocorrências, além de usar epsilon/alfa gregos no lugar dos símbolos IPA. A extração normaliza os três casos — a fonética no painel está limpa.
>
> ### ⚠️ `02_Contractions.pdf` — genuíno, mas mínimo
>
> **3 páginas.** Handout do Writing Center da San José State University (Andrew Tucker, 2011/rev. 2014). É conteúdo S03 legítimo — lista de contrações (`aren't`, `can't`, `they'd`, `we're`…) com a forma plena ao lado — mas é uma folha de referência, não um livro. O painel `reducoes.html` do S03 já cobre esse terreno. Serve como **complemento/conferência**, não como livro próprio.

## 0c. Atualização 2026-07-24 — estrutura completa: 22 Sistemas

> Varredura de toda a raiz. `sistemas.json` reescrito com **22 entradas**; criados os `index.html` que faltavam (S17, S18, S19, S20, S21); hubs de S11–S16 corrigidos para bater com os PDFs reais; pasta `Sistema 17 — Kids` renumerada para `Sistema 22 — Kids`.
>
> **Legenda de status:** ✅ implementado · ⏳ aguardando (PDF na pasta, painel não feito) · ❌ descartado.

### Estrutura oficial dos 22 Sistemas

| # | Sistema | PDFs | Painéis prontos | Status |
|---|---|---|---|---|
| 01 | Base. Fluência. Gramática | — (centenas de PDFs de referência) | `index.html` + jornada | ✅ |
| 02 | Dúvidas Pontuais | — | `index.html` + 2 sub-painéis | ✅ |
| 03 | Reduções do Inglês Real | 3 | `index.html` + 3 sub-painéis + `livro01` | ✅ 1/3 · ⏳ 1 · ❌ 1 |
| 04 | Motor de Verbos | — | `index.html` + 4 sub-painéis | ✅ |
| 05 | Conectar Frases | — | `index.html` + 4 sub-painéis | ✅ |
| 06 | Situar a Frase | — | `index.html` + 5 sub-painéis | ✅ |
| 07 | Baseado em Desenho Infantil | — | `index.html` | ✅ |
| 08 | Transcrições e Canais | — | `index.html` + 16 canais | ✅ |
| 09 | Prática Completa · 4 Pilares | — | `index.html` + 4 pilares | ✅ |
| 10 | Livros V01 — Conversação | 6 | `index.html` + `livro01–06` | ✅ 6/6 |
| 11 | Livros V02 — Gramática em Uso | 6 | `index.html` + `livro01–02` | ✅ 2/6 · ⏳ 4 |
| 12 | Livros V03 — American English File | 6 | `index.html` + `livro01` | ✅ 1/6 · ⏳ 5 |
| 13 | Livros V04 — English for Everyone | 6 | `index.html` + `livro01` | ✅ 1/6 · ⏳ 5 |
| 14 | Livros V05 — Business & Vocabulário | 6 | `index.html` | ⏳ 6 |
| 15 | Livros V06 — Exercícios & Vocabulário | 6 | `index.html` + `livro01–06` | ✅ 6/6 |
| 16 | Livros V07 — In Use & PMP | 6 | `index.html` + `livro01–06` | ✅ 6/6 |
| 17 | Livros V08 — Sotaque & Vocabulário | 3 | `index.html` **(criado 07-24)** | ⏳ 3 |
| 18 | Livros V09 — Cambridge B2 First | 5 | `index.html` **(criado 07-24)** | ⏳ 5 |
| 19 | Livros V10 — Gramática Avançada | 7 | `index.html` **(criado 07-24)** | ⏳ 7 |
| 20 | Livros V11 — Gramática Avançada | 5 | `index.html` **(criado 07-24)** | ⏳ 5 |
| 21 | Livros V12 — Gramática Avançada | 3 | `index.html` **(criado 07-24)** | ⏳ 3 |
| 22 | Livros — Kids | 2 | `index.html` + `livro01` | ✅ 1/2 · ⏳ 1 |

### Livros novos / movidos — registro por Sistema

**S03 · Reduções do Inglês Real** — três PDFs novos na pasta (o painel do S03 já existe e foi feito antes deles):

| Arquivo | Status |
|---|---|
| `01_Forms of Reduced English.pdf` | ❌ **descartado** — lido em 2026-07-24, é ensaio acadêmico sobre inglês simplificado (Basic English/Globish), não sobre reduções da fala. Ver bloco 0d |
| `02_Contractions.pdf` | ⏳ aguardando — 3 páginas, handout de contrações; complemento, não livro |
| `03_American English Pronunciation Rachels.pdf` | ✅ **implementado** (`livro01.html`) — 15 seções, 208 itens com fonética. Ver bloco 0d |

**S11 · V02** — hub tinha 5 cards e listava *Objective Proficiency*, que já não está aqui:

| Arquivo | Status |
|---|---|
| `01_English Grammar in Use…` | ✅ `livro01.html` — 145 unidades, 2.800 exemplos |
| `02_Grammar Practice for Intermediate Students` | ✅ `livro02.html` — 87 pontos, 400 frases |
| `03_Oxford-Guide-to-English-Grammar` | ⏳ aguardando |
| `04_Essential Grammar in Use…` | ⏳ aguardando |
| `05_English Pronunciation Made Simple` | ⏳ aguardando — **card do hub estava errado** (dizia "Objective Proficiency"), corrigido |
| `06_Reactivate Your Grammar And Vocabulary C1C2 - Exams` | ⏳ **novo** — card adicionado ao hub |
| ~~Objective Proficiency~~ | ➡️ **movido para o S19** |

**S12 · V03** — dois workbooks novos:

| Arquivo | Status |
|---|---|
| `01_American English File 1` | ✅ `livro01.html` — 16 seções, 174 frases |
| `02–04_American English File 2, 3, 4` | ⏳ aguardando |
| `05_Close-up - 2nd - C1 Workbook` | ⏳ **novo** — card adicionado |
| `06_Close-up - 1st - C2 Workbook` | ⏳ **novo** — card adicionado |

**S13 · V04**:

| Arquivo | Status |
|---|---|
| `01_English for Everyone Grammar Guide` | ✅ `livro01.html` — 36 temas, 191 frases |
| `02–05_EfE Vocabulary Builder, Junior, Practice 1 e 2` | ⏳ aguardando |
| `06_Pronouncing American English` | ⏳ **novo** — card adicionado |

**S14 · V05** — dois livros novos, nenhum painel ainda:

| Arquivo | Status |
|---|---|
| `01–04_EfE Business 1, Business 2, Course 3, Practice 4` | ⏳ aguardando |
| `05_Perfecting your english pronunciation (Susan Cameron)` | ⏳ **novo** — card adicionado |
| `06_4000 Essential English Words Book 6` | ⏳ **novo** — card adicionado |

**S15 · V06** — o card 06 apontava para um livro que não está na pasta:

| Arquivo | Status |
|---|---|
| `01_English Grammar in Use Supplementary Exercises` | ✅ `livro01.html` — 16 estruturas, 123 frases |
| `02–05_Basic Grammar in Use (×2), Collocations in Use, Phrasal Verbs in Use` | ⏳ aguardando |
| `06_Practice Makes Perfect English Conversation` | ⏳ aguardando — **card do hub estava errado** (dizia "Short Stories for Beginners"), corrigido |
| ~~Short Stories in English for Beginners~~ | ❌ **descartado** — nunca esteve nesta pasta; o arquivo com esse nome (no S10 antigo) era o tratado de Wyld, ver bloco 0 |

**S16 · V07** — três cards apontavam para livros que foram para o S19:

| Arquivo | Status |
|---|---|
| `01_PMP Complete English All-in-One for ESL Learners` | ⏳ **novo** — card adicionado |
| `02_English Vocabulary in Use Elementary 3rd` | ✅ `livro01.html` — 58 unidades, 431 itens *(o arquivo do painel continua `livro01.html`; no hub ele é o card "Livro 02", que é a posição real do PDF)* |
| `03_English Pronunciation in Use Elementary` | ⏳ aguardando |
| `04_Grammar in Use Intermediate` | ⏳ aguardando |
| `05_PMP English Vocabulary for Beginning ESL Learners` | ⏳ **novo** — card adicionado |
| `06_PMP English Verbs 3rd Edition` | ⏳ **novo** — card adicionado |
| ~~Pronunciation in Use Advanced · Advanced Grammar in Use · EVU Advanced~~ | ➡️ **movidos para o S19** |

**S17 · V08** — Sistema novo no JSON, hub criado:

| Arquivo | Status |
|---|---|
| `01_American Accent Training` | ⏳ aguardando |
| `02_Mastering the American Accent (Lisa Mojsin)` | ⏳ aguardando |
| `03_English Vocabulary in Use Upper-Intermediate` | ⏳ aguardando |

**S18 · V09** — Sistema novo no JSON, hub criado. `01`–`05` = B2 First 1 a 5 (o 04 é a versão *for Schools*): todos **⏳ aguardando**.

**S19 · V10 — Gramática Avançada** — destino dos livros C1/C2 que estavam espalhados. Regras próprias em `REGRAS_AVANCADO.md`:

| Arquivo | Origem | Status |
|---|---|---|
| `01_Objective Proficiency` | ➡️ veio do **S11** | ⏳ aguardando |
| `02_Advanced Grammar in Use` | ➡️ veio do **S16** | ⏳ aguardando |
| `03_Grammar and Vocabulary for Advanced` | — | ⏳ aguardando |
| `04_Advanced Language Practice (Michael Vince)` | — | ⏳ aguardando |
| `05_Complete Advanced Student's Book` | — | ⏳ aguardando |
| `06_English Vocabulary in Use Advanced 3rd` | ➡️ veio do **S16** | ⏳ aguardando |
| `07_English Pronunciation in Use Advanced` | ➡️ veio do **S16** | ⏳ aguardando |

**S20 · V11 — Gramática Avançada** — hub criado; todos **⏳ aguardando**. ⚠️ Só o primeiro PDF tem prefixo numérico:

| Arquivo | Status |
|---|---|
| `01_Oxford English Grammar Course Advanced with Key` | ⏳ aguardando |
| `English Vocabulary in Use Advanced 100 units…` | ⏳ aguardando — **sem prefixo `02_`** |
| `English Vocabulary in Use Upper-intermediate With answers` | ⏳ aguardando — **sem prefixo `03_`** |
| `Grammar and Vocabulary for Cambridge Advanced and Proficiency` | ⏳ aguardando — **sem prefixo `04_`** |
| `New English File - Advanced Level. Student's Book` | ⏳ aguardando — **sem prefixo `05_`** |

**S21 · V12 — Gramática Avançada** — hub criado; todos **⏳ aguardando**. ⚠️ Nenhum PDF tem prefixo numérico:

| Arquivo | Status |
|---|---|
| `Advancing Vocabulary Skills - Sherrie L. Nist` | ⏳ aguardando — **sem prefixo `01_`** |
| `English Advancing A Bridge to Success` | ⏳ aguardando — **sem prefixo `02_`** |
| `New Cambridge Advanced English Student's book` | ⏳ aguardando — **sem prefixo `03_`** |

**S22 · Kids** — era `Sistema 17 — Baseado em Livros — Kids`; pasta renumerada para 22 e as referências internas (`<title>`, eyebrow, footer, chave de scroll) corrigidas de "Sistema 17" para "Sistema 22":

| Arquivo | Status |
|---|---|
| `01_Kid's Box New Generation Level 3` | ✅ `livro01.html` — 11 seções, 242 frases |
| `02_Kid's Box American English 4` | ⏳ aguardando |

### Pendências abertas depois desta varredura

- **Renomear com prefixo numérico** os 4 PDFs do S20 e os 3 do S21 (ordem oficial = ordem dos cards no hub).
- **S14** é o único Sistema de livros sem nenhum painel implementado (6 PDFs parados).
- **S03:** o Rachel's English já está implementado (`livro01.html`). Sobra o `02_Contractions` (3 páginas) — pequeno e em boa parte já coberto pelo `livro01` e pelo `reducoes.html`.


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
> | `LIVRO_06_Como não aprender Inglês (Michael Jacobs)` | Livro de usos/erros — cheio de inglês real | ✅ **Implementado** (`livro06.html`) |
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
>
> **LIVRO_06 (Como não aprender inglês, Michael A. Jacobs) — 285 pág., lido integralmente (T3):** ao contrário dos outros, **NÃO é livro de método** — é um livro de **usos e erros** do brasileiro no inglês, riquíssimo em inglês real (falsos cognatos, pares que confundem, preposições, gramática, cultura). Estimativa: **~80% inglês real** (embutido em explicações em pt) vs. **~20% ensaios "Attitude"/método/anedotas**. Extraído para `livro06.html`:
> - **128 tópicos** em 8 capítulos (Vocabulário, Gramática, Português em Inglês, Curiosidades, Linguagem de rua, Ortografia e Pronúncia, Cultura) com **436 frases de exemplo** reais em inglês + tradução, garimpadas por seção.
> - Falsos cognatos/pares: remember×remind, lose×miss, lend×borrow, sensitive×sensible, travel×trip, win×beat, history×story, say/speak/talk/tell, etc.
> - **Descartado (§4):** as ~29 seções "Attitude" (ensaios/motivação) e os textos de método. Fonte é PDF digitalizado (OCR) — pode haver pequenos ruídos residuais.

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

**Fila vazia — nada pendente de triagem.**

Um lote já processado fica arquivado em `_processado_2026-07-26/` (188 capturas de
Instagram, `IMG_6520`–`IMG_6714`). Todo o conteúdo dele virou **6 painéis novos,
938 itens** — `gramatica-em-tabelas` (S01, 192), `falar-melhor` (S02, 168),
`livro-x-rua` (S03, 118), `familias-de-verbos` (S04, 211), `even-so-conectores`
(S05, 76) e `preposicoes-mapas` (S06, 173). Ver o `README.md` da pasta do lote,
inclusive o motivo de o lote ter sido arquivado inteiro em vez de dividido pelos
`_fontes/` de cada Sistema.

---

## 2026-08-06 — Redistribuição por nível real de conteúdo

Varredura completa dos 133 MDs de conteúdo das 25 pastas, classificados por
nível CEFR real (kids/A1/A2/B1/B2/C1-C2) a partir do conteúdo, não da pasta.
Relatório completo em `tmp/relatorio_redistribuicao.txt`.

**Regra aplicada:** o prefixo `NN_` é posicional — casa com `livroNN.html` da
mesma pasta. Por isso cada movimento levou **o par MD + painel junto**, com
renumeração no destino e fechamento da lacuna na origem. Nenhum painel ficou órfão.

| Livro | De | Para | Motivo |
|---|---|---|---|
| `Grammar For Young Learners` | S04 · Livro 05 | **S01 · Livro 03** | Oxford, ensinar gramática a crianças → KIDS |
| `EfE Junior Beginner's Course` | S09 · Livro 03 | **S01 · Livro 04** | curso infantil (Primary ELT) → KIDS |
| `Pronouncing American English` | S09 · Livro 06 | **S21 · Livro 04** | fonética sistemática → B1 |
| `English Grammar: A Resource Book for Students` | S04 · Livro 04 | **S24 · Livro 04** | linguística universitária → C1/C2 |
| `Close-up 2nd C1 Workbook` | S11 · Livro 05 | **S23 · Livro 05** | série Cengage C1, estranha à coleção AEF |
| `Close-up 1st C2 Workbook` | S11 · Livro 06 | **S23 · Livro 06** | série Cengage C2, estranha à coleção AEF |
| `Reactivate Your Grammar and Vocabulary C1C2` | S13 · Livro 06 | **S22 · Livro 08** | o próprio título declara C1/C2 |
| `Perfecting your English Pronunciation` | S19 · Livro 05 | **S22 · Livro 09** | domínio fonético C1 |
| `4000 Essential English Words Book 6` | S19 · Livro 06 | **S25 · Livro 04** | vocabulário acadêmico C1 |
| `English Vocabulary in Use Upper-intermediate` | S23 · Livro 03 | **S18 · Livro 04** | B2 (S18 já hospeda o mesmo título) |

**Renumeração para fechar lacunas na origem:**
S04 06→04, 07→05 · S09 04→03, 05→04 · S23 04→03, 05→04

**Também nesta passagem:** S21 reclassificado de C1/C2 para **B1** — seus livros
são A2/B1 (`Speak English: 30 Days`, `Pronunciation in Use Intermediate`,
`Everyday Conversations`), não avançados.

> ⚠️ As tabelas das seções anteriores usam a numeração de sistema **anterior**
> à reorganização A1→C2 (commit c2f7e15) e são mantidas como registro histórico.
